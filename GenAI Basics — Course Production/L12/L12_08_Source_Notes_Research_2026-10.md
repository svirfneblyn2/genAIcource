# L12 Source Notes: MCP and Agent Frameworks (research 2026-10-16)

Primary sources checked on 2026-10-16 for the v2 rebuild of Lesson 12. Replaces the September 2026 Drive package source notes.

## Images used in the deck

| File | What | Source |
|---|---|---|
| `assets/v2/img/claude_connectors.png` | claude.ai + → Connectors menu (slide 5) | own capture for L09 (2026-10-13), reused |
| `assets/v2/img/claude_permission.png` | claude.ai permission prompt for the Figma "Generate Diagram" tool (slide 6) | own capture for L09 (2026-10-13), reused |
| `assets/v2/img/claude_permission_zoom.png` | 2× Pillow crop of the prompt's header line (slide 6 inset) | derived from `claude_permission.png` |
| `assets/v2/img/chatgpt_plugins.png` | chatgpt.com Plugins page with the Add menu, Russian UI (slide 7) | own capture 2026-10-16 |
| `assets/v2/img/chatgpt_add_mcp_zoom.png` | 2× Pillow crop of "Добавить пользовательский сервер MCP" (slide 7 inset) | derived from `chatgpt_plugins.png` |
| `assets/v2/img/mcp_registry_crop.png` | registry.modelcontextprotocol.io: header + first two "Recently Updated" cards (slide 8) | Pillow crop of own capture 2026-10-16 (full capture removed; it is in git history) |

The schematics on slides 1–3, 13, 14 and 18 (n × m links, the MCP hub, nested layers, timeline, MCP vs A2A) are drawn in HTML/SVG in `deck_v2/build.py` with RU/EN labels; the earlier English-only PNGs (`n_times_m.png`, `mcp_hub.png`, `cover_right.png`) were removed on 2026-10-16.

Not used on slides but observed 2026-10-16: modelcontextprotocol.io intro page (spec version 2026-07-28; official "USB-C port for AI applications" analogy and the apps ↔ MCP ↔ data/tools diagram).

The slide 9 server code was run successfully with `mcp` 2.3.0 on 16.10.2026 (final course audit); it follows the mcp v2 Python SDK (`MCPServer`).

---


All values below were checked on 2026-10-16 against the URL given, unless marked otherwise.
UNVERIFIED = could not confirm from a primary source today.
The old package (Sept 2026) is mostly still current. The deltas that matter for a rebuild are under "CHANGES vs old package" at the end.

---

## 1. MCP basics

