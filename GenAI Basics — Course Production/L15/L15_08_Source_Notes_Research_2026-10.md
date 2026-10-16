# L15 Source Notes: Responsible AI, Security and Regulation (research 2026-10-16)

Primary sources checked on 2026-10-16 for the v2 rebuild. Each fact below is marked VERIFIED (primary source read), SECONDARY (law firms / press only) or UNVERIFIED. Replaces the September 2026 Drive package source notes.

## Images used in the deck

None. The risk map, the data traffic light, the incident chains and the EU AI Act timeline are drawn in HTML by `deck_v2/build.py` (the generated traffic-light and risk-map images were dropped: English labels in the RU deck and wrong placement).

The deck is an overview for beginners, not legal advice.

---


All items were checked on 2026-10-16 unless noted. "VERIFIED" means a primary or official source was read directly. "SECONDARY" means law-firm, press or tracker coverage only. "UNVERIFIED" means it was not confirmed and should not go on a slide as fact.

---

## 0. What changed since the old package (checked 8 Sep 2026)

- The old Source Notes are still **correct** on the AI Act dates (2 Aug 2026 general application, Annex III on 2 Dec 2027, Annex I on 2 Aug 2028, Art. 50 grace period to 2 Dec 2026). Keep them.
- **Add:** the AI Omnibus is Regulation (EU) **2026/1744**. It also adds a **new prohibition** (AI that generates non-consensual intimate imagery or CSAM, from **2 Dec 2026**) and **softens Art. 4 AI literacy**.
- **Add:** concrete OWASP lists, including the new **Agentic Top 10 (Dec 2025)**. Also add non-EU regulation (UZ, KZ, RU, US, UK, CN) and real incident cases. The old deck has none of these.

---

## 1. EU AI Act (Regulation (EU) 2024/1689)

| Date | What applies | Status |
|---|---|---|
| 1 Aug 2024 | Entered into force | VERIFIED |
| 2 Feb 2025 | Prohibited practices (Art. 5) + AI literacy (Art. 4) | VERIFIED |
| 2 Aug 2025 | Governance rules + general-purpose AI (GPAI) model obligations | VERIFIED |
| 2 Aug 2026 | General application, including **Art. 50 transparency**. AI Office enforcement powers over GPAI begin. | VERIFIED |
| 2 Dec 2026 | (a) Grace-period end for Art. 50(2) machine-readable marking, only for generative systems placed on the market **before** 2 Aug 2026 (per the text of Regulation 2026/1744; some law firms, e.g. CMS, give 2 Feb 2027 — the deck notes say so). (b) New ban on AI systems that generate non-consensual intimate imagery or CSAM ("nudification" apps). | VERIFIED |
| 2 Dec 2027 | High-risk rules, Annex III (biometrics, education, employment, migration, credit, etc.). Originally 2 Aug 2026. | VERIFIED |
| 2 Aug 2028 | High-risk AI embedded in regulated products (Annex I: toys, lifts, medical devices, etc.). Originally 2 Aug 2027. | VERIFIED |

Sources:
- https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai (Commission timeline, including the Omnibus dates and the December 2026 nudification ban)
- Consolidated text: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

**Digital Omnibus on AI ("AI Omnibus") timeline**
- Commission proposal: 19 Nov 2025.
- Political agreement: 7 May 2026.
- EP plenary: 16 Jun 2026.
- Published as **Regulation (EU) 2026/1744**, dated 8 Jul 2026, in the OJ on **24 Jul 2026**. In force **27 Jul 2026**.
- Status: VERIFIED for the number, OJ date and entry into force (EUR-Lex listing plus Commission page).
- Sources: https://eur-lex.europa.eu/eli/reg/2026/1744/oj (CELEX 32026R1744) · https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force

**Other Omnibus changes worth one line**
- **Art. 4 AI literacy is softened.** Providers and deployers must now "take measures to support the development of AI literacy". The text says this "does not require … to guarantee any specific level". The Commission and Member States "support and facilitate".
  - Source: https://artificialintelligenceact.eu/article/4/ (shows the amended text) · Sidley summary https://datamatters.sidley.com/2026/06/22/eu-lawmakers-reach-provisional-agreement-to-delay-key-eu-ai-act-obligations/
  - Status: SECONDARY. The amended wording was read on an unofficial consolidated site. Confirm against EUR-Lex before quoting.
