# -*- coding: utf-8 -*-
"""Build the real audio assets for the L06 deck from the L05 courier video.

    python make_audio.py            # voice-over, mix, transcripts, envelopes
    python make_audio.py --music    # also generate a music bed with MusicGen (slow on CPU)

Pipeline (the same one the lesson teaches):
  1 script      VO_LINES below (display text with digits + spoken text with words)
  2 voice       text-to-speech with open-weight models: Kokoro-82M (EN, Apache-2.0),
                Piper ru_RU-dmitri-medium (RU, voice data CC0; piper-tts package GPL-3.0)
  3 sound       native audio that Veo 3.1 generated together with the L05 clips
  4 music       optional: MusicGen-small (weights CC-BY-NC-4.0, so lesson demo only)
  5 mix         duck the Veo ambience under the voice, normalise to -14 LUFS, true peak -1 dBTP
  6 check       speech-to-text round trip with Whisper (faster-whisper, MIT), word error rate
                and a critical-term check (order number, time, minutes)

Inputs: ../../L05/demo_veo_showcase/courier_delivery_final.mp4 (Veo 3.1, 23 s, with audio)
        ../../L05/assets/v2/video/final.mp4 (same picture, 960x540, no audio)
Models are downloaded once to $L06_MODELS (default: ~/.cache/l06_models):
  kokoro-v1.0.onnx, voices-v1.0.bin  github.com/thewh1teagle/kokoro-onnx/releases/tag/model-files-v1.0
  ru_RU-dmitri-medium.onnx(.json)    huggingface.co/rhasspy/piper-voices/tree/main/ru/ru_RU/dmitri/medium
Outputs: ../assets/v2/audio/*.mp3, ../assets/v2/video/courier_voiced_{en,ru}.mp4,
         ../demo_courier_audio/report.json (loudness, transcripts, WER), envelopes for the deck.
"""
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf

HERE = Path(__file__).resolve().parent
L06 = HERE.parent
L05 = L06.parent / "L05"
SRC_AV = L05 / "demo_veo_showcase" / "courier_delivery_final.mp4"
SRC_PIC = L05 / "assets" / "v2" / "video" / "final.mp4"
MODELS = Path(os.environ.get("L06_MODELS", Path.home() / ".cache" / "l06_models"))
AUD = L06 / "assets" / "v2" / "audio"
VID = L06 / "assets" / "v2" / "video"
DEMO = L06 / "demo_courier_audio"
SR = 48000
DUR = 23.0

# (start s, display text = what the reviewer checks, spoken text = what the voice model reads)
VO_LINES = {
    "en": [
        (0.6, "6:42. Order 417 is picked up, still hot.", "Six forty-two. Order four one seven is picked up, still hot."),
        (8.4, "Rain on the avenue. The route skips the bridge.", "Rain on the avenue. The route skips the bridge."),
        (16.2, "12 minutes to the door. Anna is on her way.", "Twelve minutes to the door. Anna is on her way."),
    ],
    "ru": [
        (0.6, "6:42. Заказ 417 забран, ещё горячий.", "Шесть сорок две. Заказ четыреста семнадцать забран, ещё горячий."),
        (8.4, "На проспекте дождь. Маршрут в обход моста.", "На проспекте дождь. Маршрут в обход моста."),
        (16.2, "До двери 12 минут. Анна уже в пути.", "До двери двенадцать минут. Анна уже в пути."),
    ],
}
MUSIC_PROMPT = "calm lo-fi hip hop beat, soft electric piano, light rain mood, 85 bpm, no vocals"

# Words that must survive the round trip exactly (as a listener would write them down)
CRITICAL = {
    "en": [("6:42", r"6:42|six forty[- ]two"), ("417", r"417|four[- ]one[- ]seven|four hundred (and )?seventeen"),
           ("12 minutes", r"12 minutes|twelve minutes"), ("Anna", r"\banna\b")],
    "ru": [("6:42", r"6:42|шесть сорок два|шесть сорок две"), ("417", r"417|четыреста семнадцать"),
           ("12 минут", r"12 минут|двенадцать минут"), ("Анна", r"\bанна\b")],
}


