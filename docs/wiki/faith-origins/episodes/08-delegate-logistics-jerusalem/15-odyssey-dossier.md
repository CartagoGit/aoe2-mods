# 8. A Place for the Stranger

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `08-delegate-logistics-jerusalem` · c. 49–50 CE; identification of meetings disputed · 360×360

## Historical frame and fixed outcome

EN: Acts narrates a Jerusalem debate about gentile inclusion and circumcision. Paul gives a separate account of a Jerusalem visit and agreement in Galatians. The two cannot be treated as one securely identified meeting without argument.

ES: Hechos narra un debate en Jerusalén sobre inclusión gentil y circuncisión. Pablo ofrece por separado en Gálatas un relato de visita y acuerdo. No pueden tratarse como un encuentro identificado con certeza sin argumentarlo.

EN: The reception task changes no theological agreement. Acts and Galatians remain separately attributed accounts with a disputed relationship.

ES: La tarea de recepción no cambia ningún acuerdo teológico. Hechos y Gálatas siguen siendo relatos atribuidos por separado cuya relación se discute.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 0,
      "episodeId": "08-delegate-logistics-jerusalem",
      "order": 8,
      "selectedSourceUrl": "https://academic.oup.com/edited-volume/37088/chapter/323184625",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Acts+15&version=NRSVUE",
      "passage": "Acts 15:1–29: narrative of a Jerusalem meeting debating circumcision of gentile adherents and a set of requirements; compare Paul's distinct account in Galatians 2:1–10.",
      "supportedClaim": {
        "en": "Acts narrates a Jerusalem debate about gentile inclusion and circumcision; Paul independently describes a Jerusalem visit and agreement about mission in Galatians 2.",
        "es-ES": "Hechos narra un debate en Jerusalén sobre la inclusión gentil y la circuncisión; Pablo describe por separado una visita y un acuerdo sobre la misión en Gálatas 2."
      },
      "limitations": "Acts and Galatians cannot be harmonized into one securely identified meeting without argument; date c.49–50 is reconstructed. The Oxford Handbook page is an overview, not primary evidence; source selection should cite both accounts and signal disagreement.",
      "consultationDate": "2026-10-12",
      "status": "disputed",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Galatians+2%3A1-10&version=NRSVUE",
      "passage": "Galatians 2:1–10",
      "supportedClaim": {
        "en": "Paul describes another Jerusalem visit with Barnabas and Titus, a private presentation, agreement about missions and remembering the poor.",
        "es-ES": "Pablo describe otra visita a Jerusalén con Bernabé y Tito, una exposición privada, un acuerdo sobre misiones y el recuerdo de los pobres."
      },
      "limitations": "A retrospective Pauline account; no composition date is asserted. It does not independently establish that this is the same meeting narrated in Acts15 or a transcript of that meeting. Not a physical game object in c49–50.",
      "consultationDate": "2026-10-12",
      "status": "consulted-primary-account-with-disputed-identification",
      "coverageActuallyRead": "complete verses1–10 in linked edition; no modern scholarly harmonization consulted"
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

EN: Bring the four distinct fictional delegates alive to the western hosting district.

