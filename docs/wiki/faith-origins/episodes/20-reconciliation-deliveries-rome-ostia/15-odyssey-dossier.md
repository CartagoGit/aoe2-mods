# 20. A Letter Across the Divide

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `20-reconciliation-deliveries-rome-ostia` · c. 95 CE · 380×380

## Historical frame and fixed outcome

EN: The work known as First Clement addresses the church at Corinth from the church at Rome and argues against the removal of established ministers. The surviving letter advocates reconciliation; it does not report a completed settlement. Its author is unnamed in the text, and c.95 is a conventional approximate date.

ES: La obra conocida como Primera de Clemente se dirige desde la iglesia de Roma a la de Corinto y argumenta contra la destitución de ministros establecidos. La carta conservada aboga por la reconciliación; no informa de un acuerdo consumado. Su autor no figura en el texto y hacia el 95 es una fecha convencional aproximada.

EN: Fictional local drafts and couriers reached a Roman dispatch district. This completes preparation, not a journey to Corinth or proof that the dispute ended. The historical letter remains an appeal whose arguments and reception must be distinguished.

ES: Borradores locales y correos ficticios alcanzaron un distrito romano de despacho. Se completa la preparación, no el viaje a Corinto ni la prueba de que acabara la disputa. La carta histórica sigue siendo un llamamiento: sus argumentos y su recepción deben distinguirse.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 13,
      "episodeId": "20-reconciliation-deliveries-rome-ostia",
      "order": 20,
      "selectedSourceUrl": "https://www.earlychristianwritings.com/1clement.html",
      "consultedUrl": "https://www.earlychristianwritings.com/1clement.html",
      "passage": "1 Clement 1–3 and 47–59: letter addresses the Corinthian church, laments dissension and removal of presbyters, and urges restoration.",
      "supportedClaim": {
        "en": "1 Clement is a Roman church's letter urging reconciliation in a leadership conflict at Corinth.",
        "es-ES": "1 Clemente es una carta de la iglesia de Roma que pide reconciliación en un conflicto de liderazgo en Corinto."
      },
      "limitations": "The opening directly identifies the Roman sender and Corinthian addressee. The text does not name Clement as author; c.95 is conventional and not stated in the letter. A particular Roman copying address remains fiction.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/1010.htm",
      "passage": "1Clement opening and44–48; architect read sender/addressee, ministers removed and appeal for concord",
      "limitations": "Author unnamed in the text, datec95 conventional; advocacy not proof of restored peace or exact Roman writing address. This older translation/page numbers differ from some modern chapter divisions; no authentic dialogue or manuscript placed.",
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

EN: Collect the two northern and two southern local request notes; deliver all four distinct notes to the eastern preparation yard.

