---
id: x00005
title: "The project runs the stable DelendAI through a runtime link, with no machine path"
kind: fix
status: ready
type: proposal
track: general
date: 2026-11-24
---

# x00005 — The project runs the stable DelendAI through a runtime link, with no machine path

## goal

Both host entries start the canonical launch through the gitignored .cache/delendai-runtime link to the stable channel, so the project works the same on any machine.

## why

The VS Code entry started a development checkout by absolute path with --branch=main: it fails on any other machine and runs unreleased code.

## non-goals

- TODO: what this proposal deliberately skips.

## slices

- global_gate: type

### S1 — runtime link and canonical host entries
- **Status**: pending
- **Files**: `tools/cli/delendai-runtime.script.ts`, `package.json`, `.mcp.json`, `.vscode/mcp.json`
- **Gate**: type
- acceptance:
  - "bun run validate passes"
  - "the MCP server answers initialize and tools/list through .mcp.json"
  - "no tracked file names /home/ or the delendai development checkout"

## acceptance

- bun run validate passes
- the MCP server answers initialize and tools/list through .mcp.json
- no tracked file names /home/ or the delendai development checkout
