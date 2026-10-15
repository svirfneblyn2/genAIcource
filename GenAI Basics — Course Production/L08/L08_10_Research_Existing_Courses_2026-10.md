# L08 — AI for Data Analysis: что уже есть в мире (обзор курсов и практик, октябрь 2026)

Дата проверки: **2026-10-13**. Цель: понять, как другие учат новичков анализировать данные с AI, и что стоит взять в наш 90-минутный урок (GenAI Basics, не-аналитики, живой эфир в MS Teams).
Метод: в приоритете первичные источники (страницы курсов, help center вендоров, блоги вендоров). Сторонние пересказы помечены **[вторичный]**. `[UNCERTAIN]` — не удалось подтвердить в первичном источнике.
Фактчек по самим инструментам (лимиты, планы, даты) лежит в `L08_08_Source_Notes_Research_2026-10.md`. Здесь только то, что нужно для дизайна урока.

---

## 0. Коротко (TL;DR)

1. Почти все курсы строятся по одной цепочке: **загрузить файл → спросить «что тут есть» → почистить → посчитать (формула / pivot) → построить график → улучшить график промптами → коротко пересказать для руководителя → проверить цифры**.
2. Обычный датасет — **вымышленные продажи** (регион × продукт × квартал × выручка, иногда с текстовыми отзывами). Microsoft, Maven и Tableau используют именно его.
3. Главные «aha»-моменты: (а) AI сам пишет формулу по описанию словами; (б) из колонки отзывов за минуту получаются темы и тональность; (в) график переделывается одной фразой («отсортируй, добавь подписи»); (г) AI честно ошибается, и это ловит ручная проверка 2–3 чисел.
4. Самая «показательная» демо-среда в Excel в 2026 году — **Edit with Copilot** (бывший Agent Mode): видно, как он создаёт листы, pivot и графики прямо в книге. Но нужна **лицензия Microsoft 365 Copilot** (бизнес) или Personal/Family с AI-кредитами (≈60 в месяц) либо Premium. **Claude for Excel** и **ChatGPT for Excel** — надстройки, им достаточно подписки на сам чат-сервис.
5. Хорошо работают упражнения «chart makeover» (до/после) и «спроси сам, потом проверь».

---

## 1. Существующие курсы и уроки (2024–2026)

