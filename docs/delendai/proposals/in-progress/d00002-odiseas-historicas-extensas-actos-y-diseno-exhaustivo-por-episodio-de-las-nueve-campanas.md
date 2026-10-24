---
id: d00002
title: "Odiseas historicas extensas: actos y diseno exhaustivo por episodio de las nueve campanas"
kind: docs
status: in-progress
type: proposal
track: historical-odysseys
date: 2026-10-12
---

# d00002 — Odiseas historicas extensas: actos y diseno exhaustivo por episodio de las nueve campanas

## goal

Ampliar la base aprobada de39escenarios a nueve odiseas independientes con objetivo editorial278episodios (30/34/30/32/32/30/28/32/30), ajustable solo por evidencia y calidad, sin relleno. El arquitecto cierra cronología, arcos, cada pantalla EN/es, narradores, objetivos, mapas reales gigantes y nivelación antes de MiniMax.

## why

El usuario solicita campañas largas comparables en escala a su referencia mod550831, cada una historia paso a paso de su tradición. La base39no satisface el alcance ampliado.

## non-goals

- No producir ahora campañas históricas nativas completas ni publicar mods.
- No copiar contenido del mod de referencia ni afirmar haber inspeccionado sus archivos sin obtenerlos;licencias/artes se registran.
- No declarar perfecto el balance sin partidas, ni delegar decisiones de arquitectura/balance en Luna oMiniMax.

## slices

- global_gate: e2e

### S1 — Arquitectura editorial de odiseas, investigación y generación reutilizable
- **Status**: review
- **Files**: `tools/design/**`, `docs/design/odyssey-policy.json`, `docs/design/odyssey-production-plan.md`, `docs/design/odyssey-selections.md`, `docs/research/odyssey-research/**`
- **Gate**: e2e
- acceptance:
  - "Plan explícito de nueve odiseas por actos y curva de dificultad, criterio de hito documentado sin relleno y límites históricos/licencias."
  - "Investigación delegada contrastada por arquitecto; generadores comunes y validación de contratos sin clonar lógica por escenario."
- review-state: in_review
- review-implementer: gpt-6

