# Microsoft AI / Copilot ecosystem: state as of 13 Oct 2026

Research for the beginner lesson "Microsoft Copilot ecosystem: an overview" (90 min, Teams).
Compiled 2026-10-13. Every fact carries a source and that source's date. "(3rd-party)" marks non-Microsoft sources.
Image URLs in the Visual sources table were **checked live (HTTP 200, image content-type)** on 2026-10-13 unless marked "unverified".

---

## 0. The big picture for the lesson (what changed in 2026)

1. **One app, one name.** In Aug–Sep 2026 Microsoft merged the consumer Copilot app and the work "Microsoft 365 Copilot app" into a single app called **Microsoft Copilot**. You can sign in with a personal account, a work/school account, or both, and switch between them. Data does not flow between the two. Work users mostly get a new icon and name. Consumer users were migrated automatically.
   - Support: "Copilot App Updates for Personal, Work, and School Accounts" https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app (2026)
   - Timing (3rd-party): unified app to Windows Insiders the week of 13 Aug; mobile and web from mid-Aug; Windows and Mac apps from mid-Sep. https://www.pymnts.com/news/artificial-intelligence/2026/microsoft-unifies-consumer-and-enterprise-copilot-in-push-for-single-ai-platform/ (13 Aug 2026)
   - Name history: Office app → "Microsoft 365 Copilot" app (from 15 Jan 2025; m365.cloud.microsoft) → "Microsoft Copilot", with the web apps consolidating under copilot.cloud.microsoft. https://support.microsoft.com/en-us/microsoft-365-copilot/the-microsoft-365-app-transition-to-the-microsoft-365-copilot-app
2. **The "new Copilot" (25 Sep 2026)** has three tabs: **Home** (Chat + Cowork, plus Office in Copilot), **Code** (build small apps by describing them; same technology as GitHub Copilot) and **Autopilot** (an always-on background agent, formerly "Scout"). https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/ (25 Sep 2026, updated 9 Oct 2026)
3. **Agents everywhere.** The product moved from a chat assistant to agents that do the work: Cowork (GA 16 Jun 2026), Researcher, Analyst, Facilitator, Channel Agent, Autopilot, and Agent 365 to govern them all.
4. **Multi-model.** Copilot runs OpenAI models (GPT-5.6) and Anthropic models (Sonnet 5, Opus 5, Fable 5), plus Microsoft's own MAI models. "Auto" picks a model for you.
5. **Pricing split.** "Everyday AI" stays on a flat per-user licence. Agentic work (Cowork, Code, Autopilot, frontier models) is billed by usage in **Copilot Credits**.
6. **Consumer pruning.** Mico (the avatar), Group Chat, Podcasts, Deep Research and Copilot Labs were retired on or after 18 Aug 2026. Edge "Copilot Mode" was retired in May 2026, and Windows pulled back some Copilot integrations.

> Teaching tip: the 2025 "Fall release" features (Mico, Groups, Labs, Copilot Mode in Edge) are now **history**. Show them as "things Microsoft tried and dropped", not as current features.

---

## 1. Microsoft 365 Copilot (work)

### 1.1 Naming: what's what (Oct 2026)
| Name | What it is | Source |
|---|---|---|
| **Microsoft Copilot** (app) | The unified app for Windows, Mac, web and mobile (formerly the Microsoft 365 Copilot app, and before that the Office app). Has Home / Code / Autopilot tabs. | blogs.microsoft.com, 25 Sep 2026; support "changes" article, 2026 |
| **Copilot Chat** | Web-grounded chat included **at no extra cost** for Entra (work) users with an eligible M365 plan. Can use agents (pay-as-you-go) and Pages. Grounded on public web data only unless the user has a licence. | https://www.microsoft.com/en-us/copilot/pricing/business ; Teams AI overview https://learn.microsoft.com/en-us/microsoftteams/copilot-ai-agents-overview (updated 18 Aug 2026) |
| **Microsoft 365 Copilot** (licence, "USL") | Paid per-user licence: Copilot inside Word, Excel, PowerPoint, Outlook and Teams, grounded in work data (Graph/Work IQ), plus agents | blogs.microsoft.com 25 Sep 2026; pricing post (below) |
| **Copilot in Office** vs **Office in Copilot** | *Copilot in Office* = the AI pane inside each Office app. *Office in Copilot* = full Word/Excel/PowerPoint editing inside the Copilot app (new, 25 Sep 2026). | Directions on Microsoft (3rd-party), Sep 2026 |

### 1.2 Teams
- **Copilot in meetings:** ask questions during and after a meeting, get summaries and action items. It uses the recording, transcript and chat, so transcription must be on. https://support.microsoft.com/office/0bf9dd3c-96f7-44e2-8bb8-790bedf066b1 (ms.date 23 Dec 2025)
- **Recap / intelligent recap:** the Recap tab shows AI notes, topics or chapters, speakers, name mentions, shared content and follow-up tasks. The full intelligent recap needs Copilot or Teams Premium. https://support.microsoft.com/office/c2e3a0fe-504f-4b2c-bf85-504938f110ef (ms.date 23 Sep 2026)
- **Translate recaps:** you can change a recap's language after it is generated (Aug 2026). https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--august-2026/4551960
- **Facilitator agent:** takes live AI notes that participants can co-edit, posts the agenda with a timer per topic, answers questions in chat, and drafts a Word document from the meeting. You turn it on per scheduled meeting ("Copilot and other AI" toggle). Included with a Copilot licence. https://support.microsoft.com/en-us/teams/copilot/facilitator-in-microsoft-teams-meetings (ms.date 13 Aug 2026). Since Sep 2026 Facilitator can also run a web search and post the answer when a factual question in the meeting goes unanswered (UC Today, 3rd-party, 14 Sep 2026).
- **Copilot in chats and channels:** summarizes a chat or thread and helps you catch up and draft replies. https://support.microsoft.com/office/cccccca2-9dc8-49a9-ab76-b1a8ee21486c (ms.date 29 Dec 2025)
- **Channel Agent:** an agent in a channel that flags deadlines, writes status reports, assigns tasks, schedules meetings and answers questions. Teams AI overview (updated 18 Aug 2026).
- **Teams Phone Agent:** an AI receptionist that answers calls in 60+ languages, books appointments and routes callers (rolled out Sep 2026; billed in credits). What's New Sep 2026 https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what%E2%80%99s-new-in-microsoft-copilot--september-2026/4559107 (30 Sep 2026)
- **@Copilot in Teams:** @mention Copilot like a colleague. Private preview from end of Sep 2026. blogs.microsoft.com 25 Sep 2026. Video: "Meet @Copilot in Teams" (see table).
- **Free AI in Teams (no Copilot licence):** Copilot Chat app, suggested replies, voice isolation, video optimization. Teams Premium adds intelligent recap and live translated captions. Teams AI overview (18 Aug 2026).
- **Meeting search by topic or keyword** across body, chat and transcripts from the last 2 months (release notes, 23 Sep 2026). https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes

