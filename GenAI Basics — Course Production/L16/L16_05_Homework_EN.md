# Lesson 16 • Homework: one task done by an agent and checked by you

**Course:** GenAI Basics • Module 6 (Idea to Product)
**Submit:** the `genai-homeworks/L16/` folder in your personal GitHub repository
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)
**Time:** 2–3 hours
**Matches:** slide 15 of `presentation_L16_Agentic_Software_Development_EN_v2.html`, slides 6–9 (task, AGENTS.md, permissions, verification) and 13 (rules). Facts as of 16.10.2026.

---

## Pick one of three paths

| Path | What the agent changes | Check |
|---|---|---|
| **A. Starter project (recommended)** | adds a priority filter for tickets in `app.py` — the same example as slides 6 and 14 | `pytest -q`: all 3 tests pass |
| **B. Your own small repository** | fix a bug, add input validation or tests — something that fits in one pull request | your test or build command |
| **C. If you don't code** | a docs-only change to the README, for example a “How to run” section | a screenshot of the README page on GitHub |

### Path C without a terminal (if you don't code)

1. Open your `genai-homeworks` repository on GitHub in the browser.
2. Have a paid plan (ChatGPT Plus or Copilot Pro)? Give the task to a cloud agent — Codex in ChatGPT (web) or Copilot cloud agent: “Add a ‘How to run’ section to the README; change nothing except the README”. The agent creates a branch and a draft pull request by itself.
3. No paid plan? Ask any AI chat to write that section, then on GitHub click ✏️ on README.md, paste the text and choose “Create a new branch and start a pull request” — branch and pull request without a terminal.
4. AGENTS.md for this path has only limits (for example, “change only README.md”), no test commands.
5. Check: open the Files changed tab of the pull request and screenshot the README preview. Write your decision (accept / reject) in AGENT_EVIDENCE.md.

### Starter project (path A)

Create the `genai-homeworks/L16/` folder and put the three files below into it. You need Python 3.10+ and pytest: `pip install pytest`.

`app.py`
```python
TICKETS = [
    {"id": 1, "title": "Cannot log in", "status": "open", "priority": "high"},
    {"id": 2, "title": "Typo on the home page", "status": "open", "priority": "low"},
    {"id": 3, "title": "Export to Excel is slow", "status": "closed", "priority": "medium"},
    {"id": 4, "title": "Payment page error", "status": "open", "priority": "high"},
]


def filter_tickets(tickets, status=None):
    """Return the tickets with the given status (all tickets if status is None)."""
    if status is None:
        return list(tickets)
    return [t for t in tickets if t["status"] == status]
```

`tests/test_filter.py`
```python
from app import TICKETS, filter_tickets


def test_filter_by_status():
    ids = [t["id"] for t in filter_tickets(TICKETS, status="open")]
    assert ids == [1, 2, 4]


def test_no_filter_returns_all():
    assert len(filter_tickets(TICKETS)) == 4


def test_filter_by_priority():
    ids = [t["id"] for t in filter_tickets(TICKETS, priority="high")]
    assert ids == [1, 4]
```

`pytest.ini` (so the tests can find `app.py`)
```ini
[pytest]
pythonpath = .
```

Run `pytest -q` (or `python -m pytest -q`). Before the agent works, the new test fails and the two old ones pass:

```
..F                                                                      [100%]
FAILED tests/test_filter.py::test_filter_by_priority - TypeError: filter_tick...
1 failed, 2 passed
```

That is the “failing test first” from slide 9. The agent's task: make all three tests pass without breaking the old ones. **pytest -q** is the command that runs all tests; a **test** is a small program that checks the code does what it should.

---

## Task

1. **AGENTS.md** (or CLAUDE.md / GEMINI.md if your tool needs it): test and run commands, where the code lives, what not to touch.
2. **TASK.md:** goal, what not to touch, “done when…”, the check command, who decides.
3. **Plan:** run the agent in plan mode (or its equivalent) and paste the plan or a short excerpt of the conversation into `AGENT_EVIDENCE.md` (an “Agent's plan” section).
4. **Edits on a separate branch** (or worktree). Permission mode no looser than auto; no production keys or passwords in the folder.
5. **Check:** run the command from TASK.md yourself and read the diff. Save the command output or a screenshot (`check.png`). On path C the check is a screenshot of the README page.
6. **AGENT_EVIDENCE.md:** which agent and where, the agent's plan and whether you approved it, files changed, commands run and their results, new dependencies, review findings, remaining risks and the decision: **MERGE / REJECT / RETRY**.

A rejected patch with a good explanation of what was wrong and what you changed in the task is also an excellent result.

**Free agents:** Codex in ChatGPT (including the free plan), GitHub Copilot Free, Google Antigravity. **Not allowed:** production keys, confidential company code without permission, the no-checks mode (bypass, or `--yolo`, a flag of some command-line agents that switches off all permission prompts) outside a throwaway container.

```
genai-homeworks/L16/
├─ AGENTS.md
├─ TASK.md
├─ AGENT_EVIDENCE.md      (the agent's plan + your decision)
├─ check.png
└─ app.py, pytest.ini, tests/   (path A only)
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

**Common mistakes:** “make it convenient” instead of a checkable condition; the agent edited everything (for example, rewrote the tests so they pass); “tests passed” with no command output; working directly on main.
