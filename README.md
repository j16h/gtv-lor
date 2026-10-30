# gtv-lor

An agent skill for letters of recommendation for the UK Global Talent visa, digital technology route (Tech Nation endorsement).

It can:

- **Assess** a letter on a 5-point scale against the GOV.UK and Tech Nation rules, with pass/fail gates and a weighted overall score.
- **Improve** a letter: ranked changes and the projected score once they land.
- **Draft** a letter or a fact pack by interviewing the candidate and the recommender.
- **Check the set** of 3 letters for distinct examples, criteria coverage and textual overlap.
- **Vet recommenders** and run a **final pre-submission check**.

Rules were retrieved on 2026-10-30 from [GOV.UK](https://www.gov.uk/global-talent-digital-technology/documents-you-need-to-apply-endorsement) and the [Tech Nation guide](https://technation-globaltalentvisa-guide.notion.site/). Check both before relying on them.

## Install

Claude Code:

```bash
git clone https://github.com/j16h/gtv-lor.git
ln -s "$PWD/gtv-lor/gtv-lor" ~/.claude/skills/gtv-lor
```

Claude.ai: zip the inner `gtv-lor/` folder and upload it under Settings, Capabilities, Skills.

## Use

Type `/gtv-lor`, or share a letter and mention Global Talent or Tech Nation. Examples:

- "Score Mark's letter, I'm applying for Exceptional Talent."
- "What should change to make this letter strong?"
- "Help me get a letter from my lead investor."

The checker script runs on its own too:

```bash
python3 gtv-lor/scripts/letter_check.py letter1.pdf letter2.pdf letter3.pdf --draft brief.txt
```

## A warning

Tech Nation says templated, duplicated or AI-created letters may be treated as fraudulent, and it contacts referees. Drafts from this skill are starting points the author must rewrite in their own words. The fact pack output is the lower-risk option.

## Layout

```
gtv-lor/
  SKILL.md
  references/  requirements, rubric, interview questions, drafting rules
  scripts/     letter_check.py (stdlib only; pdftotext for PDFs)
```

Not legal or immigration advice.
