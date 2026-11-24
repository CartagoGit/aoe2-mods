# 1. Stone Beneath the Prefect's Name

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `01-administrative-records-caesarea` · 27–36 CE · 320×320

## Historical frame and fixed outcome

EN: A fragmentary inscription found at Caesarea names Pontius Pilate as prefect of Judaea and records a building dedication. It is evidence for his office, not a record of the trial of Jesus.

ES: Una inscripción fragmentaria hallada en Cesarea nombra a Poncio Pilato prefecto de Judea y registra una dedicación edilicia. Acredita su cargo; no documenta el proceso de Jesús.

EN: The inscription remains incomplete. Preserving its surviving words does not recover the missing text or establish unrelated events.

ES: La inscripción sigue incompleta. Conservar sus palabras no recupera el texto perdido ni acredita otros acontecimientos.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 24,
      "episodeId": "01-administrative-records-caesarea",
      "order": 1,
      "selectedSourceUrl": "https://cojs.org/pontius_pilate-s_tiberium_inscription-_26-36_ce/",
      "consultedUrl": "https://cojs.org/pontius_pilate-s_tiberium_inscription-_26-36_ce/",
      "passage": "COJS entry, paragraphs describing findspot, reused block, dedication and titulature; inscription translation names Pontius Pilate as prefect of Judea.",
      "supportedClaim": {
        "en": "The Caesarea inscription attests Pilate's title and a building dedication; it does not attest the trial of Jesus.",
        "es-ES": "La inscripción de Cesarea acredita el título de Pilato y una dedicación edilicia; no documenta el proceso de Jesús."
      },
      "limitations": "Fragmentary stone reused in a stairway; COJS is a secondary catalog entry. The campaign's 27–36 range is an editorial slice of the conventional prefecture dates, not the inscription's date.",
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

EN: Collect three distinct fictional dedication records from the coastal work yard.

ES: Recoge tres registros ficticios distintos de dedicación en el patio de trabajo costero.

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
        "faith-origins.01-administrative-records-caesarea.dedication-records-1",
        "faith-origins.01-administrative-records-caesarea.dedication-records-2",
        "faith-origins.01-administrative-records-caesarea.dedication-records-3"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three separate administrative copies are registered; these are not modern excavated fragments.

ES: Tres copias administrativas separadas están registradas; no son fragmentos excavados en la actualidad.

EN: Three copies can repeat the same mistake. Keep their offices and origins visible.

ES: Tres copias pueden repetir el mismo error. Conserva visibles sus cargos y procedencias.

### o2 / phase-2

EN: Bring the three original dedication-record bearers to the copying court, pay 40 wood and 20 gold, and issue one register from their records.

