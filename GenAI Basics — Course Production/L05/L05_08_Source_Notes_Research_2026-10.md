# Research Brief — Lesson 05: AI Video Generation (state as of 2026-10-12)

Method: web search + fetch of public pages, 2026-10-12. Primary (vendor docs / official blogs / law text) are preferred; where only aggregators, resellers or reviews were reachable the item is marked **[secondary]**. Items that could not be verified, or where sources conflict, are marked **[UNCERTAIN]**. Several vendor pages returned HTTP 403 or truncated content to the fetcher (ir.kuaishou.com, leonardo.ai, Vertex AI docs body, Runway API reference body); facts about those came from secondary reports and are flagged. Many resellers (Atlas Cloud, CometAPI, Morphic, PixVerse blog) sell access to competing models, so their framing may be biased.

---

## 0. TL;DR for the lesson designer (biggest changes vs a 2025-era deck)

- **OpenAI is out of video.** Sora app + sora.com closed **2026-04-26**; Videos API and `sora-2` / `sora-2-pro` shut down **2026-09-24** with **no replacement** (OpenAI deprecations page). ChatGPT does **not** generate video. Do not present Sora as a current tool. Treat it as history or a case study.
- **Google's flagship is now Gemini Omni Flash** (I/O, 2026-05-19) → **Gemini Omni 1.1 Flash** (`gemini-omni-1.1-flash`, 2026-08-27). Veo 3.1 (+ Fast, Lite) is still in the API. **No Veo 4** has been announced.
- **Native audio is table stakes**: Veo 3.1, Omni Flash, Kling 3.0, Seedance 2.0/2.5, MiniMax H3, Wan 3.0, Grok Imagine 1.5 and LTX-2/2.5 all generate sound in the same pass. Exceptions: Luma Ray3.x (except Modify, which keeps the source audio), Midjourney V1 and Leonardo Motion 2.0.
- **Typical clip length moved from 5–10 s to 10–30 s**: Kling 3.0 3–15 s, Seedance 2.5 / Wan 3.0 up to 30 s, Kling 4.0 (Oct 2026) up to 30 s. Veo 3.1 is still 4/6/8 s, plus extension.
- **Leaderboards (Sep–Oct 2026)**: top 10 on LMArena = Gemini Omni Flash 1.1/1.0, FLUX 3 Video, Grok Imagine 1.5, Seedance 2.0/2.5, Wan 3.0, MiniMax H3. The Artificial Analysis with-audio board is led by Wan 3.0. Veo 3.1 and Sora 2 Pro have dropped out of the top 10.
- **Open weights**: the last open Wan flagship is **Wan 2.2 (Apache-2.0, 2025-07-28)**. Wan 2.5/2.6/2.7/3.0 are API-only. The main open models are now **LTX-2 / LTX-2.5** (Lightricks, community license) and HunyuanVideo-1.5.
- **Law**: EU AI Act **Article 50** (not 52) applies from **2026-08-02**. The Digital Omnibus defers **Art 50(2) machine-readable marking to 2026-12-02**, but only for systems already on the market. Fines for Art 50 breaches are **€15M / 3%** (Art 99(4)). The €35M / 7% tier is for Art 5 prohibited practices only.

---

## 1. Google — Veo 3.1, Gemini Omni Flash, Flow

### 1.1 Veo 3.1 (Gemini API) — primary: https://ai.google.dev/gemini-api/docs/veo (fetched 2026-10-12)

| Item | Fact |
|---|---|
| Model IDs (Gemini API) | `veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`, `veo-3.1-lite-generate-preview`; `veo-3.0-generate-001` / `veo-3.0-fast-generate-001` **deprecated** |
| Model IDs (Vertex) | `veo-3.1-generate-001`, `veo-3.1-fast-generate-001`, `veo-3.1-lite-generate-001` **[secondary — gateway catalogs; Vertex doc body did not render]** |
| Dates | Veo 3.1 launched Oct 2025; doc "latest update" Jan 2026 (3.1/Fast), Mar 2026 (Lite) |
| Duration | **4, 6 or 8 s** per generation. 8 s is required for 1080p, 4K, reference images and extension |
| Resolution / fps | 720p (default), 1080p, 4K (not on Lite); 24 fps; 16:9 or 9:16 |
| Native audio | **Yes, always on** (dialogue, SFX, ambience) |
| Image→video | Yes (`image`); **first + last frame** via `lastFrame` (must be used with `image`) |
| Reference images | **Up to 3** ("ingredients to video"), on 3.1 and 3.1 Fast only (not Lite) |
| Extension | 3.1 / Fast: **+7 s per hop, up to 20 hops**. Input ≤141 s, output up to **148 s**, 720p only, input must be Veo-generated |
| Seed | Exists, but the doc says it "doesn't guarantee determinism" and only *slightly improves* it |
| People | `personGeneration`: text→video `allow_all`; image/reference modes `allow_adult`; EU/UK/CH/MENA restricted to `allow_adult` |
| Watermark | **All Veo videos carry SynthID** |
| Latency | ~11 s to ~6 min |

