# Instructor Script • Lesson 06: Speech and Audio AI — Voice Synthesis, Whisper, Foley Sound Design, and AI Music (90 Minutes)

**Course:** GenAI Basics • Module 2 (Multimodality) • Lesson 06 of 16 (Module 2 Finale)  
**Instructor:** Igor Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems  
**Hands-on AI R&D:** Architect & Developer of Creator Tools — AI suite for YouTube creators (Hands-on AI R&D pet-project)  
**Target Audience:** Software engineers, QA, DevOps, tech leads, solution architects  
**Format:** 24 slides (`presentation_L06_Speech_and_Audio_EN.html` / PDF) • live demos: Whisper, ElevenLabs, Cartesia, Suno v4 • interactive break timer on slide 14  
**Materials:** Lesson repository, Colab notebook `notebooks/L06_Speech_and_Audio_AI_Pipeline.ipynb`, runbook `L06_04_Live_Demo_Runbook_READY_EN.md`, homework `L06_05_Homework_EN.md`  
**Models on slides:** OpenAI Whisper (large-v3-turbo, whisper.cpp), ElevenLabs Multilingual v2, Cartesia Sonic, Kokoro-82M, Suno v4, Udio 1.5, ElevenLabs SFX, Silero VAD, Descript Audio Codec (DAC).

**Lesson Objective:** The student masters the full neural audio technology stack; understands the physics of PCM waveforms, STFT, and discrete neural codecs (EnCodec/DAC); extracts word-level subtitle timestamps in Whisper; eliminates silence hallucination loops via Silero VAD integration; selects optimal TTS engines balancing latency and prosodic emotionality (Cartesia vs. ElevenLabs); directs cadence and speech pauses via punctuation and SSML; analyzes voice cloning security risks and mitigation mechanisms (Dynamic Voice Captcha, SynthID); applies the 3-slot Foley formula for physical sound design; generates cinematic instrumental scores in Suno v4; mixes a 3-stem audio package with Sidechain Ducking in Python; and designs low-latency real-time voice agent architectures (<300ms budget).

---

## Lesson Pacing & Timetable

| Slide | Block | Time | Format | Demo / Focus | Key Takeaway |
|---|---|---|---|---|---|
| **01** | Title Cover | 00:00 — 02:00 | Intro | — | Module 2 grand finale. From 1D acoustic pressure waves to discrete neural codecs. The 10/90 Axiom in audio: neural generation is 10%; VAD, LUFS, watermarking, and stem mixing is 90%. |
| **02** | Blind Listening Hook | 02:00 — 05:00 | Interactive | 4 Audio Clips A–D | Chat poll. Which clips are studio recordings and which are AI? Auditory cues: breath intake, sibilants, room reflections. |
| **03** | Evolution 2020–2026 | 05:00 — 08:00 | Timeline | WaveNet to Codecs | All 4 clips are 100% generative AI! Timbre is solved; 2026 challenges are sub-150ms conversational latency and multi-stem phase alignment. |
| **04** | Curriculum Roadmap | 08:00 — 10:00 | Stepper | Bridge from L05 | Video clips from L05 were mute! Today we bring our courier and packshot to life with speech, wheel spray Foley, and music. |
| **05** | Sound Physics & Codecs | 10:00 — 14:00 | Theory | PCM ➔ STFT ➔ Mel ➔ DAC | Audio as discrete tokens. How neural codecs (RVQ) enabled Transformers to generate 48kHz audio streams. |
| **06** | STT: Whisper Architecture | 14:00 — 18:00 | Architecture | Encoder-Decoder | 30-second windows, task control prefix tokens, word-level subtitle extraction via Cross-Attention matrices (`word_timestamps`). |
| **07** | Whisper in Prod & VAD | 18:00 — 22:00 | Architecture | Whisper Hallucinations | Why Whisper loops infinitely during silence. Production mitigation: Silero VAD (silence pruning) + faster-whisper (CTranslate2). |
| **08** | TTS Landscape 2026 | 22:00 — 26:00 | Matrix | 4 Model Classes | ElevenLabs (cinematic) vs Cartesia Sonic (135ms, agents) vs Kokoro-82M (local $0 WASM) vs Bark. |
| **09** | Speech Directing & Prompting| 26:00 — 30:00 | Prompting | Punctuation & Controls | Ellipses as breath intake, em-dashes as pauses. ElevenLabs controls: Stability (drama vs FAQ), Similarity Boost. |
| **10** | Voice Cloning | 30:00 — 34:00 | Comparison | Instant vs Pro (PVC) | d-vector speaker embeddings (1 min, inherits mic noise) vs deep LoRA weight fine-tuning (45 min studio, 98% fidelity). |
| **11** | Security & Watermarking | 34:00 — 38:00 | Ethics & Sec | Voice Captcha & SynthID | Phishing and spoofing vectors. Defenses: dynamic Voice Captcha (reading verification phrase), imperceptible SynthID/PerTh, C2PA. |
| **12** | Blast Radius in Audio | 38:00 — 43:00 | Governance | Green / Yellow / Red | Creator-consented dubbing (Green), customer support bots with mandatory AI disclosure (Yellow), unconsented voice cloning (Red). |
| **13** | STS & Dubbing (100+ Lang) | 43:00 — 47:00 | R&D Case | Creator Tools Pipeline | Preserving original speaker timbre. Syllable budget in LLM translation and elastic time-stretching via phase vocoder. |
| **14** | **Midpoint: Break** | **47:00 — 52:00** | **5-Min Timer** | **Pure Rest Only** | **No chat assignments. Speaker and audience recharge auditory senses before Part 2.** |
| **15** | Foley SFX Generation | 52:00 — 56:00 | Prompting | 3-Slot Foley Formula | [Source Material] + [Kinetic Action] + [Acoustic Space]. Benchmarks for bicycle wheel splashes and coffee steam. |
| **16** | Storyboard Sound Matrix | 56:00 — 60:00 | Matrix | Giant Stories Case | Creator Tools 7-column production matrix: mapping 5-second cuts to Foley layers and musical hooks. |
| **17** | Music Generation (Suno v4) | 60:00 — 64:00 | Models | Suno v4 vs Udio 1.5 | Stereo 48kHz. Instrumental toggle (preventing vocal clashing with dialogue), Extend Audio, Stem Splitting (Demucs). |
| **18** | Soundtrack Architecture | 64:00 — 68:00 | Score Spec | 5 Slots & Structural Tags | Genre + BPM + Instrumentation + Mood + Structural Tags (`[Intro]`, `[Verse]`, `[Build-up]`, `[Outro]`). |
| **19** | Multi-Stem Mixing Standards | 68:00 — 72:00 | Standards | LUFS & Sidechain Ducking| Voiceover (-14 LUFS) + SFX (-18 LUFS) + Music (-22 LUFS with -5dB ducking). Scripting in Python with `pydub`. |
| **20** | Real-Time Voice Agents | 72:00 — 76:00 | Architecture | Latency Budget (<300ms) | WebRTC ➔ Silero VAD (15ms) ➔ Whisper (80ms) ➔ Groq (50ms) ➔ Cartesia (90ms) = 285ms. Barge-in handling. |
| **21** | Code: Python Automation | 76:00 — 80:00 | Python SDK | Colab Walkthrough | Whisper word timestamps, streaming TTS API calls, stem overlaying via `overlay()`. |
| **22** | Audio Quality Audit (QA) | 80:00 — 84:00 | Checklist | 4 Acoustic Defects | Digital clipping (> -1 dBFS), phase comb-filtering (3kHz), prosody drift, lip-sync latency (<40ms). |
| **23** | Homework Assignment #6 | 84:00 — 88:00 | Practice | 3-Stem L05 Soundtrack | Score 5-second video from L05 (voice + SFX + music), submit `audio_qa.md`. Send collaborator invite. |
| **24** | Module 2 Wrap & L07 Teaser | 88:00 — 90:00 | Open Mic | Module 2 Finale | 4 engineering laws of audio. Teaser for L07: Microsoft 365 Copilot, GitHub Copilot, Graph, and Agent Mode. |

