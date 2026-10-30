# Installing gtv-lor (instructions for AI agents)

You're an AI assistant and a user asked you to install or set up **gtv-lor**, a set of skills for UK Global Talent visa recommendation letters. Work out which assistant the user is using, then follow that section. Keep it casual and do one step at a time.

Repo: https://github.com/j16h/gtv-lor

## Which section?

| The user is in | Can you install it yourself? | Section |
|----------------|------------------------------|---------|
| Claude Code (terminal, desktop or IDE) | Yes, you can run commands | [Claude Code](#claude-code) |
| Codex (CLI, IDE or app) | Yes, you can run commands | [Codex](#codex) |
| Claude (claude.ai, desktop or mobile app) | No, the user clicks; you guide | [Claude](#claude) |
| ChatGPT | No, the user clicks; you guide | [ChatGPT](#chatgpt) |
| Anything else | No setup needed | [Any other assistant](#any-other-assistant) |

---

## Claude Code

Run these, then tell the user to restart Claude Code and type `/gtv-lor`.

```bash
if [ -d ~/.gtv-lor/.git ]; then git -C ~/.gtv-lor pull --ff-only; else git clone https://github.com/j16h/gtv-lor.git ~/.gtv-lor; fi
~/.gtv-lor/install.sh
```

- If they only need to improve a letter they've written (a referee), use `~/.gtv-lor/install.sh recommender` instead.
- Check it worked: `ls ~/.claude/skills | grep gtv-lor` should list the skills.
- Updating later is the same two commands.

## Codex

Run these, then tell the user to restart Codex and type `$gtv-lor` (or just ask for help with their Global Talent letter).

```bash
if [ -d ~/.gtv-lor/.git ]; then git -C ~/.gtv-lor pull --ff-only; else git clone https://github.com/j16h/gtv-lor.git ~/.gtv-lor; fi
~/.gtv-lor/install.sh codex
```

- Referees only: `~/.gtv-lor/install.sh codex recommender`.
- Check it worked: `ls ${CODEX_HOME:-~/.codex}/skills | grep gtv-lor`.
- The skills use `python3` for their checks; if it's missing, they fall back to reading the letter.

## Claude

You can't upload skills yourself, so walk the user through it:

1. Download https://github.com/j16h/gtv-lor/raw/main/downloads/claude-ai/gtv-lor.zip and keep it zipped.
2. Open **Settings, Capabilities** and switch on **Code execution and file creation**.
3. On the same page, under **Skills**, click **Upload skill** and pick `gtv-lor.zip`.
4. Start a new chat, attach the letter and type `/gtv-lor`.

On a work or school plan, an admin may need to allow skills or code execution first.

## ChatGPT

You can't create a GPT yourself, so walk the user through it. First ask: did someone send them a GPT link? If yes, they just open it and they're done. If not (they need ChatGPT Plus or higher to build one):

1. Download and unzip https://github.com/j16h/gtv-lor/raw/main/downloads/chatgpt-gpt-kit.zip
2. In ChatGPT, go to **Explore GPTs, Create, Configure**.
3. Copy the name, description and conversation starters from `chatgpt/gpt-settings.md`.
4. Paste all of `chatgpt/instructions.md` into **Instructions**.
5. Under **Knowledge**, upload every file in `chatgpt/knowledge/`.
6. Switch on **Code Interpreter & Data Analysis**.
7. Save, choose **Anyone with the link** if they want to share it, and open the GPT.

## Any other assistant

No install. Tell the user to download https://github.com/j16h/gtv-lor/raw/main/downloads/portable/gtv-lor-prompt.md, attach it to a new chat with their letter, and say: "Follow the instructions in gtv-lor-prompt.md."

## After installing

Tell the user to start with `/gtv-lor` (`$gtv-lor` in Codex). It asks whether they're a referee with a draft or the applicant starting from scratch, takes their letter, and tells them what to run next.
