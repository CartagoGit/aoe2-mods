---
id: f00003
title: "Campana futura: Iglesia imperial 312-337"
kind: feat
status: blocked
type: proposal
track: campaign-factory
date: 2026-10-12
last-transition-id: 31be0fff-d0db-466e-be52-154bc26f7051
last-correlation-id: 31be0fff-d0db-466e-be52-154bc26f7051
last-transition-from: ready
last-transition-at: 2026-10-12T04:20:24.800Z
---

# f00003 — Campana futura: Iglesia imperial 312-337

## goal

Producir CDF-C01 / imperial-church / CDF_ImperialChurch como mod independiente, únicamente tras pilotos revisados. Responsable de contenido: MiniMax M3.1. El dossier inicial docs/wiki/imperial-church fija cronología, fuentes, narrador y tres briefs: 01-milvian-bridge (batalla312), 02-nicaea (diplomacia325), 03-new-capital (economía/comercio330), con epílogo hasta337. Reutilizar el piloto Milvio sin copiar código. No convertir el concilio en batalla religiosa ni inventar cisma católico/ortodoxo en325. Rutas finales son perspectivas geográficas/institucionales acumulativas, no cambio de los hechos históricos.

## why

Ejemplo futuro exhaustivo para ampliar la colección sin rediseñar infraestructura. Las fuentes completas y licencias deben revisarse antes de escribir narrativa final. Dependencias de contenido: pilotos técnico y narrativo aprobados; de producción: pruebas de motor.

## non-goals

- No modificar arquitectura, contratos ni herramientas fuera de un slice que lo autorice.
- No publicar mods ni generar medios pagados masivamente sin autorización.
- No afirmar pruebas de motor, traducción aprobada o derechos sin evidencia.

## slices

- global_gate: e2e

### S1 — Cerrar evidencia y diseño narrativo
- **Status**: pending
- **Files**: `docs/wiki/imperial-church`
- **Gate**: e2e
- acceptance:
  - "Resolver afirmaciones pendientes con pasajes completos e historiografía; revisar neutralidad y anacronismos."
  - "Fichas de Constantino/Majencio/representantes ficticios, cronista retrospectivo, clasificación de líneas y lista de claves; reutilizar diseño del piloto sin duplicar infraestructura."

### S2 — Metadatos, localización y medios en preparación
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/imperial-church/campaign.json`, `staging/campaigns/imperial-church/native`, `staging/campaigns/imperial-church/assets`
- **Gate**: e2e
- acceptance:
  - "Preparar metadatos permanentes, orden scenarioFiles, narradores, intro/epílogo, recap y continuidad opcional exclusivamente en staging."
  - "Preparar 17 catálogos y manifiestos/reparto/pronunciación con estados honestos; scenarioFiles puede señalar los borradores pendientes S3–S5."
  - "bun run staging:check imperial-church --partial valida los metadatos presentes y enumera explícitamente pendientes; no equivale a validar la campaña ni modificar IDs."

### S3 — Borrador misión01: acceso y batalla312
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/imperial-church/scenarios/01-milvian-bridge`
- **Gate**: e2e
- acceptance:
  - "Reutilizar diseño piloto; objetivos por fases, puente/líder y contingencias, reserva militar visible y finita."
  - "Historia documentada/licencia táctica y perfiles de dificultad; guardar escenario válido en staging y ejecutar staging:check --partial."

### S4 — Borrador misión02: negociación en Nicea325
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `staging/campaigns/imperial-church/scenarios/02-nicaea`
- **Gate**: e2e
- acceptance:
  - "Llegada/protección de delegaciones y recursos/negociación como dramatización; resultados del concilio documentados."
  - "No matar confesiones ni representar superioridad doctrinal; variables/eventos finitos y recuperación tras perder mensajeros o agotar negociación."
  - "Mantener fuentes únicamente en staging y ejecutar staging:check --partial."

### S5 — Borrador misión03: rutas de la capital330
- **Status**: pending
- **DependsOn**: [S4]
- **Files**: `staging/campaigns/imperial-church/scenarios/03-new-capital`
- **Gate**: e2e
- acceptance:
  - "Economía/comercio/logística330, geografía y facciones justificadas; rutas y alternativas; sin repetir gran batalla."
  - "Epílogo hasta337, progreso/rutas finales persistentes, continuidad opcional; catálogo S2 ya contiene las claves previstas."
  - "bun run staging:check imperial-church pasa SIN --partial y valida referencias/narración de las tres misiones; cualquier ajuste de claves/metadatos S2 requiere reclamar esos archivos oficialmente."

