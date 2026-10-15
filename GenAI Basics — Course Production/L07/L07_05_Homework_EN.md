# Lesson 07 • Homework: Take a Courier-App Feature Through Three Copilots

**Course:** GenAI Basics  
**Submission:** a public GitHub repository `courier-copilot-week` in your personal account, plus a folder `genai-homeworks/L07/` with the link (see “Submission Checklist”)  
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)  
**Estimated time:** 2–3 hours  
**Code:** a few lines of Python, written with Copilot. You need to read a diff, not to write an algorithm.  
**Tools:** free only (see below). No credit card, no paid plan, no company licence.  
**Matches:** slide 20 (homework) of `presentation_L07_Copilot_Ecosystem_EN_v2.html`, plus slide 18 (six checks = rubric), slide 19 (limits and privacy). Service facts as of 2026-10-13.

---

## Goals

1. Take one small feature of the courier app through the week from the lesson: a meeting’s notes → a brief → an issue → code and tests → a pull request → a release checklist.
2. Use Copilot in all three places: Copilot Chat (documents), GitHub Copilot in VS Code (repository), Copilot in Windows or the free chat (your PC).
3. Judge the result by the **diff and the tests**, not by the word “done”.
4. Keep evidence: three screenshots and a checklist.

Grading is based on the six checks. A change that is small, tested and honestly marked scores higher than a clever one that nobody checked.

---

## The Feature

Choose one:
- **The lesson’s rule:** “Prime subscribers get free delivery from a $75 order inside the city zone; $100 for everyone stays; outside the zone nothing changes.”
- **Your own rule** with a number, for example “rain: +$2 outside the zone for orders under $40”. Your rule **must have a threshold**, so that a boundary exists to test.

Everything is **synthetic**: the courier app, the customers, the numbers.

**Starter files:** copy the folder `demo_courier_copilot/sample_repo/` from the course materials, **without** `expected_solution/`. It contains `delivery_fee.py`, `test_delivery_fee.py` (4 tests), `ISSUE.md` (an example issue) and `.github/copilot-instructions.md`. Write your own `ISSUE.md` text for your rule; edit the instructions file if you like (keep it short).

---

## Privacy: Read Before You Start

- **Synthetic data only.** No real customers, orders, mail, chats, company code or keys, in prompts, files or screenshots.
- **Use a personal GitHub account** for this homework. The repository is public: never put anything private in it.
- **Switch training off before you start** (personal plans: Free, Pro, Pro+, Max): GitHub → Settings → Copilot → “Allow GitHub to use my data for AI model training” → **Disabled**. Since 2026-04-24 it may be on by default. Work accounts (Microsoft 365, GitHub Business and Enterprise) are not used for training, but do not use them for this task anyway.
- **Crop your screenshots:** hide your email, tokens, notifications and other tabs.
- Never paste a password or a key into a chat. If it happens: change the key.

---

## What to Do (6 Steps = 6 Checks)

| Step | Task | Deliverable | Check |
|---|---|---|---|
| **1 Brief** | Take the meeting notes (`demo_courier_copilot/meeting_notes.md` for the lesson’s rule, or write 6–10 lines for your rule). Ask Copilot Chat for a one-page brief **and to list which sentences are its own**. Mark each line: from the notes / added by Copilot. Delete or verify the added ones. | `brief.md` | 1 |
| **2 Issue** | Open an issue in your repo. It must contain the **numbers**, **what must not change**, and **which tests you want**. | issue link in `README.md` | 2 |
| **3 Code** | In VS Code with Copilot: prompt 1, plan without editing; prompt 2, implement. Copy the starter files into the repo first. Look at `git diff`. | `delivery_fee.py` | 3 |
| **4 Tests** | Boundary tests: the value, the value minus 0.01, and a case that is not covered by the rule. Run `python -m unittest -v`: all green. | `test_delivery_fee.py`, green run in a screenshot or CI | 4 |
| **5 Pull request** | Work on a branch, open a pull request that closes the issue. Get a **review comment** (Copilot code review if you have it, otherwise a human: a colleague, or you after a break). **Answer it**, then merge. | merged PR link | 5 |
| **6 Evidence** | Write a release checklist (5–6 items) and mark **one item that would stop the release**. Open it in Notepad and ask Copilot in Windows which item that is; no Copilot key or no Vision? Paste the text into the chat. Add the three screenshots to `README.md`. | `checklist.md`, `README.md` with 3 screenshots | 6 |

**Three screenshots:** (1) the brief with Copilot’s answer, (2) Copilot in the editor (plan or implementation), (3) the pull request with the review comment and the green checks.

---

## Tools (October 2026, free only)

**Free allowances are limited and change often. Verify the current terms before you start.**

