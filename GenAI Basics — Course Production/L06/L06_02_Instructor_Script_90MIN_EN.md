# Instructor Script • Lesson 06: Speech and Audio AI. Voice-over, Sound and Music for a Video (90 Minutes)

**Course:** GenAI Basics • Module 2 (Multimodality) • Lesson 06 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles. Plain language, no formulas; code only as one short reference example.
**Format:** 21 slides (`presentation_L06_Speech_and_Audio_EN_v2.html` / PDF) • class runs in **Microsoft Teams** • break timer on slide 15
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen. Videos and audio start **on click** and play **with sound**.
**Source of truth:** `deck_v2/build.py` (slide text and speaker notes). This script is generated from it (`deck_v2/make_docs.py`); if anything differs, `build.py` wins.
**Materials:** the voiced video and tracks in `assets/v2/` (made by `deck_v2/make_audio.py` from the L05 video), the measurement report `demo_courier_audio/report.json`, homework `L06_05_Homework_EN.md`.
**Facts:** as of October 2026, sources in `L06_08_Source_Notes_Research_2026-10.md`. The “recheck within 24 hours” list is at the end of the cheatsheet.

> **Before you start (Teams):** this lesson needs sound. When sharing your screen, turn on **“Include sound”** in the Share window (older Teams versions: “Include computer sound”). Test the sound on one clip before class.

**Lesson objective:** students understand the four audio AI tasks (text-to-speech, speech-to-text, speech-to-speech, music and sound effects), know where to run them (chat, web studio, API, open-weight models), can voice a video with a 6-step pipeline (script, text for the voice, voice, sound effects and music, mix, check), can estimate the cost of a second, a minute and an hour of audio, accept the result with a checklist and follow the voice consent rules.

---

## Timing (21 slides • 90 minutes incl. a 5-minute break)

| Slide | Title | Time | Min |
|---|---|---|---|
| **01** | Speech and Audio | 00:00–02:00 | 2 |
| **02** | The L05 courier video with voice-over, sound and music | 02:00–05:00 | 3 |
| **03** | Start in a web studio, automate with the API | 05:00–09:00 | 4 |
| **04** | Four audio AI tasks: what goes in and what comes out | 09:00–13:00 | 4 |
| **05** | The model guesses how text sounds, so it trips on numbers and names | 13:00–17:00 | 4 |
| **06** | Veo makes up its own lines: exact words need a separate voice | 17:00–21:00 | 4 |
| **07** | Voice-over script: text, timing and a word budget for each shot | 21:00–26:00 | 5 |
| **08** | Spoken text: numbers as words, style as a separate instruction | 26:00–31:00 | 5 |
| **09** | Three sources of a voice: library, description, clone | 31:00–35:00 | 4 |
| **10** | Sound effects and music: the licence matters most | 35:00–39:00 | 4 |
| **11** | Mixing: voice on top, background ducked, loudness normalised | 39:00–44:00 | 5 |
| **12** | Speech-to-text found errors we missed by ear | 44:00–50:00 | 6 |
| **13** | Open-weight models: $0 per minute, paid for in hardware and time | 50:00–54:00 | 4 |
| **14** | Audio models by task: commercial and open-weight | 54:00–58:00 | 4 |
| **15** | 5 minutes for coffee and resting your ears | 58:00–63:00 | 5 |
| **16** | A coding agent installs Qwen3-TTS locally and clones a voice | 63:00–67:00 | 4 |
| **17** | An hour of audio costs cents to dollars; an hour of video, over a thousand | 67:00–71:00 | 4 |
| **18** | Both our versions failed acceptance: here is the checklist | 71:00–76:00 | 5 |
| **19** | Risks and voice consent: cloning, labelling, law | 76:00–80:00 | 4 |
| **20** | Homework 6: voice your L05 video | 80:00–87:00 | 7 |
| **21** | Lesson summary | 87:00–90:00 | 3 |

Part 1 (slides 01–14, 00:00–58:00): tasks, models and the 6-step pipeline. Break (slide 15, 58:00–63:00). Part 2 (slides 16–21, 63:00–90:00): agent voice cloning, cost, acceptance, risks, homework, summary.

---

### Slide 01 (00:00–02:00) • Speech and Audio

**On screen:** Background: a frame from L05 shot 2 (the courier in the rain). Title, subtitle, lesson scope, key hints.

