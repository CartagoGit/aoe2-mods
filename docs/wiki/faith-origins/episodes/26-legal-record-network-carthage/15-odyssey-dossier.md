# 26. The Advocate's Harbour

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `26-legal-record-network-carthage` · c. 197 CE · 400×400

## Historical frame and fixed outcome

EN: Tertullian’s Apology protests condemnation without proper inquiry and describes Christian assembly, voluntary contributions and care. These are arguments and self-descriptions in a defense of Christians, not neutral legal registers. The conventional date is around 197. Our local dispatch network is fictional and grants no pardon.

ES: La Apología de Tertuliano protesta contra condenas sin una investigación adecuada y describe asambleas cristianas, contribuciones voluntarias y asistencia. Son argumentos y descripciones propias de una defensa de los cristianos, no registros jurídicos neutrales. La fecha convencional es hacia 197. La red local de despachos es ficticia y no concede indultos.

EN: Three fictional local notices and their three assigned couriers completed the network and returned after reception. No Roman sentence, Christian legal status or universal practice was changed. The Apology remains an attributed defense rather than proof that its appeal succeeded.

ES: Tres avisos locales ficticios y sus tres correos asignados completaron la red y volvieron después de la recepción. No se cambió una sentencia romana, la situación jurídica cristiana ni una práctica universal. La Apología sigue siendo una defensa atribuida, no prueba del éxito de su llamamiento.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 19,
      "episodeId": "26-legal-record-network-carthage",
      "order": 26,
      "selectedSourceUrl": "https://tertullian.org/works/apologeticum.htm",
      "consultedUrl": "https://www.tertullian.org/works/apologeticum.htm",
      "passage": "Tertullian, Apologeticum prologue §§1–3 on uninvestigated condemnation; ch.39 on Christian assembly/charity and chs.40–42 on social practice.",
      "supportedClaim": {
        "en": "Tertullian protests condemnation without inquiry and describes communal worship and care practices.",
        "es-ES": "Tertuliano protesta contra condenas sin investigación y describe culto comunitario y prácticas de asistencia."
      },
      "limitations": "The Apology is forensic rhetoric and advocacy, not a neutral legal register. The selection's c.197 date is conventional; ch.39 does not prove specific locations or every practice across Christians.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/0301.htm",
      "passage": "Apology1–2, architect read defense and legal inquiry argument",
      "limitations": "Subsequent direct retrieval timed out/HTTP403; do not claim full page or ch3/40–42 read by architect. For ch39 see separate complete chapter consultation.",
      "consultationDate": "2026-10-13",
      "status": "architect read specified passages; independent approval pending"
    },
    {
      "consultedUrl": "https://logoslibrary.org/tertullian/apology/39.html",
      "passage": "Apology39, complete displayed chapter in S.Thelwall translation",
      "limitations": "Advocacy and self-description, voluntary contribution/aid themes; no exact197local address, universal practice or authentic local legal register.",
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

EN: Collect all three local work notes and deliver them to the western coordination yard.

ES: Recoge las tres notas locales y entrégalas en el patio occidental de coordinación.

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
        "faith-origins.26-legal-record-network-carthage.local-work-notes-1",
        "faith-origins.26-legal-record-network-carthage.local-work-notes-2",
        "faith-origins.26-legal-record-network-carthage.local-work-notes-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.26-legal-record-network-carthage.local-work-notes-1",
        "faith-origins.26-legal-record-network-carthage.local-work-notes-2",
        "faith-origins.26-legal-record-network-carthage.local-work-notes-3"
      ],
      "destinations": {
        "faith-origins.26-legal-record-network-carthage.local-work-notes-1": "faith-origins.26-legal-record-network-carthage.destination-2",
        "faith-origins.26-legal-record-network-carthage.local-work-notes-2": "faith-origins.26-legal-record-network-carthage.destination-2",
        "faith-origins.26-legal-record-network-carthage.local-work-notes-3": "faith-origins.26-legal-record-network-carthage.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The three original local inputs are received.

ES: Se han recibido las tres entradas locales originales.

EN: These are local work notes, not Tertullian’s own pages.

ES: Son notas locales de trabajo, no páginas del propio Tertuliano.

### o2 / phase-2

EN: Pay 90 wood and 30 gold once at the western yard and create three separately labelled notices.

ES: Paga una vez 90 de madera y 30 de oro en el patio occidental y crea tres avisos etiquetados por separado.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 90,
        "gold": 30
      },
      "id": "req-1",
      "receivingZones": [
        "faith-origins.26-legal-record-network-carthage.destination-2"
      ],
      "allocations": {
        "faith-origins.26-legal-record-network-carthage.destination-2": {
          "wood": 90,
          "gold": 30
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.26-legal-record-network-carthage.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "faith-origins.26-legal-record-network-carthage.local-work-notes-1",
        "faith-origins.26-legal-record-network-carthage.local-work-notes-2",
        "faith-origins.26-legal-record-network-carthage.local-work-notes-3"
      ],
      "outputEntities": [
        "faith-origins.26-legal-record-network-carthage.labelled-notices-1",
        "faith-origins.26-legal-record-network-carthage.labelled-notices-2",
        "faith-origins.26-legal-record-network-carthage.labelled-notices-3"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "faith-origins.26-legal-record-network-carthage.o2.req-1.paid",
          "fromObjective": "o2",
          "amounts": {
            "wood": 90,
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

EN: One funded preparation produced three unique local notices.

ES: Una preparación financiada produjo tres avisos locales únicos.

EN: Three copies do not turn a defense into three independent sources.

ES: Tres copias no convierten una defensa en tres fuentes independientes.

### o3 / phase-3

EN: Deliver one assigned notice and one assigned courier alive to each of the original, northern and eastern courts.

ES: Entrega un aviso asignado y un correo asignado con vida en cada patio original, septentrional y oriental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "state": "arrived",
      "requiredCount": 3,
      "id": "req-1",
      "entities": [
        "faith-origins.26-legal-record-network-carthage.labelled-notices-1",
        "faith-origins.26-legal-record-network-carthage.labelled-notices-2",
        "faith-origins.26-legal-record-network-carthage.labelled-notices-3"
      ],
      "destinations": {
        "faith-origins.26-legal-record-network-carthage.labelled-notices-1": "faith-origins.26-legal-record-network-carthage.destination-1",
        "faith-origins.26-legal-record-network-carthage.labelled-notices-2": "faith-origins.26-legal-record-network-carthage.destination-3",
        "faith-origins.26-legal-record-network-carthage.labelled-notices-3": "faith-origins.26-legal-record-network-carthage.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "state": "arrived",
      "requiredCount": 3,
      "id": "req-2",
      "entities": [
        "faith-origins.26-legal-record-network-carthage.network-couriers-1",
        "faith-origins.26-legal-record-network-carthage.network-couriers-2",
        "faith-origins.26-legal-record-network-carthage.network-couriers-3"
      ],
      "destinations": {
        "faith-origins.26-legal-record-network-carthage.network-couriers-1": "faith-origins.26-legal-record-network-carthage.destination-1",
        "faith-origins.26-legal-record-network-carthage.network-couriers-2": "faith-origins.26-legal-record-network-carthage.destination-3",
        "faith-origins.26-legal-record-network-carthage.network-couriers-3": "faith-origins.26-legal-record-network-carthage.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All three distinct notice/courier destinations are received.

ES: Se han recibido los tres destinos distintos de avisos y correos.

EN: I count the three receiving desks separately. I cannot count three legal victories.

ES: Cuento por separado las tres mesas receptoras. No puedo contar tres victorias jurídicas.

### o4 / phase-4

EN: After all reception receipts, depart with the same three couriers and return all three alive to the western coordination yard.

ES: Tras todos los recibos de recepción, parte con los mismos tres correos y devuelve los tres con vida al patio occidental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "ordered-departure",
      "departureEnabledOnlyAfterReceipt": true,
      "receiptObjective": "o3",
      "receiptRequirement": "req-2",
      "id": "req-1",
      "departingEntities": [
        "faith-origins.26-legal-record-network-carthage.network-couriers-1",
        "faith-origins.26-legal-record-network-carthage.network-couriers-2",
        "faith-origins.26-legal-record-network-carthage.network-couriers-3"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-1"
      },
      "id": "req-2",
      "entities": [
        "faith-origins.26-legal-record-network-carthage.network-couriers-1",
        "faith-origins.26-legal-record-network-carthage.network-couriers-2",
        "faith-origins.26-legal-record-network-carthage.network-couriers-3"
      ],
      "destinations": {
        "faith-origins.26-legal-record-network-carthage.network-couriers-1": "faith-origins.26-legal-record-network-carthage.destination-2",
        "faith-origins.26-legal-record-network-carthage.network-couriers-2": "faith-origins.26-legal-record-network-carthage.destination-2",
        "faith-origins.26-legal-record-network-carthage.network-couriers-3": "faith-origins.26-legal-record-network-carthage.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All three original couriers returned after their recorded reception-backed departure.

ES: Los tres correos originales volvieron tras su partida registrada después de la recepción.

EN: An observed return belongs to our game; an unproved audience must remain outside it.

ES: Una vuelta observada pertenece al juego; una audiencia no acreditada debe seguir fuera de él.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/26-legal-record-network-carthage.svg)

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
        238.1,
        310.83
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
        107.47,
        236.61
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
        208.41,
        88.17
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
        297.47,
        199.5
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
    "north-road": 329.75,
    "east-road": 343.83,
    "relief": 268.74
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
  "asset": "docs/design/maps/faith-origins/odyssey/26-legal-record-network-carthage.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.26-legal-record-network-carthage.local-work-notes-1",
      "role": "fictional-local-procedure-note",
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
      "id": "faith-origins.26-legal-record-network-carthage.local-work-notes-2",
      "role": "fictional-local-procedure-note",
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
      "id": "faith-origins.26-legal-record-network-carthage.local-work-notes-3",
      "role": "fictional-local-procedure-note",
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
      "id": "faith-origins.26-legal-record-network-carthage.labelled-notices-1",
      "role": "fictional-local-circulation-notice",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.26-legal-record-network-carthage.labelled-notices-2",
      "role": "fictional-local-circulation-notice",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    },
    {
      "id": "faith-origins.26-legal-record-network-carthage.labelled-notices-3",
      "role": "fictional-local-circulation-notice",
      "initialHub": "hub-2",
      "offsetTiles": [
        -6,
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
      "id": "faith-origins.26-legal-record-network-carthage.network-couriers-1",
      "role": "fictional-voluntary-courier",
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
      "id": "faith-origins.26-legal-record-network-carthage.network-couriers-2",
      "role": "fictional-voluntary-courier",
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
      "id": "faith-origins.26-legal-record-network-carthage.network-couriers-3",
      "role": "fictional-voluntary-courier",
      "initialHub": "hub-2",
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
      "id": "faith-origins.26-legal-record-network-carthage.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.26-legal-record-network-carthage.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.26-legal-record-network-carthage.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.26-legal-record-network-carthage.destination-4",
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
    "local-work-notes": [
      "faith-origins.26-legal-record-network-carthage.local-work-notes-1",
      "faith-origins.26-legal-record-network-carthage.local-work-notes-2",
      "faith-origins.26-legal-record-network-carthage.local-work-notes-3"
    ],
    "labelled-notices": [
      "faith-origins.26-legal-record-network-carthage.labelled-notices-1",
      "faith-origins.26-legal-record-network-carthage.labelled-notices-2",
      "faith-origins.26-legal-record-network-carthage.labelled-notices-3"
    ],
    "network-couriers": [
      "faith-origins.26-legal-record-network-carthage.network-couriers-1",
      "faith-origins.26-legal-record-network-carthage.network-couriers-2",
      "faith-origins.26-legal-record-network-carthage.network-couriers-3"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.26-legal-record-network-carthage.network-couriers-1",
        "faith-origins.26-legal-record-network-carthage.network-couriers-2",
        "faith-origins.26-legal-record-network-carthage.network-couriers-3"
      ],
      "minimumAliveOrAlreadySafe": 3
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### The defense’s argument margin / El margen argumental de la defensa

EN: Recover both separate copies from the defense’s argument margin and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de el margen argumental de la defensa y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Source context attributes advocacy without manufacturing an acquittal.

ES: El contexto atribuye la defensa sin fabricar una absolución.

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
          "26-legal-record-network-carthage.side-1.entity-1",
          "26-legal-record-network-carthage.side-1.entity-2"
        ],
        "destinations": {
          "26-legal-record-network-carthage.side-1.entity-1": "26-legal-record-network-carthage.side-1.zone-1",
          "26-legal-record-network-carthage.side-1.entity-2": "26-legal-record-network-carthage.side-1.zone-1"
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
        "id": "26-legal-record-network-carthage.side-1.entity-1",
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
        "id": "26-legal-record-network-carthage.side-1.entity-2",
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
        "id": "26-legal-record-network-carthage.side-1.zone-1",
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
      "onceFlag": "26-legal-record-network-carthage.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.26-legal-record-network-carthage"
      ],
      "historicalNote": {
        "en": "Tertullian’s Apology protests condemnation without proper inquiry and describes Christian assembly, voluntary contributions and care. These are arguments and self-descriptions in a defense of Christians, not neutral legal registers. The conventional date is around 197. Our local dispatch network is fictional and grants no pardon.",
        "es-ES": "La Apología de Tertuliano protesta contra condenas sin una investigación adecuada y describe asambleas cristianas, contribuciones voluntarias y asistencia. Son argumentos y descripciones propias de una defensa de los cristianos, no registros jurídicos neutrales. La fecha convencional es hacia 197. La red local de despachos es ficticia y no concede indultos."
      },
      "hint": {
        "en": "Collect all three local work notes and deliver them to the western coordination yard.",
        "es-ES": "Recoge las tres notas locales y entrégalas en el patio occidental de coordinación."
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

### Voluntary neighbors’ provisions / Provisiones voluntarias de vecinos

EN: Bring each of the two aid crates to its assigned household at voluntary neighbors’ provisions. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en provisiones voluntarias de vecinos. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Independent household aid does not require conversion or doctrinal agreement.

ES: La ayuda a hogares independientes no exige conversión ni acuerdo doctrinal.

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
          "26-legal-record-network-carthage.side-2.entity-1",
          "26-legal-record-network-carthage.side-2.entity-2"
        ],
        "destinations": {
          "26-legal-record-network-carthage.side-2.entity-1": "26-legal-record-network-carthage.side-2.zone-1",
          "26-legal-record-network-carthage.side-2.entity-2": "26-legal-record-network-carthage.side-2.zone-2"
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
        "id": "26-legal-record-network-carthage.side-2.entity-1",
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
        "id": "26-legal-record-network-carthage.side-2.entity-2",
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
        "id": "26-legal-record-network-carthage.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "26-legal-record-network-carthage.side-2.zone-2",
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
      "onceFlag": "26-legal-record-network-carthage.side-2.rewarded",
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

### The inland work share / La aportación interior de trabajo

EN: Escort the trader of the inland work share to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de la aportación interior de trabajo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Bounded voluntary trade supports supply planning, not a purchased verdict.

ES: El comercio voluntario limitado apoya las provisiones, no compra un veredicto.

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
          "26-legal-record-network-carthage.side-3.entity-1"
        ],
        "destinations": {
          "26-legal-record-network-carthage.side-3.entity-1": "26-legal-record-network-carthage.side-3.zone-1"
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
        "receipt": "26-legal-record-network-carthage.side-3.payment",
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
        "id": "26-legal-record-network-carthage.side-3.entity-1",
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
        "id": "26-legal-record-network-carthage.side-3.zone-1",
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
      "onceFlag": "26-legal-record-network-carthage.side-3.rewarded",
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

### The north-road work shed / El cobertizo del camino norte

EN: Pay 50 wood and restore the damaged store of the north-road work shed to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el cobertizo del camino norte. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Repair ordinary finite storage, not an attested church or tribunal.

ES: Repara un almacén ordinario finito, no una iglesia ni tribunal acreditados.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "26-legal-record-network-carthage.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "26-legal-record-network-carthage.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "26-legal-record-network-carthage.side-4.payment",
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
        "id": "26-legal-record-network-carthage.side-4.entity-1",
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
        "id": "26-legal-record-network-carthage.side-4.zone-1",
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
      "onceFlag": "26-legal-record-network-carthage.side-4.rewarded",
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

### Northern dispatch viewpoints / Miradores del despacho septentrional

EN: Scout both marked viewpoints of northern dispatch viewpoints. Benefit: Mark the surveyed north-road inland circuit once; main receivers remain disclosed without it.

ES: Explora los dos miradores señalados de miradores del despacho septentrional. Ventaja: Señala una vez el circuito interior trazado north-road; los receptores principales siguen identificados sin él.

EN: Observe actual northern inland travel without uncovering a secret imperial reply.

ES: Observa el viaje interior septentrional real sin descubrir una respuesta imperial secreta.

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
          "26-legal-record-network-carthage.side-5.zone-1",
          "26-legal-record-network-carthage.side-5.zone-2"
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
        "id": "26-legal-record-network-carthage.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "26-legal-record-network-carthage.side-5.zone-2",
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
      "target": "north-road surveyed inland circuit",
      "resources": {},
      "onceFlag": "26-legal-record-network-carthage.side-5.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "north-road"
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

### The outer dispatch guide / El guía exterior de despachos

EN: Escort the local guide of the outer dispatch guide to the marked road junction. Benefit: Mark the surveyed relief inland circuit once; main receivers remain disclosed without it.

ES: Escolta al guía local de el guía exterior de despachos hasta el cruce señalado. Ventaja: Señala una vez el circuito interior trazado relief; los receptores principales siguen identificados sin él.

EN: Mark the outer inland circuit; cannot replace reception-backed courier departure.

ES: Señala el circuito exterior interior; no sustituye la partida de correos posterior a la recepción.

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
          "26-legal-record-network-carthage.side-6.entity-1"
        ],
        "destinations": {
          "26-legal-record-network-carthage.side-6.entity-1": "26-legal-record-network-carthage.side-6.zone-1"
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
        "id": "26-legal-record-network-carthage.side-6.entity-1",
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
        "id": "26-legal-record-network-carthage.side-6.zone-1",
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
      "onceFlag": "26-legal-record-network-carthage.side-6.rewarded",
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
      "id": "three-courier-dispatch",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Split three destination teams and supply investment, then stage causal returns; main 90 wood 30 goldreserved.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "source-and-north-survey",
      "optionalObjectives": [
        "side-1",
        "side-5"
      ],
      "costOfOpportunity": "Read defense context while surveying northern access; public persuasion is not a hidden game meter.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "care-and-outer-return",
      "optionalObjectives": [
        "side-2",
        "side-6"
      ],
      "costOfOpportunity": "Combine independent aid with outer courier return planning; no optional supplies are mandatory.",
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
      "wood": 798,
      "gold": 234,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 90,
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
      "wood": 770,
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
      "wood": 820,
      "gold": 245,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 90,
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
      "wood": 770,
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
      "wood": 843,
      "gold": 257,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 90,
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
      "wood": 770,
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
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.title / always | none | The Advocate's Harbour | El puerto del defensor |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.fact-intro / intro first | collection-narrator | Tertullian’s Apology protests condemnation without proper inquiry and describes Christian assembly, voluntary contributions and care. These are arguments and self-descriptions in a defense of Christians, not neutral legal registers. The conventional date is around 197. Our local dispatch network is fictional and grants no pardon. | La Apología de Tertuliano protesta contra condenas sin una investigación adecuada y describe asambleas cristianas, contribuciones voluntarias y asistencia. Son argumentos y descripciones propias de una defensa de los cristianos, no registros jurídicos neutrales. La fecha convencional es hacia 197. La red local de despachos es ficticia y no concede indultos. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.persona-intro / after handover | miriam-archive | There is force in this voice that I do not find in my own. I admire its refusal to remain unheard; I also notice how readily a defense speaks as though every neighbor were its enemy. I want to keep that tension visible. | Hay en esta voz una fuerza que no encuentro en la mía. Admiro su negativa a quedarse sin ser oída; también advierto lo fácilmente que una defensa habla como si cada vecino fuera enemigo. Quiero dejar visible esa tensión. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.route-help / available from start; repeatable without effect | none | Bring three ordinary local work notes to the western yard, pay 90 wood and 30 gold once, then create three labelled notices. Deliver one notice and one assigned courier to each of the original court, northern court and eastern court. After all receptions, record the same three couriers’ departure and return all three alive to the western yard. | Lleva tres notas ordinarias locales al patio occidental, paga una vez 90 de madera y 30 de oro y crea tres avisos etiquetados. Entrega un aviso y un correo asignado en cada patio original, septentrional y oriental. Tras todas las recepciones registra la partida de los mismos tres correos y devuélvelos con vida al patio occidental. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o1-goal / phase-1 active | none | Collect all three local work notes and deliver them to the western coordination yard. | Recoge las tres notas locales y entrégalas en el patio occidental de coordinación. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o1-receipt / o1 latched once | none | The three original local inputs are received. | Se han recibido las tres entradas locales originales. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o1-reaction / after o1 receipt | miriam-archive | These are local work notes, not Tertullian’s own pages. | Son notas locales de trabajo, no páginas del propio Tertuliano. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o2-goal / phase-2 active | none | Pay 90 wood and 30 gold once at the western yard and create three separately labelled notices. | Paga una vez 90 de madera y 30 de oro en el patio occidental y crea tres avisos etiquetados por separado. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o2-receipt / o2 latched once | none | One funded preparation produced three unique local notices. | Una preparación financiada produjo tres avisos locales únicos. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o2-reaction / after o2 receipt | miriam-archive | Three copies do not turn a defense into three independent sources. | Tres copias no convierten una defensa en tres fuentes independientes. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o3-goal / phase-3 active | none | Deliver one assigned notice and one assigned courier alive to each of the original, northern and eastern courts. | Entrega un aviso asignado y un correo asignado con vida en cada patio original, septentrional y oriental. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o3-receipt / o3 latched once | none | All three distinct notice/courier destinations are received. | Se han recibido los tres destinos distintos de avisos y correos. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o3-reaction / after o3 receipt | miriam-archive | I count the three receiving desks separately. I cannot count three legal victories. | Cuento por separado las tres mesas receptoras. No puedo contar tres victorias jurídicas. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o4-goal / phase-4 active | none | After all reception receipts, depart with the same three couriers and return all three alive to the western coordination yard. | Tras todos los recibos de recepción, parte con los mismos tres correos y devuelve los tres con vida al patio occidental. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o4-receipt / o4 latched once | none | All three original couriers returned after their recorded reception-backed departure. | Los tres correos originales volvieron tras su partida registrada después de la recepción. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.o4-reaction / after o4 receipt | miriam-archive | An observed return belongs to our game; an unproved audience must remain outside it. | Una vuelta observada pertenece al juego; una audiencia no acreditada debe seguir fuera de él. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from the defense’s argument margin and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de el margen argumental de la defensa y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-1-complete / side-1 completed | none | The defense’s argument margin completed. Its stated benefit has been granted once. | El margen argumental de la defensa: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-1-lost / side-1 failed-optional | none | The defense’s argument margin is unavailable after the loss of its unique participant or object. The main mission continues. | El margen argumental de la defensa: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at voluntary neighbors’ provisions. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en provisiones voluntarias de vecinos. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-2-complete / side-2 completed | none | Voluntary neighbors’ provisions completed. Its stated benefit has been granted once. | Provisiones voluntarias de vecinos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-2-lost / side-2 failed-optional | none | Voluntary neighbors’ provisions is unavailable after the loss of its unique participant or object. The main mission continues. | Provisiones voluntarias de vecinos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-3-goal / optional list from start | none | Escort the trader of the inland work share to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de la aportación interior de trabajo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-3-complete / side-3 completed | none | The inland work share completed. Its stated benefit has been granted once. | La aportación interior de trabajo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-3-lost / side-3 failed-optional | none | The inland work share is unavailable after the loss of its unique participant or object. The main mission continues. | La aportación interior de trabajo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the north-road work shed to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el cobertizo del camino norte. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-4-complete / side-4 completed | none | The north-road work shed completed. Its stated benefit has been granted once. | El cobertizo del camino norte: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-4-lost / side-4 failed-optional | none | The north-road work shed is unavailable after the loss of its unique participant or object. The main mission continues. | El cobertizo del camino norte: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of northern dispatch viewpoints. Benefit: Mark the surveyed north-road inland circuit once; main receivers remain disclosed without it. | Explora los dos miradores señalados de miradores del despacho septentrional. Ventaja: Señala una vez el circuito interior trazado north-road; los receptores principales siguen identificados sin él. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-5-complete / side-5 completed | none | Northern dispatch viewpoints completed. Its stated benefit has been granted once. | Miradores del despacho septentrional: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-5-lost / side-5 failed-optional | none | Northern dispatch viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores del despacho septentrional: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-6-goal / optional list from start | none | Escort the local guide of the outer dispatch guide to the marked road junction. Benefit: Mark the surveyed relief inland circuit once; main receivers remain disclosed without it. | Escolta al guía local de el guía exterior de despachos hasta el cruce señalado. Ventaja: Señala una vez el circuito interior trazado relief; los receptores principales siguen identificados sin él. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-6-complete / side-6 completed | none | The outer dispatch guide completed. Its stated benefit has been granted once. | El guía exterior de despachos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.side-6-lost / side-6 failed-optional | none | The outer dispatch guide is unavailable after the loss of its unique participant or object. The main mission continues. | El guía exterior de despachos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.fact-outro / victory first | collection-narrator | Three fictional local notices and their three assigned couriers completed the network and returned after reception. No Roman sentence, Christian legal status or universal practice was changed. The Apology remains an attributed defense rather than proof that its appeal succeeded. | Tres avisos locales ficticios y sus tres correos asignados completaron la red y volvieron después de la recepción. No se cambió una sentencia romana, la situación jurídica cristiana ni una práctica universal. La Apología sigue siendo una defensa atribuida, no prueba del éxito de su llamamiento. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.persona-outro / after fact-outro | miriam-archive | Our three messengers came back. The writer’s hoped-for hearing did not arrive with them. I can admire his insistence without supplying the answer history has not put in my hands. | Volvieron nuestros tres mensajeros. Con ellos no llegó la audiencia que esperaba el autor. Puedo admirar su insistencia sin añadir la respuesta que la historia no ha puesto en mis manos. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.26-legal-record-network-carthage.odyssey.next-episode / after persona-outro | none | Continue with What the Record Cannot Hold. This episode does not complete the campaign. | Continúa con Lo que el registro no puede guardar. Este episodio no termina la campaña. |

## Production, recovery and verification

```json
{
  "stateMachine": {
    "states": [
      "briefing",
      "phase-1",
      "phase-2",
      "phase-3",
      "phase-4",
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
        "to": "phase-4",
        "on": "objective-latched",
        "objectiveId": "o3"
      },
      {
        "from": "phase-4",
        "to": "victory",
        "on": "objective-latched",
        "objectiveId": "o4"
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
    },
    {
      "id": "receipt-gated-ordered-departure",
      "status": "reference implemented; native physical departure/arrival observers and footprints pending"
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
      "Each of the three local notice identities has its own assigned receiving court.",
      "The three original couriers must reach their own receiving courts before the dispatch receipt.",
      "A prior visit to the western yard cannot count as return: require departure in phase 4 after receipt, then the same courier’s new arrival.",
      "Notice creation requires collected inputs and the exact active payment receipt.",
      "No imperial reply, acquittal, universal practice or legal exemption is inferred.",
      "All six optionals are feasible separately or together; main victory never needs their rewards.",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