| # | Курс / урок | Провайдер | Длина | Структура | Демо и датасеты | Что делают руками |
|---|---|---|---|---|---|---|
| 1 | **ChatGPT Advanced Data Analysis** (Dr. Jules White) | Vanderbilt / Coursera | ~11 ч, 5 модулей | 1) что это и чем отличается от обычного чата; 2) use cases: документы, таблицы, медиа, zip; 3) какие задачи подходят (рамка **ACHIEVE**); 4) планирование «человек + AI»: extract → transform → analyze → create; 5) ошибки, проверка, большие документы | Свои файлы, небольшие таблицы, zip-архивы | Поиск применений, планирование шагов, контроль ошибок. 142 тыс. слушателей, рейтинг 4.8 |
| 2 | **ChatGPT & Generative AI for Data Analytics** | Maven Analytics / Coursera | ~10 ч, 7 модулей, 48 демо | Intro → ChatGPT for **Excel** (14 демо) → **Google Sheets** → Power BI → SQL → Python → итоги | Сгенерированные примеры данных, анализ одной и нескольких таблиц | Формулы, разбор ошибок, советы по графикам, EDA, conditional formatting, sparklines |
| 3 | **Data Analysis and Visualization with Generative AI in Excel** | Microsoft / Coursera (часть сертификата Microsoft 365 with Generative AI) | ~26 ч, 5 модулей, beginner | 1) подготовка и очистка, формулы; 2) PivotTable, несколько источников, пропуски, прогноз; 3) графики из промптов и дашборды; 4) executive summary и narrative; 5) проект | «Provided dataset» и данные, которые генерирует Copilot | Типы данных, очистка, формулы, pivot, прогноз продаж, графики, сводка. **Требует лицензию M365 Copilot** |
| 4 | **AB-730 AI Business Professional, Lab 03 «Analyze and visualize data with Microsoft Copilot»** | Microsoft Learning (GitHub) | **~20 мин** | 5 задач: тренды → темы отзывов и тональность → график → формула → Analyst agent и 3 пункта для слайда | `quarterly-sales-data.csv`: Region, Product, Quarter, UnitsSold, Revenue, **CustomerFeedback** | Сводка по регионам, сравнение Q1/Q2, темы отзывов, bar chart с подписями и сортировкой, формула «выручка на единицу», 3 буллета для руководства. **Ближе всего к нашему формату** |
| 5 | **Copilot in Excel adoption page** | Microsoft Adoption | 1 страница | Сценарии: Understand / Resolve issues / Model outcomes / Create and organize | Нет скачиваемой книги | Готовые промпты: «Analyze this workbook and give me interesting data insights», «Identify any inconsistencies in the data and recommend how to fix them», «generate a sales forecast» |
| 6 | **Excel with Copilot: AI-Driven Data Analysis** (George Mount) | LinkedIn Learning **[вторичный]** | 1 ч 38 мин, intermediate, ноябрь 2025 | Профилирование данных, sort/filter, формулы, несколько таблиц, функция COPILOT | — | Профилирование набора данных, AI в ячейках |
| 7 | **Copilot for Excel: Achieve More with Your AI Assistant** (Microsoft Press, Alan Murray) | LinkedIn Learning **[вторичный]** | 2 ч 58 мин, август 2025 | Формулы, графики, анализ, разные Copilot | — | — |
| 8 | **Analyzing data with ChatGPT** | **OpenAI Academy** (гайд, апрель 2026) | короткий гайд | Загрузить CSV/Excel, вставить таблицу или подключить источник → спросить по-человечески → искать аномалии → проверить | Свои файлы | Советы: использовать в начале анализа; просить модель **не путать корреляцию с причиной** и называть ограничения данных; **перед отправкой проверить пару ключевых чисел** **[вторичный пересказ, страница отдаёт 403]** |
| 9 | **Introduction to Claude Analysis** | Распространяется через Codecademy, Skillsoft, университетские порталы **[вторичный]**; на anthropic.skilljar.com не найден `[UNCERTAIN]` | короткий курс | Загрузка CSV, исправление типичных проблем, базовая статистика, графики | CSV, выгруженные из Excel/Sheets | Подготовка CSV, чистка, графики |
| 10 | **Gemini in Sheets** (mini-course) | Google Cloud Skills Boost / Google Skills **[вторичный, Class Central]** | мини-курс с бейджем | Планы, трекеры, шаблоны промптов, квиз | — | Скорее «создать таблицу», чем анализировать |
| 11 | **Data Analytics Professional Certificate** (Sean Barnes) | DeepLearning.AI / Coursera | 5 курсов, ~4 мес. | Основы аналитики, Google Sheets, Python, SQL, Tableau, модуль про LLM (как выбирать, как писать промпты, ограничения) | — | Для будущих аналитиков, **слишком глубоко** для нас. Полезна только идея «когда AI уместен» |
| 12 | **YouTube: Leila Gharani (Xelplus), Kenji Explains** | YouTube **[вторичный, пересказы HubSite365]** | 10–20 мин | Gharani (сентябрь 2025): функция `=COPILOT()` — следующие шаги из заметок смены, разбиение текста на колонки, тональность отзывов, нормализация должностей. Kenji: «Game-changer or gimmick?» — честный разбор сильных и слабых сторон Copilot | Короткие «бытовые» таблицы | Формат «я честно протестировал» хорошо удерживает новичков. **Важно:** по нашим заметкам `=COPILOT()` убрана 14.09.2026, демо этих видео устарели |

Платные корпоративные однодневки (Learning Tree «Claude in Excel», 1 день, $488; Udemy «Claude for Data Analysis», ~1 ч 48 мин) **[вторичный]** повторяют ту же цепочку: очистка → дашборд → сценарии.

