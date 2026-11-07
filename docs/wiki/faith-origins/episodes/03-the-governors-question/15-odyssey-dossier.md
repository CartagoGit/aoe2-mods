# 21. The Governor's Question

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `03-the-governors-question` · c. 112 CE · 380×380

## Historical frame and fixed outcome

EN: In Letters 10.96–97, Pliny asks Trajan about proceedings against accused Christians in Bithynia-Pontus and reports interrogation, punishments and practices attributed to those questioned. Trajan says not to seek them out and rejects anonymous accusations, while retaining punishment in proved cases. The correspondence is not a census or a decree of general religious liberty.

ES: En las cartas 10.96–97, Plinio consulta a Trajano sobre procesos contra acusados de cristianismo en Bitinia-Ponto e informa de interrogatorios, castigos y prácticas atribuidas a quienes fueron preguntados. Trajano dice que no se les busque y rechaza denuncias anónimas, manteniendo castigos en casos probados. La correspondencia no es un censo ni un decreto de libertad religiosa general.

EN: The fictional local filing party departed after its receipt. This is neither delivery of Pliny’s historical correspondence nor an acquittal, new imperial policy or proof of universal practice. The stated punishments and limitations remain features of the surviving exchange.

ES: El grupo ficticio de archivo local partió después de su recibo. Esto no es entrega de la correspondencia histórica de Plinio, una absolución, una política imperial nueva ni prueba de prácticas universales. Los castigos y límites expresados siguen perteneciendo al intercambio conservado.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 14,
      "episodeId": "03-the-governors-question",
      "order": 21,
      "selectedSourceUrl": "https://faculty.georgetown.edu/jod/texts/pliny.html",
      "consultedUrl": "https://faculty.georgetown.edu/jod/texts/pliny.html",
      "passage": "Pliny, Letters 10.96–97: Pliny asks Trajan how to handle accused Christians; reports morning meeting, ethical pledge, and meal; Trajan replies not to seek them out.",
      "supportedClaim": {
        "en": "Pliny asks Trajan about proceedings against accused Christians and reports their pre-dawn meeting and practices.",
        "es-ES": "Plinio consulta a Trajano sobre los procesos contra acusados de cristianismo e informa de sus reuniones antes del alba y prácticas."
      },
      "limitations": "Governor's correspondence, not a neutral ethnography; evidence is for Bithynia-Pontus, not a general empire-wide policy. c.112 is inferred from correspondence chronology.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://faculty.georgetown.edu/jod/texts/pliny.html",
      "passage": "Pliny, Letters10.96–97; architect read both complete displayed letters",
      "limitations": "Governor correspondence and attributed interrogated testimony, not neutral ethnography; executions/torture not playable choices. Trajan does not grant religious liberty or general uniform rules. Local Nicomedia activity and receipt are fiction, not an attested tribunal or emperor reply.",
      "consultationDate": "2026-10-13",
      "status": "architect read specified passages; independent approval pending"
    }
  ],
  "knowledgeBasis": {
    "speaker": "miriam-archive",
    "mode": "inherited letters and later sources",
    "noOmniscience": true
  }
}
```

## Main objectives and individual contracts

### o1 / phase-1

EN: Collect three distinct local procedure notes and bring them to the northern filing court.

ES: Recoge tres notas locales distintas de procedimiento y llévalas al patio septentrional de archivo.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "collected",
      "id": "req-1",
      "entities": [
        "faith-origins.03-the-governors-question.procedure-notes-1",
        "faith-origins.03-the-governors-question.procedure-notes-2",
        "faith-origins.03-the-governors-question.procedure-notes-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.03-the-governors-question.procedure-notes-1",
        "faith-origins.03-the-governors-question.procedure-notes-2",
        "faith-origins.03-the-governors-question.procedure-notes-3"
      ],
      "destinations": {
        "faith-origins.03-the-governors-question.procedure-notes-1": "faith-origins.03-the-governors-question.destination-2",
        "faith-origins.03-the-governors-question.procedure-notes-2": "faith-origins.03-the-governors-question.destination-2",
        "faith-origins.03-the-governors-question.procedure-notes-3": "faith-origins.03-the-governors-question.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three fictional procedure notes have arrived; no list of accused people was created.

ES: Han llegado tres notas ficticias de procedimiento; no se ha creado una lista de acusados.

EN: I copy questions here, not names for a prosecution.

ES: Aquí copio preguntas, no nombres para un proceso.

### o2 / phase-2

EN: Pay 40 wood and 20 gold once and create one local filing cover from the three collected notes.

ES: Paga una vez 40 de madera y 20 de oro y crea una cubierta local de archivo con las tres notas recogidas.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 40,
        "gold": 20
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.03-the-governors-question.destination-2"
      ],
      "allocations": {
        "faith-origins.03-the-governors-question.destination-2": {
          "wood": 40,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.03-the-governors-question.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "faith-origins.03-the-governors-question.procedure-notes-1",
        "faith-origins.03-the-governors-question.procedure-notes-2",
        "faith-origins.03-the-governors-question.procedure-notes-3"
      ],
      "outputEntities": [
        "faith-origins.03-the-governors-question.filing-cover-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.03-the-governors-question.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 40,
            "gold": 20
          },
          "newDebit": false
        }
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The local cover is created after its exact funded receipt.

ES: La cubierta local se ha creado tras su recibo financiado exacto.

EN: A careful filing cover is not an emperor’s order.

ES: Una cubierta de archivo cuidadosa no es una orden imperial.

### o3 / phase-3

EN: Bring the original filing cover and both original couriers alive to the eastern reception yard.

ES: Lleva la cubierta de archivo original y ambos correos originales con vida al patio receptor oriental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "faith-origins.03-the-governors-question.filing-cover-1"
      ],
      "destinations": {
        "faith-origins.03-the-governors-question.filing-cover-1": "faith-origins.03-the-governors-question.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.03-the-governors-question.onward-couriers-1",
        "faith-origins.03-the-governors-question.onward-couriers-2"
      ],
      "destinations": {
        "faith-origins.03-the-governors-question.onward-couriers-1": "faith-origins.03-the-governors-question.destination-3",
        "faith-origins.03-the-governors-question.onward-couriers-2": "faith-origins.03-the-governors-question.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The cover and both couriers are received; onward departure is now enabled.

ES: Se ha recibido la cubierta y a ambos correos; ahora se habilita su partida posterior.

EN: Only this arrival is in our account. No verdict has arrived with it.

ES: En nuestra cuenta solo consta esta llegada. Con ella no ha llegado ningún veredicto.

### o4 / phase-4

EN: After the reception receipt, depart with both same couriers and bring them alive to the onward inland station.

ES: Después del recibo de recepción, parte con ambos correos originales y llévalos con vida a la estación interior de continuación.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "ordered-departure",
      "departureEnabledOnlyAfterReceipt": true,
      "receiptObjective": "o3",
      "receiptRequirement": "req-1",
      "id": "req-1",
      "departingEntities": [
        "faith-origins.03-the-governors-question.onward-couriers-1",
        "faith-origins.03-the-governors-question.onward-couriers-2"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-1"
      },
      "id": "req-2",
      "entities": [
        "faith-origins.03-the-governors-question.onward-couriers-1",
        "faith-origins.03-the-governors-question.onward-couriers-2"
      ],
      "destinations": {
        "faith-origins.03-the-governors-question.onward-couriers-1": "faith-origins.03-the-governors-question.destination-4",
        "faith-origins.03-the-governors-question.onward-couriers-2": "faith-origins.03-the-governors-question.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The same two couriers departed after reception and reached the local onward station.

ES: Los mismos dos correos partieron después de la recepción y alcanzaron la estación local de continuación.

EN: The game can order these departures. History will not become tidier because it did.

ES: El juego puede ordenar estas partidas. Eso no hará que la historia sea más ordenada.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/03-the-governors-question.svg)

```json
{
  "bbox": [
    29.905,
    40.758,
    29.995,
    40.822
  ],
  "terrainProfile": "bithynia",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        129.34,
        194.47
      ],
      "lonLat": [
        29.934,
        40.789
      ],
      "name": {
        "en": "Local inland note court",
        "es-ES": "Patio interior local de notas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        181.98,
        85.21
      ],
      "lonLat": [
        29.948,
        40.811
      ],
      "name": {
        "en": "Northern filing court",
        "es-ES": "Patio septentrional de archivo"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        272.22,
        174.6
      ],
      "lonLat": [
        29.972,
        40.793
      ],
      "name": {
        "en": "Eastern reception yard",
        "es-ES": "Patio receptor oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        324.86,
        259.03
      ],
      "lonLat": [
        29.986,
        40.776
      ],
      "name": {
        "en": "Onward inland station",
        "es-ES": "Estación interior de continuación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "main",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "relief",
      "hubOrder": [
        "hub-1",
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "eastbound inland detour; no water crossing or industrial shore fill"
    }
  ],
  "terrainInstructions": "Fictional inland and north-shore districts near Nicomedia within Bithynia-Pontus. Gulf lies west/southwest, higher slopes north; main yards placed inland north of modern shoreline controls. No industrial fill, motorway, imperial fourth-century palace or inferred exact governor tribunal address. Rome and the imperial court remain off-map; no certainty about the location of Letters10.96–97 is assigned to these local yards. Audit ancient shore, slopes, actual footprints and local route passability.",
  "corridorStraightLengthsTiles": {
    "main": 347.79,
    "relief": 243.75
  },
  "interestSpacingTiles": [
    25,
    55
  ],
  "minimumUsableAreaFraction": 0.45,
  "activeAreaPolicy": "main districts, finite supply hinterland and six optional circuits; survey usable terrain, not rectangle area",
  "geometryStatus": "georeferenced proposal; neither raster/DEM nor native footprint/pathfinding certified",
  "geographicLayers": [
    {
      "assetId": "ne-odyssey-coastline",
      "interpretation": "modern regional shoreline control; not ancient harbor geometry"
    },
    {
      "assetId": "regional-rivers_lake_centerlines",
      "interpretation": "modern regional river controls where available; minor channels and ancient courses require separate evidence"
    }
  ],
  "schematicWaterControl": {
    "coordinates": [],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/03-the-governors-question.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.03-the-governors-question.procedure-notes-1",
      "role": "fictional-local-procedure-note",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.03-the-governors-question.procedure-notes-2",
      "role": "fictional-local-procedure-note",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.03-the-governors-question.procedure-notes-3",
      "role": "fictional-local-procedure-note",
      "initialHub": "hub-1",
      "offsetTiles": [
        -6,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.03-the-governors-question.filing-cover-1",
      "role": "fictional-local-filing-register",
      "initialHub": "hub-2",
      "offsetTiles": [
        -10,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.03-the-governors-question.onward-couriers-1",
      "role": "fictional-voluntary-courier",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.03-the-governors-question.onward-couriers-2",
      "role": "fictional-voluntary-courier",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.03-the-governors-question.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.03-the-governors-question.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.03-the-governors-question.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.03-the-governors-question.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    }
  ],
  "objectGroups": {
    "procedure-notes": [
      "faith-origins.03-the-governors-question.procedure-notes-1",
      "faith-origins.03-the-governors-question.procedure-notes-2",
      "faith-origins.03-the-governors-question.procedure-notes-3"
    ],
    "filing-cover": [
      "faith-origins.03-the-governors-question.filing-cover-1"
    ],
    "onward-couriers": [
      "faith-origins.03-the-governors-question.onward-couriers-1",
      "faith-origins.03-the-governors-question.onward-couriers-2"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.03-the-governors-question.onward-couriers-1",
        "faith-origins.03-the-governors-question.onward-couriers-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Procedural context notes / Notas de contexto del procedimiento

EN: Recover both separate copies from procedural context notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de notas de contexto del procedimiento y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Explain the correspondence’s qualifications without distributing an accused-person list.

ES: Explica los matices de la correspondencia sin distribuir una lista de acusados.

```json
{
  "id": "side-1",
  "kind": "copy",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "03-the-governors-question.side-1.entity-1",
          "03-the-governors-question.side-1.entity-2"
        ],
        "destinations": {
          "03-the-governors-question.side-1.entity-1": "03-the-governors-question.side-1.zone-1",
          "03-the-governors-question.side-1.entity-2": "03-the-governors-question.side-1.zone-1"
        },
        "requiredCount": 2,
        "aliveAtDelivery": true,
        "oncePerEntity": true,
        "noSubstitutes": true,
        "initialPlacementDoesNotCount": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "03-the-governors-question.side-1.entity-1",
        "role": "copy",
        "initialHub": "hub-3",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      },
      {
        "id": "03-the-governors-question.side-1.entity-2",
        "role": "copy",
        "initialHub": "hub-3",
        "offsetTiles": [
          -6,
          6
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "03-the-governors-question.side-1.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "unlock-context-and-hint",
      "target": "documented context and a main-goal hint",
      "resources": {},
      "onceFlag": "03-the-governors-question.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.03-the-governors-question"
      ],
      "historicalNote": {
        "en": "In Letters 10.96–97, Pliny asks Trajan about proceedings against accused Christians in Bithynia-Pontus and reports interrogation, punishments and practices attributed to those questioned. Trajan says not to seek them out and rejects anonymous accusations, while retaining punishment in proved cases. The correspondence is not a census or a decree of general religious liberty.",
        "es-ES": "En las cartas 10.96–97, Plinio consulta a Trajano sobre procesos contra acusados de cristianismo en Bitinia-Ponto e informa de interrogatorios, castigos y prácticas atribuidas a quienes fueron preguntados. Trajano dice que no se les busque y rechaza denuncias anónimas, manteniendo castigos en casos probados. La correspondencia no es un censo ni un decreto de libertad religiosa general."
      },
      "hint": {
        "en": "Collect three distinct local procedure notes and bring them to the northern filing court.",
        "es-ES": "Recoge tres notas locales distintas de procedimiento y llévalas al patio septentrional de archivo."
      }
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-3",
    "receivingHub": "hub-1",
    "corridorIds": [
      "main",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Independent inland households / Hogares interiores independientes

EN: Bring each of the two aid crates to its assigned household at independent inland households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares interiores independientes. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Help ordinary separate households without sacrificing, denouncing, converting or choosing who is executed.

ES: Ayuda a hogares ordinarios separados sin sacrificar, denunciar, convertir ni elegir ejecutados.

```json
{
  "id": "side-2",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "03-the-governors-question.side-2.entity-1",
          "03-the-governors-question.side-2.entity-2"
        ],
        "destinations": {
          "03-the-governors-question.side-2.entity-1": "03-the-governors-question.side-2.zone-1",
          "03-the-governors-question.side-2.entity-2": "03-the-governors-question.side-2.zone-2"
        },
        "requiredCount": 2,
        "aliveAtDelivery": true,
        "oncePerEntity": true,
        "noSubstitutes": true,
        "initialPlacementDoesNotCount": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "03-the-governors-question.side-2.entity-1",
        "role": "aid",
        "initialHub": "hub-1",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      },
      {
        "id": "03-the-governors-question.side-2.entity-2",
        "role": "aid",
        "initialHub": "hub-1",
        "offsetTiles": [
          -6,
          6
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "03-the-governors-question.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "03-the-governors-question.side-2.zone-2",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 100,
        "wood": 50
      },
      "onceFlag": "03-the-governors-question.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-1",
    "receivingHub": "hub-2",
    "corridorIds": [
      "main",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The north-road supply store / El almacén de provisiones del camino norte

EN: Pay 50 wood and restore the damaged store of the north-road supply store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el almacén de provisiones del camino norte. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: An ordinary finite workshop repair supports travel, not a Roman tribunal reconstruction.

ES: Reparar un taller ordinario y finito apoya el viaje, no reconstruye un tribunal romano.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "03-the-governors-question.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "03-the-governors-question.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "03-the-governors-question.side-3.payment",
        "afterArrival": false,
        "once": true,
        "protectedRecoveryCannotBeSpent": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "03-the-governors-question.side-3.entity-1",
        "role": "repair",
        "initialHub": "hub-2",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": false,
        "initialHealthFraction": 0.5,
        "damageSource": "fictional prior damage"
      }
    ],
    "zones": [
      {
        "id": "03-the-governors-question.side-3.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 200,
        "wood": 100
      },
      "onceFlag": "03-the-governors-question.side-3.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-2",
    "receivingHub": "hub-2",
    "corridorIds": [
      "main",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Coastal-road provisions / Provisiones del camino costero

EN: Escort the trader of coastal-road provisions to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de provisiones del camino costero hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A bounded voluntary exchange remains on the land side of the shore controls.

ES: Un intercambio voluntario limitado permanece en tierra respecto a los controles costeros.

```json
{
  "id": "side-4",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "03-the-governors-question.side-4.entity-1"
        ],
        "destinations": {
          "03-the-governors-question.side-4.entity-1": "03-the-governors-question.side-4.zone-1"
        },
        "requiredCount": 1,
        "aliveAtDelivery": true,
        "oncePerEntity": true,
        "noSubstitutes": true,
        "initialPlacementDoesNotCount": true
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "gold": 50
        },
        "receipt": "03-the-governors-question.side-4.payment",
        "afterArrival": true,
        "once": true,
        "protectedRecoveryCannotBeSpent": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "03-the-governors-question.side-4.entity-1",
        "role": "trade",
        "initialHub": "hub-1",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "03-the-governors-question.side-4.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 150,
        "wood": 50
      },
      "onceFlag": "03-the-governors-question.side-4.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-1",
    "receivingHub": "hub-2",
    "corridorIds": [
      "main",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Filing-road viewpoints / Miradores del camino de archivo

EN: Scout both marked viewpoints of filing-road viewpoints. Benefit: Mark the surveyed main land circuit once; main receiver markers and requirements remain available without it.

ES: Explora los dos miradores señalados de miradores del camino de archivo. Ventaja: Señala una vez el circuito terrestre trazado main; los receptores principales y sus requisitos siguen disponibles sin él.

EN: Observe actual local land circuits; no supposed imperial reply is unlocked.

ES: Observa circuitos terrestres locales reales; no desbloquea una supuesta respuesta imperial.

```json
{
  "id": "side-5",
  "kind": "scout",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "visit-zones",
        "zones": [
          "03-the-governors-question.side-5.zone-1",
          "03-the-governors-question.side-5.zone-2"
        ],
        "actor": "any-player-controlled-unit",
        "requiredCount": 2,
        "observationsPersistent": true,
        "countInitialVisibility": false
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [],
    "zones": [
      {
        "id": "03-the-governors-question.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "03-the-governors-question.side-5.zone-2",
        "hub": "hub-3",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "mark-alternative-route",
      "target": "main surveyed land circuit",
      "resources": {},
      "onceFlag": "03-the-governors-question.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "main"
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-3",
    "receivingHub": "hub-2",
    "corridorIds": [
      "main",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The inland onward guide / El guía interior de continuación

EN: Escort the local guide of the inland onward guide to the marked road junction. Benefit: Mark the surveyed relief land circuit once; main receiver markers and requirements remain available without it.

ES: Escolta al guía local de el guía interior de continuación hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado relief; los receptores principales y sus requisitos siguen disponibles sin él.

EN: Marks a known land detour without bypassing the main receipt gate.

ES: Señala un desvío terrestre conocido sin saltarse el recibo principal.

```json
{
  "id": "side-6",
  "kind": "guide",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "03-the-governors-question.side-6.entity-1"
        ],
        "destinations": {
          "03-the-governors-question.side-6.entity-1": "03-the-governors-question.side-6.zone-1"
        },
        "requiredCount": 1,
        "aliveAtDelivery": true,
        "oncePerEntity": true,
        "noSubstitutes": true,
        "initialPlacementDoesNotCount": true
      }
    ],
    "neverUseTimerInstead": true
  },
  "world": {
    "entities": [
      {
        "id": "03-the-governors-question.side-6.entity-1",
        "role": "guide",
        "initialHub": "hub-1",
        "offsetTiles": [
          -6,
          3
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "03-the-governors-question.side-6.zone-1",
        "hub": "hub-3",
        "offsetTiles": [
          8,
          0
        ],
        "radiusTiles": 3
      }
    ]
  },
  "effects": [
    {
      "kind": "mark-alternative-route",
      "target": "relief surveyed land circuit",
      "resources": {},
      "onceFlag": "03-the-governors-question.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "relief"
    }
  ],
  "stateContract": {
    "states": [
      "available",
      "completed",
      "failed-optional",
      "closed-at-terminal"
    ],
    "requiresNonterminalScenario": true,
    "persistentAcrossSave": true,
    "completionAndEffectsAtomic": true,
    "paymentBeforeReward": true,
    "paymentIsNotCompletion": true,
    "failedGoalCannotReward": true,
    "latchAtFirstCompletion": true,
    "noMainVictoryDependency": true,
    "rewardTransaction": [
      "verify all predicate ledgers and nonterminal state",
      "verify reserved stock",
      "debit reserved stock",
      "credit spendable stock",
      "set reward onceFlag",
      "set completionFlag"
    ],
    "transactionIsolation": "all-or-nothing in one native guarded operation; duplicate/reloaded completion does nothing",
    "persistentLedgers": [
      "visited-zone IDs",
      "delivered-entity IDs",
      "payment receipt",
      "reserved-stock remainder",
      "reward onceFlag",
      "completionFlag",
      "failed-optional flag"
    ],
    "terminalPriority": "main defeat/victory closes side actions first; never credit after terminal"
  },
  "reachability": {
    "originHub": "hub-1",
    "receivingHub": "hub-3",
    "corridorIds": [
      "main",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

```json
{
  "secondaryBudget": {
    "reservedRewards": {
      "food": 450,
      "wood": 200,
      "gold": 0,
      "stone": 0
    },
    "maxOptionalCosts": {
      "food": 0,
      "wood": 50,
      "gold": 50,
      "stone": 0
    },
    "reallocatedCacheAllowance": {
      "food": 600,
      "wood": 300,
      "gold": 150,
      "stone": 0
    },
    "fundingPolicy": "reward stock is segregated from the finite total bank; no duplicate caches",
    "nativeStatus": "design-only; requires certified reusable predicates and native QA"
  },
  "playstyles": [
    {
      "id": "context-and-patient-departure",
      "optionalObjectives": [
        "side-1",
        "side-5"
      ],
      "costOfOpportunity": "Read attributed evidence and survey while filing finishes; early courier dispatch cannot bypass the receipt.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "workshop-and-provisions",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Spend bounded optional supply costs while the 40wood20gold main payment remains reserved.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "household-and-inland-guide",
      "optionalObjectives": [
        "side-2",
        "side-6"
      ],
      "costOfOpportunity": "Combine independent care and known inland guidance; the imperial legal outcome is never a player reward.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    }
  ]
}
```

## Three difficulty budgets and limits

```json
{
  "easy": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 402,
      "wood": 172,
      "gold": 86,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1118,
      "wood": 748,
      "gold": 224,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 40,
      "gold": 20,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 300,
      "wood": 200,
      "gold": 100,
      "stone": 0
    },
    "replacementBudget": {
      "food": 120,
      "wood": 80,
      "gold": 40,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 1070,
      "wood": 720,
      "gold": 310,
      "stone": 100
    },
    "maxVillagers": 12,
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      30,
      55
    ],
    "difficultyLevers": "12 workers; fully marked route; independent pickups can be completed in any order.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  },
  "standard": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 350,
      "wood": 150,
      "gold": 75,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1170,
      "wood": 770,
      "gold": 235,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 40,
      "gold": 20,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 300,
      "wood": 200,
      "gold": 100,
      "stone": 0
    },
    "replacementBudget": {
      "food": 120,
      "wood": 80,
      "gold": 40,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 1070,
      "wood": 720,
      "gold": 310,
      "stone": 100
    },
    "maxVillagers": 9,
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      35,
      65
    ],
    "difficultyLevers": "9 workers; geographic approach markers with local fog; plan deliveries and gathering in parallel.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  },
  "hard": {
    "basis": "static feasibility estimate; native calibration and fun/playability assessment pending",
    "startingResources": {
      "food": 297,
      "wood": 127,
      "gold": 63,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1223,
      "wood": 793,
      "gold": 247,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 40,
      "gold": 20,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 300,
      "wood": 200,
      "gold": 100,
      "stone": 0
    },
    "replacementBudget": {
      "food": 120,
      "wood": 80,
      "gold": 40,
      "stone": 0
    },
    "supplyMargins": {
      "food": 650,
      "wood": 400,
      "gold": 150,
      "stone": 100
    },
    "accessibleWithoutOptionalRewards": {
      "food": 1070,
      "wood": 720,
      "gold": 310,
      "stone": 100
    },
    "maxVillagers": 6,
    "enemyTotalCap": 0,
    "enemyProduction": false,
    "regeneratingResources": false,
    "roughDurationMinutes": [
      40,
      75
    ],
    "difficultyLevers": "6 workers; fewer initial supplies; all essential receiving zones and costs remain disclosed; no invented hostile army or secret deadline.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.faith-origins.03-the-governors-question.odyssey.title / always | none | The Governor's Question | La pregunta del gobernador |
| scenario.faith-origins.03-the-governors-question.odyssey.fact-intro / intro first | collection-narrator | In Letters 10.96–97, Pliny asks Trajan about proceedings against accused Christians in Bithynia-Pontus and reports interrogation, punishments and practices attributed to those questioned. Trajan says not to seek them out and rejects anonymous accusations, while retaining punishment in proved cases. The correspondence is not a census or a decree of general religious liberty. | En las cartas 10.96–97, Plinio consulta a Trajano sobre procesos contra acusados de cristianismo en Bitinia-Ponto e informa de interrogatorios, castigos y prácticas atribuidas a quienes fueron preguntados. Trajano dice que no se les busque y rechaza denuncias anónimas, manteniendo castigos en casos probados. La correspondencia no es un censo ni un decreto de libertad religiosa general. |
| scenario.faith-origins.03-the-governors-question.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.03-the-governors-question.odyssey.persona-intro / after handover | miriam-archive | The governor’s own uncertainty troubles me more than a neat summary would. I was born long after his questions. I can read what he admits, but not supply a private answer for the people whose voices passed through his interrogation. | La incertidumbre del propio gobernador me inquieta más que un resumen ordenado. Nací mucho después de sus preguntas. Puedo leer lo que admite, pero no poner una respuesta privada en boca de quienes pasaron por su interrogatorio. |
| scenario.faith-origins.03-the-governors-question.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.03-the-governors-question.odyssey.route-help / available from start; repeatable without effect | none | Gather the three local procedure notes, pay for one filing cover, and stage that cover and both couriers at the eastern reception yard. Their onward departure opens only after the local arrival receipt; it is not Trajan’s reply or a pardon. All local paths remain inland. | Reúne las tres notas locales de procedimiento, paga una cubierta de archivo y prepara esa cubierta y ambos correos en el patio receptor oriental. Su partida posterior solo se habilita tras el recibo local de llegada; no es la respuesta de Trajano ni un indulto. Todas las rutas locales permanecen en tierra interior. |
| scenario.faith-origins.03-the-governors-question.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.o1-goal / phase-1 active | none | Collect three distinct local procedure notes and bring them to the northern filing court. | Recoge tres notas locales distintas de procedimiento y llévalas al patio septentrional de archivo. |
| scenario.faith-origins.03-the-governors-question.odyssey.o1-receipt / o1 latched once | none | Three fictional procedure notes have arrived; no list of accused people was created. | Han llegado tres notas ficticias de procedimiento; no se ha creado una lista de acusados. |
| scenario.faith-origins.03-the-governors-question.odyssey.o1-reaction / after o1 receipt | miriam-archive | I copy questions here, not names for a prosecution. | Aquí copio preguntas, no nombres para un proceso. |
| scenario.faith-origins.03-the-governors-question.odyssey.o2-goal / phase-2 active | none | Pay 40 wood and 20 gold once and create one local filing cover from the three collected notes. | Paga una vez 40 de madera y 20 de oro y crea una cubierta local de archivo con las tres notas recogidas. |
| scenario.faith-origins.03-the-governors-question.odyssey.o2-receipt / o2 latched once | none | The local cover is created after its exact funded receipt. | La cubierta local se ha creado tras su recibo financiado exacto. |
| scenario.faith-origins.03-the-governors-question.odyssey.o2-reaction / after o2 receipt | miriam-archive | A careful filing cover is not an emperor’s order. | Una cubierta de archivo cuidadosa no es una orden imperial. |
| scenario.faith-origins.03-the-governors-question.odyssey.o3-goal / phase-3 active | none | Bring the original filing cover and both original couriers alive to the eastern reception yard. | Lleva la cubierta de archivo original y ambos correos originales con vida al patio receptor oriental. |
| scenario.faith-origins.03-the-governors-question.odyssey.o3-receipt / o3 latched once | none | The cover and both couriers are received; onward departure is now enabled. | Se ha recibido la cubierta y a ambos correos; ahora se habilita su partida posterior. |
| scenario.faith-origins.03-the-governors-question.odyssey.o3-reaction / after o3 receipt | miriam-archive | Only this arrival is in our account. No verdict has arrived with it. | En nuestra cuenta solo consta esta llegada. Con ella no ha llegado ningún veredicto. |
| scenario.faith-origins.03-the-governors-question.odyssey.o4-goal / phase-4 active | none | After the reception receipt, depart with both same couriers and bring them alive to the onward inland station. | Después del recibo de recepción, parte con ambos correos originales y llévalos con vida a la estación interior de continuación. |
| scenario.faith-origins.03-the-governors-question.odyssey.o4-receipt / o4 latched once | none | The same two couriers departed after reception and reached the local onward station. | Los mismos dos correos partieron después de la recepción y alcanzaron la estación local de continuación. |
| scenario.faith-origins.03-the-governors-question.odyssey.o4-reaction / after o4 receipt | miriam-archive | The game can order these departures. History will not become tidier because it did. | El juego puede ordenar estas partidas. Eso no hará que la historia sea más ordenada. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from procedural context notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de notas de contexto del procedimiento y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-1-complete / side-1 completed | none | Procedural context notes completed. Its stated benefit has been granted once. | Notas de contexto del procedimiento: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-1-lost / side-1 failed-optional | none | Procedural context notes is unavailable after the loss of its unique participant or object. The main mission continues. | Notas de contexto del procedimiento: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at independent inland households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares interiores independientes. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-2-complete / side-2 completed | none | Independent inland households completed. Its stated benefit has been granted once. | Hogares interiores independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-2-lost / side-2 failed-optional | none | Independent inland households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares interiores independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the north-road supply store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el almacén de provisiones del camino norte. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-3-complete / side-3 completed | none | The north-road supply store completed. Its stated benefit has been granted once. | El almacén de provisiones del camino norte: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-3-lost / side-3 failed-optional | none | The north-road supply store is unavailable after the loss of its unique participant or object. The main mission continues. | El almacén de provisiones del camino norte: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-4-goal / optional list from start | none | Escort the trader of coastal-road provisions to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de provisiones del camino costero hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-4-complete / side-4 completed | none | Coastal-road provisions completed. Its stated benefit has been granted once. | Provisiones del camino costero: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-4-lost / side-4 failed-optional | none | Coastal-road provisions is unavailable after the loss of its unique participant or object. The main mission continues. | Provisiones del camino costero: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of filing-road viewpoints. Benefit: Mark the surveyed main land circuit once; main receiver markers and requirements remain available without it. | Explora los dos miradores señalados de miradores del camino de archivo. Ventaja: Señala una vez el circuito terrestre trazado main; los receptores principales y sus requisitos siguen disponibles sin él. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-5-complete / side-5 completed | none | Filing-road viewpoints completed. Its stated benefit has been granted once. | Miradores del camino de archivo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-5-lost / side-5 failed-optional | none | Filing-road viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores del camino de archivo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the inland onward guide to the marked road junction. Benefit: Mark the surveyed relief land circuit once; main receiver markers and requirements remain available without it. | Escolta al guía local de el guía interior de continuación hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado relief; los receptores principales y sus requisitos siguen disponibles sin él. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-6-complete / side-6 completed | none | The inland onward guide completed. Its stated benefit has been granted once. | El guía interior de continuación: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.03-the-governors-question.odyssey.side-6-lost / side-6 failed-optional | none | The inland onward guide is unavailable after the loss of its unique participant or object. The main mission continues. | El guía interior de continuación: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.03-the-governors-question.odyssey.fact-outro / victory first | collection-narrator | The fictional local filing party departed after its receipt. This is neither delivery of Pliny’s historical correspondence nor an acquittal, new imperial policy or proof of universal practice. The stated punishments and limitations remain features of the surviving exchange. | El grupo ficticio de archivo local partió después de su recibo. Esto no es entrega de la correspondencia histórica de Plinio, una absolución, una política imperial nueva ni prueba de prácticas universales. Los castigos y límites expresados siguen perteneciendo al intercambio conservado. |
| scenario.faith-origins.03-the-governors-question.odyssey.persona-outro / after fact-outro | miriam-archive | A receipt can show that a packet arrived. It cannot make the frightened person in a governor’s report feel safe. I keep those two kinds of certainty on different shelves. | Un recibo puede mostrar que llegó un paquete. No puede hacer sentirse a salvo a la persona atemorizada de un informe del gobernador. Guardo esas dos certezas en estantes diferentes. |
| scenario.faith-origins.03-the-governors-question.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.03-the-governors-question.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.03-the-governors-question.odyssey.next-episode / after persona-outro | none | Continue with Bread Read Aloud. This episode does not complete the campaign. | Continúa con Pan leído en voz alta. Este episodio no termina la campaña. |
| scenario.faith-origins.03-the-governors-question.odyssey.act-turning-point / after next-episode | collection-narrator | The next act turns from a governor’s correspondence to accounts of reading, relief and public appeals in several regions. A change of document and viewpoint does not imply a single empire-wide policy shift. | El siguiente acto pasa de la correspondencia de un gobernador a relatos de lectura, auxilio y llamamientos públicos en varias regiones. Cambiar de documento y perspectiva no implica un giro político único en todo el imperio. |

## Production, recovery and verification

```json
{
  "stateMachine": {
    "states": [
      "briefing",
      "phase-1",
      "phase-2",
      "phase-3",
      "phase-4",
      "victory",
      "defeat"
    ],
    "phaseTransitions": [
      {
        "from": "briefing",
        "to": "phase-1",
        "on": "intro-accepted"
      },
      {
        "from": "phase-1",
        "to": "phase-2",
        "on": "objective-latched",
        "objectiveId": "o1"
      },
      {
        "from": "phase-2",
        "to": "phase-3",
        "on": "objective-latched",
        "objectiveId": "o2"
      },
      {
        "from": "phase-3",
        "to": "phase-4",
        "on": "objective-latched",
        "objectiveId": "o3"
      },
      {
        "from": "phase-4",
        "to": "victory",
        "on": "objective-latched",
        "objectiveId": "o4"
      }
    ],
    "terminalPriority": "defeat first; close side rewards; one terminal latch",
    "saveLoad": "persist object identities, arrivals, collected facts, receipts, phase elapsed time and side reward balances",
    "campaignProgressWrite": false
  },
  "failureRecovery": {
    "mainIdentityLoss": "explicitly irrecoverable main-object loss causes defeat; survivor groups tolerate only their declared loss margin",
    "optionalIdentityLoss": "only corresponding task becomes failed-optional",
    "recoveryImplementation": "inventory/replacement capability pending; reserved resources alone cannot resurrect an identity"
  },
  "requiredCapabilities": [
    {
      "id": "composed-world-ledger",
      "status": "reference model implemented; native implementation pending"
    },
    {
      "id": "geographic-land-corridors",
      "status": "real-world plan authored; DEM/footprints/pathfinding pending"
    },
    {
      "id": "two-narrator-sequence",
      "status": "caption text authored; certified native SequenceItems pending"
    },
    {
      "id": "receipt-gated-ordered-departure",
      "status": "reference model implemented; native actor departure/arrival observation, district binding and early-arrival semantics pending"
    },
    {
      "id": "arrival-after-exact-departure",
      "status": "reference guard implemented in 5cf2604 and 5d9d6ab / d787a8d9, including causal recipient ledgers and generated receipt entitlements; native departure/arrival observers and routing still pending"
    }
  ],
  "artDirection": {
    "style": "sober Roman-era regional illustration; own geographic vector plan as research visual",
    "historicalControls": "no modern objects, invented quotation, sacred-person combat unit or later religious architecture",
    "referenceAssets": [],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "couriers cannot depart before o3 actual arrival receipt",
      "one courier duplicated cannot count as two",
      "departure after wrong objective receipt blocked",
      "same two staged couriers must reach onward station",
      "early final arrival cannot satisfy a later departure requirement",
      "no Roman office address inferred from correspondence",
      "no indefinite empirewide persecution or liberty claim",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
