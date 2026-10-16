# Instructor Script • Lesson 15: Responsible AI — Errors, Leaks, Deepfakes and Laws (90 Minutes)

**Course:** GenAI Basics • Module 4 (Idea to Product) • Lesson 15 of 16
**Instructor:** Ihar Rubanovich (`ihar_rubanovich@epam.com`), Engineering Manager II & AI Ambassador @ EPAM Systems
**Audience:** GenAI beginners from many roles and countries (Uzbekistan, CIS, EU). A calm, factual tone; an overview, not legal advice.
**Format:** 17 slides (`presentation_L15_Responsible_AI_Security_Regulation_EN_v2.html` / PDF) • **Microsoft Teams** • break on slide 13
**Deck controls:** `←/→` navigate, `N` speaker notes, `G` all slides, `F` fullscreen.
**Source of truth:** `deck_v2/build.py`; this script is generated from it (`deck_v2/make_docs.py`).
**Facts:** as of 16.10.2026, sources and verification status (verified / secondary) in `L15_08_Source_Notes_Research_2026-10.md`.

> **Before class:** recheck the law dates (EU AI Act, Uzbekistan, Kazakhstan, Russia) and recent cases. If students ask about their own company’s situation, refer them to their lawyers and security team.

**Lesson objective:** students know the four main AI risks at work from real cases, can classify data with the traffic light, tell personal and business plans apart, know how to guard against deepfake fraud and limit agents, understand labelling requirements and the main laws (EU, Uzbekistan, Kazakhstan, Russia), and draft AI rules for their own team.

---

## Timing (17 slides • 90 minutes incl. a 5-minute break)

| Slide | Title | Time | Min |
|---|---|---|---|
| **01** | Responsible AI | 00:00–02:00 | 2 |
| **02** | Four main AI risks at work: what happens often and what costs a lot | 02:00–07:00 | 5 |
| **03** | The model confidently makes things up — a human must check the answer | 07:00–13:00 | 6 |
| **04** | A leak starts with one pasted file: decide in advance which data may go where | 13:00–19:00 | 6 |
| **05** | Same model, different rules: personal and business plans treat data differently | 19:00–24:00 | 5 |
| **06** | A video call with “the CFO” can be fake: verify money requests through another channel | 24:00–29:00 | 5 |
| **07** | Excessive agency: an agent does whatever it has rights to — even if you did not want it to | 29:00–35:00 | 6 |
| **08** | The OWASP Top 10 for AI apps: the four that affect everyone | 35:00–40:00 | 5 |
| **09** | AI repeats the biases in its data: CVs that differed only in the name were ranked differently | 40:00–45:00 | 5 |
| **10** | Laws require labelling AI content, and technology helps: invisible marks and signatures | 45:00–50:00 | 5 |
| **11** | The EU AI Act applies in stages — most of it is in force, high-risk rules from 2027 | 50:00–56:00 | 6 |
| **12** | Uzbekistan, Kazakhstan and Russia have already passed AI laws or amendments — with a lot in common | 56:00–62:00 | 6 |
| **13** | 5 minutes: recall what you pasted into AI this week | 62:00–67:00 | 5 |
| **14** | AI rules for a team fit on one page: four points | 67:00–73:00 | 6 |
| **15** | Exercise: is this OK — and what to do differently? | 73:00–79:00 | 6 |
| **16** | Homework: one-page AI rules for your team | 79:00–85:00 | 6 |
| **17** | Lesson summary | 85:00–90:00 | 5 |

Part 1 (slides 01–12, 00:00–62:00): the risk map, made-up facts, leaks, plans, deepfakes, agents, OWASP, bias, labelling, the EU AI Act, our region. Break (slide 13, 62:00–67:00). Part 2 (slides 14–17, 67:00–90:00): team rules, exercise, homework, summary.

---

### Slide 01 (00:00–02:00) • Responsible AI

**On screen:** Lesson title.

#### Speaker (2 min)
> Welcome. In this course we learned to generate text, images, video and audio, and to build agents and prototypes. Today: how to use all of that at work without harming yourself, your company or your customers. No legal lecture: real cases, simple rules and what laws already require.

---

### Slide 02 (02:00–07:00) • Four main AI risks at work: what happens often and what costs a lot

**On screen:** Risk map: how often × damage, four risks.

#### Speaker (5 min)
> The map: horizontally how often it happens, vertically how much damage it does. Model mistakes happen all the time; damage is usually moderate if a human checks the result. A data leak is one pasted document, but the damage is large. Deepfake fraud is rare but costs millions. An agent deleting data is the new 2025–2026 risk: seconds and a disaster.
>
> Next, for each risk a real case and a rule. At the end, what laws require, and your homework: AI rules for your own team.

---

### Slide 03 (07:00–13:00) • The model confidently makes things up — a human must check the answer

**On screen:** Three numbers: 45% (EBU/BBC), 2,190 decisions, a $5,000 fine.

