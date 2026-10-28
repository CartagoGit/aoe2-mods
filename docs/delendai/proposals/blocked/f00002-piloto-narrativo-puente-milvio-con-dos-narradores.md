---
id: f00002
title: "Piloto narrativo: Puente Milvio con dos narradores"
kind: feat
status: blocked
type: proposal
track: campaign-factory
date: 2026-10-12
last-transition-id: 01519bcf-cfbd-44fa-8e80-a06c793cacaa
last-correlation-id: 01519bcf-cfbd-44fa-8e80-a06c793cacaa
last-transition-from: ready
last-transition-at: 2026-10-12T04:20:24.321Z
---

# f00002 — Piloto narrativo: Puente Milvio con dos narradores

## goal

Crear un escenario histórico piloto autocontenido de 312, como contenido del sistema existente. Responsable: MiniMax M3.1 tras base y piloto técnico revisados. Leer docs/wiki/imperial-church, guía histórica, narración, IA, medios y QA. Hecho central: Constantino derrota a Majencio; los relatos religiosos se presentan como tradición/interpretación de las fuentes, no como intervención sobrenatural verificable. Narrador general explica contexto; cronista ficticio verosímil presenta y cierra la misión. Militares/personajes no imitan voces reales. El reto principal combina batalla y control de acceso, con alternativa táctica explicada y sin refuerzos ilimitados.

## why

Comprobar historia, diseño, documentación, voces, ilustración y localización en una misión pequeña. Los detalles de despliegue exacto requieren investigación previa y quedan como dramatización hasta acreditación.

## non-goals

- No modificar arquitectura, contratos ni herramientas fuera de un slice que lo autorice.
- No publicar mods ni generar medios pagados masivamente sin autorización.
- No afirmar pruebas de motor, traducción aprobada o derechos sin evidencia.

## slices

- global_gate: e2e

### S1 — Dossier, cronología y brief verificado
- **Status**: pending
- **Files**: `docs/wiki/milvian-pilot`
- **Gate**: e2e
- acceptance:
  - "Consultar fuentes completas para Constantino, Majencio y puente312; separar hechos, tradición y licencia táctica."
  - "Narrador general y cronista particular, personajes, mapa, objetivos, contingencias y lista de claves fijados antes de redactar."

### S2 — Bundle piloto completo en preparación
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/milvian-pilot`
- **Gate**: e2e
- acceptance:
  - "Preparar metadatos y misión completos en staging: narradores, mapa, fases, derrota recuperable, reserva finita y tres dificultades."
  - "Incluir 17 catálogos con estado real, reparto/pronunciación y manifest de medios con origen/licencia/hash; no afirmar aprobación inexistente."
  - "bun run staging:check milvian-pilot pasa sin --partial; ninguna campaña activa ni ID global se incorpora todavía."

### S3 — Materialización, IDs y terminología
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/milvian-pilot`, `campaigns/milvian-pilot`, `config/string-ids.lock.json`, `config/glossary.json`
- **Gate**: e2e
- acceptance:
  - "Promover todo el bundle, ajustar rutas finales y asignar IDs con ids:allocate en la misma unidad/entrega bajo locks explícitos."
  - "Glosario de Constantino/Majencio/cargos/religión por locale, estabilidad de IDs anteriores; bun run validate y export del piloto pasan antes del commit."

### S4 — QA adversarial y balance medido
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `campaigns/milvian-pilot`, `docs/qa/milvian-pilot`
- **Gate**: e2e
- acceptance:
  - "Ejecutar casos de juego de objetivos fuera de orden, líder perdido, puente bloqueado, recursos agotados y guardar/cargar; medir las tres dificultades."
  - "Cerrar únicamente capacidades acreditadas con ZIP/hash/build/idioma y reviewer; release:check exige revisiones de historia, 17 locales, medios y motor."

## acceptance

