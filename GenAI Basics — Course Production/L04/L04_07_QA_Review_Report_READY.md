Lecture 04 - QA Review Report

Second-pass quality gate report. Review date: 2026-09-08.

# Scope

Lecture text, full instructor script, slide deck, live-demo runbook, workshop/homework, agent runbook, source notes, and demo repo.

# Critic findings and fixes applied


# Final gate verdict

• Source/Freshness: PASS, with day-of-delivery refresh required for exact model names, pricing, and limits.

• Subject Accuracy: PASS.

• Beginner Clarity: PASS.

• Voice and Tone: PASS.

• AI-ishness Removed: PASS.

• Timing Fit: PASS for 90-120 minutes with compression path.

• Practice and Student Artifact: PASS.

• Artifact Completeness: PASS.

• Slide Visual QA: PASS after render inspection.

• Overall: PASS. Status may be set to DONE.

# Known instructor risks

• Live generation can fail or produce weak output. Treat failure as a workflow-control lesson.

• Provider names are volatile. Do not spend time ranking models unless refreshed on delivery day.

• Students may try copyrighted characters or real brands. State safe-asset boundaries before the demo.



| Reviewer | Finding | Fix applied |
| --- | --- | --- |
| Subject expert | Initial outline risked implying all image tools work the same way. | Reframed around durable capabilities: generation, editing, references, masks, output handling, review. |
| Practical engineer | Needed stronger API lifecycle and metadata discussion. | Added request lifecycle, output storage, review status, hashes/metadata, retry/cost handling. |
| Pedagogy reviewer | Students may confuse prompt writing with workflow design. | Added weak vs structured vs controlled workflow demo and Image Generation Workflow Spec. |
| Beginner-student reviewer | Terms like inpainting, outpainting and mask need non-design explanations. | Added plain vocabulary table and mug examples. |
| Voice-of-Tone editor | Removed brochure style and hype; kept spoken instructor language. | Script now uses concise, practical teaching lines. |
| AI-ishness detector | Removed generic phrases about transformation and creativity at scale. | Replaced with concrete mechanics, examples, and failure modes. |
| Timing auditor | Content could overrun if provider comparison becomes a brand debate. | Added instruction: no ranking; compare capabilities only; included 90-min compression path. |
| Practice-value auditor | Homework must create a useful artifact, not reflection. | Added Image Generation Workflow Spec with rubric. |
| Visual auditor | Deck needed real visual examples and diagrams, not generic wallpaper. | Added generated teaching visuals plus workflow, anatomy, mask/edit and governance diagrams. |

