# Instructor Script • Lesson 10: Open Models. Your Laptop and a Rented GPU (90 Minutes)

**Course:** GenAI Basics • Module 4 (Open Models) • Lesson 10 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles. Plain language; code only as one short reference example (slide 11).
**Format:** 21 slides (`presentation_L10_Open_Models_Local_and_RunPod_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v2/build.py` (slide text and speaker notes). This script is generated from it (`deck_v2/make_docs.py`); if anything differs, `build.py` wins.
**Facts:** as of 16.10.2026, sources in `L10_08_Source_Notes_Research_2026-10.md`. The “recheck within 24 hours” list is at the end of the cheatsheet.

> **Before class:** install LM Studio (the classic app, not Bionic) and download `granite-4.2-3b` at Q4_K_M (2.2 GB) in advance for the slide 10 demo. Runpod is shown on screenshots; a live launch is paid and optional.

**Lesson objective:** students understand what an open model is (a file plus a licence), can estimate whether a model fits their computer and how fast it will run, run a model in LM Studio or Ollama and connect it to code through a local server, and understand when a rented GPU is needed (Runpod Pod or Serverless), what it costs and how to choose between a cloud API, a laptop and renting.

---

## Timing (21 slides • 90 minutes incl. a 5-minute break)

| Slide | Title | Time | Min |
|---|---|---|---|
| **01** | Open models | 00:00–02:00 | 2 |
| **02** | One app, three places where the model runs | 02:00–06:00 | 4 |
| **03** | An open model is a file you can download, plus its licence | 06:00–11:00 | 5 |
| **04** | Your own model: data stays home, but quality trails the leaders | 11:00–15:00 | 4 |
| **05** | Five parts: file, engine, hardware, server, app | 15:00–19:00 | 4 |
| **06** | Quantisation: the same model 2–5× smaller, slightly lower quality | 19:00–24:00 | 5 |
| **07** | The model file plus room for the conversation must fit the GPU memory | 24:00–29:00 | 5 |
| **08** | A GPU answers 2–25× faster than a CPU | 29:00–33:00 | 4 |
| **09** | LM Studio: a chat like ChatGPT, but the model runs on your machine | 33:00–38:00 | 5 |
| **10** | Demo: download a small model and ask it a work question | 38:00–43:00 | 5 |
| **11** | Turn on the server and the model answers your code like a cloud API | 43:00–48:00 | 5 |
| **12** | A coding agent installs the model for you and measures the speed | 48:00–52:00 | 4 |
| **13** | “Local” does not automatically mean “private”: check the whole data path | 52:00–56:00 | 4 |
| **14** | Open models by size: what runs where | 56:00–60:00 | 4 |
| **15** | 5 minutes: grab a coffee while the model downloads | 60:00–65:00 | 5 |
| **16** | When a laptop is not enough: four signs | 65:00–68:00 | 3 |
| **17** | Runpod: a GPU rented with per-second billing, two modes | 68:00–73:00 | 5 |
| **18** | Renting a GPU only pays off if it is busy all the time | 73:00–78:00 | 5 |
| **19** | Choose by two questions: can the data leave, and how much work is there | 78:00–82:00 | 4 |
| **20** | Homework: run a model yourself and compare it honestly with the cloud | 82:00–87:00 | 5 |
| **21** | Your own model is a file and memory; in code only the address and model name change | 87:00–90:00 | 3 |

Part 1 (slides 01–14, 00:00–60:00): open models, memory and speed, LM Studio, the local server, an agent, security, market. Break (slide 15, 60:00–65:00). Part 2 (slides 16–21, 65:00–90:00): laptop limits, Runpod, price, choosing, homework, summary.

---

### Slide 01 (00:00–02:00) • Open models

**On screen:** Lesson title, subtitle, scope; on the right three cards: cloud API, your laptop, rented GPU with their addresses.

#### Speaker (2 min)
> Welcome. So far we have used other people’s models: ChatGPT, Gemini, Claude, ElevenLabs. They live in the cloud; we pay a subscription or per token, and our data goes to the vendor. Today we run a model ourselves.
>
> Plan: what an open model is, what your computer needs, LM Studio and a local server, an agent installs a model for you, the open model market. After the break: when a laptop is not enough, renting a GPU on Runpod, price, how to choose, homework.

---

### Slide 02 (02:00–06:00) • One app, three places where the model runs

**On screen:** Schematic: your app sends a request to three addresses — cloud API, laptop (localhost:1234), rented GPU. Legend 1–3 on the right; below, “only the address and model name change”.

#### Speaker (4 min)
> On the left is an app, for example the support bot from earlier lessons. It sends a request to a model. The first option we know: a cloud API at api.openai.com or the Gemini API. The second: the same task, but the model is a file on your laptop, at localhost, meaning “this computer”. The third: your model on a rented GPU in the Runpod cloud.
>
> Why it matters. Many local tools (LM Studio, Ollama) speak the same “language” as the OpenAI API. So moving between the three options means changing the address and the model name in settings, not rewriting the app. By the end of the lesson you can choose one of the three on purpose.
>
> Question for the chat: what company data would you not send to ChatGPT? That is the first reason for a local model.

---

### Slide 03 (06:00–11:00) • An open model is a file you can download, plus its licence

**On screen:** Large Hugging Face crops: the granite-4.2-8b-GGUF header (publisher, Apache-2.0 licence) and the file list from Q4_K_M to Q8_0, callouts 1–3.

#### Speaker (5 min)
> Show the page live if there is time: huggingface.co, search “granite-4.2-8b-GGUF”. An open model is first of all weight files: trained numbers you can download and run yourself. You cannot download ChatGPT like that; it is a closed model.
>
> Three things on the page. One: who made it. IBM, Granite 4.2 with 8 billion parameters. Parameters are the numbers inside the model; more of them usually means a smarter and heavier model. Two: the licence. Apache-2.0 allows use at work and in commercial products, as long as you keep the licence text. Three: files. The same model comes in several sizes: Q2, Q4, Q8. That is compression; slide 6 covers it.
>
> GGUF is a model file format for tools like LM Studio and Ollama: weights plus a model description in one file. Licences vary. Apache-2.0 and MIT are permissive. Llama 4 has Meta’s own licence with conditions and gated access. Rule: read the licence before you build a product on a model.

---

### Slide 04 (11:00–15:00) • Your own model: data stays home, but quality trails the leaders

**On screen:** Pros and cons on the left; Artificial Analysis index bars on the right: 58 / 46 / 34; below, a task strip: ✓ emails and tickets, drafts, document search; ✗ hard reasoning and large codebases.

#### Speaker (4 min)
> The honest picture. Pros of your own model: data never leaves the computer, it works on a plane or in a closed network, there is no bill per request, and the model will not change tomorrow without you knowing (cloud model versions do change).
>
> Cons: quality. The independent Artificial Analysis ranking (index v4.3, October 2026): the best closed model, Claude Opus 5.5, scores 58; the best open model, MiMo-V2.6-Pro, 46. But MiMo is huge and will not fit a laptop. An open model that fits one gaming GPU, Qwen3.8 27B, scores 34. Enough for simple tasks, not for hard reasoning.
>
> Takeaway: a local model is good for repetitive simple tasks on sensitive data: classify tickets, extract fields from an email, write a draft. Keep the cloud for hard work.

---

### Slide 05 (15:00–19:00) • Five parts: file, engine, hardware, server, app

**On screen:** Five-part schematic with icons: model file → llama.cpp engine → hardware → localhost:1234 server → app; over the first four a bracket “LM Studio or Ollama does this for you”.

#### Speaker (4 min)
> When we use ChatGPT everything is hidden. Locally you see five parts. The model file: weights, GGUF format. The engine: a program that can run it; almost everywhere that is llama.cpp. Hardware: CPU, GPU and their memory. The server: gives the model an address, localhost:1234, so other programs can call it. And your app: a chat window or a Python script.
>
> LM Studio packs the first four parts into one program with buttons. Ollama does the same from the command line. Why know the parts: when something breaks you know where to look. The model will not load — the file does not fit in memory. It answers slowly — the CPU is computing instead of the GPU. The app gets an error — wrong address or model name.

---

### Slide 06 (19:00–24:00) • Quantisation: the same model 2–5× smaller, slightly lower quality

**On screen:** Bars of Granite 4.2 8B file sizes from Q2_K (3.4 GB) to BF16 (17.6 GB); on the right “Q4” and the JPEG analogy.

#### Speaker (5 min)
> On Hugging Face we saw many files for one model. The letter Q and a number mean quantisation, in plain words compression. The original stores each number in 16 bits: 17.6 GB for Granite 8B. Store each number more coarsely, in 8 bits, and the file is 9.4 GB; in 4 bits, 5.4 GB, a third of the original.
>
> The cost of compression is quality. 8 bits are nearly indistinguishable from the original. 4 bits are a sensible compromise, and the LM Studio docs recommend starting there. 2–3 bits are noticeably worse: the model gets confused more often. The K_M letters are a variant of the method; to start, just take Q4_K_M.
>
> Analogy: a JPEG photo. At high quality you see no difference; at heavy compression you see blocks. Rule: take the largest file that fits comfortably in memory, but no smaller than Q4.

---

### Slide 07 (24:00–29:00) • The model file plus room for the conversation must fit the GPU memory

**On screen:** Q4 bars for seven models with +25% hatching and memory lines at 6 / 8 / 16 / 24 GB; bar colour = the smallest GPU it fits (8B and 9B are green: they fit 8 GB); “+25%” on the right.

#### Speaker (5 min)
> The beginner’s main question: which model fits my computer. The solid bar is the real 4-bit file size; the hatching is a 25% margin for the context, meaning the conversation history and attached documents. The vertical lines are GPU memory (called VRAM): 6 GB on a laptop gaming GPU (like the RTX 3060 Laptop), 8 GB on many newer laptops, 16 GB on a mid-range card, 24 GB on an RTX 4090.
>
> Read it like this: if the bar plus hatching is left of a line, the model fits that GPU entirely; the bar colour is the smallest of the four GPUs it fits. 6 GB — models up to 4B. 8 GB (common in laptops) — up to 9B: Granite 8B and Qwen3.5 9B take about 7 GB with the margin. 16 GB — up to 12B, with gpt-oss-20b just squeezing in. 24 GB — up to 27B. If the model does not fit the GPU entirely, LM Studio puts part of it in system RAM, but speed drops several times.
>
> A laptop without a GPU: the model sits in system RAM, and 16 GB is enough even for 8B, but the CPU computes slowly (slide 8). So without a GPU take 3–4B, Granite 3B or Qwen 4B. Start with the smallest model that does the job; “the biggest that fits” is not the goal. LM Studio recommends 16 GB of memory or more and, on Windows, 4 GB of VRAM or more; a CPU with AVX2 is required on Windows.

---

### Slide 08 (29:00–33:00) • A GPU answers 2–25× faster than a CPU

**On screen:** Speed bars in tokens per second (laptop CPU, Apple M5, RTX 4050 Laptop, M5 Max, RTX 4090, H100) with a dashed 20 t/s line; “≥ 20 t/s” on the right; below, the wait for a half-page answer: 30 s / 9 s / 7 s / 1.6 s.

#### Speaker (4 min)
> Speed is measured in tokens per second; a token is a piece of a word, as in L02. The data are open llama.cpp measurements for a 7-billion-parameter model at 4 bits; for 8B multiply by about 0.7. A laptop CPU without a GPU gives roughly 5–15 tokens per second, our estimate: slow, but bearable for short answers.
>
> A gaming laptop with an RTX 4050 gives about 44, a base M5 Mac 32, a top M5 Max 120 (on a Mac the GPU is built into the chip and shares its memory). An RTX 4090 gives 186, a server H100 268; both can be rented, which is the second half of the lesson. People read about 4–7 tokens per second, so from 20 upwards (the dashed line) chat feels live. The bottom row shows it in seconds: a half-page answer of about 300 tokens takes a CPU half a minute and an RTX 4090 under two seconds. For batch work, such as 10,000 emails overnight, speed matters more, and that is where renting a GPU helps.
>
> Why the GPU is faster: a model is a huge number of multiplications, and a GPU does thousands of them at once and has very fast memory.

---

### Slide 09 (33:00–38:00) • LM Studio: a chat like ChatGPT, but the model runs on your machine

**On screen:** A detail of the official LM Studio screenshot (left chat, middle cut out) with callouts; legend Chat / Discover / model picker / Developer.

#### Speaker (5 min)
> LM Studio is a free app for running open models on your own computer. It looks like ChatGPT: a narrow section bar on the left, the conversation in the middle, the model picker under the input box. The difference: the model is downloaded to your disk and computed by your CPU or GPU. The slide shows a detail of the official screenshot: one of two chats with GLM-4.7-Flash.
>
> Main sections. Chat — the conversation. Discover — model search straight from Hugging Face; LM Studio tells you which files fit your memory. My Models — what is already downloaded. Developer — the local server, two slides from now. Since July 2025 LM Studio is free for work use too. The current version is 0.4.26 (October 2026).
>
> Do not confuse: the lmstudio.ai download page now offers LM Studio Bionic first — a separate agent app (released July 2026). The lesson needs the classic LM Studio, further down the download page. The alternative is Ollama, free, MIT licence; it is easy to drive with commands.

---

### Slide 10 (38:00–43:00) • Demo: download a small model and ask it a work question

**On screen:** Five demo steps on a line (find, download, load, ask, check speed), the ticket prompt, a sample good JSON answer and what to notice.

#### Speaker (5 min)
> Live demo. Before class download granite-4.2-3b at Q4_K_M (2.2 GB) so you do not depend on the internet. Five steps: Discover, search by name, Download on the Q4_K_M file, then in Chat pick the model in the bottom menu (it loads into memory in a few seconds) and send the prompt. On the right of the slide is what a good answer looks like: compare it with what the model returns. Fallback: if the Wi-Fi is slow, demo with the model downloaded in advance.
>
> The prompt is a work task from L03: extract the issue, urgency and next step from a ticket as JSON. For effect, turn off Wi-Fi before sending: the model still answers. Point at the speed line under the answer (tokens per second) and open Task Manager: you can see how much memory the model took.
>
> Question for the chat: is the answer worse or better than ChatGPT’s? A small model usually handles such a simple task but may get the format wrong. That is a fair price for 2 GB.

---

### Slide 11 (43:00–48:00) • Turn on the server and the model answers your code like a cloud API

**On screen:** The L03 Python code with the address and model name highlighted; on the right three settings: OpenAI, LM Studio, Ollama.

#### Speaker (5 min)
> The key slide for those who code. LM Studio’s Developer tab has a Start server toggle. After that the model is available at localhost:1234 and understands the same requests as the OpenAI API: chat/completions, responses, embeddings. There is also Anthropic API compatibility.
>
> On the left is the L03 code. Two lines change, highlighted in green: the address (base_url) and the model name. The local server needs no key; the library just wants some string. The /v1 at the end of the address is the API version, as at OpenAI; keep it as is. Ollama uses a different address, localhost:11434, but the idea is the same. So keep the address and model name in settings (a .env file), not in code: moving from the cloud to a laptop or to Runpod then means editing the address and model name, not the code.
>
> Caveat: “compatible” does not mean “identical”. A small model follows the JSON format less reliably and may not support tool calling. Test on your own task.

---

### Slide 12 (48:00–52:00) • A coding agent installs the model for you and measures the speed

**On screen:** Prompt for a coding agent (install Ollama, download a model, measure speed, localhost only) and three notes.

#### Speaker (4 min)
> A link to the coding-agent lessons. You do not have to install everything by hand: Codex, Antigravity or Claude Code will do it from a prompt like this. The steps are numbered so the agent skips nothing, and step 5 forbids exposing the server to the network. What a coding agent is and how to choose one: L16.
>
> Why Ollama rather than LM Studio: everything in Ollama can be done with commands (it also has a chat window, but you don't need it), which is easier for an agent. It is open-source under the MIT licence; version 0.40.5 from 14 October 2026. The Ollama server runs on localhost:11434 and also understands OpenAI-style requests. LM Studio has the lms command-line tool, and llmster for servers without a screen.
>
> Important: the agent will propose install commands. Read them before approving; install only from official sites. This is an optional homework path.

---

### Slide 13 (52:00–56:00) • “Local” does not automatically mean “private”: check the whole data path

**On screen:** Four-point data-path traffic light: local compute, downloads, plug-ins, network-exposed server; on the right the class rule.

#### Speaker (4 min)
> A common mistake: I installed the model locally, so everything is private. The generation itself does stay on the computer. But around it there is a data path. Downloading the model and updates use the internet. If you connect plug-ins (MCP servers in LM Studio) or web search, they may send data out.
>
> The most dangerous item is red: if you enable “Serve on local network” in LM Studio, other computers on the network can reach the model. For this case the server settings have Require Authentication: access by token only. For class and homework keep the server on localhost only.
>
> And the source: download model files from known publishers (IBM, Google, Alibaba Qwen, Microsoft, OpenAI, the lmstudio-community group). Unknown repacks may be tampered with.

---

### Slide 14 (56:00–60:00) • Open models by size: what runs where

**On screen:** Three lists of models with licences under coloured headers: GPU up to 8 GB, 16–24 GB, server.

#### Speaker (4 min)
> A map by size, not by ranking: what you can run on your hardware at all. Almost everything here is Apache-2.0: fine for work. Laptop: IBM Granite 4.2 (3B and 8B), Alibaba Qwen3.5 (4B and 9B), Google Gemma 4 (E4B and 12B), Mistral Ministral 3; Microsoft Phi-4 (14B, ≈ 9 GB) already needs a 12–16 GB GPU.
>
> One GPU with 16–24 GB: OpenAI’s gpt-oss-20b (the smaller of OpenAI’s two open models, 12 GB), Qwen3.8 27B, Gemma 4 31B, Granite 4.2 30B, Muse Glimmer 30B — Meta’s new open model. Server: DeepSeek V4.1 and Llama 4 are huge; they run on a cluster or via an API. Llama 4 and Qwen3.8-Flash-Next have custom licences with conditions: read them first.
>
> Names change every couple of months, so we teach the criteria: file size, licence, known publisher. Recheck the list before class.

---

### Slide 15 (60:00–65:00) • 5 minutes: grab a coffee while the model downloads

**On screen:** 5-minute break timer.

#### Speaker (5 min)
> Press “Start”. You can suggest students install LM Studio and start downloading a small model.

---

### Slide 16 (65:00–68:00) • When a laptop is not enough: four signs

**On screen:** Four signs a laptop is not enough, and the fix: the same model on a cloud GPU.

#### Speaker (3 min)
> A laptop is good for trying things, for one person and for offline work. Four signs it is time to move on. The model does not fit in memory. You need speed: say, process 10,000 emails overnight. Many simultaneous users: a laptop answers one at a time. It must run around the clock.
>
> Then you do not have to jump straight to a cloud API. You can keep the same open model, the same licence and the same code, and rent a GPU. The most beginner-friendly service is Runpod.

---

### Slide 17 (68:00–73:00) • Runpod: a GPU rented with per-second billing, two modes

**On screen:** A large crop of Runpod Community pricing, the 24 GB rows (RTX 4090 $0.34/h highlighted), and a day timeline: Pod vs Serverless; the Stop trap.

#### Speaker (5 min)
> Runpod is a GPU cloud billed per second. On the left is the pricing page (updated 8 October, captured 16 October) in Community Cloud mode, partners’ machines: an RTX 4090 with 24 GB costs $0.34 per hour, an RTX 3090 $0.22. Secure Cloud, in certified data centres, costs more: for example an L40S is $1.09 versus $0.79. On the right, one working day of a support bot in both modes.
>
> Two modes. A Pod is like your own computer in the cloud: pick a GPU and a ready template (for example PyTorch), connect via the browser (web terminal, JupyterLab) or SSH, install Ollama or vLLM, and work. You pay for every second it is on, including while you are off getting coffee. Serverless is for apps: the GPU wakes when a request arrives and sleeps without them. The first request after sleep waits for the model to load (cold start).
>
> The main beginner trap: Stop does not fully stop billing. A stopped Pod’s disk costs $0.20 per GB per month. When done — Terminate. And mind the spend limit: by default it is $80 per hour across all resources. For learning, top up only a small amount, but watch it: at a zero balance the Pod stops, and without a network volume it is deleted together with its data. In this lesson Runpod is shown on screenshots; launching one yourself is optional and paid.

---

### Slide 18 (73:00–78:00) • Renting a GPU only pays off if it is busy all the time

**On screen:** Hourly price of five GPUs on the left (A100 and H100 are SXM); on the right the price of 1M tokens on an RTX 4090 at 100 / 50 / 25 / 10% busy: $0.73 / $1.45 / $2.91 / $7.27 against a violet cloud band of $0.40–4.50.

#### Speaker (5 min)
> Hourly prices in Runpod Community Cloud: RTX 4090 $0.34, RTX 5090 $0.69, L40S $0.79, A100 SXM $1.39, H100 SXM $2.69 (SXM is the server-board version; the PCIe variant is cheaper). Secure Cloud is roughly 1.3–2.6× more. Serverless costs more per hour (RTX 4090 about $1.10), but you pay only for seconds of work.
>
> Compare with a cloud API. An RTX 4090 with an 8B model gives about 130 tokens per second, about 470 thousand tokens per hour. At $0.34 per hour that is about $0.73 per million tokens, but only if the card is busy non-stop. Cheap cloud models cost $0.40–4.50 per million output tokens and charge nothing for idle time.
>
> If the card is busy only 10% of the time, the same million tokens costs about $7.27, more than the cloud. Takeaway: money-wise your own model wins only with a large, steady stream of work. More often it is chosen for privacy, version control and offline work. That is the honest answer to “isn’t it cheaper?”. Caveat: $0.73 is the single-user worst case. A server with batching (for example vLLM) handles many requests at once, so total throughput, and with it the price per million tokens, gets several times better.

---

### Slide 19 (78:00–82:00) • Choose by two questions: can the data leave, and how much work is there

**On screen:** 2×2 grid (data may leave / must stay × few / many requests): cloud API ×2, your laptop, Runpod (Pod or Serverless); a note on Secure Cloud.

#### Speaker (4 min)
> Everything comes down to two questions. One: may the data go to the model vendor? If yes and the task is hard — a cloud API: best quality, pay for use. If no — your own model. Two: how much work? One person and a few tasks — a laptop. Requests in bursts, such as a daytime support bot — Serverless. A large steady flow or model experiments — a Pod.
>
> Chat exercise (1 min): a lawyer wants to search client contracts, 20 queries a day. What to choose? Answer: a laptop or workstation with a local model; the data is sensitive and the volume small.

---

### Slide 20 (82:00–87:00) • Homework: run a model yourself and compare it honestly with the cloud

**On screen:** Five homework steps, the genai-homeworks/L10/ submission folder, a tip for weak computers.

#### Speaker (5 min)
> Homework for the week. Install LM Studio or Ollama, download a 3–9B model at Q4. Give it three tasks from your work (on synthetic data): for example, classify an email, summarise, reply to a customer. Give the same tasks to ChatGPT or Gemini.
>
> Record the speed and memory used (a screenshot), score the answers 1 to 5 and conclude which tasks a local model is good for. Finally a decision card: API, laptop, Pod or Serverless for your task, and why. Grading looks at an honest comparison, not at which model won. Details and criteria are in L10_05_Homework.

---

### Slide 21 (87:00–90:00) • Your own model is a file and memory; in code only the address and model name change

**On screen:** Four lesson rules and the L11 preview.

#### Speaker (3 min)
> Four rules. An open model is a file and a licence: find it on Hugging Face and read the card. Fit the size to memory: Q4 plus a 25% margin must fit the GPU. LM Studio or Ollama give you a server on localhost, and only the address and model name change in code; never expose the server, because local does not mean private. On Runpod idle time costs money too: when done — Terminate.
>
> Next lesson: function calling. The model learns not only to answer in text but to call tools: search, compute, send. That is the first step towards agents.

---
