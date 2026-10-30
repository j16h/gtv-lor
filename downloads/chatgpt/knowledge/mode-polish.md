# /gtv-lor-polish

Read `references/rules.md`, `references/workspace.md`, `references/requirements.md` and `references/rubric.md`.

## Step 1: Inputs

- `letters/<slug>/original.docx`. If the letter is only a PDF or text, ask for the Word file; stop if there is none.
- What to change: `improvements.md` and `factpack.md`. If missing, follow `/gtv-lor-improve` first.
- The first time in a conversation, give the quick heads-up from `rules.md` (Tech Nation doesn't accept AI-written letters and checks with referees), and ask the author to go through every change and put the highlighted bits in their own words.

## Step 2: Plan the edits

Each edit is tied to an item in `improvements.md` or `factpack.md`. Edits may only:

- add or correct facts from the fact pack or confirmed by the user;
- fix rule failures (date, route vocabulary, placeholders);
- cut text to stay within 3 A4 sides;
- remove template signals: checklist headings, stock phrases, and every em-dash (`em_dashes` in the checker output), replaced by a comma, colon, semicolon or full stop.

Keep the author's voice: fewest words, the letter's own vocabulary and sentence length, untouched sentences that already score 4 or 5. No new facts, numbers, opinions or anecdotes. Do not repeat the same point in two places; when you remove a heading or paragraph, fix any sentence that pointed at it.

## Step 3: Apply

Write `letters/<slug>/edits.json`. Operations (full format in the script's docstring):

```json
[
  {"op": "replace", "old": "exact text", "new": "new text", "reason": "rule or fact"},
  {"op": "replace", "old": " \u2014 ", "new": ": ", "context": "longer unique text around it", "reason": "No em-dashes"},
  {"op": "insert", "after": "exact text", "text": " added sentence.", "reason": "..."},
  {"op": "insert_after", "anchor": "text in a paragraph", "text": "New paragraph.", "reason": "..."},
  {"op": "delete_paragraph", "anchor": "text in a paragraph", "reason": "..."}
]
```

```bash
python3 scripts/polish_docx.py letters/<slug>/original.docx letters/<slug>/edits.json letters/<slug>/polished.docx
```

If an edit fails (text not found or found twice), fix its `old`, `after`, `anchor` or `context` and rerun from `original.docx`.

## Step 4: Check

```bash
python3 scripts/letter_check.py letters/<slug>/polished.docx
```

Confirm: within 3 sides, `em_dashes` is 0, no placeholders except deliberate `[ASK AUTHOR: ...]`. Read the accepted text once for repetition and dangling references. Score it with the `/gtv-lor-eval` rubric.

## Step 5: Hand over

Show a table (edit, reason, score effect), the projected score, and tell the author: open `polished.docx` in Word, then Review, Accept or Reject each change; rewrite highlighted text in your own words; then date, sign (DocuSign) and attach your CV in the same PDF.

Update `workspace.md` (status `polished`, log line).

## Next

"Next: after you've revised it, `/gtv-lor-eval` to re-score, then `/gtv-lor-final`."
