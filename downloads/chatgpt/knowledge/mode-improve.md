# /gtv-lor-improve

Read `references/rules.md`, `references/workspace.md`, `references/requirements.md` and `references/rubric.md`.

## Step 1: Load the score

Use `letters/<slug>/assessment.md`. If it is missing or older than the letter, follow `/gtv-lor-evaluate` first (same conversation is fine).

## Step 2: Rank the changes

Order by score gained per unit of effort; keep the 5 to 8 that matter most.

1. **Gate failures** with the exact fix (add the date, sign via DocuSign and keep the log, put the author's CV inside the same PDF).
2. **Heavy dimensions** (D2 and D3 weigh 2): for each low score, quote the line, say what the next score level needs per the rubric anchors, and which fact would get it there.
3. **Consistency**: anything that contradicts `profile.md`, the applicant's plans or another letter.
4. **Authenticity**: template signals to remove (checklist headings, stock phrases, em-dashes), overlap with other letters.
5. **Room**: if the letter is near 3 sides, name what to cut to fit the additions.

## Step 3: Fill the facts

For every change that needs a fact, take it from `profile.md` or `factpack.md`. If it is missing, ask the user in one batch (AskUserQuestion when available). Verify numbers the user gives where you can; never invent one. If the user is the recommender and the fact is the applicant's, mark it `[ASK APPLICANT: ...]`.

## Step 4: Write the outputs

- `letters/<slug>/improvements.md`: the ranked list (change, rule or dimension, quote, fact to use, score effect) and the projected score if all land, plus what still holds it below 5.
- `letters/<slug>/factpack.md` (create or update): the facts and rule points in plain words for the author, grouped as must fix / biggest gains / where to make room. No sample sentences. Top line: "Please write any changes in your own words."

Update `workspace.md` (status `improved`, log line).

## Brief audit

If the input is the applicant's note to recommenders rather than a letter, check it against every rule in `requirements.md` sections 2 to 5: omissions, wrong statements (for example "CV or LinkedIn" against rule F5b), and template risks it creates (a shared starting draft, one facts list for all 3 authors, hyperbole). Write `brief-audit.md`.

## Next

"Next: rewrite in your own words, then `/gtv-lor-evaluate` to re-score. Or `/gtv-lor-polish` to see these changes as highlighted tracked edits in your .docx."
