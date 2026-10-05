# HW #3: First API Call and Prompt Patterns in Code - Report

**Student:** [Full Name / EPAM Email]  
**Model:** `gemini-3.5-flash-lite` (Google GenAI SDK)  
**Date:** [YYYY-MM-DD]  
**Reviewer:** `ihar_rubanovich@epam.com`  
**Selected Track:** [Track A / Track B / Both tracks]  

---

## 1. Input Data

### For Track A (Structured Output)
- **Sanitized Ticket / Email (No PII):**
```text
[Paste sanitized customer email or ticket text]
```

### For Track B (Prompt Patterns on Video Transcript)
- **Video Source:** [YouTube URL and title]
- **Transcript Snippet:** [First 2-3 lines of transcript for context]
- **Defined Task (`my_task`):**
```text
[Task text passed in prompt]
```

---

## 2. Execution Results

### Track A: Structured Output (`triage`)
```json
[Paste content of track_a_structured_output from result.json]
```

### Track B: Model Generation (`my_response`)
```text
[Paste generated model response]
```

---

## 3. Telemetry & Cost Breakdown

| Metric | Value |
| :--- | :--- |
| **Prompt Tokens (input)** | [from track_b_tokens.input or usage_metadata] |
| **Candidates Tokens (output)** | [from track_b_tokens.output] |
| **Thoughts Tokens (thinking)** | [from track_b_tokens.thinking] |
| **Total Billed Output Tokens** | `output + thinking = ` [...] |
| **Calculated Inference Cost (USD)** | `$0.00...` ($0.30/1M input, $2.50/1M output) |

---

## 4. Engineering Takeaways

1. **Structured Output (JSON Contract):** [Did the API strictly respect the Pydantic schema? Any validation errors?]
2. **Data Isolation (XML Tags):** [How did the model handle boundaries specified by `<transcript>` tags?]
3. **Thinking & Latency:** [Was thinking budget justified for this reasoning depth?]
