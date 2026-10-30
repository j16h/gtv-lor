---
name: gtv-lor
description: Start here for UK Global Talent visa (Tech Nation, digital technology) letters of recommendation. Asks who you are and for your document, sets up a workspace, shows progress, and routes to the right gtv-lor command. Two workflows - a recommender improving an existing letter (evaluate, improve, polish, final) and writing a letter from scratch (profile, referees, write). Use when the user types /gtv-lor, mentions a Global Talent, GTV or Tech Nation recommendation letter or LOR, or asks "where do I start", "which gtv-lor command". Do NOT use for other visas or general job references.
metadata:
  author: Julian Kalichman
  version: 3.0.0
  sources-retrieved: 2026-10-30
---

# gtv-lor: start here

Read `references/rules.md` and `references/workspace.md` first.

## Step 1: Show where things stand

Look for `gtv-lor-workspace/workspace.md`.

- **Found**: print the Letters table and the last 3 Log lines, then go to Step 4.
- **Not found**: say "Let's set up your workspace" and continue.

## Step 2: Ask who you are and what you have

Ask together (AskUserQuestion if available):

1. **Role**:
   - "I'm a recommender and I have a draft letter"
   - "I'm a recommender starting from scratch"
   - "I'm the applicant, planning my letters"
2. **Route**: Exceptional Talent (leader), Exceptional Promise (potential leader, early career), or not sure.
3. **Applicant's name** as in their passport.

## Step 3: Add the document

Ask for the letter if the role has one:

> Add your letter: attach the file, give a path (.docx, .pdf, .md or .txt), or paste the text. A .docx is best: it is the only format `/gtv-lor-polish` can edit.

- Ask for the author's name to make the slug (e.g. `dario-krpan`).
- Save it, unchanged, as `gtv-lor-workspace/letters/<slug>/original.<ext>` (pasted text: `original.md`).
- Also invite: a fact pack or brief from the applicant, the applicant's CV or personal statement, other letters. Save them in the workspace (`letters/<slug>/factpack.md`, `profile.md`).

Create `workspace.md` from the template in `references/workspace.md`. If the current directory is a git repository, suggest adding `gtv-lor-workspace/` to `.gitignore`.

## Step 4: Route

Show the workflow for their role, mark steps already done (from the Letters table), and name the next command.

**Workflow A: improve a draft** (recommender with a letter)

```
/gtv-lor-evaluate   score it 1 to 5 against the rules
/gtv-lor-improve    ranked changes, plus a fact pack of what to add
/gtv-lor-polish     optional: the changes as highlighted tracked edits in your .docx
   (rewrite in your own words)
/gtv-lor-evaluate   re-score your revision
/gtv-lor-final      pre-submission checklist
```

**Workflow B: from scratch** (applicant, or recommender without a draft)

```
/gtv-lor-profile    interview: the applicant's route, criteria, achievements, UK plans
/gtv-lor-referees   applicant only: pick 3 referees, one main example each
/gtv-lor-write      per referee: a fact pack (lower risk) or a draft to rewrite
   (the author writes the letter)
then Workflow A for each letter
/gtv-lor-portfolio  check all 3 letters as a set
/gtv-lor-final      pre-submission checklist
```

Then: "Next: run `/gtv-lor-<step>`." If the user prefers, continue straight into that step in this conversation by following that command's instructions.

## Commands

| Command | Use it to |
|---------|-----------|
| `/gtv-lor` | Start, add documents, see status |
| `/gtv-lor-evaluate` | Score a letter 1 to 5 |
| `/gtv-lor-improve` | Get ranked changes and a fact pack |
| `/gtv-lor-polish` | Apply changes as highlighted tracked edits (.docx) |
| `/gtv-lor-profile` | Capture the applicant's facts |
| `/gtv-lor-referees` | Choose and vet referees |
| `/gtv-lor-write` | Fact pack or draft for one author |
| `/gtv-lor-portfolio` | Check the 3 letters together |
| `/gtv-lor-final` | Pre-submission checklist |
