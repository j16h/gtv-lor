---
name: gtv-lor
description: "All-in-one helper for UK Global Talent visa (Tech Nation, digital technology) letters of recommendation. Asks who you are and for your document, then scores a letter 1 to 5 against the GOV.UK and Tech Nation rules, ranks improvements, polishes a .docx with highlighted tracked changes, interviews the applicant and referees to write a letter or fact pack from scratch, checks the 3 letters as a set, and runs a final check. Use when the user mentions a Global Talent, GTV or Tech Nation recommendation letter or LOR, types /gtv-lor or any gtv-lor skill name, or asks to \"score\", \"improve\", \"polish\", \"write\" or \"check\" such a letter. Do NOT use for other visas or general job references."
metadata:
  author: Julian Kalichman
  version: 3.1.0
  sources-retrieved: 2026-10-30
---

# gtv-lor (all-in-one)

This one upload contains all 9 gtv-lor skills, each as a mode file. Read `references/rules.md` and `references/workspace.md` first.

## Skills

Each skill lives in `modes/`. When the user types the skill name, says its plain word ("evaluate", "polish"), or the flow below reaches it, read that file and follow it. Inside the mode files, "follow `/gtv-lor-<x>`" means read `modes/<x>.md`.

| Skill | Mode file | Use it to |
|---------|-----------|-----------|
| `/gtv-lor-eval` | `modes/eval.md` | Score a letter 1 to 5 |
| `/gtv-lor-improve` | `modes/improve.md` | Ranked changes and a fact pack |
| `/gtv-lor-polish` | `modes/polish.md` | Changes as highlighted tracked edits (.docx) |
| `/gtv-lor-profile` | `modes/profile.md` | Capture the applicant's facts |
| `/gtv-lor-referees` | `modes/referees.md` | Choose and vet referees |
| `/gtv-lor-write` | `modes/write.md` | Fact pack or draft for one author |
| `/gtv-lor-portfolio` | `modes/portfolio.md` | Check the 3 letters together |
| `/gtv-lor-final` | `modes/final.md` | Pre-submission checklist |

## Start (when no skill is named)

1. **Where things stand.** If the user attached files from an earlier chat (`workspace.md`, assessments, fact packs), read them and show progress.
2. **Ask** (a few at a time):
   - Role: recommender with a draft letter / recommender starting from scratch / the applicant planning letters.
   - Route: Exceptional Talent (leader), Exceptional Promise (potential leader, early career), or not sure.
   - The applicant's name as in their passport.
3. **Add the document.** "Attach your letter (a .docx is best: it's the only format I can polish), or paste the text. If the applicant sent you a fact pack or brief, attach that too."
4. **Route.** Show the workflow for their role, mark done steps, and offer to start the next one now.

**Workflow A, improve a draft** (recommender with a letter): evaluate, improve, optionally polish, author rewrites, evaluate again, final.

**Workflow B, from scratch** (applicant, or recommender without a draft): profile, referees (applicant only), write, then Workflow A for each letter, portfolio, final.

## Files in a chat

There is no folder that lasts between chats. Keep the workspace files from `references/workspace.md` in the conversation, and at the end of each step offer every new or changed file (assessment, fact pack, polished .docx, workspace.md) as a download. Tell the user to attach them again when they continue in a new chat.

Scripts are in `scripts/`. If code execution is unavailable, do the checks by reading and say so; for polish, give the edits as a table (current text, suggested text, reason) instead of a .docx.
