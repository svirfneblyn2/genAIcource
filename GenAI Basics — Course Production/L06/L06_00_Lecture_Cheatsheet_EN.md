# 1-Page Speaker Cheatsheet • Lesson 06 (v2: 21 Slides • 90 Minutes)
*Speaker: Ihar Rubanovich (EPAM Systems • ihar_rubanovich@epam.com)*  
*Topic: Speech and Audio. Voice-over, sound and music for a video • facts as of 2026-10-12*  
*Presentation: `presentation_L06_Speech_and_Audio_EN_v2.html` (PDF: same basename) • source: `deck_v2/build.py` • full script: `L06_02_Instructor_Script_90MIN_EN.md`*  
*Homework: `L06_05_Homework_EN.md` • Repo: `genai-homeworks/L06/` • Collaborator: `ihar_rubanovich@epam.com`*

---

### Teams: before you start
* **Sound is required.** Share → turn on **“Include sound”** (older Teams: “Include computer sound”). Test one clip before class.
* Deck: `F` fullscreen, `←/→` navigate, `N` notes, `G` slide grid. Audio and video play **on click, with sound**. The PDF shows “▶ audio / video in the HTML version”.
* Clicks: **sl. 2** voiced courier video (23 s) • **sl. 6** two Veo audio clips • **sl. 10** music bed • **sl. 12** optional live demo: drop `mix_en.mp3` into Google AI Studio, prompt “Transcribe verbatim. Do not correct mistakes.” • **sl. 15** timer “Start” • **sl. 16** clone sample, then clone.
* Pipeline (6 steps, strip on slides 7–12): **1** script • **2** spoken text • **3** voice • **4** effects and music • **5** mix • **6** check.

---

### Part 1 (00:00–58:00)
* **01 Cover (2, 00–02):** L04 images → L05 video → today voice, sound, music.
* **02 Example (3, 02–05):** voiced L05 video. 3 lines, 9.3 s of speech, open-weight voices on a laptop (Kokoro EN, Piper RU); 3 tracks: voice + Veo’s own sound + MusicGen bed; **−14.4 LUFS**. Not perfect: errors found on sl. 12.
* **03 Where to generate (4, 05–09):** chat (ChatGPT, Gemini app with Lyria 3.5) • web studios (ElevenLabs, Suno, Google AI Studio; homework here) • API (OpenAI, Gemini API, Google Cloud / Azure Speech, ElevenLabs, Deepgram / AssemblyAI) • 4th path: open weights (Whisper, Kokoro, Piper, MusicGen), $0/min, licences differ.
* **04 Four tasks (4, 09–13):** text-to-speech (TTS) • speech-to-text (STT, also ASR) • speech-to-speech • music and sound effects. A voice-over uses three of them.
* **05 How it works (4, 13–17):** text → model → audio tokens → decoder → waveform. Gemini bills 25 audio tokens/s; MusicGen 50 steps/s; studio audio 48,000 numbers/s. No reading rules inside → numbers, names, abbreviations fail.
* **06 Audio inside video models (4, 17–21):** Veo invented “Here’s your order. Thank you. Have a good day.” (shot 1) and “Continue straight for 200 meters…” (failure clip); no dialogue in either prompt. Veo 3.1 on Vertex AI: **$0.40/s with audio, $0.20/s without** (`generateAudio`); Gemini API: always on. Exact words → separate voice.
* **07 Step 1 script (5, 21–26):** one row per shot: time, line, words / length, effects, music. Measured 3.2 words/s; plan 2–2.5 (RU 1.8–2.2). **8 s shot ≈ 6 s speech ≈ 12–15 words.** Exercise: line for shot 4, ≤12 words.
* **08 Step 2 spoken text (5, 26–31):** 6:42 → “six forty-two”, 417 → “four one seven” (you decide), 12 min → “twelve minutes”. Style: OpenAI `instructions`, Gemini 3.8 `style` field, ElevenLabs v3 tags `[whispers]`, pronunciation dictionaries.
* **09 Step 3 voice (4, 31–35):** library (Gemini 30 voices, OpenAI 13) • designed from a description • clone only with written consent (ElevenLabs Instant 1–2 min, Professional 30+ min; open models clone from 3 s). Test the hard words first.
* **10 Step 4 effects and music (4, 35–39):** our MusicGen bed (CC BY-NC: lesson only). Suno v6: commercial rights only on paid plans • Lyria 3.5: SynthID on every track • ElevenLabs Music 3 s–5 min • ElevenLabs Sound Effects ≤30 s.
* **11 Step 5 mix (5, 39–44):** voice −19.2 LUFS, Veo −22.8 → mix **−14.4 LUFS, −2.2 dBTP** in the final MP4 (AAC raises the peak, so limit to −3 dBTP before encoding). Ducking; Spotify −14, Apple Podcasts −16, EBU R128 −23; true peak ≤ −1 dBTP. First pass RU −0.6 dBTP failed → two-pass + limiter. No code: Audacity Auto Duck → Loudness Normalization → Limiter.
* **12 Step 6 check (6, 44–50):** Whisper small on the mix. EN: WER 18.5%, “Here’s your order” leaks from Veo audio, “642” = transcriber format → critical terms 3/4 → **4/4 after listening**. RU: «Часть 42», «Оно» = voice errors, 2/4. Never paste the script into a transcription prompt.
* **13 Local models (4, 50–54):** Hugging Face model card + weight files → cached on disk → Python package → CPU or GPU → WAV, offline. Kokoro 0.36 GB and Whisper small run on a laptop CPU (our voice-over and check). Qwen3-TTS 0.6B: 2.5 GB, CPU ≈9× slower than real time (our run); 1.7B: 4.5 GB, GPU with 8 GB+ (third-party). $0 per minute, but hardware, electricity, setup time; local wins for privacy, steady volume, experiments. Architectures (batch / streaming / voice agent) only in notes.
* **14 Market (4, 54–58):** see slide. Open ASR Leaderboard 9 Oct 2026: best commercial ≈4%, best open ≈5%, Whisper large-v3 7.84%. OpenAI shuts down tts-1 / gpt-4o-mini-tts **06.01.2027**, whisper-1 / gpt-4o-transcribe **26.02.2027**.

