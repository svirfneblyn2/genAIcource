# Research Brief — Lesson 07: GitHub, Microsoft 365 and Windows Copilot (state as of 2026-10-13)

Method: two independent passes on 2026-10-13. Pass 1 (research notes): pages read through WebFetch (a small model summarises each page, so figures are "as summarised"). Pass 2 (verification): the key claims re-opened by a second reader who did not use the first notes. **Where the two disagree, the verification wins.** Each item carries one tag:

- **[V]** confirmed in the verification pass.
- **[C]** corrected by the verification pass (the first notes were wrong or misleading; the text below is the corrected one).
- **[U]** UNVERIFIED: not confirmed on a primary page. Kept off the slides, or flagged in the speaker notes.
- **[S]** seen only in one pass or in a search snippet; treat as a pointer, not a fact.

Prices are US prices in USD. Model names are not taught (they change monthly).

The old Drive package (`07 — GitHub, Microsoft 365 and Windows Copilot Ecosystem — DONE`, Sep 2026) was an enterprise-governance lecture built on a licensed Microsoft 365 tenant and an organisation GitHub account. Its facts about plans, Recall and policy were re-checked here; the governance vocabulary is dropped (see `L07_09_Lesson_Plan_v2.md`, sections A and G).

---

## 0. TL;DR for the lesson designer

- **GitHub billing changed on 2026-06-01** [V]: "premium requests" were replaced by **GitHub AI Credits** (1 credit = $0.01, stated on the plans-page FAQ). A **Max** plan ($100) exists [V]. A separate free **Copilot Student** plan exists [V].
- **Free is limited** [V, C]: 2,000 completions a month, "limited chat and agent usage", CLI and agent mode included, **cloud agent not included**. The Free plan's AI-credit allowance has no published number [V]. A chat-request number appears only in a legacy-looking FAQ line, contradicts the pricing table, and is **not taught anywhere**.
- **Training on your data** [V]: since 2026-04-24 GitHub may use Free, Pro, Pro+ and Max interaction data unless the user sets "Allow GitHub to use my data for AI model training" to Disabled. Business and Enterprise are excluded.
- **Microsoft renamed** [V names, U date]: "Microsoft 365 Copilot" is now "Microsoft Copilot", "Microsoft 365 Copilot Chat" is now "Microsoft Copilot Chat". Labels still mix old and new names. The date of the rename is not officially stated.
- **Recall** [C]: not "GA on 2025-04-25". Correct: **rolled out gradually since April 2025 (Copilot+ PCs), off by default (opt-in)**, still labelled preview in the April 2025 post.
- **Free for students and learners:** GitHub Copilot Free, Copilot Student (verified students), Copilot Chat (web, Edge, Windows app), Microsoft Copilot Chat with a work account (included, web and what you open). That is enough for the homework.

## Corrections log (first notes → verified)

| # | First notes said | Verdict | Use this |
|---|---|---|---|
| 1 | 1 credit = $0.01 "from a secondary source" | **[V]** | Stated on the plans-page FAQ: "1 AI credit = $0.01 USD." Not on the changelog or the billing docs page. |
| 2 | Free: 2,000 completions and a fixed number of chat requests | **[C]** | 2,000 completions [V]. Say "limited chat and agent usage". The chat number is legacy FAQ wording; never print it. No Free credit number is published. |
| 3 | "coding agent" was renamed "cloud agent" | **[U]** | The name now is "Copilot cloud agent" [V]. Do not state a former name as fact. |
| 4 | "You can assign tasks to Copilot, Claude or Codex agents" | **[C]** | Third-party agents are **Preview** and only on **Pro+ and Max** (not Free, not Pro). |
| 5 | Chat modes ask / edit / agent | **[C]** | **Agent** and **Plan** [V]. Ask and Edit not confirmed as current; check live VS Code before naming them. |
| 6 | Rename of Microsoft Copilot products, with a date | **[C]** | Names [V]. Date [U]: no official dated announcement; secondary sources say mid-Aug 2026 (mobile, web) and mid-Sep 2026 (Windows, Mac), unconfirmed. |
| 7 | Researcher and Analyst only on Premium and Pro (consumer) | **[U]** by name | Say "advanced research and analytics agents": listed for Premium (limited) and Pro (highest), not for Personal and Family. |
| 8 | **Recall GA on 2025-04-25** | **WRONG** | "Rolled out gradually since April 2025, off by default." The 2025-04-25 post still says "(preview)" and "gradually rolling out ... controlled feature rollout". No page states a GA date. |
| 9 | Recall and Click to Do in the EEA in 2026 | **[U]** | Only 2025 promises ("later in 2025, timing varies"). No 2026 status page found. |
| 10 | Copilot key and Win+C | **[V]**, two behaviours | Commercial: lightweight prompt box, expandable. Consumer: full app or "quick view", configurable. Key is remappable. |
| 11 | "Hey Copilot" and Vision | **[V]** exist, **[U]** 2026 availability and regions | Opt-in wake word. Commercial: Frontier program from end of 2025. No current regional statement. |

