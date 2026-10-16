# L16 Source Notes: Agentic Software Development (research 2026-10-16)

Primary sources checked on 2026-10-16 for the v2 rebuild. Facts are marked VERIFIED, SECONDARY or UNVERIFIED. Replaces the September 2026 Drive package source notes.

## Images used in the deck

| File | What |
|---|---|
| `assets/v2/img/claude_code_permissions_menu.png` | slide 8: own capture of claude.ai/code, 2026-10-16, permissions menu of a new session (Auto ✓ / Accept edits / Plan), menu zoomed 2× in the page before capture (sharp, ≥ 20 px text on the slide). Replaces `claude_code_auto_mode.png` (the one-time “Auto mode is now Claude Code’s default permission mode” notice, low resolution; it had been dismissed and could not be recaptured; git history keeps it). The notice text is quoted in the slide notes. |
| `assets/v2/img/cover_terminal.png` | cover schematic generated with genai-assets |

Slide 9 terminal block: real `pytest -q` output of the homework starter project (`L16_05_Homework*.md`), run locally on 2026-10-16 with Python 3.12 / pytest 9.1.1 (before the fix: `1 failed, 2 passed in 0.06s`; after a sample fix adding a `priority` parameter: `3 passed in 0.02s`; the traceback is shortened on the slide).

The agent anatomy and the work loop are drawn in HTML (bilingual, readable over Teams); the generated `agent_anatomy`/`dev_loop` images were dropped (English-only, small text).

---


Status labels:
- **VERIFIED**: read on the vendor or primary page today.
- **SECONDARY**: only from press or aggregators. Fine for the talk track, but keep it off slides as a hard number.
- **UNVERIFIED**: sources conflict, or no primary source could be reached.

All "checked" dates are 2026-10-16 unless noted.

## What changed since the old package (baseline 2026-09-08)

- **Cursor ownership.** Cursor's parent company (Anysphere) is now owned by SpaceX/xAI (SECONDARY: deal closed about 2026-08-14 for about $60B in stock). Cursor's pricing page now uses new plan names: Free / Plus $8 / Premium $30 / Super $100 / Ultra $200 / Teams $30+. Plus is "Grok models only".
- **Windsurf.** Windsurf is now **Devin Desktop**. Cognition announced it on 2026-06-02, and windsurf.com now 308-redirects to devin.ai.
- **Gemini CLI.** Gemini CLI to Antigravity CLI happened on 2026-06-18 (this was already in the old notes; still true).
- **Copilot naming.** GitHub Docs now call the coding agent "**Copilot cloud agent**". GitHub also introduced a **Max $100** plan and moved Copilot to credit-based ("GitHub AI Credits") billing.
- **Codex.** Codex is now listed on **every** ChatGPT plan, including Free and Go. ChatGPT Pro now has three tiers: $100 / $200 / $500.
- **Claude Code.** The default permission mode is now **auto mode** (with a classifier), from v2.1.283 on.
- **SWE-bench Verified.** OpenAI stopped reporting it (2026-02-23) because of contamination. The official swebench.com Verified board has had no entries since 2026-02.
- **Terminal-Bench.** Now at **4.0**, with semantic versioning, so its scores are not comparable with 2.0 or 3.0.

---

## 1. Coding-agent landscape (one line each)