- Consultar fuentes completas para Constantino, Majencio y puente312; separar hechos, tradición y licencia táctica.
- Narrador general y cronista particular, personajes, mapa, objetivos, contingencias y lista de claves fijados antes de redactar.
- Preparar metadatos y misión completos en staging: narradores, mapa, fases, derrota recuperable, reserva finita y tres dificultades.
- Incluir 17 catálogos con estado real, reparto/pronunciación y manifest de medios con origen/licencia/hash; no afirmar aprobación inexistente.
- bun run staging:check milvian-pilot pasa sin --partial; ninguna campaña activa ni ID global se incorpora todavía.
- Promover todo el bundle, ajustar rutas finales y asignar IDs con ids:allocate en la misma unidad/entrega bajo locks explícitos.
- Glosario de Constantino/Majencio/cargos/religión por locale, estabilidad de IDs anteriores; bun run validate y export del piloto pasan antes del commit.
- Ejecutar casos de juego de objetivos fuera de orden, líder perdido, puente bloqueado, recursos agotados y guardar/cargar; medir las tres dificultades.
- Cerrar únicamente capacidades acreditadas con ZIP/hash/build/idioma y reviewer; release:check exige revisiones de historia, 17 locales, medios y motor.

## Contexto, estado inicial y dependencias

Dependencias: i00001 y piloto técnico revisados. Estado inicial: fixture técnico y herramientas presentes; contenido histórico completo no creado; evidencias de juego pendientes. Consultar el estado vivo de DelendAI antes de empezar: esta tabla no desbloquea tareas por sí sola.

## Requisitos compartidos

Leer `AGENTS.md`, `docs/production/plan.md`, `docs/architecture/overview.md`, `docs/guides/scenarios.md`, `docs/guides/history.md`, `docs/guides/narration-and-characters.md`, `docs/guides/localization.md`, `docs/guides/audio.md`, `docs/guides/visual-assets.md`, `docs/guides/ai-and-balance.md`, `docs/guides/qa.md` y `docs/guides/publishing.md`. sourceLocale=en, español completo, claves semánticas, lock global, identidad técnica permanente, 17 locales revisados, narradores general/particular y voces consistentes, recursos licenciados y enemigos con economía/reserva explicada. Las carpetas wiki siguen `docs/templates/wiki-campaign.md`.

## Riesgos y decisiones cerradas

Riesgos: pasajes históricos no consultados, anacronismos, coexistencia de cadenas, fallos de guardado/carga, prioridad terminal en un tick, licencias y tamaño del audio. Documentar resultado negativo y propuesta concreta de resolución; no suplirlo con éxito ficticio. Las dependencias narrativas siempre son opcionales para el jugador. Un problema de infraestructura corresponde al arquitecto; el agente de contenido no modifica packages/tools por su cuenta.

## Entregables, revisión y cierre

Entregar fuentes declarativas, dossier, glosario/IDs donde el slice lo permita, manifest multimedia, informes de build/QA y evidencia vinculada al artefacto. Cada slice debe integrar con `bun run validate` verde. Los borradores se preparan en staging/campaigns, fuera de loadProject; staging:check valida esquemas y declara pendientes explícitamente. El slice final de materialización posee campañas, borradores, lock y glosario, y los incorpora juntos antes de validar/commitear. Seguir docs/guides/staging.md. Gate de cada slice: `bun run validate`; si afecta archivos nativos, ejecutar `bun run test:export`; exportar su campaña cuando esté materializada en campaigns, nunca un borrador staging. Las plantillas de staging se comprueban como fuentes y su integración nativa queda pendiente del slice de materialización. Para cierre de contenido publicable: `bun run release:check <id>`, revisión histórica/lingüística/media y revisión independiente oficial. Registrar el commit y resultados; no marcar done mediante edición de markdown. La subida del mod es una acción separada y autorizada por el propietario.


## Contrato de diseño ampliado por el propietario

El diseño vigente está en docs/design/catalog.json y docs/design/production-contract.md; el dossier específico es docs/wiki/imperial-church/12-production-blueprint.md. La nueva fuente es en, con español completo. S1 compara el contrato cerrado y registra discrepancias; no diseña otra campaña. Los planos de escenarios, objectivePlan con ledgers, todas las pantallas, bibliografía/narrador y presupuestos estimados son instrucciones del arquitecto. Mantener identidades y claves anteriores. Dependencias ampliadas: d00001/i00002 revisadas e integradas; i00003 para capacidades faltantes y s00001 para evidencia de motor en entrega. El piloto Milvio reutiliza 01-milvian-bridge de C01, mapa360×360, como piloto real de rendimiento; no copiar infraestructura ni conservar un mapa pequeño provisional como la versión de la misión histórica. El laboratorio de rutas mantiene32×32 por su finalidad técnica. Todas las afirmaciones de balance siguen estimated hasta partidas registradas.
