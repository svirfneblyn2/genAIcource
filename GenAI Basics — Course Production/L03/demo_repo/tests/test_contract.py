import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pydantic import ValidationError
from contracts import SupportTicket


def main() -> None:
    fixture = json.loads((ROOT / "expected_structured_output.json").read_text(encoding="utf-8"))
    obj = SupportTicket.model_validate(fixture)
    assert obj.category == "bug"
    assert obj.priority == "high"
    assert len(obj.summary) <= 160

    for field, value in [("category", "incident"), ("priority", "urgent")]:
        bad = dict(fixture)
        bad[field] = value
        try:
            SupportTicket.model_validate(bad)
        except ValidationError:
            pass
        else:
            raise AssertionError(f"invalid {field} was accepted")

    bad = dict(fixture)
    bad["summary"] = "x" * 161
    try:
        SupportTicket.model_validate(bad)
    except ValidationError:
        pass
    else:
        raise AssertionError("overlong summary was accepted")

    print("PASS: local contract checks 4/4")


if __name__ == "__main__":
    main()