| Fact | Value | Source |
|---|---|---|
| Created by | Anthropic, announced **25 Nov 2024**. It describes MCP as "an open standard" for secure, two-way connections between data sources and AI tools. | https://www.anthropic.com/news/model-context-protocol |
| Governance | Anthropic donated MCP to the **Agentic AI Foundation (AAIF)** on **9 Dec 2025**. AAIF is a directed fund under the **Linux Foundation**, co-founded by Anthropic, Block and OpenAI, with support from Google, Microsoft, AWS, Cloudflare and Bloomberg. Founding projects: MCP, goose (Block), AGENTS.md (OpenAI). "The Model Context Protocol's governance model will remain unchanged." | https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation |
| Other AAIF projects (Aug 2026) | AGENTS.md, goose, MCP, agentgateway, and **A2A** (joined 17 Aug 2026) | https://aaif.io/blog/a2a-joins-aaif |
| Latest spec version | **2026-07-28** (status "Current"). Previous version: 2025-11-25. | https://modelcontextprotocol.io/specification/versioning |
| Spec release post | 28 Jul 2026. The headline change: MCP became **stateless**. No initialize handshake and no session ID; every request carries its own version and capabilities. | https://blog.modelcontextprotocol.io/posts/2026-07-28/ |
| Message format | JSON-RPC 2.0, UTF-8 | https://modelcontextprotocol.io/specification/latest |
| Three roles | **Host**: "LLM applications that initiate connections". **Client**: "Connectors within the host application". **Server**: "Services that provide context and capabilities". | https://modelcontextprotocol.io/specification/latest |
| Analogy used by the spec | The spec says it takes inspiration from the Language Server Protocol (LSP) | same |
| Server primitives | **Tools**: functions the AI model executes (model-controlled). **Resources**: context and data for the user or model. **Prompts**: templated messages and workflows for users. | same |
| Client primitives | **Elicitation**: a server asks the user for more information. Roots and Sampling still exist but are **Deprecated as of 2026-07-28** (see below). | same; https://modelcontextprotocol.io/specification/2026-07-28/deprecated |
| Deprecated in 2026-07-28 | **Roots** (migration: pass folders via tool parameters or config). **Sampling** (migration: call LLM provider APIs directly). **Logging** (migration: stderr or OpenTelemetry). **Dynamic Client Registration** (migration: Client ID Metadata Documents). These remain functional; earliest removal is in a revision released on or after 2027-07-28. The **HTTP+SSE transport** has been deprecated since 2025-03-26. | https://modelcontextprotocol.io/specification/2026-07-28/deprecated |
| Extensions (optional, opt-in) | **Tasks** (long-running jobs), **Skills over MCP**, and **MCP Apps** (interactive UI such as charts or forms rendered inline in chat) | https://modelcontextprotocol.io/specification/latest |
| Other 2026-07-28 changes | `server/discover` RPC. Multi Round-Trip Requests replace server-initiated requests. Cache hints (`ttlMs`, `cacheScope`) on list results. `Mcp-Method`/`Mcp-Name` HTTP headers. Tasks moved to an extension. | https://modelcontextprotocol.io/specification/2026-07-28/changelog |
| Transports | Two standard transports. **stdio**: "newline-delimited messages over the standard streams of a client-launched subprocess" (local). **Streamable HTTP**: "each message is an HTTP POST to a single MCP endpoint; replies arrive as a JSON object or a request-scoped SSE stream" (remote). Custom transports are allowed. | https://modelcontextprotocol.io/specification/2026-07-28/basic/transports |
| Auth | Authorization is **OPTIONAL**. For HTTP transports it is based on **OAuth 2.1** (IETF draft) plus RFC 9728 Protected Resource Metadata, RFC 8707 Resource Indicators, PKCE and RFC 9207 issuer validation. The MCP server acts as an OAuth 2.1 resource server. **stdio servers SHOULD NOT use it** and take credentials from the environment instead. Tokens must never go in the URL query string. | https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization |
| Human in the loop | The spec says there "SHOULD always be a human in the loop with the ability to deny tool invocations". Apps should show which tools are exposed, show indicators when a tool runs, and ask for confirmation. Clients MUST treat tool annotations as untrusted unless they come from trusted servers. | https://modelcontextprotocol.io/specification/2026-07-28/server/tools |

## 2. Registry and popular servers

