---
id: f00006
title: "Autoria designada: The Keys of the Eternal City"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: 7d6237c9-5302-4013-9921-ca7b9b5d0f4c
last-correlation-id: 7d6237c9-5302-4013-9921-ca7b9b5d0f4c
last-transition-from: ready
last-transition-at: 2026-10-12T14:24:19.895Z
---

# f00006 — Autoria designada: The Keys of the Eternal City

## goal

MiniMax M3.1 materializa `church-of-rome` / CDF-C03 como odisea independiente de 32 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. Esta propuesta permanece bloqueada: una selección de episodios no es un contrato aprobado.

## why

La ampliación del propietario reemplaza la extensión de la base de 39 misiones. Se conserva cada ID de campaña, progreso, escenario y slice existente; el orden de episodio es independiente del número S. Los nuevos slices identifican cada trabajo adicional, sin encargar historia, geografía, diseño o nivelación a MiniMax.

## non-goals

- No diseñar historia, mapas, narradores, objetivos, arquitectura o balance por iniciativa del agente de contenido.
- No representar la falta de capacidad con un temporizador, texto, refuerzo infinito o stock duplicado.
- No confundir selección, dossier, exportación o test estático con GAME VERIFIED; sin publicación ni generación pagada masiva.

## prerequisites

`d00002` completo y revisado para esta odisea; `i00003` con las capacidades usadas implementadas; `f00001` y `f00002` pilotos acreditados; `s00001` con evidencia de motor. Recuperar dependencias y estados vivos de DelendAI. No cambiar blocked por tener este documento ni por contar carpetas.

## fuentes de trabajo y actos

Fuente editorial: `docs/design/odysseys/church-of-rome.json`. Índice: `docs/wiki/church-of-rome/14-odyssey-arc.md`. Expediente de cada misión: `docs/wiki/church-of-rome/episodes/<scenarioId>/15-odyssey-dossier.md`, disponible solo cuando se haya redactado. Los documentos anteriores de la base son antecedentes; no autorizan ejecutar un antiguo final a mitad del arco ampliado.

| Acto | Título fuente | Episodios en orden | Slices asignados |
|---|---|---|---|
| act-1 | Two Claims to One City | 1, 2, 3, 4, 5, 6 | S8, S9, S10, S11, S12, S13 |
| act-2 | Bread After the Empire | 7, 8, 9, 10, 11, 12 | S3, S14, S15, S16, S17, S18 |
| act-3 | Through the Gothic Ashes | 13, 14, 15, 16, 17, 18 | S19, S20, S21, S22, S4, S23 |
| act-4 | Keys Between Two Courts | 19, 20, 21, 22, 23, 24, 25 | S24, S25, S26, S27, S28, S29, S30 |
| act-5 | The Crown and the Road | 26, 27, 28, 29, 30, 31, 32 | S31, S5, S32, S33, S34, S35, S6 |

## slices

- global_gate: e2e

### S1 — Comprobar los expedientes aprobados sin rediseñarlos
- **Status**: pending
- **Files**: `docs/qa/church-of-rome/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Verificar los 32 expedientes completos de church-of-rome, cinco actos, pasajes consultados y revisión independiente del arquitecto. Si falta un objetivo, mapa, pantalla o nivelación, informar la brecha; no decidirlo MiniMax."
  - "Contrastar IDs estables, sourceLocale=en, EN/es-ES completos, voz factual común antes de persona situada y orden de campaña no bloqueante; conservar estados pendientes de otros idiomas y medios."

### S2 — Metadatos, pantallas de campaña y medios en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/church-of-rome/campaign.json`, `staging/campaigns/church-of-rome/native`, `staging/campaigns/church-of-rome/assets`
- **Gate**: e2e
- acceptance:
  - "Materializar la arquitectura editorial aprobada: persona propia, recaps y aviso de predecesora recomendado sin bloqueo; recordar elecciones acumulativas sin borrar otras claves ni autoiniciar otra campaña."
  - "EN/es-ES completos con claves semánticas, captions y manifiestos con hash/licencia; solo medios aprobados, sin fotos restauradas presentadas como escena antigua. staging:check --partial sin promover contenido parcial."

