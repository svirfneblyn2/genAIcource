# L09 Source Notes: Claude ecosystem and Artifacts (fact sheet)

Checked on: **2026-10-13** (all URLs below were read on this date unless marked otherwise).
Rule: official Anthropic pages first; news only where official pages are missing. `[UNCERTAIN]` = not confirmed on an official page, or sources conflict.

---

## 1. Model lineup (Claude 5.x family)

Current lineup per the official models page: **Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5**. Source: https://platform.claude.com/docs/en/about-claude/models/overview

| Model | Positioning (official wording, shortened) | API price in / out per 1M tokens | Context / max output | Released |
|---|---|---|---|---|
| Claude Fable 5.1 | Most capable widely released model. For demanding reasoning and long-horizon agent work. Slowest. | $10 / $50 | 1M / 128K | ~2026-09-01 `[UNCERTAIN: inferred from retirement date "not sooner than Sep 1, 2027"; news confirms launch but not the day]` |
| Claude Opus 5.5 | "For long-running agentic coding and knowledge work". The docs say to **start here** for most workloads. | $4 / $20 (40% cheaper than Opus 5) | 1M / 128K | 2026-09-22 |
| Claude Sonnet 5.5 | "The best combination of speed and intelligence". Fast. | $2 / $10 | 1M / 128K | 2026-09-28 |
| Claude Haiku 5.5 | High-volume, latency-sensitive work (classification, extraction, routing). Fastest and cheapest. | from $0.10 / $0.50 (prompts up to 100K tokens; $0.50 / $2.50 above that) | 1M / 128K | 2026-10-07 |

- Release dates for Opus, Sonnet and Haiku 5.5 come from the "Introducing ..." posts in the Anthropic newsroom: https://www.anthropic.com/news
- All four models have knowledge cutoff Jun 2026, adaptive thinking and vision. Batch API is 50% off. https://platform.claude.com/docs/en/about-claude/models/overview
- **Claude Mythos 5.1** is the same model as Fable 5.1 with different safeguards. Access is limited to trusted-access programs (cyber and life sciences). Same price. https://platform.claude.com/docs/en/about-claude/model-deprecations and SD Times: https://sdtimes.com/tag/mythos-5-1/
- Earlier 2026 models (still listed as active "legacy"): Opus 4.6 (~Feb 5), Opus 4.7 (~Apr 16), Opus 4.8 (~May 28), Fable 5 / Mythos 5 (Jun 9), Sonnet 5 (~Jun 30), Opus 5 (~Jul 24). `[UNCERTAIN: day = retirement date minus 1 year]`. Fable 5 on Jun 9 is confirmed by news: https://smartscope.blog/en/blog/claude-fable-5-mythos-5-release/
- Claude Mythos Preview (Apr 7, 2026, Project Glasswing, defensive cybersecurity only, about 50 organisations) is now deprecated. https://platform.claude.com/docs/en/about-claude/model-deprecations and https://www.anthropic.com/glasswing
- **Default model in the claude.ai app**: `[UNCERTAIN]` No official page found. The API docs recommend Opus 5.5 as the starting point. For the Free plan, third-party guides name Sonnet 4.6 or Sonnet 5 (pre-5.5 data). Check in the app's model menu before recording.
- Teaching line: **Fable = biggest and smartest, Opus = strong default for serious work, Sonnet = fast all-rounder, Haiku = fastest and cheapest.**

## 2. Product surfaces

