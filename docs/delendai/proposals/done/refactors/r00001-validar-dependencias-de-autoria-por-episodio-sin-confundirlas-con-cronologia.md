---
id: r00001
title: "Validar dependencias de autoría por episodio sin confundirlas con cronología"
kind: refactor
status: done
type: proposal
track: campaign-factory
date: 2026-10-24
last-transition-id: f6891988-e749-4afe-bab3-de8feeb7fdaa
last-correlation-id: f6891988-e749-4afe-bab3-de8feeb7fdaa
last-transition-from: review
last-transition-at: 2026-10-24T21:01:52.756Z
shipped-in:
  - "56290e10233fa54e133007b9340c99eb259fe366"
---

# r00001 — Validar dependencias de autoría por episodio sin confundirlas con cronología

## goal

Permitir autoría de fuentes de episodios aprobados tras metadatos comunes, conservando orden canónico, identidades, gates de promoción y revisión independiente. Auditar el grafo real en vez de exigir una cadena cronológica de trabajo. No cambia esquemas de campaña, progreso ni aprobación histórica/nativa.

## why

El propietario pide que MiniMax materialice episodios ya preparados mientras el arquitecto termina los siguientes. El validador actual confunde orden del jugador y orden de trabajo: obliga a una cadena serial de autoría. Debe aceptar la nueva planificación sin permitir promoción temprana, ciclos o pérdida de identidades.

## non-goals

- No implementar campañas, nuevos esquemas de escenario, operaciones nativas, cambios de IDs/progreso ni aprobación de contenido.
- No copiar el runtime de DelendAI: este validador sólo comprueba documentos y asignaciones del proyecto, como ya hacía.
- No desbloquear propuestas históricas ni editar sus estados. La enmienda de planificación se entrega por d00002/S11 y conserva sus gates.

## slices

- global_gate: none

### S1 — Auditoría de dependencias y pruebas adversas
- **Status**: done
- **Files**: `tools/design/odyssey_assignments.validator.py`, `tools/design/test_design.py`
- **Gate**: e2e
- acceptance:
  - "Aceptar el grafo vigente en cadena y episodios independientes tras S2 sin cambiar orden de presentación ni identidad de episodios/slices."
  - "Rechazar ciclos, referencias desconocidas/duplicadas, episodios sin S2 como ancestro y promoción que no espere todos los episodios; conservar detección de estados de dossier y slots divergentes."
  - "Pruebas focalizadas significativas y bun run validate; revisión independiente y publicación oficial. No modificar contratos, IDs, gameplay ni estados de las propuestas históricas."
- shipped-in: `ebac7f36553f`
- review-state: done
- review-implementer: gpt-6
- review-reviewer: gpt-6-luna
- review-log: approved by gpt-6-luna — verified at 56290e10233f, validate exit 0 and tests 142/142 claimed, no recorded run cited; acceptance 3/3: (1) Inspected audit_authoring_dependencies and audit_assignments at 56290e1: the DAG permits serial, independent, and mixed dependencies; the canonical episodeSele… (2) The four added focused tests cover cycles, unknown/duplicate edges, malformed/missing metadata ancestry, and promotion omitting each episode. Existing assignme… (3) Ran `python3 tools/design/test_design.py` (94/94) and `bun run validate` (exit 0; 142/142 Bun tests, 2069 expectations, docs and campaign validation passed). T… — Independent review of delivery 56290e10233fa54e133007b9340c99eb259fe366. I verified the DAG contract, preservation of canonical episode identity/order and dossier status, all three acceptance criteria, and the declared non-goals. The focused design suite and bun run validate passed independently. This approves r00001/S1 only; no campaign or historical dossier approval is implied.

## acceptance

- Aceptar el grafo vigente en cadena y episodios independientes tras S2 sin cambiar orden de presentación ni identidad de episodios/slices.
- Rechazar ciclos, referencias desconocidas/duplicadas, episodios sin S2 como ancestro y promoción que no espere todos los episodios; conservar detección de estados de dossier y slots divergentes.
- Pruebas focalizadas significativas y bun run validate; revisión independiente y publicación oficial. No modificar contratos, IDs, gameplay ni estados de las propuestas históricas.