| Fact | Value | Source |
|---|---|---|
| Official MCP Registry | https://registry.modelcontextprotocol.io. It is still **in preview**: "Breaking changes or data resets may occur before general availability." It stores **metadata only** (server.json), not code. Names are reverse-DNS namespaces verified via GitHub or DNS. It is meant to feed downstream aggregators and marketplaces, not to be used directly by hosts. Security scanning is delegated to npm, PyPI and Docker, and to aggregators. | https://modelcontextprotocol.io/registry/about |
| Registry size | **44,440 servers** (latest version of each). Of these, 28,568 list a remote (HTTP) endpoint and 17,491 list an installable package. I counted these myself by paging the public API `GET /v0.1/servers?version=latest` on 2026-10-16. The registry does not publish a count itself. It is in preview and includes many hobby entries. | https://registry.modelcontextprotocol.io/v0.1/servers?version=latest |
| Reference servers (maintained in the official repo) | Everything, Fetch, Filesystem, Git, Memory, Sequential Thinking, Time | https://github.com/modelcontextprotocol/servers |
| Archived reference servers | GitHub, GitLab, Google Drive, Google Maps, PostgreSQL, Puppeteer, Redis, Sentry, Slack (now maintained by Zencoder), SQLite, Brave Search, and others. They were replaced by vendor-run servers. **Do not teach `@modelcontextprotocol/server-github`**: npm marks it "Package no longer supported". | same; https://registry.npmjs.org/@modelcontextprotocol/server-github |
| Filesystem server | `@modelcontextprotocol/server-filesystem` v1.0.0 (npm, 2026-10) | npm registry |
| Vendor (official) remote servers found in the registry | **GitHub**: `io.github.github/github-mcp-server` v2.0.2, `https://api.githubcopilot.com/mcp/`. **Notion**: `com.notion/mcp`, `https://mcp.notion.com/mcp`. **Figma**: `com.figma.mcp/mcp`, `https://mcp.figma.com/mcp`. **Atlassian**: `com.atlassian/atlassian-mcp-server` v2.0.0, `https://mcp.atlassian.com/v2/mcp`. **Stripe**: `https://mcp.stripe.com`. **Microsoft Learn**: `https://learn.microsoft.com/api/mcp`. | registry API `/v0.1/servers/{name}/versions/latest` |
| Slack | Official Slack MCP server at `https://mcp.slack.com/mcp` (Streamable HTTP, OAuth; no SSE). Partner clients include Claude.ai, Claude Code, Perplexity and Cursor. | https://docs.slack.dev/ai/slack-mcp-server/ |
| Google Drive / Gmail | Official Google Workspace remote MCP servers: `https://drivemcp.googleapis.com/mcp/v1` and `https://gmailmcp.googleapis.com/mcp/v1`. Both are in the **Developer Preview Program**, use OAuth 2.0 and require a Cloud project. Not beginner-friendly. | https://developers.google.com/workspace/guides/configure-mcp-servers (search snippet; page not opened) |

## 3. Hosts and how a beginner adds a server (Oct 2026)