| Where | Free tool | Notes |
|---|---|---|
| Brief, notes | **Copilot Chat** (web, Edge or the Windows app) with the notes pasted in | Work Microsoft 365 with Copilot in Word is optional, not required |
| Issue, PR | **github.com** (free account) | Copilot code review on a PR may use paid credits on free plans: a human review comment is accepted |
| Code | **VS Code** + **GitHub Copilot Free** (completion, chat, agent in limited amounts) | Verified students: **Copilot Student** is free. Free chat and agent usage is limited per month; if it runs out, use Copilot Chat on the web and paste the code by hand, and write that in `README.md` |
| Windows | Copilot key or `Win+C`, the Copilot app, Vision | Not available on your device? Paste the checklist text into the free chat |
| Tests | `python -m unittest -v` (Python 3, nothing to install) | CI is optional: a screenshot of the terminal is enough |

**Not needed and not allowed here:** the cloud agent (“Assign to Copilot”, paid; L16), paid plans, real customer data, other people’s code.

---

## Directory Structure for Submission

```
courier-copilot-week/            # public GitHub repository
├── brief.md                     # the brief with the “from notes / added by Copilot” marks
├── delivery_fee.py              # your change, small
├── test_delivery_fee.py         # boundary tests, all green
├── checklist.md                 # release checklist, one stopping item marked
├── README.md                    # 3 screenshots, links to issue and PR, six-check table
└── .github/copilot-instructions.md   # optional: your team rules (5 lines)
```

---

## Template: `brief.md`

```markdown
# Brief: [feature name]

Source: meeting notes of [date]

[One page: what we decided, what stays the same, open questions, owners.]

## Where each line comes from
| Line | From the notes? | Action |
|---|---|---|
| Prime subscribers get free delivery from $75 in the city | yes | kept |
| Expected effect: more repeat orders | no, added by Copilot | deleted |
```

## Template: `checklist.md`

```markdown
# Release checklist: [feature name]

1. Unit tests are green.
2. [Who confirms the number.]
3. [Where the feature flag is on.]
4. [Who updates the support reply.]
5. [What number you compare for 24 hours after release.]
6. [The item that stops the release: "Roll back if ... changes unexpectedly".]  **STOP ITEM**

Copilot answer to "Which item stops the release if ... ?": [quote]
```

## Template: `README.md`

```markdown
# courier-copilot-week

**Student:** [name / EPAM alias]  **Feature:** [the lesson's rule / my rule: ...]
**Issue:** [link]  **Merged pull request:** [link]

## Screenshots
1. Brief: ![brief](img/1_brief.png)
2. Copilot in the editor: ![editor](img/2_editor.png)
3. Pull request: ![pr](img/3_pr.png)

## Six checks
| # | Check | Result | Evidence |
|:-|:---|:-:|:---|
| 1 | The brief marks what is from the notes and what is invented | ✓ / ✗ | brief.md, table “Where each line comes from” |
| 2 | The issue has numbers and what must not change | | issue link |
| 3 | The change is small (≤ 10 lines of logic) | | `git diff --stat`: [+N −M] |
| 4 | Tests are green and check the boundary (value, value − 0.01, not covered) | | screenshot / CI: [N of N] |
| 5 | The review was read and answered | | PR link, comment and reply |
| 6 | Evidence is kept: 3 screenshots + checklist with a stop item | | this file, checklist.md |

## What Copilot got wrong or I changed
[2–4 sentences. Honest notes earn points.]

## Tools used and limits hit
[Which free tools; did a limit run out; what you did instead.]
```

---

## How We Grade (rubric = slide 18, six checks)

| # | Check | Passes if |
|---|---|---|
| 1 | Brief | every line is marked “from the notes” or “added by Copilot”; added lines are deleted or verified |
| 2 | Issue | it states the numbers **and** what must not change, and which tests are wanted |
| 3 | Small change | the diff has ≤ 10 lines of logic (tests do not count); no new dependencies |
| 4 | Tests | cover the boundary (value, value − 0.01, a case outside the rule), all green; shown in a screenshot or CI |
| 5 | Review | the PR has a review comment (Copilot or human) with your reply; the PR is merged |
| 6 | Evidence | 3 screenshots in `README.md`; `checklist.md` names one item that would stop the release |

Completeness (required, not graded separately): all five files present, the repository is public, no real data.

---

## Submission Checklist

1. [ ] Training on your data is switched off in your personal GitHub settings (before you started).
2. [ ] Public repository `courier-copilot-week` has `brief.md`, `delivery_fee.py`, `test_delivery_fee.py`, `checklist.md`, `README.md`.
3. [ ] One pull request is **merged**, and it has a review comment with your answer.
4. [ ] `README.md` has 3 screenshots, the issue and PR links, and the six-check table with evidence.
5. [ ] In your `genai-homeworks` repository: branch `feature/L07-copilot-homework` with `genai-homeworks/L07/README.md` that contains only the link to `courier-copilot-week`, submitted via Pull Request to `main`.
6. [ ] Reviewer `ihar_rubanovich@epam.com` invited as a collaborator to both repositories.
7. [ ] No real customer data, secrets or private code anywhere, including screenshots.
