# L10 Source Notes: Open Models, LM Studio, Local Inference and RunPod (research 2026-10-16)

Primary sources checked on 2026-10-16 for the v2 rebuild of Lesson 10. Replaces the September 2026 Drive package source notes (`10 — Open Models, LM Studio, Local Inference and RunPod — DONE/L10_08_Source_Notes_READY.docx`).

## Images used in the deck

| File | What | Source |
|---|---|---|
| `assets/v2/img/hf_granite_header.png`, `hf_granite_files.png` | Hugging Face page and file list of `ibm-granite/granite-4.2-8b-GGUF` | own capture 2026-10-16, https://huggingface.co/ibm-granite/granite-4.2-8b-GGUF/tree/main |
| `assets/v2/img/lmstudio_app.png` | LM Studio app with two chats (GLM-4.7-Flash) | official image, credit "LM Studio / Element Labs", https://lmstudio.ai/assets/marketing/blog/0.4.0/app-screen.png (0.4.0 release blog, Jan 2026) |
| `assets/v2/img/runpod_pricing_community.png` | Runpod pricing page, Pods, Community Cloud (RTX 4090 $0.34/hr row highlighted on the slide), page "Updated October 8, 2026" | own capture 2026-10-16, https://www.runpod.io/pricing |

Schematics (cover, slide 2 "three places", slide 5 "five parts") are drawn in HTML/SVG inside `deck_v2/build.py` with RU/EN labels; the earlier genai-assets PNGs (`hook_three_places.png`, `cover_right.png`, `five_layers.png`, `five_layers_crop.png`) and the unused reference capture `lmstudio_bionic_home.png` were removed in the final audit round (2026-10-16).

LM Studio itself was not installed for this rebuild (owner decision 2026-10-16), so there are no own LM Studio screenshots; replace `lmstudio_app.png` with an own capture of LM Studio 0.4.x when available.

---

All facts checked on **2026-10-16** unless marked otherwise. Primary sources only. **UNVERIFIED** = could not confirm from a primary source.

---

## 1. LM Studio

