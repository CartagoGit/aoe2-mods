---
id: f00008
title: "Autoria designada: Beneath the Desert Stars"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: d5f7532b-a8f2-43b2-ad02-4cddbade10b6
last-correlation-id: d5f7532b-a8f2-43b2-ad02-4cddbade10b6
last-transition-from: ready
last-transition-at: 2026-10-12T14:24:36.791Z
---

# f00008 — Autoria designada: Beneath the Desert Stars

## goal

MiniMax M3.1 materializa `first-caliphs` / CDF-I00 como odisea independiente de 30 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. La propuesta conserva su estado operativo hasta comprobar los gates. Una selección no es un contrato aprobado: sólo se materializa el subconjunto con paquete individual aprobado para fuentes; el resto de la odisea puede seguir en diseño.

## why

La ampliación del propietario reemplaza la extensión de la base de 39 misiones. Se conserva cada ID de campaña, progreso, escenario y slice existente; el orden de episodio es independiente del número S. Los nuevos slices identifican cada trabajo adicional, sin encargar historia, geografía, diseño o nivelación a MiniMax.

## non-goals

- No diseñar historia, mapas, narradores, objetivos, arquitectura o balance por iniciativa del agente de contenido.
- No representar la falta de capacidad con un temporizador, texto, refuerzo infinito o stock duplicado.
- No confundir selección, dossier, exportación o test estático con GAME VERIFIED; sin publicación ni generación pagada masiva.

## prerequisites

Autoría de fuentes en paralelo: `d00002/S1` integrado y revisado; arquitectura editorial de esta campaña y al menos un expediente individual aprobados para fuentes; esquema y referencia reutilizable disponibles para todas las operaciones de ese expediente individual; flujo de staging del piloto `f00001/S2` revisado. No se exige terminar los expedientes de los cinco actos ni de otras odiseas para empezar un episodio preparado. S1 mantiene una matriz por episodio; cada slice comprueba su propio paquete aprobado, sin delegar diseño a MiniMax.

Esta habilitación sirve sólo para fuentes en staging. La referencia tipada no certifica terreno, exportación o motor. Capacidades nativas de `i00003` y propuestas especializadas, pilotos `f00001`/`f00002`, plantillas reales y evidencia `s00001` se exigen antes de exportar/promover las operaciones que las usan, y siguen pendientes cuando no exista evidencia. No sustituir operaciones ni prometer una campaña jugable por cerrar un slice de fuentes. La promoción exige todos los expedientes y episodios de esta odisea completos/revisados, sus dependencias nativas y su QA real.

Recuperar estados vivos de DelendAI. Esta enmienda no cambia por sí sola blocked, no concede aprobación a ningún dossier y no permite saltar una dependencia real. El [paquete por entrega](../../../handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md) fija el traspaso y la devolución de hallazgos.

## fuentes de trabajo y actos

Fuente editorial: `docs/design/odysseys/first-caliphs.json`. Índice: `docs/wiki/first-caliphs/14-odyssey-arc.md`. Expediente de cada misión: `docs/wiki/first-caliphs/episodes/<scenarioId>/15-odyssey-dossier.md`, disponible solo cuando se haya redactado. Los documentos anteriores de la base son antecedentes; no autorizan ejecutar un antiguo final a mitad del arco ampliado.

| Acto | Título fuente | Episodios en orden | Slices asignados |
|---|---|---|---|
| act-1 | Voices of the Meccan Roads | 1, 2, 3, 4, 5, 6, 7 | S9, S10, S11, S12, S13, S14, S3 |
| act-2 | The Oasis and the Pact | 8, 9, 10, 11, 12, 13, 14 | S15, S16, S17, S18, S19, S20, S21 |
| act-3 | Roads Beyond Arabia | 15, 16, 17, 18, 19, 20, 21 | S22, S4, S23, S24, S5, S6, S25 |
| act-4 | Rivers and New Ledgers | 22, 23, 24, 25, 26 | S26, S27, S7, S28, S29 |
| act-5 | A Horizon Divided | 27, 28, 29, 30 | S30, S31, S32, S33 |