| Surface | What it does (one line) | Plans | Source |
|---|---|---|---|
| claude.ai web, desktop (Mac, Windows; Linux beta), iOS and Android | Main chat app. Usage is shared across all of them. | All (Free+) | https://claude.com/pricing , https://code.claude.com/docs/en/overview |
| **"One Claude" (Sep 16, 2026)** | Cowork and chat merged into one Claude. Claude decides whether a request needs a quick answer or a long multi-step job, can keep working after you close the laptop, and can run scheduled tasks. Rolled out first to Pro and Max; Team and Free "soon"; Enterprise gets 30 days' notice. | Pro and Max first | https://claude.com/resources/articles/cowork-is-now-claude |
| Claude Cowork (history) | Desktop agent for non-coding work: you pick a folder and it reads and edits the files. Research preview Jan 12, 2026 (Max, macOS). GA around Apr 9, 2026. Now merged into Claude (see above). | was Max, then Pro+ | https://heise.de/-11139805 , https://pasqualepillitteri.it/en/news/755/anthropic-managed-agents-cowork-ga-april-9-2026 `[news]` |
| Claude Code | Agentic coding tool: reads the codebase, edits files, runs commands. Runs in the terminal CLI, VS Code/Cursor, JetBrains, the desktop app (Code tab), the web (claude.ai/code), mobile, Slack, Chrome, and GitHub/GitLab CI. Also has Routines (scheduled cloud runs). | Pro, Max, Team, Enterprise (or a Console API account). Not Free. | https://code.claude.com/docs/en/overview , https://claude.com/pricing |
| Claude in Chrome | Browser extension: Claude reads, clicks and fills in pages in your Chrome. GA Aug 26, 2026. Side panel version still in beta. | Paid plans only | https://claude.com/claude-in-chrome , https://gigazine.net/gsc_news/en/20260827-claude-chrome-available/ `[news]` |
| Claude for Microsoft 365 | Add-ins for Excel, PowerPoint and Word (GA May 2026) and Outlook (public beta). They share context across the apps. | Pro, Max, Team, Enterprise (per pricing page) | https://claude.com/pricing , https://thenewstack.io/claude-word-excel-powerpoint-outlook-microsoft-office/ `[news]` |
| Claude for Google Docs, Sheets and Slides | Add-on plus connectors, in beta (Oct 6, 2026). | `[UNCERTAIN]` | https://claude.com/resources/articles/claude-now-works-in-google-docs-sheets-and-slides |
| Claude Tag (Slack) | A shared @Claude teammate in Slack channels. Can run long or scheduled tasks. Replaced the old Claude for Slack app. Beta from Jun 23, 2026. | Team, Enterprise | https://www.thestar.com.my/tech/tech-news/2026/06/24/anthropic-launches-claude-tag-in-research-preview-for-slack-users `[news]` , https://claude.com/docs/claude-tag/overview |
| Claude Design | Visuals, mockups, prototypes, slides and landing pages that follow your design system. Launched Apr 17, 2026 as a research preview. Now an artifact template inside Claude. The standalone claude.ai/design closes Dec 14, 2026. | All plans (since Oct 8, 2026) | https://claude.com/product/design , https://claude.com/resources/articles/dashboards-and-motion |
| Claude Docs / Slides / Dashboards / Motion | Artifact templates (see section 3). | see section 3 | https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them |
| Other 2026 launches | Claude for Government GA; Claude Security (beta, Enterprise). | - | https://claude.com/resources/product-announcements , https://claude.com/pricing |

## 3. Artifacts (redesigned Sep 16, 2026)

- **Official definition**: an artifact is "anything Claude makes for you that you'd put in front of someone". It opens beside the chat, and you can edit it, come back to it and share it. Claude makes one for substantial, self-contained content (usually more than 15 lines) that is likely to be reused. https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them
- **What artifacts can be**: documents, code snippets, single-page websites, images, diagrams and flowcharts, dashboards, small interactive tools (same URL). Underneath, these are HTML/JS pages or Markdown documents. The Claude Code docs say an artifact is "a single HTML page", and the source file can be `.html` or `.md`. https://code.claude.com/docs/en/artifacts . SVG, Mermaid and React (the older type names) are no longer listed as separate types `[UNCERTAIN: still renderable as HTML/JS; not named on the current page]`.
- **Templates** (https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them):
  - **Docs**: living documents you co-write with Claude and teammates. All plans.
  - **Slides**: decks you edit, present inside Claude, and export to PowerPoint or PDF. All plans.
  - **Design**: visuals, mockups, prototypes. All plans.
  - **Dashboards** (beta): built live from data platforms or connected apps (BigQuery, Snowflake, Databricks, Salesforce). Each chart shows its query and last refresh. Pro and up.
  - **Motion** (beta): animated explainers exported as MP4. Team and Enterprise.
  - Docs, Slides and Design came out of beta on Oct 8, 2026 (more than 45M made). Enterprise gets them on by default from Oct 15, 2026. https://claude.com/resources/articles/dashboards-and-motion
