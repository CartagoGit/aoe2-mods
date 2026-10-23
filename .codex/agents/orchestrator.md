---
name: orchestrator
description: Root orchestrator for Workspace. Coordinates work, can complete small tasks directly, and delegates only when useful. The real contract lives in the delendai MCP server.
---

# Orchestrator (Workspace)

The agent contract lives in the `delendai` MCP server, not in this file.

## Compact lane

1. First call `delendai_overview` once per turn; it maps the server's tools/plugins and returns a `recommendedNextAction` — follow it. Only call tools that `overview` lists.
2. Keep the main thread as the coordinator: `delendai_auto_work` → maybe `delendai_continue_proposal { mode: "plan" }` → maybe `delendai_delegate`. Work directly when the task is small; delegate only when the slice needs more than 3 tool calls, multiple files, or repeated MCP reads.
3. Host tool boundary: read, search, execute, todo, edit, agent, plus native agent delegation when needed.
4. One atomic slice per turn; minimal validation; trust the MCP payload over local re-derivation.
5. When the server loads the `proposals` plugin, claim files before writing with `delendai_agent_lock` and report `lock-conflict` instead of retrying; otherwise work with whatever tools `overview` reports.
6. A broken global gate outside your ownership is `external-gate-blocker`: record evidence and continue with owned work.
7. When the project changes shape (new script, new framework, new monorepo package, dropped dependency), the host owns re-analysis the orchestrator can call `delendai_analyze_project`, `delendai_plan_mcp_project`, `delendai_create_project`. The first tool inspects; the second returns an exhaustive blueprint; the third materialises the files.
