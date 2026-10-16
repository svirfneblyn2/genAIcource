# Lesson 11 • Cheatsheet: function calling and your first agent

**In one sentence:** a model does not know live data, so you give it tools: it proposes a function call, your program checks and runs it, and the result goes back to the model; an agent is that loop with a step limit, and a human confirms risky actions.

## Slides and timing (90 min)
* **01 Cover (2, 0–2).**
* **02 The problem (4, 2–6):** without a tool the model invents the order status; with a tool it answers from data (AI Studio screenshot).
* **03 You have seen this (4, 6–10):** Claude: web search → “not conclusive” → reads 3 pages → answer (Ollama v0.40.5).
* **04 A tool (5, 10–15):** name, description, parameters; the model does not see the function’s code.
* **05 Who does what (5, 15–20):** the model proposes; the program checks, asks a human, runs, logs.
* **06 Demo, step 1 (5, 20–25):** AI Studio, Gemini 3.8 Flash, call `get_order_status(order_id="417")`.
* **07 Demo, step 2 (4, 25–29):** function response `{"status": "on the way", "courier": "Anna", "eta_minutes": 12}` → the model’s answer to the customer.
* **08 Built-in tools (4, 29–33):** code, search, Maps, URL context; OpenAI web_search, file_search, code_interpreter, computer, mcp; Anthropic web search (~$10 per 1,000), web fetch, code.
* **09 Description (4, 33–37):** weak `get_data`, good `get_order_status` with “what, what for, when”.
* **10 Agent (5, 37–42):** model + tools + loop; final answer when no tool is needed; a step limit.
* **11 Code (5, 42–47):** google-genai, a function with a docstring in `tools=[...]`, automatic calling, up to 10 calls by default.
* **12 Local models (4, 47–51):** Qwen3.5, Granite 4.2, gpt-oss-20b via Ollama/LM Studio; small models err more.
* **13 An agent builds an agent (4, 51–55):** prompt for Claude Code / Codex / Antigravity.
* **14 Market (4, 55–59):** ChatGPT Work, Claude, Gemini Tasks; OpenAI Agents SDK, Claude Agent SDK, Gemini API; Agent Builder shuts down 30.11.2026.
* **15 Break (5, 59–64).**
* **16 Risks (5, 64–69):** prompt injection (#1 on OWASP), action without asking, endless loop, too much access.
* **17 Reliability (4, 69–73):** τ²-bench best 87.9%, τ³-bench (banking) 55.2%.
* **18 Rules (4, 73–77):** narrow tools, checks in code, a human confirms, limits and a log.
* **19 Exercise (5, 77–82):** 4 customer questions → which tool.
* **20 Homework (5, 82–87).**
* **21 Summary (3, 87–90):** L12 (MCP) preview.

## Terms in plain words
| Term | Plain words |
|---|---|
| Tool | an action the model may ask for: find, compute, send |
| Function call | the model’s reply “call get_order_status with 417” instead of text |
| Function declaration | name, description and parameters — all the model knows about a tool |
| Trust boundary | the line between the model (may be wrong) and the program (checks and runs) |
| Agent | a model with tools working in a loop until the task is done |
| Prompt injection | someone else’s text in a page or email trying to command the model |
| Docstring | a Python function’s description string; the library passes it to the model as the tool description |

## Recheck within 24 hours of class
1. AI Studio: the default model (now the paid Gemini 4 Argon), the path Run settings → Tools → Function calling → Edit.
2. Model names: Gemini (3.8 Flash), OpenAI (gpt-6), Claude (5.5).
3. Status of ChatGPT Work, Gemini Tasks (plans, countries), OpenAI Agent Builder (shutdown 30.11.2026).
4. Tool-capable models in the Ollama library.
5. Latest τ²-bench / τ³-bench results.
6. Anthropic web search price.
