---
id: f00007
title: "Autoria designada: Beyond the Golden Gate"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: 9f55b54b-2494-464d-9b22-98bea15db7a3
last-correlation-id: 9f55b54b-2494-464d-9b22-98bea15db7a3
last-transition-from: ready
last-transition-at: 2026-10-12T14:24:28.544Z
---

# f00007 — Autoria designada: Beyond the Golden Gate

## goal

MiniMax M3.1 materializa `new-rome` / CDF-C04 como odisea independiente de 32 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. La propuesta conserva su estado operativo hasta comprobar los gates. Una selección no es un contrato aprobado: sólo se materializa el subconjunto con paquete individual aprobado para fuentes; el resto de la odisea puede seguir en diseño.

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

Fuente editorial: `docs/design/odysseys/new-rome.json`. Índice: `docs/wiki/new-rome/14-odyssey-arc.md`. Expediente de cada misión: `docs/wiki/new-rome/episodes/<scenarioId>/15-odyssey-dossier.md`, disponible solo cuando se haya redactado. Los documentos anteriores de la base son antecedentes; no autorizan ejecutar un antiguo final a mitad del arco ampliado.

| Acto | Título fuente | Episodios en orden | Slices asignados |
|---|---|---|---|
| act-1 | Heirs of the Eastern Gate | 1, 2, 3, 4, 5, 6, 7, 8 | S9, S10, S11, S12, S13, S14, S15, S16 |
| act-2 | The Council and the City | 9, 10, 11, 12, 13, 14, 15, 16, 17 | S3, S17, S18, S19, S4, S20, S21, S5, S22 |
| act-3 | Grain Beneath the Siege | 18, 19, 20, 21, 22 | S23, S24, S25, S26, S6 |
| act-4 | Images at the Edge | 23, 24, 25 | S27, S28, S7 |
| act-5 | The Mosaic Restored | 26, 27, 28, 29, 30, 31, 32 | S29, S30, S31, S32, S33, S34, S35 |

## slices

- global_gate: e2e

### S1 — Comprobar los expedientes aprobados sin rediseñarlos
- **Status**: pending
- **Files**: `docs/qa/new-rome/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Verificar el manifiesto completo de 32 episodios y cinco actos de new-rome, con estado por episodio. Para iniciar fuentes basta al menos un expediente individual completo y aprobado para ese alcance, sus pasajes consultados, decisiones de geografía/narrador/objetivos/nivelación cerradas y revisión independiente. Los demás quedan pendientes; MiniMax informa brechas, no las decide."
  - "Contrastar IDs estables, sourceLocale=en, EN/es-ES completos, voz factual común antes de persona situada y orden de campaña no bloqueante; conservar estados pendientes de otros idiomas y medios."

### S2 — Metadatos, pantallas de campaña y medios en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/new-rome/campaign.json`, `staging/campaigns/new-rome/native`, `staging/campaigns/new-rome/assets`
- **Gate**: e2e
- acceptance:
  - "Materializar la arquitectura editorial aprobada: persona propia, recaps y aviso de predecesora recomendado sin bloqueo; recordar elecciones acumulativas sin borrar otras claves ni autoiniciar otra campaña."
  - "EN/es-ES completos con claves semánticas, captions y manifiestos con hash/licencia; solo medios aprobados, sin fotos restauradas presentadas como escena antigua. staging:check --partial sin promover contenido parcial."

