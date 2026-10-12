# Урок 04 • Live Demo Runbook & Prompt Copybook
## Сборник готовых промптов для живого показа и практики

**Курс:** GenAI Basics • Модуль 2 (Мультимодальность)  
**Инструктор:** Игорь Рубанович (EPAM Systems)  
**Модели / Сервисы:** Google Gemini (Nano Banana Pro / 2), ChatGPT (GPT-4o Images), Leonardo.ai, Midjourney v6.1  

Этот документ создан для того, чтобы во время лекции вы могли в один клик скопировать нужный промпт, вставить его в выбранный сервис или прикрепить референс и получить гарантированный, проверенный результат.

---

## Оглавление

1. [Блок 1: Свободный vs Структурный промпт (ChatGPT / Gemini)](#блок-1-свободный-vs-структурный-промпт)
2. [Блок 2: Точный текст и списки обязательных деталей](#блок-2-точный-текст-и-списки-обязательных-деталей)
3. [Блок 3: Дельта-правки («Измени только X, сохрани остальное»)](#блок-3-дельта-правки)
4. [Блок 4: Демо в Leonardo.ai (Canvas, Inpainting, Guidance Scale)](#блок-4-демо-в-leonardoai)
5. [Блок 5: Консистентный персонаж (Кейс курьера доставки Glovo)](#блок-5-консистентный-персонаж)
6. [Блок 6: E-commerce фотосессия товара (Кружка)](#блок-6-e-commerce-фотосессия-товара)
7. [Блок 7: Мульти-референсная композиция (Персонаж + Товар)](#блок-7-мульти-референсная-композиция)
8. [Блок 8: Словарь фотографа (Оптика и освещение)](#блок-8-словарь-фотографа)
9. [Блок 9: Интерактивный хук (6 исторических лиц 2014–2026)](#блок-9-интерактивный-хук)

---

## Блок 1: Свободный vs Структурный промпт

> **Цель демо:** Показать, как модель в свободном промпте «додумывает» 80% параметров сама, а в структурном (6 слотов) — строго следует инженерной спецификации.  
> **Куда вставлять:** ChatGPT, Gemini app или Colab.  
> **Формат:** 16:9.  

### 1.1. Свободный промпт (Free-form)
```text
a cozy coffee shop in the morning
```
*Что обсудить с аудиторией:* Модель сама выбрала ракурс, людей, мебель, освещение. Полная потеря контроля.

### 1.2. Структурный инженерный промпт (6 слотов)
```text
Subject: a speckled cream ceramic mug of black coffee with a thin wisp of steam, standing on a worn oak counter in the right third of the frame.
Setting: a small Scandinavian-style coffee shop at 7 a.m., empty, chairs still up on two tables in the soft-focus background, a brass espresso machine on the left.
Composition and camera: eye-level, 35mm lens, f/2.0, shallow depth of field, the mug is the sharpest object.
Lighting: low warm sunlight from a window on the left, long soft shadows, dust visible in the light beam.
Style: realistic editorial photography, natural colors, slight film grain.
Constraints: no people, no text, no logos.
```
*Что проверить:* Кафе пустое? Стулья подняты на столы? Кружка в правой трети? Свет слева? Каждый слот на месте.

---

## Блок 2: Точный текст и списки обязательных деталей

> **Цель демо:** Показать рендеринг надписей без опечаток и удержание мелких объектов.  
> **Куда вставлять:** ChatGPT, Gemini app (Nano Banana Pro) или AI Studio.  
> **Формат:** 16:9.  

```text
Subject: a speckled cream ceramic mug of black coffee with a thin wisp of steam, standing on a worn oak counter in the right third of the frame.
Setting: a small Scandinavian-style coffee shop at 7 a.m., empty, chairs still up on two tables in the soft-focus background, a brass espresso machine on the left.
Composition and camera: eye-level, 35mm lens, f/2.0, shallow depth of field, the mug is the sharpest object.
Lighting: low warm sunlight from a window on the left, long soft shadows, dust visible in the light beam.
Style: realistic editorial photography, natural colors, slight film grain.
Must-have details: next to the mug, a small black chalkboard sign written in white chalk handwriting that reads exactly "FLAT WHITE 3.50" on the first line and "OPEN 7:00" on the second line; a single croissant on a white plate behind the mug; a sprig of dried lavender in a tiny glass vase.
Constraints: no people, no other text, no logos.
```
*Правило:* Текст всегда в **кавычках**, со словом *exactly*, коротко, без лишних символов.

---

## Блок 3: Дельта-правки

> **Цель демо:** Не перегенерировать картинку с нуля, а передать ранее сгенерированный кадр как референс и изменить ровно один элемент.  
> **Куда вставлять:** ChatGPT (в том же треде) или Gemini app (прикрепить изображение из Блока 1.2).  

### 3.1. Замена объекта (Object Swap)
**Референс:** Прикрепить картинку `A2_structured.png` (или результат из Блока 1.2).
```text
Edit this photo. Replace only the ceramic mug with a tall glass of iced latte with visible layers of coffee and milk and a few ice cubes. Keep everything else exactly the same: camera angle, framing, counter, espresso machine, background, light direction and shadows. The new glass must cast a matching shadow on the counter.
```

### 3.2. Смена освещения и времени суток (Relighting)
**Референс:** Прикрепить картинку `A2_structured.png`.
```text
Edit this photo. Change only the time of day to a rainy evening: dark blue dusk outside the window, raindrops on the glass, warm interior pendant lamps switched on. Keep the exact same composition, objects, mug and camera angle.
```

---

## Блок 4: Демо в Leonardo.ai

> **Цель демо:** Показать Tier 2 Creative Canvas, за который платят дизайнеры: кисть инпейнтинга, точный Guidance Scale и негативные промпты.  
> **Где открывать:** [leonardo.ai](https://leonardo.ai) $\to$ **Canvas Editor** (или Image Generation).  

### 4.1. Генерация в Leonardo (Photoreal / Phoenix)
* **Prompt:**
```text
cinematic medium shot of an artisanal coffee corner, raw wooden table, ceramic tableware, soft morning haze, 50mm f/1.4, hyperrealistic, high fidelity
```
* **Negative Prompt:**
```text
blurry, low quality, cartoon, oversaturated, deformed hands, duplicate objects, plastic skin, watermark, signature
```
* **Параметры в панели:**
  - Model: Leonardo Phoenix или Kino XL
  - Guidance Scale: `7.0` (если поставить 14 — появятся кислотные пережженные артефакты; если 3 — проигнорирует промпт)
  - Aspect Ratio: `16:9`

### 4.2. Inpainting в Canvas (Замена кистью)
1. Загрузите кадр на холст Canvas.
2. Выберите инструмент **Mask (Кисть)** и закрасьте только кружку / центральный предмет.
3. Поместите рамку генерации (Bounding Box) прямо над замаскированной областью.
4. Введите промпт замены:
```text
a vintage bronze mechanical alarm clock, intricate gears, ticking bells, soft warm reflection
```
5. Нажмите **Generate** (сгенерируются 4 варианта вставки на выбор).

---

## Блок 5: Консистентный персонаж

> **Кейс:** Курьер доставки Glovo (сквозной бенчмарк курса).  
> **Куда вставлять:** ChatGPT, Gemini (Nano Banana Pro) или Midjourney.  

### 5.1. Мастер-референс: Character Reference Sheet
```text
Character reference sheet on a plain light grey background: the same young woman food delivery courier shown four times in a row - front view, three-quarter view, side profile, back view - full body, standing neutral pose. Fixed appearance: about 28 years old, short curly dark-brown hair, light-brown skin, small silver hoop earring in the left ear, bright yellow waterproof jacket with a reflective grey stripe across the chest, black cargo trousers, white sneakers, a square turquoise thermal delivery backpack. No brand names, no logos, no text. Clean, evenly lit studio photography.
```
*Результат сохраняем как `C1_sheet.png`.*

### 5.2. Сцена 1: Курьер на велосипеде под дождем
**Референс:** Прикрепить `C1_sheet.png`.
```text
Use the attached character sheet as the identity reference. The same courier (same face, hair, earring, yellow jacket with grey stripe, turquoise backpack) is riding a city bicycle through a rainy evening street with wet cobblestones reflecting shop lights. Medium shot, 50mm lens, motion blur in the background. Realistic photography. No logos, no text.
```

### 5.3. Сцена 2: Доставка у двери квартиры клиенту
**Референс:** Прикрепить `C1_sheet.png`.
```text
Use the attached character sheet as the identity reference. The same courier (same face, hair, earring, yellow jacket with grey stripe, turquoise backpack on her back) is standing at an apartment door and handing a brown paper food bag to a customer, whose hands only are visible. Warm hallway light, eye-level, 35mm lens. Realistic photography. No logos, no text.
```

### 5.4. Сцена 3: Перерыв на скамейке в парке
**Референс:** Прикрепить `C1_sheet.png`.
```text
Use the attached character sheet as the identity reference. Close-up portrait of the same courier (same face, curly hair, silver hoop earring, yellow jacket with grey stripe) sitting on a park bench during a break, smiling at her phone, turquoise backpack beside her. Golden-hour backlight, 85mm lens, f/1.8. Realistic photography. No logos, no text.
```

---

## Блок 6: E-commerce фотосессия товара

> **Кейс:** Керамическая кружка ручной работы.  
> **Формат:** 1:1 (квадрат для маркетплейса/каталога).  

### 6.1. Мастер-пэкшот на белом фоне (Packshot)
```text
Studio e-commerce packshot of a single handmade ceramic mug: cylindrical body, speckled cream glaze with small brown dots, unglazed terracotta-brown band at the base, round C-shaped handle on the right. Centered, three-quarter front view, pure white seamless background, soft even light, subtle contact shadow. No text, no logo.
```
*Результат сохраняем как `D0_packshot.png`.*

### 6.2. Кадр 1: Лайфстайл на кухне (Kitchen counter)
**Референс:** Прикрепить `D0_packshot.png`.
```text
Product photo session. Place exactly this mug (same shape, speckled cream glaze, terracotta base band, handle on the right) on a light travertine kitchen counter next to a window in the morning. A moka pot and a linen towel out of focus behind. Soft natural light, 50mm lens, f/2.8. Do not change the mug's shape, color, glaze pattern or proportions.
```

### 6.3. Кадр 2: Флэтлей сверху (Top-down flat lay)
**Референс:** Прикрепить `D0_packshot.png`.
```text
Product photo session. Overhead flat lay, top-down view: exactly this mug (same speckled cream glaze and terracotta base) filled with cappuccino with latte art, on a sage-green linen cloth, surrounded by scattered coffee beans, an open notebook and a small spoon. Even diffused light. Do not change the mug's design.
```

### 6.4. Кадр 3: В руках в уличном кафе (In hands)
**Референс:** Прикрепить `D0_packshot.png`.
```text
Product photo session. Two hands in a knitted beige sweater hold exactly this mug (same speckled cream glaze, terracotta base band, handle shape) at an outdoor cafe table on an autumn morning; blurred street and fallen leaves in the background. 85mm lens, f/1.8, warm tones. Keep the mug design identical.
```

### 6.5. Кадр 4: Рекламный баннер с типографикой (Ad Banner)
**Референс:** Прикрепить `D0_packshot.png`.
```text
Minimalist advertising banner. Exactly this mug on a dark charcoal stone surface, dramatic side light from the left, a soft curl of steam. Large clean sans-serif headline in the upper area that reads exactly "MORNING RITUAL" and a smaller line below it that reads exactly "Handmade ceramics". Generous negative space. Keep the mug design identical.
```

---

## Блок 7: Мульти-референсная композиция

> **Цель демо:** Передать модели **два разных референса** и четко обозначить их роли (Персонаж + Товар).  
> **Референсы:** Прикрепить `C1_sheet.png` (Референс 1) и `D0_packshot.png` (Референс 2).  
> **Куда вставлять:** Google Gemini (Nano Banana Pro) или ChatGPT Images.  
> **Формат:** 16:9.  

```text
Combine the two references. Image 1 is the character (identity reference), image 2 is the product (product reference). The same courier from image 1, in her yellow jacket with grey stripe, sits at a coffee shop window counter on her break and drinks from exactly the mug from image 2 (same speckled cream glaze and terracotta base). Her turquoise backpack is on the floor next to her stool. Morning light, 35mm lens, realistic photography. No logos, no text.
```

---

## Блок 8: Словарь фотографа

> **Цель демо:** Показать разницу между профессиональными терминами оптики и света на одном и том же персонаже.  
> **Референс:** Прикрепить `C1_sheet.png`.  
> **Формат:** 4:3.  

### 8.1. Широкий угол (24mm Wide Angle — окружение в кадре)
```text
Use the attached character sheet as the identity reference: the same courier (same face, curly hair, yellow jacket with grey stripe, turquoise backpack), standing next to her city bicycle on a quiet street. Realistic photography. No logos, no text. Camera: 24mm wide-angle lens, wide shot, the courier small in the frame, the whole street and buildings visible.
```

### 8.2. Портретная оптика и боке (85mm f/1.8 — размытие фона)
```text
Use the attached character sheet as the identity reference: the same courier (same face, curly hair, yellow jacket with grey stripe, turquoise backpack), standing next to her city bicycle on a quiet street. Realistic photography. No logos, no text. Camera: 85mm portrait lens, f/1.8, head-and-shoulders close-up, strongly blurred background bokeh.
```

### 8.3. Нижний ракурс (Low angle hero shot)
```text
Use the attached character sheet as the identity reference: the same courier (same face, curly hair, yellow jacket with grey stripe, turquoise backpack), standing next to her city bicycle on a quiet street. Realistic photography. No logos, no text. Camera: low angle shot from knee height looking up, 35mm lens.
```

### 8.4. Золотой час и контровой свет (Golden Hour Rim Light)
```text
Use the attached character sheet as the identity reference: the same courier (same face, curly hair, yellow jacket with grey stripe, turquoise backpack), standing next to her city bicycle on a quiet street. Realistic photography. No logos, no text. Light: golden hour, low warm sun behind her, rim light on her hair, long shadows. Medium shot, 50mm.
```

---

## Блок 9: Интерактивный хук

> Если на лекции захотите показать, как генерировались портреты для исторического ряда 2014–2026:

### 9.1. GAN 2014 (Ранняя пиксельная эпоха)
```text
A low-resolution 64x64 pixelated blurry face of a person, early GAN 2014 era, extreme pixelation, distorted blurry features, monochrome grey and muted sepia colors, retro CRT monitor macro texture. No text, no letters.
```

### 9.2. StyleGAN 2018 (Артефакт уха и восковая кожа)
```text
Headshot of a smiling young man generated by early StyleGAN in 2018. Slightly plastic skin texture, perfectly centered face, blurred ambiguous background with colorful bokeh artifacts, subtle asymmetry in the left ear structure. No text.
```

### 9.3. Stable Diffusion 2022 (Пластиковый глянец)
```text
A studio portrait of a woman with smooth glossy plastic skin, characteristic of Stable Diffusion 1.5 in 2022, slightly airbrushed look, cinematic lighting, oversaturated digital art style, soft focus background. No text.
```

### 9.4. Midjourney v5 2023 (Кинематографичный кьяроскуро)
```text
Cinematic 35mm portrait of a middle-aged craftsman in a leather apron, dramatic chiaroscuro Rembrandt lighting, rich color grading, sharp detailed stubble and eyes, moody atmospheric background, Midjourney aesthetic. No text.
```

### 9.5. FLUX.1 2024 (Сверхдетализация пор)
```text
Ultra-realistic candid close-up portrait of an elderly fisherman with deep wrinkles, weathered skin with visible pores and sunspots, natural daylight, grey beard, wool beanie, authentic unedited raw photography. No text.
```

### 9.6. Nano Banana Pro 2026 (Живое фото из жизни)
```text
An authentic smartphone photo taken in October 2026: a young woman laughing in a crowded outdoor cafe, holding a matcha latte, natural messy windblown hair, candid imperfect expression, realistic skin imperfections, authentic daylight, subtle lens distortion of a modern phone camera. No text.
```

---

## Памятка по горячим клавишам и параметрам сервисов

| Сервис | Ключевые параметры | Главный трюк |
|---|---|---|
| **ChatGPT** | Естественный диалог | «Change only X, keep the rest». Текст в точных кавычках `""`. |
| **Gemini / Nano Banana** | Прикрепление до 3 референсов | «Image 1 is character, Image 2 is product». Идеально держит надписи. |
| **Leonardo.ai** | Guidance Scale `7–9`, Canvas Inpainting | Маскируйте кистью область замены, не меняйте весь кадр целиком. |
| **Midjourney** | `--ar 16:9`, `--v 6.1`, `--style raw`, `--s 100` | Кнопка **Vary (Region)** для инпейнтинга; `--cref <url>` для персонажа. |
