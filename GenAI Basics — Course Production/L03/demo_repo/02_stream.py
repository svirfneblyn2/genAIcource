from common import build_client, get_model

client = build_client()
stream = client.responses.create(
    model=get_model(),
    input="Explain streaming in five short sentences.",
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
print()
