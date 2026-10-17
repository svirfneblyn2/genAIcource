"""Build the frozen, anonymised L08 teaching sample from the what-to-shoot database.

Reads the connection string from the DATABASE_URL environment variable (never stored here).
The session is read-only: only SELECT statements are executed. Tables touched:
channels, videos, video_stat_observations, niches, niche_channels. Nothing else.

Output (next to this script):
  channels_sample.csv, videos_sample.csv, channels_sample.duckdb, sample_meta.json

Usage:
  pip install "psycopg[binary]" duckdb pandas
  set DATABASE_URL=...   (PowerShell: $env:DATABASE_URL = "...")
  python make_channels_sample.py
"""
import json
import os
import re
from pathlib import Path

import pandas as pd
import psycopg

OUT = Path(__file__).resolve().parent
MIN_VIDEOS_WITH_STATS = 10   # a channel needs at least this many videos with a view count
VIDEOS_PER_CHANNEL = 25      # cap per channel -> ~45k videos in total
MAX_CHANNELS = 2000
SEED = "l08-teaching-sample-2026-10"  # fixed so the sample is reproducible

# Short Russian labels for the author's niche names (internal names are not exported).
NICHE_LABELS = {
    "Выпечка: пироги, бисквиты, рулеты": "Выпечка: пироги и бисквиты",
    "Кулинария супы": "Супы",
    "Kekse Welt (seed dataset)": "Печенье и десерты (DE)",
    "Колбасы и сосиски: крафт, сосиски без лица, субтитры": "Колбасы и сосиски",
    "Выпечка: дрожжевое тесто, хлеб, булочки": "Хлеб и дрожжевая выпечка",
    "Outdoor Grill & Campfire Cooking (seed dataset)": "Гриль и костёр",
}

COUNTRY = {"United States": "US", "India": "IN", "Brazil": "BR", "Indonesia": "ID",
           "Mexico": "MX", "United Kingdom": "GB", "Spain": "ES", "Russia": "RU",
           "Germany": "DE", "France": "FR", "Italy": "IT", "Canada": "CA", "Poland": "PL",
           "Ukraine": "UA", "Turkey": "TR", "Türkiye": "TR", "Pakistan": "PK",
           "Australia": "AU", "Japan": "JP", "Philippines": "PH", "Austria": "AT"}

LANGUAGE = {"english": "en", "russian": "ru", "german": "de", "spanish": "es", "french": "fr",
            "portuguese": "pt", "arabic": "ar", "hindi": "hi", "indonesian": "id",
            "turkish": "tr", "thai": "th", "italian": "it", "polish": "pl",
            "ukrainian": "uk", "japanese": "ja", "korean": "ko", "vietnamese": "vi",
            "urdu": "ur", "bengali": "bn", "dutch": "nl", "chinese": "zh"}

EMAIL = re.compile(r"[\w.+-]+@[\w-]+(\.[\w-]+)+")
URL = re.compile(r"(https?://|www\.)\S+", re.I)
DOMAIN = re.compile(r"\b[\w-]+\.(com|ru|de|net|org|io|me|ly|gl|tv|info|shop|store|su|ua|by|kz)(/\S*)?\b", re.I)
PHONE_CAND = re.compile(r"\+?\d[\d\s()-]{8,}\d")  # phone-like: 10+ digits, no dots (dates/episode numbers stay)
# 11-char YouTube-video-id-like tokens left in downloader-style titles ("y2mate com ... <id> 360p")
YT_ID = re.compile(r"(?<![\w-])(?=[\w-]*\d)(?=[\w-]*[A-Z])(?=[\w-]*[a-z])(?!\d+-[A-Z])[\w-]{11}(?![\w-])")
MASKS = {"email": 0, "url": 0, "phone": 0, "youtube_id": 0}


def clean(text):
    """Remove emails, URLs, bare domains, video-id-like tokens and phone-like numbers from a title."""
    if not isinstance(text, str):
        return None
    for name, rx in (("email", EMAIL), ("url", URL), ("url", DOMAIN), ("youtube_id", YT_ID)):
        text, n = rx.subn("", text)
        MASKS[name] += n

    def phone(m):
        if sum(ch.isdigit() for ch in m.group()) >= 10:
            MASKS["phone"] += 1
            return ""
        return m.group()
    text = PHONE_CAND.sub(phone, text)
    return re.sub(r"\s{2,}", " ", text).strip(" -|•·")