---

## Detailed Slide-by-Slide Script (Slides 01 — 24)

### Part 1: Acoustic Physics, STT (Whisper), and Speech Synthesis (00:00 — 47:00)

---

### Slide 01 (00:00 — 02:00) • Title Cover: Speech and Audio AI
**On Screen:** Clean, dark C4-themed title slide. Title: `Speech and Audio AI: Text-to-Speech, Whisper, Foley Sound Design, and AI Music`. Subtitle: `From 1D acoustic pressure waves and mel-spectrograms to discrete neural codecs, word-level timestamps, and synchronized multi-stem audio`. 10/90 Axiom callout card.

#### Speaker Delivery:
> "Hello everyone, and welcome! Today marks a major milestone: we are concluding Module 2 of our curriculum — Multimodality.
> 
> Let us review our engineering progression so far:
> * In **Lesson 04**, we mastered the generation of static visual assets: consistent characters, lighting vectors, and photorealistic product shots.
> * In **Lesson 05**, we animated those assets across time using diffusion transformers (Image-to-Video) to produce cinematic 5-second video shots.
> 
> But if you inspect the video outputs from Lesson 05, you will notice one critical flaw: they are completely mute. There is no physical sound of bicycle tires splashing through rain, no human voiceover, no atmospheric musical score. In cinema, commercial advertising, and interactive applications, audio accounts for at least 50% of the perceived quality. A viewer will tolerate slightly imperfect visual rendering, but harsh, distorted, or unsynchronized audio causes users to close a video within the first 3 seconds.
> 
> Today, we treat generative audio as a rigorous systems engineering discipline. Here, our **10/90 Axiom** holds true with absolute precision: generating raw audio waveforms with a neural network represents only 10% of a production system. The remaining 90% consists of Voice Activity Detection (VAD), LUFS loudness compliance, word-level subtitle alignment, anti-spoofing security, conversational latency budgets below 150 milliseconds, and multi-stem audio engineering. Let us dive in!"

---

### Slide 02 (02:00 — 05:00) • Blind Listening Hook: The Turing Test for Ears
**On Screen:** Four interactive audio sample cards labeled [A] through [D]. Question banner: *"Can your auditory perception distinguish synthetic audio from physical acoustic recording?"*.

