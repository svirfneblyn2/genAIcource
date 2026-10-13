# Урок 07 • Runbook живого демо
## Три демо: бриф, код, Windows. Точные промпты, ожидаемый результат, запасной вариант

**Курс:** GenAI Basics • Урок 07 из 16  
**Преподаватель:** Ihar Rubanovich (EPAM Systems • `ihar_rubanovich@epam.com`)  
**Инструменты (октябрь 2026):** Copilot в Word или бесплатный Copilot Chat (Edge, веб, приложение Windows) • VS Code + расширение GitHub Copilot (тариф Free) • Блокнот + Copilot в Windows.  
**Данные:** только придуманные, из `demo_courier_copilot/`. Никакой настоящей почты, чатов, файлов и клиентов.  
**Итого:** 14 минут внутри слайдов 6, 10–11 и 17. Остальные слайды идут без демо.

> **Связь с колодой (21 слайд):** демо A → слайды 5–6 • демо B → слайды 9–13 • демо C → слайды 16–17.  
> **Главное правило:** смотрим на **diff и тесты**, а не на слово «готово». Copilot отвечает по-разному каждый раз; ваш результат не обязан совпасть с ожидаемым слово в слово, он обязан пройти проверки.

---

## 1. Перед занятием

### За день
- [ ] Аккаунты: демо-аккаунт **GitHub** (тариф Free достаточно); аккаунт **Microsoft** для Copilot Chat (личный или рабочий Microsoft 365). Лицензия Copilot для Word не нужна: есть запасной путь через бесплатный чат.
- [ ] **VS Code** установлен, расширение **GitHub Copilot** (и Copilot Chat) стоит, вы **вошли** под демо-аккаунтом. Откройте панель чата Copilot и задайте любой вопрос: ответ пришёл.
- [ ] **Обучение на данных выключено** для личного GitHub-аккаунта: Settings → Copilot → «Allow GitHub to use my data for AI model training» = **Disabled**. Для рабочих аккаунтов Business и Enterprise данные не используются, но проверьте, на каком аккаунте вы вошли.
- [ ] **Репозиторий склонирован** (см. ниже «Подготовка репозитория для демо B»), `python smoke_check.py` печатает `BASELINE TESTS PASS` (4 теста).
- [ ] На демо-ПК проверьте: клавиша Copilot (или `Win+C`), приложение Copilot, Vision, поиск по файлам. Чего нет, того нет: запасной путь описан в демо C.
- [ ] `meeting_notes.md` и `release_checklist.txt` открываются; Блокнот на экране готов.
- [ ] Python 3 стоит, терминал открывается в папке репозитория.
- [ ] Прочитайте `demo_courier_copilot/surface_preflight.md` (10 минут перед началом).

### За 10 минут до начала (Teams)
- [ ] Демонстрация **всего экрана**, не одного окна. Закройте почту, мессенджеры, уведомления.
- [ ] Шрифт в VS Code и терминале крупный (Ctrl `+`), чтобы читалось в Teams.
- [ ] Вкладки заранее открыты: Edge с Copilot Chat, VS Code с папкой репозитория, Блокнот с `release_checklist.txt`, слайды 6, 11, 17 (запасные результаты).
- [ ] Фоном под рукой `fallback_outputs/` (три файла).

### Подготовка репозитория для демо B
```bash
cp -r demo_courier_copilot/sample_repo ~/courier-app-demo
cd ~/courier-app-demo
mv expected_solution ../expected_solution_L07     # спрятать готовое решение
git init && git add -A && git commit -m "base"    # без коммита не будет git diff
python smoke_check.py                              # FIXTURES OK ... BASELINE TESTS PASS
```
Готовое решение лежит отдельно; оно нужно только чтобы сравнить diff Copilot с настоящим (слайд 11).

---

## 2. Правило 90 секунд

Если кнопки нет, интерфейс другой или Copilot молчит: **не чините на глазах у класса**.
1. Скажите: **«Кнопка переехала, правило нет.»**
2. Не больше **90 секунд** на поиск. Засеките.
3. Покажите готовый результат: слайд (6, 11 или 17) или файл из `fallback_outputs/`.
4. Скажите вслух, что это подготовленный результат, а не ответ ИИ.
5. Идём дальше; разбор после занятия.

Универсальный запасной приём для любого Copilot: **вставьте текст в бесплатный чат**.

---

## 3. Демо A. Бриф из заметок (слайд 6, 3 минуты)

**Цель:** показать приём «дай источник, попроси структуру, потребуй отметить, что придумано».  
**Где:** Copilot в Word, или бесплатный Copilot Chat в Edge с вставленным текстом `meeting_notes.md`.  
**Вход:** `demo_courier_copilot/meeting_notes.md` (встреча «Prime delivery rule», 5 октября 2026, Anna, Pavel, Ola).

