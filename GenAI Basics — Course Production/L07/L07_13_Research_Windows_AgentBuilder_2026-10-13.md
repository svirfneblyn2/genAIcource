# Copilot on Windows (free consumer) + Agent Builder + Copilot APIs: state as of 13 Oct 2026

This file extends `research_ms_ecosystem.md` and does not repeat what it already covers (unified app, pricing, Hey Copilot, Recall basics, Click to Do EEA note, Edge). Compiled 2026-10-13.
"ms.date" is the Microsoft Learn metadata date. Many support.microsoft.com pages show only "© Microsoft 2026" and no article date; these are marked "(no date, live 13 Oct 2026)". "(3rd-party)" marks non-Microsoft sources.

> **Naming change, important for the slides.** Learn now says: *"Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat."* The primary URL is `copilot.cloud.microsoft`. https://learn.microsoft.com/en-us/copilot/manage (ms.date 12 Oct 2026). Agent Builder docs still use the old name "Microsoft 365 Copilot".

---

## A. Copilot on Windows 11 and the free consumer Copilot app (personal Microsoft account)

### A1. What it can do

| Feature | What it does | Free personal account? | Copilot+ PC only? | Region notes | Source (date) |
|---|---|---|---|---|---|
| Chat | Questions, writing, web answers | Yes. Signing in adds "chat history, image creation, longer conversations, and voice interactions". | No. Any Windows 11 PC. | 170+ markets (prior file) | https://support.microsoft.com/en-us/topic/getting-started-with-copilot-on-windows-1159c61f-86c3-4755-bf83-7fbff7e0982d (no date, live 13 Oct 2026) |
| Launch | Copilot key, **Win + C** (full app or "quick view"; set in Account > Settings > Copilot Keyboard Shortcuts), pen button | Yes | No | – | same |
| "Hey, Copilot" | Opt-in wake word | Yes | No | – | same page; details in prior file |
| Voice | Spoken conversation | Yes, when signed in (limits below) | No | – | same |
| **Vision** | Share a window or desktop (Windows/web) or the camera (mobile) **during a voice chat**. Copilot can highlight things but "won't click, type, or scroll". Each session is independent. | **Unclear.** The Vision page lists eligibility as "a Microsoft 365 Personal, Family, or Premium subscription and a personal Microsoft account". The AI-credits page lists Vision as "Standard usage" for Personal/Family. No free tier is listed. | No | "availability might vary while features roll out" | https://support.microsoft.com/en-us/microsoft-copilot/using-copilot-vision-with-microsoft-copilot (no date, live 13 Oct 2026) |
| Screenshots | Share all or part of the screen from the Composer **+** menu | Yes | No | – | getting-started page |
| Image generation and editing | Creates images in chat | Yes, with limits (see A2) | No | – | https://support.microsoft.com/en-us/microsoft-365-copilot/what-is-microsoft-copilot-app (no date) |
| Create Word/Excel/PowerPoint files | "Creating images and Word, Excel, and PowerPoint files" is listed as an app feature | Yes (listed for the personal experience) | No | – | same |
| **File upload** | **Up to 20 files per conversation, up to 50 MB per file.** Formats: PDF, DOCX, XLSX, PPTX · PNG, JPEG, PJP, JFIF · TXT, TEXT, JSON, CSV, MD. Files are kept "no longer than 18 months". Applies to "All Microsoft Copilot experiences", including personal accounts. | Yes | No | – | https://support.microsoft.com/en-us/microsoft-365-copilot/file-upload-in-microsoft-copilot (no date, live 13 Oct 2026) |
| **File search (local files)** | "Finds, opens, and answers questions about files", including synced OneDrive files. Lists .docx, .xlsx, .pptx, .txt, .pdf, .json; "supports most file types". | Yes | No (semantic search is better on Copilot+ PCs) | – | getting-started page |
| Web pages in a side pane | Links open in a side pane. With permission, Copilot can use the tabs opened in that conversation. | Yes | No | – | same |
| Settings help (in Copilot) | Points you to the right Windows setting from a plain-language request | Yes | No | – | same |
| **Agent in Settings** (Settings search box) | Describe a change in words; the agent can apply it | Yes (OS feature) | **Yes, Copilot+ PC** ("Available now on Copilot+ PCs") | 10 languages: zh-Hans, en, fr, de, hi, it, ja, ko, pt, es. All countries except China (support page). | https://www.microsoft.com/windows/windows-11-specifications ; https://support.microsoft.com/en-us/windows/experience/exploring-windows-settings ; languages expanded in KB5074105 (29 Jan 2026) |
| Click to Do | AI actions on what is on screen | Yes. "Subscription required for some actions." | **Yes, Copilot+ PC** | "varies by device, region, language". The Ask Copilot action is not in the EEA (prior file). | Windows 11 specs page |
| Recall (preview) | Searchable snapshots | Yes | **Yes, Copilot+ PC**. Needs Windows Hello Enhanced Sign-in Security. | Optimized for en, zh-Hans, fr, de, ja, es | Windows 11 specs page; defaults in prior file (opt-in, off by default) |
| Improved Windows search | Semantic search over local files | Yes | **Yes, Copilot+ PC** | Same 6 languages | Windows 11 specs page |
| **Copilot Actions on Windows** | Agent that does multi-step tasks in a separate **agent workspace**. It can request access to 6 known folders (Documents, Downloads, Desktop, Music, Pictures, Videos), with per-agent "Allow Always / Ask every time / Never allow" (default: ask). | **Still preview.** Windows Insiders only, via Copilot Labs. Enable it in Settings > System > AI Components > Experimental agentic features (off by default; admin only; applies to all users on the device). | Not stated | Insider rollout was "worldwide, excluding EEA" (Insider blog, 17 Nov 2025) | https://support.microsoft.com/en-us/windows/ai/ai-features/experimental-agentic-features (updated 5 Dec 2025); https://blogs.windows.com/windows-insider/2025/11/17/copilot-on-windows-copilot-actions-begins-rolling-out-to-windows-insiders/ |
| **Ask Copilot / Copilot in taskbar Search** | **Oct 2026 announcement:** (1) "Actions in Windows Search": thousands of taskbar actions such as dark mode, Do Not Disturb or arranging windows, rolling out to Windows Insiders (experimental channel) from 7 Oct 2026. (2) The new Copilot in taskbar Search for inline answers: **opt-in, "select markets later this year"**. | – | No | Select markets | https://blogs.windows.com/windowsexperience/2026/10/07/building-windows-for-hybrid-intelligence/ (7 Oct 2026) |
| **Hybrid intelligence** (coming) | Copilot+ PCs get **local context** (your files and recent activity, with permission), **local actions** (organize files, diagnostics, troubleshooting), on-device models, plus Home, Code and Autopilot on the PC | Not stated | **Yes, Copilot+ PC** | "may vary by device, market, and silicon". **"Coming months".** | same blog |