| Host | How to add | Source |
|---|---|---|
| **Claude.ai (web/desktop), remote servers** | **Customize > Connectors**, then "+ Add" > "Add custom connector". Enter a name and the remote MCP URL, then Continue, set auth, then Add. Available on **Free (limited to 1 custom connector)**, Pro and Max. On Team/Enterprise an Owner adds it under Organization settings > Connectors and members click "Connect". There is also a Connectors Directory of vetted connectors. | https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp ; https://support.claude.com/en/articles/11176164 |
| **Claude Desktop, local servers** | (a) **Desktop extensions (.mcpb)**: Settings > Extensions > "Browse extensions" > Install. One click, no JSON. (b) Manual: the Claude menu > Settings... > **Developer** > **Edit Config**. This opens `claude_desktop_config.json` (Windows `%APPDATA%\Claude\claude_desktop_config.json`, macOS `~/Library/Application Support/Claude/`). Add an `mcpServers` block, then **fully quit and restart** Claude. Check it via the "+" button > Connectors > Manage connectors. Logs are in `%APPDATA%\Claude\logs\mcp*.log`. | https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop ; https://modelcontextprotocol.io/docs/develop/connect-local-servers |
| Claude permissions | Support doc: "Only choose **'Allow always'** for tools you trust to run unsupervised". Tools can be disabled in the "Search and tools" menu. Team/Enterprise Owners can set each tool to **Always allow / Needs approval / Blocked** org-wide. The exact wording of the per-call dialog buttons ("Allow once" vs "Allow always") is **UNVERIFIED**; take a screenshot before teaching it. | same two support articles |
| **ChatGPT** | Custom MCP servers are now added as **plugins**: open the ChatGPT **Plugins** page, click "+" > "**Add custom MCP server**", then enter a name and a Server URL (or a Secure MCP Tunnel), choose auth (OAuth / No authentication), accept the risk warning, and "Create as a plugin" > install. ChatGPT is **remote only** (SSE or streaming HTTP); local stdio servers need a tunnel. Plans: **PARTLY VERIFIED (16.10.2026, final audit)**: OpenAI's ChatGPT developer-mode guide (developers.openai.com/api/docs/guides/developer-mode, seen via search result; direct fetch returned 404/403) lists Pro, Plus, Business, Enterprise and Edu accounts on the web, turned on under Settings → Apps → Advanced settings → Developer mode. The **Free plan is not listed**. One third-party guide (Boomi) says Plus/Pro get read-only custom connectors; not confirmed by OpenAI. The deck therefore says "your own server in ChatGPT needs a paid plan (developer mode); check yours". Earlier note: help.openai.com returned 403. The help article "Developer mode and full MCP connectors in ChatGPT" (12584461) exists. A search snippet says Business/Enterprise/Edu on web, with full MCP write actions in beta. DevDay 2026 (recap page also 403) was plugin-centric and added support for a *proposed* MCP Events spec. | https://developers.openai.com/api/docs/guides/custom-mcp-server ; https://developers.openai.com/apps-sdk/deploy/connect-chatgpt ; https://openai.com/index/devday-2026-recap/ (not readable) |
| **Gemini app (consumer)** | gemini.google.com > Settings > **Connected Apps** > Custom apps > "Add a custom app", then enter the MCP server URL. **Web only** for setup. Requirements: personal account, **18+ and in the US**, English only, Keep Activity on. "Gemini requires manual confirmation for any write actions." This is not available to most non-US students. | https://support.google.com/gemini/answer/17209137 |
| **Gemini CLI** | `gemini mcp add <name> <command-or-url>` or `mcpServers` in settings.json. The `trust` flag skips confirmations. **However**, from **18 Jun 2026** Gemini CLI stopped serving Google AI Pro/Ultra and free Code Assist individual users; they were moved to **Antigravity CLI**. Gemini CLI still works with paid API keys and enterprise licences. **Do not use Gemini CLI as the beginner demo.** | https://geminicli.com/docs/tools/mcp-server/ ; https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ (19 May 2026) |
| **Microsoft Copilot Studio** | Agent > **Tools** > Add a tool > New tool > **Model Context Protocol** (onboarding wizard). Enter server name, description and URL, then auth: None / API key / OAuth 2.0. Supports **Streamable HTTP only**; SSE has not been supported since Aug 2025. Supports tools and resources (not prompts). Requires generative orchestration. | https://learn.microsoft.com/en-us/microsoft-copilot-studio/mcp-add-existing-server-to-agent (updated 2026-10-15) |
| **VS Code + GitHub Copilot** | Extensions view, search `@mcp` (gallery) > Install. Or the command **MCP: Add Server**. Or `.vscode/mcp.json` (`servers` key) / `.mcp.json` (`mcpServers`). Shows a trust dialog on first start, and "You might be asked to confirm each tool invocation". | https://code.visualstudio.com/docs/copilot/customization/mcp-servers |
| **Cursor** | Marketplace "Add to Cursor" (one click), or `.cursor/mcp.json` / `~/.cursor/mcp.json`. By default it asks for approval before MCP tools run. | https://cursor.com/docs/context/mcp |
| **LM Studio** | MCP host since **0.3.17**. Right sidebar **Program** tab > Install > **Edit mcp.json** (Cursor-style `mcpServers`). Supports local and remote servers, plus "Add to LM Studio" deeplinks. It warns: "Never install MCPs from untrusted sources", and notes that big servers can overflow a small local model's context. Whether it shows a tool-call confirmation dialog is **UNVERIFIED** (not on the docs page today). | https://lmstudio.ai/docs/app/mcp |
| **Ollama** | **Not an MCP host itself.** Ollama's docs index has no MCP page. Ollama supplies models to MCP-capable hosts (Claude Code, Codex CLI, Goose, VS Code, etc. are listed as integrations). Community bridges exist. | https://docs.ollama.com/llms.txt |
| **Codex CLI** | `codex mcp add <name> -- <command>` or `[mcp_servers.<name>]` in `~/.codex/config.toml`. Supports stdio and Streamable HTTP. `codex mcp login` for OAuth. | https://learn.chatgpt.com/docs/extend/mcp?surface=cli |
| **Google ADK** | `McpToolset` connects an ADK agent to an MCP server (stdio or HTTP). | https://adk.dev/tools-custom/mcp-tools/ |
| **Microsoft Agent Framework / OpenAI Agents SDK / Claude Agent SDK** | All three include MCP clients (see section 7) | see section 7 |