#### Speaker (6 min)
> Risk number one by frequency. A study by the European Broadcasting Union and the BBC, October 2025: 22 public broadcasters from 18 countries checked over 3,000 answers from ChatGPT, Copilot, Gemini and Perplexity about news. 45% had at least one significant issue: a wrong source, an outdated fact.
>
> The best-known case is Mata v. Avianca in the US, 2023: lawyers filed a brief citing cases ChatGPT had invented and were fined 5,000 dollars. The judge stressed that using AI is fine, but checking is the lawyer’s duty. The open database kept by researcher Damien Charlotin now lists 2,190 such court decisions worldwide. The rule is simple: anything that leaves your hands gets checked against the original source.

---

### Slide 04 (13:00–19:00) • A leak starts with one pasted file: decide in advance which data may go where

**On screen:** The data traffic light; the Samsung and Grok cases.

#### Speaker (6 min)
> The data traffic light — a simple scheme for a team. Green: public data — website texts, published documents — any AI. Amber: internal — plans, internal emails — only company-approved AI. Red: customer personal data, passwords, contracts — never in an AI chat without explicit approval.
>
> Two cases. Samsung, 2023: engineers pasted internal code into ChatGPT, and the company temporarily banned generative AI tools on work devices. Grok, 2025: the share button published chats, and about 370 thousand conversations appeared in Google search, some with personal data and even a password (as reported by Forbes). Takeaway: the danger is not only the model but the buttons around it.

---

### Slide 05 (19:00–24:00) • Same model, different rules: personal and business plans treat data differently

**On screen:** Personal vs business plans: who trains on data by default.

#### Speaker (5 min)
> A common mistake: “I have paid ChatGPT Plus, so it is safe”. No: personal ChatGPT plans may train on your chats by default until you switch it off in Settings → Data controls. Since August 2025 Claude lets the user choose, and if training is allowed, data is kept for up to five years.
>
> Business plans — ChatGPT Business and Enterprise, Claude for Work, Gemini in Google Workspace — do not train on company data by default. So the rule: work documents only go into the business account the company gave you.

---

### Slide 06 (24:00–29:00) • A video call with “the CFO” can be fake: verify money requests through another channel

**On screen:** Arup $25M and three rules against deepfake calls.

#### Speaker (5 min)
> One of the most expensive known cases: the engineering firm Arup, Hong Kong, early 2024. A finance employee joined a video call where the “CFO” and several “colleagues” were deepfakes. The employee made 15 transfers, about 200 million Hong Kong dollars, roughly 25 million US dollars. Arup confirmed the case.
>
> Similar schemes exist in our region: in 2025 Ukrainian police broke up call centres that video-called people in Kazakhstan, using deepfakes and uniforms to pose as police and bank staff. The defence is organisational: call back on a known number, agree a code word for urgent money requests and remember that urgency plus a request for secrecy is the main sign of fraud.

---

### Slide 07 (29:00–35:00) • Excessive agency: an agent does whatever it has rights to — even if you did not want it to

**On screen:** PocketOS (9 seconds) and Replit; rules for agents.

#### Speaker (6 min)
> A new risk we discussed in L11 and L12. April 2026, PocketOS: a coding agent in Cursor came across an access token in an unrelated file and in nine seconds deleted the production database along with its backups; the service was down for about 30 hours. July 2025, Replit: an agent deleted a production database during a declared code freeze and then misreported the state.
>
> OWASP’s risk list calls this “Excessive Agency”. The agent is not evil — it simply does what it has rights to. Hence the rules: least privilege, no production keys near the agent, human confirmation for deletion and money, backups kept separately where the agent cannot reach.

---

### Slide 08 (35:00–40:00) • The OWASP Top 10 for AI apps: the four that affect everyone

**On screen:** Four OWASP LLM Top 10 risks: LLM01, LLM02, LLM06, LLM09.

#### Speaker (5 min)
> OWASP is a non-profit community of security specialists. Its “Top 10 for LLM Applications”, 2025 edition, is the common language developers and security teams use to discuss AI. Of the ten items, four affect every user: prompt injection, sensitive information disclosure, excessive agency and misinformation.
>
> The other six are for developers: supply chain, data poisoning, output handling, system prompt leakage, vector stores, unbounded consumption. For agents, OWASP released a separate Top 10 in December 2025.

---

### Slide 09 (40:00–45:00) • AI repeats the biases in its data: CVs that differed only in the name were ranked differently

**On screen:** CV study bars: 85% / 9% / 52% / 11%.

#### Speaker (5 min)
> A University of Washington study had language models rank CVs that differed only in the candidate’s name. CVs with white-associated names were chosen in 85% of comparisons, Black-associated in 9%. Male-associated names in 52%, female in 11%. The model does not “want” to discriminate — it repeats the biases in the data it learned from.
>
> That is why decisions about people — hiring, credit, dismissal — AI may prepare, but a human makes. In the EU such systems are high-risk (duties apply from December 2027), and Uzbekistan’s law forbids basing decisions that affect people’s rights on AI output alone.

---

### Slide 10 (45:00–50:00) • Laws require labelling AI content, and technology helps: invisible marks and signatures

