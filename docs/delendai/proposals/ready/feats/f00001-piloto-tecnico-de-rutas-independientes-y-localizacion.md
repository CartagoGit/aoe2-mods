---
id: f00001
title: "Piloto tecnico de rutas independientes y localizacion"
kind: feat
status: ready
type: proposal
track: campaign-factory
date: 2026-10-12
last-transition-id: c0eedc78-28dc-4ca9-aaa3-4226f3efd47c
last-correlation-id: c0eedc78-28dc-4ca9-aaa3-4226f3efd47c
last-transition-from: blocked
last-transition-at: 2026-10-12T11:57:38.189Z
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

### S1 — Especificación y matriz del laboratorio
- **Status**: pending
- **Files**: `docs/wiki/route-pilot`
- **Gate**: e2e
- acceptance:
  - "Definir mapas mínimos, victoria A/B, replay, recapitulación y lista cerrada de textos/personajes; no atribuir hechos históricos a fixtures."
  - "Casos nuevo perfil, A, B, ambas, guardar/cargar, victoria simultánea y cambio de idioma."

### S2 — Borradores completos de los dos mods
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/route-pilot`, `staging/campaigns/route-successor`
- **Gate**: e2e
- acceptance:
  - "Fuentes completas de ambos mods en staging: escenarios, metadatos, narradores, 17 catálogos draft con claves semánticas y manifiestos licenciados."
  - "Claves progress.route-pilot.route-a y progress.route-pilot.route-b permanentes; terminal común; predecesora opcional y sucesora autocontenida."
  - "bun run staging:check route-pilot y bun run staging:check route-successor pasan sin --partial. No activar carpetas en campaigns ni modificar el lock en este slice."

### S3 — Materialización conjunta, IDs y glosario
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/route-pilot`, `staging/campaigns/route-successor`, `campaigns/route-pilot`, `campaigns/route-successor`, `config/string-ids.lock.json`, `config/glossary.json`
- **Gate**: e2e
- acceptance:
  - "Reclamar todas las rutas del slice y promover ambos bundles completos en una misma entrega; ajustar asset.path al destino final y validar sus bytes/hashes."
  - "Ejecutar ids:allocate después de materializar y antes del commit; IDs previos inmutables, namespaces únicos, glosario completo por locale."
  - "bun run validate y export de ambos mods pasan; el commit incluye fuentes, escenarios, catálogos y lock, sin referencias pendientes."

### S4 — Verificación y dossier de entrega
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `docs/qa/route-pilot`
- **Gate**: e2e
- acceptance:
  - "Registrar comandos, hashes y capacidades; bun run validate y export de ambas campañas."
  - "No cerrar GAME VERIFIED ni PRODUCTION READY sin pruebas reales vinculadas al ZIP; estado de traducciones/medios honesto."

## acceptance

- Definir mapas mínimos, victoria A/B, replay, recapitulación y lista cerrada de textos/personajes; no atribuir hechos históricos a fixtures.
- Casos nuevo perfil, A, B, ambas, guardar/cargar, victoria simultánea y cambio de idioma.
- Fuentes completas de ambos mods en staging: escenarios, metadatos, narradores, 17 catálogos draft con claves semánticas y manifiestos licenciados.
- Claves progress.route-pilot.route-a y progress.route-pilot.route-b permanentes; terminal común; predecesora opcional y sucesora autocontenida.
- bun run staging:check route-pilot y bun run staging:check route-successor pasan sin --partial. No activar carpetas en campaigns ni modificar el lock en este slice.
- Reclamar todas las rutas del slice y promover ambos bundles completos en una misma entrega; ajustar asset.path al destino final y validar sus bytes/hashes.
- Ejecutar ids:allocate después de materializar y antes del commit; IDs previos inmutables, namespaces únicos, glosario completo por locale.
- bun run validate y export de ambos mods pasan; el commit incluye fuentes, escenarios, catálogos y lock, sin referencias pendientes.
- Registrar comandos, hashes y capacidades; bun run validate y export de ambas campañas.
- No cerrar GAME VERIFIED ni PRODUCTION READY sin pruebas reales vinculadas al ZIP; estado de traducciones/medios honesto.

