from pathlib import Path

from common import BASE_DIR, build_client, get_model
from contracts import SupportTicket

client = build_client()
ticket_text = (BASE_DIR / "sample_ticket.txt").read_text(encoding="utf-8")

response = client.responses.parse(
    model=get_model(),
    instructions=(
        "Classify the support ticket. If intent or severity is ambiguous, "
        "set needs_human_review=true. Do not invent missing facts."
    ),
    input=ticket_text,
    text_format=SupportTicket,
)

ticket = response.output_parsed
if ticket is None:
    raise RuntimeError("No parsed structured output returned")

print(ticket.model_dump_json(indent=2))
print(f"request_id={response._request_id}")
