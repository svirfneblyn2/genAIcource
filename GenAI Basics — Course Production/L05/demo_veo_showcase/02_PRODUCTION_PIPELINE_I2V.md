# Демо 2: «Инженерная норма» (The Production 3-Shot I2V Pipeline)

> **Принцип киноинженерии:** Непрерывное 12-15-секундное видео разбивается на **3 независимых шота** (кадра). Для каждого шота используется стабильный ключевой кадр (Keyframe Image) и короткий кинематографический промпт вектора движения (dx/dt). Склейка выполняется детерминированно через FFmpeg за 0.2 секунды.

---

## Шот 1: Забор пакета со стойки кафе (Cafe Pickup)

* **Исходное изображение (Keyframe):** `shot1_cafe_pickup.png`
* **Режим в сервисе:** **Image-to-Video (I2V)** (загрузите картинку как *First Frame / Starting Image*)
* **Сервис:** Google Veo 2/3 / Kling AI / Runway Gen-3 / Seedance
* **Длительность:** 4–5 сек | **Motion Score / Intensity:** `0.45` (умеренная скорость)

### Промпт:
```text
I2V starting from image. Medium tracking shot, eye-level. 
The smiling female courier in yellow jacket smoothly lifts the brown kraft paper food bag from the oak counter and turns with purpose toward the cafe exit. 
Warm morning sunlight through tall windows, subtle dust motes floating in sunbeam, steady cinema camera motion, natural human kinetics. 
No morphing of hands, no distortion of bag.
```

---

## Шот 2: Поездка на велосипеде под дождем (Rain Avenue Ride)

* **Исходное изображение (Keyframe):** `shot2_bike_rain.png`
* **Режим в сервисе:** **Image-to-Video (I2V)** (загрузите картинку как *First Frame / Starting Image*)
* **Сервис:** Google Veo 2/3 / Kling AI (рекомендуется для биомеханики педалей) / Seedance
* **Длительность:** 4–5 сек | **Motion Score / Intensity:** `0.70` (высокая динамика колес и капель)

### Промпт:
```text
I2V starting from image. Dynamic low-angle tracking shot moving forward alongside the courier. 
The courier pedals her bicycle forward through the rain-slicked city avenue at twilight. 
Bicycle wheels spinning smoothly forward with water spray cutting through shallow puddles. 
Wet cobblestones and asphalt reflecting golden shop lights and sodium streetlamps. 
Camera tracks forward parallel to the rider at matching bicycle speed.
```

---

## Шот 3: Инфографика навигации (Map UI Telemetry Zoom)

* **Исходное изображение (Keyframe):** `shot3_map_route.png`
* **Режим в сервисе:** **Image-to-Video (I2V)** (загрузите картинку как *First Frame / Starting Image*)
* **Сервис:** Google Veo 2/3 / Kling AI / Luma Dream Machine
* **Длительность:** 3–4 сек | **Motion Score / Intensity:** `0.40` (контролируемый цифровой зум)

### Промпт:
```text
I2V starting from image. 3D isometric digital delivery navigation map in dark mode. 
Smooth digital camera push-in and subtle tilt. 
The electric cyan GPS route trajectory line pulses and draws itself smoothly forward along the city street grid toward the orange destination waypoint pin. 
Clean high-tech UI motion graphics, crisp telemetry indicators, stable vector geometry.
```

---

## Склейка роликов через FFmpeg (Детерминированный монтаж)

Когда вы сгенерируете и скачаете 3 файла как `shot1.mp4`, `shot2.mp4`, `shot3.mp4` в эту папку, запустите скрипт монтажа:

```bash
python assemble_montage.py
```

### Команда FFmpeg вручную:
```bash
ffmpeg -i shot1.mp4 -i shot2.mp4 -i shot3.mp4 -filter_complex "[0:v][1:v]xfade=transition=wipeleft:duration=0.3:offset=3.7[v1]; [v1][2:v]xfade=transition=fadeblack:duration=0.4:offset=7.4[outv]" -map "[outv]" -c:v libx264 -crf 18 courier_delivery_story.mp4
```

### Результат:
* Ролик получается кинематографичным, без единого артефакта или мутации рук.
* Четкие лица, точные фирменные цвета куртки и рюкзака.
* Идеальная физика педалей и брызг воды.
* Четкая векторная инфографика маршрута.