### S8 — Episodio 1: A Stranger at the Roman Door
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/01-refuge-and-petition-reception-rome-ostia`, `docs/qa/church-of-rome/episodes/01-refuge-and-petition-reception-rome-ostia`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-refuge-and-petition-reception-rome-ostia
- **Order**: 1
- **HistoricalFrame**: 339–340 CE; geography=rome-ostia; core=refuge-and-petition-reception
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/01-refuge-and-petition-reception-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S9 — Episodio 2: A Road to Two Councils
- **Status**: pending
- **DependsOn**: [S8]
- **Files**: `staging/campaigns/church-of-rome/scenarios/02-separate-delegation-logistics-sardica`, `docs/qa/church-of-rome/episodes/02-separate-delegation-logistics-sardica`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-separate-delegation-logistics-sardica
- **Order**: 2
- **HistoricalFrame**: 343 CE; chronology qualified; geography=sardica; core=separate-delegation-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/02-separate-delegation-logistics-sardica: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 3: Letters to a Distant Bishop
- **Status**: pending
- **DependsOn**: [S9]
- **Files**: `staging/campaigns/church-of-rome/scenarios/03-exile-supply-and-correspondence-beroea-thrace`, `docs/qa/church-of-rome/episodes/03-exile-supply-and-correspondence-beroea-thrace`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-exile-supply-and-correspondence-beroea-thrace
- **Order**: 3
- **HistoricalFrame**: 355–357 CE; geography=beroea-thrace; core=exile-supply-and-correspondence
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/03-exile-supply-and-correspondence-beroea-thrace: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S11 — Episodio 4: The Formula by the Sea
- **Status**: pending
- **DependsOn**: [S10]
- **Files**: `staging/campaigns/church-of-rome/scenarios/04-draft-and-delegate-network-rimini`, `docs/qa/church-of-rome/episodes/04-draft-and-delegate-network-rimini`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 04-draft-and-delegate-network-rimini
- **Order**: 4
- **HistoricalFrame**: 359 CE; geography=rimini; core=draft-and-delegate-network
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/04-draft-and-delegate-network-rimini: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S12 — Episodio 5: Two Names for the Same Chair
- **Status**: pending
- **DependsOn**: [S11]
- **Files**: `staging/campaigns/church-of-rome/scenarios/05-neutral-civilian-extraction-rome-ostia`, `docs/qa/church-of-rome/episodes/05-neutral-civilian-extraction-rome-ostia`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 05-neutral-civilian-extraction-rome-ostia
- **Order**: 5
- **HistoricalFrame**: 366–367 CE; factional violence; geography=rome-ostia; core=neutral-civilian-extraction
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/05-neutral-civilian-extraction-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S13 — Episodio 6: The Door That Stayed Closed
- **Status**: pending
- **DependsOn**: [S12]
- **Files**: `staging/campaigns/church-of-rome/scenarios/06-petition-and-accountability-records-milan`, `docs/qa/church-of-rome/episodes/06-petition-and-accountability-records-milan`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 06-petition-and-accountability-records-milan
- **Order**: 6
- **HistoricalFrame**: 390 CE; massacre in Thessalonica reported off-map; geography=milan; core=petition-and-accountability-records
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/06-petition-and-accountability-records-milan: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S3 — Episodio 7: Bread beyond the Gates
- **Status**: pending
- **DependsOn**: [S13]
- **Files**: `staging/campaigns/church-of-rome/scenarios/01-bread-beyond-the-gates`, `docs/qa/church-of-rome/episodes/01-bread-beyond-the-gates`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 01-bread-beyond-the-gates
- **Order**: 7
- **HistoricalFrame**: 410 CE; geography=rome-ostia; core=sanctuary-supply-and-evacuation
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/01-bread-beyond-the-gates: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 8: The Court after the Last Emperor
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `staging/campaigns/church-of-rome/scenarios/08-administrative-transition-ravenna`, `docs/qa/church-of-rome/episodes/08-administrative-transition-ravenna`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 08-administrative-transition-ravenna
- **Order**: 8
- **HistoricalFrame**: 476 CE; geography=ravenna; core=administrative-transition
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/08-administrative-transition-ravenna: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S15 — Episodio 9: The Banquet's Long Shadow
- **Status**: pending
- **DependsOn**: [S14]
- **Files**: `staging/campaigns/church-of-rome/scenarios/09-civilian-record-preservation-ravenna`, `docs/qa/church-of-rome/episodes/09-civilian-record-preservation-ravenna`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 09-civilian-record-preservation-ravenna
- **Order**: 9
- **HistoricalFrame**: 493 CE; killing reported, not rewarded; geography=ravenna; core=civilian-record-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/09-civilian-record-preservation-ravenna: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S16 — Episodio 10: Two Powers in One Letter
- **Status**: pending
- **DependsOn**: [S15]
- **Files**: `staging/campaigns/church-of-rome/scenarios/10-correspondence-consignment-rome-ostia`, `docs/qa/church-of-rome/episodes/10-correspondence-consignment-rome-ostia`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-correspondence-consignment-rome-ostia
- **Order**: 10
- **HistoricalFrame**: 494 CE; geography=rome-ostia; core=correspondence-consignment
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/10-correspondence-consignment-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S17 — Episodio 11: Across the Old Division
- **Status**: pending
- **DependsOn**: [S16]
- **Files**: `staging/campaigns/church-of-rome/scenarios/11-reconciliation-document-logistics-constantinople`, `docs/qa/church-of-rome/episodes/11-reconciliation-document-logistics-constantinople`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 11-reconciliation-document-logistics-constantinople
- **Order**: 11
- **HistoricalFrame**: 519 CE; geography=constantinople; core=reconciliation-document-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/11-reconciliation-document-logistics-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S18 — Episodio 12: An Embassy without a Safe Return
- **Status**: pending
- **DependsOn**: [S17]
- **Files**: `staging/campaigns/church-of-rome/scenarios/12-returning-delegation-aid-ravenna`, `docs/qa/church-of-rome/episodes/12-returning-delegation-aid-ravenna`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 12-returning-delegation-aid-ravenna
- **Order**: 12
- **HistoricalFrame**: 525–526 CE; embassyConstantinople reported; geography=ravenna; core=returning-delegation-aid
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/12-returning-delegation-aid-ravenna: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S19 — Episodio 13: An Army through the Gates
- **Status**: pending
- **DependsOn**: [S18]
- **Files**: `staging/campaigns/church-of-rome/scenarios/13-district-supply-under-occupation-rome-ostia`, `docs/qa/church-of-rome/episodes/13-district-supply-under-occupation-rome-ostia`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 13-district-supply-under-occupation-rome-ostia
- **Order**: 13
- **HistoricalFrame**: 536 CE; geography=rome-ostia; core=district-supply-under-occupation
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/13-district-supply-under-occupation-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 14: The Year outside the Walls
- **Status**: pending
- **DependsOn**: [S19]
- **Files**: `staging/campaigns/church-of-rome/scenarios/14-finite-siege-and-urban-relief-rome-ostia`, `docs/qa/church-of-rome/episodes/14-finite-siege-and-urban-relief-rome-ostia`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 14-finite-siege-and-urban-relief-rome-ostia
- **Order**: 14
- **HistoricalFrame**: 537–538 CE; geography=rome-ostia; core=finite-siege-and-urban-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/14-finite-siege-and-urban-relief-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S21 — Episodio 15: The Empty Streets of Rome
- **Status**: pending
- **DependsOn**: [S20]
- **Files**: `staging/campaigns/church-of-rome/scenarios/15-archive-extraction-and-refuge-rome-ostia`, `docs/qa/church-of-rome/episodes/15-archive-extraction-and-refuge-rome-ostia`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 15-archive-extraction-and-refuge-rome-ostia
- **Order**: 15
- **HistoricalFrame**: 546 CE; geography=rome-ostia; core=archive-extraction-and-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/15-archive-extraction-and-refuge-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S22 — Episodio 16: Dispatches after the Gothic War
- **Status**: pending
- **DependsOn**: [S21]
- **Files**: `staging/campaigns/church-of-rome/scenarios/16-return-and-repair-rome-ostia`, `docs/qa/church-of-rome/episodes/16-return-and-repair-rome-ostia`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 16-return-and-repair-rome-ostia
- **Order**: 16
- **HistoricalFrame**: 552–553 CE; Taginae reported off-map; geography=rome-ostia; core=return-and-repair
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/16-return-and-repair-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S4 — Episodio 17: The Price of Peace
- **Status**: pending
- **DependsOn**: [S22]
- **Files**: `staging/campaigns/church-of-rome/scenarios/02-the-price-of-peace`, `docs/qa/church-of-rome/episodes/02-the-price-of-peace`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 02-the-price-of-peace
- **Order**: 17
- **HistoricalFrame**: 593–595 CE; Gregory590as prologue; geography=rome-ostia; core=finite-payment-and-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/02-the-price-of-peace: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S23 — Episodio 18: The Road beyond the Channel
- **Status**: pending
- **DependsOn**: [S4]
- **Files**: `staging/campaigns/church-of-rome/scenarios/18-hospitality-and-mission-supply-kent`, `docs/qa/church-of-rome/episodes/18-hospitality-and-mission-supply-kent`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 18-hospitality-and-mission-supply-kent
- **Order**: 18
- **HistoricalFrame**: 596–597 CE; Rome dispatch prologue; geography=kent; core=hospitality-and-mission-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/18-hospitality-and-mission-supply-kent: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S24 — Episodio 19: A Roof for Older Stones
- **Status**: pending
- **DependsOn**: [S23]
- **Files**: `staging/campaigns/church-of-rome/scenarios/19-finite-building-conversion-rome-ostia`, `docs/qa/church-of-rome/episodes/19-finite-building-conversion-rome-ostia`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 19-finite-building-conversion-rome-ostia
- **Order**: 19
- **HistoricalFrame**: 609 or613 CE; exact dedication debated; geography=rome-ostia; core=finite-building-conversion
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/19-finite-building-conversion-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 20: The Words at the Lateran
- **Status**: pending
- **DependsOn**: [S24]
- **Files**: `staging/campaigns/church-of-rome/scenarios/20-council-record-comparison-rome-ostia`, `docs/qa/church-of-rome/episodes/20-council-record-comparison-rome-ostia`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 20-council-record-comparison-rome-ostia
- **Order**: 20
- **HistoricalFrame**: October649 CE; geography=rome-ostia; core=council-record-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/20-council-record-comparison-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S26 — Episodio 21: Letters from the Cold Shore
- **Status**: pending
- **DependsOn**: [S25]
- **Files**: `staging/campaigns/church-of-rome/scenarios/21-exile-relief-and-copying-cherson`, `docs/qa/church-of-rome/episodes/21-exile-relief-and-copying-cherson`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 21-exile-relief-and-copying-cherson
- **Order**: 21
- **HistoricalFrame**: 655 CE; death655/656qualified; geography=cherson; core=exile-relief-and-copying
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/21-exile-relief-and-copying-cherson: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S27 — Episodio 22: Bronze Leaving the City
- **Status**: pending
- **DependsOn**: [S26]
- **Files**: `staging/campaigns/church-of-rome/scenarios/22-finite-material-records-rome-ostia`, `docs/qa/church-of-rome/episodes/22-finite-material-records-rome-ostia`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 22-finite-material-records-rome-ostia
- **Order**: 22
- **HistoricalFrame**: 663 CE; geography=rome-ostia; core=finite-material-records
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/22-finite-material-records-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S28 — Episodio 23: The Legates across the Water
- **Status**: pending
- **DependsOn**: [S27]
- **Files**: `staging/campaigns/church-of-rome/scenarios/23-delegation-and-document-escort-constantinople`, `docs/qa/church-of-rome/episodes/23-delegation-and-document-escort-constantinople`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-delegation-and-document-escort-constantinople
- **Order**: 23
- **HistoricalFrame**: 680–681 CE; geography=constantinople; core=delegation-and-document-escort
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/23-delegation-and-document-escort-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S29 — Episodio 24: Canons at the Roman Door
- **Status**: pending
- **DependsOn**: [S28]
- **Files**: `staging/campaigns/church-of-rome/scenarios/24-disputed-document-reception-rome-ostia`, `docs/qa/church-of-rome/episodes/24-disputed-document-reception-rome-ostia`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 24-disputed-document-reception-rome-ostia
- **Order**: 24
- **HistoricalFrame**: 692 CE; geography=rome-ostia; core=disputed-document-reception
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/24-disputed-document-reception-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S30 — Episodio 25: Images before the Synod
- **Status**: pending
- **DependsOn**: [S29]
- **Files**: `staging/campaigns/church-of-rome/scenarios/25-artisan-and-council-logistics-rome-ostia`, `docs/qa/church-of-rome/episodes/25-artisan-and-council-logistics-rome-ostia`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 25-artisan-and-council-logistics-rome-ostia
- **Order**: 25
- **HistoricalFrame**: 731 CE; geography=rome-ostia; core=artisan-and-council-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/25-artisan-and-council-logistics-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S31 — Episodio 26: Beyond the Alpine Promise
- **Status**: pending
- **DependsOn**: [S30]
- **Files**: `staging/campaigns/church-of-rome/scenarios/26-delegate-and-oath-logistics-saint-denis`, `docs/qa/church-of-rome/episodes/26-delegate-and-oath-logistics-saint-denis`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 26-delegate-and-oath-logistics-saint-denis
- **Order**: 26
- **HistoricalFrame**: 754 CE; Saint-Denis local focus; geography=saint-denis; core=delegate-and-oath-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/26-delegate-and-oath-logistics-saint-denis: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 27: The Roads to Pavia
- **Status**: pending
- **DependsOn**: [S31]
- **Files**: `staging/campaigns/church-of-rome/scenarios/03-roads-to-pavia`, `docs/qa/church-of-rome/episodes/03-roads-to-pavia`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 03-roads-to-pavia
- **Order**: 27
- **HistoricalFrame**: 754–756 CE; geography=pavia; core=finite-campaign-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/03-roads-to-pavia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S32 — Episodio 28: At the Lombard Gate
- **Status**: pending
- **DependsOn**: [S5]
- **Files**: `staging/campaigns/church-of-rome/scenarios/28-finite-siege-and-civilian-withdrawal-pavia`, `docs/qa/church-of-rome/episodes/28-finite-siege-and-civilian-withdrawal-pavia`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 28-finite-siege-and-civilian-withdrawal-pavia
- **Order**: 28
- **HistoricalFrame**: 773–774 CE; earlier768context only; geography=pavia; core=finite-siege-and-civilian-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/28-finite-siege-and-civilian-withdrawal-pavia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S33 — Episodio 29: Roman Letters beside the Lake
- **Status**: pending
- **DependsOn**: [S32]
- **Files**: `staging/campaigns/church-of-rome/scenarios/29-delegate-logistics-and-copying-nicaea`, `docs/qa/church-of-rome/episodes/29-delegate-logistics-and-copying-nicaea`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 29-delegate-logistics-and-copying-nicaea
- **Order**: 29
- **HistoricalFrame**: 787 CE; geography=nicaea; core=delegate-logistics-and-copying
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/29-delegate-logistics-and-copying-nicaea: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S34 — Episodio 30: Keys Sent down the Road
- **Status**: pending
- **DependsOn**: [S33]
- **Files**: `staging/campaigns/church-of-rome/scenarios/30-symbolic-consignment-and-couriers-rome-ostia`, `docs/qa/church-of-rome/episodes/30-symbolic-consignment-and-couriers-rome-ostia`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 30-symbolic-consignment-and-couriers-rome-ostia
- **Order**: 30
- **HistoricalFrame**: 795 CE; geography=rome-ostia; core=symbolic-consignment-and-couriers
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/30-symbolic-consignment-and-couriers-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S35 — Episodio 31: A Refuge at the Northern Court
- **Status**: pending
- **DependsOn**: [S34]
- **Files**: `staging/campaigns/church-of-rome/scenarios/31-refuge-and-petition-escort-paderborn`, `docs/qa/church-of-rome/episodes/31-refuge-and-petition-escort-paderborn`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 31-refuge-and-petition-escort-paderborn
- **Order**: 31
- **HistoricalFrame**: 799 CE; geography=paderborn; core=refuge-and-petition-escort
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/31-refuge-and-petition-escort-paderborn: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S6 — Episodio 32: A Crown at Dawn
- **Status**: pending
- **DependsOn**: [S35]
- **Files**: `staging/campaigns/church-of-rome/scenarios/04-a-crown-at-dawn`, `docs/qa/church-of-rome/episodes/04-a-crown-at-dawn`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 04-a-crown-at-dawn
- **Order**: 32
- **HistoricalFrame**: 25 December800 CE; geography=rome-ostia; core=ceremony-supply-and-final-perspective
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/04-a-crown-at-dawn: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S7 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S6]
- **Files**: `staging/campaigns/church-of-rome`, `campaigns/church-of-rome`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/church-of-rome/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 32 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 32 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates previos reales; sin atribuir a MiniMax el cierre de decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
