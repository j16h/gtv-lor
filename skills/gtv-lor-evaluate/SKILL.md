---
name: gtv-lor-evaluate
description: Scores a UK Global Talent visa (Tech Nation) recommendation letter on a 1 to 5 scale against the GOV.UK and Tech Nation rules - pass/fail gates, eight weighted dimensions with quotes, authorship risk and a verdict. Part of the gtv-lor suite. Use when the user types /gtv-lor-evaluate or asks to "score", "assess", "rate" or "check" a Global Talent or Tech Nation LOR, including re-scoring a revised letter. Accepts .docx, .pdf, .md, .txt or pasted text. Do NOT use for other visas.
metadata:
  author: Julian Kalichman
  version: 3.0.0
---

# /gtv-lor-evaluate

Read `references/rules.md`, `references/workspace.md`, `references/requirements.md` and `references/rubric.md`.

## Step 1: Pick the letter

From `gtv-lor-workspace/workspace.md`: if one letter exists, use it; if several, ask which. If the user attaches a new letter here, save it as `letters/<slug>/original.<ext>` first. For a re-score, use the newest revision the user gives (save as `letters/<slug>/revision-<n>.<ext>`). Route comes from `workspace.md`; ask if unknown.

## Step 2: Mechanical checks

```bash
python3 scripts/letter_check.py letters/<slug>/original.docx [other letters] [--draft letters/<slug>/factpack.md]
```

Run from inside `gtv-lor-workspace/` (adjust paths), with `scripts/` resolved relative to this skill's folder. Read:

- `estimated_a4_sides` over 3: likely too long (count includes the credentials block, so verify).
- `em_dashes` above 0: note as a D7 signal.
- `placeholders`: any value fails G10.
- `cross_letter_overlap` above 0.05 or `draft_overlap` above 0.10: template risk; quote the shared phrases.
- A .docx with tracked changes is read with changes accepted.

If the script cannot run, check by reading and say so.

## Step 3: Score

Apply `rubric.md` in order: gates G1 to G10 (pass / fail / cannot tell), D1 to D8 (1 to 5, one quote each), authenticity signals, weighted overall with caps, verdict. If a `factpack.md` or `profile.md` exists, use it for D8 (claims match evidence) and consistency.

## Step 4: Report

Write `letters/<slug>/assessment.md` and show it:

```
Overall: 3.4 / 5, Needs work   (route: Exceptional Talent)
Gates: 9 pass, 1 fail (G9 author CV not in the file)

| Dimension | Score | Evidence (quote) |
| D1 Author credibility and relationship | 3 | "..." |
| D2 Achievements (x2) | 4 | "..." |
...
Authenticity: low | medium | high
- signal: "quote"

Biggest gaps: 3 bullets, most important first
```

If a previous `assessment.md` exists, add a "Change since last score" line per dimension.

Update `workspace.md` (status `evaluated`, score, log line).

## Next

- Score below 4.5: "Next: `/gtv-lor-improve`."
- 4.5 or above: "Next: `/gtv-lor-final`."
- All 3 letters evaluated: also suggest `/gtv-lor-portfolio`.

## Troubleshooting

- **PDF with no text layer**: ask for the .docx or text; mark signature and logo "cannot tell".
- **Not in English**: rule F7 needs an authorised translation; assess the translation.
- **Rules may have changed**: sources retrieved 2026-10-30; if much later, re-read the two URLs in `requirements.md`.
