-- Учебные запросы к channels_sample.duckdb (DuckDB).
-- Таблица channels: одна строка = один канал. Таблица videos: одна строка = одно видео.
-- Запуск: python run_queries.py (результаты попадут в папку results/).

-- name: q1_views_by_channel_size
-- Вопрос 1. Сколько просмотров набирает типичное видео у маленьких и больших каналов?
-- MEDIAN = «типичное» значение: половина видео выше, половина ниже. Среднее портят редкие хиты.
SELECT c.size_bucket                                  AS channel_size,
       COUNT(DISTINCT c.channel_id)                   AS channels,
       COUNT(*)                                       AS videos,
       MEDIAN(v.views)                                AS median_views_per_video,
       ROUND(MEDIAN(v.views / c.subscriber_count), 2) AS median_views_per_subscriber
FROM videos v
JOIN channels c ON c.channel_id = v.channel_id
GROUP BY c.size_bucket
ORDER BY c.size_bucket;

-- name: q2_views_by_duration
-- Вопрос 2. Видео какой длины набирают больше всего просмотров?
-- Берём только видео, у которых известна длительность.
SELECT duration_bucket,
       COUNT(*)                    AS videos,
       COUNT(DISTINCT channel_id)  AS channels,
       MEDIAN(views)               AS median_views
FROM videos
WHERE duration_bucket IS NOT NULL
GROUP BY duration_bucket
ORDER BY duration_bucket;

-- name: q3_upload_frequency_vs_views
-- Вопрос 3. Помогает ли выпускать видео чаще? Сравниваем внутри одного размера канала,
-- иначе сравним «большие против маленьких», а не «часто против редко».
SELECT c.size_bucket                                   AS channel_size,
       CASE WHEN c.uploads_per_month < 4 THEN 'a: реже раза в неделю'
            ELSE 'b: раз в неделю и чаще' END          AS upload_frequency,
       COUNT(DISTINCT c.channel_id)                    AS channels,
       MEDIAN(v.views)                                 AS median_views_per_video
FROM videos v JOIN channels c ON c.channel_id = v.channel_id
WHERE c.uploads_per_month IS NOT NULL
GROUP BY ALL
ORDER BY channel_size, upload_frequency;

-- name: q4_duration_vs_own_channel
-- Вопрос 4 (проверка вопроса 2). Длинные видео лучше — или их просто снимают большие каналы?
-- Сравниваем каждое видео с типичным видео ЕГО ЖЕ канала: 1.0 = как обычно, 1.2 = на 20% больше.
WITH v AS (
    SELECT *, views / MEDIAN(views) OVER (PARTITION BY channel_id) AS vs_own_channel
    FROM videos)
SELECT duration_bucket,
       COUNT(*)                         AS videos,
       ROUND(MEDIAN(vs_own_channel), 2) AS median_vs_own_channel
FROM v WHERE duration_bucket IS NOT NULL
GROUP BY duration_bucket ORDER BY duration_bucket;