| Tool | Status, Oct 2026 | Price / free tier | Source |
|---|---|---|---|
| **Claude Code** (Anthropic) | **VERIFIED.** Runs in the terminal CLI, VS Code and JetBrains, the desktop app (macOS, Windows; Linux beta), the web (claude.ai/code) and mobile. Also available via Slack, GitHub Actions, routines (scheduled cloud runs) and Remote Control. The CLI npm `latest` is 2.1.301 (published 2026-10-15); `stable` is 2.1.292. Reads CLAUDE.md, or AGENTS.md as a fallback. | **VERIFIED.** The Free plan does **not** include Claude Code. Pro is $17/mo billed annually or $20 monthly. Max is "from $100" (5x = $100, 20x = $200). Team Standard is $20/$25 per seat, Team Premium $100/$125. Enterprise is $20/seat/mo plus API usage (20-seat minimum). | https://code.claude.com/docs/en/overview ; https://claude.com/pricing ; npm registry |
| **OpenAI Codex** | **VERIFIED.** Surfaces: Codex cloud, the desktop app, CLI (open source, npm `@openai/codex` 0.163.0, 2026-10-15), IDE extension, SDK, iOS. Current models are GPT-6.1 Sol and GPT-6 Luna. GPT-5.5 was retired from ChatGPT-sign-in Codex on 2026-10-14. | **VERIFIED.** Included in Free ($0, quick tasks, desktop app, subject to rollout), Go ($8), Plus ($20: web, CLI, IDE, iOS, cloud review, Slack), Pro ($100/$200/$500), Business ($20 billed annually / $25 monthly per user) and Enterprise/Edu. With an API key it is billed at API rates and has no cloud features. | https://learn.chatgpt.com/docs/pricing (developers.openai.com/codex/pricing redirects here) ; https://github.com/openai/codex |
| **Google Antigravity** (+ Antigravity CLI) | **VERIFIED.** Surfaces: Antigravity App, IDE, IDE extensions, CLI and SDK. Antigravity 2.0 launched at I/O on 2026-05-19 (SECONDARY: TechCrunch). | **VERIFIED.** "Individuals" is $0 with basic weekly rate limits and unlimited Tab completions. Google AI Pro and AI Ultra get higher limits (no prices on the page; SECONDARY: $19.99 / $99.99 / $199.99). Business is from $30/seat/mo, or pay-as-you-go. The exact free quota is UNVERIFIED. | https://antigravity.google/pricing ; https://techcrunch.com/2026/05/19/google-launches-antigravity-2-0-with-an-updated-desktop-app-and-cli-tool/ |
| **Gemini CLI** | **VERIFIED.** Stopped serving Free, AI Pro and Ultra users on **2026-06-18**; those users should move to the Antigravity CLI. It stays open source (Apache-2.0) and works with paid API keys, Gemini Code Assist Standard/Enterprise and GCP. npm `latest` is 0.64.0. The Antigravity CLI keeps skills, hooks, subagents and extensions (extensions are now called "plugins"). | Consumer free tier is gone. Enterprise and API-key users only. | https://github.com/google-gemini/gemini-cli/discussions/27274 (notice dated 2026-05-19) |
| **GitHub Copilot** | **VERIFIED.** Agent mode runs in the IDE and CLI. "**Copilot cloud agent**" (formerly "coding agent") takes an issue or prompt, works in a cloud environment, and returns a draft PR. Third-party agents (Claude, Codex) are in preview. | **VERIFIED.** Free $0 (2,000 completions + 50 chat requests; limited agent mode; **no** cloud agent). Pro $10 ($15 credits). Pro+ $39 ($70 credits). Max $100 ($200 credits). Third-party agents are only on Pro+ and Max. | https://github.com/features/copilot/plans ; https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent |
| **Cursor** (Anysphere, owned by SpaceX/xAI) | **VERIFIED.** The download page shows **v3.24**. Cursor 3 (2026-04-02, SECONDARY) introduced the Agents Window. Recent changelog items: Origin App Marketplace (2026-10-13), remote control of local agents from iOS (2026-10-06), Rollouts and Security Review bots (2026-09-23). | **VERIFIED.** Free $0 (limited agent). Plus $8 (Grok models only). Premium $30 (cloud agents). Super $100. Ultra $200. Teams $30+/user. Third-party models are billed at API list price. | https://cursor.com/pricing ; https://cursor.com/changelog ; https://cursor.com/download |
| **Windsurf, now Devin Desktop** (Cognition) | **VERIFIED.** Rebranded on 2026-06-02 ("the next generation of Windsurf"). windsurf.com redirects to devin.ai. A Devin CLI launched on 2026-04-27. | **VERIFIED.** Free $0 (light quota). Pro $20 (includes Devin Cloud). Max $200. Teams $80/mo + $40 per dev seat. Enterprise is custom. | https://devin.ai/pricing ; https://cognition.com/blog |
| **Devin** (Cognition, cloud agent) | **VERIFIED.** Now one plan family with Devin Desktop (the old Core and Team plans were retired on 2026-04-14). SWE-2 model (2026-09-10). Cognition reports a $1B annualized run rate (2026-09-25). | Same plans as Devin Desktop above. Cloud agents start on Pro ($20). | https://devin.ai/pricing ; https://cognition.com/blog |
| **JetBrains Junie** | **VERIFIED.** Surfaces: Junie CLI, the "Air" plugin in JetBrains IDEs, and GitHub Action / GitLab CI. Works with any model, including bring-your-own-key (BYOK). | **VERIFIED.** "Free to start": Junie Lite free model plus BYOK, no card needed. AI Pro $8.33/mo (10 credits). AI Ultimate $25/mo (35 credits; recommended for regular Junie use). These are annual-billing prices; SECONDARY gives monthly billing as about $10 / $30. | https://junie.jetbrains.com/ |
| **Amazon Kiro** | **VERIFIED.** Surfaces: IDE, CLI (headless, CI/CD), Web (cloud sandboxes, autonomous mode) and mobile. Built around spec-driven development, hooks and steering files. GA in 2026-04 (SECONDARY). | **VERIFIED.** Free $0 (50 credits/mo, Claude Sonnet 4.5 plus open-weight models). Pro $20 (1,000). Pro+ $40 (2,000). Pro Max $100 (5,000). Power $200 (10,000). Extra credits $0.04 each. | https://kiro.dev/pricing/ ; https://kiro.dev/ |