ES: Recoge las dos notas locales septentrionales y las dos meridionales; entrega las cuatro notas distintas en el patio oriental de preparación.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-1",
      "entities": [
        "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-1",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-1",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-1",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-2"
      ],
      "destinations": {
        "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-1": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-4",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-2": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-1",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-2"
      ],
      "destinations": {
        "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-1": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-4",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-2": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Two separate note pairs have arrived without substituting one for the other.

ES: Han llegado dos parejas separadas de notas sin sustituir una por otra.

EN: A reply assembled from only one side would be easier. That is not why I became a copyist.

ES: Sería más fácil preparar una respuesta con un solo lado. No me hice copista para eso.

### o2 / phase-2

EN: Pay 60 wood and 20 gold at the preparation yard, then create one cover register from the four collected request notes.

ES: Paga 60 de madera y 20 de oro en el patio de preparación y después crea un registro de cubierta con las cuatro notas recogidas.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 60,
        "gold": 20
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-4"
      ],
      "allocations": {
        "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-4": {
          "wood": 60,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.20-reconciliation-deliveries-rome-ostia.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-1",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-2",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-1",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-2"
      ],
      "outputEntities": [
        "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-cover-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.20-reconciliation-deliveries-rome-ostia.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 60,
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

EN: One preparation register is backed by its exact paid receipt and four original inputs.

ES: Un registro de preparación está respaldado por su recibo pagado exacto y cuatro entradas originales.

EN: The cover records our preparation, not a verdict on who was right at Corinth.

ES: La cubierta registra nuestra preparación, no un veredicto sobre quién tenía razón en Corinto.

### o3 / phase-3

EN: Bring the original cover register and both original couriers alive to the inland dispatch district.

ES: Lleva el registro de cubierta original y ambos correos originales con vida al distrito interior de despacho.

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
        "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-cover-1"
      ],
      "destinations": {
        "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-cover-1": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-1",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-2"
      ],
      "destinations": {
        "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-1": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-5",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-2": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-5"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The local dispatch party is ready; no off-map delivery or reconciliation has been certified.

ES: El grupo local de despacho está listo; no se ha acreditado entrega fuera del mapa ni reconciliación.

EN: The road begins where this scene ends. Another voice will have to tell what followed.

ES: El camino empieza donde acaba esta escena. Otra voz deberá contar lo que vino después.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/20-reconciliation-deliveries-rome-ostia.svg)

```json
{
  "bbox": [
    12.48,
    41.87,
    12.555,
    41.93
  ],
  "terrainProfile": "rome-ostia",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        179.01,
        183.86
      ],
      "lonLat": [
        12.515,
        41.901
      ],
      "name": {
        "en": "Central courier court",
        "es-ES": "Patio central de correos"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        153.82,
        87.98
      ],
      "lonLat": [
        12.509,
        41.918
      ],
      "name": {
        "en": "Northern request court",
        "es-ES": "Patio septentrional de peticiones"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        141.22,
        302.3
      ],
      "lonLat": [
        12.506,
        41.88
      ],
      "name": {
        "en": "Southern request court",
        "es-ES": "Patio meridional de peticiones"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        271.36,
        189.5
      ],
      "lonLat": [
        12.537,
        41.9
      ],
      "name": {
        "en": "Eastern preparation yard",
        "es-ES": "Patio oriental de preparación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        317.53,
        104.9
      ],
      "lonLat": [
        12.548,
        41.915
      ],
      "name": {
        "en": "Inland dispatch district",
        "es-ES": "Distrito interior de despacho"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-drafts",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "south-drafts",
      "hubOrder": [
        "hub-1",
        "hub-3",
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "relief",
      "hubOrder": [
        "hub-2",
        "hub-1",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "surveyed cross-circuit land detour east of Tiber"
    }
  ],
  "terrainInstructions": "Local Rome scene east of the Tiber. North/south collection and eastern inland departure remain on land; Corinth is off-map, no miracle arrival or coast-to-Greece ground route. No later basilica, Vatican court, medieval bound Bible or exact named church location. Ordinary fictional workshops and household courts; terrain, dated streets and receiving footprints pending. Do not treat modern shore controls as Roman harbor geometry.",
  "corridorStraightLengthsTiles": {
    "north-drafts": 350.82,
    "south-drafts": 392.92,
    "relief": 223.46
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
    "coordinates": [
      [
        12.477,
        41.95
      ],
      [
        12.47,
        41.925
      ],
      [
        12.47,
        41.9
      ],
      [
        12.475,
        41.87
      ],
      [
        12.42,
        41.85
      ],
      [
        12.4,
        41.8
      ],
      [
        12.28,
        41.76
      ],
      [
        12.23,
        41.73
      ]
    ],
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
  "asset": "docs/design/maps/faith-origins/odyssey/20-reconciliation-deliveries-rome-ostia.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-1",
      "role": "fictional-local-request-note",
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
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-2",
      "role": "fictional-local-request-note",
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
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-1",
      "role": "fictional-local-request-note",
      "initialHub": "hub-3",
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
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-2",
      "role": "fictional-local-request-note",
      "initialHub": "hub-3",
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
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-cover-1",
      "role": "fictional-preparation-register",
      "initialHub": "hub-4",
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
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-1",
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
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-2",
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
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.20-reconciliation-deliveries-rome-ostia.destination-5",
      "hub": "hub-5",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    }
  ],
  "objectGroups": {
    "north-local-requests": [
      "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-1",
      "faith-origins.20-reconciliation-deliveries-rome-ostia.north-local-requests-2"
    ],
    "south-local-requests": [
      "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-1",
      "faith-origins.20-reconciliation-deliveries-rome-ostia.south-local-requests-2"
    ],
    "dispatch-cover": [
      "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-cover-1"
    ],
    "dispatch-couriers": [
      "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-1",
      "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-2"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-1",
        "faith-origins.20-reconciliation-deliveries-rome-ostia.dispatch-couriers-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Context without a verdict / Contexto sin veredicto

EN: Recover both separate copies from context without a verdict and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de contexto sin veredicto y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Local working annotations explain the letter’s advocacy; no canonical autograph is placed.

ES: Anotaciones locales de trabajo explican la argumentación; no se coloca un autógrafo canónico.

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
          "20-reconciliation-deliveries-rome-ostia.side-1.entity-1",
          "20-reconciliation-deliveries-rome-ostia.side-1.entity-2"
        ],
        "destinations": {
          "20-reconciliation-deliveries-rome-ostia.side-1.entity-1": "20-reconciliation-deliveries-rome-ostia.side-1.zone-1",
          "20-reconciliation-deliveries-rome-ostia.side-1.entity-2": "20-reconciliation-deliveries-rome-ostia.side-1.zone-1"
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-1.entity-1",
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-1.entity-2",
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-1.zone-1",
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
      "onceFlag": "20-reconciliation-deliveries-rome-ostia.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.20-reconciliation-deliveries-rome-ostia"
      ],
      "historicalNote": {
        "en": "The work known as First Clement addresses the church at Corinth from the church at Rome and argues against the removal of established ministers. The surviving letter advocates reconciliation; it does not report a completed settlement. Its author is unnamed in the text, and c.95 is a conventional approximate date.",
        "es-ES": "La obra conocida como Primera de Clemente se dirige desde la iglesia de Roma a la de Corinto y argumenta contra la destitución de ministros establecidos. La carta conservada aboga por la reconciliación; no informa de un acuerdo consumado. Su autor no figura en el texto y hacia el 95 es una fecha convencional aproximada."
      },
      "hint": {
        "en": "Collect the two northern and two southern local request notes; deliver all four distinct notes to the eastern preparation yard.",
        "es-ES": "Recoge las dos notas locales septentrionales y las dos meridionales; entrega las cuatro notas distintas en el patio oriental de preparación."
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
      "north-drafts",
      "south-drafts",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Preparing households / Hogares que preparan la salida

EN: Bring each of the two aid crates to its assigned household at preparing households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares que preparan la salida. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Support independent households without forcing agreement on leadership.

ES: Apoya hogares independientes sin imponer acuerdo sobre el liderazgo.

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
          "20-reconciliation-deliveries-rome-ostia.side-2.entity-1",
          "20-reconciliation-deliveries-rome-ostia.side-2.entity-2"
        ],
        "destinations": {
          "20-reconciliation-deliveries-rome-ostia.side-2.entity-1": "20-reconciliation-deliveries-rome-ostia.side-2.zone-1",
          "20-reconciliation-deliveries-rome-ostia.side-2.entity-2": "20-reconciliation-deliveries-rome-ostia.side-2.zone-2"
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-2.entity-1",
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-2.entity-2",
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "20-reconciliation-deliveries-rome-ostia.side-2.zone-2",
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
      "onceFlag": "20-reconciliation-deliveries-rome-ostia.side-2.rewarded",
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
      "north-drafts",
      "south-drafts",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Separate dispatch supplies / Provisiones separadas de despacho

EN: Escort the trader of separate dispatch supplies to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de provisiones separadas de despacho hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One bounded exchange supports courier work without replacing the main cover payment.

ES: Un intercambio limitado apoya a los correos sin sustituir el pago principal de la cubierta.

```json
{
  "id": "side-3",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "20-reconciliation-deliveries-rome-ostia.side-3.entity-1"
        ],
        "destinations": {
          "20-reconciliation-deliveries-rome-ostia.side-3.entity-1": "20-reconciliation-deliveries-rome-ostia.side-3.zone-1"
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
        "receipt": "20-reconciliation-deliveries-rome-ostia.side-3.payment",
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-3.entity-1",
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-3.zone-1",
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
      "onceFlag": "20-reconciliation-deliveries-rome-ostia.side-3.rewarded",
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
      "north-drafts",
      "south-drafts",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The eastern writing shed / El cobertizo oriental de escritura

EN: Pay 50 wood and restore the damaged store of the eastern writing shed to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el cobertizo oriental de escritura. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair ordinary storage, not a proven first-century basilica.

ES: Repara un almacén ordinario, no una supuesta basílica del siglo I.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "20-reconciliation-deliveries-rome-ostia.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "20-reconciliation-deliveries-rome-ostia.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "20-reconciliation-deliveries-rome-ostia.side-4.payment",
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-4.entity-1",
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-4.zone-1",
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
      "onceFlag": "20-reconciliation-deliveries-rome-ostia.side-4.rewarded",
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
      "north-drafts",
      "south-drafts",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Northern draft-road survey / Reconocimiento del camino norte de borradores

EN: Scout both marked viewpoints of northern draft-road survey. Benefit: Mark the surveyed north-drafts land circuit once; main receiver markers and requirements remain available without it.

ES: Explora los dos miradores señalados de reconocimiento del camino norte de borradores. Ventaja: Señala una vez el circuito terrestre trazado north-drafts; los receptores principales y sus requisitos siguen disponibles sin él.

EN: Survey the northern request circuit independently of its theological argument.

ES: Reconoce el circuito de peticiones septentrional independientemente de su argumentación teológica.

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
          "20-reconciliation-deliveries-rome-ostia.side-5.zone-1",
          "20-reconciliation-deliveries-rome-ostia.side-5.zone-2"
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "20-reconciliation-deliveries-rome-ostia.side-5.zone-2",
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
      "target": "north-drafts surveyed land circuit",
      "resources": {},
      "onceFlag": "20-reconciliation-deliveries-rome-ostia.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "north-drafts"
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
      "north-drafts",
      "south-drafts",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Southern dispatch guide / Guía meridional de despacho

EN: Escort the local guide of southern dispatch guide to the marked road junction. Benefit: Mark the surveyed south-drafts land circuit once; main receiver markers and requirements remain available without it.

ES: Escolta al guía local de guía meridional de despacho hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado south-drafts; los receptores principales y sus requisitos siguen disponibles sin él.

EN: Marks a south-circuit route; cannot ensure reception in Corinth.

ES: Señala una ruta del circuito sur; no garantiza recepción en Corinto.

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
          "20-reconciliation-deliveries-rome-ostia.side-6.entity-1"
        ],
        "destinations": {
          "20-reconciliation-deliveries-rome-ostia.side-6.entity-1": "20-reconciliation-deliveries-rome-ostia.side-6.zone-1"
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-6.entity-1",
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
        "id": "20-reconciliation-deliveries-rome-ostia.side-6.zone-1",
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
      "target": "south-drafts surveyed land circuit",
      "resources": {},
      "onceFlag": "20-reconciliation-deliveries-rome-ostia.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "south-drafts"
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
      "north-drafts",
      "south-drafts",
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
      "id": "two-team-preparation",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Invest finite writing supply and run two collecting teams, preserving the 60wood20gold main debit.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "context-before-dispatch",
      "optionalObjectives": [
        "side-1",
        "side-5"
      ],
      "costOfOpportunity": "Read attributed argument and survey the north before combining four original notes.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "household-and-south-road",
      "optionalObjectives": [
        "side-2",
        "side-6"
      ],
      "costOfOpportunity": "Support independent households and guide the south branch; disagreement itself is not a defeat flag.",
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
      "wood": 768,
      "gold": 224,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 60,
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
      "wood": 740,
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
      "wood": 790,
      "gold": 235,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 60,
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
      "wood": 740,
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
      "wood": 813,
      "gold": 247,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 60,
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
      "wood": 740,
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
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.title / always | none | A Letter Across the Divide | Una carta sobre la división |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.fact-intro / intro first | collection-narrator | The work known as First Clement addresses the church at Corinth from the church at Rome and argues against the removal of established ministers. The surviving letter advocates reconciliation; it does not report a completed settlement. Its author is unnamed in the text, and c.95 is a conventional approximate date. | La obra conocida como Primera de Clemente se dirige desde la iglesia de Roma a la de Corinto y argumenta contra la destitución de ministros establecidos. La carta conservada aboga por la reconciliación; no informa de un acuerdo consumado. Su autor no figura en el texto y hacia el 95 es una fecha convencional aproximada. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.persona-intro / after handover | miriam-archive | I once confused a strong appeal with an agreement. A page can ask for peace in every line and still leave its reader free to refuse. In this older letter, I listen for what is urged, then stop where the evidence stops. | Una vez confundí un llamamiento firme con un acuerdo. Una página puede pedir paz en cada línea y dejar al lector libre de negarse. En esta carta anterior escucho lo que se reclama y me detengo donde termina la evidencia. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.route-help / available from start; repeatable without effect | none | This is one local Roman scene. All receivers are marked, and every route remains east of the Tiber. Any journey to Corinth stays outside the playable map. | Es una escena romana local. Todos los receptores están señalados y las rutas permanecen al este del Tíber. Cualquier viaje hasta Corinto queda fuera del mapa jugable. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.o1-goal / phase-1 active | none | Collect the two northern and two southern local request notes; deliver all four distinct notes to the eastern preparation yard. | Recoge las dos notas locales septentrionales y las dos meridionales; entrega las cuatro notas distintas en el patio oriental de preparación. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.o1-receipt / o1 latched once | none | Two separate note pairs have arrived without substituting one for the other. | Han llegado dos parejas separadas de notas sin sustituir una por otra. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.o1-reaction / after o1 receipt | miriam-archive | A reply assembled from only one side would be easier. That is not why I became a copyist. | Sería más fácil preparar una respuesta con un solo lado. No me hice copista para eso. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.o2-goal / phase-2 active | none | Pay 60 wood and 20 gold at the preparation yard, then create one cover register from the four collected request notes. | Paga 60 de madera y 20 de oro en el patio de preparación y después crea un registro de cubierta con las cuatro notas recogidas. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.o2-receipt / o2 latched once | none | One preparation register is backed by its exact paid receipt and four original inputs. | Un registro de preparación está respaldado por su recibo pagado exacto y cuatro entradas originales. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.o2-reaction / after o2 receipt | miriam-archive | The cover records our preparation, not a verdict on who was right at Corinth. | La cubierta registra nuestra preparación, no un veredicto sobre quién tenía razón en Corinto. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.o3-goal / phase-3 active | none | Bring the original cover register and both original couriers alive to the inland dispatch district. | Lleva el registro de cubierta original y ambos correos originales con vida al distrito interior de despacho. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.o3-receipt / o3 latched once | none | The local dispatch party is ready; no off-map delivery or reconciliation has been certified. | El grupo local de despacho está listo; no se ha acreditado entrega fuera del mapa ni reconciliación. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.o3-reaction / after o3 receipt | miriam-archive | The road begins where this scene ends. Another voice will have to tell what followed. | El camino empieza donde acaba esta escena. Otra voz deberá contar lo que vino después. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from context without a verdict and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de contexto sin veredicto y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-1-complete / side-1 completed | none | Context without a verdict completed. Its stated benefit has been granted once. | Contexto sin veredicto: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-1-lost / side-1 failed-optional | none | Context without a verdict is unavailable after the loss of its unique participant or object. The main mission continues. | Contexto sin veredicto: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at preparing households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares que preparan la salida. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-2-complete / side-2 completed | none | Preparing households completed. Its stated benefit has been granted once. | Hogares que preparan la salida: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-2-lost / side-2 failed-optional | none | Preparing households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares que preparan la salida: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-3-goal / optional list from start | none | Escort the trader of separate dispatch supplies to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de provisiones separadas de despacho hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-3-complete / side-3 completed | none | Separate dispatch supplies completed. Its stated benefit has been granted once. | Provisiones separadas de despacho: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-3-lost / side-3 failed-optional | none | Separate dispatch supplies is unavailable after the loss of its unique participant or object. The main mission continues. | Provisiones separadas de despacho: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the eastern writing shed to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el cobertizo oriental de escritura. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-4-complete / side-4 completed | none | The eastern writing shed completed. Its stated benefit has been granted once. | El cobertizo oriental de escritura: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-4-lost / side-4 failed-optional | none | The eastern writing shed is unavailable after the loss of its unique participant or object. The main mission continues. | El cobertizo oriental de escritura: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of northern draft-road survey. Benefit: Mark the surveyed north-drafts land circuit once; main receiver markers and requirements remain available without it. | Explora los dos miradores señalados de reconocimiento del camino norte de borradores. Ventaja: Señala una vez el circuito terrestre trazado north-drafts; los receptores principales y sus requisitos siguen disponibles sin él. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-5-complete / side-5 completed | none | Northern draft-road survey completed. Its stated benefit has been granted once. | Reconocimiento del camino norte de borradores: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-5-lost / side-5 failed-optional | none | Northern draft-road survey is unavailable after the loss of its unique participant or object. The main mission continues. | Reconocimiento del camino norte de borradores: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-6-goal / optional list from start | none | Escort the local guide of southern dispatch guide to the marked road junction. Benefit: Mark the surveyed south-drafts land circuit once; main receiver markers and requirements remain available without it. | Escolta al guía local de guía meridional de despacho hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado south-drafts; los receptores principales y sus requisitos siguen disponibles sin él. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-6-complete / side-6 completed | none | Southern dispatch guide completed. Its stated benefit has been granted once. | Guía meridional de despacho: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.side-6-lost / side-6 failed-optional | none | Southern dispatch guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía meridional de despacho: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.fact-outro / victory first | collection-narrator | Fictional local drafts and couriers reached a Roman dispatch district. This completes preparation, not a journey to Corinth or proof that the dispute ended. The historical letter remains an appeal whose arguments and reception must be distinguished. | Borradores locales y correos ficticios alcanzaron un distrito romano de despacho. Se completa la preparación, no el viaje a Corinto ni la prueba de que acabara la disputa. La carta histórica sigue siendo un llamamiento: sus argumentos y su recepción deben distinguirse. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.persona-outro / after fact-outro | miriam-archive | I can fold a page and choose a road. I cannot fold another person’s answer into the same packet. Let the shelf preserve that distinction, however much I want a peaceful ending. | Puedo doblar una página y elegir un camino. No puedo doblar en el mismo paquete la respuesta ajena. Que la estantería conserve esa distinción, por mucho que desee un final pacífico. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.20-reconciliation-deliveries-rome-ostia.odyssey.next-episode / after persona-outro | none | Continue with The Governor's Question. This episode does not complete the campaign. | Continúa con La pregunta del gobernador. Este episodio no termina la campaña. |

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
      "both distinct request pairs required",
      "same two couriers required alive at local dispatch",
      "no modern translation as ancient packet",
      "prepared cover cannot prove Corinth reception or accord",
      "every route east ofTiber; no forced bridge",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
