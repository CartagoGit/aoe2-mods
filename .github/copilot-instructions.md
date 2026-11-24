# Copilot Instructions - Workspace

## Source of truth

The MCP server `DelendAI:AOE2-mods` rules. Do NOT re-derive workflow from docs:

- Entry point: `delendai_overview` (ALWAYS the first call) — it lists the server's tools, plugins and a `recommendedNextAction`.
- The multi-agent proposal workflow (`delendai_auto_work`, `delendai_continue_proposal`, `delendai_delegate`, `delendai_agent_lock`, quality gates via `delendai_get_validation_matrix`) is available when the server loads the `proposals` plugin (`delendai --plugins=proposals`).

## Lane

- Default model: `<your-model>`.
- MCP payload first, one atomic slice, minimal validation, serial continuity.
- Orchestration threshold: keep the root chat to coordination calls. Delegate any slice that needs more than 3 tool calls, multiple files, or repeated MCP reads.
- Every final message ends with ONE close marker line (see the close-markers constant of this host).
