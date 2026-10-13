# 14. The Appeal Beside the Sea

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `14-administrative-intrigue-caesarea` · c. 57–60 CE · 340×340

## Historical frame and fixed outcome

EN: In Acts, Paul appeals to Caesar while held at Caesarea under Festus. It is a later literary account, not a surviving court transcript. The administrative courier work here is fictional and does not control the historical appeal’s outcome.

ES: En Hechos, Pablo apela al César mientras está detenido en Cesarea bajo Festo. Es un relato literario posterior, no una transcripción judicial conservada. El trabajo de correo administrativo es ficticio y no controla el resultado de la apelación histórica.

EN: The fictional records have been dispatched within the Caesarea setting. Their delivery neither authenticates Acts as a court transcript nor changes Paul’s narrated appeal or subsequent journey.

ES: Los registros ficticios se han enviado dentro de la ambientación de Cesarea. Su entrega no autentica Hechos como transcripción judicial ni altera la apelación narrada de Pablo o su viaje posterior.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 6,
      "episodeId": "14-administrative-intrigue-caesarea",
      "order": 14,
      "selectedSourceUrl": "https://www.perseus.tufts.edu/hopper/text?doc=Acts+21",
      "consultedUrl": "https://www.biblegateway.com/passage/?search=Acts+25%3A10-12&version=NRSVUE",
      "passage": "Acts 25:10–12: Paul invokes his appeal to Caesar before Festus; Acts 21–26 gives the preceding detention narrative.",
      "supportedClaim": {
        "en": "In Acts' narrative, Paul appeals to Caesar before Festus while held at Caesarea.",
        "es-ES": "En el relato de Hechos, Pablo apela al César ante Festo mientras está detenido en Cesarea."
      },
      "limitations": "This is a theological narrative, not a surviving court transcript. The appeal passage supports the appeal, not every claim about causes, dates, or legal procedure; use Caesarea as scene, not Jerusalem after departure.",
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

EN: Collect three distinct local administrative notes and take them to the record-office yard.

