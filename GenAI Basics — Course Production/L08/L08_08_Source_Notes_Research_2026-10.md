# L08 — AI for Data Analysis: фактчек-заметки (по состоянию на октябрь 2026)

Дата проверки всех источников: **2026-10-13** (если не указано иное).
Метод: только первичные источники (документация вендоров, help center, страницы цен, release notes, arXiv). Сторонние статьи использовались только для поиска и помечены отдельно.
`[UNCERTAIN]` — не удалось подтвердить в первичном источнике.

---

## Главное для слайдов

1. **ChatGPT анализирует данные, запуская Python** в «stateful Jupyter notebook environment»; DataFrame показываются как интерактивные таблицы. Интерактивные графики: только bar, line, pie, scatter. *(help.openai.com, 8437071)*
2. **Лимиты ChatGPT:** CSV/таблицы — около 50 MB на файл (зависит от размера строки); документы — до 512 MB; до 80 файлов за 3 часа; **Free — 3 загрузки в день**. *(help.openai.com, 8555545)*
3. **Python-среда ChatGPT не ходит в интернет**: внешние данные нужно загрузить файлом или подключить через connector (Google Drive, OneDrive, SharePoint). *(help.openai.com, 8437071)*
4. **ChatGPT for Excel и Google Sheets** — боковая панель внутри таблицы. GA для всех планов с 5 мая 2026, включая Free и Go с ограниченным доступом. *(openai.com/index/chatgpt-for-excel; help.openai.com 20001063)*
5. **GPT-6 в ChatGPT (7 октября 2026):** Plus, Pro, Business и Enterprise получают GPT-6 Sol, Free и Go получают GPT-6 Luna. Новая функция Intelligent UI строит в ответе графики и интерактивные элементы. *(openai.com/index/gpt-6-for-everyone)*
6. **Claude:** «Code execution and file creation» есть на **всех** планах, включая Free. Claude создаёт .xlsx, .pptx, .docx и PDF. Лимит — **30 MB на файл**. *(support.claude.com 12111783)*
7. **Claude for Excel** — GA для Pro, Max, Team и Enterprise. Отвечает со ссылками на конкретные ячейки. Не поддерживает Data tables, макросы, VBA и Excel на iPad. *(claude.com/docs/office-agents/excel)*
8. **Claude for Google Workspace** (Docs, Sheets, Slides) — public beta с 6 октября 2026, на всех платных планах. *(claude.com/resources/articles/…)*
9. **Google Sheets:** функция `=AI("prompt", [range])` (также `=Gemini()`) работает только с текстом. За один запуск генерируются **только первые 350 выделенных ячеек**. Всю таблицу функция не видит. *(support.google.com/docs/answer/15877199)*
10. **Gemini API code execution:** код выполняется **не дольше 30 секунд**. Набор библиотек фиксированный, свои установить нельзя. Графики строятся только через matplotlib. *(ai.google.dev)*
11. **Microsoft:** функция **=COPILOT() убрана из Excel 14 сентября 2026**: при пересчёте старые формулы выдают `#NAME?`. Её заменяет Copilot в Excel (бывший «Agent Mode», теперь «Edit with Copilot»), который с 25 августа 2026 умеет выполнять Python. *(support.microsoft.com; learn.microsoft.com release notes)*
12. **OpenAI API:** Code Interpreter работает в контейнерах 1g, 4g, 16g и 64g. Цена — **$0.03, $0.12, $0.48 и $1.92 за 20-минутную сессию** соответственно. Контейнер удаляется после 20 минут простоя. *(developers.openai.com)*
13. **Бенчмарк DABstep (2025):** даже лучший агент решил только **14.55 %** «Hard»-задач по многошаговому анализу данных. *(arXiv 2506.23719)*
14. **DSBench (2024):** лучший агент решил **34.12 %** задач анализа данных. *(arXiv 2409.07703)*
15. **Приватность:** по умолчанию на обучение **не** идут данные бизнес-планов (ChatGPT Business/Enterprise, Claude Team/Enterprise/API, Google Workspace). С потребительскими планами всё зависит от настроек: в ChatGPT нужно выключить «Improve the model for everyone», в Gemini обучение связано с настройкой «Keep Activity».

