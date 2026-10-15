# Module 08 demo assets

Synthetic Northstar sales dataset for teaching AI-assisted data analysis.

## Instructor path

Run:

```bash
python reference_analysis.py
```

This produces deterministic local outputs without network access or third-party packages. Use `fallback_outputs/expected_local_outputs` if a live AI surface or API is unavailable. Pre-rendered charts are included in `fallback_outputs/`.

## Teaching issues intentionally injected

- one duplicate `order_id`,
- one missing `region`,
- one non-canonical date separator,
- one domain anomaly where `returns > orders`.

The reference flow removes only the documented duplicate, labels the missing region `UNKNOWN`, normalizes the date separator, and **does not invent a repair** for the impossible returns value.

## Student path

Copy the `student_starter/` folder. Students create a Verified Analysis Pack and must include verification evidence plus one unsupported claim they refused to make.