---

## 1. GitHub Copilot: plans, prices, limits

- Individual plans: **Free $0, Pro $10/month, Pro+ $39/month, Max $100/month** [V] — [GitHub Copilot plans](https://github.com/features/copilot/plans), [Docs: Plans](https://docs.github.com/en/copilot/get-started/plans) (checked 2026-10-13)
- **Free:** 2,000 inline completions a month [V]; "limited chat and agent usage" per the pricing table [V]; includes Copilot CLI and agent mode [V]; automatic model selection only; **cloud agent not included** [V]; chat skills in IDEs not available on Free. The Free AI-credit allowance has no published number [V]. The plans-page FAQ has an older chat-request line that conflicts with the table [C]: do not quote it — [plans page](https://github.com/features/copilot/plans), [Docs: Plans](https://docs.github.com/en/copilot/get-started/plans) (checked 2026-10-13)
- **Copilot Student:** its own free plan for verified students; automatic model selection only; no third-party agents [V] — [Docs: Plans](https://docs.github.com/en/copilot/get-started/plans) (checked 2026-10-13)
- Verified teachers and maintainers of popular open-source projects "may be eligible" for free Copilot Pro [V] — [Docs: Plans](https://docs.github.com/en/copilot/get-started/plans) (checked 2026-10-13)
- **Business $19** per granted seat/month (1,900 AI credits per user); **Enterprise $39** per granted seat/month (3,900 credits); Enterprise needs GitHub Enterprise Cloud and is not available for GitHub Enterprise Server [V] — [Docs: Plans](https://docs.github.com/en/copilot/get-started/plans) (checked 2026-10-13)
- Included credits: Pro 1,500 (1,000 base + 500 flex), Pro+ 7,000 (3,900 + 3,100), Max 20,000 (10,000 + 10,000) [V] — [Docs: Plans](https://docs.github.com/en/copilot/get-started/plans) (checked 2026-10-13)
- **Billing change:** from 2026-06-01 all plans moved to usage-based billing; premium request units were replaced by GitHub AI Credits, metered by input, output and cached tokens at each model's API rate [V] — [GitHub changelog 2026-04-27](https://github.blog/changelog/2026/04/27/github-copilot-is-moving-to-usage-based-billing/) (checked 2026-10-13)
- **1 AI credit = $0.01** [V, from the plans-page FAQ] — so Pro's 1,500 credits = $15 of usage; Pro+ 7,000 = $70 — [plans page](https://github.com/features/copilot/plans) (checked 2026-10-13)
- Code completions and next edit suggestions remain included and do not use credits [S: changelog only] — [GitHub changelog 2026-04-27](https://github.blog/changelog/2026/04/27/github-copilot-is-moving-to-usage-based-billing/) (checked 2026-10-13)
- The old low-cost-model fallback after running out of allowance was discontinued; admins set budgets (enterprise, cost centre, user) [S] — same changelog (checked 2026-10-13)
- Legacy "premium requests" still apply only to Pro/Pro+ **annual** subscribers who stayed on legacy billing: Pro 300/month, Pro+ 1,500/month, extra requests $0.04 each [V]; code review costs a fixed 13 premium requests per review from 2026-06-01 [S] — [Docs: premium requests](https://docs.github.com/en/copilot/concepts/billing/copilot-requests) (checked 2026-10-13)
- Annual Pro/Pro+ keep premium-request pricing until expiry, then move to Free (or upgrade to monthly) [S] — [GitHub changelog 2026-04-27](https://github.blog/changelog/2026/04/27/github-copilot-is-moving-to-usage-based-billing/) (checked 2026-10-13)
- Business/Enterprise promo extra usage June–August 2026 ($30 / $70 per month) has expired; do not teach it as current [S] — same changelog (checked 2026-10-13)
- Copilot code review also consumes GitHub Actions minutes in addition to AI credits [S] — same changelog (checked 2026-10-13)

## 2. GitHub Copilot: surfaces, modes, names, IDEs

- Surfaces named on the product page: GitHub Copilot app (desktop), Copilot in VS Code, "Agents on GitHub", Copilot CLI, Copilot Code Review, Copilot Spaces — [GitHub Copilot features](https://github.com/features/copilot) (checked 2026-10-13)
- Official name of the issue-to-PR agent: **"Copilot cloud agent"** [V]; it can "research a repository, plan changes, and implement them in the background", from an issue or pull request, one PR per task. **The former name "coding agent" is [U]**: the page has no rename note; do not state it — [About Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent) (checked 2026-10-13)
- Cloud agent: not on Free; included in Student and paid plans [V] — [Docs: Plans](https://docs.github.com/en/copilot/get-started/plans) (checked 2026-10-13)
- **Third-party agents** (Claude by Anthropic, OpenAI Codex): **Preview, Pro+ and Max only** [C] — [plans page](https://github.com/features/copilot/plans) (checked 2026-10-13)
- **Copilot CLI is available on all plans including Free** [V] ("All plans include Copilot CLI and Copilot app"); it uses AI credits — [Docs: Plans](https://docs.github.com/en/copilot/get-started/plans) (checked 2026-10-13)
- **Chat modes in VS Code:** **Agent** and **Plan** are confirmed ("You can ask Agent to propose an approach before editing"; "Select Plan, where available") [V]. **Ask and Edit are [U]**; the plans FAQ still says "Copilot Edits". Teach "agent"; look at live VS Code before naming other modes — [VS Code: agents overview](https://code.visualstudio.com/docs/copilot/agents/overview) (checked 2026-10-13)
- Code review: runs on pull requests on github.com (not in VS Code or other IDEs); off by default for organisations; unlicensed users' usage is billed as AI credits [S] — [GitHub Copilot features](https://github.com/features/copilot) (checked 2026-10-13)
- Copilot Spaces: shared source of truth from docs and repo context for teams [S] — [GitHub Copilot features](https://github.com/features/copilot) (checked 2026-10-13)
- GitHub Mobile supports all Copilot plans [S] — same page (checked 2026-10-13)
- IDEs listed: VS Code, Visual Studio, JetBrains IDEs, Xcode, Neovim, Eclipse (Raycast also listed) [S] — same page (checked 2026-10-13)
- Docs describe inline suggestions, chat Q&A, agentic work, code review, custom agents — [Docs: Copilot features](https://docs.github.com/en/copilot/get-started/features) (checked 2026-10-13)

## 3. GitHub Copilot: model choice

- Selectable model families: OpenAI (GPT), Anthropic (Claude), Google (Gemini), Microsoft (MAI-Code), Moonshot AI (Kimi), xAI (Grok) [S] — [Supported AI models in Copilot](https://docs.github.com/en/copilot/reference/ai-models/supported-models) (checked 2026-10-13)
- "Auto" model selection draws from a per-client list; Free and Student are auto-only; paid plans choose models [V for Free] — [Supported models](https://docs.github.com/en/copilot/reference/ai-models/supported-models), [Plans](https://docs.github.com/en/copilot/get-started/plans) (checked 2026-10-13)
- Model names change often. Do not hard-code model names in slides — [plans page](https://github.com/features/copilot/plans) (checked 2026-10-13)

## 4. GitHub Copilot: customisation (slide 13)

- Repo-wide instructions: `.github/copilot-instructions.md` — [Add repository instructions](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions) (checked 2026-10-13)
- Path-specific: `.github/instructions/NAME.instructions.md` with an `applyTo` glob in the frontmatter — same source (checked 2026-10-13)
- `AGENTS.md` is supported anywhere in the repo (nearest wins); a single `CLAUDE.md` or `GEMINI.md` in the root also works — same source (checked 2026-10-13)
- Agent skills: code review reads skills from the head branch; the exact path is [U] (so is `.github/prompts/*.prompt.md`). The features page lists "agent skills" and "custom agents" — [Copilot features](https://docs.github.com/en/copilot/get-started/features) (checked 2026-10-13)
- MCP: docs mention "MCP servers from other providers" as supported. In the course this is L12 — [Copilot features](https://docs.github.com/en/copilot/get-started/features) (checked 2026-10-13)

## 5. GitHub Copilot: policies and data (slide 19)

- "GitHub does not use Copilot Business or Copilot Enterprise customer data to train AI models" [V] — [Manage Copilot policies](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies), [GitHub Copilot features](https://github.com/features/copilot) (checked 2026-10-13)
- **Since 2026-04-24** GitHub may use interactions (inputs, outputs, snippets, context) of **Free, Pro, Pro+ and Max** users for model training unless they set **"Allow GitHub to use my data for AI model training" to Disabled** in their personal Copilot settings [V] — [Manage Copilot policies](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies) (checked 2026-10-13)
- "Suggestions matching public code": Allow or Block; Block checks each suggestion plus about 150 characters of context against public GitHub code; Allow shows match details and source links [S] — [Manage Copilot policies](https://docs.github.com/en/copilot/how-tos/manage-your-account/manage-policies) (checked 2026-10-13)
- Content exclusion: Business and Enterprise only; does not apply in VS Code edit and agent modes; public preview on github.com and GitHub Mobile [S] — [Content exclusion](https://docs.github.com/en/copilot/concepts/context/content-exclusion) (checked 2026-10-13)

## 6. Microsoft: Copilot Chat vs licence, consumer plans (slides 6–8)

- **RENAME** [V names, U date]: "Microsoft 365 Copilot is now named Microsoft Copilot, and Microsoft 365 Copilot Chat is now named Microsoft Copilot Chat. Some experiences, licenses, and capabilities might continue to reference Microsoft 365 Copilot." Learn also says "The Microsoft 365 Copilot app is now called Microsoft Copilot." No official dated announcement was found. Secondary sources (LinkedIn, news; not official) say mid-Aug 2026 (mobile, web) and mid-Sep 2026 (Windows, Mac): unconfirmed. Earlier, on 2025-01-15, the Office app was renamed "Microsoft 365 Copilot" app — [Enterprise data protection (Learn)](https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection), [License options (Learn)](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing) (checked 2026-10-13)
- **Copilot Chat** is included at no extra cost with an eligible Microsoft 365 subscription, signed in with a Microsoft Entra work account: "Using Copilot Chat doesn't require a Microsoft 365 Copilot license"; the web scope is free; grounded in the web plus content you upload or open (limited organisation grounding in Outlook); **no Graph or Work IQ grounding** [V] — [Overview of Copilot Chat](https://learn.microsoft.com/en-us/copilot/overview), [Manage Windows Copilot](https://learn.microsoft.com/en-us/windows/client-management/manage-windows-copilot) (checked 2026-10-13)
- Microsoft 365 Copilot (Basic) = no add-on licence but standard access to Copilot in Word, Excel, PowerPoint, OneNote; web data only [S] — [What is Microsoft Copilot?](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview) (checked 2026-10-13)
- Microsoft 365 Copilot (Premium) = add-on licence: priority access, grounding in Microsoft Graph, Work IQ, semantic indexing, Copilot Search, advanced agents [S] — same source (checked 2026-10-13)
- Apps with Copilot: Word, Excel, PowerPoint, Outlook, OneNote, Teams, Forms [S] — same source (checked 2026-10-13)
- **Licence prices** per user/month, **paid yearly** [V]: Business **$23.50**, Enterprise **$30.00**. Business needs Business Basic/Standard/Premium/Apps for Business/Teams Essentials; Microsoft 365 E7 includes Copilot [S]. The microsoft.com business pricing page returned 503; the price came from the main Copilot page — [Microsoft Copilot](https://www.microsoft.com/microsoft-365-copilot), [License options (Learn)](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing) (checked 2026-10-13)
- **Consumer** [V]: Personal $9.99/mo ($99.99/yr); Family $12.99/mo ($129.99/yr; AI for the owner only); Premium $19.99/mo ($199.99/yr); Pro $99.99/mo, **monthly billing only** — [Copilot pricing for individuals](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals) (checked 2026-10-13)
- Consumer AI limits are relative levels (standard / extensive); benefits cannot be shared; Cowork preview US and Canada only [S]. The pricing page does not name Researcher or Analyst: say "advanced research and analytics agents", limited on Premium, highest on Pro, not listed for Personal and Family [U by name] — [AI credits and limits (support)](https://support.microsoft.com/en-us/office/ai-credits-and-limits-for-microsoft-365-personal-family-and-premium-68530f1a-4459-4d02-9818-8233c1f673b8) (checked 2026-10-13)
- Personal and Family "60 AI credits a month" came from a search summary only; the support page gave levels, no numbers. **[U]**, not taught.

## 7. Agents (not covered in the lesson; for questions)

- Agent Builder: declarative agents from natural language, at microsoft365.com/chat, office.com/chat and Teams desktop and web; not on mobile; actions and connectors need Copilot Studio; skills in Agent Builder are Frontier preview [S] — [Agent Builder overview](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder) (checked 2026-10-13)
- Copilot Studio: low-code agent tool, licensed separately, does not need a Copilot licence [S] — [What is Microsoft Copilot?](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview) (checked 2026-10-13)
- Copilot Chat includes declarative agents grounded in instructions and public sites; work-data agents are pay-as-you-go [S] — same source (checked 2026-10-13)
- Researcher and Analyst: GA announced 2025-06-02 for licensed users [S: search result, page not opened] — [Microsoft 365 blog](https://www.microsoft.com/en-us/microsoft-365/blog/2025/06/02/researcher-and-analyst-are-now-generally-available-in-microsoft-365-copilot/)
- Autopilot (cloud personal agent) is Private Preview; Code is in Frontier [S] — [Microsoft Copilot](https://www.microsoft.com/microsoft-365-copilot) (checked 2026-10-13)

## 8. Microsoft: data protection (slide 19, one line)

- Prompts and responses are covered by the DPA and Product Terms, Microsoft as data processor [S] — [Enterprise data protection (Learn)](https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection) (checked 2026-10-13)
- "Your data isn't used to train foundation models": prompts, responses and Graph data [S] — same source (checked 2026-10-13)
- Applies when signed in with an Entra work or school account, for Copilot Chat and licensed Copilot [S] — [What is Microsoft Copilot?](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-overview) (checked 2026-10-13)
- Web queries go to Bing, handled separately, not used to train LLMs; the EU Data Boundary does not cover web queries, and Anthropic models are currently excluded from it [S] — [Enterprise data protection (Learn)](https://learn.microsoft.com/en-us/copilot/microsoft-365/enterprise-data-protection) (checked 2026-10-13)

## 9. Windows: Microsoft Copilot app (slide 16)

- Consumer app features: **Copilot Vision** ("can see browser windows or apps you have open on your screen and then answer questions or help you do something step by step"), voice, opt-in "Hey, Copilot", file search (docx, xlsx, pptx, txt, pdf, json; OneDrive synced), screenshots, links in a side pane [V]. Vision exists in the consumer app; **regional availability is [U]** — [Copilot on Windows (support)](https://support.microsoft.com/en-us/topic/copilot-on-windows-1159c61f-86c3-4755-bf83-7fbff7e0982d) (checked 2026-10-13)
- "Hey Copilot" is an opt-in wake word [V]. For commercial users it comes through the Frontier program (from the end of 2025); **current availability in 2026 is [U]** — [Manage Windows Copilot](https://learn.microsoft.com/en-us/windows/client-management/manage-windows-copilot) (checked 2026-10-13)
- Copilot Actions began Insider rollout on 2025-11-17 as experimental, working on local files in an Agent Workspace [S: search result]; **2026 status [U]** — [Windows Insider blog](https://blogs.windows.com/windows-insider/2025/11/17/copilot-on-windows-copilot-actions-begins-rolling-out-to-windows-insiders/)
- The consumer app does not support Entra sign-in; **work accounts are redirected to m365.cloud.microsoft/chat** [V] — [Manage Windows Copilot](https://learn.microsoft.com/en-us/windows/client-management/manage-windows-copilot) (checked 2026-10-13)

## 10. Copilot+ PC and Recall (one line in the lesson, slide 16 notes)

- A **40+ TOPS NPU** is required for many AI features [V] — [Copilot+ PCs developer guide](https://learn.microsoft.com/en-us/windows/ai/npu-devices/) (checked 2026-10-13)
- **Recall** needs a Copilot+ PC meeting Secured-core, **16 GB RAM, 256 GB storage, at least 50 GB free** to enable, BitLocker or Device Encryption, Windows Hello ESS [V]. "To use Recall you need to opt in to saving snapshots" — **off by default** [V]; removed by default on managed work and school devices [S]; optimised for English, Chinese (Simplified), French, German, Japanese, Spanish [S] — [Recall (support)](https://support.microsoft.com/windows/retrace-your-steps-with-recall-aa03f8a0-a78b-4b3e-b0a1-2eb8ac48701c) (checked 2026-10-13)
- **Recall rollout [C]:** *Rolled out gradually since April 2025, off by default.* The first notes said "GA on 2025-04-25". That is **wrong**: the 2025-04-25 Windows blog still labels Recall "(preview)" and says the features are "gradually rolling out ... via controlled feature rollout (CFR) to consumers". No page states a GA date — [Windows Experience blog 2025-04-25](https://blogs.windows.com/windowsexperience/2025/04/25/copilot-pcs-are-the-most-performant-windows-pcs-ever-built-now-with-more-ai-features-that-empower-you-every-day/); [Recall overview (Learn)](https://learn.microsoft.com/en-us/windows/apps/develop/windows-integration/recall/)
- Click to Do: acts on text and images on screen; availability varies by device, region and language [S] — [Copilot+ PCs](https://www.microsoft.com/en-us/windows/copilot-plus-pcs) (checked 2026-10-13)
- **EEA in 2026 [U]:** Recall reached the EEA in 2025 (KB5062660, 2025-07-22 preview notes; seen via a search snippet only). Click to Do in the EEA lacks some actions (snippet only). Original promise: "Recall and Click to Do will be coming to European Economic Area later in 2025; timing varies." No 2026 status page found — [KB5062660](https://support.microsoft.com/en-gb/servicing/os/windows-11/2025/07/july-22-2025-kb5062660-os-build-26100-4770-preview)
- Improved Windows search has limited formats and the same six languages [S]; Copilot+ experiences "vary by device and market" [S] — [Copilot+ PCs](https://www.microsoft.com/en-us/windows/copilot-plus-pcs)

## 11. Copilot key (slide 16)

- **Two behaviours** [V]. Commercial: "pressing the Copilot key (or Win+C for users without a Copilot key) now opens a lightweight prompt box", expandable to the full app; a short press then the voice icon, a long press opens the voice controller. Consumer: the shortcut "can either launch the full application or just a smaller 'quick view'" (a setting in the app). Remappable in Settings → Personalization → Text input → Customize Copilot key (Search, Custom or an app) — [Manage Windows Copilot](https://learn.microsoft.com/en-us/windows/client-management/manage-windows-copilot), [Copilot on Windows (support)](https://support.microsoft.com/en-us/topic/copilot-on-windows-1159c61f-86c3-4755-bf83-7fbff7e0982d) (checked 2026-10-13)
- Some devices use the key in place of Right Ctrl or the Menu key; a Windows remap setting was announced "later this year" with no date [S] — [Copilot key updates](https://support.microsoft.com/en-us/accessibility/windows/copilot/understand-updates-to-the-copilot-key-on-windows-devices) (checked 2026-10-13)

## 12. Notable 2026 changes (do not get wrong)

- GitHub: usage-based billing since 2026-06-01 ("AI credits", not "premium requests") [V]; Max plan $100 [V]; Copilot Student plan [V]; data-training default for individuals since 2026-04-24 [V].
- Microsoft: "Microsoft 365 Copilot" → "Microsoft Copilot", "Microsoft 365 Copilot Chat" → "Microsoft Copilot Chat" [V names]; Copilot URL copilot.cloud.microsoft [S]; in-product "Basic / Premium" labels [S] — [License options (Learn)](https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing)
- The legacy "Turn Off Windows Copilot" policy is subject to near-term deprecation; use AppLocker [S] — [Manage Windows Copilot](https://learn.microsoft.com/en-us/windows/client-management/manage-windows-copilot)

## Prices (US, USD, checked 2026-10-13)

| Product | Price | Source |
|---|---|---|
| GitHub Copilot Free | $0 (2,000 completions; limited chat and agent usage) | [plans](https://github.com/features/copilot/plans) |
| GitHub Copilot Student | free for verified students | [docs](https://docs.github.com/en/copilot/get-started/plans) |
| GitHub Copilot Pro | $10/month (1,500 credits) | [docs](https://docs.github.com/en/copilot/get-started/plans) |
| GitHub Copilot Pro+ | $39/month (7,000 credits) | [docs](https://docs.github.com/en/copilot/get-started/plans) |
| GitHub Copilot Max | $100/month (20,000 credits) | [docs](https://docs.github.com/en/copilot/get-started/plans) |
| GitHub Copilot Business | $19/seat/month (1,900 credits) | [docs](https://docs.github.com/en/copilot/get-started/plans) |
| GitHub Copilot Enterprise | $39/seat/month (3,900 credits) | [docs](https://docs.github.com/en/copilot/get-started/plans) |
| Extra GitHub usage | $0.01 per AI credit [V]; legacy $0.04 per premium request | [plans FAQ](https://github.com/features/copilot/plans), [docs](https://docs.github.com/en/copilot/concepts/billing/copilot-requests) |
| Microsoft Copilot Chat (work) | included with eligible Microsoft 365, no extra cost | [Learn](https://learn.microsoft.com/en-us/copilot/overview) |
| Microsoft Copilot (Business) | $23.50/user/month, paid yearly | [MS](https://www.microsoft.com/microsoft-365-copilot) |
| Microsoft Copilot (Enterprise) | $30.00/user/month, paid yearly | [MS](https://www.microsoft.com/microsoft-365-copilot) |
| Microsoft 365 Personal | $9.99/mo, $99.99/yr | [MS](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals) |
| Microsoft 365 Family | $12.99/mo, $129.99/yr | [MS](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals) |
| Microsoft 365 Premium | $19.99/mo, $199.99/yr | [MS](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals) |
| Microsoft 365 Pro (consumer) | $99.99/mo, monthly billing only | [MS](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/individuals) |

The "Individuals $9.99" on the Copilot page equals the Personal plan price; it was not confirmed to be a separate product. Only slide 8 shows prices.

## Volatile — recheck before class

Recheck within 24 hours of class (open the page, compare, fix `build.py` slide 8 or the speaker note):
- GitHub plan names, prices, credit allotments, what Free includes, the Max plan, Copilot Student terms (change monthly).
- Model list and names (not taught; do not name them in answers).
- Data-training default and the exact wording and path of "Allow GitHub to use my data for AI model training".
- Whether the cloud agent, code review and third-party agents are available on the plan you demo with.
- VS Code mode names (Agent, Plan; Ask and Edit unverified) and the Copilot extension UI.
- Microsoft rename status (old and new names coexist), Basic / Premium labels, the Business price ($23.50) and any promo end date.
- Consumer plan prices and AI limits, Cowork region (US and Canada preview).
- Copilot key behaviour, Vision, "Hey Copilot" and Copilot Actions status and regions; the key-remap update.
- Recall and Click to Do availability, including the EEA.
- Frontier and Private Preview items (Autopilot, Code, Agent Builder skills).

## Could not verify

- The Free plan's AI-credit amount (docs say "an allowance", no number).
- Official names "ask / edit mode" for Copilot Chat in IDEs; the name "next edit suggestions" (only in the billing changelog); the exact path for agent skills and prompt files.
- Whether "coding agent" was renamed "cloud agent" (docs use "cloud agent", no rename note).
- The date of the Microsoft Copilot rename (no official dated announcement).
- Researcher and Analyst by name on consumer plans; availability beyond the 2025 GA.
- Personal and Family "60 AI credits a month".
- Vision regional availability; "Hey Copilot" availability in 2026; Copilot Actions status in 2026.
- Recall and Click to Do in the EEA in 2026.
- Microsoft Copilot business pricing pages (503); third-party blogs report other SMB promos, not used.
- Copilot Spaces and GitHub Mobile details beyond a one-line description.

## Tool limits of this research

All quotes are WebFetch-model outputs. The plans documentation page is 215k characters; about 200k were read. Search-result-only items are marked [S].