---

## 1. ChatGPT: анализ данных (бывш. Advanced Data Analysis / Code Interpreter)

| Факт | Подтверждение | Источник |
|---|---|---|
| **Название.** Help Center сейчас называет функцию просто **«Data analysis with ChatGPT»**. Названия «Advanced Data Analysis» и «Code Interpreter» в актуальной статье не используются | ✔ | https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt (2026-10-13; статья обновлена «5 days ago») |
| **Механизм.** ChatGPT «writes and runs Python code in a stateful Jupyter notebook environment». DataFrame выводятся как interactive tables | ✔ | там же |
| **Графики.** Static (PNG) + «Switch to interactive chart». Интерактивными бывают только bar, line, pie, scatter, остальные типы — статичные картинки | ✔ | там же |
| **Типы файлов для анализа:** .xls, .xlsx, .csv, PDF, .json, .xml, .yaml, .txt, .md. Таблицы для загрузки: XLSX, XLS, CSV, TSV | ✔ | 8437071 + https://help.openai.com/en/articles/8555545 (2026-10-13) |
| **Ограничение:** «The Python environment… cannot make external web requests or API calls» | ✔ | 8437071 |
| **Connectors:** можно прикреплять файлы из Google Drive, OneDrive и SharePoint, если connectors доступны аккаунту. С 10 сентября 2026 в ChatGPT Library добавлены Box, Dropbox и SharePoint (Go/Plus/Pro/Business/Edu/Enterprise, web) | ✔ | 8437071; https://help.openai.com/en/articles/6825453-chatgpt-release-notes (запись от 2026-09-10) |
| **Размер файлов:** документы и презентации до 512 MB; текст и документы до 2 млн токенов на файл (для таблиц лимит в токенах не действует); **CSV и таблицы ≈ 50 MB** «depending on the size of each row»; изображения до 20 MB | ✔ | 8555545 |
| **Лимит по числу строк** нигде официально не указан. Ограничение задаётся только размером файла (~50 MB) | [UNCERTAIN] — числа строк нет в первичном источнике | 8555545 |
| **Частота загрузок:** до 80 файлов за 3 часа, Free — 3 загрузки в день; в часы пик лимиты могут снижаться. Хранилище: 25 GB на пользователя, 100 GB на организацию | ✔ | 8555545 |
| **Файлы в Project:** Free — 5, Go/Plus — 25, Edu/Pro/Business/Enterprise — 40 | ✔ | 8555545 |
| **Планы.** Загрузка документов и таблиц доступна на Free и всех платных планах, с разными лимитами | ✔ | 8555545 |
| Анализ данных на Free работает именно через Python (а не только через чтение файла) | [UNCERTAIN] — в статье только «Available file types can vary by model, plan…» | 8437071 |
| **Модели в ChatGPT (Chat).** С 7 октября 2026 Plus, Pro, Business и Enterprise работают на **GPT-6 Sol**, Free и Go — на **GPT-6 Luna**. В режиме Pro reasoning используется **GPT-6 Astra**. Модели вкладок Work и Codex отдельные: GPT-6 Sol/Luna с 22 сентября, GPT-6.1 Sol с 29 сентября 2026 | ✔ | https://openai.com/index/gpt-6-for-everyone/ ; release notes 6825453 (2026-10-13) |
| **Intelligent UI** (с 7 октября 2026): GPT-6 собирает ответ из текста, графиков и интерактивных элементов | ✔ | gpt-6-for-everyone |
| **ChatGPT for Excel:** beta с 5 марта 2026 (GPT-5.4); ChatGPT for Google Sheets — beta с 22 апреля 2026; **GA для всех планов с 5 мая 2026 («powered by GPT-5.5»)** | ✔ | https://openai.com/index/chatgpt-for-excel/ (2026-10-13) |
| **ChatGPT for Excel/Sheets: доступ по планам.** Free, Go, Plus, Pro, Business, Enterprise, Edu, K-12. «Free and Go include limited usage access». Ограничения: макросы и VBA поддерживаются не полностью, ChatGPT memory недоступна. Логи могут храниться в OpenAI 30 дней | ✔ | https://help.openai.com/en/articles/20001063-chatgpt-for-excel-and-google-sheets (2026-10-13) |
| **ChatGPT for Word** (17 сентября 2026): тот же add-in, что для Excel и PowerPoint, на всех планах | ✔ | release notes 6825453 |
| **ChatGPT Work.** Режим Work создаёт и редактирует документы, таблицы и презентации. Для работы внутри открытой книги Excel help center направляет в Codex в desktop-приложении | ✔ (частично) | https://help.openai.com/en/articles/20001278 (найдено через поиск); release notes |
| Дата запуска ChatGPT Work (9 июля 2026) и модель на старте (GPT-5.6) | [UNCERTAIN] — известны только из сторонних статей | — |
| Сохраняется ли «ChatGPT agent» отдельным продуктом в октябре 2026 | [UNCERTAIN] — в просмотренных release notes упоминаются Work, dots и Codex, но не «ChatGPT agent» | — |
| **Data plugin** (10 сентября 2026) в ChatGPT Work и Codex анализирует подключённые бизнес-данные и строит дашборды | ✔ | release notes 6825453 |