> Teaching line: on a normal Windows 11 PC the free Copilot app gives you chat, voice, image creation, file upload and file search. The "agentic" Windows features (agent in Settings, Click to Do, Recall, and the coming local actions) need a Copilot+ PC, and Copilot Actions is still an Insider preview.

### A2. Limits on the free tier and what subscriptions raise

**Microsoft publishes almost no hard numbers for the consumer tier in Oct 2026.**

| Limit | Value | Status / source |
|---|---|---|
| Files per conversation | **20** | Official: file-upload page |
| File size | **50 MB per file** | Official: file-upload page |
| File retention | ≤ **18 months** | Official |
| Conversation history retention | **18 months** by default | Official: https://support.microsoft.com/en-us/topic/privacy-faq-for-microsoft-copilot-27b3a435-8dc9-4b55-9a4b-58eeb9647a7f |
| Daily or monthly chat cap | **Not published.** Microsoft dropped fixed daily chat quotas in 2025. | Unverified / not stated |
| Prompt length (characters) | **Not published.** Forum reports range from 8,000 to 128,000. | Unverified |
| Image generations ("boosts") | **Not published for 2026.** 3rd-party sources say about 15 fast "boosts" (per day or per week; they disagree), then slower generation. | Unverified (3rd-party) |
| Voice minutes | **Not published.** Old 2024 reports said about 30 min/day. A 2025 statement said voice and Think Deeper were "free and unlimited" with priority for subscribers (heise, Feb 2025). | Unverified |
| Think Deeper / reasoning | Not published for free users | Unverified |

**What Microsoft 365 subscriptions raise.** "AI credits and limits for Microsoft 365 subscriptions" (support, **"Last updated: October 2026"**): https://support.microsoft.com/en-us/microsoft-365-copilot/ai-credits-and-limits-for-microsoft-365-subscriptions
The page gives **relative tiers only, no numbers**. It covers 4 plans; the free tier is not in the table.

