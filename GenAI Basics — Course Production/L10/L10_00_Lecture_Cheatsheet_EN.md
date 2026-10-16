# Lesson 10 • Cheatsheet: open models, LM Studio, Runpod

**In one sentence:** an open model is a weights file plus a licence; if the Q4 file plus a 25% margin fits the GPU memory, you can run it yourself in LM Studio or Ollama and connect it to code by changing only the address and model name; when a laptop is not enough, run the same model on a rented Runpod GPU.

## Slides and timing (90 min)
* **01 Cover (2, 0–2).**
* **02 One app, three places (4, 2–6):** cloud API / laptop `localhost:1234` / rented GPU. Only the address and model name change, not the code.
* **03 Open model = file + licence (5, 6–11):** Hugging Face `ibm-granite/granite-4.2-8b-GGUF`, Apache-2.0, files 5.35–9.35 GB (in the screenshot: Q4_K_M … Q8_0).
* **04 Why (4, 11–15):** pros and cons; Artificial Analysis index 58 (Claude Opus 5.5) / 46 (MiMo-V2.6-Pro) / 34 (Qwen3.8 27B).
* **05 Five parts (4, 15–19):** file → llama.cpp engine → hardware → server → app; LM Studio or Ollama bundles the first four.
* **06 Quantisation (5, 19–24):** Granite 4.2 8B: Q2_K 3.4 · Q4_K_M 5.4 · Q8_0 9.4 · BF16 17.6 GB. Start at Q4.
* **07 Will it fit (5, 24–29):** Q4: Granite 3B 2.2 · Qwen3.5 4B 2.7 · Granite 8B 5.4 · Qwen3.5 9B 5.6 · Gemma 4 12B 7.4 · gpt-oss-20b 12.1 · Qwen3.8 27B 16.8 GB. Plus 25% for context. Bar colour = the smallest GPU (6 / 16 / 24 GB) it fits; 8 GB → up to 9B.
* **08 Speed (4, 29–33):** tokens/s (7B Q4, llama.cpp): CPU ≈10 (estimate), M5 32, RTX 4050 Laptop 44, M5 Max 120, RTX 4090 186, H100 268. Comfortable from 20. A GPU is 2–25× faster than a CPU.
* **09 LM Studio (5, 33–38):** Chat, Discover, My Models, Developer. Free, also for work. Version 0.4.26. Do not confuse with Bionic.
* **10 Demo (5, 38–43):** granite-4.2-3b Q4_K_M (2.2 GB, download in advance), ticket prompt → JSON.
* **11 Local server (5, 43–48):** Developer → Start server, `http://localhost:1234/v1`; Ollama `http://localhost:11434/v1`. The address and model name change (and the key).
* **12 An agent installs the model (4, 48–52):** prompt for Claude Code / Codex / Antigravity: Ollama, model, speed, localhost only.
* **13 Local ≠ private (4, 52–56):** downloads, tools (MCP), a network-exposed server → Require Authentication (token login). Rule: localhost only, models only from official sources (Hugging Face, ollama.com) by known publishers.
* **14 Market (4, 56–60):** laptop / one GPU / server; almost all Apache-2.0; Llama 4 and Qwen3.8-Flash-Next have custom licences.
* **15 Break (5, 60–65).**
* **16 Laptop limits (3, 65–68):** does not fit, too slow, many users, 24/7.
* **17 Runpod (5, 68–73):** Pod (you start and stop it) and Serverless (wakes on request). Stop still bills the disk → Terminate. At a zero balance the Pod stops, and without a network volume it is deleted with its data.
* **18 Price (5, 73–78):** Community per hour: RTX 4090 $0.34 · 5090 $0.69 · L40S $0.79 · A100 SXM $1.39 · H100 SXM $2.69. A 4090 at 100% load ≈ $0.73 per 1M tokens versus $0.40–4.50 for cheap cloud models ($0.73 is the single-user worst case; vLLM with batching gets several times more).
* **19 How to choose (4, 78–82):** can the data leave × how much work → API / laptop / Serverless / Pod. Sensitive data on Runpod → Secure Cloud (RTX 4090 $0.89/h).
* **20 Homework (5, 82–87):** run a model yourself, 3 tasks against the cloud, speed, decision card; submit to `genai-homeworks/L10/`.
* **21 Summary (3, 87–90):** four rules, L11 preview.

## Terms in plain words
| Term | Plain words |
|---|---|
| Weights, parameters | the trained numbers inside a model; “8B” = 8 billion |
| Open model | weights you may download and run yourself under a licence |
| GGUF | model file format for LM Studio, Ollama, llama.cpp |
| Quantisation (Q4, Q8) | compression: each number stored with fewer bits |
| VRAM | GPU memory; the model must fit in it |
| Tokens per second | generation speed; people read ≈ 4–7 |
| localhost | “this computer”; the server is visible only to you |
| Pod / Serverless | a rented computer with a GPU / a GPU on demand |

## Recheck within 24 hours of class
1. LM Studio version, tab names, “Start server”, compatible endpoints (lmstudio.ai/docs).
2. The Ollama tag for Granite 4.2 3B and the Ollama version (ollama.com/library).
3. GGUF sizes on Hugging Face (granite-4.2-3b/8b, Qwen3.5, Gemma 4, gpt-oss-20b).
4. Artificial Analysis index (artificialanalysis.ai).
5. Runpod Pod and Serverless prices, stopped-Pod disk price, spending limit (runpod.io/pricing, docs.runpod.io).
6. Cheap cloud model prices per 1M tokens (Gemini, OpenAI).
7. New open models in the last month (Qwen, Gemma, Granite, Llama/Muse, Mistral).
