---
id: f00009
title: "Autoria designada: The Shattered Oath"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: 9386a406-9f49-4140-b53c-c7e034c50896
last-correlation-id: 9386a406-9f49-4140-b53c-c7e034c50896
last-transition-from: ready
last-transition-at: 2026-10-12T14:24:45.866Z
---

# f00009 — Autoria designada: The Shattered Oath

## goal

MiniMax M3.1 materializa `first-fitna` / CDF-I01 como odisea independiente de 28 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. Esta propuesta permanece bloqueada: una selección de episodios no es un contrato aprobado.

## why

La ampliación del propietario reemplaza la extensión de la base de 39 misiones. Se conserva cada ID de campaña, progreso, escenario y slice existente; el orden de episodio es independiente del número S. Los nuevos slices identifican cada trabajo adicional, sin encargar historia, geografía, diseño o nivelación a MiniMax.

## non-goals

- No diseñar historia, mapas, narradores, objetivos, arquitectura o balance por iniciativa del agente de contenido.
- No representar la falta de capacidad con un temporizador, texto, refuerzo infinito o stock duplicado.
- No confundir selección, dossier, exportación o test estático con GAME VERIFIED; sin publicación ni generación pagada masiva.

## prerequisites

`d00002` completo y revisado para esta odisea; `i00003` con las capacidades usadas implementadas; `f00001` y `f00002` pilotos acreditados; `s00001` con evidencia de motor. Recuperar dependencias y estados vivos de DelendAI. No cambiar blocked por tener este documento ni por contar carpetas.

## fuentes de trabajo y actos

Fuente editorial: `docs/design/odysseys/first-fitna.json`. Índice: `docs/wiki/first-fitna/14-odyssey-arc.md`. Expediente de cada misión: `docs/wiki/first-fitna/episodes/<scenarioId>/15-odyssey-dossier.md`, disponible solo cuando se haya redactado. Los documentos anteriores de la base son antecedentes; no autorizan ejecutar un antiguo final a mitad del arco ampliado.

| Acto | Título fuente | Episodios en orden | Slices asignados |
|---|---|---|---|
| act-1 | Dispatches Before the Storm | 1, 2, 3, 4, 5 | S3, S9, S10, S11, S12 |
| act-2 | The City Between the Camps | 6, 7, 8, 9, 10, 11 | S13, S14, S4, S15, S16, S17 |
| act-3 | Water and Broken Words | 12, 13, 14, 15, 16 | S18, S5, S19, S20, S21 |
| act-4 | The Price of Arbitration | 17, 18, 19, 20, 21, 22, 23 | S22, S23, S24, S6, S25, S26, S27 |
| act-5 | The Oath That Could Not Hold | 24, 25, 26, 27, 28 | S28, S29, S30, S31, S7 |

## slices

- global_gate: e2e

### S1 — Comprobar los expedientes aprobados sin rediseñarlos
- **Status**: pending
- **Files**: `docs/qa/first-fitna/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Verificar los 28 expedientes completos de first-fitna, cinco actos, pasajes consultados y revisión independiente del arquitecto. Si falta un objetivo, mapa, pantalla o nivelación, informar la brecha; no decidirlo MiniMax."
  - "Contrastar IDs estables, sourceLocale=en, EN/es-ES completos, voz factual común antes de persona situada y orden de campaña no bloqueante; conservar estados pendientes de otros idiomas y medios."

### S2 — Metadatos, pantallas de campaña y medios en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/first-fitna/campaign.json`, `staging/campaigns/first-fitna/native`, `staging/campaigns/first-fitna/assets`
- **Gate**: e2e
- acceptance:
  - "Materializar la arquitectura editorial aprobada: persona propia, recaps y aviso de predecesora recomendado sin bloqueo; recordar elecciones acumulativas sin borrar otras claves ni autoiniciar otra campaña."
  - "EN/es-ES completos con claves semánticas, captions y manifiestos con hash/licencia; solo medios aprobados, sin fotos restauradas presentadas como escena antigua. staging:check --partial sin promover contenido parcial."

