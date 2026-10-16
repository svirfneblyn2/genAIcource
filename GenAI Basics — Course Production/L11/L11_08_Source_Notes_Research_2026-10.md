# L11 Source Notes: Function Calling and Your First Agent (research 2026-10-16)

Primary sources checked on 2026-10-16 for the v2 rebuild of Lesson 11. Replaces the September 2026 Drive package source notes (`11 — Function Calling and Building Your First Agent — DONE/L11_08_Source_Notes.docx`).

## Images used in the deck

| File | What | Source |
|---|---|---|
| `assets/v2/img/aistudio_fn_declare.png` | Function declarations editor with `get_order_status` | own capture, Google AI Studio, 2026-10-16 |
| `assets/v2/img/aistudio_fn_call.png`, `aistudio_fn_done.png` | Gemini 3.8 Flash proposes `get_order_status(order_id="417")`; synthetic function response; final answer | own capture, Google AI Studio, 2026-10-16 (free tier, synthetic data); re-cropped with Pillow for larger on-slide text (empty UI bands removed, answer cropped on the right) |
| `assets/v2/img/aistudio_fn_call_full.png`, `aistudio_fn_done_full.png` | the uncropped originals of the two captures above (not shown in the deck) | own capture, 2026-10-16 |
| `assets/v2/img/aistudio_tools_panel.png` | Run settings → Tools panel | own capture, 2026-10-16 |
| `assets/v2/img/claude_websearch_tight.png`, `aistudio_fn_declare_tight.png` | tighter crops of the two captures, used on slides 3 and 4 so UI text is ≥ 17px | derived 2026-10-16 |
| `assets/v2/img/claude_websearch.png` | claude.ai answering "latest Ollama version" with web search and page reads | own capture, 2026-10-16 (sidebar cropped out) |
| — | cover, slide 5 (trust boundary) and slide 10 (agent loop) schematics | drawn in HTML/SVG in `deck_v2/build.py` (`app_steps()`, `boundary_diagram()`, `loop_diagram()`), RU/EN labels; replaced the English-only genai-assets images on 2026-10-16 |

Observed in the AI Studio capture: the default model in a new chat is the paid Gemini 4 Argon; switch to Gemini 3.8 Flash for the free demo. Function calling: Run settings → Tools → switch on → Edit function declarations (Code Editor / Visual Editor). The model returns a `get_order_status` block with `{"order_id": "417"}` and an "Enter a function response" field.

The slide 11 code was not executed for this rebuild (no Gemini API key on the build machine); it follows the google-genai automatic function calling pattern from the official docs.

---


Checked: 2026-10-16 (all URLs below fetched that day unless marked otherwise).
Scope: beginner lesson (L03 = LLM API in Python, L10 = LM Studio / Ollama, L12 = MCP + frameworks).
Rule used: official docs first. **UNVERIFIED** = could not confirm from a primary source today.

---

## 0. What changed since the Sept 2026 package (L11_08_Source_Notes, checked 2026-09-08)

| Topic | Sept 2026 package | Now (2026-10-16) | Impact |
|---|---|---|---|
| OpenAI models | not named (volatile) | Flagship `gpt-6-astra`, balanced `gpt-6.1-sol`, cheap `gpt-6-luna`. GPT-6 Astra / GPT-6.1 Sol **require the Responses API for tool calling** | If live demo uses Chat Completions, use an older model (docs use GPT-5.6 Terra there) or switch demo to Responses |
| OpenAI new layers | Responses + Chat Completions | Plus **Agents API** (OpenAI-hosted agent), **Agents SDK** (0.24.0, 2026-10-15), **tool search**, **custom tools** (free text + grammar) | One slide: "3 ways to build" (Responses / Agents SDK / Agents API) |
| OpenAI Agent Builder | — | Being deprecated; shuts down **2026-11-30** | Do not demo Agent Builder |
| ChatGPT "agent mode" | (if referenced) | **ChatGPT agent discontinued**, replaced by **ChatGPT Work** (launched 2026-07-09) | Update any "ChatGPT agent mode" mention |
| Gemini API surface | generateContent, FunctionCall / FunctionResponse | **Interactions API GA (June 2026), recommended for new projects**; generateContent "now considered legacy" but fully supported. Mode names now lower-case `auto / any / none / validated` in `tool_choice` | Translation slide: Gemini wire format changed (`function_call` step / `function_result`) |
| Gemini app agent | — | "Spark" renamed **Tasks in Gemini** (help page) | Use new name |
| Anthropic | strict:true, forced-tool caveat | Same concepts; Claude 5.5 family current (`claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5`) plus `claude-fable-5-1` | Forced tool use (`any`/`tool`) row is blank for Opus 5.5 / Sonnet 5.5 in the token table — caveat "support varies by model" still valid |

