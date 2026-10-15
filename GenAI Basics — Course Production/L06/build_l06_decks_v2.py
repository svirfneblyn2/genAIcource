# -*- coding: utf-8 -*-
"""
Build high-fidelity HTML and PDF slide decks for Lesson 06: Speech and Audio AI (RU & EN).
Includes:
- Full-screen Hero Title Cover (Slide 01)
- UI Screenshots: ElevenLabs Studio, ElevenLabs SFX, Whisper Playground, Suno v4 Studio
- High-Density Diagrams: Google Audio Ecosystem, RVQ Codecs, Sidechain Ducking, Voice Agent Waterfall
"""

import sys
import shutil
import subprocess
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

/* Cover Slide */
.cover { padding: 0 !important; position: relative; overflow: hidden; }
.cover .hero-bg { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; opacity: .45; }
.cover .shade { position: absolute; inset: 0; background: linear-gradient(90deg, rgba(11,15,23,.97) 0%, rgba(11,15,23,.90) 50%, rgba(11,15,23,.45) 100%); }
.cover .txt { position: relative; padding: 0 76px; height: 100%; display: flex; flex-direction: column; justify-content: center; max-width: 1120px; z-index: 2; }
.cover .kicker { font-family: var(--mono); font-size: 15px; letter-spacing: .08em; text-transform: uppercase; color: var(--cyan); margin-bottom: 12px; }
.cover h1 { font-family: var(--display); font-size: 84px; font-weight: 800; line-height: 1.02; letter-spacing: -0.035em; color: var(--fg); margin: 0; }
.cover h2 { font-size: 32px; font-weight: 600; line-height: 1.3; color: var(--cyan); margin-top: 18px; text-wrap: balance; }
.cover p { font-size: 21px; line-height: 1.5; color: var(--muted); margin-top: 18px; max-width: 880px; }
.cover .axiom-box { margin-top: 24px; padding: 18px 24px; background: rgba(56,189,248,.07); border: 1px solid rgba(56,189,248,.3); border-radius: 12px; max-width: 880px; font-size: 18px; line-height: 1.45; color: #cbd5e1; }
.cover .axiom-box b { color: var(--cyan); }
.cover .keys { position: absolute; left: 76px; bottom: 26px; font-family: var(--mono); font-size: 13px; color: var(--dim); z-index: 2; }

/* Standard Typography */
.kicker { font-family: var(--mono); font-size: 14px; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: var(--k, var(--cyan)); margin-bottom: 10px; }
.title { font-family: var(--display); font-weight: 700; font-size: 44px; line-height: 1.14; letter-spacing: -0.02em; text-wrap: balance; max-width: 1450px; }
.lead { font-size: 21px; line-height: 1.38; color: var(--muted); margin-top: 10px; max-width: 1350px; text-wrap: balance; }
.body { flex: 1 1 0; min-height: 0; margin-top: 22px; display: flex; flex-direction: column; justify-content: center; }
.foot { position: absolute; left: 72px; right: 72px; bottom: 20px; display: flex; justify-content: space-between; font-family: var(--mono); font-size: 13px; color: var(--dim); }

/* Grid Layouts */
.row { display: grid; gap: 32px; flex: 1 1 0; min-height: 0; }
.c2 { grid-template-columns: 1fr 1fr; }
.c3 { grid-template-columns: repeat(3, 1fr); }
.c4 { grid-template-columns: repeat(4, 1fr); }
.stack { display: flex; flex-direction: column; gap: 16px; min-height: 0; min-width: 0; }
.center { justify-content: center; }

/* Visual UI & Diagram Layouts */
.row.img-split { display: grid; grid-template-columns: 1.12fr 0.88fr; gap: 36px; align-items: center; }
.row.img-split-reverse { display: grid; grid-template-columns: 0.88fr 1.12fr; gap: 36px; align-items: center; }
.pic-frame { border-radius: 12px; border: 1px solid var(--line); overflow: hidden; background: #000; box-shadow: 0 16px 40px rgba(0,0,0,0.5); display: flex; max-height: 520px; }
.pic-frame img { width: 100%; height: 100%; object-fit: contain; display: block; }

/* Cards & Elements */
.card-box { background: var(--surface-card); border: 1px solid var(--line); border-radius: 12px; padding: 20px; display: flex; flex-direction: column; gap: 10px; }
.card-box.active { border-color: var(--cyan); }
.card-label { font-family: var(--mono); font-size: 13px; letter-spacing: .08em; text-transform: uppercase; font-weight: 700; color: var(--k, var(--cyan)); }
.pt { display: flex; flex-direction: column; gap: 6px; }
.pt .h { font-size: 21px; font-weight: 700; line-height: 1.25; }
.pt .d { font-size: 17px; line-height: 1.38; color: var(--muted); }
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

.timer-box { font-family: var(--mono); font-size: 120px; font-weight: 800; color: var(--amber); text-align: center; line-height: 1; margin: 16px 0; }
.timer-btn { align-self: center; background: var(--amber); color: #0b0f17; font-family: var(--mono); font-size: 18px; font-weight: 700; padding: 14px 32px; border: none; border-radius: 8px; cursor: pointer; }
.timer-btn:hover { background: #f59e0b; }

@media print {
  @page { size: 1600px 900px; margin: 0; }
  body { overflow: visible; background: var(--bg); -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  .stage { position: static; transform: none; width: 1600px; height: auto; border-radius: 0; box-shadow: none; overflow: visible; }
  .slide { position: relative; display: flex !important; width: 1600px; height: 900px; break-after: page; page-break-after: always; }
  .drawer, .grid, button { display: none !important; }
}
"""

JS = """
let cur = 1;
const slides = document.querySelectorAll('.slide');
const total = slides.length;
const stage = document.getElementById('stage');
const drawer = document.getElementById('drawer');
const grid = document.getElementById('grid');

function fit() {
  const sx = window.innerWidth / 1600;
  const sy = window.innerHeight / 900;
  const s = Math.min(sx, sy);
  stage.style.setProperty('--s', s);
}
window.addEventListener('resize', fit);
fit();

function show(n) {
  if (n < 1) n = 1;
  if (n > total) n = total;
  slides.forEach(s => s.classList.remove('active'));
  slides[n - 1].classList.add('active');
  cur = n;
  updateDrawer();
  updateGrid();
}

function updateDrawer() {
  const s = slides[cur - 1];
  const t = s.querySelector('template.notes');
  document.getElementById('drawer-tx').innerHTML = t ? t.innerHTML : '<em>Нет заметок к этому слайду.</em>';
  document.getElementById('drawer-hd').innerText = `СЛАЙД ${String(cur).padStart(2, '0')} / ${String(total).padStart(2, '0')}`;
}

function updateGrid() {
  document.querySelectorAll('.grid button').forEach((b, idx) => {
    b.classList.toggle('cur', idx + 1 === cur);
  });
}

function buildGrid() {
  grid.innerHTML = '';
  slides.forEach((s, idx) => {
    const btn = document.createElement('button');
    const titleEl = s.querySelector('.title, h1');
    const t = titleEl ? titleEl.innerText : `Слайд ${idx + 1}`;
    btn.innerHTML = `<span>СЛАЙД ${String(idx + 1).padStart(2, '0')}</span>${t}`;
    btn.onclick = () => { show(idx + 1); grid.classList.remove('open'); };
    grid.appendChild(btn);
  });
}
buildGrid();

window.addEventListener('keydown', (e) => {
  if (e.key === 'ArrowRight' || e.key === ' ') { show(cur + 1); }
  else if (e.key === 'ArrowLeft') { show(cur - 1); }
  else if (e.key === 'Home') { show(1); }
  else if (e.key === 'End') { show(total); }
  else if (e.key.toLowerCase() === 'n') { drawer.classList.toggle('open'); }
  else if (e.key.toLowerCase() === 'g') { grid.classList.toggle('open'); }
  else if (e.key.toLowerCase() === 'f') {
    if (!document.fullscreenElement) { document.documentElement.requestFullscreen(); }
    else { document.exitFullscreen(); }
  }
});

let timerInt = null;
let timeLeft = 300;
function toggleTimer() {
  const btn = document.getElementById('timer-btn');
  const disp = document.getElementById('timer-disp');
  if (timerInt) {
    clearInterval(timerInt);
    timerInt = null;
    btn.innerText = 'СТАРТ 5 МИН';
  } else {
    btn.innerText = 'ПАУЗА';
    timerInt = setInterval(() => {
      timeLeft--;
      if (timeLeft <= 0) {
        clearInterval(timerInt);
        timerInt = null;
        disp.innerText = '00:00';
        btn.innerText = 'ВРЕМЯ ВЫШЛО';
        return;
      }
      const m = String(Math.floor(timeLeft / 60)).padStart(2, '0');
      const s = String(timeLeft % 60).padStart(2, '0');
      disp.innerText = `${m}:${s}`;
    }, 1000);
  }
}
"""

print("Deck configuration ready.")
