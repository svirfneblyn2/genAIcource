# HTML and CSS Template for Advanced GenAI Module 01 Presentation Deck
import json

def render_deck(slides):
    total_slides = len(slides)
    
    # Generate slide pages HTML
    slides_html_list = []
    speaker_notes_dict = {}
    grid_cards_html_list = []
    
    for s in slides:
        idx = s["index"]
        idx_str = f"{idx:02d}"
        tot_str = f"{total_slides:02d}"
        
        speaker_notes_dict[str(idx)] = {
            "goal": s["notes"]["goal"],
            "talkTrack": s["notes"]["talkTrack"],
            "timing": s["notes"]["timing"]
        }
        
        slide_html = f'''      <section class="slide-page{' active' if idx == 1 else ''}" data-slide="{idx}">
        <div class="slide-topbar">
          <div class="kicker-tag">{s["kicker"]}</div>
          <div class="index-tag">{idx_str} / {tot_str}</div>
        </div>
        <h1 class="slide-title">{s["title"]}</h1>
        <p class="slide-lead">{s["lead"]}</p>
        
        <div class="diagram-arena">
{s["svg"]}
        </div>
        
        <div class="slide-footer">
          <div class="takeaway-pill">{s["takeaway"]}</div>
          <div class="section-pill">{s.get("section", "Module 01")}</div>
        </div>
      </section>'''
        slides_html_list.append(slide_html)
        
        # Grid thumbnail card
        grid_card = f'''        <div class="grid-item{' active' if idx == 1 else ''}" data-slide="{idx}">
          <div class="grid-item-num">Slide {idx_str}</div>
          <div class="grid-item-name">{s["title"]}</div>
          <div class="grid-item-lead">{s["lead"][:75]}...</div>
        </div>'''
        grid_cards_html_list.append(grid_card)

    all_slides_html = "\n".join(slides_html_list)
    all_grid_cards_html = "\n".join(grid_cards_html_list)
    speaker_notes_json = json.dumps(speaker_notes_dict, indent=2)

    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Module 01: Cloud AI Capabilities Overview | Systems Engineering Deck</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      /* Calm Engineering Palette */
      --bg-canvas: #0e131b;
      --bg-surface: #141c28;
      --bg-surface-alt: #1b2434;
      --border-subtle: #253245;
      --border-focus: #3b82f6;
      --border-strong: #364761;
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      /* Semantic Functional Accents */
      --accent-blue: #60a5fa;   /* AWS & Technical Primary */
      --accent-purple: #b4a4e5; /* Azure & Agent Orchestration */
      --accent-amber: #e0c58e;  /* Google Cloud & Cost */
      --accent-green: #6ee7b7;  /* Success, Verified, Local */
      --accent-coral: #d98585;  /* Risk, Boundaries, Rejected */
      
      --font-sans: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', 'Fira Code', monospace;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background-color: var(--bg-canvas);
      color: var(--text-main);
      font-family: var(--font-sans);
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      display: flex;
      flex-direction: column;
      user-select: none;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
    }}

    /* Main Presentation Stage & Scaling Wrapper */
    main.stage-wrapper {{
      flex: 1;
      width: 100vw;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(circle at 50% 20%, rgba(27, 36, 52, 0.45) 0%, rgba(14, 19, 27, 0.98) 75%);
      position: relative;
      overflow: hidden;
    }}

    .slide-frame {{
      width: 1440px;
      height: 810px;
      min-width: 1440px;
      min-height: 810px;
      transform-origin: center center;
      background: var(--bg-surface);
      border: 1px solid var(--border-strong);
      border-radius: 10px;
      box-shadow: 0 30px 70px -20px rgba(0, 0, 0, 0.8), 0 0 1px 1px rgba(255, 255, 255, 0.05);
      position: relative;
      overflow: hidden;
      display: flex;
      flex-direction: column;
    }}

    .slide-page {{
      position: absolute;
      inset: 0;
      padding: 34px 48px 24px 48px;
      display: none;
      flex-direction: column;
      opacity: 0;
      transition: opacity 0.2s ease;
      background: var(--bg-surface);
    }}

    .slide-page.active {{
      display: flex;
      opacity: 1;
      z-index: 10;
    }}

    /* Topbar Layout */
    .slide-topbar {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 8px;
    }}

    .kicker-tag {{
      font-size: 15px;
      color: var(--accent-blue);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      display: flex;
      align-items: center;
      gap: 8px;
    }}

    .kicker-tag::before {{
      content: '';
      display: inline-block;
      width: 8px;
      height: 8px;
      background-color: var(--accent-blue);
      border-radius: 50%;
    }}

    .index-tag {{
      font-family: var(--font-mono);
      font-size: 15px;
      color: var(--text-dim);
      background: rgba(37, 50, 69, 0.5);
      padding: 3px 12px;
      border-radius: 4px;
      border: 1px solid var(--border-subtle);
    }}

    /* Title & Lead */
    .slide-title {{
      font-size: 38px;
      font-weight: 800;
      line-height: 1.15;
      color: #ffffff;
      margin-bottom: 6px;
      letter-spacing: -0.02em;
    }}

    .slide-lead {{
      font-size: 18px;
      color: var(--text-muted);
      line-height: 1.38;
      margin-bottom: 12px;
      max-width: 1360px;
    }}

    /* Central Diagram Arena */
    .diagram-arena {{
      flex: 1 1 0%;
      min-height: 0;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      background: #111722;
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 10px 14px;
      overflow: hidden;
    }}

    .blueprint-svg {{
      width: 100%;
      height: 100%;
      max-height: 100%;
      overflow: visible;
    }}

    /* SVG Blueprint Classes */
    .node-box {{
      fill: #161f2c;
      stroke: var(--border-subtle);
      stroke-width: 1.5;
      rx: 6;
    }}

    .node-box-active {{
      fill: #1a2538;
      stroke: var(--accent-blue);
      stroke-width: 1.8;
      rx: 6;
    }}

    .node-box-active-purple {{
      fill: #1a2538;
      stroke: var(--accent-purple);
      stroke-width: 1.8;
      rx: 6;
    }}

    .node-box-active-amber {{
      fill: #1a2538;
      stroke: var(--accent-amber);
      stroke-width: 1.8;
      rx: 6;
    }}

    .node-box-active-green {{
      fill: #152420;
      stroke: var(--accent-green);
      stroke-width: 1.8;
      rx: 6;
    }}

    .node-box-active-coral {{
      fill: #24191d;
      stroke: var(--accent-coral);
      stroke-width: 1.8;
      rx: 6;
    }}

    .node-box-alt {{
      fill: #141c28;
      stroke: #334155;
      stroke-width: 1.5;
      rx: 6;
    }}

    .swimlane-bg {{
      fill: #121824;
      stroke: #1e293b;
      stroke-width: 1.2;
      rx: 8;
    }}

    .text-h1 {{
      font-family: var(--font-sans);
      font-size: 15.5px;
      font-weight: 700;
      fill: #ffffff;
    }}

    .text-h2 {{
      font-family: var(--font-sans);
      font-size: 13.5px;
      font-weight: 600;
      fill: #e2e8f0;
    }}

    .text-p {{
      font-family: var(--font-sans);
      font-size: 12.5px;
      fill: #94a3b8;
    }}

    .text-dim {{
      font-family: var(--font-sans);
      font-size: 11.5px;
      fill: #64748b;
    }}

    .text-mono {{
      font-family: var(--font-mono);
      font-size: 12px;
      fill: var(--accent-blue);
    }}

    .text-mono-purple {{
      font-family: var(--font-mono);
      font-size: 12px;
      fill: var(--accent-purple);
    }}

    .text-mono-amber {{
      font-family: var(--font-mono);
      font-size: 12px;
      fill: var(--accent-amber);
    }}

    .text-mono-green {{
      font-family: var(--font-mono);
      font-size: 12px;
      fill: var(--accent-green);
    }}

    .text-mono-coral {{
      font-family: var(--font-mono);
      font-size: 12px;
      fill: var(--accent-coral);
    }}

    /* Slide Footer */
    .slide-footer {{
      margin-top: 10px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 14px;
      color: var(--text-dim);
      border-top: 1px solid var(--border-subtle);
      padding-top: 8px;
    }}

    .takeaway-pill {{
      color: #cbd5e1;
      display: flex;
      align-items: center;
      gap: 8px;
      font-size: 13.5px;
      font-weight: 500;
    }}

    .takeaway-pill::before {{
      content: 'TAKEAWAY:';
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--accent-amber);
      background: rgba(224, 197, 142, 0.12);
      border: 1px solid rgba(224, 197, 142, 0.3);
      padding: 2px 6px;
      border-radius: 4px;
      font-weight: 700;
    }}

    .section-pill {{
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--accent-blue);
      background: rgba(96, 165, 250, 0.1);
      border: 1px solid rgba(96, 165, 250, 0.25);
      padding: 2px 8px;
      border-radius: 4px;
    }}

    /* Micro-Controls Panel */
    .bottom-controls {{
      position: fixed;
      bottom: 12px;
      right: 24px;
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(14, 19, 27, 0.94);
      backdrop-filter: blur(8px);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 4px 8px;
      z-index: 200;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.5);
    }}

    .btn-ctrl {{
      background: #1b2434;
      border: 1px solid var(--border-subtle);
      color: var(--text-main);
      padding: 4px 10px;
      border-radius: 4px;
      font-size: 12px;
      font-family: var(--font-mono);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s ease;
    }}

    .btn-ctrl:hover {{
      background: #253245;
      border-color: var(--accent-blue);
      color: #ffffff;
    }}

    .slide-counter {{
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-muted);
      padding: 0 6px;
    }}

    /* Progress Bar */
    .deck-progress {{
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100vw;
      height: 3px;
      background: var(--border-subtle);
      z-index: 300;
    }}

    .progress-fill {{
      height: 100%;
      background: var(--accent-blue);
      width: 3.7%;
      transition: width 0.2s ease;
    }}

    /* Notes Drawer */
    .notes-drawer {{
      position: fixed;
      right: -520px;
      top: 0;
      bottom: 0;
      width: 500px;
      z-index: 400;
      background: #121824;
      border-left: 1px solid var(--border-strong);
      box-shadow: -10px 0 30px rgba(0, 0, 0, 0.7);
      transition: right 0.25s ease;
      display: flex;
      flex-direction: column;
      padding: 28px;
    }}

    .notes-drawer.open {{
      right: 0;
    }}

    .notes-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-bottom: 16px;
      border-bottom: 1px solid var(--border-subtle);
      margin-bottom: 20px;
    }}

    .notes-title {{
      font-size: 16px;
      color: var(--accent-amber);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .btn-close-notes {{
      background: none;
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      cursor: pointer;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 14px;
    }}

    .btn-close-notes:hover {{
      color: #ffffff;
      border-color: var(--text-main);
    }}

    .notes-body {{
      font-size: 14.5px;
      color: #cbd5e1;
      line-height: 1.6;
      overflow-y: auto;
      flex: 1;
    }}

    .notes-tag {{
      font-size: 12px;
      color: var(--accent-blue);
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-top: 14px;
      margin-bottom: 4px;
    }}

    .notes-box {{
      margin-top: 16px;
      padding: 12px 14px;
      background: rgba(224, 197, 142, 0.08);
      border: 1px solid rgba(224, 197, 142, 0.25);
      border-radius: 6px;
      font-size: 13px;
      color: #f5e8c7;
    }}

    /* Grid View Overlay */
    .grid-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(14, 19, 27, 0.96);
      backdrop-filter: blur(12px);
      z-index: 500;
      display: none;
      flex-direction: column;
      padding: 30px 48px;
    }}

    .grid-overlay.open {{
      display: flex;
    }}

    .grid-top {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
    }}

    .grid-title {{
      font-size: 22px;
      font-weight: 700;
      color: #ffffff;
    }}

    .grid-sheet {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 16px;
      overflow-y: auto;
      flex: 1;
      padding-right: 8px;
    }}

    .grid-item {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 14px 18px;
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .grid-item:hover {{
      border-color: var(--accent-blue);
      transform: translateY(-2px);
    }}

    .grid-item.active {{
      border-color: var(--accent-blue);
      box-shadow: 0 0 12px rgba(96, 165, 250, 0.25);
      background: #192334;
    }}

    .grid-item-num {{
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--accent-blue);
      font-weight: 700;
    }}

    .grid-item-name {{
      font-size: 14px;
      font-weight: 600;
      color: #ffffff;
      line-height: 1.35;
    }}

    .grid-item-lead {{
      font-size: 12px;
      color: var(--text-dim);
      line-height: 1.3;
    }}

    /* Export & Print Styles (1440pt x 810pt Headless Chrome Vector PDF) */
    @media print {{
      @page {{
        size: 1440pt 810pt;
        margin: 0;
      }}
      html, body {{
        background-color: #0e131b !important;
        color: #f8fafc !important;
        overflow: visible !important;
        height: auto !important;
        width: 1440pt !important;
        display: block !important;
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
      }}
      main.stage-wrapper {{
        position: static !important;
        height: auto !important;
        width: 1440pt !important;
        overflow: visible !important;
        display: block !important;
        background: transparent !important;
        margin: 0 !important;
        padding: 0 !important;
      }}
      .slide-frame {{
        position: static !important;
        height: auto !important;
        width: 1440pt !important;
        overflow: visible !important;
        display: block !important;
        background: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        box-shadow: none !important;
        margin: 0 !important;
        padding: 0 !important;
        transform: none !important;
      }}
      .slide-page {{
        display: flex !important;
        flex-direction: column !important;
        position: relative !important;
        opacity: 1 !important;
        page-break-after: always !important;
        page-break-inside: avoid !important;
        break-after: page !important;
        break-inside: avoid !important;
        width: 1440pt !important;
        height: 810pt !important;
        max-height: 810pt !important;
        overflow: hidden !important;
        box-sizing: border-box !important;
        background: #0e131b !important;
        padding: 34px 48px 24px 48px !important;
        margin: 0 !important;
      }}
      .slide-page:last-of-type {{
        break-after: avoid !important;
        page-break-after: avoid !important;
      }}
      .bottom-controls, .notes-drawer, .grid-overlay, .deck-progress {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Main Presentation Stage -->
  <main class="stage-wrapper">
    <div class="slide-frame">
{all_slides_html}
    </div>
  </main>

  <!-- Progress Bar -->
  <div class="deck-progress">
    <div class="progress-fill" id="progress-fill"></div>
  </div>

  <!-- Micro-Navigation Panel -->
  <div class="bottom-controls">
    <button class="btn-ctrl" id="btn-prev" title="Previous Slide [Left Arrow]">&larr;</button>
    <span class="slide-counter" id="slide-indicator">01 / {total_slides:02d}</span>
    <button class="btn-ctrl" id="btn-next" title="Next Slide [Right Arrow]">&rarr;</button>
    <button class="btn-ctrl" id="btn-grid" title="Slide Grid [G]">Grid [G]</button>
    <button class="btn-ctrl" id="btn-notes" title="Speaker Notes [N]">Notes [N]</button>
    <button class="btn-ctrl" id="btn-fs" title="Toggle Fullscreen [F]">FS [F]</button>
  </div>

  <!-- Speaker Notes Drawer -->
  <aside class="notes-drawer" id="notes-drawer">
    <div class="notes-header">
      <div class="notes-title" id="notes-title">Speaker Notes &middot; Slide 01</div>
      <button class="btn-close-notes" id="btn-close-notes" title="Close Notes [Esc]">&times;</button>
    </div>
    <div class="notes-body" id="notes-body">
      <!-- Populated dynamically via JS -->
    </div>
  </aside>

  <!-- Slide Overview Grid Overlay -->
  <div class="grid-overlay" id="grid-overlay">
    <div class="grid-top">
      <div class="grid-title">Lecture Navigation &middot; 27 Architecture Slides</div>
      <button class="btn-close-notes" id="btn-close-grid" title="Close Grid [Esc]">&times;</button>
    </div>
    <div class="grid-sheet" id="grid-sheet">
{all_grid_cards_html}
    </div>
  </div>

  <script>
    const speakerNotes = {speaker_notes_json};
    const totalSlides = {total_slides};
    let currentSlide = 1;

    function scaleStage() {{
      const frame = document.querySelector('.slide-frame');
      if (!frame) return;
      const targetW = 1440;
      const targetH = 810;
      const scale = Math.min(window.innerWidth / targetW, window.innerHeight / targetH);
      frame.style.transform = `scale(${{scale}})`;
    }}

    function showSlide(num) {{
      if (num < 1) num = 1;
      if (num > totalSlides) num = totalSlides;
      currentSlide = num;

      document.querySelectorAll('.slide-page').forEach(el => {{
        el.classList.remove('active');
      }});
      const activeEl = document.querySelector(`.slide-page[data-slide="${{num}}"]`);
      if (activeEl) activeEl.classList.add('active');

      document.getElementById('slide-indicator').textContent = `${{String(num).padStart(2, '0')}} / ${{String(totalSlides).padStart(2, '0')}}`;
      document.getElementById('progress-fill').style.width = `${{(num / totalSlides) * 100}}%`;

      document.querySelectorAll('.grid-item').forEach(el => el.classList.remove('active'));
      const activeGrid = document.querySelector(`.grid-item[data-slide="${{num}}"]`);
      if (activeGrid) activeGrid.classList.add('active');

      updateNotes(num);
    }}

    function updateNotes(num) {{
      const data = speakerNotes[num] || {{ goal: 'No notes', talkTrack: 'No talk track', timing: 'N/A' }};
      document.getElementById('notes-title').innerHTML = `Speaker Notes &middot; Slide ${{String(num).padStart(2, '0')}}`;
      document.getElementById('notes-body').innerHTML = `
        <div class="notes-tag">PEDAGOGICAL GOAL</div>
        <p>${{data.goal}}</p>
        
        <div class="notes-tag">TALK TRACK &amp; DELIVERY</div>
        <p>${{data.talkTrack}}</p>
        
        <div class="notes-box">
          <strong>Session Timing:</strong> ${{data.timing}}
        </div>
      `;
    }}

    window.addEventListener('keydown', (e) => {{
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        e.preventDefault();
        showSlide(currentSlide + 1);
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault();
        showSlide(currentSlide - 1);
      }} else if (e.key === 'Home') {{
        e.preventDefault();
        showSlide(1);
      }} else if (e.key === 'End') {{
        e.preventDefault();
        showSlide(totalSlides);
      }} else if (e.key.toLowerCase() === 'n') {{
        toggleNotes();
      }} else if (e.key.toLowerCase() === 'g') {{
        toggleGrid();
      }} else if (e.key.toLowerCase() === 'f') {{
        toggleFullscreen();
      }} else if (e.key === 'Escape') {{
        closeModals();
      }}
    }});

    document.getElementById('btn-prev').addEventListener('click', () => showSlide(currentSlide - 1));
    document.getElementById('btn-next').addEventListener('click', () => showSlide(currentSlide + 1));
    document.getElementById('btn-notes').addEventListener('click', toggleNotes);
    document.getElementById('btn-close-notes').addEventListener('click', toggleNotes);
    document.getElementById('btn-grid').addEventListener('click', toggleGrid);
    document.getElementById('btn-close-grid').addEventListener('click', toggleGrid);
    document.getElementById('btn-fs').addEventListener('click', toggleFullscreen);

    function toggleNotes() {{
      document.getElementById('notes-drawer').classList.toggle('open');
    }}

    function toggleGrid() {{
      const overlay = document.getElementById('grid-overlay');
      overlay.classList.toggle('open');
    }}

    function closeModals() {{
      document.getElementById('notes-drawer').classList.remove('open');
      document.getElementById('grid-overlay').classList.remove('open');
    }}

    function toggleFullscreen() {{
      if (!document.fullscreenElement) {{
        document.documentElement.requestFullscreen().catch(() => {{}});
      }} else {{
        if (document.exitFullscreen) document.exitFullscreen();
      }}
    }}

    window.addEventListener('resize', scaleStage);

    window.addEventListener('DOMContentLoaded', () => {{
      scaleStage();
      document.querySelectorAll('.grid-item').forEach(card => {{
        const sNum = card.getAttribute('data-slide');
        card.addEventListener('click', () => {{
          showSlide(parseInt(sNum, 10));
          toggleGrid();
        }});
      }});
      showSlide(1);
    }});
  </script>
</body>
</html>'''
