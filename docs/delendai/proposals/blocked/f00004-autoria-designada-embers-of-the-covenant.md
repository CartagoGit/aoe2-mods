---
id: f00004
title: "Autoria designada: Embers of the Covenant"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: ea45b8aa-2ca2-4146-86e5-41799fddfb2a
last-correlation-id: ea45b8aa-2ca2-4146-86e5-41799fddfb2a
last-transition-from: ready
last-transition-at: 2026-10-12T14:24:02.846Z
---

# f00004 — Autoria designada: Embers of the Covenant

## goal

MiniMax M3.1 materializa `faith-origins` / CDF-C00 como odisea independiente de 30 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. Esta propuesta permanece bloqueada: una selección de episodios no es un contrato aprobado.

## why

La ampliación del propietario reemplaza la extensión de la base de 39 misiones. Se conserva cada ID de campaña, progreso, escenario y slice existente; el orden de episodio es independiente del número S. Los nuevos slices identifican cada trabajo adicional, sin encargar historia, geografía, diseño o nivelación a MiniMax.

## non-goals

- No diseñar historia, mapas, narradores, objetivos, arquitectura o balance por iniciativa del agente de contenido.
- No representar la falta de capacidad con un temporizador, texto, refuerzo infinito o stock duplicado.
- No confundir selección, dossier, exportación o test estático con GAME VERIFIED; sin publicación ni generación pagada masiva.

## prerequisites

`d00002` completo y revisado para esta odisea; `i00003` con las capacidades usadas implementadas; `f00001` y `f00002` pilotos acreditados; `s00001` con evidencia de motor. Recuperar dependencias y estados vivos de DelendAI. No cambiar blocked por tener este documento ni por contar carpetas.

## fuentes de trabajo y actos

Fuente editorial: `docs/design/odysseys/faith-origins.json`. Índice: `docs/wiki/faith-origins/14-odyssey-arc.md`. Expediente de cada misión: `docs/wiki/faith-origins/episodes/<scenarioId>/15-odyssey-dossier.md`, disponible solo cuando se haya redactado. Los documentos anteriores de la base son antecedentes; no autorizan ejecutar un antiguo final a mitad del arco ampliado.

| Acto | Título fuente | Episodios en orden | Slices asignados |
|---|---|---|---|
| act-1 | Names Before the Ashes | 1, 2, 3, 4, 5, 6, 7, 8 | S8, S9, S10, S11, S12, S3, S13, S14 |
| act-2 | Across the Many Roads | 9, 10, 11, 12, 13, 14, 15 | S15, S16, S17, S18, S19, S20, S21 |
| act-3 | Under a Broken Roof | 16, 17, 18, 19, 20, 21 | S22, S4, S23, S24, S25, S5 |
| act-4 | Voices Before the Tribunal | 22, 23, 24, 25, 26, 27 | S26, S27, S28, S29, S30, S31 |
| act-5 | The Archive and the Dawn | 28, 29, 30 | S32, S33, S6 |

## slices

- global_gate: e2e

### S1 — Comprobar los expedientes aprobados sin rediseñarlos
- **Status**: pending
- **Files**: `docs/qa/faith-origins/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Verificar los 30 expedientes completos de faith-origins, cinco actos, pasajes consultados y revisión independiente del arquitecto. Si falta un objetivo, mapa, pantalla o nivelación, informar la brecha; no decidirlo MiniMax."
  - "Contrastar IDs estables, sourceLocale=en, EN/es-ES completos, voz factual común antes de persona situada y orden de campaña no bloqueante; conservar estados pendientes de otros idiomas y medios."

### S2 — Metadatos, pantallas de campaña y medios en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/faith-origins/campaign.json`, `staging/campaigns/faith-origins/native`, `staging/campaigns/faith-origins/assets`
- **Gate**: e2e
- acceptance:
  - "Materializar la arquitectura editorial aprobada: persona propia, recaps y aviso de predecesora recomendado sin bloqueo; recordar elecciones acumulativas sin borrar otras claves ni autoiniciar otra campaña."
  - "EN/es-ES completos con claves semánticas, captions y manifiestos con hash/licencia; solo medios aprobados, sin fotos restauradas presentadas como escena antigua. staging:check --partial sin promover contenido parcial."