**Промпт (вставьте заметки целиком перед ним или прикрепите файл):**
```text
Using only these notes, write a one-page brief: decisions, open questions, owners. At the end list which sentences are yours.
```
*Промпт на английском, как на слайде. Для русскоязычной группы можно: «Используя только эти заметки, напиши бриф на одну страницу: решения, открытые вопросы, ответственные. В конце перечисли, какие предложения написал ты сам.»*

**Ожидаемый результат** (ориентир, `fallback_outputs/brief_expected.md`, слова Copilot будут другие):
> Approved change: Prime subscribers get free delivery from a $75 order inside the city zone. Free delivery from $100 stays for everyone. Deliveries outside the zone do not change. Pavel builds it behind a feature flag in staging, Ola updates the support reply, and the team watches the delivery-cost number for 24 hours after the release. Who owns the flag rollout is still open.

**Что проверить вместе с классом (4 пункта):**
1. **$75 для Prime** и только **в городе**.
2. **$100 для всех остаётся.**
3. **Вне зоны ничего не меняется.**
4. **Владелец флага не назначен** (открытый вопрос остался открытым).
Затем смотрим список «что написал я сам». Такие строки (например, «ожидаемый эффект: больше повторных заказов», как на слайде 6) **нет в заметках**: удалить или проверить. Это проверка 1 из слайда 18.

**Запасной вариант:**
- Нет Word-Copilot: бесплатный Copilot Chat, вставьте заметки.
- Нет доступа вообще: покажите `fallback_outputs/brief_expected.md` и слайд 6. Скажите, что это подготовленный текст, не ИИ.

---

## 4. Демо B. Код в VS Code (слайды 10–11, 8 минут)

**Цель:** увидеть, что именно изменил Copilot, и проверить это тестами.  
**Где:** VS Code + GitHub Copilot Free, папка `~/courier-app-demo`.  
**Вход:** `ISSUE.md` (issue #12), `.github/copilot-instructions.md` (5 правил), `delivery_fee.py`, `test_delivery_fee.py` (4 теста).

### Шаг 1. План (≈2 минуты)
Откройте чат Copilot. Прикрепите `ISSUE.md` и `.github/copilot-instructions.md` (или оставьте открытыми). Промпт 1:
```text
Read ISSUE.md and .github/copilot-instructions.md, propose a plan, do not edit.
```
**Ожидается:** план из нескольких пунктов, файлы не меняются. Примерно как на слайде 10: 1) ветка Prime для города от 75, 2) правило от 100 остаётся, 3) три теста.  
**Проверьте:** упомянуты порог $75, **только город**, правило $100, границы 75 и 74.99, тест не-Prime. Если Copilot начал править файлы, нажмите «отменить» и повторите промпт.

### Шаг 2. Реализация (≈3 минуты)
Промпт 2 (режим агента, если он есть; названия режимов меняются, ищите «Agent»):
```text
Implement it, add boundary tests, run the tests.
```
Нет агента? Это обычный чат: скопируйте код из ответа в `delivery_fee.py` и `test_delivery_fee.py` руками и запустите тесты сами.

### Шаг 3. Проверка (≈3 минуты, главное)
В терминале VS Code:
```bash
git diff
python -m unittest -v
```
**Ожидаемый результат** (настоящий запуск, `deck_v2/artifacts.json`, слайд 11):
```diff
--- a/delivery_fee.py
+++ b/delivery_fee.py
@@ -14,6 +14,8 @@ def delivery_fee(order: Order) -> float:
         raise ValueError("subtotal must be non-negative")
     if order.subtotal >= 100:
         return 0.0
+    if order.zone.upper() == "CITY" and order.is_prime and order.subtotal >= 75:
+        return 0.0
     if order.zone.upper() == "CITY":
         return 7.50
     return 18.00
--- a/test_delivery_fee.py
+++ b/test_delivery_fee.py
@@ -12,6 +12,15 @@ class DeliveryFeeTests(unittest.TestCase):
     def test_free_delivery_from_100(self):
         self.assertEqual(delivery_fee(Order(100, "CITY")), 0.0)
 
+    def test_prime_free_at_75(self):
+        self.assertEqual(delivery_fee(Order(75, "CITY", True)), 0.0)
+
+    def test_prime_below_75_pays(self):
+        self.assertEqual(delivery_fee(Order(74.99, "CITY", True)), 7.50)
+
+    def test_non_prime_at_75_pays(self):
+        self.assertEqual(delivery_fee(Order(75, "CITY", False)), 7.50)
+
     def test_negative_subtotal_rejected(self):
         with self.assertRaises(ValueError):
             delivery_fee(Order(-1, "CITY"))
```
```text
test_city_standard ... ok
test_free_delivery_from_100 ... ok
test_negative_subtotal_rejected ... ok
test_non_prime_at_75_pays ... ok
test_outside_standard ... ok
test_prime_below_75_pays ... ok
test_prime_free_at_75 ... ok

Ran 7 tests
OK
```
*(Имена тестов у Copilot могут отличаться; важно, что тестов не меньше 7 и все `ok`.)*

