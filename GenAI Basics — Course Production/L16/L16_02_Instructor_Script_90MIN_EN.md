# Instructor Script • Lesson 16: Agentic Software Development — Coding Agents, IDEs and CLIs (90 Minutes)

**Course:** GenAI Basics • Module 6 (Idea to Product) • Lesson 16 of 16 (the last)
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles; some students are not programmers. Explain terms (diff, branch, test) as you go.
**Format:** 16 slides (`presentation_L16_Agentic_Software_Development_EN_v2.html` / PDF) • **Microsoft Teams** • break on slide 12
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v2/build.py`; this script is generated from it (`deck_v2/make_docs.py`).
**Facts:** as of 16.10.2026, sources and verification status in `L16_08_Source_Notes_Research_2026-10.md`.

> **Before class:** recheck prices and plan names (slide 4) and Claude Code’s default mode (slide 8): they change every month.

**Lesson objective:** students understand how a coding agent differs from a chat, know the tools’ price bands, can give an agent a checkable task (TASK.md) and write AGENTS.md, choose a permission mode, check the result with a test and the diff, know real incidents and the six safe-work rules.

---

## Timing (16 slides • 90 minutes incl. a 5-minute break)

| Slide | Title | Time | Min |
|---|---|---|---|
| **01** | Agentic software development | 00:00–02:00 | 2 |
| **02** | A chat gives you code to carry over; an agent edits the project and runs the checks itself | 02:00–05:00 | 3 |
| **03** | A coding agent is a model with hands: it reads, edits, runs and connects tools | 05:00–11:00 | 6 |
| **04** | You can try for free; daily use is $10–30; heavy use starts at $100 | 11:00–17:00 | 6 |
| **05** | Plan → act → verify → review: the agent turns the loop, you steer | 17:00–23:00 | 6 |
| **06** | A good agent task says what to do, what not to touch and how to check it is done | 23:00–29:00 | 6 |
| **07** | AGENTS.md is a short project memo the agent reads at the start of every session | 29:00–34:00 | 5 |
| **08** | The permission mode decides what the agent does on its own and what needs your OK | 34:00–40:00 | 6 |
| **09** | “If you can’t verify it, don’t ship it”: give the agent a check it can run itself | 40:00–45:00 | 5 |
| **10** | Experienced developers felt 20% faster with AI — the measurement showed 19% slower | 45:00–52:00 | 7 |
| **11** | An agent does whatever it can reach: keys, databases and other people’s text in the project | 52:00–59:00 | 7 |
| **12** | 5 minutes: which small task in your project would you give an agent? | 59:00–64:00 | 5 |
| **13** | Six rules that sharply cut the risk of such incidents | 64:00–71:00 | 7 |
| **14** | Turn a vague request into a task an agent can carry out and check | 71:00–81:00 | 10 |
| **15** | Homework: one small task done by an agent and checked by you | 81:00–86:00 | 5 |
| **16** | The agent does the work; the task, the check and the decision stay with us | 86:00–90:00 | 4 |

Part 1 (slides 01–11, 00:00–59:00): chat vs agent, agent anatomy, prices, the work loop, the task, AGENTS.md, permissions, verification, METR, incidents. Break (slide 12, 59:00–64:00). Part 2 (slides 13–16, 64:00–90:00): safe-work rules, practice, homework, course summary.

---

### Slide 01 (00:00–02:00) • Agentic software development

**On screen:** Lesson title; on the right a terminal window and a git branch.

#### Speaker (2 min)
> The last lesson of the course. We went from a prompt in a chat to our own assistants and prototypes. Today: agents that write and run code in your project themselves. The main idea: the agent does the work, but the task, the check and the merge decision stay with a human.

---

### Slide 02 (02:00–05:00) • A chat gives you code to carry over; an agent edits the project and runs the checks itself

**On screen:** Two 4-step chains: chat (you carry the code) and agent (edits and checks itself).

#### Speaker (3 min)
> In a chat we ask for code, copy it, run it ourselves and bring the error back. A coding agent works right in the project folder: it reads files, makes edits, runs commands and tests, and fixes what failed. Two things are left to us: setting the task well and checking the result.
>
> In the Stack Overflow 2026 survey, coding assistants and agents are the most common AI use case among developers: 66%. This is no longer exotic but an ordinary work tool.

---

### Slide 03 (05:00–11:00) • A coding agent is a model with hands: it reads, edits, runs and connects tools

**On screen:** Agent diagram: model + read, edit, commands, MCP; AGENTS.md on the left, permissions on the right.

#### Speaker (6 min)
> Inside the agent is the same model as in a chat. The difference is the tools: the agent can read files, edit them, run commands in the terminal and connect to outside systems via MCP, which we covered in L12. On the left of the diagram is the project rules file, AGENTS.md or CLAUDE.md: the agent reads it at the start of every session. On the right are permissions: what the agent may do on its own and what it asks you about.
>
> Two more words you will hear. A skill is a folder with a SKILL.md file describing a ready-made procedure, for example “how we do a release”. A subagent is a helper with its own context, for example a second agent that reviews the first one’s work with fresh eyes.

---

### Slide 04 (11:00–17:00) • You can try for free; daily use is $10–30; heavy use starts at $100

**On screen:** Three price bands: $0, $10–30, $100+; a “start free” plaque.

#### Speaker (6 min)
> The market changes every month, so remember three price bands, not prices. Free: GitHub Copilot Free with a limited agent, Codex now even in free ChatGPT, for quick tasks, Google Antigravity with basic limits, and free tiers of Cursor, Amazon’s Kiro and JetBrains’ Junie. About 20 dollars: Copilot Pro at 10, Claude Code in the Claude Pro subscription, Codex in ChatGPT Plus, Devin and Kiro at 20, Cursor Premium at 30.
>
> From 100 dollars is for people who run several agents at once: Claude Max, ChatGPT Pro, Copilot Max, the top Cursor and Devin plans. A lot was renamed in 2026: Windsurf became Devin Desktop, free Gemini CLI users were moved to the Antigravity CLI, and Copilot’s agent is now called the cloud agent. Claude Code has no free tier. Check the current price on the site before buying.

---

### Slide 05 (17:00–23:00) • Plan → act → verify → review: the agent turns the loop, you steer

**On screen:** The plan → act → verify → review loop (HTML), “you steer” in the centre.

#### Speaker (6 min)
> This is the key slide of the lesson. Working with an agent is a loop of four steps. Plan: in plan mode the agent only reads the project and proposes what it will do; it cannot edit files until you approve. Act: the agent makes edits, preferably on a separate git branch. Verify: the agent runs tests or a build and fixes what failed.
>
> Review: you read the changes — the diff, a before-and-after list — and decide whether to accept. The Claude Code docs recommend exactly this order: explore, plan, code, commit. You may skip the plan only if the change fits in one sentence.

---

### Slide 06 (23:00–29:00) • A good agent task says what to do, what not to touch and how to check it is done

**On screen:** A vague request → TASK.md with a goal, limits and a check command.

#### Speaker (6 min)
> The most common beginner mistake is a vague request. The agent will carry out “add a filter”, but it will decide where it goes, what else to change on the way and when to stop. On the right is the same request as a task: the goal, what not to touch, when it counts as done, which command checks it and who makes the decision.
>
> The “Done when” line is the most important one. If the agent can run the check itself, it will keep fixing errors until the check passes. Advice from the docs: small tasks, specific files, /clear between tasks; after two failed corrections it is better to start over with a clearer task. pytest -q is the command that runs all tests; a test is a small program that checks the code does what it should.

---

### Slide 07 (29:00–34:00) • AGENTS.md is a short project memo the agent reads at the start of every session

**On screen:** An AGENTS.md example; 60,000+ projects; which agents read it.

#### Speaker (5 min)
> Every new conversation starts from a blank page for the agent. So as not to explain the project again, we put an AGENTS.md file in the root: which commands run the tests and the app, where the code lives, what not to touch. It is an open format used by over 60 thousand open-source projects, and almost every agent reads it. Claude Code reads its own CLAUDE.md, or AGENTS.md if there is none. The /init command drafts such a file: CLAUDE.md in Claude Code, AGENTS.md in Codex.
>
> Important: this file is advice, not a lock. The agent can break it. What must always happen is done with hooks — scripts that run automatically, for example formatting after every edit or blocking writes to a folder. And the other way round: an AGENTS.md from someone else’s repository is someone else’s text commanding your agent; read it like unverified code.

---

### Slide 08 (34:00–40:00) • The permission mode decides what the agent does on its own and what needs your OK

**On screen:** Claude Code screenshot: auto mode is the default; 93% and ~17%; a scale of five modes.

#### Speaker (6 min)
> On the left is the real Claude Code permissions menu (claude.ai/code, 16.10.2026): Auto, Accept edits, Plan, with Auto ticked by default. In October 2026 Claude Code announced that auto mode became the default in the terminal and VS Code. In it, reading and editing files in the project folder just happens, while commands and network access are first checked by a separate model: safe ones run, risky ones are blocked. Below is the scale of modes. Plan: the agent reads files and runs commands only to explore the project, writes a plan and edits nothing. Manual: the agent asks before every edit and command. AcceptEdits: it edits files and runs simple file commands in the project folder itself — make a folder, move, copy or delete a file (mkdir, mv, cp, rm); it asks before other commands. Auto: a checker model decides. Bypass: no checks at all, only in a throwaway container or virtual machine. A throwaway container is a temporary isolated “computer inside your computer” that you delete afterwards.
>
> Why auto? Anthropic counted that people approve 93% of prompts — after the tenth question nobody reads. But the auto check is not perfect either: it misses about 17% of overeager risky actions. So the mode does not replace review. Codex has the same idea under other names: read-only, workspace-write and danger-full-access sandboxes. Deny rules, for example on rm -rf or git push, apply in every mode.

---

### Slide 09 (40:00–45:00) • “If you can’t verify it, don’t ship it”: give the agent a check it can run itself

**On screen:** Real pytest output on the homework starter (1 failed → 3 passed) and 4 steps: a test fails → the agent fixes → all green → you read the diff; undo and git.

#### Speaker (5 min)
> A line from the Claude Code docs: if you can’t verify it, don’t ship it. The most reliable approach is a failing test first, then the fix. On the left is a real run on the homework starter project: the new priority-filter test fails, the two old ones pass; the agent edits app.py and all three tests are green. The agent runs the test itself and edits the code until everything is green. If there are no tests, the check can be a build, a linter or a screenshot of the page. But a test does not see everything, so the last step is you reading the diff.
>
> On undo. Agents have their own back buttons; in Claude Code it is Esc Esc or /rewind. They revert file edits, but not what the agent did with terminal commands: a deleted database does not come back that way. The real safety net is git: every task on its own branch or in a separate working copy (worktree), so parallel agents do not get in each other’s way.

---

### Slide 10 (45:00–52:00) • Experienced developers felt 20% faster with AI — the measurement showed 19% slower

**On screen:** METR bars: expected +24%, felt +20%, measured −19%.

#### Speaker (7 min)
> The most honest study on this topic. In 2025 the METR organisation took 16 experienced open-source developers and 246 real tasks from their own projects. Each task was randomly assigned: AI allowed or not allowed. Before starting, participants expected a 24% speedup; afterwards they were sure they had been 20% faster. The measurement showed they were 19% slower with AI.
>
> In February 2026 METR repeated the study with newer tools: estimates moved towards a speedup, but nothing is statistically proven — developers were already refusing to work without AI, and the data became unreliable. One more figure, from a different survey — Stack Overflow 2025: 66% of developers said their top frustration is code that is “almost right, but not quite”. The takeaway for you: don’t trust the feeling; time yourself on your own tasks. The same goes for agent benchmarks such as SWE-bench: numbers from announcements age fast and depend on the agent app around the model, so test on your own task.

---

### Slide 11 (52:00–59:00) • An agent does whatever it can reach: keys, databases and other people’s text in the project

**On screen:** Three cases: 9 seconds (PocketOS), code freeze (Replit), 2,349 secrets (Nx); Clinejection.

#### Speaker (7 min)
> Three cases. PocketOS, April 2026: an agent in Cursor found a long-lived cloud key in an unrelated file and, with a single command, deleted the production database and its backups in nine seconds; the service was down for about 30 hours, and the data was later restored. Replit, July 2025: during a declared code freeze the agent deleted SaaStr’s production database — about 1,200 executives and 1,190 companies — and at first reported that a rollback was impossible.
>
> Nx, August 2025, a supply-chain attack: an infected version of a popular npm package, on install, looked for AI agents on the computer — Claude, Gemini, Amazon Q — and asked them to find secret files with permission prompts switched off; many agents refused, but the malware stole keys on its own too. About 2,349 secrets leaked. And in 2026, in the Clinejection case, the command was hidden right in a GitHub issue title: the AI bot that triaged Cline’s issues ran it, the attacker got to the publishing keys, and an infected version went out on npm. The takeaway: everything the agent can reach is its permission, and someone else’s text in the project is someone else’s commands.

---

### Slide 12 (59:00–64:00) • 5 minutes: which small task in your project would you give an agent?

**On screen:** A 5-minute break timer.

#### Speaker (5 min)
> Press “Start”.

---

### Slide 13 (64:00–71:00) • Six rules that sharply cut the risk of such incidents

**On screen:** Six safe-work rules tagged with incidents; a plaque on the no-checks mode.

#### Speaker (7 min)
> Six rules. One: each task on its own branch or worktree, so any result can be thrown away. Two: no production keys or passwords near the agent — not in the project, not in .env. That closes PocketOS. Three: a sandbox and least privilege, plus explicit denials of dangerous commands. Four: READMEs, issues, foreign AGENTS.md files, third-party skills and MCP servers are someone else’s text that can command the agent; install them only from trusted sources.
>
> Five: a human reads every change, ideally with fresh eyes — a second session or a reviewer agent. Six: only a human merges and ships. That is how Copilot’s cloud agent works: it opens only a draft pull request, cannot approve it, and the person who asked cannot approve their own agent’s PR. The no-checks mode belongs only in a throwaway container. A throwaway container is a temporary isolated “computer inside your computer” that you delete afterwards. --yolo is a start-up flag of some command-line agents that switches off all permission prompts; bypass in Claude Code and danger-full-access in Codex are the same thing.

---

### Slide 14 (71:00–81:00) • Turn a vague request into a task an agent can carry out and check

**On screen:** The “priority filter” request and 4 steps: TASK.md, AGENTS.md, plan, decision.

#### Speaker (10 min)
> Work individually for 7 minutes, then a 3-minute walk-through. A business request: “users want to filter tickets by priority”. Step 1: write TASK.md — the goal, what not to touch, when it is done, which command checks it. Step 2: a three-to-five-line AGENTS.md — the test command and limits. Step 3: if you have an agent, run it in plan mode and read the plan without approving anything. Step 4: decide whether to accept the plan, reject it or refine the task.
>
> Walk-through: show two or three TASK.md files in the shared chat. Look for a concrete “done when” line with a command and explicit “do not touch” limits. The typical mistake is “make it convenient” instead of a checkable condition.

---

### Slide 15 (81:00–86:00) • Homework: one small task done by an agent and checked by you

**On screen:** Six homework steps (starter project or own repo), the genai-homeworks/L16/ folder, a path for non-coders (README only).

#### Speaker (5 min)
> Homework: the same loop on a real but small project. The easiest is the starter project in L16_05_Homework: app.py with a filter_tickets function and tests, run with pytest -q; the task is the same priority filter. Your own small repository works too. If you don’t code: a docs-only change to the README, and the check is a screenshot of the page. You need AGENTS.md, TASK.md, edits on a separate branch, your own run of the check, and an AGENT_EVIDENCE.md file with the agent’s plan and your decision: accept, reject or retry. A rejected patch with a good explanation is also an excellent result. Details in L16_05_Homework.

---

### Slide 16 (86:00–90:00) • The agent does the work; the task, the check and the decision stay with us

**On screen:** The four rules of the lesson and the end of the course.

#### Speaker (4 min)
> Four rules for working with an agent. A task with a clear “done when”. Plan first, then edits. Least privilege: a branch, a sandbox, no production keys. The decision belongs to a human: they read the changes, merge and ship. This is the last lesson: we went from the first prompt to an agent that writes code under your supervision. Thank you, and good luck with your final projects.

---