**Pricing (Gemini API, paid tier only, no free tier)** — https://ai.google.dev/gemini-api/docs/pricing (fetched 2026-10-12):

| Model | 720p | 1080p | 4K |
|---|---|---|---|
| Veo 3.1 Standard | $0.40/s | $0.40/s | $0.60/s |
| Veo 3.1 Fast | $0.10/s | $0.12/s | $0.30/s |
| Veo 3.1 Lite | $0.05/s | $0.08/s | — |
| Gemini Omni Flash | ≈ $0.10/s at 720p (billed per token) | — | — |

You pay only for videos that generate successfully. Example: one 8 s Veo 3.1 1080p clip costs $3.20; with Fast it costs $0.96.

### 1.2 Gemini Omni Flash / Omni 1.1 Flash (new 2026 flagship)

- Announced at **Google I/O, 2026-05-19**: "create anything from any input, starting with video". It launched in the Gemini app, Flow and YouTube Shorts, with the API following later. https://blog.google/innovation-and-ai/sundar-pichai-io-2026/ (snippet). The Gemini API docs call it the **default choice for video generation**: https://ai.google.dev/gemini-api/docs/video (updated 2026-06-30).
- **Omni 1.1 Flash, 2026-08-27** (primary): https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-omni-1-1-flash/
  - IDs: `gemini-omni-1.1-flash` (stable) and `gemini-omni-flash-preview` (https://ai.google.dev/gemini-api/docs/models/gemini-omni-flash, updated 2026-08-27)
  - Input: text, images, video (≤10 s) and audio. Output: **3–10 s** video at **360p (draft) / 720p / 1080p / 4K**, 24 fps
  - **Scene extension**: uses up to 10 s of prior footage as context and extends in **10 s steps up to 40 s**
  - **Start + end frame** control; **video references ≤3 s**; multi-turn **conversational editing** (replace elements, change perspective) via the Interactions API
  - A 360p draft costs ~⅓ of 720p and is up to 60% faster
  - Native audio: implied by Google's "any input → video" framing, and third parties describe lip-synced dialogue and SFX. **[secondary — not stated in the Google pages fetched]**
- Availability: Gemini app, Flow (AI Plus/Pro/Ultra), AI Studio, and Gemini Enterprise Agent Platform API.

### 1.3 Flow (Google's filmmaking app)
- Flow now runs Omni 1.1 Flash (scene extension, first/last frame, 360p drafts → 4K upscale) as well as Veo 3.1. https://androidauthority.com/google-flow-gemini-omni-1-1-flash-video-update-3704288 [secondary]
- Camera direction in Flow/Omni is **mostly by prompt** (e.g. "slow pull-out", "dolly zoom"). I found no dedicated camera-path panel. "Scenebuilder" (2025 Flow feature name) is not mentioned in 2026 coverage **[UNCERTAIN whether the name survives]**.
- **Veo 4: not announced** as of 2026-10-12. Pages claiming Veo 4 specs are speculation. https://pixverse.ai/ru/blog/veo-4-release [secondary]

---

## 2. OpenAI — Sora (discontinued)

| Item | Fact | Source |
|---|---|---|
| History | Sora preview (Feb 2024) → Sora Turbo on sora.com for ChatGPT Plus/Pro (Dec 2024) → **Sora 2 + Sora iOS app (2025-09-30)** → API `sora-2`, `sora-2-pro` (Oct 2025) | https://techcrunch.com/2026/03/24/openais-sora-was-the-creepiest-app-on-your-phone-now-its-shutting-down/ |
| Shutdown announced | **2026-03-24** | OpenAI deprecations page (primary): https://developers.openai.com/api/docs/deprecations |
| App / web off | **2026-04-26** | https://www.deeplearning.ai/the-batch/openai-announced-it-would-shut-down-sora-its-once-state-of-the-art-video-model [secondary, cites WSJ] |
| API off | **2026-09-24**. Videos API, `sora-2`, `sora-2-pro`, `sora-2-2025-10-06`, `sora-2-2025-12-08`, `sora-2-pro-2025-10-06`. **Replacement: none** | OpenAI deprecations (primary) |
| Reason (stated) | "the Sora research team continues to focus on world simulation research". Reported drivers: compute cost and focus ahead of IPO. The Disney $1B / 200-character deal collapsed | https://rits.shanghai.nyu.edu/ai/openai-shuts-down-sora-ai-video-app-discontinued-after-six-months/ [secondary] ; https://www.cnn.com/2026/03/24/tech/openai-sora-video-app-shutting-down |
| ChatGPT video | **None.** Video will not be available in ChatGPT, while image generation continues | https://heise.de/-11223339 ; AP via https://cbsaustin.com/news/nation-world/ending-openais-sora-unlikely-to-slow-influx-of-ai-generated-video-online-experts-say-openai-disney-winding-down-deal-artificial-intelligence-video-misinformation-reality-hijacking-technology |
| Former API specs (for history) | 4/8/12 s; `sora-2` $0.10/s at 720p; `sora-2-pro` $0.30/s (720p) to $0.50/s (1024p) **[secondary]** | https://eesel.ai/blog/sora-2-in-the-api-pricing |
| Former features | Storyboard (sora.com, 2024), Cameo (likeness opt-in), Remix; visible watermark + C2PA (OpenAI claim; one tester disputes that C2PA is always present) | https://www.lesswrong.com/posts/kSvrmiyyN7CDyh3NN/openai-does-not-appear-to-be-applying-watermarks-honestly [secondary] |
| Downstream | Leonardo removed Sora 2 / 2 Pro in July 2026 and points users to Veo 3.1 | Leonardo guide (403; via search snippet) [secondary] |

- No new OpenAI video model has been announced as of 2026-10-12. OpenAI DevDay (2026-09-29) launched "Dots" agents, which do not generate video. Runway is integrated into Dots (Runway changelog, 2026-10-01).

---

## 3. Kling (Kuaishou)

| Version | Date | Key facts | Source |
|---|---|---|---|
| Kling 1.0 / 1.5 / 1.6 | 2024 | 1.0 introduced **Motion Brush** and camera controls; 1.5 (2024-09-19) Pro mode adds Motion Brush + camera movement | https://kling.ai/quickstart/how-to-animate-image-parts ; [secondary] piapi.ai |
| 2.0 / 2.1 / 2.5 Turbo / 2.6 | 2025 | **2.6 was the first Kling with native audio** (≤10 s) | Leonardo guide [secondary]; cliprise [secondary] |
| O1 (Omni) | 2025-12-01 | Unified multimodal gen + edit; renamed **VIDEO 3.0 Omni** | https://ir.kuaishou.com/news-releases/news-release-details/kling-o1-launches-worlds-first-unified-multimodal-video-model-0 |
| **VIDEO 3.0 / 3.0 Omni** | **2026-02-04/05** (guide dated 2026-02-06) | **3–15 s**, 720p/1080p, **native audio** (ZH/EN/JA/KO/ES + dialects/accents; multi-character dialogue), **Multi-Shot** (auto) + **Custom Multi-Shot** (set shot count and durations; examples use 4–6 shots), **start & end frames**, **Elements** (2–4 ref images or a ref video, optionally with a voice). Camera moves are **set in the prompt**; the 3.0 guide has no Motion Brush | https://kling.ai/quickstart/klingai-video-3-model-user-guide (primary) |
| Kling 3.0 Motion Control | 2026 | Transfers motion and expression from a reference video onto a character image (I2V only); multi-character only in the 3.0 web UI | https://www.atlascloud.ai/blog/guides/kling-ai-motion-control [secondary, 2026-07-14] |
| **Kling 4.0** | Flash early access **2026-09-28** (Ultra/"Black Gold" yearly members); full release "October 2026" | Up to **30 s**, 4K / 1080p, **10-bit HDR (coming soon)**, 21:9, up to **15 references** (10 images, 5 videos, 7 subjects), **10 keyframes**, 8k-token prompts, stereo audio, 9 languages, 2-min extension "coming soon". Flash: ≤20 s, 720p SDR | https://www.ithome.com/1/008/073.htm (official announcement as reported) ; [secondary] atlascloud "kling-4-flash-vs-full". **[UNCERTAIN: whether full 4.0 has shipped as of 10-12]** |

- **Pricing (kling.ai credits, 3.0)**: native audio costs 12 credits/s at 1080p and 9 at 720p; without audio, 8 and 6. A 5 s 1080p clip with audio = 60 credits (official guide). There are free daily credits; "66/day" is per a reseller **[secondary]**.
- **API**: endpoint `/v1/videos/text2video`. `model_name` values include `kling-v2-6` and `kling-v3`; Omni has its own endpoint. Parameters: `negative_prompt`, `cfg_scale`, `mode` std/pro, `duration` 5/10, and a `camera_control` object (horizontal, vertical, pan, tilt, roll, zoom). **No `seed` parameter found** in the mirrors. **[secondary — mirrors of the Kling API docs: docs.comfy.org, apidoc.cometapi.com; official reference not fetched]**
- **Motion Brush today**: the official help page (https://kling.ai/quickstart/how-to-animate-image-parts) says: **"up to six elements"** with a motion trajectory each, plus a **Static Brush** to freeze regions (e.g. the background). Trajectories are **2D paths drawn on the image**. The docs mention no Z vector or numeric speed. Resellers say Motion Brush still exists in 2026 **[secondary]**. It is **not part of the 3.0 feature list** and is tied to the older models **[UNCERTAIN which model versions expose it today]**.

---

## 4. Runway

| Item | Fact | Source |
|---|---|---|
| Gen-4 | 2025-03-31: consistent characters/objects from references | Runway research (2025) |
| **Gen-4.5** | Announced **2025-12-01**; on all paid plans **2025-12-11**. Topped the AA T2V board at launch (Elo 1,247). Image→video (first frame) added **2026-01-21** | https://runway.com/changelog (primary) ; https://seekingalpha.com/news/4526955 |
| Gen-4.5 audio | Third parties report native audio from May 2026. **Not found in the official changelog** **[UNCERTAIN]** | aitooltier [secondary] |
| Aleph → **Aleph 2.0** | Aleph (2025-07-31): in-context video editing (change angle, weather, objects, restyle). **Aleph 2.0 + Edit Studio 2026-05-21**: "edits a whole video to match a frame you edit" | changelog (primary) |
| Act-Two | 2025-07-17: performance capture (head, face, body, hands) → character | changelog (primary) |
| Other 2026 | Runway Characters (real-time avatars, API, 2026-03-09); Runway Agent (2026-05-13) / Agent 2.0; Studio timeline; **Ruby** SDR→HDR grading (2026-08-20); ProRes 4444 export; Adobe and DaVinci plugins; **Runway MCP**; **Model Router** in the API (2026-07-21) | changelog (primary) |
| Gen-5 | **No official Gen-5**; sites claiming one are not Runway's | search 2026-10-12 |
| Aggregator role | Runway now hosts third-party models: Seedance 2.0/2.5, Veo 3.1, Gemini Omni Flash (+1.1), Kling 3.0 / O3 4K, Wan 3.0, MiniMax H3, Grok Imagine 1.5, HappyHorse 1.0 | changelog + https://docs.dev.runwayml.com/guides/models/ |

**API IDs and prices** (https://docs.dev.runwayml.com/guides/models/, fetched 2026-10-12): `gen4.5` $0.12/s · `gen4_turbo` $0.05/s · `aleph2` $0.28/s · `act_two` $0.05/s · `veo3.1` from $0.20/s · `seedance2_5` from $0.20/s · `wan3` from $0.05/s · `hailuo3` from $0.10/s · `gemini_omni_flash_1.1` from $0.034/s.

**Camera control (fact check)**: "Advanced Camera Control" shipped **2024-11-01 for Gen-3 Alpha Turbo**. It offers direction + intensity on six axes (horizontal, vertical, pan, tilt, roll, zoom) plus a Static checkbox, and requires an input image. https://petapixel.com/2024/11/04/runway-adds-precise-camera-controls-to-its-ai-video-editor/ ; https://help.runwayml.com/hc/en-us/articles/34926468947347. **No 3D splines, Bézier paths or multi-camera rigs were found** in Runway's docs or changelog. In Gen-4/4.5, camera is mostly prompt- and reference-driven, and Aleph can re-render a clip from a new angle.

**Seed**: Runway's guide says reusing a seed with the same prompt gives "nearly identical" results (https://runway.com/resources/what-is-an-ai-image-seed). The API exposes `seed` for gen4 models **[UNCERTAIN — API reference body not rendered]**.

---

## 5. Luma (Dream Machine / Ray)

| Model | Date | Facts | Source |
|---|---|---|---|
| Ray2 | 2025-01 | 5/10 s; **Camera Motion Concepts** (2025-03): 15+ moves incl. **Orbit left/right**, crane, push/pull, pan, tilt, truck, roll, bolt cam, aerial drone, tiny planet | https://lumalabs.ai/changelog/camera-motion-concepts-launch |
| Ray3 | 2025-09 | "Reasoning" video model; **native 16-bit HDR, ACES EXR export**; Draft mode | https://pasqualepillitteri.it/en/news/4026/luma-dream-machine-ray3-review-2026 [secondary] |
| Ray3 Modify | 2025-12-18 | Video→video with character refs + start/end frame | https://techcrunch.com/2025/12/18/luma-releases-a-new-ai-model-that-lets-users-generate-a-video-from-a-start-and-end-frame |
| Ray3.14 | **2026-01-26** | Native 1080p, 4× faster, 3× cheaper per second; no character ref, **no native audio** | https://www.businesswire.com/news/home/20260126744711/en |
| **Ray3.2** (current) | **2026-06-09** | T2V/I2V **5 or 10 s**; 360p draft / 540p / 720p / 1080p; **native 16-bit HDR + EXR (ACES2065-1)**; **up to 16 keyframes**; **Camera Motion Transfer** (copies a camera move from a source clip); **Modify Video** up to 20 s @24 fps with performance and face transfer (≤8 faces); Reframe; **no native audio** (Modify/Reframe keep the source audio); API available | https://lumalabs.ai/ray (primary) ; date via https://miralab.co.jp/media/?p=103663 [secondary] |

Credits for Ray3.2: a 5 s clip costs 20 (360p) / 100 (720p) / 400 (1080p) credits. HDR costs 2× and HDR+EXR 3× (lumalabs.ai/ray). There is **no "360° orbit mode"**: Orbit left/right is one camera concept among many. Third-party guides describe it as giving "360-degree views" **[secondary]**.

---

## 6. Wan (Alibaba) — open vs closed

| Version | Weights | License | Facts | Source |
|---|---|---|---|---|
| Wan 2.1 | Open | Apache-2.0 | Early 2025; 1.3B / 14B | — |
| **Wan 2.2** | **Open** (HF + GitHub) | **Apache-2.0** | **2025-07-28**. MoE T2V/I2V-A14B (480p/720p, **≥80 GB VRAM** on a single GPU); **TI2V-5B: 720p @24 fps, 5 s, runs on a 24 GB card (RTX 4090)**; S2V-14B (speech→video); Animate-14B | https://github.com/Wan-Video/Wan2.2 (primary) |
| Wan 2.5 / 2.6 / 2.7 | **Closed (API only)** | — | 2.5 added audio; 2.7 ≤15 s; release dates not confirmed by Alibaba | https://www.atlascloud.ai/blog/tips/is-wan-3.0-open-source [secondary] |
| **Wan 3.0** | **Closed** (official page: "Open Source: No") | — | Beta 2026-08-06; GA **2026-08-24**; up to **30 s**, ≤1080p, native multilingual audio; inputs: text, image, audio, video, PDF/PPT; $0.05 / $0.10 / $0.20 per s (480p / 720p / 1080p); Model Studio / Qwen Cloud | https://thenextweb.com/news/alibaba-wan3-video-model-after-share-sale [secondary] |

Local run: Wan 2.2 TI2V-5B via ComfyUI / Diffusers on 24 GB. The A14B models need quantization or offload to fit consumer GPUs. **Pages claiming "Wan 3.0 open-sourced under Apache-2.0" are false** (they recycle Wan 2.1 details).

---

## 7. Other models relevant in 2026 (one block each)

- **Seedance (ByteDance)**: **Seedance 2.0 launched 2026-02-12**: native audio, multi-shot, refs up to 9 images, 3 videos and 3 audio files, ~15 s, up to 1080p (4K on Runway since 2026-07-22). Rolled out via Dreamina/CapCut, in the US from ~2026-04-08. Disney, Paramount, WBD, Netflix and the MPA raised infringement complaints. https://eweek.com/news/bytedance-seedance-2-ai-video-race ; https://www.freemalaysiatoday.com/category/business/2026/03/26/bytedance-quietly-rolls-out-seedance-2-0-globally. **Seedance 2.5** (announced 2026-06-23; on Runway 2026-08-11) **up to 30 s** with native audio, 1080p, 480p draft mode. Runway changelog (primary) gives 30 s / 1080p; "50 references / 4K" comes from morphic [secondary].
- **MiniMax Hailuo 3.0 (H3)**: shown at WAIC 2026-07-17, launched 2026-07-31. 5–15 s, 2K @24 fps, stereo native audio, start/end frames, refs (9 images / 3 videos / 3 audio). Variants: H3 Max. Open weights / 33B claims **[UNCERTAIN, secondary]**. https://app.adgreetz.com/changelog/58-hailuo-03-h3-video-models [secondary]. Earlier Hailuo 02 / 2.3 (2025) is still Leonardo's default video model **[secondary]**.
- **Pika**: Pika 2.5 (early 2026) is the flagship. T2V/I2V/V2V, 1080p, Pikaffects/Pikadditions, own API (dev.pika.art). Positioned for social content rather than cinema. https://www.cliprise.app/news/pika-2-5-released [secondary]
- **Midjourney Video V1** (2025-06-18): **image→video only**, 5 s base, extend 4 s × 4 → ~21 s, ~480p, **no audio, no camera control**. No V2 found as of Oct 2026. https://techcrunch.com/2025/06/18/midjourney-launches-its-first-ai-video-generation-model-V1
- **Grok Imagine Video 1.5 (xAI/SpaceXAI)**: 2026-06-16/17. Native audio incl. lip-synced dialogue; July update added up to 7 image refs, voice reference and native 1080p. API `grok-imagine-video-1.5` (POST /v1/videos/generations) ~$0.08 / $0.14 / $0.25 per s (480p / 720p / 1080p) **[secondary]**; Lite variant from $0.02/s, 1–15 s. https://aiweekly.co/node/3143 [secondary]
- **LTX (Lightricks)**: **LTX-2** (announced 2025-10-23; open weights + training code 2026-01-06): joint audio+video, up to 4K/50 fps, ≤20 s, runs on consumer GPUs. **LTX-2.5 (2026-08-11)**: 22B open-weight asymmetric dual-stream DiT (audio+video), multi-shot "connected scenes", **LTX-2.x Community License** (separate agreement for large companies). https://en.wikipedia.org/wiki/LTX-2 ; https://comfyui-wiki.com/en/news/2026-08-11-ltx-2-5-open-weights-release [secondary]
- **HunyuanVideo (Tencent)**: v1 13B (2024-12-03); **HunyuanVideo-1.5 (Nov 2025)** open weights under the Tencent Hunyuan Community License (excludes EU/UK/South Korea; >100M MAU needs a separate license). "HunyuanVideo 2.0" is **unverified**. https://osai-index.eu/model/hunyuanvideo
- **FLUX 3 Video (BFL)**, **HappyHorse 1.0/1.1 (Alibaba)**, **Meta muse-video**, **Utopai X**, **SkyReels V4**: appear in the 2026 leaderboard top 10 (see §10). Not researched further.
- **Leonardo.ai**: a **multi-model host**. Own model **Motion 2.0** (5 s, 480p Fast / 720p Quality, **no audio**). Hosted: Veo 3 / 3.1 / 3.1 Fast, Kling 2.1 / 2.5 / 2.6 / 3.0 / 3.0 Turbo, Hailuo (default, "Unlimited"), Seedance 1.0 / 2.0 / 2.5, MiniMax H3, Wan 2.6 / 2.7, FLUX 3 Video. **Sora 2 removed July 2026.** Leonardo "AI video models" guide, updated 2026-08-10 (page 403; via snippet) [secondary]; https://docs.leonardo.ai/me/docs/motion-20 ; https://intercom.help/leonardo-ai/en/articles/11027827

---

## 8. Lip-sync / avatars / native dialogue

| Product | Current state (Oct 2026) | Source |
|---|---|---|
| **HeyGen** | **Avatar V** (2026-04-08): avatar from a ~15 s recording, multi-angle stability, long-form; Video Agent, AI Studio | https://www.heygen.com/blog/announcing-avatar-v |
| **Hedra** | Character-3 (Mar 2025; image+audio+text → talking/full-body); **Omnia** (2026-02-05): audio-conditioned with dynamic environments + camera control; separate "Avatar" model; 4,000+ voices, voice cloning | https://www.hedra.com/video-models/hedra-character-3 |
| **Synthesia** | **Express-2** (2025-09-04): DiT full-body avatars, 1080p/30 fps, arbitrary length. **Synthesia 3.0** (2025-10-01): Video Agents (interactive), prompt-created avatars, single-image personal avatars | https://www.synthesia.io/post/express-2-is-synthesias-next-chapter-for-full-body-expressive-ai-avatars ; https://www.synthesia.io/post/synthesia-3-0-the-next-era-of-video |
| **Native dialogue in general models** | Veo 3.1 (always-on audio), Kling 3.0 (multi-character, 5 languages), Seedance 2.0/2.5, MiniMax H3, Grok Imagine 1.5, Wan 3.0, LTX-2. Sora 2 had it but is discontinued. Runway Characters = real-time avatars via API | §§1–7 |

---

## 9. Provenance and law

### 9.1 Watermarking / provenance
- **SynthID (Google)**: on **all** Veo outputs (Gemini API docs). The **Gemini app verifies video** (since 2025-12): upload ≤100 MB / ≤90 s and it reports which segments of the audio and visual tracks carry SynthID. https://blog.google/innovation-and-ai/products/verify-google-ai-videos-gemini-app/
- **SynthID adopters** beyond Google: NVIDIA Cosmos; OpenAI, Kakao and ElevenLabs added **May 2026**. A public SynthID Detector portal exists **[secondary]**: https://ecosistemastartup.com/google-abre-synthid-detector-para-detectar-contenido-de-ia/
- **C2PA**: Steering Committee = **Adobe, Amazon, BBC, Google, Meta, Microsoft, OpenAI, Publicis, Sony, TikTok, Truepic**. **Runway** is a General Member. **Kuaishou, Luma and EPAM are not listed.** https://c2pa.org/membership/ (fetched 2026-10-12)
- **EPAM is NOT a C2PA member** (absent from the member list; no press release found).
- Signing in practice: Google (C2PA + SynthID on images; Chrome/Search C2PA detection announced at I/O 2026 is image-only), OpenAI (Sora videos claimed C2PA + visible watermark; images C2PA + SynthID since 2026-05), Adobe Firefly (Content Credentials). C2PA metadata is easily stripped by re-encoding; SynthID survives compression, resizing and cropping.

### 9.2 EU AI Act
- **Article 50** of Regulation (EU) 2024/1689 holds the transparency obligations. **Art 52 was the number in the 2021 Commission proposal**; the final text is Art 50. https://artificialintelligenceact.eu/article/50/
  - **50(2)**: *providers* of systems generating synthetic audio, image, video or text must mark outputs "in a machine-readable format and detectable as artificially generated or manipulated" (watermarks/metadata; "as far as technically feasible").
  - **50(4)**: *deployers* must **disclose deepfakes** (image, audio, video). For evidently artistic, satirical or fictional works, a light-touch disclosure is enough. Public-interest text must also be disclosed unless it was human-edited.
- **Applies from 2026-08-02.** The **Digital Omnibus on AI** (published in the OJ 2026-07-24, in force 2026-07-27) defers **only Art 50(2)** to **2026-12-02**, and only for systems placed on the market **before** 2026-08-02. Deepfake labelling (50(4)) and chatbot disclosure have applied since 2026-08-02. https://www.mondaq.com/uk/new-technology/1823160/the-digital-omnibus-on-ai-enters-into-force-today [secondary] ; https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-article50-watermarking-deadline/ [secondary]
- **Code of Practice on marking and labelling AI-generated content**: final version **2026-06-10**, voluntary. It requires **at least two layers** of machine-readable marking (e.g. metadata + watermark). https://digital-strategy.ec.europa.eu/en/news/commission-publishes-code-practice-marking-and-labelling-ai-generated-content
- **Fines (Art 99)**: Art 5 prohibited practices **€35M / 7%** · **other obligations incl. Art 50: €15M / 3%** · incorrect information €7.5M / 1%. For SMEs, whichever is lower applies. https://artificialintelligenceact.eu/article/99/

### 9.3 Other 2026 deepfake law
- **US TAKE IT DOWN Act** (signed 2025-05-19): criminalizes non-consensual intimate imagery including AI deepfakes. **Platform notice-and-removal (48 h) has been enforced by the FTC since 2026-05-19**; FTC warning letters went to 12 "nudify" sites; civil penalty up to $53,088 per violation. https://www.jdsupra.com/legalnews/ftc-sends-warning-letters-to-companies-1534409/ [secondary]
- **US NO FAKES Act**: reintroduced 2026-05-20 (S. 4591 / H.R. 8915, with DMCA-style counter-notice); **passed Senate Judiciary 2026-06-18**; **stalled**: Sen. Cruz objected to unanimous consent, and the bill is on hold until at least November (Daily Journal, 2026-10-07). **Not law.** https://www.blackburn.senate.gov/2026/6/blackburn-coons-bipartisan-bill-to-protect-individuals-and-creators-from-deepfakes-passes-senate-judiciary-committee ; https://www.dailyjournal.com/article/395055-no-fakes-act-dead-for-now-as-cruz-objects-to-unanimous-consent-request
- **Denmark likeness law**: a copyright-act amendment protecting face and voice (50 years post-mortem; parody/satire exempt), notified to the EU as TRIS 2025/0654/DK. The original target of 2026-03-31 slipped; **the bill was being (re)introduced ~2026-10-08. Not yet in force.** https://www.euronews.com/2026/10/08/denmark-introduces-a-bill-protecting-peoples-faces-and-voices-from-deepfakes ; https://intellectual-property-helpdesk.ec.europa.eu/news-events/news/denmarks-proposed-copyright-rules-deepfakes-2026-06-01_en

---

## 10. Benchmarks (human-preference Elo)

**LMArena (arena.ai) Text-to-Video, dated 2026-09-21** (https://arena.ai/leaderboard/text-to-video, fetched 2026-10-12):
1 gemini-omni-1.1-flash 1516 · 2 gemini-omni-flash 1513 · 3 flux-3-video 1493 (prelim) · 4 grok-imagine-video-1.5-agent 1492 (prelim) · 5 dreamina-seedance-2.0-720p 1479 · 6 wan3.0 1476 · 7 dreamina-seedance-2.5-720p 1474 · 8 minimax-h3 1460 · 9 muse-video (Meta) 1456 · 10 happyhorse-1.0 1427. Veo 3.1 and Sora 2 Pro sit at ~1,364 (Aug snapshot [secondary]).

**Artificial Analysis Video Arena, T2V with audio (v2.0)** (https://artificialanalysis.ai/video/leaderboard/text-to-video, fetched 2026-10-12, no date shown):
1 Wan 3.0 1156 · 2 Utopai X 1149 · 3 Seedance 2.5 1143 · 4 MiniMax H3 (768p) 1137 · 5 MiniMax H3 Max 1130 · 6 FLUX 3 1128 · 7 Seedance 2.0 1116 · 8 Gemini Omni Flash 1.1 1113 · 9 SkyReels V4 1074 · 10 Agnes-Video-2.5 1057. Silent board top 5: Wan 3.0, H3 Max, H3, Seedance 2.5, FLUX 3.

Teaching point: the two arenas disagree on #1, and leaders change monthly. Cite the date and board (with or without audio).

---

## 11. Seeds, durations, multi-shot

- **Seed determinism**: no major cloud video API guarantees determinism. Veo: seed "doesn't guarantee determinism" (Gemini API docs). Kling API: no seed parameter found in the mirrored docs **[secondary]**. Sora API: discontinued; no seed parameter known **[UNCERTAIN]**. Runway: seed gives "nearly identical" results **[UNCERTAIN for API]**. Only **open-weights local** runs (Wan 2.2, LTX-2, Hunyuan) give bit-reproducible output with a fixed seed, sampler and hardware/software stack.
- **Typical durations (Oct 2026)**: Veo 3.1 4/6/8 s (+7 s extensions to 148 s) · Omni Flash 3–10 s (+10 s extensions to 40 s) · Kling 3.0 3–15 s; 4.0 ≤30 s · Seedance 2.5 / Wan 3.0 ≤30 s · H3 5–15 s · Luma Ray3.2 5/10 s · MJ V1 5 s (→21 s) · Leonardo Motion 2.0 5 s.
- **Multi-shot / storyboard**: Kling 3.0 Multi-Shot / Custom Multi-Shot (shot count + per-shot duration), Seedance 2.0 multi-shot, LTX-2.5 "connected scenes", Kling 4.0 timeline editor + 10 keyframes, Luma 16 keyframes, Runway Agent/Studio timeline, Google Flow (extend + first/last frame). The Sora Storyboard **is gone** with Sora.

---

## 12. Claims to check in deck

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| 1 | "Diffusion Transformers natively simulate Navier-Stokes fluid dynamics" | **FALSE** | DiTs learn statistical patterns of pixels. No PDE solver is involved. Physics-IQ (Google DeepMind/INSAIT, WACV 2026): physical understanding is "severely limited" and "unrelated to visual realism" (https://arxiv.org/abs/2501.09038). Kang et al., ICML 2025: models show "case-based" generalization and fail out of distribution (https://arxiv.org/abs/2411.02385). Suggested wording: "learn plausible-looking fluid motion from data". |
| 2 | "ChatGPT 4o generates video" | **FALSE** | GPT-4o generated images (Mar 2025), not video. Video was Sora (separate app/site), and Sora has been shut down (app 2026-04-26, API 2026-09-24). ChatGPT has no video generation. OpenAI deprecations; heise. |
| 3 | "Consumer chat apps have no camera control" | **MOSTLY TRUE, needs nuance** | Gemini app / Omni: camera only via prompt text. But the consumer *video* apps do have controls: Kling (camera_control, Motion Brush on older models), Luma (Camera Motion Concepts, Camera Motion Transfer), Runway (Advanced Camera Control since Gen-3 Turbo), Flow (first/last frame for orbits/zooms). Say "chat apps: prompt-only; dedicated video apps: explicit controls". |
| 4 | "Cloud APIs give deterministic seeds + LoRA" | **FALSE** | Veo docs: seed "doesn't guarantee determinism". Kling API: no seed found. Closed APIs (Veo, Kling, Runway, Omni) offer no LoRA fine-tuning. LoRA is an **open-weights** feature (Wan 2.2, LTX-2, Hunyuan), sometimes offered by hosts serving those open models **[general]**. Flip it: "open weights give reproducibility + LoRA; cloud APIs give quality + references". |
| 5 | "EU AI Act Article 52 mandates watermarking" | **FALSE (wrong article)** | Final text: **Art 50(2)** (provider machine-readable marking) and **Art 50(4)** (deployer deepfake disclosure). Art 52 was the 2021 proposal numbering. Applies from 2026-08-02; 50(2) deferred to 2026-12-02 for legacy systems (Digital Omnibus). |
| 6 | "Fines up to €35M or 7% for synthetic media labeling" | **FALSE** | Art 99(4): **€15M or 3%** for Art 50 breaches. €35M / 7% is Art 99(3), for prohibited practices (Art 5). https://artificialintelligenceact.eu/article/99/ |
| 7 | "EPAM is a C2PA member" | **FALSE / unsupported** | Not on https://c2pa.org/membership/ (fetched 2026-10-12); no announcement found. Remove the claim or ask EPAM marketing for confirmation. |
| 8 | "Leonardo Motion has integrated audio, 4s loops" | **FALSE** | Motion 2.0 = **5 s**, 480p/720p, **no audio**. Audio on Leonardo comes from hosted third-party models (Veo 3.x, Kling 2.6+/3.0, Seedance). "Loops" is a usage pattern, not a mode **[secondary]**. |
| 9 | "Luma has 360 orbit mode" | **MISLEADING** | Luma offers **Orbit left/right** as one of 15+ Camera Motion Concepts (Ray2+), and Ray3.2 adds Camera Motion Transfer. There is no named "360 orbit mode". https://lumalabs.ai/changelog/camera-motion-concepts-launch |
| 10 | "Kling Motion Brush 6 layers with X,Y,Z vectors and speed-0 freeze mask" | **PARTLY TRUE** | Official: **up to 6 elements**, each with a **2D trajectory** drawn on the image, plus a **Static Brush** to freeze regions. No Z vector or numeric speed. Motion Brush belongs to 1.x/2.x-era models and is not in the 3.0 feature list. https://kling.ai/quickstart/how-to-animate-image-parts |
| 11 | "Runway 3D splines multi-camera bezier" | **FALSE** | Runway's Advanced Camera Control (Gen-3 Alpha Turbo, 2024-11-01) = direction + intensity on 6 axes plus Static. No splines, Bézier paths or multi-camera rigs in the docs or changelog. Gen-4.5 camera is prompt/reference-driven; Aleph can re-render from a new angle. |

---

## 13. Open items to re-check right before delivery
- Whether **Kling 4.0** full release has shipped (planned for October 2026) and its final API IDs and prices.
- Gemini Omni 1.1 Flash: official per-second prices for 360p/1080p/4K, and an official statement on native audio.
- Vertex AI Veo 3.1 GA IDs (`-001`) and Vertex pricing (doc body did not render).
- Runway API `seed` semantics, and whether Gen-4.5 has native audio (not in the changelog).
- Seedance 2.5 official spec sheet (reference count, 4K).
- Denmark likeness bill: whether it passed the Folketing.
- NO FAKES Act after November 2026.
