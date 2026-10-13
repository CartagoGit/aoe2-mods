# 5. Fifteen Days, Many Voices

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `05-witness-comparison-jerusalem` · c. 36–40 CE · 320×320

## Historical frame and fixed outcome

EN: In Galatians, Paul reports visiting Jerusalem, spending fifteen days with Cephas and meeting James. His relative chronology leaves the calendar date uncertain.

ES: En Gálatas, Pablo informa de una visita a Jerusalén, quince días con Cefas y un encuentro con Santiago. Su cronología relativa deja incierta la fecha de calendario.

EN: The exercise distinguishes the claims in Paul’s surviving account from fictional archival notes. It supplies no independent transcript of the meetings.

ES: El ejercicio distingue las afirmaciones del relato conservado de Pablo de notas archivísticas ficticias. No aporta una transcripción independiente de los encuentros.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 28,
      "episodeId": "05-witness-comparison-jerusalem",
      "order": 5,
      "selectedSourceUrl": "https://www.biblegateway.com/passage/?search=Galatians+1%3A18-19&version=NIV%3BNRSVUE%3BKJV%3BNKJV",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Galatians+1%3A18-19&version=NRSVUE",
      "passage": "Galatians 1:18–19, especially Paul's 'fifteen days' and named contacts; Yale Bible Study chronology page consulted for the broader chronology anchor (Gallio/Delphi).",
      "supportedClaim": {
        "en": "Paul reports a Jerusalem visit, a fifteen-day stay with Cephas, and seeing James.",
        "es-ES": "Pablo informa de una visita a Jerusalén, una estancia de quince días con Cefas y un encuentro con Santiago."
      },
      "limitations": "This repeats the preceding episode's source/event and should be made a distinct editorial angle or treated as duplicate. Relative interval and date of Paul's call remain uncertain; the Yale overview does not make the exact year certain.",
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

EN: Collect three distinct fictional attendance notes for the local visit. Galatians is a later source for the narrator, not a map object.

ES: Recoge tres notas ficticias distintas de asistencia a la visita local. Gálatas es una fuente posterior del narrador, no un objeto del mapa.

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
        "faith-origins.05-witness-comparison-jerusalem.comparison-notes-1",
        "faith-origins.05-witness-comparison-jerusalem.comparison-notes-2",
        "faith-origins.05-witness-comparison-jerusalem.comparison-notes-3"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three fictional working notes are separate gameplay objects, not three historical testimonies.

ES: Tres notas de trabajo ficticias son objetos jugables separados, no tres testimonios históricos.

EN: More pages do not always mean more witnesses.

ES: Más páginas no siempre significan más testigos.

### o2 / phase-2

EN: Fund comparison with 30 wood and derive one qualified summary using all three notes.

