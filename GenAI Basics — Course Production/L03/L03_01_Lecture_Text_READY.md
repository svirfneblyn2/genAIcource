# Lecture 03 — LLM API with Python: Streaming and Structured Output

Production-ready teaching text: from a prompt to a reliable software boundary

GenAI Basics  •  Module 03  •  Refreshed 2026-09-14

# Audience and promise

Audience: students who understand prompts, context, tokens and grounding from Module 02, but may never have called an LLM API from code.

By the end of the session, students can make a Responses API request from Python, stream output as events, parse a Pydantic-typed structured response, and design a bounded failure/observability policy around the call.

Core engineering idea: an LLM API call is a boundary between probabilistic behavior and deterministic software. The boundary needs an explicit contract: inputs, model, schema, timeout, retry policy, validation and evidence.

# Learning outcomes

- Explain the request path: Python application → SDK → HTTPS → model service → typed response object.
- Keep API credentials outside source code and verify that local secret files cannot be committed.
- Make a minimal request with the OpenAI Python SDK Responses API.
- Consume streamed output-text delta events and distinguish time-to-first-visible-output from total runtime.
- Define a Pydantic schema and obtain a typed result with client.responses.parse(..., text_format=...).
- Separate schema validity, semantic validity and business/action validity.
- Handle rate limits, API status errors, connection failures and timeouts without unbounded retries.
- Record request ID, model, elapsed time and usage so a failed or expensive request can be investigated.
# 1. Why browser chat habits are not enough

A human can repair a slightly odd answer in a chat window. Software often cannot. If the next component expects category=bug and receives a friendly paragraph instead, the application boundary has failed even if the prose is excellent.

The useful question is not “Did the model answer?” It is “Did the application receive a result that is valid enough to display, store, route or act on?” That changes how we design the call.

# 2. Mental model: what the SDK does

The Python SDK is a typed client for a remote HTTP API. It does not contain the model weights. Your program constructs a request; the SDK serializes it; the service authenticates and runs the model; the SDK returns typed response objects or typed exceptions.

# 3. Setup and secret hygiene

The first production habit is not clever prompting. It is keeping credentials out of the code and out of the student artifact.


- Keep .env in .gitignore. Commit .env.example with placeholder values only.
- Create one key for the teaching environment; rotate it if it ever appears in a screenshot, repository or chat.
- Configure the model through OPENAI_MODEL so the code is not tied to a volatile model alias.
- Run a local preflight before the live call: Python version, package versions, model value and whether a key is present.
# 4. First request: minimal, explicit and inspectable


The code makes five choices visible: the client policy, the model, stable instructions, task input and the response fields we care about. Do not start by printing a huge raw response dump. Start with the fields that teach the contract.

# 5. Request anatomy

Model choice is a runtime configuration decision, not a permanent truth. As checked on 2026-09-14, the official GPT-5.6 Terra page lists Responses API, streaming and structured outputs as supported. The course uses it as a prepared default, but the repository reads OPENAI_MODEL so delivery can switch to another compatible model without code edits.

# 6. Response anatomy and evidence

- output_text — convenient aggregate text for normal text responses.
- output — typed response items when you need finer control.
- usage — provider-reported input/output usage; log it rather than guessing from visible words.
- _request_id — public request identifier exposed by the SDK; useful when debugging a slow or failed call.
- error exception classes — operational categories your code can handle deliberately.
A useful telemetry envelope for a production call is: model, request ID, elapsed time, usage, success/failure category and an application correlation ID. Do not log the API key or sensitive prompt contents by default.

# 7. Streaming: the response becomes an event flow

Without streaming, a user waits until the response object is complete. With streaming, the server emits events and the client can render text deltas as they arrive. This usually improves perceived responsiveness. It does not mean the model used fewer tokens or completed the entire task earlier.


Think of streaming as transport semantics: request created → events arrive → output accumulates → terminal event. The application may need to handle interruption, partial display and cleanup. A streamed partial answer is not automatically a valid final business artifact.

# 8. Structured outputs: solve the shape problem

Prompting “return JSON” is a convention. A structured output schema is a contract. In Python, Pydantic gives us a concise way to define allowed fields, types and value constraints, and the current OpenAI Python SDK supports passing a Pydantic class to responses.parse.


The typed result is useful because downstream code can work with ticket.priority as a constrained value rather than splitting prose or hoping a JSON key exists.

# 9. Three levels of validation

Structured output gives strong help with the first level. It does not guarantee the second or third. Consequential workflows still need domain checks, confidence/ambiguity handling, reference data validation and, where appropriate, human review.

# 10. Failure taxonomy: errors are part of the interface


As checked against the current SDK documentation, selected transient failures are retried by default. The course sets max_retries=2 explicitly so students can see the policy. Production systems should choose the number and timeout based on their latency budget, idempotency and failure semantics—not because “two” is universally correct.

# 11. Cost and latency: measure first

