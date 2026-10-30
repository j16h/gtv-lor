#!/usr/bin/env python3
"""Copy shared references and scripts into each skill, then build upload zips
and the downloads for Claude.ai, ChatGPT and any other chatbot.

Usage: python3 bin/sync.py [--check]

shared/ is the source of truth. Each skill gets only the files it needs
(MANIFEST below), so every skill folder is self-contained and works when
uploaded alone to Claude.ai. --check exits 1 if any copy is stale.
"""
import shutil
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"
DIST = ROOT / "dist"
PLATFORMS = ROOT / "platforms"
DOWNLOADS = ROOT / "downloads"

BASE = ["references/rules.md", "references/workspace.md"]
CHECK = ["scripts/letter_check.py"]
MANIFEST = {
    "gtv-lor": BASE,
    "gtv-lor-evaluate": BASE + ["references/requirements.md", "references/rubric.md"] + CHECK,
    "gtv-lor-improve": BASE + ["references/requirements.md", "references/rubric.md"] + CHECK,
    "gtv-lor-polish": BASE + ["references/requirements.md", "references/rubric.md", "scripts/polish_docx.py"] + CHECK,
    "gtv-lor-final": BASE + ["references/requirements.md", "references/rubric.md"] + CHECK,
    "gtv-lor-profile": BASE + ["references/interview.md"],
    "gtv-lor-referees": BASE + ["references/requirements.md", "references/interview.md"],
    "gtv-lor-write": BASE + ["references/requirements.md", "references/rubric.md", "references/interview.md",
                             "references/drafting.md"] + CHECK,
    "gtv-lor-portfolio": BASE + ["references/requirements.md", "references/rubric.md"] + CHECK,
}
MODES = ["evaluate", "improve", "polish", "profile", "referees", "write", "portfolio", "final"]
REFS = ["rules", "workspace", "requirements", "rubric", "interview", "drafting"]
SCRIPTS = ["letter_check.py", "polish_docx.py"]
RECOMMENDER_SET = ["gtv-lor", "gtv-lor-evaluate", "gtv-lor-improve", "gtv-lor-polish", "gtv-lor-final"]


def main(check: bool) -> None:
    stale = []
    for skill, files in MANIFEST.items():
        dest = SKILLS / skill
        if not (dest / "SKILL.md").exists():
            sys.exit(f"missing {dest}/SKILL.md")
        wanted = {dest / f for f in files}
        for sub in ("references", "scripts"):
            for f in (dest / sub).glob("*") if (dest / sub).exists() else []:
                if f not in wanted:
                    stale.append(str(f.relative_to(ROOT)))
                    if not check:
                        f.unlink()
        for f in files:
            src, dst = SHARED / f, dest / f
            if not dst.exists() or dst.read_bytes() != src.read_bytes():
                stale.append(str(dst.relative_to(ROOT)))
                if not check:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
    if check:
        if stale:
            sys.exit("stale copies, run python3 bin/sync.py:\n  " + "\n  ".join(stale))
        print("all skill copies up to date")
        return
    DIST.mkdir(exist_ok=True)
    for skill in MANIFEST:
        with zipfile.ZipFile(DIST / f"{skill}.zip", "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted((SKILLS / skill).rglob("*")):
                if f.is_file() and f.name != ".DS_Store" and "__pycache__" not in f.parts:
                    z.write(f, f.relative_to(SKILLS))
    with zipfile.ZipFile(DIST / "gtv-lor-recommender-set.zip", "w") as z:
        for skill in RECOMMENDER_SET:
            z.write(DIST / f"{skill}.zip", f"{skill}.zip")
    build_downloads()
    print(f"synced {len(stale)} file(s); zips in {DIST.relative_to(ROOT)}/, downloads in {DOWNLOADS.relative_to(ROOT)}/")


def mode_text(mode: str) -> str:
    """A sub-skill's SKILL.md without its frontmatter."""
    text = (SKILLS / f"gtv-lor-{mode}" / "SKILL.md").read_text()
    return text.split("---", 2)[2].lstrip()


def build_downloads() -> None:
    if DOWNLOADS.exists():
        shutil.rmtree(DOWNLOADS)

    # Claude.ai: one skill holding every command
    with zipfile.ZipFile(_mk(DOWNLOADS / "claude-ai") / "gtv-lor.zip",
                         "w", zipfile.ZIP_DEFLATED) as z:
        z.write(PLATFORMS / "bundle" / "SKILL.md", "gtv-lor/SKILL.md")
        for r in REFS:
            z.write(SHARED / "references" / f"{r}.md", f"gtv-lor/references/{r}.md")
        for sc in SCRIPTS:
            z.write(SHARED / "scripts" / sc, f"gtv-lor/scripts/{sc}")
        for m in MODES:
            z.writestr(f"gtv-lor/modes/{m}.md", mode_text(m))

    # ChatGPT: Custom GPT kit
    kit = _mk(DOWNLOADS / "chatgpt")
    knowledge = _mk(kit / "knowledge")
    instructions = (PLATFORMS / "chatgpt" / "instructions.md").read_text()
    if len(instructions) > 8000:
        sys.exit(f"ChatGPT instructions are {len(instructions)} chars; the limit is 8000")
    shutil.copy2(PLATFORMS / "chatgpt" / "instructions.md", kit / "instructions.md")
    shutil.copy2(PLATFORMS / "chatgpt" / "gpt-settings.md", kit / "gpt-settings.md")
    for r in REFS:
        shutil.copy2(SHARED / "references" / f"{r}.md", knowledge / f"{r}.md")
    for sc in SCRIPTS:
        shutil.copy2(SHARED / "scripts" / sc, knowledge / sc)
    for m in MODES:
        (knowledge / f"mode-{m}.md").write_text(mode_text(m))
    with zipfile.ZipFile(DOWNLOADS / "chatgpt-gpt-kit.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(kit.rglob("*")):
            if f.is_file():
                z.write(f, f.relative_to(DOWNLOADS))

    # Any chatbot: one file
    parts = [(PLATFORMS / "portable" / "header.md").read_text()]
    names = {"rules": "Rules", "workspace": "Workspace", "requirements": "Requirements", "rubric": "Rubric",
             "interview": "Interview", "drafting": "Drafting"}
    for r in ["rules", "workspace", "requirements", "rubric"]:
        parts.append(f"# Section: {names[r]} (references/{r}.md)\n\n" + (SHARED / "references" / f"{r}.md").read_text())
    for m in MODES:
        parts.append(f"# Section: Mode: {m} (/gtv-lor-{m})\n\n" + mode_text(m))
    for r in ["interview", "drafting"]:
        parts.append(f"# Section: {names[r]} (references/{r}.md)\n\n" + (SHARED / "references" / f"{r}.md").read_text())
    (_mk(DOWNLOADS / "portable") / "gtv-lor-prompt.md").write_text("\n\n---\n\n".join(parts))


def _mk(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


if __name__ == "__main__":
    main("--check" in sys.argv)
