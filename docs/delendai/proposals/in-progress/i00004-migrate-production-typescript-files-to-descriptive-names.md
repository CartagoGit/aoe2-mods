---
id: i00004
title: "Migrate Production TypeScript Files to Descriptive Names"
kind: infra
status: in-progress
type: proposal
track: general
date: 2026-10-12
last-transition-id: 2be77f27-43b2-4008-ae64-1f81d73faff1
last-correlation-id: 2be77f27-43b2-4008-ae64-1f81d73faff1
last-transition-from: ready
last-transition-at: 2026-10-12T15:57:17.255Z
shipped-in:
  - "4e2a3cd1652497e8b8ef350ef96fb5f5cdc73539"
---

# i00004 — Migrate Production TypeScript Files to Descriptive Names

## Goal

Rename every production TypeScript module to a descriptive `<responsibility>.<type>.ts` name, remove `index.ts` entrypoints/barrels, and update every dependent import and repository reference without changing runtime behavior or moving code between domain folders.

## why

The current package entrypoints hide module ownership behind `index.ts` and several CLI filenames describe implementation history rather than responsibility. Explicit names make imports and files searchable, and expose the purpose of each production module at its path.

## non-goals

- No behavior, public identifiers, schemas, campaign contracts, or export format changes.
- No new services, abstractions, or package boundaries; only split an existing mixed helper module when needed to give existing responsibilities clear descriptive names.
- Keep existing domain directories. Test filenames may retain the established `*.test.ts` convention; update their imports and fixtures where they refer to renamed production paths.
- Do not modify `docs/design/**` or `tools/design/**`.
- No campaign content, engine behavior, adapter capability, or dependency changes.

## slices

- global_gate: lint

### S1 — Rename production TypeScript modules and update references
- **Status**: done
- **Files**: `packages/**/*.ts`, `tools/cli/**/*.ts`, `tests/**/*.ts`, `package.json`, `tsconfig.json`, `README.md`, `docs/architecture/overview.md`, `docs/standards/naming.md`, other non-design repository references found by search
- **Gate**: type

Scope includes all production files under `packages/` and `tools/cli/`, including currently unnamed `index.ts` modules and CLI entrypoints. It includes static and dynamic imports, scripts, TypeScript configuration, tests/fixtures, and non-design documentation references. The chosen basename must reflect the file's existing contents; preserve package/domain folders. Keep test files under their current test naming convention.
- review-state: done
- review-implementer: gpt-6-luna
- review-reviewer: gpt-6.1-sol
- review-log: approved by gpt-6.1-sol — verified at 4e2a3cd16524, validate exit 0, tests 45/45 — Independent formal naming review; code reviewed ca86c67 and identical integrated4e2a3cd. No game certification and no d00002 approval.

## acceptance

- No production module remains named `index.ts`; each production TypeScript file is named `<responsibility>.<type>.ts` with an ASCII kebab-case responsibility and an accurate type suffix.
- No production import resolves through a directory barrel or relies on implicit `index.ts`; all imports point to the concrete descriptive module.
- Every package script, CLI invocation, dynamic import, test fixture, TypeScript include, and non-design documentation reference to renamed paths resolves to the new path.
- `docs/standards/naming.md` states the descriptive production TypeScript filename rule and the test-file exception; `docs/architecture/overview.md` describes concrete module paths without barrel entrypoints.
- Existing package/domain directories remain unchanged and code behavior is unchanged.
- `bun install --frozen-lockfile`, `bun run validate`, and `bun run test:export` pass in the isolated unit.
- The diff contains no edits under `docs/design/**` or `tools/design/**`.
