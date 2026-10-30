#!/usr/bin/env python3
"""Apply suggested edits to a .docx letter as Word tracked changes.

Usage:
  python3 polish_docx.py LETTER.docx EDITS.json OUT.docx

Inserted text is a tracked insertion highlighted yellow; removed text is a
tracked deletion; every edit carries a Word comment with its reason. The
author opens OUT.docx in Word and accepts, rejects or rewrites each change.

EDITS.json is a list of objects, applied in order:

  {"op": "replace", "old": "exact text", "new": "new text", "reason": "..."}
      "old" must occur exactly once in the document, inside one paragraph.
      "new" may be "" to delete.
  {"op": "insert", "after": "exact text", "text": "...", "reason": "..."}
      Inserts text right after "after" (unique, inside one paragraph), deleting nothing.
  {"op": "insert_after", "anchor": "text in a paragraph", "text": "...", "reason": "..."}
      Adds a new paragraph after the paragraph containing "anchor".
  {"op": "delete_paragraph", "anchor": "text in a paragraph", "reason": "..."}

Stdlib only. Formatting of untouched text is preserved.
"""
import datetime
import html
import json
import re
import sys
import zipfile

AUTHOR = "gtv-lor suggestion"
DATE = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
COMMENTS_CT = "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml"
COMMENTS_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/comments"

PARA_RE = re.compile(r"<w:p[ >].*?</w:p>", re.S)
RUN_RE = re.compile(r"<w:r[ >].*?</w:r>", re.S)
RPR_RE = re.compile(r"<w:rPr>.*?</w:rPr>", re.S)
T_RE = re.compile(r"<w:t(?: [^>]*)?>(.*?)</w:t>|<w:t(?: [^>]*)?/>", re.S)
# rPr children that must come after w:highlight (ECMA-376 order)
AFTER_HIGHLIGHT = ("u", "effect", "bdr", "shd", "fitText", "vertAlign", "rtl", "cs", "em",
                   "lang", "eastAsianLayout", "specVanish", "oMath")


class EditError(Exception):
    pass


class Ids:
    def __init__(self, start: int):
        self.n = start

    def next(self) -> int:
        self.n += 1
        return self.n


def esc(text: str) -> str:
    return html.escape(text, quote=False)


def run_text(run: str) -> str | None:
    """Text of a simple run, or None if the run holds anything but rPr + one w:t."""
    body = RPR_RE.sub("", run, count=1)
    body = re.sub(r"^<w:r[^>]*>|</w:r>$", "", body)
    parts = T_RE.findall(body)
    if len(parts) != 1 or T_RE.sub("", body).strip():
        return None
    return html.unescape(parts[0])


def visible_text(run: str) -> str:
    return "".join(html.unescape(t) for t in T_RE.findall(run))


def run_open(run: str) -> str:
    return re.match(r"<w:r[^>]*>", run).group(0)


def rpr_of(run: str) -> str:
    m = RPR_RE.search(run)
    return m.group(0) if m else ""


def highlighted(rpr: str) -> str:
    inner = rpr[len("<w:rPr>"):-len("</w:rPr>")] if rpr else ""
    inner = re.sub(r"<w:highlight [^>]*/>", "", inner)
    hl = '<w:highlight w:val="yellow"/>'
    for tag in AFTER_HIGHLIGHT:
        m = re.search(rf"<w:{tag}[ />]", inner)
        if m:
            return f"<w:rPr>{inner[:m.start()]}{hl}{inner[m.start():]}</w:rPr>"
    return f"<w:rPr>{inner}{hl}</w:rPr>"


def make_run(open_tag: str, rpr: str, text: str, deleted: bool = False) -> str:
    tag = "w:delText" if deleted else "w:t"
    return f'{open_tag}{rpr}<{tag} xml:space="preserve">{esc(text)}</{tag}></w:r>'


def to_deleted(run: str) -> str:
    run = re.sub(r"<w:t(\s|>|/)", r"<w:delText\1", run)
    run = run.replace("</w:t>", "</w:delText>")
    return run.replace("<w:instrText", "<w:delInstrText").replace("</w:instrText>", "</w:delInstrText>")


def comment_parts(cid: int) -> tuple[str, str]:
    start = f'<w:commentRangeStart w:id="{cid}"/>'
    end = (f'<w:commentRangeEnd w:id="{cid}"/>'
           f'<w:r><w:rPr><w:rStyle w:val="CommentReference"/></w:rPr><w:commentReference w:id="{cid}"/></w:r>')
    return start, end