| Fact | Value | Source |
|---|---|---|
| Current desktop version | **LM Studio 0.4.26** (Build 5), released **October 13, 2026**. Updated llama.cpp runtime 2.50.0; added `/v1/decisions`; can run alongside Bionic. | https://lmstudio.ai/download ; https://lmstudio.ai/changelog/lmstudio-v0.4.26 |
| Big recent milestones | 0.4.0 (Jan 28, 2026): server deployment / llmster, parallel requests with continuous batching, new REST API, refreshed UI. | https://lmstudio.ai/blog/0.4.0 |
| **New product to be aware of** | **LM Studio Bionic** (launched Jul 16, 2026) is a *separate* "AI agent for open models" app (coding, documents, voice, optional cloud models). The download page now offers **two downloads**: Bionic and "LM Studio" (the classic app). The `/changelog` page lists mostly Bionic releases (Bionic 1.1.8, Oct 12, 2026). Bionic runs local models on the LM Studio runtime. **For the lesson, use the classic LM Studio app**, and mention Bionic in one line so students aren't confused on the download page. | https://lmstudio.ai/blog/introducing-lm-studio-bionic ; https://lmstudio.ai/download |
| Pricing page | The pricing page is now about Bionic: Free $0 (local models, LM Link up to 5 devices), Bionic+ $20/mo, Pro $100/mo (US-hosted cloud open models such as Kimi K3, GLM 5.3, DeepSeek V4 Flash). Running local models stays free. | https://lmstudio.ai/pricing |
| OS: macOS | Apple Silicon only (M1/M2/M3/M4); **macOS 14.0+**; 16 GB+ RAM recommended (8 GB Macs work with small models and modest context); **Intel Macs not supported**. | https://lmstudio.ai/docs/app/system-requirements |
| OS: Windows | x64 and ARM (Snapdragon X Elite); **AVX2 required** on x64; **16 GB RAM recommended**; **4 GB+ dedicated VRAM recommended**. | same |
| OS: Linux | x64 and ARM64 (aarch64); AppImage; Ubuntu 20.04+ (versions newer than 22 "not well tested"); x64 ships with AVX2 by default. No RAM figure is given for Linux. | same |
| Engines | GGUF via llama.cpp (Mac/Win/Linux); MLX on Apple Silicon. | https://lmstudio.ai/docs/app |
| Main UI tabs (names in current docs) | **Chat** tab (load model + chat), **Discover** tab (search/download, shortcut Ctrl+2 / Cmd+2), **Developer** tab (start the server: toggle "Start server"), **My Models** tab (models folder). UI modes: **User** (chat only, auto-config) vs **Developer** (all advanced settings; it replaced the old Developer + Power User modes). | https://lmstudio.ai/docs/app/basics ; https://lmstudio.ai/docs/app/basics/download-model ; https://lmstudio.ai/docs/developer/core/server ; https://lmstudio.ai/docs/cli ; https://lmstudio.ai/docs/app/user-interface/modes |
| Quantization guidance (docs) | "Choose a 4-bit option or higher if your machine is capable enough." | https://lmstudio.ai/docs/app/basics/download-model |
| Local server default | `http://localhost:1234` (docs: "Once the server is running, it listens on http://localhost:1234"). The port can be changed in Server Settings or with `lms server start --port N`. If you leave out `--port`, it uses the last port you used. | https://lmstudio.ai/docs/app/basics/lmstudio-vs-llmster-vs-lms ; https://lmstudio.ai/docs/cli/serve/server-start ; https://lmstudio.ai/docs/developer/core/server/settings |
| OpenAI-compatible endpoints | `GET /v1/models`, `POST /v1/responses`, `POST /v1/chat/completions`, `POST /v1/embeddings`, `POST /v1/completions` (legacy), plus a new `POST /v1/decisions`. Base URL: `http://localhost:1234/v1`. | https://lmstudio.ai/docs/developer/openai-compat |
| Other API families | Native REST API (chat, list/load/unload/download models), **Anthropic-compatible** Messages endpoint, "Jev (TypeSafe AI)-compatible" endpoint, and SDKs lmstudio-python and lmstudio-js. | https://lmstudio.ai/docs/developer/core/server |
| Server settings | Server Port; **Require Authentication** (API token in the Authorization header); **Serve on Local Network**; per-request MCP options. | https://lmstudio.ai/docs/developer/core/server/settings |
| `lms` CLI | Installed with the app (you must run the app once first) or with llmster. **MIT licensed** (github.com/lmstudio-ai/lms). Key commands: `lms get <model>`, `lms ls`, `lms load <model> [--gpu=max\|auto\|0.0-1.0] [--context-length=N] [--identifier=name]`, `lms ps`, `lms unload [--all]`, `lms server start/stop/status`, `lms chat`, `lms log stream`, `lms daemon up/down/status`, `lms runtime`. | https://lmstudio.ai/docs/cli ; https://api.github.com/repos/lmstudio-ai/lms |
| Headless: **llmster** | "LM Studio's headless daemon": runs with no GUI on Linux servers, cloud/GPU boxes, CI, or as a boot service. You don't need the desktop app. Install: `curl -fsSL https://lmstudio.ai/install.sh \| bash` (Mac/Linux), `irm https://lmstudio.ai/install.ps1 \| iex` (Windows). Then `lms get` → `lms load` → `lms server start` → `curl http://localhost:1234/v1/models`. **This is a good fit for the Runpod segment** (same API on a rented GPU). | https://lmstudio.ai/download ; https://lmstudio.ai/docs/app/basics/lmstudio-vs-llmster-vs-lms ; https://lmstudio.ai/docs/developer/core/headless_llmster |
| Licence / work use | Free for home **and work** since **Jul 8, 2025**: "no need to fill a form or contact us." The app terms grant a "non-exclusive, non-transferable license to use the Software solely for Your personal and / or internal business purposes". The app is proprietary (closed source); only lms and the SDKs are MIT. Each model has its **own** licence, separate from the app. | https://lmstudio.ai/blog/free-for-work ; https://lmstudio.ai/app-terms |
| Official images (use with credit "Image: LM Studio / Element Labs") | App screenshot from the 0.4.0 blog (Jan 2026 UI, may differ slightly from 0.4.26): https://lmstudio.ai/assets/marketing/blog/0.4.0/app-screen.png (HTTP 200, PNG). Also in that post: `.../0.4.0/llmster@2x.png`, `daemon@2x.png`, `tokens@2x.png` (they redirect, 307). App logo: https://lmstudio.ai/assets/marketing/lmstudio-app-logo.webp . Brand kit: https://lmstudio.ai/brand (downloads are under their usage terms). The docs pages for Chat/Discover/Server have **no screenshots**. **Recommendation:** take your own screenshots of 0.4.26 on synthetic data. | https://lmstudio.ai/blog/0.4.0 ; https://lmstudio.ai/brand |

