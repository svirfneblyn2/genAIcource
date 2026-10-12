# Урок 05 • Live Demo Runbook & Prompt Copybook
## Сборник готовых промптов и сценариев для живого показа генерации видео

**Курс:** GenAI Basics • Модуль 2 (Мультимодальность)  
**Инструктор:** Игорь Рубанович (EPAM Systems • `ihar_rubanovich@epam.com`)  
**Сервисы (октябрь 2026):** Kling 3.0 (Web & API), Runway Gen-4.5, Google Veo 3.1 (Gemini API / Vertex AI) и Gemini Omni (приложение Gemini / Flow), Luma Ray3.2 (Dream Machine), HeyGen / Hedra. Sora закрыта (приложение — 26.04.2026, API — 24.09.2026).  
**Код:** короткий пример `google-genai` (Veo) — слайд 14 и Блок 9 ниже. Ноутбук `L05_Video_Generation_API_Pipeline.ipynb` работает с реальным Veo 3.1 API; платные вызовы выключены флагом `RUN_PAID = False`.

Этот документ предназначен для спикера и студентов: во время занятия или самостоятельной практики вы можете скопировать промпты, вставить их в выбранный сервис вместе с референсными кадрами из L04 и получить более предсказуемый результат. Гарантий нет — каждый клип проверяйте по чек-листу приёмки (слайд 16).

> **Привязка к деку v2 (19 слайдов):** Блок 2 → слайды 4, 5, 8 • Блок 3 → слайд 9 • Блок 4 → слайды 5, 8 • Блоки 5–6 → слайд 10 • Блок 7 → слайд 18 (трек А) • Блок 9 → слайд 14 • Блоки 1, 8, 10 — вне дека (доп. материал; звук и речь — в L06).  
> **На занятии** показываем только готовые клипы из `demo_veo_showcase/` (новые не генерируем), по клику и без звука. В Microsoft Teams при демонстрации экрана включите «Оптимизировать для движения и видео».

---

## Оглавление

