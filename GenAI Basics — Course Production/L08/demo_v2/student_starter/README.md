# Урок 08 • Стартовый набор для домашнего задания / Lesson 08 • Homework starter kit

## RU

Задание: `L08_05_Homework_v2.md`. Сдаёте папку `analysis_pack/` в `genai-homeworks/L08/`.

| Файл | Что это |
|---|---|
| `northstar_2025.xlsx` | Учебные продажи интернет-магазина Northstar за 2025 год. Лист `Sales` — 1261 строка, лист `Reviews` — 357 отзывов на русском |
| `northstar_2025_EN.xlsx` | Тот же файл с отзывами на английском. Числа те же |
| `northstar_sales_2026-01.csv` | Продажи за январь 2026 — «файл следующего месяца» для рецепта. Только продажи, отзывов нет |
| `report_template.md` | Каркас страницы отчёта: вопрос → 3 графика → 3 вывода → 1 «чего данные не доказывают» |
| `checks_template.md` | Проверка за 60 секунд + одно правдоподобное утверждение, которое данные не доказывают |

**Колонки `Sales`:** `order_date` (дата), `channel` (канал: Search, Social, Email, Organic), `category` (категория), `region` (регион), `warehouse` (склад), `orders` (заказы), `revenue` (выручка, $), `ad_spend` (рекламный расход, $), `returns` (возвраты, шт.).
Одна строка — продажи за день в одном сочетании «канал × категория × регион × склад». Email и Organic рекламу не покупают, поэтому `ad_spend` у них равен нулю. Это не пропуск.

**Колонки `Reviews`:** `review_id`, `review_date`, `region`, `category`, `warehouse`, `rating` (1–5), `comment` (текст отзыва).

Данные вымышленные. Их можно загружать в любой чат. В данных есть пара ошибок — найдите их сами.

## EN

Assignment: `L08_05_Homework_EN_v2.md`. Submit an `analysis_pack/` folder to `genai-homeworks/L08/`.

| File | What it is |
|---|---|
| `northstar_2025_EN.xlsx` | Practice sales of the Northstar online shop for 2025. `Sales` sheet — 1261 rows, `Reviews` sheet — 357 reviews in English |
| `northstar_2025.xlsx` | The same file with reviews in Russian. Same numbers |
| `northstar_sales_2026-01.csv` | Sales for January 2026 — “next month’s file” for the recipe. Sales only, no reviews |
| `report_template.md` | Report page skeleton: question → 3 charts → 3 findings → 1 “what the data does not prove” |
| `checks_template.md` | The 60-second check + one plausible claim the data does not prove |

**`Sales` columns:** `order_date`, `channel` (Search, Social, Email, Organic), `category`, `region`, `warehouse`, `orders`, `revenue` ($), `ad_spend` ($), `returns` (count).
One row is one day of sales for one “channel × category × region × warehouse” combination. Email and Organic buy no advertising, so their `ad_spend` is zero. That is not a missing value.

**`Reviews` columns:** `review_id`, `review_date`, `region`, `category`, `warehouse`, `rating` (1–5), `comment` (review text).

The data is fictional. You can upload it to any chat. It contains a couple of errors — find them yourself.
