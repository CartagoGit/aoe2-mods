---
id: i00002
title: "Autoria en ingles y localizacion canonica explicita por campana"
kind: infra
status: in-progress
type: proposal
track: campaign-design
date: 2026-10-12
---

# i00002 — Autoria en ingles y localizacion canonica explicita por campana

## goal

Aplicar la instrucción posterior del propietario: inglés en como idioma inicial para títulos y contenido nuevo, español es-ES completo para el jugador. Añadir sourceLocale explícito por campaña, reutilizarlo en validación y asignación de IDs, conservar el fixture anterior en es-ES sin renumerar IDs y documentar migración. No cambiar identidades técnicas/publicId.

## why

La instrucción del propietario cambia el idioma inicial a inglés; los validadores y CLI actuales presuponen es-ES y deben dejar de hacerlo.

## non-goals

- No autoaprobar traducciones ni suponer fallback del juego.

## slices

- global_gate: e2e

### S1 — Seleccionar locale fuente y eliminar supuestos españoles en herramientas
- **Status**: pending
- **Files**: `packages/schemas`, `packages/localization`, `packages/campaign-compiler`, `tools/cli`, `campaigns/technical-pilot/campaign.json`, `tests/unit/localization.test.ts`, `docs/decisions/0003-english-authoring.md`, `docs/guides/localization.md`
- **Gate**: e2e
- acceptance:
  - "Campañas nuevas sourceLocale=en; fixture existente declara es-ES; JSON Schema, CLI y validador usan la fuente declarada."
  - "Pruebas significativas de catálogo fuente inglés y falta de sourceLocale, integridad de claves/placeholders y IDs existentes estables."
  - "bun run validate pasa y revisión formal independiente requerida antes de cerrar."

## acceptance

- Campañas nuevas sourceLocale=en; fixture existente declara es-ES; JSON Schema, CLI y validador usan la fuente declarada.
- Pruebas significativas de catálogo fuente inglés y falta de sourceLocale, integridad de claves/placeholders y IDs existentes estables.
- bun run validate pasa y revisión formal independiente requerida antes de cerrar.