1. [Блок 1: Хук-викторина (4 видеосцены A–D)](#блок-1-хук-викторина-4-видеосцены-ad)
2. [Блок 2: Ловушка свободного промпта vs 6-слотовый temporal-промпт](#блок-2-ловушка-свободного-промпта-vs-6-слотовый-temporal-промпт)
3. [Блок 3: Кинематографический словарь камеры (Pan, Dolly, Orbit, FPV)](#блок-3-кинематографический-словарь-камеры)
4. [Блок 4: Пайплайн Image-to-Video (Курьер Glovo в дождь)](#блок-4-пайплайн-image-to-video-курьер-glovo-в-дождь)
5. [Блок 5: Motion Brush (Колеса и брызги + статичная зона)](#блок-5-motion-brush-региональная-динамика)
6. [Блок 6: First & Last Frame (Интерполяция пути курьера)](#блок-6-first--last-frame-интерполяция)
7. [Блок 7: E-Commerce пэкшот товара (Кружка: Orbit & Steam)](#блок-7-e-commerce-пэкшот-товара)
8. [Блок 8: Говорящий аватар и липсинк (Talking Head)](#блок-8-говорящий-аватар-и-липсинк)
9. [Блок 9: Асинхронный вызов через Python SDK](#блок-9-асинхронный-вызов-через-python-sdk)
10. [Блок 10: Продакшн-матрица сториборда (Студийный кейс Creator Tools)](#блок-10-продакшн-матрица-сториборда-студийный-кейс-creator-tools)

---

## Блок 1: Хук-викторина (4 видеосцены A–D)

> **В деке v2 не используется:** хук на слайде 2 — готовый ролик `final` (23 с). Блок оставлен как доп. материал.  
> **Цель:** Интерактивная калибровка внимания аудитории на микроартефактах физики и движения.  
> **Формат:** 16:9, 24 fps, длительность 4–5 сек.

### Клип [A] • FPV-дрон над каньоном (Google Veo 3.1)
```text
High-speed cinematic FPV drone dive down a dramatic red sandstone canyon, skimming just inches above jagged rocks and desert brush, golden hour sunlight flaring across the camera lens, extreme motion blur on foreground rocks, perfectly smooth stabilization.
```

### Клип [B] • Макро-слоумо кофе (Runway Gen-4.5)
```text
Extreme macro close-up, 120fps high-speed phantom camera footage: dark rich espresso pouring into a ceramic mug, liquid creating a deep vortex, tiny microscopic droplets splashing upwards in zero-gravity slow motion, warm morning backlight illuminating steam particles.
```

### Клип [C] • Диалог крупным планом (Kling 3.0 Omni)
```text
Cinematic tight portrait of a 28-year-old woman speaking passionately in an emotional dialogue, authentic natural eye blinks, subtle micro-movements of facial muscles and eyebrows, natural dental texture, shallow depth of field, 85mm portrait lens, 24fps.
```

### Клип [D] • Ночной неоновый Токио (Wan 2.2 MoE)
```text
A rainy night on a bustling Tokyo pedestrian crossing, pedestrians holding transparent umbrellas, neon signs reflecting coherently in deep asphalt puddles, camera smoothly tracking forward at waist height, anamorphic lens flares, wet reflective textures.
```

---

## Блок 2: Ловушка свободного промпта vs Инженерный пайплайн (Showcase в Veo / Kling)

> **Цель:** Наглядно показать, как наивный «поток сознания» в Text-to-Video ломает физику, анатомию и монтаж, и как инженерная декомпозиция на 3 шота (I2V) дает безупречный результат.  
> **Готовые материалы:** Папка `demo_veo_showcase/` с ключевыми кадрами `shot1_cafe_pickup.png`, `shot2_bike_rain.png`, `shot3_map_route.png` и скриптом склейки `assemble_montage.py`.

### 2.1. Наивный «поток мыслей» (Trainwreck T2V)
```text
Our friendly Glovo delivery courier enters a warm cozy Scandinavian cafe, walks up to the wooden counter and picks up a brown paper food delivery bag, puts it securely inside her turquoise backpack, then cuts to her riding a city bicycle through the rainy avenue at dusk with glowing streetlights and wet cobblestones, and then camera zooms in to a digital smartphone map with a glowing navigation route arrow pointing to the delivery address.
```
*Что наблюдать (4 типичные ошибки — по реальному клипу `trainwreck_naive_t2v.mp4`, слайд 4):*
1. **00:02 — Действие пропущено:** пакет остался на стойке — в рюкзак его так и не положили.
2. **00:03 — Детали поплыли после склейки:** надпись на коробе меняется («Glono» → «Glovo») — заодно пример порчи бренда.
3. **00:05 — Пространство сломалось:** руль с телефоном «въезжает» в кадр, а курьер всё ещё едет впереди.
4. **00:07 — Псевдотекст:** «Delivery Admest» вместо «Delivery Address».

Причина одна: на 8 секунд модели дали 3 сцены и 5 действий.

### 2.2. Профессиональный 6-слотовый промпт (Одиночный шот)
```text
[Subject & State]: Young Glovo delivery courier wearing a vibrant yellow jacket with gray reflective stripe and a matte black helmet, seated on a gravel bicycle.
[Action Vector]: Pedals forward at a steady moderate rhythm, body leaning slightly forward, hands firmly gripping drop handlebars, wheels spinning smoothly forward.
[Camera Trajectory]: Smooth low-angle tracking shot moving parallel to the bicycle on the left, camera locked at wheel height, steady horizon, zero camera shake.
[Environment Dynamics]: Wet city street at dusk, tires cutting through shallow rainwater puddles with fine water spray, neon shop reflections shimmering on asphalt.
[Lighting & Tempo]: Cinematic twilight, warm sodium streetlights, 24fps film motion blur, natural momentum and deceleration.
[Negative Constraints]: No backwards wheel rotation, no morphing of bicycle frame, no extra limbs, no camera jitter, no unrealistic speed bursts.
```
*Примечание:* слот «Negative» работает там, где есть отдельное поле negative prompt (Kling, Wan). Для Veo переформулируйте позитивно («wheels spinning forward», «smooth steady camera»). Реальный промпт нашего шота 2 — на слайде 8.

---

## Блок 3: Кинематографический словарь камеры

> **Цель:** Продемонстрировать управляемость виртуальной камеры через стандартные термины кинооператоров.  
> **Сервис:** Runway Gen-4.5 (камера словами или настройками направления и силы движения) / Kling 3.0 (камера задаётся в промпте) / Gemini, Flow (только словами).  
> **Формат:** 16:9, длительность 5 сек (Veo 3.1 — 4/6/8 сек). Совет: одно движение камеры на шот.

### 3.1. Dolly In (Кинематографический наезд с параллаксом)
```text
Cinematic slow Dolly In on an antique brass microscope standing on an oak laboratory table, foreground dust particles drifting, background bookshelf softly blurring, 35mm lens, steady camera movement forward.
```

### 3.2. Orbit / Arc Shot (Облёт)
```text
Smooth slow orbit arc shot revolving partway around a luxury mechanical wristwatch placed on dark volcanic stone, continuous smooth counter-clockwise camera circle, subtle glints of light reflecting off the sapphire glass.
```

### 3.3. Crane Up / Jib Shot (Подъем крана)
```text
Camera starts at ground level looking at autumn fallen leaves on wet cobblestones, then smoothly cranes upward 10 feet into the air to reveal a historic European cathedral square at sunrise.
```

---

## Блок 4: Пайплайн Image-to-Video (Курьер Glovo в дождь)

> **Цель:** Главный производственный паттерн. Оживление утвержденного статичного кадра из L04 без потери внешности.  
> **Входной файл:** `GenAI Basics — Course Production/L04/assets/examples/C2_rain.jpg`  
> **Куда загружать:** Поле первого кадра (image-to-video) в Kling 3.0 / Runway Gen-4.5 / Flow (Veo 3.1).

### Промпт движения (камера + действие + детали движения):
```text
The courier begins pedaling forward down the rainy street, bicycle wheels rotating smoothly forward cutting through puddles with realistic water spray. Soft rain streaks fall diagonally across the frame. Camera tracks steadily alongside at bicycle speed. Background urban buildings and streetlights blur with gentle motion bokeh. Maintain exact facial features, curly hair, earring, and yellow jacket colors unchanged.
```

*Параметры в интерфейсе:*
* Камера: словами в промпте («tracking shot alongside»). Где есть отдельные настройки — в Runway направление и сила движения, в Kling параметры камеры — выберите одно горизонтальное движение без зума.
* Длительность: `5s` (Veo 3.1 — `4/6/8s`).
* Конкретные числа в настройках подбираются под сервис — универсальных значений нет.

---

## Блок 5: Motion Brush (Региональная динамика)

> **Цель:** Задать, что и куда движется в кадре, а фон оставить неподвижным (слайд 10).  
> **Сервис:** Kling, инструмент Motion Brush — есть в моделях Kling 1.x–2.x; в списке функций Kling 3.0 его нет. Официально: до 6 выделенных элементов, у каждого своя 2D-стрелка-траектория на кадре, плюс Static Brush (статичная зона). Оси Z и числовой скорости нет.  
> **Входной файл:** `C2_rain.jpg`.

### Разметка:
1. **Элемент 1 — курьер с велосипедом:** стрелка-траектория по направлению движения (вперёд по улице).
2. **Элемент 2 — брызги из лужи у колеса:** короткая стрелка от лужи вверх-назад.
3. **Static Brush — фон (здания, фонари):** статичная зона, фон не двигается.

Внешность курьера (лицо, куртка, рюкзак) держим одобренным первым кадром (I2V), а не маской. Результат стабильнее, но не гарантирован — проверяйте по чек-листу.

---

## Блок 6: First & Last Frame (Интерполяция)

> **Цель:** Управляемый переход между двумя фиксированными состояниями сюжета (модель достраивает движение между двумя картинками).  
> **Сервис:** режим «первый + последний кадр»: Kling 3.0 / Veo 3.1 (Flow; в API — `lastFrame`) / Gemini Omni / Hailuo H3.  
> **Стартовый кадр (Start Frame):** `C3_door.jpg` (Курьер берет пакет у стойки кофейни).  
> **Финальный кадр (End Frame):** `C4_rest.jpg` (Курьер выходит на крыльцо кофейни с пакетом).

### Промпт связки:
```text
The courier nods politely to the barista, turns around with the paper bag securely held in one hand, walks smoothly across the polished wooden floor toward the glass entrance door, pushes the door open with his elbow, stepping out onto the street. Physically plausible human movement, natural weight shift, seamless transition between keyframes.
```

---

## Блок 7: E-Commerce пэкшот товара (Кружка: Orbit & Steam)

> **Цель:** Коммерческая видеореклама для карточки маркетплейса на основе пэкшота из L04 (= трек А домашки, слайд 18).  
> **Входной файл:** `D0_packshot.png` (Керамическая кружка на белом фоне) или `A3_details.jpg` (Кружка на деревянной стойке).  
> **Куда загружать:** Kling 3.0 / Luma Ray3.2 (у Luma есть готовые движения Orbit left/right; режима «360° облёт» нет) / Flow (Veo 3.1) — Image-to-Video.

### Промпт анимации пэкшота:
```text
Camera performs an elegant slow orbit arc around the ceramic coffee mug on the wooden counter, thin delicate wisp of aromatic steam rising and swirling gracefully from the hot dark coffee, warm morning sunlight creating shimmering caustic reflections inside the mug, premium cinematic commercial lighting, smooth steady motion.
```

---

## Блок 8: Говорящий аватар и липсинк (Talking Head)

> **В деке v2 не показывается** — звук и речь разбираем в L06.  
> **Цель:** Демонстрация аватаров для корпоративных FAQ и обучения. Аватары/липсинк — отдельная ниша; диалог со звуком умеют и генеративные модели (Veo 3.1, Kling 3.0, Seedance и др.).  
> **Сервис:** HeyGen (Avatar V) / Hedra (Character-3, Omnia) / Kling 3.0 (диалог с нативным звуком).  
> **Входной портрет:** Фото курьера крупным планом или оператора службы поддержки.  
> **Аудиофайл:** Сгенерированная реплика (или текстовый ввод TTS).

### Текст реплики для проверки артикуляции:
```text
"Здравствуйте! Ваш заказ из кофейни успешно получен. Я уже выехал по вашему адресу и буду у парадной через двенадцать минут. Пожалуйста, держите телефон под рукой!"
```
*На что обратить внимание:* Синхронность согласных букв (Б, П, М) при смыкании губ, естественное моргание, отсутствие искажений зубов.

---

## Блок 9: Асинхронный вызов через Python SDK

> **Цель:** Показать, как это выглядит в коде (слайд 14, только для справки — для ДЗ код не нужен).  
> **Библиотека:** `google-genai` (та же, что в L03 и L04), ключ из переменной `GEMINI_API_KEY`. Бесплатного тарифа для Veo нет: 720p — Veo 3.1 $0.40/с, Fast $0.10/с, Lite $0.05/с; платим только за успешные видео.

```python
import time
from google import genai
from google.genai import types

client = genai.Client()  # ключ из GEMINI_API_KEY
op = client.models.generate_videos(
    model="veo-3.1-fast-generate-preview",
    prompt="Tracking shot alongside the courier",
    image=types.Image.from_file(location="shot2.png"),
)
while not op.done:  # ждём: от ~11 с до ~6 мин
    time.sleep(10)
    op = client.operations.get(op)
video = op.response.generated_videos[0].video
client.files.download(file=video)
video.save("shot2.mp4")
```

Три шага: **отправил → подождал → скачал**. Видео делается долго, поэтому сервис сразу возвращает «квитанцию» (операцию), а мы раз в 10 секунд спрашиваем, готово ли.

---

## Блок 10: Продакшн-матрица сториборда (Студийный кейс Creator Tools)

> **Цель:** Показать промышленный стандарт подготовки многокадрового ролика (Multi-Shot Video Pipeline) на примере реального R&D-проекта спикера — 10-серийного исторического псевдодокументального цикла *Giant Stories* (лабораторный проект Creator Tools).  
> **Главный инсайт:** Профессиональный ИИ-видеопродакшн начинается не в интерфейсе диффузионной модели, а в **7-колоночной таблице раскадровки**, где каждый шот заранее связывается с оптикой, вектором движения, звуковыми слоями и музыкой.

### 10.1. Эталонная 7-колоночная матрица шотов (Storyboard Matrix)

| # | Шот / Тайминг | Ключевой визуальный хук | Закадровый голос (Voice-Over) | IMAGE prompt (Оптика, свет, стиль) | VIDEO prompt (Кинематика, динамика, эффекты) | Фоли SFX слой | Музыкальный акцент |
| :- | :- | :- | :- | :- | :- | :- | :- |
| **01** | `Sealed Crate 1929` (5 сек) | Опечатанный ящик `PECOS 1423` в таможенном подвале | *«Этот ящик был опечатан таможней в 1929 году — и с тех пор его никто не открывал...»* | `16:9 cinematic aspect-ratio, grainy black-and-white archival still. Dim Customs vault, single brass gas-lamp overhead (2700K). Weathered pine crate stencilled "PECOS 1423 • CONFIDENTIAL". Cobweb traces, dust motes. Negative: no color, no modern barcodes, no LED.` | `16:9 archival motion, 5s. Handheld dolly-in (35mm) from darkness toward lamplit crate. Slow speed-ramp; subtle handheld micro-shake; gate-weave flicker. Negative: no morphing, no digital noise.` | Гул подвала, капли воды, шуршание крысы | Низкий контрабасовый дрон, приглушенная медь |
| **02** | `Drill Strike` (5 сек) | Геологи на буровой натыкаются на гигантскую кость | *«Обычная разведка нефти наткнулась на нечто тверже гранита...»* | `16:9 cinematic b&w still, 24mm wide lens. High-noon desert sun, Rio Grande brush. Three oil drillers in grease-stained coveralls frozen in shock around drill pit, massive fossilized bone exposed in clay.` | `16:9 crane-down, 5s, 24mm. Shot starts on dust-blown sky, smoothly descends toward excavation pit; soil crumbles, heat haze shimmers. Steady descent.` | Стрекот цикад, скрежет лопаты, удивленный вздох | Удар тома ➔ пульсирующий суб-бас каждые 2 сек |
| **03** | `Rotary Press` (5 сек) | Газетные ротационные машины печатают сенсацию | *«Газеты от Сан-Антонио до Хьюстона кричали о 4-метровом титане...»* | `16:9 overhead pressroom still, 40mm lens. Historic rotary printing press in full motion, fresh newspapers with bold headline "GIANT UNEARTHED", ink mist, harsh industrial pendants.` | `16:9 whip-pan, 5s, 40mm. Rapid whip-pan starting from spinning mechanical gears, landing crisp and locked on the moving paper headline. Frame jitter, paper flutter.` | Грохот типографии, шипение свежей краски | Нарастающее тремоло струнных |
| **04** | `Smithsonian Denial` (5 сек) | Клерк за пишущей машинкой штампует отказ | *«Смитсоновский институт заявил, что груз так и не прибыл...»* | `16:9 desk-level still, 50mm lens. Green banker lamp casting warm pool of light. Remington typewriter, typed official refusal letter, wax stamp, cigarette smoke curling.` | `16:9 macro push, 5s, 50mm. Slow push-in racking focus from typewriter keys to ink signature and red "DENIED" stamp. Zero camera shake.` | Сухой стук клавиш машинки, звонок каретки, гул лампы | Одиночная партия виолончели, тиканье часов |

---

### 10.2. Библиотека профессиональной операторской оптики (Lens & Camera Grammar)

Использование точных физических параметров оптики (фокусное расстояние, диафрагма, схема света) кардинально улучшает управляемость кадра:

1. **24mm Wide-Angle (Эпический масштаб и глубина):**
   * *Промпт камеры:* `16:9 crane-down, 24mm wide lens. Smooth descent from wide horizon down to foreground rocks; pronounced perspective distortion on edges, expansive depth of field.`
2. **35mm Cinematic Street/Action (Естественное восприятие человека):**
   * *Промпт камеры:* `16:9 handheld tracking shot, 35mm lens. Camera glides forward at waist height following the subject; gentle natural sway, balanced foreground/background relationship.`
3. **40mm Whip-Pan (Динамический монтажный переход):**
   * *Промпт камеры:* `16:9 rapid whip-pan, 40mm lens. Fast directional camera sweep with intense horizontal motion blur, resolving instantly onto stationary subject.`
4. **45mm Parallax Slide (Плавное скольжение с разделением планов):**
   * *Промпт камеры:* `16:9 lateral parallax tracking slide, 45mm lens. Camera slides horizontally left to right; foreground objects move noticeably faster than background, creating tactile dimensional depth.`
5. **50mm Macro Push & Rack-Focus (Драматический фокус на детали):**
   * *Промпт камеры:* `16:9 macro push, 50mm lens, f/2.0 shallow depth of field. Camera pushes forward 10 inches while racking focus smoothly from blurred foreground object to pin-sharp background detail.`
6. **60mm Orbit Arc (Студийный круговой облет предмета):**
   * *Промпт камеры:* `16:9 continuous 180-degree orbit, 60mm lens. Smooth circular tracking around the central subject, background slowly rotating with creamy bokeh.`

---

### 10.3. Паттерн рефлексивной генерации сценария в ChatGPT (Self-Reflection Loop)

Чтобы LLM генерировала не плоские клише, а плотный кинематографический сценарий, адаптированный под генераторы видео (Kling, Runway, Veo), используйте мета-промпт с встроенным шагом самокритики:

```text
Act as an elite documentary film director and visual showrunner.
Let's work step-by-step to generate a suspenseful 6-scene storyboard (each shot strictly 5 seconds).

For each scene:
1. Describe the key visual action and emotional beat.
2. Formulate the exact voice-over line (maximum 12 words, tense and cinematic).
3. Draft a 16:9 Image Prompt specifying lens focal length (mm), lighting temperature (Kelvin), and historical textures.
4. Draft a matching 16:9 Video Motion Prompt specifying exact camera kinematics (dolly, crane, whip-pan) and physical dynamics.
5. SELF-REFLECTION STEP: Before finalizing the scene, ask yourself: "What specific visual flaw or ambiguity would cause a video diffusion model to morph or hallucinate here?" Add explicit negative constraints to eliminate that risk.

Let's begin with Scene 1.
```

---

### 10.4. Практическая экономика токенов и времени в Kling AI

Уроки из сотен часов продакшена Creator Tools:
1. **Переключатель «1 вывод вместо 2» (Single Output Mode):** В веб-интерфейсе Kling по умолчанию включена генерация 2 вариантов на каждый промпт. Для драфтов и проверки композиции **всегда переключайте на 1 вывод** — это экономит ровно **50% баланса кредитов**.
2. **Короткие сегменты вместо длинных:** Kling 3.0 умеет 3–15 с за генерацию, но на черновиках не начинайте с длинных клипов: короткие шоты стабильнее длинных, а ошибки в длинной сцене дороже переделывать. Генерируйте шоты по 5 с и при необходимости продлевайте клип или склеивайте шоты в монтаже.
3. **Водяной знак и маркировка:** даже если сервис позволяет скачать клип без видимого водяного знака, пометку «создано ИИ» в публикации сохраняйте (EU AI Act, ст. 50 — слайд 17).
4. **Оффлайн-апскейл (Topaz Video AI vs Cloud Upscale):** Облачные апскейлеры внутри генераторов стоят дополнительных кредитов и часто «замыливают» зернистость. Промышленный стандарт — скачивание нативного 1080p рендера и локальный апскейл через Topaz Video AI (модели Proteus или Iris) с сохранением плёночного зерна.

