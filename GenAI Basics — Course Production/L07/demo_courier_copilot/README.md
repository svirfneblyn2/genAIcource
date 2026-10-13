# Lesson 07 demo kit: the courier-app week

Synthetic data only. No real customers, mail, chats or repositories.

Files
- `sample_repo/` - the Python project: `delivery_fee.py`, `test_delivery_fee.py`, `ISSUE.md`,
  `.github/copilot-instructions.md`, and `expected_solution/` (the 2-line change plus 3 new tests).
- `meeting_notes.md` - paste into Copilot in Teams/Word or free Copilot Chat (slides 05-06).
- `release_checklist.txt` - open on Windows and ask Copilot about it (slide 17).
- `fallback_outputs/` - deterministic results if a Copilot button is missing or the UI changed.

Check before class: `cd sample_repo && python smoke_check.py` (baseline: 4 tests pass).
The real diff and the 7-test output used on slides 11-13 come from `../deck_v2/make_artifacts.py`.

Rule for the demo: judge Copilot by the diff and the tests, not by the word "done".
If a button moved, the rule did not: show the fallback and move on after 90 seconds.