### Break (58:00–63:00)
* **15 Break (5):** “Start”. Rest only, no chat tasks.

### Part 2 (63:00–90:00)
* **16 Agent + local clone (4, 63–67):** prompt for Claude Code / Antigravity / Codex: check hardware → separate Python env → `pip install qwen-tts` → download `Qwen/Qwen3-TTS-12Hz-0.6B-Base` (Apache-2.0) → `clone.py` with `generate_voice_clone(text, language, ref_audio, ref_text)` → run offline. Sample 3–10 s + exact transcript. Our demo: synthetic Kokoro sample, CPU, EN 4.6 s in 42 s. Own voice only. Gemini API code moved to README.
* **17 Cost (4, 67–71):** table below. Voicing our video ≈ 1 cent. An hour of ElevenLabs voice ($4.80) = 12 s of Veo 3.1. Homework example ≈ $0.07 at list price, $0 on free tiers.
* **18 Acceptance (5, 71–76):** 1 words • 2 pronunciation • 3 timing • 4 mix (no stray speech) • 5 loudness −14 ± 1 LUFS, true peak ≤ −1 dBTP • 6 rights and AI label. Both our versions rejected (EN: Veo line; RU: voice + Veo line missed by Russian speech-to-text). **= homework rubric.** Meter without code: Youlean Loudness Meter, DaVinci Resolve.
* **19 Risks (4, 76–80):** green library/designed voice • amber own or colleague’s clone with written consent • red client/manager/public figure. OpenAI and Google: consent phrase; ElevenLabs Professional: read-out; Azure: application only; open models: no checks. EU AI Act Art. 50 from 2 Aug 2026, fines €15M / 3%. OpenAI: disclose AI voice. Fideuram ≈€95M (press reports, Feb 2026).
* **20 Homework (7, 80–87):** voice your L05 video in 6 steps; two no-code voice services; background with licence; −14 ± 1 LUFS + meter screenshot; `transcript.txt`, `audio_qa.md`, `audio_spec.md`; end caption “AI-generated”. Own voice or library voices only.
* **21 Summary (3, 87–90):** 6 rules, one per step. Next: L07 GitHub, Microsoft 365 and Copilot.

---

### Key numbers (checked 2026-10-12)
| What | $ / second | $ / minute | $ / hour |
|---|---|---|---|
| Gemini 3.8 Flash TTS ($9 / 1M audio tokens, until 31.12.2026) | $0.00022 | $0.0135 | $0.81 |
| ElevenLabs v3 / v4 ($0.08 / 1K characters) | $0.00133 | $0.08 | $4.80 |
| OpenAI gpt-transcribe | $0.00007 | $0.0045 | $0.27 |
| ElevenLabs Scribe v2 | $0.00006 | $0.0037 | $0.22 |
| OpenAI gpt-live-1 (+ backend model) | $0.00083 | $0.05 | $3.00 |
| ElevenLabs Music | $0.0025 | $0.15 | $9.00 |
| Conversion | 1 minute of speech ≈ 1,000 characters (ElevenLabs) | | |

### Recheck within 24 hours of class
Gemini TTS model ID and call shape • Gemini TTS price change on 01.01.2027 • OpenAI deprecation dates (TTS 06.01.2027, gpt-realtime 20.01.2027, transcribe 26.02.2027) • ElevenLabs prices and free credits • Suno v6 plans • Veo 3.1 with / without audio prices • Open ASR Leaderboard figures • Lyria 3.5 availability • EU AI Act Art. 50(2) grace period • Teams “Include sound” label • Fideuram case figures. Full list: end of `L06_08_Source_Notes_Research_2026-10.md`.
