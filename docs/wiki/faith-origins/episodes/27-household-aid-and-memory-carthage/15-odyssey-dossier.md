# 27. What the Record Cannot Hold

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `27-household-aid-and-memory-carthage` · 203 CE · 360×360

## Historical frame and fixed outcome

EN: The Passion of Perpetua and Felicity transmits accounts of imprisonment, visions and execution at Carthage, conventionally dated 203. Its literary layers and religious interpretations require attribution. The reported deaths remain fixed; the playable care circuit concerns separate fictional neighbors, never the historical prisoners or their children.

ES: La Pasión de Perpetua y Felicidad transmite relatos de encarcelamiento, visiones y ejecución en Cartago, fechados convencionalmente en 203. Sus capas literarias e interpretaciones religiosas requieren atribución. Las muertes relatadas permanecen fijas; el circuito jugable de cuidados trata de vecinos ficticios separados, nunca de los prisioneros históricos ni de sus hijos.

EN: Four fictional neighbors and three original care parcels reached their assigned inland sites after a paid preparation. This is local imaginative care, not a liberation, change of sentence or reconstructed conversation with Perpetua or Felicity. The text’s visions remain reported visions.

ES: Cuatro vecinos ficticios y tres paquetes originales de cuidados llegaron a sus lugares interiores asignados tras una preparación pagada. Es cuidado local imaginado, no una liberación, cambio de sentencia ni conversación reconstruida con Perpetua o Felicidad. Las visiones del texto siguen siendo visiones relatadas.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 20,
      "episodeId": "27-household-aid-and-memory-carthage",
      "order": 27,
      "selectedSourceUrl": "https://www.earlychristianwritings.com/text/perpetua.html",
      "consultedUrl": "https://www.earlychristianwritings.com/text/perpetua.html",
      "passage": "Passion of Perpetua and Felicity §§3–10 (first-person prison visions) and §§16–21 (trial/execution); page introduction dates event 203.",
      "supportedClaim": {
        "en": "The Passion preserves a near-contemporary Christian account of Perpetua and Felicity's imprisonment and execution at Carthage.",
        "es-ES": "La Pasión conserva un relato cristiano cercano a los hechos sobre el encarcelamiento y ejecución de Perpetua y Felicidad en Cartago."
      },
      "limitations": "The work has a complex literary/redactional history and theological vision material; date 203 is conventional and the page's introductory header is secondary. Treat visions as the text's claims, not verified supernatural events.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/0324.htm",
      "passage": "Passion, displayed chapters1–3 and5–6; first-person attributed account, visions, editor’s continuation and deaths",
      "limitations": "Older page chapter grouping differs from modern sections3–10/16–21. Literary/redactional attribution; no invented voice, execution rescue, miraculous immunity or definite extant amphitheater identification.",
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

EN: Collect all three original care parcels and deliver them to the western coordination yard.

