# Workspace

Every gtv-lor skill reads and writes one folder, so work carries over between skills and sessions.

## Where

- **Claude Code**: `gtv-lor-workspace/` in the current directory. Create it if missing.
- **Claude.ai** (no persistent files): keep the same structure in the conversation, and at the end of each skill offer each new or changed file as a download. Ask the user to attach the files again in a new chat.

## Layout

```
gtv-lor-workspace/
  workspace.md                 who is using it, route, status of each step
  profile.md                   the applicant's facts (from /gtv-lor-profile)
  referees.md                  referees and evidence map (from /gtv-lor-referees)
  letters/
    <author-slug>/             one folder per letter, e.g. jane-smith
      original.docx|.pdf|.md   the author's letter as received, never edited
      factpack.md              facts and rules for the author
      assessment.md            latest score report (from /gtv-lor-eval)
      improvements.md          ranked changes (from /gtv-lor-improve)
      edits.json               edits applied by /gtv-lor-polish
      polished.docx            tracked-changes copy (from /gtv-lor-polish)
      draft.md                 draft for the author to rewrite (from /gtv-lor-write)
  final-check.md               (from /gtv-lor-final)
```

`<author-slug>` is the author's name in lower case with hyphens.

## workspace.md

```
# gtv-lor workspace
Applicant: <name as in passport>
Route: Exceptional Talent | Exceptional Promise | unknown
User role: recommender | applicant
Workflow: improve-a-draft | from-scratch

## Letters
| Author | Status | Score | Updated |
| jane-smith | evaluated | 3.0 | 2026-10-30 |

## Log
- 2026-10-30 /gtv-lor-eval jane-smith: 3.0, Needs work
```

Status values, in order: `received`, `factpack`, `drafted`, `evaluated`, `improved`, `polished`, `final`.

## Rules for every skill

1. Start by reading `workspace.md`. If it is missing, tell the user to run `/gtv-lor` first, or create it by asking the two questions `/gtv-lor` asks (role and route).
2. Never edit `original.*`. Write new files next to it.
3. Update the Letters table and append one Log line before finishing.
4. End by naming the next skill(s) to run.
5. The workspace holds personal data. Never commit it to a public repository; suggest adding `gtv-lor-workspace/` to `.gitignore` if the directory is a git repo.
