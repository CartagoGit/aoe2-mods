# 23. A Petition from Sardes

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `23-petition-escort-sardes` · c. 170–180 CE · 360×360

## Historical frame and fixed outcome

EN: Eusebius preserves fragments of an appeal attributed to Melito of Sardis. Its author reports dispossession and asks the emperor to examine the measures and their origin. The fragment is an advocate’s argument, not proof of a uniform policy or a successful repeal. Its date is approximate.

ES: Eusebio conserva fragmentos de un llamamiento atribuido a Melitón de Sardes. Su autor denuncia desposesiones y pide al emperador que examine las medidas y su origen. El fragmento es una argumentación de parte, no prueba de una política uniforme ni de una revocación lograda. Su fecha es aproximada.

EN: The fictional party has dispatched a local working packet after gathering materials. It has not delivered Melito’s historical appeal to the emperor, secured a reply or repealed a decree. The transmitted fragment leaves those outcomes unproved.

ES: El grupo ficticio ha despachado un paquete local de trabajo tras reunir sus materiales. No ha entregado al emperador el llamamiento histórico de Melitón, obtenido respuesta ni revocado un decreto. El fragmento transmitido no acredita esos resultados.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 16,
      "episodeId": "23-petition-escort-sardes",
      "order": 23,
      "selectedSourceUrl": "https://www.earlychristianwritings.com/melito.html",
      "consultedUrl": "https://jerihna.sourceschretiennes.org/en/work-editions/apologia-ad-marcum-aurelium-/oxford-early-christian-texts",
      "passage": "Melito, Apology fragments preserved at Eusebius, Ecclesiastical History 4.26.5–11; source record gives fragment provenance and bibliographic editions.",
      "supportedClaim": {
        "en": "Eusebius preserves fragments of a work attributed to Melito and addressed to an emperor, arguing that Christian teaching had benefited the empire.",
        "es-ES": "Eusebio conserva fragmentos de una obra atribuida a Melitón y dirigida a un emperador, donde sostiene que la enseñanza cristiana benefició al imperio."
      },
      "limitations": "The fragment does not simply 'denounce measures' in the form asserted by the candidate; it asks the emperor to examine recent anti-Christian measures and appeals to imperial justice. The surviving text is fragmentary, mediated by Eusebius, and date/address details are debated.",
      "consultationDate": "2026-10-12",
      "status": "disputed",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://en.wikisource.org/wiki/Nicene_and_Post-Nicene_Fathers:_Series_II/Volume_I/Church_History_of_Eusebius/Book_IV/Chapter_26",
      "passage": "HEIV26.5–11; architect read appeal, alleged plundering, request to examine measures and rhetoric of imperial favor",
      "limitations": "Old public-domain translation mediated by Eusebius; fragmentary advocacy, no proved answer, repeal or exact local address. New Advent bookIV repeatedly timed out; not claimed as consulted full text.",
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

EN: Collect both household requests and both workshop requests; deliver all four original identities to the filing yard.

ES: Recoge ambas peticiones domésticas y ambas artesanales; entrega las cuatro identidades originales en el patio de archivo.

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
        "faith-origins.23-petition-escort-sardes.household-requests-1",
        "faith-origins.23-petition-escort-sardes.household-requests-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "faith-origins.23-petition-escort-sardes.workshop-requests-1",
        "faith-origins.23-petition-escort-sardes.workshop-requests-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "faith-origins.23-petition-escort-sardes.household-requests-1",
        "faith-origins.23-petition-escort-sardes.household-requests-2"
      ],
      "destinations": {
        "faith-origins.23-petition-escort-sardes.household-requests-1": "faith-origins.23-petition-escort-sardes.destination-3",
        "faith-origins.23-petition-escort-sardes.household-requests-2": "faith-origins.23-petition-escort-sardes.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "faith-origins.23-petition-escort-sardes.workshop-requests-1",
        "faith-origins.23-petition-escort-sardes.workshop-requests-2"
      ],
      "destinations": {
        "faith-origins.23-petition-escort-sardes.workshop-requests-1": "faith-origins.23-petition-escort-sardes.destination-3",
        "faith-origins.23-petition-escort-sardes.workshop-requests-2": "faith-origins.23-petition-escort-sardes.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both local request groups are received separately.

ES: Se han recibido por separado ambos grupos locales de peticiones.

EN: Our invented requests cannot authenticate a missing ancient page.

ES: Nuestras peticiones inventadas no autentican una página antigua perdida.

### o2 / phase-2

EN: Pay 80 wood and 30 gold once at the filing yard; create the local working cover from all four collected requests.

ES: Paga una vez 80 de madera y 30 de oro en el patio de archivo; crea la cubierta local de trabajo a partir de las cuatro peticiones recogidas.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 80,
        "gold": 30
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.23-petition-escort-sardes.destination-3"
      ],
      "allocations": {
        "faith-origins.23-petition-escort-sardes.destination-3": {
          "wood": 80,
          "gold": 30
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.23-petition-escort-sardes.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "faith-origins.23-petition-escort-sardes.household-requests-1",
        "faith-origins.23-petition-escort-sardes.household-requests-2",
        "faith-origins.23-petition-escort-sardes.workshop-requests-1",
        "faith-origins.23-petition-escort-sardes.workshop-requests-2"
      ],
      "outputEntities": [
        "faith-origins.23-petition-escort-sardes.working-cover-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.23-petition-escort-sardes.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 80,
            "gold": 30
          },
          "newDebit": false
        }
      ]
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The funded local cover is ready; no official seal or reply has been created.

