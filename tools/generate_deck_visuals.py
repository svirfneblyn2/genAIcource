import sys
import os
from pathlib import Path

# Add tools to sys.path
sys.path.append(r"d:\Repos\genAIcource\tools")
from image_generator import generate_vertex_image

TASKS = [
    {
        "output": r"d:\Repos\genAIcource\GenAI Basics — Course Production\L05\assets\l05_cover_hero.png",
        "prompt": "Cinematic dark engineering film production monitor, generative AI video timelines, 3D spacetime latents, futuristic director console with video render nodes, dark C4 theme #0b0f17, neon cyan and amber accents, clean and crisp, 16:9",
    },
    {
        "output": r"d:\Repos\genAIcource\GenAI Basics — Course Production\L06\assets\l06_cover_hero.png",
        "prompt": "Cinematic dark engineering audio studio hero visual, digital sound wave visualizer, mel-spectrogram glow, studio microphone, neural audio codec nodes, dark C4 theme #0b0f17, neon cyan and emerald lighting, professional and sharp, 16:9",
    },
    {
        "output": r"d:\Repos\genAIcource\GenAI Basics — Course Production\L06\assets\elevenlabs_studio_ui.png",
        "prompt": "High-fidelity modern UI dashboard mockup of ElevenLabs Speech Synthesis Studio, dark theme #0b0f17, Voice Selection panel showing Adam and Custom PVC Clone, sliders for Stability (0.35) and Similarity (0.75), text script editor with pauses and phonetic markup, audio waveform player at bottom, clean software interface, crisp typography, 16:9",
    },
    {
        "output": r"d:\Repos\genAIcource\GenAI Basics — Course Production\L06\assets\elevenlabs_sfx_ui.png",
        "prompt": "Modern software UI interface mockup of ElevenLabs Sound Effects Studio, dark engineering theme #0b0f17, text prompt box with 'Bicycle tires splashing violently through rain puddle, cinema foley', duration slider set to 5.0s, prompt influence slider, audio wave player with 48kHz stereo indicator, download button, crisp English UI, 16:9",
    },
    {
        "output": r"d:\Repos\genAIcource\GenAI Basics — Course Production\L06\assets\whisper_playground_ui.png",
        "prompt": "Clean modern Web UI interface mockup of OpenAI Whisper speech recognition playground, dark theme #0b0f17, top mel-spectrogram audio wave visualizer, language dropdown 'ru/en', model selector 'large-v3-turbo', live transcription window with word-level timestamps [00:01.20 --> 00:01.48], crisp technical typography, 16:9",
    },
    {
        "output": r"d:\Repos\genAIcource\GenAI Basics — Course Production\L06\assets\google_audio_ecosystem.png",
        "prompt": "C4 architecture infographic of Google Audio & Speech Ecosystem, dark theme #0b0f17: Google Cloud Speech-to-Text v2 Chirp, Text-to-Speech Studio Journey voices, Google DeepMind AudioLM and Lyria music engine, Google Gemini native multimodal audio-in audio-out, Google SynthID audio watermarking badge, cyan and emerald accents, 16:9",
    },
    {
        "output": r"d:\Repos\genAIcource\GenAI Basics — Course Production\L06\assets\suno_v4_studio_ui.png",
        "prompt": "Modern UI dashboard mockup of Suno v4 Music Creation Studio, dark theme #0b0f17, Instrumental toggle enabled, lyrics editor with prompt tags [Intro: Chillhop acoustic], [Verse: 74 BPM], [Build-up: Cello], Style of Music prompt field, multi-track waveform player, stem separation Demucs controls, crisp English typography, 16:9",
    },
    {
        "output": r"d:\Repos\genAIcource\GenAI Basics — Course Production\L06\assets\sidechain_ducking_diagram.png",
        "prompt": "Technical audio engineering diagram of Sidechain Ducking and Multi-Stem Mixing, dark theme #0b0f17: Track 1 Voiceover at -14 LUFS, Track 2 Foley SFX at -18 LUFS, Track 3 Music Underscore dynamically ducked by -5 dB during voiceover speech, visual envelope curves, decibel meters, clean engineering aesthetic, 16:9",
    },
    {
        "output": r"d:\Repos\genAIcource\GenAI Basics — Course Production\L06\assets\voice_agent_latency_arch.png",
        "prompt": "C4 latency waterfall architectural diagram for Real-Time Voice Agents (<300ms budget), dark theme #0b0f17: WebRTC In (20ms), Silero VAD (15ms), Streaming Whisper Turbo (80ms), Groq LLaMA 3.3 (50ms), Cartesia Sonic TTS (90ms), Speaker Out (30ms), total 285ms, with Barge-In WebSocket interrupt loop, cyan and amber nodes, 16:9",
    },
]

for idx, task in enumerate(TASKS, 1):
    out_path = Path(task["output"])
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists():
        print(f"[{idx}/{len(TASKS)}] Skipping {out_path.name} (already exists)")
        continue
    print(f"[{idx}/{len(TASKS)}] Generating {out_path.name}...")
    try:
        generate_vertex_image(prompt=task["prompt"], output_path=str(out_path), aspect_ratio="16:9")
        print(f" -> OK: {out_path} ({out_path.stat().st_size} bytes)")
    except Exception as e:
        print(f" -> ERROR: {e}")
