# Local AI Coding Environments & Agent Shells: Beginner's Guide

> **Goal:** Understand what AI coding environments are, where to download them, how their free tiers work, and what every newcomer needs to know before starting.

---

## 1. What Are AI Coding Environments?

Traditional code editors (like classic Notepad or basic VS Code) are passive: they display text and highlight syntax, but they have no understanding of what you are building.

**AI-first coding environments and agent shells** connect a code editor directly to modern Large Language Models (LLMs). Instead of copying and pasting code back and forth to a website chat window, the AI lives directly inside your workspace:
* **Context Awareness:** The AI can see your open files, directory tree, and error messages.
* **Inline Edits:** You can highlight a paragraph or function and instruct the AI to rewrite, fix, or optimize it on the spot.
* **Autonomous Agents:** Modern environments feature "Agent Mode", where the AI can create folders, write new files, and run terminal commands (like Git) with your approval.

---

## 2. Tool Comparison & Free Downloads

The table below outlines the primary AI development environments, their free-tier policies and official download links (as of 16.10.2026; prices change often — L16 has the current overview):

| Tool & Provider | Type | Download Link | Free Tier Details | Best For |
|---|---|---|---|---|
| **Google Antigravity**<br>*(Google)* | AI-first IDE + Antigravity CLI | [antigravity.google](https://antigravity.google) | **Individuals plan: $0** with basic weekly rate limits (Gemini models). Higher limits with Google AI Pro / Ultra. The consumer Gemini CLI moved here in June 2026. | Multi-step agent workflows, zero-config onboarding, Gemini models. |
| **GitHub Copilot / OpenAI Codex**<br>*(GitHub & OpenAI)* | Extension for VS Code / JetBrains; Codex app, CLI and IDE extension | [code.visualstudio.com](https://code.visualstudio.com)<br>+ [Copilot](https://github.com/features/copilot) · [Codex](https://openai.com/codex) | **Copilot Free:** 2,000 completions + 50 chat requests a month, limited agent mode.<br>**Codex** is included in every ChatGPT plan, including Free (quick tasks). | Inline autocomplete for VS Code users; Codex for agent tasks from a ChatGPT account. |
| **Anthropic Claude**<br>*(Anthropic)* | Claude app (web, desktop) + Claude Code agent | [claude.ai/download](https://claude.ai/download)<br>+ [Claude Code](https://code.claude.com/docs/en/overview) | **Claude Free:** chat in the web and desktop app with daily limits.<br>**Claude Code has no free tier:** it starts with the Pro plan ($20/month, $17 billed yearly). | Long-document analysis, Artifacts; Claude Code for serious agent work (L16). |
| **Cursor**<br>*(Anysphere)* | AI-first IDE (VS Code fork) | [cursor.com](https://cursor.com) | **Free:** limited agent requests. Paid: Plus $8 (Grok models only), Premium $30 (cloud agents). | Codebase indexing, fast multi-file refactoring. |

---

## 3. Critical Information for Beginners

Before you begin working with local AI tools, keep these four operational principles in mind:

### 1. Account Logins vs. API Keys
* **Account Logins (Free Tiers):** Most tools (Antigravity, Cursor, GitHub Copilot Free) allow you to sign in with your regular Google or GitHub account. You do not need to enter credit cards or deal with billing.
* **API Keys (Pay-as-you-go):** If you build custom Python scripts or use command-line agent tools, you will encounter API keys. API keys meter consumption per 1 million tokens. Do not share API keys publicly or commit them to GitHub.

### 2. Rate Limits & Rolling Quotas
Free tiers are generous, but they operate on **rate limits** (e.g., a cap of requests per 3 hours, or a daily reset counter).  
* *Best Practice:* Do not paste massive 5,000-line log files into chat repeatedly. Keep your prompts focused on the specific function or markdown section you are editing.

### 3. Context Window Boundaries
An AI model only "remembers" the files currently attached to its active prompt context.  
* In editors like Antigravity and Cursor, use the **`@` symbol** (e.g., `@README.md` or `@solution.py`) to explicitly point the AI to the exact file you want it to inspect. This saves tokens and prevents the model from hallucinating.

### 4. Data Privacy & Proprietary Code
* Never paste sensitive client passwords, access tokens, customer PII (Personally Identifiable Information), or confidential business data into personal free-tier accounts.
* When working on enterprise client projects, always use enterprise-approved instances that guarantee data privacy and zero training on customer code.
