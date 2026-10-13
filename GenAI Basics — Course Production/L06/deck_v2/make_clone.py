# -*- coding: utf-8 -*-
"""Local voice cloning demo for slide 16: Qwen3-TTS 0.6B Base on a CPU, no GPU, no API.

    python make_clone.py

Consent: the reference voice is SYNTHETIC (Kokoro-82M voice af_heart, generated below), so no
real person's voice is cloned. In class and in the homework: clone only your own voice.

Steps (the same ones the coding-agent prompt on slide 16 asks for):
  1 reference: ~6 s of the voice + its exact transcript
  2 load Qwen/Qwen3-TTS-12Hz-0.6B-Base (Apache-2.0) from Hugging Face (~2.5 GB, cached in ~/.cache/huggingface)
  3 generate_voice_clone(text, language, ref_audio, ref_text) for an English and two Russian lines
  4 measure load time, generation time and the real-time factor; check the result with Whisper

Requires: pip install qwen-tts soundfile kokoro-onnx faster-whisper (CPU torch is enough).
Outputs: ../assets/v2/audio/clone_*.mp3 and ../demo_courier_audio/clone_report.json
"""
import json
import os
import platform
import subprocess
import time
from pathlib import Path

import numpy as np
import soundfile as sf

HERE = Path(__file__).resolve().parent
L06 = HERE.parent
AUD = L06 / "assets" / "v2" / "audio"
MODELS = Path(os.environ.get("L06_MODELS", Path.home() / ".cache" / "l06_models"))
MODEL_ID = "Qwen/Qwen3-TTS-12Hz-0.6B-Base"
REF_TEXT = ("Good evening. This is the dispatch desk. Your courier has picked up the order "
            "and is riding through the rain.")
JOBS = [("en_1", "English", "Six forty-two. Order four one seven is picked up, still hot."),
        ("ru_1", "Russian", "Шесть сорок две. Заказ четыреста семнадцать забран, ещё горячий."),
        ("ru_3", "Russian", "До двери двенадцать минут. Анна уже в пути.")]


def mp3(wav, name):
    subprocess.run(["ffmpeg", "-y", "-i", str(wav), "-b:a", "128k", str(AUD / f"{name}.mp3")],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def main():
    import torch
    from faster_whisper import WhisperModel
    from kokoro_onnx import Kokoro
    from qwen_tts import Qwen3TTSModel

    tmp = L06 / "demo_courier_audio" / "_clone_tmp"
    tmp.mkdir(parents=True, exist_ok=True)
    k = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
    s, sr = k.create(REF_TEXT, voice="af_heart", speed=1.0, lang="en-us")
    ref = tmp / "ref.wav"
    sf.write(str(ref), s, sr)
    mp3(ref, "clone_reference")

    t0 = time.time()
    model = Qwen3TTSModel.from_pretrained(MODEL_ID, device_map="cpu", dtype=torch.float32)
    load_s = time.time() - t0
    whisper = WhisperModel("small", device="cpu", compute_type="int8")
    report = {"model": MODEL_ID, "device": "CPU only, " + f"{os.cpu_count()} cores, {platform.machine()}",
              "reference": {"voice": "Kokoro-82M af_heart (synthetic)", "seconds": round(len(s) / sr, 1), "text": REF_TEXT},
              "load_seconds": round(load_s, 1), "lines": []}
    for name, lang, text in JOBS:
        t = time.time()
        wavs, out_sr = model.generate_voice_clone(text=text, language=lang, ref_audio=str(ref), ref_text=REF_TEXT)
        gen_s = time.time() - t
        out = tmp / f"{name}.wav"
        sf.write(str(out), wavs[0], out_sr)
        mp3(out, f"clone_{name}")
        audio_s = len(wavs[0]) / out_sr
        x = np.interp(np.linspace(0, len(wavs[0]) - 1, int(audio_s * 16000)), np.arange(len(wavs[0])), wavs[0]).astype(np.float32)
        segs, _ = whisper.transcribe(x, language="ru" if lang == "Russian" else "en")
        report["lines"].append({"name": name, "language": lang, "text": text, "audio_seconds": round(audio_s, 1),
                                "generation_seconds": round(gen_s, 1), "real_time_factor": round(gen_s / audio_s, 1),
                                "whisper": " ".join(x.text.strip() for x in segs)})
        print(report["lines"][-1])
    (L06 / "demo_courier_audio" / "clone_report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()


if __name__ == "__main__":
    main()