## 2. Ollama (alternative, one line)
**Ollama**: an open-source CLI and background service that pulls and runs open models locally. It serves an OpenAI-compatible API at `http://localhost:11434/v1/` (chat/completions and responses). **MIT licence**. Latest release **v0.40.5 (2026-10-14)**. It also offers optional cloud models.
Sources: https://github.com/ollama/ollama (API: license MIT) ; https://github.com/ollama/ollama/releases/latest ; https://github.com/ollama/ollama/blob/main/docs/openai.mdx

## 3. Open-weight LLMs (Oct 2026): newest versions, sizes, licences
Source for each row: the Hugging Face API `https://huggingface.co/api/models/<id>` (cardData.license, safetensors.total), checked 2026-10-16.

| Family | Newest relevant release | Sizes (params) | Licence | Laptop / single-GPU fit |
|---|---|---|---|---|
| **Qwen (Alibaba)** | **Qwen3.8** (Aug 2026): `Qwen3.8-27B` (27.8B dense); `Qwen3.8-Flash-Next` (~180B); `Qwen3.8-2.4T-A95B`. Small sizes come from **Qwen3.5** (Feb 2026): 0.8B, 2B, 4B (4.66B), 9B (9.65B), 27B, 35B-A3B, 122B-A10B, 397B-A17B. **Qwen3.6** (Apr 2026): 27B, 35B-A3B. | as listed | 3.8-27B, 3.5-*, 3.6-*: **Apache-2.0**. 3.8-Flash-Next: **custom "qwen-community-1.0"**. 3.8-2.4T: custom "qwen3.8-max" | Laptop: Qwen3.5-4B / 9B. 24 GB GPU: Qwen3.8-27B Q4. 24–32 GB: Qwen3.6-35B-A3B Q4 |
| **Gemma (Google)** | **Gemma 4** (Mar–May 2026): E2B, E4B (~8.0B total incl. embeddings, "effective 4B"), 12B (11.96B, May 2026), 26B-A4B (MoE), 31B. Official QAT Q4_0 GGUFs (Jun 2026). | as listed | **Apache-2.0** (HF card tag; Gemma 3 used the custom Gemma terms) | Laptop: E4B, 12B. GPU: 26B-A4B, 31B |
| **Llama (Meta)** | **Llama 4** Scout 17B-16E (109B total) / Maverick 17B-128E (Apr 2025). No newer Llama on HF. Meta's newer open models use the **"Muse" brand**: `Muse-Glimmer-30B` (29.8B, Aug 2026), `Muse-Spark-Open-816B-A42B` (Sep 2026). | as listed | Llama 4: **custom Llama 4 licence, gated**. Muse Glimmer 30B: **Apache-2.0**. Muse Spark Open: **custom "muse-model-license", gated** | Llama 4 is too big for a laptop. Muse Glimmer 30B Q4_K_M = 16.76 GB (fits a 24 GB GPU) |
| **Mistral** | **Ministral 3** (2512): 3B, 8B (8.9B), 14B (Instruct, Reasoning, Base; official GGUF). **Mistral Small 4** 119B (2603). Mistral Medium 3.5 128B (Mar 2026). | as listed | Ministral 3, Small 4: **Apache-2.0**. Medium 3.5: licence not checked (**UNVERIFIED**) | Laptop: Ministral 3 3B/8B/14B |
| **IBM Granite** | **Granite 4.2** (Aug 2026): 3B (3.66B), 8B (8.79B), 30B (29.3B). Official GGUF, MLX, FP8, NVFP4. (Granite 4.1 Apr 2026; the old deck used Granite 4.0 Micro.) | as listed | **Apache-2.0** | **Good classroom default: granite-4.2-3b** (2.24 GB Q4_K_M) |
| **gpt-oss (OpenAI)** | gpt-oss-20b (20.9B, MoE) and gpt-oss-120b (116.8B), Aug 2025. Still the newest OpenAI open-weight LLMs on HF. | as listed | **Apache-2.0** | 20b MXFP4 GGUF = 12.11 GB (16 GB GPU or 16–24 GB Mac); this is the model the LM Studio docs use in their examples |
| **Phi (Microsoft)** | Newest is still **phi-4** (14.7B, Dec 2024) and Phi-4-mini / mini-reasoning (2025). No Phi-5 on HF. Microsoft's newer small models have other names (for example FrogNano-4B-2609, MIT). | as listed | **MIT** | Phi-4 14B Q4 fits a laptop with a GPU; it's dated, so treat it as optional |
| **DeepSeek** | **DeepSeek-V4.1-Flash** (Sep 2026, ~763B total), **V4-Pro-0813** (~1.65T) | huge MoE | **MIT** | **Not** for laptop or single GPU. Use the API or a multi-GPU cluster |

