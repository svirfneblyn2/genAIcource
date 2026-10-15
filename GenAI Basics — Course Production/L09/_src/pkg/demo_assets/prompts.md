# L09 Demo Prompts

## Weak prompt
Make a dashboard for these support tickets.

## Strong prompt
Create a Claude Artifact: a single-page support triage dashboard for the attached CSV. The user is a support lead who has three minutes each morning. Show summary KPIs, stale P1/P2 warnings, a filterable ticket table, owner workload, and a short "what to act on first" section. Do not expose emails or private customer notes. Use no external libraries. Acceptance tests: every P1 ticket older than two days must be visible above the fold; tickets with missing owners must be called out; the page must still be usable if JavaScript is disabled enough to read the core table.

## Targeted revision prompt
The first version is useful but not ready. Move stale P1 tickets above the fold, add a plain-language explanation of the top action, and create a small acceptance-test section at the bottom. Preserve the privacy constraint and avoid external dependencies.
