# L09 Demo Assets — Claude Ecosystem and Artifacts

Files:
- support_tickets.csv: sanitized sample support-ticket data.
- prompts.md: weak prompt, strong prompt and targeted revision prompt.
- artifact_prototype.html: offline fallback artifact for inspection practice.
- api_tool_loop_mock.py: tiny no-dependency simulation of a tool-use loop.
- artifact_acceptance_matrix.csv: student acceptance-test template.
- .claude/skills/artifact-brief/SKILL.md: minimal example Skill structure.

Smoke tests:
1. Open artifact_prototype.html in a browser.
2. Run `python api_tool_loop_mock.py`.
3. Inspect the HTML against the acceptance matrix.
