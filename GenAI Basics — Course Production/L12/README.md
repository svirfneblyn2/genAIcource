# Lesson 12: MCP and Agent Frameworks

## Status: deck v2 (21 slides, 90 min), facts as of 2026-10-16, audits applied

Rebuilt from the September 2026 Drive package (`12 — MCP, Tools and Agent Frameworks — DONE`: engineering-heavy pptx with JSON-RPC, the protocol handshake and an MCP Boundary Canvas). The v2 deck is a beginner tour: why a standard (3 × 3 vs 3 + 3), MCP as a USB-C plug, host / client / server and tools / resources / prompts, Claude connectors and the permission prompt (own captures reused from L09), where MCP works, the official registry, a 10-line server (mcp SDK v2 `MCPServer`), connecting it, a coding-agent prompt, security (tool poisoning, injected text, permissions, rug pull), three layers (function calling, MCP, framework), scale, then frameworks, a complexity ladder, A2A, an exercise, homework and summary.

## Source of truth
- **Generator:** `deck_v2/build.py` + `style.css` + `deck.js` (same engine as L06, L10, L11). `python deck_v2/build.py` or `--no-pdf`.
- **Instructor scripts** `L12_02_*`: `python deck_v2/make_docs.py`.
- **Decks:** `presentation_L12_MCP_and_Agent_Frameworks_v2.html` / `_EN_v2.html` + PDFs.
- **Facts:** `L12_08_Source_Notes_Research_2026-10.md` (checked 2026-10-16, image credits).
- **Companion documents:** cheatsheets with the 24 h recheck list (`L12_00_*`), homework (`L12_05_*`).

## Before class
Check the Claude connectors path and the permission-prompt labels (screenshots are from 2026-10-13). The slide 9 code is a reference and was not executed for this build: `pip install mcp` (Python 3.11+) and test it in MCP Inspector before showing it.
