---
id: f00003
title: "Autoria designada: The Eagle and the Cross"
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

# f00003 — Autoria designada: The Eagle and the Cross

## goal

MiniMax M3.1 materializa `imperial-church` / CDF-C01 como odisea independiente de 29 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. Esta propuesta permanece bloqueada: una selección de episodios no es un contrato aprobado.

## why

La ampliación del propietario reemplaza la extensión de la base de 39 misiones. Se conserva cada ID de campaña, progreso, escenario y slice existente; el orden de episodio es independiente del número S. Los nuevos slices identifican cada trabajo adicional, sin encargar historia, geografía, diseño o nivelación a MiniMax.

## non-goals

- No diseñar historia, mapas, narradores, objetivos, arquitectura o balance por iniciativa del agente de contenido.
- No representar la falta de capacidad con un temporizador, texto, refuerzo infinito o stock duplicado.
- No confundir selección, dossier, exportación o test estático con GAME VERIFIED; sin publicación ni generación pagada masiva.

## prerequisites

`d00002` completo y revisado para esta odisea; `i00003` con las capacidades usadas implementadas; `f00001` y `f00002` pilotos acreditados; `s00001` con evidencia de motor. Recuperar dependencias y estados vivos de DelendAI. No cambiar blocked por tener este documento ni por contar carpetas.

## fuentes de trabajo y actos

Fuente editorial: `docs/design/odysseys/imperial-church.json`. Índice: `docs/wiki/imperial-church/14-odyssey-arc.md`. Expediente de cada misión: `docs/wiki/imperial-church/episodes/<scenarioId>/15-odyssey-dossier.md`, disponible solo cuando se haya redactado. Los documentos anteriores de la base son antecedentes; no autorizan ejecutar un antiguo final a mitad del arco ampliado.

| Acto | Título fuente | Episodios en orden | Slices asignados |
|---|---|---|---|
| act-1 | Eagle Over the River | 1, 2, 3, 4, 5, 6 | S3, S7, S8, S9, S10, S11 |
| act-2 | A Creed in Many Tongues | 7, 8, 9, 10, 11, 12 | S12, S14, S15, S13, S16, S4 |
| act-3 | Stone and Succession | 13, 14, 15, 16, 17, 18, 19 | S17, S5, S18, S19, S20, S21, S22 |
| act-4 | Councils Without Concord | 20, 21, 22, 23, 24, 25 | S23, S24, S25, S26, S27, S28 |
| act-5 | The Weight of Orthodoxy | 26, 27, 28, 29 | S29, S30, S31, S32 |

## slices

- global_gate: e2e

### S1 — Comprobar los expedientes aprobados sin rediseñarlos
- **Status**: pending
- **Files**: `docs/qa/imperial-church/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Verificar los 29 expedientes completos de imperial-church, cinco actos, pasajes consultados y revisión independiente del arquitecto. Si falta un objetivo, mapa, pantalla o nivelación, informar la brecha; no decidirlo MiniMax."
  - "Contrastar IDs estables, sourceLocale=en, EN/es-ES completos, voz factual común antes de persona situada y orden de campaña no bloqueante; conservar estados pendientes de otros idiomas y medios."

### S2 — Metadatos, pantallas de campaña y medios en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/imperial-church/campaign.json`, `staging/campaigns/imperial-church/native`, `staging/campaigns/imperial-church/assets`
- **Gate**: e2e
- acceptance:
  - "Materializar la arquitectura editorial aprobada: persona propia, recaps y aviso de predecesora recomendado sin bloqueo; recordar elecciones acumulativas sin borrar otras claves ni autoiniciar otra campaña."
  - "EN/es-ES completos con claves semánticas, captions y manifiestos con hash/licencia; solo medios aprobados, sin fotos restauradas presentadas como escena antigua. staging:check --partial sin promover contenido parcial."

