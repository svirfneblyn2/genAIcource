# Lesson 06: Speech and Audio AI. Voice-over, sound and music for a video

## Status: deck v2 (21 slides, 90 min), facts rechecked and audit fixes applied 2026-10-16

2026-10-16 revision (day of class): volatile facts rechecked (only the Open ASR Leaderboard changed); student-mode and visual audits applied. Slides 3, 8 and 9 now use real Google AI Studio screenshots with numbered callouts instead of text cards; slide 17 is a log-scale bar chart of the price of one hour instead of a price table; jargon cut on slides 2, 5, 11; the word-budget rule on slide 7 and the 6:42 example on slide 8 fixed; slide 12 says what Whisper did not hear.

Deck structure: the L05 courier video with a voice-over, where to generate (chat, web studio, API, open weights), four audio tasks, how a speech model works, audio inside video models (Veo invents lines), then a 6-step pipeline (1 script, 2 text for the voice, 3 voice, 4 sound effects and music, 5 mix, 6 check with speech-to-text), local open-weight models, market, break, a coding agent cloning a voice with Qwen3-TTS, cost per second / minute / hour, acceptance checklist, risks and voice consent, homework (voice your L05 video), summary. Lesson graph: `L06_10_Lesson_Graph.md`. PDFs built with headless Edge on 2026-10-12 (21 pages each); rebuild after any deck change with `python deck_v2/build.py` on a machine with Edge.

The old Drive package (`06 — Speech and Audio AI — DONE`, Sep 2026: docx/pptx, speech-to-text only, mock demo repo) is replaced by this folder. Its useful parts (batch / streaming / realtime, word error rate plus critical terms, synthetic audio only) live on slides 12–13.

## Source of truth
- **Generator:** `deck_v2/build.py` (RU/EN strings side by side, `t("ru", "en")`; slide order in `SLIDES`; minutes per slide in `min=`) + `deck_v2/style.css` + `deck_v2/deck.js`. Run `python deck_v2/build.py` (HTML + PDF via headless Edge) or `--no-pdf`. Edit the generator, not the HTML.
- **Instructor scripts** `L06_02_*` are generated from the deck: `python deck_v2/make_docs.py` (timing table and speaker text come from `build.py`).
- **Audio assets:** `python deck_v2/make_audio.py` (add `--music` to regenerate the music bed). It voices the L05 courier video with open-weight models on CPU, mixes it to −14 LUFS and checks it with Whisper. Outputs: `assets/v2/audio/*.mp3`, `assets/v2/video/courier_voiced_{en,ru}.mp4`, `deck_v2/envelopes.json` (waveforms for the slides) and `demo_courier_audio/report.json` (loudness, transcripts, word error rate, critical terms). The deck reads its numbers from `report.json`.
  - Models (downloaded once to `$L06_MODELS`, default `~/.cache/l06_models`): Kokoro-82M (Apache-2.0) `kokoro-v1.0.onnx` + `voices-v1.0.bin`; Piper `ru_RU-dmitri-medium` (voice data CC0, `piper-tts` GPL-3.0); MusicGen-small (CC-BY-NC-4.0, lesson use only); Whisper small via `faster-whisper` (MIT).
  - Python packages: `kokoro-onnx soundfile piper-tts faster-whisper` (+ `torch transformers` for `--music`), plus `ffmpeg` on PATH.
- **Slide decks (RU/EN):** `presentation_L06_Speech_and_Audio_v2.html` / `presentation_L06_Speech_and_Audio_EN_v2.html` + PDFs with the same basenames. Self-contained HTML (inline CSS/JS, media by relative path): `←/→` navigate, `N` speaker notes, `G` slide grid, `F` fullscreen, break timer on slide 15. Audio and video play on click **with sound**; in the PDF each player shows a label “▶ audio / video in the HTML version”.
- **Facts:** `L06_08_Source_Notes_Research_2026-10.md` (primary sources, checked 2026-10-12; volatile list at the end).
- **Companion documents:** instructor scripts (`L06_02_*`), cheatsheets (`L06_00_*`), homework (`L06_05_*`), lesson graph (`L06_10_*`).

