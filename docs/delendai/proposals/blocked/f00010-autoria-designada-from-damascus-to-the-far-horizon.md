---
id: f00010
title: "Autoria designada: From Damascus to the Far Horizon"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: b1a11751-fc17-47ec-a614-d31adfc62768
last-correlation-id: b1a11751-fc17-47ec-a614-d31adfc62768
last-transition-from: ready
last-transition-at: 2026-10-12T14:24:55.142Z
---

# f00010 — Autoria designada: From Damascus to the Far Horizon

## goal

MiniMax M3.1 materializa umayyads exclusivamente según docs/wiki/umayyads/12-production-blueprint.md, 13-narrator-bible.md, sus 5 dossiers y docs/design/catalog.json. El arquitecto ya fija historia, voz, mapas, objetivos, dificultad y pantallas.

## why

El usuario pide contenido mecánico con decisiones históricas/geográficas/arquitectónicas preparadas y revisión real.

## non-goals

- No rediseñar arquitectura/historia/balance por iniciativa propia.
- No presentar planos/estimaciones como mapas jugados ni publicar sin autorización.

## slices

- global_gate: e2e

### S1 — Verificar el contrato cerrado, sin redisenarlo
- **Status**: pending
- **Files**: `docs/qa/umayyads/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Comparar docs/wiki/umayyads/12-production-blueprint.md y docs/design/catalog.json: identidad, narrador, fechas, fuentes, mapas, pantallas y tres perfiles; informar discrepancias al arquitecto, no decidir historia/balance nuevo."
  - "Fuente en inglés sourceLocale=en, español completo, antecesora opcional y rutas exactas. Gates previos: d00001/i00002 revisadas e integradas; piloto f00001/f00002; i00003 capacidades + s00001 motor para entrega."

### S2 — Metadatos, todas las pantallas y manifiestos en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/umayyads/campaign.json`, `staging/campaigns/umayyads/native`, `staging/campaigns/umayyads/assets`
- **Gate**: e2e
- acceptance:
  - "Implementar literalmente campaña/umayyads en catalog.json; EN/es-ES todas las claves de pantallas, dos narradores, finales y avisos, 17 destinos con estado real; conservar IDs y recomendaciones no bloqueantes."
  - "Imágenes licenciadas u originales según artDirection; research references no se copian como escenas antiguas; ejecutar staging:check --partial. No generar audio/arte pagado ni publicar."

### S3 — Materializar 01-ledgers-of-damascus
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/01-ledgers-of-damascus`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/umayyads/scenarios/01-ledgers-of-damascus.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S4 — Materializar 02-stone-and-memory
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `staging/campaigns/umayyads/scenarios/02-stone-and-memory`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/umayyads/scenarios/02-stone-and-memory.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S5 — Materializar 03-the-western-shore
- **Status**: pending
- **DependsOn**: [S4]
- **Files**: `staging/campaigns/umayyads/scenarios/03-the-western-shore`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/umayyads/scenarios/03-the-western-shore.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S6 — Materializar 04-the-narrow-sea
- **Status**: pending
- **DependsOn**: [S5]
- **Files**: `staging/campaigns/umayyads/scenarios/04-the-narrow-sea`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/umayyads/scenarios/04-the-narrow-sea.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S7 — Materializar 05-the-last-crossing
- **Status**: pending
- **DependsOn**: [S6]
- **Files**: `staging/campaigns/umayyads/scenarios/05-the-last-crossing`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/umayyads/scenarios/05-the-last-crossing.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S8 — Materializacion conjunta, IDs y entrega comprobada
- **Status**: pending
- **DependsOn**: [S7]
- **Files**: `staging/campaigns/umayyads`, `campaigns/umayyads`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/umayyads/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover bundle completo junto a IDs/glosario en la misma entrega; bun run validate, build/export/candidate reales; 17 textos revisados y assets/audio con licencias/hash antes de release."
  - "Ejecutar QA de cada dossier y playtests de docs/design/production-contract.md; mediciones hash/build/locale/dificultad, pedir al arquitecto calibración justificada, no declarar perfecto por tests. Revisión independiente y work publish; subir mods requiere autorización separada."

## acceptance

- Comparar docs/wiki/umayyads/12-production-blueprint.md y docs/design/catalog.json: identidad, narrador, fechas, fuentes, mapas, pantallas y tres perfiles; informar discrepancias al arquitecto, no decidir historia/balance nuevo.
- Fuente en inglés sourceLocale=en, español completo, antecesora opcional y rutas exactas. Gates previos: d00001/i00002 revisadas e integradas; piloto f00001/f00002; i00003 capacidades + s00001 motor para entrega.
- Implementar literalmente campaña/umayyads en catalog.json; EN/es-ES todas las claves de pantallas, dos narradores, finales y avisos, 17 destinos con estado real; conservar IDs y recomendaciones no bloqueantes.
- Imágenes licenciadas u originales según artDirection; research references no se copian como escenas antiguas; ejecutar staging:check --partial. No generar audio/arte pagado ni publicar.
- Única especificación: docs/wiki/umayyads/scenarios/01-ledgers-of-damascus.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Única especificación: docs/wiki/umayyads/scenarios/02-stone-and-memory.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Única especificación: docs/wiki/umayyads/scenarios/03-the-western-shore.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Única especificación: docs/wiki/umayyads/scenarios/04-the-narrow-sea.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Única especificación: docs/wiki/umayyads/scenarios/05-the-last-crossing.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Promover bundle completo junto a IDs/glosario en la misma entrega; bun run validate, build/export/candidate reales; 17 textos revisados y assets/audio con licencias/hash antes de release.
- Ejecutar QA de cada dossier y playtests de docs/design/production-contract.md; mediciones hash/build/locale/dificultad, pedir al arquitecto calibración justificada, no declarar perfecto por tests. Revisión independiente y work publish; subir mods requiere autorización separada.