## 4. MCP Inspector

| Fact | Value | Source |
|---|---|---|
| What it is | "the reference developer tool for testing and debugging MCP servers". One package with three clients: **Web** (default), **CLI** (`--cli`) and **TUI** (`--tui`). It handles both the legacy and the 2026-07-28 protocol eras. | https://modelcontextprotocol.io/docs/tools/inspector |
| Run | `npx @modelcontextprotocol/inspector` (add servers in the UI), or `npx @modelcontextprotocol/inspector <command to start server>`, e.g. `npx -y @modelcontextprotocol/inspector npx @modelcontextprotocol/server-filesystem ~/Desktop`. Remote: `--server-url https://.../mcp --transport http`. The launch URL includes a per-launch token and opens in the browser. | same |
| Requirement | **Node 22.19.0 or newer** | same |
| Version | `@modelcontextprotocol/inspector` **2.11.0** (npm, 2026-10-16) | https://registry.npmjs.org/@modelcontextprotocol/inspector/latest |
| From Python | `uv run mcp dev server.py` starts the server and opens Inspector (needs `npx` on PATH) | https://py.sdk.modelcontextprotocol.io/ |

## 5. Building a tiny server

| Fact | Value | Source |
|---|---|---|
| Python SDK | PyPI `mcp` **2.3.0** (2 Oct 2026). **v2 is the "current stable release line"** (2.0.0 released 28 Jul 2026). MIT licence. | https://pypi.org/pypi/mcp/json ; https://py.sdk.modelcontextprotocol.io/ |
| Python version | Conflicting: SDK docs say "Python **3.11+**", PyPI metadata says `>=3.10`, and the MCP tutorial says 3.10+. **Teach 3.11+.** | same; https://modelcontextprotocol.io/docs/develop/build-server |
| **FastMCP renamed** | In v2 `FastMCP` was **renamed to `MCPServer`**. `from mcp.server.fastmcp import FastMCP` now raises **ModuleNotFoundError**. New import: `from mcp.server import MCPServer` (also available as `mcp.server.mcpserver`). Note: the separate third-party package `fastmcp` (v4.1.0, Apache-2.0) still exists; do not confuse the two. | https://py.sdk.modelcontextprotocol.io/migration/ ; https://pypi.org/pypi/fastmcp/json |
| Install | `uv add "mcp[cli]"` or `pip install "mcp[cli]"` | https://py.sdk.modelcontextprotocol.io/ |
| Minimal example (official) | see below | same + build-server tutorial |
| TypeScript SDK | **v2 is current stable** (released 2026-07-27) and ships as two packages, **`@modelcontextprotocol/server`** and **`@modelcontextprotocol/client`** (both 2.3.1). The legacy `@modelcontextprotocol/sdk` 1.32.1 is on the v1.x **maintenance line** (spec ≤ 2025-11-25), with fixes for at least 6 months. Tutorial import: `import { McpServer } from "@modelcontextprotocol/server"; import { serveStdio } from "@modelcontextprotocol/server/stdio";` | https://ts.sdk.modelcontextprotocol.io/ ; https://modelcontextprotocol.io/docs/develop/build-server ; npm |
| Tier 1 SDKs on 2026-07-28 | TypeScript, Python, Go, C# (Rust in beta) | https://blog.modelcontextprotocol.io/posts/2026-07-28/ |