- **Free plan**: you can create artifacts in chat on **all plans**. Connecting apps and storing data require Pro or higher. The setting "Code execution and file creation" must be on. (support article above)
- **Where they live**: the **Artifacts tab** in the sidebar. Artifacts made before Sep 16, 2026 are "legacy artifacts": they keep working, but new ones can't be made in the old way. Cowork "live artifacts" made before Aug 19, 2026 still work but can't be edited in place. (support article above)
- **AI-powered artifacts**: artifacts can call Claude, so they work as small apps. Viewers sign in with their own account, need no API key, and **usage counts against the viewer's plan** (it costs the creator nothing). New artifacts ask for permission the first time they call Claude. (support article above)
- **Persistent storage**: Pro and up. Two kinds: *personal* (each user sees only their own data) or *shared* (everyone sees the same data). 20 MB per artifact, text only. (support article above)
- **Connected apps / MCP in artifacts**: artifacts can call your connectors (for example Asana, Google Calendar, Slack) through the **viewer's own** connections. Connector tools that need approval for each action are not available to artifacts. On Pro and up. Under the hood these are MCP connectors (https://code.claude.com/docs/en/artifacts : "Pull live data with MCP connectors").
- **Sharing**: every artifact **starts private**. https://support.claude.com/en/articles/9547008-share-artifacts
  - Free, Pro, Max: **publish = public link, so anyone with the link can view and interact**, even without an account.
  - Team and Enterprise: share with specific people or "Everyone in your organization". "Anyone with the link" only works after an Owner turns on *External sharing*. It is not available for artifacts that use connected apps or call Claude.
  - Access levels: view, comment, or edit (depends on the type). Email invites are in beta.
  - "Remix" (old name): legacy artifacts on Free, Pro and Max can be built on by copying the code into a new chat. Only do this with artifacts from people you trust.
- **Artifacts from Claude Code**: Claude Code can publish session output as a live page at claude.ai/code/artifact/... The page updates in place, keeps versions, collects comments, and has a gallery at claude.ai/code/artifacts. Pro and up, and requires a claude.ai login (not an API key). https://code.claude.com/docs/en/artifacts
- **Enterprise controls**: CMEK support, admins pick which templates are allowed, a retention policy, audit log events, and the Compliance API. https://claude.com/resources/articles/dashboards-and-motion , https://code.claude.com/docs/en/artifacts
- Conflict to note: the Claude Code docs still say "Templates are in beta… on by default on Pro, Max, and Team". The newer Oct 8 post says they are out of beta on all plans. Use the Oct 8 post.

## 4. Projects, Memory, Connectors, Search, Research, Files, Code

- **Projects**: workspaces with their own knowledge files and custom instructions. Free has up to 5 projects. Team and Enterprise can share projects. https://claude.com/pricing
- **Memory**: Claude remembers preferences and context across chats and can search past chats. Free users got it on Mar 2, 2026 (paid plans had it from 2025). You can pause it, delete it, or use incognito chats. https://claude.com/pricing (Memory: all plans) , https://www.bloomberg.com/news/articles/2026-03-03/anthropic-tries-to-win-users-from-chatgpt-with-memory-feature `[news]`. Whether "search past chats" is paid-only: `[UNCERTAIN]`.
- **Connectors** (built on MCP): ready-made connectors in the **Connectors Directory** (Google Drive, Gmail, Calendar, GitHub, Notion, Slack, Asana, ...) plus custom remote MCP connectors. Available on all plans, but Free gets **1 custom connector**. https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-MCP , https://claude.com/docs/connectors/custom/remote-mcp
- **Web search**: all plans, including Free. **Research** (deep multi-step research): Pro and up. https://claude.com/pricing
- **File creation and code execution**: Claude runs code in a cloud sandbox to create real .xlsx, .docx, .pptx and .pdf files. Turn it on with the "Code execution and file creation" setting (also needed for artifacts). https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them

