---
id: f00005
title: "Autoria designada: Keepers of the Unbroken Word"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: 0e3540ac-c57e-420f-921c-ad4c2635f091
last-correlation-id: 0e3540ac-c57e-420f-921c-ad4c2635f091
last-transition-from: ready
last-transition-at: 2026-10-12T14:24:10.781Z
---

# f00005 — Autoria designada: Keepers of the Unbroken Word

## goal

MiniMax M3.1 materializa `jewish-tradition` / CDF-C02 como odisea independiente de 30 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. La propuesta conserva su estado operativo hasta comprobar los gates. Una selección no es un contrato aprobado: sólo se materializa el subconjunto con paquete individual aprobado para fuentes; el resto de la odisea puede seguir en diseño.

## why

La ampliación del propietario reemplaza la extensión de la base de 39 misiones. Se conserva cada ID de campaña, progreso, escenario y slice existente; el orden de episodio es independiente del número S. Los nuevos slices identifican cada trabajo adicional, sin encargar historia, geografía, diseño o nivelación a MiniMax.

## non-goals

- No diseñar historia, mapas, narradores, objetivos, arquitectura o balance por iniciativa del agente de contenido.
- No representar la falta de capacidad con un temporizador, texto, refuerzo infinito o stock duplicado.
- No confundir selección, dossier, exportación o test estático con GAME VERIFIED; sin publicación ni generación pagada masiva.

## prerequisites

Autoría de fuentes en paralelo: `d00002/S1` integrado y revisado; arquitectura editorial de esta campaña y al menos un expediente individual aprobados para fuentes; esquema y referencia reutilizable de todas sus operaciones disponibles; flujo de staging del piloto `f00001/S2` revisado. No se exige terminar los expedientes de los cinco actos ni de otras odiseas para empezar un episodio preparado. S1 mantiene una matriz por episodio; cada slice comprueba su propio paquete aprobado, sin delegar diseño a MiniMax.

Esta habilitación sirve sólo para fuentes en staging. La referencia tipada no certifica terreno, exportación o motor. Capacidades nativas de `i00003` y propuestas especializadas, pilotos `f00001`/`f00002`, plantillas reales y evidencia `s00001` se exigen antes de exportar/promover las operaciones que las usan, y siguen pendientes cuando no exista evidencia. No sustituir operaciones ni prometer una campaña jugable por cerrar un slice de fuentes. La promoción exige todos los expedientes y episodios de esta odisea completos/revisados, sus dependencias nativas y su QA real.

Recuperar estados vivos de DelendAI. Esta enmienda no cambia por sí sola blocked, no concede aprobación a ningún dossier y no permite saltar una dependencia real. El [paquete por entrega](../../../handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md) fija el traspaso y la devolución de hallazgos.

## fuentes de trabajo y actos

Fuente editorial: `docs/design/odysseys/jewish-tradition.json`. Índice: `docs/wiki/jewish-tradition/14-odyssey-arc.md`. Expediente de cada misión: `docs/wiki/jewish-tradition/episodes/<scenarioId>/15-odyssey-dossier.md`, disponible solo cuando se haya redactado. Los documentos anteriores de la base son antecedentes; no autorizan ejecutar un antiguo final a mitad del arco ampliado.

| Acto | Título fuente | Episodios en orden | Slices asignados |
|---|---|---|---|
| act-1 | After the House Fell | 1, 2, 3, 4, 5 | S3, S8, S9, S10, S11 |
| act-2 | Names in the Wilderness | 6, 7, 8, 9, 10, 11, 12 | S12, S13, S14, S15, S16, S17, S18 |
| act-3 | Schools Beyond the River | 13, 14, 15, 16, 17 | S4, S19, S20, S5, S21 |
| act-4 | Stone, Law, and Memory | 18, 19, 20, 21, 22, 23, 24 | S22, S23, S24, S25, S26, S27, S28 |
| act-5 | The Word Without a Throne | 25, 26, 27, 28, 29, 30 | S29, S30, S31, S32, S33, S6 |

## slices

- global_gate: e2e