### 3b. Real GGUF file sizes (HF API `?blobs=true`, checked 2026-10-16; GB = 10^9 bytes)

| Model (repo) | Q4_K_M | Q8_0 | Other |
|---|---|---|---|
| **granite-4.2-3b** (`ibm-granite/granite-4.2-3b-GGUF`) | **2.24 GB** | **3.89 GB** | Q4_0 2.13; bf16 7.32 |
| Qwen3.5-4B (`unsloth/Qwen3.5-4B-GGUF`) | 2.74 GB | 4.48 GB | + mmproj 0.68 for vision |
| gemma-4-E4B-it (`lmstudio-community/gemma-4-E4B-it-GGUF`) | 5.34 GB | 8.03 GB | + mmproj 0.99 |
| **granite-4.2-8b** (`ibm-granite/granite-4.2-8b-GGUF`) | **5.35 GB** | **9.35 GB** | bf16 17.59 |
| Qwen3.5-9B (`lmstudio-community/Qwen3.5-9B-GGUF`) | 5.63 GB | 9.53 GB | + mmproj 0.92 |
| gemma-4-12B-it (`lmstudio-community/gemma-4-12B-it-GGUF`) | 7.38 GB | 12.67 GB | Google official QAT Q4_0: 6.98 GB (`google/gemma-4-12B-it-qat-q4_0-gguf`) |
| gpt-oss-20b (`lmstudio-community/gpt-oss-20b-GGUF`) | n/a | n/a | MXFP4 (native) 12.11 GB |
| Qwen3.8-27B (`lmstudio-community/Qwen3.8-27B-GGUF`) | 16.81 GB | 29.05 GB | |
| **granite-4.2-30b** (`ibm-granite/granite-4.2-30b-GGUF`) | **17.72 GB** | **31.11 GB** | bf16 58.6 (2 parts) |
| Qwen3.6-35B-A3B (`lmstudio-community/Qwen3.6-35B-A3B-GGUF`) | 21.17 GB | 36.90 GB | |

Teaching point: Q8_0 is about 1.7× the size of Q4_K_M. One family (Granite 4.2: 3B / 8B / 30B, all Apache-2.0, official GGUF) gives a clean 3-row example: **2.2 / 5.4 / 17.7 GB** at Q4_K_M, and the file size is not the whole memory need (KV cache comes on top).

## 4. Open vs closed quality gap (one data point)
**Artificial Analysis Intelligence Index v4.3.2** (10 evals), page read 2026-10-16:
- Top overall: **Claude Opus 5.5 (max) = 58** (proprietary). Next: Claude Sonnet 5.5 56, Meta "Muse Wonder Full" 56, GPT-6 Astra 53, Gemini 4 Argon 53.
- Top open-weights: **MiMo-V2.6-Pro (Xiaomi) = 46**, GLM-5.3 (max) 45, Step 5 Preview 44, Kimi K3 (max) 44, DeepSeek V4.1 Flash 39, Qwen3.8 27B 34.
- So the gap is **~12 index points** between the best closed and best open models. Open models that fit a single GPU (for example Qwen3.8 27B at 34) are ~24 points behind the top.
Sources: https://artificialanalysis.ai/models/open-source ; https://artificialanalysis.ai/leaderboards/models (neither page shows a date; the date checked is 2026-10-16). LMArena (now arena.ai) blocked automated access (Cloudflare 403), so there is **no LMArena data point (UNVERIFIED)**.

## 5. Runpod (official styling is now "Runpod", not "RunPod", since June 2025, per the docs)

