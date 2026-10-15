# L09 — Homework: two things of different types

**Goal:** get comfortable in Claude and learn to check what it made.
**You need:** a claude.ai account (the free plan is enough). In Settings → Capabilities, **Artifacts** must be on; for a mini app also **AI-powered artifacts**.

## Task

1. **Thing #1 — a deck or a document** on a work or study topic.
   Example: “Make a 5-slide deck: what my working day looks like / what my project is about / what I learned in this course.”
2. **Thing #2 — a dashboard, diagram or mini app** from your own data.
   - Dashboard: upload a table (CSV or Excel) and ask what matters most in it.
   - Diagram: “draw how the … process works”.
   - Mini app: a coach, a quiz, a flashcard generator.
   **Anonymise** the data before uploading: replace names, emails, phone numbers, contract numbers.
3. **Check each thing** with three questions:
   - Are the numbers and facts right? (compare with the source)
   - What did Claude make up? (ask it: “what did you invent?”)
   - Is there any personal data inside?
4. **One precise fix.** Pick what you didn’t like and ask for a specific change: *what’s wrong → what to change → what to keep*. Not “make it better”.

## What you hand in

```
genai-homeworks/L09/
├── prompts.md      # your 2 prompts + the fix
├── check.md        # answers to the 3 check questions for each thing
└── links.txt       # 2 links (only if there is no personal data inside) or screenshots/
```

## Grading

| Criterion | Good | Needs work |
|---|---|---|
| Two things of different types | both present | one, or both of the same type |
| Check | found at least one inaccuracy or invention | “all perfect” with no explanation |
| Fix | one, specific | “make it better” |
| Safety | data anonymised, link shared deliberately | personal data in the artifact or behind the link |

## Extra (optional)

Create a **project** for your topic: upload 1–2 files and write instructions (like the lesson’s demo project, `demo_assets/prompts_en.md`). Make one of the two things inside it and describe what changed compared with a normal chat.
