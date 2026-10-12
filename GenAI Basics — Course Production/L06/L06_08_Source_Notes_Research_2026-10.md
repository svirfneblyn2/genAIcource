# Research Brief — Lesson 06: Speech and Audio AI (state as of 2026-10-12)

Method: web search and fetch of public pages on 2026-10-12, three parallel research passes (A: text-to-speech, cloning, speech-to-text; B: realtime voice and music; C: audio in video models, provenance, consent and law), plus our own measurements on the course audio (`demo_courier_audio/report.json`, produced by `deck_v2/make_audio.py`). Primary sources (vendor docs, pricing pages, model cards, legislation, regulator pages) are preferred and marked **[P]**; secondary sources are marked **[S]** or **SECONDARY**; anything not confirmed is **NOT VERIFIED** and is kept off the slides or flagged in the notes.

The old Drive package (`06 — Speech and Audio AI — DONE`, checked 2026-09-08) covered speech-to-text only (batch / streaming / realtime, WER, local Whisper, a mock demo repo). Its useful parts (three speech architectures, WER plus critical terms, “Speaker 1 is not Alice”, synthetic fixtures only) are kept in slides 12–13. Everything about text-to-speech, cloning, music, audio in video models, cost per hour and consent is new.

---

## 0. TL;DR for the lesson designer (what changed vs a 2025-era deck)

- **OpenAI audio generation moved on.** New file transcription model `gpt-transcribe` ($0.0045/min, released 2026-07-28) and live `gpt-live-transcribe` ($0.017/min). `whisper-1` and `gpt-4o-(mini-)transcribe(-diarize)` are deprecated on 2026-08-26 and **shut down on 2027-02-26**. Realtime voice: `gpt-realtime-2` (2026-05-07), `gpt-realtime-2.1` (2026-07-06), full-duplex `gpt-live-1` GA 2026-09-10 at $0.05/min plus backend. No `gpt-tts` model exists; TTS is still `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd`.
- **Google:** Gemini 3.8 Flash TTS ($9 per 1M audio tokens through 2026-12-31, $18 from 2027-01-01; 25 audio tokens per second → ≈ $0.0135/min), voice design and voice replication with consent audio in the Gemini API; Lyria 3.5 music GA in Gemini API and Gemini app (2026-09-03/04, $0.08 per song); Gemini Live and Live Translate; Chirp 3 STT in Speech-to-Text V2.
- **ElevenLabs:** v4 / v4 Turbo are new; v3, Multilingual v2, Flash v2.5 remain. API list price $0.08 per 1K characters (≈ $0.08/min); Scribe v2 STT $0.22/hour; Agents $0.08/min; Music $0.15/min; SFX up to 30 s.
- **Music:** Suno v6 (2026-09-09; commercial rights on paid plans only), Lyria 3.5, ElevenLabs Music, Stable Audio 3.0 (partly open weights). Labels: UMG and WMG settled with Udio (Oct–Nov 2025), WMG with Suno (2025-11-25); UMG and Sony still sue Suno.
- **Consent:** every big vendor gates cloning (fixed consent phrase, allowlist, or a live read-out). Open models (Qwen3-TTS, Chatterbox) clone from 3–10 s with no checks.
- **Law:** EU AI Act Art. 50 applies from 2026-08-02 (Digital Omnibus: grace to 2026-12-02 for Art. 50(2) marking of systems already on the market). Fines up to €15M / 3%. FCC 2024: AI voices in robocalls are “artificial” under the TCPA. NO FAKES Act is not law.
- **Loudness:** Spotify −14 LUFS, true peak below −1 dBTP; EBU R128 −23 LUFS; Apple Podcasts −16 LKFS. YouTube −14 LUFS only secondary.

## 1. Our own measurements (course audio, 2026-10-12)

Produced by `deck_v2/make_audio.py` on a laptop-class CPU, no GPU. All numbers on slides 2, 5, 7, 11, 12 and 18 come from `demo_courier_audio/report.json`.