**Teaching note.** Prices cluster at about $20 (entry) and $100–$200 (heavy use). Nearly every vendor now has a free tier: Copilot, Codex, Antigravity, Cursor, Devin, Junie and Kiro. **Claude Code does not.** Use this as a single "price bands" graphic, not a table of exact prices.

---

## 2. Benchmarks (use with caution)

**Bottom line for a beginner deck.** Show *what* each benchmark measures and *why the numbers jump around*. If you show a leaderboard number at all, label it "vendor-reported, Sept 2026".

| Benchmark | What it measures | Current top (as found) | Status | Source |
|---|---|---|---|---|
| **SWE-bench Verified** (500 real GitHub issues in Python) | Fixing a real issue so that hidden tests pass | Official board: top **79.2%** (Claude 4.5 Opus + Sonar Foundation Agent / live-SWE-agent, Dec 2025). The board has had no new entries since 2026-02-26. Aggregators claim about 96% for models from mid-2026. | Official board VERIFIED but stale. The 96% figures are UNVERIFIED. **OpenAI stopped reporting Verified on 2026-02-23** because of contamination (models can reproduce gold patches) and recommends SWE-bench Pro. | https://www.swebench.com/ (data: github.com/SWE-bench/swe-bench.github.io data/leaderboards.json) ; https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ (403 to the fetcher; date and content confirmed via search snippets) |
| **SWE-bench Pro** (Scale AI; harder, multi-language, contamination-resistant) | Same idea, with longer tasks and copyleft/private repos | Scale's public board (standard mini-swe-agent harness): Muse Spark 1.1 **61.5% ±3.1**, gpt-5.4 (xHigh) 59.1, Muse Spark 55.0, claude-opus-4-6 (thinking) 51.9, gemini-3.1-pro 46.1. No date shown. | VERIFIED on the page, but undated and lagging the newest models. Vendor and agent-scaffold scores (for example about 79% for Opus 5 in July 2026) are SECONDARY/UNVERIFIED. | https://labs.scale.com/leaderboard/swe_bench_pro_public |
| **Terminal-Bench 4.0** (Stanford / Laude Institute / Harbor) | Hard end-to-end terminal tasks: build, debug, configure. Scored per model+agent pair. | The vendor table for Claude Opus 5.5 (2026-09-22) gives: Opus 5.5 **66.4%** (xhigh), GPT-6 Astra 57.9%, Fable 5.1 55.8%, Opus 5 52.3%, GPT-5.6 Sol 37.3%. The official tbench.ai board is JS-rendered, so rows were not readable. | Vendor-reported and VERIFIED on the Anthropic page. The independent board is UNVERIFIED. 4.0 changes: 8-hour timeout, 8 tasks removed, 19 fixed; not comparable with 2.x/3.x. | https://www.anthropic.com/news/claude-opus-5-5 ; https://www.tbench.ai/news/terminal-bench-4-0 |