**Concepts**
- **Pods**: dedicated GPU instances (a container with a GPU, plus Jupyter/SSH). **Secure Cloud** runs in T3/T4 data centers. **Community Cloud** uses vetted peer-to-peer providers and is cheaper. Pricing options: **On-demand** or **Savings plan** (3 or 6 months prepaid). Billed **per second** for compute and storage, with no ingress/egress fees. https://docs.runpod.io/pods/overview ; https://docs.runpod.io/pods/pricing
- **Serverless**: endpoints with workers that scale with requests. **Flex workers** scale to zero and pay the standard per-second rate. **Active workers** run 24/7, have no cold start, and get a discount through sales. Endpoint types: **queue-based** (`/run`, `/runsync`, handler functions) or **load-balancing** (direct HTTP). Defaults: Active workers 0, **Max workers 3**, **Idle timeout 5 s**, Execution timeout 600 s, FlashBoot on. You pay for cold start + execution + idle-timeout time. A scaled-down worker is not billed. https://docs.runpod.io/serverless/pricing ; https://docs.runpod.io/serverless/endpoints/endpoint-configurations
- Also: Clusters (multi-node), Hub, and Public Endpoints (pay-per-call models).

**Pod prices, on-demand $/hr** (pricing page "Updated October 8, 2026", JSON-LD offers) https://www.runpod.io/pricing

| GPU | VRAM | Community | Secure |
|---|---|---|---|
| RTX 4090 | 24 GB | **$0.34** | **$0.89** |
| RTX 5090 | 32 GB | $0.69 | $1.19 |
| L40S | 48 GB | $0.79 | $1.09 |
| A100 SXM 80GB | 80 GB | $1.39 | $1.79 |
| A100 PCIe 80GB | 80 GB | $1.19 | $1.79 |
| H100 PCIe | 80 GB | $1.99 | $2.89 |
| H100 SXM | 80 GB | $2.69 | $3.99 |
| (cheap) RTX 3090 / RTX A5000 | 24 GB | $0.22 / $0.16 | $0.50 / $0.27 |

**Serverless flex prices** (pricing page; the HTML marks these `data-price="flex"`). Per second = hourly ÷ 3600.

| Tier | $/hr (flex) | ≈ $/s |
|---|---|---|
| 24 GB 4090 PRO | $1.10 | ~$0.00031 |
| 24 GB L4/A5000/3090 | $0.69 | ~$0.00019 |
| 32 GB 5090 PRO | $1.58 | ~$0.00044 |
| 48 GB L40/L40S/6000 Ada PRO | $1.75 | ~$0.00049 |
| 80 GB A100 | $2.72 | ~$0.00076 |
| 80 GB H100 PRO | $4.79 | ~$0.00133 |

- **Active-worker prices: UNVERIFIED.** The pricing page only shows them after you click a toggle (JavaScript). The docs only say "Discounts available through sales inquiry".
- **Mismatch:** the docs table (endpoint-configurations) lists older per-second prices: 4090 PRO $0.00031, L40S $0.00053, A100 $0.00076, H100 PRO $0.00116. The 4090 and A100 match the pricing page; L40S and H100 do not. **Use the pricing page.**

