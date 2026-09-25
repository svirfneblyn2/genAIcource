import time
import openai

from common import build_client, get_model

client = build_client()
started = time.perf_counter()

try:
    response = client.responses.create(
        model=get_model(),
        input="Give one sentence explaining why bounded retries matter.",
    )
    elapsed_ms = round((time.perf_counter() - started) * 1000)
    print({
        "model": get_model(),
        "request_id": response._request_id,
        "elapsed_ms": elapsed_ms,
        "usage": str(response.usage),
    })
except openai.RateLimitError as exc:
    print(f"rate_limit request_id={exc.request_id}")
except openai.APITimeoutError:
    print("timeout: no usable response before the configured deadline")
except openai.APIConnectionError:
    print("connection: request did not reach a usable API response")
except openai.APIStatusError as exc:
    print(f"api_status={exc.status_code} request_id={exc.request_id}")
