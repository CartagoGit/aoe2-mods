---
id: i00006
title: "Presencia local de checkpoint sin prolongarla hasta la victoria"
kind: infra
status: ready
type: proposal
track: campaign-design
date: 2026-10-17
---

# i00006 — Presencia local de checkpoint sin prolongarla hasta la victoria

## goal

Añadir una capacidad reutilizable explícita de presencia simultánea solo al completar un objetivo intermedio, conservando literalmente current-entity-presence y su reevaluación terminal. Resolver el requisito observado en imperial-church/32 sin cambiar IDs, rangos ni semánticas aprobadas.

## why

Revisión independiente de f35ad5c: o2 requiere cuatro originales a pie al oeste y dos montados en el centro; o3 exige ambos mínimos al suroeste. Noventa combinaciones y todos los latches pasan, pero tick/enter-phase terminal quedan bloqueados porque current-entity-presence reevalúa los predecesores. ADR0005 y su implementación son coherentes: falta una capacidad distinta. No sustituir por arrived, flags, actores inmovilizados ni eliminar controles finales.

## non-goals

- Cambiar la semántica o forma serializada de contratos existentes que no opten por la nueva capacidad.
- Renumerar cadenas, IDs, campañas o perfiles del catálogo; producir campañas nativas completas.
- Afirmar observer nativo, terreno histórico o balance sin evidencia del motor.

## slices

- global_gate: e2e

### S1 — Contrato aditivo y referencia de checkpoint
- **Status**: review
- **Files**: `packages/schemas`, `packages/gameplay-state`, `packages/gameplay-validation`, `packages/scenario-compiler`, `tools/design/episode_dossier.validator.py`, `tools/design/test_design.py`, `tests/unit/checkpoint-presence.test.ts`, `docs/design/checkpoint-entity-presence.md`, `docs/decisions/0006-checkpoint-entity-presence.md`
- **Gate**: e2e
- acceptance:
  - "Nuevo kind estricto checkpoint-entity-presence con identidades, destinos y mínimo; requiere batch fresco monotónico al latch, no admite record-predicate, arrival ni booleanos como sustitutos. Solo objetivo intermedio: rechazar si su objetivo gobierna transición terminal directa a victoria."
  - "Reutilizar observación, generación causal, validación y cardinalidad. Checkpoint se fija una vez en su fase; no reevalúa su presencia como ancestro al terminal. current-entity-presence conserva todos sus checks terminales y comportamiento de perfiles previos."
  - "Pruebas end-to-end de referencia: reunión intermedia simultánea, retirada posterior a otro receptor y victoria con batch fresco final; salida/unknown/dead/wrongzone/replacement/stale, derivación prematura, guardado/carga, pago una vez y prioridad de derrota. La presencia final continua sigue bloqueando si se abandona."
  - "SchemaVersion1/perfilv2/IDs intactos; perfiles no opt-in conservan fingerprints/snapshots. Exportador sigue rechazando capacidades nativas no implementadas. bun run validate y test:export si afecta adaptador; revisión de modelo independiente."
- review-state: in_review
- review-implementer: gpt-6-luna

### S2 — Observer nativo y certificación de alcance temporal
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `packages/aoe2-adapter`, `tools/python`, `tests/fixtures/checkpoint-presence`, `docs/qa/checkpoint-presence-native`
- **Gate**: e2e
- acceptance:
  - "Depende de la base nativa i00003/S3 e i00005/S2. Implementar observación real de dos lugares simultáneos y latch de checkpoint, liberar exigencia de puesto tras latch y conservar recheck final continuo."
  - "Round-trip/export y motor con hash/build/plataforma: movimiento mismo tick, muerte, guardado antes/después, batch stale, checkpoint incompleto y final abandonado. Sin implementación, rechazo explícito; no representar como funcional."

### S3 — Alineación del dossier y traspaso designado
- **Status**: pending
- **DependsOn**: [S1, S2]
- **Files**: `docs/design/odysseys/imperial-church.json`, `docs/design/maps/imperial-church`, `docs/wiki/imperial-church`, `docs/design/voices`, `docs/research/odyssey-research`, `docs/handoffs`, `docs/qa/campaign-design`
- **Gate**: e2e
- acceptance:
  - "La especificación designará explícitamente checkpoint-entity-presence en o2 y current-entity-presence en o3, mantendrá objetivos, supervivientes, pagos e historia. Referencia y soporte nativo con estados distintos; no promover MiniMax por una prueba de reducer."
  - "Reevaluar las90combinaciones hasta terminal por ambas APIs y adversarios, conservar31dossiers anteriores y metadatos, revisión independiente y publicación oficial. Geografía/IA/jugabilidad y aprobación histórica siguen gates propios."

## acceptance

- Nuevo kind estricto checkpoint-entity-presence con identidades, destinos y mínimo; requiere batch fresco monotónico al latch, no admite record-predicate, arrival ni booleanos como sustitutos. Solo objetivo intermedio: rechazar si su objetivo gobierna transición terminal directa a victoria.
- Reutilizar observación, generación causal, validación y cardinalidad. Checkpoint se fija una vez en su fase; no reevalúa su presencia como ancestro al terminal. current-entity-presence conserva todos sus checks terminales y comportamiento de perfiles previos.
- Pruebas end-to-end de referencia: reunión intermedia simultánea, retirada posterior a otro receptor y victoria con batch fresco final; salida/unknown/dead/wrongzone/replacement/stale, derivación prematura, guardado/carga, pago una vez y prioridad de derrota. La presencia final continua sigue bloqueando si se abandona.
- SchemaVersion1/perfilv2/IDs intactos; perfiles no opt-in conservan fingerprints/snapshots. Exportador sigue rechazando capacidades nativas no implementadas. bun run validate y test:export si afecta adaptador; revisión de modelo independiente.
- Depende de la base nativa i00003/S3 e i00005/S2. Implementar observación real de dos lugares simultáneos y latch de checkpoint, liberar exigencia de puesto tras latch y conservar recheck final continuo.
- Round-trip/export y motor con hash/build/plataforma: movimiento mismo tick, muerte, guardado antes/después, batch stale, checkpoint incompleto y final abandonado. Sin implementación, rechazo explícito; no representar como funcional.
- La especificación designará explícitamente checkpoint-entity-presence en o2 y current-entity-presence en o3, mantendrá objetivos, supervivientes, pagos e historia. Referencia y soporte nativo con estados distintos; no promover MiniMax por una prueba de reducer.
- Reevaluar las90combinaciones hasta terminal por ambas APIs y adversarios, conservar31dossiers anteriores y metadatos, revisión independiente y publicación oficial. Geografía/IA/jugabilidad y aprobación histórica siguen gates propios.