### S1 — Comprobar los expedientes aprobados sin rediseñarlos
- **Status**: pending
- **Files**: `docs/qa/jewish-tradition/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Verificar el manifiesto completo de 30 episodios y cinco actos de jewish-tradition, con estado por episodio. Para iniciar fuentes basta al menos un expediente individual completo y aprobado para ese alcance, sus pasajes consultados, decisiones de geografía/narrador/objetivos/nivelación cerradas y revisión independiente. Los demás quedan pendientes; MiniMax informa brechas, no las decide."
  - "Contrastar IDs estables, sourceLocale=en, EN/es-ES completos, voz factual común antes de persona situada y orden de campaña no bloqueante; conservar estados pendientes de otros idiomas y medios."

### S2 — Metadatos, pantallas de campaña y medios en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/jewish-tradition/campaign.json`, `staging/campaigns/jewish-tradition/native`, `staging/campaigns/jewish-tradition/assets`
- **Gate**: e2e
- acceptance:
  - "Materializar la arquitectura editorial aprobada: persona propia, recaps y aviso de predecesora recomendado sin bloqueo; recordar elecciones acumulativas sin borrar otras claves ni autoiniciar otra campaña."
  - "EN/es-ES completos con claves semánticas, captions y manifiestos con hash/licencia; solo medios aprobados, sin fotos restauradas presentadas como escena antigua. staging:check --partial sin promover contenido parcial."