### S3 — Episodio 1: News from Medina
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-fitna/scenarios/01-news-from-medina`, `docs/qa/first-fitna/episodes/01-news-from-medina`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-news-from-medina
- **Order**: 1
- **HistoricalFrame**: mid656 CE; geography=medina; core=delegation-reception-and-household-aid
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/01-news-from-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S9 — Episodio 2: After the Sealed Door
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `staging/campaigns/first-fitna/scenarios/02-civilian-refuge-and-record-preservation-medina`, `docs/qa/first-fitna/episodes/02-civilian-refuge-and-record-preservation-medina`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-civilian-refuge-and-record-preservation-medina
- **Order**: 2
- **HistoricalFrame**: 656 CE; murder is reported, not playable; geography=medina; core=civilian-refuge-and-record-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/02-civilian-refuge-and-record-preservation-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 3: A Seal Accepted in Uncertainty
- **Status**: pending
- **DependsOn**: [S9]
- **Files**: `staging/campaigns/first-fitna/scenarios/03-administrative-transition-medina`, `docs/qa/first-fitna/episodes/03-administrative-transition-medina`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-administrative-transition-medina
- **Order**: 3
- **HistoricalFrame**: 656 CE; motives attributed; geography=medina; core=administrative-transition
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/03-administrative-transition-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S11 — Episodio 4: The Message on the Pilgrim Road
- **Status**: pending
- **DependsOn**: [S10]
- **Files**: `staging/campaigns/first-fitna/scenarios/04-disputed-correspondence-mecca`, `docs/qa/first-fitna/episodes/04-disputed-correspondence-mecca`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 04-disputed-correspondence-mecca
- **Order**: 4
- **HistoricalFrame**: 656 CE; geography=mecca; core=disputed-correspondence
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/04-disputed-correspondence-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S12 — Episodio 5: Two Names in the Dispatch
- **Status**: pending
- **DependsOn**: [S11]
- **Files**: `staging/campaigns/first-fitna/scenarios/05-rival-petition-and-witness-records-medina`, `docs/qa/first-fitna/episodes/05-rival-petition-and-witness-records-medina`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 05-rival-petition-and-witness-records-medina
- **Order**: 5
- **HistoricalFrame**: 656 CE; geography=medina; core=rival-petition-and-witness-records
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/05-rival-petition-and-witness-records-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S13 — Episodio 6: Toward the River City
- **Status**: pending
- **DependsOn**: [S12]
- **Files**: `staging/campaigns/first-fitna/scenarios/06-arriving-delegation-and-supply-basra`, `docs/qa/first-fitna/episodes/06-arriving-delegation-and-supply-basra`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 06-arriving-delegation-and-supply-basra
- **Order**: 6
- **HistoricalFrame**: 656 CE; travelArabiaoff-map; geography=basra; core=arriving-delegation-and-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/06-arriving-delegation-and-supply-basra: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 7: The Streets between the Camps
- **Status**: pending
- **DependsOn**: [S13]
- **Files**: `staging/campaigns/first-fitna/scenarios/07-civilian-extraction-under-unrest-basra`, `docs/qa/first-fitna/episodes/07-civilian-extraction-under-unrest-basra`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 07-civilian-extraction-under-unrest-basra
- **Order**: 7
- **HistoricalFrame**: 656 CE; geography=basra; core=civilian-extraction-under-unrest
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/07-civilian-extraction-under-unrest-basra: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S4 — Episodio 8: Between the Camps
- **Status**: pending
- **DependsOn**: [S14]
- **Files**: `staging/campaigns/first-fitna/scenarios/02-between-the-camps`, `docs/qa/first-fitna/episodes/02-between-the-camps`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 02-between-the-camps
- **Order**: 8
- **HistoricalFrame**: 656 CE; geography=basra; core=finite-field-battle-and-care
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/02-between-the-camps: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S15 — Episodio 9: Accounts after the Battle
- **Status**: pending
- **DependsOn**: [S4]
- **Files**: `staging/campaigns/first-fitna/scenarios/09-bounded-distribution-and-receipts-basra`, `docs/qa/first-fitna/episodes/09-bounded-distribution-and-receipts-basra`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 09-bounded-distribution-and-receipts-basra
- **Order**: 9
- **HistoricalFrame**: 656 CE; distribution accounts attributed; geography=basra; core=bounded-distribution-and-receipts
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/09-bounded-distribution-and-receipts-basra: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S16 — Episodio 10: The Quarter on the Kufa Road
- **Status**: pending
- **DependsOn**: [S15]
- **Files**: `staging/campaigns/first-fitna/scenarios/10-camp-and-household-reception-kufa`, `docs/qa/first-fitna/episodes/10-camp-and-household-reception-kufa`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-camp-and-household-reception-kufa
- **Order**: 10
- **HistoricalFrame**: 656/657 CE; geography=kufa; core=camp-and-household-reception
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/10-camp-and-household-reception-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S17 — Episodio 11: Words across a Divided Road
- **Status**: pending
- **DependsOn**: [S16]
- **Files**: `staging/campaigns/first-fitna/scenarios/11-two-way-correspondence-kufa`, `docs/qa/first-fitna/episodes/11-two-way-correspondence-kufa`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 11-two-way-correspondence-kufa
- **Order**: 11
- **HistoricalFrame**: 656–657 CE; geography=kufa; core=two-way-correspondence
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/11-two-way-correspondence-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S18 — Episodio 12: A Reply from Damascus
- **Status**: pending
- **DependsOn**: [S17]
- **Files**: `staging/campaigns/first-fitna/scenarios/12-rival-claims-and-dispatch-comparison-damascus`, `docs/qa/first-fitna/episodes/12-rival-claims-and-dispatch-comparison-damascus`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 12-rival-claims-and-dispatch-comparison-damascus
- **Order**: 12
- **HistoricalFrame**: 656–657 CE; geography=damascus; core=rival-claims-and-dispatch-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/12-rival-claims-and-dispatch-comparison-damascus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 13: Water and Words
- **Status**: pending
- **DependsOn**: [S18]
- **Files**: `staging/campaigns/first-fitna/scenarios/03-water-and-words`, `docs/qa/first-fitna/episodes/03-water-and-words`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 03-water-and-words
- **Order**: 13
- **HistoricalFrame**: 657 CE; fiercefighting191integrated; geography=siffin; core=finite-river-battle-and-care
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/03-water-and-words: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S19 — Episodio 14: When the Fighting Was Stopped
- **Status**: pending
- **DependsOn**: [S5]
- **Files**: `staging/campaigns/first-fitna/scenarios/14-ceasefire-withdrawal-and-care-siffin`, `docs/qa/first-fitna/episodes/14-ceasefire-withdrawal-and-care-siffin`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 14-ceasefire-withdrawal-and-care-siffin
- **Order**: 14
- **HistoricalFrame**: 657 CE; Qur'an-folioaccount192attributed; geography=siffin; core=ceasefire-withdrawal-and-care
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/14-ceasefire-withdrawal-and-care-siffin: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 15: Terms beside the River
- **Status**: pending
- **DependsOn**: [S19]
- **Files**: `staging/campaigns/first-fitna/scenarios/15-paired-protocol-delivery-siffin`, `docs/qa/first-fitna/episodes/15-paired-protocol-delivery-siffin`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 15-paired-protocol-delivery-siffin
- **Order**: 15
- **HistoricalFrame**: 657 CE; geography=siffin; core=paired-protocol-delivery
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/15-paired-protocol-delivery-siffin: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S21 — Episodio 16: The Names Chosen for Arbitration
- **Status**: pending
- **DependsOn**: [S20]
- **Files**: `staging/campaigns/first-fitna/scenarios/16-witness-and-record-comparison-kufa`, `docs/qa/first-fitna/episodes/16-witness-and-record-comparison-kufa`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 16-witness-and-record-comparison-kufa
- **Order**: 16
- **HistoricalFrame**: 657/658 CE; geography=kufa; core=witness-and-record-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/16-witness-and-record-comparison-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S22 — Episodio 17: The Road through Harura
- **Status**: pending
- **DependsOn**: [S21]
- **Files**: `staging/campaigns/first-fitna/scenarios/17-voluntary-household-relocation-harura`, `docs/qa/first-fitna/episodes/17-voluntary-household-relocation-harura`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 17-voluntary-household-relocation-harura
- **Order**: 17
- **HistoricalFrame**: 657/658 CE; geography=harura; core=voluntary-household-relocation
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/17-voluntary-household-relocation-harura: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S23 — Episodio 18: Papers at Dumat al-Jandal
- **Status**: pending
- **DependsOn**: [S22]
- **Files**: `staging/campaigns/first-fitna/scenarios/18-separate-delegation-logistics-dumat-al-jandal`, `docs/qa/first-fitna/episodes/18-separate-delegation-logistics-dumat-al-jandal`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 18-separate-delegation-logistics-dumat-al-jandal
- **Order**: 18
- **HistoricalFrame**: February658 approximate; Ramadan37AHaccordingPoonawala; geography=dumat-al-jandal; core=separate-delegation-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/18-separate-delegation-logistics-dumat-al-jandal: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S24 — Episodio 19: The Reply That Would Not Settle
- **Status**: pending
- **DependsOn**: [S23]
- **Files**: `staging/campaigns/first-fitna/scenarios/19-disputed-correspondence-and-provision-kufa`, `docs/qa/first-fitna/episodes/19-disputed-correspondence-and-provision-kufa`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 19-disputed-correspondence-and-provision-kufa
- **Order**: 19
- **HistoricalFrame**: 658 CE; geography=kufa; core=disputed-correspondence-and-provision
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/19-disputed-correspondence-and-provision-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S6 — Episodio 20: The Canal Road
- **Status**: pending
- **DependsOn**: [S24]
- **Files**: `staging/campaigns/first-fitna/scenarios/04-the-canal-road`, `docs/qa/first-fitna/episodes/04-the-canal-road`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 04-the-canal-road
- **Order**: 20
- **HistoricalFrame**: 658 CE conventional; geography=nahrawan; core=finite-withdrawal-and-civilian-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/04-the-canal-road: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 21: The Egyptian Dispatch
- **Status**: pending
- **DependsOn**: [S6]
- **Files**: `staging/campaigns/first-fitna/scenarios/21-civilian-record-preservation-fustat`, `docs/qa/first-fitna/episodes/21-civilian-record-preservation-fustat`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 21-civilian-record-preservation-fustat
- **Order**: 21
- **HistoricalFrame**: 658 CE; Egyptloss not660; correctionrequiresexactpassage; geography=fustat; core=civilian-record-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/21-civilian-record-preservation-fustat: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S26 — Episodio 22: A Seat Empty at Adhruh
- **Status**: pending
- **DependsOn**: [S25]
- **Files**: `staging/campaigns/first-fitna/scenarios/22-delegate-reception-and-source-comparison-adhruh`, `docs/qa/first-fitna/episodes/22-delegate-reception-and-source-comparison-adhruh`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 22-delegate-reception-and-source-comparison-adhruh
- **Order**: 22
- **HistoricalFrame**: January659 approximate; Shaban38AHaccordingPoonawala; geography=adhruh; core=delegate-reception-and-source-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/22-delegate-reception-and-source-comparison-adhruh: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S27 — Episodio 23: The Farms beyond the Patrols
- **Status**: pending
- **DependsOn**: [S26]
- **Files**: `staging/campaigns/first-fitna/scenarios/23-bounded-rural-relief-kufa`, `docs/qa/first-fitna/episodes/23-bounded-rural-relief-kufa`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-bounded-rural-relief-kufa
- **Order**: 23
- **HistoricalFrame**: 659–660 CE; onefictionallocalraid, remoteincursionsreported; geography=kufa; core=bounded-rural-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/23-bounded-rural-relief-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S28 — Episodio 24: News from the Hijaz Roads
- **Status**: pending
- **DependsOn**: [S27]
- **Files**: `staging/campaigns/first-fitna/scenarios/24-civilian-refuge-and-dispatch-medina`, `docs/qa/first-fitna/episodes/24-civilian-refuge-and-dispatch-medina`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 24-civilian-refuge-and-dispatch-medina
- **Order**: 24
- **HistoricalFrame**: 660 CE; BusrraidsseparatefromEgypt658; geography=medina; core=civilian-refuge-and-dispatch
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/24-civilian-refuge-and-dispatch-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S29 — Episodio 25: The Night of the Last Report
- **Status**: pending
- **DependsOn**: [S28]
- **Files**: `staging/campaigns/first-fitna/scenarios/25-care-and-record-preservation-kufa`, `docs/qa/first-fitna/episodes/25-care-and-record-preservation-kufa`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 25-care-and-record-preservation-kufa
- **Order**: 25
- **HistoricalFrame**: January661 approximate; woundanddeath204consolidated; geography=kufa; core=care-and-record-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/25-care-and-record-preservation-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S30 — Episodio 26: The Seal after the Loss
- **Status**: pending
- **DependsOn**: [S29]
- **Files**: `staging/campaigns/first-fitna/scenarios/26-administrative-transition-and-household-supply-kufa`, `docs/qa/first-fitna/episodes/26-administrative-transition-and-household-supply-kufa`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 26-administrative-transition-and-household-supply-kufa
- **Order**: 26
- **HistoricalFrame**: 661 CE; geography=kufa; core=administrative-transition-and-household-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/26-administrative-transition-and-household-supply-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S31 — Episodio 27: A Letter with an Open Seal
- **Status**: pending
- **DependsOn**: [S30]
- **Files**: `staging/campaigns/first-fitna/scenarios/27-paired-protocol-and-bounded-negotiation-kufa`, `docs/qa/first-fitna/episodes/27-paired-protocol-and-bounded-negotiation-kufa`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 27-paired-protocol-and-bounded-negotiation-kufa
- **Order**: 27
- **HistoricalFrame**: 661 CE; geography=kufa; core=paired-protocol-and-bounded-negotiation
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/27-paired-protocol-and-bounded-negotiation-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S7 — Episodio 28: Two Archives beneath One Roof
- **Status**: pending
- **DependsOn**: [S31]
- **Files**: `staging/campaigns/first-fitna/scenarios/05-two-archives`, `docs/qa/first-fitna/episodes/05-two-archives`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 05-two-archives
- **Order**: 28
- **HistoricalFrame**: August661 approximate; RabiII41AH; geography=kufa; core=archive-and-final-perspective
- acceptance:
  - "Materializar únicamente el expediente aprobado first-fitna/05-two-archives: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S8 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S7]
- **Files**: `staging/campaigns/first-fitna`, `campaigns/first-fitna`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/first-fitna/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 28 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 28 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates previos reales; sin atribuir a MiniMax el cierre de decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