**On screen:** SynthID, C2PA, “no mark ≠ human”; where labelling is already required.

#### Speaker (5 min)
> The common thread across countries’ laws is labelling AI content. China has required visible and hidden labels since 1 September 2025. In the EU, AI Act Article 50 from 2 August 2026: a chatbot must say it is AI, generators must add a machine-readable mark, deepfakes need a visible label; generators already on the market before 2 August 2026 have until 2 December 2026 to add the machine-readable mark. Kazakhstan — from January 2026. In Russia, for platforms with over 500 thousand daily users — from 1 March 2027; sources disagree on how mandatory it is.
>
> Technology: Google’s SynthID is an invisible mark inside an image, sound or text; you can check an image in the Gemini app. C2PA is signed provenance data supported by Adobe, Google, Microsoft, OpenAI and others; but a screenshot strips it. Two takeaways: no mark does not mean a human made it, and a mark does not mean the content is true.

---

### Slide 11 (50:00–56:00) • The EU AI Act applies in stages — most of it is in force, high-risk rules from 2027

**On screen:** EU AI Act timeline and fines.

#### Speaker (6 min)
> The EU AI Act is the first major AI law. It applies in stages. Since February 2025 dangerous practices such as social scoring are banned. Since August 2025 — rules for general-purpose models. From 2 August 2026 most of it applies, including Article 50 labelling. The 2026 amendments (Regulation 2026/1744) added, from 2 December 2026, a ban on generators of non-consensual intimate images and moved the high-risk rules — hiring, credit, education — to December 2027.
>
> Fines: up to 35 million euros or 7% of worldwide turnover for prohibited practices, up to 15 million or 3% for most other violations. The law also covers companies outside the EU if their AI systems are used in the EU.

---

### Slide 12 (56:00–62:00) • Uzbekistan, Kazakhstan and Russia have already passed AI laws or amendments — with a lot in common

**On screen:** Uzbekistan, Kazakhstan, Russia, US/UK — one line each.

#### Speaker (6 min)
> Uzbekistan: law ZRU-1115, signed on 21 January 2026, amends the Law on Informatization and the Code of Administrative Responsibility. Decisions affecting human rights must not rest solely on AI output; spreading personal data via AI is prohibited; fines are 50–100 base calculation units. There is an AI development strategy to 2030 (PP-358). Whether labelling made it into the final text we could not confirm; it was in the draft.
>
> Kazakhstan: the Law “On Artificial Intelligence”, signed on 17 November 2025, in force since 18 January 2026 — described by lawyers as the first standalone AI law in Central Asia: a ban on manipulative AI, mandatory labelling. Russia: a framework law published in July 2026, general provisions from 1 September 2026, labelling rules for platforms with over 500 thousand daily users from 1 March 2027; sources disagree on whether labelling is mandatory. The US has no comprehensive federal AI law: there are state laws, executive orders and narrow federal laws, for example against intimate deepfakes; the UK takes a sector approach. This is an overview, not legal advice.

---

### Slide 13 (62:00–67:00) • 5 minutes: recall what you pasted into AI this week

**On screen:** 5-minute break timer.

#### Speaker (5 min)
> Press “Start”.

---

### Slide 14 (67:00–73:00) • AI rules for a team fit on one page: four points

**On screen:** Four points of team AI rules.

#### Speaker (6 min)
> Everything we discussed boils down to four points that fit on one page for a team. One: a list of approved tools and business accounts. Two: the data traffic light. Three: a human checks numbers, links and any decisions about people before sending. Four: how to label AI content and where to report if something goes wrong.
>
> If your company already has an AI policy, start from it and make a short version for your team. If not, this is a good first step to bring to your manager.

---

### Slide 15 (73:00–79:00) • Exercise: is this OK — and what to do differently?

**On screen:** Four work situations: OK or not.

#### Speaker (6 min)
> Four situations for the chat. Walk-through. A client contract into ChatGPT: only into a business account with a data protection agreement, never a personal one. An image for social media: fine, but check the generator’s licence, do not depict real people or brands, and label AI content where the law or the platform requires.
>
> Sorting CVs: AI may help, but a human decides, and you must check for bias — remember the names study. An urgent payment request on video from the CEO: stop and call back on a known number — that is the Arup scenario.

---

### Slide 16 (79:00–85:00) • Homework: one-page AI rules for your team

**On screen:** Five homework steps: team AI rules.

#### Speaker (6 min)
> Homework: a one-page set of AI rules for your team covering the four points of the lesson, with examples from your real tasks. You may ask AI for a draft, but checking and completing it is your job. No client names or internal data. Details in L15_05_Homework.

---

### Slide 17 (85:00–90:00) • Lesson summary

**On screen:** Four rules and the L16 preview.

#### Speaker (5 min)
> Four rules. Check numbers, links and quotes against the source. The data traffic light: work data only into work AI. Decisions about people, money and deletion are made by a human. Label deepfakes and AI content where the law or the platform requires it. The last lesson: agentic software development.

---