def run(*cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def resample(x, sr_in, sr_out=SR):
    if sr_in == sr_out:
        return x.astype(np.float32)
    n = int(round(len(x) * sr_out / sr_in))
    return np.interp(np.linspace(0, len(x) - 1, n), np.arange(len(x)), x).astype(np.float32)


def tts_en(text):
    from kokoro_onnx import Kokoro
    k = Kokoro(str(MODELS / "kokoro-v1.0.onnx"), str(MODELS / "voices-v1.0.bin"))
    s, sr = k.create(text, voice="af_heart", speed=1.0, lang="en-us")
    return resample(np.asarray(s), sr)


def tts_ru(text):
    from piper import PiperVoice, SynthesisConfig
    v = PiperVoice.load(str(MODELS / "ru_RU-dmitri-medium.onnx"))
    cfg = SynthesisConfig(noise_scale=0.0, noise_w_scale=0.0)  # no sampling noise: same audio on every run
    pcm = b"".join(c.audio_int16_bytes for c in v.synthesize(text, syn_config=cfg))
    return resample(np.frombuffer(pcm, dtype=np.int16) / 32768.0, v.config.sample_rate)


def voice_track(lang):
    out = np.zeros(int(DUR * SR), dtype=np.float32)
    lines = []
    for start, display, spoken in VO_LINES[lang]:
        x = (tts_en if lang == "en" else tts_ru)(spoken)
        x = x / (np.abs(x).max() + 1e-9) * 0.7
        i = int(start * SR)
        out[i:i + len(x)] += x[: len(out) - i]
        lines.append({"start": start, "end": round(start + len(x) / SR, 2), "display": display, "spoken": spoken})
    return out, lines


def loudness(path):
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    tail = p.stderr[p.stderr.rfind("Summary:"):]
    lufs = float(re.search(r"I:\s+(-?[\d.]+) LUFS", tail).group(1))
    tp = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", tail).group(1))
    return lufs, tp


def normalise(src, dst, target=-14.0, tp=-1.5):
    """Two-pass loudness normalisation (EBU R128 measurement, linear gain), then a true-peak limiter."""
    p = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(src), "-af", f"loudnorm=I={target}:TP={tp}:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    m = json.loads(p.stderr[p.stderr.rfind("{"):p.stderr.rfind("}") + 1])
    af = (f"loudnorm=I={target}:TP={tp}:LRA=11:linear=true:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']},"
          f"aresample={SR * 4},alimiter=limit={10 ** (tp / 20):.4f}:level=false,aresample={SR}")
    run("ffmpeg", "-y", "-i", str(src), "-af", af, "-ar", str(SR), str(dst))


def envelope(path, n=460):
    x, sr = sf.read(str(path), always_2d=True)
    x = x.mean(axis=1)
    hop = max(1, len(x) // n)
    env = [float(np.sqrt(np.mean(x[i * hop:(i + 1) * hop] ** 2))) for i in range(n)]
    return [round(v, 4) for v in env]


def transcribe(path, lang):
    from faster_whisper import WhisperModel
    m = WhisperModel("small", device="cpu", compute_type="int8")
    x, sr = sf.read(str(path), always_2d=True)
    x = resample(x.mean(axis=1), sr, 16000)  # Whisper expects 16 kHz mono
    segs, info = m.transcribe(x, language=lang, word_timestamps=False, vad_filter=True)
    return [{"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip()} for s in segs]


def norm(s):
    s = s.lower().replace("ё", "е")
    return re.sub(r"[^\w\s:]", " ", s).split()


def wer(ref, hyp):
    r, h = norm(ref), norm(hyp)
    d = np.zeros((len(r) + 1, len(h) + 1), dtype=int)
    d[:, 0] = range(len(r) + 1)
    d[0, :] = range(len(h) + 1)
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            d[i, j] = min(d[i - 1, j] + 1, d[i, j - 1] + 1, d[i - 1, j - 1] + (r[i - 1] != h[j - 1]))
    return round(d[len(r), len(h)] / max(1, len(r)), 3), len(r)


def musicgen(out_wav):
    import torch
    from transformers import AutoProcessor, MusicgenForConditionalGeneration
    torch.manual_seed(7)
    proc = AutoProcessor.from_pretrained("facebook/musicgen-small")
    model = MusicgenForConditionalGeneration.from_pretrained("facebook/musicgen-small")
    prompt = MUSIC_PROMPT
    inputs = proc(text=[prompt], padding=True, return_tensors="pt")
    audio = model.generate(**inputs, max_new_tokens=int(DUR * 50) + 10, do_sample=True, guidance_scale=3.0)
    sr = model.config.audio_encoder.sampling_rate
    x = audio[0, 0].cpu().numpy()
    sf.write(str(out_wav), resample(x, sr)[: int(DUR * SR)], SR)
    return prompt


def main():
    for d in (AUD, VID, DEMO):
        d.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp(prefix="l06_"))
    envs_extra = {}
    report = {"source_video": "L05/demo_veo_showcase/courier_delivery_final.mp4 (Veo 3.1, 23 s)",
              "music_prompt": MUSIC_PROMPT, "music_model": "facebook/musicgen-small (CC-BY-NC-4.0), seed 7", "langs": {}}

    # 3 sound: native Veo audio
    veo = tmp / "veo.wav"
    run("ffmpeg", "-y", "-i", str(SRC_AV), "-vn", "-ac", "2", "-ar", str(SR), "-t", str(DUR), str(veo))
    report["veo_native"] = dict(zip(("lufs", "true_peak_dbfs"), loudness(veo)))
    run("ffmpeg", "-y", "-i", str(veo), "-b:a", "128k", str(AUD / "veo_native.mp3"))

    for name, src in (("veo_shot1", "shot1.mp4"), ("veo_trainwreck", "trainwreck_naive_t2v.mp4")):
        run("ffmpeg", "-y", "-i", str(L05 / "demo_veo_showcase" / src), "-vn", "-ac", "2", "-b:a", "128k", str(AUD / f"{name}.mp3"))
        envs_extra[name] = str(AUD / f"{name}.mp3")

    # 4 music (optional)
    music = tmp / "music.wav"
    if "--music" in sys.argv:
        musicgen(music)
        run("ffmpeg", "-y", "-i", str(music), "-b:a", "128k", str(AUD / "music_bed.mp3"))
    elif (AUD / "music_bed.mp3").exists():
        run("ffmpeg", "-y", "-i", str(AUD / "music_bed.mp3"), "-ac", "1", "-ar", str(SR), str(music))
    has_music = music.exists()

    envs = {"veo": envelope(veo)}
    for name, path in envs_extra.items():
        w = tmp / f"{name}.wav"
        run("ffmpeg", "-y", "-i", path, "-ar", str(SR), str(w))
        envs[name] = envelope(w, 300)
        report[name] = {"transcript": transcribe(w, "en")}
    if has_music:
        envs["music"] = envelope(music)
    for lang in ("en", "ru"):
        vo, lines = voice_track(lang)
        vo_wav = tmp / f"vo_{lang}.wav"
        sf.write(str(vo_wav), vo, SR)
        run("ffmpeg", "-y", "-i", str(vo_wav), "-b:a", "128k", str(AUD / f"vo_{lang}.mp3"))
        envs[f"vo_{lang}"] = envelope(vo_wav)
        envs[f"vo_{lang}_fine"] = envelope(vo_wav, 2300)  # 10 ms bins for the "how it works" slide

        # 5 mix: Veo bed (and music) ducked by the voice, then loudness-normalised
        mix = tmp / f"mix_{lang}.wav"
        bed = "[1:a]volume=0.8[bed0];"
        if has_music:
            bed = "[1:a]volume=0.8[v];[2:a]volume=0.35,aresample=48000,aformat=channel_layouts=stereo[m];[v][m]amix=inputs=2:normalize=0[bed0];"
        graph = (f"[0:a]aformat=channel_layouts=stereo,asplit=2[vo][sc];{bed}"
                 "[bed0][sc]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];"
                 "[vo][duck]amix=inputs=2:normalize=0[out]")
        ins = ["-i", str(vo_wav), "-i", str(veo)] + (["-i", str(music)] if has_music else [])
        pre = tmp / f"premix_{lang}.wav"
        run("ffmpeg", "-y", *ins, "-filter_complex", graph, "-map", "[out]", "-ar", str(SR), "-t", str(DUR), str(pre))
        normalise(pre, mix)
        run("ffmpeg", "-y", "-i", str(mix), "-b:a", "160k", str(AUD / f"mix_{lang}.mp3"))
        run("ffmpeg", "-y", "-i", str(SRC_PIC), "-i", str(mix), "-map", "0:v", "-map", "1:a", "-c:v", "copy",
            "-c:a", "aac", "-b:a", "160k", "-shortest", str(VID / f"courier_voiced_{lang}.mp4"))
        envs[f"mix_{lang}"] = envelope(mix)

        # 6 check: speech-to-text round trip on the final mix
        segs = transcribe(mix, lang)
        hyp = " ".join(s["text"] for s in segs)
        ref = " ".join(spoken for _, _, spoken in VO_LINES[lang])
        w, n = wer(ref, hyp)
        w_disp, _ = wer(" ".join(d for _, d, _ in VO_LINES[lang]), hyp)  # Whisper writes digits, so also score vs display text
        crit = [{"term": term, "ok": bool(re.search(rx, hyp.lower()))} for term, rx in CRITICAL[lang]]
        report["langs"][lang] = {"lines": lines, "mix": dict(zip(("lufs", "true_peak_dbfs"), loudness(mix))),
                                 "voice_only": dict(zip(("lufs", "true_peak_dbfs"), loudness(vo_wav))),
                                 "transcript": segs, "wer": w, "wer_vs_display": w_disp, "ref_words": n, "critical_terms": crit}
        print(lang, "WER", w, crit)

    (DEMO / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    (HERE / "envelopes.json").write_text(json.dumps(envs), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "langs"}, indent=1))


if __name__ == "__main__":
    main()
