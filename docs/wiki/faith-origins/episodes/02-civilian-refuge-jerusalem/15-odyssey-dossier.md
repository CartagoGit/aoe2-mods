# 2. When the City Held Its Breath

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `02-civilian-refuge-jerusalem` · c. 30–33 CE · 340×340

## Historical frame and fixed outcome

EN: Tacitus, writing decades later, reports the execution of Christus under Tiberius by Pontius Pilate. The conventional dating around 30–33 is reconstructed. The households and refuge journey here are fictional.

ES: Tácito, décadas después, informa de la ejecución de Christus bajo Tiberio por Poncio Pilato. La fecha convencional hacia 30–33 es una reconstrucción. Los hogares y su traslado al refugio son ficticios.

EN: Local success changes no documented execution and proves no ancient refuge operation. The historical account and the fictional household task remain separate.

ES: El éxito local no cambia la ejecución documentada ni demuestra una operación antigua de refugio. El relato histórico y la tarea doméstica ficticia siguen separados.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 25,
      "episodeId": "02-civilian-refuge-jerusalem",
      "order": 2,
      "selectedSourceUrl": "https://www.perseus.tufts.edu/hopper/text?doc=Tac.+Ann.+15.44",
      "consultedUrl": "https://dcc.dickinson.edu/tacitus-annals/15-44",
      "passage": "Tacitus, Annals 15.44, passage on Christus and the Neronian punishments; DCC notes distinguish Tacitus' report from other evidence and observe Christian sources do not mention an arson charge.",
      "supportedClaim": {
        "en": "Tacitus, writing decades later, says Christus was executed under Tiberius by Pontius Pilate. The passage does not place the execution in a specific year or record a refuge episode.",
        "es-ES": "Tácito, décadas después, dice que Christus fue ejecutado bajo Tiberio por Poncio Pilato. El pasaje no fija un año concreto ni registra un episodio de refugio."
      },
      "limitations": "Retrospective Roman literary testimony, not eyewitness evidence. The 30–33 date is a modern estimate; the episode candidate's 'Christian sources' wording should cite those separately if retained.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
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

EN: Bring at least six of the same eight households to the southern receiving court alive.