ES: Está lista la cubierta local financiada; no se ha creado un sello oficial ni una respuesta.

EN: I can label our work without lending it the emperor’s authority.

ES: Puedo etiquetar nuestro trabajo sin prestarle la autoridad del emperador.

### o3 / phase-3

EN: Bring the original local cover and both original couriers alive to the eastern inland dispatch station.

ES: Lleva la cubierta local original y ambos correos originales con vida a la estación oriental interior de despacho.

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
        "faith-origins.23-petition-escort-sardes.working-cover-1"
      ],
      "destinations": {
        "faith-origins.23-petition-escort-sardes.working-cover-1": "faith-origins.23-petition-escort-sardes.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.23-petition-escort-sardes.dispatch-couriers-1",
        "faith-origins.23-petition-escort-sardes.dispatch-couriers-2"
      ],
      "destinations": {
        "faith-origins.23-petition-escort-sardes.dispatch-couriers-1": "faith-origins.23-petition-escort-sardes.destination-4",
        "faith-origins.23-petition-escort-sardes.dispatch-couriers-2": "faith-origins.23-petition-escort-sardes.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The fictional local dispatch is complete; a subsequent imperial delivery is not observed.

ES: Se ha completado el despacho local ficticio; no se observa una entrega imperial posterior.

EN: A departure point is a promise of travel, not evidence of its ending.

ES: Un punto de salida promete un viaje, no acredita su final.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/23-petition-escort-sardes.svg)