**Что проверить вместе с классом (это проверки 3 и 4 слайда 18):**
1. **Diff маленький:** 2 строки логики, новых зависимостей нет (правило 2 из инструкций).
2. Условие: **город + Prime + от 75**, стоит **после** правила «от 100 для всех».
3. **Вне зоны 18.00 не тронуто**, ошибка при отрицательной сумме на месте.
4. Тесты на **75, 74.99 и не-Prime**; **7 из 7 зелёные**.
5. Сравните с `../expected_solution_L07/delivery_fee.py`: решение Copilot может отличаться, но поведение то же.

**Запасной вариант:**
- Copilot молчит, лимит исчерпан или нет входа: **слайд 11** уже содержит настоящие diff и вывод тестов. Скопируйте решение: `cp ../expected_solution_L07/*.py .` и запустите `python -m unittest -v`: получите те же 7 ok.
- Нет агента: чат + ручная вставка (см. шаг 2).
- Тесты красные: покажите это классу. Это и есть смысл проверки: «готово» в чате ничего не доказывает. Попросите Copilot исправить, не больше одной попытки; иначе запасной вариант.
- Эталонное описание хорошего решения: `fallback_outputs/review_expected.md` (5 пунктов).

---

## 5. Демо C. Windows и чек-лист (слайд 17, 3 минуты)

**Цель:** показать, что локальный файл становится контекстом, а Copilot видит только то окно, которым вы поделились (слайд 16).  
**Где:** Блокнот с `release_checklist.txt` + Copilot в Windows (клавиша Copilot или `Win+C`).  
**Вход:** `demo_courier_copilot/release_checklist.txt` (6 пунктов).

**Шаги:** откройте файл в Блокноте → нажмите клавишу Copilot → включите **Vision** и выберите окно Блокнота (или вставьте текст файла в чат) → задайте вопрос.

**Промпт:**
```text
Which item catches an outside-zone fee change?
```
**Ожидаемый результат** (`fallback_outputs/checklist_answer.md`):
> Item 6, “Roll back the flag if outside-zone fees change unexpectedly.”

**Проверьте:** ответ **цитирует пункт 6**, а не пересказывает вольно. Спросите класс: почему Copilot ответил именно по этому файлу? Потому что файл **открыт и показан**.

**Запасной вариант:**
- Нет клавиши Copilot: `Win+C` или откройте приложение Copilot.
- Нет Vision (устройство, регион, версия Windows): **вставьте текст файла** в чат.
- Рабочий аккаунт: приложение откроет веб-чат (это нормально, см. слайд 16); вставьте текст туда.
- Ничего не открывается: `fallback_outputs/checklist_answer.md` и слайд 17. «Кнопка переехала, правило нет.»
- Про Copilot+ PC и Recall не рассказываем дольше одной строки: часть функций нужна такого ПК, Recall по умолчанию выключен, у вас его может не быть.

---

## 6. Если что-то пошло не так

| Симптом | Что делать |
|---|---|
| Copilot взял другое число, чем в заметках | Показать проверку 2 слайда 18: числа сверяем с источником. Исправить промптом или вручную. |
| Copilot изменил зону «вне города» | Тест `test_outside_standard` покажет. Это хороший пример, зачем тесты. |
| Агент поменял больше файлов, чем нужно | Проверка 3: «изменение маленькое». Отмените, повторите промпт 2 со словами «change only delivery_fee.py and the tests». |
| Лимит чата Free исчерпан | Переключиться на запасной вариант B (слайд 11), сказать об этом классу. |
| Вход слетел | Не входить заново на глазах: запасные результаты. |
| В ответ попал секрет или чужие данные | Остановиться; напомнить правило 5: ни секретов, ни данных клиентов в запросе. Здесь данные придуманные. |

## 7. Итог демо (30 секунд)
«Три разных окна, один приём: показали нужное, попросили структуру, **проверили по diff, тестам и источнику**.»

*Файлы:* `demo_courier_copilot/` (`sample_repo/`, `meeting_notes.md`, `release_checklist.txt`, `fallback_outputs/`, `surface_preflight.md`), `deck_v2/artifacts.json`. Перепроверить за сутки: список в конце `L07_00_Lecture_Cheatsheet.md`.
