// L04 deck v2 runtime: scaling stage, keyboard/click navigation, notes drawer, slide grid, break timer.
(function () {
  const stage = document.getElementById('stage');
  const slides = [...document.querySelectorAll('.slide')];
  const total = slides.length;
  const drawer = document.getElementById('drawer');
  const grid = document.getElementById('grid');
  let cur = 1;

  function fit() {
    const s = Math.min(window.innerWidth / 1600, window.innerHeight / 900) * 0.98;
    stage.style.setProperty('--s', s);
  }

  function show(n) {
    if (n < 1 || n > total) return;
    cur = n;
    slides.forEach((el, i) => el.classList.toggle('active', i + 1 === n));
    const notes = slides[n - 1].querySelector('.notes');
    drawer.querySelector('.hd').textContent = `${T.notes} • ${String(n).padStart(2, '0')} / ${total}`;
    drawer.querySelector('.tx').innerHTML = notes ? notes.innerHTML : '';
    if (location.hash !== '#' + n) history.replaceState(null, '', '#' + n);
    grid.querySelectorAll('button').forEach((b, i) => b.classList.toggle('cur', i + 1 === n));
  }

  slides.forEach((el, i) => {
    const b = document.createElement('button');
    const t = el.querySelector('.title, h1');
    b.innerHTML = `<span>${String(i + 1).padStart(2, '0')}</span>${t ? t.textContent : ''}`;
    b.onclick = () => { show(i + 1); grid.classList.remove('open'); };
    grid.appendChild(b);
  });

  document.addEventListener('keydown', (e) => {
    if (['ArrowRight', 'PageDown', ' '].includes(e.key)) { e.preventDefault(); show(cur + 1); }
    else if (['ArrowLeft', 'PageUp'].includes(e.key)) { e.preventDefault(); show(cur - 1); }
    else if (e.key === 'Home') show(1);
    else if (e.key === 'End') show(total);
    else if (e.key.toLowerCase() === 'n') drawer.classList.toggle('open');
    else if (e.key.toLowerCase() === 'g') grid.classList.toggle('open');
    else if (e.key.toLowerCase() === 'f') {
      if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {});
      else document.exitFullscreen().catch(() => {});
    } else if (e.key === 'Escape') { grid.classList.remove('open'); drawer.classList.remove('open'); }
  });
  stage.addEventListener('click', (e) => {
    if (e.target.closest('button')) return;
    const r = stage.getBoundingClientRect();
    show(e.clientX > r.left + r.width / 3 ? cur + 1 : cur - 1);
  });
  window.addEventListener('resize', fit);
  window.addEventListener('hashchange', () => show(parseInt(location.hash.slice(1), 10) || 1));

  // break timer
  let left = 300, timer = null;
  const clock = document.getElementById('clock');
  const startBtn = document.getElementById('timerStart');
  const fmt = (s) => `${String(Math.floor(s / 60)).padStart(2, '0')}:${String(s % 60).padStart(2, '0')}`;
  if (startBtn) {
    startBtn.onclick = () => {
      if (timer) { clearInterval(timer); timer = null; startBtn.textContent = T.start; return; }
      startBtn.textContent = T.pause;
      timer = setInterval(() => {
        left = Math.max(0, left - 1); clock.textContent = fmt(left);
        if (!left) { clearInterval(timer); timer = null; startBtn.textContent = T.done; }
      }, 1000);
    };
    document.getElementById('timerReset').onclick = () => {
      clearInterval(timer); timer = null; left = 300; clock.textContent = fmt(left); startBtn.textContent = T.start;
    };
  }

  fit();
  show(parseInt(location.hash.slice(1), 10) || 1);
})();