ES: Financia la comparación con 30 de madera y prepara un resumen matizado usando las tres notas.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 30
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.05-witness-comparison-jerusalem.destination-2"
      ],
      "allocations": {
        "faith-origins.05-witness-comparison-jerusalem.destination-2": {
          "wood": 30
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.05-witness-comparison-jerusalem.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "id": "req-2",
      "inputEntities": [
        "faith-origins.05-witness-comparison-jerusalem.comparison-notes-1",
        "faith-origins.05-witness-comparison-jerusalem.comparison-notes-2",
        "faith-origins.05-witness-comparison-jerusalem.comparison-notes-3"
      ],
      "outputEntities": [
        "faith-origins.05-witness-comparison-jerusalem.qualified-summary-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.05-witness-comparison-jerusalem.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 30
          },
          "newDebit": false
        }
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The fictional visit summary is complete. It is not a surviving first-century document.

ES: El resumen ficticio de la visita está completo. No es un documento del siglo I conservado.

EN: A date can stay uncertain without the record being useless.

ES: Una fecha puede seguir incierta sin que el registro resulte inútil.

### o3 / phase-3

EN: Deliver the qualified summary to the south copy register.

ES: Entrega el resumen matizado en el registro de copias del sur.

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
        "faith-origins.05-witness-comparison-jerusalem.qualified-summary-1"
      ],
      "destinations": {
        "faith-origins.05-witness-comparison-jerusalem.qualified-summary-1": "faith-origins.05-witness-comparison-jerusalem.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The fictional visit summary reached the local receiving register.

ES: El resumen ficticio de la visita llega al registro receptor local.

EN: Leave the uncertain year visible beside the fifteen days.

ES: Deja visible el año incierto junto a los quince días.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/05-witness-comparison-jerusalem.svg)

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
        167.07,
        116.78
      ],
      "lonLat": [
        35.215,
        31.804
      ],
      "name": {
        "en": "Northwest archive stores",
        "es-ES": "Depósitos del archivo noroeste"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        168.58,
        154.16
      ],
      "lonLat": [
        35.216,
        31.783
      ],
      "name": {
        "en": "Western comparison court",
        "es-ES": "Patio occidental de comparación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        186.74,
        204.0
      ],
      "lonLat": [
        35.228,
        31.755
      ],
      "name": {
        "en": "South copy register",
        "es-ES": "Registro de copias meridional"
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
  "terrainInstructions": "Plateau archive reconstruction with west/south land movement, not an asserted archaeological school. No playable Cephas, James or Paul; meetings remain in attributed context.",
  "mainRouteLengthStraightTiles": 90.46,
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
  "asset": "docs/design/maps/faith-origins/odyssey/05-witness-comparison-jerusalem.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.05-witness-comparison-jerusalem.comparison-notes-1",
      "role": "fictional-contemporary-attendance-note",
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
      "id": "faith-origins.05-witness-comparison-jerusalem.comparison-notes-2",
      "role": "fictional-contemporary-attendance-note",
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
      "id": "faith-origins.05-witness-comparison-jerusalem.comparison-notes-3",
      "role": "fictional-contemporary-attendance-note",
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
      "id": "faith-origins.05-witness-comparison-jerusalem.qualified-summary-1",
      "role": "fictional-derived-visit-summary",
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
      "generationPolicy": "derive only from all three collected notes; none is an independent ancient transcript",
      "historicalMaterialPolicy": "fictional local working record or participant; never a surviving ancient original, later canonical book, literal source transcript or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.05-witness-comparison-jerusalem.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.05-witness-comparison-jerusalem.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.05-witness-comparison-jerusalem.destination-3",
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
    "comparison-notes": [
      "faith-origins.05-witness-comparison-jerusalem.comparison-notes-1",
      "faith-origins.05-witness-comparison-jerusalem.comparison-notes-2",
      "faith-origins.05-witness-comparison-jerusalem.comparison-notes-3"
    ],
    "qualified-summary": [
      "faith-origins.05-witness-comparison-jerusalem.qualified-summary-1"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Archive households / Hogares del archivo

EN: Bring each of the two aid crates to its assigned household at archive households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del archivo. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Supplies serve fictional archival workers.

ES: Los suministros sirven a trabajadores archivísticos ficticios.

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
          "05-witness-comparison-jerusalem.side-1.entity-1",
          "05-witness-comparison-jerusalem.side-1.entity-2"
        ],
        "destinations": {
          "05-witness-comparison-jerusalem.side-1.entity-1": "05-witness-comparison-jerusalem.side-1.zone-1",
          "05-witness-comparison-jerusalem.side-1.entity-2": "05-witness-comparison-jerusalem.side-1.zone-2"
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
        "id": "05-witness-comparison-jerusalem.side-1.entity-1",
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
        "id": "05-witness-comparison-jerusalem.side-1.entity-2",
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
        "id": "05-witness-comparison-jerusalem.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "05-witness-comparison-jerusalem.side-1.zone-2",
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
      "onceFlag": "05-witness-comparison-jerusalem.side-1.rewarded",
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

### Catalog labels / Etiquetas del catálogo

EN: Recover both separate copies from catalog labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de etiquetas del catálogo y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Two labels preserve source attribution.

ES: Dos etiquetas conservan la atribución de la fuente.

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
          "05-witness-comparison-jerusalem.side-2.entity-1",
          "05-witness-comparison-jerusalem.side-2.entity-2"
        ],
        "destinations": {
          "05-witness-comparison-jerusalem.side-2.entity-1": "05-witness-comparison-jerusalem.side-2.zone-1",
          "05-witness-comparison-jerusalem.side-2.entity-2": "05-witness-comparison-jerusalem.side-2.zone-1"
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
        "id": "05-witness-comparison-jerusalem.side-2.entity-1",
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
        "id": "05-witness-comparison-jerusalem.side-2.entity-2",
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
        "id": "05-witness-comparison-jerusalem.side-2.zone-1",
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
      "onceFlag": "05-witness-comparison-jerusalem.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.05-witness-comparison-jerusalem"
      ],
      "historicalNote": {
        "en": "In Galatians, Paul reports visiting Jerusalem, spending fifteen days with Cephas and meeting James. His relative chronology leaves the calendar date uncertain.",
        "es-ES": "En Gálatas, Pablo informa de una visita a Jerusalén, quince días con Cefas y un encuentro con Santiago. Su cronología relativa deja incierta la fecha de calendario."
      },
      "hint": {
        "en": "Collect three distinct fictional attendance notes for the local visit. Galatians is a later source for the narrator, not a map object.",
        "es-ES": "Recoge tres notas ficticias distintas de asistencia a la visita local. Gálatas es una fuente posterior del narrador, no un objeto del mapa."
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

### Comparison shelves / Estantes de comparación

EN: Pay 50 wood and restore the damaged store of comparison shelves to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de estantes de comparación. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Restore finite archival infrastructure.

ES: Restaura infraestructura archivística finita.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "05-witness-comparison-jerusalem.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "05-witness-comparison-jerusalem.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "05-witness-comparison-jerusalem.side-3.payment",
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
        "id": "05-witness-comparison-jerusalem.side-3.entity-1",
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
        "id": "05-witness-comparison-jerusalem.side-3.zone-1",
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
      "onceFlag": "05-witness-comparison-jerusalem.side-3.rewarded",
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

### Writing supplies / Materiales de escritura

EN: Escort the trader of writing supplies to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de materiales de escritura hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Local trade does not produce new historical evidence.

ES: El comercio local no produce pruebas históricas nuevas.

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
          "05-witness-comparison-jerusalem.side-4.entity-1"
        ],
        "destinations": {
          "05-witness-comparison-jerusalem.side-4.entity-1": "05-witness-comparison-jerusalem.side-4.zone-1"
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
        "receipt": "05-witness-comparison-jerusalem.side-4.payment",
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
        "id": "05-witness-comparison-jerusalem.side-4.entity-1",
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
        "id": "05-witness-comparison-jerusalem.side-4.zone-1",
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
      "onceFlag": "05-witness-comparison-jerusalem.side-4.rewarded",
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

### Plateau messenger guide / Guía de mensajeros de la meseta

EN: Escort the local guide of plateau messenger guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía de mensajeros de la meseta hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: Alternate land access helps movement.

ES: El acceso terrestre alternativo facilita el movimiento.

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
          "05-witness-comparison-jerusalem.side-5.entity-1"
        ],
        "destinations": {
          "05-witness-comparison-jerusalem.side-5.entity-1": "05-witness-comparison-jerusalem.side-5.zone-1"
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
        "id": "05-witness-comparison-jerusalem.side-5.entity-1",
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
        "id": "05-witness-comparison-jerusalem.side-5.zone-1",
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
      "onceFlag": "05-witness-comparison-jerusalem.side-5.rewarded",
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

### Guest copyists / Copistas huéspedes

EN: Bring both voluntary evacuee groups from guest copyists to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de copistas huéspedes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Offer voluntary lodging to distinct optional participants.

ES: Ofrece alojamiento voluntario a participantes opcionales distintos.

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
          "05-witness-comparison-jerusalem.side-6.entity-1",
          "05-witness-comparison-jerusalem.side-6.entity-2"
        ],
        "destinations": {
          "05-witness-comparison-jerusalem.side-6.entity-1": "05-witness-comparison-jerusalem.side-6.zone-1",
          "05-witness-comparison-jerusalem.side-6.entity-2": "05-witness-comparison-jerusalem.side-6.zone-1"
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
        "id": "05-witness-comparison-jerusalem.side-6.entity-1",
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
        "id": "05-witness-comparison-jerusalem.side-6.entity-2",
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
        "id": "05-witness-comparison-jerusalem.side-6.zone-1",
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
      "onceFlag": "05-witness-comparison-jerusalem.side-6.rewarded",
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
      "food": 1218,
      "wood": 738,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 30,
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
      "food": 1070,
      "wood": 710,
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
      "food": 1270,
      "wood": 760,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 30,
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
      "food": 1070,
      "wood": 710,
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
      "food": 1323,
      "wood": 783,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 30,
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
      "food": 1070,
      "wood": 710,
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
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.title / always | none | Fifteen Days, Many Voices | Quince días, muchas voces |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.fact-intro / intro first | collection-narrator | In Galatians, Paul reports visiting Jerusalem, spending fifteen days with Cephas and meeting James. His relative chronology leaves the calendar date uncertain. | En Gálatas, Pablo informa de una visita a Jerusalén, quince días con Cefas y un encuentro con Santiago. Su cronología relativa deja incierta la fecha de calendario. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.persona-intro / after handover | miriam-archive | Fifteen days: a precise memory inside an uncertain calendar. I have learned not to mistake one kind of precision for another. | Quince días: un recuerdo preciso dentro de un calendario incierto. He aprendido a no confundir una clase de precisión con otra. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.route-help / available from start; repeatable without effect | none | Compare sources in the western court, then use the southern land route. Three gameplay notes do not create three historical witnesses. | Compara las fuentes en el patio occidental y sigue la ruta terrestre del sur. Tres notas jugables no crean tres testigos históricos. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.o1-goal / phase-1 active | none | Collect three distinct fictional attendance notes for the local visit. Galatians is a later source for the narrator, not a map object. | Recoge tres notas ficticias distintas de asistencia a la visita local. Gálatas es una fuente posterior del narrador, no un objeto del mapa. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.o1-receipt / o1 latched once | none | Three fictional working notes are separate gameplay objects, not three historical testimonies. | Tres notas de trabajo ficticias son objetos jugables separados, no tres testimonios históricos. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.o1-reaction / after o1 receipt | miriam-archive | More pages do not always mean more witnesses. | Más páginas no siempre significan más testigos. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.o2-goal / phase-2 active | none | Fund comparison with 30 wood and derive one qualified summary using all three notes. | Financia la comparación con 30 de madera y prepara un resumen matizado usando las tres notas. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.o2-receipt / o2 latched once | none | The fictional visit summary is complete. It is not a surviving first-century document. | El resumen ficticio de la visita está completo. No es un documento del siglo I conservado. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.o2-reaction / after o2 receipt | miriam-archive | A date can stay uncertain without the record being useless. | Una fecha puede seguir incierta sin que el registro resulte inútil. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.o3-goal / phase-3 active | none | Deliver the qualified summary to the south copy register. | Entrega el resumen matizado en el registro de copias del sur. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.o3-receipt / o3 latched once | none | The fictional visit summary reached the local receiving register. | El resumen ficticio de la visita llega al registro receptor local. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.o3-reaction / after o3 receipt | miriam-archive | Leave the uncertain year visible beside the fifteen days. | Deja visible el año incierto junto a los quince días. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at archive households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares del archivo. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-1-complete / side-1 completed | none | Archive households completed. Its stated benefit has been granted once. | Hogares del archivo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-1-lost / side-1 failed-optional | none | Archive households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares del archivo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from catalog labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de etiquetas del catálogo y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-2-complete / side-2 completed | none | Catalog labels completed. Its stated benefit has been granted once. | Etiquetas del catálogo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-2-lost / side-2 failed-optional | none | Catalog labels is unavailable after the loss of its unique participant or object. The main mission continues. | Etiquetas del catálogo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of comparison shelves to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de estantes de comparación. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-3-complete / side-3 completed | none | Comparison shelves completed. Its stated benefit has been granted once. | Estantes de comparación: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-3-lost / side-3 failed-optional | none | Comparison shelves is unavailable after the loss of its unique participant or object. The main mission continues. | Estantes de comparación: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-4-goal / optional list from start | none | Escort the trader of writing supplies to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de materiales de escritura hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-4-complete / side-4 completed | none | Writing supplies completed. Its stated benefit has been granted once. | Materiales de escritura: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-4-lost / side-4 failed-optional | none | Writing supplies is unavailable after the loss of its unique participant or object. The main mission continues. | Materiales de escritura: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-5-goal / optional list from start | none | Escort the local guide of plateau messenger guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía de mensajeros de la meseta hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-5-complete / side-5 completed | none | Plateau messenger guide completed. Its stated benefit has been granted once. | Guía de mensajeros de la meseta: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-5-lost / side-5 failed-optional | none | Plateau messenger guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía de mensajeros de la meseta: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from guest copyists to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de copistas huéspedes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-6-complete / side-6 completed | none | Guest copyists completed. Its stated benefit has been granted once. | Copistas huéspedes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.side-6-lost / side-6 failed-optional | none | Guest copyists is unavailable after the loss of its unique participant or object. The main mission continues. | Copistas huéspedes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.fact-outro / victory first | collection-narrator | The exercise distinguishes the claims in Paul’s surviving account from fictional archival notes. It supplies no independent transcript of the meetings. | El ejercicio distingue las afirmaciones del relato conservado de Pablo de notas archivísticas ficticias. No aporta una transcripción independiente de los encuentros. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.persona-outro / after fact-outro | miriam-archive | I would rather preserve a speaker and a limit than make a tidy chronology no source can carry. | Prefiero conservar una voz y un límite antes que ordenar una cronología que ninguna fuente sostiene. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.05-witness-comparison-jerusalem.odyssey.next-episode / after persona-outro | none | Continue with Letters on the Orontes. This episode does not complete the campaign. | Continúa con Cartas sobre el Orontes. Este episodio no termina la campaña. |

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
      "two notes cannot derive summary",
      "a summary arriving before derivation earns nothing",
      "fictional notes do not become independent source claims",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