**Источники к разделу 1:**
- Vanderbilt: https://www.coursera.org/learn/chatgpt-advanced-data-analysis ; анонс: https://vanderbilt.edu/datascience/2023/08/29/new-course-chatgpt-advanced-data-analysis-by-dr-jules-white-associate-professor-of-computer-science
- Maven: https://www.coursera.org/learn/chatgpt-for-data-analytics
- Microsoft на Coursera: https://www.coursera.org/learn/data-analysis-and-visualization-with-copilot-in-excel
- Лаб AB-730: https://microsoftlearning.github.io/AB-730-AI-business-professional/Instructions/Labs/03-analyze-and-visualize-data.html
- Adoption: https://adoption.microsoft.com/copilot-in-excel/
- LinkedIn Learning (через листинг TAMU): https://dsait.tamu.edu/news/2025/11/18/excel-with-copilot-ai-driven-data-analysis/
- OpenAI Academy: https://openai.com/academy/data-analysis ; Help: https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt
- Claude Analysis: https://www.codecademy.com/learn/ext-courses/introduction-to-claude-analysis
- Gemini in Sheets mini-course: https://www.classcentral.com/course/google-cloud-skills-boost-duet-ai-in-google-sheets-274037
- DeepLearning.AI: https://www.deeplearning.ai/courses/data-analytics ; https://www.coursera.org/professional-certificates/data-analytics
- Gharani (пересказ): https://www.hubsite365.com/en-ww/crm-pages/new-excel-copilot-function-too-good-to-be-true.htm ; Kenji (пересказ): https://www.hubsite365.com/en-ww/crm-pages/my-honest-experience-using-copilot-in-excel.htm

---

## 2. Общие паттерны

### 2.1. Темы, которые есть почти везде
| Тема | Как часто | Комментарий |
|---|---|---|
| «Спроси свой файл» (обзор, инсайты, тренды) | везде | Первый промпт почти всегда: «Analyze this … and give me insights» |
| Очистка данных (типы, пропуски, дубликаты, несогласованность) | почти везде | У Microsoft это целый модуль; OpenAI даёт советы по подготовке: заголовки в первой строке, одна строка = одна запись, без нескольких таблиц на листе |
| Формула по описанию словами + объяснение формулы | везде, где есть Excel/Sheets | Самый понятный новичку «aha» |
| PivotTable / группировка | Microsoft, Maven | Часто в виде «summarize revenue by region in a new sheet» |
| График + доводка промптами | везде | Сортировка, подписи, цвета |
| Текстовая колонка → темы и тональность | Microsoft lab, Gharani | Сильный момент для не-аналитиков: «у меня нет чисел, но есть отзывы» |
| Короткий пересказ для руководства (3 буллета / executive summary) | Microsoft (модуль 4, лаб), OpenAI | Связывает анализ с реальной работой |
| Проверка и ограничения (ошибки, корреляция ≠ причина) | Vanderbilt (модуль 5), OpenAI | У хороших курсов это **отдельный шаг**, а не сноска |
| Прогноз / сценарии «что если» | Microsoft, Claude for Excel | Для новичков — опционально |

### 2.2. Типичные демо-датасеты
- **Вымышленные продажи** (регион, продукт, квартал, штуки, выручка) — Microsoft lab, Coursera, Superstore.
- **Продажи + свободный текст отзывов** — Microsoft `quarterly-sales-data.csv` (CustomerFeedback).
- **Данные, сгенерированные самим AI** («create an Excel file of fake sales data for North, South, East, West») — Microsoft support, Maven.
- **Финансовые модели** (DCF, LBO) — Claude for Excel и ChatGPT for Excel. Для нашей аудитории **не подходят**.

### 2.3. Типичные «aha»-моменты
1. Формула по описанию: «посчитай выручку на единицу для каждой строки».
2. Колонка отзывов за минуту превращается в темы и метку тональности для каждой строки.
3. График переделывается одной фразой: «добавь подписи, отсортируй по убыванию».
4. AI работает **внутри** книги: появляются новые листы, pivot и графики (Edit with Copilot, Claude for Excel).
5. Отрицательный aha: AI уверенно ошибается. Например, «pivot» оказывается вставленными значениями без связи с данными, или цифры слегка не сходятся (тест Techfinitive с ChatGPT в Excel) **[вторичный]**: https://www.techfinitive.com/explainers/chatgpt-in-excel-take-the-pain-out-of-spreadsheet-work/
6. «Одинаковая статистика — разные картинки» (**Datasaurus Dozen**, Autodesk Research, CHI 2017): у 13 наборов совпадают среднее, SD и корреляция, а графики — динозавр, звезда, крест. Отсюда правило: **всегда смотри на график, а не только на сводку**. https://www.research.autodesk.com/publications/same-stats-different-graphs/