#### Speaker (2 min)
> Welcome. Third lesson of the multimodality module: in L04 we made images, in L05 we turned them into video, today we add voice, sound and music.
>
> Plan: a finished voiced video, where to generate, four audio tasks, how a model handles sound, what audio inside video models can do, then a 6-step pipeline, local models and the market. After the break: an agent clones a voice, cost, acceptance, risks and voice consent, homework.
>
> Before you start: Teams: this lesson needs sound. In Share, turn on “Include sound” (older versions: “Include computer sound”). Test the sound on one clip before you start.

---

### Slide 02 (02:00–05:00) • The L05 courier video with voice-over, sound and music

**On screen:** Left: the voiced courier video (23 s, with sound, click to play). Right: three numbers: 3 lines, 3 tracks, final loudness in LUFS.

#### Speaker (3 min)
> Start the clip with a click, with sound (23 seconds). It is the same L05 video: three Veo 3.1 shots. Ask the chat: what do you hear, how many layers of sound?
>
> Answer: three layers. The narrator: three lines, 9.3 seconds of speech from an open-weight text-to-speech model running on a laptop (Kokoro for English, Piper for Russian). The sound Veo generated with the video: cafe, rain. And a music bed from the open MusicGen model. Everything is mixed to −14 LUFS (Loudness Units relative to Full Scale, a loudness measure), the level Spotify normalises tracks to.
>
> The result is not perfect: later in the lesson we find its errors with speech-to-text. That is today’s main skill: produce, then check.
>
> Teams: this lesson needs sound. In Share, turn on “Include sound” (older versions: “Include computer sound”). Test the sound on one clip before you start.

---

### Slide 03 (05:00–09:00) • Start in a web studio, automate with the API

**On screen:** A full-width Google AI Studio → Generate speech frame with callouts 1–4 (text, style, model, result); below it the legend, the key code line from Get code and two more paths (chat, open models).

#### Speaker (4 min)
> The same choice as in L04 and L05: chat, web studio, API. Chat apps: ChatGPT voice mode, the Gemini app with Gemini Live; since September 2026 the Gemini app also makes music with Lyria 3.5. Good for trying things, but you barely control the voice, pace and length.
>
> The screenshot is Google AI Studio, Generate speech (captured 16.10.2026): 1 the line text, 2 the style in its own field, 3 the model and voice, 4 the result, ready to download. Free and no code; you can show it live in a minute. Other web studios: ElevenLabs (voices, cloning, sound effects, music, dubbing), Suno (songs). This is where the homework happens.
>
> Application programming interfaces (APIs): OpenAI (speech synthesis, transcription, Realtime), Gemini API (speech generation, Live, Lyria), Google Cloud and Azure Speech, ElevenLabs API, Deepgram and AssemblyAI for transcription. Billed per character of text, per audio token or per minute of audio; we compare them on the cost slide.
>
> Open weights: our whole example was made with them on a laptop without a graphics card. Free per minute, but each model has its own licence; MusicGen, for example, is non-commercial only.

---

### Slide 04 (09:00–13:00) • Four audio AI tasks: what goes in and what comes out

**On screen:** Four input → output cards: text-to-speech, speech-to-text, speech-to-speech, music and sound effects; under each, an “in our example” line (Kokoro/Piper, Whisper, —, MusicGen).

#### Speaker (4 min)
> “Audio AI” hides four different tasks. Look at input and output. Text to voice: text-to-speech, TTS. Voice to text: speech-to-text, STT, also called automatic speech recognition, ASR; same thing. Voice to voice: voice agents and translation. Text to music and sound effects.
>
> Different tasks use different models and different prices: synthesis is billed per character, transcription per minute, voice agents per minute of conversation, music per track.
>
> Voicing a video uses three of the four tasks: text-to-speech for the voice, music and effects for the background, speech-to-text for the check. Voice agents get one architecture slide; you build agents in module 5 (L11–L13).

---

### Slide 05 (13:00–17:00) • The model guesses how text sounds, so it trips on numbers and names

**On screen:** Chain text → model → audio tokens → decoder → waveform; the real waveform of line 1; two notes: data volume and why numbers and names fail.

