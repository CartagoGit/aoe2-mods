---
id: f00001
title: "Piloto tecnico de rutas independientes y localizacion"
kind: feat
status: ready
type: proposal
track: campaign-factory
date: 2026-10-12
---

# f00001 — Piloto tecnico de rutas independientes y localizacion

## goal

Crear únicamente contenido para un piloto técnico A/B y una sucesora autocontenida, usando contratos, CLI, IDs y adaptador existentes. Responsable posterior: MiniMax M3.1. No cambiar packages ni tools. Diseñar dos victorias excluyentes dentro de una partida pero acumulables al rejugar: destruir el castillo A o B y escribir claves distintas. Reutilizar terminal para evitar doble final. Aviso estático y narrativa condicional opcional; todas las campañas siguen accesibles. Fuentes técnicas: update128442, update141935 y documentación del parser citadas en capabilities.

## why

Demostrar el flujo completo antes de producir mapas históricos. Depende de base revisada; acreditación en motor depende de la propuesta de compatibilidad, no bloquear creación de contenido declarativo.

## non-goals

- No modificar arquitectura, contratos ni herramientas fuera de un slice que lo autorice.
- No publicar mods ni generar medios pagados masivamente sin autorización.
- No afirmar pruebas de motor, traducción aprobada o derechos sin evidencia.

## slices

- global_gate: e2e

### S1 — Especificacion y matriz del laboratorio
- **Status**: pending
- **Files**: `docs/wiki/route-pilot/**`
- **Gate**: e2e
- acceptance:
  - "Definir mapas mínimos, victoria A/B, replay y recapitulación; no atribuir hechos históricos a fixtures."
  - "Casos nuevos/perfil sin datos, A, B, ambas, guardar/cargar, victoria simultánea y cambio de idioma."

### S2 — Campañas y escenarios del piloto
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `campaigns/route-pilot/**`, `campaigns/route-successor/**`
- **Gate**: e2e
- acceptance:
  - "Fuentes JSON completas y unidades existentes; dos objetivos con variables y eventos finitos dentro del DSL."
  - "Claves progress.route-pilot.route-a y progress.route-pilot.route-b permanentes y terminal común sin borrar la otra."
  - "Narradores diferenciados, todos los textos semánticos; predecesora opcional."

### S3 — Reserva de IDs y glosario
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `config/string-ids.lock.json`, `config/glossary.json`
- **Gate**: e2e
- acceptance:
  - "Ejecutar ids:allocate en unidad con lock explícito, comprobar que IDs existentes no cambian."
  - "Traducciones de 17 locales con estado honesto; mantener namespaces globales únicos."

### S4 — Verificacion y dossier de entrega
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `docs/qa/route-pilot/**`
- **Gate**: e2e
- acceptance:
  - "bun run validate y export de cada campaña; informes con hashes y delimitación de capacidades."
  - "No cerrar GAME VERIFIED ni PRODUCTION READY sin resultados reales de las pruebas vinculadas al ZIP."

## acceptance

- Definir mapas mínimos, victoria A/B, replay y recapitulación; no atribuir hechos históricos a fixtures.
- Casos nuevos/perfil sin datos, A, B, ambas, guardar/cargar, victoria simultánea y cambio de idioma.
- Fuentes JSON completas y unidades existentes; dos objetivos con variables y eventos finitos dentro del DSL.
- Claves progress.route-pilot.route-a y progress.route-pilot.route-b permanentes y terminal común sin borrar la otra.
- Narradores diferenciados, todos los textos semánticos; predecesora opcional.
- Ejecutar ids:allocate en unidad con lock explícito, comprobar que IDs existentes no cambian.
- Traducciones de 17 locales con estado honesto; mantener namespaces globales únicos.
- bun run validate y export de cada campaña; informes con hashes y delimitación de capacidades.
- No cerrar GAME VERIFIED ni PRODUCTION READY sin resultados reales de las pruebas vinculadas al ZIP.

## Contexto, estado inicial y dependencias

Dependencias: i00001 revisada e integrada. Estado inicial: fixture técnico y herramientas presentes; contenido histórico completo no creado; evidencias de juego pendientes. Consultar el estado vivo de DelendAI antes de empezar: esta tabla no desbloquea tareas por sí sola.

## Requisitos compartidos

Leer `AGENTS.md`, `docs/production/plan.md`, `docs/architecture/overview.md`, `docs/guides/scenarios.md`, `docs/guides/history.md`, `docs/guides/narration-and-characters.md`, `docs/guides/localization.md`, `docs/guides/audio.md`, `docs/guides/visual-assets.md`, `docs/guides/ai-and-balance.md`, `docs/guides/qa.md` y `docs/guides/publishing.md`. Canonical es-ES, claves semánticas, lock global, identidad técnica permanente, 17 locales revisados, narradores general/particular y voces consistentes, recursos licenciados y enemigos con economía/reserva explicada. Las carpetas wiki siguen `docs/templates/wiki-campaign.md`.

## Riesgos y decisiones cerradas

Riesgos: pasajes históricos no consultados, anacronismos, coexistencia de cadenas, fallos de guardado/carga, prioridad terminal en un tick, licencias y tamaño del audio. Documentar resultado negativo y propuesta concreta de resolución; no suplirlo con éxito ficticio. Las dependencias narrativas siempre son opcionales para el jugador. Un problema de infraestructura corresponde al arquitecto; el agente de contenido no modifica packages/tools por su cuenta.

## Entregables, revisión y cierre

Entregar fuentes declarativas, dossier, glosario/IDs donde el slice lo permita, manifest multimedia, informes de build/QA y evidencia vinculada al artefacto. Gate de cada slice: `bun run validate`; si afecta archivos nativos, ejecutar `bun run test:export` y exportar su campaña. Para cierre de contenido publicable: `bun run release:check <id>`, revisión histórica/lingüística/media y revisión independiente oficial. Registrar el commit y resultados; no marcar done mediante edición de markdown. La subida del mod es una acción separada y autorizada por el propietario.