### S2 — Embers of the Covenant: expediente de odisea y episodios
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/design/odysseys/faith-origins.json`, `docs/wiki/faith-origins/**`, `docs/design/maps/faith-origins/**`
- **Gate**: e2e
- acceptance:
  - "Objetivo editorial30episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro."
  - "Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico."
  - "Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos."

### S3 — The Eagle and the Cross: expediente de odisea y episodios
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/design/odysseys/imperial-church.json`, `docs/wiki/imperial-church/**`, `docs/design/maps/imperial-church/**`
- **Gate**: e2e
- acceptance:
  - "Objetivo editorial34episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro."
  - "Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico."
  - "Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos."

### S4 — Keepers of the Unbroken Word: expediente de odisea y episodios
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/design/odysseys/jewish-tradition.json`, `docs/wiki/jewish-tradition/**`, `docs/design/maps/jewish-tradition/**`
- **Gate**: e2e
- acceptance:
  - "Objetivo editorial30episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro."
  - "Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico."
  - "Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos."

### S5 — The Keys of the Eternal City: expediente de odisea y episodios
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/design/odysseys/church-of-rome.json`, `docs/wiki/church-of-rome/**`, `docs/design/maps/church-of-rome/**`
- **Gate**: e2e
- acceptance:
  - "Objetivo editorial32episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro."
  - "Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico."
  - "Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos."

### S6 — Beyond the Golden Gate: expediente de odisea y episodios
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/design/odysseys/new-rome.json`, `docs/wiki/new-rome/**`, `docs/design/maps/new-rome/**`
- **Gate**: e2e
- acceptance:
  - "Objetivo editorial32episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro."
  - "Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico."
  - "Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos."

### S7 — Beneath the Desert Stars: expediente de odisea y episodios
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/design/odysseys/first-caliphs.json`, `docs/wiki/first-caliphs/**`, `docs/design/maps/first-caliphs/**`
- **Gate**: e2e
- acceptance:
  - "Objetivo editorial30episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro."
  - "Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico."
  - "Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos."

### S8 — The Shattered Oath: expediente de odisea y episodios
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/design/odysseys/first-fitna.json`, `docs/wiki/first-fitna/**`, `docs/design/maps/first-fitna/**`
- **Gate**: e2e
- acceptance:
  - "Objetivo editorial28episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro."
  - "Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico."
  - "Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos."

### S9 — From Damascus to the Far Horizon: expediente de odisea y episodios
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/design/odysseys/umayyads.json`, `docs/wiki/umayyads/**`, `docs/design/maps/umayyads/**`
- **Gate**: e2e
- acceptance:
  - "Objetivo editorial32episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro."
  - "Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico."
  - "Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos."

### S10 — The River Remembers: expediente de odisea y episodios
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `docs/design/odysseys/house-of-ali.json`, `docs/wiki/house-of-ali/**`, `docs/design/maps/house-of-ali/**`
- **Gate**: e2e
- acceptance:
  - "Objetivo editorial30episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro."
  - "Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico."
  - "Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos."

### S11 — Catálogo consolidado, propuestas por acto y traspaso mecánico
- **Status**: pending
- **DependsOn**: [S2, S3, S4, S5, S6, S7, S8, S9, S10]
- **Files**: `docs/design/catalog.json`, `docs/design/geography.json`, `docs/design/sources.json`, `docs/design/assignments.json`, `docs/design/README.md`, `docs/design/production-contract.md`, `docs/handoffs/**`, `docs/qa/campaign-design/**`, `docs/production/**`, `docs/delendai/proposals/**`, `README.md`
- **Gate**: e2e
- acceptance:
  - "Cada propuesta DelendAI tiene slices por actos/episodios y contratos exactos para MiniMax; revisión independiente y gate antes de integración."
  - "Entradas y cierres con recap/continuación específica, avisos no bloqueantes, cronologías solapadas declaradas e identidad estable."
  - "Catálogo consolidado y wiki reproducibles; QA de juego pendiente explicitamente, sin presentar documentación como campaña implementada."

## acceptance

- Plan explícito de nueve odiseas por actos y curva de dificultad, criterio de hito documentado sin relleno y límites históricos/licencias.
- Investigación delegada contrastada por arquitecto; generadores comunes y validación de contratos sin clonar lógica por escenario.
- Objetivo editorial30episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro.
- Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico.
- Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos.
- Objetivo editorial34episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro.
- Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico.
- Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos.
- Objetivo editorial30episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro.
- Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico.
- Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos.
- Objetivo editorial32episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro.
- Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico.
- Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos.
- Objetivo editorial32episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro.
- Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico.
- Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos.
- Objetivo editorial30episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro.
- Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico.
- Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos.
- Objetivo editorial28episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro.
- Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico.
- Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos.
- Objetivo editorial32episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro.
- Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico.
- Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos.
- Objetivo editorial30episodios coherentes, cada uno con fecha/fuente/pasaje/cautela,geografía, arco y rol del narrador sin conocimiento futuro.
- Cada episodio especifica tres perfiles, estados/ledgers compuestos, eventos, pantallas EN/es y plano; retos distintos y puntos de inflexión claros, preservando desenlace histórico.
- Reusar infraestructura y registrar capacidades faltantes; no aceptar cartas sin destino, familias distintas, alias ni timers sustituyendo hechos.
- Cada propuesta DelendAI tiene slices por actos/episodios y contratos exactos para MiniMax; revisión independiente y gate antes de integración.
- Entradas y cierres con recap/continuación específica, avisos no bloqueantes, cronologías solapadas declaradas e identidad estable.
- Catálogo consolidado y wiki reproducibles; QA de juego pendiente explicitamente, sin presentar documentación como campaña implementada.

## Requisitos adicionales del propietario

La migración de TypeScript a nombres responsabilidad.tipo.ts sin index/barrels pertenece a i00004. Todos los escenarios deben ofrecer6–8objetivos secundarios viables, cuatro mecánicas y tres formas de jugar; cada tarea fija sus requisitos compuestos, recompensa o consecuencia finita, coste de oportunidad, estado persistente y fallos opcionales que no bloquean la victoria principal. Los fondos se reasignan sin sumar depósitos anteriores; los receptores y miradores son independientes y se auditan espacialmente. Estos criterios se aplican a todos los episodios nuevos además de la base39.


## Enmienda de cobertura imperial, 2026-10-15

Cinco puntos de inflexión365–380 amplían imperial-church de29a34selecciones y el total273a278. Véase docs/design/imperial-coverage-amendment.md. Se conservan todos los IDs previos, cinco actos y claves de progreso; el final sigue siendo el escenario semántico29-council-and-final-perspective-constantinople, ahora orden34. Son selecciones con fuentes acotadas, no cinco dossiers aprobados ni autoría desbloqueada.
