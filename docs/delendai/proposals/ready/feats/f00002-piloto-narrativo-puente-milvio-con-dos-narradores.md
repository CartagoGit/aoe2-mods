---
id: f00002
title: "Piloto narrativo: Puente Milvio con dos narradores"
kind: feat
status: ready
type: proposal
track: campaign-factory
date: 2026-10-12
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

### S1 — Dossier, cronologia y brief verificado
- **Status**: pending
- **Files**: `docs/wiki/milvian-pilot/**`
- **Gate**: e2e
- acceptance:
  - "Leer Eusebio HE IX.9 y Lactancio De mortibus persecutorum 44; contrastar diferencias con historiografía académica."
  - "Documentar cada afirmación, fecha, título, geografía, facción y representación de civilización; no asumir que Byzantines equivale exactamente a Roma312."
  - "Separar tradiciones, diálogo inventado y hechos; sensibilidad cultural revisada."

### S2 — Mapa, objetivos y campaña piloto
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `campaigns/milvian-pilot/**`
- **Gate**: e2e
- acceptance:
  - "Brief cerrado, especificación completa, geografía fundada y conectividad; mapa con rutas alternativas."
  - "Economía/reservas, tres perfiles, eventos, recuperaciones para objetivo destruido antes de tiempo y personaje crítico."
  - "Intro/outro general y cronista; 17 catálogos con estados de revisión, recursos con permisos y voces por locale; ninguna API paga masiva."

### S3 — IDs y terminologia revisada
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `config/string-ids.lock.json`, `config/glossary.json`
- **Gate**: e2e
- acceptance:
  - "IDs estables sin colisión y glosario de Constantino/Majencio/cargos/religión por locale."
  - "No alterar claves de progreso ni nombres del motor al traducir."

### S4 — QA adversarial y balance medido
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `docs/qa/milvian-pilot/**`
- **Gate**: e2e
- acceptance:
  - "Casos bridge-block/critical-unit/early-destruction/exhaustion/simultaneous-terminal/save-load; pasos reproducibles y severidad."
  - "Métricas estimadas separadas de duración/pérdidas/reacción medidas; distintas estrategias en tres dificultades."
  - "Gate release completo, todas las licencias y revisión editorial; detener publicación si falla motor, idioma o permisos."

## acceptance

- Leer Eusebio HE IX.9 y Lactancio De mortibus persecutorum 44; contrastar diferencias con historiografía académica.
- Documentar cada afirmación, fecha, título, geografía, facción y representación de civilización; no asumir que Byzantines equivale exactamente a Roma312.
- Separar tradiciones, diálogo inventado y hechos; sensibilidad cultural revisada.
- Brief cerrado, especificación completa, geografía fundada y conectividad; mapa con rutas alternativas.
- Economía/reservas, tres perfiles, eventos, recuperaciones para objetivo destruido antes de tiempo y personaje crítico.
- Intro/outro general y cronista; 17 catálogos con estados de revisión, recursos con permisos y voces por locale; ninguna API paga masiva.
- IDs estables sin colisión y glosario de Constantino/Majencio/cargos/religión por locale.
- No alterar claves de progreso ni nombres del motor al traducir.
- Casos bridge-block/critical-unit/early-destruction/exhaustion/simultaneous-terminal/save-load; pasos reproducibles y severidad.
- Métricas estimadas separadas de duración/pérdidas/reacción medidas; distintas estrategias en tres dificultades.
- Gate release completo, todas las licencias y revisión editorial; detener publicación si falla motor, idioma o permisos.

## Contexto, estado inicial y dependencias

Dependencias: i00001 y piloto técnico revisados. Estado inicial: fixture técnico y herramientas presentes; contenido histórico completo no creado; evidencias de juego pendientes. Consultar el estado vivo de DelendAI antes de empezar: esta tabla no desbloquea tareas por sí sola.

## Requisitos compartidos

Leer `AGENTS.md`, `docs/production/plan.md`, `docs/architecture/overview.md`, `docs/guides/scenarios.md`, `docs/guides/history.md`, `docs/guides/narration-and-characters.md`, `docs/guides/localization.md`, `docs/guides/audio.md`, `docs/guides/visual-assets.md`, `docs/guides/ai-and-balance.md`, `docs/guides/qa.md` y `docs/guides/publishing.md`. Canonical es-ES, claves semánticas, lock global, identidad técnica permanente, 17 locales revisados, narradores general/particular y voces consistentes, recursos licenciados y enemigos con economía/reserva explicada. Las carpetas wiki siguen `docs/templates/wiki-campaign.md`.

## Riesgos y decisiones cerradas

Riesgos: pasajes históricos no consultados, anacronismos, coexistencia de cadenas, fallos de guardado/carga, prioridad terminal en un tick, licencias y tamaño del audio. Documentar resultado negativo y propuesta concreta de resolución; no suplirlo con éxito ficticio. Las dependencias narrativas siempre son opcionales para el jugador. Un problema de infraestructura corresponde al arquitecto; el agente de contenido no modifica packages/tools por su cuenta.

## Entregables, revisión y cierre

Entregar fuentes declarativas, dossier, glosario/IDs donde el slice lo permita, manifest multimedia, informes de build/QA y evidencia vinculada al artefacto. Gate de cada slice: `bun run validate`; si afecta archivos nativos, ejecutar `bun run test:export` y exportar su campaña. Para cierre de contenido publicable: `bun run release:check <id>`, revisión histórica/lingüística/media y revisión independiente oficial. Registrar el commit y resultados; no marcar done mediante edición de markdown. La subida del mod es una acción separada y autorizada por el propietario.
