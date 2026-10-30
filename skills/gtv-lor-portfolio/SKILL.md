---
name: gtv-lor-portfolio
description: Checks a UK Global Talent visa (Tech Nation) applicant's 3 recommendation letters as a set - distinct main examples, coverage of the chosen criteria, author mix and independence, consistent facts and plans, and textual overlap - and names the weakest letter and how to fix it. Part of the gtv-lor suite. Use when the user types /gtv-lor-portfolio or has 2 or 3 Global Talent LORs and asks whether they "work together", "overlap" or "cover the criteria". Do NOT use for other visas.
metadata:
  author: Julian Kalichman
  version: 3.0.0
---

# /gtv-lor-portfolio

Read `references/rules.md`, `references/workspace.md`, `references/requirements.md` and `references/rubric.md`.

## Step 1: Gather

All letters under `letters/*/` (latest revision of each), `profile.md`, `referees.md`. Each letter needs a current `assessment.md`; follow `/gtv-lor-eval` for any that lack one.

## Step 2: Mechanical overlap

```bash
python3 scripts/letter_check.py letters/a/<latest> letters/b/<latest> letters/c/<latest>
```

Any pair above 0.05 in `cross_letter_overlap`: quote the shared phrases.

## Step 3: Score the set (1 to 5 each)

From the portfolio section of `rubric.md`:

- **Distinct examples**: one headline example per letter; shared background is fine.
- **Coverage**: mandatory criterion and both optional criteria from `profile.md`.
- **Author mix**: at least two arm's-length authors; not all from one organisation.
- **Consistency**: names, titles, dates, numbers and plans agree across letters and `profile.md`. Platform-wide numbers appear in one letter only.
- **Textual independence**: structure, openings and phrasing differ.

## Step 4: Report

Write `portfolio.md`: the five scores, the individual letter scores side by side, the weakest letter and the single change that would most improve the set. Update `workspace.md` (log line).

## Next

Fixes needed: name `/gtv-lor-improve` for the letter concerned. Set is strong: "Next: `/gtv-lor-final`."