### 1.3 Word
- Drafts from a prompt, notes or a referenced file, and rewrites selected text. https://support.microsoft.com/en-us/word/copilot/draft-and-add-content-with-copilot-in-word (ms.date 16 Sep 2026)
- "Edit with Copilot" works directly inside the open document (formerly called Agent Mode). https://support.microsoft.com/en-US/Word/edit-with-copilot-in-word (15 Sep 2026)
- Aug 2026: inserts hyperlinks, understands images in reference files, highlights the exact words it edited. Sep 2026: citations in responses, arranging images and shapes. What's New Aug and Sep 2026.
- Word default model: Claude Sonnet 5 (release notes, 25 Aug 2026; volatile).

### 1.4 Excel
- **"Agent Mode" was renamed.** It is now simply *Copilot in Excel*, with three modes: **edit** (default; changes the workbook live), **plan** (proposes steps for you to approve) and **chat** (no changes). Open it from the Copilot icon at the bottom right. https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel (ms.date 24 Sep 2026)
- Agent Mode in Excel went GA on Windows in Jan 2026 (3rd-party: sumproduct.com).
- **The =COPILOT() function was retired on 14 Sep 2026.** Old cells keep their cached values, but return #NAME? when they recalculate. Use the Copilot pane instead. https://support.microsoft.com/en-us/excel/functions/copilot-function (ms.date 14 Sep 2026). **Do not teach =COPILOT() as current.**
- Skills (for example finance skills), change history, links that jump to changed ranges (Sep 2026), Power BI grounding (Aug 2026). Release notes; blogs.microsoft.com 25 Sep 2026.

### 1.5 PowerPoint
- Create a deck from a prompt or a Word file. Copilot may ask clarifying questions (audience, style). https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d
- Edit with Copilot, plus prebuilt skills ("Review this preso", "Visualize this slide"). https://support.microsoft.com/en-us/powerpoint/edit-with-copilot-in-powerpoint (28 Aug 2026)
- Brand Kit, strict brand adherence, custom skills (Aug–Oct 2026), connectors (Sep 2026), long-running tasks that keep going after you close PowerPoint (Oct 2026). What's New Aug and Sep 2026; release notes 6 Oct 2026.
- You can choose the model when editing. https://support.microsoft.com/en-us/office/choose-your-model-when-editing-with-copilot-in-powerpoint

### 1.6 Outlook
- Summarize a thread (with citations), draft and coach replies, summarize attachments. https://support.microsoft.com/en-us/outlook/copilot-pages/summarize-an-email-thread-with-copilot-in-outlook (24 Apr 2026)
- Inbox triage in natural language: delete, move, categorize, manage rules and folders, with confirmation required for more than 5 emails or any rule change (release notes, 23 Sep 2026).

### 1.7 OneNote, Loop, Pages, Notebooks
- **Copilot Pages:** turns a chat answer into an editable, shareable page beside the chat. Available to work accounts with SharePoint or OneDrive even without a Copilot licence. https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-pages (ms.date 24 Sep 2026)
- **Copilot Notebooks:** a workspace of chats, files, pages and links that Copilot answers from. Since Aug 2026 there is a lightweight version in the Copilot app and the full workspace in **OneNote**, kept in sync. Researcher and Analyst can run inside a notebook. https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks (8 Sep 2026); What's New Aug 2026
- Loop: Facilitator's notes are a Loop component, and Loop must be enabled in Teams (Facilitator support page). Loop is no longer a headline Copilot surface; Pages and Notebooks took that role.

### 1.8 Copilot Search
- One AI search box across M365 and third-party connectors. Since 6 Oct 2026 it embeds a chat pane in the search results. Since Sep 2026 it is becoming the default search in SharePoint and OneDrive (Frontier), and admins can mark up to 100 "authoritative" sites. Release notes 6 Oct 2026; What's New Sep 2026; https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-search

### 1.9 Built-in agents
Source: "Agents built by Microsoft" https://support.microsoft.com/en-us/microsoft-365-copilot/agents-built-by-microsoft (ms.date 30 Sep 2026)
- **Researcher:** multi-step research over the web and your work data, producing a cited report. Available to M365 Premium/Pro consumers and to work users with the Copilot licence. Supports **Claude** (admin must allow Anthropic models), **Critique** and **Model Council** (multi-model checking), and Computer Use (Frontier). It replaces consumer "Deep Research". https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-researcher-in-microsoft-365-copilot (8 Sep 2026)
- **Analyst:** data analysis from attached files (sales by region, forecasts). https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-analyst-in-microsoft-365-copilot
- **Visual Creator** (images, video, prototypes), plus **Idea Coach, Writing Coach, Prompt Coach, Learning Coach, Career Coach** and a **Workflows** agent.
- In apps: **Facilitator**, **Channel Agent**, **Planner Agent chat** (Sep 2026), **Teams Phone Agent**; Word/Excel/PowerPoint agents in the Copilot app.
- **Cowork (the main agent of 2026):** describe an outcome and Cowork plans and runs multi-step work across M365 and the web (documents, email, meetings, files), asking approval before sensitive actions. Has an effort level (Light → Max), the /cost skill and Automations (scheduled or triggered tasks). **GA for business on 16 Jun 2026.** Built with Anthropic. https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/ ; consumer preview (US/Canada, Premium/Pro): https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-cowork (ms.date 14 Sep 2026)
- **Autopilot (formerly Scout):** a cloud agent with its own identity, memory, computer and workspace. It watches channels, follows up and runs recurring work, and you @mention it. Private preview from end of Sep 2026. Announced at Build on 2 Jun 2026; built on OpenClaw and Work IQ. blogs.microsoft.com 25 Sep 2026 and 2 Jun 2026.
- **Build your own agent** in Copilot (Agent Builder, templates): https://support.microsoft.com/en-us/microsoft-365-copilot/build-your-own-agent-with-microsoft-365-copilot (29 Sep 2026)