### S8 — Episodio 1: Stone Beneath the Prefect's Name
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/faith-origins/scenarios/01-administrative-records-caesarea`, `docs/qa/faith-origins/episodes/01-administrative-records-caesarea`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-administrative-records-caesarea
- **Order**: 1
- **HistoricalFrame**: 27–36 CE; geography=caesarea; core=administrative-records
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/01-administrative-records-caesarea: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S9 — Episodio 2: When the City Held Its Breath
- **Status**: pending
- **DependsOn**: [S8]
- **Files**: `staging/campaigns/faith-origins/scenarios/02-civilian-refuge-jerusalem`, `docs/qa/faith-origins/episodes/02-civilian-refuge-jerusalem`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-civilian-refuge-jerusalem
- **Order**: 2
- **HistoricalFrame**: c. 30–33 CE; geography=jerusalem; core=civilian-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/02-civilian-refuge-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 3: A Table in Jerusalem
- **Status**: pending
- **DependsOn**: [S9]
- **Files**: `staging/campaigns/faith-origins/scenarios/03-shared-provision-jerusalem`, `docs/qa/faith-origins/episodes/03-shared-provision-jerusalem`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-shared-provision-jerusalem
- **Order**: 3
- **HistoricalFrame**: c. 30–40 CE; geography=jerusalem; core=shared-provision
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/03-shared-provision-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S11 — Episodio 4: The Road He Remembered
- **Status**: pending
- **DependsOn**: [S10]
- **Files**: `staging/campaigns/faith-origins/scenarios/04-testimony-relay-damascus`, `docs/qa/faith-origins/episodes/04-testimony-relay-damascus`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 04-testimony-relay-damascus
- **Order**: 4
- **HistoricalFrame**: c. 33–36 CE; geography=damascus; core=testimony-relay
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/04-testimony-relay-damascus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S12 — Episodio 5: Fifteen Days, Many Voices
- **Status**: pending
- **DependsOn**: [S11]
- **Files**: `staging/campaigns/faith-origins/scenarios/05-witness-comparison-jerusalem`, `docs/qa/faith-origins/episodes/05-witness-comparison-jerusalem`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 05-witness-comparison-jerusalem
- **Order**: 5
- **HistoricalFrame**: c. 36–40 CE; geography=jerusalem; core=witness-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/05-witness-comparison-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S3 — Episodio 6: Letters on the Orontes
- **Status**: pending
- **DependsOn**: [S12]
- **Files**: `staging/campaigns/faith-origins/scenarios/01-roads-of-antioch`, `docs/qa/faith-origins/episodes/01-roads-of-antioch`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-roads-of-antioch
- **Order**: 6
- **HistoricalFrame**: c. 40–49 CE; conventional early-network reconstruction; geography=antioch; core=network-escort
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/01-roads-of-antioch: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S13 — Episodio 7: The Doors That Closed
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `staging/campaigns/faith-origins/scenarios/07-household-relocation-rome-ostia`, `docs/qa/faith-origins/episodes/07-household-relocation-rome-ostia`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 07-household-relocation-rome-ostia
- **Order**: 7
- **HistoricalFrame**: c. 49 CE; geography=rome-ostia; core=household-relocation
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/07-household-relocation-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 8: A Place for the Stranger
- **Status**: pending
- **DependsOn**: [S13]
- **Files**: `staging/campaigns/faith-origins/scenarios/08-delegate-logistics-jerusalem`, `docs/qa/faith-origins/episodes/08-delegate-logistics-jerusalem`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 08-delegate-logistics-jerusalem
- **Order**: 8
- **HistoricalFrame**: c. 49–50 CE; identification of meetings disputed; geography=jerusalem; core=delegate-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/08-delegate-logistics-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S15 — Episodio 9: The Weaver's Harbour
- **Status**: pending
- **DependsOn**: [S14]
- **Files**: `staging/campaigns/faith-origins/scenarios/09-district-production-corinth`, `docs/qa/faith-origins/episodes/09-district-production-corinth`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 09-district-production-corinth
- **Order**: 9
- **HistoricalFrame**: c. 50–52 CE; geography=corinth; core=district-production
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/09-district-production-corinth: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S16 — Episodio 10: Before the First Letter Faded
- **Status**: pending
- **DependsOn**: [S15]
- **Files**: `staging/campaigns/faith-origins/scenarios/10-copy-and-relay-corinth`, `docs/qa/faith-origins/episodes/10-copy-and-relay-corinth`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-copy-and-relay-corinth
- **Order**: 10
- **HistoricalFrame**: c. 50–51 CE; geography=corinth; core=copy-and-relay
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/10-copy-and-relay-corinth: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S17 — Episodio 11: The Argument Across the Water
- **Status**: pending
- **DependsOn**: [S16]
- **Files**: `staging/campaigns/faith-origins/scenarios/11-distributed-preservation-ephesus`, `docs/qa/faith-origins/episodes/11-distributed-preservation-ephesus`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 11-distributed-preservation-ephesus
- **Order**: 11
- **HistoricalFrame**: c. 54–55 CE; writing location uncertain; geography=ephesus; core=distributed-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/11-distributed-preservation-ephesus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S18 — Episodio 12: Many Hands in One House
- **Status**: pending
- **DependsOn**: [S17]
- **Files**: `staging/campaigns/faith-origins/scenarios/12-bounded-community-aid-ephesus`, `docs/qa/faith-origins/episodes/12-bounded-community-aid-ephesus`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 12-bounded-community-aid-ephesus
- **Order**: 12
- **HistoricalFrame**: c. 54–55 CE; geography=ephesus; core=bounded-community-aid
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/12-bounded-community-aid-ephesus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S19 — Episodio 13: Words for a Distant City
- **Status**: pending
- **DependsOn**: [S18]
- **Files**: `staging/campaigns/faith-origins/scenarios/13-consignment-and-correspondence-corinth`, `docs/qa/faith-origins/episodes/13-consignment-and-correspondence-corinth`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 13-consignment-and-correspondence-corinth
- **Order**: 13
- **HistoricalFrame**: c. 56–58 CE; geography=corinth; core=consignment-and-correspondence
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/13-consignment-and-correspondence-corinth: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 14: The Appeal Beside the Sea
- **Status**: pending
- **DependsOn**: [S19]
- **Files**: `staging/campaigns/faith-origins/scenarios/14-administrative-intrigue-caesarea`, `docs/qa/faith-origins/episodes/14-administrative-intrigue-caesarea`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 14-administrative-intrigue-caesarea
- **Order**: 14
- **HistoricalFrame**: c. 57–60 CE; geography=caesarea; core=administrative-intrigue
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/14-administrative-intrigue-caesarea: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S21 — Episodio 15: Ash over the Seven Hills
- **Status**: pending
- **DependsOn**: [S20]
- **Files**: `staging/campaigns/faith-origins/scenarios/15-evacuation-and-recovery-rome-ostia`, `docs/qa/faith-origins/episodes/15-evacuation-and-recovery-rome-ostia`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 15-evacuation-and-recovery-rome-ostia
- **Order**: 15
- **HistoricalFrame**: 64 CE; geography=rome-ostia; core=evacuation-and-recovery
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/15-evacuation-and-recovery-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S22 — Episodio 16: A Story in the Shadow of War
- **Status**: pending
- **DependsOn**: [S21]
- **Files**: `staging/campaigns/faith-origins/scenarios/16-comparative-copying-antioch`, `docs/qa/faith-origins/episodes/16-comparative-copying-antioch`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 16-comparative-copying-antioch
- **Order**: 16
- **HistoricalFrame**: c. 65–70 CE; authorial location not known; geography=antioch; core=comparative-copying
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/16-comparative-copying-antioch: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S4 — Episodio 17: The Names Beyond the Siege
- **Status**: pending
- **DependsOn**: [S22]
- **Files**: `staging/campaigns/faith-origins/scenarios/02-after-the-siege`, `docs/qa/faith-origins/episodes/02-after-the-siege`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 02-after-the-siege
- **Order**: 17
- **HistoricalFrame**: 70 CE; geography=jerusalem; core=civilian-evacuation
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/02-after-the-siege: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S23 — Episodio 18: Two Voices, Unfinished Margins
- **Status**: pending
- **DependsOn**: [S4]
- **Files**: `staging/campaigns/faith-origins/scenarios/18-parallel-archive-logistics-antioch`, `docs/qa/faith-origins/episodes/18-parallel-archive-logistics-antioch`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 18-parallel-archive-logistics-antioch
- **Order**: 18
- **HistoricalFrame**: c. 80–90 CE; location is fictional local circulation, not authorial provenance; geography=antioch; core=parallel-archive-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/18-parallel-archive-logistics-antioch: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S24 — Episodio 19: The House Before the Road
- **Status**: pending
- **DependsOn**: [S23]
- **Files**: `staging/campaigns/faith-origins/scenarios/19-hospitality-network-antioch`, `docs/qa/faith-origins/episodes/19-hospitality-network-antioch`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 19-hospitality-network-antioch
- **Order**: 19
- **HistoricalFrame**: c. 90–100 CE; Syrian provenance proposed; geography=antioch; core=hospitality-network
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/19-hospitality-network-antioch: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 20: A Letter Across the Divide
- **Status**: pending
- **DependsOn**: [S24]
- **Files**: `staging/campaigns/faith-origins/scenarios/20-reconciliation-deliveries-rome-ostia`, `docs/qa/faith-origins/episodes/20-reconciliation-deliveries-rome-ostia`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 20-reconciliation-deliveries-rome-ostia
- **Order**: 20
- **HistoricalFrame**: c. 95 CE; geography=rome-ostia; core=reconciliation-deliveries
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/20-reconciliation-deliveries-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 21: The Governor's Question
- **Status**: pending
- **DependsOn**: [S25]
- **Files**: `staging/campaigns/faith-origins/scenarios/03-the-governors-question`, `docs/qa/faith-origins/episodes/03-the-governors-question`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 03-the-governors-question
- **Order**: 21
- **HistoricalFrame**: c. 112 CE; geography=bithynia; core=administrative-intrigue
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/03-the-governors-question: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S26 — Episodio 22: Bread Read Aloud
- **Status**: pending
- **DependsOn**: [S5]
- **Files**: `staging/campaigns/faith-origins/scenarios/22-reading-and-relief-rome-ostia`, `docs/qa/faith-origins/episodes/22-reading-and-relief-rome-ostia`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 22-reading-and-relief-rome-ostia
- **Order**: 22
- **HistoricalFrame**: c. 150–160 CE; geography=rome-ostia; core=reading-and-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/22-reading-and-relief-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S27 — Episodio 23: A Petition from Sardes
- **Status**: pending
- **DependsOn**: [S26]
- **Files**: `staging/campaigns/faith-origins/scenarios/23-petition-escort-sardes`, `docs/qa/faith-origins/episodes/23-petition-escort-sardes`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-petition-escort-sardes
- **Order**: 23
- **HistoricalFrame**: c. 170–180 CE; geography=sardes; core=petition-escort
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/23-petition-escort-sardes: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S28 — Episodio 24: The River Kept Their Names
- **Status**: pending
- **DependsOn**: [S27]
- **Files**: `staging/campaigns/faith-origins/scenarios/24-witness-and-evacuation-lyon`, `docs/qa/faith-origins/episodes/24-witness-and-evacuation-lyon`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 24-witness-and-evacuation-lyon
- **Order**: 24
- **HistoricalFrame**: 177 CE; geography=lyon; core=witness-and-evacuation
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/24-witness-and-evacuation-lyon: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S29 — Episodio 25: Voices Against the Fragments
- **Status**: pending
- **DependsOn**: [S28]
- **Files**: `staging/campaigns/faith-origins/scenarios/25-archive-comparison-lyon`, `docs/qa/faith-origins/episodes/25-archive-comparison-lyon`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 25-archive-comparison-lyon
- **Order**: 25
- **HistoricalFrame**: c. 180–200 CE; geography=lyon; core=archive-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/25-archive-comparison-lyon: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S30 — Episodio 26: The Advocate's Harbour
- **Status**: pending
- **DependsOn**: [S29]
- **Files**: `staging/campaigns/faith-origins/scenarios/26-legal-record-network-carthage`, `docs/qa/faith-origins/episodes/26-legal-record-network-carthage`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 26-legal-record-network-carthage
- **Order**: 26
- **HistoricalFrame**: c. 197 CE; geography=carthage; core=legal-record-network
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/26-legal-record-network-carthage: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S31 — Episodio 27: What the Record Cannot Hold
- **Status**: pending
- **DependsOn**: [S30]
- **Files**: `staging/campaigns/faith-origins/scenarios/27-household-aid-and-memory-carthage`, `docs/qa/faith-origins/episodes/27-household-aid-and-memory-carthage`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 27-household-aid-and-memory-carthage
- **Order**: 27
- **HistoricalFrame**: 203 CE; geography=carthage; core=household-aid-and-memory
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/27-household-aid-and-memory-carthage: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S32 — Episodio 28: The Seal on the Certificate
- **Status**: pending
- **DependsOn**: [S31]
- **Files**: `staging/campaigns/faith-origins/scenarios/28-certificate-and-refuge-egypt-middle-nile`, `docs/qa/faith-origins/episodes/28-certificate-and-refuge-egypt-middle-nile`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 28-certificate-and-refuge-egypt-middle-nile
- **Order**: 28
- **HistoricalFrame**: 249–251 CE; geography=egypt-middle-nile; core=certificate-and-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/28-certificate-and-refuge-egypt-middle-nile: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S33 — Episodio 29: A Harbour Under Orders
- **Status**: pending
- **DependsOn**: [S32]
- **Files**: `staging/campaigns/faith-origins/scenarios/29-bounded-evacuation-carthage`, `docs/qa/faith-origins/episodes/29-bounded-evacuation-carthage`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 29-bounded-evacuation-carthage
- **Order**: 29
- **HistoricalFrame**: 257–258 CE; geography=carthage; core=bounded-evacuation
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/29-bounded-evacuation-carthage: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S6 — Episodio 30: A Different Dawn
- **Status**: pending
- **DependsOn**: [S33]
- **Files**: `staging/campaigns/faith-origins/scenarios/04-a-different-dawn`, `docs/qa/faith-origins/episodes/04-a-different-dawn`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 04-a-different-dawn
- **Order**: 30
- **HistoricalFrame**: 303–313 CE; Milan local archive is dramatization, persecution and restitution vary regionally; geography=milan; core=supply-and-testimony
- acceptance:
  - "Materializar únicamente el expediente aprobado faith-origins/04-a-different-dawn: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S7 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S6]
- **Files**: `staging/campaigns/faith-origins`, `campaigns/faith-origins`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/faith-origins/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 30 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 30 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates previos reales; sin atribuir a MiniMax el cierre de decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