ES: Recoge los tres paquetes originales de cuidados y entrégalos en el patio occidental.

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
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-1",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-2",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-1",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-2",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-3"
      ],
      "destinations": {
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-1": "faith-origins.27-household-aid-and-memory-carthage.destination-2",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-2": "faith-origins.27-household-aid-and-memory-carthage.destination-2",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-3": "faith-origins.27-household-aid-and-memory-carthage.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All three original care parcels reached preparation.

ES: Los tres paquetes originales de cuidados llegaron a su preparación.

EN: These ordinary parcels carry no claim to an ancient relic.

ES: Estos paquetes ordinarios no pretenden ser reliquias antiguas.

### o2 / phase-2

EN: Pay 240 food and 80 wood once at the western coordination yard.

ES: Paga una vez 240 de alimento y 80 de madera en el patio occidental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 240,
        "wood": 80
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.27-household-aid-and-memory-carthage.destination-2"
      ],
      "allocations": {
        "faith-origins.27-household-aid-and-memory-carthage.destination-2": {
          "food": 240,
          "wood": 80
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.27-household-aid-and-memory-carthage.o2.req-1.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The local care circuit is funded once.

ES: El circuito local de cuidados está financiado una vez.

EN: Care is what this payment supports; no sentence can be bought away.

ES: Este pago sostiene cuidados; no compra la desaparición de una sentencia.

### o3 / phase-3

EN: Bring two assigned fictional neighbors alive to each northern/eastern court and all three original care parcels to the eastern court.

ES: Lleva con vida dos vecinos ficticios asignados a cada patio norte y este, y los tres paquetes originales al patio oriental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "state": "arrived",
      "requiredCount": 4,
      "id": "req-1",
      "entities": [
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-1",
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-2",
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-3",
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-4"
      ],
      "destinations": {
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-1": "faith-origins.27-household-aid-and-memory-carthage.destination-3",
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-2": "faith-origins.27-household-aid-and-memory-carthage.destination-3",
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-3": "faith-origins.27-household-aid-and-memory-carthage.destination-4",
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-4": "faith-origins.27-household-aid-and-memory-carthage.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-1",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-2",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-3"
      ],
      "destinations": {
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-1": "faith-origins.27-household-aid-and-memory-carthage.destination-4",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-2": "faith-origins.27-household-aid-and-memory-carthage.destination-4",
        "faith-origins.27-household-aid-and-memory-carthage.care-parcels-3": "faith-origins.27-household-aid-and-memory-carthage.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Four separate neighbors and three original parcels reached their assigned care sites.

ES: Cuatro vecinos distintos y tres paquetes originales llegaron a sus lugares asignados de cuidado.

EN: I will not name an invented neighbor after a martyr to make our success sound larger.

ES: No daré a un vecino inventado el nombre de un mártir para engrandecer nuestro éxito.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/27-household-aid-and-memory-carthage.svg)

```json
{
  "bbox": [
    10.283,
    36.843,
    10.334,
    36.891
  ],
  "terrainProfile": "carthage",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        214.23,
        279.67
      ],
      "lonLat": [
        10.315,
        36.852
      ],
      "name": {
        "en": "Local inland pickup court",
        "es-ES": "Patio interior local de recogida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        96.69,
        212.89
      ],
      "lonLat": [
        10.293,
        36.862
      ],
      "name": {
        "en": "Western coordination yard",
        "es-ES": "Patio occidental de coordinación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        187.51,
        79.33
      ],
      "lonLat": [
        10.31,
        36.882
      ],
      "name": {
        "en": "Northern local receiving court",
        "es-ES": "Patio receptor local septentrional"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        267.65,
        179.5
      ],
      "lonLat": [
        10.325,
        36.867
      ],
      "name": {
        "en": "Eastern inland receiving court",
        "es-ES": "Patio receptor interior oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-road",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-road",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "relief",
      "hubOrder": [
        "hub-3",
        "hub-4",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "graded inland outer circuit; no coast or lagoon crossing"
    }
  ],
  "terrainInstructions": "Roman Carthage local inland scene west of the eastern sea/coastal control. Byrsa hill and slopes retain their relative eastern position; four activity courts are invented local workplaces, not tribunal, prison, amphitheater or martyrdom coordinates. Main activity remains inland and no dock, lagoon, water crossing or naval trip is mandatory. Keep grade changes and finite field/workshop supplies; no continuous desert, Spanish/Ottoman fort, later Christian basilica, modern railway/villa or current reconstructed bath/arena footprint as an exact 197–258 scene. Ancient shoreline, building dates and navigability require independent evidence. Source-mentioned trials/deaths are off the playable route.",
  "corridorStraightLengthsTiles": {
    "north-road": 296.7,
    "east-road": 309.38,
    "relief": 241.81
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
  "asset": "docs/design/maps/faith-origins/odyssey/27-household-aid-and-memory-carthage.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.27-household-aid-and-memory-carthage.care-parcels-1",
      "role": "fictional-neighborhood-care-parcel",
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
      "id": "faith-origins.27-household-aid-and-memory-carthage.care-parcels-2",
      "role": "fictional-neighborhood-care-parcel",
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
      "id": "faith-origins.27-household-aid-and-memory-carthage.care-parcels-3",
      "role": "fictional-neighborhood-care-parcel",
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
      "id": "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-1",
      "role": "fictional-voluntary-neighbor",
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
      "id": "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-2",
      "role": "fictional-voluntary-neighbor",
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
      "id": "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-3",
      "role": "fictional-voluntary-neighbor",
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
      "id": "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-4",
      "role": "fictional-voluntary-neighbor",
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
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "faith-origins.27-household-aid-and-memory-carthage.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.27-household-aid-and-memory-carthage.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.27-household-aid-and-memory-carthage.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.27-household-aid-and-memory-carthage.destination-4",
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
    "care-parcels": [
      "faith-origins.27-household-aid-and-memory-carthage.care-parcels-1",
      "faith-origins.27-household-aid-and-memory-carthage.care-parcels-2",
      "faith-origins.27-household-aid-and-memory-carthage.care-parcels-3"
    ],
    "care-neighbors": [
      "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-1",
      "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-2",
      "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-3",
      "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-4"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-1",
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-2",
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-3",
        "faith-origins.27-household-aid-and-memory-carthage.care-neighbors-4"
      ],
      "minimumAliveOrAlreadySafe": 4
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Households beyond the main circuit / Hogares fuera del circuito principal

EN: Bring each of the two aid crates to its assigned household at households beyond the main circuit. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares fuera del circuito principal. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Optional recipients are identity-disjoint from all four main neighbors.

ES: Los receptores opcionales tienen identidades distintas de los cuatro vecinos principales.

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
          "27-household-aid-and-memory-carthage.side-1.entity-1",
          "27-household-aid-and-memory-carthage.side-1.entity-2"
        ],
        "destinations": {
          "27-household-aid-and-memory-carthage.side-1.entity-1": "27-household-aid-and-memory-carthage.side-1.zone-1",
          "27-household-aid-and-memory-carthage.side-1.entity-2": "27-household-aid-and-memory-carthage.side-1.zone-2"
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
        "id": "27-household-aid-and-memory-carthage.side-1.entity-1",
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
        "id": "27-household-aid-and-memory-carthage.side-1.entity-2",
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
        "id": "27-household-aid-and-memory-carthage.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "27-household-aid-and-memory-carthage.side-1.zone-2",
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
      "onceFlag": "27-household-aid-and-memory-carthage.side-1.rewarded",
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
      "north-road",
      "east-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The vision and the account / La visión y el relato

EN: Recover both separate copies from the vision and the account and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de la visión y el relato y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Qualified context keeps first-person literary material separate from the editor’s narrative and neutral summary.

ES: El contexto separa el material literario en primera persona de la narración del editor y del resumen neutral.

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
          "27-household-aid-and-memory-carthage.side-2.entity-1",
          "27-household-aid-and-memory-carthage.side-2.entity-2"
        ],
        "destinations": {
          "27-household-aid-and-memory-carthage.side-2.entity-1": "27-household-aid-and-memory-carthage.side-2.zone-1",
          "27-household-aid-and-memory-carthage.side-2.entity-2": "27-household-aid-and-memory-carthage.side-2.zone-1"
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
        "id": "27-household-aid-and-memory-carthage.side-2.entity-1",
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
        "id": "27-household-aid-and-memory-carthage.side-2.entity-2",
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
        "id": "27-household-aid-and-memory-carthage.side-2.zone-1",
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
      "onceFlag": "27-household-aid-and-memory-carthage.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.27-household-aid-and-memory-carthage"
      ],
      "historicalNote": {
        "en": "The Passion of Perpetua and Felicity transmits accounts of imprisonment, visions and execution at Carthage, conventionally dated 203. Its literary layers and religious interpretations require attribution. The reported deaths remain fixed; the playable care circuit concerns separate fictional neighbors, never the historical prisoners or their children.",
        "es-ES": "La Pasión de Perpetua y Felicidad transmite relatos de encarcelamiento, visiones y ejecución en Cartago, fechados convencionalmente en 203. Sus capas literarias e interpretaciones religiosas requieren atribución. Las muertes relatadas permanecen fijas; el circuito jugable de cuidados trata de vecinos ficticios separados, nunca de los prisioneros históricos ni de sus hijos."
      },
      "hint": {
        "en": "Collect all three original care parcels and deliver them to the western coordination yard.",
        "es-ES": "Recoge los tres paquetes originales de cuidados y entrégalos en el patio occidental."
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
      "north-road",
      "east-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### An independent inland care shed / Un cobertizo interior de cuidados independiente

EN: Pay 50 wood and restore the damaged store of an independent inland care shed to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de un cobertizo interior de cuidados independiente. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A finite shed repair never heals or liberates an actual martyr.

ES: Reparar un cobertizo finito nunca sana ni libera a un mártir real.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "27-household-aid-and-memory-carthage.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "27-household-aid-and-memory-carthage.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "27-household-aid-and-memory-carthage.side-3.payment",
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
        "id": "27-household-aid-and-memory-carthage.side-3.entity-1",
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
        "id": "27-household-aid-and-memory-carthage.side-3.zone-1",
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
      "onceFlag": "27-household-aid-and-memory-carthage.side-3.rewarded",
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
      "north-road",
      "east-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Two separate voluntary travelers / Dos viajeros voluntarios separados

EN: Bring both voluntary evacuee groups from two separate voluntary travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de dos viajeros voluntarios separados al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Optional travelers are invented adults, never Perpetua’s infant or Felicity’s child.

ES: Los viajeros opcionales son adultos inventados, nunca el lactante de Perpetua ni la hija de Felicidad.

```json
{
  "id": "side-4",
  "kind": "extract",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "27-household-aid-and-memory-carthage.side-4.entity-1",
          "27-household-aid-and-memory-carthage.side-4.entity-2"
        ],
        "destinations": {
          "27-household-aid-and-memory-carthage.side-4.entity-1": "27-household-aid-and-memory-carthage.side-4.zone-1",
          "27-household-aid-and-memory-carthage.side-4.entity-2": "27-household-aid-and-memory-carthage.side-4.zone-1"
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
        "id": "27-household-aid-and-memory-carthage.side-4.entity-1",
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
        "id": "27-household-aid-and-memory-carthage.side-4.entity-2",
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
        "id": "27-household-aid-and-memory-carthage.side-4.zone-1",
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
      "onceFlag": "27-household-aid-and-memory-carthage.side-4.rewarded",
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
      "north-road",
      "east-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Eastern care-road viewpoints / Miradores del camino oriental de cuidados

EN: Scout both marked viewpoints of eastern care-road viewpoints. Benefit: Mark the surveyed east-road inland circuit once; main receivers remain disclosed without it.

ES: Explora los dos miradores señalados de miradores del camino oriental de cuidados. Ventaja: Señala una vez el circuito interior trazado east-road; los receptores principales siguen identificados sin él.

EN: Survey the actual local eastern circuit, not a passage into an arena or prison.

ES: Reconoce el circuito oriental local real, no un paso a una arena o prisión.

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
          "27-household-aid-and-memory-carthage.side-5.zone-1",
          "27-household-aid-and-memory-carthage.side-5.zone-2"
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
        "id": "27-household-aid-and-memory-carthage.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "27-household-aid-and-memory-carthage.side-5.zone-2",
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
      "target": "east-road surveyed inland circuit",
      "resources": {},
      "onceFlag": "27-household-aid-and-memory-carthage.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "east-road"
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
      "north-road",
      "east-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The neighbors’ outer guide / El guía exterior de vecinos

EN: Escort the local guide of the neighbors’ outer guide to the marked road junction. Benefit: Mark the surveyed relief inland circuit once; main receivers remain disclosed without it.

ES: Escolta al guía local de el guía exterior de vecinos hasta el cruce señalado. Ventaja: Señala una vez el circuito interior trazado relief; los receptores principales siguen identificados sin él.

EN: Marks the outer inland land circuit; cannot recover relics or reverse the Passion.

ES: Señala el circuito terrestre interior exterior; no recupera reliquias ni revierte la Pasión.

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
          "27-household-aid-and-memory-carthage.side-6.entity-1"
        ],
        "destinations": {
          "27-household-aid-and-memory-carthage.side-6.entity-1": "27-household-aid-and-memory-carthage.side-6.zone-1"
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
        "id": "27-household-aid-and-memory-carthage.side-6.entity-1",
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
        "id": "27-household-aid-and-memory-carthage.side-6.zone-1",
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
      "target": "relief surveyed inland circuit",
      "resources": {},
      "onceFlag": "27-household-aid-and-memory-carthage.side-6.rewarded",
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
      "north-road",
      "east-road",
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
      "food": 400,
      "wood": 150,
      "gold": 25,
      "stone": 0
    },
    "maxOptionalCosts": {
      "food": 0,
      "wood": 50,
      "gold": 0,
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
      "id": "parcels-and-north-neighbors",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Split preparation and north/east delivery; keep parcel identities distinct from people.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "context-and-independent-care",
      "optionalObjectives": [
        "side-1",
        "side-2"
      ],
      "costOfOpportunity": "Complete separate neighbor aid and read attributed literary context while 240 food 80 woodmain cost stays reserved.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "outer-traveler-circuit",
      "optionalObjectives": [
        "side-4",
        "side-6"
      ],
      "costOfOpportunity": "Escort optional independent travelers along the graded outer route; they cannot replace main neighbors.",
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
      "food": 1308,
      "wood": 738,
      "gold": 229,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
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
      "food": 1310,
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
      "food": 1360,
      "wood": 760,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
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
      "food": 1310,
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
      "food": 1413,
      "wood": 783,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
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
      "food": 1310,
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
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.title / always | none | What the Record Cannot Hold | Lo que el registro no puede guardar |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.fact-intro / intro first | collection-narrator | The Passion of Perpetua and Felicity transmits accounts of imprisonment, visions and execution at Carthage, conventionally dated 203. Its literary layers and religious interpretations require attribution. The reported deaths remain fixed; the playable care circuit concerns separate fictional neighbors, never the historical prisoners or their children. | La Pasión de Perpetua y Felicidad transmite relatos de encarcelamiento, visiones y ejecución en Cartago, fechados convencionalmente en 203. Sus capas literarias e interpretaciones religiosas requieren atribución. Las muertes relatadas permanecen fijas; el circuito jugable de cuidados trata de vecinos ficticios separados, nunca de los prisioneros históricos ni de sus hijos. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.persona-intro / after handover | miriam-archive | The words attributed to a young mother trouble me more than any tidy register can show. I am a copyist, and I did not hear her. I can tell you what this inherited text does to me; I cannot step into her place or put a new answer in her mouth. | Las palabras atribuidas a una madre joven me inquietan más de lo que puede mostrar un registro limpio. Soy copista y no la oí. Puedo contarte lo que este texto heredado provoca en mí; no puedo ocupar su lugar ni poner una respuesta nueva en su boca. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.route-help / available from start; repeatable without effect | none | Collect three original care parcels and stage them at the western coordination yard. Pay 240 food and 80 wood there once. Bring two assigned fictional neighbors to the northern court and two to the eastern court; deliver all three original care parcels to the eastern court. No prison, arena, martyr or historical infant is a playable target. | Recoge tres paquetes originales de cuidados y prepáralos en el patio occidental. Paga allí una vez 240 de alimento y 80 de madera. Lleva dos vecinos ficticios asignados al patio norte y dos al oriental; entrega los tres paquetes originales en el oriental. Ninguna prisión, arena, mártir ni criatura histórica es un objetivo jugable. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.o1-goal / phase-1 active | none | Collect all three original care parcels and deliver them to the western coordination yard. | Recoge los tres paquetes originales de cuidados y entrégalos en el patio occidental. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.o1-receipt / o1 latched once | none | All three original care parcels reached preparation. | Los tres paquetes originales de cuidados llegaron a su preparación. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.o1-reaction / after o1 receipt | miriam-archive | These ordinary parcels carry no claim to an ancient relic. | Estos paquetes ordinarios no pretenden ser reliquias antiguas. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.o2-goal / phase-2 active | none | Pay 240 food and 80 wood once at the western coordination yard. | Paga una vez 240 de alimento y 80 de madera en el patio occidental. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.o2-receipt / o2 latched once | none | The local care circuit is funded once. | El circuito local de cuidados está financiado una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.o2-reaction / after o2 receipt | miriam-archive | Care is what this payment supports; no sentence can be bought away. | Este pago sostiene cuidados; no compra la desaparición de una sentencia. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.o3-goal / phase-3 active | none | Bring two assigned fictional neighbors alive to each northern/eastern court and all three original care parcels to the eastern court. | Lleva con vida dos vecinos ficticios asignados a cada patio norte y este, y los tres paquetes originales al patio oriental. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.o3-receipt / o3 latched once | none | Four separate neighbors and three original parcels reached their assigned care sites. | Cuatro vecinos distintos y tres paquetes originales llegaron a sus lugares asignados de cuidado. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.o3-reaction / after o3 receipt | miriam-archive | I will not name an invented neighbor after a martyr to make our success sound larger. | No daré a un vecino inventado el nombre de un mártir para engrandecer nuestro éxito. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at households beyond the main circuit. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares fuera del circuito principal. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-1-complete / side-1 completed | none | Households beyond the main circuit completed. Its stated benefit has been granted once. | Hogares fuera del circuito principal: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-1-lost / side-1 failed-optional | none | Households beyond the main circuit is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares fuera del circuito principal: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from the vision and the account and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de la visión y el relato y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-2-complete / side-2 completed | none | The vision and the account completed. Its stated benefit has been granted once. | La visión y el relato: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-2-lost / side-2 failed-optional | none | The vision and the account is unavailable after the loss of its unique participant or object. The main mission continues. | La visión y el relato: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of an independent inland care shed to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de un cobertizo interior de cuidados independiente. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-3-complete / side-3 completed | none | An independent inland care shed completed. Its stated benefit has been granted once. | Un cobertizo interior de cuidados independiente: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-3-lost / side-3 failed-optional | none | An independent inland care shed is unavailable after the loss of its unique participant or object. The main mission continues. | Un cobertizo interior de cuidados independiente: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-4-goal / optional list from start | none | Bring both voluntary evacuee groups from two separate voluntary travelers to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de dos viajeros voluntarios separados al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-4-complete / side-4 completed | none | Two separate voluntary travelers completed. Its stated benefit has been granted once. | Dos viajeros voluntarios separados: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-4-lost / side-4 failed-optional | none | Two separate voluntary travelers is unavailable after the loss of its unique participant or object. The main mission continues. | Dos viajeros voluntarios separados: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of eastern care-road viewpoints. Benefit: Mark the surveyed east-road inland circuit once; main receivers remain disclosed without it. | Explora los dos miradores señalados de miradores del camino oriental de cuidados. Ventaja: Señala una vez el circuito interior trazado east-road; los receptores principales siguen identificados sin él. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-5-complete / side-5 completed | none | Eastern care-road viewpoints completed. Its stated benefit has been granted once. | Miradores del camino oriental de cuidados: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-5-lost / side-5 failed-optional | none | Eastern care-road viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores del camino oriental de cuidados: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the neighbors’ outer guide to the marked road junction. Benefit: Mark the surveyed relief inland circuit once; main receivers remain disclosed without it. | Escolta al guía local de el guía exterior de vecinos hasta el cruce señalado. Ventaja: Señala una vez el circuito interior trazado relief; los receptores principales siguen identificados sin él. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-6-complete / side-6 completed | none | The neighbors’ outer guide completed. Its stated benefit has been granted once. | El guía exterior de vecinos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.side-6-lost / side-6 failed-optional | none | The neighbors’ outer guide is unavailable after the loss of its unique participant or object. The main mission continues. | El guía exterior de vecinos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.fact-outro / victory first | collection-narrator | Four fictional neighbors and three original care parcels reached their assigned inland sites after a paid preparation. This is local imaginative care, not a liberation, change of sentence or reconstructed conversation with Perpetua or Felicity. The text’s visions remain reported visions. | Cuatro vecinos ficticios y tres paquetes originales de cuidados llegaron a sus lugares interiores asignados tras una preparación pagada. Es cuidado local imaginado, no una liberación, cambio de sentencia ni conversación reconstruida con Perpetua o Felicidad. Las visiones del texto siguen siendo visiones relatadas. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.persona-outro / after fact-outro | miriam-archive | I want the little work we completed to matter without asking it to undo those deaths. If I lend these neighbors a story, I must keep their invented names clear of the women whose words I inherited. | Quiero que importe el pequeño trabajo terminado sin pedirle que deshaga aquellas muertes. Si presto una historia a estos vecinos, debo mantener sus nombres inventados separados de las mujeres cuyas palabras heredé. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.next-episode / after persona-outro | none | Continue with The Seal on the Certificate. This episode does not complete the campaign. | Continúa con El sello del certificado. Este episodio no termina la campaña. |
| scenario.faith-origins.27-household-aid-and-memory-carthage.odyssey.act-turning-point / after next-episode | collection-narrator | The final act changes region and evidence: an Egyptian compliance certificate, letters about Valerian and reports of persecution and restitution. Different documents cannot be folded into one uniform policy or one community’s uninterrupted experience. | El acto final cambia de región y evidencia: un certificado egipcio de cumplimiento, cartas sobre Valeriano y relatos de persecución y restitución. Documentos distintos no se funden en una política uniforme ni en la experiencia continua de una única comunidad. |

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
      "carthage-antonine-baths",
      "carthage-amphitheatre"
    ],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "Two neighbors assigned north cannot satisfy the eastern receiving court.",
      "All three original care parcel identities persist across preparation and final delivery.",
      "An optional traveler cannot substitute for a main neighbor.",
      "No historical children are escort or rescue units.",
      "No invented authentic quotation or shared martyr voice.",
      "Reported visions cannot spawn immunity, dragons or miraculous healing.",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
