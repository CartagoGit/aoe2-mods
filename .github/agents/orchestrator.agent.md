---
name: orchestrator
description: Multi-agent orchestrator
tools: [read, search, edit, execute, todo, agent, delendai:aoe2-mods/*]
user-invocable: true
---

This file is a thin redirector. The canonical contract lives in the `delendai` MCP server. On the first call of every turn, invoke `delendai_overview` and follow its `recommendedNextAction`. For non-trivial work, delegate through the swarm-coordination tools `overview` reports. Do not restate the workflow here — hardcoded tool names rot within days.