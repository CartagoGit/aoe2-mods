---
id: x00001
title: "Repair DelendAI startup validation expectations and the release branch reference"
kind: fix
status: review
type: proposal
track: general
date: 2026-11-05
shipped-in:
  - "337b792867c4345d36b1973ad9caf52cff53e0f6"
  - "4c008edcdc7de9c36f22f72d345288981a54bebe"
  - "575617c8c7db1441d78bd6beb8bba88de88ec4e2"
last-transition-id: b20f50fa-af17-4419-9b3b-9402a89ed06b
last-correlation-id: b20f50fa-af17-4419-9b3b-9402a89ed06b
last-transition-from: in-progress
last-transition-at: 2026-11-05T01:39:25.777Z
---

# x00001 — Repair DelendAI startup validation expectations and the release branch reference

## goal

Correct validationMatrix expectations to exit0 and the nonexistent release branch master to the actual main, preserving develop integration, official validation commands and forge governance; record official guard installation and verify startup using the configured server branch.

## why

The supplied 5 November boot log reports eight absent official Git guards, missing required validation expectations and an unverifiable release branch. Read-only GitHub API confirms actual branches develop/main, repository default main, no master, and explicit "Branch not protected" for main. The nonexistent name is not a credential failure. --branch=main in .vscode/mcp.json selects DelendAI source code, not the game repository branch.

## non-goals

- No remote protection/ruleset write, branch creation/deletion, release, governance bypass, error-reporting preference change or MCP source-branch change. No game/source/schema/campaign identity change.

## slices

- global_gate: type

### S1 — Correct the startup contract and verify official guards
- **Status**: review
- **Files**: `delendai.config.json`, `docs/qa/delendai-startup-recovery-20261105.md`, `docs/delendai/proposals/review/x00001-repair-delendai-startup-validation-expectations-and-the-release-branch-reference.md`
- **Gate**: type
- shipped-in: `6c5d6d0b1d03`
- review-state: in_review
- review-implementer: gpt-6

## acceptance

- Both existing project gate commands retain their exact values and declare expect=exit0; integration stays develop and release refers to actual main. The installed DelendAI schema accepts the config.
- Install/check the eight Git guards only through delendai guard install/status; no overwrite by hand and no generated merge driver copied from another project. Verify a real configured-main MCP startup has no missing-expect warning and no nonexistent-master governance blocker. Readable unprotected-main drift remains observed, never reported protected.
- Independently review the exact scoped diff, pass bun run validate and official publication. The implementer cannot approve this slice; no remote branch protection is modified.