#### Speaker (4 min)
> Link to L03 and L05: a language model predicts text tokens, a video model denoises frames. A speech model predicts audio tokens, compressed chunks of sound. A decoder (also called a vocoder) turns them back into a waveform.
>
> Scale: at 48 kHz one second of audio is 48,000 numbers. The model does not work at that level; it sees a compressed representation. Two real numbers: Gemini bills speech at 25 audio tokens per second; MusicGen, which made our music, takes 50 steps per second (4 tokens per step). Architectures differ; the principle is the same.
>
> Key point: there is no rule inside like “read 417 as four hundred seventeen”. The model has seen many text and audio pairs and guesses. That is why numbers, names and abbreviations are the most common errors. This is step 2.

---

### Slide 06 (17:00–21:00) • Veo makes up its own lines: exact words need a separate voice

**On screen:** Two players with Veo audio (shot 1 and the L05 failure clip) and the text recognised in them. Below: what video-model audio gives and does not give.

#### Speaker (4 min)
> Play both. Left: shot 1 from L05. The prompt had no dialogue, yet Veo voiced the barista and the courier: “Here’s your order. Thank you. Have a good day.” Right: the L05 failure clip. The prompt mentions a navigation map, and Veo added a navigator voice: “Continue straight for 200 meters”. We did not notice this until we ran the audio through speech-to-text.
>
> Takeaway. A video model’s audio works as background: noise, rain, footsteps, in sync with the picture. It is not free: on Vertex AI (now Gemini Enterprise Agent Platform) the generateAudio parameter turns Veo 3.1 audio off, and a second then costs $0.20 instead of $0.40; on other services such as Kling 3.0, audio also costs extra. The Gemini API documents no switch to turn Veo audio off. And the main point: a video model does not give exact words, the same voice across three shots or separate tracks for editing. It makes up lines.
>
> Rule: when you need exact words, generate the voice separately with text-to-speech, and use the video model’s audio as background or mute it. Google’s Veo prompting guide puts dialogue in quotes, sound effects after “SFX:” and background after “Ambient noise:”; that helps but guarantees nothing.

---

### Slide 07 (21:00–26:00) • Voice-over script: text, timing and a word budget for each shot

**On screen:** Script table: frame, time, line, words / length, sound effects. Below: measured speech rate and the word budget rule.

#### Speaker (5 min)
> L05 slide 7 showed the full 7-column storyboard template; in the L05 homework you filled in only the video part. Today we add the three audio columns: voice-over, sound effects, music. One row = one shot = one line.
>
> Word budget. Our voice speaks about 3.2 words per second. Plan with 2–2.5 words per second (Russian: 1.8–2.2, the words are longer) and leave about a second of silence at each cut: an 8-second shot has about 6 seconds of speech, so 12–15 words. If the text does not fit, cut the text. Speeding up the voice sounds unnatural.
>
> Exercise (1 min, chat): write the line for shot 4, “courier at the door”, in 12 words or fewer.

---

### Slide 08 (26:00–31:00) • Spoken text: numbers as words, style as a separate instruction

**On screen:** Table script → spoken text → why for 6:42, 417, 12 min. Right: a style instruction example and three ways to control the voice.

#### Speaker (5 min)
> The script is written for the viewer: “6:42”, “417”. The speech model gets a separate “spoken text” column with everything written out as words. Otherwise the model guesses: is 6:42 a time, a score or a ratio? Is 417 a number or an order ID read digit by digit?
>
> Voice style is a separate instruction, not part of the text. In OpenAI and Gemini it is a natural-language phrase: “calm, friendly dispatcher”. ElevenLabs v3 uses tags inside the text, such as [whispers]. For names and terms, ElevenLabs, Google and Azure offer pronunciation dictionaries.
>
> Who decides how 417 is read? You do, in the script, not the model. Even with correct text the voice can still get it wrong, especially in less common languages and open models. We check that in step 6.

---

### Slide 09 (31:00–35:00) • Three sources of a voice: library, description, clone

**On screen:** Left: two library voices from Google AI Studio (1) and the legend; right: the Create voice cards, Voice Design (2) and Replication (3), a caption and the tip to test the hardest words before choosing a voice.

