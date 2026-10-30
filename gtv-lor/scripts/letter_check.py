#!/usr/bin/env python3
"""Mechanical checks for Global Talent recommendation letters.

Usage:
  python3 letter_check.py LETTER [LETTER ...] [--draft DRAFT]

LETTER and DRAFT may be .txt, .md, .docx or .pdf (.pdf needs pdftotext).
Pass all 3 letters together to check them against each other. Pass the
applicant's brief or starting draft with --draft to measure how much of it
was copied.

Prints JSON. Stdlib only.
"""
import json
import re
import subprocess
import sys
import zipfile
from pathlib import Path

# Words per A4 side at 11 to 12pt with normal margins. Conservative.
WORDS_PER_SIDE = 500
MAX_SIDES = 3

DATE_RE = re.compile(
    r"\b(\d{1,2}(st|nd|rd|th)?\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?,?\s+\d{4}"
    r"|(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\.?\s+\d{1,2}(st|nd|rd|th)?,?\s+\d{4}"
    r"|\d{4}-\d{2}-\d{2}|\d{1,2}[/.]\d{1,2}[/.]\d{2,4})\b",
    re.I,
)
EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE_RE = re.compile(r"(\+?\d[\d\s().-]{7,}\d)")
PLACEHOLDER_RE = re.compile(r"\[[^\]]{1,40}\]|\{[^}]{1,40}\}|<[^>]{1,40}>|\bX{3,}\b|\bTBD\b|\bTODO\b")
GTV_RE = re.compile(r"global talent|tech nation|endorse", re.I)
UK_RE = re.compile(r"\b(UK|United Kingdom|Britain|British|London|Manchester|Edinburgh|Cambridge|Oxford|Bristol)\b")
YEARS_RE = re.compile(r"\b(since|in|from)\s+(19|20)\d{2}\b|\b\d+\s+(years|months)\b", re.I)
STOCK_PHRASES = [
    "i am writing to wholeheartedly", "wholeheartedly recommend", "testament to",
    "unwavering", "rapidly evolving", "ever-evolving", "in today's", "delve",
    "tapestry", "invaluable asset", "it is with great pleasure", "without hesitation",
    "game-changer", "cutting-edge", "spearheaded", "pivotal role", "visionary",
    "exceptional talent and dedication", "i have no doubt", "a true leader",
]


def read_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml").decode("utf8", "ignore")
        xml = re.sub(r"<w:del\b[^/]*?>.*?</w:del>", "", xml, flags=re.S)  # read with tracked changes accepted
        xml = re.sub(r"</w:p>", "\n", xml)
        return re.sub(r"<[^>]+>", "", xml)
    if suffix == ".pdf":
        out = subprocess.run(["pdftotext", "-layout", str(path), "-"], capture_output=True, text=True)
        if out.returncode != 0:
            sys.exit(f"pdftotext failed on {path}: {out.stderr.strip()}")
        return out.stdout
    return path.read_text(encoding="utf8", errors="ignore")


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9']+", text.lower())


def shingles(text: str, n: int = 8) -> set[tuple[str, ...]]:
    w = words(text)
    return {tuple(w[i:i + n]) for i in range(len(w) - n + 1)}


def overlap(a: str, b: str) -> dict:
    sa, sb = shingles(a), shingles(b)
    if not sa or not sb:
        return {"share_of_first": 0.0, "examples": []}
    common = sa & sb
    examples = [" ".join(s) for s in list(common)[:5]]
    return {"share_of_first": round(len(common) / len(sa), 3), "examples": examples}


def check(path: Path) -> dict:
    text = read_text(path)
    wc = len(words(text))
    lower = text.lower()
    return {
        "file": str(path),
        "word_count": wc,
        "estimated_a4_sides": round(wc / WORDS_PER_SIDE, 1),
        "over_length_risk": wc > WORDS_PER_SIDE * MAX_SIDES,
        "note_length": "Count includes the credentials and contact block, which the limit excludes.",
        "dates_found": [m.group(0) for m in DATE_RE.finditer(text)][:5],
        "emails_found": EMAIL_RE.findall(text)[:3],
        "phone_like_found": [p.strip() for p in PHONE_RE.findall(text)][:3],
        "mentions_global_talent_or_tech_nation": bool(GTV_RE.search(text)),
        "uk_mentions": len(UK_RE.findall(text)),
        "time_anchors": [m.group(0) for m in YEARS_RE.finditer(text)][:8],
        "placeholders": PLACEHOLDER_RE.findall(text)[:10],
        "stock_phrases": [p for p in STOCK_PHRASES if p in lower],
        "numbers_cited": len(re.findall(r"\b\d[\d,.]*\s?(%|k|m|bn|million|billion|users|customers|£|\$)?", text)),
        "_text": text,
    }


def main(argv: list[str]) -> None:
    draft = None
    if "--draft" in argv:
        i = argv.index("--draft")
        draft = Path(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]
    if not argv:
        sys.exit(__doc__)
    results = [check(Path(p)) for p in argv]
    report = {"letters": [], "cross_letter_overlap": [], "draft_overlap": []}
    for r in results:
        report["letters"].append({k: v for k, v in r.items() if k != "_text"})
    for i in range(len(results)):
        for j in range(i + 1, len(results)):
            o = overlap(results[i]["_text"], results[j]["_text"])
            report["cross_letter_overlap"].append({"a": results[i]["file"], "b": results[j]["file"], **o})
    if draft:
        dtext = read_text(draft)
        for r in results:
            report["draft_overlap"].append({"letter": r["file"], "draft": str(draft), **overlap(r["_text"], dtext)})
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main(sys.argv[1:])