#### Speaker Delivery:
> "We begin with a practical calibration of your ears. Before you are four studio-grade audio recordings:
> * **Clip [A]:** A warm, documentary narrator's voice with subtle breath intakes and natural dental sibilants.
> * **Clip [B]:** The Foley sound of a bicycle: rubber cutting through a gravel rainwater puddle, water spray, and chain rattle.
> * **Clip [C]:** An acoustic jazz trio: upright piano, brushed snare drum, and walking acoustic bass.
> * **Clip [D]:** A customer support telephone operator with instantaneous conversational turn-taking and natural filler words ('uh-huh', 'got it, sure').
> 
> Open the chat right now: which of these four clips were captured with physical studio microphones in the real world, and which were synthesized by neural networks? I am giving you 45 seconds. Post your predictions in the chat!"

*(The instructor pauses for 45 seconds, scanning chat responses: "A is definitely human, the breath intake is too natural," "C is live jazz musicians, you cannot synthesize swing timing," "D sounds like a real call center").*

> "Thank you for the votes! The majority of you are convinced that the jazz trio [C] or the documentary narrator [A] are authentic human recordings. Let us advance to the next slide!"

---

### Slide 03 (05:00 — 08:00) • Evolution 2020–2026: All 4 Are Pure AI!
**On Screen:** Four chronological evolutionary milestones: 2020 WaveNet ➔ 2022 Whisper & ElevenLabs v1 ➔ 2024 Suno v3 & EnCodec ➔ 2026 Cartesia, Whisper Turbo & Suno v4.

#### Speaker Delivery:
> "Every single one of these four audio clips is **100% neural network generation from 2026**!
> * The narrator [A] was generated in 1.5 seconds using ElevenLabs Multilingual v2.
> * The bicycle puddle Foley [B] was generated by ElevenLabs SFX using a text prompt.
> * The jazz trio [C] was composed and rendered in Suno v4 in Instrumental mode.
> * And the phone call [D] was driven by an interactive conversational agent powered by Cartesia Sonic with a Time-to-First-Audio latency of just 135 milliseconds!
> 
> Look at the historical timeline on your screen: only six years ago, in 2020, we were stuck in the WaveNet era. Speech synthesis was plagued by metallic comb-filtering, robotic cadences, and awkward unnatural pauses. In 2022, Whisper and ElevenLabs proved that deep learning could both transcribe and synthesize human speech with human-level accuracy and studio warmth.
> 
> By 2026, the question of acoustic timbre and fidelity is solved. Today's primary engineering challenges are **ultra-low conversational latency (sub-150ms for voice agents)** and **deterministic multi-stem mixing** without phase interference and frequency masking."

---

### Slide 04 (08:00 — 10:00) • Curriculum Roadmap & Bridge from L05
**On Screen:** Module 2 visual progression roadmap. A clear flow arrow showing the mute video assets from L05 (Glovo courier and ceramic mug) receiving a synchronized 3-layer soundtrack (voiceover, Foley, music).

#### Speaker Delivery:
> "Let us look at our architectural curriculum roadmap. Module 1 established the foundation: tokens, prompting vectors, and API integration. In Module 2, we have executed an end-to-end creative pipeline:
> * In Lesson 04, we generated the high-resolution source images: our Glovo courier in the rain `C2_rain.jpg` and our studio coffee mug `D0_packshot.png`.
> * In Lesson 05, we animated those images in Kling and Runway: camera dolly movements, rotating steam, and spinning bike wheels.
> 
> But as we noted, those video files are silent. Today, we construct the complete 3-stem acoustic architecture for them:
> 1. **Stem 1 — Voiceover Narration:** A concise, cinematic narrative line.
> 2. **Stem 2 — Foley Sound Effects (SFX):** Grounded physical audio: tires cutting through water or ceramic meeting polished oak.
> 3. **Stem 3 — Background Music Score:** An instrumental thematic underscore that dynamically ducks in volume whenever speech occurs.
> 
> By the end of this session, your mute clips will be transformed into fully realized commercial video deliverables."

---

### Slide 05 (10:00 — 14:00) • Physics of Sound & Discrete Neural Codecs
**On Screen:** Four architectural transformation stages: 1D PCM Waveform ➔ Short-Time Fourier Transform (STFT) ➔ 2D Mel-Spectrogram ➔ Neural Discrete Codecs (EnCodec, DAC).

