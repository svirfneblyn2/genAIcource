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

The table below outlines the primary AI development environments available today, their free-tier policies, and official download links:

| Tool & Provider | Type | Download Link | Free Tier Details | Best For |
|---|---|---|---|---|
| **Google Antigravity**<br>*(Google DeepMind)* | Standalone AI-first IDE (VS Code based) + CLI (`agy`) | [antigravity.google](https://antigravity.google) | **100% Free** via Google Account.<br>Includes generous daily request quotas for Gemini 2.5 / Flash and agent orchestration. $300 Google Cloud credit available for enterprise expansion. | Multi-step agent workflows, zero-config onboarding, native Gemini model ecosystem. |
| **GitHub Copilot / Codex**<br>*(GitHub & OpenAI)* | Extension for VS Code / JetBrains + ChatGPT Desktop Canvas | [code.visualstudio.com](https://code.visualstudio.com)<br>+ [Copilot Extension](https://github.com/features/copilot) | **Copilot Free Plan:**<br>Includes 2,000 code completions/month and 50 chat messages/month with standard GitHub account.<br>ChatGPT Desktop Free includes Canvas mode. | Fast inline autocomplete, seamless integration for existing VS Code users. |
| **Anthropic Claude**<br>*(Anthropic)* | Desktop App + Claude Code CLI agent | [claude.ai/download](https://claude.ai/download)<br>+ [Claude Code CLI](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/overview) | **Claude Free Tier:**<br>Free web and desktop access to Claude 3.5 Sonnet with rolling daily limits.<br>Claude Code CLI requires an Anthropic Console account ($5 free initial sign-up credit). | Deep architectural reasoning, long-document analysis, visual UI Artifacts. |
| **Cursor**<br>*(Anysphere)* | Standalone AI-first IDE (VS Code fork) | [cursor.com](https://cursor.com) | **Cursor Hobby (Free):**<br>Includes 2-week Pro trial upon signup, then continues with 2,000 completions and 50 slow agent requests per month at $0. | Full codebase indexing, rapid file-to-file refactoring, keyboard-driven workflow. |

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
