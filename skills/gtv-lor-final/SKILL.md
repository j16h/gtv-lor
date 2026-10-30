---
name: gtv-lor-final
description: "Pre-submission checklist for UK Global Talent visa (Tech Nation) recommendation letters - every gate passes, one PDF with letter plus author CV, e-signature log kept, translations, dates, numbers matching evidence, and no overlap between the 3 letters. Part of the gtv-lor suite. Use when the user types /gtv-lor-final or says they are \"about to submit\", \"ready to send\" or wants a \"final check\" of Global Talent LORs. Do NOT use for other visas."
metadata:
  author: Julian Kalichman
  version: 3.0.0
---

# /gtv-lor-final

Read `references/rules.md`, `references/workspace.md`, `references/requirements.md` and `references/rubric.md`.

## Step 1: Gather

The signed final PDF of each letter (ask for it; save as `letters/<slug>/final.pdf`), `profile.md`, and the evidence list if the applicant has one.

## Step 2: Check each letter

```bash
python3 scripts/letter_check.py letters/*/final.pdf
```

For each letter confirm, as pass / fail / cannot tell:

- Gates G1 to G10 all pass (`rubric.md`).
- One PDF holds the letter and the author's CV (F5b).
- Signed; e-signature audit log kept (F6).
- English, or an authorised translation attached (F7).
- Dated, and the date is recent.
- Every number, title and date matches `profile.md` and the evidence documents (X4, X5).
- No placeholders: no `[ASK AUTHOR` or `[AUTHOR TO CONFIRM` left.
- `em_dashes` is 0 (house style; not a Tech Nation rule).

## Step 3: Check the set

- 3 letters (N1), each with a different main example (N2).
- `cross_letter_overlap` under 0.05 for every pair.
- The applicant's name is spelled identically everywhere, as in the passport.

## Step 4: Report

Write `final-check.md`: blockers first, then warnings, then passes. Update `workspace.md` (status `final` for letters that pass, log line).

## Next

All clear: "Ready to submit with your application." Otherwise name the command that fixes each blocker.
