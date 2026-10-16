# Lesson 16 • Homework: one task done by an agent and checked by you

**Course:** GenAI Basics • Module 4 (Idea to Product)
**Submit:** the `genai-homeworks/L16/` folder in your personal GitHub repository
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)
**Time:** 2–3 hours
**Matches:** slide 15 of `presentation_L16_Agentic_Software_Development_EN_v2.html`, slides 6–9 (task, AGENTS.md, permissions, verification) and 13 (rules). Facts as of 16.10.2026.

---

## Task

Pick a **small** repository you are allowed to change: your own, a practice one or your L14 prototype. The change must fit in one pull request: fix a bug, add input validation, tests or docs.

1. **AGENTS.md** (or CLAUDE.md / GEMINI.md if your tool needs it): test and run commands, where the code lives, what not to touch.
2. **TASK.md:** goal, what not to touch, “done when…”, the check command, who decides.
3. **Plan:** run the agent in plan mode (or its equivalent) and save the plan or a short excerpt of the conversation.
4. **Edits on a separate branch** (or worktree). Permission mode no looser than auto; no production keys or passwords in the folder.
5. **Check:** run the command from TASK.md yourself and read the diff. Save the command output or a screenshot (`check.png`).
6. **AGENT_EVIDENCE.md:** which agent and where, whether you approved the plan, files changed, commands run and their results, new dependencies, review findings, remaining risks and the decision: **MERGE / REJECT / RETRY**.

A rejected patch with a good explanation of what was wrong and what you changed in the task is also an excellent result.

**Free agents:** Codex in ChatGPT (including the free plan), GitHub Copilot Free, Google Antigravity. **Not allowed:** production keys, confidential company code without permission, the no-checks mode (bypass, --yolo) outside a throwaway container.

```
L16_homework/
├─ AGENTS.md
├─ TASK.md
├─ AGENT_EVIDENCE.md
└─ check.png
```

---

## Grading (10 points)

| Criterion | Points |
|---|---|
| TASK.md: a checkable “done when” and limits | 3 |
| AGENTS.md: concrete commands and limits | 2 |
| Small change, on a separate branch, no unrelated edits | 2 |
| You ran the check; output or screenshot attached | 2 |
| A decision with reasons and remaining risks | 1 |

**Common mistakes:** “make it convenient” instead of a checkable condition; the agent edited everything; “tests passed” with no command output; working directly on main.
