# Урок 06 • Live Demo Runbook & Prompt Copybook
## Сборник готовых промптов и сценариев для живого показа работы со звуком

**Курс:** GenAI Basics • Модуль 2 (Мультимодальность)  
**Инструктор:** Игорь Рубанович (EPAM Systems • `ihar_rubanovich@epam.com`)  
**Сервисы:** OpenAI Whisper (API & faster-whisper), ElevenLabs (Multilingual v2 & SFX), Cartesia Sonic, Suno v4, Udio 1.5, Silero VAD  
**Код:** Colab `notebooks/L06_Speech_and_Audio_AI_Pipeline.ipynb`

Этот документ предназначен для спикера и студентов: во время занятия или самостоятельной практики вы можете в один клик скопировать выверенные промпты, параметры генерации и фрагменты кода для озвучивания видеоклипов из L05.

---

## Оглавление

1. [Блок 1: Хук-викторина (4 аудиосцены A–D)](#блок-1-хук-викторина-4-аудиосцены-ad)
2. [Блок 2: Распознавание речи Whisper и извлечение пословных таймкодов](#блок-2-распознавание-речи-whisper-и-извлечение-пословных-таймкодов)
3. [Блок 3: Фильтрация тишины через Silero VAD против галлюцинаций](#блок-3-фильтрация-тишины-через-silero-vad-против-галлюцинаций)
4. [Блок 4: Синтез закадрового голоса (ElevenLabs TTS & Cartesia Sonic)](#блок-4-синтез-закадрового-голоса-elevenlabs-tts--cartesia-sonic)
5. [Блок 5: Генерация предметных шумов и фоли (SFX AI)](#блок-5-генерация-предметных-шумов-и-фоли-sfx-ai)
6. [Блок 6: Студийная звуковая матрица (Кейс Creator Tools Giant Stories)](#блок-6-студийная-звуковая-матрица-кейс-creator-tools-giant-stories)
7. [Блок 7: Генерация инструментального саундтрека в Suno v4](#блок-7-генерация-инструментального-саундтрека-в-suno-v4)
8. [Блок 8: Сведение мультитрека и Sidechain Ducking на Python](#блок-8-сведение-мультитрека-и-sidechain-ducking-на-python)
9. [Блок 9: Архитектура голосового агента реального времени (<300 мс)](#блок-9-архитектура-голосового-агента-реального-времени-300-мс)

---

## Блок 1: Хук-викторина (4 аудиосцены A–D)

> **Цель:** Калибровка слухового аппарата студентов на выявление артефактов нейросинтеза.  
> **Формат:** 44.1 / 48 кГц, длительность 5–8 сек.

### Клип [A] • Студийная дикторская начитка (ElevenLabs Multilingual v2)
* **Промпт/Текст:**
```text
In 1911, deep within the Nevada desert... two miners entered a sealed limestone cavern, completely unprepared for the fossilized silhouette waiting in the dark.
```
* **Параметры:** Voice: `George (Warm Narration)`, Stability: `0.38`, Similarity: `0.80`, Style Exaggeration: `0.10`.

### Клип [B] • Фоли-шум велосипеда курьера (ElevenLabs SFX)
* **Промпт:**
```text
Bicycle rubber tires splashing violently through a deep rainwater puddle on wet cobblestone, fine water spray, quiet evening city background hum, cinema foley, 24fps sync
```
* **Параметры:** Duration: `5.0s`, Prompt Influence: `0.85`.

### Клип [C] • Инструментальное джаз-трио (Suno v4)
* **Стиль (Style prompt):**
```text
Acoustic jazz trio, slow 72 BPM swing, upright piano chords, brushed snare drum, acoustic upright bass walking line, warm vintage tape saturation, instrumental
```
* **Настройки:** `Instrumental: ON`, Model: `v4`.

### Клип [D] • Живой диалог колл-центра (Cartesia Sonic Voice Agent)
* **Текст:**
```text
"Hello! Yes, I can certainly see your order from the Scandinavian bakery. The courier is just two blocks away on Elm Street — should be at your lobby in three minutes."
```
* **Параметры:** Model: `sonic-english`, Latency mode: `ultra-low`, Chunk size: `128 tokens`.

---

## Блок 2: Распознавание речи Whisper и извлечение пословных таймкодов

> **Цель:** Показать, как извлечь субтитры с точностью до 20 мс для монтажа видео.

```python
import whisper

# Загрузка турбо-модели
model = whisper.load_model("turbo")

# Транскрибация с пословными тайм-кодами
result = model.transcribe(
    "narration.mp3",
    language="en",
    word_timestamps=True,
    temperature=0.0
)

print(f"Detected language: {result['language']}")
for segment in result["segments"]:
    print(f"\n--- Фрагмент [{segment['start']:.2f}s -> {segment['end']:.2f}s] ---")
    for word_info in segment["words"]:
        print(f"  [{word_info['start']:6.2f}s - {word_info['end']:6.2f}s]: {word_info['word']}")
```

---

## Блок 3: Фильтрация тишины через Silero VAD против галлюцинаций

> **Цель:** Исключить циклические галлюцинации Whisper (*repetition loops*) в пустых паузах.

```python
import torch

# Загрузка сверхбыстрой модели Silero VAD (1 МБ)
model, utils = torch.hub.load(
    repo_or_dir='snakers4/silero-vad',
    model='silero_vad',
    force_reload=False
)
(get_speech_timestamps, save_audio, read_audio, VADIterator, collect_chunks) = utils

# Чтение аудио
wav = read_audio('raw_recording.wav', sampling_rate=16000)

# Извлечение интервалов с чистой речью (отсекаем тишину)
speech_timestamps = get_speech_timestamps(
    wav,
    model,
    sampling_rate=16000,
    threshold=0.5,
    min_speech_duration_ms=250,
    min_silence_duration_ms=300
)

print(f"Обнаружено речевых интервалов: {len(speech_timestamps)}")
for ts in speech_timestamps:
    print(f"Речь от {ts['start']/16000:.2f}с до {ts['end']/16000:.2f}с")
```

---

## Блок 4: Синтез закадрового голоса (ElevenLabs TTS & Cartesia Sonic)

### 4.1. Сценарная реплика для курьера Glovo (L05)
```text
The evening rain cuts across the asphalt, but order number 42 is already en route... twelve minutes to doorstep.
```

### 4.2. Сценарная реплика для коммерческого пэкшота кружки (L05)
```text
Single-origin Ethiopian roast... freshly pulled at ninety-three degrees. Morning clarity, distilled.
```

### 4.3. Вызов API ElevenLabs в Python
```python
import requests

ELEVENLABS_API_KEY = "YOUR_API_KEY"
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel / Cinematic Narration

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
headers = {
    "xi-api-key": ELEVENLABS_API_KEY,
    "Content-Type": "application/json"
}
payload = {
    "text": "The evening rain cuts across the asphalt... but order number 42 is already en route.",
    "model_id": "eleven_multilingual_v2",
    "voice_settings": {
        "stability": 0.40,
        "similarity_boost": 0.80,
        "style": 0.15,
        "use_speaker_boost": True
    }
}

response = requests.post(url, json=payload, headers=headers)
with open("voiceover.mp3", "wb") as f:
    f.write(response.content)
print("Voiceover synthesized successfully.")
```

---

## Блок 5: Генерация предметных шумов и фоли (SFX AI)

### 5.1. Курьер Glovo в дождь (Шот 2 из L05)
```text
Gravel bicycle tires cutting through shallow street rain puddle with realistic water spray, quiet evening city breeze, wet asphalt tire hiss, 24fps cinematic sync
```

### 5.2. Кофейный пэкшот (Кружка на стойке)
```text
Ceramic coffee mug gently placed onto solid oak wooden counter, light ceramic thud, thin steam wisp hiss, quiet cafe background ambience
```

### 5.3. Передача пакета заказчику (Шот 3 из L05)
```text
Brown kraft paper food bag rustling gently as hands pass it forward, quiet domestic doorway acoustics, soft indoor floor step
```

---

## Блок 6: Студийная звуковая матрица (Кейс Creator Tools Giant Stories)

Готовые промпты фоли и музыки из 10-серийного цикла псевдодокументалистики:

| Сцена | Визуальный план | Промпт для ElevenLabs SFX | Промпт для Suno v4 (Music) |
| :--- | :--- | :--- | :--- |
| **01. Sealed Crate** | Опечатанный ящик 1929 года в подвале | `Distant stone vault hum, slow water dripping on concrete, subtle rat scuttle, hollow reverberation` | `Bowed acoustic double bass drone, dark mysterious cello swell, 65 BPM, instrumental, atmospheric noir` |
| **02. Drill Strike** | Буровики натыкаются на окаменелость | `Cicadas buzz in hot desert wind, heavy shovel violently scraping dense fossilized stone, sudden gasping breath` | `Ominous sub-bass pulse every 2 seconds, distant muted brass stab, desert tension, instrumental` |
| **03. Rotary Press** | Ротационные станки печатают газету | `Historic industrial rotary printing press mechanical clatter, fresh wet ink roller hiss, paper sheet flutter` | `Fast driving string quartet tremolo, mechanical clockwork rhythm, 120 BPM, investigative thriller, instrumental` |
| **04. Denial Letter** | Клерк печатает отказ на машинке | `Vintage mechanical typewriter key clacking, carriage return bell ding, banker lamp 60Hz hum, paper rustle` | `Melancholic solo cello phrase decaying into analog tape hiss, sparse minimal piano notes, 70 BPM, instrumental` |

---

## Блок 7: Генерация инструментального саундтрека в Suno v4

### 7.1. Промпт для ролика Glovo Courier (Дождь, вечер, сумерки)
* **Prompt (Style of Music):**
```text
Lo-fi acoustic guitar chillhop, slow 74 BPM unhurried groove, gentle vinyl crackle, warm upright bass, rain ambiance texture, twilight mood, instrumental
```
* **Lyrics Box (Теги структуры):**
```text
[Intro]
Gentle fingerpicked acoustic guitar, rain texture, soft Rhodes chord

[Main Groove]
Muted bass enters, smooth brushed drums, melodic guitar refrain

[Outro]
Guitar notes fade out into soft rain hiss
```

### 7.2. Промпт для E-Commerce пэкшота (Кружка кофе)
* **Prompt (Style of Music):**
```text
Minimalist Scandinavian acoustic piano, warm 80 BPM, clean contemporary jazz feel, upright bass, soft mallet marimba accents, morning coffee commercial, instrumental
```

---

## Блок 8: Сведение мультитрека и Sidechain Ducking на Python

```python
from pydub import AudioSegment

# Загрузка 3 сгенерированных стемов
voice = AudioSegment.from_file("voiceover.mp3")      # Диктор
foley = AudioSegment.from_file("foley_splash.mp3")   # Брызги луж
music = AudioSegment.from_file("music_lofi.mp3")     # Саундтрек

# Выравнивание целевой громкости стемов (LUFS normalization simulation)
voice = voice.apply_gain(+1.0)   # Доводим голос до -14 LUFS
foley = foley.apply_gain(-4.0)   # Шумы окружения на -18 LUFS

# Ручной Sidechain Ducking: приглушаем музыку на -5 дБ на время речи
music_intro = music[:500] - 8.0               # До речи
music_during_speech = music[500:len(voice)+500] - 13.0  # Ducking (-5 дБ глубже)
music_tail = music[len(voice)+500:] - 8.0     # Возврат после речи

ducked_music = music_intro + music_during_speech + music_tail

# Наложение дорожек с миллисекундным таймингом
final_mix = ducked_music.overlay(voice, position=500).overlay(foley, position=1200)

# Экспорт мастер-трека
final_mix.export("final_commercial_soundtrack.mp3", format="mp3", bitrate="320k")
print("Финальный мастер-трек успешно экспортирован: final_commercial_soundtrack.mp3")
```

---

## Блок 9: Архитектура голосового агента реального времени (<300 мс)

```python
# Эскиз сквозного асинхронного цикла речевого агента на WebSockets
import asyncio

async def voice_agent_loop(audio_stream_in, audio_stream_out):
    vad = SileroVAD()
    stt_client = DeepgramLiveClient()
    llm_client = GroqStreamingClient(model="llama-3.3-70b-versatile")
    tts_client = CartesiaSonicStreamingClient()
    
    async for pcm_chunk in audio_stream_in:
        # 1. Проверка активности голоса (15 мс)
        if vad.is_speech(pcm_chunk):
            user_text_token = await stt_client.push(pcm_chunk)
            
            # 2. Потоковая генерация ответа в LLM (50 мс TTFT)
            async for llm_token in llm_client.stream_response(user_text_token):
                
                # 3. Потоковый синтез речи (90 мс TTFT)
                async for audio_chunk in tts_client.stream_speech(llm_token):
                    await audio_stream_out.play(audio_chunk)
                    
        # 4. Обработка перебивания (Barge-in)
        elif vad.is_interruption():
            await tts_client.cancel_active_stream()
            await audio_stream_out.clear_buffer()
```
