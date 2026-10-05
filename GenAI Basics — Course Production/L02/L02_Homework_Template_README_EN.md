# Homework #2: Chat Prompting - Report

**Student:** [First Last / EPAM Email]  
**Model:** [e.g. ChatGPT standard / Gemini Flash / Claude Sonnet]  
**Date:** [YYYY-MM-DD]  
**Reviewer:** `ihar_rubanovich@epam.com`

> Each prompt requires a fresh chat session. Paste model outputs without manual edits.

---

## Experiment 1: Zero-Shot without Schema (Prompt 1, M3)

**Answer 1:**
```text
[model answer]
```

**Answer 2 (after Regenerate):**
```text
[model answer]
```

**Observation:** [Did categories drift? Can a backend parser ingest this output?]

---

## Experiment 2: Zero-Shot with Schema Rules (Prompt 2, M1-M5)

| ID | Model Output (raw) | Category Correct? | Single Line? |
| :---: | :--- | :---: | :---: |
| M1 | | | |
| M2 | | | |
| M3 | | | |
| M4 | | | |
| M5 | | | |

**Observation:** [Output formatting consistency; handling of missing order number for M4.]

---

## Experiment 3: Few-Shot In-Context Learning (Prompt 3, M1-M5)

| ID | Model Output (raw) | Category Correct? | Single Line? |
| :---: | :--- | :---: | :---: |
| M1 | | | |
| M2 | | | |
| M3 | | | |
| M4 | | | |
| M5 | | | |

**Observation:** [Format compliance rate for `CATEGORY | PRIORITY | ORDER_NUMBER`; placeholder used for M4.]

---

## Experiment 4: Chain-of-Thought (Arithmetic Reasoning on M6)

| Run | 4a: Prompt 3 (Direct) | 4b: Prompt 4 (CoT) |
| :---: | :--- | :--- |
| 1 | | [final line of answer] |
| 2 | | |
| 3 | | |
| **P1 out of 3** | _/3 | _/3 |
| **Output length** | [one line / N paragraphs] | [one line / N paragraphs] |

**Full 4b Output Sample:**
```text
[model answer]
```

**Observation:** [Accuracy impact of reasoning instructions vs token length overhead.]

---

## Experiment 5: XML Delimiters and Injection Defense

| Variant | Prompt Type | Message | Model Output (raw) | Classified Target Message |
| :---: | :--- | :---: | :--- | :--- |
| 5a | Prompt 3 (flat) | M7 | | [cutlery complaint vs confirmation message] |
| 5b | Prompt 3 + rule in prose | M7 | | |
| 5c | Prompt 5 (XML) | M7 | | |
| 5d | Prompt 3 (flat) | M8 | | |
| 5d | Prompt 5 (XML) | M8 | | |

**Observation:** [Did flat text fall for prompt injection? Did prose rules prevent override? Did XML tags guarantee boundary isolation?]

---

## Summary Metrics

| Experiment | Configuration | Measured Metric |
| :--- | :--- | :--- |
| 1 | Zero-Shot without schema (M3 x2) | [consistency across runs] |
| 2 | Zero-Shot with schema rules (M1-M5) | Correct: _/5, Single line: _/5 |
| 3 | Few-Shot (M1-M5) | Correct: _/5, Single line: _/5 |
| 4a / 4b | Direct vs CoT (M6 x3) | P1 detection rate: _/3 vs _/3 |
| 5a-5c | Flat vs Flat+Rule vs XML (M7) | [classified target] |
| 5d | Flat vs XML override (M8) | [override resistance] |

---

## Conclusions

1. **Zero-Shot without Schema:** [...]
2. **Few-Shot In-Context Learning:** [...]
3. **Chain-of-Thought:** [...]
4. **XML Tag Boundaries:** [...]
