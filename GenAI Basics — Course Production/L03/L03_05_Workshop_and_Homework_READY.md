# Lecture 03 — Workshop and Homework

Build a typed intake router with evidence, ambiguity handling and local tests

GenAI Basics  •  Module 03  •  Refreshed 2026-09-14

# Student mission

Build a small Python artifact that converts one kind of unstructured intake text into a typed Pydantic object that another component could consume. The artifact must make uncertainty visible rather than hiding it.

# Choose one domain

- Bug report triage
- Product feedback intake
- Event request intake
- Simple internal service request
# Required student artifact

# In-class steps (9 minutes in the full path)

- Define the downstream decision first: what will another program do with this object?
- Choose 3–5 fields. Add one field that explicitly represents uncertainty/review.
- Write the clear and ambiguous example before calling the model.
- Run local Pydantic validation against one valid and one invalid fixture.
- If time allows, call the model for the clear example and compare the typed result with your expected fields.
# Homework extension

- Complete the live structured-output call and keep the model value in environment/config.
- Add at least three deterministic contract tests.
- Add one business validation outside the model (for example, allowed customer ID, date range, threshold or supported country).
- Log model, request ID, elapsed time and usage for the live call. Do not log secrets.
- Write 100–150 words: what does your schema guarantee, and what does it not guarantee?
- Optional: add a separate streamed human-facing explanation, but do not use the stream as the machine-readable contract.
# Rubric — 10 points

# Expected learning outcome

A useful submission is not a flashy chatbot. It is a small repository another engineer can inspect and say: “I know the expected shape, I know what happens on ambiguity, I can run the local checks, and I know what evidence exists when the remote call fails.”


| File | Minimum content |
| --- | --- |
| contracts.py | One Pydantic model with at least one Literal enum, one bounded text field and needs_human_review: bool. |
| examples/clear.txt | A clear input with an expected classification. |
| examples/ambiguous.txt | An input where a human should review before automation. |
| classify.py | Responses API structured-output call, model configured outside source code. |
| tests/test_contract.py | Local deterministic tests for invalid enum/value/length cases. |
| README.md | Setup, contract explanation, ambiguity policy and safe fallback. |
| EVIDENCE.md | One successful example or prepared expected result; one telemetry sample without secrets. |


| Criterion | Points | Evidence |
| --- | --- | --- |
| Contract quality | 2 | Fields/types/enums are appropriate and bounded. |
| Ambiguity handling | 2 | Ambiguous example is realistic and routes to review rather than forced certainty. |
| Deterministic tests | 2 | At least three local validation cases; invalid data is rejected. |
| API boundary | 2 | Structured call is isolated, model is configurable, secret is not in source. |
| Operational evidence | 1 | Request ID/latency/usage recorded safely. |
| Explanation | 1 | Student clearly separates schema, semantic and business validity. |
