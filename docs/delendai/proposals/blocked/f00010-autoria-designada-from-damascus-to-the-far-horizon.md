---
id: f00010
title: "Autoria designada: From Damascus to the Far Horizon"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: b1a11751-fc17-47ec-a614-d31adfc62768
last-correlation-id: b1a11751-fc17-47ec-a614-d31adfc62768
last-transition-from: ready
last-transition-at: 2026-10-12T14:24:55.142Z
---

# f00010 — Autoria designada: From Damascus to the Far Horizon

## goal

MiniMax M3.1 materializa `umayyads` / CDF-I02 como odisea independiente de 32 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. La propuesta conserva su estado operativo hasta comprobar los gates. Una selección no es un contrato aprobado: sólo se materializa el subconjunto con paquete individual aprobado para fuentes; el resto de la odisea puede seguir en diseño.

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

Fuente editorial: `docs/design/odysseys/umayyads.json`. Índice: `docs/wiki/umayyads/14-odyssey-arc.md`. Expediente de cada misión: `docs/wiki/umayyads/episodes/<scenarioId>/15-odyssey-dossier.md`, disponible solo cuando se haya redactado. Los documentos anteriores de la base son antecedentes; no autorizan ejecutar un antiguo final a mitad del arco ampliado.

| Acto | Título fuente | Episodios en orden | Slices asignados |
|---|---|---|---|
| act-1 | The Ledger of Damascus | 1, 2, 3 | S3, S9, S10 |
| act-2 | The Second Fracture | 4, 5, 6, 7, 8, 9, 10, 11, 12 | S11, S12, S13, S14, S4, S15, S16, S17, S5 |
| act-3 | Across the Oxus | 13, 14, 15, 16, 17, 18, 19 | S18, S19, S20, S21, S22, S23, S24 |
| act-4 | The Sea and the Far Horizon | 20, 21, 22, 23, 24, 25, 26, 27 | S6, S25, S26, S27, S28, S29, S30, S31 |
| act-5 | The Last Accounts | 28, 29, 30, 31, 32 | S32, S33, S34, S7, S35 |

## slices

- global_gate: e2e

### S1 — Comprobar los expedientes aprobados sin rediseñarlos
- **Status**: pending
- **Files**: `docs/qa/umayyads/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Verificar el manifiesto completo de 32 episodios y cinco actos de umayyads, con estado por episodio. Para iniciar fuentes basta al menos un expediente individual completo y aprobado para ese alcance, sus pasajes consultados, decisiones de geografía/narrador/objetivos/nivelación cerradas y revisión independiente. Los demás quedan pendientes; MiniMax informa brechas, no las decide."
  - "Contrastar IDs estables, sourceLocale=en, EN/es-ES completos, voz factual común antes de persona situada y orden de campaña no bloqueante; conservar estados pendientes de otros idiomas y medios."

### S2 — Metadatos, pantallas de campaña y medios en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/umayyads/campaign.json`, `staging/campaigns/umayyads/native`, `staging/campaigns/umayyads/assets`
- **Gate**: e2e
- acceptance:
  - "Materializar la arquitectura editorial aprobada: persona propia, recaps y aviso de predecesora recomendado sin bloqueo; recordar elecciones acumulativas sin borrar otras claves ni autoiniciar otra campaña."
  - "EN/es-ES completos con claves semánticas, captions y manifiestos con hash/licencia; solo medios aprobados, sin fotos restauradas presentadas como escena antigua. staging:check --partial sin promover contenido parcial."

