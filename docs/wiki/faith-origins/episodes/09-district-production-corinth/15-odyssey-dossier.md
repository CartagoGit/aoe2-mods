# 9. The Weaver's Harbour

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `09-district-production-corinth` · c. 50–52 CE · 380×380

## Historical frame and fixed outcome

EN: Acts portrays Paul living and working in Corinth with Prisca and Aquila, and later appearing before Gallio. The narrative is not an employment ledger or court transcript. The local workshop and its goods are fictional.

ES: Hechos presenta a Pablo viviendo y trabajando en Corinto con Prisca y Aquila y compareciendo después ante Galión. El relato no es un registro laboral ni una transcripción judicial. El taller local y sus bienes son ficticios.

EN: The delivery illustrates an imagined workshop economy in Roman Corinth. Neither these orders nor their successful delivery establish the details of the household portrayed in Acts.

ES: La entrega representa una economía de taller imaginada en la Corinto romana. Ni estos encargos ni su entrega satisfactoria acreditan los detalles del hogar descrito en Hechos.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 1,
      "episodeId": "09-district-production-corinth",
      "order": 9,
      "selectedSourceUrl": "https://dcc.dickinson.edu/greek-new-testament/acts/18",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Acts+18&version=NRSVUE",
      "passage": "Acts 18:1–18: Paul meets Prisca and Aquila in Corinth, stays eighteen months, and is brought before Gallio; compare Gallio inscription for the proconsul's tenure.",
      "supportedClaim": {
        "en": "Acts reports Paul working with Prisca and Aquila in Corinth and staying there eighteen months; the Gallio episode provides a chronological anchor.",
        "es-ES": "Hechos informa que Pablo trabajó con Prisca y Aquila en Corinto y permaneció allí dieciocho meses; el episodio de Galión sirve de ancla cronológica."
      },
      "limitations": "Narrative source, not a contemporary record of founding. Exact 50–52 dating depends on the Delphi inscription's date and chronology reconstruction; DCC URL listed in selection was unavailable in the earlier consultation.",
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

EN: Recover three distinct workshop material lots.

ES: Recupera tres lotes distintos de materiales del taller.

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
        "faith-origins.09-district-production-corinth.work-materials-1",
        "faith-origins.09-district-production-corinth.work-materials-2",
        "faith-origins.09-district-production-corinth.work-materials-3"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three material identities collected.

ES: Tres identidades de material recogidas.

EN: A repeated mark is not another bundle.

ES: Una marca repetida no es otro bulto.

### o2 / phase-2

EN: Pay 100 wood and 50 gold at the workshop and turn the three lots into four finished bundles once.

ES: Paga 100 de madera y 50 de oro en el taller y transforma una sola vez los tres lotes en cuatro bultos acabados.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 100,
        "gold": 50
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.09-district-production-corinth.destination-1"
      ],
      "allocations": {
        "faith-origins.09-district-production-corinth.destination-1": {
          "wood": 100,
          "gold": 50
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.09-district-production-corinth.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "requiresInputsCollected": true,
      "id": "req-2",
      "inputEntities": [
        "faith-origins.09-district-production-corinth.work-materials-1",
        "faith-origins.09-district-production-corinth.work-materials-2",
        "faith-origins.09-district-production-corinth.work-materials-3"
      ],
      "outputEntities": [
        "faith-origins.09-district-production-corinth.finished-bundles-1",
        "faith-origins.09-district-production-corinth.finished-bundles-2",
        "faith-origins.09-district-production-corinth.finished-bundles-3",
        "faith-origins.09-district-production-corinth.finished-bundles-4"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.09-district-production-corinth.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 100,
            "gold": 50
          },
          "newDebit": false
        }
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: One funded production receipt and four derived identities.

ES: Un recibo de producción financiada y cuatro identidades derivadas.

EN: My account describes invented work, not a contract signed by Paul.

ES: Mi cuenta describe trabajo inventado, no un contrato firmado por Pablo.

### o3 / phase-3

EN: Deliver bundles 1–2 to the Lechaion-road yard and bundles 3–4 to the eastern post.

ES: Entrega los bultos 1–2 en el patio del camino a Lequeo y los bultos 3–4 en el puesto oriental.

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
        "faith-origins.09-district-production-corinth.finished-bundles-1",
        "faith-origins.09-district-production-corinth.finished-bundles-2",
        "faith-origins.09-district-production-corinth.finished-bundles-3",
        "faith-origins.09-district-production-corinth.finished-bundles-4"
      ],
      "destinations": {
        "faith-origins.09-district-production-corinth.finished-bundles-1": "faith-origins.09-district-production-corinth.destination-2",
        "faith-origins.09-district-production-corinth.finished-bundles-2": "faith-origins.09-district-production-corinth.destination-2",
        "faith-origins.09-district-production-corinth.finished-bundles-3": "faith-origins.09-district-production-corinth.destination-3",
        "faith-origins.09-district-production-corinth.finished-bundles-4": "faith-origins.09-district-production-corinth.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All four assigned deliveries are registered; wrong-post deliveries do not count.

ES: Las cuatro entregas asignadas están registradas; las entregas en otro puesto no cuentan.

EN: Two destinations, four objects: do not let the total hide the wrong address.

ES: Dos destinos, cuatro objetos: que el total no oculte una dirección equivocada.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/09-district-production-corinth.svg)