## 5. Skills (Agent Skills)

- **What a Skill is**: a folder with a `SKILL.md` file (name and description in the header, then instructions). It can also hold scripts, templates and reference files. Claude reads only the name and description at first, and loads the full skill when a task needs it ("progressive disclosure"). https://agentskills.io/home , https://claude.com/skills
- **Where it works**: claude.ai on all plans (Team and Enterprise can deploy org-wide: https://claude.com/pricing), Claude Code (`/skill-name`: https://code.claude.com/docs/en/skills ), and the API (Skills API, now out of beta: https://platform.claude.com/docs/en/build-with-claude/skills-guide ).
- **Built-in Anthropic skills**: docx, xlsx, pptx and pdf (these generate the Office and PDF files), plus a skill-creator skill. https://claude.com/skills `[UNCERTAIN: the exact current list on the page was not enumerated]`
- **Open standard**: introduced Oct 2025, published as an open standard on Dec 18, 2025 at **agentskills.io**. Adopted by 25+ products (OpenAI Codex, Gemini CLI, GitHub Copilot, Cursor, VS Code ...). https://agentskills.io/ , https://www.unite.ai/anthropic-opens-agent-skills-standard-continuing-its-pattern-of-building-industry-infrastructure `[news; adoption count approximate]`
- **Plugins and marketplaces**: plugins bundle skills, commands, agents, hooks and MCP servers, and install from marketplaces (Claude Code; Cowork plugins since Feb 2026). https://code.claude.com/docs/en/plugins `[UNCERTAIN: Cowork plugin date from news]`

## 6. Plans and prices (Oct 2026)

Source: https://claude.com/pricing
- **Free** $0: chat on all platforms, web search, memory, artifacts, Docs/Slides/Design, connectors, skills, up to 5 projects.
- **Pro** $20/mo (or $17/mo billed annually, $200/yr): adds Claude Code, Research, more models, Chrome, Microsoft 365, Dashboards.
- **Max 5x / 20x** from $100/mo (5x) and $200/mo (20x) `[20x price from 2025 memory, page says "from $100"]`: 5x or 20x Pro usage, priority access, and $100-200/mo in API credits.
- **Team**: Standard seat $20 (annual) or $25 (monthly); Premium seat $100 or $125. 2 to 150 seats. SSO, no training on your data by default, admin controls.
- **Enterprise**: $20/seat/mo billed annually **plus usage at API rates**. Adds SCIM, audit logs, the Compliance API, custom retention, and a HIPAA-ready option.
- **Usage limits, in one line**: usage is a pool shared across web, desktop, mobile and Claude Code. It resets on a rolling 5-hour window (paid plans also have weekly caps), with no fixed message count. Pro gets at least 5x Free; when you hit the limit, wait, upgrade, or turn on usage credits billed at API rates.

## 7. Developer side (simple terms)

- **Messages API**: one endpoint (`POST /v1/messages`). You send messages and get Claude's reply. https://platform.claude.com/docs/en/get-started
- **Tool use**: you describe functions. Claude asks to call them and your code runs them. Server tools such as web search, web fetch and code execution run on Anthropic's side. https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview
- **Files API** (out of beta): upload a file once and reference it by ID in later requests. **Citations**: answers point to the exact passages in your documents. https://platform.claude.com/docs/en/build-with-claude/files , https://platform.claude.com/docs/en/build-with-claude/citations
- **Prompt caching**: reuse a long, repeated prompt prefix. Cache reads cost **10% of the input price (90% saving)**, or 5% on Opus 5.5 and Sonnet 5.5, and 2.5% on Fable 5.1. Writing to the cache costs 1.25x (5-minute TTL, the default) or 2x (1-hour TTL). https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- **Claude Agent SDK**: Claude Code's agent loop and tools as a library (Python and TypeScript) for building your own agents. https://code.claude.com/docs/en/agent-sdk/overview
- **Claude Managed Agents** (public beta Apr 8, 2026): Anthropic runs the agent loop and a sandbox for you. Price is API tokens plus $0.08 per session-hour. https://platform.claude.com/docs/en/managed-agents/overview , https://itbrief.com.au/story/anthropic-launches-claude-managed-agents-in-public-beta `[news for price/date]`
- **Clouds**: Amazon Bedrock, Google Cloud (Vertex AI), **Microsoft Foundry**, and the new **Claude Platform on AWS** (run by Anthropic). Every current model is on all of them. https://platform.claude.com/docs/en/about-claude/models/overview

## 8. Privacy and governance (beginner level)

- **Training on consumer chats**: since the consumer terms update (announced Aug 28, 2025; existing users had to choose by Oct 8, 2025), Free, Pro and Max users (including Claude Code on those accounts) **choose** whether their chats are used for training. If you allow it, data is kept up to **5 years**; if not, **30 days**. Deleted chats, incognito chats and connector content are not used. https://www.anthropic.com/news/updates-to-our-consumer-terms , https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training
- **The default**: in the pop-up, the "Help improve Claude" toggle was **on by default**, so it was effectively opt-out. Change it in Settings > Privacy. `[UNCERTAIN: default reported by news, not stated on official page]` https://www.smithstephen.com/p/claude-flips-the-privacy-default
- **Team, Enterprise, API, Education, Gov**: covered by commercial terms, so **no training on your data by default**. https://www.anthropic.com/news/updates-to-our-consumer-terms , https://claude.com/pricing
- **What a public artifact link means**: anyone who has the link can open it and use it, with no login needed. Treat it as published on the internet. On Team and Enterprise this is off until an admin turns it on, and turning it off blocks existing public links. https://support.claude.com/en/articles/9547008-share-artifacts , https://code.claude.com/docs/en/artifacts
- **Artifact retention (organisations)**: admins can set separate retention periods for private and shared artifacts. https://code.claude.com/docs/en/artifacts

## 9. Notable 2026 news for a beginner course

- Jan 12: **Cowork** research preview (a Claude agent for files and desktop tasks). https://heise.de/-11139805 `[news]`
- Mar 2: **Memory** for Free users. `[news, Bloomberg]`
- Apr 7: **Claude Mythos Preview** and **Project Glasswing**. Anthropic withheld the model from general release because of its cyber capabilities. https://www.anthropic.com/glasswing
- Apr 8-9: **Managed Agents** beta and **Cowork GA**. Apr 17: **Claude Design**. `[news]`
- May: **Claude for Excel, PowerPoint and Word** GA; Outlook beta. `[news]`
- Jun 9: **Fable 5**, the first Mythos-class model released to the public. Jun 23: **Claude Tag** in Slack. `[news]`. June: Anthropic reportedly **filed confidentially for an IPO** `[UNCERTAIN, news via Reuters/The Star]`.
- Aug 26: **Claude in Chrome GA**. Around Sep 1: **Fable 5.1**.
- Sep 16: **"One Claude"**: Cowork and chat merged, plus the new Artifacts with Docs, Slides and Design. https://claude.com/resources/articles/cowork-is-now-claude
- Sep 22 / 28 / Oct 7: **Opus 5.5, Sonnet 5.5, Haiku 5.5**. https://www.anthropic.com/news
- Oct 6: Google Docs/Sheets/Slides add-on. Oct 8: **Dashboards and Motion**; Docs, Slides and Design out of beta on all plans. Oct 8: 2026 Usage Policy update. https://claude.com/resources/articles/dashboards-and-motion , https://www.anthropic.com/news

## Official launch post for the Artifacts redesign

- **"Claude Cowork and chat are now one Claude"**, **Sep 16, 2026**: https://claude.com/resources/articles/cowork-is-now-claude (also at /blog/cowork-is-now-claude). It introduced Docs and Slides and brought Design into conversations. Sep 16 is also the date the support article uses to separate legacy artifacts from new ones.
- Follow-up: **"Build live dashboards and animate explainers with Claude"**, Oct 8, 2026: https://claude.com/resources/articles/dashboards-and-motion
- No separate post titled "artifacts redesign" was found.

## Official images (credit: "Image: Anthropic / claude.com")

I checked these visually (contact sheet). Illustrations are Anthropic's hand-drawn brand art; screenshots show the real UI.

| What it shows | Image URL | Found on |
|---|---|---|
| **Screenshot**: Dashboard artifact ("Bike share, System overview") next to the chat | https://assets.claude.com/7688d4d3b888c17cf4b3553f537f291882a92656.png | /resources/articles/dashboards-and-motion |
| **Screenshot**: typing `/motion` in the message box to pick Motion | https://assets.claude.com/46f88e8de631c732fa245ad453262e6ef35c0e73.png | same |
| **Screenshot**: Claude Code artifact viewer with the Share menu (org audience, versions, mockups and funnel chart) | https://mintcdn.com/claude-code/kaHIYYMIYMYPxQg9/images/artifacts-viewer.png?fit=max&auto=format&n=kaHIYYMIYMYPxQg9&q=85&s=dbfd671cdb0d15f49f808b9e89778fe1 | https://code.claude.com/docs/en/artifacts |
| **Screenshot**: chat snippet "build the reveal deck…, Building the launch deck" (Slides in a conversation) | https://assets.claude.com/5417c7f247242efc74cab6cab3a72de5e1a8ea7c.png | https://claude.com/features/artifacts |
| **Screenshot**: Claude making a skill ("sales-call-prep", Download) | https://assets.claude.com/572b84df17db14b777351330da9080808c60a0c7.jpg | https://claude.com/skills |
| **Screenshot**: chat plus browser side by side (pricing-comparison task, Cowork/agent) | https://assets.claude.com/e0035a095d8888c9739f8acb305f517b25d469eb.jpg | https://claude.com/product/cowork |
| **Screenshot**: Claude Code in a terminal | https://assets.claude.com/d4645137a0c197beee5313fedbf9417d035452fc.webp | https://claude.com/product/claude-code |
| **Screenshot**: Claude Code extension in VS Code | https://assets.claude.com/454390de9d9ccefb6082b7c2440c7547c1ec3964.webp | same |
| **Screenshot**: Claude Code on the web | https://assets.claude.com/60bc422c7916679b221ea6d55ba27adc584ac66e.webp | same |
| Illustration: easel (Artifacts page social image) | https://assets.claude.com/6dc7dfac91662cacf52534a25252db332309cb0d.jpg | /features/artifacts |
| Illustration: Design page social image | https://assets.claude.com/e4b264424c992d5dc8f29ee10d1dd0662e34a6ca.jpg | /product/design |
| Illustration: Cowork page social image | https://assets.claude.com/9716b96b8df867765a639f3ea8a07170508200bf.jpg | /product/cowork |
| Illustration: Skills page social image | https://assets.claude.com/143afdc0f503ccbec15a051fa5dcf71bb6bb1da0.jpg | /skills |
| Illustration: Claude in Chrome page | https://assets.claude.com/c8184fa257625063ff8fc3253e83260d57f0f32c.jpg | /claude-in-chrome |
| Video (webm) loops: Artifacts / Design / Cowork / Skills | https://assets.claude.com/c5788873a7fbd74ad7caec11fa90610ee8d8bc14.webm , https://assets.claude.com/f0dd16266306d6e9526aebb58f38a4f46f2c4942.webm , https://assets.claude.com/0d948b3a3dbf8e9669c90f8a669af1be99dd2fa0.webm , https://assets.claude.com/3ec626bfee08f251c31203f17f02c5c032213ffe.webm | product pages above (not inspected frame by frame) |

The anthropic.com/news posts for Opus, Sonnet and Haiku 5.5 were not scraped for images. Before reuse, check claude.com's terms or the press kit (https://www.anthropic.com/press-kit `[UNCERTAIN: URL not verified]`).

## 10. Additions verified directly by the deck author (2026-10-13)

Read in the built-in browser from https://support.claude.com/en/articles/17153992-what-are-artifacts-and-how-do-i-use-them ("Updated this week"):
- **Export**: Docs → Word, PDF, Markdown, Google Docs; decks → PowerPoint, PDF or straight to Google Slides; designs → .zip, PDF, PowerPoint, standalone HTML; animations → MP4. (Dashboards: no export listed — "each chart shows its query and when it was last refreshed".)
- **Editing**: ask Claude, or edit directly in template artifacts; in a doc, highlight text → "Edit with Claude".
- **AI-powered artifacts**: "the app runs on Anthropic's infrastructure. People using it sign in with their Claude account… no API keys… usage counts against each person's own plan limits". No plan restriction stated (the feature table lists only "Connect your apps" and "Store data" as Pro+).
- **Mobile**: iOS/Android can ask for a design, deck or doc and edit; sharing settings only on web/desktop.
- **Fix errors**: "Try fixing with Claude" button.
- Official screenshot in the deck (slide 6 / cover) shows the model picker reading "Opus 5.5 Medium" in the chat input.

API model ids (from the Claude Code environment of 2026-10-13): `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`, `claude-haiku-5-5`.

Official images used in the deck (downloaded with the author's permission, credited "Image: Anthropic"): `assets/official/` — dashboard_artifact.png (cover, slide 6), code_artifact_share.png (slide 20), skill_create.jpg (slide 17), agent_browser.jpg (slide 18), code_terminal.webp (unused).

## 11. Real UI screenshots (deck v2, captured 2026-10-13)

Captured by Claude in Chrome in the course author's claude.ai account (Max plan, Opus 5.5 Medium), with chat history, pinned projects and the email blurred. Originals: `assets/screens/`, crops for the deck: `deck/make_screens.py` → `assets/img/scr_*.jpg`.
Observed in the UI that day (facts used on slides):
- Sidebar: New, Projects, Artifacts, Scheduled, Customize, More; chat / Code toggle at the top.
- "+" menu: Add files or photos, Skills, Connectors, Design system, Plugins, Devices, Research, Memory.
- Model menu captions: Fable 5.1 "For your toughest challenges"; Opus 5.5 "For complex work and everyday tasks" (selected); Sonnet 5.5 "Most efficient for simpler tasks"; Haiku 5.5 "Fastest for quick answers"; plus Effort (Medium) and More models.
- Artifacts tab → "Make something new": Docs (New), Slides (New), Design (New), Dashboard (Beta). Banner: "Claude Design lives here now".
- Slides artifact Share panel: General access "Only people invited" (default) / "Anyone with the link — people with the link can view, but not edit"; Export: PDF, PowerPoint (.pptx, 3 options), PNG, Send to Google Slides, More formats.
- Connector permission prompt: "Claude wants to use Generate Diagram from Figma" — Decline / Allow once / Always allow.
- Settings → Privacy: "Help improve our AI models — Allow the use of your chats and coding sessions to train…" (ON in the author's account).
- Settings → Capabilities: Artifacts (on), AI-powered artifacts (OFF in the author's account), Inline visualizations.
- Project page: Instructions, Context (files), Memory, Scheduled; "Claude references the same knowledge every time you talk to it in this project."
Demo artifacts and chats created for the lesson remain in the author's account (private): Planёrka dashboard + 3 slides, courier deck, operator guide (Docs), landing (Design), complaint diagram, operator coach app, project "Демо L09: поддержка курьеров".