---

## 1. OpenAI

### 1.1 Function calling flow
- Five steps: send request with tools → model returns tool call → your app runs code → send tool output back → model answers (or calls more tools). Loop can repeat.
  URL: https://developers.openai.com/api/docs/guides/function-calling (checked 2026-10-16; page has no date)
- Responses API items: `function_call` (has `call_id`, `name`, JSON-string `arguments`) → you return `function_call_output` with the same `call_id` and an `output` string. Reasoning items returned with tool calls must be passed back. Same URL.
- **Responses vs Chat Completions:** guide recommends Responses. "GPT-6 Astra and GPT-6.1 Sol require the Responses API for tool calling." Chat Completions examples use GPT-5.6 Terra with reasoning disabled. Same URL.
- **Strict mode:** `strict: true` requires `additionalProperties: false` on every object and every property listed in `required`; optional = add `null` to the type. In Responses, if `strict` is omitted the API tries to normalize the schema to strict and falls back to non-strict; Chat Completions is non-strict by default. Same URL.
- **Parallel tool calls:** model may call several functions per turn; `parallel_tool_calls: false` → zero or one call. Same URL.
- **tool_choice:** `auto` (default), `required`, forced specific function, `allowed_tools` (subset), `none`. Same URL.
- **New since Sept:** custom tools (free-text input, optional Lark/regex grammar; item `custom_tool_call`); tool search (`tool_search`, `defer_loading`, namespaces; needs `gpt-5.4`+). Same URL.

### 1.2 Built-in (hosted) tools — Responses API
URL: https://developers.openai.com/api/docs/guides/tools (checked 2026-10-16)
| Tool | `type` string | Note |
|---|---|---|
| Web search | `web_search` | |
| File search | `file_search` | needs `vector_store_ids` |
| Code interpreter | `code_interpreter` | Responses, Chat Completions, Assistants; not deprecated — https://developers.openai.com/api/docs/guides/tools-code-interpreter |
| Computer use | `computer` | old `computer-use-preview` has a migration path; examples use `gpt-6.1-sol` — https://developers.openai.com/api/docs/guides/tools-computer-use |
| Remote MCP / connectors | `mcp` | `server_url` or legacy `connector_id` (deprecated for models released after 2026-09-01); approval required by default — https://developers.openai.com/api/docs/guides/tools-connectors-mcp |
| Tool search | `tool_search` | gpt-5.4+ only |
| Function | `function` | your own functions |
| Also listed (no type string shown) | Shell, Skills, Image generation, Programmatic Tool Calling, apply_patch | |