## Contexto, estado inicial y dependencias

Dependencias: i00001 revisada e integrada. Estado inicial: fixture técnico y herramientas presentes; contenido histórico completo no creado; evidencias de juego pendientes. Consultar el estado vivo de DelendAI antes de empezar: esta tabla no desbloquea tareas por sí sola.

## Requisitos compartidos

Leer `AGENTS.md`, `docs/production/plan.md`, `docs/architecture/overview.md`, `docs/guides/scenarios.md`, `docs/guides/history.md`, `docs/guides/narration-and-characters.md`, `docs/guides/localization.md`, `docs/guides/audio.md`, `docs/guides/visual-assets.md`, `docs/guides/ai-and-balance.md`, `docs/guides/qa.md` y `docs/guides/publishing.md`. sourceLocale=en, español completo, claves semánticas, lock global, identidad técnica permanente, 17 locales revisados, narradores general/particular y voces consistentes, recursos licenciados y enemigos con economía/reserva explicada. Las carpetas wiki siguen `docs/templates/wiki-campaign.md`.

## Riesgos y decisiones cerradas

Riesgos: pasajes históricos no consultados, anacronismos, coexistencia de cadenas, fallos de guardado/carga, prioridad terminal en un tick, licencias y tamaño del audio. Documentar resultado negativo y propuesta concreta de resolución; no suplirlo con éxito ficticio. Las dependencias narrativas siempre son opcionales para el jugador. Un problema de infraestructura corresponde al arquitecto; el agente de contenido no modifica packages/tools por su cuenta.

## Entregables, revisión y cierre

Entregar fuentes declarativas, dossier, glosario/IDs donde el slice lo permita, manifest multimedia, informes de build/QA y evidencia vinculada al artefacto. Cada slice debe integrar con `bun run validate` verde. Los borradores se preparan en staging/campaigns, fuera de loadProject; staging:check valida esquemas y declara pendientes explícitamente. El slice final de materialización posee campañas, borradores, lock y glosario, y los incorpora juntos antes de validar/commitear. Seguir docs/guides/staging.md. Gate de cada slice: `bun run validate`; si afecta archivos nativos, ejecutar `bun run test:export`; exportar su campaña cuando esté materializada en campaigns, nunca un borrador staging. Las plantillas de staging se comprueban como fuentes y su integración nativa queda pendiente del slice de materialización. Para cierre de contenido publicable: `bun run release:check <id>`, revisión histórica/lingüística/media y revisión independiente oficial. Registrar el commit y resultados; no marcar done mediante edición de markdown. La subida del mod es una acción separada y autorizada por el propietario.


## Contrato de diseño ampliado por el propietario

El diseño vigente está en docs/design/catalog.json y docs/design/production-contract.md; el dossier específico es docs/wiki/route-pilot/00-brief.md (para el laboratorio, seguir en su lugar docs/wiki/route-pilot/00-brief.md y pilots de catalog.json). La nueva fuente es en, con español completo. S1 compara el contrato cerrado y registra discrepancias; no diseña otra campaña. Los planos de escenarios, objectivePlan con ledgers, todas las pantallas, bibliografía/narrador y presupuestos estimados son instrucciones del arquitecto. Mantener identidades y claves anteriores. Dependencias ampliadas: d00001/i00002 revisadas e integradas; i00003 para capacidades faltantes y s00001 para evidencia de motor en entrega. El piloto Milvio reutiliza 01-milvian-bridge de C01, mapa360×360, como piloto real de rendimiento; no copiar infraestructura ni conservar un mapa pequeño provisional como la versión de la misión histórica. El laboratorio de rutas mantiene32×32 por su finalidad técnica. Todas las afirmaciones de balance siguen estimated hasta partidas registradas.
