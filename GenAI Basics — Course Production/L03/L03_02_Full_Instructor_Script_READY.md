# Lecture 03 — Full Instructor Script

116-minute delivery path with a 90-minute compression path

GenAI Basics  •  Module 03  •  Refreshed 2026-09-14

# Delivery map

# 0–10 min — Hook: chat answer vs software contract

Instructor says: “A chat answer can be a little messy and still be useful, because a person is sitting there. Software is less forgiving. If the next line of code expects category=bug and it gets a beautiful paragraph, the model may have answered the human question while the application still failed.”

Show a short support-ticket paragraph next to a typed object with category, priority, summary and needs_human_review. Do not explain structured outputs yet. Ask: “Which one can a routing service consume without guessing?” Take two or three answers.

Instructor says: “That is today’s problem. We are not learning how to chat from Python. We are learning how to put a probabilistic model behind an engineering boundary that downstream code can trust enough to use.”

Ask: “What can go wrong even if the text is grammatically perfect?” Guide answers toward wrong field values, missing fields, ambiguity, timeout, quota, secret leakage and no evidence for debugging. Write only keywords, not a long list.

Transition: “We will build the boundary in layers: request, stream, schema, validation, failure policy and evidence.”

# 10–26 min — Environment, secrets and the first request

Open the repository. Start with .gitignore and .env.example before opening any API code.

Instructor says: “The first GenAI engineering skill today is not prompting. It is not leaking a credential. A demo key in a screenshot is still a leaked key.”

Point out that .env is ignored and .env.example contains placeholders only. Explain that the model value is also configuration because model availability and names can change. Run `python 00_preflight.py`. It should print Python/package versions, model value and whether a key is present, but it must not call the network.

Run `python tests/test_contract.py` next. Say: “This test proves that the local application contract works before we pay for or depend on a remote call. It cannot prove model quality. It proves that our deterministic boundary behaves deterministically.”

Open 01_first_call.py. Read it top to bottom. Do not spend time on import syntax. Point at `OpenAI(timeout=20.0, max_retries=2)` and say: “We make two operational choices visible immediately: a deadline and a bounded retry policy.”

Before running, ask: “Where will the model execute?” Wait for “remote service / cloud API”. Then run the script. If it succeeds, show output_text, request_id and usage. If the environment has no working key/model access, use the prepared expected output and continue; do not troubleshoot credentials live for more than two minutes.

Instructor says: “A minimal useful call is not just prompt in, text out. It has a model choice, stable instructions, task input, a deadline and evidence.”

# 26–40 min — Request and response anatomy

Move to the architecture slide. Trace with the pointer: Python application → SDK → HTTPS → Responses API → model → typed response. Then trace back.

Instructor says: “The SDK is not the AI. It is a typed client. That distinction matters because failures can happen before the model runs, while it runs, or after we receive content that our application refuses to accept.”

Ask students to name one responsibility that belongs to the application rather than the SDK. Good answers: task definition, schema, timeout budget, business validation, logging policy, side effects.

Open the request code. Point out model, instructions and input. Say: “Treat instructions as stable task policy and input as the current work item. That is a useful design separation even when the API lets you express richer content.”

Now show output_text, usage and `_request_id`. Instructor says: “If a user tells you ‘the AI failed at 14:03’, that is not enough to debug. A request ID plus your own correlation ID gives you an operational trail.”

Mini-check: ask “Should we log every prompt in plaintext?” Expected answer: no; logging content can create security/privacy problems. Log enough metadata to operate the system, and handle sensitive payload logging explicitly.

# 40–55 min — Streaming: transport behavior, not extra intelligence

Open 02_stream.py. Ask students to predict what changes when `stream=True`. Do not accept “it becomes faster” without qualification.

Instructor says: “The request still has to be generated. Streaming changes when the client can see parts of the output. The user may see the first text earlier even if total generation time and token usage are similar.”

Run the script and point at successive `response.output_text.delta` events. On the slide, animate the conceptual sequence verbally: request accepted, first delta, more deltas, terminal completion.

Ask: “Where is streaming valuable?” Collect: chat UI, CLI assistants, live summaries, progressive rendering. Then ask: “Where can it be dangerous?” Look for prematurely acting on incomplete content, broken partial UI state, treating partial output as a completed record.

Instructor says: “A partial stream is display state. It is not automatically a valid final business object.”

If live streaming fails, use the runbook’s pre-recorded expected event sequence. The learning point is the event contract, not watching letters appear.

# 55–79 min — Structured output and validation

Show `sample_ticket.txt` before code. Ask the class: “If another service must route this ticket, what fields would you require?” Gather four fields and reveal the prepared Pydantic model.

Walk through each field: category and priority use Literal values, summary has a maximum length, and needs_human_review is the escape hatch for ambiguity. Explain that an ambiguity flag is often more valuable than pretending every input belongs cleanly in one class.

Open 03_structured.py. Instructor says: “Notice the change. We are no longer asking politely for JSON and then hoping. We pass the schema through `text_format`, and the SDK returns a parsed typed result.”

Run the clear ticket. Print the typed object. Then switch to `sample_ticket_ambiguous.txt`. Before running, ask which field is likely to be uncertain and why the correct behavior may be review=true rather than forced automation.