## slices

- global_gate: e2e

### S1 — Comprobar los expedientes aprobados sin rediseñarlos
- **Status**: pending
- **Files**: `docs/qa/first-caliphs/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Verificar el manifiesto completo de 30 episodios y cinco actos de first-caliphs, con estado por episodio. Para iniciar fuentes basta al menos un expediente individual completo y aprobado para ese alcance, sus pasajes consultados, decisiones de geografía/narrador/objetivos/nivelación cerradas y revisión independiente. Los demás quedan pendientes; MiniMax informa brechas, no las decide."
  - "Contrastar IDs estables, sourceLocale=en, EN/es-ES completos, voz factual común antes de persona situada y orden de campaña no bloqueante; conservar estados pendientes de otros idiomas y medios."

### S2 — Metadatos, pantallas de campaña y medios en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/first-caliphs/campaign.json`, `staging/campaigns/first-caliphs/native`, `staging/campaigns/first-caliphs/assets`
- **Gate**: e2e
- acceptance:
  - "Materializar la arquitectura editorial aprobada: persona propia, recaps y aviso de predecesora recomendado sin bloqueo; recordar elecciones acumulativas sin borrar otras claves ni autoiniciar otra campaña."
  - "EN/es-ES completos con claves semánticas, captions y manifiestos con hash/licencia; solo medios aprobados, sin fotos restauradas presentadas como escena antigua. staging:check --partial sin promover contenido parcial."