### S3 — Episodio 1: Ledgers of Damascus
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/01-ledgers-of-damascus`, `docs/qa/umayyads/episodes/01-ledgers-of-damascus`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-ledgers-of-damascus
- **Order**: 1
- **HistoricalFrame**: 661 CE; geography=damascus; core=administrative-and-market-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/01-ledgers-of-damascus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S9 — Episodio 2: The Son Named in the Letter
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/02-succession-and-rival-records-damascus`, `docs/qa/umayyads/episodes/02-succession-and-rival-records-damascus`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-succession-and-rival-records-damascus
- **Order**: 2
- **HistoricalFrame**: 680 CE; geography=damascus; core=succession-and-rival-records
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/02-succession-and-rival-records-damascus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 3: News That Crossed the Desert
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/03-off-map-witness-and-relief-damascus`, `docs/qa/umayyads/episodes/03-off-map-witness-and-relief-damascus`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-off-map-witness-and-relief-damascus
- **Order**: 3
- **HistoricalFrame**: October680 conventional; Karbala itself off-map; geography=damascus; core=off-map-witness-and-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/03-off-map-witness-and-relief-damascus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S11 — Episodio 4: The Roads after al-Harra
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/04-bounded-civilian-withdrawal-medina`, `docs/qa/umayyads/episodes/04-bounded-civilian-withdrawal-medina`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 04-bounded-civilian-withdrawal-medina
- **Order**: 4
- **HistoricalFrame**: 683 CE; geography=medina; core=bounded-civilian-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/04-bounded-civilian-withdrawal-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S12 — Episodio 5: The City beneath the Siege
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/05-finite-siege-and-household-relief-mecca`, `docs/qa/umayyads/episodes/05-finite-siege-and-household-relief-mecca`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 05-finite-siege-and-household-relief-mecca
- **Order**: 5
- **HistoricalFrame**: 683 CE; geography=mecca; core=finite-siege-and-household-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/05-finite-siege-and-household-relief-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S13 — Episodio 6: The Assembly on the Plateau
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/06-separate-delegation-and-supply-jabiya`, `docs/qa/umayyads/episodes/06-separate-delegation-and-supply-jabiya`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 06-separate-delegation-and-supply-jabiya
- **Order**: 6
- **HistoricalFrame**: 684 CE; geography=jabiya; core=separate-delegation-and-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/06-separate-delegation-and-supply-jabiya: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 7: The Seal of Abd al-Malik
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/07-administrative-transition-damascus`, `docs/qa/umayyads/episodes/07-administrative-transition-damascus`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 07-administrative-transition-damascus
- **Order**: 7
- **HistoricalFrame**: 685 CE; geography=damascus; core=administrative-transition
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/07-administrative-transition-damascus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S4 — Episodio 8: Stone and Memory
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/02-stone-and-memory`, `docs/qa/umayyads/episodes/02-stone-and-memory`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 02-stone-and-memory
- **Order**: 8
- **HistoricalFrame**: 691/692 CE; geography=jerusalem; core=finite-monument-works
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/02-stone-and-memory: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S15 — Episodio 9: After the Second Siege
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/09-civilian-refuge-and-property-records-mecca`, `docs/qa/umayyads/episodes/09-civilian-refuge-and-property-records-mecca`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 09-civilian-refuge-and-property-records-mecca
- **Order**: 9
- **HistoricalFrame**: 692 CE; geography=mecca; core=civilian-refuge-and-property-records
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/09-civilian-refuge-and-property-records-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S16 — Episodio 10: A Governor at the Iraqi Door
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/10-fiscal-and-witness-records-kufa`, `docs/qa/umayyads/episodes/10-fiscal-and-witness-records-kufa`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-fiscal-and-witness-records-kufa
- **Order**: 10
- **HistoricalFrame**: 694 CE; geography=kufa; core=fiscal-and-witness-records
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/10-fiscal-and-witness-records-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S17 — Episodio 11: Gold without the Old Portrait
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/11-finite-mint-and-market-reconciliation-damascus`, `docs/qa/umayyads/episodes/11-finite-mint-and-market-reconciliation-damascus`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 11-finite-mint-and-market-reconciliation-damascus
- **Order**: 11
- **HistoricalFrame**: 696–697 CE; phasedreforms; geography=damascus; core=finite-mint-and-market-reconciliation
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/11-finite-mint-and-market-reconciliation-damascus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 12: The Western Shore
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/03-the-western-shore`, `docs/qa/umayyads/episodes/03-the-western-shore`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 03-the-western-shore
- **Order**: 12
- **HistoricalFrame**: 698 CE; geography=carthage; core=finite-harbour-battle-and-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/03-the-western-shore: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S18 — Episodio 13: The Fields of the Broken Banner
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/13-finite-battle-and-civilian-extraction-kufa`, `docs/qa/umayyads/episodes/13-finite-battle-and-civilian-extraction-kufa`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 13-finite-battle-and-civilian-extraction-kufa
- **Order**: 13
- **HistoricalFrame**: 700–701 CE; DayralJamajimregionalfootprintuncertain; geography=kufa; core=finite-battle-and-civilian-extraction
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/13-finite-battle-and-civilian-extraction-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S19 — Episodio 14: Orders at the Eastern Gate
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/14-provincial-dispatch-and-provision-merv`, `docs/qa/umayyads/episodes/14-provincial-dispatch-and-provision-merv`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 14-provincial-dispatch-and-provision-merv
- **Order**: 14
- **HistoricalFrame**: 705 CE; geography=merv; core=provincial-dispatch-and-provision
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/14-provincial-dispatch-and-provision-merv: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 15: The Walls of Paykand
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/15-finite-siege-and-trade-recovery-paykand`, `docs/qa/umayyads/episodes/15-finite-siege-and-trade-recovery-paykand`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 15-finite-siege-and-trade-recovery-paykand
- **Order**: 15
- **HistoricalFrame**: 706 CE; geography=paykand; core=finite-siege-and-trade-recovery
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/15-finite-siege-and-trade-recovery-paykand: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S21 — Episodio 16: The Roads through Ramitin
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/16-finite-relief-and-withdrawal-ramitin`, `docs/qa/umayyads/episodes/16-finite-relief-and-withdrawal-ramitin`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 16-finite-relief-and-withdrawal-ramitin
- **Order**: 16
- **HistoricalFrame**: 707 CE; localityidentificationqualified; geography=ramitin; core=finite-relief-and-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/16-finite-relief-and-withdrawal-ramitin: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S22 — Episodio 17: A Receipt at Bukhara's Gate
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/17-tribute-and-household-receipts-bukhara`, `docs/qa/umayyads/episodes/17-tribute-and-household-receipts-bukhara`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 17-tribute-and-household-receipts-bukhara
- **Order**: 17
- **HistoricalFrame**: 709 CE; geography=bukhara; core=tribute-and-household-receipts
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/17-tribute-and-household-receipts-bukhara: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S23 — Episodio 18: A Message from Tokharistan
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/18-civilian-record-and-refuge-balkh`, `docs/qa/umayyads/episodes/18-civilian-record-and-refuge-balkh`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 18-civilian-record-and-refuge-balkh
- **Order**: 18
- **HistoricalFrame**: 710 CE; captureofNizakreported, notplayerexecution; geography=balkh; core=civilian-record-and-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/18-civilian-record-and-refuge-balkh: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S24 — Episodio 19: Tribute beyond the Mountain Road
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/19-off-map-dispatch-and-bounded-accounts-balkh`, `docs/qa/umayyads/episodes/19-off-map-dispatch-and-bounded-accounts-balkh`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 19-off-map-dispatch-and-bounded-accounts-balkh
- **Order**: 19
- **HistoricalFrame**: 711 CE; Zabulistanoff-map, locationnotassertedinBalkh; geography=balkh; core=off-map-dispatch-and-bounded-accounts
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/19-off-map-dispatch-and-bounded-accounts-balkh: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S6 — Episodio 20: The Narrow Sea
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/04-the-narrow-sea`, `docs/qa/umayyads/episodes/04-the-narrow-sea`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 04-the-narrow-sea
- **Order**: 20
- **HistoricalFrame**: 711–712 CE; geography=gibraltar; core=finite-strait-convoy-and-civilian-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/04-the-narrow-sea: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 21: Accounts on the Lower Oxus
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/21-bounded-river-trade-and-receipts-khwarazm`, `docs/qa/umayyads/episodes/21-bounded-river-trade-and-receipts-khwarazm`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 21-bounded-river-trade-and-receipts-khwarazm
- **Order**: 21
- **HistoricalFrame**: 712 CE; geography=khwarazm; core=bounded-river-trade-and-receipts
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/21-bounded-river-trade-and-receipts-khwarazm: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S26 — Episodio 22: The City at the End of the Road
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/22-finite-siege-and-property-records-samarkand`, `docs/qa/umayyads/episodes/22-finite-siege-and-property-records-samarkand`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 22-finite-siege-and-property-records-samarkand
- **Order**: 22
- **HistoricalFrame**: 712 CE; geography=samarkand; core=finite-siege-and-property-records
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/22-finite-siege-and-property-records-samarkand: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S27 — Episodio 23: The Citadel's New Courtyard
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/23-finite-works-and-source-comparison-bukhara`, `docs/qa/umayyads/episodes/23-finite-works-and-source-comparison-bukhara`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-finite-works-and-source-comparison-bukhara
- **Order**: 23
- **HistoricalFrame**: 712–713 CE; attendanceclaimsattributed, noconversiongoal; geography=bukhara; core=finite-works-and-source-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/23-finite-works-and-source-comparison-bukhara: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S28 — Episodio 24: Toward the Shash Oasis
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/24-finite-caravan-and-relief-tashkent`, `docs/qa/umayyads/episodes/24-finite-caravan-and-relief-tashkent`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 24-finite-caravan-and-relief-tashkent
- **Order**: 24
- **HistoricalFrame**: 714 CE; Fergana/Isfijabreportedoff-map; geography=tashkent; core=finite-caravan-and-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/24-finite-caravan-and-relief-tashkent: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S29 — Episodio 25: The Camp without Its Commander
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/25-finite-withdrawal-and-record-preservation-fergana`, `docs/qa/umayyads/episodes/25-finite-withdrawal-and-record-preservation-fergana`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 25-finite-withdrawal-and-record-preservation-fergana
- **Order**: 25
- **HistoricalFrame**: 715 CE; commanderhistoricaldeathreported; geography=fergana; core=finite-withdrawal-and-record-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/25-finite-withdrawal-and-record-preservation-fergana: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S30 — Episodio 26: The Winter beyond the Strait
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/26-finite-siege-withdrawal-and-supply-constantinople`, `docs/qa/umayyads/episodes/26-finite-siege-withdrawal-and-supply-constantinople`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 26-finite-siege-withdrawal-and-supply-constantinople
- **Order**: 26
- **HistoricalFrame**: 717–718 CE; siegefailsregardlesslocalachievement; geography=constantinople; core=finite-siege-withdrawal-and-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/26-finite-siege-withdrawal-and-supply-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S31 — Episodio 27: The Quarter after Zayd's Revolt
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/27-bounded-civilian-refuge-kufa`, `docs/qa/umayyads/episodes/27-bounded-civilian-refuge-kufa`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 27-bounded-civilian-refuge-kufa
- **Order**: 27
- **HistoricalFrame**: 740 CE; dateconversionvariants; geography=kufa; core=bounded-civilian-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/27-bounded-civilian-refuge-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S32 — Episodio 28: The Seals That Would Not Hold
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/28-competing-provincial-dispatches-damascus`, `docs/qa/umayyads/episodes/28-competing-provincial-dispatches-damascus`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 28-competing-provincial-dispatches-damascus
- **Order**: 28
- **HistoricalFrame**: 744–747 CE; onecity receivesreports; geography=damascus; core=competing-provincial-dispatches
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/28-competing-provincial-dispatches-damascus: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S33 — Episodio 29: A Banner Raised in Marw
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/29-bounded-camp-and-civilian-provision-merv`, `docs/qa/umayyads/episodes/29-bounded-camp-and-civilian-provision-merv`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 29-bounded-camp-and-civilian-provision-merv
- **Order**: 29
- **HistoricalFrame**: 747 CE; geography=merv; core=bounded-camp-and-civilian-provision
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/29-bounded-camp-and-civilian-provision-merv: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S34 — Episodio 30: A New Voice at Kufa
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/30-administrative-and-household-reception-kufa`, `docs/qa/umayyads/episodes/30-administrative-and-household-reception-kufa`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 30-administrative-and-household-reception-kufa
- **Order**: 30
- **HistoricalFrame**: November749 CE; geography=kufa; core=administrative-and-household-reception
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/30-administrative-and-household-reception-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S7 — Episodio 31: The Last Crossing
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/05-the-last-crossing`, `docs/qa/umayyads/episodes/05-the-last-crossing`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 05-the-last-crossing
- **Order**: 31
- **HistoricalFrame**: 750 CE; geography=zab; core=finite-river-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/05-the-last-crossing: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S35 — Episodio 32: The Dynasty's Last Dispatch
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/umayyads/scenarios/32-civilian-records-and-final-perspective-fustat`, `docs/qa/umayyads/episodes/32-civilian-records-and-final-perspective-fustat`, `staging/campaigns/umayyads/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 32-civilian-records-and-final-perspective-fustat
- **Order**: 32
- **HistoricalFrame**: August750 CE; killingatBusirreportedoff-map; geography=fustat; core=civilian-records-and-final-perspective
- acceptance:
  - "Materializar únicamente el expediente aprobado umayyads/32-civilian-records-and-final-perspective-fustat: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S8 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S3, S9, S10, S11, S12, S13, S14, S4, S15, S16, S17, S5, S18, S19, S20, S21, S22, S23, S24, S6, S25, S26, S27, S28, S29, S30, S31, S32, S33, S34, S7, S35]
- **Files**: `staging/campaigns/umayyads`, `campaigns/umayyads`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/umayyads/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 32 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 32 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates por entrega reales: fuentes por episodio aprobado, promoción sólo con la odisea completa y sus pruebas nativas; sin atribuir a MiniMax decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
