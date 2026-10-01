"""Comprehensive Bilingual Deck Generator for Lesson 04: Image Generation and Editing APIs
Produces:
  - presentation_L04_Image_Generation_APIs.html (Russian)
  - presentation_L04_Image_Generation_APIs_EN.html (English)
Strictly adheres to:
  - 21 canonical slides from GEMINI.md
  - C4 Dark Engineering Theme (#0c111a, #121927, #172134, #38bdf8, #34d399, #fbbf24, #f87171, #c084fc)
  - Zero-clipping flexbox layouts
  - True 100% bilingual parity (zero Cyrillic in English deck)
  - Full verbatim speaker notes drawer (key N)
  - Modal grid overview (key G)
  - Fullscreen toggle (key F)
  - Interactive 5-minute break timer on Slide 15
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()

def render_html(lang="ru"):
    is_ru = (lang == "ru")
    title_doc = "Урок 04: Генерация и редактирование изображений через API | GenAI Basics" if is_ru else "Lesson 04: Image Generation and Editing APIs | GenAI Basics"
    notes_label = "Суфлер спикера (Заметки • Клавиша N)" if is_ru else "Speaker Notes (Key N)"
    grid_label = "Обзор всех 21 слайдов (Клавиша G)" if is_ru else "All 21 Slides Overview (Key G)"
    start_5m = "СТАРТ 5 МИН" if is_ru else "START 5 MIN"
    pause_txt = "ПАУЗА" if is_ru else "PAUSE"
    time_up = "ВРЕМЯ ВЫШЛО" if is_ru else "TIME IS UP"
    reset_txt = "СБРОС" if is_ru else "RESET"
    footer_mod = "МОДУЛЬ 2 • МУЛЬТИМОДАЛЬНОСТЬ" if is_ru else "MODULE 2 • MULTIMODALITY"

    html = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title_doc}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg-canvas: #0c111a;
      --bg-surface: #121927;
      --bg-card: #172134;
      --bg-card-subtle: #1e2a42;
      
      --border-subtle: rgba(255, 255, 255, 0.08);
      --border-strong: rgba(255, 255, 255, 0.16);
      --border-card: rgba(148, 163, 184, 0.16);
      
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      
      --c4-primary: #38bdf8;
      --c4-indigo: #818cf8;
      --c4-success: #34d399;
      --c4-warning: #fbbf24;
      --c4-danger: #f87171;
      --c4-purple: #c084fc;
      
      --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      --font-mono: 'JetBrains Mono', monospace;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      background-color: var(--bg-canvas);
      color: var(--text-main);
      font-family: var(--font-sans);
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      display: flex;
      user-select: none;
      -webkit-font-smoothing: antialiased;
    }}

    main.stage-wrapper {{
      flex: 1;
      position: relative;
      display: flex;
      align-items: center;
      justify-content: center;
      background: var(--bg-canvas);
      padding: 16px;
      overflow: hidden;
    }}

    .slide-frame {{
      width: 96vw;
      max-width: 1560px;
      aspect-ratio: 16 / 9;
      max-height: 94vh;
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 12px;
      box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }}

    .slide-page {{
      display: none;
      flex: 1 1 0;
      height: 100%;
      min-height: 0;
      max-height: 100%;
      flex-direction: column;
      padding: 24px 38px 16px 38px;
      position: relative;
      animation: fadeIn 0.15s ease-out;
      overflow: hidden;
      box-sizing: border-box;
    }}

    .slide-page.active {{
      display: flex;
    }}

    .slide-page.visual-slide {{
      padding: 20px 32px 14px 32px;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: scale(0.996); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    .slide-topbar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 6px;
      flex-shrink: 0;
    }}

    .slide-tag {{
      font-family: var(--font-mono);
      font-size: 12.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--c4-primary);
      display: inline-flex;
      align-items: center;
      gap: 7px;
    }}

    .slide-tag::before {{
      content: '';
      display: inline-block;
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--c4-primary);
    }}

    .slide-module-info {{
      font-size: 13px;
      color: var(--text-dim);
      font-family: var(--font-mono);
      font-weight: 500;
    }}

    .slide-title {{
      font-size: 30px;
      font-weight: 800;
      letter-spacing: -0.025em;
      color: #fff;
      line-height: 1.15;
      margin-bottom: 3px;
      flex-shrink: 0;
    }}

    .slide-subtitle {{
      font-size: 15px;
      color: var(--text-muted);
      line-height: 1.35;
      margin-bottom: 12px;
      flex-shrink: 0;
    }}

    .slide-content-arena {{
      flex: 1 1 0;
      min-height: 0;
      max-height: 100%;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
      margin-bottom: 8px;
    }}

    .slide-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: auto;
      padding-top: 8px;
      border-top: 1px solid var(--border-subtle);
      font-family: var(--font-mono);
      font-size: 12px;
      color: var(--text-dim);
      flex-shrink: 0;
    }}

    .footer-left {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .footer-right {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}

    .progress-bar-container {{
      width: 90px;
      height: 4px;
      background: rgba(255, 255, 255, 0.08);
      border-radius: 2px;
      overflow: hidden;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: var(--c4-primary);
      border-radius: 2px;
      transition: width 0.2s ease;
    }}

    .slide-counter {{
      font-weight: 600;
      color: var(--text-muted);
    }}

    .c4-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-card);
      border-radius: 10px;
      padding: 16px 20px;
      display: flex;
      flex-direction: column;
      position: relative;
      overflow: hidden;
    }}

    .c4-card.highlight {{
      border-color: rgba(56, 189, 248, 0.35);
      background: linear-gradient(180deg, rgba(56, 189, 248, 0.05) 0%, var(--bg-card) 100%);
    }}

    .c4-card.accent-emerald {{
      border-color: rgba(52, 211, 153, 0.35);
      background: linear-gradient(180deg, rgba(52, 211, 153, 0.05) 0%, var(--bg-card) 100%);
    }}

    .c4-card.accent-amber {{
      border-color: rgba(251, 191, 36, 0.35);
      background: linear-gradient(180deg, rgba(251, 191, 36, 0.05) 0%, var(--bg-card) 100%);
    }}

    .c4-card.accent-red {{
      border-color: rgba(248, 113, 113, 0.35);
      background: linear-gradient(180deg, rgba(248, 113, 113, 0.05) 0%, var(--bg-card) 100%);
    }}

    .c4-card.accent-purple {{
      border-color: rgba(192, 132, 252, 0.35);
      background: linear-gradient(180deg, rgba(192, 132, 252, 0.05) 0%, var(--bg-card) 100%);
    }}

    .card-label {{
      font-family: var(--font-mono);
      font-size: 11.5px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      margin-bottom: 5px;
      color: var(--c4-primary);
    }}

    .card-title {{
      font-size: 16.5px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 6px;
      line-height: 1.25;
    }}

    .card-desc {{
      font-size: 13.5px;
      color: var(--text-muted);
      line-height: 1.45;
    }}

    .visual-container {{
      flex: 1 1 0;
      min-height: 0;
      max-height: 100%;
      display: flex;
      align-items: center;
      justify-content: center;
      background: rgba(0, 0, 0, 0.3);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      overflow: hidden;
      padding: 6px;
    }}

    .visual-container img {{
      max-width: 100%;
      max-height: 100%;
      object-fit: contain;
      border-radius: 6px;
    }}

    /* Speaker Notes Drawer */
    #speakerNotesDrawer {{
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      max-height: 260px;
      background: #090d15;
      border-top: 2px solid var(--c4-primary);
      padding: 18px 28px;
      box-shadow: 0 -10px 30px rgba(0,0,0,0.8);
      z-index: 1000;
      transform: translateY(105%);
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1);
      display: flex;
      flex-direction: column;
      gap: 8px;
      overflow-y: auto;
    }}

    #speakerNotesDrawer.open {{
      transform: translateY(0);
    }}

    .drawer-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border-subtle);
      padding-bottom: 8px;
    }}

    .drawer-title {{
      font-family: var(--font-mono);
      font-size: 13px;
      font-weight: 700;
      color: var(--c4-primary);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }}

    .drawer-close {{
      background: none;
      border: none;
      color: var(--text-dim);
      font-size: 18px;
      cursor: pointer;
    }}

    .drawer-close:hover {{ color: #fff; }}

    .drawer-body {{
      font-size: 14.5px;
      line-height: 1.55;
      color: #e2e8f0;
      white-space: pre-wrap;
    }}

    /* Grid Overview Modal */
    #gridModal {{
      position: fixed;
      top: 0; left: 0; right: 0; bottom: 0;
      background: rgba(12, 17, 26, 0.95);
      backdrop-filter: blur(10px);
      z-index: 2000;
      display: none;
      flex-direction: column;
      padding: 30px;
      overflow-y: auto;
    }}

    #gridModal.open {{ display: flex; }}

    .grid-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
    }}

    .grid-title {{
      font-size: 20px;
      font-weight: 700;
      color: #fff;
    }}

    .grid-cards {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
      gap: 16px;
    }}

    .grid-card-item {{
      background: var(--bg-surface);
      border: 1px solid var(--border-subtle);
      border-radius: 8px;
      padding: 14px;
      cursor: pointer;
      transition: all 0.15s ease;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }}

    .grid-card-item:hover {{
      border-color: var(--c4-primary);
      transform: translateY(-2px);
    }}

    .grid-card-num {{
      font-family: var(--font-mono);
      font-size: 11px;
      font-weight: 700;
      color: var(--c4-primary);
    }}

    .grid-card-title {{
      font-size: 13px;
      font-weight: 600;
      color: #fff;
      line-height: 1.3;
    }}

    .row {{ display: flex; gap: 14px; }}
    .col {{ display: flex; flex-direction: column; gap: 12px; }}
    .flex-1 {{ flex: 1; }}
    .flex-15 {{ flex: 1.5; }}
    .flex-2 {{ flex: 2; }}

    code {{
      font-family: var(--font-mono);
      background: rgba(255, 255, 255, 0.08);
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 13px;
      color: var(--c4-primary);
    }}

    /* Export & Print Styles (1440pt x 810pt Vector PDF) */
    @media print {{
      @page {{
        size: 1440pt 810pt;
        margin: 0;
      }}
      html, body {{
        background: var(--bg-canvas) !important;
        color: var(--text-main) !important;
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
        aspect-ratio: auto !important;
        max-width: none !important;
        max-height: none !important;
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
        background: var(--bg-surface) !important;
        padding: 24px 38px 16px 38px !important;
        margin: 0 !important;
      }}
      .slide-page:last-of-type {{
        break-after: avoid !important;
        page-break-after: avoid !important;
      }}
      #speakerNotesDrawer, #gridModal {{
        display: none !important;
      }}
    }}
  </style>
</head>
<body>
  <main class="stage-wrapper">
    <div class="slide-frame">
"""

    def slide_header(num, tag, title, subtitle):
        return f"""
        <div class="slide-topbar">
          <div class="slide-tag">{tag}</div>
          <div class="slide-module-info">{footer_mod} • 2026</div>
        </div>
        <div class="slide-title">{title}</div>
        <div class="slide-subtitle">{subtitle}</div>
        """

    def slide_footer(num):
        pct = round((num / 21) * 100)
        return f"""
        <div class="slide-footer">
          <div class="footer-left"><span>EPAM Systems</span><span>•</span><span>GenAI Basics</span></div>
          <div class="footer-right">
            <div class="progress-bar-container"><div class="progress-bar-fill" id="fill-s{num}" style="width: {pct}%"></div></div>
            <span class="slide-counter" id="counter-s{num}">{num:02d} / 21</span>
          </div>
        </div>
        """

    # -------------------------------------------------------------
    # SLIDE 01: COVER
    # -------------------------------------------------------------
    s01_tag = "МОДУЛЬ 2 • УРОК 04" if is_ru else "MODULE 2 • LESSON 04"
    s01_title = "Генерация и редактирование изображений через API" if is_ru else "Image Generation and Editing APIs"
    s01_sub = "От случайных пикселей к контролируемым инженерным пайплайнам" if is_ru else "From Random Pixels to Controlled Production Pipelines"
    s01_axiom = (
        "Аксиома 10/90: Вызов модели через API — это лишь 10% решения. 90% продакшена — это маски, фиксация геометрии, "
        "объектные хранилища S3/GCS, декодирование Base64, аудит метаданных и шлюзы модерации."
        if is_ru else
        "The 10/90 Axiom: The model API call is only 10% of the system. 90% of production reality is masks, geometric preservation, "
        "S3/GCS object storage, Base64 decoding, metadata audit trails, and moderation review gates."
    )
    s01_p1_t = "Визуальные примитивы" if is_ru else "Visual Primitives"
    s01_p1_d = "Text-to-Image, Inpainting, Outpainting, маски и разделение сигналов референсов." if is_ru else "Text-to-Image, Inpainting, Outpainting, masks, and decoupled reference signals."
    s01_p2_t = "Контрактный контроль" if is_ru else "Contractual Control"
    s01_p2_d = "Анатомия промпта как техзадания: неприкосновенные свойства и критерии приемки." if is_ru else "Prompt anatomy as an engineering spec: sacred attributes and acceptance criteria."
    s01_p3_t = "Продакшен-пайплайн" if is_ru else "Production Pipeline"
    s01_p3_d = "Аудит метаданных, Base64 декодирование, Blast Radius и Human-in-the-Loop." if is_ru else "Metadata audit trails, Base64 decoding, Blast Radius, and Human-in-the-Loop gates."
    s01_notes = "Вводный слайд. Опрос аудитории в чате: 1 - вызывали Image API кодом, 2 - только веб-интерфейсы." if is_ru else "Introduction. Audience check in chat: 1 - called Image APIs via code, 2 - web browser UIs only."

    html += f"""
      <section class="slide-page active" id="slide-1">
        {slide_header(1, s01_tag, s01_title, s01_sub)}
        <div class="slide-content-arena" style="gap: 16px;">
          <div class="c4-card highlight" style="padding: 22px 26px; border-left: 5px solid var(--c4-primary);">
            <div class="card-label">{"АКСИОМА 10/90 В COMPUTER VISION" if is_ru else "THE 10/90 AXIOM IN COMPUTER VISION"}</div>
            <div style="font-size: 17px; font-weight: 600; color: #fff; line-height: 1.45;">
              «{s01_axiom}»
            </div>
          </div>
          <div class="row" style="flex: 1; gap: 16px;">
            <div class="c4-card flex-1">
              <div class="card-label" style="color: var(--c4-primary);">01 • PRIMITIVES</div>
              <div class="card-title">{s01_p1_t}</div>
              <div class="card-desc">{s01_p1_d}</div>
            </div>
            <div class="c4-card flex-1">
              <div class="card-label" style="color: var(--c4-success);">02 • CONTROL</div>
              <div class="card-title">{s01_p2_t}</div>
              <div class="card-desc">{s01_p2_d}</div>
            </div>
            <div class="c4-card flex-1">
              <div class="card-label" style="color: var(--c4-warning);">03 • PIPELINE</div>
              <div class="card-title">{s01_p3_t}</div>
              <div class="card-desc">{s01_p3_d}</div>
            </div>
          </div>
        </div>
        {slide_footer(1)}
        <div class="speaker-notes" style="display:none;">{s01_notes}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 02: INSTRUCTOR PROFILE
    # -------------------------------------------------------------
    s02_tag = "ИНСТРУКТОР" if is_ru else "INSTRUCTOR"
    s02_title = "Игорь Рубанович" if is_ru else "Igor Rubanovich"
    s02_sub = "Engineering Manager II & AI Ambassador @ EPAM Systems"
    s02_c1_t = "Архитектура и системное лидерство" if is_ru else "Architecture & Systems Leadership"
    s02_c1_d = "15+ лет в IT-инженерии, управление распределенными командами и внедрение AI-ассистентов в корпоративный SDLC." if is_ru else "15+ years in enterprise software, distributed leadership, and embedding AI assistants into engineering workflows."
    s02_c2_t = "Архитектор Creator Tools (Пет-проект)" if is_ru else "Architect of Creator Tools (Pet-Project)"
    s02_c2_d = "Создатель и архитектор Creator Tools — набора AI-инструментов для авторов YouTube, помогающих экономить время на производстве контента, оптимизировать процессы и зарабатывать больше." if is_ru else "Creator and architect of Creator Tools — a suite of AI tools for YouTube creators designed to save production time, streamline content workflows, and increase earnings."
    s02_c3_t = "EPAM CodeMie @ Dawn Foods"
    s02_c3_d = "Ускорение SDLC на 35% при разработке фич, модульном тестировании и архитектурной документации." if is_ru else "35% SDLC acceleration across feature development, unit testing, and architectural documentation."
    s02_c4_t = "Сдача домашних заданий" if is_ru else "Homework Submissions"
    s02_c4_d = "Коллаборация в GitHub и ревью кода: <code>ihar_rubanovich@epam.com</code>" if is_ru else "GitHub collaboration and code reviews: <code>ihar_rubanovich@epam.com</code>"
    s02_notes = "Опыт практического R&D (Creator Tools для YouTube как пет-проект) и корпоративные кейсы (CodeMie @ Dawn Foods)." if is_ru else "Hands-on AI R&D (Creator Tools for YouTube pet-project) and enterprise delivery (CodeMie @ Dawn Foods)."

    html += f"""
      <section class="slide-page" id="slide-2">
        {slide_header(2, s02_tag, s02_title, s02_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 20px;">
            <div style="flex: 0 0 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; background: rgba(0,0,0,0.25); border: 1px solid var(--border-subtle); border-radius: 10px; padding: 16px;">
              <img src="assets/speaker_photo.jpg" alt="Igor Rubanovich" style="width: 170px; height: 170px; border-radius: 50%; object-fit: cover; border: 2px solid var(--c4-primary); margin-bottom: 12px;">
              <div style="font-weight: 700; color: #fff; font-size: 15px; text-align: center;">Igor Rubanovich</div>
              <div style="font-family: var(--font-mono); font-size: 12px; color: var(--text-dim); text-align: center; margin-top: 4px;">ihar_rubanovich@epam.com</div>
            </div>
            <div style="flex: 1; display: grid; grid-template-columns: 1fr 1fr; gap: 14px;">
              <div class="c4-card flex-1">
                <div class="card-label">ENTERPRISE DELIVERY</div>
                <div class="card-title">{s02_c1_t}</div>
                <div class="card-desc">{s02_c1_d}</div>
              </div>
              <div class="c4-card highlight flex-1">
                <div class="card-label" style="color: var(--c4-primary);">{"ПРАКТИЧЕСКИЙ AI R&D" if is_ru else "HANDS-ON AI R&D"}</div>
                <div class="card-title">{s02_c2_t}</div>
                <div class="card-desc">{s02_c2_d}</div>
              </div>
              <div class="c4-card flex-1">
                <div class="card-label" style="color: var(--c4-success);">{"РЕАЛЬНЫЙ КЕЙС" if is_ru else "PRODUCTION CASE"}</div>
                <div class="card-title">{s02_c3_t}</div>
                <div class="card-desc">{s02_c3_d}</div>
              </div>
              <div class="c4-card flex-1">
                <div class="card-label" style="color: var(--c4-warning);">{"ОБРАТНАЯ СВЯЗЬ" if is_ru else "OFFICIAL CONTACT"}</div>
                <div class="card-title">{s02_c4_t}</div>
                <div class="card-desc">{s02_c4_d}</div>
              </div>
            </div>
          </div>
        </div>
        {slide_footer(2)}
        <div class="speaker-notes" style="display:none;">{s02_notes}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 03: CURRICULUM ROADMAP
    # -------------------------------------------------------------
    s03_tag = "ДОРОЖНАЯ КАРТА" if is_ru else "ROADMAP"
    s03_title = "Дорожная карта курса: Где мы находимся" if is_ru else "Curriculum Roadmap: Where We Are"
    s03_sub = "16 занятий в 6 модулях: от текстовых BPE-токенов к мультимодальности и агентам" if is_ru else "16 lessons across 6 modules: from text BPE tokens to multimodality and autonomous agents"
    m1_t = "Фундамент и Core API" if is_ru else "Foundations & Core API"
    m1_d = "BPE-токены, промптинг, контекстное окно, вызовы API на Python, стриминг и структурированный JSON." if is_ru else "BPE tokens, prompt engineering, context windows, Python API calls, streaming, and structured JSON."
    m2_t = "Мультимодальность" if is_ru else "Multimodality"
    m2_d = (
        "• L04: Изображения и редактирование (API)<br>• L05: Видеогенерация (Runway, Kling, Sora)<br>• L06: Речь и аудио (ElevenLabs, Whisper)"
        if is_ru else
        "• L04: Image APIs & Inpainting<br>• L05: Video Generation (Runway, Kling, Sora)<br>• L06: Speech & Audio (ElevenLabs, Whisper)"
    )
    m3_t = "Инструменты инженера" if is_ru else "Developer Tooling"
    m3_d = "GitHub Copilot, экосистема Claude Artifacts, продвинутый анализ данных и генерация кода." if is_ru else "GitHub Copilot, Claude Artifacts, Advanced Data Analysis, and automated code generation."
    m4_t = "Локальный AI и открытые модели" if is_ru else "Local AI & Open Weights"
    m4_d = "LM Studio, Ollama, квантование весов, локальный инференс и облачный деплой на RunPod." if is_ru else "LM Studio, Ollama, weight quantization, local inference, and cloud deployment on RunPod."
    m5_t = "Агенты и протокол MCP" if is_ru else "Agents & MCP Protocol"
    m5_d = "Function Calling, создание первых автономных агентов, архитектура Model Context Protocol." if is_ru else "Function Calling, building first autonomous agents, Model Context Protocol architecture."
    m6_t = "Продакшен и Agentic IDE" if is_ru else "Production & Agentic IDEs"
    m6_d = "Быстрое прототипирование на Streamlit, безопасность и этика, Cursor, Windsurf, Claude Code." if is_ru else "Streamlit rapid prototyping, safety/guardrails, Cursor, Windsurf, and Claude Code CLI."

    html += f"""
      <section class="slide-page" id="slide-3">
        {slide_header(3, s03_tag, s03_title, s03_sub)}
        <div class="slide-content-arena" style="gap: 12px;">
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; flex: 1;">
            <div class="c4-card" style="opacity: 0.7;">
              <div class="card-label">{"МОДУЛЬ 1 • L01-L03" if is_ru else "MODULE 1 • L01-L03"}</div>
              <div class="card-title" style="color: var(--text-muted);">{m1_t}</div>
              <div class="card-desc">{m1_d}</div>
              <div style="margin-top: auto; color: var(--c4-success); font-family: var(--font-mono); font-size: 11.5px; font-weight: 700;">✓ {"ЗАВЕРШЕН" if is_ru else "COMPLETED"}</div>
            </div>
            <div class="c4-card highlight" style="border-width: 2px;">
              <div class="card-label" style="color: var(--c4-primary);">{"ВЫ ЗДЕСЬ • МОДУЛЬ 2" if is_ru else "YOU ARE HERE • MODULE 2"}</div>
              <div class="card-title" style="color: #fff;">{m2_t}</div>
              <div class="card-desc" style="color: #e2e8f0;">{m2_d}</div>
              <div style="margin-top: auto; color: var(--c4-primary); font-family: var(--font-mono); font-size: 11.5px; font-weight: 700;">▶ {"ТЕКУЩИЙ ЭТАП" if is_ru else "CURRENT PHASE"}</div>
            </div>
            <div class="c4-card" style="opacity: 0.7;">
              <div class="card-label">{"МОДУЛЬ 3 • L07-L09" if is_ru else "MODULE 3 • L07-L09"}</div>
              <div class="card-title" style="color: var(--text-muted);">{m3_t}</div>
              <div class="card-desc">{m3_d}</div>
              <div style="margin-top: auto; color: var(--text-dim); font-family: var(--font-mono); font-size: 11.5px;">⏳ {"СЛЕДУЮЩИЙ" if is_ru else "UPCOMING"}</div>
            </div>
            <div class="c4-card" style="opacity: 0.7;">
              <div class="card-label">{"МОДУЛЬ 4 • L10" if is_ru else "MODULE 4 • L10"}</div>
              <div class="card-title" style="color: var(--text-muted);">{m4_t}</div>
              <div class="card-desc">{m4_d}</div>
              <div style="margin-top: auto; color: var(--text-dim); font-family: var(--font-mono); font-size: 11.5px;">⏳ {"СЛЕДУЮЩИЙ" if is_ru else "UPCOMING"}</div>
            </div>
            <div class="c4-card" style="opacity: 0.7;">
              <div class="card-label">{"МОДУЛЬ 5 • L11-L13" if is_ru else "MODULE 5 • L11-L13"}</div>
              <div class="card-title" style="color: var(--text-muted);">{m5_t}</div>
              <div class="card-desc">{m5_d}</div>
              <div style="margin-top: auto; color: var(--text-dim); font-family: var(--font-mono); font-size: 11.5px;">⏳ {"СЛЕДУЮЩИЙ" if is_ru else "UPCOMING"}</div>
            </div>
            <div class="c4-card" style="opacity: 0.7;">
              <div class="card-label">{"МОДУЛЬ 6 • L14-L16" if is_ru else "MODULE 6 • L14-L16"}</div>
              <div class="card-title" style="color: var(--text-muted);">{m6_t}</div>
              <div class="card-desc">{m6_d}</div>
              <div style="margin-top: auto; color: var(--text-dim); font-family: var(--font-mono); font-size: 11.5px;">⏳ {"СЛЕДУЮЩИЙ" if is_ru else "UPCOMING"}</div>
            </div>
          </div>
        </div>
        {slide_footer(3)}
        <div class="speaker-notes" style="display:none;">{"Навигация по курсу. Мы переходим от токенов к мультимодальности." if is_ru else "Roadmap review. Moving from text tokens to multimodality."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 04: GITHUB WORKFLOW
    # -------------------------------------------------------------
    s04_tag = "СТАНДАРТ СДАЧИ" if is_ru else "SUBMISSION STANDARD"
    s04_title = "GitHub Workflow и структура артефактов" if is_ru else "GitHub Workflow & Artifact Structure"
    s04_sub = "Стандартизированная сдача домашек: ветка lesson-04 и воспроизводимый пакет" if is_ru else "Standardized homework submission: lesson-04 branch and reproducible artifact package"
    s04_p1_t = "Ветка lesson-04 и Pull Request" if is_ru else "lesson-04 Branch & Pull Request"
    s04_p1_d = "Все изменения вносятся в отдельную ветку. Открывается PR в main, в рецензенты добавляется ihar_rubanovich@epam.com. Никаких прямых пушей в main." if is_ru else "All changes committed to feature branch. Open PR to main, add ihar_rubanovich@epam.com as reviewer. Zero direct pushes to main."
    s04_p2_t = "Запрет приватных данных и закрытых брендов" if is_ru else "Data Privacy & Brand Governance"
    s04_p2_d = "Никаких реальных лиц сотрудников без письменного согласия, закрытых чертежей или невыпущенных продуктов. Используем открытые тестовые ассеты." if is_ru else "No real faces without consent, confidential blueprints, or unreleased assets. Use open synthetic references."

    html += f"""
      <section class="slide-page" id="slide-4">
        {slide_header(4, s04_tag, s04_title, s04_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 18px;">
            <div class="c4-card flex-1" style="font-family: var(--font-mono); font-size: 13px; line-height: 1.6; background: #080d14;">
              <div class="card-label" style="font-family: var(--font-sans);">{"ДЕРЕВО РЕПОЗИТОРИЯ • L04" if is_ru else "REPOSITORY TREE • L04"}</div>
              <div style="color: var(--c4-primary); font-weight: 700;">genai-homeworks/</div>
              <div style="color: var(--text-dim);">├── L01/</div>
              <div style="color: var(--text-dim);">├── L02/</div>
              <div style="color: var(--text-dim);">├── L03/</div>
              <div style="color: var(--c4-warning); font-weight: 700;">└── L04/</div>
              <div style="color: #e2e8f0; padding-left: 20px;">├── <strong style="color: var(--c4-primary);">brief.md</strong> <span style="color: var(--text-dim);"># Visual Generation Canvas</span></div>
              <div style="color: #e2e8f0; padding-left: 20px;">├── <strong style="color: #e2e8f0);">references/</strong> <span style="color: var(--text-dim);"># {"Исходные фото и маски" if is_ru else "Source references & masks"}</span></div>
              <div style="color: #e2e8f0; padding-left: 20px;">├── <strong style="color: #e2e8f0);">prompt_v1.txt</strong> <span style="color: var(--text-dim);"># {"Начальный промпт" if is_ru else "Initial prompt"}</span></div>
              <div style="color: #e2e8f0; padding-left: 20px;">├── <strong style="color: var(--c4-success);">prompt_v2.txt</strong> <span style="color: var(--text-dim);"># {"Промпт со спецификацией табу" if is_ru else "Production prompt with sacred rules"}</span></div>
              <div style="color: #e2e8f0; padding-left: 20px;">├── <strong style="color: #e2e8f0);">candidates/</strong> <span style="color: var(--text-dim);"># {"Сгенерированные варианты" if is_ru else "Generated candidate outputs"}</span></div>
              <div style="color: #e2e8f0; padding-left: 20px;">├── <strong style="color: var(--c4-warning);">qa.md</strong> <span style="color: var(--text-dim);"># {"Чек-лист аудита дефектов" if is_ru else "Defect audit scorecard"}</span></div>
              <div style="color: #e2e8f0; padding-left: 20px;">└── <strong style="color: var(--c4-primary);">selected/</strong> <span style="color: var(--text-dim);"># {"Принятый результат + метаданные" if is_ru else "Accepted asset + audit metadata"}</span></div>
            </div>
            <div class="col flex-1" style="gap: 14px;">
              <div class="c4-card highlight">
                <div class="card-label">{"ПРОТОКОЛ СДАЧИ" if is_ru else "SUBMISSION PROTOCOL"}</div>
                <div class="card-title">{s04_p1_t}</div>
                <div class="card-desc">{s04_p1_d}</div>
              </div>
              <div class="c4-card accent-red">
                <div class="card-label" style="color: var(--c4-danger);">{"ПОЛИТИКА БЕЗОПАСНОСТИ" if is_ru else "GOVERNANCE & SAFETY"}</div>
                <div class="card-title">{s04_p2_t}</div>
                <div class="card-desc">{s04_p2_d}</div>
              </div>
            </div>
          </div>
        </div>
        {slide_footer(4)}
        <div class="speaker-notes" style="display:none;">{"Объяснить артефакты домашней работы в GitHub." if is_ru else "Explain GitHub submission structure for L04."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 05: THE TRAP: PRETTY != USABLE
    # -------------------------------------------------------------
    s05_tag = "РЕАЛЬНОСТЬ ПРОДАКШЕНА" if is_ru else "PRODUCTION REALITY"
    s05_title = "Ловушка: «Красиво ≠ Пригодно» (Pretty ≠ Usable)" if is_ru else "The Trap: Pretty ≠ Usable"
    s05_sub = "Почему эстетически безупречная картинка может стать скрытой катастрофой для бизнеса" if is_ru else "Why an aesthetically flawless image can become a silent catastrophe in enterprise systems"
    s05_f1 = "Искажение формы изделия: Ручка сместилась на 15%, геометрия керамики поплыла — покупатель получит товар с другой эргономикой." if is_ru else "Product geometry drift: Handle shifted by 15%, ceramic curvature morphed — customer receives a different physical item."
    s05_f2 = "Галлюцинация логотипа: Официальный товарный знак превращается в бессмысленный псевдо-шрифт." if is_ru else "Brand logo hallucination: Official trademark mutates into distorted pseudo-text."
    s05_f3 = "Ложные утверждения: Появление несуществующих характеристик (розетка EU-стандарта на рынке США)." if is_ru else "Factual misrepresentation: Hallucinating non-existent features (e.g. EU wall outlet in US campaign)."
    s05_f4 = "Юридические риски: Случайное появление элементов защищенных стилей или лиц без согласия." if is_ru else "Copyright & privacy risks: Accidental replication of protected artist styles or unconsented likenesses."
    s05_f5 = "Нулевая воспроизводимость: Случайный результат невозможно повторить для следующей партии товаров." if is_ru else "Zero reproducibility: Unrepeatable outputs that cannot be systematized in production pipelines."

    html += f"""
      <section class="slide-page" id="slide-5">
        {slide_header(5, s05_tag, s05_title, s05_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 16px;">
            <div class="c4-card flex-1" style="background: rgba(56, 189, 248, 0.04); border-color: rgba(56, 189, 248, 0.25);">
              <div class="card-label" style="color: var(--c4-primary);">{"РАЗВЛЕЧЕНИЕ VS ПРОДАКШЕН" if is_ru else "ENTERTAINMENT VS PRODUCTION"}</div>
              <div class="card-title" style="font-size: 18px;">{"Иллюзия совершенства" if is_ru else "The Illusion of Perfection"}</div>
              <div class="card-desc" style="font-size: 14px; line-height: 1.55; margin-top: 10px;">
                {"В текстовых моделях плохой ответ виден сразу: код не компилируется или факт неверен.<br><br>В генерации графики <strong>непригодная картинка выглядит кинематографично и дорого</strong>. Человеческий мозг очаровывается сочным светом и не замечает, что объект перестал соответствовать реальности." if is_ru else "In LLMs, failures are obvious upon reading: broken syntax or factual errors.<br><br>In visual generation, <strong>an unusable image can look cinematic and gorgeous</strong>. The human eye is seduced by lighting and fails to spot critical geometric drift."}
              </div>
            </div>
            <div class="c4-card accent-red flex-15">
              <div class="card-label" style="color: var(--c4-danger);">{"5 ТИХИХ КАТАСТРОФ В ПРОДАКШЕНЕ" if is_ru else "5 SILENT PRODUCTION FAILURES"}</div>
              <div class="col" style="gap: 10px; margin-top: 8px;">
                <div style="display: flex; gap: 10px; font-size: 13px; color: #e2e8f0; line-height: 1.4;">
                  <strong style="color: var(--c4-danger); font-family: var(--font-mono);">01</strong><span>{s05_f1}</span>
                </div>
                <div style="display: flex; gap: 10px; font-size: 13px; color: #e2e8f0; line-height: 1.4;">
                  <strong style="color: var(--c4-danger); font-family: var(--font-mono);">02</strong><span>{s05_f2}</span>
                </div>
                <div style="display: flex; gap: 10px; font-size: 13px; color: #e2e8f0; line-height: 1.4;">
                  <strong style="color: var(--c4-danger); font-family: var(--font-mono);">03</strong><span>{s05_f3}</span>
                </div>
                <div style="display: flex; gap: 10px; font-size: 13px; color: #e2e8f0; line-height: 1.4;">
                  <strong style="color: var(--c4-danger); font-family: var(--font-mono);">04</strong><span>{s05_f4}</span>
                </div>
                <div style="display: flex; gap: 10px; font-size: 13px; color: #e2e8f0; line-height: 1.4;">
                  <strong style="color: var(--c4-danger); font-family: var(--font-mono);">05</strong><span>{s05_f5}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
        {slide_footer(5)}
        <div class="speaker-notes" style="display:none;">{"Ловушка визуальной красоты: почему красивая картинка может быть непригодна для e-commerce." if is_ru else "The trap of aesthetics: why beautiful graphics can fail e-commerce requirements."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 06: MODALITY SHIFT: DIFFUSION PHYSICS
    # -------------------------------------------------------------
    s06_tag = "ФИЗИКА МОДЕЛЕЙ" if is_ru else "MODEL PHYSICS"
    s06_title = "Смена модальности: Физика диффузии и латентного пространства" if is_ru else "Modality Shift: Diffusion Physics & Latent Space"
    s06_sub = "Почему изображение — это не BPE-токены, и как работает пошаговое удаление шума (Denoising)" if is_ru else "Why images are not discrete BPE tokens, and how iterative denoising operates in latent space"
    s06_banner = (
        "<strong>Текстовые LLM:</strong> Дискретные BPE-токены $w_1 \\to w_2 \\to w_3$, авторегрессия. &nbsp;|&nbsp; <strong>Диффузия & DiT:</strong> Непрерывные тензоры, латентный VAE и пошаговый Denoising."
        if is_ru else
        "<strong>Text LLMs:</strong> Discrete BPE tokens $w_1 \\to w_2 \\to w_3$, autoregression. &nbsp;|&nbsp; <strong>Diffusion & DiT:</strong> Continuous tensors, VAE latent space, and iterative Denoising."
    )
    s06_c1_t = "Сжатие пространства" if is_ru else "Latent Space Compression"
    s06_c1_d = "Миллионы RGB-пикселей сжимаются вариационным автоэнкодером (VAE) в 8–16 раз в компактное скрытое пространство z. Инференс происходит над тензорами." if is_ru else "Millions of RGB pixels compressed by Variational Autoencoder (VAE) by 8x-16x into compact latent space z for efficient inference."
    s06_c2_t = "Очистка шума (Denoising)" if is_ru else "Iterative Denoising"
    s06_c2_d = "Картинку учат пошагово удалять белый гауссовский шум за 20–50 шагов. Нейросеть (UNet или DiT) на каждом шаге вычисляет дельту шума." if is_ru else "Model trained to reverse Gaussian noise over 20-50 steps. UNet or DiT predicts noise increments at each discrete step."
    s06_c3_t = "Кросс-внимание и Seed" if is_ru else "Conditioning & Seed"
    s06_c3_d = "Текстовый энкодер (CLIP / T5) передает эмбеддинги через Cross-Attention. Seed (зерно шума) определяет стартовую матрицу: фиксация seed дает воспроизводимость." if is_ru else "CLIP/T5 text encoder directs denoising via Cross-Attention. Seed pins initial Gaussian distribution for reproducible outputs."

    html += f"""
      <section class="slide-page" id="slide-6">
        {slide_header(6, s06_tag, s06_title, s06_sub)}
        <div class="slide-content-arena" style="gap: 14px;">
          <div class="c4-card highlight" style="padding: 12px 18px; font-size: 14px; text-align: center;">
            {s06_banner}
          </div>
          <div class="row" style="flex: 1; gap: 14px;">
            <div class="c4-card flex-1">
              <div class="card-label">1. VAE LATENT SPACE</div>
              <div class="card-title">{s06_c1_t}</div>
              <div class="card-desc">{s06_c1_d}</div>
            </div>
            <div class="c4-card flex-1">
              <div class="card-label" style="color: var(--c4-warning);">2. FORWARD & REVERSE DENOISING</div>
              <div class="card-title">{s06_c2_t}</div>
              <div class="card-desc">{s06_c2_d}</div>
            </div>
            <div class="c4-card flex-1">
              <div class="card-label" style="color: var(--c4-success);">3. CONDITIONING & SEED</div>
              <div class="card-title">{s06_c3_t}</div>
              <div class="card-desc">{s06_c3_d}</div>
            </div>
          </div>
        </div>
        {slide_footer(6)}
        <div class="speaker-notes" style="display:none;">{"Физика диффузии: латентное пространство VAE, пошаговое удаление шума и важность фиксации Seed." if is_ru else "Diffusion physics: VAE latent space, iterative denoising steps, and pinning Seed for reproducibility."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 07: WORKFLOW PIPELINE (VISUAL)
    # -------------------------------------------------------------
    s07_tag = "СИСТЕМНАЯ АРХИТЕКТУРА" if is_ru else "SYSTEM ARCHITECTURE"
    s07_title = "Ментальная модель: Генерация как пайплайн" if is_ru else "Mental Model: Generation as a Pipeline"
    s07_sub = "Модель — лишь один узел; управляемость рождается в архитектурной обвязке до и после вызова" if is_ru else "The model is only one node; predictability is engineered in the pipeline before and after inference"

    html += f"""
      <section class="slide-page visual-slide" id="slide-7">
        {slide_header(7, s07_tag, s07_title, s07_sub)}
        <div class="slide-content-arena">
          <div class="visual-container">
            <img src="assets/image_generation_workflow_pipeline.png" alt="Image Generation Workflow Pipeline">
          </div>
        </div>
        {slide_footer(7)}
        <div class="speaker-notes" style="display:none;">{"Сквозной C4-пайплайн: входные ассеты, шлюз API, инференс, хранилище S3, Base64 декодер, метаданные и шлюз модерации." if is_ru else "End-to-end C4 pipeline: assets, gateway, inference, S3 storage, Base64 decoder, metadata audit DB, review gate."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 08: THE 6 VISUAL PRIMITIVES
    # -------------------------------------------------------------
    s08_tag = "БАЗОВЫЕ ПРИМИТИВЫ" if is_ru else "CORE PRIMITIVES"
    s08_title = "6 визуальных примитивов компьютерного зрения" if is_ru else "The 6 Visual Primitives of Image AI"
    s08_sub = "Фундаментальные операции, комбинация которых закрывает любые прикладные сценарии" if is_ru else "The foundational operations combined to solve all commercial visual engineering workflows"
    p1_t = "Генерация с нуля" if is_ru else "Synthesis From Scratch"
    p1_d = "Создание пикселей исключительно по тексту. Для концепт-арта и раскадровок без жесткой фиксации объекта." if is_ru else "Synthesizing pixels from text alone. Best for concept ideation and storyboard backdrops."
    p2_t = "Трансформация референса" if is_ru else "Reference Transformation"
    p2_d = "Подача входного фото и текста. Модель сохраняет композицию, превращая скетч в финальный фото-рендер." if is_ru else "Conditioning on source image plus prompt. Preserves spatial composition while restyling."
    p3_t = "Редактирование по маске" if is_ru else "Masked Region Editing"
    p3_d = "Замена пикселей внутри альфа-маски. Замена фона вокруг товара с сохранением 100% геометрии изделия." if is_ru else "Modifying pixels strictly within mask boundary. Swapping product background while freezing product."
    p4_t = "Расширение холста" if is_ru else "Canvas Outpainting"
    p4_d = "Дорисовывание окружения за пределами границ кадра. Превращение фото 1:1 в широкоформатный баннер 16:9." if is_ru else "Generating scene beyond original canvas borders. Expanding 1:1 square photo to 16:9 banner."
    p5_t = "Опорные сигналы" if is_ru else "Multimodal Conditioning"
    p5_d = "Фиксация идентичности товара (IP-Adapter), колористики (Style Reference) или каркаса позы (ControlNet)." if is_ru else "Pinning product identity (IP-Adapter), aesthetics (Style Reference), or pose skeletons (ControlNet)."
    p6_t = "Аппаратные запреты" if is_ru else "Negative Constraints"
    p6_d = "Жесткий фильтр в конфигурации: исключение текста, водяных знаков, анатомических дефектов и лишних чашек." if is_ru else "Deterministic exclusion: stripping unwanted text, watermarks, duplicate objects, and anatomical glitches."

    html += f"""
      <section class="slide-page" id="slide-8">
        {slide_header(8, s08_tag, s08_title, s08_sub)}
        <div class="slide-content-arena">
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; flex: 1;">
            <div class="c4-card">
              <div class="card-label">01 • TEXT-TO-IMAGE</div>
              <div class="card-title">{p1_t}</div>
              <div class="card-desc">{p1_d}</div>
            </div>
            <div class="c4-card">
              <div class="card-label">02 • IMAGE-TO-IMAGE</div>
              <div class="card-title">{p2_t}</div>
              <div class="card-desc">{p2_d}</div>
            </div>
            <div class="c4-card highlight">
              <div class="card-label" style="color: var(--c4-primary);">03 • INPAINTING</div>
              <div class="card-title">{p3_t}</div>
              <div class="card-desc">{p3_d}</div>
            </div>
            <div class="c4-card">
              <div class="card-label">04 • OUTPAINTING</div>
              <div class="card-title">{p4_t}</div>
              <div class="card-desc">{p4_d}</div>
            </div>
            <div class="c4-card">
              <div class="card-label">05 • REFERENCE SIGNALS</div>
              <div class="card-title">{p5_t}</div>
              <div class="card-desc">{p5_d}</div>
            </div>
            <div class="c4-card accent-red">
              <div class="card-label" style="color: var(--c4-danger);">06 • NEGATIVE CONSTRAINTS</div>
              <div class="card-title">{p6_t}</div>
              <div class="card-desc">{p6_d}</div>
            </div>
          </div>
        </div>
        {slide_footer(8)}
        <div class="speaker-notes" style="display:none;">{"6 примитивов. Обязательно выделить Inpainting как главный инструмент для e-commerce." if is_ru else "6 primitives. Emphasize inpainting as the core primitive for commercial e-commerce."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 09: PROMPT ANATOMY
    # -------------------------------------------------------------
    s09_tag = "ИНЖЕНЕРНЫЙ ПРОМПТ" if is_ru else "ENGINEERING PROMPT"
    s09_title = "Анатомия промпта: Инженерное ТЗ, а не поэма" if is_ru else "Prompt Anatomy: An Engineering Brief, Not a Poem"
    s09_sub = "Разделение промпта на изолированные технические параметры вместо эмоциональных прилагательных" if is_ru else "Deconstructing visual prompts into explicit parameters instead of decorative adjectives"
    a1_t = "Центральная сущность" if is_ru else "Focal Entity"
    a1_d = "Объект в фокусе: один предмет, точный материал, глазурь, цвет. Без размытых абстракций." if is_ru else "Single hero object, physical material, glaze texture, surface reflectance. Zero ambiguity."
    a2_t = "Ракурс и верстка" if is_ru else "Framing & Camera"
    a2_d = "Угол съемки (eye-level, macro), малая глубина резкости, свободное пространство для верстки." if is_ru else "Eye-level product macro, shallow depth of field, clean negative space reserved for typography."
    a3_t = "Сцена и атмосфера" if is_ru else "Scene & Lighting"
    a3_d = "Материал поверхности (травертин, дерево), мягкий направленный свет слева, реалистичные тени." if is_ru else "Surface material (travertine), lateral natural light from left, realistic contact shadows."
    a4_t = "Тип съемки" if is_ru else "Aesthetic Language"
    a4_d = "Commercial editorial product photography. Запрет на 3D-рендеры, рисунки и фильтры." if is_ru else "Commercial editorial photography. Explicit prohibition of 3D renders or illustrations."
    a5_t = "Что нельзя менять" if is_ru else "Sacred Attributes (Taboo)"
    a5_d = "<strong>Главная строчка:</strong> форма ручки, пропорции изделия и логотип обязаны остаться нетронутыми." if is_ru else "<strong>Most critical line:</strong> mug geometry, handle curvature, and logo must remain untouched."
    a6_t = "Критерии отбора" if is_ru else "Acceptance Criteria"
    a6_d = "Чек-лист: совпадение контура товара, отсутствие текста, естественность света, модерация." if is_ru else "Checklist: catalog contour match, zero unwanted text, realistic lighting, moderation pass."

    html += f"""
      <section class="slide-page" id="slide-9">
        {slide_header(9, s09_tag, s09_title, s09_sub)}
        <div class="slide-content-arena">
          <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; flex: 1;">
            <div class="c4-card">
              <div class="card-label">{"SUBJECT • ОБЪЕКТ" if is_ru else "SUBJECT • HERO OBJECT"}</div>
              <div class="card-title">{a1_t}</div>
              <div class="card-desc">{a1_d}</div>
            </div>
            <div class="c4-card">
              <div class="card-label">{"COMPOSITION • КАДР" if is_ru else "COMPOSITION • FRAMING"}</div>
              <div class="card-title">{a2_t}</div>
              <div class="card-desc">{a2_d}</div>
            </div>
            <div class="c4-card">
              <div class="card-label">{"ENVIRONMENT • СВЕТ" if is_ru else "ENVIRONMENT • LIGHTING"}</div>
              <div class="card-title">{a3_t}</div>
              <div class="card-desc">{a3_d}</div>
            </div>
            <div class="c4-card">
              <div class="card-label">{"STYLE • ЭСТЕТИКА" if is_ru else "STYLE • AESTHETIC"}</div>
              <div class="card-title">{a4_t}</div>
              <div class="card-desc">{a4_d}</div>
            </div>
            <div class="c4-card accent-amber">
              <div class="card-label" style="color: var(--c4-warning);">{"SACRED ATTRIBUTES • ТАБУ" if is_ru else "SACRED ATTRIBUTES • TABOO"}</div>
              <div class="card-title">{a5_t}</div>
              <div class="card-desc">{a5_d}</div>
            </div>
            <div class="c4-card accent-emerald">
              <div class="card-label" style="color: var(--c4-success);">{"ACCEPTANCE • ПРИЕМКА" if is_ru else "ACCEPTANCE • CRITERIA"}</div>
              <div class="card-title">{a6_t}</div>
              <div class="card-desc">{a6_d}</div>
            </div>
          </div>
        </div>
        {slide_footer(9)}
        <div class="speaker-notes" style="display:none;">{"Анатомия промпта. Подчеркнуть, что самое важное указание - что НЕЛЬЗЯ менять." if is_ru else "Prompt anatomy. Emphasize that the most critical directive is what MUST NOT change."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 10: BEFORE / AFTER
    # -------------------------------------------------------------
    s10_tag = "СРАВНЕНИЕ В ЛОБ" if is_ru else "BEFORE VS AFTER"
    s10_title = "Сравнение: Слабый промпт vs Инженерный бриф" if is_ru else "Before vs After: Weak Prompt vs Production Spec"
    s10_sub = "Как одна и та же задача решается на уровне случайной лотереи и на уровне предсказуемого контракта" if is_ru else "How the exact same task executes as an unpredictable gamble vs a deterministic contract"
    w_prompt = '"Сделай красивую рекламу этой кружки в уютной студии."' if is_ru else '"Make a beautiful ad image for this mug in a cozy studio."'
    w_res = (
        "<strong>Типичный результат:</strong><br>• Модель берет 99% творческой свободы.<br>• Ручка изменила форму, глазурь поплыла.<br>• В кадре появились случайные круассаны и лишняя чашка.<br>• <em>Непригодно для каталога и автоматизации.</em>"
        if is_ru else
        "<strong>Typical Failure:</strong><br>• Model takes 99% creative freedom.<br>• Handle geometry morphs, glaze drifts.<br>• Unsolicited props and duplicate mugs hallucinated.<br>• <em>Unusable for commercial catalog pipelines.</em>"
    )
    c_prompt = (
        '"Using input_product.png as protected reference, preserve mug shape, speckled glaze, handle ergonomics, and proportions 100%. Replace only background and surface with pale travertine studio in soft natural morning light. Eye-level, 16:9 crop, 2K. No text, no hands, no extra mugs. Return 3 variants. Acceptance: zero geometry drift against catalog master."'
    )
    c_res = (
        "<strong>Инженерный результат:</strong><br>• Изолированные параметры, готовые к параметризации через JSON в коде.<br>• 100% сохранение физической идентичности товара.<br>• Четкие критерии для ручного или автоматического QA-отбора."
        if is_ru else
        "<strong>Production Outcome:</strong><br>• Isolated parameters parameterized via backend JSON.<br>• 100% physical geometry and brand preservation.<br>• Deterministic criteria for automated QA gates."
    )

    html += f"""
      <section class="slide-page" id="slide-10">
        {slide_header(10, s10_tag, s10_title, s10_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 16px;">
            <div class="c4-card accent-red flex-1">
              <div class="card-label" style="color: var(--c4-danger);">{"СЛАБЫЙ ПРОМПТ (РУЛЕТКА)" if is_ru else "WEAK PROMPT (GAMBLE)"}</div>
              <div style="font-family: var(--font-mono); font-size: 14.5px; color: #fff; background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px; margin: 8px 0 12px 0;">
                {w_prompt}
              </div>
              <div class="card-desc" style="line-height: 1.55;">
                {w_res}
              </div>
            </div>
            <div class="c4-card highlight flex-15">
              <div class="card-label" style="color: var(--c4-primary);">{"ИНЖЕНЕРНЫЙ БРИФ (ПАЙПЛАЙН)" if is_ru else "PRODUCTION SPEC (PIPELINE)"}</div>
              <div style="font-family: var(--font-mono); font-size: 13.5px; color: #fff; background: rgba(0,0,0,0.3); padding: 12px; border-radius: 6px; margin: 8px 0 12px 0; line-height: 1.45;">
                {c_prompt}
              </div>
              <div class="card-desc" style="line-height: 1.55;">
                {c_res}
              </div>
            </div>
          </div>
        </div>
        {slide_footer(10)}
        <div class="speaker-notes" style="display:none;">{"Сравнение слабого и контролируемого промпта. Показать переход от поэзии к спецификации." if is_ru else "Contrast weak vs controlled prompt. Demonstrate shift from poetry to technical spec."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 11: REFERENCE SIGNALS (VISUAL)
    # -------------------------------------------------------------
    s11_tag = "МУЛЬТИМОДАЛЬНЫЙ КОНТРОЛЬ" if is_ru else "MULTIMODAL CONTROL"
    s11_title = "Сигналы референсов и мультимодальный контроль" if is_ru else "Reference Signals & Multimodal Control"
    s11_sub = "Разделение векторов: идентичность продукта (IP-Adapter), эстетика (Style) и геометрия (ControlNet)" if is_ru else "Decoupling conditioning vectors: product identity (IP-Adapter), aesthetics (Style), and geometry (ControlNet)"

    html += f"""
      <section class="slide-page visual-slide" id="slide-11">
        {slide_header(11, s11_tag, s11_title, s11_sub)}
        <div class="slide-content-arena">
          <div class="visual-container">
            <img src="assets/multimodal_reference_control.png" alt="Multimodal Reference Control">
          </div>
        </div>
        {slide_footer(11)}
        <div class="speaker-notes" style="display:none;">{"Разделение референсов: Identity (IP-Adapter) сохраняет лицо/продукт, Style передает настроение, Layout (ControlNet) фиксирует позу." if is_ru else "Decoupling references: Identity (IP-Adapter), Style (palette/light), Layout (ControlNet pose/depth)."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 12: INPAINTING & MASKING (VISUAL)
    # -------------------------------------------------------------
    s12_tag = "МЕХАНИКА ИНПЕЙНТИНГА" if is_ru else "INPAINTING MECHANICS"
    s12_title = "Механика Inpainting и маскирования" if is_ru else "Inpainting & Masking Mechanics"
    s12_sub = "Как бинарная альфа-маска и размытие краев (Edge Feathering) защищают пиксели изделия" if is_ru else "How binary alpha masks and edge feathering protect physical product geometry"

    html += f"""
      <section class="slide-page visual-slide" id="slide-12">
        {slide_header(12, s12_tag, s12_title, s12_sub)}
        <div class="slide-content-arena">
          <div class="visual-container">
            <img src="assets/inpainting_mask_mechanics.png" alt="Inpainting and Masking Mechanics">
          </div>
        </div>
        {slide_footer(12)}
        <div class="speaker-notes" style="display:none;">{"Механика маски: черная зона (замороженные пиксели), белая зона (зашумление и денойзинг), сглаживание шва (feathering)." if is_ru else "Mask mechanics: black frozen zone, white active denoising zone, edge feathering for seamless contact shadows."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 13: API LIFECYCLE
    # -------------------------------------------------------------
    s13_tag = "СЕТЕВЫЕ ПРОТОКОЛЫ" if is_ru else "NETWORK PROTOCOLS"
    s13_title = "Жизненный цикл API и сетевые пакеты" if is_ru else "API Lifecycle & Network Payloads"
    s13_sub = "Передача бинарных данных по проводу: синхронный Base64 vs асинхронные очереди (Job Queue)" if is_ru else "Traversing the wire: Synchronous Base64 payloads vs Asynchronous Job Queue Polling"
    p1_body = (
        "<strong>Где используется:</strong> Google Gemini API, OpenAI Images API.<br><br>• Клиент отправляет JSON с Base64-строкой изображения.<br>• Сокет удерживается 3–6 секунд.<br>• Сервер возвращает Base64-байты прямо в теле ответа.<br>• <strong>Плюс:</strong> Мгновенная интеграция в интерактивные боты.<br>• <strong>Минус:</strong> Риск таймаута на тяжелых 4K-пакетах."
        if is_ru else
        "<strong>Where used:</strong> Google Gemini API, OpenAI Images API.<br><br>• Client sends JSON with Base64-encoded image.<br>• HTTP socket remains open for 3-6 seconds.<br>• Server returns Base64 bytes directly in response payload.<br>• <strong>Pros:</strong> Immediate interactive conversational flow.<br>• <strong>Cons:</strong> Gateway timeout risk on batch 4K generation."
    )
    p2_body = (
        "<strong>Где используется:</strong> Adobe Firefly Services, Midjourney, Local ComfyUI.<br><br>• Запрос немедленно возвращает <code>HTTP 202 Accepted</code> с <code>job_id: 'img_98765'</code>.<br>• Клиент опрашивает статус (Polling) или ждет Webhook.<br>• Готовый файл скачивается по временной подписанной ссылке из S3.<br>• <strong>Плюс:</strong> Надежность и масштабируемость очереди."
        if is_ru else
        "<strong>Where used:</strong> Adobe Firefly Services, Midjourney, ComfyUI.<br><br>• Request immediately returns <code>HTTP 202 Accepted</code> with <code>job_id: 'img_98765'</code>.<br>• Backend polls status endpoint or handles webhook.<br>• Output downloaded via ephemeral signed S3 URL.<br>• <strong>Pros:</strong> Robust asynchronous decoupling."
    )

    html += f"""
      <section class="slide-page" id="slide-13">
        {slide_header(13, s13_tag, s13_title, s13_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 16px;">
            <div class="c4-card highlight flex-1">
              <div class="card-label" style="color: var(--c4-primary);">{"ПАТТЕРН 1 • СИНХРОННЫЙ BASE64" if is_ru else "PATTERN 1 • SYNCHRONOUS BASE64"}</div>
              <div class="card-title">{"Прямой возврат байтов (2–5 сек)" if is_ru else "Direct Byte Stream (2-5s)"}</div>
              <div class="card-desc" style="line-height: 1.55; margin-top: 8px;">
                {p1_body}
              </div>
            </div>
            <div class="c4-card accent-purple flex-1">
              <div class="card-label" style="color: var(--c4-purple);">{"ПАТТЕРН 2 • АСИНХРОННАЯ ОЧЕРЕДЬ" if is_ru else "PATTERN 2 • ASYNC JOB QUEUE"}</div>
              <div class="card-title">{"Опрос статуса и вебхуки (30–60 сек)" if is_ru else "Polling & Webhooks (30-60s)"}</div>
              <div class="card-desc" style="line-height: 1.55; margin-top: 8px;">
                {p2_body}
              </div>
            </div>
          </div>
        </div>
        {slide_footer(13)}
        <div class="speaker-notes" style="display:none;">{"Сетевые паттерны: синхронный Base64 для диалогов vs асинхронный Job Queue для студийного продакшена." if is_ru else "Network patterns: Synchronous Base64 for chat vs Asynchronous Job Queue for heavy studios."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 14: PROVIDER LANDSCAPE
    # -------------------------------------------------------------
    s14_tag = "ЛАНДШАФТ ПРОВАЙДЕРОВ" if is_ru else "PROVIDER LANDSCAPE"
    s14_title = "Ландшафт провайдеров без маркетингового хайпа" if is_ru else "Provider Landscape Without Hype"
    s14_sub = "Сравнение ключевых платформ 2026 года по архитектурным возможностям и корпоративной защите" if is_ru else "Comparing primary 2026 visual platforms by architecture, speed, and enterprise legal indemnity"
    pr1 = "Глубокое понимание сложных смысловых инструкций, генерация и редактирование. Интеграция генерации как инструмента (Tool Calling) внутри агентов." if is_ru else "High prompt comprehension, generation, and editing. Seamless integration as an agent tool via Responses API."
    pr2 = "Нативный мультимодальный контекст диалога: возможность редактировать картинку через естественные уточнения в общем чате. Быстрый Base64 возврат." if is_ru else "Native multimodal conversational context: iterative image editing via dialog refinement. Low-latency Base64 streaming."
    pr3 = "Золотой стандарт энтерпрайза: обучение строго на лицензионном стоке, юридическая страховка от исков (indemnity), послойное редактирование PSD." if is_ru else "Enterprise benchmark: trained exclusively on licensed stock, full commercial indemnity, Photoshop PSD layer APIs."
    pr4 = "Полный контроль весов, локальный запуск в закрытом контуре компании, безлимитная генерация и поддержка расширений ControlNet и LoRA." if is_ru else "Total weight ownership, on-premise execution, zero data exfiltration, unrestricted ControlNet and LoRA fine-tuning."

    html += f"""
      <section class="slide-page" id="slide-14">
        {slide_header(14, s14_tag, s14_title, s14_sub)}
        <div class="slide-content-arena">
          <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 14px; flex: 1;">
            <div class="c4-card flex-1">
              <div class="card-label" style="color: var(--c4-primary);">OPENAI IMAGES & RESPONSES</div>
              <div class="card-title">GPT-Image-2 / DALL-E</div>
              <div class="card-desc">{pr1}</div>
            </div>
            <div class="c4-card highlight flex-1">
              <div class="card-label" style="color: var(--c4-success);">GOOGLE CLOUD / GEMINI</div>
              <div class="card-title">Gemini 3.1 Flash Image & Imagen 3/4</div>
              <div class="card-desc">{pr2}</div>
            </div>
            <div class="c4-card accent-amber flex-1">
              <div class="card-label" style="color: var(--c4-warning);">ADOBE FIREFLY SERVICES</div>
              <div class="card-title">Firefly Image5 & Photoshop API v2</div>
              <div class="card-desc">{pr3}</div>
            </div>
            <div class="c4-card accent-purple flex-1">
              <div class="card-label" style="color: var(--c4-purple);">OPEN SOURCE & LOCAL HOSTING</div>
              <div class="card-title">FLUX.1 / SDXL on RunPod</div>
              <div class="card-desc">{pr4}</div>
            </div>
          </div>
        </div>
        {slide_footer(14)}
        <div class="speaker-notes" style="display:none;">{"Сравнение 4 семейств платформ. Выбирать инструмент под задачу: коммерческая чистота Firefly vs скорость Gemini." if is_ru else "Vendor comparison. Match capabilities to business constraints: commercial indemnity vs raw speed."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 15: MIDPOINT BREAK
    # -------------------------------------------------------------
    s15_tag = "ЭКВАТОР • 5 МИНУТ" if is_ru else "EQUATOR • 5 MINUTES"
    s15_title = "Экватор: Перерыв 5 минут" if is_ru else "Midpoint Break: 5 Minutes"
    s15_sub = "Время перезагрузить внимание перед продакшен-айсбергом, Blast Radius и живым кодом" if is_ru else "Time for cognitive rest before diving into the 10/90 iceberg, Blast Radius, and live demo code"
    b_desc = (
        "Отдохните 5 минут и переведите дыхание. Никаких рабочих тем в чате — полный отдых мозга. Во второй части: продакшен-айсберг 10/90, Blast Radius, запуск кода и домашка."
        if is_ru else
        "Step away, hydrate, and stretch. Pure cognitive rest — no chat work discussions. In 5 minutes: the 10/90 iceberg, Blast Radius, live demo code, and homework."
    )

    html += f"""
      <section class="slide-page" id="slide-15">
        {slide_header(15, s15_tag, s15_title, s15_sub)}
        <div class="slide-content-arena" style="align-items: center; justify-content: center;">
          <div class="c4-card accent-amber" style="width: 520px; align-items: center; padding: 28px; text-align: center;">
            <div class="card-label" style="color: var(--c4-warning); font-size: 13px;">{"ИНТЕРАКТИВНЫЙ ТАЙМЕР ПЕРЕРЫВА" if is_ru else "INTERACTIVE BREAK TIMER"}</div>
            <div id="breakTimerDisplay" style="font-family: var(--font-mono); font-size: 76px; font-weight: 800; color: #fff; margin: 12px 0; letter-spacing: -0.04em;">
              05:00
            </div>
            <div class="row" style="gap: 12px; margin-bottom: 16px;">
              <button id="timerToggleBtn" onclick="toggleBreakTimer()" style="background: var(--c4-warning); color: #0c111a; border: none; border-radius: 6px; padding: 10px 22px; font-weight: 700; font-family: var(--font-mono); cursor: pointer;">
                {start_5m}
              </button>
              <button onclick="resetBreakTimer()" style="background: rgba(255,255,255,0.08); color: #fff; border: 1px solid var(--border-subtle); border-radius: 6px; padding: 10px 18px; font-weight: 600; font-family: var(--font-mono); cursor: pointer;">
                {reset_txt}
              </button>
            </div>
            <div class="card-desc" style="font-size: 13.5px; line-height: 1.5;">
              {b_desc}
            </div>
          </div>
        </div>
        {slide_footer(15)}
        <div class="speaker-notes" style="display:none;">{"Нажать кнопку старта таймера. Полный отдых мозга, без рабочих тем в чате." if is_ru else "Click Start 5 Min button. Total cognitive rest without work discussions in chat."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 16: THE 10/90 ICEBERG (VISUAL)
    # -------------------------------------------------------------
    s16_tag = "ЭНТЕРПРАЙЗ-АЙСБЕРГ" if is_ru else "ENTERPRISE ICEBERG"
    s16_title = "Айсберг 10/90 в Computer Vision" if is_ru else "The 10/90 Iceberg in Computer Vision"
    s16_sub = "10% видимый вызов API модели vs 90% невидимой инженерной инфраструктуры" if is_ru else "The 10% visible model API call vs 90% submerged production engineering infrastructure"

    html += f"""
      <section class="slide-page visual-slide" id="slide-16">
        {slide_header(16, s16_tag, s16_title, s16_sub)}
        <div class="slide-content-arena">
          <div class="visual-container">
            <img src="assets/image_api_10_90_iceberg.png" alt="The 10/90 Computer Vision Iceberg">
          </div>
        </div>
        {slide_footer(16)}
        <div class="speaker-notes" style="display:none;">{"Айсберг 10/90: подводная инфраструктура (хранение S3, Base64, PII модерация, очереди, аудит, ревью)." if is_ru else "The 10/90 iceberg: submerged engineering (S3, Base64 parser, PII/NSFW gates, async queues, audit trail)."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 17: BLAST RADIUS
    # -------------------------------------------------------------
    s17_tag = "УПРАВЛЕНИЕ РИСКАМИ" if is_ru else "RISK GOVERNANCE"
    s17_title = "Зоны риска Blast Radius в генерации изображений" if is_ru else "Blast Radius Governance in Image AI"
    s17_sub = "Светофор допустимой автономии: где ИИ безопасен, а где действует абсолютное табу" if is_ru else "Traffic-light autonomy matrix: where AI is safe vs where autonomous execution is forbidden"
    br_g = (
        "<strong>Сценарии:</strong><br>• Внутренние мудборды для дизайнеров.<br>• Синтетические аватарки и мок-данные для QA-тестирования.<br>• Эскизы для мозгового штурма.<br><br><em>Модель может работать полностью автономно. Ошибка не стоит ничего.</em>"
        if is_ru else
        "<strong>Scenarios:</strong><br>• Internal design moodboards.<br>• Synthetic profile avatars for QA load testing.<br>• Brainstorming exploratory sketches.<br><br><em>Autonomous execution permitted. Zero business blast radius.</em>"
    )
    br_y = (
        "<strong>Сценарии:</strong><br>• Карточки товаров для e-commerce маркетплейса.<br>• Иллюстрации в корпоративный блог.<br>• Превью-обложки для роликов на YouTube.<br><br><em>Модель генерирует 3–4 кандидата, но публикацию утверждает человек.</em>"
        if is_ru else
        "<strong>Scenarios:</strong><br>• Marketplace e-commerce backgrounds.<br>• Editorial blog graphics.<br>• YouTube video thumbnails.<br><br><em>Model acts as copilot; human editor holds final publishing sign-off.</em>"
    )
    br_r = (
        "<strong>Сценарии:</strong><br>• Юридические и судебные доказательства.<br>• Медицинская диагностика и снимки.<br>• Печать упаковки с составом лекарств и ГОСТ.<br>• Изменение официальных товарных знаков.<br><br><em>Прямой запрет на использование генеративного ИИ.</em>"
        if is_ru else
        "<strong>Scenarios:</strong><br>• Legal evidence and courtroom documentation.<br>• Medical imaging diagnostics.<br>• Direct-to-print packaging with certified claims.<br>• Official corporate logo modifications.<br><br><em>AI autonomy strictly forbidden.</em>"
    )

    html += f"""
      <section class="slide-page" id="slide-17">
        {slide_header(17, s17_tag, s17_title, s17_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 14px;">
            <div class="c4-card accent-emerald flex-1">
              <div class="card-label" style="color: var(--c4-success);">{"🟢 ЗЕЛЕНАЯ ЗОНА • АВТОНОМИЯ" if is_ru else "🟢 GREEN TIER • AUTONOMOUS"}</div>
              <div class="card-title">{"Нулевой риск ошибки" if is_ru else "Zero Business Risk"}</div>
              <div class="card-desc" style="line-height: 1.55; margin-top: 8px;">
                {br_g}
              </div>
            </div>
            <div class="c4-card accent-amber flex-1">
              <div class="card-label" style="color: var(--c4-warning);">{"🟡 ЖЕЛТАЯ ЗОНА • HUMAN-IN-THE-LOOP" if is_ru else "🟡 YELLOW TIER • HUMAN-IN-THE-LOOP"}</div>
              <div class="card-title">{"Умеренный риск" if is_ru else "Moderate Operational Risk"}</div>
              <div class="card-desc" style="line-height: 1.55; margin-top: 8px;">
                {br_y}
              </div>
            </div>
            <div class="c4-card accent-red flex-1">
              <div class="card-label" style="color: var(--c4-danger);">{"🔴 КРАСНАЯ ЗОНА • ТАБУ" if is_ru else "🔴 RED TIER • STRICT TABOO"}</div>
              <div class="card-title">{"Катастрофический риск" if is_ru else "Severe Liability Risk"}</div>
              <div class="card-desc" style="line-height: 1.55; margin-top: 8px;">
                {br_r}
              </div>
            </div>
          </div>
        </div>
        {slide_footer(17)}
        <div class="speaker-notes" style="display:none;">{"Светофор Blast Radius. Четкие границы: где ИИ автономен, где нужен человек, а где табу." if is_ru else "Blast Radius traffic light. Delineate autonomous, copilot, and forbidden domains."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 18: LIVE DEMO RUNBOOK
    # -------------------------------------------------------------
    s18_tag = "ЖИВОЙ КОД" if is_ru else "LIVE DEMO"
    s18_title = "Лайв-демо: Путь от хаоса к контролю" if is_ru else "Live Demo: From Chaos to Control"
    s18_sub = "Запуск скриптов demo_repo: генерация героя, сравнение эдитов и сборка промпта из JSON" if is_ru else "Running demo_repo scripts: hero generation, comparing edits, and programmatic prompt assembly"
    d1_d = (
        "• Запрос к <code>gemini-3.1-flash-image</code>.<br>• Параметры: <code>aspect_ratio: '16:9'</code>.<br>• Декодирование байтов <code>base64.b64decode()</code>.<br>• Запись файла на диск в <code>out/</code>."
        if is_ru else
        "• API request to <code>gemini-3.1-flash-image</code>.<br>• Response format: <code>aspect_ratio: '16:9'</code>.<br>• Base64 byte decoding via Python.<br>• Persisting asset to disk in <code>out/</code>."
    )
    d2_d = (
        "• <code>--mode vague</code>: абстрактный промпт ломает форму ручки и текстуру.<br>• <code>--mode controlled</code>: жесткие табу сохраняют 100% геометрии кружки и меняют только фон на травертин."
        if is_ru else
        "• <code>--mode vague</code>: naive prompt breaks handle curvature and glaze.<br>• <code>--mode controlled</code>: sacred constraints preserve 100% of mug geometry while swapping background to travertine."
    )
    d3_d = (
        "• Чтение <code>visual_spec.json</code>.<br>• Программная конкатенация параметров: Subject, Environment, Constraints, Ratio.<br>• Исключение человеческих ошибок в строке промпта."
        if is_ru else
        "• Reading schema from <code>visual_spec.json</code>.<br>• Deterministic assembly of Subject, Camera, Constraints, and Ratio.<br>• Eliminating prompt injection and human typos."
    )

    html += f"""
      <section class="slide-page" id="slide-18">
        {slide_header(18, s18_tag, s18_title, s18_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 14px;">
            <div class="c4-card flex-1">
              <div class="card-label">{"РАУНД 1 • 01_GENERATE.PY" if is_ru else "ROUND 1 • 01_GENERATE.PY"}</div>
              <div class="card-title">{"Первый вызов и Base64" if is_ru else "First Call & Base64"}</div>
              <div class="card-desc" style="line-height: 1.5;">{d1_d}</div>
            </div>
            <div class="c4-card highlight flex-1">
              <div class="card-label" style="color: var(--c4-primary);">{"РАУНД 2 • 02_EDIT.PY" if is_ru else "ROUND 2 • 02_EDIT.PY"}</div>
              <div class="card-title">Vague vs Controlled</div>
              <div class="card-desc" style="line-height: 1.5;">{d2_d}</div>
            </div>
            <div class="c4-card accent-purple flex-1">
              <div class="card-label" style="color: var(--c4-purple);">{"РАУНД 3 • 03_BUILD_PROMPT.PY" if is_ru else "ROUND 3 • 03_BUILD_PROMPT.PY"}</div>
              <div class="card-title">{"Сборка из JSON-схемы" if is_ru else "JSON Schema Assembly"}</div>
              <div class="card-desc" style="line-height: 1.5;">{d3_d}</div>
            </div>
          </div>
        </div>
        {slide_footer(18)}
        <div class="speaker-notes" style="display:none;">{"Лайв-демо: запуск трех скриптов. Сравнить результаты vague vs controlled." if is_ru else "Live demo: running 3 scripts. Compare vague vs controlled image preservation."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 19: DECISION MATRIX
    # -------------------------------------------------------------
    s19_tag = "ДЕРЕВО РЕШЕНИЙ" if is_ru else "DECISION TREE"
    s19_title = "Дерево решений: GenAI vs Классический CV vs Детерминированный софт" if is_ru else "Decision Matrix: GenAI vs Classical CV vs Deterministic Tools"
    s19_sub = "Принцип «Сначала проблема, а не ИИ»: когда диффузионные модели не нужны и опасны" if is_ru else "Problem first, not AI first: identifying when generative diffusion is unnecessary and harmful"
    dm1 = (
        "<strong>Когда выбирать:</strong><br>• Векторные логотипы и товарные знаки.<br>• Точная типографика, даты, ценники.<br>• Верстка рекламных баннеров по сетке.<br><br><em>$0 затрат, 0ms задержки, 100% точность букв.</em>"
        if is_ru else
        "<strong>When to choose:</strong><br>• Vector logos and trademarks.<br>• Crisp typography, pricing, dates.<br>• Grid-aligned banner composition.<br><br><em>$0 cost, 0ms latency, 100% typographic accuracy.</em>"
    )
    dm2 = (
        "<strong>Когда выбирать:</strong><br>• Детекция брака деталей на конвейере.<br>• Распознавание штрихкодов и номеров.<br>• Кадрирование лиц и выравнивание горизонта.<br><br><em>2–5ms локальный инференс на обычном CPU, $0 за токены.</em>"
        if is_ru else
        "<strong>When to choose:</strong><br>• Conveyor belt defect detection.<br>• Barcode and license plate recognition.<br>• Face cropping and edge alignment.<br><br><em>2-5ms local CPU inference, $0 API tokens.</em>"
    )
    dm3 = (
        "<strong>Когда выбирать:</strong><br>• Замена фона вокруг товара в e-commerce.<br>• Создание фотореалистичных текстур и сцен.<br>• Вариативность концепт-арта и баннеров.<br><br><em>Сложное семантическое рассуждение о пикселях и свете.</em>"
        if is_ru else
        "<strong>When to choose:</strong><br>• E-commerce background replacement.<br>• Photorealistic texture and lighting synthesis.<br>• Creative asset variations.<br><br><em>Semantic reasoning over high-dimensional pixels.</em>"
    )

    html += f"""
      <section class="slide-page" id="slide-19">
        {slide_header(19, s19_tag, s19_title, s19_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 14px;">
            <div class="c4-card flex-1">
              <div class="card-label">SOFTWARE 1.0 • DETERMINISTIC</div>
              <div class="card-title">Figma / CSS / SVG / Pillow</div>
              <div class="card-desc" style="line-height: 1.55; margin-top: 8px;">{dm1}</div>
            </div>
            <div class="c4-card flex-1">
              <div class="card-label">SOFTWARE 2.0 • CLASSICAL CV</div>
              <div class="card-title">OpenCV / YOLO / Canny</div>
              <div class="card-desc" style="line-height: 1.55; margin-top: 8px;">{dm2}</div>
            </div>
            <div class="c4-card highlight flex-1">
              <div class="card-label" style="color: var(--c4-primary);">SOFTWARE 3.0 • GENERATIVE AI</div>
              <div class="card-title">Diffusion & Multimodal APIs</div>
              <div class="card-desc" style="line-height: 1.55; margin-top: 8px;">{dm3}</div>
            </div>
          </div>
        </div>
        {slide_footer(19)}
        <div class="speaker-notes" style="display:none;">{"Сначала проблема, а не AI. Не генерировать текст диффузией - использовать детерминированные инструменты." if is_ru else "Problem first, not AI first. Never generate critical typography with diffusion; use deterministic design tools."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 20: HOMEWORK ASSIGNMENT
    # -------------------------------------------------------------
    s20_tag = "ДОМАШНЕЕ ЗАДАНИЕ" if is_ru else "HOMEWORK ASSIGNMENT"
    s20_title = "Домашнее задание: Reproducible Image Workflow Pack" if is_ru else "Homework: Reproducible Image Workflow Pack"
    s20_sub = "Создание воспроизводимого пакета генерации с формализацией ТЗ и аудитом качества" if is_ru else "Engineering a reproducible generation package with formal brief and quality scorecard"
    hw_sc = (
        "<strong>1. E-commerce:</strong> Замена фона товарной карточки с сохранением формы изделия (керамика, часы, электроника).<br><br><strong>2. YouTube / Медиа:</strong> Превью-обложка для ролика с пустой зоной под типографику (паттерн Creator Tools).<br><br><strong>3. Tech Event:</strong> Баннер технологического митапа с негативным пространством под даты и спикеров."
        if is_ru else
        "<strong>1. E-commerce:</strong> Product background replacement preserving geometry (ceramics, watch, electronics).<br><br><strong>2. YouTube / Media:</strong> Video thumbnail plate with clean negative space for typography (Creator Tools benchmark).<br><br><strong>3. Tech Event:</strong> Conference announcement banner with presentation-safe zones."
    )
    hw_ch = (
        "<div>✓ <code>brief.md</code> — заполненный Visual Generation Canvas (цель, табу, критерии).</div>"
        "<div>✓ <code>references/</code> — исходные фото-референсы (без приватных данных).</div>"
        "<div>✓ <code>prompt_v1.txt</code> и <code>prompt_v2.txt</code> — итерационный лог промптов.</div>"
        "<div>✓ <code>candidates/</code> — минимум 2 сгенерированных варианта.</div>"
        "<div>✓ <code>qa.md</code> — оценка кандидатов по рубрикатору (геометрия, артефакты, свет).</div>"
        "<div>✓ <code>selected/</code> — финальный принятый ассет + метаданные генерации.</div>"
        "<div style='margin-top: 6px; color: var(--c4-warning); font-size: 13px;'>➔ Ветка <code>lesson-04</code>, PR в <code>main</code>, коллаборатор: <code>ihar_rubanovich@epam.com</code>.</div>"
        if is_ru else
        "<div>✓ <code>brief.md</code> — completed Visual Generation Canvas (goals, constraints, criteria).</div>"
        "<div>✓ <code>references/</code> — source input assets (no unreleased private data).</div>"
        "<div>✓ <code>prompt_v1.txt</code> & <code>prompt_v2.txt</code> — prompt iteration audit trail.</div>"
        "<div>✓ <code>candidates/</code> — minimum 2 candidate generation outputs.</div>"
        "<div>✓ <code>qa.md</code> — defect audit scorecard evaluating failure modes.</div>"
        "<div>✓ <code>selected/</code> — final accepted asset with recorded execution metadata.</div>"
        "<div style='margin-top: 6px; color: var(--c4-warning); font-size: 13px;'>➔ Branch <code>lesson-04</code>, PR to <code>main</code>, invite: <code>ihar_rubanovich@epam.com</code>.</div>"
    )

    html += f"""
      <section class="slide-page" id="slide-20">
        {slide_header(20, s20_tag, s20_title, s20_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 16px;">
            <div class="c4-card flex-1">
              <div class="card-label">{"СЦЕНАРИЙ НА ВЫБОР" if is_ru else "CHOOSE ONE SCENARIO"}</div>
              <div class="card-title">{"3 прикладных трека" if is_ru else "3 Real-World Tracks"}</div>
              <div class="card-desc" style="line-height: 1.6; margin-top: 8px;">{hw_sc}</div>
            </div>
            <div class="c4-card highlight flex-15">
              <div class="card-label" style="color: var(--c4-primary);">{"ЧЕК-ЛИСТ АРТЕФАКТОВ • GENAI-HOMEWORKS/L04/" if is_ru else "ARTIFACT CHECKLIST • GENAI-HOMEWORKS/L04/"}</div>
              <div class="col" style="gap: 8px; margin-top: 8px; font-size: 13.5px; color: #e2e8f0;">{hw_ch}</div>
            </div>
          </div>
        </div>
        {slide_footer(20)}
        <div class="speaker-notes" style="display:none;">{"Домашнее задание: объяснить структуру репозитория и критерии приемки." if is_ru else "Homework memo: explain repository structure and objective rubric."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # SLIDE 21: WRAP-UP & NEXT SESSION
    # -------------------------------------------------------------
    s21_tag = "ИТОГИ И АНОНС" if is_ru else "SUMMARY & TEASER"
    s21_title = "Резюме, открытый микрофон и анонс Урока 05" if is_ru else "Wrap-up, Open Mic & Next Session Teaser"
    s21_sub = "3 главных вывода занятия и анонс перехода к генерации и трансформации видео" if is_ru else "3 core engineering takeaways and previewing our transition into video generation"
    t1 = "<strong>1. Картинка в продакшене — это ТЗ, а не лотерея.</strong> Фиксация геометрии и строгие запреты важнее декоративных прилагательных." if is_ru else "<strong>1. Production imagery is a specification, not roulette.</strong> Pinning geometry and sacred constraints outweighs decorative adjectives."
    t2 = "<strong>2. Маски и референсы дают аппаратный контроль.</strong> Разделяйте сигналы стиля, идентичности объекта и каркаса сцены." if is_ru else "<strong>2. Masks and reference signals provide hardware-level control.</strong> Decouple style, identity, and layout conditioning."
    t3 = "<strong>3. Айсберг 90% решает всё.</strong> Успех системы определяется объектным хранилищем, декодированием Base64 и Human-in-the-Loop." if is_ru else "<strong>3. The 90% iceberg governs production reliability.</strong> Object storage, Base64 decoding, and review gates determine success."
    l05_desc = (
        "Продолжение <strong>Модуля 2: Мультимодальность</strong>.<br><br>Переход от статичных пикселей к временному измерению: <strong>Runway Gen-3</strong>, <strong>Kling</strong>, <strong>OpenAI Sora</strong>, <strong>Pika</strong>. Управление движением камеры (Camera Motion Control), интерполяция кадров и сквозные видео-пайплайны."
        if is_ru else
        "Continuing <strong>Module 2: Multimodality</strong>.<br><br>Expanding from static pixels into the temporal domain: <strong>Runway Gen-3</strong>, <strong>Kling</strong>, <strong>OpenAI Sora</strong>, <strong>Pika</strong>. Camera Motion Control, frame interpolation, and end-to-end video pipelines."
    )
    open_mic = "🎙️ Микрофоны открыты — задавайте вопросы голосом и в чате!" if is_ru else "🎙️ Microphones open — questions welcome in voice and chat!"

    html += f"""
      <section class="slide-page" id="slide-21">
        {slide_header(21, s21_tag, s21_title, s21_sub)}
        <div class="slide-content-arena">
          <div class="row" style="flex: 1; gap: 16px;">
            <div class="c4-card highlight flex-1">
              <div class="card-label" style="color: var(--c4-primary);">{"ГЛАВНЫЕ ВЫВОДЫ УРОКА" if is_ru else "KEY TAKEAWAYS"}</div>
              <div class="col" style="gap: 12px; margin-top: 8px;">
                <div style="font-size: 14.5px; color: #e2e8f0; line-height: 1.5;">{t1}</div>
                <div style="font-size: 14.5px; color: #e2e8f0; line-height: 1.5;">{t2}</div>
                <div style="font-size: 14.5px; color: #e2e8f0; line-height: 1.5;">{t3}</div>
              </div>
            </div>
            <div class="c4-card accent-purple flex-1">
              <div class="card-label" style="color: var(--c4-purple);">NEXT SESSION • {"УРОК 05" if is_ru else "LESSON 05"}</div>
              <div class="card-title" style="font-size: 18px; margin-top: 4px;">{"Генерация и трансформация видео" if is_ru else "Video Generation Models & APIs"}</div>
              <div class="card-desc" style="font-size: 14px; line-height: 1.55; margin-top: 8px;">{l05_desc}</div>
            </div>
          </div>
          <div style="margin-top: 14px; text-align: center; font-size: 15px; color: var(--c4-primary); font-weight: 600;">
            {open_mic}
          </div>
        </div>
        {slide_footer(21)}
        <div class="speaker-notes" style="display:none;">{"Резюме урока, анонс видеогенерации (Урок 05) и переход к вопросам." if is_ru else "Wrap-up, teaser for video generation in Lesson 05, open mic."}</div>
      </section>
    """

    # -------------------------------------------------------------
    # FOOTER & SCRIPTS
    # -------------------------------------------------------------
    html += f"""
    </div>
  </main>

  <!-- Speaker Notes Drawer -->
  <aside id="speakerNotesDrawer">
    <div class="drawer-header">
      <span class="drawer-title">{notes_label}</span>
      <button class="drawer-close" onclick="toggleSpeakerNotes()">✕</button>
    </div>
    <div class="drawer-body" id="drawerBody">{"Заметки загружаются..." if is_ru else "Loading notes..."}</div>
  </aside>

  <!-- Grid View Modal -->
  <div id="gridModal">
    <div class="grid-header">
      <span class="grid-title">{grid_label}</span>
      <button class="drawer-close" onclick="toggleGridModal()">✕</button>
    </div>
    <div class="grid-cards" id="gridCardsContainer"></div>
  </div>

  <script>
    const slides = Array.from(document.querySelectorAll('.slide-page'));
    const totalSlides = slides.length;
    let currentSlide = 1;

    function updateFooter(slideNum) {{
      const pct = Math.round((slideNum / totalSlides) * 100);
      const counter = document.getElementById(`counter-s${{slideNum}}`);
      const fill = document.getElementById(`fill-s${{slideNum}}`);
      if (counter) counter.innerText = `${{String(slideNum).padStart(2, '0')}} / ${{totalSlides}}`;
      if (fill) fill.style.width = `${{pct}}%`;
    }}

    function showSlide(num) {{
      if (num < 1) num = 1;
      if (num > totalSlides) num = totalSlides;
      currentSlide = num;

      slides.forEach((s, idx) => {{
        if (idx + 1 === num) {{
          s.classList.add('active');
          updateFooter(num);
          const noteEl = s.querySelector('.speaker-notes');
          const drawerBody = document.getElementById('drawerBody');
          if (noteEl && drawerBody) {{
            drawerBody.innerHTML = noteEl.innerHTML;
          }}
        }} else {{
          s.classList.remove('active');
        }}
      }});
      window.location.hash = `#${{num}}`;
    }}

    function nextSlide() {{
      if (currentSlide < totalSlides) showSlide(currentSlide + 1);
    }}

    function prevSlide() {{
      if (currentSlide > 1) showSlide(currentSlide - 1);
    }}

    function toggleSpeakerNotes() {{
      document.getElementById('speakerNotesDrawer').classList.toggle('open');
    }}

    function toggleGridModal() {{
      const modal = document.getElementById('gridModal');
      modal.classList.toggle('open');
      if (modal.classList.contains('open')) buildGridCards();
    }}

    function buildGridCards() {{
      const container = document.getElementById('gridCardsContainer');
      container.innerHTML = '';
      slides.forEach((s, idx) => {{
        const titleEl = s.querySelector('.slide-title');
        const title = titleEl ? titleEl.innerText : `Slide ${{idx + 1}}`;
        const card = document.createElement('div');
        card.className = 'grid-card-item';
        card.innerHTML = `
          <span class="grid-card-num">SLIDE ${{String(idx + 1).padStart(2, '0')}}</span>
          <span class="grid-card-title">${{title}}</span>
        `;
        card.onclick = () => {{
          showSlide(idx + 1);
          toggleGridModal();
        }};
        container.appendChild(card);
      }});
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {{
        e.preventDefault(); nextSlide();
      }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {{
        e.preventDefault(); prevSlide();
      }} else if (e.key.toLowerCase() === 'n') {{
        e.preventDefault(); toggleSpeakerNotes();
      }} else if (e.key.toLowerCase() === 'g') {{
        e.preventDefault(); toggleGridModal();
      }} else if (e.key.toLowerCase() === 'f') {{
        e.preventDefault();
        if (!document.fullscreenElement) {{
          document.documentElement.requestFullscreen().catch(() => {{}});
        }} else {{
          document.exitFullscreen().catch(() => {{}});
        }}
      }} else if (e.key === 'Escape') {{
        const modal = document.getElementById('gridModal');
        if (modal.classList.contains('open')) toggleGridModal();
      }}
    }});

    // 5-min timer
    let timerDuration = 5 * 60;
    let timerRemaining = timerDuration;
    let timerInterval = null;

    function formatTime(sec) {{
      const m = Math.floor(sec / 60).toString().padStart(2, '0');
      const s = (sec % 60).toString().padStart(2, '0');
      return `${{m}}:${{s}}`;
    }}

    function toggleBreakTimer() {{
      const btn = document.getElementById('timerToggleBtn');
      if (timerInterval) {{
        clearInterval(timerInterval);
        timerInterval = null;
        btn.innerText = '{start_5m}';
        btn.style.background = 'var(--c4-warning)';
        btn.style.color = '#0c111a';
      }} else {{
        btn.innerText = '{pause_txt}';
        btn.style.background = 'var(--c4-danger)';
        btn.style.color = '#fff';
        timerInterval = setInterval(() => {{
          if (timerRemaining > 0) {{
            timerRemaining--;
            const disp = document.getElementById('breakTimerDisplay');
            if (disp) disp.innerText = formatTime(timerRemaining);
          }} else {{
            clearInterval(timerInterval);
            timerInterval = null;
            btn.innerText = '{time_up}';
            btn.style.background = 'var(--c4-success)';
          }}
        }}, 1000);
      }}
    }}

    function resetBreakTimer() {{
      if (timerInterval) {{
        clearInterval(timerInterval);
        timerInterval = null;
      }}
      timerRemaining = timerDuration;
      const disp = document.getElementById('breakTimerDisplay');
      if (disp) disp.innerText = formatTime(timerRemaining);
      const btn = document.getElementById('timerToggleBtn');
      if (btn) {{
        btn.innerText = '{start_5m}';
        btn.style.background = 'var(--c4-warning)';
        btn.style.color = '#0c111a';
      }}
    }}

    const hashVal = parseInt(window.location.hash.replace('#', ''), 10);
    if (!isNaN(hashVal) && hashVal >= 1 && hashVal <= totalSlides) {{
      showSlide(hashVal);
    }} else {{
      showSlide(1);
    }}

    window.addEventListener('hashchange', () => {{
      const h = parseInt(window.location.hash.replace('#', ''), 10);
      if (!isNaN(h) && h >= 1 && h <= totalSlides) showSlide(h);
    }});
  </script>
</body>
</html>
"""
    return html

def main():
    # 1. Russian Deck
    ru_html = render_html(lang="ru")
    out_ru = BASE_DIR / "presentation_L04_Image_Generation_APIs.html"
    out_ru.write_text(ru_html, encoding="utf-8")
    print(f"Generated RU Deck: {out_ru} ({len(ru_html)} bytes)")

    # 2. English Deck
    en_html = render_html(lang="en")
    out_en = BASE_DIR / "presentation_L04_Image_Generation_APIs_EN.html"
    out_en.write_text(en_html, encoding="utf-8")
    print(f"Generated EN Deck: {out_en} ({len(en_html)} bytes)")

if __name__ == "__main__":
    main()