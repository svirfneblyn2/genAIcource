from common import build_client, get_model

client = build_client()
response = client.responses.create(
    model=get_model(),
    instructions="Answer for a first-year IT student. Be concise and concrete.",
    input="Explain the difference between an API and an SDK in three bullets.",
)

print(response.output_text)
print(f"request_id={response._request_id}")
print(f"usage={response.usage}")