| Item | Value |
|---|---|
| Source video | L05 `courier_delivery_final.mp4`, Veo 3.1, 23 s, with native audio |
| Veo native audio | −22.8 LUFS integrated, −0.5 dBTP |
| Veo invented speech (Whisper small) | shot 1: “Here's your order. Thank you. Have a good day.” (prompt has no dialogue); failure clip: “Continue straight for 200 meters, then your destination is on the left.” (prompt asks for no voice) |
| Voice EN | Kokoro-82M (Apache-2.0), voice `af_heart`; 3 lines, 30 words, ≈ 9.2 s, ≈ 3.2 words/s, 154 characters |
| Voice RU | Piper `ru_RU-dmitri-medium` (voice data CC0; `piper-tts` 1.8.0 is GPL-3.0), sampling noise off for reproducibility |
| Music | MusicGen-small (weights CC-BY-NC-4.0), seed 7, prompt in `make_audio.py`; EnCodec frame rate 50 Hz (model config) |
| Mix | Veo bed + music, sidechain ducking under the voice, two-pass loudnorm + limiter: −14.0 LUFS, −1.1 dBTP (both languages). A single-pass loudnorm gave −0.6 dBTP on RU (fail). |
| Round trip | Whisper small (faster-whisper, MIT). EN: WER 18.5% vs display text, critical terms 3/4 (“642” for “6:42” is transcriber formatting; “Here's your order” leaks from Veo audio). RU: WER ≈ 14%, critical terms 2/4 (voice reads “Шесть” as “Часть”, “Анна” as “Оно”). Whisper medium hears RU “6-42” but still “оно”. |

---


---

## Research A: TTS, Voice Cloning, STT/ASR (fact sheet)

- Lesson: "Speech and Audio AI" (GenAI Basics)
- Date checked for every item: **2026-10-12** (unless noted otherwise)
- Method: vendor pages fetched live (WebFetch / curl of the HTML / official price APIs). Quotes are verbatim from the fetched pages. Anything not confirmed on a primary page is marked **NOT VERIFIED** or **SECONDARY**.

#### 0. Conversion assumptions (read first)

| Assumption | Value | Source |
|---|---|---|
| Characters per minute of English speech | **~1,000 chars/min** (900 to 1,000 range; at 150 wpm x ~6 chars/word incl. spaces = ~900) | ElevenLabs uses 1K chars = ~1 min on its own price table: "$0.08 ~$0.08/minute 10,000 ~10 min" (https://elevenlabs.io/pricing/api) |
| Gemini audio tokens | **25 tokens per second = 1,500 tokens/min** | "Audio tokens correspond to 25 tokens per second of audio" (https://ai.google.dev/gemini-api/docs/pricing and https://cloud.google.com/text-to-speech/pricing) |
| OpenAI gpt-4o-mini-tts audio tokens | ~1,250 audio tokens/min (implied by OpenAI's historical $0.015/min estimate at $12/1M) | SECONDARY, see 1.1 |
| $/hour | $/min x 60 | arithmetic |

All per-minute figures for character-billed TTS below use 1,000 chars/min. At 900 chars/min, multiply by 0.9.

---

#### 1. OpenAI

Pricing page: https://developers.openai.com/api/docs/pricing (platform.openai.com/docs/pricing now 301-redirects here). The page has no "last updated" date.

#### 1.1 TTS

| Model | Vendor unit and price | $/min | $/hr | Quote |
|---|---|---|---|---|
| `gpt-4o-mini-tts` (snapshots `gpt-4o-mini-tts-2025-03-20`, `gpt-4o-mini-tts-2025-12-15` = default) | Text in $0.60 / 1M tokens; audio out **$12.00 / 1M tokens** | **~$0.015** (estimate) | **~$0.90** | "\| gpt-4o-mini-tts \| Audio \| - \| - \| $12.00 \|" and "\| gpt-4o-mini-tts \| Text \| $0.60 \| - \| - \|" |
| `tts-1` | **$15.00 / 1M characters** | $0.015 | $0.90 | "\| tts-1 \| Text \| $15.00 / 1M characters \|" |
| `tts-1-hd` | **$30.00 / 1M characters** | $0.030 | $1.80 | "\| tts-1-hd \| Text \| $30.00 / 1M characters \|" |

- The $0.015/min for gpt-4o-mini-tts is **SECONDARY**: the current pricing page shows no "Estimated cost" column for TTS (only for transcription). Earlier OpenAI pricing and OpenAI forum replies cited "$0.015 / minute" (https://community.openai.com/t/understanding-gpt-4o-mini-tts-pricing-input-characters-cost/1151816). Speaking slower raises audio-token count and cost.
- Model page: https://developers.openai.com/api/docs/models/gpt-4o-mini-tts : "GPT-4o Mini TTS is a text-to-speech model built on GPT-4o Mini".
- TTS guide (https://developers.openai.com/api/docs/guides/text-to-speech): 13 built-in voices listed (alloy, ash, ballad, coral, echo, fable, nova, onyx, sage, shimmer, verse, marin, cedar). It recommends "`marin` or `cedar`" for best quality. The guide intro says "11 built-in voices", which conflicts with the 13 it lists.
- Disclosure: the usage policies require "a clear disclosure to end users that the TTS voice they are hearing is AI-generated" (as quoted on the TTS guide).
- No `gpt-tts` model appears on the pricing page. (NOT FOUND)
- Speech-to-speech and realtime models, for context (per 1M audio tokens, in / out): `gpt-realtime`, `gpt-realtime-2`, `gpt-realtime-2.1`, `gpt-audio`, `gpt-audio-1.5` at $32 / $64. `gpt-realtime-mini`, `gpt-realtime-2.1-mini`, `gpt-audio-mini` at $10 / $20. `gpt-live-1` costs $0.05/min (sessions, backend billed separately).

#### 1.2 Custom voices (OpenAI's voice cloning)

Source: https://developers.openai.com/api/docs/guides/custom-voices

- Access is limited: "Custom voices are limited to eligible customers." You go through sales.
- Consent: "The consent audio recording must only include one of the following phrases." and "Any divergence from the script will lead to a failure."
- English consent phrase: **"I am the owner of this voice and I consent to OpenAI using this voice to create a synthetic voice model."**
- Sample: "The audio samples must be 30 seconds or less." The consent recording and the sample must come from the same person.
- Limit: "At most 20 voices can be created per organization."
- Works with: `gpt-4o-mini-tts` (TTS), `gpt-realtime-2` (Realtime), `gpt-live-1`.
- Terms: subject to the "Text-to-Speech Supplemental Agreement".

#### 1.3 Transcription (STT)

The pricing page's transcription table has an "Estimated cost" column.

| Model | $/min (OpenAI estimate) | $/hr | Quote |
|---|---|---|---|
| `gpt-transcribe` (new, recommended) | **$0.0045** | $0.27 | "\| gpt-transcribe \| Transcription \| - \| - \| $0.0045 / minute \|" |
| `gpt-4o-transcribe` | **$0.006** (tokens: $2.50 in / $10.00 out per 1M) | $0.36 | "\| gpt-4o-transcribe \| Transcription \| $2.50 \| $10.00 \| $0.006 / minute \|" |
| `gpt-4o-mini-transcribe` | **$0.003** ($1.25 / $5.00) | $0.18 | "\| gpt-4o-mini-transcribe \| Transcription \| $1.25 \| $5.00 \| $0.003 / minute \|" |
| `gpt-4o-transcribe-diarize` | $0.006 | $0.36 | "Transcription + diarization ... $0.006 / minute" |
| Whisper (`whisper-1`) | **$0.006** | $0.36 | "\| Whisper \| Transcription \| - \| - \| $0.006 / minute \|" |
| `gpt-live-transcribe` (live audio) | **$0.017** | $1.02 | "\| gpt-live-transcribe \| Live transcription \| - \| - \| $0.017 / minute \|" |
| `gpt-realtime-whisper` | $0.017 | $1.02 | "Live transcription ... $0.017 / minute" |
| `gpt-realtime-translate` | $0.034 | $2.04 | "Live translation ... $0.034 / minute" |

- STT guide (https://developers.openai.com/api/docs/guides/speech-to-text): "Start with `gpt-transcribe`. This is the recommended model for transcribing recorded speech in its original language."
  - `whisper-1` is still needed for word and segment timestamps, and is the only model behind the translations endpoint ("supports translation into English only").
  - Diarization: "Use `gpt-4o-transcribe-diarize` only when you need to identify who speaks".
  - Limits: "Files can be up to 25 MB." Formats: mp3, mp4, mpeg, mpga, m4a, wav, webm.
- gpt-transcribe model page (https://developers.openai.com/api/docs/models/gpt-transcribe): "High-accuracy speech-to-text model for file and Realtime input transcription". The page gives no release date and makes no WER claim.

---

#### 2. Google

#### 2.1 Gemini API TTS

Sources: https://ai.google.dev/gemini-api/docs/pricing (paid tier, per 1M tokens) and https://ai.google.dev/gemini-api/docs/speech-generation

| Model ID | Text in / 1M | Audio out / 1M | $/min (1,500 tok/min) | $/hr | Note |
|---|---|---|---|---|---|
| `gemini-3.8-flash-tts` | $0.50 | **$9.00** "through December 31, 2026" | **$0.0135** | $0.81 | From Jan 1, 2027: $1.00 / **$18.00**, so $0.027/min and $1.62/hr. Batch: $4.50 audio out |
| `gemini-3.8-flash-lite-tts` | $0.50 | **$6.00** through Dec 31, 2026 | $0.009 | $0.54 | From Jan 1, 2027: $12.00 out, so $0.018/min |
| `gemini-3.1-flash-tts-preview` | $1.00 | $20.00 | $0.030 | $1.80 | |
| `gemini-2.5-flash-preview-tts` | $0.50 | $10.00 | $0.015 | $0.90 | Listed on the pricing page but missing from the speech-generation page's model list. Possibly being phased out: NOT VERIFIED |
| `gemini-2.5-pro-preview-tts` | $1.00 | $20.00 | $0.030 | $1.80 | |

- Quotes: "$9.00 (audio) through December 31, 2026." / "$18.00 (audio) starting January 1, 2027." / "Audio tokens correspond to 25 tokens per second of audio."
- Text-input cost is negligible: ~250 text tokens per minute of speech costs ~$0.0001.
- Capabilities (speech-generation page):
  - "30 curated voices", plus an Extended Voice Library of "Hundreds of additional voices".
  - Languages: 3.8 Flash TTS "over 130 languages"; 3.8 Flash-Lite "over 100 languages".
  - Multi-speaker: "supports up to 2 speakers using prebuilt voices".
- Custom voices in the Gemini API:
  - "Voice design" from a text description, and "Voice replication": "Replicate a speaker's voice from reference and consent audio in Google AI Studio or using POST /v1beta/voices".
  - Listed only for the 3.8 Flash and Flash-Lite TTS models.
  - Limit: 200 stored voices per project.
  - The exact consent wording and any allowlist for the Gemini API are NOT VERIFIED; the page does not state them.
- SynthID on Gemini TTS output: NOT VERIFIED (the speech-generation page does not mention it).
- Gemini 3.x and 2.5 TTS models are also listed on the Cloud TTS pricing page at the same token prices, e.g. "Gemini 3.8 Flash TTS (Preview)** through December 31, 2026 ... Output tokens: $9.00 per 1 million audio tokens".

#### 2.2 Gemini audio-in models (for STT comparison)

Source: same Gemini pricing page. The per-minute figures are Google's own, marked with an asterisk.

| Model | Audio in | Text out | Combined $/min | $/hr |
|---|---|---|---|---|
| Gemini 3.5 Transcribe | "$2.00 or $0.003/min* (audio)" | "$12.00 or $0.002/min* (text)" | ~$0.005 | ~$0.30 |
| Gemini 3.5 Transcribe Live | "$3.50 or $0.005/min* (audio)" | "$21.00 or $0.004/min* (text)" | ~$0.009 | ~$0.54 |

Exact Gemini 3.5 Transcribe model ID strings were not captured: NOT VERIFIED.

#### 2.3 Cloud Text-to-Speech

Source: https://cloud.google.com/text-to-speech/pricing (raw HTML, fetched 2026-10-12)

| Voice type | Free tier / month | Price per 1M chars | $/min | $/hr |
|---|---|---|---|---|
| **Chirp 3: HD voices** | 0 to 1M chars | **$30** ("US$0.00003 per character (US$30 per 1 million characters)") | $0.030 | $1.80 |
| **Instant custom voice** | "Not available" | **$60** ("US$0.00006 per character (US$60 per 1 million characters)") | $0.060 | $3.60 |
| Studio (legacy) | 0 to 1M | $160 | $0.16 | $9.60 |
| Neural2 (legacy) | 0 to 1M | $16 | $0.016 | $0.96 |
| WaveNet (legacy) | 0 to 4M | $4 (page text reads "US$4per 1 million characters") | $0.004 | $0.24 |
| Standard (legacy) | 0 to 4M | $4 | $0.004 | $0.24 |

The page groups WaveNet, Neural2, Studio and Standard under "Legacy TTS models". The $4 WaveNet price is as printed; it was historically $16, so recheck before quoting it.

**Instant Custom Voice (Chirp 3)**, source: https://cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice

- Allowlist: "Important: Access to Instant Custom Voice is restricted to allow-listed users. To request access, contact a member of the sales team."
- Consent: "record the required consent statement as a single-channel audio file in the appropriate language ... up to 10 seconds long."
  - en-US script: **"I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model."**
  - A custom script is not allowed: "You must use the provided consent statement script for your chosen language."
- Reference audio: "record up to 10 seconds of audio". "The audio should be as close to 10 seconds as possible."
- API: `voices:generateVoiceCloningKey` (v1beta1) with `reference_audio` and `voice_talent_consent`.

#### 2.4 Cloud Speech-to-Text V2 (Chirp 3)

Sources: https://cloud.google.com/speech-to-text/pricing and https://cloud.google.com/speech-to-text/v2/docs/chirp_3-model (page "Last updated 2026-10-09 UTC")

- Model ID: "Chirp 3 `chirp_3`". It is "exclusively available within the Speech-to-Text API V2".
- "Chirp 3 provides enhanced accuracy and speed beyond previous Chirp models and provides diarization and automatic language detection."
- GA in `us` and `eu` multi-regions.

V2 standard recognition, list price:

| Monthly volume | $/min | $/hr |
|---|---|---|
| 0 to 500,000 min | **$0.016** | **$0.96** |
| 500K to 1M min | $0.010 | $0.60 |
| 1M to 2M min | $0.008 | $0.48 |
| 2M+ min | $0.004 | $0.24 |

- Quote: "Standard 0 minute to 500,000 minute $0.016 / 1 minute, per 1 month / account".
- Dynamic batch: "Standard¹ $0.003 / 1 minute" (= $0.18/hr).
- "Standard¹ models include: default, command_and_search, latest_short, latest_long, phone_call, video, chirp (Speech-to-Text V2 only)". Billing is rounded up to 1-second increments.
- The pricing page names "chirp", not `chirp_3` explicitly. Billing Chirp 3 at the Standard rate is an **inference** (NOT VERIFIED by name).

---

#### 3. ElevenLabs

#### 3.1 Models

Source: https://elevenlabs.io/docs/overview/models

| Model ID | Languages | Character limit | Latency |
|---|---|---|---|
| `eleven_v4` (NEW, flagship) | 90+ | 10,000 (~10 min) | not stated |
| `eleven_v4_turbo` (NEW) | 90+ | not stated | ~100 ms |
| `eleven_v3` | 70+ | 5,000 | not stated |
| `eleven_v3_conversational` | 70+ | not stated | ~280 ms |
| `eleven_multilingual_v2` | 29 | 10,000 | not stated |
| `eleven_flash_v2_5` | 32 | 40,000 | ~75 ms |
| `eleven_flash_v2` | English only | 30,000 | ~75 ms |

- STT models: `scribe_v2`, `scribe_v2_realtime` (~150 ms), `scribe_v2_medical`.
- Deprecated: `eleven_turbo_v2_5` (replaced by `eleven_flash_v2_5`), `eleven_turbo_v2` (replaced by `eleven_flash_v2`), `scribe_v1` (replaced by `scribe_v2`).

#### 3.2 API pay-as-you-go prices

Source: https://elevenlabs.io/pricing/api. ElevenLabs equates 1K characters with ~1 minute.

| Product | Unit price | $/min | $/hr |
|---|---|---|---|
| v4 TTS | $0.08 per 1K chars list. Promo $0.022: "72% off until Oct 12" | $0.08 ($0.022 promo) | $4.80 ($1.32 promo) |
| v4 Turbo | $0.04 per 1K list. Promo $0.011 until Oct 12 | $0.04 | $2.40 |
| v3 | "$0.08 Price per 1K characters" | $0.08 | $4.80 |
| v3 Conversational | $0.04 per 1K | $0.04 | $2.40 |
| v2 Multilingual | $0.08 per 1K | $0.08 | $4.80 |
| Flash / Turbo | "$0.04 Price per 1K characters" | $0.04 | $2.40 |
| **Scribe v2 (STT)** | **"$0.22 Price per hour"** | $0.0037 | $0.22 |
| Scribe v2 Realtime | "$0.39 Price per hour" | $0.0065 | $0.39 |
| Scribe v2 Medical | $0.22/hr | | |

- Scribe add-ons (keyterm prompting, transcript editing) cost extra per hour; the page shows "$0.050" for one of them.
- Scribe marketing claim: "Over 98% transcription accuracy". Vendor claim, not a benchmark.
- The v4 promo ends on the class-prep date (Oct 12), so quote list prices.

#### 3.3 Subscription plans

Source: https://elevenlabs.io/pricing (monthly billing, FAQ text)

| Plan | $/month | Credits/month | Notes |
|---|---|---|---|
| Free | $0 | 10,000 | no commercial license |
| Starter | $6 (promo "$1" first month, "Until Oct 18") | 30,000 | "Commercial License", "Instant Voice Cloning" |
| Creator | $22 ($11 first month) | 121,000 | "Professional Voice Cloning" |
| Pro | $99 | 600,000 | 44.1 kHz PCM via API |
| Scale | $299 | 1,800,000 | 3 seats, 3 PVCs |
| Business | $990 | 6,000,000 | 10 seats, 10 PVCs, "Low-latency TTS as low as 5c/minute" |
| Enterprise | custom | custom | |

- FAQ quote: "Free $0 (10,000 credits); Starter $6 (30,000 credits); Creator $22 (121,000 credits, $11 for the first month); Pro $99 (600,000 credits); Scale $299 (1,800,000 credits, 3 seats); Business $990 (6,000,000 credits, 10 seats); Enterprise is custom."
- Credits: "For V2 Multilingual models, 1 text character equals 1 credit. For V2 Flash/Turbo English and V2.5 Flash/Turbo Multilingual models, discounted pricing applies for API usage, costing between 0.5 and 1 credit per character."
- UI comparison table, approximate TTS minutes included and price per extra minute:

| Plan | Minutes included | Extra minute |
|---|---|---|
| Free | ~10 | none |
| Starter | ~30 | ~$0.36 |
| Creator | ~121 | ~$0.20 |
| Pro | ~600 | ~$0.18 |
| Scale | ~1,800 | ~$0.17 |
| Business | ~6,000 | ~$0.17 |

  The column alignment in the scraped table is ambiguous, so the extra-minute prices are approximate.
- Banner: "Meet Eleven v4, our most emotive model yet. With 3x credits included on Creator+ until October 12".

#### 3.4 Voice cloning and verification

- **Instant Voice Cloning (IVC)**, source: https://elevenlabs.io/docs/product-guides/voices/voice-cloning/instant-voice-cloning
  - Sample length: "Approximately 1-2 minutes of clear audio".
  - "Avoid recording more than 3 minutes".
  - Consent: the user must "confirm that you have the right and consent to clone the voice". This is a self-attestation checkbox; there is no voice captcha for IVC.
  - Available from the Starter plan.
- **Professional Voice Cloning (PVC)**, source: https://elevenlabs.io/docs/product-guides/voices/voice-cloning/professional-voice-cloning
  - "All Professional Voice Clones require a verification process to confirm that the voice belongs to you."
  - Audio: "The bare minimum we recommend is 30 minutes of audio"; optimal "closer to 2-3 hours".
  - Available from the Creator plan.
- **Voice captcha**, source: https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/professional-voice-cloning
  - "a verification step is required to ensure you have permission to use the voice".
  - The captcha "image contains several lines of text that the voice owner will need to read out loud and record".
  - Submitted via `captcha.verify`.
  - Manual verification "should only be used if the previous verification steps have failed or are not possible".
  - SECONDARY detail from the ElevenLabs voice guide (search snippet): the user reads the prompt aloud within 10 seconds, the system compares that voice to the training data, and the user gets several attempts before manual review.

---

#### 4. Azure AI Speech

- Prices source: the Azure Retail Prices API (official machine-readable list prices), https://prices.azure.com/api/retail/prices filtered to productName "Azure Speech", region eastus.
- The marketing page https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/ renders prices with JavaScript ("$-") and could not be scraped.

| Meter (verbatim) | Price | $/min | $/hr | Effective from |
|---|---|---|---|---|
| "S1 Neural Text To Speech Characters" | **$15.00 / 1M chars** | $0.015 | $0.90 | 2024-02-01 |
| "Neural HD Text to Speech Characters" | $22.00 / 1M | $0.022 | $1.32 | 2026-03-01 |
| "Text to Speech - Personal Voice Characters" | $24.00 / 1M | $0.024 | $1.44 | 2024-02-01 |
| "S1 Custom Neural Realtime Characters" (professional voice) | $24.00 / 1M | | | 2021-02-01 |
| "CNV Neural HD Synthesis Characters" | $48.00 / 1M | | | 2025-07-01 |
| "S1 Custom Neural Training" | $52 / compute hour | | | |
| "S1 Custom Neural Voice Model Hosting Unit" | $4.032 / hour | | | |
| "S1 Speech To Text" (standard real-time) | **$1.00 / hour** | $0.0167 | $1.00 | 2018-11-01 |
| "S1 Speech to Text Batch" | **$0.18 / hour** | $0.003 | $0.18 | 2024-05-01 |
| "Fast Transcription Speech To Text" | $0.36 / hour | $0.006 | $0.36 | 2024-11-01 |
| "Fast Transcription Promo Speech To Text" | $0.10 / hour | | | 2026-09-01 (promo) |

- Free F0 tier (pricing page text): "Real-time Transcription: 5 audio hours free per month" and "Neural 0.5 million characters free per month".
- The page also lists "MAI Transcribe-2", "MAI Transcribe-1.5", "MAI-Voice" and "LLM Speech Transcription" SKUs. Their prices were not in the retail API pull: NOT VERIFIED.
- Leaderboard entries "microsoft/azure-speech-06-2026" and "-07-2026" appear on the Open ASR Leaderboard (see section 7).

**Consent and limited access**

- Limited Access policy: https://learn.microsoft.com/en-us/azure/ai-foundry/responsible-ai/speech-service/text-to-speech/limited-access (ms.date 2026-03-31)
  - "custom neural voice is a Limited Access feature available by registration only, and only for certain use cases."
  - "Only customers managed by Microsoft, meaning those who are working directly with Microsoft account teams, are eligible for access."
  - "Microsoft will require the customer to upload a recorded audio file ... with a pre-defined statement from the voice talent acknowledging that the customer will use the talent's voice to create a synthetic voice."
  - Microsoft "reserves the right to use Microsoft's speaker recognition biometric identification technology on this recorded acknowledgement statement and verify it against the training audio data".
  - Customers must "obtain explicit written permission from voice talent" and "disclose the synthetic nature" to users.
  - "Personal voice ... is a Limited Access feature and requires registration and approval."
- Personal voice overview: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/personal-voice-overview (ms.date 2026-09-09)
  - "A 5–90-second human speech sample".
  - "Speaker's verbal statement required. No unapproved use case allowed."
  - "A recorded statement from the user is required acknowledging that the customer ... will create and use their voice."
  - Synthesis in "91 languages supported across 100+ locales".

---

#### 5. Deepgram and AssemblyAI

#### 5.1 Deepgram

Source: https://deepgram.com/pricing (raw HTML cross-checked)

| Model / mode | Pay As You Go $/min | Growth $/min | PAYG $/hr |
|---|---|---|---|
| **Nova-3 Monolingual, pre-recorded** | **$0.0043** | $0.0036 | **$0.258** |
| Nova-3 Multilingual, pre-recorded | $0.0052 | $0.0043 | $0.312 |
| Nova-3 Monolingual, streaming | $0.0048 (promo; struck-through $0.0077) | $0.0042 | $0.288 |
| Nova-3 Multilingual, streaming | $0.0058 (promo; struck-through $0.0092) | $0.0050 | $0.348 |
| Flux English (streaming, voice-agent ASR) | $0.0065 | $0.0057 | $0.39 |
| Flux Multilingual | $0.0078 | $0.0068 | $0.468 |
| Aura-2 TTS | $0.030 per 1K chars (= $0.03/min at 1K chars/min) | $0.027 | $1.80 |

- Free credit: "Every new account receives $200 in free credit".
- No Nova-4 on the page (NOT FOUND).

#### 5.2 AssemblyAI

Source: https://www.assemblyai.com/pricing (raw HTML cross-checked)

| Model | $/hr | $/min | Quote |
|---|---|---|---|
| **Universal-3.5 Pro** (`universal-3-5-pro`, async) | **$0.21** | $0.0035 | "works across 18 languages, with native code switching and our most accurate speaker diarization yet. $0.21 /hr" |
| Universal-2 (async) | **$0.15** | $0.0025 | "trained on over 12.5 million hours of audio data. Supports 99 languages. ... $0.15 /hr" |
| Universal-3.6 Pro Realtime (streaming, NEW) | $0.45 | $0.0075 | "Supports 32 languages ... $0.45 /hr" |
| Universal-Streaming (English) | $0.15 | $0.0025 | "$0.15 /hr" |
| Universal-Streaming Multilingual | $0.15 | $0.0025 | "Supports English, Spanish, German, French, Portuguese, and Italian. $0.15 /hr" |

- Add-ons such as keyterms prompting and prompting are "$0.05 /hr" each on Universal-3.5 Pro.
- Free credit: "$50 in free credits, no credit card required."
- **Slam-1 is deprecated**: no price listed, and the docs say to migrate to Universal-3.5 Pro (via WebFetch summary; exact quote not captured).

---

#### 6. Open-weights models

#### 6.1 STT

| Model | License | Facts | Source |
|---|---|---|---|
| **OpenAI Whisper** (code and original checkpoints) | **MIT** ("MIT License Copyright (c) 2022 OpenAI") | Sizes: tiny 39M, base 74M, small 244M, medium 769M, large 1550M, turbo 809M. VRAM ~1/1/2/5/10/6 GB. Relative speed tiny ~10x, turbo ~8x vs large 1x. Quote: "the `turbo` model is an optimized version of `large-v3` that offers faster transcription speed with a minimal degradation in accuracy." | https://github.com/openai/whisper (README and LICENSE via raw.githubusercontent.com) |
| `openai/whisper-large-v3` (HF) | Tagged **apache-2.0** on the HF hub (differs from the MIT GitHub repo) | | https://huggingface.co/api/models/openai/whisper-large-v3 |
| `openai/whisper-large-v3-turbo` (HF) | **MIT** | ~6.28M downloads (HF API counter) | https://huggingface.co/api/models/openai/whisper-large-v3-turbo |
| NVIDIA `parakeet-tdt-0.6b-v3` | CC-BY-4.0 | | HF API |
| NVIDIA `canary-qwen-2.5b` | CC-BY-4.0 | | HF API |
| `Qwen/Qwen3-ASR-1.7B` | Apache-2.0 | created 2026-01-28 | HF API |
| `mistralai/Voxtral-Mini-4B-Realtime-2602` | Apache-2.0 | | HF API |

#### 6.2 TTS

| Model | License | Facts | Source |
|---|---|---|---|
| **Kokoro-82M** (`hexgrad/Kokoro-82M`) | **Apache-2.0** | "open-weight TTS model with 82 million parameters" and "With Apache-licensed weights, Kokoro can be deployed anywhere from production environments to personal projects." ~10.7M downloads | https://huggingface.co/hexgrad/Kokoro-82M |
| **Piper** | Engine now **GPL-3.0** | Old repo README: "Development has moved: https://github.com/OHF-Voice/piper1-gpl". The new repo's COPYING file is "GNU GENERAL PUBLIC LICENSE Version 3". PyPI `piper-tts` 1.8.0 license: "GPL-3.0-or-later". The old `rhasspy/piper` was MIT. Voices repo `rhasspy/piper-voices` is tagged MIT on HF, but individual voices carry their own dataset licenses (not checked per voice). | https://github.com/rhasspy/piper, https://github.com/OHF-Voice/piper1-gpl, https://pypi.org/pypi/piper-tts/json |
| **Chatterbox** (`ResembleAI/chatterbox`) | **MIT** | Latest is "Chatterbox Multilingual V3 ... keeps the same 0.5B model size", with zero-shot voice cloning. A built-in watermark was not seen in the README excerpt: NOT VERIFIED | https://huggingface.co/ResembleAI/chatterbox |
| **Dia-1.6B** (`nari-labs/Dia-1.6B`) | Apache-2.0 | dialogue TTS | HF API |
| **Sesame CSM-1B** (`sesame/csm-1b`) | Apache-2.0 | | HF API |
| **Orpheus 3B** (`canopylabs/orpheus-3b-0.1-ft`) | Apache-2.0 | | HF API |
| **VibeVoice-1.5B** (Microsoft) | MIT | Long-form multi-speaker. Card: "limited to research purpose use", "We do not recommend using VibeVoice in commercial or real-world applications", "Added an imperceptible watermark to generated audio". VibeVoice-Large shows "Disabled". | https://huggingface.co/microsoft/VibeVoice-1.5B |
| VibeVoice-Realtime-0.5B | MIT | | HF API |
| **Qwen3-TTS** (`Qwen/Qwen3-TTS-12Hz-1.7B-*`, 0.6B) | Apache-2.0 | Created 2026-01-21. Base models are "capable of 3-second rapid voice clone from user audio input". 10 languages. ~2.2M downloads (CustomVoice) | https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice |
| VoxCPM2 (`openbmb/VoxCPM2`) | Apache-2.0 | created 2026-04-03 | HF API |
| Fish Audio S2 Pro, Higgs TTS 3, XTTS-v2 (Coqui) | "other" (custom or non-commercial) | XTTS-v2 is under the Coqui Public Model License (non-commercial); exact terms NOT VERIFIED | HF API tags |

Teaching point: zero-shot cloning from ~3 to 10 seconds of audio is now available in permissively licensed open models (Qwen3-TTS, Chatterbox). Commercial APIs gate cloning behind consent recordings or allowlists; open weights do not.

---

#### 7. WER and leaderboards

**Definition**, source: https://huggingface.co/spaces/evaluate-metric/wer (README)

- "WER = (S + D + I) / N = (S + D + I) / (S + D + C)". S = substitutions, D = deletions, I = insertions, "N is the number of words in the reference (N=S+D+C)".
- "This value indicates the average number of errors per reference word. The lower the value, the better".
- Note: because insertions are counted, WER can exceed 100%.

**Hugging Face Open ASR Leaderboard**, https://huggingface.co/spaces/hf-audio/open_asr_leaderboard

- Space last modified 2026-10-09.
- Current version label: **"09-10-2026": "Add openai/gpt-transcribe. Add URGENT24 to avg English WER."** (from `init.py`). The label "09-10-2026" is probably day-month-year = 9 Oct 2026, matching the space's last-modified date.
- Default English average covers: AMI, Earnings22, Gigaspeech, LibriSpeech clean and other, SPGISpeech, URGENT24, Voice Arena Monsoon, VoxPopuli, plus two private sets (scripted and conversational).
- Raw data: `hf-audio/open-asr-leaderboard-results/english_short_latest.csv` @ revision d3c0e9a.

Top entries, ranked two ways (lower WER is better):

| Rank | By the CSV "avg" column | Avg WER % | By my mean of the 9 public English sets | Avg WER % |
|---|---|---|---|---|
| 1 | reson8/resonant-1-flash | 4.02 | zoom/scribe_v2_pro | 4.08 |
| 2 | zoom/scribe_v1 | 4.15 | microsoft/azure-speech-07-2026 | 4.49 |
| 3 | microsoft/azure-speech-06-2026 | 4.26 | modulate/multilingual | 4.53 |
| 4 | sophea/asr-k1 (preview) | 4.68 | elevenlabs/scribe_v2 | 4.55 |
| 5 | zoom/scribe_v2_pro | 4.77 | | |

Other rankings by my 9-set mean: AssemblyAI universal-3-5-pro 4.87; best open model Qwen3-ASR-1.7B 4.94 (Apache-2.0); CohereLabs/cohere-transcribe-03-2026 5.21 (Apache-2.0).

Reference points from the CSV "avg" column:

| Model | Avg WER % | License |
|---|---|---|
| elevenlabs/scribe_v2 | 5.37 | proprietary |
| assemblyai/universal-3-5-pro | 5.80 | proprietary |
| openai/gpt-transcribe | 6.38 | proprietary |
| nvidia/parakeet-tdt-0.6b-v3 | 6.51 | |
| openai/whisper-large-v3 | 7.84 | |
| openai/whisper-large-v3-turbo | 8.39 | |

- **NOT VERIFIED: the exact on-screen ranking.** The UI recomputes the average and adds private sets, so the two methods above disagree.
- Safe statement for slides: "As of Oct 2026, top commercial ASR scores ~4–5% average English WER on the HF Open ASR Leaderboard. The best open models score ~5–6%. Whisper large-v3 scores ~7.8%."
- Deepgram and Google Chirp 3 entries were not found in this CSV.

---

#### 8. Summary comparison (list prices, Oct 12 2026)

**TTS ($/min at ~1,000 chars/min; x60 for $/hr)**

| Model | $/min |
|---|---|
| Google Standard/WaveNet (legacy) | 0.004 |
| Gemini 3.8 Flash-Lite TTS | 0.009 |
| Gemini 3.8 Flash TTS (through Dec 31 2026) | 0.0135 |
| OpenAI tts-1 / Azure Neural / gpt-4o-mini-tts (~) / Gemini 2.5 Flash TTS | 0.015 |
| Azure Neural HD | 0.022 |
| Chirp 3 HD / tts-1-hd / Deepgram Aura-2 / Gemini 3.1 Flash & 2.5 Pro TTS | 0.030 |
| ElevenLabs Flash / v4 Turbo | 0.04 |
| Google Instant Custom Voice | 0.06 |
| ElevenLabs v4 / v3 / Multilingual v2 | 0.08 |

**STT ($/hr)**

| Model | $/hr |
|---|---|
| AssemblyAI Universal-2 | 0.15 |
| OpenAI gpt-4o-mini-transcribe / Azure batch / Google dynamic batch | 0.18 |
| AssemblyAI Universal-3.5 Pro | 0.21 |
| ElevenLabs Scribe v2 | 0.22 |
| Deepgram Nova-3 batch | 0.258 |
| OpenAI gpt-transcribe | 0.27 |
| Gemini 3.5 Transcribe (~) | 0.30 |
| Whisper API / gpt-4o-transcribe / Azure Fast | 0.36 |
| Google STT V2 standard (incl. Chirp, first 500K min) | 0.96 |
| Azure real-time standard | 1.00 |
| OpenAI gpt-live-transcribe | 1.02 |

---

### Volatile: recheck 24h before class

1. **ElevenLabs promos.** The v4 "72% off until Oct 12" ($0.022/1K) and the "3x credits on Creator+ until October 12" banner end today. The Starter "$1 first month" offer runs "Until Oct 18". Quote list prices.
2. **Gemini 3.8 Flash and Flash-Lite TTS prices double on Jan 1, 2027** ($9 to $18 and $6 to $12 per 1M audio tokens). If class is after Jan 1, use the new prices. The 3.8 TTS models are "(Preview)" on the Cloud pricing page.
3. **Gemini 2.5 Flash Preview TTS** is listed on pricing but missing from the speech-generation docs; it may be deprecated.
4. **Deepgram Nova-3 streaming prices are promotional** (struck-through $0.0077 and $0.0092).
5. **Azure "Fast Transcription Promo" at $0.10/hr** (from 2026-09-01). Azure MAI-Transcribe and MAI-Voice prices are unverified.
6. **OpenAI**: `gpt-transcribe` and `gpt-live-transcribe` are new. Check whether OpenAI adds a TTS successor (`gpt-tts`, none today) or publishes a $/min estimate for gpt-4o-mini-tts (currently not on the page, so $0.015 is secondary).
7. **Google Cloud TTS WaveNet printed at $4/1M** (historically $16). Recheck before quoting.
8. **Open ASR Leaderboard** changes often (last update 2026-10-09). Screenshot the UI the day before and quote what it shows, not the CSV-derived ranks above.
9. **AssemblyAI** model naming moves fast (Universal-3.5 Pro, Universal-3.6 Pro Realtime). Slam-1 is deprecated.
10. **ElevenLabs model list**: v4 and v4 Turbo are brand new. Check whether v3 or Multilingual v2 get deprecated.
11. **Custom voice and cloning access rules** can change: OpenAI (eligible customers only), Google ICV (allowlist), Azure (Limited Access, Microsoft-managed customers), and the Gemini API voice replication consent wording.

---

## Research B: Realtime Voice (S2S) and Music Generation

Lesson: "Speech and Audio AI" (GenAI Basics). All items checked 2026-10-12 unless noted.
Rule: P = primary source (vendor/official), S = secondary source. Quotes come from WebFetch extraction, so they may contain small paraphrase artefacts. Re-open the URL before putting a quote on a slide.

---

#### 1. Speech-to-speech / realtime voice

#### 1.1 OpenAI Realtime API (P: https://developers.openai.com/api/docs/pricing, checked 2026-10-12)

| Model | Audio in $/1M tok | Cached audio in $/1M | Audio out $/1M |
|---|---|---|---|
| gpt-realtime-2.1 | 32.00 | 0.40 | 64.00 |
| gpt-realtime-2.1-mini | 10.00 | 0.30 | 20.00 |
| gpt-realtime-2 | 32.00 | 0.40 | 64.00 |
| gpt-realtime-1.5 | 32.00 | 0.40 | 64.00 |
| gpt-realtime | 32.00 | 0.40 | 64.00 |
| gpt-realtime-mini | 10.00 | 0.30 | 20.00 |

Per-minute products on the same page:
- gpt-live-1 (GPT-Live sessions): **$0.05 / minute**, billed per second. Backend model and tool usage are charged separately.
- gpt-realtime-translate (live speech translation): **$0.034 / minute**.
- gpt-realtime-whisper / gpt-live-transcribe (streaming STT): **$0.017 / minute**.
- gpt-transcribe (file STT): **$0.0045 / minute**.

Timeline (P: https://developers.openai.com/api/docs/changelog):
- 2026-05-07: gpt-realtime-2 released, described as "a new realtime voice model with configurable reasoning for speech-to-speech agents". gpt-realtime-translate ("for streaming speech translation") and gpt-realtime-whisper ("for streaming speech-to-text") were released the same day.
- 2026-07-06: gpt-realtime-2.1 released, "an updated realtime reasoning model with improved alphanumeric recognition". A distilled 2.1-mini was released alongside it.
- 2026-07-28: gpt-transcribe and gpt-live-transcribe released.
- 2026-08-26: whisper-1 and gpt-4o-(mini-)transcribe(-diarize) deprecated. "These models will shut down on February 26, 2027."
- 2026-09-10: GPT-Live 1 (`gpt-live-1`) "is now generally available in the API". It is full-duplex and costs $0.05/min.
- Translate supports 70+ input languages and 13 output languages. This comes from the OpenAI announcement https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/, which returned 403 to the fetcher. The figure is confirmed only via a search snippet (S-level). PARTIALLY VERIFIED.
- gpt-realtime-2 context window grew from 32K to 128K tokens (S: news summaries). NOT VERIFIED on a primary page.
- Official $/minute estimate for token-billed gpt-realtime-2: **NOT VERIFIED**. No official per-minute figure was found. Do not invent one; show token prices instead.

#### 1.2 Google Gemini Live API (P: https://ai.google.dev/gemini-api/docs/pricing, paid tier)
- Gemini 3.8 Live, Gemini 3.8 Live Extended Thinking, and Gemini 3.1 Flash Live Preview:
  - Input: "$3.00 or $0.005/min (audio)" per 1M tokens.
  - Output: "$12.00 or $0.018/min (audio)".
- Gemini 2.5 Flash Native Audio (`gemini-2.5-flash-native-audio-preview-12-2025`): input $3.00 (audio/video), output $12.00 (audio) per 1M tokens.
- Gemini 3.5 Live Translate (`gemini-3.5-live-translate-preview`): input "$3.50 or $0.0053/min", output "$21.00 or $0.0315/min".
- Gemini 3.5 Transcribe Live (`gemini-3.5-transcribe-live`): input "$3.50 or $0.005/min".
- Note: the model names 3.8 / 3.1 Flash Live come from the fetcher output. Re-open the page before class to confirm exact names.

#### 1.3 ElevenLabs Agents (P: https://elevenlabs.io/pricing/api)
- Agents: "Price per minute" **$0.08**, burst **$0.160/min**.
- Included minutes / concurrent calls: Free 15 min / 4 calls; Starter 75 / 6; Creator 275 / 10; Pro 1,238 / 20; Scale 3,738 / 30; Business 12,375 / 40.
- Caveat: the fetcher mapped table rows to plan names by row order.

#### 1.4 Azure Voice Live API (P: https://azure.microsoft.com/en-us/pricing/details/speech/)
- Tiers: Voice Live **Pro** (gpt-realtime, gpt-realtime-2, gpt-realtime-2.1, gpt-5, ...), **Standard** (gpt-realtime-mini, gpt-5-mini, ...), **Lite** (gpt-5-nano, phi4-mm-realtime, phi4-mini), plus **BYO**. All tiers use "per m token billing". The page states: "Voice Live pricing tiers are determined by the LLM models selected by developers."
- Actual $ numbers: **NOT VERIFIED**. The page rendered "$-" placeholders.
- A 2025 Microsoft Tech Community post (S, likely outdated) lists Pro audio at about $17 in / $38 out per 1M tokens and native GPT-4o-realtime audio input at about $44.

#### 1.5 Speech translation products
- OpenAI gpt-realtime-translate: $0.034/min (see 1.1).
- Google Gemini 3.5 Live Translate. Source (P): https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-live-3-5-translate/, dated 2026-06-09.
  - Supports "over 70 languages" for near real-time speech-to-speech translation and "stays just a few seconds behind the speaker".
  - Available as a public preview in the Gemini Live API and AI Studio, in the Google Translate app, and in Google Meet (private preview for enterprise, rolling out later).
- Google Meet speech translation went GA for businesses. Source (P): https://workspaceupdates.googleblog.com/2026/02/speech-translation-meet-ga.html.
  - Bidirectional between English and Spanish, French, German, Portuguese, and Italian.
  - Only one language pair can be active per meeting.
  - Mobile rollout started in April 2026 (https://workspaceupdates.googleblog.com/2026/04/speech-translation-in-google-meet-is-now-rolling-out-to-mobile-devices.html).
  - The Hindi addition is NOT VERIFIED (help center and blog disagree).

---

#### 2. Music generation

#### 2.1 Suno
- **Latest model: v6 family**, released 2026-09-09 (P: https://suno.com/blog/introducing-v6). The post says "v6 comes in three models":
  - v6 and v6-wild for "Pro and Premier subscribers".
  - v6-mini is "available to everyone".
  - Built "with our industry partners, including Warner Music Group, BMG and Believe".
  - All pre-v6 models are retired from new generation. Old songs stay playable.
- Plans (P: https://suno.com/pricing):

| Plan | Price | Credits | Downloads | Commercial rights | Models |
|---|---|---|---|---|---|
| Free | $0 | 50 credits/day | "No monthly song downloads" (7 lifetime trial downloads, personal use only) | "No commercial rights" | v6-mini |
| Pro | $8/mo (shown with annual billing, "Saves $24 by billing yearly") | 2,500/mo | 20/mo | Yes | v6, v6-wild |
| Premier | $24/mo (annual, "Saves $72") | 10,000/mo | 60/mo | Yes | v6, v6-wild |

  - Month-to-month price is NOT VERIFIED. By implication it would be about $10 for Pro and $30 for Premier; confirm on the page.
- Credits per song: Suno's hub says the free 50 daily credits give "up to 10 short songs per day", Pro is "around 500 songs", and Premier is "up to 2,000 songs". That implies about 5 credits per song. The official per-song cost is NOT VERIFIED as an explicit figure.
- Download limits took effect "starting September 3, including songs created before that date". Source (P): https://help.suno.com/en/articles/13614785. Free: "Up to 7 total (lifetime) trial downloads for personal, non-commercial use only."
- Ownership (P: https://help.suno.com/en/articles/2416769):
  - Paid: "you are considered the owner of the song... You also retain the rights to commercial use for the song, even if you end your subscription."
  - Free: "we retain ownership of the songs you generate", non-commercial use only.
  - Upgrading later does not grant retroactive rights by default (https://help.suno.com/en/articles/2425729).
- Copyrightability (P: https://help.suno.com/en/articles/2746945): "the material may not be eligible for copyright protection... Music made 100% with AI would not qualify for copyright protection... Writing the prompt does not constitute the creation of the song."
- API:
  - https://platform.suno.com/ says "Make music with the Suno API" and "Sign in to manage your API account". It appears to be an official generation API, but availability and pricing are NOT VERIFIED.
  - Suno also runs a free AI-provenance detection API (https://suno.com/suno-credentials).
  - Many "Suno API" sites are third-party wrappers and are not official.

#### 2.2 Udio
- 2025-10-29/30: UMG settled with Udio and the two plan a licensed "walled garden" platform for 2026 (S: https://musically.com/2025/10/30/umg-settles-udio-lawsuit-companies-plan-new-ai-music-service-together/). The UMG primary site is blocked for the fetcher.
- Downloads were disabled right after the UMG deal, then briefly reopened for 48h (S: https://www.digitalmusicnews.com/2025/10/31/udio-downloads-disabled-umg-deal/).
- Warner–Udio settlement 2025-11-19 (S: trackers). The exact terms are NOT VERIFIED.
- Whether the licensed platform has launched, and the current download policy as of Oct 2026: **NOT VERIFIED**. The Udio pricing page returned no content.

#### 2.3 Google Lyria
- **Lyria 3.5** (`lyria-3.5`):
  - GA in the Gemini API on 2026-09-03 (P changelog: https://ai.google.dev/gemini-api/docs/changelog).
  - In the Gemini app since 2026-09-04: "available to all users globally on the web and in the mobile app" (P: https://blog.google/innovation-and-ai/products/gemini-app/better-tracks-lyria-gemini/).
  - Also available in AI Studio, Google Flow Music, and Google Vids.
- Gemini API prices (P: https://ai.google.dev/gemini-api/docs/pricing; paid only, no free tier):
  - Lyria 3.5 full song: **$0.08 per song**.
  - Lyria 3 Pro Preview full song: $0.08 per song.
  - Lyria 3 Clip Preview (30 s): **$0.04 per song**.
- Specs (P: https://ai.google.dev/gemini-api/docs/music-generation):
  - Clip "always generates a 30-second clip".
  - Lyria 3.5 makes songs of "A couple of minutes" and outputs MP3 by default (WAV optional).
  - "All generated audio includes a SynthID audio watermark".
  - Prompts that request "specific artist voices or the generation of copyrighted lyrics" are filtered.
- Vertex AI: lyria-3-pro-preview produces up to 184 s and lyria-3-clip-preview 30 s (S: search snippet of Vertex docs).
- Lyria 2 on Vertex is "$0.06 per 30 seconds" and outputs 30 s WAV at 48 kHz (P via search snippet: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/lyria-music-generation). The direct page fetch was truncated, so this is PARTIALLY VERIFIED.
- **Lyria RealTime** (`models/lyria-realtime-exp`) (P: https://ai.google.dev/gemini-api/docs/realtime-music-generation):
  - "Lyria RealTime is an experimental model."
  - "Instrumental only". Raw 16-bit PCM, 48 kHz stereo, watermarked.
  - Price: NOT VERIFIED (not on the pricing page).

#### 2.4 ElevenLabs Music
- Music v2 announced 2026-05-26 (P: https://elevenlabs.io/blog/introducing-music-v2).
  - "cleared for commercial use, so every track you generate is yours to use".
  - Partners named: Believe ("recent licensing collaborations with Believe").
- Docs (P: https://elevenlabs.io/docs/overview/capabilities/music):
  - "cleared for nearly all commercial uses". Usage varies by plan, per https://elevenlabs.io/eleven-music-model-specific-terms.
  - Duration: minimum 3 s, maximum 5 min.
  - API model id `music_v2_5`.
- Price (P: https://elevenlabs.io/pricing/api): **$0.15 per minute** of music. Included minutes: Free 3, Starter 40, Creator 147, Pro 660, Scale 1,993, Business 6,600.
- Merlin/Kobalt deals: NOT VERIFIED in the current sources.

#### 2.5 Stable Audio (Stability AI)
- **Stable Audio 3.0** (P: https://stability.ai/news-updates/meet-stable-audio-3-the-model-family-built-for-artistic-experimentation-with-open-weight-models). The page is dated "May 20" with no year. 2026 is likely but NOT VERIFIED.
  - Four models: Small SFX, Small, Medium, and Large.
  - Small SFX, Small, and Medium have open weights on Hugging Face. Large is available via API and enterprise self-host.
  - Medium goes "up to 6:20".
  - "All Stable Audio 3.0 models are trained on fully licensed data."
  - Outputs fall under the Stability AI Community License (commercial use allowed). Organizations with more than $1M annual revenue need the Enterprise License.
- Stable Audio 2.5: "commercially safe", trained on licensed data, and aimed at enterprise. API price is 8 credits (1 credit = $0.01, so about $0.08 per generation). Source (P/S mix): https://stability.ai/news-updates/stability-ai-introduces-stable-audio-25-the-first-audio-model-built-for-enterprise-sound-production-at-scale and https://platform.stability.ai/pricing. PARTIALLY VERIFIED.

---

#### 3. Legal / licensing status

#### 3.1 Labels vs Suno / Udio (labels' primary sites are blocked for the fetcher, so dates below are S unless noted)
- UMG and Udio settled on 2025-10-29/30 (S: Music Ally, Hollywood Reporter). They plan a licensed platform for 2026, trained on licensed music. No financial terms were disclosed.
- WMG and Udio settled on 2025-11-19 (S).
- WMG and Suno settled and partnered on 2025-11-25 (S). Confirmed by Suno (P: https://suno.com/blog/wmg-partnership).
  - New licensed models in 2026, which became v6.
  - Downloads require a paid account.
  - Reported $500M figure: S, single source, NOT VERIFIED.
- UMG and Sony vs Suno: still active in D. Mass. as of late Sep 2026 (S: https://ailawsuittracker.com/cases/umg-v-suno/, https://www.digitalmusicnews.com/2026/04/09/suno-universal-music-lawsuit-settlement-impasse/).
  - DMCA §1201 claim added in Aug 2026.
  - New suit filed 2026-09-18 over about 60,202 recordings.
- Sony vs Udio: still active in S.D.N.Y. A second suit was filed 2026-07-20 (S).
- GEMA vs Suno: the Munich Regional Court ruled for GEMA (S). Date NOT VERIFIED.
- US fair-use merits ruling is not expected before 2027 (S).

#### 3.2 US Copyright Office
- Report "Copyright and Artificial Intelligence, Part 2: Copyrightability", released **2025-01-29** (P: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf).
  - Key positions: "prompts do not alone provide sufficient control". AI-assisted works are protectable where a human determines sufficient expressive elements (perceptible human work, or creative selection/arrangement/modification).
  - No change to the law is needed.
- 2026-03-02: the US Supreme Court denied cert in Thaler v. Perlmutter (No. 25-449), leaving the human-authorship requirement intact (S: https://www.morganlewis.com/pubs/2026/03/us-supreme-court-declines-to-consider-whether-ai-alone-can-create-copyrighted-works).
- 2026-05-12: Register Perlmutter's Senate testimony restates "prompts alone are unlikely to satisfy the requirements of sufficient human contribution" (P: https://copyright.gov/laws/hearings/Testimony-Register-Shira-Perlmutter-May-12-2026-Hearing-Senate-Judiciary-IP-Subcommittee.pdf, via search snippet).
- Any new 2026 registration guidance: NOT VERIFIED (none found).

#### 3.3 Streaming platforms
- **Spotify**, 2025-09-25 (P: https://newsroom.spotify.com/2025-09-25/spotify-strengthens-ai-protections/):
  - Stricter impersonation policy: vocal impersonation only with the artist's authorization.
  - Music spam filter.
  - Supports the "industry standard for AI disclosures in music credits, developed through DDEX".
- **Spotify AI Persona badge**, 2026-08-11 (P: https://newsroom.spotify.com/2026-08-11/ai-persona-badges-transparency/):
  - "The badge signals to listeners that an artist's identity may be AI-generated and does not represent a real person."
  - Rolled out from mid-September 2026.
  - "By default, Spotify will not include AI Personas in any editorial or algorithmic recommendations."
  - "Tens of thousands of AI credits" are submitted daily.
- **Deezer** (P: Deezer newsroom):
  - AI tagging for listeners launched in **June 2025**. The July 2026 release is internally inconsistent on this date.
  - Jan 2026: about 60,000 AI tracks/day, about 39% of deliveries (https://newsroom-deezer.com/2026/01/ai-generated-music-deezer-selling-detection-tool/).
  - Apr 2026: about 75,000/day, 44% (https://newsroom-deezer.com/2026/04/ai-generated-tracks-represent-44-of-new-uploaded-music/).
  - Jul 2026: about 90,000/day, **more than 50% of daily uploads at peak in June 2026** (https://newsroom-deezer.com/2026/07/ai-music-exceeds-50-percent-daily-uploads-deezer/).
  - AI music is 1–3% of streams, and up to 85% of those streams are fraudulent and demonetized.
  - Detected tracks are excluded from algorithmic recommendations and editorial playlists.
  - Claimed detection accuracy is 99.8%.

---

#### 4. Sound effects
- **ElevenLabs Sound Effects** (P: https://elevenlabs.io/docs/overview/capabilities/sound-effects):
  - "Maximum duration: 30 seconds per generation".
  - Seamless looping is available.
  - "40 credits per second when duration is specified".
  - Output is MP3, or WAV 48 kHz for non-looping effects.
- API price (P: https://elevenlabs.io/pricing/api): **$0.12 per minute**. Included generations: Free 8, Starter 150, Creator 605, Pro 3,000.
- Other: Stable Audio 3.0 Small SFX is open-weight (see 2.5).

---

#### 5. Loudness targets
- **Spotify** (P: https://support.spotify.com/us/artists/article/loudness-normalization/):
  - Normal "-14dB LUFS", Loud "-11dB LUFS", Quiet "-19dB LUFS".
  - "Keep it below -1dB TP (True Peak) max". For masters louder than -14 LUFS, keep TP below -2 dB.
- **EBU R 128** (P: https://tech.ebu.ch/docs/r/r128.pdf):
  - Target Level **-23.0 LUFS**, max true peak **-1 dBTP**, measured with an ITU-R BS.1770 meter.
  - Tolerance is ±0.2 LU (rev. 2020, per Tech 3343) and ±1 LU for live programmes.
  - Short-form content (R 128 s1) adds a max short-term loudness of -18 LUFS.
- **Apple Podcasts** (P: https://podcasters.apple.com/support/893-audio-requirements): about **-16 LKFS ±1 dB**, true peak not above -1 dBFS, per ITU-R BS.1770.
- **YouTube**: about -14 LUFS integrated; YouTube turns loud content down and does not boost quiet content.
  - Only secondary sources (https://en.wikipedia.org/wiki/Audio_normalization, Youlean, MeterPlugs) support this.
  - **NOT VERIFIED on a YouTube primary page.** YouTube Help only documents "Stable volume" (on by default).
- Ads (Google DV360 creative spec): -24 LKFS ±2 (P: https://support.google.com/displayvideo/answer/3129957). This applies to ads only.

---

Volatile: recheck 24h before class

---

## Research C: audio in video models, provenance, voice consent and law

Lesson: "Speech and Audio AI" (GenAI Basics). Researcher pass, date checked for all items: **2026-10-12**.
Legend: [P] = primary source (vendor docs, legislation, regulator); [S] = secondary (press or blog), used only when no primary was reachable; **NOT VERIFIED** = could not confirm from a source.

---

#### 1. Native audio inside video models

#### 1.1 Veo 3.1 (Google): audio is generated by default and can be switched off in the API
- **Claim:** In the Vertex AI / Agent Platform Veo API, the `generateAudio` parameter defaults to **true**.
  - Quote: "generateAudio boolean — Whether to generate audio along with the video. If true, an audio track is generated for the videos. Defaults to true."
  - URL [P]: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoGenerationModelParams (checked 2026-10-12)
  - Caveat: the Gemini API (ai.google.dev) Veo page does not document an audio on/off switch. A developer-forum thread says `generate_audio=False` is rejected on the Gemini API: https://discuss.ai.google.dev/t/veo-3-api-generate-audio-parameter-not-supported-last-frame-limitations/119206 [S, forum]. Treat the switch as **Vertex-only**. On the Gemini API, audio-off is **NOT VERIFIED**.
- **Claim:** Gemini API docs: "Veo 3.1 is a model for generating video with native audio."
  - URL [P]: https://ai.google.dev/gemini-api/docs/video (checked 2026-10-12)

#### 1.2 Veo 3.1 prompt conventions for audio (official Google Cloud blog)
- **Claim:** Google's official Veo 3.1 prompting guide (published **15 Oct 2025**) defines three audio prompt conventions:
  - "**Dialogue:** Use quotation marks for specific speech (e.g., A woman says, "We have to leave now.")."
  - "**Sound effects (SFX):** Describe sounds with clarity (e.g., SFX: thunder cracks in the distance)."
  - "**Ambient noise:** Define the background soundscape (e.g., Ambient noise: the quiet hum of a starship bridge)."
  - Also: "Veo 3.1 can generate a complete soundtrack based on your text instructions."
  - URL [P]: https://cloud.google.com/blog/products/ai-machine-learning/ultimate-prompting-guide-for-veo-3-1 (checked 2026-10-12)
- Supporting [P]: the Vertex prompt guide splits audio into "Sound effects: individual, distinct sounds that occur within the scene", "Ambient noise: the general background noise that makes a location feel real" and "Dialogue: spoken words from characters or a narrator". It also says "Clearly specify if you want audio." https://docs.cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide. (That page still refers to `veo-3.0-generate-001` "in Preview", so parts of it are stale.)
- "No music" as a negative cue appears only in third-party guides [S] (e.g. atlabs.ai). It is **NOT VERIFIED** in Google docs.

#### 1.3 Veo pricing: audio is a price toggle on Vertex and included by default on the Gemini API
- **Gemini API** (per second, paid tier; the page lists only with-audio rates):
  - Veo 3.1 Standard: **$0.40/s** (720p and 1080p), **$0.60/s** (4K)
  - Veo 3.1 Fast: **$0.10** (720p), **$0.12** (1080p), **$0.30** (4K)
  - Veo 3.1 Lite: **$0.05** (720p), **$0.08** (1080p). Quote: "(4k output not supported)"
  - "You will only be charged if your video is successfully generated."
  - URL [P]: https://ai.google.dev/gemini-api/docs/pricing (checked 2026-10-12)
- **Vertex / Gemini Enterprise Agent Platform** lists separate "Video + Audio generation" and "Video generation" rows:

| Model | Video + Audio | Video only |
|---|---|---|
| Veo 3.1 | $0.40 (720p/1080p), $0.60 (4K) | **$0.20** (720p/1080p), **$0.40** (4K) |
| Veo 3.1 Fast | $0.10 / $0.12 / $0.30 (720p/1080p/4K) | $0.08 / $0.10 / $0.25 |
| Veo 3.1 Lite | $0.05 / $0.08 (720p/1080p) | $0.03 / $0.05 |
| Veo 3 | $0.40 (720p/1080p) | $0.20 |

  - Quote (row description): "Generate high-quality videos with synchronized speech/sound effects from a text prompt or reference image".
  - URL [P]: https://cloud.google.com/vertex-ai/generative-ai/pricing (now redirects to https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing; checked 2026-10-12)
  - Caveat: the Vertex table shows the unit as "/ 1 count", not "per second". The per-second reading is inferred because the numbers match the Gemini API page, which labels them per second.
  - **Takeaway for slide:** on Veo 3.1 Standard, audio doubles the price ($0.20 to $0.40 per second). On Fast and Lite it adds 20 to 67%.

#### 1.4 Kling 3.0 (Kuaishou): native audio is a separate, higher per-second rate
- Official Kling developer pricing (units and USD per second):
  - **Kling 3.0:** "No Native Audio" **0.6 unit ($0.084)/s** at 720p and **0.8 unit ($0.112)/s** at 1080p. "With Native Audio x No Voice Control" **0.9 unit ($0.126)/s** at 720p and **1.2 units ($0.168)/s** at 1080p. 4K is **3.0 units ($0.42)/s** with or without audio.
  - **Kling 3.0 Omni:** no audio $0.084 (720p) / $0.112 (1080p). With native audio **$0.112 (720p) / $0.14 (1080p)**.
  - **Kling 3.0 Turbo:** "With Native Audio" only: $0.112 (720p) / $0.14 (1080p).
  - Footnote: "Failed video generations will not deduct any unit."
  - URL [P]: https://kling.ai/dev/pricing (klingai.com/global/dev/pricing redirects there; pricing JSON embedded in the page; checked 2026-10-12)
  - **Takeaway:** on Kling 3.0, audio adds +50% per second (0.6 to 0.9 units at 720p).
- Kling consumer credit guide (blog, 28 Jul 2026) gives only "native 4K ... at 30 credits per second". https://kling.ai/blog/kling-video-3-0-credit-cost-guide [P]
- The consumer-app credit rates with and without audio (6/8 vs 9/12 credits per second, +2 for voice control) appear only in third-party guides [S]. **NOT VERIFIED** on a Kling page.
- Kling 2.6 audio pricing: **NOT VERIFIED.** No official rate found, and third-party figures conflict. Native audio launched with 2.6 on 3 Dec 2025 per press [S].

#### 1.5 Gemini Omni (Google, 2026): video with audio, controlled by prompt
- Gemini API docs (model `gemini-omni-1.1-flash`):
  - "The model generates a video with audio based on your text description."
  - "By default the model will try to generate an appropriate audio track for a video." Negative prompts such as "No dialogue" and "No extra sound effects" are suggested. **No documented parameter to turn audio off.**
  - "All generated videos include SynthID watermarking, which is invisible to viewers."
  - Extensions: "You can extend videos by 10s, up to a total length of 40s."
  - URL [P]: https://ai.google.dev/gemini-api/docs/omni (checked 2026-10-12)
- Launch blog (Google I/O 2026, May 2026): "In time we will support output modalities like image and audio." Here "audio" means standalone audio output; the videos already carry sound. Also: "While only voice references will be supported for audio to start…" and "All videos created with Omni include our imperceptible SynthID digital watermark."
  - URL [P]: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/
- Pricing (Gemini API and Vertex): video output **$17.50 per 1M tokens**. Vertex footnote: "5792 tokens per second of 720p video … 8688 tokens per second of 1080p … 17376 tokens per second of 4k video for video outputs (with audio)". At 720p this is about **$0.10 per second, audio included**, with no audio-off discount listed.
  - URLs [P]: https://ai.google.dev/gemini-api/docs/pricing ; https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing

---

#### 2. Watermarking and provenance for audio

#### 2.1 Google SynthID (audio)
- "SynthID embeds a watermark into any audio generated or published through our AI music generation model Lyria". It also covers NotebookLM Audio Overviews (podcast feature). The page says the watermark is "inaudible to the human ear" and robust to noise, MP3 compression and speed change.
  - URL [P]: https://deepmind.google/models/synthid/ (checked 2026-10-12)
- Gemini TTS and native audio: "All audio outputs from our models are marked with SynthID, our advanced watermarking technology, allowing you to detect whether speech has been created or edited using Google AI."
  - URL [P]: https://deepmind.google/models/gemini-audio/ (lists 3.8 Flash TTS, 3.8 Flash-Lite TTS, 3.8 Live, etc.)
- **Verification in the Gemini app:** audio checks are supported. Limits: "audio files need to be less than 1 hour each". Files must be 100 MB or less, about 10 audio checks / 3 hours per rolling 24h. "Gemini can currently only recognize content created by Google AI tools." A negative result does not prove a file is human-made.
  - URL [P]: https://support.google.com/gemini/answer/16722517?hl=en
- **SynthID Detector portal:** checks image, video and audio. For audio it highlights the segments where a watermark is detected. Launched 2025.
  - URL [P]: https://blog.google/innovation-and-ai/products/google-synthid-ai-content-detector/
- **Google I/O 2026 (20 May 2026):** "we recently added SynthID verification for image, video and audio to the Gemini app". The post says it has been used **50 million** times and is expanding to Search and then Chrome. Google is also "adding verification for C2PA Content Credentials" in the Gemini app. Quote: "companies like OpenAI, Kakao and ElevenLabs are bringing SynthID technology to more of their AI-generated content."
  - URL [P]: https://blog.google/innovation-and-ai/technology/ai/google-io-2026-all-our-announcements/

#### 2.2 ElevenLabs detection
- **Audio Detector** (current, sign-in required): "Uses watermarking technology to detect imperceptible watermarks embedded in ElevenLabs-generated audio." Quote: "The tool first checks for a watermark, then falls back to the AI Speech Classifier if no watermark is found." Also: "The Audio Detector can only detect watermarks embedded by ElevenLabs." Third-party models served through ElevenLabs are "generally not watermarked."
  - URL [P]: https://elevenlabs.io/docs/eleven-creative/audio-tools/audio-detector
- **AI Speech Classifier** (legacy, no login): "99% precision, 80% recall" on unmodified ElevenLabs audio. It "may produce false positives or miss modified audio." The product page says it does not reliably classify Eleven v3 output and cannot detect other providers.
  - URLs [P]: https://elevenlabs.io/ai-speech-classifier ; https://elevenlabs.io/docs/eleven-creative/audio-tools/ai-speech-classifier

#### 2.3 OpenAI TTS disclosure requirement
- Quote: "Our usage policies require you to provide a clear disclosure to end users that the TTS voice they are hearing is AI-generated and not a human voice."
  - URL [P]: https://developers.openai.com/api/docs/guides/text-to-speech (platform.openai.com redirects here; checked 2026-10-12)
  - openai.com/policies/usage-policies returned 403, so the policy text itself was not re-read today.

#### 2.4 C2PA for audio files
- The C2PA 2.2 specification defines manifest embedding for audio. MP3 and FLAC use an ID3v2 GEOB frame: "The C2PA Manifest Store shall be embedded into a ID3v2-compatible, compressed audio file (e.g., MP3 or FLAC)…". WAV and BWF use a RIFF chunk: "…embedded into a RIFF-compatible file (i.e., WAV, AVI or WebP) as the data of a chunk with an identifier of C2PA."
  - URL [P]: https://spec.c2pa.org/specifications/specifications/2.2/specs/C2PA_Specification.html (Annex A.3.4 and A.3.6)
- Teaching point: C2PA is metadata and can be stripped. SynthID is a watermark inside the signal. They complement each other. The Gemini Help page notes that Content Credentials "can show whether AI was involved, but they don't confirm that a file is AI-generated."

---

#### 3. Law and policy on synthetic voices

#### 3.1 EU AI Act Article 50
- **Application date confirmed:** "Article 50 of the AI Act applies as from 2 August 2026."
- **Grace period (Digital Omnibus):** "A limited grace period is envisaged only for AI systems placed on the market before 2 August 2026 … Providers of such systems must comply with those obligations only as from **2 December 2026**." The grace period covers only Art. 50(2), the marking and detection duty. It does not cover the Art. 50(4) deepfake disclosure duty for deployers.
- Retroactivity: "Content generated prior to 2 August 2026 does not need to be labelled retroactively."
- **Fines:** "Fines can reach up to 15 million euros or 3% of total worldwide turnover for the preceding financial year".
- Deepfake definition includes audio: "AI-generated or manipulated image, audio or video content that resembles existing persons, objects…" that "would falsely appear to a person to be authentic or truthful."
  - URL [P]: https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act (checked 2026-10-12)
- Article text. **Art. 50(2):** providers of systems "generating synthetic audio, image, video or text content" shall ensure outputs "are marked in a machine-readable format and detectable as artificially generated or manipulated." **Art. 50(4):** deployers of deepfakes "shall disclose that the content has been artificially generated or manipulated". A lighter regime applies to evidently artistic or satirical works.
  - URL [S, unofficial consolidated text]: https://artificialintelligenceact.eu/article/50/ ; official: Regulation (EU) 2024/1689 on EUR-Lex (EUR-Lex returned an empty page today).
- **Digital Omnibus on AI status:** Commission page: political agreement **7 May 2026**; "entered into force on 27 July 2026". High-risk Annex III rules now "apply from 2 December 2027" and Annex I rules from 2 August 2028. A new prohibition on non-consensual sexual deepfakes / CSAM ("nudification" apps) "comes into effect in December 2026".
  - URL [P]: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
  - Council voting record: adopted **29 June 2026** (Council doc 11301/26, file 2025/0359 (COD), "Digital Omnibus on AI – Adoption of the legislative act"). https://data.consilium.europa.eu/doc/document/ST-11301-2026-INIT/en/pdf [P]
  - OJ reference appears to be OJ L 2026/1744 (from a search-result title). **NOT VERIFIED:** EUR-Lex returned an empty response.
- **Code of Practice on Transparency of AI-Generated Content:** published **10 June 2026**. Quote: "These AI systems benefit from a transitional period for compliance until 2 December 2026." The Art. 50 FAQ says the Commission and AI Board assessed it as adequate. A Commission opinion is dated 9 July 2026.
  - URL [P]: https://digital-strategy.ec.europa.eu/en/faqs/code-practice-transparency-ai-generated-content

#### 3.2 US: FCC ruling on AI voices in robocalls (Feb 2024)
- "WASHINGTON, **February 8, 2024**—Today the Federal Communications Commission announced the unanimous adoption of a Declaratory Ruling that recognizes calls made with AI-generated voices are "artificial" under the Telephone Consumer Protection Act (TCPA). The ruling, which takes effect immediately, makes voice cloning technology used in common robocall scams targeting consumers illegal."
  - URL [P]: https://docs.fcc.gov/public/attachments/DOC-400393A1.txt ; ruling FCC 24-17 (CG Docket 23-362): https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf
  - Related: FCC proposed a **$6 million** fine for AI-voice-cloned election robocalls (cited in FCC 24-84, https://docs.fcc.gov/public/attachments/FCC-24-84A1.pdf) [P].

#### 3.3 Tennessee ELVIS Act (2024)
- Ensuring Likeness, Voice, and Image Security Act of 2024, HB2091 / SB2096, **Public Chapter 588**. Signing ceremony 21 Mar 2024. The legislature record shows "Signed by Governor" dated 03/26/2024. **Effective 1 July 2024.** Passed the House 93-0 and the Senate 30-0.
- Bill summary: "an individual also has a property right in the use of that individual's voice". It also creates liability for distributing "an algorithm, software, tool, or other technology… whose primary purpose is the production of an individual's photograph, voice, or likeness" without authorization.
  - URLs [P]: https://wapp.capitol.tn.gov/apps/BillInfo/Default?BillNumber=HB2091&ga=113 ; https://www.tn.gov/governor/news/2024/3/21/photos--gov--lee-signs-elvis-act-into-law.html

#### 3.4 NO FAKES Act: not law as of 2026-10-12
- The current vehicle is **S.4591, "NO FAKES Act of 2026"** (119th Congress), with identical House bill **H.R.8915**.
  - 2026-05-20: introduced and referred to Senate Judiciary.
  - 2026-06-18: "Ordered to be reported with an amendment in the nature of a substitute favorably."
  - 2026-06-24: "Placed on Senate Legislative Calendar under General Orders. Calendar No. 446." This is the **latest action**. There has been no floor vote.
  - H.R.8915: latest action 2026-05-20, "Referred to the House Committee on the Judiciary."
  - The 2025 versions (S.1367 / H.R.2794) stalled in committee after 2025-04-09.
  - Source [P]: congress.gov API (https://api.congress.gov/v3/bill/119/s/4591/actions), human page https://www.congress.gov/bill/119th-congress/senate-bill/4591

#### 3.5 TAKE IT DOWN Act (signed May 2025)
- S.146, "Became Public Law No: **119-12**" on **2025-05-19**.
- Scope: CRS summary. The act "prohibits the nonconsensual online publication of intimate visual depictions of individuals, both authentic and computer-generated". Covered platforms "must remove such depictions within **48 hours** of notification."
- **Teaching note:** it covers **visual** depictions only, not voice or audio. Do not present it as a voice law.
  - URL [P]: https://www.congress.gov/bill/119th-congress/senate-bill/146 (via api.congress.gov summaries)
- Platform compliance deadline (one year after enactment, 19 May 2026): **NOT VERIFIED** in today's fetch.

#### 3.6 Denmark: likeness and voice protection in copyright law, still a bill
- Ministry of Culture press release, **8 Oct 2026**: "Kulturminister Zenia Stampe fremsætter i dag et lovforslag" (the Culture Minister introduces a bill today). It makes it illegal to share realistic digital imitations of a person, "herunder vedkommendes udseende og stemme" (including their appearance and voice). It has an exception for "karikaturer, parodier, satire og magt- og samfundskritik". The minister "håber, loven kan træde i kraft allerede ved årsskiftet" (hopes the law can take effect at the turn of the year).
  - URL [P]: https://kum.dk/aktuelt/nyheder/kulturminister-vil-daemme-op-for-delinger-af-digitale-efterligninger-fra-aarsskiftet
- Status as of 2026-10-12: **introduced, not adopted.** Secondary reports [S] give it the number **L 49** with a target date of 1 Jan 2027 (aipolicydesk.com, ppc.land). ft.dk was blocked (403), so the bill number and date are **NOT VERIFIED**.
- History: political agreement of 26 June 2025 and a draft consultation from 7 July 2025 (ft.dk KUU bilag 232). The earlier plan to take effect on 31 Mar 2026 slipped.

#### 3.7 Notable 2026 voice-deepfake fraud case
- **Fideuram (Intesa Sanpaolo private bank), Italy, February 2026:** about **€95 million** was wired to foreign accounts, mainly in China and Hong Kong. Fraudsters sent a fake WhatsApp message from the group CEO and then made a phone call in which the voice of a real lawyer, **Paolo Nastasi** (A&O Shearman Italia), was cloned with AI. **€36 million** was still missing; a Chinese bank returned €40M and a Portuguese bank recovered further sums. Milan prosecutors are investigating. The case became public on 25 Sep 2026.
  - Quote (Il Post): "circa 95 milioni di euro su conti esteri"; "mancano ancora 36 milioni"; "avrebbero riprodotto la voce di Nastasi usando strumenti di intelligenza artificiale".
  - URL [S, news; based on Corriere della Sera / Reuters]: https://www.ilpost.it/2026/09/25/fideuram-truffa-whatsapp-ai/ ; https://gulfnews.com/world/europe/ai-voice-cloning-scam-hits-italian-bank-fake-executives-trigger-95m-overseas-transfers-1.500688692
  - No official bank or police statement was found. **Treat as press-reported.**
- Regulator context [P]: FBI IC3 PSA **I-051525-PSA (15 May 2025)** warns of "text messages and AI-generated voice messages" impersonating senior US officials "Since April 2025". It recommends independent call-back verification and a family code word. https://www.ic3.gov/PSA/2025/PSA250515
- Arup, Hong Kong 2024: about US$25.6M lost via a deepfake video call. This is older and a video case; mention only as background [S].

---

#### 4. Consent mechanics at vendors

| Vendor | Mechanism | Quote | URL [P] |
|---|---|---|---|
| **ElevenLabs PVC** | The voice owner reads text from a CAPTCHA image, live | "a verification step is required to ensure you have permission to use the voice." "The image contains several lines of text that the voice owner will need to read out loud and record." Manual verification "should only be used if the previous verification steps have failed or are not possible." | https://elevenlabs.io/docs/eleven-api/guides/how-to/voices/professional-voice-cloning |
| **Google Chirp 3 Instant Custom Voice** | Recorded consent statement (≤10 s) + allow-list | "Access to Instant Custom Voice is restricted to allow-listed users." The statement reads "I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model." | https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice |
| **Google Gemini 3.8 Flash TTS voice replication** (2026) | Must send `consent_audio` from the same speaker; "The service verifies consent" | "I am the owner of this voice and have consented to the creation of a synthetic model of my voice through the use of Google Cloud." Reference audio 10–30 s. | https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/text-to-speech/voice-replication ; Gemini API: https://ai.google.dev/gemini-api/docs/speech-generation |
| **Microsoft Azure personal voice** | Verbal consent statement + restricted access | "it's required that every voice be created with explicit consent from the user." "Access to the API is restricted to eligible customers and approved use cases." Audio prompt 5–90 s. | https://learn.microsoft.com/en-us/azure/ai-services/speech-service/personal-voice-overview |
| **Microsoft professional voice (Custom Neural Voice)** | Limited Access registration + voice talent statement + **written permission** | "custom neural voice is a Limited Access feature available by registration only, and only for certain use cases." "Customers must warrant that they have obtained explicit written permission from voice talent prior to creating a voice model". Customers "will disclose the synthetic nature of the service to users". Statement: "I [state your first and last name] am aware that recordings of my voice will be used by [state the name of the company] to create and use a synthetic version of my voice." | https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/text-to-speech/limited-access ; https://learn.microsoft.com/en-us/azure/ai-services/speech-service/professional-voice-create-consent |
| **OpenAI custom voices** (2026) | Eligible customers only; consent recording + matching sample | "Custom voices are limited to eligible customers." "Consent recording: This recording captures the voice actor providing consent to create a likeness of their voice." "The voice must match the consent recording." "At most 20 voices can be created per organization." Samples must be "30 seconds or less". Phrase: "I am the owner of this voice and I consent to OpenAI using this voice to create a synthetic voice model." "Any divergence from the script will lead to a failure." | https://developers.openai.com/api/docs/guides/custom-voices |

**Pattern for the slide:** every major vendor requires two things: (1) the speaker's own voice saying a fixed consent sentence, matched against the sample, and (2) gating through an allow-list, eligibility review or live CAPTCHA. None of them takes a checkbox alone.

---

#### 5. Primary guidance on written consent for cloning employees' voices
- **Found (vendor, primary):** Microsoft's Limited Access terms require customers to "warrant that they have obtained **explicit written permission** from voice talent prior to creating a voice model" and to share the "Disclosure for voice and avatar talent" with the talent in advance. The same page assigns the customer responsibility for "(i) providing notice to data subjects, including with respect to retention periods and destruction; (ii) obtaining consent from data subjects; and (iii), deleting the Biometric Data". This is the closest primary rule that fits an employee-voice case.
  - URL [P]: https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/speech-service/text-to-speech/limited-access
- **Regulator guidance that names employee voice cloning:** **NOT FOUND.** UK ICO biometric guidance (drafts) and the EDPB consent guidelines address employee consent and biometric data in general, not voice cloning. They were not re-fetched today, so their contents are **NOT VERIFIED**. A general GDPR principle, reported only by secondary law-firm commentary, is that consent in employment is rarely "freely given" because of the power imbalance.

---

### Items NOT VERIFIED (summary)
- Veo audio-off switch on the Gemini API (only Vertex `generateAudio` is documented).
- "No music" negative cue as official Google guidance.
- Kling consumer-app credit rates with and without audio; Kling 2.6 audio pricing.
- OJ number of the Digital Omnibus on AI (L 2026/1744) and its final Art. 50 wording (EUR-Lex was unreachable).
- Danish bill number L 49 and its 1 Jan 2027 target date (ft.dk was blocked; the minister said only "ved årsskiftet").
- Official bank or police statement on the Fideuram case (press only).
- OpenAI usage-policies page text (403). The disclosure quote comes from the OpenAI TTS docs.
- Regulator guidance specific to employee voice cloning.

**Volatile: recheck 24h before class**
