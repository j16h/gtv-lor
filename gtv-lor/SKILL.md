---
name: gtv-lor
description: Assesses, improves and drafts letters of recommendation (LOR) for the UK Global Talent visa, digital technology route (Tech Nation endorsement). Scores a letter on a 5-point scale against the official GOV.UK and Tech Nation rules, lists the changes that would make it strong, interviews the candidate and recommender to draft a new letter or fact pack, polishes an existing letter into a Word file with highlighted tracked changes, checks all 3 letters as a set, audits briefs sent to recommenders, and runs a pre-submission check. Use when the user mentions a recommendation, reference or endorsement letter together with Global Talent, GTV, Tech Nation, Exceptional Talent or Exceptional Promise, or asks to "score my LOR", "improve this letter", "polish this letter", "write a letter for my referee", "check my recommenders". Accepts pasted text, .txt, .md, .docx or .pdf. Do NOT use for other visas (Skilled Worker, O-1, EB-1) or for general job references.
metadata:
  author: Julian Kalichman
  version: 2.2.0
  sources-retrieved: 2026-10-30
---

# Global Talent letter review

## Critical

- **Rules first.** Read `references/requirements.md` (verbatim rules with IDs) before any mode. Cite rule IDs and quote the letter for every finding.
- **The fraud rules apply to everything this skill produces.** Tech Nation says templated, duplicated or AI-created letters "may be considered fraudulent", and it contacts referees. So:
  - Drafts are built only from interview answers, never invented facts, and are labelled as drafts for the author to rewrite.
  - Recommendations say what to add and why, with the facts to use. They do not hand over polished replacement sentences unless the user asks for a draft (Mode 3) or a polish (Mode 7).
  - Tell the user this risk once, plainly, the first time they ask for a draft.
- **Rule versus judgement.** A missing date is a rule failure; "generic" is judgement. Label which is which.
- **No em-dashes, ever.** Nothing this skill writes (reports, fact packs, drafts, polish edits) contains an em-dash (U+2014). Use a comma, colon, semicolon, parentheses or a new sentence. In Mode 7, also replace the letter's existing em-dashes as tracked edits.
- **Signals are not proof.** Say "reads as templated", never "was written by AI".

## Pick the mode

| User wants | Mode |
|------------|------|
| "Score / assess / is this good enough" | 1 Assess |
| "What should change / make it stronger" | 2 Improve (runs Mode 1 first) |
| "Write / draft a letter", no letter yet | 3 Draft |
| Has 2 or 3 letters | 4 Portfolio (after Mode 1 on each) |
| Choosing recommenders | 5 Recommender check |
| About to submit | 6 Final check |
| Shares a note to recommenders | Brief audit (end of Mode 2) |
| "Polish / edit / apply the fixes" to an existing letter | 7 Polish |

If unclear, ask one question. Route (Exceptional Talent or Exceptional Promise) matters for every mode: ask if unknown.

## Mode 1: Assess (5-point scale)

1. Save pasted text to a scratch file. Run:
   ```bash
   python3 scripts/letter_check.py letter.pdf [other letters] [--draft brief.txt]
   ```
   Read: `estimated_a4_sides` over 3 (count includes the credentials block, so verify before failing); cross-letter overlap above 0.05 or draft overlap above 0.10 means template risk; any `placeholders` fails G10. If the script cannot run, check by reading and say so.
2. Apply `references/rubric.md`: gates G1 to G10, then D1 to D8 on the 1 to 5 scale with a quote per score, then the weighted overall score with its caps and verdict.
3. Report:

```
Overall: 3.4 / 5, Needs work   (route: Exceptional Talent)
Gates: 9 pass, 1 cannot tell (G7 signature: check the PDF)

| Dimension | Score | Evidence |
| D1 Author credibility | 4 | "..." |
...
Authenticity: signals with quotes
```

## Mode 2: Improve

Run Mode 1, then list changes ranked by score gained per unit of effort:

1. **Gate failures first**: each with the exact fix (add date, sign via DocuSign, attach CV in the same PDF).
2. **Lowest-scoring heavy dimensions next** (D2, D3 weigh 2): for each, say what the next score level needs per the rubric anchors, and which facts from the candidate's evidence would get it there. Ask the user for missing facts instead of inventing them.
3. **Authenticity fixes**: phrases to cut and why; overlaps with other letters to replace.
4. End with the projected score if all fixes land, and what would still hold it below 5.

Keep it to the 5 to 8 changes that matter most. If the user then asks for rewritten text, switch to Mode 3 for that section, with the same drafting rules.

**Brief audit**: when the input is the applicant's note to recommenders, check it against every rule in `requirements.md` sections 2 to 5: what it omits, what it states wrongly (for example "CV or LinkedIn" versus Tech Nation's CV-inside-the-letter rule F5b), and what template risk it creates (a shared starting draft, one facts list for all 3 authors, hyperbole the author might repeat).