| Feature | Personal | Family | Premium | Pro |
|---|---|---|---|---|
| Chat | Extensive | Extensive | Extensive | Extensive |
| Deep reasoning | Extensive | Extensive | Extensive | Extensive |
| Pages | Extensive | Extensive | Extensive | Extensive |
| Audio Overview | Standard | Standard | Extensive | Extensive |
| Voice | Standard | Standard | More | Highest |
| Vision | Standard | Standard | More | Highest |
| Image gen | Standard | Standard | Extensive | Extensive |
| Researcher | – | – | Extensive | Extensive |
| Analyst | – | – | Extensive | Extensive |
| Cowork (preview, US and Canada only) | – | – | Extensive | Extensive |
| Priority access | Yes | Yes | Yes | Yes |

The page also says: AI credits are "monthly allotments" shared across Microsoft 365 and Windows apps, but it doesn't give their size. AI benefits are **owner-only** and can't be shared. Limits "may change based on the feature, entry point, system conditions". You can check usage under account.microsoft.com > "Services & subscriptions".

### A3. Integrations

- **Connectors (personal):** Microsoft OneDrive, Outlook.com (email, calendar, contacts), Google Drive, Google Gmail, Calendar and Contacts. "You can turn on as many connectors as you want". Turn them on via Profile > Connectors > Connect, then toggle per conversation. On copilot.com use **+ > Use connectors**. Copilot does not store a separate copy of your data. **Account rule:** the Microsoft account you sign in with must match the one used for OneDrive/Outlook. **Eligibility line:** "Personal Microsoft accounts - Microsoft 365 Personal, Family, Premium, Pro", so whether free accounts get connectors is unclear. **Platforms:** "currently available on Copilot.com and on Copilot Mobile (iOS and Android)". The Windows app is not listed, although the Oct 2025 Windows video "Copilot connectors on Windows" showed it. https://support.microsoft.com/en-us/microsoft-copilot/connecting-microsoft-copilot-to-other-services (no date, live 13 Oct 2026)
- **Export / document creation:** create Word, Excel, PowerPoint or PDF from chat ("Export this to a Word document"). An **Export** button appears on responses of about 600+ characters (Windows Insider rollout, Oct 2025; 3rd-party write-ups of the Insider blog). The unified app page lists "Creating … Word, Excel, and PowerPoint files" as a core feature.
- **Pages, memory, Edge:** see the prior file. The memory controls are in A4 below.
- **Sign-in options:** Microsoft Account, Apple ID or Google Account (desktop, web and mobile). https://support.microsoft.com/en-us/microsoft-365-copilot/what-is-microsoft-copilot-app
- **Office in Copilot for personal accounts:** not confirmed on a support page (unverified).
- **Opening and acting on apps:** Vision only guides you and takes no actions. Copilot Actions (Insider) can act inside apps in the agent workspace. Local actions on Copilot+ PCs are "coming months".

### A4. Privacy settings (personal accounts)

Source: "Microsoft Copilot privacy controls" https://support.microsoft.com/en-us/topic/microsoft-copilot-privacy-controls-8e479f27-6eb6-48c5-8d6a-c134062e2be6 and "Privacy FAQ for Microsoft Copilot" (both: no date, both reference the updated app "as of August 18, 2026"; the controls page says it covers the *older* app version, so the menus may move).

- **Model training toggles:** **"Training on conversation activity"** and **"Training on voice conversations"**. On copilot.com: profile icon > profile name > **Privacy**. On Windows/macOS: profile icon > **Settings > Privacy**. On mobile: menu > profile > **Account > Privacy**.
- **Default:** training is **on by default** for eligible consumers ("Except for certain categories of users or users who have opted out…"). Opting out excludes **future** conversations.
- **Never trained on:** Entra (work/school) users, Microsoft 365 Personal/Family subscribers, users who aren't signed in, signed-in users under 18, users who opted out, and users in **Brazil, China (excl. Hong Kong), Israel, Nigeria, South Korea and Vietnam**. *(The EEA is not named in the current FAQ text.)*
- **Opting out does not affect** other product improvement, ads, safety or compliance uses.
- **Memory:** **"Personalization and memory"** is **on by default** where available. Find it under profile > **Memory**, with **"Delete all Memory"** (this does not delete conversation history). You can also ask Copilot to forget something specific. Turning personalization off makes Copilot forget its memories.
- **Other toggles:** "Microsoft usage data", "See ads that interest you" (account.microsoft.com/privacy/ad-settings).
- **Recall:** opt-in, off by default, encrypted, Windows Hello (prior file). It also requires Enhanced Sign-in Security (Windows 11 specs page).

---

## B. Agent Builder (Microsoft 365 Copilot / Copilot Chat) and Copilot Studio

### B1. What an agent is, where it lives, who can build one

