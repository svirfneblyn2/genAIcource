# Lesson 06 • Live Demo Runbook & Prompt Copybook
## Verified Prompts, Pipelines, and Live Scenarios for Audio & Speech AI

**Course:** GenAI Basics • Module 2 (Multimodality)  
**Instructor:** Igor Rubanovich (EPAM Systems • `ihar_rubanovich@epam.com`)  
**Services:** OpenAI Whisper (API & faster-whisper), ElevenLabs (Multilingual v2 & SFX), Cartesia Sonic, Suno v4, Udio 1.5, Silero VAD  
**Code:** Colab `notebooks/L06_Speech_and_Audio_AI_Pipeline.ipynb`

This copybook provides battle-tested prompts, parameter configurations, and Python scripts to score and dub the generative video clips synthesized in Lesson 05.

---

## Table of Contents

1. [Block 1: Hook Quiz (4 Audio Clips A–D)](#block-1-hook-quiz-4-audio-clips-ad)
2. [Block 2: Whisper STT & Word-Level Timestamp Extraction](#block-2-whisper-stt--word-level-timestamp-extraction)
3. [Block 3: Silence Pre-filtering with Silero VAD](#block-3-silence-pre-filtering-with-silero-vad)
4. [Block 4: Voiceover Synthesis (ElevenLabs TTS & Cartesia Sonic)](#block-4-voiceover-synthesis-elevenlabs-tts--cartesia-sonic)
5. [Block 5: Foley Sound Effects Generation (SFX AI)](#block-5-foley-sound-effects-generation-sfx-ai)
6. [Block 6: Studio Sound Design Matrix (Creator Tools Giant Stories Case)](#block-6-studio-sound-design-matrix-creator-tools-giant-stories-case)
7. [Block 7: Instrumental Soundtrack Synthesis in Suno v4](#block-7-instrumental-soundtrack-synthesis-in-suno-v4)
8. [Block 8: Multi-Stem Assembly & Sidechain Ducking in Python](#block-8-multi-stem-assembly--sidechain-ducking-in-python)
9. [Block 9: Sub-300ms Real-Time Voice Agent Architecture](#block-9-sub-300ms-real-time-voice-agent-architecture)

---

## Block 1: Hook Quiz (4 Audio Clips A–D)

> **Objective:** Acoustic calibration of the audience to detect neural generative artifacts.  
> **Format:** 44.1 / 48 kHz, duration 5–8s.

### Clip [A] • Studio Voiceover Narration (ElevenLabs Multilingual v2)
* **Prompt/Text:**
```text
In 1911, deep within the Nevada desert... two miners entered a sealed limestone cavern, completely unprepared for the fossilized silhouette waiting in the dark.
```
* **Parameters:** Voice: `George (Warm Narration)`, Stability: `0.38`, Similarity: `0.80`, Style Exaggeration: `0.10`.

### Clip [B] • Courier Bicycle Foley SFX (ElevenLabs SFX)
* **Prompt:**
```text
Bicycle rubber tires splashing violently through a deep rainwater puddle on wet cobblestone, fine water spray, quiet evening city background hum, cinema foley, 24fps sync
```
* **Parameters:** Duration: `5.0s`, Prompt Influence: `0.85`.

### Clip [C] • Acoustic Jazz Trio (Suno v4)
* **Style of Music:**
```text
Acoustic jazz trio, slow 72 BPM swing, upright piano chords, brushed snare drum, acoustic upright bass walking line, warm vintage tape saturation, instrumental
```
* **Parameters:** `Instrumental: ON`, Model: `v4`.

### Clip [D] • Live Support Conversation (Cartesia Sonic Voice Agent)
* **Text:**
```text
"Hello! Yes, I can certainly see your order from the Scandinavian bakery. The courier is just two blocks away on Elm Street — should be at your lobby in three minutes."
```
* **Parameters:** Model: `sonic-english`, Latency mode: `ultra-low`, Chunk size: `128 tokens`.

---

## Block 2: Whisper STT & Word-Level Timestamp Extraction

> **Objective:** Extract millisecond-accurate subtitle timestamps for automated video editing.

```python
import whisper

# Load fast turbo model
model = whisper.load_model("turbo")

# Transcribe with word-level alignment
result = model.transcribe(
    "narration.mp3",
    language="en",
    word_timestamps=True,
    temperature=0.0
)

print(f"Detected language: {result['language']}")
for segment in result["segments"]:
    print(f"\n--- Segment [{segment['start']:.2f}s -> {segment['end']:.2f}s] ---")
    for word_info in segment["words"]:
        print(f"  [{word_info['start']:6.2f}s - {word_info['end']:6.2f}s]: {word_info['word']}")
```

---

## Block 3: Silence Pre-filtering with Silero VAD

> **Objective:** Eliminate autoregressive hallucination loops in silent audio windows.

```python
import torch

# Load ultra-lightweight Silero VAD model (1MB)
model, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-vad',
    model='silero_vad',
    force_reload=False
)
(get_speech_timestamps, save_audio, read_audio, VADIterator, collect_chunks) = utils

# Load waveform
wav = read_audio('raw_recording.wav', sampling_rate=16000)

# Extract speech intervals with strict thresholds
speech_timestamps = get_speech_timestamps(
    wav,
    model,
    sampling_rate=16000,
    threshold=0.5,
    min_speech_duration_ms=250,
    min_silence_duration_ms=300
)

print(f"Speech segments detected: {len(speech_timestamps)}")
for ts in speech_timestamps:
    print(f"Speech from {ts['start']/16000:.2f}s to {ts['end']/16000:.2f}s")
```

---

## Block 4: Voiceover Synthesis (ElevenLabs TTS & Cartesia Sonic)

### 4.1. Delivery Courier Line (L05 Glovo Case)
```text
The evening rain cuts across the asphalt, but order number 42 is already en route... twelve minutes to doorstep.
```

### 4.2. Commercial Packshot Line (L05 Coffee Mug)
```text
Single-origin Ethiopian roast... freshly pulled at ninety-three degrees. Morning clarity, distilled.
```

### 4.3. Python API Integration for ElevenLabs
```python
import requests

ELEVENLABS_API_KEY = "YOUR_API_KEY"
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel / Cinematic Narration

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}
payload = {
    "text": "The evening rain cuts across the asphalt... but order number 42 is already en route.",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.40,
        "similarity_boost": 0.80,
        "style": 0.15,
        "use_speaker_boost": True
    }
}

response = requests.post(url, json=payload, headers=headers)
with open("voiceover.mp3", "wb") as f:
    f.write(response.content)
print("Voiceover synthesized successfully.")
```

---

## Block 5: Foley Sound Effects Generation (SFX AI)

### 5.1. Glovo Courier in Rain (Shot 2 from L05)
```text
Gravel bicycle tires cutting through shallow street rain puddle with realistic water spray, quiet evening city breeze, wet asphalt tire hiss, 24fps cinematic sync
```

### 5.2. Ceramic Packshot (Coffee Mug on Oak Counter)
```text
Ceramic coffee mug gently placed onto solid oak wooden counter, light ceramic thud, thin steam wisp hiss, quiet cafe background ambience
```

### 5.3. Handover Moment (Shot 3 from L05)
```text
Brown kraft paper food bag rustling gently as hands pass it forward, quiet domestic doorway acoustics, soft indoor floor step
```

---

## Block 6: Studio Sound Design Matrix (Creator Tools Giant Stories Case)

Battle-tested Foley and music prompts from the 10-episode pseudo-documentary series:

| Scene | Key Visual | ElevenLabs SFX Prompt | Suno v4 Music Prompt |
| :--- | :--- | :--- | :--- |
| **01. Sealed Crate** | Sealed 1929 Customs vault crate | `Distant stone vault hum, slow water dripping on concrete, subtle rat scuttle, hollow reverberation` | `Bowed acoustic double bass drone, dark mysterious cello swell, 65 BPM, instrumental, atmospheric noir` |
| **02. Drill Strike** | Oil drillers strike fossil bone | `Cicadas buzz in hot desert wind, heavy shovel violently scraping dense fossilized stone, sudden gasping breath` | `Ominous sub-bass pulse every 2 seconds, distant muted brass stab, desert tension, instrumental` |
| **03. Rotary Press** | Historic press churning headlines | `Historic industrial rotary printing press mechanical clatter, fresh wet ink roller hiss, paper sheet flutter` | `Fast driving string quartet tremolo, mechanical clockwork rhythm, 120 BPM, investigative thriller, instrumental` |
| **04. Denial Letter** | Clerk typing official rejection | `Vintage mechanical typewriter key clacking, carriage return bell ding, banker lamp 60Hz hum, paper rustle` | `Melancholic solo cello phrase decaying into analog tape hiss, sparse minimal piano notes, 70 BPM, instrumental` |

---

## Block 7: Instrumental Soundtrack Synthesis in Suno v4

### 7.1. Glovo Courier Soundtrack (Rain, Dusk, City)
* **Prompt (Style of Music):**
```text
Lo-fi acoustic guitar chillhop, slow 74 BPM unhurried groove, gentle vinyl crackle, warm upright bass, rain ambiance texture, twilight mood, instrumental
```
* **Lyrics Box (Arrangement Tags):**
```text
[Intro]
Gentle fingerpicked acoustic guitar, rain texture, soft Rhodes chord

[Main Groove]
Muted bass enters, smooth brushed drums, melodic guitar refrain

[Outro]
Guitar notes fade out into soft rain hiss
```

### 7.2. Product Commercial Soundtrack (Coffee Mug Packshot)
* **Prompt (Style of Music):**
```text
Minimalist Scandinavian acoustic piano, warm 80 BPM, clean contemporary jazz feel, upright bass, soft mallet marimba accents, morning coffee commercial, instrumental
```

---

## Block 8: Multi-Stem Assembly & Sidechain Ducking in Python

```python
from pydub import AudioSegment

# Load the 3 generated audio stems
voice = AudioSegment.from_file("voiceover.mp3")      # Narrator
foley = AudioSegment.from_file("foley_splash.mp3")   # Bicycle splash
music = AudioSegment.from_file("music_lofi.mp3")     # Background score

# Normalize target loudness levels
voice = voice.apply_gain(+1.0)   # Target -14 LUFS
foley = foley.apply_gain(-4.0)   # Target -18 LUFS

# Implement Sidechain Ducking: attenuate music by -5dB during voiceover
music_intro = music[:500] - 8.0
music_during_speech = music[500:len(voice)+500] - 13.0  # Ducked -5dB deeper
music_tail = music[len(voice)+500:] - 8.0

ducked_music = music_intro + music_during_speech + music_tail

# Overlay stems with frame-accurate offsets
final_mix = ducked_music.overlay(voice, position=500).overlay(foley, position=1200)

# Export mastered soundtrack
final_mix.export("final_commercial_soundtrack.mp3", format="mp3", bitrate="320k")
print("Master soundtrack exported successfully.")
```

---

## Block 9: Sub-300ms Real-Time Voice Agent Architecture

```python
# Asynchronous pipeline loop for real-time speech agents
import asyncio

async def voice_agent_loop(audio_stream_in, audio_stream_out):
    vad = SileroVAD()
    stt_client = DeepgramLiveClient()
    llm_client = GroqStreamingClient(model="llama-3.3-70b-versatile")
    tts_client = CartesiaSonicStreamingClient()
    
    async for pcm_chunk in audio_stream_in:
        # 1. Voice Activity Detection (15ms)
        if vad.is_speech(pcm_chunk):
            user_text_token = await stt_client.push(pcm_chunk)
            
            # 2. LLM response streaming (50ms TTFT)
            async for llm_token in llm_client.stream_response(user_text_token):
                
                # 3. Streaming neural TTS synthesis (90ms TTFT)
                async for audio_chunk in tts_client.stream_speech(llm_token):
                    await audio_stream_out.play(audio_chunk)
                    
        # 4. Immediate barge-in cancellation
        elif vad.is_interruption():
            await tts_client.cancel_active_stream()
            await audio_stream_out.clear_buffer()
```