```json
{
  "bbox": [
    22.83,
    37.875,
    23.065,
    37.975
  ],
  "terrainProfile": "corinth",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        106.7,
        222.36
      ],
      "lonLat": [
        22.89,
        37.907
      ],
      "name": {
        "en": "Inland workshop yard",
        "es-ES": "Patio del taller interior"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        113.9,
        173.07
      ],
      "lonLat": [
        22.895,
        37.934
      ],
      "name": {
        "en": "Lechaion road receiving yard",
        "es-ES": "Patio receptor del camino a Lequeo"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        229.1,
        213.23
      ],
      "lonLat": [
        22.975,
        37.912
      ],
      "name": {
        "en": "Eastern inland consignment post",
        "es-ES": "Puesto interior de remesas orientales"
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
  "terrainInstructions": "Corinthian Gulf north, Acrocorinth south, Saronic Gulf east. Keep workshop inland and eastern post west of Cenchreae shore. No modern canal, later Frankish fortress or Christian basilica. Main deliveries branch north/east after production; do not force a sea crossing. Archeological terrace/road path certification pending.",
  "mainRouteLengthStraightTiles": 171.81,
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
  "schematicWaterControl": null,
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/09-district-production-corinth.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.09-district-production-corinth.work-materials-1",
      "role": "fictional-workshop-material",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.09-district-production-corinth.work-materials-2",
      "role": "fictional-workshop-material",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.09-district-production-corinth.work-materials-3",
      "role": "fictional-workshop-material",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.09-district-production-corinth.finished-bundles-1",
      "role": "fictional-finished-workshop-bundle",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.09-district-production-corinth.finished-bundles-2",
      "role": "fictional-finished-workshop-bundle",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.09-district-production-corinth.finished-bundles-3",
      "role": "fictional-finished-workshop-bundle",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.09-district-production-corinth.finished-bundles-4",
      "role": "fictional-finished-workshop-bundle",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.09-district-production-corinth.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.09-district-production-corinth.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.09-district-production-corinth.destination-3",
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
    "work-materials": [
      "faith-origins.09-district-production-corinth.work-materials-1",
      "faith-origins.09-district-production-corinth.work-materials-2",
      "faith-origins.09-district-production-corinth.work-materials-3"
    ],
    "finished-bundles": [
      "faith-origins.09-district-production-corinth.finished-bundles-1",
      "faith-origins.09-district-production-corinth.finished-bundles-2",
      "faith-origins.09-district-production-corinth.finished-bundles-3",
      "faith-origins.09-district-production-corinth.finished-bundles-4"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Workyard roof / Tejado del taller

EN: Pay 50 wood and restore the damaged store of workyard roof to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de tejado del taller. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A local repair supports the workshop without inventing an apostolic building.

ES: Una reparación local apoya al taller sin inventar un edificio apostólico.

```json
{
  "id": "side-1",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "09-district-production-corinth.side-1.entity-1",
        "health": "full",
        "paymentReceipt": "09-district-production-corinth.side-1.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "09-district-production-corinth.side-1.payment",
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
        "id": "09-district-production-corinth.side-1.entity-1",
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
        "id": "09-district-production-corinth.side-1.zone-1",
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
      "onceFlag": "09-district-production-corinth.side-1.rewarded",
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

### Cloth consignment / Remesa de tejidos

EN: Escort the trader of cloth consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de remesa de tejidos hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A separate fictional trader creates one bounded exchange.

ES: Un comerciante ficticio separado permite un intercambio limitado.

```json
{
  "id": "side-2",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "09-district-production-corinth.side-2.entity-1"
        ],
        "destinations": {
          "09-district-production-corinth.side-2.entity-1": "09-district-production-corinth.side-2.zone-1"
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
        "receipt": "09-district-production-corinth.side-2.payment",
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
        "id": "09-district-production-corinth.side-2.entity-1",
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
        "id": "09-district-production-corinth.side-2.zone-1",
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
      "onceFlag": "09-district-production-corinth.side-2.rewarded",
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

### Separate order sheets / Hojas separadas de encargo

EN: Recover both separate copies from separate order sheets and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de hojas separadas de encargo y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Copies are fictional contemporary orders, not Acts manuscripts.

ES: Las copias son encargos contemporáneos ficticios, no manuscritos de Hechos.

```json
{
  "id": "side-3",
  "kind": "copy",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "09-district-production-corinth.side-3.entity-1",
          "09-district-production-corinth.side-3.entity-2"
        ],
        "destinations": {
          "09-district-production-corinth.side-3.entity-1": "09-district-production-corinth.side-3.zone-1",
          "09-district-production-corinth.side-3.entity-2": "09-district-production-corinth.side-3.zone-1"
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
        "id": "09-district-production-corinth.side-3.entity-1",
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
        "id": "09-district-production-corinth.side-3.entity-2",
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
        "id": "09-district-production-corinth.side-3.zone-1",
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
      "onceFlag": "09-district-production-corinth.side-3.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.09-district-production-corinth"
      ],
      "historicalNote": {
        "en": "Acts portrays Paul living and working in Corinth with Prisca and Aquila, and later appearing before Gallio. The narrative is not an employment ledger or court transcript. The local workshop and its goods are fictional.",
        "es-ES": "Hechos presenta a Pablo viviendo y trabajando en Corinto con Prisca y Aquila y compareciendo después ante Galión. El relato no es un registro laboral ni una transcripción judicial. El taller local y sus bienes son ficticios."
      },
      "hint": {
        "en": "Recover three distinct workshop material lots.",
        "es-ES": "Recupera tres lotes distintos de materiales del taller."
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

### Terrace road guide / Guía del camino entre terrazas

EN: Escort the local guide of terrace road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía del camino entre terrazas hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: A surveyed slope route offers navigation help, not a shortcut through Acrocorinth.

ES: Una ruta de pendiente comprobada ayuda a orientarse sin atravesar Acrocorinto.

```json
{
  "id": "side-4",
  "kind": "guide",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "09-district-production-corinth.side-4.entity-1"
        ],
        "destinations": {
          "09-district-production-corinth.side-4.entity-1": "09-district-production-corinth.side-4.zone-1"
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
        "id": "09-district-production-corinth.side-4.entity-1",
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
        "id": "09-district-production-corinth.side-4.zone-1",
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
      "onceFlag": "09-district-production-corinth.side-4.rewarded",
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

### Workers households / Hogares de trabajadores

EN: Bring each of the two aid crates to its assigned household at workers households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de trabajadores. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Two optional aid recipients never replace mandatory workshop bundles.

ES: Dos receptores opcionales de ayuda nunca sustituyen los bultos principales.

```json
{
  "id": "side-5",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "09-district-production-corinth.side-5.entity-1",
          "09-district-production-corinth.side-5.entity-2"
        ],
        "destinations": {
          "09-district-production-corinth.side-5.entity-1": "09-district-production-corinth.side-5.zone-1",
          "09-district-production-corinth.side-5.entity-2": "09-district-production-corinth.side-5.zone-2"
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
        "id": "09-district-production-corinth.side-5.entity-1",
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
        "id": "09-district-production-corinth.side-5.entity-2",
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
        "id": "09-district-production-corinth.side-5.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "09-district-production-corinth.side-5.zone-2",
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
      "onceFlag": "09-district-production-corinth.side-5.rewarded",
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

### Visiting apprentices / Aprendices visitantes

EN: Bring both voluntary evacuee groups from visiting apprentices to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de aprendices visitantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Voluntary travelers are fictional and unrelated to sacred protagonists.

ES: Los viajeros voluntarios son ficticios y ajenos a los protagonistas venerados.

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
          "09-district-production-corinth.side-6.entity-1",
          "09-district-production-corinth.side-6.entity-2"
        ],
        "destinations": {
          "09-district-production-corinth.side-6.entity-1": "09-district-production-corinth.side-6.zone-1",
          "09-district-production-corinth.side-6.entity-2": "09-district-production-corinth.side-6.zone-1"
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
        "id": "09-district-production-corinth.side-6.entity-1",
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
        "id": "09-district-production-corinth.side-6.entity-2",
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
        "id": "09-district-production-corinth.side-6.zone-1",
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
      "onceFlag": "09-district-production-corinth.side-6.rewarded",
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
      "id": "workshop-investment",
      "optionalObjectives": [
        "side-1",
        "side-2"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Spend50wood and50gold on bounded workyard improvements; reserve the100wood/50gold main production first."
    },
    {
      "id": "careful-dispatch",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Recover order copies and guide before dispatch; accept a detour for information, never change assigned destinations."
    },
    {
      "id": "neighbor-support",
      "optionalObjectives": [
        "side-5",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Divert transport effort to separate households/apprentices while workshop collection continues."
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
      "food": 1218,
      "wood": 808,
      "gold": 279,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 100,
      "gold": 50,
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
      "wood": 780,
      "gold": 340,
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
    "difficultyLevers": "12 workers; all pickup sites and receiving posts marked; open work order and detour choice.",
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
      "food": 1270,
      "wood": 830,
      "gold": 290,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 100,
      "gold": 50,
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
      "wood": 780,
      "gold": 340,
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
    "difficultyLevers": "9 workers; parallel work and local fog; essential receivers/costs always shown.",
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
      "food": 1323,
      "wood": 853,
      "gold": 302,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 100,
      "gold": 50,
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
      "wood": 780,
      "gold": 340,
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
    "difficultyLevers": "6 workers; lower start stock; organize parallel gathering and deliveries. No concealed requirements, unlimited enemies or changes to native health/movement.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.faith-origins.09-district-production-corinth.odyssey.title / always | none | The Weaver's Harbour | El puerto del tejedor |
| scenario.faith-origins.09-district-production-corinth.odyssey.fact-intro / intro first | collection-narrator | Acts portrays Paul living and working in Corinth with Prisca and Aquila, and later appearing before Gallio. The narrative is not an employment ledger or court transcript. The local workshop and its goods are fictional. | Hechos presenta a Pablo viviendo y trabajando en Corinto con Prisca y Aquila y compareciendo después ante Galión. El relato no es un registro laboral ni una transcripción judicial. El taller local y sus bienes son ficticios. |
| scenario.faith-origins.09-district-production-corinth.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.09-district-production-corinth.odyssey.persona-intro / after handover | miriam-archive | A copyist knows the ache in a wrist after a long day. I did not share their workshop, but I refuse to make ordinary work disappear behind the names an archive remembers. | Una copista conoce el dolor de muñeca al acabar una jornada larga. No compartí su taller, pero me niego a borrar el trabajo cotidiano detrás de los nombres que recuerda un archivo. |
| scenario.faith-origins.09-district-production-corinth.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.09-district-production-corinth.odyssey.route-help / available from start; repeatable without effect | none | After production, divide the four assigned bundles between north-road and east-road receiving posts. The east post is inland; no sea journey is simulated. | Tras la producción, reparte los cuatro bultos asignados entre los puestos del camino norte y oriental. El puesto oriental está en tierra; no se simula una travesía marítima. |
| scenario.faith-origins.09-district-production-corinth.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.o1-goal / phase-1 active | none | Recover three distinct workshop material lots. | Recupera tres lotes distintos de materiales del taller. |
| scenario.faith-origins.09-district-production-corinth.odyssey.o1-receipt / o1 latched once | none | Three material identities collected. | Tres identidades de material recogidas. |
| scenario.faith-origins.09-district-production-corinth.odyssey.o1-reaction / after o1 receipt | miriam-archive | A repeated mark is not another bundle. | Una marca repetida no es otro bulto. |
| scenario.faith-origins.09-district-production-corinth.odyssey.o2-goal / phase-2 active | none | Pay 100 wood and 50 gold at the workshop and turn the three lots into four finished bundles once. | Paga 100 de madera y 50 de oro en el taller y transforma una sola vez los tres lotes en cuatro bultos acabados. |
| scenario.faith-origins.09-district-production-corinth.odyssey.o2-receipt / o2 latched once | none | One funded production receipt and four derived identities. | Un recibo de producción financiada y cuatro identidades derivadas. |
| scenario.faith-origins.09-district-production-corinth.odyssey.o2-reaction / after o2 receipt | miriam-archive | My account describes invented work, not a contract signed by Paul. | Mi cuenta describe trabajo inventado, no un contrato firmado por Pablo. |
| scenario.faith-origins.09-district-production-corinth.odyssey.o3-goal / phase-3 active | none | Deliver bundles 1–2 to the Lechaion-road yard and bundles 3–4 to the eastern post. | Entrega los bultos 1–2 en el patio del camino a Lequeo y los bultos 3–4 en el puesto oriental. |
| scenario.faith-origins.09-district-production-corinth.odyssey.o3-receipt / o3 latched once | none | All four assigned deliveries are registered; wrong-post deliveries do not count. | Las cuatro entregas asignadas están registradas; las entregas en otro puesto no cuentan. |
| scenario.faith-origins.09-district-production-corinth.odyssey.o3-reaction / after o3 receipt | miriam-archive | Two destinations, four objects: do not let the total hide the wrong address. | Dos destinos, cuatro objetos: que el total no oculte una dirección equivocada. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-1-goal / optional list from start | none | Pay 50 wood and restore the damaged store of workyard roof to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de tejado del taller. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-1-complete / side-1 completed | none | Workyard roof completed. Its stated benefit has been granted once. | Tejado del taller: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-1-lost / side-1 failed-optional | none | Workyard roof is unavailable after the loss of its unique participant or object. The main mission continues. | Tejado del taller: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-2-goal / optional list from start | none | Escort the trader of cloth consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de remesa de tejidos hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-2-complete / side-2 completed | none | Cloth consignment completed. Its stated benefit has been granted once. | Remesa de tejidos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-2-lost / side-2 failed-optional | none | Cloth consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Remesa de tejidos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-3-goal / optional list from start | none | Recover both separate copies from separate order sheets and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de hojas separadas de encargo y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-3-complete / side-3 completed | none | Separate order sheets completed. Its stated benefit has been granted once. | Hojas separadas de encargo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-3-lost / side-3 failed-optional | none | Separate order sheets is unavailable after the loss of its unique participant or object. The main mission continues. | Hojas separadas de encargo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-4-goal / optional list from start | none | Escort the local guide of terrace road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía del camino entre terrazas hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-4-complete / side-4 completed | none | Terrace road guide completed. Its stated benefit has been granted once. | Guía del camino entre terrazas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-4-lost / side-4 failed-optional | none | Terrace road guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del camino entre terrazas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-5-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at workers households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de trabajadores. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-5-complete / side-5 completed | none | Workers households completed. Its stated benefit has been granted once. | Hogares de trabajadores: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-5-lost / side-5 failed-optional | none | Workers households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares de trabajadores: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from visiting apprentices to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de aprendices visitantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-6-complete / side-6 completed | none | Visiting apprentices completed. Its stated benefit has been granted once. | Aprendices visitantes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.09-district-production-corinth.odyssey.side-6-lost / side-6 failed-optional | none | Visiting apprentices is unavailable after the loss of its unique participant or object. The main mission continues. | Aprendices visitantes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.09-district-production-corinth.odyssey.fact-outro / victory first | collection-narrator | The delivery illustrates an imagined workshop economy in Roman Corinth. Neither these orders nor their successful delivery establish the details of the household portrayed in Acts. | La entrega representa una economía de taller imaginada en la Corinto romana. Ni estos encargos ni su entrega satisfactoria acreditan los detalles del hogar descrito en Hechos. |
| scenario.faith-origins.09-district-production-corinth.odyssey.persona-outro / after fact-outro | miriam-archive | We have counted the bundles. Now remember the hands. They belong in the story even when no inscription gives us their names. | Hemos contado los bultos. Recuerda ahora las manos: merecen estar en la historia aunque ninguna inscripción nos dé sus nombres. |
| scenario.faith-origins.09-district-production-corinth.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.09-district-production-corinth.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.09-district-production-corinth.odyssey.next-episode / after persona-outro | none | Continue with Before the First Letter Faded. This episode does not complete the campaign. | Continúa con Antes de que se borrase la primera carta. Este episodio no termina la campaña. |

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
      "wrong recipient cannot credit bundle",
      "one bundle cannot count at both receiving posts",
      "derived bundles unavailable before funded collection",
      "no free or repeat workshop generation",
      "Lechaion approach north of ancient center; no modern canal",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