- **Definition:** Agent Builder builds **declarative agents**, meaning Copilot plus **instructions + knowledge + capabilities** (and skills, in preview). Agent Builder **"doesn't support authoring actions that integrate external services"**; for those, *copy the agent to Copilot Studio*. https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder (ms.date 30 Sep 2026, updated 12 Oct 2026)
- **Where:** in the Copilot app left pane under **Agents > New agent**, at microsoft365.com/chat, office.com/chat (now copilot.cloud.microsoft), and in Teams desktop and web. **Not on mobile.** The Microsoft Mechanics and Tholfsen videos (Sep 2026) show it at `copilot.cloud.microsoft/agents/new`. Admins can turn Agent Builder off.
- **Personal Microsoft accounts:** **no official evidence that consumers can build agents.** The support page says "availability can vary by account type and license". All Agent Builder docs are tenant-based (Entra). Treat it as a work/school feature (unverified for consumers).
- **Copilot Chat without an M365 Copilot licence (e.g. a university A1/A3 tenant):** **yes, users can build and use agents, with limited knowledge.** Learn: "Copilot Chat users have access to agents that extend its capabilities and can be grounded on instructions or the web." The FAQ adds: "If you have a Microsoft 365 subscription, you can build and test agents in Microsoft 365 Copilot Chat, with limited capabilities." https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/prerequisites (ms.date 30 Sep 2026). *Caveat:* the same page says users without an add-on licence "might see Copilot Chat entry points… access is limited or disabled depending on tenant configuration". The tenant admin decides.
- **Education eligibility:** Copilot Chat is included in **Microsoft 365 A5/A3/A1** and Office 365 A1 / A1 Plus. **Students 13+** can use it once the admin takes extra steps. https://learn.microsoft.com/en-us/copilot/manage (ms.date 12 Oct 2026)

**Capability by licence** (Learn prerequisites, ms.date 30 Sep 2026):

| Capability | Copilot Chat (no PAYG) | Copilot Chat + pay-as-you-go (Copilot Credits) | M365 Copilot licence |
|---|---|---|---|
| Custom instructions | ✅ | ✅ | ✅ |
| Code interpreter | ✅ | ✅ | ✅ |
| Image generator | ✅ | ✅ | ✅ |
| Web search / scoped web search (public sites) | ✅ | ✅ | ✅ |
| Custom actions, MCP Apps | ✅ | ✅ | ✅ |
| Copilot connectors | ❌ | ✅ (metered) | ✅ |
| SharePoint data | ❌ | ✅ (metered) | ✅ |
| **Embedded (uploaded) files** | ❌ | ✅ (metered) | ✅ |
| Dataverse | ❌ | ✅ | ✅ |
| Email, People, Teams messages, Teams meetings | ❌ | ❌ | ✅ |

"Usage limits apply to all included features." With PAYG, "agents grounded in public data or instructions are free to use"; agents grounded in tenant data are billed in Copilot Credits. PAYG needs an Azure subscription and a billing policy in the M365 admin center.

> Classroom implication: a student in a typical A1/A3 tenant **can build an agent with instructions + public websites + code interpreter + image generator**, but **can't upload files or use SharePoint** unless the university enabled pay-as-you-go or bought licences.

### B2. Step by step

Sources: "Build agents in Agent Builder" https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-build-agents (ms.date 30 Sep 2026); "Add knowledge" https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge (30 Sep 2026); "Share and manage" https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-share-manage-agents (30 Sep 2026, updated 12 Oct 2026); support "Build your own agent" https://support.microsoft.com/en-us/microsoft-365-copilot/build-your-own-agent-with-microsoft-365-copilot.

**UI labels drift (important).** The Learn docs say **Describe / Configure / Try it**. The **Sep 2026 UI in both videos** shows a start page titled **"Build your own specialist agent"** with the chat box "Message Agent Builder", **Skip →**, and tabs **Templates | My agents**. After that comes a split view: the Agent Builder chat on the left, and on the right a header toggle **Configure | Preview** (plus **Monitor** after creation) with **Create** / **Update** buttons. The "Try it" tab is now labelled **Preview**.

1. **Open it:** Copilot app > **Agents > New agent**.
2. **Option A, describe (recommended):** type what the agent should do in "Message Agent Builder". Use **+** to add knowledge (Add work content / Upload images and files / Attach cloud files). Agent Builder drafts the **name, description, instructions** (with guidelines, steps, error handling and examples), knowledge and suggested prompts, and it can suggest refinements ("Review my agent and suggest improvements", "Undo last change").
3. **Option B, configure manually:** **Skip to configure** (now "Skip →"). Fields:
   - **Name**: max **30 characters**
   - **Icon**: Generate, Browse or Upload. PNG, 192×192, **≤ 1 MB**
   - **Model** (default response mode): **Auto** (default) / **Quick response** / **Think deeper**
   - **Description**: max **1,000 characters**
   - **Instructions**: max **8,000 characters**
   - **Knowledge** (see limits below), plus toggles **Search all websites**, **Only use specified sources** (prioritizes your sources but cannot fully block general knowledge) and **Reference people in organization** (licensed users)
   - **Capabilities**: **Create documents, charts, and code** (code interpreter) and **Create images** (image generator)
   - **Starter / Suggested prompts**: title + message, "no minimum number"
   - **Skills** (preview, **Frontier Program only**)
