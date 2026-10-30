#!/usr/bin/env python3
"""Copy shared references and scripts into each skill, then build upload zips.

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
    print(f"synced {len(stale)} file(s); zips in {DIST.relative_to(ROOT)}/")


if __name__ == "__main__":
    main("--check" in sys.argv)