def replace_in_paragraph(para: str, old: str, new: str, ids: Ids, cid: int, keep_old: bool = False) -> str:
    runs = [(m.start(), m.end(), m.group(0)) for m in RUN_RE.finditer(para)]
    texts = [visible_text(r[2]) for r in runs]
    full = "".join(texts)
    start = full.index(old)
    end = start + len(old)

    pos = 0
    first_rpr, first_open, placed_start, last_touched = None, None, False, None
    end_rpr, end_open = None, None
    pieces = []  # (run_index, replacement_xml)
    for i, (rs, re_, run) in enumerate(runs):
        t = texts[i]
        a, b = pos, pos + len(t)
        pos = b
        if b <= start or a >= end or not t:
            if not t and start < a < end:
                pieces.append((i, f'<w:del w:id="{ids.next()}" w:author="{AUTHOR}" w:date="{DATE}">{to_deleted(run)}</w:del>'))
            continue
        simple = run_text(run)
        lo, hi = max(start, a) - a, min(end, b) - a
        if simple is None and (lo > 0 or hi < len(t)):
            raise EditError(f"match splits a complex run; widen or narrow the match: {old[:50]!r}")
        open_tag, rpr = run_open(run), rpr_of(run)
        if first_rpr is None:
            first_rpr, first_open = rpr, open_tag
        end_rpr, end_open = rpr, open_tag
        xml = ""
        if lo > 0:
            xml += make_run(open_tag, rpr, t[:lo])
        if not placed_start:
            xml += comment_parts(cid)[0]
            placed_start = True
        if hi > lo and keep_old:
            xml += make_run(open_tag, rpr, t[lo:hi]) if simple is not None else run
        elif hi > lo:
            deleted = make_run(open_tag, rpr, t[lo:hi], deleted=True) if simple is not None else to_deleted(run)
            xml += f'<w:del w:id="{ids.next()}" w:author="{AUTHOR}" w:date="{DATE}">{deleted}</w:del>'
        last_touched = i
        tail = make_run(open_tag, rpr, t[hi:]) if hi < len(t) else ""
        pieces.append((i, xml + ("{INS}" if end <= b else "") + tail))

    if first_rpr is None:
        raise EditError(f"could not locate runs for: {old[:50]!r}")
    ins = ""
    if new:
        ins = (f'<w:ins w:id="{ids.next()}" w:author="{AUTHOR}" w:date="{DATE}">'
               f'{make_run(end_open if keep_old else first_open, highlighted(end_rpr if keep_old else first_rpr), new)}</w:ins>')
    ins += comment_parts(cid)[1]
    replaced = dict(pieces)
    if "{INS}" not in "".join(replaced.values()):
        replaced[last_touched] = replaced[last_touched] + "{INS}"
    for i in sorted(replaced, reverse=True):
        rs, re_, _ = runs[i]
        para = para[:rs] + replaced[i].replace("{INS}", ins) + para[re_:]
    return para


def mark_para_inserted(ppr: str, ids: Ids) -> str:
    mark = f'<w:ins w:id="{ids.next()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
    if not ppr:
        return f"<w:pPr><w:rPr>{mark}</w:rPr></w:pPr>"
    if "<w:rPr>" in ppr:
        return ppr.replace("<w:rPr>", f"<w:rPr>{mark}", 1)
    return ppr.replace("</w:pPr>", f"<w:rPr>{mark}</w:rPr></w:pPr>")


def mark_para_deleted(ppr: str, ids: Ids) -> str:
    mark = f'<w:del w:id="{ids.next()}" w:author="{AUTHOR}" w:date="{DATE}"/>'
    if not ppr:
        return f"<w:pPr><w:rPr>{mark}</w:rPr></w:pPr>"
    if "<w:rPr>" in ppr:
        return ppr.replace("</w:rPr></w:pPr>", f"{mark}</w:rPr></w:pPr>", 1)
    return ppr.replace("</w:pPr>", f"<w:rPr>{mark}</w:rPr></w:pPr>")


def ppr_of(para: str) -> str:
    m = re.search(r"<w:pPr>.*?</w:pPr>", para, re.S)
    return m.group(0) if m else ""


def find_para(doc: str, needle: str) -> re.Match:
    hits = [m for m in PARA_RE.finditer(doc)
            if needle in "".join(visible_text(r) for r in RUN_RE.findall(m.group(0)))]
    if len(hits) != 1:
        raise EditError(f"{len(hits)} paragraphs contain {needle[:50]!r}; need exactly 1")
    return hits[0]