4. **Option C, start from a template** (see B3) and then refine.
5. **Test** in **Try it / Preview**. It is enabled once the agent has a name, description and instructions. **New chat** resets the conversation. Sharing prompts, feedback and @mentions don't work in the test pane.
6. **Create.** A dialog says "Your agent was created successfully! This agent is currently **private** and only available to you", with **Share** / **Start chat** buttons. Later edits autosave but only go live after **Update**.
7. **Share:** the **Share** dialog > "Add a name, group, or email". Roles are **Can edit** (owner; groups cannot be owners) and **Can chat**. "Send notification" is optional. Options: **Copy chat link**, **Edit link**, and the toggle **"Org-wide sharing for chat access"** (makes the agent visible in the Agent Store). Admins may restrict sharing to All users / Specific users or groups / No users. You can also **Submit to your org catalog** (admin approval, shown under "Built by your org"), or **Download .zip file** to sideload into Teams. About-this-agent "Short description" is max 80 characters.
8. **Limitations:** agents built in Agent Builder **can't be used in Teams group or 1:1 chats**. Customer Managed Keys are not supported. Delete is permanent.

**Knowledge limits per agent** (Learn "Add knowledge", 30 Sep 2026):

| Source | Limit |
|---|---|
| Public website URLs | **4 URLs**, max **two path levels**, no query parameters |
| SharePoint files, folders, sites | **100 files** |
| SharePoint lists | **1 list** (≤ 20,000 rows and 50 MB of text) |
| OneDrive files | **50 files** |
| Teams | **5 chats and 5 meetings** (or "My Teams chats and meetings") |
| **Uploaded (embedded) files** | **20 files** (no folders) |
| Email | All of "My emails" (it can't be scoped) |
| Copilot connectors, Dynamics/Power Apps | No documented number; admin must enable |
| **Embedded file sizes** | .doc/.docx/.pdf/.ppt/.pptx/.txt: **512 MB**; .xls/.xlsx: **30 MB**; .html only via SharePoint |

Files that are password-protected or carry some sensitivity labels fail. Anyone who can use the agent can see answers grounded in its embedded files.

### B3. Templates (Learn, ms.date 30 Sep 2026: 21 templates)

https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-templates-overview
AI Learning Advisor · **Career Coach** · Corporate Communications Crafter · **Customer Insight Assistant** · Executive Briefing Agent · **Idea Coach** · Interview Question Assistant · **Learning Coach** · Meeting Coach · My Company Policy · Personal News Digest · Plan My Day · Project Delta Digest · **Prompt Coach** · **Quiz Tutor** · Request for Proposal Generator · Scrum Assistant · SME Finder · Status Update Agent · **Text Translator** · **Writing Coach**.
The Sep 2026 start page shows 3 cards (Plan My Day, Project Delta Digest, Executive Briefing Agent) and a "View all" link (Tholfsen video, 00:50). Note that templates such as Plan My Day and Personal News Digest depend on M365 data (email/Teams), so they need a licence to work fully.

**Example agents for students and small teams.** Each one works on **free Copilot Chat knowledge** (instructions + public web), unless marked otherwise.

1. **Course Study Buddy** (knowledge: course website URL, up to 4 URLs; code interpreter on)
   *Instructions:* "You are a study tutor for the course 'Intro to GenAI'. Explain concepts at beginner level, then check understanding with one short question. Use only the course site for facts about deadlines and grading, and say 'I don't know – check the syllabus' if it isn't there. Never write graded homework for the student; give hints and worked examples on similar problems instead. End each answer with a 3-bullet summary."
   *Starter prompts:* "Explain RAG like I'm new", "Quiz me on week 3", "Make a 7-day revision plan".
2. **Quiz Tutor / Flashcard maker** (from the Quiz Tutor template)
   "Create 5 multiple-choice questions on the topic the user gives, one at a time. Wait for the answer, say why it is right or wrong, track the score, and at the end list the weak topics to review."
3. **Writing Coach for reports** (template)
   "Give feedback on clarity, structure, grammar and tone. Don't rewrite the whole text: quote the sentence, explain the issue, and suggest one improved version. Use our style rules: active voice, short sentences, define every acronym."
4. **Team Meeting Notes → Action Items** (for a small team; uses Teams meetings knowledge, so it **needs an M365 Copilot licence**)
   "From the selected meetings, list decisions, owners and due dates in a table, then draft a short follow-up email. If an owner or date is missing, flag it instead of guessing."
5. **Prompt Coach** (template)
   "Analyse the user's prompt with the GCSE checklist (Goal, Context, Source, Expectations). Score it 1–5, explain the missing pieces, and return an improved prompt."
6. **Data Helper** (code interpreter; upload a CSV in chat, or as embedded knowledge if PAYG/licence)
   "When the user shares a table, describe it first (columns, rows, missing values), then answer with a chart and 3 plain-language insights. Show the formula or steps you used."

### B4. Copilot Studio: when to move up

- **Move up when** you need actions or workflows that call external services, connectors (Power Platform/premium), publishing to channels beyond Copilot/Teams (website, etc.), strict "only my sources" control, autonomous triggers, evaluations, multi-agent setups or your own models. Agent Builder has **"Copy to Copilot Studio"** in the agent's "..." menu (Tholfsen video 08:20; Learn "copy-agent-to-copilot-studio").
- **Studio free trial:** "You can sign up for Copilot Studio as an individual". You can build and test in the test chat, but **"you can't publish the agent"**. You can extend once **by 30 days**, and agents keep working **90 days** after expiry. **A work or school account is needed** (personal emails are rejected), and admins can disable self-service sign-up. The **trial length isn't stated** on the page. https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing-subscriptions (ms.date 3 Aug 2026)
- **Students:** no student or developer offer is listed on the Studio pricing page. The **Microsoft 365 Developer Program** sandbox is limited to Visual Studio Pro/Enterprise subscribers, ISV Success, eligible partners and Premier/Unified customers (Learn prerequisites, 30 Sep 2026). The Copilot Studio for Teams plan **excludes EDU A1**.
- **Pricing:** capacity pack **$200/month for 25,000 Copilot Credits**; pay-as-you-go via Azure (third-party sources say $0.01/credit; the Microsoft page links to Azure pricing without giving the number); up to 20% off with Commit Units. New Azure accounts get $200 credit. https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio (live 13 Oct 2026)

### B5. Videos (YouTube; checked 13 Oct 2026 with yt-dlp)

| Rank | Title | Channel | Upload | Length | Views | URL |
|---|---|---|---|---|---|---|
| 1 (downloaded) | Create agents fast with Agent Builder in Copilot | **Microsoft Mechanics** (presenter: Ned Friend, Group PM, Copilot Agent Builder) | 2026-09-22 | 9:34 | 22k | https://www.youtube.com/watch?v=dlS2meHJWAk |
| 2 (downloaded) | How to Use the NEW Agent Builder in Microsoft Copilot - Build an AI Agent in Minutes (2026) | Mike Tholfsen (Microsoft PM, personal channel) | 2026-09-28 | 10:27 | 88k | https://www.youtube.com/watch?v=knOhSmOkqMM |
| 3 | Microsoft Copilot Agent Builder Just Got WAY Better | Shane Young | 2026-10-05 | 21:44 | 22k | https://www.youtube.com/watch?v=2CEKxAttNic |
| 4 | Learn to Build Your Own Custom Agent - Agent Builder (2026) | M365 Copilot Connection | 2026-10-08 | 16:17 | 2.6k | https://www.youtube.com/watch?v=Q2SJaGDL7jk |
| 5 | The EASIEST Way to Build a Copilot Agent (NEW Agent Builder Tutorial) | Collaboration Simplified | 2026-02-28 | 14:30 | 211k | https://www.youtube.com/watch?v=9_Dw9qcjLgA (older UI) |
| alt | Build and Use Agents in Microsoft 365 Copilot: Complete Tutorial (2026) | Lisa Crosbie | 2026-02-09 | 56:28 | 118k | https://www.youtube.com/watch?v=4yQDmJ1n-dU (older UI) |

Both downloaded videos show the **current Sep 2026 UI** (Skills section, Configure/Preview/Monitor). Videos from before Sep 2026 show the older Describe/Configure layout.

---

## C. Can we query Copilot programmatically?

There is **no public API for the free consumer Copilot** (copilot.com / the Windows app). Microsoft documents none, and third-party "Copilot APIs" are scraping. For work accounts, the **Microsoft 365 Copilot APIs** live under Microsoft Graph (`graph.microsoft.com/v1.0|beta/copilot`): the **Retrieval API** (RAG over SharePoint/OneDrive/connectors; GA), the **Chat API (preview**, text answers only, no actions), the **Search API (preview)**, Meeting Insights, Interaction Export and change notifications, usage reports and package management. All of them **require a Microsoft 365 Copilot licence per user** plus E3/E5 or equivalent. ("The Microsoft Graph APIs are available under standard Microsoft 365 license terms; the Copilot APIs require a Microsoft 365 Copilot license.") https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-apis-overview (ms.date 6 Aug 2026). The one exception is that the Retrieval API has a **pay-as-you-go preview** for unlicensed users, for tenant sources (SharePoint, connectors) only; it needs at least one Copilot licence in the tenant. https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/api/ai-services/retrieval/paygo-retrieval . The **Work IQ APIs** (GA 16 Jun 2026) are billed in Copilot Credits (prior file). **For developers who just want the same models:** use **Microsoft Foundry** (formerly Azure AI Foundry), which serves Azure OpenAI GPT models, Anthropic Claude models and Microsoft's **MAI** models. MAI-Thinking-1 is in **Foundry preview since Aug 2026** (sources disagree on public vs private), with a Chat Completions-compatible endpoint, 256k context (3rd-party: scalevise.com, mer.vin). MAI-Image-2.5, MAI-Voice-2 and MAI-Transcribe-1.5 are also in Foundry (microsoft.ai, 2 Jun 2026, prior file). These are pay-per-token Azure services with an Azure subscription, not a Copilot subscription.

---

## Unverified / volatile

1. **Free-tier numbers:** daily chat cap, prompt character limit, image "boosts" (about 15, daily or weekly?), voice minutes, Think Deeper limits. **None are published by Microsoft in Oct 2026.**
2. **Size of "AI credits"** for Personal/Family/Premium/Pro: the page gives tiers, not numbers.
3. **Vision on a free personal account:** the support page lists only M365 Personal/Family/Premium. Confirm in a live free account.
4. **Connectors on a free account and in the Windows app:** the support page lists M365 subscribers and copilot.com/mobile only.
5. **Agent Builder for personal (consumer) accounts:** no evidence. Treat it as work/school only.
6. **Copilot Studio trial length** (not stated; historically 30 or 60 days).
7. **Copilot Actions on Windows** GA date: still an Insider preview (support page last updated Dec 2025).
8. **Export button threshold (~600 characters):** from 3rd-party write-ups of the Oct 2025 Insider post.
9. **EEA:** model-training defaults and the availability of Ask Copilot/Copilot Actions in the EEA are not stated on current pages.
10. **UI labels:** Learn says "Try it", "Skip to configure" and a Describe tab, while the Sep 2026 UI shows "Preview", "Skip →" and "Build your own specialist agent". Expect more changes at Ignite (17–20 Nov 2026).
11. **Privacy controls page** says it describes the older (pre-18 Aug 2026) app. Menu paths may differ in the unified app.
12. **MAI-Thinking-1** preview tier and price (3rd-party claims $2 per 1M input tokens).

---

## Frames and screenshots

### YouTube picks (1920×1080, in `scratchpad/yt/picks/`)

| File | What it shows | Video title | Channel | Date | URL with timestamp |
|---|---|---|---|---|---|
| agentbuilder__knOhSmOkqMM__00-50.png | **Start page** inside the Copilot app (Chat/Cowork, Agents in the left nav): "Build your own specialist agent", Message Agent Builder box, **Templates / My agents**, Plan My Day / Project Delta Digest / Executive Briefing cards (yellow cursor highlight on the left) | How to Use the NEW Agent Builder in Microsoft Copilot… (2026) | Mike Tholfsen | 2026-09-28 | https://www.youtube.com/watch?v=knOhSmOkqMM&t=50s |
| agentbuilder__dlS2meHJWAk__03-08.png | **Describe step:** a natural-language agent description with two knowledge chips attached (Expense Submission doc + SharePoint site). Clean, full screen. | Create agents fast with Agent Builder in Copilot | Microsoft Mechanics | 2026-09-22 | https://www.youtube.com/watch?v=dlS2meHJWAk&t=188s |
| agentbuilder__dlS2meHJWAk__03-58.png | **Configure view:** generated "New Staff Guide" agent with name, description, **Instructions** (Role, Operating Guidelines) and Skills (Preview); chat on the left says "Reasoning completed in 7 steps" | same | Microsoft Mechanics | 2026-09-22 | https://www.youtube.com/watch?v=dlS2meHJWAk&t=238s |
| agentbuilder__dlS2meHJWAk__05-08.png | **Knowledge section:** Cloud files (SharePoint: CaldovaOnboarding) on, Outlook, Teams, Copilot connectors, Web search toggles, Attachments | same | Microsoft Mechanics | 2026-09-22 | https://www.youtube.com/watch?v=dlS2meHJWAk&t=308s |
| agentbuilder__knOhSmOkqMM__06-45.png | **Preview (test) pane:** the finished "New Staff Onboarding" agent with icon, description and 5 starter-prompt cards; Configure/Preview toggle; Create button | Tholfsen video | Mike Tholfsen | 2026-09-28 | https://www.youtube.com/watch?v=knOhSmOkqMM&t=405s |
| agentbuilder__knOhSmOkqMM__06-50.png | **Test answer** in Preview: Week 1 onboarding plan table with citations | same | Mike Tholfsen | 2026-09-28 | https://www.youtube.com/watch?v=knOhSmOkqMM&t=410s |
| agentbuilder__dlS2meHJWAk__07-10.png | **Created:** "Your agent was created successfully! This agent is currently private…" with Share / Start chat | Mechanics video | Microsoft Mechanics | 2026-09-22 | https://www.youtube.com/watch?v=dlS2meHJWAk&t=430s |
| agentbuilder__knOhSmOkqMM__08-00.png | **Share:** Add people dialog with **Can chat** role and Send notification (Configure / Preview / **Monitor** tabs visible) | Tholfsen video | Mike Tholfsen | 2026-09-28 | https://www.youtube.com/watch?v=knOhSmOkqMM&t=480s |

Other useful frames in `yt/frames/agentbuilder_knOhSmOkqMM/`: 00-40 (Agents store with the "New agent" tile), 02-00 (Add content picker), 06-20 (icon Generate/Browse/Upload), 08-20 ("..." menu with Copy to Copilot Studio / Download zip), 09-40 (Monitor tab analytics). All frames and contact sheets are in `yt/frames/agentbuilder_<id>/` (`_sheet_*.jpg` = scene detection, `_pa_*.jpg` = periodic).

### Official Microsoft screenshots (in `scratchpad/ms/`, all HTTP 200 image/png on 2026-10-13)

Learn base: `https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/assets/images/agent-builder-screenshots/<name>.png`. Support base: `https://support.microsoft.com/en-us/microsoft-365-copilot/media/<name>.png`.

| File | What it shows | Page (date) |
|---|---|---|
| ab_new-agent-screen.png (1367×690) | Older New Agent screen: "What can I take off your hands today?" and **Skip to configure** | agent-builder overview (30 Sep 2026) |
| ab_agent-configuration.png (710×1303, tall) | Full Configure tab of a "Learning Coach": instructions, knowledge, capabilities, suggested prompts | build-agents (30 Sep 2026) |
| ab_agent-builder-template.png (1406×1255) | Idea Coach template in Configure (instructions, Work content toggles, suggested prompts) | build-agents |
| ab_add-knowledge-agent-builder-describe.png (450×328) | The **+** menu: Add work content / Upload images and files / Attach cloud files | add-knowledge (30 Sep 2026) |
| ab_agent-builder-knowledge-configure.png (743×414) | Knowledge: URL/drop box, Search all websites, Only use specified sources, Reference org chart toggles | add-knowledge |
| ab_web-search-enter-link.png (934×713) | New Knowledge UI: Cloud files / Outlook / Teams / Copilot connectors / Web search with "Enter a link" | add-knowledge |
| ab_embedded-authoring-copilot-connectors.png (1311×583) | "Choose other data sources": Azure DevOps, Confluence, GitHub connectors | add-knowledge |
| ab_share-agent-new.png (942×580) | Share dialog: Org-wide sharing toggle, Can edit / Can chat, Copy chat link | share-manage (12 Oct 2026) |
| ab_add-people-panel.png (958×400) | Add people panel, Can chat, Send notification | share-manage |
| ab_role-dropdown.png (474×291) | Role dropdown: Can chat / Can edit / Remove | share-manage |
| ab_agent-builder-view-agents.png (1321×448) | My agents list (Email Summarizer, Prompt Coach, Idea Coach) and View all agents | share-manage |
| ab_support_built-in-templates-for-agents.png (430×433) | Template list: Career Coach, Customer Insights Assistant, Idea Coach, Interview Questions Assistant, Learning Coach | support "Build your own agent" (no date) |
| ab_support_starter-prompts-for-agent.png (420×442) | Prompt Coach starter prompts in the test pane | same |

Scripts: `tools/scenes_ab.py` (scene detection + contact sheets) and `tools/periodic_ab.py` (frames every N seconds).
