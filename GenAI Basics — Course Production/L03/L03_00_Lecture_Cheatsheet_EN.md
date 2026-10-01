# 1-Page Speaker Cheatsheet • Lesson 03 (20 Slides • 90 Minutes)
*Speaker: Igor Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*  
*Topic: LLM API with Python: Architecture, Tooling, and First Programmatic Call (2026 Standards)*

---

### Part 1: How LLM APIs Work Under the Hood (00:00 — 55:00)

* **Slide 01 (00–04 min) • Title:** LLM API with Python. Core takeaway: An LLM is not a "website" or "magic"; it is a remote cloud HTTP server accepting tokens and returning probabilities. Our objective is wrapping probabilistic output in resilient software contracts. Chat poll: who has invoked APIs programmatically (1) versus web-chatting only (2)?
* **Slide 02 (04–08 min) • Curriculum Roadmap (Stepper):** Concluding Module 1 (L01–L03). API execution is the universal foundation: required for image ingestion in Module 2, tool invocation in Module 5, and autonomous agents in Module 6.
* **Slide 03 (08–13 min) • Interaction Architecture (Flow):** Why the model does not run locally on your laptop. Application $	o$ HTTPS POST to Cloud API Gateway (Auth & Quotas) $	o$ Datacenter GPU Cluster (Token generation) $	o$ Network response.
* **Slide 04 (13–17 min) • Anatomy of an HTTP Request (C4 Diagram):** End-to-end packet journey across the REST API Boundary: student script on the client side, proprietary GPU cluster on the server side.
* **Slide 05 (17–22 min) • Why Use an SDK (Shield Layer):** Raw HTTP versus official SDKs. SDKs manage connection pooling, socket keep-alive, exponential backoff retries on HTTP 429, and type hints.
* **Slide 06 (22–27 min) • First Call: Google AI Studio ➔ Colab (Code):** Browser execution via ▶ Play. Bridge from Google AI Studio (`aistudio.google.com`): tune prompt visually, click **"Get Code"**, and execute in Colab via secure `userdata.get('GEMINI_API_KEY')` with zero secret exposure. 2026 model standard: `gemini-3.5-flash` (15 RPM free tier).
* **Slide 07 (27–31 min) • Response Anatomy (Digital Receipt):** Server payload: `response.text`, `finish_reason` (`STOP` vs `MAX_TOKENS`), and `usage_metadata` (`prompt_token_count`, `candidates_token_count`, `total_token_count` for budget and quota audits).
* **Slide 08 (31–35 min) • API Key Security (Hygiene):** An API key is a live corporate credit card. Automated scrapers monitor public GitHub commits in real time. Standard: `.env` file, strict `.gitignore` rules, Colab Secrets vault 🔑.
* **Slide 09 (35–40 min) • Streaming: Physics & UX (Timeline):** Monolithic blocking wait (5s lag) versus instantaneous Time to First Token (TTFT = 200ms) via Server-Sent Events (SSE).
* **Slide 10 (40–44 min) • Streaming in Code (`generate_content_stream`):** How streaming delivers token deltas: `for chunk in response: print(chunk.text, end="", flush=True)`. The role of `flush=True` and when to avoid streaming (background batch ETL and database writes).
* **Slide 11 (44–48 min) • Bridge to Lesson 02: Prompt Engineering in Code (XML & One-Shot):** Translating prompt skills into code parameters. System authority via `system_instruction` (anti-prompt injection), XML demarcations (`<context>`, `<rules>`, `<document>`), and One-Shot exemplars with `temperature=0.0` for 100% determinism.
* **Slide 12 (48–51 min) • Structured Outputs (Constrained Decoding):** Hardware-enforced schema guarantee. The inference engine dynamically masks out token logits that would violate JSON syntax. 100% syntactic reliability.
* **Slide 13 (51–55 min) • Practical Ticket Triage into JSON (Code):** Enforcing schemas via `response_mime_type="application/json"` and `temperature=0.0` on `gemini-3.5-flash`. Transforming unstructured dispute text into typed dictionary fields (`category`, `amount_usd`, `urgent`).

---

### Midpoint Break: 5 Minutes (55:00 — 60:00)

* **Slide 14 • 5-Minute Coffee Break:**  
  *Press the "START 5 MIN" button on screen.* Instructor announcement: "Take 5 minutes to recharge. In the second half, we will dissect network failure modes, inspect the 2026 model landscape, and execute our live Google Colab notebook." *(Strictly no chat Q&A during break—allow students to rest!)*

---

### Part 2: Reliability, Library Ecosystem, and Homework (60:00 — 90:00)

* **Slide 15 (60–65 min) • Network Resilience (What Can Go Wrong):** 
  - `401 Unauthorized` — invalid or revoked credentials.
  - `429 Rate Limit` — quota exhaustion. Handled via exponential backoff.
  - `500 / 503 Provider Error` — temporary datacenter saturation.
  - `Timeout` — hung socket. Always supply `timeout=30.0` to prevent service lockup.
* **Slide 16 (65–70 min) • Python AI Tooling Landscape (3 Layers):** 
  - Layer 1: Raw network I/O (`requests`, `curl`).
  - Layer 2: Official vendor SDKs (`google-genai`, `openai`, `anthropic`) — core engineering foundation.
  - Layer 3: High-level orchestrators (`LangChain`, `LlamaIndex`) — only adopt when foundational SDKs reach limits.
* **Slide 17 (70–74 min) • 2026 Model Matrix (OpenAI vs Claude vs Gemini):** 
  - OpenAI: `gpt-4o` and `o3-mini` (function calling & schema standards).
  - Anthropic: `claude-3-7-sonnet` (Thinking mode, architectural reasoning).
  - Google: `gemini-3.5-flash` and `gemini-3.8-flash` (2M+ window, native audio/video multimodal, 15 RPM free tier).
  - Open-weights: `DeepSeek-V3 / R1` and unified wrappers like `LiteLLM`.
* **Slide 18 (74–79 min) • First AI Script Checklist (5 Rules):** Secret hygiene in `.env` $	o$ Explicit 30s timeout $	o$ Zero temperature for data extraction $	o$ Strict schema via `response_mime_type` $	o$ Audit logging of token usage.
* **Slide 19 (79–85 min) • Homework Assignment #3 (Colab & Applied Production Case):** 
  - **Track A (Standard):** Triage workplace documents into strict JSON.
  - **Track B (Applied Engineering Pipeline • Creator Tools Pattern):** YouTube Video Analyzer — input any technical video/webinar URL, fetch transcripts in 1 second, pass through Lesson 02 XML template to `gemini-3.5-flash`, and generate an Executive Briefing Memo (TL;DR, key decisions, action items).
  - Submit `result.json` to GitHub repository: `genai-homeworks/L03/`. Collaborator: `ihar_rubanovich@epam.com`.
* **Slide 20 (85–90 min) • Q&A and Lesson 04 Teaser:** 3 takeaways: LLMs are web servers, prompt engineering maps to SDK parameters, multimodal schemas protect production. Next session: Module 2 (Images & Video with DALL-E 3, Midjourney, Stable Diffusion, Imagen). Open mic!