#### Speaker Delivery:
> "Now let us look under the hood. What makes audio fundamentally harder for neural networks than text or static images?
> 
> Text is discrete by definition: tokens from a vocabulary. An image is a 2D matrix of discrete pixels at a fixed resolution. But sound is a **continuous, one-dimensional pressure wave propagating through air across time**.
> 
> Consider standard CD-quality audio at 44.1 kHz: a single second of mono audio consists of **44,100 continuous floating-point samples**. If we attempted to feed those raw samples into an autoregressive transformer the way we feed text tokens into an LLM, the model's context window would be exhausted after just two seconds of audio!
> 
> Historically, speech recognition circumvented this problem using the **Short-Time Fourier Transform (STFT)** to produce **Mel-Spectrograms**: breaking audio into overlapping 25-millisecond windows and mapping frequency energy onto a psychoacoustic mel scale. This 2D representation is exactly what OpenAI Whisper consumes as input.
> 
> However, the true breakthrough in generative audio occurred in 2024 with the introduction of **discrete neural audio codecs (Meta's EnCodec and Descript Audio Codec — DAC)**.
> 
> How does a neural codec operate? It employs Residual Vector Quantization (RVQ). An encoder compresses continuous 48 kHz studio audio through several quantization codebooks into a discrete stream of **integer tokens — at just ~50 tokens per second**!
> 
> This is a profound shift: neural codecs converted continuous acoustic waveforms into a **discrete language** that standard Transformer architectures can model autoregressively. This single architectural leap unlocked Bark, Suno, Udio, and modern ElevenLabs."

---

### Slide 06 (14:00 — 18:00) • STT: Whisper Architecture & Timestamps
**On Screen:** Architectural diagram of OpenAI Whisper. Dual-tower Encoder-Decoder Transformer, 30-second audio chunking, task control prefix tokens, and the Cross-Attention word alignment block (`word_timestamps=True`).

#### Speaker Delivery:
> "Let us examine the first foundational pillar of speech technology: Speech-to-Text (STT). In industry production, the global standard remains OpenAI Whisper.
> 
> Look at the dual-tower architecture on your screen:
> 1. **Audio Encoder:** Consumes an 80- or 128-channel mel-spectrogram representing a 30-second audio slice. Two 1D convolutional layers downsample the time dimension by a factor of 4, followed by a stack of standard Transformer self-attention blocks extracting deep acoustic representations.
> 2. **Text Decoder:** An autoregressive Transformer decoder. Notice how it is steered: via special prefix prompt tokens: `<|startoftranscript|>`, language selection tokens like `<|en|>` or `<|es|>`, task tokens (`<|transcribe|>` for transcription or `<|translate|>` for direct translation into English), and timestamp formatting tokens.
> 
> Now, pay close attention to the right-hand panel: **Word-Level Timestamps**. In production video pipelines, getting raw text is insufficient. You need to know the exact millisecond each individual word was spoken so your automated rendering engine can burn perfectly synchronized subtitle cards onto the screen.
> 
> By running Whisper with `word_timestamps=True`, the model inspects the Cross-Attention weights between the text decoder and audio encoder tokens. Using dynamic time warping (DTW), it identifies the precise acoustic boundaries for every single word with an error margin under 20 milliseconds. You get production-ready `.srt` and `.sbv` files with zero manual alignment!"

---

### Slide 07 (18:00 — 22:00) • Whisper in Production: Hallucinations & Silero VAD
**On Screen:** Two-column production failure vs. solution comparison. Left: raw Whisper failure modes (infinite repetition loops in silence, music masking). Right: production pipeline (Silero VAD pre-filtering + faster-whisper CTranslate2 runtime).

#### Speaker Delivery:
> "However, if you take raw Whisper from OpenAI's repository and run it blindly on an hour-long corporate video or podcast, you will encounter serious production bugs.
> 
> **Failure Mode 1: Infinite Repetition Loops in Silence.**  
> Whisper's decoder is an autoregressive language model. If a speaker pauses or finishes speaking, leaving only microphone hiss, room noise, or silence in the 30-second window, the decoder cannot emit silence tokens. It conditions on its own previously predicted tokens and spirals into an infinite hallucination loop trained from its YouTube crawl: *'Thank you for watching! Don't forget to like and subscribe...'*.
> 
> **Failure Mode 2: Music Masking.**  
> Loud background music often leads Whisper to classify an entire speech segment as non-verbal noise, returning an empty transcript string.
> 
> **How do production systems resolve this?**
> By implementing a two-stage pipeline:
> 1. **Silero VAD at the Ingestion Boundary:** Silero Voice Activity Detection is an ultra-lightweight neural network (under 1 MB). In less than 2 milliseconds, it scans the raw waveform, detects genuine human speech boundaries, and strips away all silence and background noise. Whisper receives **only verified speech segments**. This completely eliminates silence hallucination loops!
> 2. **faster-whisper Engine (CTranslate2 Runtime):** By reimplementing Whisper in optimized C++ with INT8 and FP16 quantization, faster-whisper executes **4 times faster than standard PyTorch Whisper** while cutting GPU memory consumption in half."

---

### Slide 08 (22:00 — 26:00) • TTS Landscape 2026: Latency vs. Fidelity
**On Screen:** Four model cards categorized by architectural profile: ElevenLabs Multilingual v2, Cartesia Sonic, Kokoro-82M, and Bark.

#### Speaker Delivery:
> "Now let us examine the reverse problem: Text-to-Speech (TTS). In 2026, the landscape is partitioned into four distinct engineering categories:
> 1. **Studio Cloud Leaders (ElevenLabs Multilingual v2):** The benchmark for human expressiveness, 48 kHz studio fidelity, and 32+ languages. Ideal for pre-rendered video narration, voice acting, and audiobooks. Time-to-First-Audio latency is approximately 350 milliseconds.
> 2. **Ultra-Low Latency Conversational Engines (Cartesia Sonic):** Built on State-Space Model architectures rather than heavy Transformers, Cartesia achieves a breakthrough latency: **135 milliseconds to first audio byte**! This is designed specifically for real-time telephone agents and interactive voice bots.
> 3. **Open-Weight Edge Models (Kokoro-82M):** A compact model with just 82 million parameters under an Apache 2.0 license. It runs entirely on local CPUs or inside web browsers via WebAssembly. Zero cloud API costs, zero data exfiltration.
> 4. **Paralinguistic Experimental Models (Suno Bark):** Fully autoregressive generative audio capable of rendering human non-verbal vocalizations: sighs, laughter, hesitations, throat clearing, and whispered phrases.
> 
> The architectural selection heuristic: Use ElevenLabs for high-end video post-production. Use Cartesia Sonic for real-time voice agents. Use Kokoro-82M for offline, cost-sensitive, or privacy-critical applications."

---

### Slide 09 (26:00 — 30:00) • Speech Directing & TTS Prompting
**On Screen:** Left: punctuation cues and SSML/IPA phonetic syntax. Right: ElevenLabs control sliders (Stability, Similarity Boost, Style Exaggeration).

#### Speaker Delivery:
> "How do we direct the prosody, pacing, and emotional expression of a synthetic voice? Writing text for a TTS engine is fundamentally different from writing prose for visual reading.
> 
> **Punctuation as Musical Notation:**
> * Ellipses (`...`) force the model to take an audible breath and decelerate speech velocity.
> * Em-dashes (`—`) create a pronounced pause, allowing dramatic emphasis before a key phrase.
> * Capitalizing entire words signals the acoustic decoder to apply prosodic stress and pitch elevation.
> * For complex enterprise or brand names (such as Glovo or EPAM), bypass spelling ambiguity using International Phonetic Alphabet (IPA) tags: `<phoneme alphabet="ipa" ph="ɡloʊvoʊ">Glovo</phoneme>`.
> 
> **Tuning Engine Parameters:**
> Pay close attention to the **Stability** slider in ElevenLabs:
> * Set to **0.30**: The voice becomes highly dynamic, emotionally charged, and theatrical — ideal for drama and cinematic trailers.
> * Set to **0.85**: The model dampens pitch variance and delivers an authoritative, uniform delivery — mandatory for corporate documentation, legal disclaimers, and interactive IVR systems."

---

### Slide 10 (30:00 — 34:00) • Voice Cloning: Instant vs. Professional
**On Screen:** Two-column comparison: Instant Voice Cloning (IVC, zero-shot, d-vectors) vs. Professional Voice Cloning (PVC, LoRA deep weight fine-tuning).

#### Speaker Delivery:
> "Let us examine voice cloning. There are two fundamentally different engineering approaches:
> 
> **1. Instant Voice Cloning (IVC / Zero-Shot):**  
> Requires only 60 seconds of reference audio. The system extracts a 512-dimensional speaker embedding vector (d-vector) and conditions the base foundation model during synthesis. Setup time is 5 seconds, and training cost is $0.  
> *The architectural pitfall:* Acoustic similarity is around 80%. Furthermore, if your 60-second reference sample was recorded on a laptop microphone with room reverberation and air conditioning hum, that room acoustic and noise floor are permanently baked into every generated audio file!
> 
> **2. Professional Voice Cloning (PVC / Full Model Adaptation):**  
> Requires 30 to 60 minutes of pristine, dry studio recordings. A dedicated training pipeline fine-tunes low-rank adaptation weights (LoRA) on enterprise GPUs over 2 to 4 hours.  
> *The outcome:* 98% acoustic fidelity, immaculate articulation, and the ability to synthesize whispers, shouts, and nuanced inflections in the authentic vocal timbre of the subject."

---

### Slide 11 (34:00 — 38:00) • Security, Anti-Spoofing & Watermarking
**On Screen:** Three architectural blocks: 2026 Threat Vectors, Dynamic Voice Captcha (consent verification), and In-Band Audio Watermarking (Google SynthID Audio, ElevenLabs PerTh, C2PA manifests).

#### Speaker Delivery:
> "Now we must address security. Voice cloning introduces severe enterprise risk surfaces: executive impersonation (CEO voice fraud), social engineering phishing attacks, and biometric bypass against banking voice authentication systems.
> 
> How does modern enterprise engineering defend against these vectors?
> 1. **Dynamic Voice Captcha:** You cannot simply upload an illicit audio recording of an executive to clone their voice. Modern platforms generate a dynamic, one-time verification script containing the current timestamp and a randomized cryptographic phrase that the voice owner must read aloud live into their camera.
> 2. **In-Band Acoustic Watermarking (Google SynthID for Audio and ElevenLabs PerTh):** The generative engine introduces micro-modulations into the phase relationships of inaudible high-frequency harmonics. To human ears, the sound is pristine. But an automated spectral detector can mathematically verify the presence of the synthetic watermark — even after MP3 compression, filtering, and ambient room re-recording!
> 3. **C2PA Cryptographic Provenance:** Cryptographically signed metadata injected directly into the audio container documenting model provenance and asset creation timestamps."

---

### Slide 12 (38:00 — 43:00) • Blast Radius Matrix in Audio
**On Screen:** Risk governance traffic light: Green Zone (Autonomous), Yellow Zone (Human-in-the-Loop), Red Zone (Strictly Prohibited).

#### Speaker Delivery:
> "Let us reinforce our enterprise boundaries using our Blast Radius framework:
> * **Green Zone (Autonomous Execution):** Ambient Foley generation, authorized dubbing of creator-owned videos (as implemented in Creator Tools), and rough-cut voiceovers for internal design prototypes. Risk of damage is zero.
> * **Yellow Zone (Human-in-the-Loop Co-Pilots):** Tier-1 customer support voice agents (which must include a mandatory audio disclosure: *'You are speaking with an automated virtual assistant'*), and commercial brand advertising (which must pass audio QA sign-off by a lead sound designer prior to broadcast).
> * **Red Zone (Strictly Forbidden for Autonomous Execution):** Cloning the voice of any third party without explicit signed consent, synthesizing emergency response announcements, generating synthetic courtroom evidence, or spoofing financial biometrics. These carry severe legal liability and must be blocked at the API gateway."

---

### Slide 13 (43:00 — 47:00) • Speech-to-Speech & Multilingual Dubbing (100+ Lang)
**On Screen:** Architecture diagram of the Creator Tools Multilingual Dubbing Pipeline. Whisper ➔ LLM Translation with Syllable Budgeting ➔ Voice Conversion ➔ Phase Vocoder Elastic Time-Stretching.

#### Speaker Delivery:
> "Let me share an authentic engineering case study from my R&D work on Creator Tools — our automated multilingual dubbing pipeline supporting 100+ languages for YouTube creators.
> 
> What is the primary engineering bottleneck in direct video translation? **Variable syllable density across languages.** A sentence spoken in German or Russian is, on average, 25% longer in syllable count than the exact same thought expressed in English. If you translate the text verbatim and render it with a TTS engine, the audio track drifts: the video scene has already cut away, but the translated voiceover is still speaking!
> 
> **How did we solve this in Creator Tools?**
> 1. Whisper transcribes the original dialogue and extracts precise word timestamps.
> 2. A calibrated LLM system prompt enforces a strict **Syllable Budget**, instructing the translation model to choose concise synonyms that match the source timing.
> 3. A Voice Conversion neural network renders the target language while cloning the unique vocal timbre, pitch contours, and breath dynamics of the original speaker.
> 4. A Phase Vocoder performs **Elastic Time-Stretching** to fine-tune cadence within a ±15% window without introducing pitch distortion.
> 
> The result: an audience in Brazil, Germany, or Japan hears the creator speaking their native language with frame-accurate synchronization to on-screen cuts!"

---

### Slide 14 (47:00 — 52:00) • Midpoint: 5-Minute Break
**On Screen:** Interactive countdown timer with a 'START 5 MIN' trigger button. Summary card previewing the second half.

#### Speaker Delivery:
> "We have reached our midpoint. Processing audio engineering concepts places heavy cognitive demands on your auditory system.
> 
> We are taking a strict 5-minute break. I am triggering the countdown timer on the screen. Please step away from your monitors, drink some water, and give your ears complete silence. Do not post work questions in the chat during this window — this time is reserved exclusively for mental recharge. We reconvene in exactly 5 minutes!"

*(The instructor starts the timer. 5 minutes of quiet intermission).*

---

### Part 2: Foley SFX, Music, Multi-Stem Mixing, Voice Agents & Homework (52:00 — 90:00)

---

### Slide 15 (52:00 — 56:00) • Sound Effects (SFX AI): Generating Foley from Text
**On Screen:** 3-Slot Foley Prompt Formula. Real-world benchmark prompts for the Glovo courier bicycle splash and the coffee mug packshot.

#### Speaker Delivery:
> "Welcome back, everyone! Let us initiate the second half of our session: physical sound effects, music generation, and multi-track audio engineering.
> 
> Historically, sound editors spent hours hunting through stock SFX libraries to find matching Foley recordings. Today, state-of-the-art models like ElevenLabs SFX and Stable Audio generate custom, photorealistic physical sound effects directly from descriptive text prompts.
> 
> Here is our **3-Slot Foley Prompt Formula**:
> 1. **Slot 1 — Physical Material (Source):** Explicit acoustic materials interacting (`rubber tires`, `ceramic mug`, `hollow oak`).
> 2. **Slot 2 — Kinetic Action (Dynamics):** The velocity, force, and nature of the mechanical motion (`splashing violently`, `scraping stone`, `steam hissing`).
> 3. **Slot 3 — Acoustic Environment (Space):** Geometric acoustics and reverberation characteristics (`outdoor wet alleyway reflections`, `dry soundstage`, `cavernous warehouse echo`).
> 
> Look at our reference prompt on the slide for our Glovo courier:  
> `Bicycle rubber tires splashing violently through a deep rainwater puddle on wet cobblestone, fine water spray, quiet evening city background hum, cinema foley`.  
> The model synthesizes the exact acoustic signature of rubber meeting water with pristine spatial positioning!"

---

### Slide 16 (56:00 — 60:00) • Storyboard Sound Design (Creator Tools Giant Stories Case)
**On Screen:** Four-scene production table excerpted from the Creator Tools *Giant Stories* workflow, demonstrating the mapping of 5-second cuts to Foley layers and musical hooks.

#### Speaker Delivery:
> "Let us look at how this operates within an industrial production matrix. Before you is an excerpt from our Creator Tools *Giant Stories* workflow:
> * **Shot 1 (A Wax-Sealed Vault Crate from 1929):** The Foley layer specifies a low stone basement resonance, occasional water drips, and the skitter of a rat. The musical hook is a low, bowed contrabass drone.
> * **Shot 2 (Oil Derrick Drilling in Texas Heat):** The Foley layer features cicadas buzzing in oppressive heat and a heavy shovel scraping across dry stone. The musical hook is a pulsing sub-bass beat every two seconds.
> * **Shot 3 (Rotary Printing Press):** The Foley layer delivers mechanical rhythm and ink spray hisses. The music introduces a rising tremolo violin section.
> 
> Here is the critical takeaway: sound design must be architected **before video generation**, not tacked on as an afterthought! When you assemble your video cuts, your acoustic blueprints are already locked."

---

### Slide 17 (60:00 — 64:00) • AI Music Generation: Suno v4 and Udio 1.5
**On Screen:** Three technical feature cards: Suno v4 (48 kHz stereo, Instrumental Toggle), Udio 1.5 (Audio Inpainting), and Neural Stem Separation (Demucs v4).

#### Speaker Delivery:
> "The third layer of our soundtrack is background music. In 2026, the two industry powerhouses are Suno v4 and Udio 1.5.
> 
> Both platforms synthesize 3- to 4-minute full musical arrangements in broadcast-grade 48 kHz stereo.
> 
> **An Essential Production Rule for Video Soundtracks:**  
> Always activate the **Instrumental Toggle**! If your generative music track includes synthesized vocal lines, those vocal formants will clash directly with your narrator's voice, rendering the spoken words unintelligible to the audience.
> 
> Now observe the right-hand panel: **Neural Stem Separation**. Using models like Meta's Demucs v4, you can take any generated stereo music master and isolate it into four discrete tracks: drums, bass, melodic instruments, and vocals. This enables precise level adjustments and EQ sculpting during your final mix."

---

### Slide 18 (64:00 — 68:00) • Music Prompt Architecture & Structural Tags
**On Screen:** 5-Slot Music Prompt Specification and structural tag markup in the lyrics editor (`[Intro]`, `[Verse]`, `[Build-up]`, `[Outro]`).

#### Speaker Delivery:
> "How do we direct the dynamic arc of an AI music score? We employ a 5-Slot prompt structure:
> 1. **Genre & Subgenre:** `Lo-fi acoustic chillhop` or `Cinematic neo-classical ambient`.
> 2. **Tempo & Cadence (BPM):** Precise rhythmic speed (`slow 74 BPM` or `driving 120 BPM pulse`).
> 3. **Instrumentation:** Specific acoustic timbres (`fingerpicked acoustic guitar, upright bass, brushed snare`).
> 4. **Mood & Texture:** `Melancholic, twilight ambience, introspective warmth`.
> 5. **Structural Tags in the Lyrics Window:**  
> Even in instrumental mode, the lyrics text area serves as an arrangement console!
> Writing `[Intro]` commands the model to begin with a delicate, sparse motif. Adding `[Build-up]` cues the entrance of strings to heighten emotional tension. Adding `[Outro]` instructs the composition to resolve gracefully, aligning with your final video cut."

---

### Slide 19 (68:00 — 72:00) • Multi-Stem Mixing Standards & Sidechain Ducking
**On Screen:** Target LUFS levels for the three audio stems. Sidechain Ducking diagram showing automated -5 dB attenuation on music whenever voiceover is active.

#### Speaker Delivery:
> "We have three distinct audio stems: voiceover, Foley effects, and background music. How do we blend them into a cohesive master?
> 
> If you simply sum the three audio files at full volume, the mix will clip, distort, and collapse into acoustic mud. We apply broadcast audio engineering standards:
> * **Stem 1 — Voiceover Narration:** Target integrated loudness of **-14 LUFS** with true peaks below -1.0 dBFS. High-pass filter everything below 80 Hz to remove low-end rumble.
> * **Stem 2 — Foley Sound Effects:** Target loudness of **-18 LUFS**, panned across the stereo field to match on-screen spatial movement.
> * **Stem 3 — Music with Sidechain Ducking:** During pauses, the music sits at -18 LUFS. But the moment the narrator speaks, automated ducking attenuates the music by **-4 to -6 dB** (down to -22 LUFS). When speech ends, the music smoothly ramps back to nominal level.
> 
> In Python, using `pydub`, this entire ducking calculation and multi-track rendering requires less than 10 lines of clean code!"

---

### Slide 20 (72:00 — 76:00) • Real-Time Voice Agents (<300ms Latency Budget)
**On Screen:** Real-time latency budget waterfall: WebRTC Audio In (20ms) ➔ Silero VAD (15ms) ➔ Streaming Whisper Turbo (80ms) ➔ Groq LLaMA 3.3 (50ms) ➔ Cartesia Sonic (90ms) = **285ms**. Barge-in handling loop.

#### Speaker Delivery:
> "Let us look beyond pre-rendered video editing toward the frontier of AI systems in 2026: **Real-Time Interactive Voice Agents**.
> 
> Why can we not rely on standard batch APIs? Because human psychology interprets conversational pauses longer than 300 milliseconds as phone lag, connection drops, or awkward hesitation.
> 
> Examine the latency budget on your screen:
> 1. WebRTC audio packet ingestion: 20 ms
> 2. Voice end-of-speech detection via Silero VAD: 15 ms
> 3. Streaming speech-to-text in Whisper Turbo: 80 ms
> 4. Time-to-First-Token generation via Groq or Cerebras LLaMA 3.3: 50 ms
> 5. Streaming Time-to-First-Audio in Cartesia Sonic: 90 ms
> 6. Client speaker playback buffer: 30 ms
> 
> **Total round-trip latency: 285 milliseconds!** The agent responds with instantaneous, human-like cadence!
> 
> Furthermore, if the user interrupts mid-sentence, our **Barge-In** circuit trips: the client VAD sends an interrupt signal over WebSocket, canceling server generation and terminating audio playback within 20 milliseconds."

---

### Slide 21 (76:00 — 80:00) • Python API Automation: Pipeline Implementation
**On Screen:** Two executable Python snippets: Whisper word timestamp extraction and `pydub` multi-stem overlay with ducking. Direct link to Google Colab.

#### Speaker Delivery:
> "Let us look at the production code. In our companion Colab notebook, `notebooks/L06_Speech_and_Audio_AI_Pipeline.ipynb`, we have implemented the full pipeline:
> * In Block 1, we execute Whisper and parse word boundaries to generate timestamped subtitle files.
> * In Block 2, we load our three stems and execute `music.overlay(voice).overlay(sfx)` with dynamic gain adjustments to output our master `.wav` and `.mp4` container.
> 
> The notebook is thoroughly tested, includes synthetic audio generators for offline execution, and runs at $0 cost on free GPU tiers."

---

### Slide 22 (80:00 — 84:00) • Audio Quality Assurance (Audio QA) Checklist
**On Screen:** 4 Critical Acoustic Defects: Digital clipping (> -1 dBFS), metallic comb-filtering (3 kHz), prosody drift, and lip-sync offset (> 40 ms).

#### Speaker Delivery:
> "Before any audio deliverable is shipped to production, it must pass a rigorous engineering quality audit:
> 1. **Digital Clipping:** Peak signal levels must never exceed -1.0 dBFS. Any signal attempting to cross 0 dBFS results in harsh digital distortion on mobile speakers.
> 2. **Phase Comb-Filtering:** Inspect the frequency spectrogram around 3 kHz. If the voice exhibits a tinny, hollow telephone timbre, switch to a 48 kHz neural vocoder.
> 3. **Prosody Drift:** If a synthetic voice abruptly shifts pitch or energy mid-sentence, increase the Stability slider to lock consistency.
> 4. **Lip-Sync Latency:** For on-camera dialogue, discrepancy between visible lip closure on bilabial consonants (B, P, M) and acoustic transients must remain below 40 milliseconds. Human vision immediately detects larger synchronization lags."

---

### Slide 23 (84:00 — 88:00) • Homework Assignment #6
**On Screen:** GitHub submission tree for `genai-homeworks/L06/`. Three audio stems: `01_voiceover.mp3`, `02_foley_sfx.mp3`, `03_music_bg.mp3`, `final_video_with_audio.mp4`, and `audio_qa.md`.

#### Speaker Delivery:
> "Here is your homework assignment for Lesson 06.
> 
> Your objective is to take the 5-second video clip you generated in Lesson 05 (the Glovo courier, the coffee mug packshot, or a cut from your storyboard) and produce a professional 3-stem soundtrack:
> 1. **Stem 1 (Voiceover):** Generate one concise narrative line using ElevenLabs, Cartesia, or Kokoro.
> 2. **Stem 2 (Foley SFX):** Synthesize realistic physical sound effects (puddle splashes, steam hiss, ceramic clink) using ElevenLabs SFX.
> 3. **Stem 3 (Background Music):** Compose an instrumental score in Suno v4 or Udio, ducked under the narrator's voice.
> 
> Assemble the final video in your editor of choice or using our Colab script, complete the `audio_qa.md` checklist, and commit your assets to `genai-homeworks/L06/` on GitHub. Add `ihar_rubanovich@epam.com` as a collaborator. Feedback will be provided within 48 hours."

---

### Slide 24 (88:00 — 90:00) • Module 2 Wrap & Lesson 07 Teaser (Copilot)
**On Screen:** 4 Engineering Laws of Audio. Module 2 completion banner. Teaser for Module 3 (Lesson 07: Microsoft 365 Copilot, GitHub Copilot, Semantic Index, and IDE Agent Mode).

#### Speaker Delivery:
> "To conclude our session, let us review our 4 Engineering Laws of Audio:
> 1. **VAD First:** Never pass raw audio into Whisper without upstream Silero VAD silence pruning.
> 2. **Punctuation Governs Breath:** Shape TTS rhythm using ellipses and em-dashes.
> 3. **Instrumental Only for Video:** Never include AI vocals in background music beneath dialogue.
> 4. **Sidechain Ducking:** Always attenuate background music by 5 dB whenever speech occurs.
> 
> Congratulations, everyone: **Module 2: Multimodality is officially complete!** You now command the skills to produce studio-grade images, cinematic video, and broadcast-ready audio.
> 
> Next week, we launch **Module 3: AI in Software Engineering**. We will explore **Microsoft 365 Copilot, GitHub Copilot, Graph grounding architectures, and autonomous Agent Mode in modern IDEs**. We will also analyze the real-world **EPAM CodeMie @ Dawn Foods** case study, which delivered a verified 35% SDLC acceleration!
> 
> Thank you for your time and focus today. The floor is now open for your questions!"