#### Speaker (4 min)
> Three sources of a voice; all three are visible in Google AI Studio (screenshots from 16.10.2026). A library voice: the service’s licence already covers it. Gemini has 30 prebuilt API voices, OpenAI 13. Our example uses Kokoro af_heart for English and Piper dmitri for Russian. Create new voice opens the other two paths: Voice Design (a voice from a description; in AI Studio it needs the paid tier) and Voice Replication (a clone from a short recording; the service asks you to verify the voice is yours). The clone card is greyed out in the screenshot: it is not enabled on our account, which is normal; it is turned on separately and only for your own voice.
>
> Technically: one line = one file (line1.wav, line2.wav…). In the editor, place each file at the start time from the script and check it is not longer than the shot’s speech window. Designed voice: describe the voice in text and the service generates a new one. Available in ElevenLabs (Voice Design) and the Gemini API. Check that the result does not sound like a known person.
>
> Clone: a real person’s voice from recordings. ElevenLabs Instant needs 1–2 minutes of audio, Professional 30 minutes or more. Open models such as Qwen3-TTS clone from 3 seconds. That is why the big services ask for proof of consent: OpenAI and Google require a recorded fixed consent phrase, Azure gives access only on application, and ElevenLabs asks the voice owner to read a verification text for a professional clone. Details on the risk slide.

---

### Slide 10 (35:00–39:00) • Sound effects and music: the licence matters most

**On screen:** Player with the MusicGen bed, its prompt and licence. Right: table of Suno v6, Lyria 3.5, ElevenLabs Music and SFX (length, commercial use).

#### Speaker (4 min)
> Play the bed. The open MusicGen-small model made it from the prompt on the left, on a laptop, 23 seconds to match the video. A music prompt works like an image prompt: genre, instruments, mood, tempo, “no vocals”.
>
> The point here is the licence, not the quality. MusicGen weights are CC-BY-NC: fine for a lesson, not for a commercial video. For services, rights depend on your plan at the moment of generation: Suno gives commercial rights only on paid plans; on the free plan Suno owns the songs, and upgrading later does not grant rights retroactively. Google’s Lyria 3.5 is in the Gemini app and the Gemini API, and every track carries an invisible SynthID mark. ElevenLabs Music: 3 seconds to 5 minutes, “cleared for nearly all commercial uses” under their terms. ElevenLabs sound effects: up to 30 seconds per generation.
>
> Often the sound effects already exist: the video model’s own audio from L05 (cafe, rain). We use it as the background.

---

### Slide 11 (39:00–44:00) • Mixing: voice on top, background ducked, loudness normalised

**On screen:** Four real tracks (voice, Veo audio, music, mix) with loudness; three rules (ducking, loudness, peak) and the ffmpeg command.

#### Speaker (5 min)
> These are the real tracks of our video. The voice alone is −19.2 LUFS, Veo’s audio −22.8 LUFS, then music and the final mix. The background gets quieter where the voice speaks: that is ducking. It is hard to see on the picture; listen for it.
>
> LUFS is a loudness unit that follows human hearing. Streaming platforms normalise tracks to their level: Spotify to −14 LUFS, Apple Podcasts to −16. The European Broadcasting Union broadcast standard EBU R128 is −23. A quieter video gets raised together with its noise; a louder one gets turned down. The second number is true peak: no higher than −1 dBTP, otherwise MP3 or AAC encoding adds distortion.
>
> Our first normalisation pass gave a −0.6 dBTP peak on the Russian version, which fails the −1 dBTP limit. Two-pass normalisation plus a limiter fixed it. One more lesson: AAC encoding for the video raises the peak by about half a decibel, so we set the limiter with headroom: at least −2 dBTP rather than −1 (AAC adds 0.5–0.8 dB). In our clip the limiter was at −3; the final MP4 is about −2 dBTP, which meets the −1 limit. No code: Audacity, steps on the right. Without Auto Duck, simply lower the background by 10–15 dB wherever the voice speaks. A music bed is quiet music under the voice. With code, ffmpeg does the same: the sidechaincompress filter (the voice controls how much the background drops) and loudnorm.
>
> Teams: this lesson needs sound. In Share, turn on “Include sound” (older versions: “Include computer sound”). Test the sound on one clip before you start.

---

### Slide 12 (44:00–50:00) • Speech-to-text found errors we missed by ear

**On screen:** The script and what Whisper heard, highlighted (red: error, green: correct critical term, amber: formatting only); the errors explained. Right: word error rate and the number of correct critical terms.

