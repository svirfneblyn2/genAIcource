# Lesson 12 • Homework: pick MCP servers for your task and write the access rules

**Course:** GenAI Basics • Module 3 (Own Models and Agents)  
**Submit:** the `genai-homeworks/L12/` folder in your personal GitHub repository  
**Reviewer:** Ihar Rubanovich (`ihar_rubanovich@epam.com`)  
**Time:** 2–3 hours  
**Code:** not required. Your own server is optional (slides 9–11).  
**Matches:** slide 20 of `presentation_L12_MCP_and_Agent_Frameworks_EN_v2.html`, plus slides 5–6 (connectors and permissions), 8 (registry), 12 (security), 19 (exercise). Facts as of 16.10.2026.

---

## Steps

### 1. The task (15 min)
In 3–5 sentences describe a work task where the AI needs your data or services (mail, files, tasks, CRM, calendar).

### 2. Servers (30 min)
Find 2–3 suitable MCP servers:
- in Claude: Customize → Connectors (or the “+” button in a chat → Connectors);
- in ChatGPT: Plugins;
- in the registry at registry.modelcontextprotocol.io.

For each, record in `servers.md`: the publisher (the company’s official server or third-party), the tools it offers, the permissions it asks for (read, write, delete, send).

### 3. Connect on test data (40 min)
Connect one server in Claude or ChatGPT to a **personal or training** account with test data (for example a separate Google Drive folder with synthetic files). Ask 3 questions that need the server. Screenshot the permission prompt.

### 4. Access rules (20 min)
In `rules.md`:
- what you allow “always” (read-only tools only);
- what you confirm every time;
- what you never connect, and why;
- what you will do if a server updates and asks for new permissions.

### 5. Optional
Build your own MCP server with the slide 11 prompt and connect it to Claude Desktop or LM Studio (the L10 model). Test it in MCP Inspector.

---

## What to submit

```
genai-homeworks/L12/
├─ README.md    # task, which server you connected, conclusion (5–10 lines)
├─ servers.md   # 2–3 servers: publisher, tools, permissions
├─ demo.png     # permission prompt screenshot
└─ rules.md     # always / every time / never
```

## Grading (10 points)

| Criterion | Points |
|---|---|
| Servers fit the task; publisher and permissions recorded | 3 |
| A server connected on test data; permission screenshot | 3 |
| Access rules: least privilege, “always” only for reading | 3 |
| Test data and personal or training accounts only | 1 |

**Common mistakes:** connecting work mail or a corporate Drive without approval; “Always allow” for a tool that sends or deletes; a third-party server instead of the official one.
