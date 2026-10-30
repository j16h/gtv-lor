---
name: gtv-lor-write
description: Prepares one UK Global Talent visa (Tech Nation) recommendation letter from scratch - interviews the author for their own view, then produces either a fact pack (facts and rules, no sample sentences, lower risk) or a draft the author must rewrite, marked with gaps to confirm, scored before handover. Part of the gtv-lor suite. Use when the user types /gtv-lor-write or asks to "write", "draft" or "start" a Global Talent LOR, or to prepare a brief or fact pack for a recommender. Do NOT use to edit an existing letter (use /gtv-lor-polish) or for other visas.
metadata:
  author: Julian Kalichman
  version: 3.0.0
---

# /gtv-lor-write

Read `references/rules.md`, `references/workspace.md`, `references/requirements.md`, `references/rubric.md`, `references/interview.md` and `references/drafting.md`.

## Step 1: Context

Needs `profile.md` (else follow `/gtv-lor-profile`). For an applicant with several letters, use `referees.md` for this author's main example (else follow `/gtv-lor-referees`). Ask which author; slug as in `workspace.md`.

## Step 2: The author's own view

The strongest letters come from the author's answers, not the applicant's. Use Round 3 of `interview.md`:

- If the author is the user, interview them directly, a few questions at a time.
- If the applicant is the user, offer the Round 3 questions as a short list to forward to the author, and continue with the applicant's answers marked `[AUTHOR TO CONFIRM]`.

## Step 3: Choose the output

Ask, recommending the fact pack:

- **Fact pack** (lower risk): the rules in plain words, this author's main example with numbers and evidence, relationship dates, the applicant's plans, what this letter must not repeat from the others, and the line "Please write this in your own words; letters that look templated can be treated as fraudulent." No sample sentences. Save `letters/<slug>/factpack.md`.
- **Draft** for the author to rewrite: say once that Tech Nation calls AI-created letters unacceptable and contacts referees. Follow `drafting.md`: only facts from answers, gaps as `[ASK AUTHOR: ...]`, unconfirmed opinions as `[AUTHOR TO CONFIRM]`, a shape and opening different from the other letters, no checklist headings, no stock phrases, no em-dashes, 1.5 to 2.5 A4 sides. Save `letters/<slug>/draft.md` (and a .docx if the user wants one), with "DRAFT for <author> to rewrite in their own words" at the top.

## Step 4: Check before handover

```bash
python3 scripts/letter_check.py letters/<slug>/draft.md [other letters] --draft profile.md
```

For a draft: score it with the `/gtv-lor-evaluate` rubric and revise until every content dimension is 4+ (D7 stays capped until the author rewrites it). Attach the "make it yours" checklist from `drafting.md`.

Update `workspace.md` (status `factpack` or `drafted`, log line).

## Next

"Send it to <author>. When their letter comes back, run `/gtv-lor` to add it, then `/gtv-lor-evaluate`."