Draw three validation layers on the board or use the slide: schema, semantic, business/action. Say: “Pydantic can reject priority=urgent if urgent is not allowed. It cannot prove that the model chose high rather than medium for the right reason. And even a semantically correct classification may still require a human before a consequential action.”

Ask students for one validation rule outside the model. Examples: customer ID must exist, release date must be in the future, amount must be below an approval threshold, country must be in supported markets.

Instructor says: “Structured output solves the shape problem. It does not solve truth, policy or accountability.”

# 79–96 min — Failures, bounded retries and observability

Open 04_observability.py. Present the failure taxonomy one row at a time: timeout, connection, rate limit, other status error, validation failure.

Instructor says: “Retry is not a synonym for error handling. A retry only makes sense when the failure is plausibly transient, the operation is safe to repeat, and the latency budget can afford another attempt.”

Explain that the current SDK retries selected transient failures by default; this demo sets max_retries=2 explicitly so the policy is visible. Avoid teaching the default count as a universal rule. It is an implementation detail to re-check.

Show the telemetry dictionary: model, request ID, elapsed milliseconds, usage. Ask: “What is missing if this is a multi-request web application?” Expected: application request/correlation ID, user/session or tenant context where appropriate, success/failure category, perhaps feature/version—without secrets or unnecessary sensitive content.

Failure exercise: ask students to choose a response for each scenario. (1) DNS/network interruption: connection category. (2) quota/rate limit: backoff/reduce concurrency. (3) invalid request/model: fix configuration; retrying the same bad request is pointless. (4) schema valid but wrong category: domain evaluation/business review, not transport retry.

# 96–104 min — Model choice, usage and cost without memorizing a price card

Show the conceptual model-choice slide. Say: “As of today, the official OpenAI model pages position different GPT-5.6 variants for different quality/cost points. That is a delivery-day fact, not a timeless lesson.”

Instructor says: “The durable rule is: choose the cheapest model that reliably clears your quality bar for the task, and verify required feature support. Then measure usage and latency. Do not choose by model prestige.”

Point at response.usage. Explain input versus output usage and that generated verbosity can be expensive. Do not put a detailed price table in the core deck; keep volatile pricing in source notes.

# 104–113 min — Active workshop: build a typed router

Pair students. Give each pair one input type: bug report, product feedback or event request. The artifact must include: a Pydantic schema with at least one enum, one bounded text field and a `needs_human_review` boolean; one clear example; one ambiguous example; a local validation test; and a README explaining when the application refuses automation.

Instructor says: “Your goal is not the cleverest schema. Your goal is a contract a teammate could review.”

At minute 109, stop coding. Ask each pair to show one ambiguity that should force review=true. Select one example to discuss. If nobody has a good ambiguity, use “export format changed; not sure if bug or intended; finance needs it tomorrow.”

# 113–116 min — Debrief and close

Ask three fast questions: “What does streaming change?” “What does structured output guarantee?” “What evidence would you log for an API call?”

Instructor closes: “The smallest useful GenAI application boundary is now visible: secret and config → request → streamed or typed response → validation → evidence → only then a side effect. That pattern survives model changes.”

Assign homework: complete the router artifact, add one failure test, capture a sample telemetry line, and write three sentences explaining the difference between schema validity and business validity. Next module reuses the same API habits for image generation and editing.

# 90-minute compression path

# Likely student questions and concise answers


| Block | Time | Purpose |
| --- | --- | --- |
| Hook: prose vs contract | 0–10 | Make the reliability problem concrete. |
| Setup + first call | 10–26 | Secret hygiene, environment, minimal Responses call. |
| Request/response anatomy | 26–40 | Make the remote API boundary visible. |
| Streaming | 40–55 | Event flow and latency semantics. |
| Structured output | 55–79 | Typed extraction + three-level validation. |
| Failures + observability | 79–96 | Timeouts, retries, request IDs, usage. |
| Model/cost decisions | 96–104 | Configuration, measurement, volatile facts. |
| Active workshop | 104–113 | Student builds a schema contract. |
| Debrief + close | 113–116 | Consolidate the boundary and hand off homework. |


| Keep | Compress / move |
| --- | --- |
| 0–8 hook | Use one example; no extended discussion. |
| 8–20 setup + first call | Run preflight + one live request only. |
| 20–31 architecture | Skip debugger/raw response exploration. |
| 31–42 streaming | One run + one misconception check. |
| 42–62 structured output | Keep clear + ambiguous ticket and three validation layers. |
| 62–74 failure policy | Use taxonomy matrix; move detailed scenarios to homework. |
| 74–80 model/usage | One conceptual slide; no price discussion. |
| 80–87 workshop | Schema + ambiguous example only; tests become homework. |
| 87–90 close | Three-question recap. |


| Question | Answer |
| --- | --- |
| Why not just ask for JSON? | Valid JSON is not the same as schema adherence; a typed schema gives a stronger application contract. |
| Does streaming make the model cheaper? | Not inherently. It changes delivery timing; usage depends on the actual request/output. |
| Does Pydantic prove the classification is correct? | No. It validates structure and constraints, not semantic truth or business policy. |
| Can I put a key in a notebook just for class? | Avoid it. Use environment-based secrets and assume notebooks/screenshots can be shared. |
| Should every error retry? | No. Retry only plausibly transient failures and keep attempts bounded by the latency/side-effect budget. |
| Do we need async Python today? | No. Synchronous code keeps the API concepts visible; concurrency is a separate application design topic. |
