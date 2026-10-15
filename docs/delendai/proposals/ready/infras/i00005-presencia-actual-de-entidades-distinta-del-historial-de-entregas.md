---
id: i00005
title: "Presencia actual de entidades distinta del historial de entregas"
kind: infra
status: ready
type: proposal
track: architecture
date: 2026-10-14
---

# i00005 — Presencia actual de entidades distinta del historial de entregas

## goal

Implementar el contrato live-entity-presence: comprobar en el tick de cierre identidad viva y posición actual en su zona asignada, sin usar arrived histórico como residencia. La aprobación previa i00003/S1 se conserva; esta ampliación nueva requiere revisión propia. Prioridad: los tres legajos y custodios de Milán350. La implementación nativa depende además de i00003/S3 y su motor observador; no desbloquear autoría histórica por un contrato de referencia.

## why

Revisión independiente GPT-6.1 reprodujo que tras llegar a otra zona el historial de la primera llegada sigue verdadero. Es correcto para receipts, pero permite ganar aunque legajos/custodios hayan dejado su depósito. Corregir narrativa simple donde no hace falta permanencia, y exigir un observable espacial reversible donde sí. Diseñar y probar estructura antes de asignar contenido mecánico a MiniMax.

## non-goals

- No convertir arrived en un booleano mutable ni borrar recibos históricos.
- No inventar custodia física, cargo de transportista o bloqueo de movimiento.
- No alterar IDs de campañas, reservas de cadenas o el veredicto ya aprobado de i00003/S1.
- No afirmar GAME VERIFIED, geografía antigua aprobada o calibración con pruebas estáticas.

## slices

- global_gate: e2e

### S1 — Contrato y referencia de presencia actual
- **Status**: in-progress
- **Files**: `packages/schemas`, `packages/gameplay-state`, `packages/gameplay-validation`, `packages/scenario-compiler`, `tests/unit/entity-presence.test.ts`, `docs/decisions/0005-live-entity-presence.md`
- **Gate**: e2e
- acceptance:
  - "Predicado live-entity-presence con IDs únicos, destinos por entidad, mínimo factible y posición/vida actuales. Observaciones reversibles tipadas y snapshot inmutable; desconocido o fuera de zona no satisface. Llegadas históricas permanecen inmutables."
  - "Reevaluar antes de latch/terminal en el mismo tick. Guardado/carga con fingerprint y refresco de posiciones, movimientos a otra zona, salida/reentrada, identidad equivocada, muerte previa y presencia insuficiente. Modelo/código nuevo requiere revisión independiente propia."
- review-state: changes_requested
- review-implementer: gpt-6-sol
- review-reviewer: gpt-6.1-sol
- review-log: requested_changes by gpt-6.1-sol — Independent review of integrated8c55de534460c859c5f187bc6ccd4274d92075fb. P1: current-entity-presence counts an unproduced derived-token output: valid profile declares custodian-1 produced by producer.derive; fresh six-actor batch latches return with no derivation fact. livePresenceSatisfied omits generationReady used by existing entity observers. Repro /tmp/gpt61-i00005-generated-repro.ts. P1: invalid/stale live batch returns before automatic deadline defeat; valid deadline10s, tick now11 gives defeat without batch but null terminal with duplicate-identity batch. Repro /tmp/gpt61-i00005-invalid-deadline-repro.ts. Preserve whole-batch rejection and prohibit stale positive reuse while retaining independent defeat priority. Own validate passes99/99 tests357expects; these cross-contract cases are uncovered. Detailed report /tmp/gpt61-i00005-S1-review.md. S2/S3/native/history excluded.

### S2 — Observadores espaciales nativos
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `packages/aoe2-adapter`, `tools/python`, `tests/fixtures/native-presence`
- **Gate**: e2e
- acceptance:
  - "Prerequisito adicional obligatorio: i00003/S3 integrado y acreditado. Mapear observación de ubicación/vida del mismo tick a zonas reales; no receipt ni timer como posición. Fuera de soporte rechazar explícitamente."
  - "Round-trip, xs-check y export con casos mover custodio/legajo tras primera entrega, salida y regreso, muerte, movimiento en mismo tick de victoria, carga de partida. Evidencia AoE2/build/hash separada; gameVerified permanece false sin juego."

### S3 — Promoción de contratos y QA de depósitos
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `tools/design/episode_dossier.validator.py`, `docs/design/odysseys/imperial-church.json`, `docs/qa/entity-presence`, `docs/handoffs/MINIMAX-M3.1-PRESENCE.md`
- **Gate**: e2e
- acceptance:
  - "Milán350 conserva tres legajos y tres custodios distintos actualmente presentes en depósitos asignados al completarse el regreso de escribientes. No congelar ni sustituir identities y no reutilizar arrivals para estancia."
  - "Dossiers que solo necesitan recepción histórica lo dicen así. Cerrar gates de fuente/terreno/native/balance antes de autoría MiniMax; no declarar todas las odiseas aprobadas por esta capacidad."

## acceptance

- Predicado live-entity-presence con IDs únicos, destinos por entidad, mínimo factible y posición/vida actuales. Observaciones reversibles tipadas y snapshot inmutable; desconocido o fuera de zona no satisface. Llegadas históricas permanecen inmutables.
- Reevaluar antes de latch/terminal en el mismo tick. Guardado/carga con fingerprint y refresco de posiciones, movimientos a otra zona, salida/reentrada, identidad equivocada, muerte previa y presencia insuficiente. Modelo/código nuevo requiere revisión independiente propia.
- Prerequisito adicional obligatorio: i00003/S3 integrado y acreditado. Mapear observación de ubicación/vida del mismo tick a zonas reales; no receipt ni timer como posición. Fuera de soporte rechazar explícitamente.
- Round-trip, xs-check y export con casos mover custodio/legajo tras primera entrega, salida y regreso, muerte, movimiento en mismo tick de victoria, carga de partida. Evidencia AoE2/build/hash separada; gameVerified permanece false sin juego.
- Milán350 conserva tres legajos y tres custodios distintos actualmente presentes en depósitos asignados al completarse el regreso de escribientes. No congelar ni sustituir identities y no reutilizar arrivals para estancia.
- Dossiers que solo necesitan recepción histórica lo dicen así. Cerrar gates de fuente/terreno/native/balance antes de autoría MiniMax; no declarar todas las odiseas aprobadas por esta capacidad.