- Time to first visible output matters for interactive UX; streaming can improve it.
- Total response time matters for batch or workflow completion.
- Input and output token usage are separate; long generated answers can dominate usage.
- Provider prices and model lineups change. Keep prices in source notes or a delivery-day appendix, not in the core mental model.
- Choose the lowest-cost model that reliably meets a measured quality target; re-evaluate on model changes.
# 12. A practical application boundary

- Load configuration and secret from the environment.
- Validate or sanitize task input before sending it.
- Call a model that supports the required feature.
- Use streaming for progressive human display or structured output for machine consumption; do not conflate the two.
- Validate the result at schema, semantic and business levels.
- Record request ID, model, elapsed time and usage.
- Only then store, display or trigger side effects.
# 13. Live lab

The lab uses one support-ticket workflow. We start with a plain call, stream an explanation, extract a typed ticket, then inspect request ID/usage and the local failure policy. The purpose is not to memorize the SDK. It is to see the same software boundary become progressively more reliable.

# 14. Takeaways

- The SDK is a client for a remote API; it is not the model.
- Streaming changes delivery behavior. It is not a different intelligence mode.
- Structured output constrains shape; semantic truth and action safety still need validation.
- Timeouts, bounded retries, request IDs, usage and secret handling belong in the first useful implementation, not in a future “productionization” phase.
- Keep volatile model/version facts outside the core lesson and re-check them before delivery.

| Human-facing answer | Application-facing contract |
| --- | --- |
| A paragraph can be acceptable. | Fields, types and allowed values need to be explicit. |
| A person spots ambiguity. | Code needs an ambiguity path such as needs_human_review. |
| Errors can be retried manually. | Timeouts, retries and failure classes must be bounded. |
| Debugging can be anecdotal. | Request ID, latency and usage should be recorded. |


| Layer | Responsibility |
| --- | --- |
| Your application | Task definition, user data, model selection, schema, timeout/retry policy, validation and side effects. |
| Python SDK | Authentication headers, HTTP transport, serialization, response types, streaming event types and typed exceptions. |
| Responses API | Model execution and response/event generation. |
| Your application again | Validation, logging, display, storage, escalation or rejection. |


| # .env — local only, never commit OPENAI_API_KEY=replace_me OPENAI_MODEL=gpt-5.6-terra |
| --- |


| from openai import OpenAI  client = OpenAI(timeout=20.0, max_retries=2) response = client.responses.create(     model="gpt-5.6-terra",     instructions="Answer for a first-year IT student. Be concise and concrete.",     input="Explain the difference between an API and an SDK in three bullets.", )  print(response.output_text) print(response._request_id) print(response.usage) |
| --- |


| Part | Question to ask |
| --- | --- |
| Model | Does this model support the capability I need, and is its quality/cost/latency appropriate? |
| Instructions | What behavior should remain stable across inputs? |
| Input | What task data belongs to this request? |
| Timeout | How long is the application willing to wait? |
| Retry policy | Which failures are transient, and how many attempts are acceptable? |


| stream = client.responses.create(     model=model,     input="Explain streaming in five short sentences.",     stream=True, )  for event in stream:     if event.type == "response.output_text.delta":         print(event.delta, end="", flush=True) print() |
| --- |


| from typing import Literal from pydantic import BaseModel, Field  class SupportTicket(BaseModel):     category: Literal["bug", "question", "feature"]     priority: Literal["low", "medium", "high"]     summary: str = Field(min_length=1, max_length=160)     needs_human_review: bool  response = client.responses.parse(     model=model,     instructions=(         "Classify the ticket. If intent or severity is ambiguous, "         "set needs_human_review=true. Do not invent missing facts."     ),     input=ticket_text,     text_format=SupportTicket, )  ticket = response.output_parsed |
| --- |


| Level | Question | Example failure |
| --- | --- | --- |
| Schema validity | Does the output match fields/types/enums? | priority="urgent" when only low/medium/high is allowed. |
| Semantic validity | Do the fields reflect the source input? | A question is incorrectly classified as a bug. |
| Business/action validity | Is it safe and appropriate to act automatically? | A high-impact ambiguous ticket is routed without human review. |


| Failure | Typical meaning | Application response |
| --- | --- | --- |
| Timeout | No usable response before the deadline. | Fail or retry within a bounded policy; do not wait forever. |
| Connection error | Network path did not produce a usable API response. | Retry only if policy allows; surface network category. |
| Rate limit | Capacity/quota/rate policy rejected the request. | Back off; reduce concurrency or retry later. |
| Other API status error | Service returned an HTTP error status. | Inspect status + request ID; retry only when it is actually transient. |
| Validation failure | Returned content cannot be accepted as the contract. | Reject/escalate; do not coerce silently. |


| import openai  try:     response = client.responses.create(model=model, input="One sentence about retries") except openai.RateLimitError as exc:     print("rate limit", exc.request_id) except openai.APITimeoutError:     print("timeout") except openai.APIConnectionError:     print("connection") except openai.APIStatusError as exc:     print(exc.status_code, exc.request_id) |
| --- |
