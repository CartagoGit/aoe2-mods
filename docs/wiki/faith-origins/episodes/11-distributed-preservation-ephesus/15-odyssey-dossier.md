# 11. The Argument Across the Water

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `11-distributed-preservation-ephesus` · c. 54–55 CE; writing location uncertain · 360×360

## Historical frame and fixed outcome

EN: Galatians presents Paul’s argument about law, circumcision and membership. Scholars dispute the recipients, date and writing place. This Ephesian preservation scene is fiction; it does not identify where Galatians was composed.

ES: Gálatas presenta la argumentación de Pablo sobre ley, circuncisión y pertenencia. Se discuten sus destinatarios, fecha y lugar de escritura. Esta escena de conservación en Éfeso es ficticia; no identifica dónde se compuso Gálatas.

EN: A fictional network has preserved its local discussion notes. The operation neither determines the letter’s provenance nor turns Paul’s polemic into an objective account of every Jewish or Christian community.

ES: Una red ficticia ha conservado sus notas locales de discusión. La operación no determina la procedencia de la carta ni convierte la polémica de Pablo en una descripción objetiva de todas las comunidades judías o cristianas.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 3,
      "episodeId": "11-distributed-preservation-ephesus",
      "order": 11,
      "selectedSourceUrl": "https://www.bibleodyssey.org/articles/galatians/",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Galatians&version=NRSVUE",
      "passage": "Galatians 1–2 and 3:1–5: Paul's argument about his commission, Abraham, law, and gentile belonging; SBL Bible Odyssey link listed in dossier was unavailable in prior consultation.",
      "supportedClaim": {
        "en": "Galatians preserves a dispute over gentile belonging, circumcision, and the law as argued by Paul.",
        "es-ES": "Gálatas conserva una disputa sobre la pertenencia gentil, la circuncisión y la ley tal como la argumenta Pablo."
      },
      "limitations": "The letter itself supports the dispute; neither its place of composition nor c.54–55 is established by these chapters. Ephesus is not securely documented as the writing location.",
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

EN: Collect four distinct local discussion notes.