ES: Lleva con vida a los cuatro delegados ficticios distintos al barrio de acogida occidental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "faith-origins.08-delegate-logistics-jerusalem.delegates-1",
        "faith-origins.08-delegate-logistics-jerusalem.delegates-2",
        "faith-origins.08-delegate-logistics-jerusalem.delegates-3",
        "faith-origins.08-delegate-logistics-jerusalem.delegates-4"
      ],
      "destinations": {
        "faith-origins.08-delegate-logistics-jerusalem.delegates-1": "faith-origins.08-delegate-logistics-jerusalem.destination-2",
        "faith-origins.08-delegate-logistics-jerusalem.delegates-2": "faith-origins.08-delegate-logistics-jerusalem.destination-2",
        "faith-origins.08-delegate-logistics-jerusalem.delegates-3": "faith-origins.08-delegate-logistics-jerusalem.destination-2",
        "faith-origins.08-delegate-logistics-jerusalem.delegates-4": "faith-origins.08-delegate-logistics-jerusalem.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Four distinct arrivals are registered; no historical speaker is a controllable delegate.

ES: Se registran cuatro llegadas distintas; ningún portavoz histórico es un delegado controlable.

EN: Hospitality does not require me to supply a speech for someone who left none.

ES: La hospitalidad no me obliga a inventar un discurso para quien no dejó uno.

### o2 / phase-2

EN: Provide one reception payment of 200 food and collect two separately labeled fictional delegate journey notes.

ES: Entrega un único pago de recepción de 200 de alimento y recoge dos notas ficticias de viaje de delegados etiquetadas por separado.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 200
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.08-delegate-logistics-jerusalem.destination-2"
      ],
      "allocations": {
        "faith-origins.08-delegate-logistics-jerusalem.destination-2": {
          "food": 200
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.08-delegate-logistics-jerusalem.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-1",
        "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-2"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Two fictional journey notes and one reception payment are registered. Neither note is Acts or Galatians.

ES: Se registran dos notas ficticias de viaje y un pago de recepción. Ninguna nota es Hechos ni Gálatas.

EN: Keep each account under its own name.

ES: Conserva cada relato bajo su propio nombre.

### o3 / phase-3

EN: Deliver both distinct fictional journey notes to the south return station.

ES: Entrega las dos notas ficticias distintas de viaje en la estación de regreso sur.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-1",
        "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-2"
      ],
      "destinations": {
        "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-1": "faith-origins.08-delegate-logistics-jerusalem.destination-3",
        "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-2": "faith-origins.08-delegate-logistics-jerusalem.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both fictional journey notes have arrived; the mission supplies no transcript of the meeting.

ES: Llegan las dos notas ficticias de viaje; la misión no aporta una transcripción de la reunión.

EN: Leaving them separate is a decision too. It is the one the evidence asks of me.

ES: Dejarlas separadas también es una decisión. Es la que me pide la evidencia.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/08-delegate-logistics-jerusalem.svg)

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
        177.8,
        125.41
      ],
      "lonLat": [
        35.209,
        31.807
      ],
      "name": {
        "en": "Northwest visitor approach",
        "es-ES": "Acceso de visitantes noroeste"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        191.42,
        183.51
      ],
      "lonLat": [
        35.217,
        31.778
      ],
      "name": {
        "en": "Western hosting district",
        "es-ES": "Barrio de acogida occidental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        210.15,
        243.61
      ],
      "lonLat": [
        35.228,
        31.748
      ],
      "name": {
        "en": "South return station",
        "es-ES": "Estación de regreso sur"
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
  "terrainInstructions": "Western plateau visitor activity, sacred meeting persons remain contextual. City compounds fictitious; no doctrinal conversion mechanics, no cathedral anachronism.",
  "corridorStraightLengthsTiles": {
    "main": 122.63,
    "relief": 122.63
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
  "asset": "docs/design/maps/faith-origins/odyssey/08-delegate-logistics-jerusalem.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.08-delegate-logistics-jerusalem.delegates-1",
      "role": "fictional-local-delegate",
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
      "id": "faith-origins.08-delegate-logistics-jerusalem.delegates-2",
      "role": "fictional-local-delegate",
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
      "id": "faith-origins.08-delegate-logistics-jerusalem.delegates-3",
      "role": "fictional-local-delegate",
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
      "id": "faith-origins.08-delegate-logistics-jerusalem.delegates-4",
      "role": "fictional-local-delegate",
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
      "id": "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-1",
      "role": "fictional-contemporary-delegate-journey-note",
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
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    },
    {
      "id": "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-2",
      "role": "fictional-contemporary-delegate-journey-note",
      "initialHub": "hub-2",
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
    }
  ],
  "zones": [
    {
      "id": "faith-origins.08-delegate-logistics-jerusalem.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.08-delegate-logistics-jerusalem.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.08-delegate-logistics-jerusalem.destination-3",
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
    "delegates": [
      "faith-origins.08-delegate-logistics-jerusalem.delegates-1",
      "faith-origins.08-delegate-logistics-jerusalem.delegates-2",
      "faith-origins.08-delegate-logistics-jerusalem.delegates-3",
      "faith-origins.08-delegate-logistics-jerusalem.delegates-4"
    ],
    "separate-accounts": [
      "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-1",
      "faith-origins.08-delegate-logistics-jerusalem.separate-accounts-2"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Hosting households / Hogares de acogida

EN: Bring each of the two aid crates to its assigned household at hosting households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de acogida. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Supports visitors without buying doctrine.

ES: Ayuda a visitantes sin comprar doctrinas.

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
          "08-delegate-logistics-jerusalem.side-1.entity-1",
          "08-delegate-logistics-jerusalem.side-1.entity-2"
        ],
        "destinations": {
          "08-delegate-logistics-jerusalem.side-1.entity-1": "08-delegate-logistics-jerusalem.side-1.zone-1",
          "08-delegate-logistics-jerusalem.side-1.entity-2": "08-delegate-logistics-jerusalem.side-1.zone-2"
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
        "id": "08-delegate-logistics-jerusalem.side-1.entity-1",
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
        "id": "08-delegate-logistics-jerusalem.side-1.entity-2",
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
        "id": "08-delegate-logistics-jerusalem.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "08-delegate-logistics-jerusalem.side-1.zone-2",
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
      "onceFlag": "08-delegate-logistics-jerusalem.side-1.rewarded",
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

### Two separate labels / Dos etiquetas separadas

EN: Recover both separate copies from two separate labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de dos etiquetas separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Two fictional journey labels preserve distinct gameplay identities; no future canonical text is an object.

ES: Dos etiquetas ficticias de viaje conservan identidades jugables distintas; ningún texto canónico posterior es un objeto.

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
          "08-delegate-logistics-jerusalem.side-2.entity-1",
          "08-delegate-logistics-jerusalem.side-2.entity-2"
        ],
        "destinations": {
          "08-delegate-logistics-jerusalem.side-2.entity-1": "08-delegate-logistics-jerusalem.side-2.zone-1",
          "08-delegate-logistics-jerusalem.side-2.entity-2": "08-delegate-logistics-jerusalem.side-2.zone-1"
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
        "id": "08-delegate-logistics-jerusalem.side-2.entity-1",
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
        "id": "08-delegate-logistics-jerusalem.side-2.entity-2",
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
        "id": "08-delegate-logistics-jerusalem.side-2.zone-1",
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
      "onceFlag": "08-delegate-logistics-jerusalem.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.08-delegate-logistics-jerusalem"
      ],
      "historicalNote": {
        "en": "Acts narrates a Jerusalem debate about gentile inclusion and circumcision. Paul gives a separate account of a Jerusalem visit and agreement in Galatians. The two cannot be treated as one securely identified meeting without argument.",
        "es-ES": "Hechos narra un debate en Jerusalén sobre inclusión gentil y circuncisión. Pablo ofrece por separado en Gálatas un relato de visita y acuerdo. No pueden tratarse como un encuentro identificado con certeza sin argumentarlo."
      },
      "hint": {
        "en": "Bring the four distinct fictional delegates alive to the western hosting district.",
        "es-ES": "Lleva con vida a los cuatro delegados ficticios distintos al barrio de acogida occidental."
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

### Visitor store / Almacén de visitantes

EN: Pay 50 wood and restore the damaged store of visitor store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén de visitantes. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair supports finite hospitality supplies.

ES: La reparación ayuda a suministros finitos de hospitalidad.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "08-delegate-logistics-jerusalem.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "08-delegate-logistics-jerusalem.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "08-delegate-logistics-jerusalem.side-3.payment",
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
        "id": "08-delegate-logistics-jerusalem.side-3.entity-1",
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
        "id": "08-delegate-logistics-jerusalem.side-3.zone-1",
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
      "onceFlag": "08-delegate-logistics-jerusalem.side-3.rewarded",
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

### Reception trader / Comerciante de recepción

EN: Escort the trader of reception trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de comerciante de recepción hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Finite consignment reduces travel cost.

ES: La remesa finita reduce el coste del viaje.

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
          "08-delegate-logistics-jerusalem.side-4.entity-1"
        ],
        "destinations": {
          "08-delegate-logistics-jerusalem.side-4.entity-1": "08-delegate-logistics-jerusalem.side-4.zone-1"
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
        "receipt": "08-delegate-logistics-jerusalem.side-4.payment",
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
        "id": "08-delegate-logistics-jerusalem.side-4.entity-1",
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
        "id": "08-delegate-logistics-jerusalem.side-4.zone-1",
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
      "onceFlag": "08-delegate-logistics-jerusalem.side-4.rewarded",
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

### Return road guide / Guía del camino de regreso

EN: Escort the local guide of return road guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task.

ES: Escolta al guía local de guía del camino de regreso hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea.

EN: Shows the southern land departure.

ES: Señala la salida terrestre del sur.

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
          "08-delegate-logistics-jerusalem.side-5.entity-1"
        ],
        "destinations": {
          "08-delegate-logistics-jerusalem.side-5.entity-1": "08-delegate-logistics-jerusalem.side-5.zone-1"
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
        "id": "08-delegate-logistics-jerusalem.side-5.entity-1",
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
        "id": "08-delegate-logistics-jerusalem.side-5.zone-1",
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
      "target": "relief surveyed land corridor",
      "resources": {},
      "onceFlag": "08-delegate-logistics-jerusalem.side-5.rewarded",
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

### Guests choosing to move / Huéspedes que deciden trasladarse

EN: Bring both voluntary evacuee groups from guests choosing to move to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de huéspedes que deciden trasladarse al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Voluntary departure is distinct from exile.

ES: La salida voluntaria se distingue del exilio.

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
          "08-delegate-logistics-jerusalem.side-6.entity-1",
          "08-delegate-logistics-jerusalem.side-6.entity-2"
        ],
        "destinations": {
          "08-delegate-logistics-jerusalem.side-6.entity-1": "08-delegate-logistics-jerusalem.side-6.zone-1",
          "08-delegate-logistics-jerusalem.side-6.entity-2": "08-delegate-logistics-jerusalem.side-6.zone-1"
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
        "id": "08-delegate-logistics-jerusalem.side-6.entity-1",
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
        "id": "08-delegate-logistics-jerusalem.side-6.entity-2",
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
        "id": "08-delegate-logistics-jerusalem.side-6.zone-1",
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
      "onceFlag": "08-delegate-logistics-jerusalem.side-6.rewarded",
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
      "food": 1418,
      "wood": 708,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 200,
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
      "food": 1270,
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
      "food": 1470,
      "wood": 730,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 200,
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
      "food": 1270,
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
      "food": 1523,
      "wood": 753,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 200,
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
      "food": 1270,
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
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.title / always | none | A Place for the Stranger | Un lugar para el extranjero |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.fact-intro / intro first | collection-narrator | Acts narrates a Jerusalem debate about gentile inclusion and circumcision. Paul gives a separate account of a Jerusalem visit and agreement in Galatians. The two cannot be treated as one securely identified meeting without argument. | Hechos narra un debate en Jerusalén sobre inclusión gentil y circuncisión. Pablo ofrece por separado en Gálatas un relato de visita y acuerdo. No pueden tratarse como un encuentro identificado con certeza sin argumentarlo. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.persona-intro / after handover | miriam-archive | In my later archive, two accounts can sit on the same shelf without becoming the same page. These local journey notes are our reconstruction, not those later books. | En mi archivo posterior, dos relatos pueden estar en el mismo estante sin convertirse en la misma página. Estas notas locales de viaje son nuestra reconstrucción, no esos libros posteriores. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.route-help / available from start; repeatable without effect | none | Host the visitors on the western plateau. Keep both account-copy identities through the southern return route. | Acoge a los visitantes en la meseta occidental. Conserva ambas identidades de las copias durante el regreso por el sur. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.o1-goal / phase-1 active | none | Bring the four distinct fictional delegates alive to the western hosting district. | Lleva con vida a los cuatro delegados ficticios distintos al barrio de acogida occidental. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.o1-receipt / o1 latched once | none | Four distinct arrivals are registered; no historical speaker is a controllable delegate. | Se registran cuatro llegadas distintas; ningún portavoz histórico es un delegado controlable. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.o1-reaction / after o1 receipt | miriam-archive | Hospitality does not require me to supply a speech for someone who left none. | La hospitalidad no me obliga a inventar un discurso para quien no dejó uno. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.o2-goal / phase-2 active | none | Provide one reception payment of 200 food and collect two separately labeled fictional delegate journey notes. | Entrega un único pago de recepción de 200 de alimento y recoge dos notas ficticias de viaje de delegados etiquetadas por separado. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.o2-receipt / o2 latched once | none | Two fictional journey notes and one reception payment are registered. Neither note is Acts or Galatians. | Se registran dos notas ficticias de viaje y un pago de recepción. Ninguna nota es Hechos ni Gálatas. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.o2-reaction / after o2 receipt | miriam-archive | Keep each account under its own name. | Conserva cada relato bajo su propio nombre. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.o3-goal / phase-3 active | none | Deliver both distinct fictional journey notes to the south return station. | Entrega las dos notas ficticias distintas de viaje en la estación de regreso sur. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.o3-receipt / o3 latched once | none | Both fictional journey notes have arrived; the mission supplies no transcript of the meeting. | Llegan las dos notas ficticias de viaje; la misión no aporta una transcripción de la reunión. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.o3-reaction / after o3 receipt | miriam-archive | Leaving them separate is a decision too. It is the one the evidence asks of me. | Dejarlas separadas también es una decisión. Es la que me pide la evidencia. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at hosting households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de acogida. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-1-complete / side-1 completed | none | Hosting households completed. Its stated benefit has been granted once. | Hogares de acogida: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-1-lost / side-1 failed-optional | none | Hosting households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares de acogida: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from two separate labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de dos etiquetas separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-2-complete / side-2 completed | none | Two separate labels completed. Its stated benefit has been granted once. | Dos etiquetas separadas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-2-lost / side-2 failed-optional | none | Two separate labels is unavailable after the loss of its unique participant or object. The main mission continues. | Dos etiquetas separadas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of visitor store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén de visitantes. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-3-complete / side-3 completed | none | Visitor store completed. Its stated benefit has been granted once. | Almacén de visitantes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-3-lost / side-3 failed-optional | none | Visitor store is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén de visitantes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-4-goal / optional list from start | none | Escort the trader of reception trader to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de comerciante de recepción hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-4-complete / side-4 completed | none | Reception trader completed. Its stated benefit has been granted once. | Comerciante de recepción: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-4-lost / side-4 failed-optional | none | Reception trader is unavailable after the loss of its unique participant or object. The main mission continues. | Comerciante de recepción: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-5-goal / optional list from start | none | Escort the local guide of return road guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task. | Escolta al guía local de guía del camino de regreso hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-5-complete / side-5 completed | none | Return road guide completed. Its stated benefit has been granted once. | Guía del camino de regreso: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-5-lost / side-5 failed-optional | none | Return road guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del camino de regreso: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from guests choosing to move to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de huéspedes que deciden trasladarse al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-6-complete / side-6 completed | none | Guests choosing to move completed. Its stated benefit has been granted once. | Huéspedes que deciden trasladarse: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.side-6-lost / side-6 failed-optional | none | Guests choosing to move is unavailable after the loss of its unique participant or object. The main mission continues. | Huéspedes que deciden trasladarse: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.fact-outro / victory first | collection-narrator | The reception task changes no theological agreement. Acts and Galatians remain separately attributed accounts with a disputed relationship. | La tarea de recepción no cambia ningún acuerdo teológico. Hechos y Gálatas siguen siendo relatos atribuidos por separado cuya relación se discute. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.persona-outro / after fact-outro | miriam-archive | We have made room for visitors and left room for disagreement. An archive needs both kinds of space. | Hemos hecho sitio para los visitantes y hemos dejado sitio para el desacuerdo. Un archivo necesita ambas clases de espacio. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.next-episode / after persona-outro | none | Continue with The Weaver's Harbour. This episode does not complete the campaign. | Continúa con El puerto del tejedor. Este episodio no termina la campaña. |
| scenario.faith-origins.08-delegate-logistics-jerusalem.odyssey.act-turning-point / after next-episode | collection-narrator | The next act follows work and letters in Mediterranean cities. Continue with The Weaver's Harbour. Jerusalem remains a place of diverse communities, not a conquered origin point. | El siguiente acto recorre el trabajo y las cartas de ciudades mediterráneas. Continúa con El puerto del tejedor. Jerusalén sigue siendo un lugar de comunidades diversas, no un origen conquistado. |

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
      "two texts cannot collapse into one counted record",
      "all four fictitious delegates required",
      "no theological verdict attached to an optional reward",
      "act transition names actual next selected episode",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
