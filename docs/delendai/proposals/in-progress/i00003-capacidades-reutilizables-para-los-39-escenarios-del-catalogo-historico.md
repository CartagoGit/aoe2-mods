---
id: i00003
title: "Capacidades reutilizables para los 39 escenarios del catalogo historico"
kind: infra
status: in-progress
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: 09d125c0-d3e9-4028-b0e6-d2c2a0b2de07
last-correlation-id: 09d125c0-d3e9-4028-b0e6-d2c2a0b2de07
last-transition-from: ready
last-transition-at: 2026-10-12T16:26:27.521Z
---

# i00003 — Capacidades reutilizables para los 39 escenarios del catalogo historico

## goal

El arquitecto amplía y acredita el perfil para cumplir literalmente docs/design/production-contract.md y docs/design/catalog.json. MiniMax no inventa condiciones ni sustituye una mecánica por tiempo. Entrega infraestructura reutilizable y fixtures adversariales antes de materializar historia.

## why

Los dossiers requieren contadores de entidades/entregas, fases con reloj relativo, recuperación, transporte, control de reservas y narrativa nativa; la existencia de bring/resource/task/spawn no acredita por sí sola estos compuestos.

## non-goals

- No crear contenido histórico ni cambiar nombres/IDs existentes.
- No afirmar QA del motor mediante tests estáticos.

## slices

- global_gate: e2e

### S1 — Contratos de fases y transacciones idempotentes
- **Status**: review
- **Files**: `packages/schemas`, `packages/gameplay-validation`, `packages/gameplay-state`, `packages/scenario-compiler`, `packages/aoe2-adapter/native-campaign.renderer.ts`, `tests/unit/phase-ledgers.test.ts`, `docs/decisions/0004-composed-objectives-profile-v2.md`, `docs/architecture/overview.md`
- **Gate**: e2e
- acceptance:
  - "Operaciones de objectivePlan explícitas, entrega por entidad sin doble cobro, recurso total atómico, supervivientes 6/8, phase-clock relativo; reusar bring/resource/diplomacy cuando sean suficientes."
  - "Pruebas de destrucción temprana, reentrada, múltiples predicados/tick, copias, pago único y guardado; ADR y migración sin renumerar IDs."
- review-state: in_review
- review-implementer: gpt-6
- review-log: requested_changes by gpt-6.1-sol — P1: duplicate exportedLedgers IDs pass structural validation/compilation and overwrite recipient identities in computeExportedLedgers. Independent reproduction on integrated 0fd5e0d: objective-a exports served twice from receive-a/receive-b; compiler accepts, served becomes [receiver-a], valid unit-a withdrawal cannot latch despite both deliveries. Reject duplicate ledger IDs per objective and add an adversarial compiler/reducer regression. P2: duplicate enemyRoster.mobilizations IDs also pass; reducer.find releases only first cohort. Reject duplicate wave IDs. Independent gate passes 86/86,289 expectations and export3variants/2round-trips, gameVerified=false; passing tests do not close these findings. No verdict on S2/S3/S4 or historical/native/game QA.
- review-log: resubmitted by gpt-6 — resubmitted; answers the request above: Correction bd843e4 by gpt-6 on integrated 5d3d479; independent reevaluation conforming, request next peer-review round; original implementation metadata gpt-6-luna is retained honestly.

### S2 — Mapa y transporte geográfico
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `tools/map`, `tests/maps`, `docs/architecture/geographic-maps.md`
- **Gate**: e2e
- acceptance:
  - "Rasterizar bbox/controles 300–400 con orientación calibrada, raster de relieve, footprint y puentes; no transformar una ruta que cruza agua en tierra ficticia."
  - "Fixture real de carga/desembarco, barco perdido, ruta alternativa, cliff impasable; perfcaps de catalog.json."

### S3 — Reserva militar y adaptación nativa
- **Status**: pending
- **DependsOn**: [S1, S2]
- **Files**: `packages/aoe2-adapter`, `tools/python`, `tests/fixtures/native-history`
- **Gate**: e2e
- acceptance:
  - "Implementar la IR acreditada: roster precolocado finito, tres movilizaciones una vez con avisos y preservación tras carga, sin economía oculta."
  - "Round-trip y xs-check; bun run test:export; navegación y fases con evidencia de motor requieren s00001 y tester."

### S4 — Plantillas de dos narradores y progreso
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `templates/native`, `docs/qa/history-capabilities`
- **Gate**: e2e
- acceptance:
  - "Native SequenceItems común→persona en intro/outro, captions EN/es, variantes progreso ausente/presente/ambas/desconocido, recomendación estática nunca bloqueante."
  - "Probar en AoE2 con hash/build/perfil guardado/locales; registrar capacidad implementada frente a GAME VERIFIED."

## acceptance

- Operaciones de objectivePlan explícitas, entrega por entidad sin doble cobro, recurso total atómico, supervivientes 6/8, phase-clock relativo; reusar bring/resource/diplomacy cuando sean suficientes.
- Pruebas de destrucción temprana, reentrada, múltiples predicados/tick, copias, pago único y guardado; ADR y migración sin renumerar IDs.
- Rasterizar bbox/controles 300–400 con orientación calibrada, raster de relieve, footprint y puentes; no transformar una ruta que cruza agua en tierra ficticia.
- Fixture real de carga/desembarco, barco perdido, ruta alternativa, cliff impasable; perfcaps de catalog.json.
- Implementar la IR acreditada: roster precolocado finito, tres movilizaciones una vez con avisos y preservación tras carga, sin economía oculta.
- Round-trip y xs-check; bun run test:export; navegación y fases con evidencia de motor requieren s00001 y tester.
- Native SequenceItems común→persona en intro/outro, captions EN/es, variantes progreso ausente/presente/ambas/desconocido, recomendación estática nunca bloqueante.
- Probar en AoE2 con hash/build/perfil guardado/locales; registrar capacidad implementada frente a GAME VERIFIED.