```json
{
  "bbox": [
    28.032,
    38.487,
    28.078,
    38.519
  ],
  "terrainProfile": "sardes",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        207.37,
        268.54
      ],
      "lonLat": [
        28.059,
        38.493
      ],
      "name": {
        "en": "Eastern household request court",
        "es-ES": "Patio oriental de peticiones domésticas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        130.72,
        117.17
      ],
      "lonLat": [
        28.048,
        38.51
      ],
      "name": {
        "en": "Northern workshop request court",
        "es-ES": "Patio septentrional de peticiones artesanales"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        242.21,
        188.4
      ],
      "lonLat": [
        28.064,
        38.502
      ],
      "name": {
        "en": "Local assembly and filing yard",
        "es-ES": "Patio local de reunión y archivo"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        304.93,
        90.46
      ],
      "lonLat": [
        28.073,
        38.513
      ],
      "name": {
        "en": "Eastern inland dispatch station",
        "es-ES": "Estación oriental interior de despacho"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "household-road",
      "hubOrder": [
        "hub-1",
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "workshop-road",
      "hubOrder": [
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
        "hub-2",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "east of schematic Pactolus; graded lower-slope access, no acropolis shortcut or river ford"
    }
  ],
  "terrainInstructions": "Sardis on the lower Tmolus foothills and Hermus plain margin. Four fictional local districts lie east of the schematic Pactolus control and avoid its alluvial fan and the steep acropolis. Grade each inland approach from DEM and dated archaeology before native work; straight corridor sketches are not navigable paths. No forced river crossing, modern highway, Ottoman village, later city wall, restored Marble Court or late-antique synagogue mosaics. The UNESCO point is a whole-property anchor, never Melito’s desk or a second-century building footprint. Long-distance imperial correspondence leaves the map.",
  "corridorStraightLengthsTiles": {
    "household-road": 203.69,
    "workshop-road": 248.6,
    "relief": 345.92
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
        28.031,
        38.465
      ],
      [
        28.031,
        38.475
      ],
      [
        28.036,
        38.488
      ],
      [
        28.038,
        38.502
      ],
      [
        28.034,
        38.515
      ],
      [
        28.03,
        38.525
      ]
    ],
    "certainty": "architect schematic relation only, not surveyed current or ancient river centerline; do not rasterize as native water",
    "renderAs": "river-line"
  },
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/faith-origins/odyssey/23-petition-escort-sardes.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.23-petition-escort-sardes.household-requests-1",
      "role": "fictional-local-request",
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
      "id": "faith-origins.23-petition-escort-sardes.household-requests-2",
      "role": "fictional-local-request",
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
      "id": "faith-origins.23-petition-escort-sardes.workshop-requests-1",
      "role": "fictional-local-request",
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
      "id": "faith-origins.23-petition-escort-sardes.workshop-requests-2",
      "role": "fictional-local-request",
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
      "id": "faith-origins.23-petition-escort-sardes.working-cover-1",
      "role": "fictional-local-dispatch-cover",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.23-petition-escort-sardes.dispatch-couriers-1",
      "role": "fictional-voluntary-courier",
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
      "id": "faith-origins.23-petition-escort-sardes.dispatch-couriers-2",
      "role": "fictional-voluntary-courier",
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
    }
  ],
  "zones": [
    {
      "id": "faith-origins.23-petition-escort-sardes.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.23-petition-escort-sardes.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.23-petition-escort-sardes.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.23-petition-escort-sardes.destination-4",
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
    "household-requests": [
      "faith-origins.23-petition-escort-sardes.household-requests-1",
      "faith-origins.23-petition-escort-sardes.household-requests-2"
    ],
    "workshop-requests": [
      "faith-origins.23-petition-escort-sardes.workshop-requests-1",
      "faith-origins.23-petition-escort-sardes.workshop-requests-2"
    ],
    "working-cover": [
      "faith-origins.23-petition-escort-sardes.working-cover-1"
    ],
    "dispatch-couriers": [
      "faith-origins.23-petition-escort-sardes.dispatch-couriers-1",
      "faith-origins.23-petition-escort-sardes.dispatch-couriers-2"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.23-petition-escort-sardes.dispatch-couriers-1",
        "faith-origins.23-petition-escort-sardes.dispatch-couriers-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### The unanswered margin / El margen sin respuesta

EN: Recover both separate copies from the unanswered margin and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de el margen sin respuesta y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Source context distinguishes a surviving appeal from an unproved imperial answer.

ES: El contexto distingue un llamamiento conservado de una respuesta imperial no acreditada.

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
          "23-petition-escort-sardes.side-1.entity-1",
          "23-petition-escort-sardes.side-1.entity-2"
        ],
        "destinations": {
          "23-petition-escort-sardes.side-1.entity-1": "23-petition-escort-sardes.side-1.zone-1",
          "23-petition-escort-sardes.side-1.entity-2": "23-petition-escort-sardes.side-1.zone-1"
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
        "id": "23-petition-escort-sardes.side-1.entity-1",
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
        "id": "23-petition-escort-sardes.side-1.entity-2",
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
        "id": "23-petition-escort-sardes.side-1.zone-1",
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
      "onceFlag": "23-petition-escort-sardes.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.23-petition-escort-sardes"
      ],
      "historicalNote": {
        "en": "Eusebius preserves fragments of an appeal attributed to Melito of Sardis. Its author reports dispossession and asks the emperor to examine the measures and their origin. The fragment is an advocate’s argument, not proof of a uniform policy or a successful repeal. Its date is approximate.",
        "es-ES": "Eusebio conserva fragmentos de un llamamiento atribuido a Melitón de Sardes. Su autor denuncia desposesiones y pide al emperador que examine las medidas y su origen. El fragmento es una argumentación de parte, no prueba de una política uniforme ni de una revocación lograda. Su fecha es aproximada."
      },
      "hint": {
        "en": "Collect both household requests and both workshop requests; deliver all four original identities to the filing yard.",
        "es-ES": "Recoge ambas peticiones domésticas y ambas artesanales; entrega las cuatro identidades originales en el patio de archivo."
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
      "household-road",
      "workshop-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Independent lower-slope households / Hogares independientes de la ladera baja

EN: Bring each of the two aid crates to its assigned household at independent lower-slope households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes de la ladera baja. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Two separate aid deliveries do not substitute for the four main requests.

ES: Dos entregas de ayuda separadas no sustituyen las cuatro peticiones principales.

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
          "23-petition-escort-sardes.side-2.entity-1",
          "23-petition-escort-sardes.side-2.entity-2"
        ],
        "destinations": {
          "23-petition-escort-sardes.side-2.entity-1": "23-petition-escort-sardes.side-2.zone-1",
          "23-petition-escort-sardes.side-2.entity-2": "23-petition-escort-sardes.side-2.zone-2"
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
        "id": "23-petition-escort-sardes.side-2.entity-1",
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
        "id": "23-petition-escort-sardes.side-2.entity-2",
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
        "id": "23-petition-escort-sardes.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "23-petition-escort-sardes.side-2.zone-2",
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
      "onceFlag": "23-petition-escort-sardes.side-2.rewarded",
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
      "household-road",
      "workshop-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The lower-road supply shed / El cobertizo de provisiones del camino bajo

EN: Pay 50 wood and restore the damaged store of the lower-road supply shed to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el cobertizo de provisiones del camino bajo. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A finite ordinary shed repair cannot restore a later monumental Marble Court.

ES: Reparar un cobertizo ordinario finito no restaura un Patio de Mármol posterior.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "23-petition-escort-sardes.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "23-petition-escort-sardes.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "23-petition-escort-sardes.side-3.payment",
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
        "id": "23-petition-escort-sardes.side-3.entity-1",
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
        "id": "23-petition-escort-sardes.side-3.zone-1",
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
      "onceFlag": "23-petition-escort-sardes.side-3.rewarded",
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
      "household-road",
      "workshop-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The workshop provision share / La aportación de provisiones del taller

EN: Escort the trader of the workshop provision share to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de la aportación de provisiones del taller hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A bounded exchange helps the local journey and does not purchase an imperial verdict.

ES: Un intercambio limitado ayuda al viaje local y no compra un veredicto imperial.

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
          "23-petition-escort-sardes.side-4.entity-1"
        ],
        "destinations": {
          "23-petition-escort-sardes.side-4.entity-1": "23-petition-escort-sardes.side-4.zone-1"
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
        "receipt": "23-petition-escort-sardes.side-4.payment",
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
        "id": "23-petition-escort-sardes.side-4.entity-1",
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
        "id": "23-petition-escort-sardes.side-4.zone-1",
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
      "onceFlag": "23-petition-escort-sardes.side-4.rewarded",
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
      "household-road",
      "workshop-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Northern approach viewpoints / Miradores del acceso septentrional

EN: Scout both marked viewpoints of northern approach viewpoints. Benefit: Mark the surveyed workshop-road land circuit once. All main receivers remain disclosed without this optional task.

ES: Explora los dos miradores señalados de miradores del acceso septentrional. Ventaja: Señala una vez el circuito terrestre trazado workshop-road. Todos los receptores principales siguen identificados sin esta tarea opcional.

EN: Observe the workshop-road approach, not the steep acropolis as an invented shortcut.

ES: Observa el acceso del camino artesanal, no la acrópolis escarpada como atajo inventado.

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
          "23-petition-escort-sardes.side-5.zone-1",
          "23-petition-escort-sardes.side-5.zone-2"
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
        "id": "23-petition-escort-sardes.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "23-petition-escort-sardes.side-5.zone-2",
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
      "target": "workshop-road surveyed land circuit",
      "resources": {},
      "onceFlag": "23-petition-escort-sardes.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "workshop-road"
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
      "household-road",
      "workshop-road",
      "relief"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A lower-slope inland guide / Un guía interior de la ladera baja

EN: Escort the local guide of a lower-slope inland guide to the marked road junction. Benefit: Mark the surveyed relief land circuit once. All main receivers remain disclosed without this optional task.

ES: Escolta al guía local de un guía interior de la ladera baja hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado relief. Todos los receptores principales siguen identificados sin esta tarea opcional.

EN: Marks the surveyed eastern-bank circuit without creating a ford or official travel permit.

ES: Señala el circuito trazado de la margen oriental sin crear un vado ni permiso oficial de viaje.

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
          "23-petition-escort-sardes.side-6.entity-1"
        ],
        "destinations": {
          "23-petition-escort-sardes.side-6.entity-1": "23-petition-escort-sardes.side-6.zone-1"
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
        "id": "23-petition-escort-sardes.side-6.entity-1",
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
        "id": "23-petition-escort-sardes.side-6.zone-1",
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
      "onceFlag": "23-petition-escort-sardes.side-6.rewarded",
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
      "household-road",
      "workshop-road",
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
      "id": "split-request-crews",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Split household/workshop collection and finite supply investment; reserve the exact80wood30goldmain cost.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "context-and-north-survey",
      "optionalObjectives": [
        "side-1",
        "side-5"
      ],
      "costOfOpportunity": "Read the fragment’s limits while surveying the separate northern pickup approach.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "care-and-low-slope-dispatch",
      "optionalObjectives": [
        "side-2",
        "side-6"
      ],
      "costOfOpportunity": "Combine independent aid with the graded relief circuit; preserve both original couriers.",
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
      "wood": 788,
      "gold": 234,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
      "gold": 30,
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
      "gold": 320,
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
      "wood": 810,
      "gold": 245,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
      "gold": 30,
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
      "gold": 320,
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
      "wood": 833,
      "gold": 257,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 80,
      "gold": 30,
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
      "gold": 320,
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
| scenario.faith-origins.23-petition-escort-sardes.odyssey.title / always | none | A Petition from Sardes | Una petición desde Sardes |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.fact-intro / intro first | collection-narrator | Eusebius preserves fragments of an appeal attributed to Melito of Sardis. Its author reports dispossession and asks the emperor to examine the measures and their origin. The fragment is an advocate’s argument, not proof of a uniform policy or a successful repeal. Its date is approximate. | Eusebio conserva fragmentos de un llamamiento atribuido a Melitón de Sardes. Su autor denuncia desposesiones y pide al emperador que examine las medidas y su origen. El fragmento es una argumentación de parte, no prueba de una política uniforme ni de una revocación lograda. Su fecha es aproximada. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.persona-intro / after handover | miriam-archive | I have inherited this appeal, not the answer its writer hoped for. I find myself wanting to put a reassuring reply on the next shelf. That wish is mine; the empty shelf must remain empty. | He heredado este llamamiento, no la respuesta que esperaba quien lo escribió. Me descubro deseando colocar una contestación tranquilizadora en el estante siguiente. Ese deseo es mío; el estante vacío debe seguir vacío. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.route-help / available from start; repeatable without effect | none | Collect the two household requests from the eastern court and the two workshop requests from the northern court. Bring all four to the filing yard, pay 80 wood and 30 gold once, and assemble one local cover. Deliver it with both original couriers to the eastern dispatch station; the emperor and any reply remain off-map. | Recoge las dos peticiones domésticas del patio oriental y las dos artesanales del septentrional. Lleva las cuatro al patio de archivo, paga una vez 80 de madera y 30 de oro y prepara una cubierta local. Entrégala con ambos correos originales en la estación oriental de despacho; el emperador y cualquier respuesta quedan fuera del mapa. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.o1-goal / phase-1 active | none | Collect both household requests and both workshop requests; deliver all four original identities to the filing yard. | Recoge ambas peticiones domésticas y ambas artesanales; entrega las cuatro identidades originales en el patio de archivo. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.o1-receipt / o1 latched once | none | Both local request groups are received separately. | Se han recibido por separado ambos grupos locales de peticiones. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.o1-reaction / after o1 receipt | miriam-archive | Our invented requests cannot authenticate a missing ancient page. | Nuestras peticiones inventadas no autentican una página antigua perdida. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.o2-goal / phase-2 active | none | Pay 80 wood and 30 gold once at the filing yard; create the local working cover from all four collected requests. | Paga una vez 80 de madera y 30 de oro en el patio de archivo; crea la cubierta local de trabajo a partir de las cuatro peticiones recogidas. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.o2-receipt / o2 latched once | none | The funded local cover is ready; no official seal or reply has been created. | Está lista la cubierta local financiada; no se ha creado un sello oficial ni una respuesta. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.o2-reaction / after o2 receipt | miriam-archive | I can label our work without lending it the emperor’s authority. | Puedo etiquetar nuestro trabajo sin prestarle la autoridad del emperador. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.o3-goal / phase-3 active | none | Bring the original local cover and both original couriers alive to the eastern inland dispatch station. | Lleva la cubierta local original y ambos correos originales con vida a la estación oriental interior de despacho. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.o3-receipt / o3 latched once | none | The fictional local dispatch is complete; a subsequent imperial delivery is not observed. | Se ha completado el despacho local ficticio; no se observa una entrega imperial posterior. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.o3-reaction / after o3 receipt | miriam-archive | A departure point is a promise of travel, not evidence of its ending. | Un punto de salida promete un viaje, no acredita su final. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from the unanswered margin and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de el margen sin respuesta y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-1-complete / side-1 completed | none | The unanswered margin completed. Its stated benefit has been granted once. | El margen sin respuesta: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-1-lost / side-1 failed-optional | none | The unanswered margin is unavailable after the loss of its unique participant or object. The main mission continues. | El margen sin respuesta: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at independent lower-slope households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares independientes de la ladera baja. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-2-complete / side-2 completed | none | Independent lower-slope households completed. Its stated benefit has been granted once. | Hogares independientes de la ladera baja: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-2-lost / side-2 failed-optional | none | Independent lower-slope households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares independientes de la ladera baja: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the lower-road supply shed to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el cobertizo de provisiones del camino bajo. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-3-complete / side-3 completed | none | The lower-road supply shed completed. Its stated benefit has been granted once. | El cobertizo de provisiones del camino bajo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-3-lost / side-3 failed-optional | none | The lower-road supply shed is unavailable after the loss of its unique participant or object. The main mission continues. | El cobertizo de provisiones del camino bajo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-4-goal / optional list from start | none | Escort the trader of the workshop provision share to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de la aportación de provisiones del taller hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-4-complete / side-4 completed | none | The workshop provision share completed. Its stated benefit has been granted once. | La aportación de provisiones del taller: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-4-lost / side-4 failed-optional | none | The workshop provision share is unavailable after the loss of its unique participant or object. The main mission continues. | La aportación de provisiones del taller: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of northern approach viewpoints. Benefit: Mark the surveyed workshop-road land circuit once. All main receivers remain disclosed without this optional task. | Explora los dos miradores señalados de miradores del acceso septentrional. Ventaja: Señala una vez el circuito terrestre trazado workshop-road. Todos los receptores principales siguen identificados sin esta tarea opcional. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-5-complete / side-5 completed | none | Northern approach viewpoints completed. Its stated benefit has been granted once. | Miradores del acceso septentrional: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-5-lost / side-5 failed-optional | none | Northern approach viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores del acceso septentrional: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-6-goal / optional list from start | none | Escort the local guide of a lower-slope inland guide to the marked road junction. Benefit: Mark the surveyed relief land circuit once. All main receivers remain disclosed without this optional task. | Escolta al guía local de un guía interior de la ladera baja hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre trazado relief. Todos los receptores principales siguen identificados sin esta tarea opcional. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-6-complete / side-6 completed | none | A lower-slope inland guide completed. Its stated benefit has been granted once. | Un guía interior de la ladera baja: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.side-6-lost / side-6 failed-optional | none | A lower-slope inland guide is unavailable after the loss of its unique participant or object. The main mission continues. | Un guía interior de la ladera baja: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.fact-outro / victory first | collection-narrator | The fictional party has dispatched a local working packet after gathering materials. It has not delivered Melito’s historical appeal to the emperor, secured a reply or repealed a decree. The transmitted fragment leaves those outcomes unproved. | El grupo ficticio ha despachado un paquete local de trabajo tras reunir sus materiales. No ha entregado al emperador el llamamiento histórico de Melitón, obtenido respuesta ni revocado un decreto. El fragmento transmitido no acredita esos resultados. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.persona-outro / after fact-outro | miriam-archive | I can finish our imagined packet without finishing someone else’s uncertainty. The restraint costs me more than the ink. | Puedo terminar nuestro paquete imaginado sin resolver la incertidumbre ajena. Esa prudencia me cuesta más que la tinta. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.23-petition-escort-sardes.odyssey.next-episode / after persona-outro | none | Continue with The River Kept Their Names. This episode does not complete the campaign. | Continúa con El río conservó sus nombres. Este episodio no termina la campaña. |

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
      "one request identity cannot count in both request groups",
      "four requests at wrong court do not satisfy arrival",
      "cover cannot derive before exact80wood30goldreceipt",
      "both original couriers required independently of packet identity",
      "no route crosses schematic Pactolus or climbs an ungraded acropolis",
      "later Sardis reference photographs never shown as170–180views",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