ES: Recoge tres notas administrativas locales distintas y llévalas al patio de registro.

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
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-1",
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-2",
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-1",
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-2",
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-3"
      ],
      "destinations": {
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-1": "faith-origins.14-administrative-intrigue-caesarea.destination-2",
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-2": "faith-origins.14-administrative-intrigue-caesarea.destination-2",
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-3": "faith-origins.14-administrative-intrigue-caesarea.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three original fictional notes reached the record office.

ES: Tres notas ficticias originales han llegado al registro.

EN: They are neither a court transcript nor an appeal signed by Paul.

ES: No son una transcripción judicial ni una apelación firmada por Pablo.

### o2 / phase-2

EN: Pay 40 wood and 20 gold once and derive one local dispatch register from the three notes.

ES: Paga una sola vez 40 de madera y 20 de oro y elabora un registro local de envío a partir de las tres notas.

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
        "faith-origins.14-administrative-intrigue-caesarea.destination-2"
      ],
      "allocations": {
        "faith-origins.14-administrative-intrigue-caesarea.destination-2": {
          "wood": 40,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.14-administrative-intrigue-caesarea.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "requiresInputsCollected": true,
      "id": "req-2",
      "inputEntities": [
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-1",
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-2",
        "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-3"
      ],
      "outputEntities": [
        "faith-origins.14-administrative-intrigue-caesarea.local-dispatch-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.14-administrative-intrigue-caesarea.o2.req-1.paid",
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

EN: One administrative charge and one derived local register recorded.

ES: Un cobro administrativo y un registro local derivado registrados.

EN: The neatness of our fiction cannot make its paperwork ancient evidence.

ES: La pulcritud de nuestra ficción no convierte sus papeles en evidencia antigua.

### o3 / phase-3

EN: Bring the register and the independent courier alive to the east-road dispatch post.

ES: Lleva con vida el registro y al correo independiente al puesto del camino oriental.

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
        "faith-origins.14-administrative-intrigue-caesarea.local-dispatch-register-1"
      ],
      "destinations": {
        "faith-origins.14-administrative-intrigue-caesarea.local-dispatch-register-1": "faith-origins.14-administrative-intrigue-caesarea.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.14-administrative-intrigue-caesarea.independent-courier-1"
      ],
      "destinations": {
        "faith-origins.14-administrative-intrigue-caesarea.independent-courier-1": "faith-origins.14-administrative-intrigue-caesarea.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The derived register and the original courier identity arrived together at dispatch.

ES: El registro derivado y la identidad original del correo han llegado al envío.

EN: I can record a local departure. I cannot read every intention behind the source.

ES: Puedo registrar una salida local. No puedo leer todas las intenciones detrás de la fuente.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/14-administrative-intrigue-caesarea.svg)

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
        171.09,
        188.39
      ],
      "lonLat": [
        34.918,
        32.5
      ],
      "name": {
        "en": "Inland local petition court",
        "es-ES": "Patio interior de solicitudes locales"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        158.35,
        120.39
      ],
      "lonLat": [
        34.914,
        32.518
      ],
      "name": {
        "en": "Northern record office yard",
        "es-ES": "Patio de registro septentrional"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        241.19,
        154.39
      ],
      "lonLat": [
        34.94,
        32.509
      ],
      "name": {
        "en": "East-road dispatch post",
        "es-ES": "Puesto de envío del camino oriental"
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
  "terrainInstructions": "Mediterranean west, all fictional office/post activity districts inland east of modern shore control. No modern museum, Crusader walls or invented palace/courtroom excavated address. Sea/imperial journey off-map; no battle or jailbreak fabricated to decide sacred figure fate.",
  "corridorStraightLengthsTiles": {
    "main": 158.73,
    "relief": 158.73
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
  "asset": "docs/design/maps/faith-origins/odyssey/14-administrative-intrigue-caesarea.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-1",
      "role": "fictional-local-administrative-note",
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
      "id": "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-2",
      "role": "fictional-local-administrative-note",
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
      "id": "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-3",
      "role": "fictional-local-administrative-note",
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
      "id": "faith-origins.14-administrative-intrigue-caesarea.local-dispatch-register-1",
      "role": "fictional-local-dispatch-register",
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
      "generationPolicy": "created once only after collected input identities and explicit derivation; not available at start",
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    },
    {
      "id": "faith-origins.14-administrative-intrigue-caesarea.independent-courier-1",
      "role": "fictional-independent-administrative-courier",
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
      "historicalMaterialPolicy": "fictional contemporary local participant/working item; no surviving canonical original, invented ancient quotation or later source book"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.14-administrative-intrigue-caesarea.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.14-administrative-intrigue-caesarea.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.14-administrative-intrigue-caesarea.destination-3",
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
    "local-admin-notes": [
      "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-1",
      "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-2",
      "faith-origins.14-administrative-intrigue-caesarea.local-admin-notes-3"
    ],
    "local-dispatch-register": [
      "faith-origins.14-administrative-intrigue-caesarea.local-dispatch-register-1"
    ],
    "independent-courier": [
      "faith-origins.14-administrative-intrigue-caesarea.independent-courier-1"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.14-administrative-intrigue-caesarea.independent-courier-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Separate municipal working copies / Copias de trabajo municipales separadas

EN: Recover both separate copies from separate municipal working copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de copias de trabajo municipales separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Optional copies offer attribution context, not authentic court transcripts.

ES: Las copias opcionales aportan contexto de atribución, no transcripciones judiciales auténticas.

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
          "14-administrative-intrigue-caesarea.side-1.entity-1",
          "14-administrative-intrigue-caesarea.side-1.entity-2"
        ],
        "destinations": {
          "14-administrative-intrigue-caesarea.side-1.entity-1": "14-administrative-intrigue-caesarea.side-1.zone-1",
          "14-administrative-intrigue-caesarea.side-1.entity-2": "14-administrative-intrigue-caesarea.side-1.zone-1"
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
        "id": "14-administrative-intrigue-caesarea.side-1.entity-1",
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
        "id": "14-administrative-intrigue-caesarea.side-1.entity-2",
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
        "id": "14-administrative-intrigue-caesarea.side-1.zone-1",
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
      "onceFlag": "14-administrative-intrigue-caesarea.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.14-administrative-intrigue-caesarea"
      ],
      "historicalNote": {
        "en": "In Acts, Paul appeals to Caesar while held at Caesarea under Festus. It is a later literary account, not a surviving court transcript. The administrative courier work here is fictional and does not control the historical appeal’s outcome.",
        "es-ES": "En Hechos, Pablo apela al César mientras está detenido en Cesarea bajo Festo. Es un relato literario posterior, no una transcripción judicial conservada. El trabajo de correo administrativo es ficticio y no controla el resultado de la apelación histórica."
      },
      "hint": {
        "en": "Collect three distinct local administrative notes and take them to the record-office yard.",
        "es-ES": "Recoge tres notas administrativas locales distintas y llévalas al patio de registro."
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

### Coastal road junction guide / Guía del cruce costero

EN: Escort the local guide of coastal road junction guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task.

ES: Escolta al guía local de guía del cruce costero hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea.

EN: Marks an inland route without claiming a palace address.

ES: Señala una ruta interior sin atribuirle una dirección palaciega.

```json
{
  "id": "side-2",
  "kind": "guide",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "14-administrative-intrigue-caesarea.side-2.entity-1"
        ],
        "destinations": {
          "14-administrative-intrigue-caesarea.side-2.entity-1": "14-administrative-intrigue-caesarea.side-2.zone-1"
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
        "id": "14-administrative-intrigue-caesarea.side-2.entity-1",
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
        "id": "14-administrative-intrigue-caesarea.side-2.zone-1",
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
      "onceFlag": "14-administrative-intrigue-caesarea.side-2.rewarded",
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

### Record-yard shelter / Cobertizo del patio de registro

EN: Pay 50 wood and restore the damaged store of record-yard shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de cobertizo del patio de registro. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Finite repair is separate from the main administrative debit.

ES: La reparación finita es distinta del cobro administrativo principal.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "14-administrative-intrigue-caesarea.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "14-administrative-intrigue-caesarea.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "14-administrative-intrigue-caesarea.side-3.payment",
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
        "id": "14-administrative-intrigue-caesarea.side-3.entity-1",
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
        "id": "14-administrative-intrigue-caesarea.side-3.zone-1",
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
      "onceFlag": "14-administrative-intrigue-caesarea.side-3.rewarded",
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

### Courier grain seller / Vendedor de grano del correo

EN: Escort the trader of courier grain seller to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de vendedor de grano del correo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One voluntary trade supports local logistics without purchasing legal outcomes.

ES: Un intercambio voluntario apoya la logística local sin comprar resultados judiciales.

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
          "14-administrative-intrigue-caesarea.side-4.entity-1"
        ],
        "destinations": {
          "14-administrative-intrigue-caesarea.side-4.entity-1": "14-administrative-intrigue-caesarea.side-4.zone-1"
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
        "receipt": "14-administrative-intrigue-caesarea.side-4.payment",
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
        "id": "14-administrative-intrigue-caesarea.side-4.entity-1",
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
        "id": "14-administrative-intrigue-caesarea.side-4.zone-1",
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
      "onceFlag": "14-administrative-intrigue-caesarea.side-4.rewarded",
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

### Independent service households / Hogares independientes de servicio

EN: Bring each of the two aid crates to its assigned household at independent service households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes de servicio. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Aid never bribes the historical court or changes the appeal.

ES: La ayuda nunca soborna al tribunal histórico ni cambia la apelación.

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
          "14-administrative-intrigue-caesarea.side-5.entity-1",
          "14-administrative-intrigue-caesarea.side-5.entity-2"
        ],
        "destinations": {
          "14-administrative-intrigue-caesarea.side-5.entity-1": "14-administrative-intrigue-caesarea.side-5.zone-1",
          "14-administrative-intrigue-caesarea.side-5.entity-2": "14-administrative-intrigue-caesarea.side-5.zone-2"
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
        "id": "14-administrative-intrigue-caesarea.side-5.entity-1",
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
        "id": "14-administrative-intrigue-caesarea.side-5.entity-2",
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
        "id": "14-administrative-intrigue-caesarea.side-5.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "14-administrative-intrigue-caesarea.side-5.zone-2",
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
      "onceFlag": "14-administrative-intrigue-caesarea.side-5.rewarded",
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

### Independent coastal travelers / Viajeros costeros independientes

EN: Bring both voluntary evacuee groups from independent coastal travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de viajeros costeros independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Optional voluntary arrivals never count as the main courier.

ES: Las llegadas voluntarias opcionales nunca cuentan como el correo principal.

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
          "14-administrative-intrigue-caesarea.side-6.entity-1",
          "14-administrative-intrigue-caesarea.side-6.entity-2"
        ],
        "destinations": {
          "14-administrative-intrigue-caesarea.side-6.entity-1": "14-administrative-intrigue-caesarea.side-6.zone-1",
          "14-administrative-intrigue-caesarea.side-6.entity-2": "14-administrative-intrigue-caesarea.side-6.zone-1"
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
        "id": "14-administrative-intrigue-caesarea.side-6.entity-1",
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
        "id": "14-administrative-intrigue-caesarea.side-6.entity-2",
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
        "id": "14-administrative-intrigue-caesarea.side-6.zone-1",
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
      "onceFlag": "14-administrative-intrigue-caesarea.side-6.rewarded",
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
      "id": "source-conscious-dispatch",
      "optionalObjectives": [
        "side-1",
        "side-2"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Read attributed context and survey land route first; historical verdict remains outside player control."
    },
    {
      "id": "local-supply-network",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Invest finite50wood/50gold in logistics after reserving40wood/20gold administrative debit."
    },
    {
      "id": "service-and-care",
      "optionalObjectives": [
        "side-5",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "costOfOpportunity": "Support independent households while main courier work proceeds; optional loss never defeats appeal logistics."
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
      "wood": 748,
      "gold": 249,
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
      "wood": 770,
      "gold": 260,
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
      "wood": 793,
      "gold": 272,
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
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.title / always | none | The Appeal Beside the Sea | La apelación junto al mar |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.fact-intro / intro first | collection-narrator | In Acts, Paul appeals to Caesar while held at Caesarea under Festus. It is a later literary account, not a surviving court transcript. The administrative courier work here is fictional and does not control the historical appeal’s outcome. | En Hechos, Pablo apela al César mientras está detenido en Cesarea bajo Festo. Es un relato literario posterior, no una transcripción judicial conservada. El trabajo de correo administrativo es ficticio y no controla el resultado de la apelación histórica. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.persona-intro / after handover | miriam-archive | A formal title once frightened me into copying a page without asking where it came from. I learned to question titles as well as stories. Here I will say plainly whose account I am reading. | Una vez un título formal me intimidó y copié una página sin preguntar de dónde procedía. Aprendí a interrogar títulos y relatos. Aquí diré claramente de quién es la versión que leo. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.route-help / available from start; repeatable without effect | none | The offices are fictional inland districts. Complete the local record chain and courier arrival; there is no player-controlled trial or rescue of Paul. | Las oficinas son ámbitos interiores ficticios. Completa la cadena local de registros y la llegada del correo; el jugador no dirige un juicio ni un rescate de Pablo. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.o1-goal / phase-1 active | none | Collect three distinct local administrative notes and take them to the record-office yard. | Recoge tres notas administrativas locales distintas y llévalas al patio de registro. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.o1-receipt / o1 latched once | none | Three original fictional notes reached the record office. | Tres notas ficticias originales han llegado al registro. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.o1-reaction / after o1 receipt | miriam-archive | They are neither a court transcript nor an appeal signed by Paul. | No son una transcripción judicial ni una apelación firmada por Pablo. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.o2-goal / phase-2 active | none | Pay 40 wood and 20 gold once and derive one local dispatch register from the three notes. | Paga una sola vez 40 de madera y 20 de oro y elabora un registro local de envío a partir de las tres notas. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.o2-receipt / o2 latched once | none | One administrative charge and one derived local register recorded. | Un cobro administrativo y un registro local derivado registrados. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.o2-reaction / after o2 receipt | miriam-archive | The neatness of our fiction cannot make its paperwork ancient evidence. | La pulcritud de nuestra ficción no convierte sus papeles en evidencia antigua. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.o3-goal / phase-3 active | none | Bring the register and the independent courier alive to the east-road dispatch post. | Lleva con vida el registro y al correo independiente al puesto del camino oriental. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.o3-receipt / o3 latched once | none | The derived register and the original courier identity arrived together at dispatch. | El registro derivado y la identidad original del correo han llegado al envío. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.o3-reaction / after o3 receipt | miriam-archive | I can record a local departure. I cannot read every intention behind the source. | Puedo registrar una salida local. No puedo leer todas las intenciones detrás de la fuente. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from separate municipal working copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de copias de trabajo municipales separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-1-complete / side-1 completed | none | Separate municipal working copies completed. Its stated benefit has been granted once. | Copias de trabajo municipales separadas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-1-lost / side-1 failed-optional | none | Separate municipal working copies is unavailable after the loss of its unique participant or object. The main mission continues. | Copias de trabajo municipales separadas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-2-goal / optional list from start | none | Escort the local guide of coastal road junction guide to the marked road junction. Benefit: Mark the surveyed relief corridor once; no enemy is created, no terrain is changed, and main receivers remain known without this task. | Escolta al guía local de guía del cruce costero hasta el cruce señalado. Ventaja: Señala una vez el corredor trazado relief; no crea enemigos ni modifica el terreno, y los receptores principales ya son conocidos sin esta tarea. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-2-complete / side-2 completed | none | Coastal road junction guide completed. Its stated benefit has been granted once. | Guía del cruce costero: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-2-lost / side-2 failed-optional | none | Coastal road junction guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del cruce costero: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of record-yard shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de cobertizo del patio de registro. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-3-complete / side-3 completed | none | Record-yard shelter completed. Its stated benefit has been granted once. | Cobertizo del patio de registro: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-3-lost / side-3 failed-optional | none | Record-yard shelter is unavailable after the loss of its unique participant or object. The main mission continues. | Cobertizo del patio de registro: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-4-goal / optional list from start | none | Escort the trader of courier grain seller to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de vendedor de grano del correo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-4-complete / side-4 completed | none | Courier grain seller completed. Its stated benefit has been granted once. | Vendedor de grano del correo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-4-lost / side-4 failed-optional | none | Courier grain seller is unavailable after the loss of its unique participant or object. The main mission continues. | Vendedor de grano del correo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-5-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at independent service households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes de servicio. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-5-complete / side-5 completed | none | Independent service households completed. Its stated benefit has been granted once. | Hogares independientes de servicio: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-5-lost / side-5 failed-optional | none | Independent service households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares independientes de servicio: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-6-goal / optional list from start | none | Bring both voluntary evacuee groups from independent coastal travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de viajeros costeros independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-6-complete / side-6 completed | none | Independent coastal travelers completed. Its stated benefit has been granted once. | Viajeros costeros independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.side-6-lost / side-6 failed-optional | none | Independent coastal travelers is unavailable after the loss of its unique participant or object. The main mission continues. | Viajeros costeros independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.fact-outro / victory first | collection-narrator | The fictional records have been dispatched within the Caesarea setting. Their delivery neither authenticates Acts as a court transcript nor changes Paul’s narrated appeal or subsequent journey. | Los registros ficticios se han enviado dentro de la ambientación de Cesarea. Su entrega no autentica Hechos como transcripción judicial ni altera la apelación narrada de Pablo o su viaje posterior. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.persona-outro / after fact-outro | miriam-archive | There are seals I can describe and motives I cannot know. A faithful copy does not grant me access to another person’s mind. | Hay sellos que puedo describir y motivos que no puedo conocer. Una copia fiel no me da acceso a la mente ajena. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.14-administrative-intrigue-caesarea.odyssey.next-episode / after persona-outro | none | Continue with Ash over the Seven Hills. This episode does not complete the campaign. | Continúa con Ceniza sobre las siete colinas. Este episodio no termina la campaña. |

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
      "register cannot derive from only two notes",
      "bribery cannot alter historical appeal",
      "independent courier not Paul or court participant",
      "optional copies cannot fill three main notes",
      "sea and later fortifications never used as local courier shortcut",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
