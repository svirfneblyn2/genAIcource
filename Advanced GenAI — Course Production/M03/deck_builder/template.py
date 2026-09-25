# -*- coding: utf-8 -*-
# HTML and CSS Template for Advanced GenAI Module 03 Presentation Deck
# Calm Engineering Design System: 1440x810 native, vector SVG blueprints, interactive speaker notes

def render_deck(slides):
    total_slides = len(slides)
    tot_str = f"{total_slides:02d}"
    
    slides_html_list = []
    
    for s in slides:
        idx = s["index"]
        idx_str = f"{idx:02d}"
        active_class = " active" if idx == 1 else ""
        
        slide_html = f"""      <section class="slide-container{active_class}" id="slide-{idx_str}" data-slide="{idx}">
        <div class="slide-header">
          <div class="header-left">
            <span class="category-badge">{s["badge"]}</span>
            <h1 class="slide-title">{s["title"]}</h1>
            <p class="slide-subtitle">{s["subtitle"]}</p>
          </div>
          <div class="slide-counter">{idx_str} / {tot_str}</div>
        </div>
        <div class="slide-canvas">
          <div class="diagram-arena">
{s["svg"]}
          </div>
        </div>
        <div class="slide-footer">
          <div class="takeaway-pill">
            <span class="takeaway-tag">{s["takeaway_tag"]}</span>
            <span>{s["takeaway"]}</span>
          </div>
          <div class="footer-meta">ADVANCED GENAI | ARCHITECTURE TRACK</div>
        </div>
        <div class="speaker-notes-data" style="display: none;">
{s["notes"]}
        </div>
      </section>"""
        slides_html_list.append(slide_html)

    all_slides_html = "\n".join(slides_html_list)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Module 03: Vector Stores and RAG | Systems Engineering Deck</title>
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
      
      /* Functional Muted Technical Accents */
      --accent-blue: #60a5fa;
      --accent-green: #6ee7b7;
      --accent-amber: #e0c58e;
      --accent-coral: #d98585;
      --accent-purple: #b4a4e5;
      
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
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

    /* Main Deck Stage */
    main.stage-wrapper {{
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
      overflow: hidden;
      padding: 12px;
    }}

    .slide-viewport {{
      width: 1440px;
      height: 810px;
      position: relative;
      background-color: var(--bg-canvas);
      transform-origin: center center;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      flex-shrink: 0;
    }}

    .slide-container {{
      width: 100%;
      height: 100%;
      position: absolute;
      top: 0;
      left: 0;
      display: none;
      flex-direction: column;
      padding: 38px 48px 24px 48px;
      background-color: var(--bg-canvas);
      background-image: 
        radial-gradient(circle at 100% 0%, rgba(96, 165, 250, 0.03) 0%, transparent 40%),
        radial-gradient(circle at 0% 100%, rgba(180, 164, 229, 0.03) 0%, transparent 40%);
    }}

    .slide-container.active {{
      display: flex;
    }}

    /* Slide Header */
    .slide-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 14px;
      position: relative;
    }}

    .header-left {{
      display: flex;
      flex-direction: column;
      gap: 5px;
      max-width: 1100px;
    }}

    .category-badge {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent-blue);
      background-color: rgba(96, 165, 250, 0.08);
      border: 1px solid rgba(96, 165, 250, 0.2);
      padding: 3px 9px;
      border-radius: 4px;
      width: fit-content;
    }}

    .category-badge::before {{
      content: "";
      display: inline-block;
      width: 5px;
      height: 5px;
      border-radius: 50%;
      background-color: var(--accent-blue);
    }}

    .slide-title {{
      font-size: 26px;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-main);
      line-height: 1.15;
    }}

    .slide-subtitle {{
      font-size: 13.5px;
      color: var(--text-muted);
      font-weight: 400;
      line-height: 1.35;
    }}

    .slide-counter {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 500;
      color: var(--text-dim);
      background-color: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      padding: 4px 10px;
      border-radius: 4px;
    }}

    /* Slide Canvas Arena */
    .slide-canvas {{
      flex: 1;
      width: 100%;
      position: relative;
      margin-bottom: 12px;
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      background-color: rgba(20, 28, 40, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 12px;
      overflow: hidden;
    }}

    .diagram-arena {{
      width: 100%;
      height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
    }}

    .diagram-arena svg {{
      width: 100%;
      height: 100%;
      max-height: 520px;
    }}

    /* Footer Takeaway Bar */
    .slide-footer {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-subtle);
      padding-top: 10px;
      height: 38px;
    }}

    .takeaway-pill {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-size: 12.5px;
      color: var(--text-main);
      font-weight: 500;
    }}

    .takeaway-tag {{
      font-family: var(--font-mono);
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--accent-amber);
      background-color: rgba(224, 197, 142, 0.12);
      border: 1px solid rgba(224, 197, 142, 0.3);
      padding: 2px 7px;
      border-radius: 3px;
    }}

    .footer-meta {{
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--text-dim);
    }}

    /* SVG Base Styling */
    text {{
      font-family: var(--font-sans);
    }}
    .text-title {{ font-weight: 700; fill: #ffffff; }}
    .text-h1 {{ font-weight: 600; fill: #f8fafc; }}
    .text-h2 {{ font-weight: 600; fill: var(--text-muted); }}
    .text-p {{ font-weight: 400; fill: #cbd5e1; }}
    .text-muted {{ font-weight: 400; fill: #94a3b8; }}
    .text-dim {{ font-weight: 400; fill: #64748b; }}
    .text-mono {{ font-family: var(--font-mono); font-weight: 500; }}
    .text-mono-bold {{ font-family: var(--font-mono); font-weight: 700; }}

    /* Interactive Speaker Notes Drawer */
    .notes-drawer {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      height: 280px;
      background-color: #0b0f16;
      border-top: 2px solid var(--border-focus);
      box-shadow: 0 -10px 25px rgba(0, 0, 0, 0.8);
      z-index: 1000;
      transform: translateY(100%);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
    }}

    .notes-drawer.open {{
      transform: translateY(0);
    }}

    .notes-header {{
      padding: 10px 24px;
      background-color: var(--bg-surface);
      border-bottom: 1px solid var(--border-subtle);
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .notes-title {{
      font-family: var(--font-mono);
      font-size: 12px;
      font-weight: 600;
      color: var(--accent-blue);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .notes-close-btn {{
      background: none;
      border: 1px solid var(--border-subtle);
      color: var(--text-muted);
      cursor: pointer;
      font-family: var(--font-mono);
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 3px;
    }}

    .notes-content {{
      flex: 1;
      padding: 16px 24px;
      overflow-y: auto;
      font-size: 13.5px;
      line-height: 1.6;
      color: #e2e8f0;
      user-select: text;
    }}

    .notes-content h4 {{
      font-size: 12px;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      color: var(--accent-amber);
      margin: 8px 0 4px 0;
      font-family: var(--font-mono);
    }}

    .notes-content p {{
      margin-bottom: 8px;
    }}

    /* Grid Overview Modal */
    .grid-modal {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: rgba(14, 19, 27, 0.95);
      backdrop-filter: blur(8px);
      z-index: 2000;
      display: none;
      flex-direction: column;
      padding: 30px;
    }}

    .grid-modal.open {{
      display: flex;
    }}

    .grid-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 20px;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 12px;
    }}

    .grid-title {{
      font-size: 18px;
      font-weight: 700;
      color: #fff;
    }}

    .grid-container {{
      flex: 1;
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 16px;
      overflow-y: auto;
      padding-right: 8px;
    }}

    .grid-card {{
      background-color: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 14px;
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      flex-direction: column;
      gap: 8px;
      height: 130px;
    }}

    .grid-card:hover {{
      border-color: var(--accent-blue);
      transform: translateY(-2px);
    }}

    .grid-card.active {{
      border-color: var(--border-focus);
      background-color: rgba(59, 130, 246, 0.08);
    }}

    .grid-card-num {{
      font-family: var(--font-mono);
      font-size: 11px;
      color: var(--accent-blue);
      font-weight: 600;
    }}

    .grid-card-title {{
      font-size: 13px;
      font-weight: 600;
      color: #fff;
      line-height: 1.3;
    }}

    /* Micro Control Toolbar */
    .controls-toolbar {{
      position: fixed;
      bottom: 16px;
      right: 16px;
      display: flex;
      align-items: center;
      gap: 6px;
      background-color: rgba(20, 28, 40, 0.85);
      border: 1px solid var(--border-subtle);
      border-radius: 6px;
      padding: 4px 6px;
      z-index: 500;
      backdrop-filter: blur(4px);
    }}

    .tool-btn {{
      background: none;
      border: none;
      color: var(--text-muted);
      cursor: pointer;
      font-family: var(--font-mono);
      font-size: 11px;
      padding: 4px 8px;
      border-radius: 4px;
      transition: all 0.1s ease;
    }}

    .tool-btn:hover {{
      color: #fff;
      background-color: rgba(255, 255, 255, 0.08);
    }}

    /* Print / PDF Export Optimization (Exact 1440pt x 810pt Vector Export) */
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
      .slide-viewport {{
        position: static !important;
        height: auto !important;
        width: 1440pt !important;
        overflow: visible !important;
        display: block !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        margin: 0 !important;
        padding: 0 !important;
        transform: none !important;
      }}
      .slide-container {{
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
        padding: 38px 48px 24px 48px !important;
        margin: 0 !important;
      }}
      .slide-container:last-of-type {{
        break-after: avoid !important;
        page-break-after: avoid !important;
      }}
      .controls-toolbar, .notes-drawer, .grid-modal {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body>

  <main class="stage-wrapper">
    <div class="slide-viewport" id="viewport">
{all_slides_html}
    </div>
  </main>

  <!-- Interactive Controls Toolbar -->
  <div class="controls-toolbar">
    <button class="tool-btn" id="btn-prev" title="Previous Slide (Left Arrow / Page Up)">Prev</button>
    <button class="tool-btn" id="btn-next" title="Next Slide (Right Arrow / Space / Page Down)">Next</button>
    <span style="color: var(--border-subtle);">|</span>
    <button class="tool-btn" id="btn-notes" title="Toggle Speaker Notes (N)">Notes [N]</button>
    <button class="tool-btn" id="btn-grid" title="Slide Overview Grid (G)">Grid [G]</button>
    <button class="tool-btn" id="btn-fullscreen" title="Toggle Fullscreen (F)">FS [F]</button>
  </div>

  <!-- Speaker Notes Drawer -->
  <div class="notes-drawer" id="notes-drawer">
    <div class="notes-header">
      <span class="notes-title" id="notes-slide-indicator">Speaker Notes: Slide 01</span>
      <button class="notes-close-btn" id="btn-close-notes">Esc / Close</button>
    </div>
    <div class="notes-content" id="notes-body">
      <!-- Dynamic notes content -->
    </div>
  </div>

  <!-- Slide Overview Grid Modal -->
  <div class="grid-modal" id="grid-modal">
    <div class="grid-header">
      <span class="grid-title">Slide Overview Grid</span>
      <button class="notes-close-btn" id="btn-close-grid">Esc / Close</button>
    </div>
    <div class="grid-container" id="grid-container">
      <!-- Dynamic grid cards -->
    </div>
  </div>

  <script>
    // Slide Navigation & Viewport Engine
    (function() {{
      const slides = document.querySelectorAll('.slide-container');
      const totalSlides = slides.length;
      let currentIndex = 0;
      
      const viewport = document.getElementById('viewport');
      const notesDrawer = document.getElementById('notes-drawer');
      const notesBody = document.getElementById('notes-body');
      const notesIndicator = document.getElementById('notes-slide-indicator');
      const gridModal = document.getElementById('grid-modal');
      const gridContainer = document.getElementById('grid-container');

      // Populate Grid
      slides.forEach((s, idx) => {{
        const title = s.querySelector('.slide-title') ? s.querySelector('.slide-title').textContent : `Slide ${{idx+1}}`;
        const card = document.createElement('div');
        card.className = `grid-card ${{idx === 0 ? 'active' : ''}}`;
        card.dataset.index = idx;
        card.innerHTML = `
          <span class="grid-card-num">Slide ${{String(idx+1).padStart(2, '0')}} / ${{totalSlides}}</span>
          <span class="grid-card-title">${{title}}</span>
        `;
        card.addEventListener('click', () => {{
          goToSlide(idx);
          toggleGrid(false);
        }});
        gridContainer.appendChild(card);
      }});

      // Responsive Auto-Scaling (1440x810 native)
      function resizeViewport() {{
        const wrapper = document.querySelector('.stage-wrapper');
        const availWidth = wrapper.clientWidth - 24;
        const availHeight = wrapper.clientHeight - 24;
        
        const scaleX = availWidth / 1440;
        const scaleY = availHeight / 810;
        const scale = Math.min(scaleX, scaleY);
        
        viewport.style.transform = `scale(${{scale}})`;
      }}

      window.addEventListener('resize', resizeViewport);
      resizeViewport();

      function updateSlide(index) {{
        slides.forEach((s, idx) => {{
          s.classList.toggle('active', idx === index);
        }});

        // Update speaker notes
        const currentSlide = slides[index];
        const notesElem = currentSlide.querySelector('.speaker-notes-data');
        if (notesElem) {{
          notesBody.innerHTML = notesElem.innerHTML;
        }} else {{
          notesBody.innerHTML = "<p>No speaker notes for this slide.</p>";
        }}
        notesIndicator.textContent = `Speaker Notes: Slide ${{String(index+1).padStart(2, '0')}} / ${{totalSlides}}`;

        // Update Grid Active State
        document.querySelectorAll('.grid-card').forEach((gc, idx) => {{
          gc.classList.toggle('active', idx === index);
        }});
      }}

      function goToSlide(index) {{
        if (index >= 0 && index < totalSlides) {{
          currentIndex = index;
          updateSlide(currentIndex);
        }}
      }}

      function nextSlide() {{
        if (currentIndex < totalSlides - 1) {{
          goToSlide(currentIndex + 1);
        }}
      }}

      function prevSlide() {{
        if (currentIndex > 0) {{
          goToSlide(currentIndex - 1);
        }}
      }}

      function toggleNotes(force) {{
        const isOpen = force !== undefined ? force : !notesDrawer.classList.contains('open');
        notesDrawer.classList.toggle('open', isOpen);
      }}

      function toggleGrid(force) {{
        const isOpen = force !== undefined ? force : !gridModal.classList.contains('open');
        gridModal.classList.toggle('open', isOpen);
      }}

      function toggleFullscreen() {{
        if (!document.fullscreenElement) {{
          document.documentElement.requestFullscreen().catch(err => console.error(err));
        }} else {{
          if (document.exitFullscreen) {{
            document.exitFullscreen();
          }}
        }}
      }}

      // Keyboard Controls
      window.addEventListener('keydown', (e) => {{
        if (gridModal.classList.contains('open')) {{
          if (e.key === 'Escape' || e.key === 'g' || e.key === 'G') {{
            toggleGrid(false);
          }}
          return;
        }}

        switch(e.key) {{
          case 'ArrowRight':
          case 'Space':
          case 'PageDown':
            e.preventDefault();
            nextSlide();
            break;
          case 'ArrowLeft':
          case 'PageUp':
            e.preventDefault();
            prevSlide();
            break;
          case 'Home':
            e.preventDefault();
            goToSlide(0);
            break;
          case 'End':
            e.preventDefault();
            goToSlide(totalSlides - 1);
            break;
          case 'n':
          case 'N':
            toggleNotes();
            break;
          case 'g':
          case 'G':
            toggleGrid();
            break;
          case 'f':
          case 'F':
            toggleFullscreen();
            break;
          case 'Escape':
            toggleNotes(false);
            toggleGrid(false);
            break;
        }}
      }});

      // Button Bindings
      document.getElementById('btn-prev').addEventListener('click', prevSlide);
      document.getElementById('btn-next').addEventListener('click', nextSlide);
      document.getElementById('btn-notes').addEventListener('click', () => toggleNotes());
      document.getElementById('btn-close-notes').addEventListener('click', () => toggleNotes(false));
      document.getElementById('btn-grid').addEventListener('click', () => toggleGrid());
      document.getElementById('btn-close-grid').addEventListener('click', () => toggleGrid(false));
      document.getElementById('btn-fullscreen').addEventListener('click', toggleFullscreen);

      // Initialize
      updateSlide(0);
    }})();
  </script>
</body>
</html>
"""
