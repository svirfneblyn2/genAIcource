# -*- coding: utf-8 -*-
"""
Full deck generator for Lesson 06: Speech and Audio AI (RU and EN)
Generates:
  - presentation_L06_Speech_and_Audio.html
  - presentation_L06_Speech_and_Audio_EN.html
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

def find_edge():
    for c in [shutil.which("msedge"),
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
              r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"]:
        if c and Path(c).exists():
            return c
    sys.exit("msedge not found")

CSS = """
:root {
  --bg: #0b0f17;
  --surface: #121a28;
  --surface-card: #0f1624;
  --line: rgba(148, 163, 184, 0.18);
  --fg: #f1f5f9;
  --muted: #9aa8bc;
  --dim: #5f6e84;
  --cyan: #38bdf8;
  --green: #34d399;
  --amber: #fbbf24;
  --red: #f87171;
  --violet: #c084fc;
  --display: 'Onest', 'Segoe UI', Arial, sans-serif;
  --body: 'Onest', 'Segoe UI', Arial, sans-serif;
  --mono: 'JetBrains Mono', Consolas, monospace;
  color-scheme: dark;
}
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { height: 100%; }
body { background: #05080e; color: var(--fg); font-family: var(--body); overflow: hidden; -webkit-font-smoothing: antialiased; }

.stage { position: absolute; left: 50%; top: 50%; width: 1600px; height: 900px; transform: translate(-50%, -50%) scale(var(--s, 1)); transform-origin: center; background: var(--bg); overflow: hidden; border-radius: 6px; box-shadow: 0 30px 80px rgba(0,0,0,.6); }
.slide { position: absolute; inset: 0; padding: 50px 72px 58px; display: none; flex-direction: column; }
.slide.active { display: flex; }

.kicker { font-family: var(--mono); font-size: 14px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: var(--k, var(--cyan)); margin-bottom: 10px; }
.title { font-family: var(--display); font-weight: 700; font-size: 46px; line-height: 1.14; letter-spacing: -0.02em; text-wrap: balance; max-width: 1450px; }
.lead { font-size: 21px; line-height: 1.38; color: var(--muted); margin-top: 10px; max-width: 1350px; text-wrap: balance; }
.body { flex: 1 1 0; min-height: 0; margin-top: 24px; display: flex; flex-direction: column; justify-content: center; }
.foot { position: absolute; left: 72px; right: 72px; bottom: 20px; display: flex; justify-content: space-between; font-family: var(--mono); font-size: 13px; color: var(--dim); }

.row { display: grid; gap: 32px; flex: 1 1 0; min-height: 0; }
.c2 { grid-template-columns: 1fr 1fr; }
.c3 { grid-template-columns: repeat(3, 1fr); }
.c4 { grid-template-columns: repeat(4, 1fr); }
.stack { display: flex; flex-direction: column; gap: 16px; min-height: 0; min-width: 0; }
.center { justify-content: center; }

.card-box { background: var(--surface-card); border: 1px solid var(--line); border-radius: 12px; padding: 20px; display: flex; flex-direction: column; gap: 10px; }
.card-box.active { border-color: var(--cyan); }
.card-label { font-family: var(--mono); font-size: 13px; letter-spacing: .08em; text-transform: uppercase; font-weight: 700; color: var(--k, var(--cyan)); }
.pt { display: flex; flex-direction: column; gap: 6px; }
.pt .h { font-size: 22px; font-weight: 700; line-height: 1.25; }
.pt .d { font-size: 18px; line-height: 1.38; color: var(--muted); }
.pt .d b { color: var(--fg); font-weight: 600; }
.note { font-size: 18px; line-height: 1.45; color: var(--muted); border-left: 3px solid var(--k, var(--cyan)); padding: 4px 0 4px 16px; }
.note b { color: var(--fg); }
code, .code-inline { font-family: var(--mono); font-size: .88em; background: rgba(255,255,255,.07); padding: 2px 7px; border-radius: 6px; color: #e2e8f0; }

.audio-tile { background: #0a0e17; border: 1px solid var(--line); border-radius: 12px; padding: 16px; display: flex; flex-direction: column; gap: 12px; position: relative; }
.audio-badge { position: absolute; top: 14px; right: 14px; font-family: var(--mono); font-size: 11px; padding: 3px 8px; border-radius: 4px; background: rgba(0,0,0,.7); font-weight: 700; }
.waveform-box { height: 120px; border-radius: 8px; background: #131d2e; display: flex; align-items: center; justify-content: center; position: relative; border: 1px dashed rgba(255,255,255,.1); gap: 4px; padding: 0 20px; }
.wave-bar { width: 5px; background: var(--cyan); border-radius: 3px; height: var(--h, 40%); opacity: 0.85; }
.play-btn { width: 44px; height: 44px; border-radius: 50%; background: rgba(192,132,252,.2); border: 2px solid var(--violet); display: flex; align-items: center; justify-content: center; color: var(--violet); font-size: 18px; margin-right: 12px; }

.stepper { display: grid; grid-template-columns: repeat(6, 1fr); gap: 12px; }
.step-item { background: var(--surface-card); border: 1px solid var(--line); border-radius: 10px; padding: 14px; display: flex; flex-direction: column; gap: 6px; }
.step-item.active { border-color: var(--cyan); background: rgba(56,189,248,.08); }
.step-item.done { border-color: var(--green); }
.step-num { font-family: var(--mono); font-size: 12px; color: var(--dim); font-weight: 700; }
.step-item.active .step-num { color: var(--cyan); }
.step-item.done .step-num { color: var(--green); }
.step-title { font-size: 16px; font-weight: 700; }
.step-sub { font-size: 13px; color: var(--muted); }

table.t { width: 100%; border-collapse: collapse; font-size: 17px; }
table.t th { text-align: left; font-family: var(--mono); font-size: 13px; letter-spacing: .08em; text-transform: uppercase; color: var(--dim); font-weight: 700; padding: 0 12px 10px; border-bottom: 1px solid var(--line); }
table.t td { padding: 10px 12px; border-bottom: 1px solid var(--line); color: var(--muted); vertical-align: middle; line-height: 1.35; }
table.t td:first-child { color: var(--fg); font-weight: 600; white-space: nowrap; }

.drawer { position: fixed; right: 0; top: 0; bottom: 0; width: 440px; background: #0f172a; border-left: 1px solid #334155; transform: translateX(100%); transition: transform .25s ease; z-index: 1000; padding: 28px; display: flex; flex-direction: column; gap: 16px; overflow-y: auto; }
.drawer.open { transform: translateX(0); }
.drawer .hd { font-family: var(--mono); font-size: 13px; letter-spacing: .08em; text-transform: uppercase; color: var(--cyan); }
.drawer .tx { font-size: 17px; line-height: 1.5; color: #cbd5e1; }
.grid { position: fixed; inset: 0; background: rgba(5,8,14,.92); backdrop-filter: blur(10px); display: none; grid-template-columns: repeat(6, 1fr); gap: 14px; padding: 40px; z-index: 2000; overflow-y: auto; }
.grid.open { display: grid; }
.grid button { background: var(--surface); border: 1px solid var(--line); border-radius: 8px; padding: 14px; color: var(--fg); text-align: left; cursor: pointer; display: flex; flex-direction: column; gap: 8px; font-family: var(--body); }
.grid button:hover { border-color: var(--cyan); }
.grid button.cur { border-color: var(--cyan); background: rgba(56,189,248,.1); }
.grid button span { font-family: var(--mono); font-size: 12px; color: var(--cyan); }

@media print {
  @page { size: 1600px 900px; margin: 0; }
  body { overflow: visible; background: var(--bg); -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .stage { position: static; transform: none; width: 1600px; height: auto; border-radius: 0; box-shadow: none; overflow: visible; }
  .slide { position: relative; display: flex !important; width: 1600px; height: 900px; break-after: page; page-break-after: always; }
  .drawer, .grid, button { display: none !important; }
}
"""

JS = """
(function(){
  const stage = document.getElementById('stage');
  const slides = Array.from(document.querySelectorAll('.slide'));
  const drawer = document.getElementById('drawer');
  const grid = document.getElementById('grid');
  let cur = 0;

  function resize(){
    const s = Math.min(window.innerWidth / 1600, window.innerHeight / 900);
    stage.style.setProperty('--s', s);
  }
  window.addEventListener('resize', resize);
  resize();

  function show(n){
    if (n < 0 || n >= slides.length) return;
    slides[cur].classList.remove('active');
    cur = n;
    slides[cur].classList.add('active');
    updateDrawer();
    updateGrid();
  }

  function updateDrawer(){
    const t = slides[cur].querySelector('template.notes');
    const isEn = document.documentElement.lang === 'en';
    drawer.querySelector('.hd').textContent = isEn ? `SLIDE ${cur+1} / ${slides.length} • SPEAKER NOTES` : `СЛАЙД ${cur+1} / ${slides.length} • ЗАМЕТКИ СПИКЕРА`;
    drawer.querySelector('.tx').innerHTML = t ? t.innerHTML : (isEn ? '<i>No speaker notes for this slide.</i>' : '<i>Нет заметок для этого слайда.</i>');
  }

  function initGrid(){
    grid.innerHTML = '';
    slides.forEach((s, i) => {
      const b = document.createElement('button');
      const title = s.querySelector('.title') ? s.querySelector('.title').textContent : `Slide ${i+1}`;
      b.innerHTML = `<span>#${(i+1).toString().padStart(2, '0')}</span><strong>${title}</strong>`;
      b.onclick = () => { show(i); grid.classList.remove('open'); };
      grid.appendChild(b);
    });
  }
  function updateGrid(){
    Array.from(grid.children).forEach((b, i) => {
      b.classList.toggle('cur', i === cur);
    });
  }
  initGrid();

  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') { show(cur + 1); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { show(cur - 1); }
    else if (e.key.toLowerCase() === 'n') { drawer.classList.toggle('open'); }
    else if (e.key.toLowerCase() === 'g') { grid.classList.toggle('open'); }
    else if (e.key.toLowerCase() === 'f') {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen();
      else document.exitFullscreen();
    }
  });

  const timerBtn = document.getElementById('timer-btn');
  const timerReset = document.getElementById('timer-reset');
  const timerDisplay = document.getElementById('timer-display');
  if (timerBtn && timerDisplay) {
    const isEn = document.documentElement.lang === 'en';
    let timeLeft = 300;
    let timerId = null;
    function updateTimer() {
      const m = Math.floor(timeLeft / 60);
      const s = timeLeft % 60;
      timerDisplay.textContent = `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
    }
    timerBtn.onclick = () => {
      if (timerId) {
        clearInterval(timerId);
        timerId = null;
        timerBtn.textContent = isEn ? 'START 5 MIN' : 'СТАРТ 5 МИН';
      } else {
        timerBtn.textContent = isEn ? 'PAUSE' : 'ПАУЗА';
        timerId = setInterval(() => {
          if (timeLeft > 0) {
            timeLeft--;
            updateTimer();
          } else {
            clearInterval(timerId);
            timerId = null;
            timerBtn.textContent = isEn ? "TIME'S UP" : 'ВРЕМЯ ВЫШЛО';
          }
        }, 1000);
      }
    };
    if (timerReset) {
      timerReset.onclick = () => {
        if (timerId) { clearInterval(timerId); timerId = null; }
        timeLeft = 300;
        updateTimer();
        timerBtn.textContent = isEn ? 'START 5 MIN' : 'СТАРТ 5 МИН';
      };
    }
  }
})();
"""

def build_deck(lang="ru"):
    is_en = (lang == "en")
    kicker = "GenAI Basics • Lesson 06 • Module 2: Multimodality" if is_en else "GenAI Basics • Урок 06 • Модуль 2: Мультимодальность"
    foot = "GenAI Basics • Lesson 06 • Speech and Audio AI" if is_en else "GenAI Basics • Урок 06 • Речь и аудио AI"
    html_title = "Lesson 06: Speech and Audio AI | GenAI Basics" if is_en else "Урок 06: Речь и аудио AI — синтез речи, Whisper, Foley и генерация музыки | GenAI Basics"

    # We build the 24 slides:
    s = []

    # Slide 1: Cover
    s.append(f"""
<section class="slide active" data-n="1">
  <div class="kicker">{kicker}</div>
  <h1 class="title">{"Speech and Audio AI: Text-to-Speech, Whisper, Foley Sound Design & Music Pipelines" if is_en else "Речь и аудио AI: синтез речи, Whisper, саунд-дизайн Foley и генерация музыки"}</h1>
  <p class="lead">{"From 1D acoustic pressure waves and mel-spectrograms to discrete neural codecs, word-level timestamps, and synchronized multi-stem audio." if is_en else "От одномерных звуковых волн и мел-спектрограмм к дискретным нейрокодекам, пословным таймкодам и синхронизированному мультитреку."}</p>
  <div class="body">
    <div class="row c2" style="align-items:center;">
      <div class="stack center" style="gap:20px;">
        <div class="card-box" style="border-color:var(--cyan);background:rgba(56,189,248,.04);">
          <div class="card-label">{"THE 10/90 AXIOM IN GENERATIVE AUDIO" if is_en else "АКСИОМА 10/90 В ГЕНЕРАТИВНОМ ЗВУКЕ"}</div>
          <div style="font-size:21px;line-height:1.45;color:var(--fg);">
            {"The neural model synthesizing raw audio tokens is just <b>10% of production</b>.<br>The remaining <b>90%</b> is Voice Activity Detection (VAD), LUFS loudness normalization, word-level subtitle alignment, SynthID watermarking, sub-150ms streaming latency, and multi-stem mixing." if is_en else "Нейросетевая модель, генерирующая сырую форму волны — это лишь <b>10% успеха</b>.<br>Остальные <b>90%</b> — это Voice Activity Detection (VAD), нормализация громкости LUFS, пословные таймкоды, водяные знаки SynthID/C2PA, задержка менее 150 мс и сведение дорожек (Stem Mixing)."}
          </div>
        </div>
        <div class="note"><b>{"Instructor:" if is_en else "Спикер:"}</b> {"Igor Rubanovich (EPAM Systems • AI Ambassador & Engineering Manager II). Hands-on AI R&D: Architect and developer of Creator Tools — a suite of AI tools for YouTube creators." if is_en else "Игорь Рубанович (EPAM Systems • AI Ambassador & Engineering Manager II). Практический AI R&D: Архитектор и разработчик Creator Tools — набор AI-инструментов для авторов YouTube."}</div>
      </div>
      <div class="stack center">
        <div class="card-box" style="background:var(--surface);">
          <div class="card-label" style="color:var(--amber)">{"KEY TOPICS OF THIS 90-MINUTE SESSION" if is_en else "КЛЮЧЕВЫЕ ТЕМЫ 90-МИНУТНОГО ЗАНЯТИЯ"}</div>
          <ul style="list-style:none;display:flex;flex-direction:column;gap:12px;font-size:18px;color:var(--muted);padding-left:4px;">
            <li>🔹 <b>{"Acoustic Physics & Codecs:" if is_en else "Физика звука и нейрокодеки:"}</b> {"PCM, STFT, Mel-Spectrograms, EnCodec & DAC" if is_en else "PCM, STFT, мел-спектрограммы, EnCodec и DAC"}</li>
            <li>🔹 <b>{"Speech-to-Text (STT):" if is_en else "Распознавание речи (STT):"}</b> {"Whisper architecture, repetition loops & Silero VAD" if is_en else "Архитектура Whisper, петли галлюцинаций и Silero VAD"}</li>
            <li>🔹 <b>{"Text-to-Speech (TTS):" if is_en else "Синтез речи (TTS):"}</b> {"ElevenLabs, Cartesia (135ms TTFT), Kokoro & prosody steering" if is_en else "ElevenLabs, Cartesia (135 мс TTFT), Kokoro и управление эмоциями"}</li>
            <li>🔹 <b>{"Voice Cloning & Ethics:" if is_en else "Клонирование голоса и этика:"}</b> {"Instant vs Pro, Voice Captcha consent, SynthID/PerTh" if is_en else "Instant vs Pro, Voice Captcha, водяные знаки SynthID"}</li>
            <li>🔹 <b>{"Foley & Sound Design (SFX AI):" if is_en else "Шумы и Foley (SFX AI):"}</b> {"Generating physics-aligned ambient audio" if is_en else "Генерация предметных звуков и акустики окружения"}</li>
            <li>🔹 <b>{"AI Music & Multi-Stem Assembly:" if is_en else "Музыка AI и сведение дорожек:"}</b> {"Suno v4, Udio 1.5, ducking, Python mixing" if is_en else "Suno v4, Udio 1.5, дакинг и сборка в Python"}</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>01 / 24</span></div>
  <template class="notes">{"Welcome students. Open Module 2 grand finale: Audio and Speech. Emphasize that in L05 our video generations were mute; today we engineer the complete acoustic spectrum." if is_en else "Приветствуем студентов. Открываем финал Модуля 2: Аудио и речь. Подчеркиваем: в L05 видео были немыми; сегодня мы оживляем их полным спектром звука."}</template>
</section>
""")

    # Slide 2: Hook Quiz
    s.append(f"""
<section class="slide" data-n="2">
  <div class="kicker">{"Interactive Calibration • Blind Audio Test" if is_en else "Интерактивная калибровка • Слепой тест на слух"}</div>
  <h2 class="title">{"Blind Listening Quiz: Can Your Ear Detect Generative Audio?" if is_en else "Викторина-хук: способен ли ваш слух отличить синтетический звук?"}</h2>
  <p class="lead">{"Listen to 4 studio-grade audio fragments. Which of these are recorded with physical microphones, and which are pure neural synthesis?" if is_en else "Прослушайте 4 студийных аудиофрагмента. Какие из них записаны микрофоном Neumann, а какие сгенерированы нейросетью?"}</p>
  <div class="body">
    <div class="row c4">
      <div class="audio-tile">
        <div class="audio-badge" style="color:var(--cyan)">{"CLIP [A]" if is_en else "КЛИП [A]"}</div>
        <div class="waveform-box">
          <div class="play-btn">▶</div>
          <div class="wave-bar" style="--h:30%"></div><div class="wave-bar" style="--h:70%"></div><div class="wave-bar" style="--h:95%"></div><div class="wave-bar" style="--h:40%"></div><div class="wave-bar" style="--h:85%"></div><div class="wave-bar" style="--h:60%"></div>
        </div>
        <div class="pt"><div class="h">{"Studio Voiceover" if is_en else "Дикторская начитка"}</div><div class="d">{"Warm documentary narrator tone, subtle breathing intake, crisp sibilants." if is_en else "Бархатный тембр документалиста, естественный вдох, звонкие согласные."}</div></div>
      </div>
      <div class="audio-tile">
        <div class="audio-badge" style="color:var(--green)">{"CLIP [B]" if is_en else "КЛИП [B]"}</div>
        <div class="waveform-box">
          <div class="play-btn">▶</div>
          <div class="wave-bar" style="--h:20%"></div><div class="wave-bar" style="--h:50%"></div><div class="wave-bar" style="--h:80%"></div><div class="wave-bar" style="--h:90%"></div><div class="wave-bar" style="--h:40%"></div><div class="wave-bar" style="--h:30%"></div>
        </div>
        <div class="pt"><div class="h">{"Bicycle Foley SFX" if is_en else "Фоли-шум велосипеда"}</div><div class="d">{"Tires splashing through gravel puddles, chain rattle, wet asphalt spray." if is_en else "Шины режут гравийную лужу, звон цепи, реалистичный мокрый асфальт."}</div></div>
      </div>
      <div class="audio-tile">
        <div class="audio-badge" style="color:var(--amber)">{"CLIP [C]" if is_en else "КЛИП [C]"}</div>
        <div class="waveform-box">
          <div class="play-btn">▶</div>
          <div class="wave-bar" style="--h:60%"></div><div class="wave-bar" style="--h:80%"></div><div class="wave-bar" style="--h:75%"></div><div class="wave-bar" style="--h:90%"></div><div class="wave-bar" style="--h:65%"></div><div class="wave-bar" style="--h:85%"></div>
        </div>
        <div class="pt"><div class="h">{"Acoustic Jazz Trio" if is_en else "Акустический джаз"}</div><div class="d">{"Upright piano, brushed snare drum, acoustic upright bass swing groove." if is_en else "Живое пианино, щеточки по малому барабану, пульсирующий контрабас."}</div></div>
      </div>
      <div class="audio-tile">
        <div class="audio-badge" style="color:var(--violet)">{"CLIP [D]" if is_en else "КЛИП [D]"}</div>
        <div class="waveform-box">
          <div class="play-btn">▶</div>
          <div class="wave-bar" style="--h:40%"></div><div class="wave-bar" style="--h:60%"></div><div class="wave-bar" style="--h:55%"></div><div class="wave-bar" style="--h:70%"></div><div class="wave-bar" style="--h:50%"></div><div class="wave-bar" style="--h:35%"></div>
        </div>
        <div class="pt"><div class="h">{"Customer Support Call" if is_en else "Звонок в техподдержку"}</div><div class="d">{"130ms live dialogue interruption, natural conversational fillers ('uh-huh', 'sure')." if is_en else "Диалог с задержкой 130 мс, перебивание собеседника, междометия «угу», «да-да»."}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--amber)"><b>{"Interactive Question for Chat:" if is_en else "Вопрос в чат:"}</b> {"Drop your guesses in chat: which clips are 100% synthetic AI? Give the audience 45 seconds before revealing." if is_en else "Напишите в чат, какие из 4 фрагментов — 100% нейросетевая генерация? Дать студентам 45 секунд на ответы."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>02 / 24</span></div>
  <template class="notes">{"Play snippets or describe acoustic artifacts. Ask chat: A, B, C, or D? Reveal on next slide: ALL FOUR are 2026 generative AI!" if is_en else "Слушаем ответы в чате. Студенты часто думают, что джаз (C) или дыхание (A) точно настоящие. Раскрываем карты на следующем слайде: все 4 — чистый ИИ 2026 года!"}</template>
</section>
""")

    # Slide 3: Evolution
    s.append(f"""
<section class="slide" data-n="3">
  <div class="kicker">{"Historical Trajectory • 2020–2026" if is_en else "Эволюция нейрозвука • 2020–2026"}</div>
  <h2 class="title">{"The Acoustic Revolution: From Metallic Buzz to 48kHz Neural Reality" if is_en else "Хроника преодоления робота: от металлического зуммера к студийным 48 кГц"}</h2>
  <p class="lead">{"All 4 clips were 100% synthesized. In six years, audio AI jumped from robotic text-to-speech to full conversational agency." if is_en else "Все 4 аудиофрагмента были на 100% сгенерированы ИИ. За 6 лет аудиотехнологии прошли путь от синтезаторов навигаторов до живых речевых агентов."}</p>
  <div class="body">
    <div class="row c4">
      <div class="card-box">
        <div class="card-label">{"2020–2021 • ROBOTIC PHONEMES" if is_en else "2020–2021 • РОБОТИЗИРОВАННЫЙ ЗВОН"}</div>
        <div class="pt"><div class="h">WaveNet & FastSpeech</div><div class="d"><b>{"State:" if is_en else "Срез:"}</b> {"Robotic metallic comb-filtering, flat monotone cadence, zero emotional expressivity, 16kHz bandwidth." if is_en else "Металлический фазовый шум, роботизированная интонация без пауз и эмоций, полоса пропускания 16 кГц."}</div></div>
      </div>
      <div class="card-box">
        <div class="card-label">{"2022–2023 • FOUNDATIONAL STT/TTS" if is_en else "2022–2023 • ПРОРЫВ РАСПОЗНАВАНИЯ"}</div>
        <div class="pt"><div class="h">OpenAI Whisper & ElevenLabs v1</div><div class="d"><b>{"State:" if is_en else "Срез:"}</b> {"Whisper solves speech recognition at scale; ElevenLabs introduces believable human prosody and voice cloning." if is_en else "OpenAI Whisper решает задачу транскрибации; ElevenLabs вводит эмоциональную выразительность и клонирование."}</div></div>
      </div>
      <div class="card-box">
        <div class="card-label">{"2024–2025 • DISCRETE AUDIO CODECS" if is_en else "2024–2025 • НЕЙРОКОДЕКИ И МУЗЫКА"}</div>
        <div class="pt"><div class="h">Suno v3, Udio & EnCodec</div><div class="d"><b>{"State:" if is_en else "Срез:"}</b> {"Full 3-minute stereo song generation with vocals; text-to-sound-effects (SFX); end-to-end discrete audio tokenization." if is_en else "Полноценные 3-минутные песни с вокалом и куплетами; текстовая генерация фоли-шумов (SFX); дискретные токены звука."}</div></div>
      </div>
      <div class="card-box active" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"2026 • REAL-TIME VOICE AGENTS" if is_en else "2026 • ГОЛОСОВЫЕ АГЕНТЫ ON-DEVICE"}</div>
        <div class="pt"><div class="h">Cartesia Sonic, Whisper v3 & Suno v4</div><div class="d"><b>{"State:" if is_en else "Срез:"}</b> {"Sub-150ms full-duplex speech loops, studio 48kHz fidelity, zero-shot multilingual voice cloning with native timbre preservation." if is_en else "Задержка речевого цикла менее 150 мс, студийное качество 48 кГц, мгновенный перевод речи с сохранением оригинального тембра."}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"The Core 2026 Challenge:" if is_en else "Вызов 2026 года:"}</b> {"Timbre and fidelity are solved. The frontier is <b>temporal latency (<150ms for voice agents)</b> and <b>multi-stem synchronization</b>." if is_en else "Вопрос естественности тембра закрыт. Главная битва идет за <b>минимальную задержку диалога (<150 мс)</b> и <b>мультитрековое сведение</b>."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>03 / 24</span></div>
  <template class="notes">{"Trace the timeline. Explain that audio models process 44,100 samples per second per channel — far denser than text tokens." if is_en else "Показываем хронологию. Подчеркиваем: звук сложнее текста тем, что секунда аудио — это 44 100 отсчетов амплитуды."}</template>
</section>
""")

    # Slide 4: Roadmap & Bridge
    s.append(f"""
<section class="slide" data-n="4">
  <div class="kicker">{"Curriculum Roadmap • Module 2 Grand Finale" if is_en else "Дорожная карта курса • Финал Модуля 2"}</div>
  <h2 class="title">{"Completing Multimodality: Giving Sound to Silent Generative Video" if is_en else "Завершение мультимодальности: озвучивание немых роликов из L05"}</h2>
  <p class="lead">{"Module 2 connects text prompts to physical perception. In L04 we created static pixels; in L05 we gave them motion. Today we add voice, Foley, and music." if is_en else "Модуль 2 переводит текстовые промпты в физический мир. В L04 мы зафиксировали кадры, в L05 оживили движение. Сегодня мы даем роликам голос, шумы и саундтрек."}</p>
  <div class="body">
    <div class="stepper" style="margin-bottom:24px;">
      <div class="step-item done"><div class="step-num">{"M1 • DONE" if is_en else "M1 • ГОТОВО"}</div><div class="step-title">{"Foundations" if is_en else "База LLM"}</div><div class="step-sub">{"L01–L03: LLMs & API" if is_en else "L01–L03: Промпты и API"}</div></div>
      <div class="step-item done"><div class="step-num">{"L04 • DONE" if is_en else "L04 • ГОТОВО"}</div><div class="step-title">{"Images" if is_en else "Картинки"}</div><div class="step-sub">{"Prompts, C2_rain, packshot" if is_en else "Промпты, C2_rain, пэкшот"}</div></div>
      <div class="step-item done"><div class="step-num">{"L05 • DONE" if is_en else "L05 • ГОТОВО"}</div><div class="step-title">{"Video" if is_en else "Видео"}</div><div class="step-sub">{"I2V, camera vectors, montage" if is_en else "I2V, камеры, монтаж"}</div></div>
      <div class="step-item active"><div class="step-num">{"L06 • HERE" if is_en else "L06 • ЗДЕСЬ"}</div><div class="step-title">{"Speech & Audio" if is_en else "Речь и звук"}</div><div class="step-sub">{"TTS, Whisper, Foley, Music" if is_en else "TTS, Whisper, Foley, саундтрек"}</div></div>
      <div class="step-item"><div class="step-num">{"M3 • NEXT" if is_en else "M3 • ДАЛЕЕ"}</div><div class="step-title">{"Ecosystem" if is_en else "Экосистема"}</div><div class="step-sub">{"L07: Copilot, M365 & Dev" if is_en else "L07: Copilot, M365 и Dev"}</div></div>
      <div class="step-item"><div class="step-num">{"M4–M6" if is_en else "M4–M6"}</div><div class="step-title">{"Agents & Production" if is_en else "Агенты и код"}</div><div class="step-sub">{"L08–L16: MCP & Code" if is_en else "L08–L16: MCP, архитектура"}</div></div>
    </div>
    <div class="row c2">
      <div class="card-box" style="border-color:var(--amber)">
        <div class="card-label" style="color:var(--amber)">{"THE ASSETS INHERITED FROM L05" if is_en else "ЧТО МЫ ПОЛУЧИЛИ ИЗ УРОКА 05"}</div>
        <div class="pt"><div class="h">{"Mute 5-Second Video Takes" if is_en else "Немые 5-секундные видеодубли"}</div><div class="d">{"Our Glovo courier pedaling in the rain (<code>shot2_bike_rain.mp4</code>) and rotating mug packshot (<code>packshot_360.mp4</code>) are visually complete, but emotionally silent." if is_en else "Курьер Glovo под дождем (<code>shot2_bike_rain.mp4</code>) и вращающаяся кружка кофе (<code>packshot_360.mp4</code>) безупречны визуально, но кинематографически мертвы без звука."}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"WHAT L06 ADDS TO COMPLETE PRODUCTION" if is_en else "ЧТО L06 ДАЕТ ДЛЯ ПОЛНОГО ПРОДАКШЕНА"}</div>
        <div class="pt"><div class="h">{"The Complete 3-Stem Audio Score" if is_en else "3-слойный акустический саундтрек"}</div><div class="d"><b>{"1. Voiceover:" if is_en else "1. Закадровый голос:"}</b> {"Crisp neural narration." if is_en else "синтез речи диктора с точной артикуляцией."}<br><b>{"2. Foley SFX:" if is_en else "2. Фоли SFX:"}</b> {"Splash of tires, rain on jacket, bicycle chain hum." if is_en else "брызги луж, шелест дождевика, трещотка втулки велосипеда."}<br><b>{"3. Music Underscore:" if is_en else "3. Музыка:"}</b> {"Subtle acoustic guitar groove with ducking." if is_en else "атмосферный фон с автоматическим приглушением (ducking)."}</div></div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>04 / 24</span></div>
  <template class="notes">{"Bridge L04 and L05 into L06. Students see that every lesson builds directly on top of earlier artifacts." if is_en else "Показываем преемственность. Модуль 2 логически закрывается: от текста к картинке, затем к видео, и наконец к полному аудиовизуальному продакшену."}</template>
</section>
""")

    # Slide 5: Physics of Audio & Codecs
    s.append(f"""
<section class="slide" data-n="5">
  <div class="kicker">{"Acoustic Engineering • Physics & Representations" if is_en else "Физика звука и нейросети • От волны к токенам"}</div>
  <h2 class="title">{"The Physics of Audio: Waveforms, Mel-Spectrograms, and Neural Codecs" if is_en else "Природа звука: форма волны, мел-спектрограммы и дискретные нейрокодеки"}</h2>
  <p class="lead">{"Computers perceive sound as 1D air pressure oscillations. AI models must compress continuous time into discrete tokens." if is_en else "Компьютер видит звук как одномерное колебание давления воздуха. Нейросети научились сжимать непрерывную волну в дискретные токены."}</p>
  <div class="body">
    <div class="row c4">
      <div class="card-box">
        <div class="card-label">{"1. RAW WAVEFORM (1D PCM)" if is_en else "1. СЫРАЯ ФОРМА ВОЛНЫ (PCM)"}</div>
        <div class="pt"><div class="h">{"44,100 Hz / 16-bit" if is_en else "44 100 Гц / 16 бит"}</div><div class="d">{"Uncompressed amplitude measurements over time. 1 second = 44,100 numbers. Too dense for autoregressive LLMs." if is_en else "Массив амплитуд во времени. 1 секунда стерео = 88 200 чисел. Слишком плотно для авторегрессионных трансформеров."}</div></div>
      </div>
      <div class="card-box">
        <div class="card-label">{"2. FOURIER TRANSFORM (STFT)" if is_en else "2. ПРЕОБРАЗОВАНИЕ ФУРЬЕ (STFT)"}</div>
        <div class="pt"><div class="h">{"Time ➔ Frequency" if is_en else "Время ➔ Частоты"}</div><div class="d">{"Windowed FFT decomposes overlapping audio frames into sinusoidal frequency bins and phase angles." if is_en else "Оконное преобразование раскладывает скользящие фрагменты звука на гармонические частотные составляющие."}</div></div>
      </div>
      <div class="card-box">
        <div class="card-label">{"3. MEL-SPECTROGRAM" if is_en else "3. МЕЛ-СПЕКТРОГРАММА"}</div>
        <div class="pt"><div class="h">{"2D Perceptual Image" if is_en else "2D-картинка частот"}</div><div class="d">{"Compresses frequencies onto the non-linear Mel scale matching human cochlear biology. Standard input for Whisper." if is_en else "Частоты масштабируются по шкале Mel, имитируя нелинейный слуховой аппарат человека. Основа работы Whisper."}</div></div>
      </div>
      <div class="card-box active" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"4. NEURAL CODEC (EnCodec / DAC)" if is_en else "4. ДИСКРЕТНЫЙ НЕЙРОКОДЕК (DAC / EnCodec)"}</div>
        <div class="pt"><div class="h">{"Discrete Audio Tokens" if is_en else "Токены звука"}</div><div class="d">{"Residual Vector Quantization (RVQ) compresses 48kHz audio into codebooks of integer token IDs (50 tokens/sec)." if is_en else "Остаточное векторное квантование (RVQ) сжимает звук в поток целочисленных токенов (50 токенов/сек)."}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"Key Engineering Concept:" if is_en else "Главный инженерный вывод:"}</b> {"Audio codecs turn continuous sound into <b>discrete tokens</b>, allowing standard Transformer LLMs to generate audio exactly like text!" if is_en else "Нейрокодеки превращают аудио в <b>дискретные токены</b>, благодаря чему обычные LLM могут генерировать звук так же, как текст!"}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>05 / 24</span></div>
  <template class="notes">{"Explain why LLMs couldn't generate audio before codecs. 44.1kHz is too large; EnCodec/DAC compress audio into token streams." if is_en else "Объясняем разницу между аналоговой волной, спектрограммой и современным токенизированным звуком. Это фундамент Suno, Bark и ElevenLabs."}</template>
</section>
""")

    # Slide 6: Whisper STT Architecture
    s.append(f"""
<section class="slide" data-n="6">
  <div class="kicker">{"Speech-to-Text • Foundational Architecture" if is_en else "Распознавание речи • Архитектура STT"}</div>
  <h2 class="title">{"OpenAI Whisper: Encoder-Decoder Transformer for Universal Speech Recognition" if is_en else "OpenAI Whisper: архитектура энкодер-декодер и точные пословные таймкоды"}</h2>
  <p class="lead">{"Whisper processes audio in 30-second windows through a dual-tower Transformer architecture trained on 680,000+ hours of multilingual speech." if is_en else "Whisper обрабатывает звук окнами по 30 секунд через классический двухбашенный трансформер, обученный на 680 000+ часах аудио."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="stack center">
        <div class="card-box" style="border-color:var(--cyan)">
          <div class="card-label">{"WHISPER ARCHITECTURE PIPELINE" if is_en else "АРХИТЕКТУРНЫЙ ПАЙПЛАЙН WHISPER"}</div>
          <div class="pt"><div class="h">{"1. Audio Encoder (Conformer / ViT)" if is_en else "1. Аудио-энкодер (Audio Encoder)"}</div><div class="d">{"80-channel mel-spectrogram ➔ 2 convolutional downsampling layers (4x) ➔ stack of Transformer Encoder self-attention blocks." if is_en else "80-канальная мел-спектрограмма ➔ 2 сверточных слоя со сжатием 4x ➔ блоки внимания Transformer Encoder, извлекающие акустический контекст."}</div></div>
          <div class="pt" style="margin-top:10px;"><div class="h">{"2. Text Decoder (Autoregressive)" if is_en else "2. Текстовый декодер (Text Decoder)"}</div><div class="d">{"Autoregressive decoder with Cross-Attention generates text tokens with task prefix tokens:<br><code>&lt;|startoftranscript|&gt; &lt;|en|&gt; &lt;|transcribe|&gt; &lt;|notimestamps|&gt;</code>" if is_en else "Авторегрессионный декодер с Cross-Attention генерирует слова с управляющими токенами задачи:<br><code>&lt;|startoftranscript|&gt; &lt;|ru|&gt; &lt;|transcribe|&gt; &lt;|notimestamps|&gt;</code>"}</div></div>
        </div>
      </div>
      <div class="stack center">
        <div class="card-box" style="background:var(--surface);">
          <div class="card-label" style="color:var(--green)">{"WORD-LEVEL TIMESTAMPS (FRAME-ACCURATE SUBTITLES)" if is_en else "WORD-LEVEL TIMESTAMPS (СУБТИТРЫ С ТОЧНОСТЬЮ ДО СЛОВА)"}</div>
          <div style="font-size:18px;line-height:1.45;color:var(--muted);">
            {"In <code>word_timestamps=True</code> mode, Whisper analyzes Cross-Attention weights between decoder and encoder to pinpoint the exact millisecond boundaries of each word.<br><br><b>Output:</b> Ready-to-use <code>.srt</code> and <code>.sbv</code> subtitle files for editing suites and YouTube with zero manual timing adjustments." if is_en else "При включении <code>word_timestamps=True</code> Whisper анализирует матрицы внимания (Cross-Attention) декодера к энкодеру, определяя точные тайминги каждого слова.<br><br><b>Результат:</b> Готовые файлы субтитров <code>.srt</code> и <code>.sbv</code> для монтажа и YouTube с точностью до 20 мс без ручной подгонки."}
          </div>
        </div>
        <div class="note"><b>{"2026 Production Standard:" if is_en else "Стандарт 2026 года:"}</b> {"Model <code>whisper-large-v3-turbo</code> (809M parameters, 8x faster than v3 with 99% accuracy) and <code>faster-whisper</code> runtime." if is_en else "Модель <code>whisper-large-v3-turbo</code> (809M параметров, в 8 раз быстрее v3 при сохранении 99% точности) и движок <code>faster-whisper</code>."}</div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>06 / 24</span></div>
  <template class="notes">{"Explain Whisper internals. Encoder takes 30s mel-spectrogram; decoder predicts language token, task token, timestamp tokens, and text tokens." if is_en else "Разбираем архитектуру Whisper. Показываем, как энкодер сжимает 30 секунд звука, а декодер пошагово выводит слова и специальные токены времени."}</template>
</section>
""")

    # Slide 7: Whisper in Production & VAD
    s.append(f"""
<section class="slide" data-n="7">
  <div class="kicker">{"STT Engineering • Production Realities" if is_en else "STT в продакшене • Инженерные сбои и защита"}</div>
  <h2 class="title">{"Whisper in Production: Hallucination Loops, Music Bleed, and Silero VAD" if is_en else "Whisper в проде: петли галлюцинаций в тишине, музыка и связка с Silero VAD"}</h2>
  <p class="lead">{"Raw Whisper fails in silence, music, and long pauses. Production systems wrap Whisper in Voice Activity Detection (VAD) pre-processors." if is_en else "Сырой Whisper дает сбои в длинных паузах, тишине и под музыку. Промышленный стандарт требует Voice Activity Detection (VAD) фильтрации."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="card-box" style="border-color:var(--red)">
        <div class="card-label" style="color:var(--red)">{"RAW WHISPER PRODUCTION FAILURES" if is_en else "ТИПИЧНЫЕ КРАХИ RAW WHISPER В ПРОДАКШЕНЕ"}</div>
        <div class="pt"><div class="h">{"1. Silence Repetition Loops" if is_en else "1. Петли галлюцинаций в тишине (Repetition Loops)"}</div><div class="d">{"When a 30s window contains only silence or room tone, the autoregressive decoder loops endlessly: <i>'Thank you for watching! Please subscribe...'</i>" if is_en else "Когда в 30-секундном окне только тишина или шум микрофона, декодер входит в цикл и генерирует галлюцинации: <i>«Спасибо за просмотр! Ставьте лайк...»</i>"}</div></div>
        <div class="pt" style="margin-top:8px;"><div class="h">{"2. Skipping Speech Under Loud Music" if is_en else "2. Пропуск речи под громким саундтреком"}</div><div class="d">{"Under high BGM volume, Whisper classifies the audio window as non-speech and returns an empty transcript." if is_en else "Если в видео играет музыка, Whisper склонен классифицировать весь отрезок как неречевой и выдает пустую строку."}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--green)">
        <div class="card-label" style="color:var(--green)">{"ENGINEERING FIX: SILERO VAD + CTRANSLATE2" if is_en else "ИНЖЕНЕРНОЕ РЕШЕНИЕ: ПАТТЕРН SILERO VAD + CTRANSLATE2"}</div>
        <div class="pt"><div class="h">{"1. Silero VAD Pre-filtering" if is_en else "1. Предобработка через Silero VAD"}</div><div class="d">{"Lightweight model (1MB) cuts audio strictly along human speech boundaries in 2ms, feeding zero silence into Whisper." if is_en else "Сверхбыстрая модель (1 МБ) нарезает аудио строго по границам речи, отсекая тишину. В Whisper уходят только отрезки с живым голосом."}</div></div>
        <div class="pt" style="margin-top:8px;"><div class="h">{"2. faster-whisper (CTranslate2)" if is_en else "2. Движок faster-whisper (CTranslate2)"}</div><div class="d">{"INT8/FP16 quantization gives <b>4x faster inference</b> and halves VRAM footprint compared to native PyTorch." if is_en else "Оптимизированный C++ рантайм с квантованием INT8/FP16 дает <b>4-кратное ускорение инференса</b> и снижает расход памяти VRAM вдвое."}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"STT Engineering Rule:" if is_en else "Инженерное правило STT:"}</b> {"Never feed long raw audio recordings directly into Whisper without VAD segmentation. 90% of Whisper hallucinations occur in silent intervals." if is_en else "Никогда не подавайте в Whisper длинную запись без VAD-сегментации. 90% галлюцинаций и сбоев таймкодов возникают в пустых паузах."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>07 / 24</span></div>
  <template class="notes">{"Explain why companies complain about Whisper hallucinations. It's an autoregressive decoder! In silence it hallucinates common dataset end-tokens. Solution: VAD." if is_en else "Учим продакшн-надежности. Объясняем феномен галлюцинаций в тишине: декодер обязан выводить токены, и цепляется за паттерны из обучающего корпуса (YouTube outros)."}</template>
</section>
""")

    # Slide 8: TTS Landscape 2026
    s.append(f"""
<section class="slide" data-n="8">
  <div class="kicker">{"Text-to-Speech • Model Landscape 2026" if is_en else "Синтез речи • Ландшафт движков 2026"}</div>
  <h2 class="title">{"Text-to-Speech (TTS): Studio Quality, Low Latency, and Open Weights" if is_en else "Text-to-Speech (TTS): студийное качество, ультра-низкая задержка и открытые веса"}</h2>
  <p class="lead">{"The TTS market is divided into four architectural tiers based on latency, emotional control, and hosting requirements." if is_en else "Рынок речевых моделей разделен на 4 инженерных класса по критериям задержки, эмоционального контроля и размещения."}</p>
  <div class="body">
    <div class="row c4">
      <div class="card-box">
        <div class="card-label">{"TIER 1 • STUDIO CLOUD" if is_en else "КЛАСС 1 • СТУДИЙНЫЕ ОБЛАКА"}</div>
        <div class="pt"><div class="h">ElevenLabs Multilingual v2</div><div class="d"><b>{"Focus:" if is_en else "Фокус:"}</b> {"Maximum emotional nuance, audiobooks, movie dubbing, 32+ languages. Highest fidelity, ~350ms TTFT." if is_en else "Максимальная эмоциональная выразительность, дубляж кино, аудиокниги. 32+ языка, TTFT ~350 мс."}</div></div>
      </div>
      <div class="card-box active" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"TIER 2 • CONVERSATIONAL AGENTS" if is_en else "КЛАСС 2 • РЕЧЕВЫЕ АГЕНТЫ"}</div>
        <div class="pt"><div class="h">Cartesia Sonic / PlayHT 2.0</div><div class="d"><b>{"Focus:" if is_en else "Фокус:"}</b> {"Ultra-low latency: <b>135ms Time-to-First-Audio-Byte</b>. State-space architecture designed for real-time live phone dialogs." if is_en else "Ультра-низкая задержка: <b>135 мс до первого байта звука</b>. Архитектура State-Space для живых телефонных диалогов."}</div></div>
      </div>
      <div class="card-box">
        <div class="card-label">{"TIER 3 • OPEN-SOURCE EDGE" if is_en else "КЛАСС 3 • ОТКРЫТЫЙ EDGE-ИНФЕРЕНС"}</div>
        <div class="pt"><div class="h">Kokoro-82M / Chatterbox</div><div class="d"><b>{"Focus:" if is_en else "Фокус:"}</b> {"Compact 82M parameter model, Apache 2.0. Runs in browser via WebAssembly or on CPU with zero cloud costs." if is_en else "Компактная модель на 82M параметров (Apache 2.0). Работает прямо в браузере через WASM или на CPU за $0 облачных затрат."}</div></div>
      </div>
      <div class="card-box">
        <div class="card-label">{"TIER 4 • PARALINGUISTIC EXPERIMENTAL" if is_en else "КЛАСС 4 • НЕВЕРБАЛЬНАЯ РЕЧЬ"}</div>
        <div class="pt"><div class="h">Suno Bark / AudioCraft</div><div class="d"><b>{"Focus:" if is_en else "Фокус:"}</b> {"Autoregressive synthesis capable of laughs, sighs, throat clears, crying, and spontaneous human stammering." if is_en else "Авторегрессионные сети, способные генерировать смех, вздохи, кашель, плач и запинки живой человеческой речи."}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"Architectural Decision Rule:" if is_en else "Правило выбора архитектуры:"}</b> {"For marketing videos and YouTube dubbing — ElevenLabs. For interactive phone/WebRTC agents — Cartesia Sonic. For offline privacy on client devices — Kokoro." if is_en else "Для видеорекламы и дубляжа YouTube — ElevenLabs. Для интерактивных голосовых агентов по телефону — Cartesia. Для приватного локального инференса — Kokoro."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>08 / 24</span></div>
  <template class="notes">{"Walk through the 4 tiers. Emphasize that latency (Cartesia) and emotional nuance (ElevenLabs) represent different engineering trade-offs." if is_en else "Сравниваем 4 класса. Подчеркиваем: борьба за задержку (Cartesia) и борьба за кинематографичность (ElevenLabs) требуют разных подходов."}</template>
</section>
""")

    # Slide 9: Expressive Prompting & Steering
    s.append(f"""
<section class="slide" data-n="9">
  <div class="kicker">{"Prompt Engineering • Speech Directing" if is_en else "Промптинг речи • Режиссура голоса"}</div>
  <h2 class="title">{"Expressive Voice Prompting: Punctuation Pacing, SSML, and Stability Sliders" if is_en else "Управление выразительностью: пунктуационные паузы, SSML и ползунки Stability"}</h2>
  <p class="lead">{"In modern TTS, text formatting serves as musical notation for the neural acoustic decoder." if is_en else "В современных TTS пунктуация и разметка работают как нотная партитура для нейросетевого декодера."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="card-box">
        <div class="card-label">{"PUNCTUATION & PHONETIC NOTATION" if is_en else "СИНТАКСИЧЕСКАЯ И ФОНЕТИЧЕСКАЯ РАЗМЕТКА"}</div>
        <div class="pt"><div class="h">{"1. Micro-Pauses & Cadence" if is_en else "1. Микро-паузы и темп"}</div><div class="d">{"Ellipses (<code>...</code>) inject a natural breath intake. Em-dashes (<code>—</code>) create a suspenseful pause. Capitalization triggers vocal emphasis and pitch spikes." if is_en else "Многоточия (<code>...</code>) заставляют модель сделать естественный вдох. Длинные тире (<code>—</code>) создают интонационную паузу. Заглавные буквы поднимают тон."}</div></div>
        <div class="pt" style="margin-top:10px;"><div class="h">{"2. SSML & Phoneme Tags" if is_en else "2. Теги SSML и ударения"}</div><div class="d">{"Use IPA markup for tricky brand names:<br><code>&lt;phoneme alphabet=\"ipa\" ph=\"kwɪz\"&gt;cuisse&lt;/phoneme&gt;</code><br>Or insert strict silence: <code>&lt;break time=\"600ms\"/&gt;</code>" if is_en else "Фонетическая транскрипция для сложных терминов и брендов:<br><code>&lt;phoneme alphabet=\"ipa\" ph=\"ɡloʊvoʊ\"&gt;Glovo&lt;/phoneme&gt;</code><br>Фиксация точной паузы: <code>&lt;break time=\"600ms\"/&gt;</code>"}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"VOICE STEERING SLIDERS (ELEVENLABS PARAMETERS)" if is_en else "ПАРАМЕТРЫ УПРАВЛЕНИЯ ГОЛОСОМ (ELEVENLABS)"}</div>
        <div class="pt"><div class="h">{"Stability (0.0 — 1.0)" if is_en else "Stability (0.0 — 1.0)"}</div><div class="d">{"<b>Low (0.30):</b> High emotional variability, dramatic acting, whispered lines.<br><b>High (0.85):</b> Consistent corporate delivery, zero voice crack, strict FAQ reading." if is_en else "<b>Низкая (0.30):</b> Высокая эмоциональная вариативность, драматизм, шепот.<br><b>Высокая (0.85):</b> Монотонная стабильность, подходит для банковских FAQ и навигаторов."}</div></div>
        <div class="pt" style="margin-top:10px;"><div class="h">{"Similarity Boost & Style Exaggeration" if is_en else "Similarity Boost и Style Exaggeration"}</div><div class="d">{"<b>Similarity (0.75):</b> Matches reference speaker timbre without amplifying background room noise.<br><b>Style (0.15):</b> Adds subtle theatrical energy without audio distortion." if is_en else "<b>Similarity (0.75):</b> Точное соответствие референсному голосу без захвата шума комнаты.<br><b>Style (0.15):</b> Добавляет энергию диктора без паразитных искажений."}</div></div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>09 / 24</span></div>
  <template class="notes">{"Show how writing for TTS differs from writing for reading. You must punctuate for breath!" if is_en else "Показываем студентам разницу между текстом для чтения глазами и текстом для TTS. Текст для синтеза нужно размечать дыханием!"}</template>
</section>
""")

    # Slide 10: Voice Cloning
    s.append(f"""
<section class="slide" data-n="10">
  <div class="kicker">{"Voice Cloning • Engineering Methodologies" if is_en else "Клонирование голоса • Технологические уровни"}</div>
  <h2 class="title">{"Voice Cloning: Instant (Zero-Shot) vs Professional Fine-Tuning" if is_en else "Клонирование голоса: мгновенное (Zero-Shot) против профессионального студийного"}</h2>
  <p class="lead">{"Voice cloning operates on two fundamentally different architectures: dynamic reference embedding vs deep parameter adaptation." if is_en else "Клонирование голоса работает на двух принципиально разных принципах: динамический векторный эмбеддинг против файн-тюнинга весов."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="card-box">
        <div class="card-label">{"INSTANT VOICE CLONING (IVC • ZERO-SHOT)" if is_en else "МГНОВЕННОЕ КЛОНИРОВАНИЕ (INSTANT • ZERO-SHOT)"}</div>
        <div class="pt"><div class="h">{"1 Minute of Reference Audio" if is_en else "1 минута аудио • Эмбеддинг тембра"}</div><div class="d">{"<b>Mechanism:</b> Speaker verification encoder extracts a 512-dimensional d-vector (speaker embedding) conditioning the base TTS model in real-time." if is_en else "<b>Механика:</b> Энкодер извлекает 512-мерный d-вектор спикера, который динамически подмешивается в базовую модель при генерации."}</div></div>
        <div class="pt" style="margin-top:8px;"><div class="h">{"Pros & Cons" if is_en else "Плюсы и минусы"}</div><div class="d">{"⚡ Ready in 5 seconds. $0 training cost.<br>⚠️ Fidelity ~75–80%. Replicates background hiss and room reverb. Flat emotional dynamic range." if is_en else "⚡ Готово за 5 секунд, $0 затрат на обучение.<br>⚠️ Сходство ~75–80%. Захватывает комнатное эхо и шумы микрофона. Узкий эмоциональный диапазон."}</div></div>
      </div>
      <div class="card-box active" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"PROFESSIONAL VOICE CLONING (PVC • FULL FINE-TUNING)" if is_en else "ПРОФЕССИОНАЛЬНОЕ КЛОНИРОВАНИЕ (PROFESSIONAL PVC)"}</div>
        <div class="pt"><div class="h">{"30–60 Minutes of Studio Stems" if is_en else "30–60 минут студийных записей • Дообучение весов"}</div><div class="d">{"<b>Mechanism:</b> Dedicated LoRA / weight fine-tuning run on cloud GPUs over phonetically balanced multi-emotional datasets." if is_en else "<b>Механика:</b> Полноценный файн-тюнинг весов модели (LoRA) на GPU по фонетически сбалансированному корпусу записей."}</div></div>
        <div class="pt" style="margin-top:8px;"><div class="h">{"Pros & Cons" if is_en else "Плюсы и минусы"}</div><div class="d">{"🏆 Studio 98% fidelity. Full dynamic range (whisper to projection). Natural micro-prosody.<br>⏳ Requires 2–4 hours GPU training and strict studio acoustic isolation." if is_en else "🏆 Студийная идентичность 98%. Полный динамический диапазон (от шепота до крика).<br>⏳ Требует 2–4 часа обучения на GPU и стерильных условий студийной записи."}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"Production Rule:" if is_en else "Инженерное правило:"}</b> {"Never use Instant Cloning for high-profile customer interfaces. Noise in the sample degrades synthetic prosody across every downstream call." if is_en else "Никогда не используйте Instant Cloning для фронт-линии брендов. Любой микрофонный шум референса навечно въедается во все синтезированные фразы."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>10 / 24</span></div>
  <template class="notes">{"Differentiate Instant vs Pro cloning. Explain speaker embeddings (d-vectors) vs neural parameter fine-tuning." if is_en else "Разбираем математику d-векторов против дообучения весов нейросети. Объясняем, почему плохой микрофон портит мгновенный клон."}</template>
</section>
""")

    # Slide 11: Security & Watermarking
    s.append(f"""
<section class="slide" data-n="11">
  <div class="kicker">{"AI Safety & Governance • Acoustic Forensics" if is_en else "Безопасность и защита • Акустическая криминалистика"}</div>
  <h2 class="title">{"Voice Security, Anti-Spoofing, and Imperceptible Audio Watermarking" if is_en else "Безопасность синтеза: защита от дипфейков, Voice Captcha и скрытый вотермаркинг"}</h2>
  <p class="lead">{"Cloned voices present severe social engineering risks. Modern voice platforms enforce explicit consent verification and cryptographic watermarks." if is_en else "Голосовые дипфейки несут риски финансового мошенничества. Современные платформы внедряют проверку согласия и акустические водяные знаки."}</p>
  <div class="body">
    <div class="row c3">
      <div class="card-box" style="border-color:var(--red)">
        <div class="card-label" style="color:var(--red)">{"THREAT VECTORS 2026" if is_en else "ВЕКТОРЫ УГРОЗ 2026"}</div>
        <div class="pt"><div class="h">{"CEO Fraud & Biometric Bypass" if is_en else "CEO-Fraud и взлом биометрии"}</div><div class="d">{"• Spoofing banking voice authentication.<br>• Real-time phone scams mimicking family members.<br>• Disinformation and fabricated audio evidence." if is_en else "• Обход голосовой аутентификации в банках.<br>• Телефонный фишинг голосами близких.<br>• Фальсификация аудиозаписей в суде и медиа."}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--amber)">
        <div class="card-label" style="color:var(--amber)">{"DYNAMIC VOICE CAPTCHA" if is_en else "ДИНАМИЧЕСКИЙ VOICE CAPTCHA"}</div>
        <div class="pt"><div class="h">{"Live Consent Verification" if is_en else "Верификация согласия спикера"}</div><div class="d">{"Before activating a custom voice clone, the speaker must read a randomized one-time verification script on camera or live mic to prove active consent." if is_en else "Перед активацией клона спикер обязан зачитать с микрофона сгенерированный одноразовый текст. Запрет клонирования третьих лиц по слитым записям."}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--green)">
        <div class="card-label" style="color:var(--green)">{"IN-BAND WATERMARKING" if is_en else "АКУСТИЧЕСКИЕ ВОДЯНЫЕ ЗНАКИ"}</div>
        <div class="pt"><div class="h">{"SynthID Audio & PerTh" if is_en else "Google SynthID и PerTh"}</div><div class="d">{"Google SynthID for Audio embeds imperceptible mathematical frequency shifts into the audio spectrum that survive MP3 compression, filtering, and room reverb." if is_en else "Технологии Google SynthID for Audio и ElevenLabs PerTh вшивают микроскопический фазовый паттерн в звук, устойчивый к MP3-сжатию и шумам."}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"C2PA Audio Provenance:" if is_en else "Стандарт C2PA для аудио:"}</b> {"Open metadata standard cryptographically signing audio containers, guaranteeing origin traceability from creation to playback." if is_en else "Открытый стандарт метаданных криптографически подписывает аудиофайл, гарантируя прозрачную историю генерации."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>11 / 24</span></div>
  <template class="notes">{"Address ethics head-on. Explain that responsible AI engineers always implement consent verification and watermarking." if is_en else "Обсуждаем этику и безопасность. Инженер GenAI обязан знать механизмы криминалистической верификации звука."}</template>
</section>
""")

    # Slide 12: Blast Radius
    s.append(f"""
<section class="slide" data-n="12">
  <div class="kicker">{"Risk Architecture • Traffic Light Framework" if is_en else "Архитектура рисков • Светофор Blast Radius"}</div>
  <h2 class="title">{"Blast Radius Governance: Traffic Light Boundaries for Audio AI" if is_en else "Матрица Blast Radius: границы автономности в генеративном аудио"}</h2>
  <p class="lead">{"Define strict architectural boundaries before deploying speech generation models into enterprise infrastructure." if is_en else "Четкое разделение сценариев применения генеративного звука по уровню допустимого риска."}</p>
  <div class="body">
    <div class="row c3">
      <div class="card-box" style="border-color:var(--green)">
        <div class="card-label" style="color:var(--green)">{"GREEN ZONE • AUTONOMOUS" if is_en else "ЗЕЛЕНАЯ ЗОНА • АВТОНОМНО"}</div>
        <div class="pt"><div class="h">{"Zero Harm Potential" if is_en else "Нулевой потенциал ущерба"}</div><div class="d">{"• Foley sound effects and background ambient noises.<br>• Authorized creator video dubbing (Creator Tools case).<br>• Internal synthetic voiceover drafts for internal presentations." if is_en else "• Фоли-шумы окружения и спецэффекты.<br>• Авторизованный перевод авторских видео (кейс Creator Tools).<br>• Черновые начитки презентаций и образовательных демо."}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--amber)">
        <div class="card-label" style="color:var(--amber)">{"YELLOW ZONE • HUMAN-IN-THE-LOOP" if is_en else "ЖЕЛТАЯ ЗОНА • HUMAN-IN-THE-LOOP"}</div>
        <div class="pt"><div class="h">{"Strict Oversight Required" if is_en else "Контроль и дисклеймеры"}</div><div class="d">{"• Automated phone customer support bots (mandatory audio disclosure: <i>'You are speaking with an AI assistant'</i>).<br>• Commercial product advertisements (sound engineer audit before release)." if is_en else "• Голосовые боты первой линии поддержки (обязательный дисклеймер: <i>«С вами говорит виртуальный ассистент»</i>).<br>• Коммерческая реклама брендов (аудит звукорежиссера)."}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--red)">
        <div class="card-label" style="color:var(--red)">{"RED ZONE • ABSOLUTELY FORBIDDEN" if is_en else "КРАСНАЯ ЗОНА • КАТЕГОРИЧЕСКИЙ ЗАПРЕТ"}</div>
        <div class="pt"><div class="h">{"Zero Direct Execution" if is_en else "Криминальный риск"}</div><div class="d">{"• Cloning voices of living persons without legally executed written consent.<br>• Automated synthesis of emergency 911 calls or regulatory notices.<br>• Fabricating evidence or executive announcements." if is_en else "• Клонирование голосов живых людей без юридического согласия.<br>• Автоматическая генерация экстренных оповещений от властей.<br>• Обход систем биометрической аутентификации."}</div></div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>12 / 24</span></div>
  <template class="notes">{"Enforce the traffic light boundaries. Compliance rule: never synthesize third-party voices without signed consent." if is_en else "Закрепляем светофор рисков. Напоминаем корпоративные стандарты EPAM и международное регулирование AI Act."}</template>
</section>
""")

    # Slide 13: Voice Conversion & Multilingual Dubbing
    s.append(f"""
<section class="slide" data-n="13">
  <div class="kicker">{"Speech-to-Speech • Global Localization" if is_en else "Speech-to-Speech • Глобальный дубляж"}</div>
  <h2 class="title">{"Voice Conversion & Multilingual Dubbing: 1 Click to 100+ Languages" if is_en else "Мультиязычный дубляж и Speech-to-Speech: 1 клик на 100+ языков"}</h2>
  <p class="lead">{"Speech-to-Speech (STS) swaps language while preserving the original speaker's timbre, cadence, and vocal acting (Creator Tools Case)." if is_en else "Speech-to-Speech (STS) заменяет язык речи, сохраняя уникальный тембр, дыхание и актерскую подачу оригинального спикера."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="card-box" style="border-color:var(--cyan)">
        <div class="card-label">{"END-TO-END DUBBING PIPELINE (CREATOR TOOLS ARCHITECTURE)" if is_en else "АРХИТЕКТУРА СКВОЗНОГО ДУБЛЯЖА (CREATOR TOOLS)"}</div>
        <div class="pt"><div class="h">{"1. Whisper STT + Word Align" if is_en else "1. Whisper STT + пословный тайминг"}</div><div class="d">{"Extract words, exact timestamps, and breathing pauses from original audio." if is_en else "Извлечение исходного текста, тайм-кодов каждого слова и пауз дыхания."}</div></div>
        <div class="pt" style="margin-top:8px;"><div class="h">{"2. LLM Translation with Syllable Budget" if is_en else "2. LLM-перевод с ограничением по слогам"}</div><div class="d">{"German/Russian requires ~25% more syllables than English. Prompt instructs LLM to compress grammar to fit exact target durations." if is_en else "Немецкий/русский длиннее английского на ~25%. LLM переводит с жестким ограничением длины фразы под хронометраж."}</div></div>
        <div class="pt" style="margin-top:8px;"><div class="h">{"3. STS Timbre Transfer + Elastic Time-Stretch" if is_en else "3. STS-синтез тембра + эластичный стретчинг"}</div><div class="d">{"Target voice synthesized with original actor timbre. Micro-timing fitted via Phase Vocoder without pitch shifting." if is_en else "Синтез голоса в тембре автора. Микро-подгонка фазовым вокодером без изменения высоты тона."}</div></div>
      </div>
      <div class="card-box" style="background:var(--surface);">
        <div class="card-label" style="color:var(--green)">{"REAL-WORLD CREATOR TOOLS IMPACT" if is_en else "РЕАЛЬНЫЙ ЭФФЕКТ В CREATOR TOOLS"}</div>
        <div style="font-size:18px;line-height:1.45;color:var(--muted);">
          В проекте Creator Tools этот пайплайн переводит YouTube-ролики на 100+ языков с автоматической синхронизацией субтитров <code>.sbv</code>.<br><br>
          <b>Результат:</b> YouTube-каналы выходят на международный трафик (Латинская Америка, Азия, Европа) с нулевыми затратами на студии дубляжа.
        </div>
        <div class="note" style="margin-top:16px;"><b>Технологический ключ:</b> Сохранение тембра спикера дает зрителю ощущение, что автор лично говорит на его родном языке.</div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>13 / 24</span></div>
  <template class="notes">{"Explain the engineering elegance of speech-to-speech. Highlight the syllabus constraint in LLM translation." if is_en else "Показываем реальный кейс Creator Tools. Объясняем, почему прямой машинный перевод не ложится на видео без контроля слогов."}</template>
</section>
""")

    # Slide 14: Midpoint Break
    s.append(f"""
<section class="slide" data-n="14">
  <div class="kicker">{"Midpoint Break • Cognitive Reset" if is_en else "Экватор занятия • Когнитивная перезагрузка"}</div>
  <h2 class="title">{"5-Minute Coffee Break: Reset Your Ears and Mind" if is_en else "Перерыв 5 минут: отдых слуха и перезагрузка внимания"}</h2>
  <p class="lead">{"Generative audio requires intense acoustic listening. Step away from the screen, grab fresh water, and stretch." if is_en else "Восприятие звука требует предельной слуховой концентрации. Отойдите от монитора, выпейте воды и передохните."}</p>
  <div class="body">
    <div class="stack center" style="align-items:center;gap:28px;">
      <div style="font-family:var(--mono);font-size:84px;font-weight:700;color:var(--cyan);letter-spacing:.05em;" id="timer-display">05:00</div>
      <div style="display:flex;gap:16px;">
        <button id="timer-btn" style="background:var(--cyan);color:#0b0f17;font-family:var(--mono);font-weight:700;font-size:18px;border:none;border-radius:8px;padding:12px 28px;cursor:pointer;">{"START 5 MIN" if is_en else "СТАРТ 5 МИН"}</button>
        <button id="timer-reset" style="background:var(--surface);color:var(--fg);border:1px solid var(--line);font-family:var(--mono);font-size:18px;border-radius:8px;padding:12px 24px;cursor:pointer;">{"RESET" if is_en else "СБРОС"}</button>
      </div>
      <div class="card-box" style="max-width:800px;text-align:center;">
        <div class="card-label" style="color:var(--amber)">{"COMING UP IN PART TWO" if is_en else "ВО ВТОРОЙ ПОЛОВИНЕ ЗАНЯТИЯ"}</div>
        <div style="font-size:19px;color:var(--muted);line-height:1.4;">
          {"Foley Sound Effects (SFX AI) ➔ Creator Tools Giant Stories Audio Matrices ➔ AI Music Generation (Suno v4) ➔ Multi-Stem Assembly in Python ➔ Real-Time Voice Agents Architecture." if is_en else "Генерация фоли-шумов (SFX AI) ➔ Звуковые матрицы Creator Tools Giant Stories ➔ Генерация музыки (Suno v4) ➔ Сведение мультитрека в Python ➔ Архитектура голосовых агентов."}
        </div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>14 / 24</span></div>
  <template class="notes">{"Strictly a 5-minute break. Do not solicit routine tasks in chat. Let students rest before diving into Foley, music, and agents." if is_en else "Строго 5 минут отдыха. Не задаем вопросов в чат, даем аудитории отдохнуть. Проверяем Colab и вкладки Suno/ElevenLabs."}</template>
</section>
""")

    # Slide 15: Sound Effects (SFX AI)
    s.append(f"""
<section class="slide" data-n="15">
  <div class="kicker">{"Foley & Sound Design • SFX Diffusion" if is_en else "Шумы и саунд-дизайн • Диффузия звуковых эффектов"}</div>
  <h2 class="title">{"Sound Effects (SFX AI): Generating Foley and Physical Acoustics" if is_en else "Sound Effects (SFX AI): генерация фоли-шумов и физической акустики"}</h2>
  <p class="lead">{"Modern audio diffusion models generate bespoke sound effects directly from text prompts, replacing legacy static stock libraries." if is_en else "Диффузионные аудионетросети генерируют предметные шумы по текстовому описанию, заменяя библиотеки стоковых сэмплов."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="card-box" style="border-color:var(--cyan)">
        <div class="card-label">{"THE 3-SLOT FOLEY PROMPT FORMULA" if is_en else "3-СЛОТОВАЯ ФОРМУЛА ПРОМПТА FOLEY"}</div>
        <div class="pt"><div class="h">{"[Source] + [Kinetic Action] + [Acoustic Space]" if is_en else "[Источник] + [Кинетическое действие] + [Акустика пространства]"}</div><div class="d">{"<b>Slot 1: Sound Source</b> — Exact physical materials (rubber tire, brass key, oak floor).<br><b>Slot 2: Kinetic Action</b> — Speed, energy, impact (splashes violently, scrapes, clicks).<br><b>Slot 3: Acoustic Space</b> — Room reverb, distance, environment (narrow wet alleyway, vault echo)." if is_en else "<b>Слот 1: Физический источник</b> — Точный материал предметов (резина, латунь, мокрый гравий).<br><b>Слот 2: Кинетика действия</b> — Сила, ускорение, характер удара (резко врезается, плавно катится).<br><b>Слот 3: Пространство</b> — Реверберация помещения (эхо каменного подвала, открытая улица)."}</div></div>
      </div>
      <div class="card-box" style="background:var(--surface);">
        <div class="card-label" style="color:var(--green)">{"PROVEN BENCHMARK PROMPTS (ELEVENLABS SFX / STABLE AUDIO)" if is_en else "ЭТАЛОННЫЕ ПРИМЕРЫ (ELEVENLABS SFX / STABLE AUDIO)"}</div>
        <div class="pt"><div class="h">{"Bicycle in Rain (Glovo Courier):" if is_en else "Велосипед под дождем (Курьер Glovo):"}</div><div class="d"><code>"Bicycle tires splashing rapidly through a deep rainwater puddle on wet cobblestone, fine water spray, quiet evening city background hum, 24fps cinema sync"</code></div></div>
        <div class="pt" style="margin-top:12px;"><div class="h">{"Espresso Pour (Packshot Mug):" if is_en else "Кофейный пэкшот (Кружка):"}</div><div class="d"><code>"Hot rich espresso pouring continuously into a thick ceramic mug, subtle bubbling crema froth, delicate steam hiss, close-up stereo microphone"</code></div></div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>15 / 24</span></div>
  <template class="notes">{"Explain the 3-slot formula. Sound design requires materials, kinetic action, and room acoustics." if is_en else "Разбираем 3-слотовую формулу фоли. Звукорежиссеру нужны: материал, кинетика удара и геометрия комнаты."}</template>
</section>
""")

    # Slide 16: Storyboard Audio Integration
    s.append(f"""
<section class="slide" data-n="16">
  <div class="kicker">{"Studio Case Study • Creator Tools Giant Stories" if is_en else "Студийный кейс • Creator Tools Giant Stories"}</div>
  <h2 class="title">{"Multi-Shot Audio Alignment: The Creator Tools Sound Matrix" if is_en else "Звуковой дизайн сториборда: продакшн-матрица Creator Tools"}</h2>
  <p class="lead">{"In the 10-episode <i>Giant Stories</i> R&D series, every 5-second video cut was pre-engineered with dedicated Foley layers and musical hooks." if is_en else "В 10-серийном цикле <i>Giant Stories</i> каждый 5-секундный шот заранее проектировался с парными слоями фоли и музыкальных акцентов."}</p>
  <div class="body">
    <table class="t">
      <thead>
        <tr>
          <th>{"Shot & Duration" if is_en else "Шот и хронометраж"}</th>
          <th>{"Key Visual (L05)" if is_en else "Визуал кадра (L05)"}</th>
          <th>{"Voiceover Line" if is_en else "Закадровый голос"}</th>
          <th>{"Foley SFX Layer (Prompt)" if is_en else "Фоли-слой SFX (Промпт)"}</th>
          <th>{"Music Underscore Hook" if is_en else "Музыкальный хук"}</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><b>{"01. Sealed Crate" if is_en else "01. Опечатанный ящик"}</b> (5s)</td>
          <td>{"Customs vault, pine crate PECOS 1423" if is_en else "Подвал таможни, ящик PECOS 1423"}</td>
          <td><i>{"“Sealed in 1929 — unopened since...”" if is_en else "«Опечатан в 1929 году — с тех пор не открывался...»"}</i></td>
          <td><code>"Distant vault hum, water dripping on concrete, rat scuttle"</code></td>
          <td>{"Bowed bass drone, muted brass" if is_en else "Низкий бас-дрон, приглушенная медь"}</td>
        </tr>
        <tr>
          <td><b>{"02. Drill Strike" if is_en else "02. Буровой бур"}</b> (5s)</td>
          <td>{"Oil drillers hit bone at noon" if is_en else "Буровики натыкаются на кость"}</td>
          <td><i>{"“Struck something harder than granite...”" if is_en else "«Наткнулись на нечто тверже гранита...»"}</i></td>
          <td><code>"Cicadas buzz, heavy shovel scrapes stone, gasping breath"</code></td>
          <td>{"Sub-bass pulse every 2s" if is_en else "Пульсирующий суб-бас каждые 2 сек"}</td>
        </tr>
        <tr>
          <td><b>{"03. Rotary Press" if is_en else "03. Ротационный пресс"}</b> (5s)</td>
          <td>{"Printing press headlines" if is_en else "Печатные станки типографии"}</td>
          <td><i>{"“Papers screamed of an 11-foot titan...”" if is_en else "«Газеты кричали о 4-метровом титане...»"}</i></td>
          <td><code>"Rotary press clatter, wet ink hiss, mechanical stamp thud"</code></td>
          <td>{"Rising string tremolo" if is_en else "Нарастающее тремоло струнных"}</td>
        </tr>
        <tr>
          <td><b>{"04. Refusal Letter" if is_en else "04. Письмо с отказом"}</b> (5s)</td>
          <td>{"Clerk typing denial letter" if is_en else "Клерк за пишущей машинкой"}</td>
          <td><i>{"“The Smithsonian swore it never arrived...”" if is_en else "«Институт заявил, что груз так и не прибыл...»"}</i></td>
          <td><code>"Typewriter key clack, carriage bell, banker lamp electrical buzz"</code></td>
          <td>{"Solo cello mourning motif" if is_en else "Соло виолончели, тиканье часов"}</td>
        </tr>
      </tbody>
    </table>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"Key Production Takeaway:" if is_en else "Главный вывод продакшена:"}</b> {"Never generate sound as an afterthought. Aligning SFX and musical cues at the storyboard stage eliminates 90% of editing friction." if is_en else "Звук нельзя оставлять «на потом». Прописывание фоли-слоев на этапе сториборда устраняет 90% проблем при финальном монтаже."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>16 / 24</span></div>
  <template class="notes">{"Walk through the table from Creator Tools. Point out how specific SFX textures (rust, typewriter, ink) match exact visual beats." if is_en else "Показываем реальную матрицу из Creator Tools. Обращаем внимание, как текстуры шума (типография, машинка, ящик) идеально ложатся на картинку."}</template>
</section>
""")

    # Slide 17: AI Music Generation
    s.append(f"""
<section class="slide" data-n="17">
  <div class="kicker">{"Music AI • State of the Art 2026" if is_en else "Генерация музыки • Модели и платформы 2026"}</div>
  <h2 class="title">{"AI Music Generation: Suno v4, Udio 1.5, and Instrumental Soundtracks" if is_en else "Генерация музыки: Suno v4, Udio 1.5 и инструментальные саундтреки"}</h2>
  <p class="lead">{"Music foundation models generate full 3-to-4-minute stereo arrangements with coherent harmonies, solos, and structural sections." if is_en else "Музыкальные диффузионные модели генерируют полноценные 3-4 минутные треки со сложной гармонией, инструменталом и аранжировкой."}</p>
  <div class="body">
    <div class="row c3">
      <div class="card-box">
        <div class="card-label">{"SUNO V4 ARCHITECTURE" if is_en else "ВОЗМОЖНОСТИ SUNO V4"}</div>
        <div class="pt"><div class="h">{"Stereo 48kHz Production" if is_en else "Студийный стереозвук 48 кГц"}</div><div class="d">{"• High dynamic range and acoustic depth.<br>• <b>Instrumental Toggle:</b> Eliminates vocal bleed for pure video background music.<br>• <b>Extend Audio:</b> Seamlessly adds 30s intros, bridges, or cinematic outros." if is_en else "• Высокий динамический диапазон.<br>• <b>Тумблер Instrumental:</b> Полное отключение вокала для фонового саундтрека видео.<br>• <b>Extend Audio:</b> Доращивание вступительных интро и завершающих аутро."}</div></div>
      </div>
      <div class="card-box">
        <div class="card-label">{"UDIO 1.5 ARCHITECTURE" if is_en else "ВОЗМОЖНОСТИ UDIO 1.5"}</div>
        <div class="pt"><div class="h">{"Surgical Arrangement Control" if is_en else "Хирургический контроль трека"}</div><div class="d">{"• Advanced prompt strength sliders.<br>• <b>Audio Inpainting:</b> Select and regenerate any 10-second segment without altering the rest of the song.<br>• Extreme genre-bending and complex jazz harmony." if is_en else "• Тонкая настройка ползунков креативности.<br>• <b>Audio Inpainting:</b> Перегенерация неудачного 10-секундного соло без изменения остального трека.<br>• Сложные джазовые и кинематографические гармонии."}</div></div>
      </div>
      <div class="card-box active" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"STEM SEPARATION (SPLIT TRACKS)" if is_en else "РАЗДЕЛЕНИЕ НА СТЕМЫ (STEM SPLITTING)"}</div>
        <div class="pt"><div class="h">{"Vocals, Drums, Bass, Other" if is_en else "4 изолированные дорожки"}</div><div class="d">{"Neural stem separators (Demucs v4) split generated songs into 4 isolated WAV files: drums, bass, vocals, and instruments, allowing custom volume balancing." if is_en else "Нейросети разделения (Demucs v4) разбивают трек на 4 чистые WAV-дорожки: барабаны, бас, инструменты и вокал для раздельного сведения."}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"Soundtrack Rule:" if is_en else "Инженерное правило саундтрека:"}</b> {"Always toggle <b>Instrumental</b> for video soundtracks. Vocals in the music track clash with the voiceover and destroy dialogue intelligibility." if is_en else "Для видео всегда включайте режим <b>Instrumental</b>. Любой вокал в музыке вступает в частотный конфликт с диктором и ломает разборчивость речи."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>17 / 24</span></div>
  <template class="notes">{"Explain Suno and Udio. Emphasize why Instrumental mode and Stem Separation are essential for video editors." if is_en else "Разбираем Suno и Udio. Объясняем, почему видеомонтажеру нужен только инструментал или разделенные стемы."}</template>
</section>
""")

    # Slide 18: Music Prompt Architecture
    s.append(f"""
<section class="slide" data-n="18">
  <div class="kicker">{"Music Prompting • Structural Notation" if is_en else "Музыкальный промптинг • Архитектура партитуры"}</div>
  <h2 class="title">{"Music Prompt Architecture: The 5-Slot Score and Structural Tags" if is_en else "Архитектура музыкального промпта: 5 слотов и теги структуры"}</h2>
  <p class="lead">{"Directing an AI music model requires specifying genre, tempo, instruments, mood, and explicit structural section tags." if is_en else "Управление музыкальной моделью строится на 5 слотах описания стиля и тегах разметки композиции."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="card-box">
        <div class="card-label">{"THE 5-SLOT MUSIC PROMPT FORMULA" if is_en else "5-СЛОТОВАЯ ФОРМУЛА МУЗЫКАЛЬНОГО ПРОМПТА"}</div>
        <div class="pt"><div class="h">{"1. Primary Genre" if is_en else "1. Основной жанр"}</div><div class="d">{"e.g., <code>Cinematic neo-classical ambient</code>, <code>Lo-fi hip-hop chillhop</code>." if is_en else "например, <code>Cinematic neo-classical ambient</code>, <code>Lo-fi hip-hop chillhop</code>."}</div></div>
        <div class="pt" style="margin-top:8px;"><div class="h">{"2. Tempo & BPM" if is_en else "2. Темп и метр (BPM)"}</div><div class="d">{"e.g., <code>Slow 72 BPM</code>, <code>128 BPM driving pulse</code>, <code>triplet swing rhythm</code>." if is_en else "например, <code>Slow 72 BPM</code>, <code>128 BPM driving pulse</code>, <code>triplet swing rhythm</code>."}</div></div>
        <div class="pt" style="margin-top:8px;"><div class="h">{"3. Core Instrumentation" if is_en else "3. Набор инструментов"}</div><div class="d">{"e.g., <code>Muted upright piano, warm Rhodes, brushed jazz drums, cello drone</code>." if is_en else "например, <code>Muted upright piano, warm Rhodes, brushed jazz drums, cello drone</code>."}</div></div>
        <div class="pt" style="margin-top:8px;"><div class="h">{"4. Emotional Tone & Mix" if is_en else "4. Настроение и сведение"}</div><div class="d">{"e.g., <code>Introspective, melancholic, twilight mood, analog tape saturation</code>." if is_en else "например, <code>Introspective, melancholic, twilight mood, analog tape saturation</code>."}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"STRUCTURAL ARRANGEMENT TAGS (SUNO / UDIO)" if is_en else "ТЕГИ РАЗМЕТКИ СТРУКТУРЫ (SUNO / UDIO)"}</div>
        <div style="font-family:var(--mono);font-size:16px;line-height:1.6;color:#dbe4f0;background:var(--surface);padding:16px;border-radius:8px;border:1px solid var(--line);">
          <span style="color:var(--cyan)">[Intro]</span><br>
          Sparse solo cello drone, rain sound effects, distant piano note<br><br>
          <span style="color:var(--green)">[Verse 1]</span><br>
          Subtle double bass enters, steady 70 BPM acoustic brushes<br><br>
          <span style="color:var(--amber)">[Build-up]</span><br>
          Strings swell, tempo tightens, rhythmic tension rises<br><br>
          <span style="color:var(--violet)">[Outro]</span><br>
          Instruments fade, single sustained Rhodes chord decaying into tape hiss
        </div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>18 / 24</span></div>
  <template class="notes">{"Teach students how to direct music like a composer. Structural tags [Intro], [Verse], [Build-up], [Outro] force the model to respect narrative progression." if is_en else "Учим студентов мыслить как саундтрек-композитор. Теги разметки [Intro], [Verse], [Build-up], [Outro] задают динамику видеоряда."}</template>
</section>
""")

    # Slide 19: Multi-Stem Assembly
    s.append(f"""
<section class="slide" data-n="19">
  <div class="kicker">{"Audio Engineering • Post-Production Mixing" if is_en else "Сведение звука • Пост-продакшн"}</div>
  <h2 class="title">{"Multi-Stem Assembly: Loudness Targets, Sidechain Ducking, and Python Stems" if is_en else "Сведение мультитрека: стандарты громкости LUFS, дакинг и пайплайн на Python"}</h2>
  <p class="lead">{"Raw generated audio stems must be dynamically balanced and frequency-shaped to create an integrated commercial soundtrack." if is_en else "Сырые аудиодорожки необходимо сбалансировать по громкости и частотам для создания чистого коммерческого микса."}</p>
  <div class="body">
    <div class="row c3">
      <div class="card-box">
        <div class="card-label">{"STEM 1 • VOICEOVER" if is_en else "СТЕМ 1 • ДИКТОР (VOICEOVER)"}</div>
        <div class="pt"><div class="h">{"Target: -14 LUFS" if is_en else "Громкость: -14 LUFS"}</div><div class="d">{"• High-pass filter at 80Hz (cuts mic rumble).<br>• Fast peak limiter at -1.0 dBFS.<br>• Center panned mono for absolute speech clarity." if is_en else "• Срез низких частот ниже 80 Гц (убирает гул микрофона).<br>• Лимитер на пиках -1.0 dBFS.<br>• Центрированная моно-панорама для максимальной разборчивости."}</div></div>
      </div>
      <div class="card-box">
        <div class="card-label">{"STEM 2 • FOLEY SFX" if is_en else "СТЕМ 2 • ШУМЫ FOLEY"}</div>
        <div class="pt"><div class="h">{"Target: -18 LUFS" if is_en else "Громкость: -18 LUFS"}</div><div class="d">{"• Stereo width panned across the stereo field.<br>• Precise millisecond frame sync to video impacts (splash, door closing)." if is_en else "• Стереопанорама в пространстве.<br>• Синхронизация до миллисекунды с ударами и событиями видеоряда (брызги, стук двери)."}</div></div>
      </div>
      <div class="card-box active" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"STEM 3 • MUSIC (WITH DUCKING)" if is_en else "СТЕМ 3 • МУЗЫКА С ДАКИНГОМ"}</div>
        <div class="pt"><div class="h">{"Target: -22 LUFS (Ducked)" if is_en else "Громкость: -22 LUFS (Приглушена)"}</div><div class="d">{"• <b>Sidechain Ducking:</b> Music automatically attenuates by -4dB to -6dB whenever voiceover speech is detected, rising back during pauses." if is_en else "• <b>Sidechain Ducking:</b> Музыка автоматически проседает на -4...-6 дБ, когда говорит диктор, и плавно возвращается в паузах."}</div></div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"Automated Python Assembly:" if is_en else "Автоматизация на Python:"}</b> {"Using <code>pydub</code> and <code>ffmpeg</code>, this 3-stem mix is computed deterministically in 1.2 seconds in code with automatic LUFS leveling." if is_en else "С помощью <code>pydub</code> и <code>ffmpeg</code> этот микс собирается программно за 1.2 секунды с автоматической нормализацией громкости."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>19 / 24</span></div>
  <template class="notes">{"Explain Sidechain Ducking. Without ducking, music drowns voice. Emphasize LUFS standards: -14 LUFS for YouTube/podcasts." if is_en else "Объясняем Sidechain Ducking. Без дакинга музыка заглушает голос. Фиксируем стандарт: -14 LUFS для YouTube и подкастов."}</template>
</section>
""")

    # Slide 20: Real-Time Voice Agents
    s.append(f"""
<section class="slide" data-n="20">
  <div class="kicker">{"Conversational AI • System Architecture" if is_en else "Голосовые агенты • Архитектура систем"}</div>
  <h2 class="title">{"Real-Time Voice Agents: The Sub-300ms Conversational Speech Loop" if is_en else "Голосовые агенты реального времени: сквозной цикл с задержкой до 300 мс"}</h2>
  <p class="lead">{"Building conversational voice agents requires coordinating five streaming services inside a strict human conversational latency budget." if is_en else "Создание речевых агентов требует координации 5 потоковых сервисов в жестком бюджете человеческого восприятия (<300 мс)."}</p>
  <div class="body">
    <div class="card-box" style="margin-bottom:20px;border-color:var(--cyan)">
      <div class="card-label">{"THE SUB-300MS LATENCY BUDGET BREAKDOWN" if is_en else "БЮДЖЕТ ЗАДЕРЖКИ ГОЛОСОВОГО АГЕНТА (ВСЕГО ~285 МС)"}</div>
      <div style="display:grid;grid-template-columns:repeat(5, 1fr);gap:12px;margin-top:8px;">
        <div style="background:var(--surface);padding:12px;border-radius:8px;border:1px solid var(--line);">
          <div style="font-family:var(--mono);color:var(--cyan);font-weight:700;">1. WebRTC In</div>
          <div style="font-size:15px;color:var(--muted);margin-top:4px;">Mic audio buffer: <b>20 ms</b></div>
        </div>
        <div style="background:var(--surface);padding:12px;border-radius:8px;border:1px solid var(--line);">
          <div style="font-family:var(--mono);color:var(--green);font-weight:700;">2. VAD Cutoff</div>
          <div style="font-size:15px;color:var(--muted);margin-top:4px;">Silero silence check: <b>15 ms</b></div>
        </div>
        <div style="background:var(--surface);padding:12px;border-radius:8px;border:1px solid var(--line);">
          <div style="font-family:var(--mono);color:var(--amber);font-weight:700;">3. Streaming STT</div>
          <div style="font-size:15px;color:var(--muted);margin-top:4px;">Whisper Turbo: <b>80 ms</b></div>
        </div>
        <div style="background:var(--surface);padding:12px;border-radius:8px;border:1px solid var(--line);">
          <div style="font-family:var(--mono);color:var(--violet);font-weight:700;">4. LLM TTFT</div>
          <div style="font-size:15px;color:var(--muted);margin-top:4px;">Groq / Cerebras Llama 3: <b>50 ms</b></div>
        </div>
        <div style="background:var(--surface);padding:12px;border-radius:8px;border:1px solid var(--line);">
          <div style="font-family:var(--mono);color:var(--cyan);font-weight:700;">5. Streaming TTS</div>
          <div style="font-size:15px;color:var(--muted);margin-top:4px;">Cartesia Sonic: <b>90 ms</b></div>
        </div>
      </div>
    </div>
    <div class="row c2">
      <div class="card-box">
        <div class="card-label">{"BARGE-IN HANDLING (USER INTERRUPTION)" if is_en else "ОБРАБОТКА ПЕРЕБИВАНИЯ (BARGE-IN)"}</div>
        <div class="pt"><div class="h">{"Immediate Stream Cancellation" if is_en else "Мгновенная отмена синтеза"}</div><div class="d">{"When user speaks while agent is talking, VAD detects speech ➔ sends WebSocket <code>cancel</code> ➔ instantly stops audio output and clears playback queue." if is_en else "Когда пользователь начинает говорить во время ответа агента, VAD фиксирует голос ➔ шлет <code>cancel</code> по WebSocket ➔ динамик мгновенно замолкает."}</div></div>
      </div>
      <div class="card-box">
        <div class="card-label">{"FULL-DUPLEX WEBRTC PROTOCOL" if is_en else "ПОЛНОДУПЛЕКСНЫЙ ПРОТОКОЛ WEBRTC"}</div>
        <div class="pt"><div class="h">{"Bidirectional Audio Pipe" if is_en else "Двусторонний поток звука"}</div><div class="d">{"WebRTC handles jitter buffers, acoustic echo cancellation (AEC), and noise suppression directly on the client side." if is_en else "WebRTC берет на себя эхоподавление (AEC), удаление акустического шума и буферизацию пакетов на стороне браузера/устройства."}</div></div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>20 / 24</span></div>
  <template class="notes">{"Walk through the latency budget. Humans perceive conversational lag after 300ms. Explain how streaming chunking achieves 285ms." if is_en else "Разбираем бюджет задержки. Человек чувствует задержку диалога, если она больше 300 мс. Показываем, как потоковые чанки дают 285 мс."}</template>
</section>
""")

    # Slide 21: Python API Automation
    s.append(f"""
<section class="slide" data-n="21">
  <div class="kicker">{"Code Implementation • Python SDK" if is_en else "Код и автоматизация • Python SDK"}</div>
  <h2 class="title">{"Automating Audio AI in Code: Whisper, ElevenLabs, and Stem Mixing" if is_en else "Автоматизация звука в коде: Whisper, ElevenLabs и сведение стемов"}</h2>
  <p class="lead">{"Production audio pipelines chain speech recognition, voice synthesis, and multi-stem audio assembly into automated Python workflows." if is_en else "Промышленный пайплайн связывает транскрибацию, синтез и сведение стемов в единый асинхронный скрипт на Python."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="card-box" style="border-color:var(--cyan)">
        <div class="card-label">{"1. WHISPER WORD TIMESTAMPS" if is_en else "1. ПОСЛОВНЫЕ ТАЙМКОДЫ В WHISPER"}</div>
        <div style="font-family:var(--mono);font-size:15px;line-height:1.5;color:#dbe4f0;background:var(--surface);padding:14px;border-radius:8px;">
import whisper<br>
model = whisper.load_model("turbo")<br>
res = model.transcribe("narration.mp3", word_timestamps=True)<br>
for seg in res["segments"]:<br>
&nbsp;&nbsp;for w in seg["words"]:<br>
&nbsp;&nbsp;&nbsp;&nbsp;print(w["start"], w["end"], w["word"])
        </div>
      </div>
      <div class="card-box" style="border-color:var(--green)">
        <div class="card-label">{"2. STREAMING TTS & DUCKED MIXING" if is_en else "2. СИНТЕЗ ELEVENLABS И СВЕДЕНИЕ PYDUB"}</div>
        <div style="font-family:var(--mono);font-size:15px;line-height:1.5;color:#dbe4f0;background:var(--surface);padding:14px;border-radius:8px;">
from pydub import AudioSegment<br>
voice = AudioSegment.from_file("voice.mp3") - 2.0<br>
sfx = AudioSegment.from_file("foley.mp3") - 6.0<br>
music = AudioSegment.from_file("music.mp3") - 12.0<br>
# Overlay stems at synchronized offsets<br>
mix = music.overlay(voice, position=0).overlay(sfx, position=1200)<br>
mix.export("final_soundtrack.mp3", format="mp3")
        </div>
      </div>
    </div>
    <div class="note" style="margin-top:20px;border-color:var(--cyan)"><b>{"Colab Notebook Ready:" if is_en else "Готовый Colab-ноутбук:"}</b> {"Execute and test this full pipeline in <code>notebooks/L06_Speech_and_Audio_AI_Pipeline.ipynb</code> with $0 spend." if is_en else "Полный рабочий пайплайн доступен в <code>notebooks/L06_Speech_and_Audio_AI_Pipeline.ipynb</code> для запуска в один клик."}</div>
  </div>
  <div class="foot"><span>{foot}</span><span>21 / 24</span></div>
  <template class="notes">{"Walk through the code snippets. Show how easy it is to extract timestamps and overlay stems in Python." if is_en else "Показываем простоту сборки в Python. Никаких сложных DAW: несколько строк кода нарезают звук и сводят дорожки."}</template>
</section>
""")

    # Slide 22: Audio QA Checklist
    s.append(f"""
<section class="slide" data-n="22">
  <div class="kicker">{"Quality Assurance • Forensic Audio Audit" if is_en else "Контроль качества • Инженерный аудио-аудит"}</div>
  <h2 class="title">{"Audio QA Checklist: Digital Clipping, Comb-Filtering, and Lip-Sync Drift" if is_en else "Инженерный чеклист Audio QA: клиппинг, фазовый шум и рассинхрон липсинка"}</h2>
  <p class="lead">{"Never deliver synthetic audio without verifying four acoustic defect classes against strict quantitative thresholds." if is_en else "Никогда не выпускайте синтетическое аудио в продакшен без проверки 4 классов акустических дефектов."}</p>
  <div class="body">
    <div class="row c4">
      <div class="card-box" style="border-color:var(--red)">
        <div class="card-label" style="color:var(--red)">{"1. DIGITAL CLIPPING" if is_en else "1. ЦИФРОВОЙ КЛИППИНГ"}</div>
        <div class="pt"><div class="h">{"Peaks > 0.0 dBFS" if is_en else "Пики > 0.0 dBFS"}</div><div class="d">{"<b>Defect:</b> Harsh squared-off waveform tops producing harsh clicking distortion.<br><b>Tolerance:</b> Zero. Peak limit to -1.0 dBFS." if is_en else "<b>Дефект:</b> Срезание верхушек синусоиды, порождающее треск и перегруз.<br><b>Допуск:</b> 0 пиков выше -1.0 dBFS."}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--amber)">
        <div class="card-label" style="color:var(--amber)">{"2. COMB-FILTERING" if is_en else "2. ФАЗОВЫЙ ШУМ"}</div>
        <div class="pt"><div class="h">{"Metallic Resonance" if is_en else "Металлический призвук"}</div><div class="d">{"<b>Defect:</b> Unnatural hollow robotic timbre around 2.5kHz–4kHz from poor neural vocoders.<br><b>Fix:</b> Switch to 48kHz HiFi vocoder." if is_en else "<b>Дефект:</b> Роботизированный призвук бочки на частотах 2.5–4 кГц.<br><b>Решение:</b> Переключение на 48 кГц HiFi-вокодер."}</div></div>
      </div>
      <div class="card-box" style="border-color:var(--amber)">
        <div class="card-label" style="color:var(--amber)">{"3. PROSODY DRIFT" if is_en else "3. ДРЕЙФ ИНТОНАЦИИ"}</div>
        <div class="pt"><div class="h">{"Pitch & Energy Jumps" if is_en else "Скачки высоты тона"}</div><div class="d">{"<b>Defect:</b> Speaker suddenly changes mood or volume mid-paragraph.<br><b>Fix:</b> Increase Stability slider to 0.70+." if is_en else "<b>Дефект:</b> Диктор внезапно меняет тембр или громкость в середине фразы.<br><b>Решение:</b> Поднять ползунок Stability до 0.70."}</div></div>
      </div>
      <div class="card-box active" style="border-color:var(--cyan)">
        <div class="card-label" style="color:var(--cyan)">{"4. LIP-SYNC DRIFT" if is_en else "4. ДРЕЙФ ЛИПСИНКА"}</div>
        <div class="pt"><div class="h">{"Audio vs Video Offset" if is_en else "Рассинхрон со ртом"}</div><div class="d">{"<b>Defect:</b> Plosive consonants (B, P, M) misaligned with visual mouth closure.<br><b>Tolerance:</b> Must not exceed 40ms offset." if is_en else "<b>Дефект:</b> Смыкание губ на звуках Б, П, М опаздывает от видео.<br><b>Допуск:</b> Смещение не более 40 мс."}</div></div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>22 / 24</span></div>
  <template class="notes">{"Review the QA checklist. Students will use this exact rubric to grade their homework in video_qa.md." if is_en else "Разбираем критерии аудита. По этой таблице студенты будут проверять свое домашнее задание."}</template>
</section>
""")

    # Slide 23: Homework Assignment
    s.append(f"""
<section class="slide" data-n="23">
  <div class="kicker">{"Practical Application • Homework #6" if is_en else "Практика • Домашнее задание №6"}</div>
  <h2 class="title">{"Homework Assignment #6: Sound Design & Scoring Your L05 Video" if is_en else "Домашнее задание №6: озвучивание и саунд-дизайн видеоролика из L05"}</h2>
  <p class="lead">{"Take your approved 5-second video from Lesson 05 and engineer a complete 3-stem synchronized audio track." if is_en else "Возьмите 5-секундный ролик из Урока 05 и создайте для него полноценный 3-слойный саундтрек."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="stack center">
        <div class="card-box" style="border-color:var(--cyan)">
          <div class="card-label">{"MANDATORY 3-STEM DELIVERABLES" if is_en else "ОБЯЗАТЕЛЬНЫЕ 3 СТЕМА САУНДТРЕКА"}</div>
          <div class="pt"><div class="h">{"1. Voiceover Narration (TTS)" if is_en else "1. Закадровый голос (TTS)"}</div><div class="d">{"Generate 1 cinematic line matching your video in ElevenLabs / Cartesia / Kokoro." if is_en else "Сгенерируйте 1 ёмкую фразу диктора в ElevenLabs, Cartesia или Kokoro."}</div></div>
          <div class="pt" style="margin-top:8px;"><div class="h">{"2. Foley Sound Effects (SFX AI)" if is_en else "2. Фоли-шумы окружения (SFX AI)"}</div><div class="d">{"Synthesize synchronized physical sound effects (puddle splash, steam, crate creak) in ElevenLabs SFX or Stable Audio." if is_en else "Сгенерируйте точные звуки предметов (брызги лужи, пар кружки, стук ящика) в ElevenLabs SFX."}</div></div>
          <div class="pt" style="margin-top:8px;"><div class="h">{"3. Background Instrumental Music" if is_en else "3. Инструментальная музыка"}</div><div class="d">{"Create a subtle instrumental soundtrack in Suno v4 or Udio 1.5 with sidechain ducking." if is_en else "Создайте фоновый инструментальный саундтрек в Suno v4 или Udio с приглушением под голос."}</div></div>
        </div>
      </div>
      <div class="stack center">
        <div class="card-box" style="background:var(--surface);">
          <div class="card-label" style="color:var(--green)">{"SUBMISSION STRUCTURE IN GITHUB" if is_en else "СТРУКТУРА СДАЧИ В GITHUB"}</div>
          <div style="font-family:var(--mono);font-size:15px;line-height:1.5;color:#cbd5e1;">
genai-homeworks/<br>
└── L06/<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── audio/<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── 01_voiceover.mp3<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;├── 02_foley_sfx.mp3<br>
&nbsp;&nbsp;&nbsp;&nbsp;│&nbsp;&nbsp;&nbsp;└── 03_music_bg.mp3<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── final_video_with_audio.mp4<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── audio_spec.md<br>
&nbsp;&nbsp;&nbsp;&nbsp;└── audio_qa.md
          </div>
        </div>
        <div class="note"><b>{"Reviewer Invite:" if is_en else "Инвайт ревьюеру:"}</b> <code>ihar_rubanovich@epam.com</code>. {"Review feedback within 48 hours." if is_en else "Обратная связь в течение 48 часов."}</div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>23 / 24</span></div>
  <template class="notes">{"Explain the homework requirements. Students take their L05 clip and add 3 stems. Fast, fun, and production-grade." if is_en else "Объясняем домашку. Студенты берут свой ролик из L05 и собирают для него 3 звуковых слоя. Практично и зрелищно."}</template>
</section>
""")

    # Slide 24: Summary & Module 3 Teaser
    s.append(f"""
<section class="slide" data-n="24">
  <div class="kicker">{"Module 2 Complete • Summary & Next Steps" if is_en else "Финал Модуля 2 • Итоги и анонс L07"}</div>
  <h2 class="title">{"Multimodality Complete: 4 Engineering Laws of Generative Audio" if is_en else "Модуль мультимодальности закрыт: 4 закона генеративного звука"}</h2>
  <p class="lead">{"We have completed Module 2 (Images, Video, and Audio). Next week: enter Module 3 and the Copilot Developer Ecosystem." if is_en else "Мы завершили Модуль 2 (Картинки, Видео и Звук). На следующем занятии переходим к Модулю 3 — экосистеме Copilot для разработчиков."}</p>
  <div class="body">
    <div class="row c2" style="gap:36px;">
      <div class="card-box" style="border-color:var(--cyan)">
        <div class="card-label">{"4 ENGINEERING LAWS OF AUDIO AI" if is_en else "4 ИНЖЕНЕРНЫХ ЗАКОНА НЕЙРОЗВУКА"}</div>
        <ul style="list-style:none;display:flex;flex-direction:column;gap:10px;font-size:18px;color:var(--muted);padding-left:4px;">
          <li><b>1. VAD First:</b> {"Never run Whisper in silence without Silero VAD." if is_en else "Никогда не запускайте Whisper в тишине без Silero VAD."}</li>
          <li><b>2. Punctuate for Breath:</b> {"Use ellipses and em-dashes to direct TTS prosody." if is_en else "Размечайте текст точками и тире для управления вдохами диктора."}</li>
          <li><b>3. Instrumental for Video:</b> {"Never use vocal tracks under spoken dialogue." if is_en else "Всегда отключайте вокал в музыке под закадровую речь."}</li>
          <li><b>4. Strict Stem Ducking:</b> {"Attenuate background music by -4dB during speech." if is_en else "Всегда приглушайте музыку на -4 дБ при наличии речи."}</li>
        </ul>
      </div>
      <div class="card-box" style="border-color:var(--violet)">
        <div class="card-label" style="color:var(--violet)">{"NEXT SESSION • LESSON 07: COPILOT ECOSYSTEM" if is_en else "СЛЕДУЮЩИЙ УРОК • L07: ЭКОСИСТЕМА COPILOT"}</div>
        <div style="font-size:18px;line-height:1.45;color:var(--fg);">
          <b>{"Module 3: AI in Software Engineering" if is_en else "Модуль 3: ИИ в разработке ПО"}</b><br>
          {"• One brand, three contexts: Microsoft 365 Copilot vs GitHub Copilot vs Copilot+ PC.<br>• Grounding architecture: Microsoft Graph, Semantic Index, and permissions.<br>• GitHub Copilot 4 modes: Inline completions, Chat, CLI, and Agent Mode.<br>• Enterprise case: EPAM CodeMie @ Dawn Foods (35% SDLC acceleration)." if is_en else "• Один бренд, три контекста: Microsoft 365 Copilot, GitHub Copilot и Copilot+ PC.<br>• Архитектура заземления: Microsoft Graph, Semantic Index и обрезка прав доступа.<br>• 4 режима GitHub Copilot: дополнение строк, чат, CLI и Agent Mode.<br>• Кейс внедрения: EPAM CodeMie @ Dawn Foods (ускорение SDLC на 35%)."}
        </div>
      </div>
    </div>
  </div>
  <div class="foot"><span>{foot}</span><span>24 / 24</span></div>
  <template class="notes">{"Congratulate students on completing Module 2 (Multimodality). Open floor for Q&A. Teaser for Lesson 07 Copilot ecosystem." if is_en else "Поздравляем студентов с закрытием Модуля 2 (Мультимодальность). Открываем микрофон для Q&A. Анонсируем Урок 07 по Copilot."}</template>
</section>
""")

    # Combine all into page
    body_content = "".join(s)

    full_html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html_title}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
{CSS}
</style>
</head>
<body>

<main class="stage" id="stage">
{body_content}
</main>

<aside class="drawer" id="drawer">
  <div class="hd">{"SPEAKER NOTES" if is_en else "ЗАМЕТКИ СПИКЕРА"}</div>
  <div class="tx"></div>
</aside>

<div class="grid" id="grid"></div>

<script>
{JS}
</script>
</body>
</html>
"""
    return full_html

def main():
    ru_path = HERE / "presentation_L06_Speech_and_Audio.html"
    en_path = HERE / "presentation_L06_Speech_and_Audio_EN.html"

    print("Generating RU presentation...")
    ru_path.write_text(build_deck("ru"), encoding="utf-8")
    print(f"Wrote {ru_path.name} ({ru_path.stat().st_size} bytes)")

    print("Generating EN presentation...")
    en_path.write_text(build_deck("en"), encoding="utf-8")
    print(f"Wrote {en_path.name} ({en_path.stat().st_size} bytes)")

    # Render PDFs via headless Edge
    edge = find_edge()
    for html_file in [ru_path, en_path]:
        pdf_file = html_file.with_suffix(".pdf")
        print(f"Compiling {html_file.name} -> {pdf_file.name}...")
        subprocess.run([edge, "--headless", "--disable-gpu", "--no-margins",
                        "--no-pdf-header-footer", "--virtual-time-budget=10000",
                        f"--print-to-pdf={pdf_file}", html_file.as_uri()], check=True)
        print(f"Wrote {pdf_file.name} ({pdf_file.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