Minimal Python server (from the official SDK docs, with the `run` line taken from the tutorial):

```python
from mcp.server import MCPServer

mcp = MCPServer("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

The schema comes from the type hints and the description from the docstring ("The MCPServer class uses Python type hints and docstrings to automatically generate tool definitions").

Claude Desktop config on Windows (official tutorial pattern; the tutorial warns you may need the full path to `uv`, from `where uv`):

```json
{
  "mcpServers": {
    "demo": {
      "command": "uv",
      "args": ["--directory", "C:\\ABSOLUTE\\PATH\\TO\\demo", "run", "server.py"]
    }
  }
}
```

LM Studio uses the same `mcpServers` shape in its mcp.json, via Program > Install > Edit mcp.json.
Logging rule for stdio servers: never `print()` to stdout, because it corrupts the protocol. Log to stderr instead (tutorial).

## 6. Security

| Fact | Value | Source |
|---|---|---|
| Spec principles | User consent and control, data privacy, tool safety. "Tools represent arbitrary code execution and must be treated with appropriate caution". "Hosts must obtain explicit user consent before invoking any tool". "MCP itself cannot enforce these security principles at the protocol level". | https://modelcontextprotocol.io/specification/latest |
| Official Security Best Practices page | Sections: Confused Deputy, **Token Passthrough** (forbidden), SSRF, State Handle Hijacking, **Local MCP Server Compromise** (show the exact command before running it, sandbox, stdio preferred for local servers), OAuth URL validation, stdio-in-proxy risks, Mix-Up attacks, Localhost redirect impersonation, CIMD trust policies, **Scope Minimization** (least privilege). The page does **not** cover tool poisoning or prompt injection by name. | https://modelcontextprotocol.io/docs/tutorials/security/security_best_practices |
| Tool poisoning, rug pull, shadowing (origin) | Invariant Labs, **1 Apr 2025**. Tool poisoning: malicious instructions "embedded within MCP tool descriptions that are invisible to users but visible to AI models". Rug pull: a server "can change the tool description after the client has already approved it". Shadowing: one server's description changes how the agent uses another, trusted tool. | https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks |
| OWASP MCP Top 10 | Status is **Beta** (project page: "Phase 3 – Beta Release and Pilot Testing"). Items: MCP01 Token Mismanagement & Secret Exposure. MCP02 Privilege Escalation via Scope Creep. **MCP03 Tool Poisoning**. MCP04 Supply Chain Attacks. MCP05 Command Injection & Execution. **MCP06 Prompt Injection via Contextual Payloads**. MCP07 Insufficient AuthN/AuthZ. MCP08 Lack of Audit and Telemetry. **MCP09 Shadow MCP Servers**. MCP10 Context Injection & Over-Sharing. | https://owasp.org/www-project-mcp-top-10/ |
| Vendor guidance (Anthropic) | Custom connectors are "not verified by Anthropic". Connect only trusted organizations and limit OAuth scopes. Malicious servers may hide instructions. Developers can change tool behaviour without notice (rug pull). Only "Allow always" for tools you trust unsupervised. Disable write tools you don't need. | https://support.claude.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp |
| Vendor guidance (Google/OpenAI/LM Studio) | Gemini: Google does not control or secure third-party MCP servers, and write actions need manual confirmation. OpenAI: custom MCP servers are "not developed or verified by OpenAI", with a risk warning in the add flow and an explicit prompt-injection warning. LM Studio: "Never install MCPs from untrusted sources." | sources in section 3 |
| Registry trust | The registry verifies only namespace ownership. Security scanning is left to package registries and aggregators. **Being listed does not mean a server is safe.** | https://modelcontextprotocol.io/registry/about |

## 7. Agent frameworks (versions from PyPI/npm, 2026-10-16)

| Framework | Latest version (date) | One-line purpose | Licence | MCP | Source |
|---|---|---|---|---|---|
| OpenAI Agents SDK | `openai-agents` **0.24.0** (15 Oct 2026); JS `@openai/agents` 0.20.0 | "lightweight, easy-to-use package with very few abstractions". Primitives: agents, handoffs/agents-as-tools, guardrails, plus sessions and tracing. | MIT | Yes (hosted MCP, Streamable HTTP, stdio) | https://openai.github.io/openai-agents-python/ |
| Claude Agent SDK | `claude-agent-sdk` **0.2.168** (15 Oct 2026); TS `@anthropic-ai/claude-agent-sdk` 0.3.301 | "the same tools, agent loop, and context management that power Claude Code, programmable in Python and TypeScript" | Repo MIT, but **use is governed by Anthropic Commercial Terms** | Yes | https://code.claude.com/docs/en/agent-sdk/overview |
| Google ADK | `google-adk` **2.12.0** (13 Oct 2026); JS `@google/adk` 2.3.0 | Agent Development Kit (Python, TS, Go, Java, Kotlin) | Apache-2.0 | `McpToolset` | https://adk.dev/tools-custom/mcp-tools/ |
| LangGraph | `langgraph` **1.2.15** (12 Oct 2026); LangChain 1.4.6 | "Building stateful, multi-actor applications with LLMs". A low-level orchestration runtime (durable execution, human-in-the-loop, persistence). | MIT | via LangChain MCP adapters | https://docs.langchain.com/oss/python/langgraph/overview |
| CrewAI | `crewai` **1.15.28** (14 Oct 2026) | "orchestrating role-playing, autonomous AI agents" (teams of agents with roles) | MIT (GitHub) | UNVERIFIED (not checked today) | https://pypi.org/project/crewai/ |
| Microsoft Agent Framework | `agent-framework` **1.22.0** (15 Oct 2026); .NET, Python, Go (Go in preview) | Agents + workflows. Microsoft calls it "the direct successor" of **AutoGen and Semantic Kernel**, "the next generation of both". | MIT | Yes (MCP clients built in) | https://learn.microsoft.com/en-us/agent-framework/overview/ |
| AutoGen | `autogen-agentchat` 0.7.5 (last release 30 Sep 2025) | **Maintenance mode**: "New users should start with Microsoft Agent Framework" | MIT | n/a | https://github.com/microsoft/autogen |
| Semantic Kernel | 1.45.0 (6 Oct 2026) | Still released; superseded by Agent Framework for new agent work | MIT | n/a | PyPI |
| LlamaIndex | `llama-index` **0.14.25** (21 Sep 2026) | "Interface between LLMs and your data" (RAG/data agents) | MIT | UNVERIFIED (not checked today) | https://pypi.org/project/llama-index/ |
| Pydantic AI | `pydantic-ai` **2.57.0** (16 Oct 2026) | "AI Agent Framework, the Pydantic way" (type-safe) | MIT | UNVERIFIED (not checked today) | https://pydantic.dev/docs/ai/ |

**A2A (Agent2Agent)**: created by Google (Apr 2025) and donated to the Linux Foundation. **A2A v1.0, "the first stable specification", shipped March 2026**. The latest GitHub release is v1.0.1 (28 May 2026); `a2a-sdk` (Python) is 1.2.2, Apache-2.0. A2A **joined AAIF on 17 Aug 2026**. It is backed by 150+ organizations. In the project's own words, "MCP is for agent-to-tool communication", while "A2A is for agent-to-agent communication".
Sources: https://a2a-protocol.org/latest/ ; https://aaif.io/blog/a2a-joins-aaif ; https://api.github.com/repos/a2aproject/A2A/releases/latest

## 8. Adoption numbers (with dates)

| Number | Date | Source |
|---|---|---|
| ">10,000 active public MCP servers", "97M+ monthly SDK downloads" (Python+TS), ">75 connectors in Claude's directory" | 9 Dec 2025 | Anthropic AAIF post |
| "close to half-a-billion downloads a month" across Tier 1 SDKs. TypeScript and Python SDKs each passed "1 billion total downloads". | 28 Jul 2026 | https://blog.modelcontextprotocol.io/posts/2026-07-28/ |
| npm `@modelcontextprotocol/sdk`: **273.3M downloads** from 13 Sep to 12 Oct 2026. This is the legacy v1 package only; the v2 packages are counted separately. | 2026-10-16 | https://api.npmjs.org/downloads/point/last-month/@modelcontextprotocol/sdk |
| PyPI `mcp`: **235.2M downloads in the last month**, 63.4M in the last week | 2026-10-16 | https://pypistats.org/api/packages/mcp/recent |
| Official MCP Registry: **44,440 servers** (latest versions; my own count via the API) | 2026-10-16 | registry API |
| AAIF ">250 members" | Aug 2026 | search summary of AAIF/Axios; **UNVERIFIED** on the primary page |

Use the 28 Jul 2026 blog number for slides ("~0.5 billion SDK downloads per month"). Add the registry count as "40,000+ servers listed in the official registry (Oct 2026)". Note that a listing is not a quality signal.

---

## CHANGES vs old package (Sept 2026) — must fix

1. The old package's Python SDK v2 example is correct in spirit, but any `FastMCP` import is now **wrong**. Use `from mcp.server import MCPServer`.
2. Python requirement: the old package said 3.10+. **The SDK docs now say 3.11+.**
3. TypeScript: the old `@modelcontextprotocol/sdk` is now the v1 maintenance line. v2 uses `@modelcontextprotocol/server` and `@modelcontextprotocol/client`.
4. The spec version 2026-07-28 is still current. **Sampling, Roots and Logging are now Deprecated.** Do not present them as core client features for beginners; show Tools/Resources/Prompts plus Elicitation.
5. The `@modelcontextprotocol/server-github` npm package is deprecated. Use GitHub's own server (`api.githubcopilot.com/mcp/`).
6. Gemini CLI is no longer a viable free beginner host (since 18 Jun 2026 → Antigravity CLI). The Gemini consumer app MCP is US-only, 18+, English.
7. ChatGPT now adds custom MCP servers as **"plugins"** (Plugins page > Add custom MCP server). Developer mode on paid plans (Plus/Pro/Business/Enterprise/Edu); Free not listed (see section 3).
8. Claude.ai menu path is now **Customize > Connectors** (not Settings > Connectors). Free plan: 1 custom connector.
9. AutoGen is in maintenance mode; Microsoft Agent Framework 1.x is the successor (MIT).
10. A2A is now v1.0 and under AAIF, the same foundation as MCP.
11. MCP Inspector 2.x needs Node ≥ 22.19.0 and has a `--cli` and `--tui` mode.

## Still UNVERIFIED

- The exact Claude per-call permission dialog button labels ("Allow once" / "Always allow"). Take a fresh screenshot.
- ChatGPT: whether Plus/Pro custom servers are read-only (one third-party claim); the plan list itself is from OpenAI's developer-mode guide via search (direct fetch failed).
- Whether Claude's ready-made Google Drive connector is available on the Free plan. The homework therefore uses the custom connector (Free: 1, VERIFIED above) as the main free path, LM Studio only for those who code.
- The LM Studio tool-call confirmation dialog.
- MCP support pages for CrewAI, LlamaIndex and Pydantic AI (believed yes; not checked today).
- AAIF member count (>250).
- The Antigravity CLI command name and its MCP support.