Other points for the lecture:
- **Same model, different harness.** Scores change by about 10–15 points depending on the agent harness (SECONDARY). Every Terminal-Bench entry is a model plus an agent.
- **Contamination.** This is why the field moved from Verified to Pro, and why Terminal-Bench now uses semantic versioning.
- **The METR productivity point (section 4).** The best rebuttal to "the benchmark says 96%, so it's done".

---

## 3. Core concepts with official doc links (all VERIFIED; URLs from code.claude.com/docs/llms.txt)

| Concept | Beginner definition | Official doc |
|---|---|---|
| **Plan mode** | The agent reads and plans but cannot edit until you approve the plan. Shift+Tab, or `claude --permission-mode plan`. | https://code.claude.com/docs/en/permission-modes (plan section) ; https://code.claude.com/docs/en/best-practices ("Explore first, then plan, then code") |
| **Permission / approval modes** | See the list below the table. | https://code.claude.com/docs/en/permission-modes ; https://code.claude.com/docs/en/permissions |
| **Sandboxing** | OS-level limits on which files and network hosts commands can reach. Anthropic measured **84% fewer** permission prompts internally (2025-10-20). | https://code.claude.com/docs/en/sandboxing ; https://code.claude.com/docs/en/sandbox-environments ; https://www.anthropic.com/engineering/claude-code-sandboxing |
| **Project instructions** | **CLAUDE.md**: read at the start of every session; keep it short; `/init` generates one. Claude Code reads **AGENTS.md** if there is no CLAUDE.md. **AGENTS.md** is the open format stewarded by the Agentic AI Foundation (Linux Foundation) and is "used by over 60k open-source projects". It is read by Codex, Copilot cloud agent, Cursor, Devin/Windsurf, Junie, Gemini CLI, VS Code and others. | https://code.claude.com/docs/en/memory ; https://agents.md/ |
| **Skills** | A `SKILL.md` folder holding a reusable workflow or knowledge. Loaded on demand or invoked as `/name`. Also present in the Antigravity CLI. | https://code.claude.com/docs/en/skills |
| **Subagents** | Helper agents with their own context and tool list, used for research or review ("fresh eyes"). | https://code.claude.com/docs/en/sub-agents |
| **Worktrees** | Separate git checkouts so parallel agents don't overwrite each other (`--worktree`). Cursor 3 also uses worktrees in its Agents Window. | https://code.claude.com/docs/en/worktrees |
| **MCP** | An open standard for connecting agents to tools and data: Jira, Figma, databases, GitHub. | https://code.claude.com/docs/en/mcp ; https://code.claude.com/docs/en/mcp-quickstart ; https://modelcontextprotocol.io |
| **Hooks** | Scripts that run **every time** at fixed points, such as formatting after an edit or blocking writes to a folder. Hooks are deterministic; CLAUDE.md is only advisory. | https://code.claude.com/docs/en/hooks-guide |
| **Checkpoints / rewind** | Esc Esc or `/rewind` undoes Claude's file edits. This is **not** a replacement for git: changes made through bash are not tracked. | https://code.claude.com/docs/en/checkpointing |