### 1.10 Agent Store, plugin registry, Work IQ, memory
- **Agent Store:** in the left navigation, "All agents" (screenshot on the "Agents built by Microsoft" page).
- **Plugin registry:** one catalog of Microsoft, partner and custom plugins (skills plus connectors) that IT approves once. GA Sep 2026. In prompts, "/" calls agents and "@" calls skills. What's New Sep 2026.
- **Work IQ:** the intelligence layer over your work data (mail, files, meetings, chats, people, and since 30 Sep 2026 Dynamics and Power Platform data). **Work IQ APIs GA on 16 Jun 2026**, billed in Copilot Credits. **Microsoft IQ** is the umbrella term (Work IQ + Fabric IQ + Foundry IQ), GA 2 Jun 2026. https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/ ; https://blogs.microsoft.com/blog/2026/06/02/microsoft-build-2026-be-yourself-at-work/
- **Memory:** Copilot remembers preferences and context (Work IQ, and Autopilot's own memory). No dedicated Oct 2026 memory release note was found. Volatile.
- **Fabric IQ:** connects Copilot to 20M+ Power BI semantic models. GA in Chat and Cowork (blogs.microsoft.com 25 Sep 2026).

---

## 2. Copilot Studio, agents, Agent 365, connectors (overview level)

- **Copilot Studio:** low-code builder for agents, workflows and now **apps** (Apps in public preview, Sep 2026). It supports the GitHub Copilot harness with hooks and a model dropdown, Foundry IQ knowledge (GA), Dataverse knowledge, evaluations, and Computer-Using Agents and real-time voice agents (GA by May 2026). https://www.microsoft.com/en-us/copilot/blog/copilot-studio/new-and-improved-build-apps-extend-agents-and-transform-business-processes-in-microsoft-copilot-studio/ (7 Oct 2026); overview https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio (25 Sep 2026)
- **Copilot Managed Runtime** (preview): Microsoft-hosted, governed hosting for apps built in Studio, Cowork and Code (blogs.microsoft.com 25 Sep 2026).
- **Agents for M365:** declarative agents (instructions + knowledge + actions) built in Copilot or Studio, surfaced in Copilot, Teams and Outlook. Foundry agents can also be published to Copilot and Teams: https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/publish-copilot
- **Agent 365:** the "control plane for agents": registry, identity (Entra), security (Defender, Purview), cost management. It covers Microsoft and third-party agents (it even detects "shadow AI" such as OpenClaw). **GA 1 May 2026, $15/user/month standalone or included in M365 E7.** https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/ ; https://learn.microsoft.com/en-us/microsoft-agent-365/overview
- **Copilot connectors** (formerly Graph connectors) index third-party data for Copilot. **Federated connectors** (GA Sep 2026) use **MCP** to fetch data live without indexing it, and are supported in Researcher, Chat and Excel. Connector management moved to M365 admin center → Copilot → Connectors in Aug 2026. Release notes, 23 Sep 2026.

---

## 3. Consumer Microsoft Copilot, Edge, Windows

### 3.1 Consumer Copilot app (copilot.microsoft.com / copilot.com, Windows, Mac, iOS, Android)
- Now the same unified **Microsoft Copilot** app, signed in with a personal Microsoft (or Google/Apple) account. Chats and content migrated automatically. Files go to OneDrive, and old Tasks content became Pages. https://support.microsoft.com/en-us/microsoft-365-copilot/learning/changes-microsoft-copilot-app
- **Retired on/after 18 Aug 2026:** Group Chat (Groups), Podcasts, Deep Research (replaced by Researcher for Premium/Pro), and Copilot Labs (3rd-party). **Mico** was removed from voice mode; reportedly it lives on only in the "Learn Live" tutoring experience (3rd-party). Same support page; https://www.techrepublic.com/article/news-microsoft-copilot-app-merger/ (Aug 2026, 3rd-party); https://www.geekwire.com/2026/microsoft-starts-merging-its-copilot-consumer-and-business-apps-in-advance-of-super-app-rollout/
- **Still there:** chat, **Voice**, **Vision** (share screen or camera during voice), image generation (free tier with limits), Pages, Cowork (preview, Premium/Pro, US/Canada), Researcher and Analyst (Premium/Pro). Usage table: https://support.microsoft.com/en-us/microsoft-365-copilot/ai-credits-and-limits-for-microsoft-365-subscriptions
- **Copilot Health** (launched 12 Mar 2026): a separate, privacy-isolated health space. It can connect 50+ wearables and US health records, cites sources including Harvard Health, and searches providers. US only, 18+, preview for Personal/Family/Premium. Temporarily unavailable for some users during the app merge. https://microsoft.ai/news/introducing-copilot-health/ ; https://support.microsoft.com/en-us/microsoft-copilot/copilot-health (5 Jun 2026)
- **Record** (mobile): records in-person conversations and produces a transcript and summary (Sep 2026, work side). What's New Sep 2026.

### 3.2 Edge
- **Copilot Mode was retired as a separate mode on 13 May 2026.** Its features moved into normal Edge: multi-tab reasoning, history and long-term memory (opt-in), Vision and Voice, a redesigned new tab page, quizzes, Study and Learn, writing assistant (US), podcasts from tabs. **Journeys** are free in English markets (mobile: US only). **Actions** became "**Browse with Copilot**": Edge desktop, M365 Premium, US only. https://blogs.windows.com/msedgedev/2026/05/13/new-updates-to-edge-across-desktop-and-mobile/ (13 May 2026)
- New Copilot new tab page for work (search + chat in one box) rolling out Oct 2026 (What's New Sep 2026).

### 3.3 Windows 11
- **Copilot app** on the taskbar; **Copilot key** on new keyboards. https://support.microsoft.com/en-au/microsoft-copilot/getting-started-with-copilot-on-windows
- **"Hey Copilot":** off by default. An on-device 10-second buffer listens for the wake word. Windows desktop app only. https://support.microsoft.com/en-us/microsoft-copilot/copilot-wake-word-hey-copilot (ms.date 1 Oct 2026)
- **Copilot Vision:** share an app window or the desktop during voice; Copilot can highlight where to click but takes no actions. 170+ markets. Work accounts got Vision in M365 Copilot in Sep 2026 (release notes), though the support page dated 26 Jun 2026 still says not for commercial customers. https://support.microsoft.com/en-us/microsoft-365-copilot/how-vision-microsoft-365-works
- **Ask Copilot on the taskbar** (opt-in replacement for the search box: Settings → Personalization → Taskbar). Type "@" to call agents. https://blogs.windows.com/windowsexperience/2025/10/16/making-every-windows-11-pc-an-ai-pc/ (16 Oct 2025); video "Ask Copilot in taskbar"
- **Agent in Settings:** describe the change in plain words and it can apply it (English; started on Copilot+ PCs). https://www.microsoft.com/en-us/windows/learning-center/two-must-try-ai-tools-that-simplify-tasks
- **Click to Do:** AI actions on whatever is on screen (summarize, rewrite, Ask Copilot), running on the local Phi Silica model. Ask Copilot is not available in the EEA. https://support.microsoft.com/en-us/windows/click-to-do-in-recall-do-more-with-what-s-on-your-screen-967304a8-32d1-4812-a904-fad59b5e6abf (21 May 2026)
- **Recall** (Copilot+ PC only: 40+ TOPS NPU, 16 GB RAM): opt-in, encrypted, Windows Hello, Win+J. https://support.microsoft.com/en-us/windows/retrace-your-steps-with-recall-aa03f8a0-a78b-4b3e-b0a1-2eb8ac48701c
- **Copilot Actions on Windows** (agent that works in your apps or files, experimental, Oct 2025). Video "Copilot Actions on Windows" (15 Oct 2025).
- **2026 pullback (3rd-party, anonymous sources):** Microsoft paused new Copilot buttons in in-box apps and is scaling back Copilot in Notepad, Paint, Photos, Snipping Tool and Widgets. Shell integrations (notifications, Settings, File Explorer) were shelved, and Recall is being reworked. https://www.windowscentral.com/microsoft/windows-11/microsoft-is-reevaluating-its-ai-efforts-on-windows-11-plans-to-reduce-copilot-integrations-and-evolve-recall (Jan 2026); https://www.windowscentral.com/microsoft/windows-11/microsoft-quietly-scraps-plans-to-bring-copilot-to-notifications-and-settings-on-windows-11-as-it-moves-to-reduce-ai-bloat-across-the-os (Mar 2026)

---

## 4. GitHub Copilot (brief)

- **Plans (individual):** Free $0 · Pro $10/mo · Pro+ $39/mo · **Max $100/mo** (new 2026). **Business $19/user/mo · Enterprise $39/user/mo.** https://github.com/features/copilot/plans (checked 13 Oct 2026)
- **Billing changed 1 Jun 2026:** premium requests were replaced by **GitHub AI Credits** (1 credit = $0.01), consumed by tokens at each model's API rate. Paid plans include credits equal to the price plus a "flex" bonus (Pro $15 total, Pro+ $70, Max $200). Completions and next-edit suggestions are free. Code review also uses Actions minutes. https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/ ; https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/
- **Surfaces:** IDE (VS Code, Visual Studio, JetBrains), **cloud/coding agent** (assign an issue → it opens a PR), **code review**, **Copilot CLI**, **Spaces** (shared context), **GitHub Copilot app** (desktop, parallel agent sessions in git worktrees, "Agent Merge"; preview 14 May, GA 17 Jun, on all plans from 7 Jul 2026), **Copilot SDK** (GA), computer use in the CLI and app (public preview, 1 Oct 2026). Pro+ can delegate to **third-party agents** (preview; the "Agent HQ" idea from Universe 2025). https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/ (2 Jun 2026); https://github.blog/changelog/2026-07-07-github-copilot-app-available-to-all/ ; https://github.blog/changelog/2026-10-01-github-copilot-can-now-interact-with-desktop-apps/
- **Models:** the plans page lists models from Anthropic (Sonnet 5/5.5, Opus 5/5.5, Fable 5/5.1, Haiku), OpenAI (GPT-5.x, GPT-6 Astra/Luna/Sol), Google Gemini 3.x, xAI Grok, Kimi, and Microsoft **MAI-Code-1.1-Flash**.
- **Bridges to M365:** the Code tab in the Copilot app uses GitHub Copilot technology and syncs with it. GitHub Copilot is available as a Teams agent (GA Oct 2026). Copilot Studio offers a "GitHub Copilot harness".

---

## 5. Other Microsoft AI

| Product | One-line state (Oct 2026) | Source (date) |
|---|---|---|
| **Microsoft Foundry** (formerly Azure AI Foundry, formerly Azure AI Studio) | Developer platform: 10,000+ models (OpenAI, Anthropic, Meta, MAI…), Agent Service with hosted agents, Foundry IQ (formerly Azure AI Search), Foundry Tools (formerly Azure AI Services), Foundry Local. Assistants API sunset 26 Aug 2026 in favour of the Responses API. | https://learn.microsoft.com/en-us/azure/foundry/what-is-foundry (13 Aug 2026) |
| **MAI models (Microsoft AI, Mustafa Suleyman)** | History: MAI-Voice-1, MAI-1-preview (Aug 2025), MAI-Image-1 (Oct 2025), MAI-Image-2 (Mar 2026). **Build, 2 Jun 2026, seven models:** MAI-Thinking-1 (reasoning; ~1T MoE), MAI-Code-1-Flash (in GitHub Copilot/VS Code), MAI-Image-2.5 (+Flash), MAI-Transcribe-1.5, MAI-Voice-2 (+Flash). Distributed via Foundry, OpenRouter, Fireworks, Baseten. The site sidebar already lists MAI-Image-2.6 and MAI-Code-1.1-Flash. | https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/ (2 Jun 2026) |
| **Image creation** (Copilot, Designer, Bing Image Creator) | Image generation is in the Copilot app (free tier with limits) and via the Visual Creator agent. Designer tools now live inside Copilot Chat. MAI-Image-2 was rolling into Copilot and Bing Image Creator (3rd-party, Mar 2026). Image generation and editing in SharePoint (Sep 2026). | support "changes" article; topedia blog Mar 2026 (3rd-party); What's New Sep 2026 |
| **Clipchamp / Paint / Photos** | Not re-verified for 2026. Paint (Image Creator, Cocreator, generative erase) and Photos (relight, super resolution) features exist, but Microsoft is **scaling back Copilot branding in Paint and Photos** (3rd-party, Jan–Mar 2026). Present them as minor. | Windows Central (Jan/Mar 2026) |
| **Bing** | Copilot Search in Bing (AI answers) for consumers; Bing grounds web answers in M365 Copilot. "Microsoft Search in Bing" for work was retired in Mar 2025 and replaced by M365 Copilot Search. | learn Q&A; office365itpros (2025) |
| **Security Copilot** | **Included in M365 E5 and E7 at no extra cost** (Message Center MC1478465, 24 Sep 2026): 400 SCUs/month per 1,000 users (max 10,000), with agents in Defender, Entra, Intune and Purview. | https://mc.merill.net/message/MC1478465 (mirror of Message Center) |
| **Dynamics 365 Copilot** | Sales Agent and Service Agent are GA *inside M365 Copilot*. Service Agent GA with 70+ MCP tools (30 Jun 2026). Work IQ grounding on Dynamics data from 30 Sep 2026. | https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/06/30/service-agent-general-availability/ ; https://www.microsoft.com/en-us/dynamics-365/blog/it-professional/2026/09/25/work-iq-business-and-workplace-intelligence-in-the-flow-of-work/ |
| **Power Platform** | Copilot in Power Apps (build apps by describing them; M365 Copilot inside model-driven apps, GA) and Power Automate (agent-authored desktop flows, self-healing, calling Copilot Studio agents). | https://www.microsoft.com/en-us/power-platform/blog/power-apps/whats-new-in-power-platform-september-2026-feature-update/ |
| **Fabric / Power BI** | Copilot in Power BI. Preview of M365 Copilot inside Power BI and Fabric (Sep 2026). Fabric IQ GA in Chat and Cowork. Legacy Power BI Q&A retires Dec 2026. | https://community.fabric.microsoft.com/blog/fbc_pbiupdatesblog/power-bi-september-2026-feature-summary/5325831 |
| **Dragon Copilot** (healthcare) | Clinical AI assistant (ambient notes, from Nuance DAX and Dragon Medical One), 100k+ clinicians. HIMSS, 5 Mar 2026: M365 Copilot and Work IQ inside Dragon, partner agents, nursing and radiology workflows, 58-language capture. Price cut and single licence from 1 May 2026 (3rd-party). | https://www.microsoft.com/en-us/microsoft-cloud/blog/healthcare/2026/03/05/unify-simplify-scale-microsoft-dragon-copilot-meets-the-moment-at-himss-2026/ |
| **Microsoft Discovery** (science R&D agents) | GA 2 Jun 2026 | Build blog, 2 Jun 2026 |

### 5.1 Which models power Copilot (Oct 2026)
- **USL (flat licence) includes:** **Auto** (routes by accuracy, speed and cost), **GPT-5.6**, **Claude Sonnet 5**; **Claude Opus 5 "with limits"**. **Usage-based:** frontier models "**Fable**" (Anthropic Claude Fable 5) and "**Astra**" (OpenAI GPT-6 Astra). "Today that means OpenAI and Anthropic, with more labs and open-weight models coming soon." https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/evolution-of-the-copilot-pricing-model/4559416 (25 Sep 2026, v7 28 Sep)
- Claude timeline in M365 Copilot: Sonnet 4 / Opus 4.1 in Researcher and Copilot Studio (24 Sep 2025, https://www.microsoft.com/en-us/microsoft-365/blog/2025/09/24/expanding-model-choice-in-microsoft-365-copilot/) → Opus 4.7 (16 Apr 2026) → Opus 4.8 → Fable 5 preview (10 Jun 2026) → **Opus 5 in Word, Excel, PowerPoint, Chat, Cowork and Studio (24 Jul 2026)** https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/available-today-anthropic-claude-opus-5-in-microsoft-365-copilot/4540524
- Anthropic models are hosted outside Microsoft-managed environments, are under Anthropic's terms, and must be enabled by an admin (Researcher-with-Claude support page; Fable 5 post).
- "Switch model" / "Try again" on any response (Aug 2026, web 6 Oct 2026).
- Microsoft plans its own model for Cowork (Directions on Microsoft, 3rd-party, Sep 2026).

---

## 6. Pricing and plans (US list prices, Oct 2026)

### Work
| Plan | Price | Notes / source |
|---|---|---|
| **Microsoft 365 Copilot Chat** | **$0** with eligible M365 work plans | Web-grounded; agents pay-as-you-go. https://www.microsoft.com/en-us/copilot/pricing/business |
| **Microsoft 365 Copilot Business** (SMB, <300 users) | **$21/user/mo** (annual); promo **$18** (Jul–Dec 2026 per Microsoft FAQ); $25.20 monthly billing (3rd-party) | Add-on to Business Basic/Standard/Premium. Launched Dec 2025: https://www.microsoft.com/en-us/copilot/blog/2025/12/02/microsoft-365-copilot-business-the-future-of-work-for-small-businesses/ . Usage-based billing on by default for new CSP Copilot Business subscriptions from **1 Dec 2026** (default cap 4,000 credits/user/mo): https://learn.microsoft.com/en-us/partner-center/announcements/2026-october |
| **Microsoft 365 Copilot** (enterprise USL) | **$30/user/mo** (annual) | Unchanged since launch (Directions on Microsoft, Sep 2026; MS did not comment on future changes) |
| **Usage-based billing (Copilot Credits)** | Metered on top of the USL | Cowork, Code, Autopilot, frontier models, advanced SharePoint/OneDrive work, Work IQ API, Managed Runtime, Teams Phone Agent. Off until an admin creates a spending policy. https://learn.microsoft.com/en-us/microsoft-365/copilot/usage-based-billing-overview-copilot-credits (30 Sep 2026). Per-credit price not stated on these pages (see volatile list). |
| **Agent 365** | $15/user/mo | GA 1 May 2026 |
| **Microsoft 365 E7 "Frontier Suite"** | $99/user/mo | E5 + M365 Copilot + Agent 365 + Entra Suite. Announced 9 Mar 2026, GA 1 May 2026 (3rd-party; Agent 365 GA blog confirms E7) |

### Consumer
| Plan | Price (US) | Copilot | Source |
|---|---|---|---|
| Free (Microsoft account) | $0 | Copilot app with limited usage and limited image generation | https://www.microsoft.com/en-us/microsoft-365/buy/compare-all-microsoft-365-products |
| Microsoft 365 Personal | $9.99/mo · $99.99/yr | Copilot in apps (standard limits); owner only | same |
| Microsoft 365 Family | $12.99/mo · $129.99/yr (up to 6 people) | AI features for the **owner only** | same |
| Microsoft 365 Premium | $19.99/mo · $199.99/yr | Higher limits, **Researcher, Analyst, Cowork preview**, Browse with Copilot (Edge) | same; AI credits page |
| **Microsoft 365 Pro** (new 2026) | **$99.99/mo** (pricing page per search snippet; not re-rendered) | Highest limits, Code preview later in 2026, 5 TB | https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals ; https://support.microsoft.com/en-us/microsoft-365-copilot/copilot-in-microsoft-365-personal-family-and-premium |
| **Copilot Pro** | **Retired.** No new sales from 1 Oct 2025; existing subscriptions stopped renewing after **1 Aug 2026** (3rd-party) | Replaced by M365 Premium | aguidetocloud.com (3rd-party) |

### GitHub Copilot
Free $0 · Pro $10 · Pro+ $39 · Max $100 (individual, monthly) · Business $19/user · Enterprise $39/user. Billed in AI Credits since 1 Jun 2026 (section 4).

---

## 7. Volatile / uncertain (verify before recording)

1. **Microsoft 365 Pro price ($99.99/mo)** and how many people it can be shared with (pricing table says 6; support says AI is owner-only). The pricing page is JS-rendered and was not re-read directly.
2. **Copilot Business promo end date:** sources disagree (30 Jun, 30 Sep or 31 Dec 2026).
3. **Copilot Credit unit price** (historically ~$0.01 pay-as-you-go for Copilot Studio). Not stated on the Oct 2026 pages read.
4. **Autopilot, Code, "Today", automatic mode routing, @Copilot in Teams:** all preview or Frontier as of Oct 2026, with dates given as "coming weeks". Expect changes at **Ignite, 17–20 Nov 2026**.
5. **Vision for work accounts:** release notes (23 Sep 2026) say rolling out, but the support page (26 Jun 2026) says not for commercial customers.
6. **Mico:** removed from the main app. Its "Learn Live" continuation comes only from 3rd-party sources.
7. **Windows Copilot pullback:** mainly anonymous-source reporting (Windows Central). The exact list of removed integrations is unclear. Recall may be renamed.
8. **Model names change monthly** (GPT-5.6 Sol/Terra/Luna, GPT-6 Astra, Claude Fable 5, Opus 5.5…). Keep slides model-agnostic ("OpenAI + Anthropic + Microsoft MAI").
9. **E7 price and promotions** are mostly from 3rd-party analyses.
10. **=COPILOT()**: retired 14 Sep 2026. Any old material showing it is outdated.
11. **Facilitator auto-enable:** still per meeting (community answer).
12. **Clipchamp / Paint / Photos AI:** not re-verified for 2026.
13. **GitHub "Agent HQ"** branding was not found on the 2026 plans page. Use "third-party agents / Copilot app" instead.
14. techcommunity.microsoft.com image URLs are not listed (dynamic URLs, not checked).

---

## Visual sources

All direct image URLs below returned HTTP 200 with an image content type on 2026-10-13. YouTube thumbnails follow the standard `https://i.ytimg.com/vi/<id>/maxresdefault.jpg` pattern. Before use, check Microsoft's terms (support and blog screenshots are © Microsoft; fine for educational illustration with attribution, not for rebranding).

| # | Surface | What it shows | Page URL | Direct image URL | Type | Date |
|---|---|---|---|---|---|---|
| 1 | Copilot app (new) | Hero: Copilot logos, "The AI built for work" | https://blogs.microsoft.com/blog/2026/09/25/introducing-the-new-copilot-with-home-code-and-autopilot/ | https://blogs.microsoft.com/wp-content/uploads/2026/09/OMB-Copilot-9-25-Hero-9_22_26.png | press graphic | 25 Sep 2026 |
| 2 | Copilot app – Home | New Home page (Chat + Cowork) | same | https://blogs.microsoft.com/wp-content/uploads/2026/09/OMB-Home-FINAL-2.png | screenshot | 25 Sep 2026 |
| 3 | Copilot app – Code | Code tab | same | https://blogs.microsoft.com/wp-content/uploads/2026/09/OMB-Code-FINAL-2.png | screenshot | 25 Sep 2026 |
| 4 | Copilot app – Autopilot | Autopilot overview: "Run the supplier review", routines, plugins | same | https://blogs.microsoft.com/wp-content/uploads/2026/09/OMB-Autopilot-FINAL-scaled.png | screenshot | 25 Sep 2026 |
| 5 | Copilot app | "New Copilot" EMEA press image | https://news.microsoft.com/source/emea/2026/09/new-microsoft-copilot-brings-home-code-and-autopilot-together/ | https://news.microsoft.com/source/emea/wp-content/uploads/2026/09/New-Copilot.png | press graphic | 25 Sep 2026 |
| 6 | Cowork | Cowork dashboard | https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/ | https://www.microsoft.com/en-us/copilot/blog/wp-content/uploads/sites/2/2026/06/Copilot-Cowork-scaled.png | screenshot | 16 Jun 2026 |
| 7 | Cowork | Infographic: light / medium / heavy tasks (billing) | same | https://www.microsoft.com/en-us/copilot/blog/wp-content/uploads/sites/2/2026/06/M365-Blog_06.16.2026_Infographic-2A_R9-1024x588.webp | diagram | 16 Jun 2026 |
| 8 | Cowork (personal) | Cowork home: chat input, suggested prompts, recent tasks | https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-cowork | https://support.microsoft.com/en-us/microsoft-365-copilot/media/cowork-overview-interface.png | screenshot | 14 Sep 2026 |
| 9 | Teams – Facilitator | Facilitator moderating a live meeting | https://support.microsoft.com/en-us/teams/copilot/facilitator-in-microsoft-teams-meetings | https://support.microsoft.com/en-us/teams/media/moderator-in-teams-meeting.png | screenshot | 13 Aug 2026 |
| 10 | Teams – Facilitator | AI notes in the Recap tab | same | https://support.microsoft.com/en-us/teams/media/ai-notes-in-the-meeting-recap.png | screenshot | 13 Aug 2026 |
| 11 | Teams – Facilitator | Generating a Word doc from the meeting (9 MB) | same | https://support.microsoft.com/en-us/teams/media/facilitator-doc-generation.png | screenshot | 13 Aug 2026 |
| 12 | Teams – Recap | Full recap page | https://support.microsoft.com/office/c2e3a0fe-504f-4b2c-bf85-504938f110ef | https://support.microsoft.com/en-us/teams/media/recap-page.png | screenshot | 23 Sep 2026 |
| 13 | Teams – Recap | Topics highlighted in the recap | same | https://support.microsoft.com/en-us/teams/media/meetingrecap.png | screenshot | 23 Sep 2026 |
| 14 | Teams – Recap | Copilot in the recap | same | https://support.microsoft.com/en-us/teams/media/copilotrecap.png | screenshot | 23 Sep 2026 |
| 15 | Teams – Recap | AI-generated notes in the recap | same | https://support.microsoft.com/en-us/teams/media/recap-ai-notes.png | screenshot | 23 Sep 2026 |
| 16 | Teams – meeting | Copilot opened from the meeting chat | https://support.microsoft.com/office/0bf9dd3c-96f7-44e2-8bb8-790bedf066b1 | https://support.microsoft.com/en-us/teams/media/copilot-entry-from-meeting-chat.png | screenshot | 23 Dec 2025 |
| 17 | Teams – meeting | Copilot in the meeting recap | same | https://support.microsoft.com/en-us/teams/media/copilot-in-meeting-recap-revised.png | screenshot | 23 Dec 2025 |
| 18 | Teams – chat | Copilot in a Teams chat | https://support.microsoft.com/office/cccccca2-9dc8-49a9-ab76-b1a8ee21486c | https://support.microsoft.com/en-us/teams/media/copilot-in-teams-chat.png | screenshot | 29 Dec 2025 |
| 19 | Teams – channel | Copilot summary of a channel thread | same | https://support.microsoft.com/en-us/teams/media/thread-summary-in-teams.png | screenshot | 29 Dec 2025 |
| 20 | Excel | Copilot in Excel, Allow editing on, example prompt | https://support.microsoft.com/en-us/excel/copilot/get-started-with-copilot-in-excel | https://support.microsoft.com/en-us/excel/media/copilot-in-excel-get-started-editing-prompt.png | screenshot | 24 Sep 2026 |
| 21 | Excel | Mode menu (edit / plan / chat) | same | https://support.microsoft.com/en-us/excel/media/copilot-in-excel-modes.png | screenshot | 24 Sep 2026 |
| 22 | Excel | Finance skills, quarterly close prompt | https://www.microsoft.com/en-us/copilot/blog/ (AI at Work blog, Jun 2026 post) | https://www.microsoft.com/en-us/copilot/blog/wp-content/uploads/sites/2/2026/06/M365_Excel-Skills_6-25_3.jpg | marketing screenshot | 25 Jun 2026 |
| 23 | Word | Edit and rewrite with Copilot (selected-text menu) | https://support.microsoft.com/en-US/Word/edit-with-copilot-in-word | https://support.microsoft.com/en-us/word/copilot/media/edit-rewrite-content/edit-content-with-copilot.png | screenshot | 15 Sep 2026 |
| 24 | PowerPoint | Agent Mode chat pane | https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d | https://support.microsoft.com/en-us/powerpoint/media/agent-mode.png | screenshot | 16 Dec 2025 |
| 25 | PowerPoint | Clarifying questions | same | https://support.microsoft.com/en-us/powerpoint/media/clarifying-questions.png | screenshot | 16 Dec 2025 |
| 26 | PowerPoint | Generated presentation | same | https://support.microsoft.com/en-us/powerpoint/media/generated-presentation.png | screenshot | 16 Dec 2025 |
| 27 | PowerPoint | Allow editing UI in the Copilot pane | https://support.microsoft.com/en-us/powerpoint/edit-with-copilot-in-powerpoint | https://support.microsoft.com/en-us/powerpoint/media/allow-editing-ui-in-ppt-copilot.png | screenshot | 28 Aug 2026 |
| 28 | PowerPoint | "Visualize this slide" skill | same | https://support.microsoft.com/en-us/powerpoint/media/visualize-this-slide-skill.png | screenshot | 28 Aug 2026 |
| 29 | Outlook | Thread summary with citations (Mac) | https://support.microsoft.com/en-us/outlook/copilot-pages/summarize-an-email-thread-with-copilot-in-outlook | https://support.microsoft.com/en-us/outlook/media/email-summary-by-copilot-in-outlook-for-mac.png | screenshot | 24 Apr 2026 |
| 30 | Outlook mobile | Email summary on iOS/Android | same | https://support.microsoft.com/en-us/outlook/media/summarize-email-with-copilot-in-outlook-on-ios-and-android.png | screenshot | 24 Apr 2026 |
| 31 | Researcher | Researcher report | https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-researcher-in-microsoft-365-copilot | https://support.microsoft.com/en-us/microsoft-365-copilot/media/researcherreport.png | screenshot | 8 Sep 2026 |
| 32 | Researcher | Flowchart: how to use Researcher | same | https://support.microsoft.com/en-us/microsoft-365-copilot/media/use-researcher-flowchart.png | diagram | 8 Sep 2026 |
| 33 | Analyst | Analyst start page | https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-analyst-in-microsoft-365-copilot | https://support.microsoft.com/en-us/microsoft-365-copilot/media/analysthome.png | screenshot | 17 Dec 2025 |
| 34 | Agent Store | Agent store | https://support.microsoft.com/en-us/microsoft-365-copilot/agents-built-by-microsoft | https://support.microsoft.com/en-us/microsoft-365-copilot/media/agent-store.png | screenshot | 30 Sep 2026 |
| 35 | Agent Builder | Built-in agent templates | https://support.microsoft.com/en-us/microsoft-365-copilot/build-your-own-agent-with-microsoft-365-copilot | https://support.microsoft.com/en-us/microsoft-365-copilot/media/built-in-templates-for-agents.png | screenshot | 29 Sep 2026 |
| 36 | Copilot Pages | Chat and Pages side by side in the Copilot app | https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-pages | https://support.microsoft.com/en-us/microsoft-365-copilot/media/copilot-chat-and-copilot-pages-side-by-side.png | screenshot | 24 Sep 2026 |
| 37 | Work IQ | "What's New in Work IQ" graphic (Build) | https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/ | https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2026/06/M365_Work-IQ_full-1.jpg | press graphic | 2 Jun 2026 |
| 38 | Credits / FinOps | Copilot credits management dashboard | same | https://www.microsoft.com/en-us/copilot/blog/wp-content/uploads/sites/2/2026/06/f6e72b96-ef70-4f6f-9309-4fd95bbe1676-1024x576.webp | screenshot | 2 Jun 2026 |
| 39 | Autopilot / Scout | Microsoft Scout featured image | AI at Work blog (Jun 2026) | https://www.microsoft.com/en-us/copilot/blog/wp-content/uploads/sites/2/2026/06/Scout-featured-image.jpg | press graphic | Jun 2026 |
| 40 | Copilot Studio | Copilot Studio Home page | https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio | https://learn.microsoft.com/en-us/microsoft-copilot-studio/media/fundamentals-what-is-copilot-studio/home-page.png | screenshot | 25 Sep 2026 |
| 41 | Copilot Studio | September 2026 "What's new" banner | https://www.microsoft.com/en-us/copilot/blog/copilot-studio/new-and-improved-build-apps-extend-agents-and-transform-business-processes-in-microsoft-copilot-studio/ | https://www.microsoft.com/en-us/copilot/blog/copilot-studio/wp-content/uploads/2026/10/Copilot-Studio_Whats-new_Sep-2026_1.jpg | press graphic | 7 Oct 2026 |
| 42 | Copilot Studio | Animated: apps + workflows + agents, one system (GIF, 2.8 MB) | same | https://www.microsoft.com/en-us/copilot/blog/copilot-studio/wp-content/uploads/2045/12/One-system-for-business-processes.gif | animated screenshot | 7 Oct 2026 |
| 43 | Copilot Studio / M365 admin | Plugin registry in the admin center | same | https://www.microsoft.com/en-us/copilot/blog/copilot-studio/wp-content/uploads/2026/10/Tools-menu.webp | screenshot | 7 Oct 2026 |
| 44 | Agent 365 | Agent 365 capabilities hero | https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/ | https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2026/05/Agent-365-new-capabilities.jpg | press graphic | 1 May 2026 |
| 45 | Agent 365 | Defender agent map (AI agents + AWS) | same | https://www.microsoft.com/en-us/security/blog/wp-content/uploads/2026/05/Agent-Map-in-Defender-1024x540.webp | screenshot | 1 May 2026 |
| 46 | Edge | Copilot in Edge "Searching your history" | https://blogs.windows.com/msedgedev/2026/05/13/new-updates-to-edge-across-desktop-and-mobile/ | https://winblogs.thesourcemediaassets.com/sites/33/2026/05/History.png | screenshot | 13 May 2026 |
| 47 | Edge | New tab page with Copilot | same | https://winblogs.thesourcemediaassets.com/sites/33/2026/05/edge-Studio_NTP.png | screenshot | 13 May 2026 |
| 48 | Edge | Hero image of the May update | same | https://winblogs.thesourcemediaassets.com/sites/33/2026/05/V3.png | press graphic | 13 May 2026 |
| 49 | Windows – Click to Do | Click to Do menu with Ask Copilot | https://support.microsoft.com/en-us/windows/click-to-do-in-recall-do-more-with-what-s-on-your-screen-967304a8-32d1-4812-a904-fad59b5e6abf | https://support.microsoft.com/en-us/windows/media/ask-copilot-menu.png | screenshot | 21 May 2026 |
| 50 | Windows – Click to Do | Interacting with text on screen | same | https://support.microsoft.com/en-us/windows/media/recall-interact-with-text.png | screenshot | 21 May 2026 |
| 51 | Windows – Recall | Recall home page | https://support.microsoft.com/en-us/windows/retrace-your-steps-with-recall-aa03f8a0-a78b-4b3e-b0a1-2eb8ac48701c | https://support.microsoft.com/en-us/windows/media/recall-homepage.png | screenshot | 10 Oct 2025 |
| 52 | Windows – Recall | Recall search results | same | https://support.microsoft.com/en-us/windows/media/recall-search-1.png | screenshot | 10 Oct 2025 |
| 53 | Windows – agent in Settings | Agent in Settings feature image | https://www.microsoft.com/en-us/windows/learning-center/two-must-try-ai-tools-that-simplify-tasks | https://cdn-dynmedia-1.microsoft.com/is/image/microsoftcorp/MSFT-two-must-try-ai-tools-that-simplify-tasks-feature-image?scl=1 | marketing image | 2025–26 |
| 54 | Windows (AI PC) | "Making every Windows 11 PC an AI PC" hero | https://blogs.windows.com/windowsexperience/2025/10/16/making-every-windows-11-pc-an-ai-pc/ | https://blogs.windows.com/wp-content/uploads/sites/2/2025/10/Windows-Blog-Hero-Image_1920.jpg | press graphic | 16 Oct 2025 |
| 55 | Gaming Copilot | Gaming Copilot on ROG Xbox Ally | same | https://blogs.windows.com/wp-content/uploads/sites/2/2025/10/Gaming-Copilot-1.jpg | press photo | 16 Oct 2025 |
| 56 | Copilot Health | "Building Copilot Health" | https://microsoft.ai/news/introducing-copilot-health/ | https://microsoft.ai/wp-content/uploads/2026/03/cp.jpg | press image | 12 Mar 2026 |
| 57 | MAI models | Stage photo: "7 New Microsoft AI Models" (Build) | https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/ | https://microsoft.ai/wp-content/uploads/2026/05/Group-2147234751-2.jpg | press photo | 2 Jun 2026 |
| 58 | MAI models | Watercolor icons: Thinking / Voice / Image / Transcribe / Code | same | https://microsoft.ai/wp-content/uploads/2026/05/thinking-1.png · …/MAI_Voice-5-1.png · …/image-5.png · …/transcribe-1.png · …/code-2.png (same folder `https://microsoft.ai/wp-content/uploads/2026/05/`) | illustrations | Jun 2026 |
| 59 | GitHub Copilot app | GitHub Copilot app header (Build) | https://github.blog/news-insights/product-news/github-copilot-app-the-agent-native-desktop-experience/ | https://github.blog/wp-content/uploads/2026/06/MSFTBuild_Blog_Header_01.jpg | press graphic | 2 Jun 2026 |
| 60 | GitHub code review | Copilot code review suggestions | same | https://github.blog/wp-content/uploads/2026/06/CCRPlatform_BlogImage_01.jpg?resize=1024%2C637 | screenshot | 2 Jun 2026 |
| 61 | Dragon Copilot | Doctor talking to patient (HIMSS 2026) | https://www.microsoft.com/en-us/microsoft-cloud/blog/healthcare/2026/03/05/unify-simplify-scale-microsoft-dragon-copilot-meets-the-moment-at-himss-2026/ | https://www.microsoft.com/en-us/microsoft-cloud/blog/wp-content/uploads/2026/03/HIMSS-2.jpg | press photo | 5 Mar 2026 |

### Official videos (title, channel, upload date)
| Surface | Title | Channel | Date | URL | Thumbnail |
|---|---|---|---|---|---|
| New Copilot app | The new Copilot: where AI-powered work comes together | Microsoft Copilot | 2026-10-02 | https://www.youtube.com/watch?v=mgSFs9rkqJs | https://i.ytimg.com/vi/mgSFs9rkqJs/maxresdefault.jpg |
| Today (Home) | Meet Today in Microsoft Copilot | Microsoft Copilot | 2026-09-24 | https://www.youtube.com/watch?v=Jv-iQSZ3YVY | https://i.ytimg.com/vi/Jv-iQSZ3YVY/maxresdefault.jpg |
| Teams | Meet @Copilot in Teams | Microsoft Copilot | 2026-09-28 | https://www.youtube.com/watch?v=KVDlhOI7WGo | https://i.ytimg.com/vi/KVDlhOI7WGo/maxresdefault.jpg |
| Cowork | Meet Microsoft 365 Copilot Cowork | Microsoft Copilot | 2026-06-16 | https://www.youtube.com/watch?v=0zu9gw-USdk | https://i.ytimg.com/vi/0zu9gw-USdk/maxresdefault.jpg |
| Researcher | Microsoft 365 Copilot: Researcher with multi-model intelligence | Microsoft Copilot | 2026-03-30 | https://www.youtube.com/watch?v=G4ZqK7_15uw | https://i.ytimg.com/vi/G4ZqK7_15uw/maxresdefault.jpg |
| Researcher + Analyst | Now available in Microsoft 365 Copilot: Researcher and Analyst agents | Microsoft Copilot | 2025-06-02 | https://www.youtube.com/watch?v=xGCaKumNY04 | https://i.ytimg.com/vi/xGCaKumNY04/maxresdefault.jpg |
| Researcher + Analyst | New reasoning agents: Researcher and Analyst in Microsoft 365 Copilot | Microsoft Mechanics | 2025-04-01 | https://www.youtube.com/watch?v=5ZVDNStqUCk | https://i.ytimg.com/vi/5ZVDNStqUCk/maxresdefault.jpg |
| Facilitator | Run more focused meetings with Facilitator Agent in Microsoft Teams | Microsoft Community Learning | 2026-03-24 | https://www.youtube.com/watch?v=FAMn1KH_V8c | https://i.ytimg.com/vi/FAMn1KH_V8c/maxresdefault.jpg |
| Copilot Studio | Microsoft Copilot Studio – 2026 Release Wave 1 | Microsoft Power Platform | 2026-04-15 | https://www.youtube.com/watch?v=es3ozt12dqs | https://i.ytimg.com/vi/es3ozt12dqs/maxresdefault.jpg |
| Edge | Get answers based on the context of your open tabs | Microsoft Edge | 2026-05-05 | https://www.youtube.com/watch?v=Q9itnNYyhGc | https://i.ytimg.com/vi/Q9itnNYyhGc/maxresdefault.jpg |
| Edge | Pickup where you left off with Journeys | Microsoft Edge | 2026-05-05 | https://www.youtube.com/watch?v=it6NFi4PO30 | https://i.ytimg.com/vi/it6NFi4PO30/maxresdefault.jpg |
| Edge | Get your day started with the redesigned new tab page | Microsoft Edge | 2026-05-04 | https://www.youtube.com/watch?v=S7CT_HiWFys | https://i.ytimg.com/vi/S7CT_HiWFys/maxresdefault.jpg |
| Edge | Study smarter with Copilot in Edge | Windows | 2026-04-10 | https://www.youtube.com/watch?v=4j3chZtjQvc | https://i.ytimg.com/vi/4j3chZtjQvc/maxresdefault.jpg |
| Windows | Ask Copilot in taskbar | Windows | 2025-10-15 | https://www.youtube.com/watch?v=ZYlYZWxci-Y | https://i.ytimg.com/vi/ZYlYZWxci-Y/maxresdefault.jpg |
| Windows | Copilot Actions on Windows | Windows | 2025-10-15 | https://www.youtube.com/watch?v=syJ0LiRJkC4 | https://i.ytimg.com/vi/syJ0LiRJkC4/maxresdefault.jpg |
| Windows | Copilot connectors on Windows | Windows | 2025-10-15 | https://www.youtube.com/watch?v=oPOCU2D0HSk | https://i.ytimg.com/vi/oPOCU2D0HSk/maxresdefault.jpg |
| GitHub | How to ship from issue to merge with the GitHub Copilot app – demo | GitHub | 2026-06-02 | https://www.youtube.com/watch?v=mv6MMQ2j128 | https://i.ytimg.com/vi/mv6MMQ2j128/maxresdefault.jpg |
| GitHub | How to run GitHub Copilot in local and cloud sandboxes – demo | GitHub | 2026-06-03 | https://www.youtube.com/watch?v=J8laUDXs08c | https://i.ytimg.com/vi/J8laUDXs08c/maxresdefault.jpg |
| Teams (community, not official) | How to Use Copilot in Microsoft Teams Meetings – 5 Powerful Features (2026) | Mike Tholfsen (Microsoft PM, personal channel) | 2026-07-20 | https://www.youtube.com/watch?v=l0nh1sYtY5A | https://i.ytimg.com/vi/l0nh1sYtY5A/maxresdefault.jpg |

Other image sources to browse:
- Microsoft support media folders (pattern `https://support.microsoft.com/en-us/<product>/media/<file>.png`) cover nearly every Copilot feature. Open a support article and use the img src.
- AI at Work blog index (lots of 2026 hero images): https://www.microsoft.com/en-us/copilot/blog/
- Microsoft Adoption, Copilot Scenario Library and release notes: https://adoption.microsoft.com/en-us/release-notes/ (not image-checked here).
- Microsoft 365 Roadmap: https://www.microsoft.com/en-us/microsoft-365/roadmap

### Helper scripts
`tools/imgs.py` (extracts and checks img/og:image/YouTube links from a page), `tools/yt.py` (YouTube title, channel, date) and `tools/txt2.py` (text of JS-heavy techcommunity posts) are in the same scratchpad folder, for re-checking before recording.
