# Проверка за 60 секунд / The 60-second check

Скопируйте этот файл в `analysis_pack/checks.md` и заполните. Каждая проверка — одна-две строки.
Copy this file to `analysis_pack/checks.md` and fill it in. One or two lines per check.

---

## 1. Строки до и после / Rows before and after

- Строк в `Sales` в исходном файле / Rows in `Sales` in the source file: ____
- Строк после чистки / Rows after cleaning: ____
- Что убрали или исправили и почему / What was removed or fixed, and why: ____
- Ответ модели совпал с файлом? / Did the model’s answer match the file? да / нет — yes / no

## 2. Одна точка глазами в источнике / One point by eye in the source

- Какая точка графика / Which chart point: ____ (например / e.g.: выручка за декабрь / December revenue)
- Как нашли в исходном файле / How you found it in the source: ____ (например / e.g.: фильтр по месяцу, сумма в строке состояния Excel / month filter, sum in Excel’s status bar)
- Число на графике / On the chart: ____ • Число в файле / In the file: ____ • Совпало? / Match? да / нет — yes / no

## 3. Процент от чего / Percent of what

Для каждого процента в отчёте: от какого месяца, периода или группы он посчитан.
For every percentage in the report: which month, period or group it is calculated from.

| Процент / Percentage | База / Base | Период / Period |
|---|---|---|
| ____ | ____ | ____ |
| ____ | ____ | ____ |

## 4. После каждой переделки — два числа / After every rework — two numbers

- Число 1 до / после / Number 1 before / after: ____ / ____
- Число 2 до / после / Number 2 before / after: ____ / ____
- Если сдвинулось — почему / If it moved — why: ____

## 5. Чего данные не доказывают / What the data does not prove

- Правдоподобное утверждение / A plausible claim: ____ (например / e.g.: «Если урезать бюджет Social, выручка не упадёт» / “If we cut the Social budget, revenue won’t drop”)
- Почему таблица этого не доказывает / Why the table does not prove it: ____
- Как проверить / How to test it: ____ (например / e.g.: тест на части регионов / a test in some regions)

---

## Только для варианта Б / Option B only

- Откуда данные и кто разрешил их использовать / Where the data comes from and who allowed its use: ____

## Бонус (по желанию) / Bonus (optional)

Где в вашей работе лежат данные и какой у системы официальный экспорт? / Where does the data live in your job, and what is the system’s official export?

- Система / System: ____
- Как выгрузить (кнопка, отчёт) / How to export (button, report): ____
- Формат / Format: ____
- Официальный API есть? / Official API? ____
