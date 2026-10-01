import json
from pathlib import Path

spec = json.loads(Path("visual_spec.json").read_text(encoding="utf-8"))
prompt = " | ".join([
    f"Subject: {spec['subject']}",
    f"Environment: {spec['environment']}",
    f"Composition: {spec['composition']}",
    f"Camera: {spec['camera']}",
    f"Lighting: {spec['lighting']}",
    f"Style: {spec['style']}",
    "Constraints: " + "; ".join(spec['constraints']),
    f"Output: {spec['output']}",
])
print(prompt)
