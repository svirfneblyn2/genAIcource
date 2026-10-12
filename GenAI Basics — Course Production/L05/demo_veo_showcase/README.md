# Быстрый чек-лист для спикера: Запуск двух генераций в Google Veo / Kling AI

В этой папке подготовлены все файлы для проведения ключевого шоу-кейса урока:
**«Наивный поток сознания (Trainwreck) vs Инженерная норма (3-Shot I2V Montage)»**.

---

## 🛑 Часть 1: Запуск «Трешняка» (Trainwreck T2V)

1. Откройте **Google Veo** (в Google AI Studio / VideoFX / Vertex AI) или **Kling AI** (режим *Text-to-Video*).
2. Откройте файл `01_TRAINWRECK_PROMPT_T2V.md` и скопируйте промпт:
   ```text
   Our friendly Glovo delivery courier enters a warm cozy Scandinavian cafe, walks up to the wooden counter and picks up a brown paper food delivery bag, puts it securely inside her turquoise backpack, then cuts to her riding a city bicycle through the rainy avenue at dusk with glowing streetlights and wet cobblestones, and then camera zooms in to a digital smartphone map with a glowing navigation route arrow pointing to the delivery address.
   ```
3. Выберите длительность 5–8 секунд, соотношение **16:9** и нажмите **Generate**.
4. Сохраните полученное видео как `trainwreck_naive_t2v.mp4` в эту папку.
5. **Что показать студентам:**
   - 0:00–0:02: руки курьера слипаются с крафтовым пакетом (топологический коллапс).
   - 0:02–0:04: вместо монтажной склейки кафе мутирует и растворяется в мостовую (морфинг-глитч).
   - 0:04–0:06: дождь идет прямо внутри кофейни (утечка контекста / prompt bleed).
   - 0:06–0:08: карта превращается в психоделическую кашу из псевдосимволов.

---

## ✅ Часть 2: Запуск «Инженерной нормы» (3-Shot I2V Production)

В сервисе переключитесь в режим **Image-to-Video (I2V)**. Для каждого шота перетащите готовый файл из этой папки и вставьте промпт из `02_PRODUCTION_PIPELINE_I2V.md`:

### Шот 1: Забор заказа в кафе
* **Картинка:** `shot1_cafe_pickup.png`
* **Промпт:** 
  ```text
  I2V starting from image. Medium tracking shot, eye-level. The smiling female courier in yellow jacket smoothly lifts the brown kraft paper food bag from the oak counter and turns with purpose toward the cafe exit. Warm morning sunlight through tall windows, subtle dust motes floating in sunbeam, steady cinema camera motion, natural human kinetics. No morphing of hands, no distortion of bag.
  ```
* Скачайте готовый файл и назовите его `shot1.mp4`.

### Шот 2: Поездка под дождем
* **Картинка:** `shot2_bike_rain.png`
* **Промпт:**
  ```text
  I2V starting from image. Dynamic low-angle tracking shot moving forward alongside the courier. The courier pedals her bicycle forward through the rain-slicked city avenue at twilight. Bicycle wheels spinning smoothly forward with water spray cutting through shallow puddles. Wet cobblestones and asphalt reflecting golden shop lights and sodium streetlamps. Camera tracks forward parallel to the rider at matching bicycle speed.
  ```
* Скачайте готовый файл и назовите его `shot2.mp4`.

### Шот 3: Зум карты доставки
* **Картинка:** `shot3_map_route.png`
* **Промпт:**
  ```text
  I2V starting from image. 3D isometric digital delivery navigation map in dark mode. Smooth digital camera push-in and subtle tilt. The electric cyan GPS route trajectory line pulses and draws itself smoothly forward along the city street grid toward the orange destination waypoint pin. Clean high-tech UI motion graphics, crisp telemetry indicators, stable vector geometry.
  ```
* Скачайте готовый файл и назовите его `shot3.mp4`.

---

## 🎬 Часть 3: Сборка в один клик

Дважды кликните по файлу `run_montage.bat` (или выполните `python assemble_montage.py`).  
FFmpeg мгновенно создаст `courier_delivery_final.mp4` с плавными кинематографическими переходами!

На занятии вы покажете:
1. `trainwreck_naive_t2v.mp4` — почему «поток сознания» уничтожает бюджет.
2. `courier_delivery_final.mp4` — как 3 контролируемых шота собираются в чистый рекламный ролик без единого артефакта.
