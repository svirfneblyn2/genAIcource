import json
from pathlib import Path
from pydantic import ValidationError

from contracts import SupportTicket

BASE_DIR = Path(__file__).resolve().parent
fixture = json.loads((BASE_DIR / "expected_structured_output.json").read_text(encoding="utf-8"))
obj = SupportTicket.model_validate(fixture)
print(obj.model_dump_json(indent=2))

bad = dict(fixture)
bad["priority"] = "urgent"
try:
    SupportTicket.model_validate(bad)
except ValidationError:
    print("PASS: invalid enum rejected locally")
else:
    raise SystemExit("FAIL: invalid enum was accepted")