def norm_country(v):
    if not isinstance(v, str) or not v.strip():
        return None
    v = v.strip()
    return v.upper() if len(v) == 2 else COUNTRY.get(v, v)


def norm_language(v):
    if not isinstance(v, str) or not v.strip():
        return None
    v = v.strip()
    if len(v) <= 3 or v[2:3] in "-_":
        return v[:2].lower()
    return LANGUAGE.get(v.split(" (")[0].lower(), v)


def size_bucket(subs):
    if subs < 10_000:
        return "1: <10k"
    if subs < 100_000:
        return "2: 10k-100k"
    if subs < 1_000_000:
        return "3: 100k-1M"
    return "4: 1M+"


def duration_bucket(sec):
    if sec is None or pd.isna(sec):
        return None
    if sec <= 60:
        return "1: до 1 мин"
    if sec <= 300:
        return "2: 1-5 мин"
    if sec <= 600:
        return "3: 5-10 мин"
    if sec <= 1200:
        return "4: 10-20 мин"
    if sec <= 2400:
        return "5: 20-40 мин"
    return "6: 40+ мин"


def main():
    salt = SEED
    with psycopg.connect(os.environ["DATABASE_URL"]) as conn:
        conn.read_only = True
        cur = conn.cursor()

        cur.execute("""select (select count(*) from channels), (select count(*) from videos),
                              (select count(*) from video_stat_observations),
                              (select count(distinct video_id) from video_stat_observations)""")
        full = dict(zip(["channels", "videos", "video_stat_observations",
                         "videos_with_any_observation"], cur.fetchone()))

        # Vetted food channels: 'selected' in at least one niche, with stats and enough videos.
        channels = pd.read_sql("""
            with stat_videos as (
                select v.channel_id, count(*) as n
                from videos v
                where exists (select 1 from video_stat_observations o where o.video_id = v.id)
                group by v.channel_id),
            niche_pick as (
                select distinct on (nc.channel_id) nc.channel_id, n.name as niche
                from niche_channels nc join niches n on n.id = nc.niche_id
                where nc.state = 'selected'
                order by nc.channel_id, nc.relevance_score desc nulls last, nc.added_at)
            select c.id, c.youtube_channel_id, c.title, c.subscriber_count, c.video_count,
                   c.view_count, c.country, c.language, c.published_at, c.observed_at,
                   np.niche, sv.n as videos_with_stats_in_db
            from channels c
            join niche_pick np on np.channel_id = c.id
            join stat_videos sv on sv.channel_id = c.id
            where c.subscriber_count is not null and c.view_count is not null
              and sv.n >= %(min_v)s
            order by md5(c.youtube_channel_id || %(salt)s)
            limit %(max_c)s""", conn, params={"min_v": MIN_VIDEOS_WITH_STATS,
                                              "salt": salt, "max_c": MAX_CHANNELS})
        ids = list(channels["id"])

        # How many of the channel's videos the collector holds (before the per-channel cap).
        activity = pd.read_sql("""
            select channel_id as id, count(*) as videos_in_db
            from videos where channel_id = any(%(ids)s) group by channel_id""",
                               conn, params={"ids": ids})

        # Up to N videos per channel, pseudo-random (not just the newest), with the latest views.
        # Likes/comments come from the latest observation that has them (many sources give views only).
        videos = pd.read_sql("""
            with obs as (
                select o.* from video_stat_observations o
                join videos v on v.id = o.video_id
                where v.channel_id = any(%(ids)s)),
            latest_views as (
                select distinct on (video_id) video_id, observed_at, views
                from obs order by video_id, observed_at desc),
            latest_likes as (
                select distinct on (video_id) video_id, likes, comments
                from obs where likes is not null order by video_id, observed_at desc),
            latest as (
                select lv.*, ll.likes, ll.comments
                from latest_views lv left join latest_likes ll using (video_id)),
            ranked as (
                select v.channel_id, v.youtube_video_id, v.title, v.published_at, v.duration_seconds,
                       v.video_kind, l.observed_at, l.views, l.likes, l.comments,
                       row_number() over (partition by v.channel_id
                                          order by md5(v.youtube_video_id || %(salt)s)) as rn
                from videos v join latest l on l.video_id = v.id)
            select * from ranked where rn <= %(cap)s""",
                             conn, params={"ids": ids, "salt": salt, "cap": VIDEOS_PER_CHANNEL})

    # ---- anonymise and tidy channels ----
    channels = channels.merge(activity, on="id", how="left")
    channels["channel_id"] = [f"ch_{i:04d}" for i in range(1, len(channels) + 1)]
    id_map = dict(zip(channels["id"], channels["channel_id"]))
    channels["title"] = channels["title"].map(clean)
    channels["country"] = channels["country"].map(norm_country)
    channels["language"] = channels["language"].map(norm_language)
    channels["niche"] = channels["niche"].map(lambda n: NICHE_LABELS.get(n, n))
    channels["size_bucket"] = channels["subscriber_count"].map(size_bucket)
    channels["channel_created"] = pd.to_datetime(channels["published_at"], utc=True).dt.date
    channels["stats_date"] = pd.to_datetime(channels["observed_at"], utc=True).dt.date
    # Lifetime average from YouTube's own counters (video_count / channel age). Publish dates in
    # the DB are too patchy for a recent-window rate (RSS gives only the last 15 uploads).
    months = (pd.to_datetime(channels["observed_at"], utc=True)
              - pd.to_datetime(channels["published_at"], utc=True)).dt.days / 30.44
    channels["uploads_per_month"] = (channels["video_count"] / months.clip(lower=1)).round(1)
    channels = channels[["channel_id", "title", "niche", "country", "language",
                         "subscriber_count", "view_count", "video_count", "size_bucket",
                         "channel_created", "videos_in_db", "uploads_per_month", "stats_date"]]

    # ---- anonymise and tidy videos ----
    videos["channel_id"] = videos["channel_id"].map(id_map)
    videos = videos.sort_values(["channel_id", "published_at"]).reset_index(drop=True)
    videos["video_id"] = [f"v_{i:06d}" for i in range(1, len(videos) + 1)]
    videos["title"] = videos["title"].map(clean)
    pub = pd.to_datetime(videos["published_at"], utc=True)
    obs = pd.to_datetime(videos["observed_at"], utc=True)
    videos["published_date"] = pub.dt.date
    videos["stats_date"] = obs.dt.date
    videos["age_days"] = (obs - pub).dt.days
    videos["duration_bucket"] = videos["duration_seconds"].map(duration_bucket)
    videos["is_short"] = (videos["video_kind"].eq("short")
                          | (videos["video_kind"].isna() & (videos["duration_seconds"] <= 60)))
    for col in ("views", "likes", "comments", "duration_seconds", "age_days"):
        videos[col] = videos[col].astype("Int64")
    videos = videos[["video_id", "channel_id", "title", "published_date", "duration_seconds",
                     "duration_bucket", "is_short", "views", "likes",
                     "comments", "stats_date", "age_days"]]

    channels.to_csv(OUT / "channels_sample.csv", index=False, encoding="utf-8")
    videos.to_csv(OUT / "videos_sample.csv", index=False, encoding="utf-8")

    import duckdb
    db = OUT / "channels_sample.duckdb"
    db.unlink(missing_ok=True)
    con = duckdb.connect(str(db))
    con.execute("create table channels as select * from channels")
    con.execute("create table videos as select * from videos")
    con.close()

    def span(col):
        col = col.dropna()
        return [str(col.min()), str(col.max())]

    meta = {"full_db": {k: int(v) for k, v in full.items()},
            "sample": {"channels": len(channels), "videos": len(videos),
                       "videos_without_publish_date": int(videos["published_date"].isna().sum())},
            "video_published": span(videos["published_date"]),
            "stats_dates": span(videos["stats_date"]),
            "channel_stats_dates": span(channels["stats_date"]),
            "masked_in_titles": MASKS}
    (OUT / "sample_meta.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(meta, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
