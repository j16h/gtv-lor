---
name: gtv-lor-profile
description: Interviews a UK Global Talent visa (Tech Nation) applicant, a few questions at a time, to build their profile - route, criteria, achievements with evidence, recognition, UK plans, passport name - which every other gtv-lor command uses for letters. Part of the gtv-lor suite. Use when the user types /gtv-lor-profile, is starting Global Talent recommendation letters from scratch, or wants to record or update the applicant's facts. Do NOT use for other visas.
metadata:
  author: Julian Kalichman
  version: 3.0.0
---

# /gtv-lor-profile

Read `references/rules.md`, `references/workspace.md` and `references/interview.md`.

## Step 1: Start from what exists

Read `profile.md` if present and ask only about gaps. Offer to read the applicant's CV, personal statement or any brief they already sent recommenders; extract facts from them first, then confirm.

## Step 2: Interview

Use Round 1 of `interview.md`, a few questions per message, AskUserQuestion for choices. Cover:

1. Route and passport name.
2. Mandatory criterion and the 2 optional criteria they will use.
3. Current role(s), companies, what each does, dates.
4. Top 3 to 5 achievements, each with a number, a date and the evidence document that proves it.
5. Recognition by others: press, awards, talks (with audience size), partnerships, approaches from outside bodies.
6. UK plans: city, what they will build, hiring, partners, timeline (only what is real).
7. Why the UK, for this work specifically.

Push gently for numbers and evidence; accept "no" and record it. If a fact can be verified from a source the user points to, verify it.

## Step 3: Write profile.md

```
# Applicant profile
Name (passport): ...
Route: ...
Criteria: mandatory ..., optional 1 ..., optional 2 ...

## Roles
## Achievements (fact, number, date, evidence document)
## Recognition
## UK plans
## Why the UK
## Open questions
```

Flag anything that weakens the application under "Open questions" (for example research from an MSc thesis, which Tech Nation does not accept, or plans that differ between documents).

Update `workspace.md` (log line).

## Next

Applicant: "Next: `/gtv-lor-referees`." Recommender writing alone: "Next: `/gtv-lor-write`."