### S3 — Episodio 1: Names beyond the Fallen House
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/01-a-city-of-names`, `docs/qa/jewish-tradition/episodes/01-a-city-of-names`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-a-city-of-names
- **Order**: 1
- **HistoricalFrame**: 70 CE; geography=jerusalem; core=civilian-evacuation
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/01-a-city-of-names: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S8 — Episodio 2: A School without Walls
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/02-refuge-and-school-supply-yavneh`, `docs/qa/jewish-tradition/episodes/02-refuge-and-school-supply-yavneh`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-refuge-and-school-supply-yavneh
- **Order**: 2
- **HistoricalFrame**: c.70–80 CE; geography=yavneh; core=refuge-and-school-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/02-refuge-and-school-supply-yavneh: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S9 — Episodio 3: The Questions We Carried
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/03-distributed-study-network-yavneh`, `docs/qa/jewish-tradition/episodes/03-distributed-study-network-yavneh`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-distributed-study-network-yavneh
- **Order**: 3
- **HistoricalFrame**: c.80–100 CE; geography=yavneh; core=distributed-study-network
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/03-distributed-study-network-yavneh: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 4: Words Still under Discussion
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/04-witness-comparison-yavneh`, `docs/qa/jewish-tradition/episodes/04-witness-comparison-yavneh`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 04-witness-comparison-yavneh
- **Order**: 4
- **HistoricalFrame**: c.90–100 CE; later rabbinic traditions; geography=yavneh; core=witness-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/04-witness-comparison-yavneh: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S11 — Episodio 5: The Weight of a Roman Receipt
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/05-fiscal-record-reconciliation-rome-ostia`, `docs/qa/jewish-tradition/episodes/05-fiscal-record-reconciliation-rome-ostia`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 05-fiscal-record-reconciliation-rome-ostia
- **Order**: 5
- **HistoricalFrame**: 96 CE; reform scope qualified; geography=rome-ostia; core=fiscal-record-reconciliation
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/05-fiscal-record-reconciliation-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S12 — Episodio 6: The Teacher in the Unfinished Line
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/06-teaching-record-escort-lod`, `docs/qa/jewish-tradition/episodes/06-teaching-record-escort-lod`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 06-teaching-record-escort-lod
- **Order**: 6
- **HistoricalFrame**: c.100–135 CE; Akiva traditionally diesc.135, not150–180; geography=lod; core=teaching-record-escort
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/06-teaching-record-escort-lod: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S13 — Episodio 7: Across the Cyrenaican Roads
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/07-civilian-refuge-cyrene`, `docs/qa/jewish-tradition/episodes/07-civilian-refuge-cyrene`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 07-civilian-refuge-cyrene
- **Order**: 7
- **HistoricalFrame**: 115–117 CE; local reconstruction; geography=cyrene; core=civilian-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/07-civilian-refuge-cyrene: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 8: The Harbour That Heard the War
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/08-harbour-supply-and-witnesses-alexandria`, `docs/qa/jewish-tradition/episodes/08-harbour-supply-and-witnesses-alexandria`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 08-harbour-supply-and-witnesses-alexandria
- **Order**: 8
- **HistoricalFrame**: 115–117 CE; Egyptian local reconstruction; geography=alexandria; core=harbour-supply-and-witnesses
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/08-harbour-supply-and-witnesses-alexandria: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S15 — Episodio 9: The City's Other Name
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/09-administrative-records-jerusalem`, `docs/qa/jewish-tradition/episodes/09-administrative-records-jerusalem`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 09-administrative-records-jerusalem
- **Order**: 9
- **HistoricalFrame**: c.130–132 CE; chronology of colonial refoundation disputed; geography=jerusalem; core=administrative-records
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/09-administrative-records-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S16 — Episodio 10: Silver beneath the Desert Sky
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/10-finite-mint-consignments-judean-hills`, `docs/qa/jewish-tradition/episodes/10-finite-mint-consignments-judean-hills`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-finite-mint-consignments-judean-hills
- **Order**: 10
- **HistoricalFrame**: 132–135 CE; geography=judean-hills; core=finite-mint-consignments
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/10-finite-mint-consignments-judean-hills: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S17 — Episodio 11: Letters at the Desert Edge
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/11-archive-extraction-judean-desert`, `docs/qa/jewish-tradition/episodes/11-archive-extraction-judean-desert`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 11-archive-extraction-judean-desert
- **Order**: 11
- **HistoricalFrame**: 132–135 CE; cave records, not an invented battle; geography=judean-desert; core=archive-extraction
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/11-archive-extraction-judean-desert: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S18 — Episodio 12: After the Last Stronghold
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/12-household-relocation-jerusalem`, `docs/qa/jewish-tradition/episodes/12-household-relocation-jerusalem`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 12-household-relocation-jerusalem
- **Order**: 12
- **HistoricalFrame**: 135 CE; administrative dates qualified; geography=jerusalem; core=household-relocation
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/12-household-relocation-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S4 — Episodio 13: The Hill and the School
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/02-the-hill-and-the-school`, `docs/qa/jewish-tradition/episodes/02-the-hill-and-the-school`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 02-the-hill-and-the-school
- **Order**: 13
- **HistoricalFrame**: c.190–220 CE; geography=galilee; core=distributed-copy-and-provision
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/02-the-hill-and-the-school: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S19 — Episodio 14: A New Name in the Register
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/14-citizenship-copy-and-receipts-galilee`, `docs/qa/jewish-tradition/episodes/14-citizenship-copy-and-receipts-galilee`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 14-citizenship-copy-and-receipts-galilee
- **Order**: 14
- **HistoricalFrame**: 212 CE; local circulation reconstruction; geography=galilee; core=citizenship-copy-and-receipts
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/14-citizenship-copy-and-receipts-galilee: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 15: Margins beside the Lake
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/15-study-and-supply-allocation-galilee`, `docs/qa/jewish-tradition/episodes/15-study-and-supply-allocation-galilee`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 15-study-and-supply-allocation-galilee
- **Order**: 15
- **HistoricalFrame**: c.220–250 CE; geography=galilee; core=study-and-supply-allocation
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/15-study-and-supply-allocation-galilee: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 16: The Painted River Quarter
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/03-the-river-quarter`, `docs/qa/jewish-tradition/episodes/03-the-river-quarter`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 03-the-river-quarter
- **Order**: 16
- **HistoricalFrame**: c.244 CE; geography=dura; core=artisan-and-river-trade
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/03-the-river-quarter: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S21 — Episodio 17: Questions beyond the Euphrates
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/17-cross-river-study-logistics-pumbedita`, `docs/qa/jewish-tradition/episodes/17-cross-river-study-logistics-pumbedita`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 17-cross-river-study-logistics-pumbedita
- **Order**: 17
- **HistoricalFrame**: c.250–300 CE; precise institutional chronology qualified; geography=pumbedita; core=cross-river-study-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/17-cross-river-study-logistics-pumbedita: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S22 — Episodio 18: The Zodiac on the Floor
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/18-finite-mosaic-works-hammath-tiberias`, `docs/qa/jewish-tradition/episodes/18-finite-mosaic-works-hammath-tiberias`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 18-finite-mosaic-works-hammath-tiberias
- **Order**: 18
- **HistoricalFrame**: 4th century CE; archaeological range, not an exact dedication; geography=hammath-tiberias; core=finite-mosaic-works
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/18-finite-mosaic-works-hammath-tiberias: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S23 — Episodio 19: The Roads after Diocaesarea
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/19-bounded-civilian-withdrawal-sepphoris`, `docs/qa/jewish-tradition/episodes/19-bounded-civilian-withdrawal-sepphoris`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 19-bounded-civilian-withdrawal-sepphoris
- **Order**: 19
- **HistoricalFrame**: 351/352 CE; late partisan reports and scale disputed; geography=sepphoris; core=bounded-civilian-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/19-bounded-civilian-withdrawal-sepphoris: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S24 — Episodio 20: The Arguments beside the Water
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/20-parallel-text-preservation-galilee`, `docs/qa/jewish-tradition/episodes/20-parallel-text-preservation-galilee`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 20-parallel-text-preservation-galilee
- **Order**: 20
- **HistoricalFrame**: c.350–400 CE; compilation process, no single closing date; geography=galilee; core=parallel-text-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/20-parallel-text-preservation-galilee: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 21: Foundations That Remained
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/21-finite-works-and-safe-withdrawal-jerusalem`, `docs/qa/jewish-tradition/episodes/21-finite-works-and-safe-withdrawal-jerusalem`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 21-finite-works-and-safe-withdrawal-jerusalem
- **Order**: 21
- **HistoricalFrame**: 363 CE; failed rebuilding initiative; geography=jerusalem; core=finite-works-and-safe-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/21-finite-works-and-safe-withdrawal-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S26 — Episodio 22: A Boundary Written in Law
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/22-law-and-community-records-thessalonica`, `docs/qa/jewish-tradition/episodes/22-law-and-community-records-thessalonica`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 22-law-and-community-records-thessalonica
- **Order**: 22
- **HistoricalFrame**: 14 March388 CE; geography=thessalonica; core=law-and-community-records
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/22-law-and-community-records-thessalonica: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S27 — Episodio 23: An Order to Protect the Doors
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/23-petition-and-restoration-records-constantinople`, `docs/qa/jewish-tradition/episodes/23-petition-and-restoration-records-constantinople`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-petition-and-restoration-records-constantinople
- **Order**: 23
- **HistoricalFrame**: 29 September393 CE; geography=constantinople; core=petition-and-restoration-records
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/23-petition-and-restoration-records-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S28 — Episodio 24: The Names on Two Faces
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/24-epigraphic-donor-logistics-aphrodisias`, `docs/qa/jewish-tradition/episodes/24-epigraphic-donor-logistics-aphrodisias`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 24-epigraphic-donor-logistics-aphrodisias
- **Order**: 24
- **HistoricalFrame**: late4th century CE; dating debated; geography=aphrodisias; core=epigraphic-donor-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/24-epigraphic-donor-logistics-aphrodisias: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S29 — Episodio 25: The Sealed Collection
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/25-bounded-fiscal-transition-milan`, `docs/qa/jewish-tradition/episodes/25-bounded-fiscal-transition-milan`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 25-bounded-fiscal-transition-milan
- **Order**: 25
- **HistoricalFrame**: 11 April399 CE; geography=milan; core=bounded-fiscal-transition
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/25-bounded-fiscal-transition-milan: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S30 — Episodio 26: Stone for the Village
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/26-finite-community-construction-huqoq`, `docs/qa/jewish-tradition/episodes/26-finite-community-construction-huqoq`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 26-finite-community-construction-huqoq
- **Order**: 26
- **HistoricalFrame**: late4th–early5th century CE; c.400; geography=huqoq; core=finite-community-construction
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/26-finite-community-construction-huqoq: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S31 — Episodio 27: The Receipt Restored
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/27-courier-and-account-restoration-rome-ostia`, `docs/qa/jewish-tradition/episodes/27-courier-and-account-restoration-rome-ostia`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 27-courier-and-account-restoration-rome-ostia
- **Order**: 27
- **HistoricalFrame**: 25 July404 CE; geography=rome-ostia; core=courier-and-account-restoration
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/27-courier-and-account-restoration-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S32 — Episodio 28: An Honour Removed
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/28-authority-and-witness-records-constantinople`, `docs/qa/jewish-tradition/episodes/28-authority-and-witness-records-constantinople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 28-authority-and-witness-records-constantinople
- **Order**: 28
- **HistoricalFrame**: 20 October415 CE; geography=constantinople; core=authority-and-witness-records
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/28-authority-and-witness-records-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S33 — Episodio 29: The Existing Doors
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/29-repair-within-restrictions-constantinople`, `docs/qa/jewish-tradition/episodes/29-repair-within-restrictions-constantinople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 29-repair-within-restrictions-constantinople
- **Order**: 29
- **HistoricalFrame**: 15 February423 CE; CTh16.8.25; geography=constantinople; core=repair-within-restrictions
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/29-repair-within-restrictions-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S6 — Episodio 30: The Living Margin
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/jewish-tradition/scenarios/04-the-living-margin`, `docs/qa/jewish-tradition/episodes/04-the-living-margin`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 04-the-living-margin
- **Order**: 30
- **HistoricalFrame**: c.425 CE; editorial limit, patriarchate end approximate; geography=galilee; core=archive-and-final-perspective
- acceptance:
  - "Materializar únicamente el expediente aprobado jewish-tradition/04-the-living-margin: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S7 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S3, S8, S9, S10, S11, S12, S13, S14, S15, S16, S17, S18, S4, S19, S20, S5, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S6]
- **Files**: `staging/campaigns/jewish-tradition`, `campaigns/jewish-tradition`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/jewish-tradition/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 30 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 30 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates por entrega reales: fuentes por episodio aprobado, promoción sólo con la odisea completa y sus pruebas nativas; sin atribuir a MiniMax decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