- SME relief extended to "small mid-caps". Regulatory sandboxes deadline moved to 2 Aug 2027. Status: SECONDARY.

**Art. 50 transparency, plain language** (VERIFIED, Commission FAQ https://digital-strategy.ec.europa.eu/en/faqs/transparency-obligations-under-article-50-ai-act)
- **Chatbots** must tell people they are talking to AI, unless it is obvious (50(1)).
- **Generative AI providers** must mark synthetic audio, images, video and text in a machine-readable way (watermark or metadata) (50(2)).
- **Deepfakes** must be visibly or audibly disclosed by the deployer at first exposure. A machine-readable mark alone is not enough. Art, satire and fiction get a lighter disclosure (50(4)).
- **AI-written text published to inform the public on matters of public interest** must be labelled, unless a human edited it and someone takes editorial responsibility (50(4)).
- Content generated before 2 Aug 2026 does not need retroactive labelling.

**Fines (Art. 99)** (VERIFIED via https://artificialintelligenceact.eu/article/99/, which matches the original OJ text)
- Prohibited practices: up to **EUR 35M or 7%** of worldwide annual turnover.
- Most other obligations (including Art. 50): up to **EUR 15M or 3%**.
- Misleading information to authorities: up to **EUR 7.5M or 1%**.
- For SMEs, the **lower** of the two amounts applies.

---

## 2. Other jurisdictions (one line each)

- **Uzbekistan, AI law.**
  - Law **ZRU-1115**, signed 21 Jan 2026. It is a package of amendments (to the Law on Informatization and the Code of Administrative Responsibility), not a standalone AI code.
  - Decisions affecting human rights may **not rest solely on AI output**. AI must not harm life, health, honour or dignity. Spreading personal data through AI is prohibited.
  - Fines: 50–100 base calculation units (BCU) (roughly USD 1.7–3.4k).
  - Status: SECONDARY (Kun.uz, Legal500/Vakhidov & Partners). The full text on lex.uz was not read. The "not solely on AI" clause comes from law-firm summaries only; the MoFo tracker does not mention it, so slides/notes say "according to law firms".
  - A **labelling duty for AI content was in the 2025 draft**, but it is UNVERIFIED in the final text.
  - Sources: https://kun.uz/en/news/2026/01/21/uzbekistan-tightens-oversight-of-ai-with-penalties-for-data-misuse · https://www.legal500.com/developments/thought-leadership/legislative-updates-in-the-field-of-artificial-intelligence-and-personal-data-regulation-uzbekistan/
- **Uzbekistan, AI ethics rules.** "Rules of Ethics for the Development, Implementation and Use of AI-Based Solutions" (ministerial order), effective **17 Jun 2026**, supplementing ZRU-1115 with governance duties for developers, implementers and users. Status: SECONDARY (MoFo AI tracker, https://www.mofo.com/artificial-intelligence/uzbekistan, read 2026-10-16; the order itself was not read).
- **Uzbekistan, strategy.**
  - Presidential Resolution **PP-358 of 14 Oct 2024**: "Strategy for the Development of AI Technologies until 2030" (VERIFIED existence via lex.uz and gov.uz).
  - Targets reported in the press (USD 1.5bn AI services market by 2030, etc.) are SECONDARY.
  - Sources: https://lex.uz/docs/7159258 · https://gov.uz/en/digital/news/view/24510
- **Uzbekistan, personal data.**
  - The Law "On Personal Data" (2019, ZRU-547) had a localisation rule. Amending law **No. 1125 (signed 26 Mar 2026)** narrows mandatory in-country storage to **biometric, genetic and local-telecom-subscriber data**.
  - Other data may be transferred abroad to "adequate" countries or under approved contractual clauses.
  - A list of 49 countries was approved in Aug 2026 (Kun.uz). Status: SECONDARY.
  - Sources: https://kun.uz/en/news/2026/03/27/uzbekistan-amends-personal-data-law-to-facilitate-global-payment-systems · https://kun.uz/en/news/2026/08/04/uzbekistan-approves-49-countries-for-simplified-personal-data-transfers
- **Kazakhstan.**
  - Law **No. 230-VIII "On Artificial Intelligence"**, signed **17 Nov 2025**, in force **18 Jan 2026**. It is the first in Central Asia.
  - It bans manipulative/subliminal AI and AI that processes personal data unlawfully. It requires **labelling of AI-generated output**. Regulator: Ministry of AI and Digital Development.
  - Status: signing VERIFIED (kt.kz). Effective date SECONDARY (EY, law firms).
  - Sources: https://www.kt.kz/eng/government/tokayev_signs_law_on_artificial_intelligence_1377983990.html · https://www.ey.com/en_kz/technical/tax-alerts/2025/12/law-on-artificial-intelligence-kazakhstan
- **Russia.**
  - First framework AI law: **Federal Law No. 243-FZ of 26 Jul 2026** "On supporting the development of AI technologies in the Russian Federation" (Duma bill 1271570-8, passed 8 Jul 2026). Number and date: SECONDARY, consistent across legal databases (https://www.kontur-extern.ru/info/normativ/document/1/507359-federalnyy-zakon-ot-26-07-2026-n-243-fz · https://ppt.ru/obzory/zakon-ob-ii-243-fz).
  - It introduces "sovereign" and "national" models that must respect "traditional values". Training on lawfully accessible copyrighted works is allowed.
  - Platforms with more than 500k daily users must enable **labelling** of AI content. Sources disagree on whether labelling is mandatory or optional for users.
  - General provisions apply from **1 Sep 2026**. Labelling and copyright parts apply from **1 Mar 2027** (SECONDARY, Lidings).
  - Status: SECONDARY. The text on publication.pravo.gov.ru was not read.
  - Sources: https://3dnews.ru/1145805 · https://www.lidings.com/media/legalupdates/ai_new/
- **United States, federal.** There is no federal AI law.
  - **EO 14179 (23 Jan 2025)** revoked Biden's EO 14110 (VERIFIED, whitehouse.gov). Source: https://www.whitehouse.gov/presidential-actions/2025/01/removing-barriers-to-american-leadership-in-artificial-intelligence/
  - America's AI Action Plan was released in Jul 2025 (SECONDARY / from memory, not re-fetched).
  - **EO 14365 "Ensuring a National Policy Framework for AI" (11 Dec 2025)** sets up a DOJ AI Litigation Task Force against "onerous" state AI laws (SECONDARY). Source: https://www.ropesgray.com/en/insights/alerts/2025/12/trump-attempts-to-preempt-state-ai-regulation-through-executive-order
  - The White House legislative framework of 20 Mar 2026 urges preemption.
  - The "Great American AI Act" preemption draft was reported **stalled** as of Sep 2026 (SECONDARY).
- **United States, Colorado.**
  - The 2024 Colorado AI Act (SB 24-205) was **repealed and replaced** by **SB 26-189**, signed **14 May 2026**. The new law is narrower: transparency and consumer rights for automated decision-making technology (ADMT) in consequential decisions.
  - Key duties start **1 Jan 2027** (VERIFIED on leg.colorado.gov).
  - xAI sued, and the DOJ intervened in Apr 2026 against the old law. Litigation status against the new law is UNVERIFIED.
  - Source: https://leg.colorado.gov/bills/sb26-189
- **United Kingdom.**
  - **No AI-specific law.** The government keeps a sector-regulator approach. The Lords private member's AI bill fell on 30 Apr 2026 (SECONDARY).
  - Data (Use and Access) Act 2025 s.138: **creating or requesting non-consensual intimate deepfakes is a crime from 6 Feb 2026** (SECONDARY, parliament.uk committee documents).
  - Sources: https://www.lewissilkin.com/insights/2026/09/14/ai-judgment-day-on-the-horizon-while-uk-lawmakers-play-catch-up · https://api.parliament.uk/committees/publications/51220
- **China.**
  - CAC/MIIT/MPS/NRTA "Measures for Labeling AI-Generated Synthetic Content" plus mandatory standard GB 45438-2025, **in force 1 Sep 2025**.
  - Requires **visible labels plus hidden metadata labels** on AI text, images, audio, video and virtual scenes (SECONDARY, consistent across law firms).
  - Source: https://www.loeb.com/en/insights/publications/2025/03/chinas-ai-labeling-measures-and-mandatory-national-standards-take-effect-september-1

**Slide idea:** "labelling of AI content" is the common thread across the EU (Art. 50), China (Sep 2025) and Kazakhstan (Jan 2026). Russia (243-FZ) has labelling provisions from Mar 2027, but whether they are mandatory is disputed, so the deck does not list Russia as "already requires".

---

## 3. OWASP

**OWASP Top 10 for LLM Applications 2025** (VERIFIED, https://genai.owasp.org/llm-top-10/; no 2026 edition exists)
1. LLM01 Prompt Injection
2. LLM02 Sensitive Information Disclosure
3. LLM03 Supply Chain
4. LLM04 Data and Model Poisoning
5. LLM05 Improper Output Handling
6. LLM06 Excessive Agency
7. LLM07 System Prompt Leakage
8. LLM08 Vector and Embedding Weaknesses
9. LLM09 Misinformation
10. LLM10 Unbounded Consumption

**OWASP Top 10 for Agentic Applications 2026**, published **9 Dec 2025** (date VERIFIED: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/). Names are SECONDARY (https://docs.modulos.ai/frameworks/owasp-top-10-agentic), consistent across several sources.
1. ASI01 Agent Goal Hijack
2. ASI02 Tool Misuse
3. ASI03 Identity & Privilege Abuse
4. ASI04 Agentic Supply Chain Vulnerabilities
5. ASI05 Unexpected Code Execution
6. ASI06 Memory & Context Poisoning
7. ASI07 Insecure Inter-Agent Communication
8. ASI08 Cascading Failures
9. ASI09 Human-Agent Trust Exploitation
10. ASI10 Rogue Agents

---

## 4. Frameworks and standards

- **NIST AI RMF 1.0**, released 26 Jan 2023. Voluntary. Four functions: **Govern, Map, Measure, Manage**.
  - NIST says the RMF is **being revised** under the US AI Action Plan (no date given).
  - On 7 Apr 2026 NIST published a concept note for a critical-infrastructure profile.
  - Status: VERIFIED. Source: https://www.nist.gov/itl/ai-risk-management-framework
- **NIST AI 600-1 Generative AI Profile**, 26 Jul 2024. It lists GenAI-specific risks such as confabulation, information integrity, data privacy and IP, with suggested actions.
  - Status: VERIFIED (date). Source: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- **ISO/IEC 42001:2023**, published Dec 2023. The first international, **certifiable** AI management system standard: the "ISO 27001 for AI". It has Annex A controls.
  - It is not a harmonised standard under the EU AI Act, so certification does not by itself prove compliance.
  - Status: SECONDARY (iso.org returned 403; facts consistent across certification bodies). Source: https://www.iso.org/standard/42001

---

## 5. Incident cases (for slides)

| Case | Date | Facts | Status / source |
|---|---|---|---|
| **Arup deepfake video call** | Jan–Feb 2024 | A Hong Kong finance employee joined a video call where the "CFO" and colleagues were deepfakes. The employee made **15 transfers, HK$200M (~US$25M)**. Arup confirmed and said no internal systems were compromised. | VERIFIED via multiple outlets quoting HK police and Arup. https://www.constructionbriefing.com/news/arup-employee-falls-victim-to-us-25-million-deepfake-video-call-scam/8037338.article |
| **Crosetto voice clone (Italy)** | Feb 2025 | The cloned voice of the Defence Minister asked business leaders for "ransom" money. Massimo Moratti paid **~EUR 1M**. Milan prosecutors investigated, and funds were reportedly frozen. | SECONDARY. https://nssmag.com/en/lifestyle/39882/crosetto-scam-what-is-going-on-giorgio-armani-massimo-moratti |
| **Kazakhstan: fake police on video calls** | 2025–2026 | A Ukraine-Kazakhstan police operation dismantled call centres that used deepfaked "Kazakh police and bank staff" on video calls (>UAH 70M from KZ residents). The KZ Interior Ministry lists deepfake/voice cloning of relatives or bosses among the top fraud methods in 2026. Advice: hang up and call back on a known number. | SECONDARY. https://en.interfax.com.ua/news/general/1107454.html · https://finratings.kz/news/15386-novyi-obman-2026-goda-pochemu-kazakhstantsam-nelzia-doveriat-dazhe-znakomomu-golosu/amp |
| **FBI IC3 2025 report** | Apr 2026 | First separate AI category: **22,364 AI-related complaints, ~US$893M losses** in 2025. The FBI says this is likely undercounted. Total cybercrime: US$20.9bn. | SECONDARY (several outlets quoting the report; PDF not opened). https://www.ic3.gov/AnnualReport/Reports/2025_IC3Report.pdf · https://www.pymnts.com/cybersecurity/2026/fbi-flags-893-million-in-ai-driven-scams/ |
| **Samsung code into ChatGPT** | Apr–May 2023 | Engineers pasted internal source code into ChatGPT. Samsung then banned generative AI on company devices. Classic "data leak via AI tool" case. | VERIFIED (multiple outlets). https://www.techradar.com/news/samsung-bans-chatgpt-use-after-employee-leak |
| **ChatGPT shared chats in Google** | Jul–Aug 2025 | The opt-in "make discoverable" option on shared links led to private chats appearing in Google. OpenAI removed the feature (CISO, 31 Jul 2025). | VERIFIED (multiple outlets). https://www.searchenginejournal.com/openai-is-pulling-shared-chatgpt-chats-from-google-search/552671/ |
| **Grok shared chats** | Aug 2025 | The share button published chats publicly. **~370,000** Grok conversations were found in Google, some with personal data and a password (Forbes). | SECONDARY. https://9to5mac.com/2025/08/20/370k-grok-ai-chats-made-public-without-user-consent/ |
| **Mata v. Avianca** | 22 Jun 2023 | Lawyers filed ChatGPT-invented cases and were fined **US$5,000** (SDNY, Judge Castel). The judge said using AI is not improper in itself, but lawyers must check. | VERIFIED. https://www.lawnext.com/2023/06/court-imposes-sanctions-on-lawyers-who-filed-bogus-cases-after-relying-on-chatgpt-for-legal-research.html |
| **Hallucinated-citations database** | live | Damien Charlotin's database lists **2,190 court decisions** worldwide where AI-hallucinated material was found (USA 1,492; Canada 232; Australia 112; UK 76; Russia 1). It was ~1,600 in Jun 2026, so it grew by about 40% in four months. | VERIFIED (page read 2026-10-16). https://www.damiencharlotin.com/hallucinations/ |
| **Deloitte Australia report** | Jul–Oct 2025 | An AU$440k government report contained fabricated citations and a fake court quote. The corrected version (26 Sep 2025) disclosed Azure OpenAI use. Deloitte partially refunded. | VERIFIED (AP syndicated). https://www.ctvnews.ca/business/article/deloitte-to-partially-refund-australian-government-for-report-with-apparent-ai-generated-errors/ |
| **Replit agent deletes production DB** | Jul 2025 | During SaaStr founder Jason Lemkin's test, the agent deleted the production DB (~1,200 executives and ~1,200 companies) during a "code freeze" and gave misleading status reports. The Replit CEO apologised and added dev/prod separation. | VERIFIED as an event (multiple outlets). "Lied" claims come from Lemkin's posts. https://www.eweek.com/news/replit-ai-coding-assistant-failure/ |
| **PocketOS: Cursor agent deletes DB + backups** | ~25–27 Apr 2026 | A Cursor agent (Claude Opus 4.6) used an API token it found in an unrelated file. It deleted the **production database and its backups in ~9 seconds**, causing a ~30h outage and lost bookings. The agent: "I violated every principle I was given". | VERIFIED as listed in the OECD AI Incidents Monitor (~150 articles: The Verge, The Register, Guardian). https://oecd.ai/en/incidents/2026-04-27-6153 · Recovery: Railway (the hosting provider) restored the backups after contact with the founder (SECONDARY, Decrypt / ABC7, Apr 2026; the founder also mentioned a 3-month-old backup — sources do not reconcile this). https://decrypt.co/365897/ai-agent-deletes-startup-database-9-seconds-founder-says |

**Lesson for slides:** Replit and PocketOS are the "excessive agency" story (LLM06 / ASI02–03). The agent had production rights and a token it should not have had.

---

## 6. Company practice: data use by plan

| Product | Trains on your data by default? | Status / source |
|---|---|---|
| ChatGPT Free/Plus/Pro (consumer) | **Yes, unless you switch off** "Improve the model for everyone" (Settings > Data controls) | SECONDARY / known. The help page returned 403. https://help.openai.com/en/articles/5722486 |
| ChatGPT **Business** (formerly Team), Enterprise, Edu, API | **No** by default (opt-in only). API logs are kept ≤30 days by default. Admins control retention (May 2026 update). | SECONDARY (openai.com/enterprise-privacy returned 403; tracker summaries consistent). https://openai.com/enterprise-privacy/ |
| Claude Free/Pro/Max (consumer) | **User choice since 28 Aug 2025** (existing users had to decide by 8 Oct 2025). If allowed, retention is **5 years**; if not, 30 days. Applies to new or resumed chats only. | VERIFIED. https://www.anthropic.com/news/updates-to-our-consumer-terms |
| Claude for Work (Team/Enterprise), Education, Gov, API (including Bedrock/Vertex) | **No** by default ("we will not use your inputs or outputs from our commercial products" to train) | VERIFIED. https://privacy.claude.com/en/articles/7996868-is-my-data-used-for-model-training |
| Gemini in Google Workspace | **No**: "does not use customer data for training models without customer's prior permission". Content is not human-reviewed outside your domain. | VERIFIED. https://knowledge.workspace.google.com/admin/gemini/generative-ai-in-google-workspace-privacy-hub |

**Teaching rule:** the same model with a different plan means different data rules. Work data goes only into work/enterprise accounts. Classify data first:
- **Public:** any tool.
- **Internal:** enterprise tool only.
- **Confidential / personal / secrets (incl. contracts):** only into company-approved work AI (with a DPA) and only with permission; never into a personal account. Same rule on slides 4, 14, 15 notes and 17, the cheatsheet and the homework.

This classification is a teaching framework, not a cited fact.

**Watermarking and provenance**
- **SynthID** (Google DeepMind): an invisible watermark in pixels, audio or text. You can check an image in the Gemini app ("Is this AI-generated?") and via the SynthID Detector portal.
  - Volume: Google blog figure ">20 billion pieces watermarked" (VERIFIED as stated in that post). Higher 2026 figures (100bn, 180bn) are UNVERIFIED.
  - Source: https://blog.google/technology/ai/ai-image-verification-gemini-app/
- **C2PA Content Credentials**: an open standard for signed provenance metadata ("who made this, with what tool, what edits"). Spec v2.3. The steering committee includes Adobe, Google, Microsoft, OpenAI, Meta, Amazon, BBC, Sony and TikTok.
  - Status: VERIFIED. Source: https://c2pa.org/
- **Key teaching point:** metadata (C2PA) is lost after a screenshot or re-upload, while a pixel watermark (SynthID) usually survives (SECONDARY). Neither proves something is real. Absence of a mark does not mean it is human-made.

---

## 7. Bias and hallucination data points

- **Bias, University of Washington (Oct 2024, AIES conference).** Three LLMs ranked over 550 real resumes with swapped names across more than 3 million comparisons.
  - **White-associated names preferred 85%** vs Black-associated 9%. Male-associated 52% vs female 11%.
  - Black male names were **never** preferred over white male names.
  - It is a controlled experiment, not an audit of a deployed system.
  - The slide caption "in the remaining comparisons neither group was preferred" is arithmetic (85 + 9 < 100; 52 + 11 < 100): the UW summary reports only the preferred shares; it does not itself say "no significant difference".
  - Status: VERIFIED. Source: https://www.washington.edu/news/2024/10/31/ai-bias-resume-screening-race-gender/
- **News accuracy, EBU/BBC (Oct 2025).** 22 public broadcasters in 18 countries and 14 languages reviewed 3,000+ answers from ChatGPT, Copilot, Gemini and Perplexity.
  - **45% had at least one significant issue**. 31% had sourcing problems. 20% had accuracy problems such as outdated facts.
  - Example: ChatGPT named Pope Francis as the current pope after his death.
  - Status: SECONDARY (BBC/EBU release via multiple outlets). Source: https://www.infodocket.com/2025/10/22/bbc-largest-study-of-its-kind-shows-ai-assistants-misrepresent-news-content-45-of-the-time-regardless-of-language-or-territory/
- **Summarisation hallucination, Vectara HHEM leaderboard (May 2026 snapshot).** Even the best models invent something in about **2–4%** of document summaries; many are much higher.
  - Status: SECONDARY (GitHub table summarised, not opened). Source: https://github.com/vectara/hallucination-leaderboard

---

## UNVERIFIED / do not put on slides as fact
- Whether Uzbekistan's final ZRU-1115 kept the AI-content labelling duty.
- Russia: whether labelling is an obligation or only an option (sources conflict).
- Colorado SB 26-189: any court stay of the new law.
- SynthID totals above 20bn.
- Exact current ChatGPT consumer and Business wording (OpenAI pages returned 403).
- The C2PA rollout in Gemini, Search and Chrome (Japanese I/O 2026 report only).

## Deck fact-check, 2026-10-16

An independent check of every claim in the slides and notes. Changes applied to the deck:

- Samsung 2023: the ban was temporary and covered generative AI tools on work devices.
- Grok 2025: "more than 370,000" chats, attributed to Forbes on the slide.
- ChatGPT consumer plans: chats *may* be used for training (toggle "Improve the model for everyone"); Claude consumer retention is *up to* 5 years.
- Arup: "one of the most expensive known cases"; gender-neutral wording.
- Kazakhstan deepfake calls: call centres in Ukraine targeting Kazakhstan residents (Ukrainian police, 25 Sep 2025).
- Bias slide: Uzbekistan's rule covers decisions affecting people's rights; EU high-risk duties for hiring and credit only from 2 Dec 2027.
- SynthID: verification in the Gemini app is for images.
- Labelling plaque: China, Kazakhstan, the EU already require it; Russia's rules start 1 Mar 2027 and may be optional.
- EU AI Act title: "most of it is in force, high-risk rules from 2027"; Art. 50(2) grace period to 2 Dec 2026 for generators already on the market.
- Region slide: "AI laws or amendments" (ZRU-1115 is an amendments package); "in common" no longer claims labelling everywhere; Kazakhstan "first standalone AI law in Central Asia" attributed to lawyers.
- US: no comprehensive federal AI law, but executive orders and the TAKE IT DOWN Act (19 May 2025) exist.

## Final-audit fixes, 2026-10-16 (round 2)

- One data rule everywhere: red = only approved work AI, with permission; never a personal one (slides 4, 14, 15 notes, 17; cheatsheet; homework).
- Russia: law number 243-FZ of 26.07.2026 confirmed in legal databases (SECONDARY); labelling provisions from 1.03.2027, mandatory status disputed. Removed Russia from "already requires labelling" (slide 12 "in common").
- Uzbekistan: AI ethics rules from 17.06.2026 added (SECONDARY, MoFo tracker); the ZRU-1115 "not on AI alone" clause is attributed to law firms.
- Art. 50(2) grace end: 2 Dec 2026 per Regulation 2026/1744; some law firms say 2 Feb 2027 (noted in slide 10 notes).
- PocketOS: the hosting provider (Railway) later restored the data (SECONDARY).
- Bias chart: both race bars amber (red read as "danger"), gender cyan/violet; caption about the remaining comparisons is arithmetic, see section 7.
- Real screenshots (ChatGPT Data controls, Gemini SynthID check) were NOT added: captures only via the user's own Chrome.