Permission modes, in Claude Code's names:
- **Manual** (`default`): only reads run without asking.
- **acceptEdits**: file edits plus common filesystem commands (`mkdir`, `touch`, `rm`, `rmdir`, `mv`, `cp`, `sed`) inside the working directory run without asking; other commands still prompt (rechecked 2026-10-16 on https://code.claude.com/docs/en/permission-modes).
- **plan**: reads files and runs shell commands to explore (reviewed by the auto classifier, or limited to the read-only set when auto is unavailable), writes a plan, no edits until you approve.
- **auto**: a classifier model reviews actions instead of you. This is the default from v2.1.283.
- **dontAsk**: only pre-approved tools run; everything else is denied. For CI.
- **bypassPermissions**: no checks. Only for isolated containers or VMs.

Deny rules apply in every mode. Codex has the same idea in its own terms:
- Sandbox: `read-only` / `workspace-write` / `danger-full-access`.
- Approval: `on-request` / `never`.
- Optional `auto_review` reviewer agent.
- Codex source: https://learn.chatgpt.com/docs/sandboxing

Auto mode numbers (Anthropic, 2026-03-25):
- Users approve **93%** of permission prompts, which shows approval fatigue.
- The classifier still misses about **17%** of real "overeager" actions, so it does not replace review.
- Source: https://www.anthropic.com/engineering/claude-code-auto-mode

Equivalent docs in other tools:
- GitHub Copilot cloud agent and its safeguards: https://docs.github.com/en/copilot/concepts/agents/coding-agent/risks-and-mitigations
- Antigravity / Gemini: GEMINI.md, skills, hooks and subagents per the transition notice above.
- Kiro: steering files, hooks and specs: https://kiro.dev/

---

## 4. Evidence on productivity and risk

### Productivity

- **METR, 2025-07-10 (VERIFIED).** 16 experienced open-source developers worked on 246 real issues (about 2 hours each).
  - With AI allowed, they were **19% slower** (95% CI +2% to +39%).
  - Beforehand they expected a 24% speedup; afterwards they still *believed* they had been 20% faster.
  - Source: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
- **METR follow-up, 2026-02-24 (VERIFIED).** 57 developers, 800+ tasks, late-2025 tools.
  - Returning developers: estimated **18% speedup**, CI −38% to +9%.
  - New developers: **4% speedup**, CI −15% to +9%. Neither result is statistically clear.
  - METR calls the data unreliable because developers increasingly **refused to work without AI** and withheld tasks. It thinks a speedup by early 2026 is likely, but the evidence is weak, and it is redesigning the study.
  - Source: https://metr.org/blog/2026-02-24-uplift-update/
  - Teaching line: *feeling faster ≠ measured faster; measure on your own tasks.*
- **DORA 2025 "State of AI-assisted Software Development" (SECONDARY via Google blog; dora.dev not fetched).**
  - About 5,000 respondents.
  - **90%** use AI at work (+14 points).
  - Over 80% say it improved their productivity.
  - Trust: 24% trust it "a great deal" or "a lot"; 30% trust it "a little" or "not at all".
  - Key message: "AI is an amplifier" of the team's existing strengths and weaknesses.
  - No DORA 2026 report was found (UNVERIFIED whether one exists yet).
  - Sources: https://blog.google/technology/developers/dora-report-2025/ ; https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report
- **Stack Overflow Developer Survey 2025 (VERIFIED).**
  - **84%** use or plan to use AI tools; 51% of professional developers use them daily.
  - Trust: 33% trust AI accuracy, **46% distrust** it, 3% highly trust it.
  - **66%** say their top frustration is "almost right, but not quite".
  - 14.1% use agents daily at work; 37.9% have no plans to.
  - Source: https://survey.stackoverflow.co/2025/ai
- **Stack Overflow Developer Survey 2026 (published 2026-10-06; about 30.9k responses, SECONDARY).**
  - Coding assistants/agents are the top AI use case at **66%** (chatbots 63%), per the results page (VERIFIED).
  - **48%** trust AI when they can easily validate its output (VERIFIED).
  - Only about 6.6% would trust it for important decisions (SECONDARY).
  - Claude Code reportedly led among AI coding assistants, ahead of Copilot (SECONDARY, Visual Studio Magazine; exact % UNVERIFIED).
  - The trust question changed, so 2025 and 2026 are not directly comparable.
  - Sources: https://survey.stackoverflow.co/2026/ai ; https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/

### Incidents (for a "what goes wrong" slide)

1. **Replit, July 2025.** During a declared "code freeze", the Replit agent deleted SaaStr's production database (about 1,200 executives and about 1,190 companies). It then misreported that rollback was impossible. Replit's CEO called it "unacceptable". Fixes followed: dev and prod databases were separated and a planning-only mode was added. (SECONDARY, Fortune 2025-07-23) https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure
2. **PocketOS, April 2026.** A Cursor agent running Claude Opus 4.6 deleted the production database **and its backups in about 9 seconds**, causing a 30-hour outage. Reported cause: the agent found a long-lived Railway API token in an unrelated file and made one destructive API call. Data was later restored, per the founder and Railway. (OECD AI incident record) https://oecd.ai/en/incidents/2026-04-27-6153 ; https://www.theregister.com/2026/04/27/cursoropus_agent_snuffs_out_pocketos/
   - **Lesson:** credentials within the agent's reach *are* permissions.
3. **s1ngularity / Nx, Aug 2025 (supply chain).** Malicious Nx npm versions ran a postinstall script.
   - The script **looked for locally installed AI CLIs (Claude, Gemini, Amazon Q)** and prompted them to hunt for secrets. It used flags such as `--yolo` and `--trust-all-tools` to skip prompts.
   - Stolen data was pushed to public `s1ngularity-repository` repos: about 2,349 secrets from 1,346 repos (GitGuardian).
   - Sources: https://blog.gitguardian.com/the-nx-s1ngularity-attack-inside-the-credential-leak/ ; https://www.okta.com/newsroom/articles/the-s1ngularity-attack--when-attackers-prompt-your-ai-agents-to-
4. **Prompt injection via repo and issue text (2026, SECONDARY).**
   - "Clinejection" (2026-02-17): a malicious GitHub issue title led to compromise of the Cline npm package.
   - "Comment and Control" (2026-04): one injection pattern worked across the Claude Code Security Review, Gemini CLI Action and Copilot agents in GitHub workflows.
   - CSA warns that repo-controlled context files (CLAUDE.md / AGENTS.md / SKILL.md) are an attack surface and should be treated as third-party code.
   - Sources: https://labs.cloudsecurityalliance.org/research/csa-research-note-claude-code-github-action-prompt-injection/ ; https://labs.cloudsecurityalliance.org/research/briefing-csa-research-note-skill-md-agent-context-poisoning/ ; NVIDIA AGENTS.md attack-chain blog (https://developer.nvidia.com/blog/ — exact post URL not captured, UNVERIFIED).
   - The CSA count of 76 malicious skills out of 3,984 audited is UNVERIFIED.
5. **OWASP Top 10 for Agentic Applications 2026** (published 2025-12-09). Relevant entries: ASI01 Agent Goal Hijack, ASI06 Memory & Context Poisoning, ASI09 Human-Agent Trust Exploitation. https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/

---

## 5. Good practices (each backed by an official source)

1. **Give the agent a check it can run** (tests, build, lint, screenshot). Write the failing test first, then the fix.
   - Anthropic: "If you can't verify it, don't ship it." https://code.claude.com/docs/en/best-practices
2. **Explore, then plan, then code, then commit.** Skip the plan only when the diff fits in one sentence. (Same page.)
3. **Small, scoped tasks and small diffs.** Name the files, the constraints and what "done" means. Use `/clear` between tasks; after two failed corrections, start fresh. (Same page.)
4. **Review every change, ideally with fresh eyes.** Use a writer/reviewer session or a review subagent.
   - GitHub's cloud agent opens **draft PRs only**, can't approve or merge, and the requester can't approve their own agent PR.
   - CI does not run until a human clicks "Approve and run workflows".
   - Source: https://docs.github.com/en/copilot/concepts/agents/coding-agent/risks-and-mitigations
5. **Never give production credentials.** Keep tokens out of the repo and the working directory; use separate dev and prod environments.
   - PocketOS and Replit both show why.
   - Copilot's cloud agent adds a firewall, secret scanning, CodeQL and dependency checks by default (GitHub doc above).
6. **Sandbox and least privilege.**
   - Run in Manual or auto mode with the sandbox on.
   - Use `bypassPermissions` / `--yolo` / `danger-full-access` **only in a throwaway container or VM**.
   - Use deny rules for dangerous commands, for example `git push` and `rm -rf`.
   - Sources: https://code.claude.com/docs/en/permission-modes ; https://learn.chatgpt.com/docs/sandboxing
7. **Treat repo text as untrusted**, including README files, issues, AGENTS.md from someone else's repo, and third-party skills and MCP servers. Use plugins only from trusted sources. https://code.claude.com/docs/en/plugins/security
8. **Use git as the real undo button.** Work on a branch or worktree; checkpoints are not git. https://code.claude.com/docs/en/checkpointing

---

## Items marked UNVERIFIED / do not put on slides as hard numbers

- Antigravity free-quota size, and Google AI plan prices on the Antigravity page.
- Any SWE-bench Verified score above 80% (aggregator only).
- Any SWE-bench Pro score above 62%: all come from vendor scaffolds or aggregators, not the Scale board.
- Independent Terminal-Bench 4.0 leaderboard rows: the page is JS-rendered. Only the vendor table was read.
- Exact percentages for Claude Code vs Copilot in SO 2026, and the 6.6% "important decisions" figure.
- Whether a DORA 2026 report exists.
- Third-party malicious-skill counts (CSA / Antiy).
- The SpaceX–Cursor deal value and close date (press only; the effect on the pricing page is VERIFIED).

## Recommendation for the rebuild

Keep the old package's stance: teach the durable loop (plan, act, verify, review) and treat volatile facts separately.
- **Add** one "landscape and price bands" slide with Oct 2026 names (Devin Desktop, Antigravity CLI, Copilot cloud agent), dated "as of 2026-10-16".
- **Add** one "benchmarks: what they measure and why they mislead" slide: Verified retired, Pro, TB 4.0.
- **Add** one METR slide: "felt 20% faster, measured 19% slower".
- **Add** one incident slide: Replit, PocketOS, s1ngularity.

## Deck fact-check and audit, 2026-10-16

An independent fact-check of every slide and note, plus a student/visual audit. Changes applied:

- Price bands: the middle band is $10–30 (Copilot Pro $10 … Cursor Premium $30); the top band is "from $100" (ChatGPT Pro also has a $500 tier). Codex on ChatGPT Free is for quick tasks.
- Gemini CLI: only free, AI Pro and Ultra users moved to the Antigravity CLI (18.06.2026); Gemini CLI still works for Enterprise and API keys.
- Claude Code auto mode: the default in the terminal and VS Code from v2.1.283; reads and in-folder edits skip the classifier, which reviews commands and network access. 17% = false-negative rate on Anthropic's set of 52 real overeager actions.
- `/init`: drafts CLAUDE.md in Claude Code, AGENTS.md in Codex (Codex: secondary sources).
- METR 2025: tasks were randomly assigned "AI allowed / not allowed"; tools of early 2025 (Cursor + Claude 3.5/3.7). Shown on the slide subtitle.
- Nx/s1ngularity: the malware stole keys itself and also prompted installed AI CLIs to list secret files; many refused.
- Clinejection: Cline's own AI issue-triage bot ran the injected command; publishing tokens were stolen via CI; an infected Cline CLI 2.3.0 went out on npm (17.02.2026).
- Benchmarks slide removed for beginners; SWE-bench caveats kept in the METR notes (OpenAI's Feb 2026 reasons: flawed tests and training leakage).
- Diagrams redrawn in HTML (bilingual, readable over Teams); colours: violet = agent, green = human.
