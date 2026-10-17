"""Run every query in queries.sql against channels_sample.duckdb and save results/<name>.csv."""
import re
from pathlib import Path

import duckdb

HERE = Path(__file__).resolve().parent
(HERE / "results").mkdir(exist_ok=True)
con = duckdb.connect(str(HERE / "channels_sample.duckdb"), read_only=True)
sql = (HERE / "queries.sql").read_text(encoding="utf-8")
for name, body in re.findall(r"-- name: (\w+)\n(.*?;)", sql, flags=re.S):
    df = con.sql(body).df()
    df.to_csv(HERE / "results" / f"{name}.csv", index=False, encoding="utf-8")
    print(f"\n== {name}\n{df.to_string(index=False)}")