### 2.4. Типичные упражнения
- «Сделай 3 вывода по таблице и проверь 2 числа вручную» (OpenAI Academy, Vanderbilt).
- «Найди несогласованности и предложи исправления» (Microsoft adoption).
- «Построй график и доведи его в 2–3 итерации» (Microsoft lab, задача 3).
- «Напиши 3 пункта для слайда руководителю» (Microsoft lab, задача 5).
- «Объясни эту формулу или ошибку» (#REF!, #DIV/0) (Claude for Excel docs, Microsoft adoption).

---

## 3. Excel (октябрь 2026): что видно на экране в живом демо

| | **Copilot in Excel / Edit with Copilot** | **Claude for Excel** | **ChatGPT for Excel** |
|---|---|---|---|
| Что это | Встроенный Copilot. «Agent Mode» переименован в **Edit with Copilot** и стал обычным режимом Copilot. Режимы: **Allow editing / Plan / Chat only** | Надстройка из AppSource («Claude for Microsoft 365»), боковая панель | Надстройка-панель (бета с 5 марта 2026, GA с мая 2026). Есть и для Google Sheets |
| Что видно на экране | Создаёт и переименовывает листы, меняет ячейки, форматирование, validation, стили; формулы; **графики, PivotTable, фигуры, связанные с данными**; тренды и выбросы; sort/filter/highlight; веб-поиск со ссылками; импорт из других книг; custom skills. Многошаговые задачи. В редакторе Microsoft сказано, что Edit with Copilot использует модели Anthropic (для части планов можно выбрать модель) | Ответы со **ссылками на конкретные ячейки** (кликабельные); меняет допущения, сохраняя формулы; ищет причину #REF!/#DIV/0; строит модели и заполняет шаблоны; **sort, filter, редактирует pivot, conditional formatting, выпадающие списки**; работает по нескольким вкладкам; **предупреждает перед перезаписью данных** | Создаёт таблицы и наборы данных по описанию, сортирует, правит формулы, считает сценарии, объясняет формулы. В тестах сторонних авторов «pivot» иногда оказывался вставленными значениями **[вторичный]** |
| Python | **Copilot in Excel with Python** («Advanced analysis»): генерирует, объясняет и вставляет Python-код на новый лист. Нужен Python in Excel, файл в OneDrive/SharePoint, AutoSave. По нашим заметкам, с 25.08.2026 Python работает и в Edit with Copilot | Нет Python in Excel. Не поддерживаются Data tables, макросы, VBA | `[UNCERTAIN]` |
| Платформы | Windows, Mac, Web — все режимы; iPad — chat и plan; iPhone и Android — только chat | Excel Web, Windows (M365, build ≥ 16.0.13127.20296), Mac ≥ 16.46. Не работает на iPad/Android и в Excel 2016/2019 | Excel (см. страницу OpenAI) |
| Какой план нужен | Бизнес: **Microsoft 365 Copilot** (~$30/польз./мес. **[вторичный]**). **С 15.04.2026** в крупных организациях (>2000 пользователей, по вторичным данным) Copilot Chat внутри Word/Excel/PowerPoint/OneNote для нелицензированных пользователей **отключён** (метки «Copilot Chat (Basic)» / «M365 Copilot (Premium)»). Дом: Personal/Family с AI-кредитами (~**60 в месяц**, лимит можно исчерпать за одно демо) или **Premium** | Любой платный Claude: **Pro, Max, Team, Enterprise** | По нашим заметкам — все планы, включая Free и Go (с ограничениями) |
| Риски для живого демо | Нужен файл в OneDrive, таблица (Format as Table) и включённый AutoSave; у слушателей без лицензии функции просто нет; на Personal заканчиваются кредиты | Предупреждение Anthropic о **prompt injection** во внешних файлах; используйте только доверенные книги | Нестабильность «псевдо-pivot» |

**Что лучше всего показывать новичкам вживую.** Если у ведущего есть лицензия M365 Copilot — **Edit with Copilot в режиме Plan, затем Allow editing**: зрители видят план, подтверждение и как в книге появляются новые лист, pivot и график. Это ближе всего к их рабочему Excel. Если лицензии нет — **Claude for Excel** (достаточно Pro): кликабельные ссылки на ячейки и предупреждение о перезаписи хорошо показывают тему «доверяй, но проверяй». ChatGPT for Excel подходит как запасной вариант, потому что доступен в Free. Но вендор позиционирует его для финмоделей, а pivot нужно проверять. Учтите: большинство участников урока, скорее всего, **не увидят** Copilot у себя без лицензии. Об этом стоит сказать прямо и дать путь «через чат» (загрузить файл в ChatGPT / Claude / Gemini).

**Официальные галереи промптов и примеры:**
- Copilot Prompt Gallery в Excel — кнопка «View prompts» в панели Copilot, категории Create / Understand / Edit / Ask **[вторичный, DataCamp]**: https://www.datacamp.com/tutorial/excel-copilot-tutorial ; общий каталог: https://copilot.cloud.microsoft/prompts `[UNCERTAIN — не открывали]`
- Adoption: https://adoption.microsoft.com/copilot-in-excel/ (готовые промпты, без скачиваемой книги)
- Microsoft lab CSV `quarterly-sales-data.csv` (ссылка в инструкции лабы AB-730)
- Генерация примера данных средствами самого Copilot: https://support.microsoft.com/en-gb/topic/use-copilot-to-create-sample-excel-data-and-word-documents-9c7cfb11-2c22-431c-9c4d-3931799cbf73
- Примеры промптов Claude for Excel: «Walk me through how the revenue number in cell C42 is calculated», «Find the source of the #REF! error in the summary tab»: https://claude.com/docs/office-agents/excel

**Источники к разделу 3:**
- https://support.microsoft.com/en-us/office/get-started-with-copilot-in-excel-d7110502-0334-4b4f-a175-a73abdfc118a
- https://support.microsoft.com/en-us/office/copilot-frontier/get-started-editing-with-copilot-in-office
- https://support.microsoft.com/office/copilot-in-excel-with-python-364e4ae9-9343-4d56-952a-5f62b0f70db6
- Roadmap (переименование Agent Mode → Edit with Copilot): https://mc.merill.net/message/RM542182
- AI-кредиты: https://support.microsoft.com/office/68530f1a-4459-4d02-9818-8233c1f673b8
- Изменение от 15.04.2026: https://it.purdue.edu/newsroom/articles/260403-microsoft-removes-in-app-copilot-chat-features-for-non-licensesd-users.php ; https://samexpert.com/copilot-chat-enterprise-restriction-april-2026/ **[вторичный]**
- FAQ Copilot in Excel (какие планы подходят): https://support.microsoft.com/en-gb/excel/copilot/frequently-asked-questions-about-copilot-in-excel
- Claude for Excel: https://claude.com/docs/office-agents/excel
- ChatGPT for Excel: https://openai.com/index/chatgpt-for-excel/ (403 при загрузке; даты по вторичным источникам и нашим заметкам L08_08)
- Gemini в Sheets (build & edit, 22.04.2026; только США и английский; Business/Enterprise Standard+, Google AI Pro/Ultra; Gemini сначала предлагает план): https://workspaceupdates.googleblog.com/2026/04/build-and-edit-complex-spreadsheets-with-Gemini-in-Google-Sheets.html

---

## 4. Визуализация с AI: что принято учить

### 4.1. Итеративная доводка графика промптами
Общий паттерн (Microsoft lab, Maven, OpenAI Help):
1. **Попросить вопрос, а не тип графика:** «Как менялась выручка по регионам?» → AI сам предлагает тип.
2. **Доводить по одному изменению за раз:** сортировка → подписи данных → одна акцентная категория → заголовок-вывод («Запад вырос на 18 %», а не «Выручка по регионам»).
3. **Попросить объяснить выбор:** «почему bar, а не pie?»
4. **Зафиксировать результат:** скачать PNG / вставить в книгу / попросить код.

Особенности инструментов:
- **ChatGPT:** интерактивными бывают только bar, line, pie, scatter (остальные — статичные картинки). Можно навести курсор, выбрать цвет (в том числе hex), скачать PNG. https://help.openai.com/en/articles/9213685-extracting-insights-with-chatgpt-data-analysis ; анонс (май 2024): https://openai.com/index/improvements-to-data-analysis-in-chatgpt
- **Gemini в Sheets (2025):** графики вставляются как **статичные картинки** и не связаны с данными. Чтобы поменять график, его нужно сгенерировать заново. https://workspaceupdates.googleblog.com/2025/01/generate-charts-and-insights-with-gemini-google-sheets.html . С апреля 2026 режим build & edit добавляет scorecards и bar charts прямо в лист («add scorecards and bar charts above my sales and inventory data»).
- **Copilot в Excel:** графики и PivotTable **связаны с исходными данными**. Это главное отличие от «картинки из чата».
- **Claude:** artifacts (интерактивный React/HTML-дашборд в боковой панели, с версиями). Официальный пример Anthropic: загрузить CSV и попросить «interactive dashboard» со сводными карточками и вкладками. https://support.claude.com/en/articles/10306677-creating-usage-analytics-with-claude-for-enterprise-audit-logs

### 4.2. «Попроси скрипт, чтобы повторить»
Частая рекомендация продвинутых гайдов: после того как график готов, попросить **Python-скрипт (pandas + matplotlib/plotly)**, который строит тот же график из того же CSV. Зачем: (1) график можно пересобрать на новых данных в следующем месяце; (2) код — это проверяемая запись того, что именно посчитано. Для не-аналитиков подавать как «рецепт» и не требовать запускать его самим. В Excel аналог — Copilot in Excel with Python, который вставляет код в лист.

### 4.3. «Chart makeover» (до/после)
- **Storytelling with Data: Before and After** (Knaflic, Cisneros, Velez; Wiley, сентябрь 2025): 20 разборов «было/стало». Принципы: убрать шум, выделить одну мысль, заголовок-вывод. https://www.storytellingwithdata.com/book-page-update
- Формат упражнения для урока: дать «плохой» график (3D-pie, 12 цветов, легенда вместо подписей) → попросить AI «сделай makeover по принципам SWD и объясни 3 изменения» → сравнить.
- Сообщество: **Makeover Monday** (еженедельный датасет + переделка) — https://makeovermonday.co.uk `[UNCERTAIN — не открывали]`

### 4.4. Гайды по выбору графика
- **FT Visual Vocabulary** (графический отдел Financial Times): 9 категорий по смыслу — deviation, correlation, ranking, distribution, change over time, magnitude, part-to-whole, spatial, flow. Есть постер и веб-версия: https://ft-interactive.github.io/visual-vocabulary/ ; репозиторий https://github.com/ft-interactive/visual-vocabulary (лицензию не нашли — для слайдов **лучше пересказать своими словами и дать ссылку**, а не копировать постер). Пересказ EU: https://data.europa.eu/apps/data-visualisation-guide/visual-vocabulary
- Полезный приём для урока: промпт «Выбери тип графика по FT Visual Vocabulary: какая у меня связь — ranking, change over time или part-to-whole?» учит думать о **вопросе**, а не о кнопке.
- **Datasaurus Dozen** — аргумент «сначала смотри на картинку» (см. 2.3).

### 4.5. Дашборды
- Copilot (Coursera-модуль 3: «interactive dashboards»), Gemini в Sheets (scorecards; в 2026 — Sheets canvas для мини-приложений **[вторичный]**), Claude artifacts, Looker Studio (бесплатный BI от Google; AI-функции в нём мы не проверяли `[UNCERTAIN]`).
- Для 90-минутного урока дашборд — это **финальный wow**, а не отдельная тема: «соедини 3 графика + 3 KPI на одном экране».

---

## 5. Бесплатные датасеты для практики

| Датасет | О чём «история» | Размер | Лицензия | Подходит нам? |
|---|---|---|---|---|
| **Maven Roasters — Coffee Shop Sales** (Maven Data Playground) | 3 кофейни в Нью-Йорке: часы пик, лучшие продукты, разница между точками | ~149 тыс. транзакций (на странице может быть указана другая версия) | **Public Domain** (по странице датасета) | ★★★ Понятно всем, есть время суток и тип продукта. https://mavenanalytics.io/data-playground/coffee-shop-sales |
| **Другие датасеты Maven Data Playground** (пиццерия, рестораны, игрушки и т. д.) | Бизнес-кейсы для челленджей | разные | Бесплатно; лицензию проверять на каждой странице | ★★ https://mavenanalytics.io/data-playground |
| **Sample – Superstore** (Tableau) | Вымышленный ритейл: мебель / офис / техника, убыточные скидки | ~10 тыс. строк | Официальную лицензию не нашли; распространяется с Tableau как учебный. `[UNCERTAIN]` для раздачи | ★★ Классика, но слушатели могли его видеть; «aha»: высокие скидки → убыток |
| **Online Retail / Online Retail II** (UCI, Daqing Chen) | Реальный онлайн-магазин подарков (Великобритания), есть возвраты и «грязь» | 540 тыс. / 1 млн строк | **CC BY 4.0** (с указанием авторства, DOI 10.24432/C5BW33) | ★★ Хорош для темы «очистка» (отрицательные количества, пустые CustomerID), но **большой**. Нужно урезать. https://archive.ics.uci.edu/dataset/352/online+retail |
| **Inside Airbnb** | Аренда жилья по городам: цены, районы, «кто на самом деле владеет» | десятки тысяч строк на город | **CC BY 4.0** (по вторичным источникам; в старом источнике указан public domain — проверить на insideairbnb.com/get-the-data) | ★★ Интересная история, но много колонок и текста. https://insideairbnb.com/get-the-data/ |
| **Our World in Data** | Глобальные темы: энергия, CO₂, здоровье | любые срезы | Данные и графики OWID — **CC BY** (с указанием источника); данные третьих сторон — по их лицензиям | ★★ Хорош для «change over time», но не про работу. https://ourworldindata.org/faq |
| **Microsoft Power BI Financial Sample** | Продажи и прибыль по сегментам и странам | ~700 строк, 1 таблица | Лицензию на странице не нашли `[UNCERTAIN]` | ★ Простой, «скучный». https://learn.microsoft.com/en-us/power-bi/create-reports/sample-financial-download |
| **Microsoft `quarterly-sales-data.csv`** (лаб AB-730) | Продажи + отзывы | маленький | Репозиторий MicrosoftLearning (лицензию проверить в репо) `[UNCERTAIN]` | ★★★ Готовая структура «числа + текст» |
| **Datasaurus Dozen** (R-пакет datasauRus) | Одинаковая статистика — разные картинки | 13×142 точки | Пакет на CRAN (лицензия в пакете) | ★★★ Для одного слайда / мини-демо. https://cran.r-project.org/web/packages/datasauRus/ |
| **Свой синтетический** (наш `northstar_sales_messy.csv` + `_truth.csv`) | Под нашу историю, с заранее заложенными ошибками | маленький | Наш | ★★★ Уже есть в `demo_assets/`. Это лучший вариант для живого эфира: мы знаем «правильный ответ» и можем проверить AI |

**Вывод по датасетам:** для живого эфира оставить свой `northstar_sales_messy.csv`: он воспроизводимый, с известной «правдой» и без лицензионных вопросов. Структуру стоит выровнять с Microsoft lab (добавить текстовую колонку отзывов, если её нет). Для домашки дать на выбор **Coffee Shop Sales (Public Domain)** или **UCI Online Retail (CC BY 4.0, урезанный)**.

---

## 6. Что заимствовать (рекомендации для L08)

1. **Цепочка из 5 задач лабы Microsoft AB-730 как скелет демо** (≈20 мин): тренды → темы и тональность отзывов → график + 2 доводки → формула словами → «3 пункта для руководителя». Она уже проверена на бизнес-пользователях и подходит под любой инструмент.
2. **Колонка свободного текста в датасете.** Для не-аналитиков «из отзывов получились темы и метка тональности на каждую строку» — самый сильный момент. Добавить колонку `customer_comment` в наш датасет.
3. **Отдельный шаг «проверь 2 числа»** (OpenAI Academy, Vanderbilt модуль 5) + слайд **Datasaurus** («сначала посмотри на график»). Сделать это ритуалом после каждого вывода AI, а не сноской.
4. **Chart makeover на одном слайде:** плохой график → промпт «makeover по принципам Storytelling with Data, объясни 3 изменения» → хороший график + заголовок-вывод. Плюс подсказка по FT Visual Vocabulary: «сначала назови тип связи».
5. **Режим Plan перед правками** (есть в Copilot, Gemini в Sheets и в виде подтверждений в Claude for Excel): учить привычке «попроси план → согласуй → разреши редактировать». Плюс в финале попросить **скрипт-рецепт** (Python), чтобы повторить график в следующем месяце.

Дополнительно: честно сказать, что Copilot внутри Excel у большинства без лицензии M365 Copilot **не появится** (изменение от 15.04.2026), и дать равноценный путь «загрузи файл в чат» (ChatGPT / Claude / Gemini).
