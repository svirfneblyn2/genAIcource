# L04 — план исправлений презентации (v2), 2026-10-12

Источник: ревью презентации `presentation_L04_Image_Generation_Services_and_Prompts.html` (RU) и `_EN.html`.
Факты сверять с `L04_08_Source_Notes_Research_2026-10.md`.
Результат: новые файлы `presentation_L04_Image_Generation_Services_and_Prompts_v2.html` / `_EN_v2.html` + PDF. Исходники v1 не трогаем.

Важно: `deck/*.py` устарели (2026-10-02) и не содержат хука/правок 11 октября. Правим HTML напрямую.

## P0 — факты (устаревшее / неверное)

| # | Слайд | Было | Стало |
|---|---|---|---|
| F1 | 6 OpenAI | DALL-E 3 / GPT Image 2.5; `dall-e-3`, `gpt-4o-image`; Assistants API | GPT Image 2 / 2.5; `gpt-image-2`, `gpt-image-2.5-flare` / `-sunburst`; убрать Assistants API |
| F2 | 6 Google | Imagen 3 / Nano Banana Pro | Nano Banana 2 / Pro / 2 Lite; `gemini-3.1-flash-image`, `gemini-3-pro-image`, `gemini-3.1-flash-lite-image` |
| F3 | 6 BFL | FLUX.1 (Pro/Dev/Schnell) | FLUX.2 (Pro/Flex/Dev, открытые веса, до 10 референсов) → FLUX 3 (07.2026) |
| F4 | 6 Midjourney | V6.1 / V8.2 | V8.2 (+ Edit Model, до 4 референсов) |
| F5 | 5, 9 | «Google Imagen», «OpenAI DALL-E», «DALL-E / Imagen 3» | GPT Image 2.x, Nano Banana, FLUX.2 |
| F6 | 5, 7 | Kling и Grok как SaaS-агрегаторы; Leonardo «просто прокси» | Kling (IMAGE 3.0/O1) и Grok (Aurora) — свои модели; Leonardo — свои модели (Phoenix/Lucid) + сторонние |
| F7 | 7 | «переключение между FLUX, Midjourney, SDXL» | убрать Midjourney (нет публичного API) → FLUX, GPT Image, Nano Banana, SDXL |
| F8 | 17, 19 | Midjourney Character Reference | Midjourney: Edit Model (до 4 референсов, заменил --cref/--oref в 08.2026) |
| F9 | 3 | «Хроника», «2026 Pro VLM», «судебный эксперт не отличит» | подпись «Реконструкция стиля эпохи (сгенерировано в 2026)», «2025 Nano Banana Pro», в заметке — «на глаз не отличить; SynthID — отличит» |
| F10 | 23 | «спектральный маркер Google», «в США и ЕС» | SynthID — водяной знак в пикселях (Google, у OpenAI с 05.2026) + C2PA; США: Thaler, отказ Верховного суда 02.03.2026; Disney/Universal v. Midjourney |
| F11 | 11 | «35mm (угол без дисторсии)» | «35mm (естественный умеренно широкий угол)» |
| F12 | 11 | Только `Constraints: no …` | + строка: Gemini лучше слушает позитивные формулировки («empty shop» вместо «no people»), `--no` / negative prompt — для MJ/SD |

## P1 — преувеличения и противоречия

| # | Слайд | Исправление |
|---|---|---|
| C1 | 11, 18, 19, 20 | убрать «100%»: «высокий контроль», «удерживает лицо», «заметно стабильнее» |
| C2 | 15 vs 23 | единое число: «после ~5–8 правок дрейф заметен» в обоих |
| C3 | 12 | must-have «лаванда слева» → честный чек-лист приемки: ✅ текст, ✅ круассан, ⚠️ лаванда не слева, ❌ лишний текст на доске сверху |
| C4 | 22 | «50 карточек за 3 минуты» → «~50 карточек за ~10 минут и ~$2–3»; код: цикл по `parts`, брать `inline_data` |
| C5 | 9 notes | «скрипт из слайда 21» → «слайда 22» |
| C6 | 16 | «Inpainting» для чат-правки → «правка по инструкции»; inpainting — только про маску в Leonardo |
| C7 | 5/6 | единая терминология: «Слой 1/2/3» (без смеси Tier/Layer) |

## P2 — вёрстка / визуал

| # | Слайд | Исправление |
|---|---|---|
| V1 | 19 | сырой LaTeX `($t_0$)` → «t₀» |
| V2 | 20, 24 | баннер D4 обрезан (`object-fit: cover`) → `contain` на темном фоне |
| V3 | 10 | метки «2 люди» и «3 кот» налезают → разнести |
| V4 | 1 | надпись «MORNING» с коллажа просвечивает под подзаголовком → сменить плитку/усилить затемнение |
| V5 | 5 | PNG-схема (англ., псевдо-C4) → HTML/SVG-схема на языке дека в стиле дека |
| V6 | 7, 8 | сгенерированные макеты UI (Sintx/Leonardo с Midjourney внутри) и пустой экран Gemini → честные схемы-иллюстрации рабочего процесса (HTML/SVG или Codex-иллюстрация) с подписью «схема интерфейса», для чата — сцена диалога «замени только кружку» с кадрами A2→B1 |
| V7 | 11,16–19 | минимальный размер текста 14px; моноширинный шрифт — только код и промпты; разгрузить 11 и 18 |

## P3 — новое содержание

| # | Что |
|---|---|
| N1 | Вернуть слайд «Как модели рисуют»: диффузия (`denoise_0–3.jpg`) vs авторегрессия (патчи) — после слайда 5 |
| N2 | Слайд «Рынок на октябрь 2026»: GPT Image 2/2.5, Nano Banana 2/Pro, Grok Imagine 2.0, Midjourney V8.2, FLUX.2/3, Kling IMAGE 3.0, Seedream 5, Ideogram 4 (JSON-промпты), Recraft V4 (SVG) — сильная сторона, референсы, цена; Arena: GPT-Image-2 #1, Grok 2.0 #2 (08.2026) |
| N3 | Таблица слайда 9: цены по моделям вместо «$0.03» (Nano Banana 2 Lite ≈ $0.034/1K, legacy Nano Banana ≈ $0.039, Grok ≈ $0.02–0.06) |
| N4 | README: число слайдов, карта, тизер L05 = видео |

## Проверка
- скриншоты всех слайдов RU и EN (`deck/shoot.py`-подход, headless Edge 1600×900), визуальный контроль переполнения;
- grep на остатки: `DALL-E`, `Imagen 3`, `gpt-4o-image`, `FLUX.1`, `V6.1`, `100%`, `$t_0$`, `Assistants`.
