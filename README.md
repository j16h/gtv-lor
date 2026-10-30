# gtv-lor

A suite of agent skills for letters of recommendation for the UK Global Talent visa, digital technology route (Tech Nation endorsement). Type `/gtv-lor` to start: it asks who you are, takes your document, sets up a workspace and tells you which command to run next.

## Two workflows

**A. Improve a draft** (a recommender who has a letter)

```
/gtv-lor            add your letter
/gtv-lor-evaluate   score it 1 to 5 against the GOV.UK and Tech Nation rules
/gtv-lor-improve    ranked changes and a fact pack of what to add
/gtv-lor-polish     optional: the changes as highlighted tracked edits in your .docx
                    (rewrite in your own words)
/gtv-lor-evaluate   re-score
/gtv-lor-final      pre-submission checklist
```

**B. From scratch** (the applicant planning letters, or a recommender without a draft)

```
/gtv-lor            set up
/gtv-lor-profile    interview: route, criteria, achievements, UK plans
/gtv-lor-referees   applicant: choose 3 referees, one main example each
/gtv-lor-write      per referee: a fact pack (lower risk) or a draft to rewrite
                    then Workflow A for each letter
/gtv-lor-portfolio  check the 3 letters as a set
/gtv-lor-final      pre-submission checklist
```

Progress is saved in `gtv-lor-workspace/` in your current folder (Claude Code), so you can stop and pick up later. It holds personal data: keep it out of public repositories.

## Install

**Claude Code**

```bash
git clone https://github.com/j16h/gtv-lor.git
./gtv-lor/install.sh
```

`./gtv-lor/install.sh recommender` installs only Workflow A (for recommenders).

**Claude.ai**: turn on Settings, Capabilities, Code execution and file creation. Build the zips with `python3 bin/sync.py` (or get them from whoever shared this with you), then upload each skill zip from `dist/` under Settings, Capabilities, Skills. Recommenders need only the five in `dist/gtv-lor-recommender-set.zip` (unzip it first: it holds one zip per skill).

## How to use

### You're a recommender with a draft letter

1. Open Claude Code in any folder (or a new chat on Claude.ai) and type `/gtv-lor`.
2. Answer: "I'm a recommender and I have a draft letter", the route (Exceptional Talent or Exceptional Promise), and the applicant's name as in their passport.
3. Add your letter: attach it, give a path such as `~/Documents/letter.docx`, or paste the text. If the applicant sent you a fact pack or brief, add it too.
4. Type `/gtv-lor-evaluate`. You get a score out of 5, the rules it passes or fails, and the biggest gaps.
5. Type `/gtv-lor-improve`. You get the changes ranked by impact and a fact pack of what to add. It asks you for any missing facts.
6. Rewrite your letter in your own words. Or type `/gtv-lor-polish` to get a copy of your .docx with the changes as tracked edits (new text highlighted, a comment on each), then review them in Word (Review, Accept or Reject) and rewrite the highlighted parts.
7. Add the revision and type `/gtv-lor-evaluate` again to re-score.
8. Sign it (DocuSign or similar), put your CV in the same PDF, and type `/gtv-lor-final` for the last check.

Example: "Score my letter for Yulian's Global Talent application, then show me what to improve."

### You're the applicant, starting from scratch

1. Type `/gtv-lor` and answer "I'm the applicant, planning my letters".
2. Type `/gtv-lor-profile`. It interviews you a few questions at a time: route, criteria, achievements with evidence, recognition, UK plans. Attach your CV or personal statement to save time.
3. Type `/gtv-lor-referees` and list the people you're considering. It checks each one and assigns each letter a different main example.
4. Type `/gtv-lor-write` for each referee. Choose a fact pack (recommended) or a draft for them to rewrite, and send it to them.
5. When each letter comes back, add it with `/gtv-lor` and the referee (or you) runs the recommender steps above.
6. With all 3 letters in, type `/gtv-lor-portfolio` to check they work as a set, then `/gtv-lor-final`.

Example: "Help me plan my 3 Global Talent letters. My referees might be my LSE supervisor, my CEO and a customer."

### Picking up later

Type `/gtv-lor` at any time to see where each letter stands and what to run next. In Claude Code this reads `gtv-lor-workspace/`; on Claude.ai, attach the files the previous chat gave you.

## Rules it checks

Retrieved 2026-10-30 from [GOV.UK](https://www.gov.uk/global-talent-digital-technology/documents-you-need-to-apply-endorsement) and the [Tech Nation guide](https://technation-globaltalentvisa-guide.notion.site/). Check both before relying on them.

## A warning

Tech Nation's guide says using AI tools to create letters of reference is not acceptable, that templated or duplicated letters may be treated as fraudulent, and that it contacts referees. The fact pack is the lower-risk output. Anything this suite writes for a letter is a suggestion the author must read, rewrite in their own words where they wish, and own.

## Layout

```
skills/<name>/SKILL.md    one folder per command, self-contained
shared/references/        rules, rubric, interview, drafting, workspace (source of truth)
shared/scripts/           letter_check.py, polish_docx.py (stdlib only; pdftotext for PDFs)
bin/sync.py               copies shared/ into each skill and builds dist/ zips
install.sh                links the skills into ~/.claude/skills
```

Edit files in `shared/`, then run `python3 bin/sync.py`. `python3 bin/sync.py --check` fails if any copy is stale.

Not legal or immigration advice.