#### Speaker (6 min)
> How to check a voice-over without listening ten times: run the final audio through speech-to-text and compare with the script. We used the open Whisper small model on a laptop. Live demo (2 min): drop mix_en.mp3 into Google AI Studio with the prompt “Transcribe verbatim. Do not correct mistakes. Write numbers as you hear them.” Never paste your script into the transcription prompt: a language model will correct the transcript towards the script and hide the errors.
>
> Word error rate, WER: substitutions plus deletions plus insertions, divided by the number of words in the script. Lower is better. But one number hides the important part: an error in the order number matters more than ten errors in articles. So we check a separate list of critical terms: time, order number, minutes, name. Before counting, write numbers the same way in both texts, otherwise “6:42” and “six forty-two” count as an error.
>
> What we found in English: the transcript starts with “Here’s your order”, the line Veo made up (slide 6), leaking through the mix. So the shot 1 audio needs to be cut or muted at the start. “642” instead of “6:42”: we listened, and the voice said it correctly; this is the transcriber’s formatting. A checking artefact, not a voice error.
>
> In Russian: “Часть 42” (“part 42”) instead of “Шесть сорок две” (“six forty-two”) and “Оно” (“it”) instead of “Анна” (Anna). We listened: it is the voice; the open Russian Piper model reads these words badly. Fix: a different voice or a rewritten line. These are real results, nothing staged.

---

### Slide 13 (50:00–54:00) • Open-weight models: $0 per minute, paid for in hardware and time

**On screen:** Flow Hugging Face → disk → Python package → CPU or GPU → WAV; model table with file sizes and our CPU measurement; $0 per minute and what you pay instead.

#### Speaker (4 min)
> An open-weight model is a set of weight files anyone can download. Almost all of them live on Hugging Face: each model has a page (model card) with a description, licence and code example. A Python package downloads the files once into a cache folder on your disk; after that it works offline. The CPU or GPU does the computing; your voice recording and text go nowhere.
>
> How much hardware. Small models run on an ordinary laptop: Kokoro (0.36 GB) and Whisper small made our voice-over and check without a GPU. Qwen3-TTS 0.6B (2.5 GB of files) also runs on a CPU, but slowly: in our measurement about 8–9 times slower than real time, so one second of audio takes 8–9 seconds. Qwen3-TTS 1.7B (4.5 GB) needs a GPU; third-party measurements say 8 GB of video memory is comfortable. Plus disk space and Python 3.10 or newer.
>
> How this affects cost. There is no per-character bill, but an hour of speech on a CPU means many hours of computer time, and a GPU costs money to buy or rent. Local makes sense when data must not leave the company, when volume is large and steady, or for experiments. For a one-off voice-over, a service at $0.08 per minute costs less than your setup time.
>
> On speech system architectures (file, stream, voice agent), briefly: transcription is batch (whole file) or streaming (partial text at once, final text later); a voice agent is a chain speech-to-text → language model → text-to-speech, or one speech-to-speech model. We build agents in module 5 (L11–L13).

---

### Slide 14 (54:00–58:00) • Audio models by task: commercial and open-weight

**On screen:** Four task rows with models; open-weight models in a green border with the licence. Below: transcription accuracy and model lifetimes.

#### Speaker (4 min)
> A map by the four tasks, three commercial examples per row; the full list with prices is in L06_08. Commercial models on the left, open-weight ones in a green border with their licence. What changed in a year: OpenAI has a new generation of transcription (gpt-transcribe) and voice models (gpt-realtime-2.1, gpt-live-1), ElevenLabs has v4, Google has Gemini 3.8 TTS and Lyria 3.5 music, Suno has v6.
>
> Accuracy: on the Hugging Face Open ASR Leaderboard the best systems are around 4–5% English word error rate, Whisper large-v3 around 7–8%. Exact figures and leaders change every few weeks; open the leaderboard before class and name the current leader. Other languages and noisy recordings score worse; test on your own data.
>
> On lifetimes: OpenAI has announced that tts-1 and gpt-4o-mini-tts shut down on 6 January 2027 (replacement: gpt-realtime-2.1-mini), and whisper-1 and gpt-4o-transcribe on 26 February 2027. So keep the model name in configuration. Model names change every few months; recheck before class.

---

### Slide 15 (58:00–63:00) • 5 minutes for coffee and resting your ears

**On screen:** 5-minute timer, Start and Reset buttons.

#### Speaker (5 min)
> Press “Start”. Rest only, no chat tasks.