ES: Recoge cuatro notas locales distintas de discusión.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "collected",
      "id": "req-1",
      "entities": [
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-1",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-2",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-3",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-4"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Four unique note identities collected.

ES: Cuatro identidades únicas de notas recogidas.

EN: Four pages are not four historical witnesses. They are objects in our reconstruction.

ES: Cuatro páginas no son cuatro testigos históricos: son objetos de nuestra reconstrucción.

### o2 / phase-2

EN: Pay 80 wood across two storage courts:40 at the north court and 40 at the south court. Deliver notes 1–2 north and 3–4 south.

ES: Paga 80 de madera entre dos patios de custodia:40 en el norte y 40 en el sur. Entrega las notas 1–2 al norte y 3–4 al sur.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 80
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.11-distributed-preservation-ephesus.destination-2",
        "faith-origins.11-distributed-preservation-ephesus.destination-3"
      ],
      "allocations": {
        "faith-origins.11-distributed-preservation-ephesus.destination-2": {
          "wood": 40
        },
        "faith-origins.11-distributed-preservation-ephesus.destination-3": {
          "wood": 40
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.11-distributed-preservation-ephesus.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-1",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-2",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-3",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-4"
      ],
      "destinations": {
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-1": "faith-origins.11-distributed-preservation-ephesus.destination-2",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-2": "faith-origins.11-distributed-preservation-ephesus.destination-2",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-3": "faith-origins.11-distributed-preservation-ephesus.destination-3",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-4": "faith-origins.11-distributed-preservation-ephesus.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Two paid storage receipts and four assigned note arrivals registered.

ES: Dos recibos de custodia pagada y cuatro llegadas asignadas registradas.

EN: Keep each destination in the ledger; one full room cannot stand for two.

ES: Conserva cada destino en el registro: una sala llena no puede contar como dos.

### o3 / phase-3

EN: Compile one local preservation register from the four collected note identities and deliver it to the inland yard.

ES: Elabora un registro local de conservación a partir de las cuatro notas recogidas y entrégalo en el patio interior.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "derived-token",
      "once": true,
      "requiresInputsCollected": true,
      "id": "req-1",
      "inputEntities": [
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-1",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-2",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-3",
        "faith-origins.11-distributed-preservation-ephesus.discussion-notes-4"
      ],
      "outputEntities": [
        "faith-origins.11-distributed-preservation-ephesus.local-preservation-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.11-distributed-preservation-ephesus.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 80
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.11-distributed-preservation-ephesus.local-preservation-register-1"
      ],
      "destinations": {
        "faith-origins.11-distributed-preservation-ephesus.local-preservation-register-1": "faith-origins.11-distributed-preservation-ephesus.destination-1"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: One derived register returned; no canonical autograph is represented.

ES: Un registro derivado ha regresado; no se representa ningún autógrafo canónico.

EN: I record what our fiction kept, and mark what our evidence cannot decide.

ES: Registro lo que conserva nuestra ficción y señalo lo que la evidencia no permite decidir.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/11-distributed-preservation-ephesus.svg)

```json
{
  "bbox": [
    27.255,
    37.875,
    27.405,
    37.995
  ],
  "terrainProfile": "ephesus",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        219.53,
        166.14
      ],
      "lonLat": [
        27.349,
        37.94
      ],
      "name": {
        "en": "Inland discussion yard",
        "es-ES": "Patio interior de discusión"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        242.7,
        78.0
      ],
      "lonLat": [
        27.36,
        37.973
      ],
      "name": {
        "en": "Northern storage district",
        "es-ES": "Barrio septentrional de custodia"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        217.42,
        267.65
      ],
      "lonLat": [
        27.348,
        37.902
      ],
      "name": {
        "en": "Southern road storage court",
        "es-ES": "Patio de custodia del camino sur"
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
  "terrainInstructions": "Northern and southern inland storage branches remain east of hypothetical ancient estuary water. No Celsus library, later churches or modern Selcuk. Modern shoreline cannot define first-century harbor; obtain dated estuary control before carving westward relief corridor.",
  "corridorStraightLengthsTiles": {
    "main": 282.46,
    "relief": 282.46
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
  "asset": "docs/design/maps/faith-origins/odyssey/11-distributed-preservation-ephesus.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.11-distributed-preservation-ephesus.discussion-notes-1",
      "role": "fictional-contemporary-discussion-note",
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
      "id": "faith-origins.11-distributed-preservation-ephesus.discussion-notes-2",
      "role": "fictional-contemporary-discussion-note",
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
      "id": "faith-origins.11-distributed-preservation-ephesus.discussion-notes-3",
      "role": "fictional-contemporary-discussion-note",
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
      "id": "faith-origins.11-distributed-preservation-ephesus.discussion-notes-4",
      "role": "fictional-contemporary-discussion-note",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.11-distributed-preservation-ephesus.local-preservation-register-1",
      "role": "fictional-preservation-register",
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
    }
  ],
  "zones": [
    {
      "id": "faith-origins.11-distributed-preservation-ephesus.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.11-distributed-preservation-ephesus.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.11-distributed-preservation-ephesus.destination-3",
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
    "discussion-notes": [
      "faith-origins.11-distributed-preservation-ephesus.discussion-notes-1",
      "faith-origins.11-distributed-preservation-ephesus.discussion-notes-2",
      "faith-origins.11-distributed-preservation-ephesus.discussion-notes-3",
      "faith-origins.11-distributed-preservation-ephesus.discussion-notes-4"
    ],
    "local-preservation-register": [
      "faith-origins.11-distributed-preservation-ephesus.local-preservation-register-1"
    ]
  },
  "survivorGroups": [],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Parallel discussion copies / Copias paralelas de discusión

EN: Recover both separate copies from parallel discussion copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de copias paralelas de discusión y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Fictional notes supply an attributed contextual comparison, not newly discovered ancient evidence.

ES: Las notas ficticias aportan una comparación contextual atribuida, no nueva evidencia antigua.

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
          "11-distributed-preservation-ephesus.side-1.entity-1",
          "11-distributed-preservation-ephesus.side-1.entity-2"
        ],
        "destinations": {
          "11-distributed-preservation-ephesus.side-1.entity-1": "11-distributed-preservation-ephesus.side-1.zone-1",
          "11-distributed-preservation-ephesus.side-1.entity-2": "11-distributed-preservation-ephesus.side-1.zone-1"
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
        "id": "11-distributed-preservation-ephesus.side-1.entity-1",
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
        "id": "11-distributed-preservation-ephesus.side-1.entity-2",
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
        "id": "11-distributed-preservation-ephesus.side-1.zone-1",
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
      "onceFlag": "11-distributed-preservation-ephesus.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.11-distributed-preservation-ephesus"
      ],
      "historicalNote": {
        "en": "Galatians presents Paul’s argument about law, circumcision and membership. Scholars dispute the recipients, date and writing place. This Ephesian preservation scene is fiction; it does not identify where Galatians was composed.",
        "es-ES": "Gálatas presenta la argumentación de Pablo sobre ley, circuncisión y pertenencia. Se discuten sus destinatarios, fecha y lugar de escritura. Esta escena de conservación en Éfeso es ficticia; no identifica dónde se compuso Gálatas."
      },
      "hint": {
        "en": "Collect four distinct local discussion notes.",
        "es-ES": "Recoge cuatro notas locales distintas de discusión."
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

### Northern store roof / Tejado del almacén norte

EN: Pay 50 wood and restore the damaged store of northern store roof to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de tejado del almacén norte. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair and main storage payment have separate identities/receipts.

ES: La reparación y el pago principal de custodia tienen identidades y recibos separados.

```json
{
  "id": "side-2",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "11-distributed-preservation-ephesus.side-2.entity-1",
        "health": "full",
        "paymentReceipt": "11-distributed-preservation-ephesus.side-2.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "11-distributed-preservation-ephesus.side-2.payment",
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
        "id": "11-distributed-preservation-ephesus.side-2.entity-1",
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
        "id": "11-distributed-preservation-ephesus.side-2.zone-1",
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
      "onceFlag": "11-distributed-preservation-ephesus.side-2.rewarded",
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

### Southern work households / Hogares de trabajo del sur

EN: Bring each of the two aid crates to its assigned household at southern work households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de trabajo del sur. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid does not change the controversy or favor a theology by force.

ES: La ayuda no altera la controversia ni favorece una teología por la fuerza.

```json
{
  "id": "side-3",
  "kind": "aid",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "11-distributed-preservation-ephesus.side-3.entity-1",
          "11-distributed-preservation-ephesus.side-3.entity-2"
        ],
        "destinations": {
          "11-distributed-preservation-ephesus.side-3.entity-1": "11-distributed-preservation-ephesus.side-3.zone-1",
          "11-distributed-preservation-ephesus.side-3.entity-2": "11-distributed-preservation-ephesus.side-3.zone-2"
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
        "id": "11-distributed-preservation-ephesus.side-3.entity-1",
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
        "id": "11-distributed-preservation-ephesus.side-3.entity-2",
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
        "id": "11-distributed-preservation-ephesus.side-3.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "11-distributed-preservation-ephesus.side-3.zone-2",
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
      "onceFlag": "11-distributed-preservation-ephesus.side-3.rewarded",
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

### Eastern slope guide / Guía de la ladera oriental

EN: Escort the local guide of eastern slope guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task.

ES: Escolta al guía local de guía de la ladera oriental hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea.

EN: A surveyed land detour avoids assuming a walk through ancient harbor water.

ES: Un desvío terrestre comprobado evita asumir un paseo por las aguas del puerto antiguo.

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
          "11-distributed-preservation-ephesus.side-4.entity-1"
        ],
        "destinations": {
          "11-distributed-preservation-ephesus.side-4.entity-1": "11-distributed-preservation-ephesus.side-4.zone-1"
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
        "id": "11-distributed-preservation-ephesus.side-4.entity-1",
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
        "id": "11-distributed-preservation-ephesus.side-4.zone-1",
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
      "onceFlag": "11-distributed-preservation-ephesus.side-4.rewarded",
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

### Independent archive helpers / Ayudantes independientes del archivo

EN: Bring both voluntary evacuee groups from independent archive helpers to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de ayudantes independientes del archivo al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Voluntary helpers are not sacred figures and cannot replace main notes.

ES: Los ayudantes voluntarios no son figuras veneradas ni sustituyen las notas principales.

```json
{
  "id": "side-5",
  "kind": "extract",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "11-distributed-preservation-ephesus.side-5.entity-1",
          "11-distributed-preservation-ephesus.side-5.entity-2"
        ],
        "destinations": {
          "11-distributed-preservation-ephesus.side-5.entity-1": "11-distributed-preservation-ephesus.side-5.zone-1",
          "11-distributed-preservation-ephesus.side-5.entity-2": "11-distributed-preservation-ephesus.side-5.zone-1"
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
        "id": "11-distributed-preservation-ephesus.side-5.entity-1",
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
        "id": "11-distributed-preservation-ephesus.side-5.entity-2",
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
        "id": "11-distributed-preservation-ephesus.side-5.zone-1",
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
      "onceFlag": "11-distributed-preservation-ephesus.side-5.rewarded",
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

### Ink and grain consignment / Remesa de tinta y grano

EN: Escort the trader of ink and grain consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de remesa de tinta y grano hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One fictional exchange offers finite food, not access to an authentic apostolic original.

ES: Un intercambio ficticio ofrece alimento finito, no acceso a un original apostólico auténtico.

```json
{
  "id": "side-6",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "11-distributed-preservation-ephesus.side-6.entity-1"
        ],
        "destinations": {
          "11-distributed-preservation-ephesus.side-6.entity-1": "11-distributed-preservation-ephesus.side-6.zone-1"
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
        "receipt": "11-distributed-preservation-ephesus.side-6.payment",
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
        "id": "11-distributed-preservation-ephesus.side-6.entity-1",
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
        "id": "11-distributed-preservation-ephesus.side-6.zone-1",
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
      "onceFlag": "11-distributed-preservation-ephesus.side-6.rewarded",
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
      "id": "distributed-stewardship",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Survey two storage branches and improve independent supplies; two exact receiving allocations remain mandatory."
    },
    {
      "id": "critical-copying",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Choose comparison/context and bounded trade without claiming a resolved dating dispute."
    },
    {
      "id": "community-support",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Support separate households/helpers while the north/south note teams operate."
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
      "wood": 788,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
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
      "wood": 760,
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
      "wood": 810,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
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
      "wood": 760,
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
      "wood": 833,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
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
      "wood": 760,
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
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.title / always | none | The Argument Across the Water | La disputa al otro lado del agua |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.fact-intro / intro first | collection-narrator | Galatians presents Paul’s argument about law, circumcision and membership. Scholars dispute the recipients, date and writing place. This Ephesian preservation scene is fiction; it does not identify where Galatians was composed. | Gálatas presenta la argumentación de Pablo sobre ley, circuncisión y pertenencia. Se discuten sus destinatarios, fecha y lugar de escritura. Esta escena de conservación en Éfeso es ficticia; no identifica dónde se compuso Gálatas. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.persona-intro / after handover | miriam-archive | I once copied an argument so impatiently that I left out the question it answered. I kept the scar of that mistake. Here I will preserve disagreement rather than pretend a map settles it. | Una vez copié un argumento con tanta impaciencia que omití la pregunta a la que respondía. Conservé la marca de aquel error. Aquí guardaré el desacuerdo, sin fingir que un mapa lo resuelve. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.route-help / available from start; repeatable without effect | none | Split the four assigned notes between northern and southern land storage courts. The register returns inland; the writing place of Galatians is not established by this map. | Reparte las cuatro notas asignadas entre los patios terrestres del norte y sur. El registro vuelve al interior; este mapa no establece el lugar de escritura de Gálatas. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.o1-goal / phase-1 active | none | Collect four distinct local discussion notes. | Recoge cuatro notas locales distintas de discusión. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.o1-receipt / o1 latched once | none | Four unique note identities collected. | Cuatro identidades únicas de notas recogidas. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.o1-reaction / after o1 receipt | miriam-archive | Four pages are not four historical witnesses. They are objects in our reconstruction. | Cuatro páginas no son cuatro testigos históricos: son objetos de nuestra reconstrucción. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.o2-goal / phase-2 active | none | Pay 80 wood across two storage courts:40 at the north court and 40 at the south court. Deliver notes 1–2 north and 3–4 south. | Paga 80 de madera entre dos patios de custodia:40 en el norte y 40 en el sur. Entrega las notas 1–2 al norte y 3–4 al sur. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.o2-receipt / o2 latched once | none | Two paid storage receipts and four assigned note arrivals registered. | Dos recibos de custodia pagada y cuatro llegadas asignadas registradas. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.o2-reaction / after o2 receipt | miriam-archive | Keep each destination in the ledger; one full room cannot stand for two. | Conserva cada destino en el registro: una sala llena no puede contar como dos. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.o3-goal / phase-3 active | none | Compile one local preservation register from the four collected note identities and deliver it to the inland yard. | Elabora un registro local de conservación a partir de las cuatro notas recogidas y entrégalo en el patio interior. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.o3-receipt / o3 latched once | none | One derived register returned; no canonical autograph is represented. | Un registro derivado ha regresado; no se representa ningún autógrafo canónico. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.o3-reaction / after o3 receipt | miriam-archive | I record what our fiction kept, and mark what our evidence cannot decide. | Registro lo que conserva nuestra ficción y señalo lo que la evidencia no permite decidir. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from parallel discussion copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de copias paralelas de discusión y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-1-complete / side-1 completed | none | Parallel discussion copies completed. Its stated benefit has been granted once. | Copias paralelas de discusión: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-1-lost / side-1 failed-optional | none | Parallel discussion copies is unavailable after the loss of its unique participant or object. The main mission continues. | Copias paralelas de discusión: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-2-goal / optional list from start | none | Pay 50 wood and restore the damaged store of northern store roof to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de tejado del almacén norte. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-2-complete / side-2 completed | none | Northern store roof completed. Its stated benefit has been granted once. | Tejado del almacén norte: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-2-lost / side-2 failed-optional | none | Northern store roof is unavailable after the loss of its unique participant or object. The main mission continues. | Tejado del almacén norte: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at southern work households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares de trabajo del sur. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-3-complete / side-3 completed | none | Southern work households completed. Its stated benefit has been granted once. | Hogares de trabajo del sur: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-3-lost / side-3 failed-optional | none | Southern work households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares de trabajo del sur: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-4-goal / optional list from start | none | Escort the local guide of eastern slope guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task. | Escolta al guía local de guía de la ladera oriental hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-4-complete / side-4 completed | none | Eastern slope guide completed. Its stated benefit has been granted once. | Guía de la ladera oriental: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-4-lost / side-4 failed-optional | none | Eastern slope guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía de la ladera oriental: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-5-goal / optional list from start | none | Bring both voluntary evacuee groups from independent archive helpers to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de ayudantes independientes del archivo al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-5-complete / side-5 completed | none | Independent archive helpers completed. Its stated benefit has been granted once. | Ayudantes independientes del archivo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-5-lost / side-5 failed-optional | none | Independent archive helpers is unavailable after the loss of its unique participant or object. The main mission continues. | Ayudantes independientes del archivo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-6-goal / optional list from start | none | Escort the trader of ink and grain consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de remesa de tinta y grano hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-6-complete / side-6 completed | none | Ink and grain consignment completed. Its stated benefit has been granted once. | Remesa de tinta y grano: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.side-6-lost / side-6 failed-optional | none | Ink and grain consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Remesa de tinta y grano: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.fact-outro / victory first | collection-narrator | A fictional network has preserved its local discussion notes. The operation neither determines the letter’s provenance nor turns Paul’s polemic into an objective account of every Jewish or Christian community. | Una red ficticia ha conservado sus notas locales de discusión. La operación no determina la procedencia de la carta ni convierte la polémica de Pablo en una descripción objetiva de todas las comunidades judías o cristianas. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.persona-outro / after fact-outro | miriam-archive | To preserve a voice is not to give it every other voice. I leave the edges of this account visible, because I have learned what a confident omission can destroy. | Conservar una voz no es atribuirle todas las demás. Dejo visibles los bordes de este relato: he aprendido cuánto puede destruir una omisión segura de sí misma. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.11-distributed-preservation-ephesus.odyssey.next-episode / after persona-outro | none | Continue with Many Hands in One House. This episode does not complete the campaign. | Continúa con Muchas manos en una casa. Este episodio no termina la campaña. |

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
      "all four notes at one court cannot win",
      "north/south payment allocations must both complete atomically",
      "no direct canon originals as gameplay notes",
      "Ephesus remains explicitly fictional local setting, not proven letter composition",
      "modern and ancient shoreline separately labeled",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