## 2. Claude (Anthropic)

| Факт | Подтверждение | Источник |
|---|---|---|
| **В приложении Claude.** Функция называется **«Code execution and file creation»** и доступна на Free, Pro, Max, Team и Enterprise (web, Desktop, Mobile). Термин «analysis tool» в текущей статье **не используется** | ✔ | https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude (2026-10-13) |
| **Создаваемые файлы:** .xlsx (с работающими формулами), .pptx, .docx, PDF, а также PNG-графики и Python-скрипты. На вход принимает CSV, TSV и другие файлы | ✔ | там же |
| **Лимит:** «30MB per file for both uploads and downloads» | ✔ | там же |
| **Сеть.** На Free, Pro и Max network access включён (можно ставить пакеты из одобренных источников). На Team и Enterprise по умолчанию выключен, включает owner. Статья противоречит сама себе в части Team | ✔ | там же |
| **Claude for Excel** — «generally available to Pro, Max, Team, and Enterprise plans». Работает в Excel on the web, Excel for Windows (M365) и Excel for Mac. Не работает на iPad, Android и в Excel 2016/2019 | ✔ | https://claude.com/docs/office-agents/excel (старый URL support.claude.com/…/12650343 перенаправляет туда), 2026-10-13 |
| **Возможности Claude for Excel:** ответы со ссылками на ячейки, правка допущений с сохранением формул, поиск ошибок (#REF!, #DIV/0), сортировка, фильтры, pivot tables, conditional formatting. Не поддерживает **Data tables, Macros/VBA** | ✔ | там же |
| **Предупреждение вендора:** не использовать для «audit-critical calculations without verification» и без человеческой проверки; работать только с доверенными таблицами (риск prompt injection) | ✔ | там же |
| **Claude for Google Workspace** (Docs, Sheets, Slides): **public beta с 6 октября 2026, на всех платных планах.** В Sheets пишет формулы, строит pivot tables и нативные графики, может «pull a range into Python» | ✔ | https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides (2026-10-13) |
| **Claude in Chrome** доступен на всех платных планах. Боковая панель в Chrome по help center всё ещё в beta. GA с 26 августа 2026 — только по сторонним статьям | [UNCERTAIN] статус GA | https://support.claude.com/en/articles/12012173-claude-in-chrome (через поиск) |
| **Модели (API, октябрь 2026):** Claude Fable 5.1 (`claude-fable-5-1`), **Claude Opus 5.5** (`claude-opus-5-5`, рекомендован «for most workloads»), Claude Sonnet 5.5 (`claude-sonnet-5-5`), Claude Haiku 5.5 (`claude-haiku-5-5`). У всех контекст 1M токенов | ✔ | https://platform.claude.com/docs/en/about-claude/models/overview (2026-10-13) |
| **API code execution tool:** контейнер 5 GiB RAM, 5 GiB диска, 1 CPU, **без интернета**. Предустановлены pandas, numpy, scipy, scikit-learn, statsmodels. Контейнер живёт 30 дней. Бесплатно 1 550 часов в месяц на организацию, дальше $0.05 за час на контейнер (минимум 5 минут). Бесплатен вместе с web search/fetch | ✔ | https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool (2026-10-13) |

## 3. Google (Gemini)

| Факт | Подтверждение | Источник |
|---|---|---|
| **=AI() в Google Sheets:** синтаксис `AI("prompt", [optional range])`, допустим и `=Gemini()`. Генерация текста, саммари, категоризация и сентимент, данные из Google Search. Только текстовые ответы. «only the first 350 selected cells with AI functions will be generated». Функция не видит всю таблицу. Вложение в IF не поддерживается. Требуется «eligible Google Workspace or Google AI plan» | ✔ | https://support.google.com/docs/answer/15877199 (2026-10-13) |
| **Gemini в боковой панели Sheets** создаёт таблицы и формулы, делает анализ («Analysis steps»), строит графики, pivot tables и conditional formatting. Работает лучше всего с нативными Sheets: .xlsx нужно сохранить как Google Sheets. **Сгенерированный график не связан с исходными данными** и не обновляется. История теряется после перезагрузки | ✔ | https://support.google.com/docs/answer/14218565 (2026-10-13) |
| Анализ в Sheets работает через Python «под капотом» | [UNCERTAIN] для 2026 — так писали в блоге Workspace Updates в январе 2025, в текущем help center Python не упоминается | https://workspaceupdates.googleblog.com/2025/01/generate-charts-and-insights-with-gemini-google-sheets.html |
| Название «Help me analyze» | [UNCERTAIN] — в первичных источниках встречается «Analyze for insights» (2025), сейчас — «Ask Gemini» | — |
| **Data Science Agent в Colab:** запущен 3 марта 2025. Генерирует рабочие notebook по описанию на естественном языке. Доступен с 18 лет «in select countries and languages». На старте занял 4-е место на DABStep | ✔ | https://developers.googleblog.com/data-science-agent-in-colab-with-gemini/ (2026-10-13) |
| GA Data Science Agent в Colab Enterprise (26 мая 2026) и текущая модель агента | [UNCERTAIN] — только вторичные источники | — |
| **Gemini API code execution:** «maximum runtime… 30 seconds». Принимает файлы (лучше всего CSV и текст), размер ограничен окном контекста. При ошибке до 5 повторов. Графики только через matplotlib. «You can't install your own libraries». Список библиотек: pandas, numpy, scikit-learn, scipy, seaborn, openpyxl, xlrd, tensorflow и др. Пример в документации — `gemini-3.8-flash` | ✔ | https://ai.google.dev/gemini-api/docs/code-execution (2026-10-13) |
| **Модели Gemini API (stable):** gemini-3.8-flash, gemini-3.6-flash, gemini-3.5-flash-lite и др.; **preview:** gemini-3.1-pro-preview, gemini-3-flash-preview | ✔ | https://ai.google.dev/gemini-api/docs/models (2026-10-13) |
| **Приложение Gemini:** в 2026 вышли 3.1 Pro (19 февраля), 3.5 Flash (19 мая), 3.6 Flash (21 июля) | ✔ | https://gemini.google/release-notes/ (2026-10-13) |
| **Загрузка файлов в приложение Gemini:** «most file types», до **100 MB** на файл (видео до 2 GB), **до 10 файлов** в одном промпте. Из таблиц можно строить графики. Отдельных лимитов для CSV/XLSX нет | ✔ | https://support.google.com/gemini/answer/14903178 (2026-10-13) |

## 4. Microsoft (Excel / M365 Copilot)

| Факт | Статус | Источник |
|---|---|---|
| **=COPILOT() убрана:** «Starting September 14, 2026, the COPILOT function is no longer available in Microsoft Excel». Функция была preview (Frontier и Insider). При пересчёте выдаёт `#NAME?`, кэшированные значения сохраняются | **Удалена** (preview → retired) | https://support.microsoft.com/en-us/office/copilot-function-5849821b-755d-4030-a38b-9e20be0cbf62 (2026-10-13) |
| **Agent Mode в Excel** теперь называется **«Edit with Copilot»**: статья поддержки с тем же ID (a2fd6fe4) носит это название. Copilot в Excel правит ячейки, формулы, графики и PivotTables, ищет в вебе, работает с локальными файлами и OneDrive/SharePoint. Режимы edit, chat и plan есть на Windows, Mac и Web | ✔ (переименование видно по URL и заголовку) | https://support.microsoft.com/en-au/office/edit-with-copilot-in-excel-a2fd6fe4-97ac-416b-b89a-22f4d1357c7a (2026-10-13) |
| Дата переименования (9 марта 2026) и точный список лицензий для Edit with Copilot (Personal/Family с AI credits, Premium, M365 Copilot, «Copilot Chat-eligible» business) | [UNCERTAIN] — получено из поисковых выдержек, текст статьи напрямую не подтверждён. Сама статья: «might not be included with your Microsoft 365 subscription» | — |
| **Python при редактировании с Copilot** (25 августа 2026, Windows/Mac/Web): «executing Python code for advanced analysis… with results outputted directly in your workbook» | ✔ GA (в release notes) | https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes (2026-10-13) |
| **Python in Excel:** Enterprise и Business — Windows (Current Channel 2408+), Mac (16.96+), Web. Family и Personal — **preview**. Нет на iPad, iPhone и Android. Free и perpetual-лицензии не поддерживаются. Standard compute входит в подписку, premium compute — платный add-on | ✔ | https://support.microsoft.com/en-us/excel/python/python-in-excel-availability (2026-10-13) |
| **Analyst agent (M365 Copilot):** reasoning-агент, выполняет Python, код можно смотреть. GA с 2025 года для лицензии Microsoft 365 Copilot | ✔ (частично, блог Microsoft 2025 найден через поиск) | https://www.microsoft.com/en-us/microsoft-365/blog/2025/03/25/introducing-researcher-and-analyst-in-microsoft-365-copilot/ |
| Текущая модель Analyst (на старте o3-mini) и лимит запросов в месяц | [UNCERTAIN] | — |

## 5. OpenAI API: Code Interpreter (Responses API)

| Факт | Подтверждение | Источник |
|---|---|---|
| **Режимы контейнера.** Auto: `"container": {"type": "auto", "memory_limit": "4g", "file_ids": [...]}`. Explicit: создать через `POST /v1/containers` (`{"name": ..., "memory_limit": "4g"}`) и передать `"container": "cntr_abc123"` | ✔ | https://developers.openai.com/api/docs/guides/tools-code-interpreter (2026-10-13) |
| **Memory tiers:** `1g` (по умолчанию), `4g`, `16g`, `64g`. Tier фиксируется на всё время жизни контейнера | ✔ | там же |
| **Жизнь контейнера:** истекает через **20 минут бездействия**, восстановить нельзя, состояние Python теряется. Лимит 100 RPM на организацию | ✔ | там же |
| **Цена:** 1 GB — $0.03, 4 GB — $0.12, 16 GB — $0.48, 64 GB — $1.92 «per 20-minute session per container». «Eligible container sessions will be billed by the minute, with a 5-minute minimum» | ✔ | https://developers.openai.com/api/docs/pricing (2026-10-13) |
| **Проверка утверждения из прошлой заметки:** модель `gpt-6-astra` **существует**: это флагман («If you're not sure where to start, use GPT-6 Astra»), используется в примерах кода к Code Interpreter. Пример `{"type":"auto","memory_limit":"4g"}` тоже **верный** | ✔ подтверждено | https://developers.openai.com/api/docs/models ; tools-code-interpreter (2026-10-13) |
| Другие флагманы в прайсе: gpt-6.1-sol, gpt-6-luna, gpt-6-sol, gpt-5.6-sol/terra/luna | ✔ | pricing |
| Список предустановленных Python-библиотек | [UNCERTAIN] — на странице не указан | — |

## 6. Другие инструменты (по одной строке)

- **Julius AI:** AI-workspace для анализа файлов и графиков. Есть Free; Plus — $20/мес (16 GB RAM, хранение файлов 7 дней), Pro — $45/мес, Business — $450/мес. *https://julius.ai/pricing (2026-10-13)*
- **Hex:** Notebook Agent находит данные, планирует анализ и пишет и запускает код в notebook. С марта 2026 Threads тоже пишет Python. *https://learn.hex.tech/docs/explore-data/notebook-view/notebook-agent ; changelog 2026-03-24 (через поиск)*
- **Databricks Genie:** «the Databricks AI experience for users» — вопросы к данным на естественном языке, с управлением доступом через Unity Catalog. *https://docs.databricks.com/aws/en/genie/ (2026-10-13)*. Статус GA на странице не указан.
- **Copilot for Power BI:** report-pane Copilot — GA, standalone Copilot — preview. Нужна платная Fabric capacity F2+ или Premium P1+; одной лицензии Pro или PPU недостаточно. Официально поддерживается только английский. *https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction (ms.date 2026-08-24)*
- **Looker Conversational Analytics:** чат с данными «powered by Gemini», опирается на семантическую модель Looker, есть Advanced Analytics на Python. Часть функций (например, dashboard agents) в preview. *https://docs.cloud.google.com/looker/docs/conversational-analytics-overview (2026-10-13)*
- **Tableau Agent (Pulse):** по странице new-features работает на «GPT 5.2», GA в Tableau Cloud+ и Tableau+ Bundle. [UNCERTAIN] — первичная страница help.tableau.com не проверена. *https://www.tableau.com/products/new-features*

## 7. Типичные ошибки и данные исследований

**Механизм ошибок (для объяснения на слайде):**
- Если LLM считает «в уме» (генерирует цифры как текст), арифметика ненадёжна. В исследовании *Faith and Fate* (Dziri et al., arXiv 2305.18654, май 2023) на примере многозначного умножения показано, что трансформеры решают композиционные задачи через «linearized subgraph matching», а не систематически. Конкретные проценты в abstract не приведены. *https://arxiv.org/abs/2305.18654*
- Если вынести вычисления в код, точность растёт. **PAL** (Gao et al., ноябрь 2022): код вместо chain-of-thought дал на GSM8K +15 п.п. top-1 против PaLM-540B с CoT. *https://arxiv.org/abs/2211.10435*
- Вендоры сами пишут о рисках. OpenAI: «review the generated code, outputs, and assumptions»; ChatGPT может выбрать не тот метод или тип графика; ненадёжно извлекает числа из сканов и картинок; на больших файлах может проанализировать не всё (8437071). Anthropic: не использовать для «audit-critical calculations without verification». Google: «Gemini features may suggest inaccurate… information».
- Неверная агрегация и «тихий» неполный анализ: OpenAI прямо пишет «A file may upload successfully but still be too large… for complete analysis» (8437071).

**Бенчмарки:**

| Бенчмарк | Что измеряет | Главный результат | Дата | Источник |
|---|---|---|---|---|
| **DABstep** (Adyen + Hugging Face) | 450+ реальных многошаговых задач анализа данных | лучший агент (o4-mini) — **14.55 %** на Hard-задачах | июнь 2025 | https://arxiv.org/abs/2506.23719 |
| **DSBench** | 466 задач анализа данных и 74 задачи моделирования (ModelOff/Eloquence, Kaggle) | лучший агент — **34.12 %** задач анализа данных | сентябрь 2024 (ICLR 2025) | https://arxiv.org/abs/2409.07703 |
| **SpreadsheetBench** | 912 реальных вопросов с Excel-форумов | «substantial gap» между SOTA и людьми (числа в abstract не приводятся) | июнь 2024 | https://arxiv.org/abs/2406.14991 |
| **BLADE** | открытые научные анализы данных, 12 датасетов | LLM «often limited to basic analyses»; агенты с доступом к данным лучше, но «still non-optimal» | август 2024 (EMNLP 2024) | https://arxiv.org/abs/2408.09667 |

- Актуальные лидерборды в 2026: на SpreadsheetBench Verified (400 задач) топ-агенты набирают выше 90 %, на DABstep в сентябре 2025 Google DS-STAR набрал 45.2 %. [UNCERTAIN] — данные из агрегаторов и блогов, официальные лидерборды не открывались. Мысль для слайда: «результаты быстро растут, но на сложных многошаговых задачах всё ещё далеко от 100 %».

## 8. Приватность и хранение данных

| Сервис | Обучение на данных по умолчанию | Хранение | Источник |
|---|---|---|---|
| **ChatGPT, потребительские планы** (Free/Go/Plus/Pro) | Управляется настройкой «Improve the model for everyone» (её нужно **выключить**, чтобы новые чаты не шли на обучение). Temporary chats на обучение не используются. Оценка 👍/👎 отправляет на обучение весь разговор | Удалённый чат стирается из систем в течение 30 дней. Temporary chat хранится до 30 дней. Файлы в Library хранятся отдельно от чата: удаление чата их не удаляет | https://help.openai.com/en/articles/7730893 ; https://help.openai.com/en/articles/8983778 (2026-10-13) |
| **ChatGPT Business/Enterprise/Edu** | «By default, OpenAI does not use content from ChatGPT Business, Enterprise, Edu… to train» | Действует retention policy рабочего пространства. Временные (transient) файлы в Enterprise могут удаляться через 48 часов | там же |
| **Claude, потребительские планы** (Free/Pro/Max) | Обучение только если пользователь «choose to allow» (настройка Model Improvement). Incognito chats на обучение не используются | Если обучение разрешено, данные хранятся в обезличенном виде до 5 лет. Удалённые чаты стираются с бэкенда за 30 дней. Срок хранения загруженных файлов не указан [UNCERTAIN] | https://privacy.claude.com/en/articles/10023580 ; https://privacy.claude.com/en/articles/10023548 (2026-10-13) |
| **Claude Team/Enterprise/API** | «By default, we will not use your inputs or outputs from our commercial products» | Claude for Excel: inputs и outputs удаляются за 30 дней, история чата хранится локально в браузере | https://privacy.claude.com/en/articles/7996868 ; claude.com/docs/office-agents/excel |
| **Gemini app (личный аккаунт)** | При включённом Keep Activity Google использует активность для улучшения сервисов, «including training generative AI models». Часть чатов читают люди-ревьюеры | Автоудаление через 18 месяцев (можно выбрать 3 или 36). При выключенном Keep Activity — 72 часа. Чаты, прошедшие ревью, хранятся до 3 лет | https://support.google.com/gemini/answer/13594961 (2026-10-13) |
| Включён ли Keep Activity по умолчанию | [UNCERTAIN] — страница этого не говорит | — |
| **Gemini в Google Workspace (рабочий аккаунт)** | Данные не используются для обучения вне домена без разрешения. «Your chats and uploaded files won't be reviewed by human reviewers» | Регулируется политиками Workspace | https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub (2026-10-13) |

---

### Сводка неподтверждённого
- Точное число строк для ChatGPT (официально указан только размер ≈50 MB).
- Сохраняется ли «ChatGPT agent» отдельным продуктом; дата запуска ChatGPT Work и модель на старте.
- Python «под капотом» в Gemini для Sheets в 2026 году; название «Help me analyze».
- GA Data Science Agent в Colab Enterprise и его текущая модель.
- Дата переименования Agent Mode → Edit with Copilot и точная матрица лицензий; текущая модель и лимиты Analyst.
- Статус GA для Claude in Chrome.
- Свежие цифры лидербордов SpreadsheetBench и DABstep за 2026 год.
- Включён ли Keep Activity в Gemini по умолчанию; срок хранения загруженных файлов в Claude.
- Tableau Agent (не проверено по help.tableau.com).