### S3 — Episodio 1: The River beneath the Eagle
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/imperial-church/scenarios/01-milvian-bridge`, `docs/qa/imperial-church/episodes/01-milvian-bridge`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-milvian-bridge
- **Order**: 1
- **HistoricalFrame**: 28 October 312 CE; geography=milvio; core=river-battle
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/01-milvian-bridge: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S7 — Episodio 2: Promises in the Winter Court
- **Status**: pending
- **DependsOn**: [S3]
- **Files**: `staging/campaigns/imperial-church/scenarios/02-bounded-negotiation-milan`, `docs/qa/imperial-church/episodes/02-bounded-negotiation-milan`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-bounded-negotiation-milan
- **Order**: 2
- **HistoricalFrame**: 313 CE; geography=milan; core=bounded-negotiation
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/02-bounded-negotiation-milan: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S8 — Episodio 3: The Doors Returned
- **Status**: pending
- **DependsOn**: [S7]
- **Files**: `staging/campaigns/imperial-church/scenarios/03-property-and-record-restoration-nicomedia`, `docs/qa/imperial-church/episodes/03-property-and-record-restoration-nicomedia`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-property-and-record-restoration-nicomedia
- **Order**: 3
- **HistoricalFrame**: 13 June 313 CE; geography=nicomedia; core=property-and-record-restoration
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/03-property-and-record-restoration-nicomedia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S9 — Episodio 4: The African Petition
- **Status**: pending
- **DependsOn**: [S8]
- **Files**: `staging/campaigns/imperial-church/scenarios/04-rival-delegation-reception-rome-ostia`, `docs/qa/imperial-church/episodes/04-rival-delegation-reception-rome-ostia`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 04-rival-delegation-reception-rome-ostia
- **Order**: 4
- **HistoricalFrame**: 313–314 CE; Roman hearing focus; geography=rome-ostia; core=rival-delegation-reception
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/04-rival-delegation-reception-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 5: The Road to Arles
- **Status**: pending
- **DependsOn**: [S9]
- **Files**: `staging/campaigns/imperial-church/scenarios/05-delegate-logistics-arles`, `docs/qa/imperial-church/episodes/05-delegate-logistics-arles`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 05-delegate-logistics-arles
- **Order**: 5
- **HistoricalFrame**: 314 CE; geography=arles; core=delegate-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/05-delegate-logistics-arles: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S11 — Episodio 6: The Field between Two Eagles
- **Status**: pending
- **DependsOn**: [S10]
- **Files**: `staging/campaigns/imperial-church/scenarios/06-finite-field-withdrawal-cibalae`, `docs/qa/imperial-church/episodes/06-finite-field-withdrawal-cibalae`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 06-finite-field-withdrawal-cibalae
- **Order**: 6
- **HistoricalFrame**: 314 or 316 CE; dating disputed; geography=cibalae; core=finite-field-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/06-finite-field-withdrawal-cibalae: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S12 — Episodio 7: A Day beneath the Law
- **Status**: pending
- **DependsOn**: [S11]
- **Files**: `staging/campaigns/imperial-church/scenarios/07-court-record-logistics-rome-ostia`, `docs/qa/imperial-church/episodes/07-court-record-logistics-rome-ostia`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 07-court-record-logistics-rome-ostia
- **Order**: 7
- **HistoricalFrame**: 321 CE; distinguish judicial rule from agricultural exception; geography=rome-ostia; core=court-record-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/07-court-record-logistics-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 8: The Maritsa Crossing
- **Status**: pending
- **DependsOn**: [S12]
- **Files**: `staging/campaigns/imperial-church/scenarios/09-crossing-and-supply-adrianople`, `docs/qa/imperial-church/episodes/09-crossing-and-supply-adrianople`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 09-crossing-and-supply-adrianople
- **Order**: 8
- **HistoricalFrame**: 3 July 324 CE, conventional; geography=adrianople; core=crossing-and-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/09-crossing-and-supply-adrianople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S15 — Episodio 9: Across the Bright Shore
- **Status**: pending
- **DependsOn**: [S14]
- **Files**: `staging/campaigns/imperial-church/scenarios/10-land-and-strait-logistics-chrysopolis`, `docs/qa/imperial-church/episodes/10-land-and-strait-logistics-chrysopolis`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-land-and-strait-logistics-chrysopolis
- **Order**: 9
- **HistoricalFrame**: 18 September 324 CE, conventional; geography=chrysopolis; core=land-and-strait-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/10-land-and-strait-logistics-chrysopolis: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S13 — Episodio 10: Words over Alexandria
- **Status**: pending
- **DependsOn**: [S15]
- **Files**: `staging/campaigns/imperial-church/scenarios/08-disputed-correspondence-alexandria`, `docs/qa/imperial-church/episodes/08-disputed-correspondence-alexandria`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 08-disputed-correspondence-alexandria
- **Order**: 10
- **HistoricalFrame**: 324–325 CE; geography=alexandria; core=disputed-correspondence
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/08-disputed-correspondence-alexandria: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S16 — Episodio 11: Before the Lakeside Council
- **Status**: pending
- **DependsOn**: [S13]
- **Files**: `staging/campaigns/imperial-church/scenarios/11-council-record-escort-antioch`, `docs/qa/imperial-church/episodes/11-council-record-escort-antioch`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 11-council-record-escort-antioch
- **Order**: 11
- **HistoricalFrame**: c.324–325 CE; exact date/order relative to imperial letter debated; geography=antioch; core=council-record-escort
- **ChronologyCaution**: S13→S16 es orden de autoría editorial; no prueba que el sínodo siguiera a la carta imperial. La carta transmitida niega comunión, no acredita destitución del cargo; refiere Ancira como lugar futuro, no Nicea.
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/11-council-record-escort-antioch: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S4 — Episodio 12: Many Voices beside the Lake
- **Status**: pending
- **DependsOn**: [S16]
- **Files**: `staging/campaigns/imperial-church/scenarios/02-nicaea`, `docs/qa/imperial-church/episodes/02-nicaea`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 02-nicaea
- **Order**: 12
- **HistoricalFrame**: 325 CE; geography=nicaea; core=delegate-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/02-nicaea: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S17 — Episodio 13: Stone above the Old City
- **Status**: pending
- **DependsOn**: [S4]
- **Files**: `staging/campaigns/imperial-church/scenarios/13-finite-works-logistics-jerusalem`, `docs/qa/imperial-church/episodes/13-finite-works-logistics-jerusalem`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 13-finite-works-logistics-jerusalem
- **Order**: 13
- **HistoricalFrame**: 326–330 CE; individual works dates qualified; geography=jerusalem; core=finite-works-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/13-finite-works-logistics-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 14: A City beneath a New Sky
- **Status**: pending
- **DependsOn**: [S17]
- **Files**: `staging/campaigns/imperial-church/scenarios/03-new-capital`, `docs/qa/imperial-church/episodes/03-new-capital`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 03-new-capital
- **Order**: 14
- **HistoricalFrame**: 11 May 330 CE; fictional works approach before dedication; geography=constantinople; core=urban-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/03-new-capital: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S18 — Episodio 15: A Letter beyond the Frontier
- **Status**: pending
- **DependsOn**: [S5]
- **Files**: `staging/campaigns/imperial-church/scenarios/15-long-distance-dispatch-nicomedia`, `docs/qa/imperial-church/episodes/15-long-distance-dispatch-nicomedia`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 15-long-distance-dispatch-nicomedia
- **Order**: 15
- **HistoricalFrame**: Undated letter within 324–337 CE; retrospective local interlude after 330; geography=nicomedia; core=long-distance-dispatch
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/15-long-distance-dispatch-nicomedia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S19 — Episodio 16: The Council on the Shore
- **Status**: pending
- **DependsOn**: [S18]
- **Files**: `staging/campaigns/imperial-church/scenarios/16-witness-record-comparison-tyre`, `docs/qa/imperial-church/episodes/16-witness-record-comparison-tyre`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 16-witness-record-comparison-tyre
- **Order**: 16
- **HistoricalFrame**: 335 CE; Tyre council focus; geography=tyre; core=witness-record-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/16-witness-record-comparison-tyre: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 17: The Empty Appointment
- **Status**: pending
- **DependsOn**: [S19]
- **Files**: `staging/campaigns/imperial-church/scenarios/17-rumour-and-source-investigation-constantinople`, `docs/qa/imperial-church/episodes/17-rumour-and-source-investigation-constantinople`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 17-rumour-and-source-investigation-constantinople
- **Order**: 17
- **HistoricalFrame**: 336 CE; geography=constantinople; core=rumour-and-source-investigation
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/17-rumour-and-source-investigation-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S21 — Episodio 18: The Court without Its Emperor
- **Status**: pending
- **DependsOn**: [S20]
- **Files**: `staging/campaigns/imperial-church/scenarios/18-administrative-transition-nicomedia`, `docs/qa/imperial-church/episodes/18-administrative-transition-nicomedia`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 18-administrative-transition-nicomedia
- **Order**: 18
- **HistoricalFrame**: 22 May 337 CE; geography=nicomedia; core=administrative-transition
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/18-administrative-transition-nicomedia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S22 — Episodio 19: Three Seals, One Inheritance
- **Status**: pending
- **DependsOn**: [S21]
- **Files**: `staging/campaigns/imperial-church/scenarios/19-competing-dispatches-constantinople`, `docs/qa/imperial-church/episodes/19-competing-dispatches-constantinople`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 19-competing-dispatches-constantinople
- **Order**: 19
- **HistoricalFrame**: 337 CE; eastern court focus, not a map of the whole empire; geography=constantinople; core=competing-dispatches
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/19-competing-dispatches-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S23 — Episodio 20: The Council That Divided
- **Status**: pending
- **DependsOn**: [S22]
- **Files**: `staging/campaigns/imperial-church/scenarios/20-separate-reception-logistics-sardica`, `docs/qa/imperial-church/episodes/20-separate-reception-logistics-sardica`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 20-separate-reception-logistics-sardica
- **Order**: 20
- **HistoricalFrame**: 343 CE; alternative342/344not excluded; geography=sardica; core=separate-reception-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/20-separate-reception-logistics-sardica: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S24 — Episodio 21: The Road Back to Alexandria
- **Status**: pending
- **DependsOn**: [S23]
- **Files**: `staging/campaigns/imperial-church/scenarios/21-returning-households-escort-alexandria`, `docs/qa/imperial-church/episodes/21-returning-households-escort-alexandria`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 21-returning-households-escort-alexandria
- **Order**: 21
- **HistoricalFrame**: 21 October 346 CE; geography=alexandria; core=returning-households-escort
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/21-returning-households-escort-alexandria: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 22: The Dispatch from Gaul
- **Status**: pending
- **DependsOn**: [S24]
- **Files**: `staging/campaigns/imperial-church/scenarios/22-civilian-record-preservation-milan`, `docs/qa/imperial-church/episodes/22-civilian-record-preservation-milan`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 22-civilian-record-preservation-milan
- **Order**: 22
- **HistoricalFrame**: 350 CE; reception of news, killing site not asserted; Constantius not yet sole emperor; geography=milan; core=civilian-record-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/22-civilian-record-preservation-milan: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S26 — Episodio 23: Seals at the Western Synod
- **Status**: pending
- **DependsOn**: [S25]
- **Files**: `staging/campaigns/imperial-church/scenarios/23-bounded-political-pressure-milan`, `docs/qa/imperial-church/episodes/23-bounded-political-pressure-milan`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-bounded-political-pressure-milan
- **Order**: 23
- **HistoricalFrame**: 355 CE; Milan hearing focus; geography=milan; core=bounded-political-pressure
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/23-bounded-political-pressure-milan: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S27 — Episodio 24: The Night of the Open Doors
- **Status**: pending
- **DependsOn**: [S26]
- **Files**: `staging/campaigns/imperial-church/scenarios/24-night-civilian-withdrawal-alexandria`, `docs/qa/imperial-church/episodes/24-night-civilian-withdrawal-alexandria`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 24-night-civilian-withdrawal-alexandria
- **Order**: 24
- **HistoricalFrame**: 356 CE; Alexandria local event, no omniscient private dialogue; geography=alexandria; core=night-civilian-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/24-night-civilian-withdrawal-alexandria: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S28 — Episodio 25: A Formula on the Adriatic Road
- **Status**: pending
- **DependsOn**: [S27]
- **Files**: `staging/campaigns/imperial-church/scenarios/25-delegate-and-draft-network-rimini`, `docs/qa/imperial-church/episodes/25-delegate-and-draft-network-rimini`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 25-delegate-and-draft-network-rimini
- **Order**: 25
- **HistoricalFrame**: 359 CE; Western council, Seleucia off-map comparison; geography=rimini; core=delegate-and-draft-network
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/25-delegate-and-draft-network-rimini: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S29 — Episodio 26: The Temples Open Again
- **Status**: pending
- **DependsOn**: [S28]
- **Files**: `staging/campaigns/imperial-church/scenarios/26-plural-civic-logistics-constantinople`, `docs/qa/imperial-church/episodes/26-plural-civic-logistics-constantinople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 26-plural-civic-logistics-constantinople
- **Order**: 26
- **HistoricalFrame**: 361 CE; geography=constantinople; core=plural-civic-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/26-plural-civic-logistics-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S30 — Episodio 27: The Return That Did Not Last
- **Status**: pending
- **DependsOn**: [S29]
- **Files**: `staging/campaigns/imperial-church/scenarios/27-return-and-departure-records-alexandria`, `docs/qa/imperial-church/episodes/27-return-and-departure-records-alexandria`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 27-return-and-departure-records-alexandria
- **Order**: 27
- **HistoricalFrame**: 362–363 CE; exile policies focus, Persian campaign reported off-map; geography=alexandria; core=return-and-departure-records
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/27-return-and-departure-records-alexandria: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S31 — Episodio 28: The Weight of an Imperial Word
- **Status**: pending
- **DependsOn**: [S30]
- **Files**: `staging/campaigns/imperial-church/scenarios/28-law-and-local-reception-thessalonica`, `docs/qa/imperial-church/episodes/28-law-and-local-reception-thessalonica`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 28-law-and-local-reception-thessalonica
- **Order**: 28
- **HistoricalFrame**: 27 February 380 CE; geography=thessalonica; core=law-and-local-reception
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/28-law-and-local-reception-thessalonica: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S32 — Episodio 29: Under the Same Eastern Sky
- **Status**: pending
- **DependsOn**: [S31]
- **Files**: `staging/campaigns/imperial-church/scenarios/29-council-and-final-perspective-constantinople`, `docs/qa/imperial-church/episodes/29-council-and-final-perspective-constantinople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 29-council-and-final-perspective-constantinople
- **Order**: 29
- **HistoricalFrame**: 381 CE; geography=constantinople; core=council-and-final-perspective
- acceptance:
  - "Materializar únicamente el expediente aprobado imperial-church/29-council-and-final-perspective-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Si expediente o capacidad no está aprobado, este slice no es ejecutable."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación real. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S6 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S32]
- **Files**: `staging/campaigns/imperial-church`, `campaigns/imperial-church`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/imperial-church/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 29 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 29 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates previos reales; sin atribuir a MiniMax el cierre de decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