### S9 — Episodio 1: The Mountain in the Remembered Story
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/01-testimony-and-household-supply-mecca`, `docs/qa/first-caliphs/episodes/01-testimony-and-household-supply-mecca`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-testimony-and-household-supply-mecca
- **Order**: 1
- **HistoricalFrame**: c.610 CE; revelation belongs to attributed tradition; geography=mecca; core=testimony-and-household-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/01-testimony-and-household-supply-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 2: Voices among the Market Stalls
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/02-civilian-network-and-records-mecca`, `docs/qa/first-caliphs/episodes/02-civilian-network-and-records-mecca`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-civilian-network-and-records-mecca
- **Order**: 2
- **HistoricalFrame**: 610s CE; public preaching conventionallyc.613; geography=mecca; core=civilian-network-and-records
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/02-civilian-network-and-records-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S11 — Episodio 3: A Passage across the Red Sea
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/03-finite-emigration-consignments-mecca`, `docs/qa/first-caliphs/episodes/03-finite-emigration-consignments-mecca`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-finite-emigration-consignments-mecca
- **Order**: 3
- **HistoricalFrame**: c.615 CE; Aksum destination off-map and uncertain; geography=mecca; core=finite-emigration-consignments
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/03-finite-emigration-consignments-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S12 — Episodio 4: The Houses under the Boycott
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/04-bounded-household-provision-mecca`, `docs/qa/first-caliphs/episodes/04-bounded-household-provision-mecca`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 04-bounded-household-provision-mecca
- **Order**: 4
- **HistoricalFrame**: c.616–619 CE; transmitted chronology uncertain; geography=mecca; core=bounded-household-provision
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/04-bounded-household-provision-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S13 — Episodio 5: The First Promise at Aqaba
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/05-delegate-logistics-and-receipts-mina-aqaba`, `docs/qa/first-caliphs/episodes/05-delegate-logistics-and-receipts-mina-aqaba`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 05-delegate-logistics-and-receipts-mina-aqaba
- **Order**: 5
- **HistoricalFrame**: 621 CE traditional; firstpledge, notsecond; geography=mina-aqaba; core=delegate-logistics-and-receipts
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/05-delegate-logistics-and-receipts-mina-aqaba: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 6: A Road Promised to Strangers
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/06-bounded-reception-planning-mina-aqaba`, `docs/qa/first-caliphs/episodes/06-bounded-reception-planning-mina-aqaba`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 06-bounded-reception-planning-mina-aqaba
- **Order**: 6
- **HistoricalFrame**: 622 CE; conventionally secondpledge; geography=mina-aqaba; core=bounded-reception-planning
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/06-bounded-reception-planning-mina-aqaba: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S3 — Episodio 7: The Oasis Road
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/01-the-oasis-road`, `docs/qa/first-caliphs/episodes/01-the-oasis-road`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-the-oasis-road
- **Order**: 7
- **HistoricalFrame**: 622 CE; geography=medina; core=migration-and-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/01-the-oasis-road: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S15 — Episodio 8: Water before the First Battle
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/08-finite-battle-supply-and-withdrawal-badr`, `docs/qa/first-caliphs/episodes/08-finite-battle-supply-and-withdrawal-badr`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 08-finite-battle-supply-and-withdrawal-badr
- **Order**: 8
- **HistoricalFrame**: 624 CE; geography=badr; core=finite-battle-supply-and-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/08-finite-battle-supply-and-withdrawal-badr: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S16 — Episodio 9: Below the Broken Ridge
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/09-finite-withdrawal-and-care-uhud`, `docs/qa/first-caliphs/episodes/09-finite-withdrawal-and-care-uhud`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 09-finite-withdrawal-and-care-uhud
- **Order**: 9
- **HistoricalFrame**: 625 CE; geography=uhud; core=finite-withdrawal-and-care
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/09-finite-withdrawal-and-care-uhud: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S17 — Episodio 10: The Ditch before the Oasis
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/10-finite-defence-and-trench-supply-medina`, `docs/qa/first-caliphs/episodes/10-finite-defence-and-trench-supply-medina`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-finite-defence-and-trench-supply-medina
- **Order**: 10
- **HistoricalFrame**: 627 CE conventional; geography=medina; core=finite-defence-and-trench-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/10-finite-defence-and-trench-supply-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S18 — Episodio 11: A Truce at the Road's End
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/11-bounded-negotiation-and-supply-hudaybiyya`, `docs/qa/first-caliphs/episodes/11-bounded-negotiation-and-supply-hudaybiyya`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 11-bounded-negotiation-and-supply-hudaybiyya
- **Order**: 11
- **HistoricalFrame**: March628 CE;6AH; geography=hudaybiyya; core=bounded-negotiation-and-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/11-bounded-negotiation-and-supply-hudaybiyya: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S19 — Episodio 12: The Forts among the Palms
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/12-finite-siege-and-civilian-extraction-khaybar`, `docs/qa/first-caliphs/episodes/12-finite-siege-and-civilian-extraction-khaybar`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 12-finite-siege-and-civilian-extraction-khaybar
- **Order**: 12
- **HistoricalFrame**: 628 CE conventional; geography=khaybar; core=finite-siege-and-civilian-extraction
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/12-finite-siege-and-civilian-extraction-khaybar: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 13: The Open Road to Mecca
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/13-civilian-provision-under-entry-mecca`, `docs/qa/first-caliphs/episodes/13-civilian-provision-under-entry-mecca`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 13-civilian-provision-under-entry-mecca
- **Order**: 13
- **HistoricalFrame**: 630 CE; Hunayn andTaif reported inaftermath; geography=mecca; core=civilian-provision-under-entry
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/13-civilian-provision-under-entry-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S21 — Episodio 14: A Community without Its Messenger
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/14-witness-and-transition-records-medina`, `docs/qa/first-caliphs/episodes/14-witness-and-transition-records-medina`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 14-witness-and-transition-records-medina
- **Order**: 14
- **HistoricalFrame**: 632 CE; geography=medina; core=witness-and-transition-records
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/14-witness-and-transition-records-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S22 — Episodio 15: Dispatches from a Divided Peninsula
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/15-disputed-tax-and-provincial-records-medina`, `docs/qa/first-caliphs/episodes/15-disputed-tax-and-provincial-records-medina`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 15-disputed-tax-and-provincial-records-medina
- **Order**: 15
- **HistoricalFrame**: 632–634 CE; campaigns reported off-map; geography=medina; core=disputed-tax-and-provincial-records
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/15-disputed-tax-and-provincial-records-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S4 — Episodio 16: The Roads of Yamama
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/02-the-roads-of-yamama`, `docs/qa/first-caliphs/episodes/02-the-roads-of-yamama`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 02-the-roads-of-yamama
- **Order**: 16
- **HistoricalFrame**: 632–633 CE probable; geography=yamama; core=finite-field-supply-and-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/02-the-roads-of-yamama: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S23 — Episodio 17: The Bridge That Could Not Hold
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/17-finite-river-withdrawal-kufa-euphrates`, `docs/qa/first-caliphs/episodes/17-finite-river-withdrawal-kufa-euphrates`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 17-finite-river-withdrawal-kufa-euphrates
- **Order**: 17
- **HistoricalFrame**: October634 CE approximate; geography=kufa-euphrates; core=finite-river-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/17-finite-river-withdrawal-kufa-euphrates: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S24 — Episodio 18: The Gates of Damascus
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/18-surrender-and-civilian-records-damascus`, `docs/qa/first-caliphs/episodes/18-surrender-and-civilian-records-damascus`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 18-surrender-and-civilian-records-damascus
- **Order**: 18
- **HistoricalFrame**: 635 CE conventional; terms traditions compared; geography=damascus; core=surrender-and-civilian-records
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/18-surrender-and-civilian-records-damascus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 19: The Edge of the River
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/03-the-edge-of-the-river`, `docs/qa/first-caliphs/episodes/03-the-edge-of-the-river`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 03-the-edge-of-the-river
- **Order**: 19
- **HistoricalFrame**: 636 CE; geography=yarmuk; core=ravine-battle-and-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/03-the-edge-of-the-river: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S6 — Episodio 20: Fields of the Sawad
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/04-fields-of-the-sawad`, `docs/qa/first-caliphs/episodes/04-fields-of-the-sawad`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 04-fields-of-the-sawad
- **Order**: 20
- **HistoricalFrame**: 634/635–637/638 CE; conventional636/637; geography=qadisiyya; core=finite-marsh-battle-and-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/04-fields-of-the-sawad: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 21: The Court beyond the Tigris
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/21-finite-river-crossing-and-civilian-records-ctesiphon`, `docs/qa/first-caliphs/episodes/21-finite-river-crossing-and-civilian-records-ctesiphon`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 21-finite-river-crossing-and-civilian-records-ctesiphon
- **Order**: 21
- **HistoricalFrame**: 637 CE conventional; Nihavand later reported; geography=ctesiphon; core=finite-river-crossing-and-civilian-records
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/21-finite-river-crossing-and-civilian-records-ctesiphon: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S26 — Episodio 22: Terms beside the Old Walls
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/22-property-and-surrender-records-jerusalem`, `docs/qa/first-caliphs/episodes/22-property-and-surrender-records-jerusalem`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 22-property-and-surrender-records-jerusalem
- **Order**: 22
- **HistoricalFrame**: 637/638 CE; capitulation chronology qualified; geography=jerusalem; core=property-and-surrender-records
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/22-property-and-surrender-records-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S27 — Episodio 23: The Road after the Truce
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/23-peaceful-supply-and-record-reception-antioch`, `docs/qa/first-caliphs/episodes/23-peaceful-supply-and-record-reception-antioch`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-peaceful-supply-and-record-reception-antioch
- **Order**: 23
- **HistoricalFrame**: 638 CE; cited source reports no armed resistance; geography=antioch; core=peaceful-supply-and-record-reception
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/23-peaceful-supply-and-record-reception-antioch: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S7 — Episodio 24: A Camp beside the Nile
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/05-a-camp-beside-the-nile`, `docs/qa/first-caliphs/episodes/05-a-camp-beside-the-nile`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 05-a-camp-beside-the-nile
- **Order**: 24
- **HistoricalFrame**: 641–642 CE; precedingcampaign639–642; geography=fustat; core=camp-and-river-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/05-a-camp-beside-the-nile: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S28 — Episodio 25: Letters from the Alexandrian Harbour
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/25-bounded-harbour-withdrawal-and-receipts-alexandria`, `docs/qa/first-caliphs/episodes/25-bounded-harbour-withdrawal-and-receipts-alexandria`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 25-bounded-harbour-withdrawal-and-receipts-alexandria
- **Order**: 25
- **HistoricalFrame**: 641/642 CE traditional; geography=alexandria; core=bounded-harbour-withdrawal-and-receipts
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/25-bounded-harbour-withdrawal-and-receipts-alexandria: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S29 — Episodio 26: Another Seal in Medina
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/26-administrative-transition-and-care-medina`, `docs/qa/first-caliphs/episodes/26-administrative-transition-and-care-medina`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 26-administrative-transition-and-care-medina
- **Order**: 26
- **HistoricalFrame**: 644 CE; geography=medina; core=administrative-transition-and-care
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/26-administrative-transition-and-care-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S30 — Episodio 27: The Island beyond the Horizon
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/27-finite-coastal-expedition-and-supply-cyprus`, `docs/qa/first-caliphs/episodes/27-finite-coastal-expedition-and-supply-cyprus`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 27-finite-coastal-expedition-and-supply-cyprus
- **Order**: 27
- **HistoricalFrame**: 649 CE conventional; geography=cyprus; core=finite-coastal-expedition-and-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/27-finite-coastal-expedition-and-supply-cyprus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S31 — Episodio 28: The Last Dispatch from Marw
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/28-civilian-refuge-and-source-comparison-merv`, `docs/qa/first-caliphs/episodes/28-civilian-refuge-and-source-comparison-merv`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 28-civilian-refuge-and-source-comparison-merv
- **Order**: 28
- **HistoricalFrame**: 651/652 CE; death reported, not an assassination objective; geography=merv; core=civilian-refuge-and-source-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/28-civilian-refuge-and-source-comparison-merv: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S32 — Episodio 29: Masts off the Lycian Shore
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/29-finite-naval-withdrawal-and-care-finike`, `docs/qa/first-caliphs/episodes/29-finite-naval-withdrawal-and-care-finike`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 29-finite-naval-withdrawal-and-care-finike
- **Order**: 29
- **HistoricalFrame**: 654–655 CE; conversion variants; geography=finike; core=finite-naval-withdrawal-and-care
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/29-finite-naval-withdrawal-and-care-finike: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S33 — Episodio 30: The House behind the Dispatches
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/first-caliphs/scenarios/30-civilian-records-and-final-perspective-medina`, `docs/qa/first-caliphs/episodes/30-civilian-records-and-final-perspective-medina`, `staging/campaigns/first-caliphs/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 30-civilian-records-and-final-perspective-medina
- **Order**: 30
- **HistoricalFrame**: mid656 CE; geography=medina; core=civilian-records-and-final-perspective
- acceptance:
  - "Materializar únicamente el expediente aprobado first-caliphs/30-civilian-records-and-final-perspective-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S8 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S9, S10, S11, S12, S13, S14, S3, S15, S16, S17, S18, S19, S20, S21, S22, S4, S23, S24, S5, S6, S25, S26, S27, S7, S28, S29, S30, S31, S32, S33]
- **Files**: `staging/campaigns/first-caliphs`, `campaigns/first-caliphs`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/first-caliphs/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 30 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 30 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates por entrega reales: fuentes por episodio aprobado, promoción sólo con la odisea completa y sus pruebas nativas; sin atribuir a MiniMax decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
