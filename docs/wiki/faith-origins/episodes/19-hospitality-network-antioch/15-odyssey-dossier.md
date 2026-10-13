# 19. The House Before the Road

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `19-hospitality-network-antioch` · c. 90–100 CE; Syrian provenance proposed · 400×400

## Historical frame and fixed outcome

EN: The Didache gives rules for receiving itinerants, helping travelers and supporting people who settle and work. These are prescriptions, not a survey of universal practice. Its Syrian provenance and date are proposals; this Antioch hospitality network is fictional.

ES: La Didaché prescribe cómo recibir itinerantes, ayudar a viajeros y apoyar a quienes se establecen y trabajan. Son normas, no un estudio de prácticas universales. Su procedencia siria y fecha son propuestas; esta red de hospitalidad en Antioquía es ficticia.

EN: Six fictional travelers received bounded help and continued along a local road. This does not demonstrate that every community followed the Didache, identify a prophet, or settle the document’s composition history.

ES: Seis viajeros ficticios recibieron ayuda limitada y siguieron por un camino local. Esto no demuestra que todas las comunidades siguieran la Didaché, identifica a un profeta ni resuelve la historia de composición del documento.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 12,
      "episodeId": "19-hospitality-network-antioch",
      "order": 19,
      "selectedSourceUrl": "https://www.earlychristianwritings.com/didache.html",
      "consultedUrl": "https://www.earlychristianwritings.com/didache.html",
      "passage": "Didache, especially chapters 7 (baptism), 9–10 (prayers), 11–13 (itinerant teachers/prophets), and 14–15 (assembly and local officers); academic discussion of composite date and provenance consulted via Cambridge HTR abstract.",
      "supportedClaim": {
        "en": "The Didache contains instructions on baptism, communal prayer, itinerant teachers, and local leadership.",
        "es-ES": "La Didaché contiene instrucciones sobre bautismo, oración comunitaria, maestros itinerantes y liderazgo local."
      },
      "limitations": "Its date and place of composition remain disputed; Syrian provenance is a proposal, not established fact. The earlychristianwritings page is an edition/translation resource, while the Cambridge source is abstract only.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.earlychristianwritings.com/text/didache-hoole.html",
      "passage": "Didache11–13; architect read itinerant/settled visitor instructions",
      "limitations": "Normative text, not universal practice or securely dated Antioch institution; text not copied verbatim into player dialogue.",
      "consultationDate": "2026-10-13",
      "status": "architect consulted; independent approval pending"
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

EN: Bring all three north-road travelers alive to the western hosting court and all three east-road travelers alive to the southern court.

