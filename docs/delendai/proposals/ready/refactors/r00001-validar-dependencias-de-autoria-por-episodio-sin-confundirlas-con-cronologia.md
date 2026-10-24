---
id: r00001
title: "Validar dependencias de autoría por episodio sin confundirlas con cronología"
kind: refactor
status: ready
type: proposal
track: campaign-factory
date: 2026-10-24
---

# r00001 — Validar dependencias de autoría por episodio sin confundirlas con cronología

## goal

Permitir autoría de fuentes de episodios aprobados tras metadatos comunes, conservando orden canónico, identidades, gates de promoción y revisión independiente. Auditar el grafo real en vez de exigir una cadena cronológica de trabajo. No cambia esquemas de campaña, progreso ni aprobación histórica/nativa.

## why

TODO: why this work matters now.

## non-goals

- TODO: what this proposal deliberately skips.

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
