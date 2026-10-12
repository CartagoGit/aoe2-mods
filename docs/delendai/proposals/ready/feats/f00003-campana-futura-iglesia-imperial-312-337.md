---
id: f00003
title: "Campana futura: Iglesia imperial 312-337"
kind: feat
status: ready
type: proposal
track: campaign-factory
date: 2026-10-12
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
- **Files**: `docs/wiki/imperial-church/**`
- **Gate**: e2e
- acceptance:
  - "Resolver afirmaciones pendientes con pasajes completos y historiografía, no solo abstracts."
  - "Fichas de Constantino, Majencio y representantes ficticios; cronista particular retrospectivo consistente; clasificación de todas las líneas."
  - "Aprobar neutralidad, anacronismos de civilizaciones y restricciones visuales antes de mapas."

### S2 — Metadatos, localizacion y medios de campaña
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `campaigns/imperial-church/campaign.json`, `campaigns/imperial-church/native/**`, `campaigns/imperial-church/assets/**`
- **Gate**: e2e
- acceptance:
  - "Metadatos permanentes, orden scenarioFiles, narrador general/particular, intro/epílogo, recap y dependencias opcionales."
  - "17 locales aprobados; reparto y pronunciación por locale; imágenes y audios con fuente/licencia/hash/revisión."
  - "Añadir escenarios por rutas previstas sin generar artefactos manualmente ni duplicar packages."

### S3 — Mision 01: control del acceso y batalla
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `campaigns/imperial-church/scenarios/01-milvian-bridge/**`
- **Gate**: e2e
- acceptance:
  - "Reutilizar diseño piloto; objetivos por fases, contingencias de puente y líder, reserva militar visible finita."
  - "Historia documentada y licencia táctica; tres dificultades con medidas tras partidas."

### S4 — Mision 02: negociacion en Nicea
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `campaigns/imperial-church/scenarios/02-nicaea/**`
- **Gate**: e2e
- acceptance:
  - "Mecánica diplomática de llegada/protección de delegaciones y recursos/negociación como dramatización."
  - "No matar confesiones para ganar, no representar una verdad doctrinal superior; resultados del concilio documentados."
  - "Variables y eventos finitos; orden alternativo, pérdidas de mensajeros y negociación agotada tienen recuperación."

### S5 — Mision 03: rutas de la nueva capital
- **Status**: pending
- **DependsOn**: [S4]
- **Files**: `campaigns/imperial-church/scenarios/03-new-capital/**`
- **Gate**: e2e
- acceptance:
  - "Economía y comercio/logística330; geografía y facciones justificadas, rutas terrestres/navales verificables."
  - "Sin repetir gran batalla; suministros vulnerables y alternativas, no oleadas sin causa."
  - "Epílogo retrospectivo hasta337 con continuidad opcional y perspectivas acumulativas."

### S6 — Registro global y auditoria de entrega
- **Status**: pending
- **DependsOn**: [S5]
- **Files**: `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/imperial-church/**`
- **Gate**: e2e
- acceptance:
  - "Reserva oficial del lock y estabilidad de IDs; glosario actualizado y revisores por locale."
  - "Todos los casos bloqueantes resueltos, métricas medidas, artefacto y evidencias coherentes."
  - "Cada criterio del gate release pasa; autorización humana requerida solo para subir mod, no durante producción reversible."

## acceptance

- Resolver afirmaciones pendientes con pasajes completos y historiografía, no solo abstracts.
- Fichas de Constantino, Majencio y representantes ficticios; cronista particular retrospectivo consistente; clasificación de todas las líneas.
- Aprobar neutralidad, anacronismos de civilizaciones y restricciones visuales antes de mapas.
- Metadatos permanentes, orden scenarioFiles, narrador general/particular, intro/epílogo, recap y dependencias opcionales.
- 17 locales aprobados; reparto y pronunciación por locale; imágenes y audios con fuente/licencia/hash/revisión.
- Añadir escenarios por rutas previstas sin generar artefactos manualmente ni duplicar packages.
- Reutilizar diseño piloto; objetivos por fases, contingencias de puente y líder, reserva militar visible finita.
- Historia documentada y licencia táctica; tres dificultades con medidas tras partidas.
- Mecánica diplomática de llegada/protección de delegaciones y recursos/negociación como dramatización.
- No matar confesiones para ganar, no representar una verdad doctrinal superior; resultados del concilio documentados.
- Variables y eventos finitos; orden alternativo, pérdidas de mensajeros y negociación agotada tienen recuperación.
- Economía y comercio/logística330; geografía y facciones justificadas, rutas terrestres/navales verificables.
- Sin repetir gran batalla; suministros vulnerables y alternativas, no oleadas sin causa.
- Epílogo retrospectivo hasta337 con continuidad opcional y perspectivas acumulativas.
- Reserva oficial del lock y estabilidad de IDs; glosario actualizado y revisores por locale.
- Todos los casos bloqueantes resueltos, métricas medidas, artefacto y evidencias coherentes.
- Cada criterio del gate release pasa; autorización humana requerida solo para subir mod, no durante producción reversible.

## Contexto, estado inicial y dependencias

Dependencias: i00001, piloto técnico y piloto narrativo revisados. Estado inicial: fixture técnico y herramientas presentes; contenido histórico completo no creado; evidencias de juego pendientes. Consultar el estado vivo de DelendAI antes de empezar: esta tabla no desbloquea tareas por sí sola.

## Requisitos compartidos

Leer `AGENTS.md`, `docs/production/plan.md`, `docs/architecture/overview.md`, `docs/guides/scenarios.md`, `docs/guides/history.md`, `docs/guides/narration-and-characters.md`, `docs/guides/localization.md`, `docs/guides/audio.md`, `docs/guides/visual-assets.md`, `docs/guides/ai-and-balance.md`, `docs/guides/qa.md` y `docs/guides/publishing.md`. Canonical es-ES, claves semánticas, lock global, identidad técnica permanente, 17 locales revisados, narradores general/particular y voces consistentes, recursos licenciados y enemigos con economía/reserva explicada. Las carpetas wiki siguen `docs/templates/wiki-campaign.md`.

## Riesgos y decisiones cerradas

Riesgos: pasajes históricos no consultados, anacronismos, coexistencia de cadenas, fallos de guardado/carga, prioridad terminal en un tick, licencias y tamaño del audio. Documentar resultado negativo y propuesta concreta de resolución; no suplirlo con éxito ficticio. Las dependencias narrativas siempre son opcionales para el jugador. Un problema de infraestructura corresponde al arquitecto; el agente de contenido no modifica packages/tools por su cuenta.

## Entregables, revisión y cierre

Entregar fuentes declarativas, dossier, glosario/IDs donde el slice lo permita, manifest multimedia, informes de build/QA y evidencia vinculada al artefacto. Gate de cada slice: `bun run validate`; si afecta archivos nativos, ejecutar `bun run test:export` y exportar su campaña. Para cierre de contenido publicable: `bun run release:check <id>`, revisión histórica/lingüística/media y revisión independiente oficial. Registrar el commit y resultados; no marcar done mediante edición de markdown. La subida del mod es una acción separada y autorizada por el propietario.