def apply(doc: str, edit: dict, ids: Ids, cid: int) -> str:
    op = edit["op"]
    if op == "replace":
        m = find_para(doc, edit["old"])
        para = replace_in_paragraph(m.group(0), edit["old"], edit.get("new", ""), ids, cid)
        return doc[:m.start()] + para + doc[m.end():]
    if op == "insert":
        m = find_para(doc, edit["after"])
        para = replace_in_paragraph(m.group(0), edit["after"], edit["text"], ids, cid, keep_old=True)
        return doc[:m.start()] + para + doc[m.end():]
    if op == "insert_after":
        m = find_para(doc, edit["anchor"])
        anchor = m.group(0)
        first_run = RUN_RE.search(anchor)
        rpr = rpr_of(first_run.group(0)) if first_run else ""
        rpr = re.sub(r"<w:b/>|<w:bCs/>", "", rpr)
        start, end = comment_parts(cid)
        ins = (f'<w:ins w:id="{ids.next()}" w:author="{AUTHOR}" w:date="{DATE}">'
               f'{make_run("<w:r>", highlighted(rpr), edit["text"])}</w:ins>')
        new_para = f"<w:p>{mark_para_inserted(ppr_of(anchor), ids)}{start}{ins}{end}</w:p>"
        return doc[:m.end()] + new_para + doc[m.end():]
    if op == "delete_paragraph":
        m = find_para(doc, edit["anchor"])
        para = m.group(0)
        ppr = ppr_of(para)
        body = para[para.index(ppr) + len(ppr):] if ppr else re.sub(r"^<w:p[^>]*>", "", para)
        body = body[:-len("</w:p>")]
        body = RUN_RE.sub(lambda r: f'<w:del w:id="{ids.next()}" w:author="{AUTHOR}" w:date="{DATE}">{to_deleted(r.group(0))}</w:del>', body)
        start, end = comment_parts(cid)
        open_tag = re.match(r"<w:p[^>]*>", para).group(0)
        new_para = f"{open_tag}{mark_para_deleted(ppr, ids)}{start}{body}{end}</w:p>"
        return doc[:m.start()] + new_para + doc[m.end():]
    raise EditError(f"unknown op {op!r}")


def comments_xml(existing: str | None, comments: list) -> str:
    items = "".join(
        f'<w:comment w:id="{cid}" w:author="{AUTHOR}" w:date="{DATE}" w:initials="GL">'
        f'<w:p><w:r><w:t xml:space="preserve">{esc(reason)}</w:t></w:r></w:p></w:comment>'
        for cid, reason in comments)
    if existing:
        return existing.replace("</w:comments>", items + "</w:comments>")
    return (f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            f'<w:comments xmlns:w="{W_NS}">{items}</w:comments>')


def main(argv: list[str]) -> None:
    if len(argv) != 3:
        sys.exit(__doc__)
    src, edits_path, out = argv
    edits = json.load(open(edits_path, encoding="utf8"))
    zin = zipfile.ZipFile(src)
    files = {n: zin.read(n) for n in zin.namelist()}
    doc = files["word/document.xml"].decode("utf8")
    existing = files.get("word/comments.xml", b"").decode("utf8") or None
    used = [int(x) for x in re.findall(r'w:id="(\d+)"', doc + (existing or ""))]
    ids = Ids(max(used, default=0) + 100)
    comments, failed = [], []
    for e in edits:
        cid = ids.next()
        try:
            doc = apply(doc, e, ids, cid)
            comments.append((cid, e.get("reason", "")))
        except (EditError, KeyError, ValueError) as err:
            failed.append({"edit": e, "error": str(err)})
    files["word/document.xml"] = doc.encode("utf8")
    files["word/comments.xml"] = comments_xml(existing, comments).encode("utf8")
    if existing is None:
        ct = files["[Content_Types].xml"].decode("utf8")
        ct = ct.replace("</Types>", f'<Override PartName="/word/comments.xml" ContentType="{COMMENTS_CT}"/></Types>')
        files["[Content_Types].xml"] = ct.encode("utf8")
        rels = files["word/_rels/document.xml.rels"].decode("utf8")
        rels = rels.replace("</Relationships>",
                            f'<Relationship Id="rIdGtvComments" Type="{COMMENTS_REL}" Target="comments.xml"/></Relationships>')
        files["word/_rels/document.xml.rels"] = rels.encode("utf8")
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for name, data in files.items():
            zout.writestr(name, data)
    print(json.dumps({"applied": len(edits) - len(failed), "failed": failed, "out": out}, indent=2))


if __name__ == "__main__":
    main(sys.argv[1:])