ES: Lleva a los tres portadores originales de los registros de dedicación al patio de copias, paga 40 de madera y 20 de oro y expide un registro a partir de sus documentos.

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
        "faith-origins.01-administrative-records-caesarea.destination-2"
      ],
      "allocations": {
        "faith-origins.01-administrative-records-caesarea.destination-2": {
          "wood": 40,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.01-administrative-records-caesarea.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "id": "req-2",
      "inputEntities": [
        "faith-origins.01-administrative-records-caesarea.dedication-records-1",
        "faith-origins.01-administrative-records-caesarea.dedication-records-2",
        "faith-origins.01-administrative-records-caesarea.dedication-records-3"
      ],
      "outputEntities": [
        "faith-origins.01-administrative-records-caesarea.register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.01-administrative-records-caesarea.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 40,
            "gold": 20
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "faith-origins.01-administrative-records-caesarea.dedication-records-1",
        "faith-origins.01-administrative-records-caesarea.dedication-records-2",
        "faith-origins.01-administrative-records-caesarea.dedication-records-3"
      ],
      "destinations": {
        "faith-origins.01-administrative-records-caesarea.dedication-records-1": "faith-origins.01-administrative-records-caesarea.destination-2",
        "faith-origins.01-administrative-records-caesarea.dedication-records-2": "faith-origins.01-administrative-records-caesarea.destination-2",
        "faith-origins.01-administrative-records-caesarea.dedication-records-3": "faith-origins.01-administrative-records-caesarea.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Materials are paid once and the register retains all three source identities.

ES: Los materiales se pagan una vez y el registro conserva las tres identidades de origen.

EN: Copy only what the record states; do not give a title the weight of a trial transcript.

ES: Copia solo lo que dice el documento; no concedas a un título el peso de una transcripción judicial.

### o3 / phase-3

EN: Deliver the derived register to the north road archive.

ES: Entrega el registro derivado en el archivo del camino norte.

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
        "faith-origins.01-administrative-records-caesarea.register-1"
      ],
      "destinations": {
        "faith-origins.01-administrative-records-caesarea.register-1": "faith-origins.01-administrative-records-caesarea.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The derived register has arrived; copying is not a second historical discovery.

ES: El registro derivado ha llegado; copiar no supone un segundo descubrimiento histórico.

EN: A careful record is a smaller victory than a grand story, and a better inheritance.

ES: Un registro cuidadoso es una victoria menor que un gran relato y una herencia mejor.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/01-administrative-records-caesarea.svg)

```json
{
  "bbox": [
    34.87,
    32.475,
    34.965,
    32.535
  ],
  "terrainProfile": "caesarea",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        119.03,
        187.94
      ],
      "lonLat": [
        34.904,
        32.497
      ],
      "name": {
        "en": "Coastal work yard",
        "es-ES": "Patio de trabajo costero"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        146.01,
        159.5
      ],
      "lonLat": [
        34.913,
        32.505
      ],
      "name": {
        "en": "Inland copying court",
        "es-ES": "Patio interior de copias"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        122.02,
        109.73
      ],
      "lonLat": [
        34.905,
        32.519
      ],
      "name": {
        "en": "North road archive",
        "es-ES": "Archivo del camino norte"
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
      "widthTiles": 10,
      "points": [
        [
          119.03,
          187.94
        ],
        [
          146.01,
          159.5
        ],
        [
          122.02,
          109.73
        ]
      ]
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
      "routePolicy": "fictional inland path established from scenario start using modern shoreline controls only; not an ancient surveyed path",
      "points": [
        [
          119.03,
          187.94
        ],
        [
          168,
          192
        ],
        [
          184,
          157
        ],
        [
          168,
          120
        ],
        [
          122.02,
          109.73
        ]
      ]
    }
  ],
  "terrainInstructions": "Mediterranean west, coastal plain east. The offshore gazetteer representative point is NOT an objective address. Keep all yards inland. No Crusader walls or modern museum; no assumption that all visible aqueduct phases existed under Pilate.",
  "corridorStraightLengthsTiles": {
    "main": 94.45,
    "relief": 94.45
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
  "schematicWaterControl": null,
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/01-administrative-records-caesarea.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.01-administrative-records-caesarea.dedication-records-1",
      "role": "fictional-administrative-dedication-copy",
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
      "id": "faith-origins.01-administrative-records-caesarea.dedication-records-2",
      "role": "fictional-administrative-dedication-copy",
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
      "id": "faith-origins.01-administrative-records-caesarea.dedication-records-3",
      "role": "fictional-administrative-dedication-copy",
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
      "id": "faith-origins.01-administrative-records-caesarea.register-1",
      "role": "derived-archive-record",
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
      "generationPolicy": "derive only from three collected fictional administrative dedication records; not modern archaeology",
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.01-administrative-records-caesarea.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.01-administrative-records-caesarea.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.01-administrative-records-caesarea.destination-3",
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
    "dedication-records": [
      "faith-origins.01-administrative-records-caesarea.dedication-records-1",
      "faith-origins.01-administrative-records-caesarea.dedication-records-2",
      "faith-origins.01-administrative-records-caesarea.dedication-records-3"
    ],
    "register": [
      "faith-origins.01-administrative-records-caesarea.register-1"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Harbor households / Hogares del puerto

EN: Bring each of the two aid crates to its assigned household at harbor households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del puerto. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Provisioning serves the working district.

ES: El auxilio sirve al barrio de trabajo.

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
          "01-administrative-records-caesarea.side-1.entity-1",
          "01-administrative-records-caesarea.side-1.entity-2"
        ],
        "destinations": {
          "01-administrative-records-caesarea.side-1.entity-1": "01-administrative-records-caesarea.side-1.zone-1",
          "01-administrative-records-caesarea.side-1.entity-2": "01-administrative-records-caesarea.side-1.zone-2"
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
        "id": "01-administrative-records-caesarea.side-1.entity-1",
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
        "id": "01-administrative-records-caesarea.side-1.entity-2",
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
        "id": "01-administrative-records-caesarea.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "01-administrative-records-caesarea.side-1.zone-2",
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
      "onceFlag": "01-administrative-records-caesarea.side-1.rewarded",
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

### Two damaged labels / Dos etiquetas dañadas

EN: Recover both separate copies from two damaged labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de dos etiquetas dañadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Preserve provenance without reconstructing missing names.

ES: Conserva la procedencia sin reconstruir nombres perdidos.

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
          "01-administrative-records-caesarea.side-2.entity-1",
          "01-administrative-records-caesarea.side-2.entity-2"
        ],
        "destinations": {
          "01-administrative-records-caesarea.side-2.entity-1": "01-administrative-records-caesarea.side-2.zone-1",
          "01-administrative-records-caesarea.side-2.entity-2": "01-administrative-records-caesarea.side-2.zone-1"
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
        "id": "01-administrative-records-caesarea.side-2.entity-1",
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
        "id": "01-administrative-records-caesarea.side-2.entity-2",
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
        "id": "01-administrative-records-caesarea.side-2.zone-1",
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
      "onceFlag": "01-administrative-records-caesarea.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.01-administrative-records-caesarea"
      ],
      "historicalNote": {
        "en": "A fragmentary inscription found at Caesarea names Pontius Pilate as prefect of Judaea and records a building dedication. It is evidence for his office, not a record of the trial of Jesus.",
        "es-ES": "Una inscripción fragmentaria hallada en Cesarea nombra a Poncio Pilato prefecto de Judea y registra una dedicación edilicia. Acredita su cargo; no documenta el proceso de Jesús."
      },
      "hint": {
        "en": "Collect three distinct fictional dedication records from the coastal work yard.",
        "es-ES": "Recoge tres registros ficticios distintos de dedicación en el patio de trabajo costero."
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

### Timber store / Almacén de vigas

EN: Pay 50 wood and restore the damaged store of timber store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén de vigas. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A local store improves finite supplies.

ES: Un almacén local mejora los suministros finitos.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "01-administrative-records-caesarea.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "01-administrative-records-caesarea.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "01-administrative-records-caesarea.side-3.payment",
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
        "id": "01-administrative-records-caesarea.side-3.entity-1",
        "role": "repair",
        "initialHub": "hub-2",
        "offsetTiles": [
          0,
          8
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
        "id": "01-administrative-records-caesarea.side-3.zone-1",
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
      "onceFlag": "01-administrative-records-caesarea.side-3.rewarded",
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

### Coastal consignment / Remesa costera

EN: Escort the trader of coastal consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de remesa costera hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Trade is distinct from the inscription evidence.

ES: El comercio es independiente de la evidencia epigráfica.

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
          "01-administrative-records-caesarea.side-4.entity-1"
        ],
        "destinations": {
          "01-administrative-records-caesarea.side-4.entity-1": "01-administrative-records-caesarea.side-4.zone-1"
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
        "receipt": "01-administrative-records-caesarea.side-4.payment",
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
        "id": "01-administrative-records-caesarea.side-4.entity-1",
        "role": "trade",
        "initialHub": "hub-1",
        "offsetTiles": [
          -2,
          -6
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "01-administrative-records-caesarea.side-4.zone-1",
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
      "onceFlag": "01-administrative-records-caesarea.side-4.rewarded",
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

### North road guide / Guía del camino norte

EN: Escort the local guide of north road guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task.

ES: Escolta al guía local de guía del camino norte hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea.

EN: Shows an inland route, never a road through the sea.

ES: Señala una ruta interior, nunca un camino por el mar.

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
          "01-administrative-records-caesarea.side-5.entity-1"
        ],
        "destinations": {
          "01-administrative-records-caesarea.side-5.entity-1": "01-administrative-records-caesarea.side-5.zone-1"
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
        "id": "01-administrative-records-caesarea.side-5.entity-1",
        "role": "guide",
        "initialHub": "hub-1",
        "offsetTiles": [
          3,
          -6
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      }
    ],
    "zones": [
      {
        "id": "01-administrative-records-caesarea.side-5.zone-1",
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
      "onceFlag": "01-administrative-records-caesarea.side-5.rewarded",
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

### Working families / Familias de trabajadores

EN: Bring both voluntary evacuee groups from working families to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de familias de trabajadores al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Voluntary relocation is a fictional activity.

ES: El traslado voluntario es una actividad ficticia.

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
          "01-administrative-records-caesarea.side-6.entity-1",
          "01-administrative-records-caesarea.side-6.entity-2"
        ],
        "destinations": {
          "01-administrative-records-caesarea.side-6.entity-1": "01-administrative-records-caesarea.side-6.zone-1",
          "01-administrative-records-caesarea.side-6.entity-2": "01-administrative-records-caesarea.side-6.zone-1"
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
        "id": "01-administrative-records-caesarea.side-6.entity-1",
        "role": "extract",
        "initialHub": "hub-3",
        "offsetTiles": [
          1,
          6
        ],
        "finite": true,
        "initiallyDelivered": false,
        "historicalPerson": false,
        "playerControllable": true
      },
      {
        "id": "01-administrative-records-caesarea.side-6.entity-2",
        "role": "extract",
        "initialHub": "hub-3",
        "offsetTiles": [
          4,
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
        "id": "01-administrative-records-caesarea.side-6.zone-1",
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
      "onceFlag": "01-administrative-records-caesarea.side-6.rewarded",
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
      "gold": 97,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1218,
      "wood": 748,
      "gold": 238,
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
      "gold": 85,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1270,
      "wood": 770,
      "gold": 250,
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
      "gold": 72,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1323,
      "wood": 793,
      "gold": 263,
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
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.title / always | none | Stone Beneath the Prefect's Name | Piedra bajo el nombre del prefecto |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.fact-intro / intro first | collection-narrator | A fragmentary inscription found at Caesarea names Pontius Pilate as prefect of Judaea and records a building dedication. It is evidence for his office, not a record of the trial of Jesus. | Una inscripción fragmentaria hallada en Cesarea nombra a Poncio Pilato prefecto de Judea y registra una dedicación edilicia. Acredita su cargo; no documenta el proceso de Jesús. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.persona-intro / after handover | miriam-archive | I copied titles as carefully as stories. I never met that prefect, and our inherited records cannot tell me everything his name now means to you. | Copié los títulos con tanto cuidado como los relatos. Nunca conocí a aquel prefecto y nuestros escritos heredados no pueden decirme todo lo que su nombre significa ahora para ti. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.route-help / available from start; repeatable without effect | none | Stay on the inland side of the coastal road. The three yards are fictional districts; the sea cannot be crossed on foot. | Permanece en el lado interior del camino costero. Los tres patios son ámbitos ficticios; no puedes cruzar el mar a pie. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.o1-goal / phase-1 active | none | Collect three distinct fictional dedication records from the coastal work yard. | Recoge tres registros ficticios distintos de dedicación en el patio de trabajo costero. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.o1-receipt / o1 latched once | none | Three separate administrative copies are registered; these are not modern excavated fragments. | Tres copias administrativas separadas están registradas; no son fragmentos excavados en la actualidad. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.o1-reaction / after o1 receipt | miriam-archive | Three copies can repeat the same mistake. Keep their offices and origins visible. | Tres copias pueden repetir el mismo error. Conserva visibles sus cargos y procedencias. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.o2-goal / phase-2 active | none | Bring the three original dedication-record bearers to the copying court, pay 40 wood and 20 gold, and issue one register from their records. | Lleva a los tres portadores originales de los registros de dedicación al patio de copias, paga 40 de madera y 20 de oro y expide un registro a partir de sus documentos. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.o2-receipt / o2 latched once | none | Materials are paid once and the register retains all three source identities. | Los materiales se pagan una vez y el registro conserva las tres identidades de origen. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.o2-reaction / after o2 receipt | miriam-archive | Copy only what the record states; do not give a title the weight of a trial transcript. | Copia solo lo que dice el documento; no concedas a un título el peso de una transcripción judicial. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.o3-goal / phase-3 active | none | Deliver the derived register to the north road archive. | Entrega el registro derivado en el archivo del camino norte. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.o3-receipt / o3 latched once | none | The derived register has arrived; copying is not a second historical discovery. | El registro derivado ha llegado; copiar no supone un segundo descubrimiento histórico. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.o3-reaction / after o3 receipt | miriam-archive | A careful record is a smaller victory than a grand story, and a better inheritance. | Un registro cuidadoso es una victoria menor que un gran relato y una herencia mejor. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at harbor households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del puerto. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-1-complete / side-1 completed | none | Harbor households completed. Its stated benefit has been granted once. | Hogares del puerto: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-1-lost / side-1 failed-optional | none | Harbor households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares del puerto: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from two damaged labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de dos etiquetas dañadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-2-complete / side-2 completed | none | Two damaged labels completed. Its stated benefit has been granted once. | Dos etiquetas dañadas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-2-lost / side-2 failed-optional | none | Two damaged labels is unavailable after the loss of its unique participant or object. The main mission continues. | Dos etiquetas dañadas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of timber store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén de vigas. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-3-complete / side-3 completed | none | Timber store completed. Its stated benefit has been granted once. | Almacén de vigas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-3-lost / side-3 failed-optional | none | Timber store is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén de vigas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-4-goal / optional list from start | none | Escort the trader of coastal consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de remesa costera hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-4-complete / side-4 completed | none | Coastal consignment completed. Its stated benefit has been granted once. | Remesa costera: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-4-lost / side-4 failed-optional | none | Coastal consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Remesa costera: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-5-goal / optional list from start | none | Escort the local guide of north road guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task. | Escolta al guía local de guía del camino norte hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-5-complete / side-5 completed | none | North road guide completed. Its stated benefit has been granted once. | Guía del camino norte: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-5-lost / side-5 failed-optional | none | North road guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del camino norte: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from working families to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de familias de trabajadores al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-6-complete / side-6 completed | none | Working families completed. Its stated benefit has been granted once. | Familias de trabajadores: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.side-6-lost / side-6 failed-optional | none | Working families is unavailable after the loss of its unique participant or object. The main mission continues. | Familias de trabajadores: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.fact-outro / victory first | collection-narrator | The inscription remains incomplete. Preserving its surviving words does not recover the missing text or establish unrelated events. | La inscripción sigue incompleta. Conservar sus palabras no recupera el texto perdido ni acredita otros acontecimientos. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.persona-outro / after fact-outro | miriam-archive | My first lesson in the archive was restraint: a title is a title, not proof of every story told about its owner. | Mi primera lección en el archivo fue la prudencia: un título es un título, no la prueba de todas las historias contadas sobre quien lo ostenta. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.01-administrative-records-caesarea.odyssey.next-episode / after persona-outro | none | Continue with When the City Held Its Breath. This episode does not complete the campaign. | Continúa con Cuando la ciudad contuvo el aliento. Este episodio no termina la campaña. |

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
    "referenceAssets": [
      "pilate-inscription-cast",
      "caesarea-aqueduct"
    ],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "register arriving before derivation: no credit",
      "only two dedication records cannot derive the register",
      "duplicate record does not reach three",
      "all activity districts remain inland",
      "Miriam never witnesses the 1961 discovery or a modern archaeological cast",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
