<div align="center">
<pre>
                  _              _                        
             __ _| |___   __    | | ___  _ __             
            / _` | __\ \ / /____| |/ _ \| '__|            
           | (_| | |_ \ V /_____| | (_) | |               
            \__, |\__| \_/      |_|\___/|_|               
            |___/                                         
                                                          
 Get your Global Talent visa recommendation letters right.
</pre>
</div>

<p align="center">
  <a href="#install"><b>Install</b></a> |
  <a href="#how-it-works"><b>How it works</b></a> |
  <a href="#skills"><b>Skills</b></a> |
  <a href="#what-you-get"><b>What you get</b></a> |
  <a href="#what-it-checks"><b>What it checks</b></a> |
  <a href="#faq"><b>FAQ</b></a>
</p>

<p align="center">Works in <b>Claude</b>, <b>ChatGPT</b>, <b>Claude Code</b>, <b>Codex</b> and pretty much any other AI assistant.</p>

---

Writing (or asking for) a recommendation letter for the **UK Global Talent visa** is fiddly. There are rules about who can write it, what it has to say and how it has to look, and it's easy to miss one.

**gtv-lor** is a set of 9 AI skills that read a letter, check it against the official GOV.UK and Tech Nation rules, score it out of 5 and tell you what to fix. No letter yet? They interview you and put together what each referee needs to write a great one.

> [!IMPORTANT]
> **Coach, not ghostwriter.** Tech Nation doesn't accept letters written by AI, and they do contact referees to check. gtv-lor shows you what's missing and what to fix, but the words in the letter should be the author's own.

## Install

Pick the assistant you already use and open its steps below. Each one comes with a **prompt you can paste** so your AI does the setup or walks you through it.

| You use | Setup | Time |
|---------|-------|:----:|
| **Claude** (web, desktop, mobile) | Upload one zip | 2 min |
| **ChatGPT** | Open a shared GPT link, or build the GPT once | 1 to 10 min |
| **Claude Code** | One terminal command | 1 min |
| **Codex** | One terminal command | 1 min |
| **Anything else** (Gemini, Copilot...) | Attach one file to a chat | 1 min |

<details>
<summary><b>Claude</b></summary>

Paste this into a Claude chat and it'll walk you through it:

```text
Help me install the gtv-lor skills. Read https://raw.githubusercontent.com/j16h/gtv-lor/main/INSTALL.md and walk me through the Claude steps one at a time.
```

Or do it yourself:

1. Download **[gtv-lor.zip](https://github.com/j16h/gtv-lor/raw/main/downloads/claude-ai/gtv-lor.zip)** and leave it zipped.
2. Go to **Settings → Capabilities** and switch on **Code execution and file creation**.
3. Under **Skills**, click **Upload skill** and pick the zip.
4. Start a new chat, attach your letter and type `/gtv-lor`.

That one upload gives you all 9 skills.

</details>

<details>
<summary><b>ChatGPT</b></summary>

Got a link to the gtv-lor GPT from someone? Just open it, you're done.

Otherwise (you'll need ChatGPT Plus or higher to build it), paste this into a chat:

```text
Help me set up the gtv-lor GPT. Read https://raw.githubusercontent.com/j16h/gtv-lor/main/INSTALL.md and walk me through the ChatGPT steps one at a time.
```

Or do it yourself:

1. Download and unzip **[chatgpt-gpt-kit.zip](https://github.com/j16h/gtv-lor/raw/main/downloads/chatgpt-gpt-kit.zip)**.
2. Go to **Explore GPTs → Create → Configure**.
3. Copy the name, description and starters from `gpt-settings.md`, and paste all of `instructions.md` into **Instructions**.
4. Under **Knowledge**, upload everything in `knowledge/`.
5. Switch on **Code Interpreter & Data Analysis**.
6. Save as **Anyone with the link** and share it with your referees. Free accounts can use it too.

</details>

<details>
<summary><b>Claude Code</b></summary>

Paste this and Claude Code installs it:

```text
Install the gtv-lor skills by following https://raw.githubusercontent.com/j16h/gtv-lor/main/INSTALL.md (Claude Code section).
```

Or run it yourself:

```bash
git clone https://github.com/j16h/gtv-lor.git ~/.gtv-lor
~/.gtv-lor/install.sh              # all 9 skills
~/.gtv-lor/install.sh recommender  # or just the referee path
```

Restart Claude Code and type `/gtv-lor`. Your progress is saved in a `gtv-lor-workspace/` folder, so you can stop and come back.

</details>

<details>
<summary><b>Codex</b></summary>

Paste this and Codex installs it:

```text
Install the gtv-lor skills by following https://raw.githubusercontent.com/j16h/gtv-lor/main/INSTALL.md (Codex section).
```

Or run it yourself:

```bash
git clone https://github.com/j16h/gtv-lor.git ~/.gtv-lor
~/.gtv-lor/install.sh codex              # all 9 skills
~/.gtv-lor/install.sh codex recommender  # or just the referee path
```

Restart Codex and type `$gtv-lor`, or just ask for help with your Global Talent letter.

</details>

<details>
<summary><b>Anything else</b></summary>

Gemini, Copilot, or Claude and ChatGPT with no setup at all:

1. Download **[gtv-lor-prompt.md](https://github.com/j16h/gtv-lor/raw/main/downloads/portable/gtv-lor-prompt.md)**.
2. Attach it to a new chat along with your letter, and say:

```text
Follow the instructions in gtv-lor-prompt.md. I'm a referee with a draft letter.
```

If the assistant can't run code, it checks by reading and gives you suggestions as a list instead of a marked-up Word file.

</details>

## How it works

Start with `/gtv-lor`. It asks who you are and puts you on one of two paths.

<div align="center">
<pre>
                       /gtv-lor                                              
                           |                                                 
                  got a draft letter?                                        
                           |                                                 
       +-------------------+-------------------+                             
       |                                       |                             
       |  yes, I'm a referee                   |  no, or I'm the applicant   
       |                                       |                             
       v                                       v                             
                                                                             
  PATH A: improve a draft                 PATH B: start from scratch         
                                                                             
  [1] eval       score out of 5           [1] profile    tell it your story  
       |                                       |                             
  [2] improve    what to fix              [2] referees   pick 3 people       
       |                                       |                             
  [3] polish     marked-up Word file      [3] write      brief each one      
       |         (optional)                    |                             
  [4] eval       score again              [4] referees write their letters   
       |                                       |                             
  [5] final      last check               [5] each letter goes through path A
                                               |                             
                                          [6] portfolio  check all 3 together
</pre>
</div>

**Path A, you've written a letter for someone:** attach it (Word is best) with anything the applicant sent you. `eval` scores it, `improve` lists what to change (asking for missing facts instead of making them up), `polish` marks up your Word file if you want, you rewrite in your own words, `eval` again, then sign, add your CV to the same PDF and run `final`.

**Path B, you're the applicant or nobody has a draft:** `profile` asks you a few questions at a time (attach your CV to speed it up), `referees` helps pick 3 people and gives each something different to talk about, `write` makes a brief for each one. When letters come back they go through path A, and `portfolio` checks the three work well together.

## Skills

gtv-lor is 9 skills that work together. Run one by typing its name, `/gtv-lor-eval` in Claude and Claude Code or `$gtv-lor-eval` in Codex, or just ask ("score my letter") and the right one kicks in. In ChatGPT and other assistants they all live in one GPT or file, so typing the word ("eval", "polish") works too.

| Skill | What it does | Path |
|-------|--------------|:----:|
| `/gtv-lor` | Start here. Asks who you are, takes your letter, shows where you're at | A B |
| `/gtv-lor-eval` | Scores a letter out of 5, quoting the bits behind each score | A |
| `/gtv-lor-improve` | What to change and why, most important first | A |
| `/gtv-lor-polish` | Marks up your Word file with suggestions to accept or reject | A |
| `/gtv-lor-final` | One last check before you submit | A |
| `/gtv-lor-profile` | Gets the applicant's story down: wins, numbers, UK plans | B |
| `/gtv-lor-referees` | Helps choose referees and splits the topics between them | B |
| `/gtv-lor-write` | A brief for one referee (or a rough draft they rewrite) | B |
| `/gtv-lor-portfolio` | Checks all 3 letters side by side | B |

## What you get

**A score you can act on.** `/gtv-lor-eval` scores 8 things, each backed by a quote from the letter, and flags any must-have you're missing:

<p align="center"><img src="assets/score-card.svg" alt="Example score: 3.5 out of 5, with a dot rating for each of 8 parts and notes on what to fix" width="720"></p>

**Your letter, marked up.** `/gtv-lor-polish` hands back your Word file with every suggestion as a tracked change, plus a comment on each saying why. Your original stays untouched. In Word you just accept, reject or rewrite:

<p align="center"><img src="assets/polish-preview.svg" alt="Example letter with highlighted additions, crossed-out deletions and margin comments" width="720"></p>

**A brief for each referee.** `/gtv-lor-improve` and `/gtv-lor-write` give the author the facts, numbers and rules they need, with no ready-made sentences, so the letter ends up in their voice.

## What it checks

Everything comes from the [GOV.UK page](https://www.gov.uk/global-talent-digital-technology/documents-you-need-to-apply-endorsement) and [Tech Nation's guide](https://technation-globaltalentvisa-guide.notion.site/), as of **30 October 2026**. They do change, so give them a look before you submit.

**The must-haves.** Miss one and the score can't go above 2.

- [ ] The author is an established expert in digital tech
- [ ] They've known the applicant's work for at least 12 months
- [ ] It's written for this application
- [ ] It's dated and signed
- [ ] It's no longer than 3 A4 pages
- [ ] It has the author's phone and email
- [ ] The author's CV is in the same file

**The 8 things it scores**, each out of 5:

| What | Weight |
|------|:------:|
| Achievements in digital tech | x2 |
| Leadership and recognition | x2 |
| Who the author is and how they know the applicant | x1.5 |
| Sounds like a real person (no templates, clichés or em-dashes) | x1.5 |
| Why the UK is good for the applicant | x1 |
| What the applicant will bring to UK tech | x1 |
| Future plans | x1 |
| Claims match the evidence | x1 |

| Overall score | Verdict |
|:-------------:|---------|
| 4.5 to 5 | Strong: send it |
| 3.5 to 4.4 | Good: minor fixes |
| 2.5 to 3.4 | Needs work |
| below 2.5 | Not usable yet |

**Across all 3 letters** it checks that each one has its own main story, together they cover the criteria you're applying under, the authors aren't all your close colleagues, names, dates and numbers line up, and they don't share wording.

## Your data

- **Claude Code and Codex:** everything stays in `gtv-lor-workspace/` on your computer. Add it to `.gitignore` and never push it anywhere public.
- **Claude, ChatGPT and others:** your files are handled by that provider under your account's terms. Chats don't remember each other, so save the files it gives you and attach them next time.
- gtv-lor doesn't send anything anywhere else.

## FAQ

**Can it just write the letter for me?**
It can do a rough draft, but we'd steer you toward the brief instead. Tech Nation doesn't accept AI-written letters and does check with referees, so whatever it drafts, the author needs to rewrite in their own words.

**Do I need a Word file?**
Only for `/gtv-lor-polish`, since that's the one that edits the file. Everything else is happy with Word, PDF, text or a paste.

**Exceptional Talent or Exceptional Promise?**
Either. It asks at the start and checks the letter talks about the applicant the right way for their route.

**How do I pick up where I left off?**
In Claude Code or Codex, run `/gtv-lor` (or `$gtv-lor`) in the same folder. Anywhere else, attach the files it gave you last time and run `/gtv-lor`.

**Is this legal advice?**
Nope. It checks letters against the published guidance. If your situation is tricky, talk to an immigration adviser.

## For maintainers

<details>
<summary>Repo layout and how to update</summary>

<br>

```text
skills/<name>/SKILL.md    one folder per skill, each works on its own
shared/references/        rules, rubric, interview, drafting, workspace: edit these
shared/scripts/           letter_check.py, polish_docx.py (plain Python; pdftotext for PDFs)
platforms/                Claude.ai bundle, ChatGPT instructions, portable header
downloads/                generated: Claude.ai zip, ChatGPT kit, portable prompt
assets/                   README images
bin/sync.py               copies shared/ into each skill, rebuilds dist/ and downloads/
install.sh                links the skills into Claude Code or Codex
INSTALL.md                install steps written for AI agents
```

1. Edit `shared/`, `skills/` or `platforms/`.
2. Run `python3 bin/sync.py`.
3. Commit everything, `downloads/` included. `python3 bin/sync.py --check` tells you if anything's out of date or a skill's frontmatter is invalid.

</details>

---

Not legal or immigration advice. Built to help, not to replace your judgement.
