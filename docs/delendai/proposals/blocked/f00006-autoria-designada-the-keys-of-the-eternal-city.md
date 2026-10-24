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

MiniMax M3.1 materializa `church-of-rome` / CDF-C03 como odisea independiente de 32 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. La propuesta conserva su estado operativo hasta comprobar los gates. Una selección no es un contrato aprobado: sólo se materializa el subconjunto con paquete individual aprobado para fuentes; el resto de la odisea puede seguir en diseño.

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
  - "Verificar el manifiesto completo de 32 episodios y cinco actos de church-of-rome, con estado por episodio. Para iniciar fuentes basta al menos un expediente individual completo y aprobado para ese alcance, sus pasajes consultados, decisiones de geografía/narrador/objetivos/nivelación cerradas y revisión independiente. Los demás quedan pendientes; MiniMax informa brechas, no las decide."
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
- **Files**: `staging/campaigns/church-of-rome/scenarios/01-refuge-and-petition-reception-rome-ostia`, `docs/qa/church-of-rome/episodes/01-refuge-and-petition-reception-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-refuge-and-petition-reception-rome-ostia
- **Order**: 1
- **HistoricalFrame**: 339–340 CE; geography=rome-ostia; core=refuge-and-petition-reception
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/01-refuge-and-petition-reception-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S9 — Episodio 2: A Road to Two Councils
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/02-separate-delegation-logistics-sardica`, `docs/qa/church-of-rome/episodes/02-separate-delegation-logistics-sardica`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-separate-delegation-logistics-sardica
- **Order**: 2
- **HistoricalFrame**: 343 CE; chronology qualified; geography=sardica; core=separate-delegation-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/02-separate-delegation-logistics-sardica: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 3: Letters to a Distant Bishop
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/03-exile-supply-and-correspondence-beroea-thrace`, `docs/qa/church-of-rome/episodes/03-exile-supply-and-correspondence-beroea-thrace`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-exile-supply-and-correspondence-beroea-thrace
- **Order**: 3
- **HistoricalFrame**: 355–357 CE; geography=beroea-thrace; core=exile-supply-and-correspondence
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/03-exile-supply-and-correspondence-beroea-thrace: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S11 — Episodio 4: The Formula by the Sea
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/04-draft-and-delegate-network-rimini`, `docs/qa/church-of-rome/episodes/04-draft-and-delegate-network-rimini`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 04-draft-and-delegate-network-rimini
- **Order**: 4
- **HistoricalFrame**: 359 CE; geography=rimini; core=draft-and-delegate-network
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/04-draft-and-delegate-network-rimini: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S12 — Episodio 5: Two Names for the Same Chair
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/05-neutral-civilian-extraction-rome-ostia`, `docs/qa/church-of-rome/episodes/05-neutral-civilian-extraction-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 05-neutral-civilian-extraction-rome-ostia
- **Order**: 5
- **HistoricalFrame**: 366–367 CE; factional violence; geography=rome-ostia; core=neutral-civilian-extraction
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/05-neutral-civilian-extraction-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S13 — Episodio 6: The Door That Stayed Closed
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/06-petition-and-accountability-records-milan`, `docs/qa/church-of-rome/episodes/06-petition-and-accountability-records-milan`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 06-petition-and-accountability-records-milan
- **Order**: 6
- **HistoricalFrame**: 390 CE; massacre in Thessalonica reported off-map; geography=milan; core=petition-and-accountability-records
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/06-petition-and-accountability-records-milan: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S3 — Episodio 7: Bread beyond the Gates
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/01-bread-beyond-the-gates`, `docs/qa/church-of-rome/episodes/01-bread-beyond-the-gates`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 01-bread-beyond-the-gates
- **Order**: 7
- **HistoricalFrame**: 410 CE; geography=rome-ostia; core=sanctuary-supply-and-evacuation
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/01-bread-beyond-the-gates: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 8: The Court after the Last Emperor
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/08-administrative-transition-ravenna`, `docs/qa/church-of-rome/episodes/08-administrative-transition-ravenna`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 08-administrative-transition-ravenna
- **Order**: 8
- **HistoricalFrame**: 476 CE; geography=ravenna; core=administrative-transition
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/08-administrative-transition-ravenna: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S15 — Episodio 9: The Banquet's Long Shadow
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/09-civilian-record-preservation-ravenna`, `docs/qa/church-of-rome/episodes/09-civilian-record-preservation-ravenna`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 09-civilian-record-preservation-ravenna
- **Order**: 9
- **HistoricalFrame**: 493 CE; killing reported, not rewarded; geography=ravenna; core=civilian-record-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/09-civilian-record-preservation-ravenna: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S16 — Episodio 10: Two Powers in One Letter
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/10-correspondence-consignment-rome-ostia`, `docs/qa/church-of-rome/episodes/10-correspondence-consignment-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-correspondence-consignment-rome-ostia
- **Order**: 10
- **HistoricalFrame**: 494 CE; geography=rome-ostia; core=correspondence-consignment
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/10-correspondence-consignment-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S17 — Episodio 11: Across the Old Division
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/11-reconciliation-document-logistics-constantinople`, `docs/qa/church-of-rome/episodes/11-reconciliation-document-logistics-constantinople`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 11-reconciliation-document-logistics-constantinople
- **Order**: 11
- **HistoricalFrame**: 519 CE; geography=constantinople; core=reconciliation-document-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/11-reconciliation-document-logistics-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S18 — Episodio 12: An Embassy without a Safe Return
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/12-returning-delegation-aid-ravenna`, `docs/qa/church-of-rome/episodes/12-returning-delegation-aid-ravenna`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 12-returning-delegation-aid-ravenna
- **Order**: 12
- **HistoricalFrame**: 525–526 CE; embassyConstantinople reported; geography=ravenna; core=returning-delegation-aid
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/12-returning-delegation-aid-ravenna: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S19 — Episodio 13: An Army through the Gates
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/13-district-supply-under-occupation-rome-ostia`, `docs/qa/church-of-rome/episodes/13-district-supply-under-occupation-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 13-district-supply-under-occupation-rome-ostia
- **Order**: 13
- **HistoricalFrame**: 536 CE; geography=rome-ostia; core=district-supply-under-occupation
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/13-district-supply-under-occupation-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 14: The Year outside the Walls
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/14-finite-siege-and-urban-relief-rome-ostia`, `docs/qa/church-of-rome/episodes/14-finite-siege-and-urban-relief-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 14-finite-siege-and-urban-relief-rome-ostia
- **Order**: 14
- **HistoricalFrame**: 537–538 CE; geography=rome-ostia; core=finite-siege-and-urban-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/14-finite-siege-and-urban-relief-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S21 — Episodio 15: The Empty Streets of Rome
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/15-archive-extraction-and-refuge-rome-ostia`, `docs/qa/church-of-rome/episodes/15-archive-extraction-and-refuge-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 15-archive-extraction-and-refuge-rome-ostia
- **Order**: 15
- **HistoricalFrame**: 546 CE; geography=rome-ostia; core=archive-extraction-and-refuge
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/15-archive-extraction-and-refuge-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S22 — Episodio 16: Dispatches after the Gothic War
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/16-return-and-repair-rome-ostia`, `docs/qa/church-of-rome/episodes/16-return-and-repair-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 16-return-and-repair-rome-ostia
- **Order**: 16
- **HistoricalFrame**: 552–553 CE; Taginae reported off-map; geography=rome-ostia; core=return-and-repair
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/16-return-and-repair-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S4 — Episodio 17: The Price of Peace
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/02-the-price-of-peace`, `docs/qa/church-of-rome/episodes/02-the-price-of-peace`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 02-the-price-of-peace
- **Order**: 17
- **HistoricalFrame**: 593–595 CE; Gregory590as prologue; geography=rome-ostia; core=finite-payment-and-relief
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/02-the-price-of-peace: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S23 — Episodio 18: The Road beyond the Channel
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/18-hospitality-and-mission-supply-kent`, `docs/qa/church-of-rome/episodes/18-hospitality-and-mission-supply-kent`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 18-hospitality-and-mission-supply-kent
- **Order**: 18
- **HistoricalFrame**: 596–597 CE; Rome dispatch prologue; geography=kent; core=hospitality-and-mission-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/18-hospitality-and-mission-supply-kent: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S24 — Episodio 19: A Roof for Older Stones
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/19-finite-building-conversion-rome-ostia`, `docs/qa/church-of-rome/episodes/19-finite-building-conversion-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 19-finite-building-conversion-rome-ostia
- **Order**: 19
- **HistoricalFrame**: 609 or613 CE; exact dedication debated; geography=rome-ostia; core=finite-building-conversion
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/19-finite-building-conversion-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 20: The Words at the Lateran
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/20-council-record-comparison-rome-ostia`, `docs/qa/church-of-rome/episodes/20-council-record-comparison-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 20-council-record-comparison-rome-ostia
- **Order**: 20
- **HistoricalFrame**: October649 CE; geography=rome-ostia; core=council-record-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/20-council-record-comparison-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S26 — Episodio 21: Letters from the Cold Shore
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/21-exile-relief-and-copying-cherson`, `docs/qa/church-of-rome/episodes/21-exile-relief-and-copying-cherson`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 21-exile-relief-and-copying-cherson
- **Order**: 21
- **HistoricalFrame**: 655 CE; death655/656qualified; geography=cherson; core=exile-relief-and-copying
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/21-exile-relief-and-copying-cherson: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S27 — Episodio 22: Bronze Leaving the City
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/22-finite-material-records-rome-ostia`, `docs/qa/church-of-rome/episodes/22-finite-material-records-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 22-finite-material-records-rome-ostia
- **Order**: 22
- **HistoricalFrame**: 663 CE; geography=rome-ostia; core=finite-material-records
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/22-finite-material-records-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S28 — Episodio 23: The Legates across the Water
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/23-delegation-and-document-escort-constantinople`, `docs/qa/church-of-rome/episodes/23-delegation-and-document-escort-constantinople`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-delegation-and-document-escort-constantinople
- **Order**: 23
- **HistoricalFrame**: 680–681 CE; geography=constantinople; core=delegation-and-document-escort
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/23-delegation-and-document-escort-constantinople: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S29 — Episodio 24: Canons at the Roman Door
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/24-disputed-document-reception-rome-ostia`, `docs/qa/church-of-rome/episodes/24-disputed-document-reception-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 24-disputed-document-reception-rome-ostia
- **Order**: 24
- **HistoricalFrame**: 692 CE; geography=rome-ostia; core=disputed-document-reception
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/24-disputed-document-reception-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S30 — Episodio 25: Images before the Synod
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/25-artisan-and-council-logistics-rome-ostia`, `docs/qa/church-of-rome/episodes/25-artisan-and-council-logistics-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 25-artisan-and-council-logistics-rome-ostia
- **Order**: 25
- **HistoricalFrame**: 731 CE; geography=rome-ostia; core=artisan-and-council-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/25-artisan-and-council-logistics-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S31 — Episodio 26: Beyond the Alpine Promise
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/26-delegate-and-oath-logistics-saint-denis`, `docs/qa/church-of-rome/episodes/26-delegate-and-oath-logistics-saint-denis`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 26-delegate-and-oath-logistics-saint-denis
- **Order**: 26
- **HistoricalFrame**: 754 CE; Saint-Denis local focus; geography=saint-denis; core=delegate-and-oath-logistics
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/26-delegate-and-oath-logistics-saint-denis: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 27: The Roads to Pavia
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/03-roads-to-pavia`, `docs/qa/church-of-rome/episodes/03-roads-to-pavia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 03-roads-to-pavia
- **Order**: 27
- **HistoricalFrame**: 754–756 CE; geography=pavia; core=finite-campaign-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/03-roads-to-pavia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S32 — Episodio 28: At the Lombard Gate
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/28-finite-siege-and-civilian-withdrawal-pavia`, `docs/qa/church-of-rome/episodes/28-finite-siege-and-civilian-withdrawal-pavia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 28-finite-siege-and-civilian-withdrawal-pavia
- **Order**: 28
- **HistoricalFrame**: 773–774 CE; earlier768context only; geography=pavia; core=finite-siege-and-civilian-withdrawal
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/28-finite-siege-and-civilian-withdrawal-pavia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S33 — Episodio 29: Roman Letters beside the Lake
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/29-delegate-logistics-and-copying-nicaea`, `docs/qa/church-of-rome/episodes/29-delegate-logistics-and-copying-nicaea`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 29-delegate-logistics-and-copying-nicaea
- **Order**: 29
- **HistoricalFrame**: 787 CE; geography=nicaea; core=delegate-logistics-and-copying
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/29-delegate-logistics-and-copying-nicaea: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S34 — Episodio 30: Keys Sent down the Road
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/30-symbolic-consignment-and-couriers-rome-ostia`, `docs/qa/church-of-rome/episodes/30-symbolic-consignment-and-couriers-rome-ostia`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 30-symbolic-consignment-and-couriers-rome-ostia
- **Order**: 30
- **HistoricalFrame**: 795 CE; geography=rome-ostia; core=symbolic-consignment-and-couriers
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/30-symbolic-consignment-and-couriers-rome-ostia: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S35 — Episodio 31: A Refuge at the Northern Court
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/31-refuge-and-petition-escort-paderborn`, `docs/qa/church-of-rome/episodes/31-refuge-and-petition-escort-paderborn`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 31-refuge-and-petition-escort-paderborn
- **Order**: 31
- **HistoricalFrame**: 799 CE; geography=paderborn; core=refuge-and-petition-escort
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/31-refuge-and-petition-escort-paderborn: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S6 — Episodio 32: A Crown at Dawn
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/church-of-rome/scenarios/04-a-crown-at-dawn`, `docs/qa/church-of-rome/episodes/04-a-crown-at-dawn`, `staging/campaigns/church-of-rome/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 04-a-crown-at-dawn
- **Order**: 32
- **HistoricalFrame**: 25 December800 CE; geography=rome-ostia; core=ceremony-supply-and-final-perspective
- acceptance:
  - "Materializar únicamente el expediente aprobado church-of-rome/04-a-crown-at-dawn: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S7 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S8, S9, S10, S11, S12, S13, S3, S14, S15, S16, S17, S18, S19, S20, S21, S22, S4, S23, S24, S25, S26, S27, S28, S29, S30, S31, S5, S32, S33, S34, S35, S6]
- **Files**: `staging/campaigns/church-of-rome`, `campaigns/church-of-rome`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/church-of-rome/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 32 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 32 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates por entrega reales: fuentes por episodio aprobado, promoción sólo con la odisea completa y sus pruebas nativas; sin atribuir a MiniMax decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
