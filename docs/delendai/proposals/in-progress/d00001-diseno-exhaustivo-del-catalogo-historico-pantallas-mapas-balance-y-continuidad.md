---
id: d00001
title: "Diseno exhaustivo del catalogo historico: pantallas mapas balance y continuidad"
kind: docs
status: in-progress
type: proposal
track: campaign-design
date: 2026-10-12
---

# d00001 — Diseno exhaustivo del catalogo historico: pantallas mapas balance y continuidad

## goal

Completar la planificación del arquitecto para las nueve campañas históricas explícitas de la conversación y sus pilotos: wiki con fuentes consultadas, geografía documentada, imágenes descargadas con licencia y hashes, especificación individual de escenarios y pantallas, balance cuantitativo estimado por dificultad, continuidad opcional exacta y propuestas/slices de autoría acotada para MiniMax. No implementar las campañas ni afirmar balance jugado.

## why

El usuario exige que las decisiones históricas, geográficas, narrativas y de balance estén resueltas por el arquitecto antes de delegar la materialización mecánica.

## non-goals

- No crear ahora mods históricos jugables completos ni ejecutar MiniMax.
- No cambiar contratos/IDs de campañas existentes ni afirmar pruebas reales del motor.
- No publicar mods ni generar medios pagados.

## slices

- global_gate: e2e

### S1 — Investigar y entregar todos los dossiers y planes de producción
- **Status**: pending
- **Files**: `docs/design`, `docs/wiki`, `docs/research`, `docs/handoffs`, `docs/production`, `docs/qa/campaign-design`, `tools/design`, `docs/delendai/proposals`, `README.md`
- **Gate**: e2e
- acceptance:
  - "Nueve campañas identificadas, cada escenario con historia/fuentes/terreno/objetivos/estados/eventos/recuperación/IA finita y easy/standard/hard explícitos."
  - "Cada pantalla tiene texto es-ES, narrador, ilustración de referencia, claves/condición y destino; sucesoras/antecesoras y claves acumulativas exactas, sin bloqueos."
  - "Descargas reales locales con licencia/procedencia/hash y mapas esquemáticos con controles geográficos; incertidumbres de historia y reconstrucción etiquetadas."
  - "Propuestas oficiales de autoría con slices que apuntan a cada dossier, mapas, pantallas y presupuesto; DSL insuficiente deriva a infraestructura, no temporizadores de sustitución."
  - "Validación de integridad de planes y descarga, bun run validate, revisión independiente e integración oficial."

## acceptance

- Nueve campañas identificadas, cada escenario con historia/fuentes/terreno/objetivos/estados/eventos/recuperación/IA finita y easy/standard/hard explícitos.
- Cada pantalla tiene texto es-ES, narrador, ilustración de referencia, claves/condición y destino; sucesoras/antecesoras y claves acumulativas exactas, sin bloqueos.
- Descargas reales locales con licencia/procedencia/hash y mapas esquemáticos con controles geográficos; incertidumbres de historia y reconstrucción etiquetadas.
- Propuestas oficiales de autoría con slices que apuntan a cada dossier, mapas, pantallas y presupuesto; DSL insuficiente deriva a infraestructura, no temporizadores de sustitución.
- Validación de integridad de planes y descarga, bun run validate, revisión independiente e integración oficial.
