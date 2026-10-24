---
id: f00011
title: "Autoria designada: The River Remembers"
kind: feat
status: blocked
type: proposal
track: campaign-design
date: 2026-10-12
last-transition-id: 11db707f-fc7f-4d78-b320-789581be2752
last-correlation-id: 11db707f-fc7f-4d78-b320-789581be2752
last-transition-from: ready
last-transition-at: 2026-10-12T14:25:03.276Z
---

# f00011 — Autoria designada: The River Remembers

## goal

MiniMax M3.1 materializa `house-of-ali` / CDF-I03 como odisea independiente de 30 episodios y cinco actos. Inglés inicial y español completo. El arquitecto aporta antes de la autoría cada expediente, fuente, voz, terreno, objetivo, presupuesto y decisión de continuidad. La propuesta conserva su estado operativo hasta comprobar los gates. Una selección no es un contrato aprobado: sólo se materializa el subconjunto con paquete individual aprobado para fuentes; el resto de la odisea puede seguir en diseño.

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

Fuente editorial: `docs/design/odysseys/house-of-ali.json`. Índice: `docs/wiki/house-of-ali/14-odyssey-arc.md`. Expediente de cada misión: `docs/wiki/house-of-ali/episodes/<scenarioId>/15-odyssey-dossier.md`, disponible solo cuando se haya redactado. Los documentos anteriores de la base son antecedentes; no autorizan ejecutar un antiguo final a mitad del arco ampliado.

| Acto | Título fuente | Episodios en orden | Slices asignados |
|---|---|---|---|
| act-1 | Clay in an Uneasy City | 1, 2, 3, 4, 5 | S8, S9, S10, S3, S11 |
| act-2 | Two Banks, One Cup | 6, 7, 8, 9, 10 | S4, S12, S13, S14, S15 |
| act-3 | A Seal and a Farewell | 11, 12, 13, 14, 15, 16 | S16, S17, S5, S18, S19, S20 |
| act-4 | Letters Without a Safe Road | 17, 18, 19, 20, 21, 22, 23 | S21, S22, S23, S24, S25, S26, S27 |
| act-5 | The River Remembers | 24, 25, 26, 27, 28, 29, 30 | S28, S29, S30, S31, S32, S33, S6 |

## slices

- global_gate: e2e

### S1 — Comprobar los expedientes aprobados sin rediseñarlos
- **Status**: pending
- **Files**: `docs/qa/house-of-ali/design-conformance.md`
- **Gate**: e2e
- acceptance:
  - "Verificar el manifiesto completo de 30 episodios y cinco actos de house-of-ali, con estado por episodio. Para iniciar fuentes basta al menos un expediente individual completo y aprobado para ese alcance, sus pasajes consultados, decisiones de geografía/narrador/objetivos/nivelación cerradas y revisión independiente. Los demás quedan pendientes; MiniMax informa brechas, no las decide."
  - "Contrastar IDs estables, sourceLocale=en, EN/es-ES completos, voz factual común antes de persona situada y orden de campaña no bloqueante; conservar estados pendientes de otros idiomas y medios."

### S2 — Metadatos, pantallas de campaña y medios en staging
- **Status**: pending
- **DependsOn**: [S1]
- **Files**: `staging/campaigns/house-of-ali/campaign.json`, `staging/campaigns/house-of-ali/native`, `staging/campaigns/house-of-ali/assets`
- **Gate**: e2e
- acceptance:
  - "Materializar la arquitectura editorial aprobada: persona propia, recaps y aviso de predecesora recomendado sin bloqueo; recordar elecciones acumulativas sin borrar otras claves ni autoiniciar otra campaña."
  - "EN/es-ES completos con claves semánticas, captions y manifiestos con hash/licencia; solo medios aprobados, sin fotos restauradas presentadas como escena antigua. staging:check --partial sin promover contenido parcial."