### S9 — Episodio 1: The Gate after Its Founder
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/01-administrative-transition-constantinople`, `docs/qa/new-rome/episodes/01-administrative-transition-constantinople`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-administrative-transition-constantinople
- **Order**: 1
- **HistoricalFrame**: 337 CE; Nicomedia death reported; geography=constantinople; core=administrative-transition
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/01-administrative-transition-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 2: The City's Place in the Canon
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/02-council-and-city-logistics-constantinople`, `docs/qa/new-rome/episodes/02-council-and-city-logistics-constantinople`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-council-and-city-logistics-constantinople
- **Order**: 2
- **HistoricalFrame**: 381 CE; geography=constantinople; core=council-and-city-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/02-council-and-city-logistics-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S11 — Episodio 3: Two Courts beneath One Memory
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/03-competing-dispatches-constantinople`, `docs/qa/new-rome/episodes/03-competing-dispatches-constantinople`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-competing-dispatches-constantinople
- **Order**: 3
- **HistoricalFrame**: 395 CE; deathMilan off-map; geography=constantinople; core=competing-dispatches
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/03-competing-dispatches-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S12 — Episodio 4: The Bishop Who Was Sent Away
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/04-civilian-refuge-and-dispatch-constantinople`, `docs/qa/new-rome/episodes/04-civilian-refuge-and-dispatch-constantinople`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 04-civilian-refuge-and-dispatch-constantinople
- **Order**: 4
- **HistoricalFrame**: 404 CE; geography=constantinople; core=civilian-refuge-and-dispatch
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/04-civilian-refuge-and-dispatch-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S13 — Episodio 5: Rooms for the Written Word
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/05-finite-school-works-constantinople`, `docs/qa/new-rome/episodes/05-finite-school-works-constantinople`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 05-finite-school-works-constantinople
- **Order**: 5
- **HistoricalFrame**: 425 CE; school institution, not modern university; geography=constantinople; core=finite-school-works
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/05-finite-school-works-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 6: Before the Delegates Arrived
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/06-separate-session-logistics-ephesus`, `docs/qa/new-rome/episodes/06-separate-session-logistics-ephesus`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 06-separate-session-logistics-ephesus
- **Order**: 6
- **HistoricalFrame**: 431 CE; geography=ephesus; core=separate-session-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/06-separate-session-logistics-ephesus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S15 — Episodio 7: A Return after the Exile
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/07-ceremony-and-household-logistics-constantinople`, `docs/qa/new-rome/episodes/07-ceremony-and-household-logistics-constantinople`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 07-ceremony-and-household-logistics-constantinople
- **Order**: 7
- **HistoricalFrame**: 438 CE; relics transfer; geography=constantinople; core=ceremony-and-household-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/07-ceremony-and-household-logistics-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S16 — Episodio 8: The Law Gathered into Books
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/08-distributed-record-collation-constantinople`, `docs/qa/new-rome/episodes/08-distributed-record-collation-constantinople`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 08-distributed-record-collation-constantinople
- **Order**: 8
- **HistoricalFrame**: 438 CE; publication/439effective distinguished; geography=constantinople; core=distributed-record-collation
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/08-distributed-record-collation-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S3 — Episodio 9: Across the Strait
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/01-across-the-strait`, `docs/qa/new-rome/episodes/01-across-the-strait`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 01-across-the-strait
- **Order**: 9
- **HistoricalFrame**: 451 CE; geography=chalcedon; core=delegate-and-ferry-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/01-across-the-strait: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S17 — Episodio 10: The Emperor at the City's Edge
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/10-ceremony-route-and-provision-constantinople`, `docs/qa/new-rome/episodes/10-ceremony-route-and-provision-constantinople`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-ceremony-route-and-provision-constantinople
- **Order**: 10
- **HistoricalFrame**: 457 CE; geography=constantinople; core=ceremony-route-and-provision
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/10-ceremony-route-and-provision-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S18 — Episodio 11: A Letter That Could Not Unite
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/11-disputed-correspondence-constantinople`, `docs/qa/new-rome/episodes/11-disputed-correspondence-constantinople`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 11-disputed-correspondence-constantinople
- **Order**: 11
- **HistoricalFrame**: 482 CE; geography=constantinople; core=disputed-correspondence
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/11-disputed-correspondence-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S19 — Episodio 12: One Seal after Two Emperors
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/12-administrative-transition-constantinople`, `docs/qa/new-rome/episodes/12-administrative-transition-constantinople`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 12-administrative-transition-constantinople
- **Order**: 12
- **HistoricalFrame**: 1 August527 CE; co-rule sinceApril; geography=constantinople; core=administrative-transition
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/12-administrative-transition-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S4 — Episodio 13: The City in Ashes
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/02-the-city-in-ashes`, `docs/qa/new-rome/episodes/02-the-city-in-ashes`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 02-the-city-in-ashes
- **Order**: 13
- **HistoricalFrame**: January532 CE; geography=constantinople; core=civilian-evacuation-under-unrest
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/02-the-city-in-ashes: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 14: Stone beneath the Great Dome
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/14-finite-construction-logistics-constantinople`, `docs/qa/new-rome/episodes/14-finite-construction-logistics-constantinople`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 14-finite-construction-logistics-constantinople
- **Order**: 14
- **HistoricalFrame**: 532–537 CE; dedication537; geography=constantinople; core=finite-construction-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/14-finite-construction-logistics-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S21 — Episodio 15: The Orontes after the Flames
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/15-bounded-civilian-extraction-antioch`, `docs/qa/new-rome/episodes/15-bounded-civilian-extraction-antioch`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 15-bounded-civilian-extraction-antioch
- **Order**: 15
- **HistoricalFrame**: 540 CE; geography=antioch; core=bounded-civilian-extraction
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/15-bounded-civilian-extraction-antioch: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 16: The Empty Granary
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/03-the-empty-granary`, `docs/qa/new-rome/episodes/03-the-empty-granary`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 03-the-empty-granary
- **Order**: 16
- **HistoricalFrame**: 542 CE; geography=constantinople; core=care-and-food-allocation
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/03-the-empty-granary: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S22 — Episodio 17: The Chapters on the Table
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/17-council-record-comparison-constantinople`, `docs/qa/new-rome/episodes/17-council-record-comparison-constantinople`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 17-council-record-comparison-constantinople
- **Order**: 17
- **HistoricalFrame**: 553 CE; geography=constantinople; core=council-record-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/17-council-record-comparison-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S23 — Episodio 18: A City between Two Armies
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/18-finite-siege-and-ferry-supply-constantinople`, `docs/qa/new-rome/episodes/18-finite-siege-and-ferry-supply-constantinople`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 18-finite-siege-and-ferry-supply-constantinople
- **Order**: 18
- **HistoricalFrame**: 626 CE; geography=constantinople; core=finite-siege-and-ferry-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/18-finite-siege-and-ferry-supply-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S24 — Episodio 19: News from the Holy City
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/19-civilian-record-and-property-logistics-jerusalem`, `docs/qa/new-rome/episodes/19-civilian-record-and-property-logistics-jerusalem`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 19-civilian-record-and-property-logistics-jerusalem
- **Order**: 19
- **HistoricalFrame**: 637/638 CE; capitulation reports qualified; geography=jerusalem; core=civilian-record-and-property-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/19-civilian-record-and-property-logistics-jerusalem: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 20: Ships in the Uncertain Years
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/20-coastal-watch-and-bounded-convoy-constantinople`, `docs/qa/new-rome/episodes/20-coastal-watch-and-bounded-convoy-constantinople`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 20-coastal-watch-and-bounded-convoy-constantinople
- **Order**: 20
- **HistoricalFrame**: c.674–678 CE; continuous siege disputed; geography=constantinople; core=coastal-watch-and-bounded-convoy
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/20-coastal-watch-and-bounded-convoy-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S26 — Episodio 21: Eighteen Sessions by the Palace
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/21-delegation-and-text-comparison-constantinople`, `docs/qa/new-rome/episodes/21-delegation-and-text-comparison-constantinople`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 21-delegation-and-text-comparison-constantinople
- **Order**: 21
- **HistoricalFrame**: 680–681 CE; geography=constantinople; core=delegation-and-text-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/21-delegation-and-text-comparison-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S6 — Episodio 22: Winter at the Walls
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/04-winter-at-the-walls`, `docs/qa/new-rome/episodes/04-winter-at-the-walls`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 04-winter-at-the-walls
- **Order**: 22
- **HistoricalFrame**: 717–718 CE; geography=constantinople; core=finite-winter-siege-and-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/04-winter-at-the-walls: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S27 — Episodio 23: An Image beneath the Orders
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/23-artisan-record-and-protection-constantinople`, `docs/qa/new-rome/episodes/23-artisan-record-and-protection-constantinople`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-artisan-record-and-protection-constantinople
- **Order**: 23
- **HistoricalFrame**: c.726–730 CE; policy chronology disputed; geography=constantinople; core=artisan-record-and-protection
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/23-artisan-record-and-protection-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S28 — Episodio 24: The Assembly at Hieria
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/24-council-and-workshop-logistics-chalcedon`, `docs/qa/new-rome/episodes/24-council-and-workshop-logistics-chalcedon`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 24-council-and-workshop-logistics-chalcedon
- **Order**: 24
- **HistoricalFrame**: 754 CE; reconstructed from later opposing acts; geography=chalcedon; core=council-and-workshop-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/24-council-and-workshop-logistics-chalcedon: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S7 — Episodio 25: Pieces of a Memory
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/05-pieces-of-a-memory`, `docs/qa/new-rome/episodes/05-pieces-of-a-memory`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 05-pieces-of-a-memory
- **Order**: 25
- **HistoricalFrame**: 787 CE; former843epilogue now separatefinale; geography=nicaea; core=restoration-and-council-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/05-pieces-of-a-memory: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S29 — Episodio 26: The Court under Irene
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/26-civilian-supply-and-succession-records-constantinople`, `docs/qa/new-rome/episodes/26-civilian-supply-and-succession-records-constantinople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 26-civilian-supply-and-succession-records-constantinople
- **Order**: 26
- **HistoricalFrame**: 797 CE; geography=constantinople; core=civilian-supply-and-succession-records
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/26-civilian-supply-and-succession-records-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S30 — Episodio 27: A Crown beyond the Western Sea
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/27-off-map-dispatch-and-comparison-constantinople`, `docs/qa/new-rome/episodes/27-off-map-dispatch-and-comparison-constantinople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 27-off-map-dispatch-and-comparison-constantinople
- **Order**: 27
- **HistoricalFrame**: 800 CE; crowningRome off-map; geography=constantinople; core=off-map-dispatch-and-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/27-off-map-dispatch-and-comparison-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S31 — Episodio 28: The Seal That Changed Hands
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/28-administrative-transition-constantinople`, `docs/qa/new-rome/episodes/28-administrative-transition-constantinople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 28-administrative-transition-constantinople
- **Order**: 28
- **HistoricalFrame**: 802 CE; geography=constantinople; core=administrative-transition
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/28-administrative-transition-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S32 — Episodio 29: The Roads below Pliska
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/29-finite-withdrawal-and-relief-pliska`, `docs/qa/new-rome/episodes/29-finite-withdrawal-and-relief-pliska`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 29-finite-withdrawal-and-relief-pliska
- **Order**: 29
- **HistoricalFrame**: 811 CE; battle-site footprint uncertain; geography=pliska; core=finite-withdrawal-and-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/29-finite-withdrawal-and-relief-pliska: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S33 — Episodio 30: A Report from the Thracian Field
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/30-civilian-refuge-and-dispatch-adrianople`, `docs/qa/new-rome/episodes/30-civilian-refuge-and-dispatch-adrianople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 30-civilian-refuge-and-dispatch-adrianople
- **Order**: 30
- **HistoricalFrame**: 813 CE; Versinikia regional location uncertain; geography=adrianople; core=civilian-refuge-and-dispatch
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/30-civilian-refuge-and-dispatch-adrianople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S34 — Episodio 31: The Covered Workshop
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/31-artisan-and-archive-preservation-constantinople`, `docs/qa/new-rome/episodes/31-artisan-and-archive-preservation-constantinople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 31-artisan-and-archive-preservation-constantinople
- **Order**: 31
- **HistoricalFrame**: 815 CE; geography=constantinople; core=artisan-and-archive-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/31-artisan-and-archive-preservation-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S35 — Episodio 32: The Mosaic Returned
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/new-rome/scenarios/32-restoration-and-final-perspective-constantinople`, `docs/qa/new-rome/episodes/32-restoration-and-final-perspective-constantinople`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 32-restoration-and-final-perspective-constantinople
- **Order**: 32
- **HistoricalFrame**: 843 CE; geography=constantinople; core=restoration-and-final-perspective
- acceptance:
  - "Materializar únicamente el expediente aprobado new-rome/32-restoration-and-final-perspective-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S8 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S9, S10, S11, S12, S13, S14, S15, S16, S3, S17, S18, S19, S4, S20, S21, S5, S22, S23, S24, S25, S26, S6, S27, S28, S7, S29, S30, S31, S32, S33, S34, S35]
- **Files**: `staging/campaigns/new-rome`, `campaigns/new-rome`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/new-rome/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 32 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 32 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates por entrega reales: fuentes por episodio aprobado, promoción sólo con la odisea completa y sus pruebas nativas; sin atribuir a MiniMax decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
