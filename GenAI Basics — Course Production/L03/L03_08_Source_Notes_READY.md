# Lecture 03 — Source Notes

Official/current sources and isolated volatile facts — checked 2026-09-14

GenAI Basics  •  Module 03  •  Refreshed 2026-09-14

# Official sources

# Volatile facts isolated from the core lesson

- OpenAI Python 3.13.0 is the current package release observed on 2026-09-14; requirements use `openai>=3.13,<4`. Re-check before delivery.
- Prepared default model is gpt-5.6-terra. It is configuration, not a permanent recommendation.
- Official Terra pricing observed on 2026-09-14 is $2.00 / 1M input text tokens and $12.00 / 1M output text tokens, with additional long-context/cache-write rules. These numbers are intentionally not embedded in the core slides.
- The SDK documents selected transient errors as automatically retried; the demo explicitly sets max_retries=2 so the policy is visible. Re-check defaults before presenting them as SDK behavior.
- The structured-output example is shown with `response.output_parsed` for beginner clarity; the official SDK example also demonstrates accessing parsed content items. If SDK behavior changes, update repository and slides as one unit.
# Source hygiene rule

Use official provider/package documentation for current API shape and capability support. Third-party blog posts may be useful for examples but are not canonical for model IDs, SDK signatures, limits or pricing. Model rankings and prices should never become course facts without a delivery-day check.


| Source | Checked | Used for |
| --- | --- | --- |
| https://pypi.org/project/openai/3.13.0/ | 2026-09-14 | Current OpenAI Python SDK release: 3.13.0, published 2026-09-10; Python >=3.10; Responses is primary API in package docs. |
| https://github.com/openai/openai-python | 2026-09-14 | SDK usage, typed exceptions, request IDs, retries/timeouts, streaming patterns. |
| https://github.com/openai/openai-python/blob/main/examples/responses/structured_outputs.py | 2026-09-14 | Current Pydantic structured-output pattern with client.responses.parse(..., text_format=...). |
| https://developers.openai.com/api/docs/models/gpt-5.6-terra | 2026-09-14 | Prepared model capabilities: Responses API, streaming and structured outputs supported; model positioned for balance of intelligence and cost. |
| https://developers.openai.com/api/docs/models | 2026-09-14 | Model-selection context; model lineup is volatile. |
| https://docs.pydantic.dev/latest/concepts/models/ | 2026-09-14 | Pydantic BaseModel validation and model constraints. |