ES: Lleva con vida al menos seis de los mismos ocho hogares al patio receptor del sur.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "faith-origins.02-civilian-refuge-jerusalem.households-1",
        "faith-origins.02-civilian-refuge-jerusalem.households-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-4",
        "faith-origins.02-civilian-refuge-jerusalem.households-5",
        "faith-origins.02-civilian-refuge-jerusalem.households-6",
        "faith-origins.02-civilian-refuge-jerusalem.households-7",
        "faith-origins.02-civilian-refuge-jerusalem.households-8"
      ],
      "destinations": {
        "faith-origins.02-civilian-refuge-jerusalem.households-1": "faith-origins.02-civilian-refuge-jerusalem.destination-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-2": "faith-origins.02-civilian-refuge-jerusalem.destination-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-3": "faith-origins.02-civilian-refuge-jerusalem.destination-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-4": "faith-origins.02-civilian-refuge-jerusalem.destination-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-5": "faith-origins.02-civilian-refuge-jerusalem.destination-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-6": "faith-origins.02-civilian-refuge-jerusalem.destination-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-7": "faith-origins.02-civilian-refuge-jerusalem.destination-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-8": "faith-origins.02-civilian-refuge-jerusalem.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true,
  "exportedLedgers": [
    {
      "id": "received-households",
      "operator": "intersection",
      "fromRequirements": [
        "req-1"
      ],
      "minimumCount": 6
    }
  ]
}
```

EN: Six distinct household arrivals are required; repeated entries do not add families.

ES: Se requieren seis llegadas de hogares distintos; repetir entradas no añade familias.

EN: Keep their names, even when a number would be easier.

ES: Conserva sus nombres, aunque un número resulte más cómodo.

### o2 / phase-2

EN: Deliver a single total of 240 food to the receiving court.

ES: Entrega un único total de 240 de alimento en el patio receptor.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 240
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.02-civilian-refuge-jerusalem.destination-2"
      ],
      "allocations": {
        "faith-origins.02-civilian-refuge-jerusalem.destination-2": {
          "food": 240
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.02-civilian-refuge-jerusalem.o2.req-1.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The 240-food receipt is paid once.

ES: El recibo de 240 de alimento se paga una vez.

EN: A receipt is dull until someone must eat.

ES: Un recibo resulta gris hasta que alguien necesita comer.

### o3 / phase-3

EN: Bring at least six supplied households to the southern road refuge alive; use the arrival ledger from the court.

ES: Lleva con vida al menos seis hogares abastecidos al refugio del camino sur; utiliza el registro de llegada del patio.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o1",
        "ledger": "received-households"
      },
      "id": "req-1",
      "entities": [
        "faith-origins.02-civilian-refuge-jerusalem.households-1",
        "faith-origins.02-civilian-refuge-jerusalem.households-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-4",
        "faith-origins.02-civilian-refuge-jerusalem.households-5",
        "faith-origins.02-civilian-refuge-jerusalem.households-6",
        "faith-origins.02-civilian-refuge-jerusalem.households-7",
        "faith-origins.02-civilian-refuge-jerusalem.households-8"
      ],
      "destinations": {
        "faith-origins.02-civilian-refuge-jerusalem.households-1": "faith-origins.02-civilian-refuge-jerusalem.destination-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-2": "faith-origins.02-civilian-refuge-jerusalem.destination-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-3": "faith-origins.02-civilian-refuge-jerusalem.destination-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-4": "faith-origins.02-civilian-refuge-jerusalem.destination-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-5": "faith-origins.02-civilian-refuge-jerusalem.destination-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-6": "faith-origins.02-civilian-refuge-jerusalem.destination-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-7": "faith-origins.02-civilian-refuge-jerusalem.destination-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-8": "faith-origins.02-civilian-refuge-jerusalem.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Only households recorded at the receiving court may count at the final refuge.

ES: Solo cuentan en el refugio final los hogares registrados en el patio receptor.

EN: They are the same people at both gates. A ledger must remember that.

ES: Son las mismas personas en ambas puertas. Un registro debe recordarlo.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/02-civilian-refuge-jerusalem.svg)

```json
{
  "bbox": [
    35.12,
    31.7,
    35.3,
    31.86
  ],
  "terrainProfile": "jerusalem",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        182.36,
        148.69
      ],
      "lonLat": [
        35.218,
        31.791
      ],
      "name": {
        "en": "Western household district",
        "es-ES": "Barrio doméstico occidental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        200.05,
        197.88
      ],
      "lonLat": [
        35.229,
        31.765
      ],
      "name": {
        "en": "Southern receiving court",
        "es-ES": "Patio receptor meridional"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        201.66,
        237.6
      ],
      "lonLat": [
        35.23,
        31.744
      ],
      "name": {
        "en": "Southern road refuge",
        "es-ES": "Refugio del camino sur"
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
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "relief",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "alternative surveyed land access in the same districts; exact intermediate geometry pending, never invent a crossing"
    }
  ],
  "terrainInstructions": "Limestone plateau, southern ravines and eastern ridge. No navigable Kidron river, no Dome of the Rock or Ottoman walls. Household compounds are fictitious and avoid sacred platforms.",
  "mainRouteLengthStraightTiles": 92.03,
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
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/02-civilian-refuge-jerusalem.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.households-1",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.households-2",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.households-3",
      "role": "fictional-family-group",
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
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.households-4",
      "role": "fictional-family-group",
      "initialHub": "hub-1",
      "offsetTiles": [
        -4,
        8
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.households-5",
      "role": "fictional-family-group",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.households-6",
      "role": "fictional-family-group",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.households-7",
      "role": "fictional-family-group",
      "initialHub": "hub-1",
      "offsetTiles": [
        -6,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.households-8",
      "role": "fictional-family-group",
      "initialHub": "hub-1",
      "offsetTiles": [
        -4,
        10
      ],
      "identity": "explicitly fictional gameplay identity",
      "finite": true,
      "replacement": "none; no free resurrection",
      "initiallyDelivered": false,
      "originRule": "separate pickup position outside every receiving zone",
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.02-civilian-refuge-jerusalem.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    }
  ],
  "objectGroups": {
    "households": [
      "faith-origins.02-civilian-refuge-jerusalem.households-1",
      "faith-origins.02-civilian-refuge-jerusalem.households-2",
      "faith-origins.02-civilian-refuge-jerusalem.households-3",
      "faith-origins.02-civilian-refuge-jerusalem.households-4",
      "faith-origins.02-civilian-refuge-jerusalem.households-5",
      "faith-origins.02-civilian-refuge-jerusalem.households-6",
      "faith-origins.02-civilian-refuge-jerusalem.households-7",
      "faith-origins.02-civilian-refuge-jerusalem.households-8"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.02-civilian-refuge-jerusalem.households-1",
        "faith-origins.02-civilian-refuge-jerusalem.households-2",
        "faith-origins.02-civilian-refuge-jerusalem.households-3",
        "faith-origins.02-civilian-refuge-jerusalem.households-4",
        "faith-origins.02-civilian-refuge-jerusalem.households-5",
        "faith-origins.02-civilian-refuge-jerusalem.households-6",
        "faith-origins.02-civilian-refuge-jerusalem.households-7",
        "faith-origins.02-civilian-refuge-jerusalem.households-8"
      ],
      "minimumAliveOrAlreadySafe": 6
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Unlisted neighbors / Vecinos sin registrar

EN: Bring each of the two aid crates to its assigned household at unlisted neighbors. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en vecinos sin registrar. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid remains independent of the eight main households.

ES: El auxilio es independiente de los ocho hogares principales.

```json
{
  "id": "side-1",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "02-civilian-refuge-jerusalem.side-1.entity-1",
          "02-civilian-refuge-jerusalem.side-1.entity-2"
        ],
        "destinations": {
          "02-civilian-refuge-jerusalem.side-1.entity-1": "02-civilian-refuge-jerusalem.side-1.zone-1",
          "02-civilian-refuge-jerusalem.side-1.entity-2": "02-civilian-refuge-jerusalem.side-1.zone-2"
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
        "id": "02-civilian-refuge-jerusalem.side-1.entity-1",
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
        "id": "02-civilian-refuge-jerusalem.side-1.entity-2",
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
        "id": "02-civilian-refuge-jerusalem.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "02-civilian-refuge-jerusalem.side-1.zone-2",
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
      "onceFlag": "02-civilian-refuge-jerusalem.side-1.rewarded",
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

### Names on two scraps / Nombres en dos fragmentos

EN: Recover both separate copies from names on two scraps and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de nombres en dos fragmentos y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Preserves fictional household records.

ES: Conserva registros domésticos ficticios.

```json
{
  "id": "side-2",
  "kind": "copy",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "02-civilian-refuge-jerusalem.side-2.entity-1",
          "02-civilian-refuge-jerusalem.side-2.entity-2"
        ],
        "destinations": {
          "02-civilian-refuge-jerusalem.side-2.entity-1": "02-civilian-refuge-jerusalem.side-2.zone-1",
          "02-civilian-refuge-jerusalem.side-2.entity-2": "02-civilian-refuge-jerusalem.side-2.zone-1"
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
        "id": "02-civilian-refuge-jerusalem.side-2.entity-1",
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
        "id": "02-civilian-refuge-jerusalem.side-2.entity-2",
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
        "id": "02-civilian-refuge-jerusalem.side-2.zone-1",
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
      "onceFlag": "02-civilian-refuge-jerusalem.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.02-civilian-refuge-jerusalem"
      ],
      "historicalNote": {
        "en": "Tacitus, writing decades later, reports the execution of Christus under Tiberius by Pontius Pilate. The conventional dating around 30–33 is reconstructed. The households and refuge journey here are fictional.",
        "es-ES": "Tácito, décadas después, informa de la ejecución de Christus bajo Tiberio por Poncio Pilato. La fecha convencional hacia 30–33 es una reconstrucción. Los hogares y su traslado al refugio son ficticios."
      },
      "hint": {
        "en": "Bring at least six of the same eight households to the southern receiving court alive.",
        "es-ES": "Lleva con vida al menos seis de los mismos ocho hogares al patio receptor del sur."
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

### Refuge store roof / Techo del almacén del refugio

EN: Pay 50 wood and restore the damaged store of refuge store roof to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de techo del almacén del refugio. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repairs a fictional receiving store.

ES: Repara un almacén receptor ficticio.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "02-civilian-refuge-jerusalem.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "02-civilian-refuge-jerusalem.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "02-civilian-refuge-jerusalem.side-3.payment",
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
        "id": "02-civilian-refuge-jerusalem.side-3.entity-1",
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
        "id": "02-civilian-refuge-jerusalem.side-3.zone-1",
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
      "onceFlag": "02-civilian-refuge-jerusalem.side-3.rewarded",
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

### Olive road trader / Comerciante del camino de los olivos

EN: Escort the trader of olive road trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de comerciante del camino de los olivos hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Finite consignment supports the refuge.

ES: Una remesa finita ayuda al refugio.

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
          "02-civilian-refuge-jerusalem.side-4.entity-1"
        ],
        "destinations": {
          "02-civilian-refuge-jerusalem.side-4.entity-1": "02-civilian-refuge-jerusalem.side-4.zone-1"
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
        "receipt": "02-civilian-refuge-jerusalem.side-4.payment",
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
        "id": "02-civilian-refuge-jerusalem.side-4.entity-1",
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
        "id": "02-civilian-refuge-jerusalem.side-4.zone-1",
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
      "onceFlag": "02-civilian-refuge-jerusalem.side-4.rewarded",
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

### Ridge road guide / Guía del camino de la cresta

EN: Escort the local guide of ridge road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía del camino de la cresta hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: Locates a land route without making the Kidron navigable.

ES: Localiza una ruta terrestre sin hacer navegable el Cedrón.

```json
{
  "id": "side-5",
  "kind": "guide",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "02-civilian-refuge-jerusalem.side-5.entity-1"
        ],
        "destinations": {
          "02-civilian-refuge-jerusalem.side-5.entity-1": "02-civilian-refuge-jerusalem.side-5.zone-1"
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
        "id": "02-civilian-refuge-jerusalem.side-5.entity-1",
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
        "id": "02-civilian-refuge-jerusalem.side-5.zone-1",
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
      "target": "relief corridor",
      "resources": {},
      "onceFlag": "02-civilian-refuge-jerusalem.side-5.rewarded",
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

### Two visiting households / Dos hogares visitantes

EN: Bring both voluntary evacuee groups from two visiting households to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de dos hogares visitantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Optional voluntary travelers cannot fill the main survivor ledger.

ES: Los viajeros opcionales no pueden completar el registro principal.

```json
{
  "id": "side-6",
  "kind": "extract",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "02-civilian-refuge-jerusalem.side-6.entity-1",
          "02-civilian-refuge-jerusalem.side-6.entity-2"
        ],
        "destinations": {
          "02-civilian-refuge-jerusalem.side-6.entity-1": "02-civilian-refuge-jerusalem.side-6.zone-1",
          "02-civilian-refuge-jerusalem.side-6.entity-2": "02-civilian-refuge-jerusalem.side-6.zone-1"
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
        "id": "02-civilian-refuge-jerusalem.side-6.entity-1",
        "role": "extract",
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
        "id": "02-civilian-refuge-jerusalem.side-6.entity-2",
        "role": "extract",
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
        "id": "02-civilian-refuge-jerusalem.side-6.zone-1",
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
      "kind": "finite-supply-withdrawal",
      "target": "optional supply stock",
      "resources": {
        "food": 100,
        "gold": 25
      },
      "onceFlag": "02-civilian-refuge-jerusalem.side-6.rewarded",
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

```json
{
  "secondaryBudget": {
    "reservedRewards": {
      "food": 550,
      "wood": 200,
      "gold": 25,
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
      "id": "household-provision",
      "optionalObjectives": [
        "side-1",
        "side-3",
        "side-4"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Detours and 50 wood/50 gold buy finite material reserves; no mandatory dependency."
    },
    {
      "id": "records-and-route",
      "optionalObjectives": [
        "side-2",
        "side-5"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Travel to the copyist and guide buys context and route information; no new historical certainty."
    },
    {
      "id": "civilian-care",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Voluntary arrivals protect distinct optional households; no substitution for main participants."
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
      "food": 1458,
      "wood": 708,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
      "wood": 0,
      "gold": 0,
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
      "food": 1310,
      "wood": 680,
      "gold": 290,
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
      "food": 1510,
      "wood": 730,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
      "wood": 0,
      "gold": 0,
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
      "food": 1310,
      "wood": 680,
      "gold": 290,
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
      "food": 1563,
      "wood": 753,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
      "wood": 0,
      "gold": 0,
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
      "food": 1310,
      "wood": 680,
      "gold": 290,
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
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.title / always | none | When the City Held Its Breath | Cuando la ciudad contuvo el aliento |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.fact-intro / intro first | collection-narrator | Tacitus, writing decades later, reports the execution of Christus under Tiberius by Pontius Pilate. The conventional dating around 30–33 is reconstructed. The households and refuge journey here are fictional. | Tácito, décadas después, informa de la ejecución de Christus bajo Tiberio por Poncio Pilato. La fecha convencional hacia 30–33 es una reconstrucción. Los hogares y su traslado al refugio son ficticios. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.persona-intro / after handover | miriam-archive | The account names an execution. It does not name these families. I give our reconstruction separate labels so grief does not become false testimony. | El relato nombra una ejecución. No nombra a estas familias. Rotulo nuestra reconstrucción por separado para que el duelo no se convierta en un testimonio falso. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.route-help / available from start; repeatable without effect | none | Follow the western plateau and southern land approaches. Keep the same household identities through both receiving zones. | Sigue la meseta occidental y los accesos terrestres del sur. Conserva las mismas identidades domésticas en ambas zonas receptoras. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.o1-goal / phase-1 active | none | Bring at least six of the same eight households to the southern receiving court alive. | Lleva con vida al menos seis de los mismos ocho hogares al patio receptor del sur. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.o1-receipt / o1 latched once | none | Six distinct household arrivals are required; repeated entries do not add families. | Se requieren seis llegadas de hogares distintos; repetir entradas no añade familias. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.o1-reaction / after o1 receipt | miriam-archive | Keep their names, even when a number would be easier. | Conserva sus nombres, aunque un número resulte más cómodo. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.o2-goal / phase-2 active | none | Deliver a single total of 240 food to the receiving court. | Entrega un único total de 240 de alimento en el patio receptor. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.o2-receipt / o2 latched once | none | The 240-food receipt is paid once. | El recibo de 240 de alimento se paga una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.o2-reaction / after o2 receipt | miriam-archive | A receipt is dull until someone must eat. | Un recibo resulta gris hasta que alguien necesita comer. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.o3-goal / phase-3 active | none | Bring at least six supplied households to the southern road refuge alive; use the arrival ledger from the court. | Lleva con vida al menos seis hogares abastecidos al refugio del camino sur; utiliza el registro de llegada del patio. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.o3-receipt / o3 latched once | none | Only households recorded at the receiving court may count at the final refuge. | Solo cuentan en el refugio final los hogares registrados en el patio receptor. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.o3-reaction / after o3 receipt | miriam-archive | They are the same people at both gates. A ledger must remember that. | Son las mismas personas en ambas puertas. Un registro debe recordarlo. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at unlisted neighbors. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en vecinos sin registrar. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-1-complete / side-1 completed | none | Unlisted neighbors completed. Its stated benefit has been granted once. | Vecinos sin registrar: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-1-lost / side-1 failed-optional | none | Unlisted neighbors is unavailable after the loss of its unique participant or object. The main mission continues. | Vecinos sin registrar: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from names on two scraps and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de nombres en dos fragmentos y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-2-complete / side-2 completed | none | Names on two scraps completed. Its stated benefit has been granted once. | Nombres en dos fragmentos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-2-lost / side-2 failed-optional | none | Names on two scraps is unavailable after the loss of its unique participant or object. The main mission continues. | Nombres en dos fragmentos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of refuge store roof to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de techo del almacén del refugio. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-3-complete / side-3 completed | none | Refuge store roof completed. Its stated benefit has been granted once. | Techo del almacén del refugio: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-3-lost / side-3 failed-optional | none | Refuge store roof is unavailable after the loss of its unique participant or object. The main mission continues. | Techo del almacén del refugio: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-4-goal / optional list from start | none | Escort the trader of olive road trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de comerciante del camino de los olivos hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-4-complete / side-4 completed | none | Olive road trader completed. Its stated benefit has been granted once. | Comerciante del camino de los olivos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-4-lost / side-4 failed-optional | none | Olive road trader is unavailable after the loss of its unique participant or object. The main mission continues. | Comerciante del camino de los olivos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-5-goal / optional list from start | none | Escort the local guide of ridge road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía del camino de la cresta hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-5-complete / side-5 completed | none | Ridge road guide completed. Its stated benefit has been granted once. | Guía del camino de la cresta: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-5-lost / side-5 failed-optional | none | Ridge road guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del camino de la cresta: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from two visiting households to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de dos hogares visitantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-6-complete / side-6 completed | none | Two visiting households completed. Its stated benefit has been granted once. | Dos hogares visitantes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.side-6-lost / side-6 failed-optional | none | Two visiting households is unavailable after the loss of its unique participant or object. The main mission continues. | Dos hogares visitantes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.fact-outro / victory first | collection-narrator | Local success changes no documented execution and proves no ancient refuge operation. The historical account and the fictional household task remain separate. | El éxito local no cambia la ejecución documentada ni demuestra una operación antigua de refugio. El relato histórico y la tarea doméstica ficticia siguen separados. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.persona-outro / after fact-outro | miriam-archive | I cannot restore those unnamed lives. I can refuse to make their imagined journey evidence for mine. | No puedo reconstruir aquellas vidas sin nombre. Sí puedo negarme a convertir su viaje imaginado en una prueba de mi relato. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.02-civilian-refuge-jerusalem.odyssey.next-episode / after persona-outro | none | Continue with A Table in Jerusalem. This episode does not complete the campaign. | Continúa con Una mesa en Jerusalén. Este episodio no termina la campaña. |

## Production, recovery and verification

```json
{
  "stateMachine": {
    "states": [
      "briefing",
      "phase-1",
      "phase-2",
      "phase-3",
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
        "to": "victory",
        "on": "objective-latched",
        "objectiveId": "o3"
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
      "six arrive at court, a different six at refuge: only intersection qualifies",
      "third household loss causes main defeat",
      "optional household arrival never counts as a main household",
      "no repeat food debit",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
