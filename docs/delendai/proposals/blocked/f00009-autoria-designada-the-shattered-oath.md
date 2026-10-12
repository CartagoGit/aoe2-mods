---
id: f00009
title: "Autoria designada: The Shattered Oath"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: 9386a406-9f49-4140-b53c-c7e034c50896
last-correlation-id: 9386a406-9f49-4140-b53c-c7e034c50896
last-transition-from: ready
last-transition-at: 2026-10-12T14:24:45.866Z
---

# f00009 — Autoria designada: The Shattered Oath

## goal

MiniMax M3.1 materializa first-fitna exclusivamente según docs/wiki/first-fitna/12-production-blueprint.md, 13-narrator-bible.md, sus 5 dossiers y docs/design/catalog.json. El arquitecto ya fija historia, voz, mapas, objetivos, dificultad y pantallas.

## why

El usuario pide contenido mecánico con decisiones históricas/geográficas/arquitectónicas preparadas y revisión real.

## non-goals

- No rediseñar arquitectura/historia/balance por iniciativa propia.
- No presentar planos/estimaciones como mapas jugados ni publicar sin autorización.

## slices

- global_gate: e2e

### S1 — Verificar el contrato cerrado, sin redisenarlo
- **Status**: pending
- **Files**: `docs/qa/first-fitna/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Comparar docs/wiki/first-fitna/12-production-blueprint.md y docs/design/catalog.json: identidad, narrador, fechas, fuentes, mapas, pantallas y tres perfiles; informar discrepancias al arquitecto, no decidir historia/balance nuevo."
  - "Fuente en inglés sourceLocale=en, español completo, antecesora opcional y rutas exactas. Gates previos: d00001/i00002 revisadas e integradas; piloto f00001/f00002; i00003 capacidades + s00001 motor para entrega."

### S2 — Metadatos, todas las pantallas y manifiestos en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/first-fitna/campaign.json`, `staging/campaigns/first-fitna/native`, `staging/campaigns/first-fitna/assets`
- **Gate**: e2e
- acceptance:
  - "Implementar literalmente campaña/first-fitna en catalog.json; EN/es-ES todas las claves de pantallas, dos narradores, finales y avisos, 17 destinos con estado real; conservar IDs y recomendaciones no bloqueantes."
  - "Imágenes licenciadas u originales según artDirection; research references no se copian como escenas antiguas; ejecutar staging:check --partial. No generar audio/arte pagado ni publicar."

### S3 — Materializar 01-news-from-medina
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-fitna/scenarios/01-news-from-medina`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/first-fitna/scenarios/01-news-from-medina.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S4 — Materializar 02-between-the-camps
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `staging/campaigns/first-fitna/scenarios/02-between-the-camps`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/first-fitna/scenarios/02-between-the-camps.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S5 — Materializar 03-water-and-words
- **Status**: pending
- **DependsOn**: [S4]
- **Files**: `staging/campaigns/first-fitna/scenarios/03-water-and-words`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/first-fitna/scenarios/03-water-and-words.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S6 — Materializar 04-the-canal-road
- **Status**: pending
- **DependsOn**: [S5]
- **Files**: `staging/campaigns/first-fitna/scenarios/04-the-canal-road`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/first-fitna/scenarios/04-the-canal-road.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S7 — Materializar 05-two-archives
- **Status**: pending
- **DependsOn**: [S6]
- **Files**: `staging/campaigns/first-fitna/scenarios/05-two-archives`
- **Gate**: e2e
- acceptance:
  - "Única especificación: docs/wiki/first-fitna/scenarios/05-two-archives.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto."
  - "Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial."

### S8 — Materializacion conjunta, IDs y entrega comprobada
- **Status**: pending
- **DependsOn**: [S7]
- **Files**: `staging/campaigns/first-fitna`, `campaigns/first-fitna`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/first-fitna/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover bundle completo junto a IDs/glosario en la misma entrega; bun run validate, build/export/candidate reales; 17 textos revisados y assets/audio con licencias/hash antes de release."
  - "Ejecutar QA de cada dossier y playtests de docs/design/production-contract.md; mediciones hash/build/locale/dificultad, pedir al arquitecto calibración justificada, no declarar perfecto por tests. Revisión independiente y work publish; subir mods requiere autorización separada."

## acceptance

- Comparar docs/wiki/first-fitna/12-production-blueprint.md y docs/design/catalog.json: identidad, narrador, fechas, fuentes, mapas, pantallas y tres perfiles; informar discrepancias al arquitecto, no decidir historia/balance nuevo.
- Fuente en inglés sourceLocale=en, español completo, antecesora opcional y rutas exactas. Gates previos: d00001/i00002 revisadas e integradas; piloto f00001/f00002; i00003 capacidades + s00001 motor para entrega.
- Implementar literalmente campaña/first-fitna en catalog.json; EN/es-ES todas las claves de pantallas, dos narradores, finales y avisos, 17 destinos con estado real; conservar IDs y recomendaciones no bloqueantes.
- Imágenes licenciadas u originales según artDirection; research references no se copian como escenas antiguas; ejecutar staging:check --partial. No generar audio/arte pagado ni publicar.
- Única especificación: docs/wiki/first-fitna/scenarios/01-news-from-medina.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Única especificación: docs/wiki/first-fitna/scenarios/02-between-the-camps.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Única especificación: docs/wiki/first-fitna/scenarios/03-water-and-words.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Única especificación: docs/wiki/first-fitna/scenarios/04-the-canal-road.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Única especificación: docs/wiki/first-fitna/scenarios/05-two-archives.md y catalog.json; copiar objetivoPlan, entidades, estado, eventos, geografía/SVG, presupuesto easy/standard/hard y QA. Ninguna decisión histórica, ruta nueva, refuerzo infinito o temporizador sustituto.
- Resolver IDs solo desde catálogo fijado; verificar footprint/transporte, estados tempranos y ledger; staging:check --partial hasta estar todos; el último ejecuta staging:check sin --partial.
- Promover bundle completo junto a IDs/glosario en la misma entrega; bun run validate, build/export/candidate reales; 17 textos revisados y assets/audio con licencias/hash antes de release.
- Ejecutar QA de cada dossier y playtests de docs/design/production-contract.md; mediciones hash/build/locale/dificultad, pedir al arquitecto calibración justificada, no declarar perfecto por tests. Revisión independiente y work publish; subir mods requiere autorización separada.