## Slide map (21 slides, 90 minutes incl. 5-minute break)
| # | Min | Time | Slide | Main visual |
|---|---|---|---|---|
| 01 | 2 | 00:00–02:00 | Cover | Frame of L05 shot 2 |
| 02 | 3 | 02:00–05:00 | The L05 courier video with voice-over, sound and music | Voiced video + 3 numbers (3 lines, 3 tracks, −14 LUFS) |
| 03 | 4 | 05:00–09:00 | Start in a web studio, automate with the API | Google AI Studio Generate speech screenshot with 4 callouts + Get code screenshot; chat and open-weight paths in one line |
| 04 | 4 | 09:00–13:00 | Four audio AI tasks | Four input → output cards |
| 05 | 4 | 13:00–17:00 | The model guesses how text sounds, so it trips on numbers and names | Plain-language chain + real waveform of line 1 |
| 06 | 4 | 17:00–21:00 | Audio inside a video model | Two Veo audio players + the lines Veo invented |
| 07 | 5 | 21:00–26:00 | Step 1: script and word budget | Script table with frames, words, length |
| 08 | 5 | 26:00–31:00 | Step 2: text for the voice | Script → spoken text table + AI Studio Style field screenshot |
| 09 | 4 | 31:00–35:00 | Step 3: three sources of a voice | AI Studio voice library + Create voice (Voice Design / Voice Replication) screenshots, 3-colour legend |
| 10 | 4 | 35:00–39:00 | Step 4: sound effects and music | MusicGen bed player + licence table |
| 11 | 5 | 39:00–44:00 | Step 5: mix | Four real waveforms, loudness, ffmpeg command |
| 12 | 6 | 44:00–50:00 | Step 6: check with speech-to-text | Script vs Whisper transcript, word error rate, critical terms |
| 13 | 4 | 50:00–54:00 | Local open-weight audio models: where they live, hardware, cost | Hugging Face → disk → package → CPU/GPU flow; model table with file sizes and measured CPU speed |
| 14 | 4 | 54:00–58:00 | Market, October 2026 | Models by task, open weights with licences |
| 15 | 5 | 58:00–63:00 | Break | Timer |
| 16 | 4 | 63:00–67:00 | A coding agent installs Qwen3-TTS locally and clones a voice | Agent prompt (Claude Code / Antigravity / Codex) + real clone demo (synthetic reference, CPU) |
| 17 | 4 | 67:00–71:00 | An hour of audio costs cents to dollars; an hour of video, hundreds | Log-scale bars, $ per hour (6 audio models + Veo 3.1) + cost of our video |
| 18 | 5 | 71:00–76:00 | Acceptance checklist | 6 items with our real result (= homework rubric) |
| 19 | 4 | 76:00–80:00 | Risks and voice consent | Traffic light, vendor consent checks, EU AI Act Art. 50 |
| 20 | 7 | 80:00–87:00 | Homework: voice your L05 video | Deliverables, repo tree |
| 21 | 3 | 87:00–90:00 | Summary | 6 rules + L07 preview |

## Local voice cloning demo (slide 16)
`python deck_v2/make_clone.py` loads `Qwen/Qwen3-TTS-12Hz-0.6B-Base` (Apache-2.0, ~2.5 GB) on a CPU, clones a **synthetic** reference voice (Kokoro `af_heart`, no real person), generates one English and two Russian lines and writes `assets/v2/audio/clone_*.mp3` and `demo_courier_audio/clone_report.json` (load time, generation time, real-time factor, Whisper transcript). Requires `pip install qwen-tts soundfile` and CPU builds of `torch` and `torchaudio` from the same release. Clone only your own voice.

## Reference code: Gemini API text-to-speech (moved from the old slide 16)
```python
from google import genai
from google.genai import types

client = genai.Client()  # key from GEMINI_API_KEY
r = client.models.generate_content(
    model="gemini-3.8-flash-tts",
    contents=types.Content(role="user", parts=[types.Part(
        text="Six forty-two. Order four one seven.",
        speech_metadata=types.SpeechMetadata(style="calm, friendly dispatcher"))]),
    config=types.GenerateContentConfig(
        response_modalities=["AUDIO"],
        speech_config=types.SpeechConfig(voice_config=types.VoiceConfig(
            prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Kore")))))
open("line1.wav", "wb").write(r.candidates[0].content.parts[0].inline_data.data)  # already WAV, 24 kHz mono
```
Gemini 3.8 TTS reads the text verbatim, so the style goes in `speech_metadata.style`, not in the text. Check the model ID before class.