## Mode 3: Draft a new letter

1. Read `references/interview.md` and `references/drafting.md`.
2. Interview in rounds: application (Round 1), the recommender (Round 2), and the author's own view (Round 3, forwarded or direct). Ask a few questions at a time; do not dump all of them.
3. Build the evidence map for all 3 letters before drafting any of them.
4. Offer the two outputs and let the user pick:
   - **Fact pack** (lower risk): the author writes from facts and rules, no sample sentences.
   - **Draft** for the author to rewrite: built only from answers, gaps marked `[ASK AUTHOR: ...]`, unconfirmed opinions marked `[AUTHOR TO CONFIRM]`.
5. Score the draft with Mode 1 and fix it until it reaches 4+ on content dimensions, then attach the "make it yours" checklist from `drafting.md`.

## Mode 4: Portfolio (all 3 letters)

Assess each letter, then score the set with the portfolio section of `rubric.md`: distinct main examples, criteria coverage, author mix, consistency of dates, titles and numbers with the CV and personal statement, and textual independence (script cross-overlap). Name the weakest letter and what would replace or fix it.

## Mode 5: Recommender check

For each candidate author, using Round 2 of `interview.md`: does the author pass G1 and G2, how arm's-length are they (A4), what main example could only they speak to, and are any two authors redundant? Recommend the strongest 3 and a reserve.

## Mode 6: Final check

Before submission, confirm per letter: gates G1 to G10 all pass; one PDF holding letter plus author CV; DocuSign or similar audit log kept; English translation if needed (F7); dated within the application window; every number matches the evidence documents; portfolio cross-overlap under 0.05. Report as a checklist with any blocker first.

## Mode 7: Polish an existing letter

Edits the author's own letter in place, as Word tracked changes, so every change is visible and the author decides.

1. **Inputs**: the letter as .docx (if only a PDF exists, ask the author for the Word file), and the improvements to make: a fact pack, the Mode 2 list, or facts the user gave in this conversation. If none exists, run Mode 2 first.
2. **Plan the edits**, each tied to a fact or a rubric finding. Edits may only:
   - add or correct facts that are in the fact pack or confirmed by the user;
   - fix rule failures (missing date, wrong route vocabulary, placeholders);
   - cut text to stay within 3 A4 sides, or remove template signals (checklist headings, stock phrases);
   - replace every em-dash in the letter (`em_dashes` in the checker output) with a comma, colon, semicolon or full stop, using `context` to target each one.
   Never add a fact, number, opinion or anecdote the author has not given. Opinions the user supplied for the author go in as `[AUTHOR TO CONFIRM]`.
3. **Keep the author's voice.** Change the fewest words that do the job. Match the letter's own vocabulary, sentence length and punctuation; do not import house style. Leave untouched every sentence that already scores 4 or 5.
4. **Write the edits** as JSON (see the script's docstring for the format), with a one-line `reason` per edit naming the fact or rule, then run:
   ```bash
   python3 scripts/polish_docx.py letter.docx edits.json letter-polished.docx
   ```
   Insertions come out highlighted yellow, deletions as tracked deletions, and each edit carries a Word comment with its reason. If an edit fails (text not found, or found twice), fix the `old` or `anchor` string and rerun from the original file.
5. **Check the result**: run `letter_check.py` on the polished file (it reads the text with changes accepted) and confirm it still fits 3 sides, then score it with Mode 1.
6. **Hand over** the polished .docx and a short change summary (edit, reason, score effect). Tell the author to review each change in Word (Review, then Accept or Reject), rewrite the highlighted parts in their own words where they wish, then sign. The first time in a conversation, say once that Tech Nation treats AI-created letters as unacceptable and contacts referees, so the author must read and own every change.

## Examples

**Assess.** "Score Mark's letter, I'm applying for Exceptional Talent." Result: 3.4 / 5, Needs work. D5 scored 2 ("the UK is a world-leading tech hub", no reason specific to the applicant); stock phrase "testament to" lowers D7 to 3.

**Draft.** "Help me get a letter from Anna, my lead investor." Actions: Round 1 if not done, Round 2 for Anna, offer Round 3 questions for Anna to answer, evidence map, then a fact pack or a draft marked for Anna to rewrite, scored at 4.1.

## Troubleshooting

- **PDF with no text layer**: the script returns no words. Ask for text or .docx; mark signatures and logos "cannot tell".
- **Letter not in English**: rule F7 needs an authorised translation; assess the translation and say the original must be submitted too.
- **Rules may have changed**: sources retrieved 2026-10-30. If the user reports a change or much time has passed, re-read both URLs in `requirements.md` first.
- **Only the candidate is answering the author questions**: proceed, but mark the author's opinions `[AUTHOR TO CONFIRM]` and say D7 will stay capped until the author has rewritten it.
