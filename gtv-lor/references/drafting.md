# Drafting a letter

Read this before Mode 3. The draft is the **author's** letter built from the **author's** answers. Tech Nation says templates and AI-created letters may be treated as fraudulent (X1 to X3) and that it contacts referees (X5). So the draft is a starting point for the author, never a finished letter to sign unread.

## Non-negotiables

1. **Facts come from interviews, never invention.** Every claim needs a source in the answers from `interview.md`. If a fact is missing, write `[ASK AUTHOR: ...]` in the draft rather than guessing. That placeholder fails gate G10 on purpose, so the draft cannot be submitted until the gap is filled.
2. **Opinions come from the author.** Judgements ("the strongest product lead I have worked with") must be what the author said or would sign under questioning. If only the candidate answered, mark those sentences `[AUTHOR TO CONFIRM]`.
3. **One letter, one main example.** Before drafting, write the evidence map (below) for all 3 letters so no headline example repeats (N2).
4. **No shared skeleton.** Do not reuse the same section order, opening or closing across letters. Do not use the GOV.UK bullets as headings.
5. **Plain, specific language.** No stock phrases from the rubric's D7 list. Prefer one anecdote with a number to three adjectives.
6. **Label it.** Put "DRAFT for [author] to rewrite in their own words" at the top of every draft.

## Evidence map (do this first)

| Letter | Author | Relationship, since | Main example (unique) | Supporting example | Criterion it backs | Evidence doc |
|--------|--------|---------------------|-----------------------|--------------------|--------------------|--------------|

Check: three different main examples; together they back the mandatory criterion and both chosen optional criteria; no claim lacks an evidence doc.

## Shape of a letter

This is a checklist of jobs, not a template. Vary the order and the openings across letters.

- **Header**: author letterhead or name, address, phone, email; date; addressed to Tech Nation, Global Talent endorsement.
- **Who I am** (2 to 4 sentences): role, years in digital technology, one marker of standing. Detailed credentials go in the attached CV.
- **How I know the work** (C2, A2): context, first contact with a month and year, how often, in what capacity.
- **What I saw** (C3): the main example told as a short story with numbers; what the applicant personally did versus the team.
- **Why this is leadership** (C4): recognition by others; comparison with peers the author has seen; Talent or Promise vocabulary.
- **The UK** (C5, C6): why the UK suits this specific work, and what the UK gains: named sectors, places, hires, partners. Only what the author believes.
- **What comes next** (C7): the plan as the author understands it, consistent with the personal statement.
- **Close and sign**: a clear statement of support, availability for contact, signature, name, title.
- **Attached**: author CV in the same PDF (F5b).

Target 1.5 to 2.5 A4 sides for the body. Longer rarely helps.

## After drafting

1. Score the draft with `rubric.md`, as harshly as a stranger's letter.
2. Run `scripts/letter_check.py` with the other letters and with the candidate's brief as `--draft`; fix any overlap above the thresholds.
3. Give the author the **make it yours** checklist:
   - Rewrite every paragraph in your own words; keep the facts.
   - Add one memory only you have (a meeting, a decision, a moment).
   - Delete anything you would not say on the phone to an assessor.
   - Check every number and date against what you know.
   - Put it on your letterhead, date it, sign with DocuSign or similar, and attach your CV in the same PDF.