---

### Slide 16 (63:00–67:00) • A coding agent installs Qwen3-TTS locally and clones a voice

**On screen:** Coding-agent prompt (Claude Code, Antigravity, Codex) to install Qwen3-TTS and clone a voice; diagram sample + text → speech in that voice; two players: synthetic sample and clone; the own-voice-only rule.

#### Speaker (4 min)
> Do not run this live: the install takes 10–20 minutes. Show the prompt and play the two pre-recorded clips. On the left is a ready prompt for a coding agent: Codex, Antigravity or Claude Code in ChatGPT. The agent checks the hardware, creates a separate Python environment, downloads the model from Hugging Face, writes the script and runs it. You only record 10 seconds of your voice (on Windows, the Sound Recorder app saves m4a; the agent converts it to WAV) and write down exactly what you said. Give the folder as a full path and put the line text into the prompt, so the agent does not have to look for anything. What a coding agent is and how to choose one: L16.
>
> What the model does. The Base version of Qwen3-TTS takes a 3–10 second voice sample and its exact transcript; from them it captures the timbre and manner. Then it takes new text and a language and generates speech in that voice. In code this is one function, generate_voice_clone(text, language, ref_audio, ref_text). There is a mode without a transcript (x_vector_only), but quality is lower.
>
> Our real run: the sample was a synthetic Kokoro voice, not a living person, so there is no consent question. The 0.6B model on an ordinary CPU without a GPU took 10 s to load. The English line took 42 s; Whisper heard: “642. Order 417 is picked up, still hot.”. Russian line 1 took 38 s; Whisper heard: “Shaste Sort 2. Заказ 417 забран еще горячий.”. Line 3: “До дверей 12 минут. Анна уже в пути.”. Note that the voice was cloned from an English sample and speaks Russian; “Анна” is now pronounced correctly, unlike with Piper. But Whisper wrote the first Russian line as “Shaste Sort 2”: the clone carried over the sample’s English accent. Record the sample in the same language as the voice-over.
>
> The reference Gemini API synthesis code (previously on this slide) is in the lesson README. The homework needs no code; a local model is optional, with your own voice only.

---

### Slide 17 (67:00–71:00) • An hour of audio costs cents to dollars; an hour of video, over a thousand

**On screen:** Price table: second, minute, hour for synthesis, transcription, speech-to-speech, music. Right: the cost of voicing our video and a comparison with video.

#### Speaker (4 min)
> Units first. Speech synthesis is billed per character of text (Google Cloud, ElevenLabs) or per audio token (Gemini). Transcription, voice agents and ElevenLabs music are billed per minute. To compare, we convert everything to price per hour, using 1,000 characters per minute of speech, ElevenLabs’ own rule. The scale is logarithmic: each tick is ×10, so in reality the Veo bar is about 300 times longer than the ElevenLabs bar.
>
> Key point: audio is orders of magnitude cheaper than video. An hour of voice costs $4.80 on ElevenLabs and under a dollar on Gemini 3.8 Flash TTS. An hour of Veo 3.1 video in L05 cost $1,440. Transcribing an hour of recording costs 22 to 27 cents. Voicing our video: about 150 characters, roughly 1 cent on ElevenLabs.
>
> Subscriptions: ElevenLabs from $6 a month (30K credits ≈ 30 minutes), Suno Pro $8 a month billed yearly. The chart excludes retakes, mixing and people’s time. Homework example: 3 lines ≈ 150 characters × 2 services × 3 retakes ≈ 900 characters ≈ $0.07 at list price; $0 on a free tier. Where the money goes: voice agents (conversation minutes plus the language model behind them) and voice retakes. And web studio subscriptions: the ElevenLabs free allowance (10K credits ≈ 10 minutes) is enough for the homework, but the free plan has no commercial licence. Prices change: Gemini 3.8 TTS doubles on 1 January 2027.

---

### Slide 18 (71:00–76:00) • Both our versions failed acceptance: here is the checklist

**On screen:** 6-item checklist with the real result of our version (✓ / ✗ / !), loudness, the reason for rejection. This is the homework rubric.