Built-in tool prices (https://developers.openai.com/api/docs/pricing, checked 2026-10-16): web search $10 / 1K calls + content tokens; file search $2.50 / 1K calls + $0.10/GB-day (1 GB free); containers (code interpreter / hosted shell) $0.03 per 20-min session (1 GB). Computer-use price not listed.

### 1.3 Models and prices (USD per 1M tokens, input / output)
URLs: https://developers.openai.com/api/docs/models and https://developers.openai.com/api/docs/pricing (checked 2026-10-16)
- `gpt-6-astra` $10 / $50 — flagship; "if you're unsure where to begin" → Astra.
- `gpt-6.1-sol` $2 / $10 — "near-Astra performance … at a lower cost".
- `gpt-6-luna` **$0.10 / $0.50** — "most efficient model for focused, high-volume tasks". **Cheapest current recommendation for a class demo.**
- Still on pricing page: `gpt-5.6-luna` $0.20/$1.20, `gpt-5.4-mini` $0.75/$4.50, `gpt-5.4-nano` $0.20/$1.25, `gpt-5-mini` $0.25/$2.00, `gpt-5-nano` $0.05/$0.40, `gpt-4.1-nano` $0.10/$0.40, `gpt-4o-mini` $0.15/$0.60.
- No mini/nano in the current GPT-6 line-up.
- Caveat: whether `gpt-6-luna` works with Chat Completions tool calling — **UNVERIFIED** (guide only names Astra and Sol as Responses-only for tools).

### 1.4 Agents: SDK and API
- **OpenAI Agents SDK** — pip `openai-agents`, import `from agents import Agent, Runner`; "production-ready" successor to Swarm; primitives: Agents, agents-as-tools / handoffs, guardrails; uses Responses API by default. Latest **0.24.0 (2026-10-15)**.
  URLs: https://openai.github.io/openai-agents-python/ , https://pypi.org/project/openai-agents/ (checked 2026-10-16)
- **Agents API** (OpenAI-hosted agent, saves progress, compaction, multi-agent, MCP) vs **Agents SDK** (your app runs the loop, you own approvals) vs **Responses API** (you build everything). Status beta/GA not stated on page.
  URL: https://developers.openai.com/api/docs/guides/agents (checked 2026-10-16)
  Launch date "public beta 2026-09-10" appears only in a secondary source → **UNVERIFIED**.
- **Agent Builder** is being deprecated; shuts down **2026-11-30** (notice on https://developers.openai.com/api/docs/guides/agent-builder-safety, checked 2026-10-16).
- SDK version: `openai` 3.31.0 (2026-10-14) — https://pypi.org/project/openai/

---

## 2. Anthropic (Claude)

### 2.1 Tool use mechanics
URL: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview and .../how-tool-use-works (checked 2026-10-16)
- Define tool with `name`, `description`, `input_schema`. Claude replies `stop_reason: "tool_use"` + one or more `tool_use` blocks (`id`, `name`, `input`). You run it and send a user message with `tool_result` blocks (`tool_use_id` = the block's `id`).
- Agentic loop: "while `stop_reason == "tool_use"`, execute the tools and continue"; exits on `end_turn`, `max_tokens`, `stop_sequence`, `refusal`.
- Contract framing (good beginner quote): "The model never executes anything on its own." (how-tool-use-works)
- Three buckets: user-defined client tools; Anthropic-schema client tools (`memory`, `bash`, `text_editor`, `computer`, `browser`); server tools run by Anthropic (`web_search`, `web_fetch`, `code_execution`, `tool_search`, plus advisor tool and MCP connector). Server tools return `server_tool_use` + result blocks; server-side loop can stop with `pause_turn`.
- `strict: true` on custom tools guarantees schema-conformant calls — https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use (from Sept notes; overview tip re-confirmed 2026-10-16).
- Parallel tool use exists; disable with `tool_choice: {"type":"auto","disable_parallel_tool_use": true}` (used in official example).
- **Tool Runner** (SDK beta) runs the loop for you: https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-runner
- Tool-use overhead: ~286 system-prompt tokens for Opus 5.5 / Sonnet 5.5 / Haiku 5.5 (auto/none). Forced-tool (`any`/`tool`) column is blank for Opus 5.5 and Sonnet 5.5 → keep "support varies by model".
- Web search server tool: **$10 per 1,000 searches** + tokens; versions `web_search_20250305`, `web_search_20260209` (dynamic filtering), `web_search_20260318`; `max_uses` caps searches; citations always on. https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
- Missing-parameter behaviour (useful teaching point): Opus is "much more likely" to ask for a missing required parameter; Sonnet may guess values (overview page).

### 2.2 Current models
URL: https://platform.claude.com/docs/en/about-claude/models/overview (checked 2026-10-16)
| Model | API ID | $ in / out per MTok | Note |
|---|---|---|---|
| Claude Fable 5.1 | `claude-fable-5-1` | 10 / 50 | demanding reasoning, long-horizon agentic work |
| Claude Opus 5.5 | `claude-opus-5-5` | 4 / 20 | **"start with Opus 5.5 for most workloads"** |
| Claude Sonnet 5.5 | `claude-sonnet-5-5` | 2 / 10 | speed + intelligence |
| Claude Haiku 5.5 | `claude-haiku-5-5` | from 0.10 / from 0.50 | fastest, high-volume |
- All current models: tool use, 1M context, 128K max output, knowledge cutoff Jun 2026.
- Verified: Opus 5.5, Sonnet 5.5, Haiku 5.5 exist (task question answered: yes). Also Fable 5.1 (not in the brief).
- Legacy still available: Fable 5, Opus 5, Opus 4.8/4.7/4.6/4.5, Sonnet 5, Sonnet 4.6, Haiku 4.5.
- SDK: `anthropic` 1.15.0 (2026-10-15) — https://pypi.org/project/anthropic/

### 2.3 Claude Agent SDK
URL: https://code.claude.com/docs/en/agent-sdk/overview (platform.claude.com/docs/en/agent-sdk/overview redirects here; checked 2026-10-16)
- "Build production AI agents with Claude Code as a library"; Python + TypeScript; same tools, agent loop, context management as Claude Code; built-in tools (files, commands, web search), hooks, subagents, MCP, permissions, sessions, skills, plugins.
- pip `claude-agent-sdk` **0.2.168 (2026-10-15)**, Python ≥3.10 — https://pypi.org/project/claude-agent-sdk/
- Related: **Claude Managed Agents** (Anthropic-hosted agent harness) — https://platform.claude.com/docs/en/managed-agents/overview (link seen, page not opened).
- Definition on the page: an agent is an application that completes a task by planning its own steps and calling tools.

---

## 3. Google Gemini

### 3.1 Function calling
URL: https://ai.google.dev/gemini-api/docs/function-calling (checked 2026-10-16)
- Same loop: declare functions (name, description, parameters) → model returns a `function_call` step → your app executes → send `function_result` → final answer.
- Examples now use the **Interactions API** (`client.interactions.create`, REST `/v1beta/interactions`) with model `gemini-3.8-flash`.
- Modes (`tool_choice` in `generation_config`): `auto` (default), `any`, `none`, `validated` (schema adherence); `allowed_tools` to restrict.
- Parallel and compositional (chained) calling supported.
- Best practice quote: "Keep active set to 10-20 tools maximum." Also: validate calls before executing.
- Built-in + custom tools in one request: supported (Gemini 3/4, Preview per tools page).
- Remote MCP inside the API: `type: "mcp_server"` (Streamable HTTP only).

### 3.2 Automatic function calling (Python `google-genai`)
URL: https://googleapis.github.io/python-genai/ (checked 2026-10-16)
- Pass a Python function in `tools=[...]` → SDK calls it and sends the result back automatically ("automatically called and responded by default").
- Disable: `automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)` → read `response.function_calls`.
- Limit: `maximum_remote_calls` (default 10).
- Examples use `gemini-flash-latest`.
- SDK version: `google-genai` **2.31.0 (2026-10-14)** — https://pypi.org/project/google-genai/
- Whether automatic function calling also works with `client.interactions.create` (vs `client.models.generate_content` / chats) — **UNVERIFIED**. Safe path for class: `client.models.generate_content` (still "fully supported").

### 3.3 Interactions API
URL: https://ai.google.dev/gemini-api/docs/interactions (checked 2026-10-16; page last updated 2026-10-15)
- GA **June 2026**, "recommended for all new projects". generateContent: "While it is now considered legacy, the original generateContent API remains fully supported." New models/tools/agentic features launch on Interactions.
- Built-in agents via Interactions: Deep Research Preview, Deep Research Max Preview, Antigravity Preview.
- For a beginner lesson: mention only; not needed for the demo.

### 3.4 Built-in tools
URL: https://ai.google.dev/gemini-api/docs/tools (checked 2026-10-16)
Google Search (grounding), Google Maps, Code Execution, URL Context, Computer Use (Preview), File Search. Combining built-in tools with function calling: Preview, Gemini 3 and 4 series.

### 3.5 Models
URL: https://ai.google.dev/gemini-api/docs/models (checked 2026-10-16)
- Recommended for new projects: **`gemini-3.8-flash`** (stable, "most intelligent Flash") or **`gemini-3.5-flash-lite`** (low cost).
- Flagship: `gemini-4-argon` (stable, 1M context).
- Shut down: `gemini-2.0-flash`, `gemini-3-pro-preview`, `gemini-2.5-computer-use-preview-10-2025`. Gemini 2.5 = limited to previous users.

### 3.6 Price / free tier
URL: https://ai.google.dev/gemini-api/docs/pricing (checked 2026-10-16)
- `gemini-3.8-flash`: free tier yes; paid $0.75 / $3.75 per 1M (until 2026-12-31), then $1.50 / $7.50 from 2027-01-01.
- `gemini-3.5-flash-lite`: free tier yes; paid $0.30 / $2.50.
- Google Search grounding: 5,000 requests/month free (shared, Gemini 3+), then $14 / 1K. The page also says the free tier does not include grounding for these models — summary looked contradictory → treat grounding-on-free-tier as **UNVERIFIED**.
- "Google AI Studio usage is free of charge in all available regions."

### 3.7 AI Studio UI — function calling (observed live in user's Chrome, 2026-10-16, model Gemini 3.8 Flash)
- Playground → right panel **Run settings** → **Tools** section with toggles:
  - Structured outputs [Edit]
  - Code execution
  - **Function calling [Edit]** — tooltip "Lets you define functions that Gemini can call"; the Edit button is labelled "Edit function declarations"
  - Grounding with Google Search
  - Grounding with Google Maps
  - URL context
- There is also a **Tools** button under the prompt box.
- Docs (https://ai.google.dev/gemini-api/docs/ai-studio-quickstart, updated 2026-07-30) confirm Run settings has toggles for structured output, function calling, code execution, grounding.
- Free: yes (AI Studio free in all available regions).
- **UNVERIFIED:** the declarations editor did not open in my test (the toggle did not visibly switch on). I also could not check how the UI shows a function call and lets you type the result by hand. Check by hand before class and take a screenshot.

---

## 4. Local models (L10 continuity)

- **LM Studio**: tool use via OpenAI-compatible `/v1/chat/completions` **and** `/v1/responses`; calls come back in `choices[0].message.tool_calls`. "Native" support (hammer badge in app) vs "Default" (LM Studio injects a system prompt; results vary). Native list on the page is old (Qwen2.5-7B, Llama 3.1/3.2, Ministral-8B), "subject to change". LM Studio is also an MCP client. Start server: Developer tab or `lms server start`.
  URLs: https://lmstudio.ai/docs/developer/openai-compat/tools , https://lmstudio.ai/docs/app (checked 2026-10-16). Current LM Studio version number — **UNVERIFIED** (not on page).
- **Ollama**: tool calling in native `/api/chat` (single, parallel, multi-turn agent loop, streaming); Python lib accepts plain Python functions as tools (schema from signature + docstring). OpenAI-compatible: `/v1/chat/completions` (Tools supported) and `/v1/responses` (function calling; stateless only; since v0.13.3). Client: `OpenAI(base_url="http://localhost:11434/v1/", api_key="ollama")`.
  URLs: https://docs.ollama.com/capabilities/tool-calling , https://docs.ollama.com/api/openai-compatibility (checked 2026-10-16)
- Small open models with the `tools` tag on ollama.com (checked 2026-10-16):
  - `qwen3.5` — 0.8b, 2b, 4b, 9b, 27b, 35b, 122b; tags vision, tools, thinking. https://ollama.com/library/qwen3.5
  - `granite4.2` — 3b (2.2 GB), 8b (5.3 GB, latest), 30b; function calling, structured JSON, thinking mode; updated ~1 month ago. https://ollama.com/library/granite4.2
  - `granite4.1` — 3b/8b/30b, tools (released 2026-04-28). https://ollama.com/library/granite4.1
  - `gpt-oss` — 20b (14 GB, runs in ~16 GB memory) and 120b; tools, thinking. https://ollama.com/library/gpt-oss
  - `qwen3.8` — 27b only visible (18 GB); tools, vision, thinking. https://ollama.com/library/qwen3.8
  - `nemotron-3.5-lightning` 30b MoE (3B active) "built for always-on agents" (tools search page).
- Classroom pick suggestion (not a source claim): `qwen3.5:4b` / `qwen3.5:9b` or `granite4.2:8b` for laptops; `gpt-oss:20b` if 16 GB+.
- Independent tool-use scores for Qwen3.5 small / Granite 4.2 / gpt-oss-20b on BFCL — **not found** (not in BFCL data file).

---

## 5. Consumer products where tool use is visible

- **ChatGPT**: "ChatGPT agent" (agent mode) is **discontinued**, replaced by **ChatGPT Work** (launched 2026-07-09; desktop app with Chat / Work / Codex modes; desktop has computer use and a built-in browser). Apps (connectors) are called with **@** or the **+** menu; apps are built on MCP; since 2026-07-09 apps moved to a plugin directory.
  Sources: https://help.openai.com/en/articles/11752874-chatgpt-agent , https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex , https://openai.com/index/chatgpt-for-your-most-ambitious-work/ , https://help.openai.com/en/articles/11487775-connected-apps-in-chatgpt
  help.openai.com returned 403 to direct fetch; facts come from search-result snippets of those official pages → mark **partially verified**. Exact UI wording (e.g. "Searched the web", step list in Work) is **UNVERIFIED**. "Chat, Work and Codex on every plan incl. Free" is **UNVERIFIED** (one search summary only).
- **Claude.ai**: web search via **+** → "Web search" (checkmark), or automatic with no toggle in the "new Claude experience". The UI shows an indicator that Claude is searching, then citations / source links, sometimes quotes and image results. Searches count toward usage limits (free accounts too). Team/Enterprise: an Owner must enable it.
  URL: https://support.claude.com/en/articles/10684626-enable-and-use-web-search (checked 2026-10-16, "updated over a week ago")
- **Gemini app**: **Tasks in Gemini** (formerly **Spark**). Progress chip → work panel with steps marked completed / current / planned; Files section; live view of a remote browser with **take over**. Asks for review before sending messages, changing data, purchases, form submits. Needs Google AI Pro/Ultra, 18+, personal account; **not in EEA, UK, Switzerland, Nigeria**. Connected apps: 40+ in one conversation (release notes); custom MCP connections.
  URL: https://support.google.com/gemini/answer/16596215 (checked 2026-10-16), https://gemini.google/release-notes/
- Simplest free option for a beginner demo: Claude.ai web search (free accounts, citations visible) or Gemini in AI Studio with Grounding with Google Search toggled. Gemini Tasks is not available in the EU/UK.

---

## 6. "AI agent" definitions (short quotes, under 15 words)

- OpenAI: "Agents can plan and complete tasks using tools, work with other agents…" — https://developers.openai.com/api/docs/guides/agents (2026-10-16)
- Anthropic (Building Effective Agents, 2024-12-19): agents are "typically just LLMs using tools based on environmental feedback in a loop." Workflows = "orchestrated through predefined code paths". — https://www.anthropic.com/engineering/building-effective-agents
- Anthropic Agent SDK: an application that completes a task by planning its own steps and calling tools (paraphrase) — https://code.claude.com/docs/en/agent-sdk/overview
- Google Cloud: "software systems that use AI to pursue goals and complete tasks" — https://cloud.google.com/discover/what-are-ai-agents (from search snippet; page not opened → quote **partially verified**)
- Agent loop (Anthropic): send tools + message → `tool_use` → run → `tool_result` → repeat while `stop_reason == "tool_use"`. OpenAI: same five steps, "can repeat as needed".

---

## 7. Risks and official guidance

- **Prompt injection through tool results / web pages:**
  - OWASP LLM01:2025 Prompt Injection: direct vs **indirect** (external content such as websites or files). Mitigations include least privilege and "human-in-the-loop controls for privileged operations". https://genai.owasp.org/llmrisk/llm01-prompt-injection/ (also LLM06:2025 Excessive Agency)
  - Anthropic computer use: "Claude will follow commands found in content even when they conflict…" (in some circumstances). Use a VM/container, keep secrets away, domain allowlist, and human confirmation for consequential actions. Classifiers flag likely injections in screenshots. https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool
  - OpenAI computer use: "Treat screen content as untrusted." Keep users in control of purchases, data transmission and destructive changes. Set step, time or cost limits and check the real outcome. https://developers.openai.com/api/docs/guides/tools-computer-use
  - OpenAI agent safety: keep tool approvals on; use structured outputs (enums, fixed schemas) between steps; guardrails are "not foolproof". https://developers.openai.com/api/docs/guides/agent-builder-safety
  - OpenAI MCP: approval required by default; "A malicious server can exfiltrate sensitive data…" https://developers.openai.com/api/docs/guides/tools-connectors-mcp
  - Google (Tasks in Gemini): hidden instructions in a site, email or doc could mislead the agent; safeguards don't guarantee protection, so supervise the agent. https://support.google.com/gemini/answer/16596215
- **Human-in-the-loop / confirmation**: all three vendors (above), plus OpenAI MCP `require_approval` and the Agents SDK ("you keep control over … approvals").
- **Loop and cost limits**: Anthropic recommends iteration caps (Building Effective Agents); `max_uses` on web search; `pause_turn` iteration cap on the server-side loop. Gemini SDK `maximum_remote_calls` default 10. OpenAI: step, time or cost limits (computer-use guide). Tool definitions cost input tokens (Anthropic ~286 extra tokens/request + schemas).

---

## 8. Benchmarks (tool-use reliability)

- **BFCL (Berkeley Function Calling Leaderboard)**: current version **V4** ("holistic agentic evaluation": web search, memory, format sensitivity; multi-turn since V3). Leaderboard page says last updated **2026-04-12**. https://gorilla.cs.berkeley.edu/leaderboard.html
  - Top of the published data file (https://gorilla.cs.berkeley.edu/data_overall.csv, fetched 2026-10-16): 1) Claude-Opus-4.5 (FC) 77.47%, 2) Claude-Sonnet-4.5 (FC) 73.24%, 3) Gemini-3-Pro-Preview (Prompt) 72.51%, 4) GLM-4.6 (FC thinking) 72.38%, 5) Grok-4.1-fast-reasoning (FC) 69.57%. Small open models are far lower, e.g. Qwen3-4B-Instruct-2507 35.68%, Llama-3.2-3B 21.95%, Granite-4.0-350m 18.98%.
  - Caveat: the file contains only late-2025 models (no GPT-6, Claude 5.x, Gemini 3.8). Treat it as an "early 2026 snapshot". Teaching point: even the best models are under 80%, and small local models are far lower.
- **τ-bench family** (Sierra; https://taubench.com/, fetched 2026-10-16): τ-bench (Jun 2024: retail, airline) → τ²-bench (Jun 2025: + telecom) → **τ³-bench (Mar 2026: banking + voice)**. Metric pass^k = the task must succeed in all k tries (reliability). The page reports Pass^1 and does not define pass^k → definition from the original τ-bench paper, **UNVERIFIED today**.
  - τ²-bench text top: Qwen3.5-397B-A17B 87.9%, Gemini 3.0 Pro 85.4%, Claude Opus 4.5 85.3%.
  - τ³-Banking text top: Qwen 3.8 Max 55.2%, Claude Opus 5 48.7%, Grok 4.5 47.9% (scores undated on page).
  - Teaching point: a realistic multi-step customer-service task (banking) is still solved only about half the time on one try.

---

## Suggested deltas for the rebuild (from the facts above)
1. Change the "translation" slide: OpenAI `function_call` / `function_call_output` + `call_id`; Anthropic `tool_use` / `tool_result` + `tool_use_id`; Gemini Interactions `function_call` step / `function_result` (generateContent `functionCall` / `functionResponse` is legacy but supported).
2. If the live demo stays on Chat Completions, don't use `gpt-6-astra` / `gpt-6.1-sol`. Prefer Responses with `gpt-6-luna` (cheapest), or a free path: Gemini `gemini-3.8-flash` free tier, or local Ollama `qwen3.5:4b` / `granite4.2:8b` through `/v1/chat/completions` (reuses L10 setup).
3. Replace any "ChatGPT agent mode" with "ChatGPT Work", and any "Gemini Spark" with "Tasks in Gemini".
4. The L12 bridge works: OpenAI `mcp` tool, Anthropic MCP connector, Gemini `mcp_server`, LM Studio as MCP client, ChatGPT apps built on MCP.
