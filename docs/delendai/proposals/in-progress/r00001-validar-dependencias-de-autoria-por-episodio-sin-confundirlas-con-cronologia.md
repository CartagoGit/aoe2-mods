---
id: r00001
title: "Validar dependencias de autoría por episodio sin confundirlas con cronología"
kind: refactor
status: in-progress
type: proposal
track: campaign-factory
date: 2026-10-24
last-transition-id: a3b9ff69-98c8-46b9-8768-c6a17de82875
last-correlation-id: a3b9ff69-98c8-46b9-8768-c6a17de82875
last-transition-from: ready
last-transition-at: 2026-10-24T20:43:43.025Z
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
- **Status**: pending
- **Files**: `tools/design/odyssey_assignments.validator.py`, `tools/design/test_design.py`
- **Gate**: e2e
- acceptance:
  - "Aceptar el grafo vigente en cadena y episodios independientes tras S2 sin cambiar orden de presentación ni identidad de episodios/slices."
  - "Rechazar ciclos, referencias desconocidas/duplicadas, episodios sin S2 como ancestro y promoción que no espere todos los episodios; conservar detección de estados de dossier y slots divergentes."
  - "Pruebas focalizadas significativas y bun run validate; revisión independiente y publicación oficial. No modificar contratos, IDs, gameplay ni estados de las propuestas históricas."

## acceptance

- Aceptar el grafo vigente en cadena y episodios independientes tras S2 sin cambiar orden de presentación ni identidad de episodios/slices.
- Rechazar ciclos, referencias desconocidas/duplicadas, episodios sin S2 como ancestro y promoción que no espere todos los episodios; conservar detección de estados de dossier y slots divergentes.
- Pruebas focalizadas significativas y bun run validate; revisión independiente y publicación oficial. No modificar contratos, IDs, gameplay ni estados de las propuestas históricas.