ES: Lleva con vida a los tres viajeros del camino norte al patio occidental de acogida y a los tres del camino oriental al patio meridional.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "faith-origins.19-hospitality-network-antioch.north-travelers-1",
        "faith-origins.19-hospitality-network-antioch.north-travelers-2",
        "faith-origins.19-hospitality-network-antioch.north-travelers-3"
      ],
      "destinations": {
        "faith-origins.19-hospitality-network-antioch.north-travelers-1": "faith-origins.19-hospitality-network-antioch.destination-2",
        "faith-origins.19-hospitality-network-antioch.north-travelers-2": "faith-origins.19-hospitality-network-antioch.destination-2",
        "faith-origins.19-hospitality-network-antioch.north-travelers-3": "faith-origins.19-hospitality-network-antioch.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.19-hospitality-network-antioch.east-travelers-1",
        "faith-origins.19-hospitality-network-antioch.east-travelers-2",
        "faith-origins.19-hospitality-network-antioch.east-travelers-3"
      ],
      "destinations": {
        "faith-origins.19-hospitality-network-antioch.east-travelers-1": "faith-origins.19-hospitality-network-antioch.destination-3",
        "faith-origins.19-hospitality-network-antioch.east-travelers-2": "faith-origins.19-hospitality-network-antioch.destination-3",
        "faith-origins.19-hospitality-network-antioch.east-travelers-3": "faith-origins.19-hospitality-network-antioch.destination-3"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true,
  "exportedLedgers": [
    {
      "id": "north-hosted",
      "operator": "intersection",
      "fromRequirements": [
        "req-1"
      ],
      "minimumCount": 3
    },
    {
      "id": "east-hosted",
      "operator": "intersection",
      "fromRequirements": [
        "req-2"
      ],
      "minimumCount": 3
    }
  ]
}
```

EN: Six distinct travelers arrived at their assigned hosts.

ES: Seis viajeros distintos han llegado a sus anfitriones asignados.

EN: They are fictional guests, not prophets whose truth a game can judge.

ES: Son huéspedes ficticios, no profetas cuya verdad pueda juzgar un juego.

### o2 / phase-2

EN: Pay 120 food at each hosting court once: 240 food in total.

ES: Paga una sola vez 120 de alimento en cada patio de acogida: 240 en total.

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
        "faith-origins.19-hospitality-network-antioch.destination-2",
        "faith-origins.19-hospitality-network-antioch.destination-3"
      ],
      "allocations": {
        "faith-origins.19-hospitality-network-antioch.destination-2": {
          "food": 120
        },
        "faith-origins.19-hospitality-network-antioch.destination-3": {
          "food": 120
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.19-hospitality-network-antioch.o2.req-1.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both hosting shares are paid with one conserved transaction.

ES: Ambas partes de acogida están pagadas mediante una transacción conservada.

EN: The rule speaks in a voice from its time; our food account measures only this imagined help.

ES: La norma habla con una voz de su tiempo; nuestra cuenta de alimento solo mide esta ayuda imaginada.

### o3 / phase-3

EN: Take the same three northern and same three eastern hosted travelers alive to the northeastern onward road.

ES: Lleva con vida a los mismos tres viajeros norteños y tres orientales acogidos al camino de continuación del nordeste.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o1",
        "ledger": "north-hosted"
      },
      "id": "req-1",
      "entities": [
        "faith-origins.19-hospitality-network-antioch.north-travelers-1",
        "faith-origins.19-hospitality-network-antioch.north-travelers-2",
        "faith-origins.19-hospitality-network-antioch.north-travelers-3"
      ],
      "destinations": {
        "faith-origins.19-hospitality-network-antioch.north-travelers-1": "faith-origins.19-hospitality-network-antioch.destination-5",
        "faith-origins.19-hospitality-network-antioch.north-travelers-2": "faith-origins.19-hospitality-network-antioch.destination-5",
        "faith-origins.19-hospitality-network-antioch.north-travelers-3": "faith-origins.19-hospitality-network-antioch.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o1",
        "ledger": "east-hosted"
      },
      "id": "req-2",
      "entities": [
        "faith-origins.19-hospitality-network-antioch.east-travelers-1",
        "faith-origins.19-hospitality-network-antioch.east-travelers-2",
        "faith-origins.19-hospitality-network-antioch.east-travelers-3"
      ],
      "destinations": {
        "faith-origins.19-hospitality-network-antioch.east-travelers-1": "faith-origins.19-hospitality-network-antioch.destination-5",
        "faith-origins.19-hospitality-network-antioch.east-travelers-2": "faith-origins.19-hospitality-network-antioch.destination-5",
        "faith-origins.19-hospitality-network-antioch.east-travelers-3": "faith-origins.19-hospitality-network-antioch.destination-5"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The six original hosted identities reached the onward road.

ES: Las seis identidades originales acogidas han alcanzado el camino de continuación.

EN: I can wish them well. I cannot invent the rest of their journey as a fact.

ES: Puedo desearles suerte. No puedo inventar como hecho el resto de su viaje.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/19-hospitality-network-antioch.svg)

```json
{
  "bbox": [
    36.14,
    36.18,
    36.205,
    36.245
  ],
  "terrainProfile": "antioch",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        210.56,
        76.18
      ],
      "lonLat": [
        36.175,
        36.235
      ],
      "name": {
        "en": "North road arrival yard",
        "es-ES": "Patio de llegada del camino norte"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        192.87,
        185.8
      ],
      "lonLat": [
        36.171,
        36.215
      ],
      "name": {
        "en": "Western inland hosting court",
        "es-ES": "Patio interior occidental de acogida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        254.78,
        311.86
      ],
      "lonLat": [
        36.185,
        36.192
      ],
      "name": {
        "en": "Southern hosting court",
        "es-ES": "Patio meridional de acogida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        312.26,
        163.87
      ],
      "lonLat": [
        36.198,
        36.219
      ],
      "name": {
        "en": "Eastern arrival court",
        "es-ES": "Patio oriental de llegada"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        307.84,
        54.26
      ],
      "lonLat": [
        36.197,
        36.239
      ],
      "name": {
        "en": "Northeastern onward road",
        "es-ES": "Camino de continuación al nordeste"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-host-road",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-host-road",
      "hubOrder": [
        "hub-4",
        "hub-3",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "hosting-relief",
      "hubOrder": [
        "hub-2",
        "hub-3"
      ],
      "mode": "land",
      "widthTiles": 6,
      "routePolicy": "survey land connection; no river crossing"
    }
  ],
  "terrainInstructions": "Local Antioch districts east of the schematic Orontes city reach, below or north of Silpius slopes as appropriate. No invented crossing, modern Antakya street grid, fourth-century basilica or later fortress. Exact terrain elevation, ancient banks and footprint checks pending. All local activities are fictional; long-distance journeys remain off-map.",
  "mainRouteLengthStraightTiles": 519.94,
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
        36.17,
        36.1
      ],
      [
        36.16,
        36.19
      ],
      [
        36.155,
        36.205
      ],
      [
        36.135,
        36.25
      ],
      [
        36.07,
        36.29
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
  "asset": "docs/design/maps/faith-origins/odyssey/19-hospitality-network-antioch.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.19-hospitality-network-antioch.north-travelers-1",
      "role": "fictional-independent-voluntary-traveler",
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
      "id": "faith-origins.19-hospitality-network-antioch.north-travelers-2",
      "role": "fictional-independent-voluntary-traveler",
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
      "id": "faith-origins.19-hospitality-network-antioch.north-travelers-3",
      "role": "fictional-independent-voluntary-traveler",
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
      "id": "faith-origins.19-hospitality-network-antioch.east-travelers-1",
      "role": "fictional-independent-voluntary-traveler",
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
      "generationPolicy": "preplaced and available",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.19-hospitality-network-antioch.east-travelers-2",
      "role": "fictional-independent-voluntary-traveler",
      "initialHub": "hub-4",
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
      "id": "faith-origins.19-hospitality-network-antioch.east-travelers-3",
      "role": "fictional-independent-voluntary-traveler",
      "initialHub": "hub-4",
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
    }
  ],
  "zones": [
    {
      "id": "faith-origins.19-hospitality-network-antioch.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.19-hospitality-network-antioch.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.19-hospitality-network-antioch.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.19-hospitality-network-antioch.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.19-hospitality-network-antioch.destination-5",
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
    "north-travelers": [
      "faith-origins.19-hospitality-network-antioch.north-travelers-1",
      "faith-origins.19-hospitality-network-antioch.north-travelers-2",
      "faith-origins.19-hospitality-network-antioch.north-travelers-3"
    ],
    "east-travelers": [
      "faith-origins.19-hospitality-network-antioch.east-travelers-1",
      "faith-origins.19-hospitality-network-antioch.east-travelers-2",
      "faith-origins.19-hospitality-network-antioch.east-travelers-3"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.19-hospitality-network-antioch.north-travelers-1",
        "faith-origins.19-hospitality-network-antioch.north-travelers-2",
        "faith-origins.19-hospitality-network-antioch.north-travelers-3"
      ],
      "minimumAliveOrAlreadySafe": 3
    },
    {
      "entities": [
        "faith-origins.19-hospitality-network-antioch.east-travelers-1",
        "faith-origins.19-hospitality-network-antioch.east-travelers-2",
        "faith-origins.19-hospitality-network-antioch.east-travelers-3"
      ],
      "minimumAliveOrAlreadySafe": 3
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Separate settled households / Hogares establecidos separados

EN: Bring each of the two aid crates to its assigned household at separate settled households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares establecidos separados. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Help separate local households; do not force religious conformity.

ES: Ayuda a hogares locales separados sin imponer conformidad religiosa.

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
          "19-hospitality-network-antioch.side-1.entity-1",
          "19-hospitality-network-antioch.side-1.entity-2"
        ],
        "destinations": {
          "19-hospitality-network-antioch.side-1.entity-1": "19-hospitality-network-antioch.side-1.zone-1",
          "19-hospitality-network-antioch.side-1.entity-2": "19-hospitality-network-antioch.side-1.zone-2"
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
        "id": "19-hospitality-network-antioch.side-1.entity-1",
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
        "id": "19-hospitality-network-antioch.side-1.entity-2",
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
        "id": "19-hospitality-network-antioch.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "19-hospitality-network-antioch.side-1.zone-2",
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
      "onceFlag": "19-hospitality-network-antioch.side-1.rewarded",
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

### Workshop shelter / Cobertizo del taller

EN: Pay 50 wood and restore the damaged store of workshop shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de cobertizo del taller. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: A voluntary craft repair offers one finite reserve, not a universal ancient welfare institution.

ES: Una reparación artesanal voluntaria ofrece una reserva finita, no una institución universal de ayuda antigua.

```json
{
  "id": "side-2",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "19-hospitality-network-antioch.side-2.entity-1",
        "health": "full",
        "paymentReceipt": "19-hospitality-network-antioch.side-2.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "19-hospitality-network-antioch.side-2.payment",
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
        "id": "19-hospitality-network-antioch.side-2.entity-1",
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
        "id": "19-hospitality-network-antioch.side-2.zone-1",
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
      "onceFlag": "19-hospitality-network-antioch.side-2.rewarded",
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

### Road grain exchange / Intercambio de grano del camino

EN: Escort the trader of road grain exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de intercambio de grano del camino hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A separate merchant supports provisions without testing a prophet for money.

ES: Un comerciante separado apoya provisiones sin someter a un profeta a una prueba de dinero.

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
          "19-hospitality-network-antioch.side-3.entity-1"
        ],
        "destinations": {
          "19-hospitality-network-antioch.side-3.entity-1": "19-hospitality-network-antioch.side-3.zone-1"
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
        "receipt": "19-hospitality-network-antioch.side-3.payment",
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
        "id": "19-hospitality-network-antioch.side-3.entity-1",
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
        "id": "19-hospitality-network-antioch.side-3.zone-1",
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
      "onceFlag": "19-hospitality-network-antioch.side-3.rewarded",
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

### Independent wayfarers / Caminantes independientes

EN: Bring both voluntary evacuee groups from independent wayfarers to the receiving refuge alive. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida los dos grupos de evacuados voluntarios de caminantes independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez.

EN: Two optional travelers never replace any of the six main guests.

ES: Dos viajeros opcionales nunca sustituyen a los seis huéspedes principales.

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
          "19-hospitality-network-antioch.side-4.entity-1",
          "19-hospitality-network-antioch.side-4.entity-2"
        ],
        "destinations": {
          "19-hospitality-network-antioch.side-4.entity-1": "19-hospitality-network-antioch.side-4.zone-1",
          "19-hospitality-network-antioch.side-4.entity-2": "19-hospitality-network-antioch.side-4.zone-1"
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
        "id": "19-hospitality-network-antioch.side-4.entity-1",
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
        "id": "19-hospitality-network-antioch.side-4.entity-2",
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
        "id": "19-hospitality-network-antioch.side-4.zone-1",
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
      "onceFlag": "19-hospitality-network-antioch.side-4.rewarded",
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

### Hospitality working notes / Notas de trabajo de acogida

EN: Recover both separate copies from hospitality working notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de notas de trabajo de acogida y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Fictional local notes explain the normative source without placing its original manuscript.

ES: Notas locales ficticias explican la fuente normativa sin colocar su manuscrito original.

```json
{
  "id": "side-5",
  "kind": "copy",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "19-hospitality-network-antioch.side-5.entity-1",
          "19-hospitality-network-antioch.side-5.entity-2"
        ],
        "destinations": {
          "19-hospitality-network-antioch.side-5.entity-1": "19-hospitality-network-antioch.side-5.zone-1",
          "19-hospitality-network-antioch.side-5.entity-2": "19-hospitality-network-antioch.side-5.zone-1"
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
        "id": "19-hospitality-network-antioch.side-5.entity-1",
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
        "id": "19-hospitality-network-antioch.side-5.entity-2",
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
        "id": "19-hospitality-network-antioch.side-5.zone-1",
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
      "onceFlag": "19-hospitality-network-antioch.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.19-hospitality-network-antioch"
      ],
      "historicalNote": {
        "en": "The Didache gives rules for receiving itinerants, helping travelers and supporting people who settle and work. These are prescriptions, not a survey of universal practice. Its Syrian provenance and date are proposals; this Antioch hospitality network is fictional.",
        "es-ES": "La Didaché prescribe cómo recibir itinerantes, ayudar a viajeros y apoyar a quienes se establecen y trabajan. Son normas, no un estudio de prácticas universales. Su procedencia siria y fecha son propuestas; esta red de hospitalidad en Antioquía es ficticia."
      },
      "hint": {
        "en": "Bring all three north-road travelers alive to the western hosting court and all three east-road travelers alive to the southern court.",
        "es-ES": "Lleva con vida a los tres viajeros del camino norte al patio occidental de acogida y a los tres del camino oriental al patio meridional."
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

### Onward road guide / Guía del camino de continuación

EN: Escort the local guide of onward road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.

ES: Escolta al guía local de guía del camino de continuación hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga.

EN: Discloses a surveyed land detour for departure.

ES: Señala un desvío terrestre comprobado para la salida.

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
          "19-hospitality-network-antioch.side-6.entity-1"
        ],
        "destinations": {
          "19-hospitality-network-antioch.side-6.entity-1": "19-hospitality-network-antioch.side-6.zone-1"
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
        "id": "19-hospitality-network-antioch.side-6.entity-1",
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
        "id": "19-hospitality-network-antioch.side-6.zone-1",
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
      "onceFlag": "19-hospitality-network-antioch.side-6.rewarded",
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
      "id": "hosting-investment",
      "optionalObjectives": [
        "side-1",
        "side-2"
      ],
      "costOfOpportunity": "Reserve240mainfood, then support households and repair while both traveler groups stage.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "transport-and-grain",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "A separate logistics team handles bounded trade and optional travelers without substituting main guests.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "context-and-road",
      "optionalObjectives": [
        "side-5",
        "side-6"
      ],
      "costOfOpportunity": "Read normative context and survey the final road; no artificial third-day death countdown.",
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
    "difficultyLevers": "12 workers; all main origins and receivers disclosed, separate labels and route markers.",
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
    "difficultyLevers": "9 workers; split collection, gathering and dispatch teams under local fog.",
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
    "difficultyLevers": "6 workers, lower finite starting stock; parallel teams and optional opportunity costs. No hidden recipient, forced secret deadline or invented army.",
    "movementPolicy": "native movement/health/damage unchanged; no difficulty cheats",
    "mainFeasibleSkippingAllOptionals": true,
    "allOptionalCostsAffordable": true
  }
}
```

## All player-facing screens

| Key / condition | Speaker | English | Español |
| --- | --- | --- | --- |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.title / always | none | The House Before the Road | La casa antes del camino |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.fact-intro / intro first | collection-narrator | The Didache gives rules for receiving itinerants, helping travelers and supporting people who settle and work. These are prescriptions, not a survey of universal practice. Its Syrian provenance and date are proposals; this Antioch hospitality network is fictional. | La Didaché prescribe cómo recibir itinerantes, ayudar a viajeros y apoyar a quienes se establecen y trabajan. Son normas, no un estudio de prácticas universales. Su procedencia siria y fecha son propuestas; esta red de hospitalidad en Antioquía es ficticia. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.persona-intro / after handover | miriam-archive | An archive can tell me what someone wanted a household to do. It cannot show me every door that opened. I remember my own threshold, and keep that memory apart from these older rules. | Un archivo puede decirme qué quería alguien que hiciera un hogar. No muestra todas las puertas que se abrieron. Recuerdo mi propio umbral y conservo ese recuerdo separado de estas normas anteriores. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.route-help / available from start; repeatable without effect | none | This is a local Antioch scene, not proof of where a text was composed. Keep the proposed routes on the city-side land bank; no required river crossing. | Es una escena local de Antioquía, no una prueba del lugar donde se compuso un texto. Mantén las rutas propuestas en tierra del lado urbano; no es necesario cruzar el río. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.o1-goal / phase-1 active | none | Bring all three north-road travelers alive to the western hosting court and all three east-road travelers alive to the southern court. | Lleva con vida a los tres viajeros del camino norte al patio occidental de acogida y a los tres del camino oriental al patio meridional. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.o1-receipt / o1 latched once | none | Six distinct travelers arrived at their assigned hosts. | Seis viajeros distintos han llegado a sus anfitriones asignados. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.o1-reaction / after o1 receipt | miriam-archive | They are fictional guests, not prophets whose truth a game can judge. | Son huéspedes ficticios, no profetas cuya verdad pueda juzgar un juego. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.o2-goal / phase-2 active | none | Pay 120 food at each hosting court once: 240 food in total. | Paga una sola vez 120 de alimento en cada patio de acogida: 240 en total. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.o2-receipt / o2 latched once | none | Both hosting shares are paid with one conserved transaction. | Ambas partes de acogida están pagadas mediante una transacción conservada. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.o2-reaction / after o2 receipt | miriam-archive | The rule speaks in a voice from its time; our food account measures only this imagined help. | La norma habla con una voz de su tiempo; nuestra cuenta de alimento solo mide esta ayuda imaginada. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.o3-goal / phase-3 active | none | Take the same three northern and same three eastern hosted travelers alive to the northeastern onward road. | Lleva con vida a los mismos tres viajeros norteños y tres orientales acogidos al camino de continuación del nordeste. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.o3-receipt / o3 latched once | none | The six original hosted identities reached the onward road. | Las seis identidades originales acogidas han alcanzado el camino de continuación. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.o3-reaction / after o3 receipt | miriam-archive | I can wish them well. I cannot invent the rest of their journey as a fact. | Puedo desearles suerte. No puedo inventar como hecho el resto de su viaje. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-1-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at separate settled households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares establecidos separados. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-1-complete / side-1 completed | none | Separate settled households completed. Its stated benefit has been granted once. | Hogares establecidos separados: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-1-lost / side-1 failed-optional | none | Separate settled households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares establecidos separados: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-2-goal / optional list from start | none | Pay 50 wood and restore the damaged store of workshop shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de cobertizo del taller. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-2-complete / side-2 completed | none | Workshop shelter completed. Its stated benefit has been granted once. | Cobertizo del taller: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-2-lost / side-2 failed-optional | none | Workshop shelter is unavailable after the loss of its unique participant or object. The main mission continues. | Cobertizo del taller: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-3-goal / optional list from start | none | Escort the trader of road grain exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de intercambio de grano del camino hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-3-complete / side-3 completed | none | Road grain exchange completed. Its stated benefit has been granted once. | Intercambio de grano del camino: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-3-lost / side-3 failed-optional | none | Road grain exchange is unavailable after the loss of its unique participant or object. The main mission continues. | Intercambio de grano del camino: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-4-goal / optional list from start | none | Bring both voluntary evacuee groups from independent wayfarers to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de caminantes independientes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-4-complete / side-4 completed | none | Independent wayfarers completed. Its stated benefit has been granted once. | Caminantes independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-4-lost / side-4 failed-optional | none | Independent wayfarers is unavailable after the loss of its unique participant or object. The main mission continues. | Caminantes independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-5-goal / optional list from start | none | Recover both separate copies from hospitality working notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de notas de trabajo de acogida y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-5-complete / side-5 completed | none | Hospitality working notes completed. Its stated benefit has been granted once. | Notas de trabajo de acogida: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-5-lost / side-5 failed-optional | none | Hospitality working notes is unavailable after the loss of its unique participant or object. The main mission continues. | Notas de trabajo de acogida: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-6-goal / optional list from start | none | Escort the local guide of onward road guide to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de guía del camino de continuación hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-6-complete / side-6 completed | none | Onward road guide completed. Its stated benefit has been granted once. | Guía del camino de continuación: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.side-6-lost / side-6 failed-optional | none | Onward road guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del camino de continuación: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.fact-outro / victory first | collection-narrator | Six fictional travelers received bounded help and continued along a local road. This does not demonstrate that every community followed the Didache, identify a prophet, or settle the document’s composition history. | Seis viajeros ficticios recibieron ayuda limitada y siguieron por un camino local. Esto no demuestra que todas las comunidades siguieran la Didaché, identifica a un profeta ni resuelve la historia de composición del documento. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.persona-outro / after fact-outro | miriam-archive | Bread offered on the road is a small action. I can value it without pretending that these six invented arrivals explain every community I have read about. | El pan ofrecido en el camino es un gesto pequeño. Puedo valorarlo sin fingir que estas seis llegadas inventadas explican todas las comunidades que he leído. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.19-hospitality-network-antioch.odyssey.next-episode / after persona-outro | none | Continue with A Letter Across the Divide. This episode does not complete the campaign. | Continúa con Una carta sobre la división. Este episodio no termina la campaña. |

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
      "same six hosted IDs must leave",
      "three arrivals atonehost cannot satisfy both courts",
      "optional traveler cannot replace main guest",
      "120foodeach not240atonehost",
      "no universal Didache practice claim",
      "all main paths stay on one landbank",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