#### Speaker (5 min)
> Six acceptance items. One: the words match the script, checked with speech-to-text and the critical terms list. Two: pronunciation of names, numbers and terms, by ear only. Three: timing, each line fits its shot. Four: mix, the voice is clear, the background is ducked, no stray speech. Five: loudness −14 LUFS plus or minus 1 and a peak no higher than −1 dBTP. Six: rights, meaning the voice and music licence, the voice owner’s consent and an “AI-generated” label.
>
> On the right is the measured result. Loudness and peak pass. The Russian version is rejected: the voice breaks “Анна” and “шесть сорок две”. The English version is rejected too: Veo’s invented line is audible at the start. Item 6 has an exclamation mark: MusicGen is non-commercial; fine for a lesson, not for a client.
>
> The same checklist is the homework rubric; the line at the bottom says what evidence each item needs. Grading is based on the error analysis, not on perfect sound.

---

### Slide 19 (76:00–80:00) • Risks and voice consent: cloning, labelling, law

**On screen:** Voice traffic light; how services check consent for a clone; EU AI Act Art. 50, OpenAI, SynthID plaque.

#### Speaker (4 min)
> For the homework: an end caption “Voice and music: AI-generated (services)”. On the left is a traffic light for voices. Green: a library voice or one designed from a description, under the service licence and with an “AI-generated” label. Amber: your own voice or a colleague’s clone, only with written consent that says the purpose, where, how long and how to withdraw. Red: a client’s, a manager’s or a public figure’s voice; not without written consent and legal review. Voice clones are used for fraud: a call “from the CEO” asking for an urgent transfer.
>
> On the right: how services check consent. OpenAI limits custom voices to eligible customers and Google Cloud to allow-listed ones; in the Gemini API any developer can replicate a voice, but only with the owner’s recorded consent phrase. ElevenLabs asks the owner to read a verification text for a professional clone, and only a checkbox for an instant clone. Azure grants clones on application and may match the consent recording to the voice. Open models clone from a few seconds and check nothing. So checking consent is your responsibility, not the service’s.
>
> Law: Article 50 of the EU AI Act applies from 2 August 2026: synthetic audio and deepfakes must be labelled, with fines up to €15M or 3% of turnover. OpenAI’s usage policies require a clear disclosure to listeners that the voice is AI-generated. Google embeds SynthID in all audio from its models (Lyria, Gemini speech); the Gemini app can check it, but only for Google content. For systems already on the market, the Art. 50(2) machine-readable marking obligation has a grace period to 2 December 2026. The fraud risk is real: according to press reports, in February 2026 the Italian bank Fideuram wired about €95M after a call in which a real lawyer’s voice was cloned.

---

### Slide 20 (80:00–87:00) • Homework 6: voice your L05 video

**On screen:** “Your L05 video” card, the genai-homeworks/L06 folder tree, five homework steps, reviewer and the consent rule.

#### Speaker (7 min)
> The homework repeats the lesson pipeline on your L05 video. Track A: product, track B: courier. If you have no video, use the lesson’s courier video from the L05 folder.
>
> Six items = the six lesson steps. Order: a 3-line script with a word budget and a spoken-text column; the voice in two no-code services, for example ElevenLabs and Google AI Studio (an API or open model is optional), keep the better one by checklist items 1–2; a background: the video model’s audio, effects or music, with its licence; a mix into final_voiced.mp4 at −14 LUFS plus or minus 1; run the result through speech-to-text and save transcript.txt; the slide 18 checklist in audio_qa.md; services, settings and cost in audio_spec.md.
>
> Label: an end caption “Voice and music: AI-generated (service names)” and the same line in audio_spec.md. Consent rule: your own voice or library voices only. Do not clone colleagues, relatives or celebrities, not even “for a test”. Grading is based on the error analysis, not on perfect sound. Details and templates are in the L06 homework file.

---

### Slide 21 (87:00–90:00) • Lesson summary

**On screen:** Six lesson rules and a frame from the video; Capstone 1 (30 of 100 points) and the L07 preview.

#### Speaker (3 min)
> Six rules, one per step: a script with a word budget; spoken text kept separate, numbers and names as words; a voice with a licence and consent; a background with a known licence; mix to −14 LUFS; check with speech-to-text and by ear.
>
> This closes the multimodality module: image, video, sound. Next lesson, L07: the Microsoft Copilot ecosystem — for you, for work, for code, for your company. Capstone 1 (voice → image) starts after this lesson: a no-code Colab, 30 of the 100 course points; 60 are needed to pass the course. Questions.

---
