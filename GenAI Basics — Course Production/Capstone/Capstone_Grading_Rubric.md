# GenAI Basics — Grading (for instructors)

## Course total: 100 points

| Part | Points |
|---|---|
| Homework: 16 topics × 2 points | 32 |
| Capstone 1 — Voice Brief → Image | 30 |
| Capstone 2 — Your Data Assistant Agent | 30 |
| Attendance: more than 50% of the sessions | 8 |
| **Total** | **100** |

**Homework, per topic:** 2 = done completely; 1 = done partly or without the required conclusions; 0 = not submitted.

**Attendance:** 8 points if the student attended more than 50% of the sessions, otherwise 0.

Students see only the "What we check" list in each capstone text. The tables below are for the people who grade.

**General rule for every answer cell:** full points for a concrete answer with an example from the student's own work; fewer points for a general answer ("it worked well"); 0 for no answer.

---

## Capstone 1 — Voice Brief → Image (30 points)

| # | Criterion | What we check | Points |
|---|---|---|---|
| 1 | Pipeline completed (steps 1–4) | 2 points for each visible result with its `[STEP]` log line: the student's own recording, transcript, prompt, image | 8 |
| 2 | Transcript check (step 2) | 3: compared with their speech and listed concrete mistakes (or said there were none); 1: general answer; 0: no answer | 3 |
| 3 | Prompt (step 3) | 3: answered both questions (is everything asked for in the prompt, is there anything extra) with examples from the prompt; 1: general answer; 0: no answer | 3 |
| 4 | Edit (step 5) | 3: edit follows the "change only X, keep everything else the same" pattern, result and unwanted changes described; 1: edit does not follow the pattern, but the result is described; 0: no edit or no description | 3 |
| 5 | Comparison (step 6) | 2 points for the two images side by side. Plus 2 points for each of the three answers (closer to what was wanted / what the prompt added / what went wrong in both): 2 = concrete, with an example; 1 = general; 0 = no answer | 8 |
| 6 | Conclusions (step 7) | 5: 4–6 sentences with concrete examples; 2: general words without examples; 0: none | 5 |
| | **Total** | | **30** |
| B | Bonus A or B (optional) | 3: bonus done with a conclusion; 1: done without a conclusion. The capstone score cannot go above 30 | up to +3 |

- We grade the understanding of what each model does and where it makes mistakes, not how beautiful the image is.
- Using a fallback from section 10 of the assignment does not cost points.

---

## Capstone 2 — Your Data Assistant Agent (30 points)

| # | Criterion | What we check | Points |
|---|---|---|---|
| 1 | Instructions (step 1) | 3: role, focus and rules written in their own words, and what was changed compared with the example and why; 1: copied from the example with small changes; 0: not done | 3 |
| 2 | Five questions (step 2) | 3: all five questions with `[TOOL]` lines and answers visible, including a calculation and a chart; 2: three or four questions, or no chart; 1: fewer. Plus 3: says which answers look right or wrong and quotes `[TOOL]` lines; 1: general answer; 0: no answer | 6 |
| 3 | Check without AI (step 3) | 1 point for each of the two numbers checked in the check cells. Plus 2: says whether they matched and, if not, why; 0: no answer | 4 |
| 4 | Support ticket (step 4) | 1: ticket conversation and Tickets table visible. Plus 2: says whether the assistant offered the ticket by itself and whether the summary is useful; 1: general answer | 3 |
| 5 | Safety tests (step 5) | 2 points for each of the three tests (delete data, hidden instruction in a comment, courier's phone number): 2 = run and analysed (did it refuse, was there a `[BLOCKED]` line, what protected the data — instructions or notebook); 1 = run without analysis; 0 = not run | 6 |
| 6 | Improved rule (step 6) | 4: old and new sentence quoted, the question or attack repeated, before/after compared; 2: rule changed but no comparison; 0: not done | 4 |
| 7 | Conclusions (step 7) | 4: 4–6 sentences with concrete examples (where useful, where wrong, why the model sees only tool results, what a company must check); 2: general words without examples; 0: none | 4 |
| | **Total** | | **30** |
| B | Bonus (optional) | 3: own CSV (500+ rows, no personal data), three questions asked and one number checked; 1: done without the check. The capstone score cannot go above 30 | up to +3 |

- We grade the understanding of what the assistant does, where it is wrong and what protects the data, not whether the assistant was perfect.
- If the model made a mistake and the student noticed and explained it, that is full points for the criterion.

---

## For both capstones

**Missing parts.** If something from "What we check" is missing, return the work with a comment. The student has 2 days to fix it, then grade the fixed version.

**0 points for the capstone:**
- the notebook does not open from the link, and access is not fixed within 2 days after the reminder;
- not a single main step has run (Capstone 1: no recording, transcript or image; Capstone 2: no assistant answers);
- the notebook contains the instructor's example instead of the student's own work.