### S6 — Materialización conjunta y auditoría de entrega
- **Status**: pending
- **DependsOn**: [S5]
- **Files**: `staging/campaigns/imperial-church`, `campaigns/imperial-church`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/imperial-church`
- **Gate**: e2e
- acceptance:
  - "Promover bundle completo y ajustar asset.path; reclamar lock/glosario y ejecutar ids:allocate antes del commit de la misma entrega."
  - "bun run validate y export de la campaña pasan; mantener estables los IDs existentes y documentar revisiones por locale."
  - "Ejecutar QA real, balance medido y release:check antes de PRODUCTION READY; evidencias vinculadas al ZIP, autorización separada para subir el mod."

## acceptance

- Resolver afirmaciones pendientes con pasajes completos e historiografía; revisar neutralidad y anacronismos.
- Fichas de Constantino/Majencio/representantes ficticios, cronista retrospectivo, clasificación de líneas y lista de claves; reutilizar diseño del piloto sin duplicar infraestructura.
- Preparar metadatos permanentes, orden scenarioFiles, narradores, intro/epílogo, recap y continuidad opcional exclusivamente en staging.
- Preparar 17 catálogos y manifiestos/reparto/pronunciación con estados honestos; scenarioFiles puede señalar los borradores pendientes S3–S5.
- bun run staging:check imperial-church --partial valida los metadatos presentes y enumera explícitamente pendientes; no equivale a validar la campaña ni modificar IDs.
- Reutilizar diseño piloto; objetivos por fases, puente/líder y contingencias, reserva militar visible y finita.
- Historia documentada/licencia táctica y perfiles de dificultad; guardar escenario válido en staging y ejecutar staging:check --partial.
- Llegada/protección de delegaciones y recursos/negociación como dramatización; resultados del concilio documentados.
- No matar confesiones ni representar superioridad doctrinal; variables/eventos finitos y recuperación tras perder mensajeros o agotar negociación.
- Mantener fuentes únicamente en staging y ejecutar staging:check --partial.
- Economía/comercio/logística330, geografía y facciones justificadas; rutas y alternativas; sin repetir gran batalla.
- Epílogo hasta337, progreso/rutas finales persistentes, continuidad opcional; catálogo S2 ya contiene las claves previstas.
- bun run staging:check imperial-church pasa SIN --partial y valida referencias/narración de las tres misiones; cualquier ajuste de claves/metadatos S2 requiere reclamar esos archivos oficialmente.
- Promover bundle completo y ajustar asset.path; reclamar lock/glosario y ejecutar ids:allocate antes del commit de la misma entrega.
- bun run validate y export de la campaña pasan; mantener estables los IDs existentes y documentar revisiones por locale.
- Ejecutar QA real, balance medido y release:check antes de PRODUCTION READY; evidencias vinculadas al ZIP, autorización separada para subir el mod.

## Contexto, estado inicial y dependencias

Dependencias: i00001, piloto técnico y piloto narrativo revisados. Estado inicial: fixture técnico y herramientas presentes; contenido histórico completo no creado; evidencias de juego pendientes. Consultar el estado vivo de DelendAI antes de empezar: esta tabla no desbloquea tareas por sí sola.

## Requisitos compartidos

Leer `AGENTS.md`, `docs/production/plan.md`, `docs/architecture/overview.md`, `docs/guides/scenarios.md`, `docs/guides/history.md`, `docs/guides/narration-and-characters.md`, `docs/guides/localization.md`, `docs/guides/audio.md`, `docs/guides/visual-assets.md`, `docs/guides/ai-and-balance.md`, `docs/guides/qa.md` y `docs/guides/publishing.md`. sourceLocale=en, español completo, claves semánticas, lock global, identidad técnica permanente, 17 locales revisados, narradores general/particular y voces consistentes, recursos licenciados y enemigos con economía/reserva explicada. Las carpetas wiki siguen `docs/templates/wiki-campaign.md`.

## Riesgos y decisiones cerradas

Riesgos: pasajes históricos no consultados, anacronismos, coexistencia de cadenas, fallos de guardado/carga, prioridad terminal en un tick, licencias y tamaño del audio. Documentar resultado negativo y propuesta concreta de resolución; no suplirlo con éxito ficticio. Las dependencias narrativas siempre son opcionales para el jugador. Un problema de infraestructura corresponde al arquitecto; el agente de contenido no modifica packages/tools por su cuenta.

## Entregables, revisión y cierre

Entregar fuentes declarativas, dossier, glosario/IDs donde el slice lo permita, manifest multimedia, informes de build/QA y evidencia vinculada al artefacto. Cada slice debe integrar con `bun run validate` verde. Los borradores se preparan en staging/campaigns, fuera de loadProject; staging:check valida esquemas y declara pendientes explícitamente. El slice final de materialización posee campañas, borradores, lock y glosario, y los incorpora juntos antes de validar/commitear. Seguir docs/guides/staging.md. Gate de cada slice: `bun run validate`; si afecta archivos nativos, ejecutar `bun run test:export`; exportar su campaña cuando esté materializada en campaigns, nunca un borrador staging. Las plantillas de staging se comprueban como fuentes y su integración nativa queda pendiente del slice de materialización. Para cierre de contenido publicable: `bun run release:check <id>`, revisión histórica/lingüística/media y revisión independiente oficial. Registrar el commit y resultados; no marcar done mediante edición de markdown. La subida del mod es una acción separada y autorizada por el propietario.


## Contrato de diseño ampliado por el propietario

El diseño vigente está en docs/design/catalog.json y docs/design/production-contract.md; el dossier específico es docs/wiki/imperial-church/12-production-blueprint.md. La nueva fuente es en, con español completo. S1 compara el contrato cerrado y registra discrepancias; no diseña otra campaña. Los planos de escenarios, objectivePlan con ledgers, todas las pantallas, bibliografía/narrador y presupuestos estimados son instrucciones del arquitecto. Mantener identidades y claves anteriores. Dependencias ampliadas: d00001/i00002 revisadas e integradas; i00003 para capacidades faltantes y s00001 para evidencia de motor en entrega. El piloto Milvio reutiliza 01-milvian-bridge de C01, mapa360×360, como piloto real de rendimiento; no copiar infraestructura ni conservar un mapa pequeño provisional como la versión de la misión histórica. El laboratorio de rutas mantiene32×32 por su finalidad técnica. Todas las afirmaciones de balance siguen estimated hasta partidas registradas.