**Storage** (https://docs.runpod.io/pods/pricing, last modified Jul 20, 2026; matches the pricing page)
- Container disk: $0.10/GB/mo while running. **Not charged when stopped**, and it is **erased when the Pod stops**.
- Volume disk: $0.10/GB/mo running, **$0.20/GB/mo when stopped**. Kept until the Pod is deleted.
- Network volume: $0.07/GB/mo (<1 TB), $0.05/GB/mo (>1 TB), the same whether stopped or running. High-performance tier $0.14/GB/mo.
- **Does stopping a Pod still bill? Yes, for storage.** Docs: "Storage charges continue to accrue on stopped Pods." The quickstart says "You'll still be charged a small amount for storage on stopped Pods ($0.20 per GB per month)... terminate it completely" if you don't need the data. https://docs.runpod.io/get-started

**Money / limits** (https://docs.runpod.io/get-started/billing-information)
- Prepaid credits, billed per second, charged every 5 min.
- **Minimum to deploy:** "at least one hour's worth of credits for your selected configuration". **No fixed minimum deposit is stated** in the docs (the old "$10 minimum" is **UNVERIFIED**). Prepaid cards should deposit at least $100.
- **Default spend limit: $80/hour** across all resources.
- At a $0 balance, Pods stop. Pods with a network volume keep their data. Pods **without** one are **terminated and their data is lost**.

## 6. Tokens/second (generation, tg128): APPROXIMATE
The benchmark model is **Llama 2 7B Q4_0 (3.56 GiB)**, llama.cpp `llama-bench`, community scoreboards maintained in the llama.cpp repo. An 8B Q4_K_M file (~5 GB) is ~1.4× bigger, so expect **about 0.7×** these numbers. Generation speed scales mostly with memory bandwidth ÷ model size.

| Hardware | 7B Q4_0 tg (t/s) | ≈ 8B Q4_K_M (est.) | Source |
|---|---|---|---|
| Laptop CPU only (DDR4/DDR5, dual channel) | no official scoreboard | **~5–15 t/s (UNVERIFIED; estimated from ~50–100 GB/s ÷ ~5 GB)** | none |
| RTX 4050 Laptop 6 GB | 43.7 | ~30 | https://github.com/ggml-org/llama.cpp/discussions/15013 |
| RTX 4060 Ti 8 GB (desktop) | 63.9 | ~45 | same |
| RTX 3060 12 GB (desktop) | 75.6 | ~50 | same |
| (8 GB *laptop* RTX 3060/4060: not on the scoreboard) | n/a | **~35–50 (UNVERIFIED; between the 4050 Laptop and 4060 Ti)** | none |
| Apple M1 / M2 / M3 / M4 (base) | 14.2 / 21.7 / 21.3 / 24.1 | ~10–17 | https://github.com/ggml-org/llama.cpp/discussions/4167 |
| Apple M4 Pro (20-core GPU) | 50.7 | ~35 | same |
| Apple M4 Max (40-core GPU) | 83.1 | ~58 | same |
| Apple M5 (10-core GPU) / M5 Max (40-core GPU) | 31.9 / 119.9 | ~22 / ~84 | same |
| RTX 4090 24 GB | 186.2 | ~130 | discussions/15013 |
| RTX 5090 32 GB | 290.0 | ~200 | same |
| H100 80 GB / A100 80 GB | 267.8 / 190.9 | ~185 / ~135 | same |

Both discussions were last updated 2026-10-01. These are single-user numbers. Servers like vLLM get much higher *total* throughput by batching many users.

## 7. API price comparison (per 1M tokens, standard paid tier)

| Model | Input | Output | Source (checked 2026-10-16) |
|---|---|---|---|
| Gemini 2.5 Flash-Lite | $0.10 | $0.40 | https://ai.google.dev/gemini-api/docs/pricing (page "Last updated 2026-10-15") |
| Gemini 3.1 Flash-Lite | $0.25 | $1.50 | same |
| Gemini 3.5 Flash-Lite (newest Lite) | $0.30 | $2.50 | same (Batch/Flex half price: $0.15 / $1.25) |
| OpenAI gpt-6-luna (newest small tier) | $0.10 | $0.50 | https://developers.openai.com/api/docs/pricing |
| OpenAI gpt-5.4-mini / gpt-5.4-nano | $0.75 / $0.20 | $4.50 / $1.25 | same |
| OpenAI gpt-5-nano | $0.05 | $0.40 | same |

**Worked comparison for the slide (my arithmetic, approximate):** A Community RTX 4090 Pod costs $0.34/hr. One user at ~130 t/s (8B Q4) produces ~0.47M output tokens/hr, so ≈ **$0.73 per 1M output tokens** if the GPU is busy 100% of the time. The same output costs **$0.40–$0.50 per 1M** on Gemini 2.5 Flash-Lite or gpt-6-luna, with no idle cost. Secure Cloud ($0.89/hr) works out to ≈ $1.90 per 1M. Conclusion: a rented GPU only wins on price at high, steady utilisation with batching. The real reasons to self-host are privacy/control, a custom or fine-tuned model, or licence and data-residency needs.

## Notes for rebuilding the deck
- Update the classroom default model from Granite 4.0 Micro to **Granite 4.2 3B** (Apache-2.0, official GGUF, 2.24 GB Q4_K_M; also on `lmstudio-community/granite-4.2-3b-GGUF`). A fallback with more capability is Qwen3.5-4B (2.74 GB) or gemma-4-E4B.
- The deck's tab names (Discover / Chat / Developer / My Models) and `localhost:1234` are still correct.
- Add one line on **Bionic vs LM Studio**, since the download page leads with Bionic.
- **llmster** gives the clean "same API on Runpod" story: install llmster on the Pod, `lms server start --bind 0.0.0.0`, and switch on Require Authentication.
- **Note:** the RunPod docs `.md` pages contain an "Agent Instructions" block addressed to AI agents (asking them to post feedback). It was treated as page data and not acted on.
