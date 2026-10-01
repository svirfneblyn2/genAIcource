"""
Урок 03: LLM API с Python — Быстрый старт для начинающих
======================================================
Этот скрипт показывает 3 главных сценария работы с LLM из кода:
1. Базовый запрос (вопрос-ответ в 5 строк)
2. Стриминг ответа (буквы бегут сразу в реальном времени)
3. Структурированный вывод (получение чистого JSON для программы)

Запуск:
    pip install openai python-dotenv
    python quickstart_simple.py
"""

import os
import json
from openai import OpenAI

# 1. Инициализация клиента
# API-ключ автоматически берется из переменной окружения OPENAI_API_KEY
# Либо можно передать явно: client = OpenAI(api_key="sk-...")
client = OpenAI()

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")

print("=" * 60)
print(f"Подключение к модели: {MODEL_NAME}")
print("=" * 60)


# =====================================================================
# Сценарий 1: Самый простой вызов (Блокирующий запрос)
# =====================================================================
print("\n[Сценарий 1] Базовый запрос (Ждем полный ответ):")

response = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "system", "content": "Ты краткий технический консультант."},
        {"role": "user", "content": "В чем главное отличие API от браузерного чата в 2 пунктах?"}
    ],
    temperature=0.2
)

# Печатаем ответ модели
print(response.choices[0].message.content)

# Полезная телеметрия: сколько токенов потрачено
usage = response.usage
print(f"\n-> Потрачено токенов: вход={usage.prompt_tokens}, выход={usage.completion_tokens}, сумма={usage.total_tokens}")


# =====================================================================
# Сценарий 2: Стриминг токенов (Server-Sent Events)
# =====================================================================
print("\n" + "=" * 60)
print("[Сценарий 2] Стриминг ответа (Буквы появляются сразу):")

stream = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {"role": "user", "content": "Объясни, почему токен не равен слову, за 3 секунды."}
    ],
    stream=True  # Включаем потоковую передачу!
)

print("Ответ: ", end="", flush=True)
for chunk in stream:
    # Каждый чанк содержит маленький кусочек текста (дельту)
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print("\n")


# =====================================================================
# Сценарий 3: Структурированный вывод (Гарантированный JSON для программы)
# =====================================================================
print("=" * 60)
print("[Сценарий 3] Структурированный JSON (Контракт для другого микросервиса):")

# Входящее неструктурированное сообщение от пользователя
user_ticket = "Здравствуйте! У меня списались 50 долларов дважды за одну подписку. Пожалуйста, верните деньги срочно!"

response_json = client.chat.completions.create(
    model=MODEL_NAME,
    messages=[
        {
            "role": "system",
            "content": (
                "Ты классификатор обращений службы поддержки. "
                "Определи категорию обращения (billing, technical, general), "
                "степень срочности (low, medium, high) и краткую суть. "
                "Отвечай строго в формате JSON."
            )
        },
        {"role": "user", "content": user_ticket}
    ],
    response_format={"type": "json_object"},  # Модель обязана вернуть валидный JSON!
    temperature=0.0  # Детерминированный вывод для парсинга
)

raw_output = response_json.choices[0].message.content
print("Сырой ответ модели (валидный JSON):")
print(raw_output)

# Наша программа может мгновенно и безопасно распарсить этот JSON:
parsed_data = json.loads(raw_output)
print("\nРаспарсенные поля в коде:")
print(f"Категория: {parsed_data.get('category')}")
print(f"Срочность:  {parsed_data.get('urgency')}")
print(f"Суть:       {parsed_data.get('summary')}")
print("=" * 60)
print("Готово! Все 3 сценария выполнены успешно.")
