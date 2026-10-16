# Lesson 12 • Cheatsheet: MCP and agent frameworks

**In one sentence:** MCP is an open “plug” standard that lets one tool server work in many AI apps; connect only trusted servers, grant least privilege and read permission prompts; reach for an agent framework when there are many steps.

## Slides and timing (90 min)
* **01 Cover (2).**  **02 The problem (4):** 3 × 3 = 9 links vs 3 + 3 = 6.
* **03 MCP = USB-C (5):** open standard, Anthropic, November 2024.
* **04 Roles (5):** host, client, server; tools, resources, prompts.
* **05 Claude connectors (5)** · **06 Permissions (5):** Decline / Allow once / Always allow.
* **07 Where it works (4):** Claude (Customize → Connectors), ChatGPT (Plugins), coding agents, LM Studio (mcp.json).
* **08 Registry (4):** ≈ 44,000 servers, no security vetting.
* **09 Your own server (5):** `from mcp.server import MCPServer`, `@mcp.tool()`.
* **10 Connecting (4):** `mcpServers`, local/remote, MCP Inspector.
* **11 An agent builds the server (4)** · **12 Security (5):** tool poisoning, injected text, too many permissions, rug pull.
* **13 Three layers (4)** · **14 Scale (4):** ≈ 0.5 bn SDK downloads a month, Agentic AI Foundation.
* **15 Break (5).**
* **16 Frameworks (5):** OpenAI Agents SDK, Claude Agent SDK, Google ADK, LangGraph, Microsoft Agent Framework, CrewAI.
* **17 When to use what (4)** · **18 A2A (4)** · **19 Exercise (4)** · **20 Homework (5)** · **21 Summary (3).**

## Terms
| Term | Plain words |
|---|---|
| MCP | a standard for connecting AI apps to tools and data |
| Host | the app where you work with AI (Claude, ChatGPT, VS Code) |
| MCP server | a program offering tools, resources and prompts |
| Connector | Claude’s name for a connected MCP server |
| Local / remote server | a program on your computer / an internet address with sign-in |
| Tool poisoning | a hidden command inside a tool description |
| Agent framework | a library that runs the agent loop: steps, memory, approvals |
| A2A | a standard for agents from different companies to talk |

## Recheck within 24 hours of class
1. The connectors path in Claude and the permission button labels; the ChatGPT path (Plugins).
2. The mcp Python SDK: version and class name (MCPServer).
3. The registry server count, MCP news (spec, foundation).
4. Framework versions.
