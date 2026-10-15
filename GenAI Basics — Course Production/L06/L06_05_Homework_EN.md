# Lesson 06 • Homework Assignment: Sound Design & Scoring Your L05 Video

**Course:** GenAI Basics • Module 2 (Multimodality)  
**Submission:** Folder `genai-homeworks/L06/` in your private course GitHub repository  
**Inspector / Reviewer:** Igor Rubanovich (`ihar_rubanovich@epam.com`)  
**Estimated Time:** 1.5–2 hours  
**Tools:**
- **TTS (Voiceover):** ElevenLabs (free tier), Cartesia Sonic, or local Kokoro-82M.
- **SFX (Foley):** ElevenLabs SFX or Stable Audio.
- **Music:** Suno v4 or Udio 1.5 (Instrumental mode).
- **Audio Mixing:** Any video editor (CapCut, DaVinci Resolve, Premiere) or course Colab (`notebooks/L06_Speech_and_Audio_AI_Pipeline.ipynb`).

---

## Objective

Master the industrial fundamentals of generative audio engineering:
1. Synthesize a cinematic voiceover line with realistic vocal pacing, micro-breaths, and zero robotic comb-filtering.
2. Generate Foley sound effects matching physical kinematics and impact moments in your video.
3. Generate a background instrumental score with zero vocal bleed.
4. Assemble a balanced 3-stem audio mix applying Sidechain Ducking.
5. Complete an engineering QA audit verifying loudness, peak headroom, and lip-sync tolerance.

---

## Select Your Base Video from Lesson 05

Work with the video clip rendered in Homework #5:
* **Option 1 (Glovo Courier):** Your `02_i2v_serviceA.mp4` clip (bicycle ride in the rain).
* **Option 2 (Product Packshot):** Your 360-degree coffee mug commercial clip.
* **Option 3 (Storyboard Cut):** Any 5-second take from your Storyboard Matrix.

---

## Mandatory 3-Stem Engineering Requirements

| Audio Stem | Action | Quality Criteria |
| :--- | :--- | :--- |
| **1. Voiceover (TTS)** | Synthesize 1 tight narrative sentence (10–15 words). | Zero metallic phase distortion; natural breath pauses (`...`); target loudness -14 LUFS. |
| **2. Foley SFX** | Generate physical Foley using the 3-slot formula. | Millisecond frame alignment with visual triggers (puddle splash, steam hiss, bag rustle); target -18 LUFS. |
| **3. Music (Suno/Udio)** | Generate an instrumental background score. | Strictly **Instrumental**; automated Sidechain Ducking (-4dB to -6dB during voiceover); target -22 LUFS. |

---

## GitHub Repository Folder Structure

Submit strictly according to this directory tree:

```
genai-homeworks/
└── L06/
    ├── audio/
    │   ├── 01_voiceover.mp3          # Clean isolated narration track
    │   ├── 02_foley_sfx.mp3          # Clean isolated Foley SFX track
    │   └── 03_music_bg.mp3           # Clean isolated instrumental music track
    ├── final_video_with_audio.mp4    # Final video container with synchronized audio
    ├── audio_spec.md                 # Prompts, models, and mixing parameters
    └── audio_qa.md                   # Engineering quality audit checklist
```

---

## Template `audio_spec.md`

```markdown
# Audio Design Specification • Homework L06

**Student:** [Your Name / EPAM Login]  
**Base Video Asset:** `genai-homeworks/L05/videos/02_i2v_serviceA.mp4`  

---

## 1. Voiceover Stem
- **Service / Model:** ElevenLabs (Multilingual v2) / Cartesia / Kokoro
- **Selected Voice:** [Voice name]
- **Narration Text:** "The evening rain cuts across the asphalt... but order number 42 is already en route."
- **Settings:** Stability: 0.40, Similarity: 0.80, Style: 0.15

---

## 2. Foley SFX Stem
- **Service:** ElevenLabs SFX / Stable Audio
- **Prompt:** "Bicycle tires splashing rapidly through a deep rainwater puddle, fine water spray, quiet city background hum, 24fps cinema sync"
- **Duration:** 5.0s

---

## 3. Music Underscore Stem
- **Service / Model:** Suno v4 / Udio 1.5
- **Style Prompt:** "Lo-fi acoustic guitar chillhop, slow 74 BPM, upright bass, rain texture, instrumental"
- **Structure Tags:** `[Intro] Fingerpicked guitar, rain ambience [Outro] Fade out`

---

## 4. Multi-Stem Mixing Parameters
- **Assembly Tool:** [CapCut / DaVinci Resolve / Python pydub]
- **Loudness Balance:** Voice: 0 dB, SFX: -4 dB, Music: -10 dB (-15 dB ducked)
```

---

## Template `audio_qa.md`

```markdown
# Audio Quality Engineering Audit (Audio QA)

| Audit Criterion | Quantitative Tolerance | Project Measurement | Verdict (PASS / FAIL) |
| :--- | :--- | :--- | :---: |
| **1. Digital Clipping** | 0 peaks exceeding -1.0 dBFS | Peak level: -1.2 dBFS | PASS |
| **2. Metallic Comb-Filtering** | No hollow resonance around 3kHz | Clean organic timbre | PASS |
| **3. Speech Intelligibility** | 100% dialogue clarity over music | Music ducked -5dB beneath voice | PASS |
| **4. Foley Synchronization** | Video offset < 40ms | Puddle splash aligns with wheel impact | PASS |
| **5. Container Integrity** | Video and audio streams match length | Video: 5.0s, Audio: 5.0s | PASS |

**Engineer Remarks:** [Brief notes on mixing challenges encountered and how you solved them].
```