### S8 — Episodio 1: A Promise in Medina
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/01-witness-and-transition-records-medina`, `docs/qa/house-of-ali/episodes/01-witness-and-transition-records-medina`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-witness-and-transition-records-medina
- **Order**: 1
- **HistoricalFrame**: 656 CE; geography=medina; core=witness-and-transition-records
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/01-witness-and-transition-records-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S9 — Episodio 2: The Doors before the Battle
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/02-civilian-refuge-and-petition-basra`, `docs/qa/house-of-ali/episodes/02-civilian-refuge-and-petition-basra`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 02-civilian-refuge-and-petition-basra
- **Order**: 2
- **HistoricalFrame**: 656 CE; geography=basra; core=civilian-refuge-and-petition
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/02-civilian-refuge-and-petition-basra: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S10 — Episodio 3: The Dust beyond Basra
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/03-finite-battle-withdrawal-and-care-basra`, `docs/qa/house-of-ali/episodes/03-finite-battle-withdrawal-and-care-basra`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 03-finite-battle-withdrawal-and-care-basra
- **Order**: 3
- **HistoricalFrame**: 656 CE; geography=basra; core=finite-battle-withdrawal-and-care
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/03-finite-battle-withdrawal-and-care-basra: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S3 — Episodio 4: The Kufan Hearth
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/01-the-kufan-hearth`, `docs/qa/house-of-ali/episodes/01-the-kufan-hearth`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 01-the-kufan-hearth
- **Order**: 4
- **HistoricalFrame**: 656/657 CE; geography=kufa; core=household-reception-and-workshop-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/01-the-kufan-hearth: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S11 — Episodio 5: The Egyptian Letter
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/05-off-map-dispatch-and-source-comparison-fustat`, `docs/qa/house-of-ali/episodes/05-off-map-dispatch-and-source-comparison-fustat`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-1
- **ScenarioId**: 05-off-map-dispatch-and-source-comparison-fustat
- **Order**: 5
- **HistoricalFrame**: c.656–657 CE; Kharbitareports, settlementnotfalselylocated; geography=fustat; core=off-map-dispatch-and-source-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/05-off-map-dispatch-and-source-comparison-fustat: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S4 — Episodio 6: A Cup at Siffin
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/02-a-cup-at-siffin`, `docs/qa/house-of-ali/episodes/02-a-cup-at-siffin`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 02-a-cup-at-siffin
- **Order**: 6
- **HistoricalFrame**: 657 CE; geography=siffin; core=finite-water-and-care-corridor
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/02-a-cup-at-siffin: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S12 — Episodio 7: The Leaves above the Spears
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/07-ceasefire-withdrawal-and-records-siffin`, `docs/qa/house-of-ali/episodes/07-ceasefire-withdrawal-and-records-siffin`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 07-ceasefire-withdrawal-and-records-siffin
- **Order**: 7
- **HistoricalFrame**: 657 CE; attributedchronicleaccount; geography=siffin; core=ceasefire-withdrawal-and-records
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/07-ceasefire-withdrawal-and-records-siffin: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S13 — Episodio 8: The Reply beside the Water
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/08-paired-protocol-delivery-siffin`, `docs/qa/house-of-ali/episodes/08-paired-protocol-delivery-siffin`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 08-paired-protocol-delivery-siffin
- **Order**: 8
- **HistoricalFrame**: 657 CE; geography=siffin; core=paired-protocol-delivery
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/08-paired-protocol-delivery-siffin: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S14 — Episodio 9: The Names in the Copied Terms
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/09-witness-and-text-comparison-kufa`, `docs/qa/house-of-ali/episodes/09-witness-and-text-comparison-kufa`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 09-witness-and-text-comparison-kufa
- **Order**: 9
- **HistoricalFrame**: 657/658 CE; geography=kufa; core=witness-and-text-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/09-witness-and-text-comparison-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S15 — Episodio 10: A House on the Harura Road
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/10-voluntary-household-relocation-harura`, `docs/qa/house-of-ali/episodes/10-voluntary-household-relocation-harura`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-2
- **ScenarioId**: 10-voluntary-household-relocation-harura
- **Order**: 10
- **HistoricalFrame**: 657/658 CE; Nahrawanlateroff-map; geography=harura; core=voluntary-household-relocation
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/10-voluntary-household-relocation-harura: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S16 — Episodio 11: Beyond the Canal's Silence
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/11-finite-civilian-withdrawal-and-care-nahrawan`, `docs/qa/house-of-ali/episodes/11-finite-civilian-withdrawal-and-care-nahrawan`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 11-finite-civilian-withdrawal-and-care-nahrawan
- **Order**: 11
- **HistoricalFrame**: 658 CE; geography=nahrawan; core=finite-civilian-withdrawal-and-care
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/11-finite-civilian-withdrawal-and-care-nahrawan: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S17 — Episodio 12: Reports from the Empty Seat
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/12-delegation-and-source-comparison-adhruh`, `docs/qa/house-of-ali/episodes/12-delegation-and-source-comparison-adhruh`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 12-delegation-and-source-comparison-adhruh
- **Order**: 12
- **HistoricalFrame**: 659 CE; geography=adhruh; core=delegation-and-source-comparison
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/12-delegation-and-source-comparison-adhruh: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S5 — Episodio 13: The Seal after Ali
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/03-the-sealed-copy`, `docs/qa/house-of-ali/episodes/03-the-sealed-copy`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 03-the-sealed-copy
- **Order**: 13
- **HistoricalFrame**: 661 CE; geography=kufa; core=administrative-transition-and-copying
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/03-the-sealed-copy: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S18 — Episodio 14: The Letter with Room for Terms
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/14-paired-protocol-and-negotiation-kufa`, `docs/qa/house-of-ali/episodes/14-paired-protocol-and-negotiation-kufa`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 14-paired-protocol-and-negotiation-kufa
- **Order**: 14
- **HistoricalFrame**: 661 CE; geography=kufa; core=paired-protocol-and-negotiation
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/14-paired-protocol-and-negotiation-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S19 — Episodio 15: The Oath That Changed the Road
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/15-finite-distribution-and-receipts-kufa`, `docs/qa/house-of-ali/episodes/15-finite-distribution-and-receipts-kufa`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 15-finite-distribution-and-receipts-kufa
- **Order**: 15
- **HistoricalFrame**: August661 approximate; geography=kufa; core=finite-distribution-and-receipts
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/15-finite-distribution-and-receipts-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S20 — Episodio 16: The Assembly's Last Account
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/16-ceremony-and-record-preservation-kufa`, `docs/qa/house-of-ali/episodes/16-ceremony-and-record-preservation-kufa`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-3
- **ScenarioId**: 16-ceremony-and-record-preservation-kufa
- **Order**: 16
- **HistoricalFrame**: 661 CE; publictransferattributed; geography=kufa; core=ceremony-and-record-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/16-ceremony-and-record-preservation-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S21 — Episodio 17: A Household Returned to Medina
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/17-returning-household-and-workshop-supply-medina`, `docs/qa/house-of-ali/episodes/17-returning-household-and-workshop-supply-medina`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 17-returning-household-and-workshop-supply-medina
- **Order**: 17
- **HistoricalFrame**: 661 CE; separatelocalreturn, notsecondtransfer; geography=medina; core=returning-household-and-workshop-supply
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/17-returning-household-and-workshop-supply-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S22 — Episodio 18: The Record after Hasan
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/18-mourning-and-witness-preservation-medina`, `docs/qa/house-of-ali/episodes/18-mourning-and-witness-preservation-medina`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 18-mourning-and-witness-preservation-medina
- **Order**: 18
- **HistoricalFrame**: 669/670 CE; disputeddateandpoisoningclaims; geography=medina; core=mourning-and-witness-preservation
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/18-mourning-and-witness-preservation-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S23 — Episodio 19: A New Name from Damascus
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/19-off-map-succession-dispatch-medina`, `docs/qa/house-of-ali/episodes/19-off-map-succession-dispatch-medina`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 19-off-map-succession-dispatch-medina
- **Order**: 19
- **HistoricalFrame**: 680 CE; YazidsuccessionDamascusreported; geography=medina; core=off-map-succession-dispatch
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/19-off-map-succession-dispatch-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S24 — Episodio 20: The Road out of Medina
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/20-finite-household-departure-medina`, `docs/qa/house-of-ali/episodes/20-finite-household-departure-medina`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 20-finite-household-departure-medina
- **Order**: 20
- **HistoricalFrame**: 680 CE; historicalfiguresoff-map; geography=medina; core=finite-household-departure
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/20-finite-household-departure-medina: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S25 — Episodio 21: Letters Reaching Mecca
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/21-two-way-correspondence-and-witnesses-mecca`, `docs/qa/house-of-ali/episodes/21-two-way-correspondence-and-witnesses-mecca`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 21-two-way-correspondence-and-witnesses-mecca
- **Order**: 21
- **HistoricalFrame**: June680 approximate; calendarconversionqualified; geography=mecca; core=two-way-correspondence-and-witnesses
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/21-two-way-correspondence-and-witnesses-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S26 — Episodio 22: The Emissary in Kufa
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/22-delegation-reception-and-support-records-kufa`, `docs/qa/house-of-ali/episodes/22-delegation-reception-and-support-records-kufa`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 22-delegation-reception-and-support-records-kufa
- **Order**: 22
- **HistoricalFrame**: 680 CE; geography=kufa; core=delegation-reception-and-support-records
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/22-delegation-reception-and-support-records-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S27 — Episodio 23: The City after the Arrests
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/23-civilian-refuge-and-record-extraction-kufa`, `docs/qa/house-of-ali/episodes/23-civilian-refuge-and-record-extraction-kufa`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-4
- **ScenarioId**: 23-civilian-refuge-and-record-extraction-kufa
- **Order**: 23
- **HistoricalFrame**: 680 CE; executionsreportednotplayergoal; geography=kufa; core=civilian-refuge-and-record-extraction
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/23-civilian-refuge-and-record-extraction-kufa: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio. Presenta el punto de inflexión del acto aprobado."

### S28 — Episodio 24: Before the News Could Catch the Road
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/24-finite-caravan-consignments-mecca`, `docs/qa/house-of-ali/episodes/24-finite-caravan-consignments-mecca`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 24-finite-caravan-consignments-mecca
- **Order**: 24
- **HistoricalFrame**: September680 approximate; exitdatevariants; geography=mecca; core=finite-caravan-consignments
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/24-finite-caravan-consignments-mecca: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S29 — Episodio 25: The Closed Roads of Qadisiyya
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/25-bounded-civilian-route-and-care-qadisiyya`, `docs/qa/house-of-ali/episodes/25-bounded-civilian-route-and-care-qadisiyya`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 25-bounded-civilian-route-and-care-qadisiyya
- **Order**: 25
- **HistoricalFrame**: 680 CE; geography=qadisiyya; core=bounded-civilian-route-and-care
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/25-bounded-civilian-route-and-care-qadisiyya: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S30 — Episodio 26: A Dispatch at Zubala
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/26-source-comparison-and-voluntary-return-zubala`, `docs/qa/house-of-ali/episodes/26-source-comparison-and-voluntary-return-zubala`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 26-source-comparison-and-voluntary-return-zubala
- **Order**: 26
- **HistoricalFrame**: 680 CE; Thalabiyyaseparatepriorreport, notsameplace; geography=zubala; core=source-comparison-and-voluntary-return
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/26-source-comparison-and-voluntary-return-zubala: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S31 — Episodio 27: Where the Road Turned Away
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/27-off-map-dispatch-and-route-replanning-qadisiyya`, `docs/qa/house-of-ali/episodes/27-off-map-dispatch-and-route-replanning-qadisiyya`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 27-off-map-dispatch-and-route-replanning-qadisiyya
- **Order**: 27
- **HistoricalFrame**: 680 CE; DhuHusamencounterreported, exactsiteunresolved; geography=qadisiyya; core=off-map-dispatch-and-route-replanning
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/27-off-map-dispatch-and-route-replanning-qadisiyya: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S32 — Episodio 28: The Camp on the Open Plain
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/28-finite-camp-and-household-provision-karbala`, `docs/qa/house-of-ali/episodes/28-finite-camp-and-household-provision-karbala`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 28-finite-camp-and-household-provision-karbala
- **Order**: 28
- **HistoricalFrame**: earlyOctober680 conventional; geography=karbala; core=finite-camp-and-household-provision
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/28-finite-camp-and-household-provision-karbala: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S33 — Episodio 29: Messages before the River Closed
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/29-separate-reception-and-record-escort-karbala`, `docs/qa/house-of-ali/episodes/29-separate-reception-and-record-escort-karbala`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 29-separate-reception-and-record-escort-karbala
- **Order**: 29
- **HistoricalFrame**: earlyOctober680 conventional; geography=karbala; core=separate-reception-and-record-escort
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/29-separate-reception-and-record-escort-karbala: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Episodio intermedio: no escribe final de campaña; muestra siguiente episodio."

### S6 — Episodio 30: The Water That Remains
- **Status**: pending
- **DependsOn**: [S2]
- **Files**: `staging/campaigns/house-of-ali/scenarios/04-the-water-that-remains`, `docs/qa/house-of-ali/episodes/04-the-water-that-remains`, `staging/campaigns/house-of-ali/campaign.json`
- **Gate**: e2e
- **Act**: act-5
- **ScenarioId**: 04-the-water-that-remains
- **Order**: 30
- **HistoricalFrame**: October680 conventional; battle262historicaloutcomeinfinale; geography=karbala; core=bounded-water-and-civilian-extraction
- acceptance:
  - "Materializar únicamente el expediente aprobado house-of-ali/04-the-water-that-remains: hechos y licencias acotados, geografía real 300–400, predicados AND/IDs/recibos/derrotas, economía y perfiles easy/standard/hard, EN/es-ES y secuencia común→persona. Reclamar también campaign.json para añadir exclusivamente claves de los 17 catálogos y referencias de medios/fuentes aprobadas de este episodio; conservar manifiesto de episodios, identidades y narradores ya cerrados. El lock de ese archivo serializa estas actualizaciones dentro de la campaña aunque el grafo permita elegir cualquier episodio preparado. Antes de reclamar, comprobar el paquete individual aprobado para fuentes y la referencia tipada de las operaciones usadas. Una referencia no es capacidad nativa: conservar explícitos exportación, terreno y QA de motor pendientes. Si el expediente o contrato de referencia falta, este slice no es ejecutable; no improvisarlo."
  - "Implementar sus 6–8 secundarios, al menos cuatro mecánicas y tres estrategias combinables: ventajas finitas/persistentes, pérdida opcional sin derrota principal, solvencia saltando todos y completando todos. QA específico, llegadas tempranas, bajas, doble cobro, guardado y navegación: adjuntar casos específicos y mantener ejecución nativa pendiente si aún no está acreditada. Este slice entrega fuentes; no certifica GAME VERIFIED ni altera operaciones para aparentarlo. Único episodio final: escribe la ruta elegida a1 preservando otras y recomienda el sucesor según elección; nunca exige predecesora ni autolanza campaña. Presenta el punto de inflexión del acto aprobado."

### S7 — Promoción conjunta y entrega acreditada
- **Status**: pending
- **DependsOn**: [S8, S9, S10, S3, S11, S4, S12, S13, S14, S15, S16, S17, S5, S18, S19, S20, S21, S22, S23, S24, S25, S26, S27, S28, S29, S30, S31, S32, S33, S6]
- **Files**: `staging/campaigns/house-of-ali`, `campaigns/house-of-ali`, `config/string-ids.lock.json`, `config/glossary.json`, `docs/qa/house-of-ali/delivery`
- **Gate**: e2e
- acceptance:
  - "Promover exactamente los 30 episodios en su orden aprobado, junto a IDs/glosario bajo propiedad conjunta. staging:check sin --partial, bun run validate y build/export/candidate según perfil acreditado; no renumerar IDs ni sustituir escenario por fixture."
  - "Evidencia de AoE2 por hash/build/locales/tres dificultades, objetivos opcionales ignorados/completos y performance. Calibración final pertenece al arquitecto/tester; revisión independiente, integración oficial y estados lingüísticos/media reales antes de release."

## acceptance

- 30 escenarios de esta odisea, cinco actos, cada slice y objetivo trazable al dossier aprobado.
- Gates por entrega reales: fuentes por episodio aprobado, promoción sólo con la odisea completa y sus pruebas nativas; sin atribuir a MiniMax decisiones históricas, geográficas o arquitectónicas.
- Independencia jugable, recomendaciones correctas, identidad estable, memoria acumulativa y progreso solo en el final efectivo.
- Predicados acreditados, 6–8 secundarios por episodio, solvencia de ambos extremos y QA medido; no aprobar por documentación estática.
