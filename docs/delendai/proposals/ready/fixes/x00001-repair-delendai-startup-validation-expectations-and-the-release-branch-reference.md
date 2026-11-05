---
id: x00001
title: "Repair DelendAI startup validation expectations and the release branch reference"
kind: fix
status: ready
type: proposal
track: general
date: 2026-11-05
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
- **Status**: pending
- **Files**: `delendai.config.json`, `docs/qa/delendai-startup-recovery-20261105.md`, `docs/delendai/proposals/ready/fixes/x00001-repair-delendai-startup-validation-expectations-and-the-release-branch-reference.md`
- **Gate**: type

## acceptance

- Both existing project gate commands retain their exact values and declare expect=exit0; integration stays develop and release refers to actual main. The installed DelendAI schema accepts the config.
- Install/check the eight Git guards only through delendai guard install/status; no overwrite by hand and no generated merge driver copied from another project. Verify a real configured-main MCP startup has no missing-expect warning and no nonexistent-master governance blocker. Readable unprotected-main drift remains observed, never reported protected.
- Independently review the exact scoped diff, pass bun run validate and official publication. The implementer cannot approve this slice; no remote branch protection is modified.
