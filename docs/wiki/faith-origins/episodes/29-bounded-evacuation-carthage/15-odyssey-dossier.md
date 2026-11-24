# 29. A Harbour Under Orders

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C00 · `29-bounded-evacuation-carthage` · 257–258 CE · 400×400

## Historical frame and fixed outcome

EN: Cyprian’s letter to Successus reports Valerian’s measures and executions at Rome. His own death is narrated separately by Pontius, who describes arrest, sentence and execution at Carthage in a Christian commemorative frame. The 257–258 sequence uses multiple sources. A fictional local household withdrawal cannot rescue Cyprian or halt the measures.

ES: La carta de Cipriano a Successus informa de medidas de Valeriano y ejecuciones en Roma. Su muerte se narra por separado en Poncio, quien describe arresto, sentencia y ejecución en Cartago desde una memoria cristiana. La secuencia 257–258 usa varias fuentes. Una retirada local ficticia de hogares no rescata a Cipriano ni detiene las medidas.

EN: At least eight actual staged fictional household identities and four original property chests reached an inland receiving court. This establishes no historically attested evacuation permit, repeal or rescue of Cyprian. Pontius’ reported execution and theological interpretation remain distinguished.

ES: Al menos ocho identidades de hogares ficticios realmente preparados y cuatro cofres originales llegaron a un patio receptor interior. Esto no acredita un permiso histórico de evacuación, una revocación ni un rescate de Cipriano. La ejecución relatada por Poncio y su interpretación teológica permanecen diferenciadas.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "event": 22,
      "episodeId": "29-bounded-evacuation-carthage",
      "order": 29,
      "selectedSourceUrl": "https://www.newadvent.org/fathers/050602.htm",
      "consultedUrl": "https://www.newadvent.org/fathers/050681.htm",
      "passage": "Cyprian, Epistle 81 §§1–2 (New Advent numbering; also catalogued as Epistle 80): report of Valerian's rescript and executions at Rome; for Cyprian's own arrest/sentence/death consult Pontius, Life and Passion §§15–18, https://www.newadvent.org/fathers/0505.htm.",
      "supportedClaim": {
        "en": "Cyprian reports Valerian's anti-clerical order and Roman executions; Pontius narrates Cyprian's arrest, sentence, and execution at Carthage.",
        "es-ES": "Cipriano informa de la orden de Valeriano contra el clero y de ejecuciones en Roma; Poncio narra el arresto, sentencia y ejecución de Cipriano en Cartago."
      },
      "limitations": "The letter does not itself attest Cyprian's own death; Pontius' near-contemporary Life/Passion is hagiographic and presents providential framing. Exact 257–258 sequence reconstructed from multiple sources; distinguish exile/first edict from execution under second edict.",
      "consultationDate": "2026-10-12",
      "status": "consulted",
      "reviewState": "consulted by collection agent; architect interpretation and independent historical review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/050681.htm",
      "passage": "Cyprian, Epistle81.1–2 (other editions80), complete displayed letter",
      "limitations": "Report of Roman measures and executions, not firsthand account of his own future execution. Different edicts and regional implementation must remain separate.",
      "consultationDate": "2026-10-13",
      "status": "architect read specified passages; independent approval pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/0505.htm",
      "passage": "Pontius15–18, architect read arrest, overnight custody, tribunal and death",
      "limitations": "Christian commemorative framing and reported dialogue, not neutral motives, contemporary cadastral coordinates, divine causation or permission for player to change death.",
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

EN: Stage at least eight original households alive and all four original property chests at the western coordination yard.

ES: Prepara con vida al menos ocho hogares originales y los cuatro cofres originales en el patio occidental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 8,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-1",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-3",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-5",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-6",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-7",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-8",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-9",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-10"
      ],
      "destinations": {
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-1": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-2": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-3": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-4": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-5": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-6": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-7": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-8": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-9": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-10": "faith-origins.29-bounded-evacuation-carthage.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "faith-origins.29-bounded-evacuation-carthage.household-property-1",
        "faith-origins.29-bounded-evacuation-carthage.household-property-2",
        "faith-origins.29-bounded-evacuation-carthage.household-property-3",
        "faith-origins.29-bounded-evacuation-carthage.household-property-4"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "faith-origins.29-bounded-evacuation-carthage.household-property-1",
        "faith-origins.29-bounded-evacuation-carthage.household-property-2",
        "faith-origins.29-bounded-evacuation-carthage.household-property-3",
        "faith-origins.29-bounded-evacuation-carthage.household-property-4"
      ],
      "destinations": {
        "faith-origins.29-bounded-evacuation-carthage.household-property-1": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.household-property-2": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.household-property-3": "faith-origins.29-bounded-evacuation-carthage.destination-2",
        "faith-origins.29-bounded-evacuation-carthage.household-property-4": "faith-origins.29-bounded-evacuation-carthage.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true,
  "exportedLedgers": [
    {
      "id": "staged-households",
      "operator": "intersection",
      "fromRequirements": [
        "req-1"
      ],
      "minimumCount": 8
    }
  ]
}
```

EN: The actual received household group and all four chests are recorded.

ES: Se registran el grupo de hogares recibido realmente y los cuatro cofres.

EN: Our local list is invented; it is not a list of historical clergy.

ES: Nuestra lista local es inventada; no es una lista de clérigos históricos.

### o2 / phase-2

EN: Collect three original ordinary local work notes, deliver them to the northern court and pay 300 food 100 wood once at the western yard.

ES: Recoge tres notas ordinarias originales, entrégalas en el patio norte y paga una vez 300 de alimento 100 de madera en el occidental.

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
        "faith-origins.29-bounded-evacuation-carthage.local-work-notes-1",
        "faith-origins.29-bounded-evacuation-carthage.local-work-notes-2",
        "faith-origins.29-bounded-evacuation-carthage.local-work-notes-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.29-bounded-evacuation-carthage.local-work-notes-1",
        "faith-origins.29-bounded-evacuation-carthage.local-work-notes-2",
        "faith-origins.29-bounded-evacuation-carthage.local-work-notes-3"
      ],
      "destinations": {
        "faith-origins.29-bounded-evacuation-carthage.local-work-notes-1": "faith-origins.29-bounded-evacuation-carthage.destination-3",
        "faith-origins.29-bounded-evacuation-carthage.local-work-notes-2": "faith-origins.29-bounded-evacuation-carthage.destination-3",
        "faith-origins.29-bounded-evacuation-carthage.local-work-notes-3": "faith-origins.29-bounded-evacuation-carthage.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 300,
        "wood": 100
      },
      "id": "req-3",
      "receivingZones": [
        "faith-origins.29-bounded-evacuation-carthage.destination-2"
      ],
      "allocations": {
        "faith-origins.29-bounded-evacuation-carthage.destination-2": {
          "food": 300,
          "wood": 100
        }
      },
      "account": "spendable",
      "paidFlag": "faith-origins.29-bounded-evacuation-carthage.o2.req-3.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The independent note circuit and one exact provision payment are complete.

ES: Se han completado el circuito independiente de notas y un pago exacto de provisiones.

EN: Ordinary local work notes cannot stand in for an emperor’s rescript.

ES: Las notas locales ordinarias no sustituyen el rescripto de un emperador.

### o3 / phase-3

EN: Bring at least eight members of the actual staged household group and all four original property chests to the eastern inland receiving court.

ES: Lleva al menos ocho miembros del grupo de hogares realmente preparado y los cuatro cofres originales al patio receptor interior oriental.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 8,
      "state": "arrived",
      "eligibleEntitiesFromLedger": {
        "objective": "o1",
        "ledger": "staged-households"
      },
      "id": "req-1",
      "entities": [
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-1",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-3",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-5",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-6",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-7",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-8",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-9",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-10"
      ],
      "destinations": {
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-1": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-2": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-3": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-4": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-5": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-6": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-7": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-8": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-9": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-10": "faith-origins.29-bounded-evacuation-carthage.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 4,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "faith-origins.29-bounded-evacuation-carthage.household-property-1",
        "faith-origins.29-bounded-evacuation-carthage.household-property-2",
        "faith-origins.29-bounded-evacuation-carthage.household-property-3",
        "faith-origins.29-bounded-evacuation-carthage.household-property-4"
      ],
      "destinations": {
        "faith-origins.29-bounded-evacuation-carthage.household-property-1": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.household-property-2": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.household-property-3": "faith-origins.29-bounded-evacuation-carthage.destination-4",
        "faith-origins.29-bounded-evacuation-carthage.household-property-4": "faith-origins.29-bounded-evacuation-carthage.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: At least eight actual staged households and four original chests reached local reception.

ES: Al menos ocho hogares realmente preparados y cuatro cofres originales llegaron a la recepción local.

EN: This imagined arrival changes none of the source’s reported deaths.

ES: Esta llegada imaginada no cambia ninguna muerte relatada por la fuente.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/faith-origins/odyssey/29-bounded-evacuation-carthage.svg)

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
  "asset": "docs/design/maps/faith-origins/odyssey/29-bounded-evacuation-carthage.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-1",
      "role": "fictional-voluntary-household",
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
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-2",
      "role": "fictional-voluntary-household",
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
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-3",
      "role": "fictional-voluntary-household",
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
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-4",
      "role": "fictional-voluntary-household",
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
    },
    {
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-5",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        10
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
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-6",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        10
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
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-7",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -6,
        10
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
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-8",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -4,
        10
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
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-9",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        12
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
      "id": "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-10",
      "role": "fictional-voluntary-household",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        12
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
      "id": "faith-origins.29-bounded-evacuation-carthage.household-property-1",
      "role": "fictional-household-property",
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
      "id": "faith-origins.29-bounded-evacuation-carthage.household-property-2",
      "role": "fictional-household-property",
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
      "id": "faith-origins.29-bounded-evacuation-carthage.household-property-3",
      "role": "fictional-household-property",
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
      "id": "faith-origins.29-bounded-evacuation-carthage.household-property-4",
      "role": "fictional-household-property",
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
    },
    {
      "id": "faith-origins.29-bounded-evacuation-carthage.local-work-notes-1",
      "role": "fictional-local-circulation-note",
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
      "id": "faith-origins.29-bounded-evacuation-carthage.local-work-notes-2",
      "role": "fictional-local-circulation-note",
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
      "id": "faith-origins.29-bounded-evacuation-carthage.local-work-notes-3",
      "role": "fictional-local-circulation-note",
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
      "id": "faith-origins.29-bounded-evacuation-carthage.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.29-bounded-evacuation-carthage.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.29-bounded-evacuation-carthage.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "faith-origins.29-bounded-evacuation-carthage.destination-4",
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
    "withdrawal-households": [
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-1",
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-2",
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-3",
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-4",
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-5",
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-6",
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-7",
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-8",
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-9",
      "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-10"
    ],
    "household-property": [
      "faith-origins.29-bounded-evacuation-carthage.household-property-1",
      "faith-origins.29-bounded-evacuation-carthage.household-property-2",
      "faith-origins.29-bounded-evacuation-carthage.household-property-3",
      "faith-origins.29-bounded-evacuation-carthage.household-property-4"
    ],
    "local-work-notes": [
      "faith-origins.29-bounded-evacuation-carthage.local-work-notes-1",
      "faith-origins.29-bounded-evacuation-carthage.local-work-notes-2",
      "faith-origins.29-bounded-evacuation-carthage.local-work-notes-3"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-1",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-2",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-3",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-4",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-5",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-6",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-7",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-8",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-9",
        "faith-origins.29-bounded-evacuation-carthage.withdrawal-households-10"
      ],
      "minimumAliveOrAlreadySafe": 8
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Two sources on separate shelves / Dos fuentes en estantes separados

EN: Recover both separate copies from two sources on separate shelves and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de dos fuentes en estantes separados y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Context distinguishes Cyprian’s report from Pontius’ narration; no invented last letter or private motive.

ES: El contexto distingue el informe de Cipriano de la narración de Poncio; no inventa última carta ni motivos privados.

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
          "29-bounded-evacuation-carthage.side-1.entity-1",
          "29-bounded-evacuation-carthage.side-1.entity-2"
        ],
        "destinations": {
          "29-bounded-evacuation-carthage.side-1.entity-1": "29-bounded-evacuation-carthage.side-1.zone-1",
          "29-bounded-evacuation-carthage.side-1.entity-2": "29-bounded-evacuation-carthage.side-1.zone-1"
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
        "id": "29-bounded-evacuation-carthage.side-1.entity-1",
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
        "id": "29-bounded-evacuation-carthage.side-1.entity-2",
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
        "id": "29-bounded-evacuation-carthage.side-1.zone-1",
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
      "onceFlag": "29-bounded-evacuation-carthage.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.faith-origins.29-bounded-evacuation-carthage"
      ],
      "historicalNote": {
        "en": "Cyprian’s letter to Successus reports Valerian’s measures and executions at Rome. His own death is narrated separately by Pontius, who describes arrest, sentence and execution at Carthage in a Christian commemorative frame. The 257–258 sequence uses multiple sources. A fictional local household withdrawal cannot rescue Cyprian or halt the measures.",
        "es-ES": "La carta de Cipriano a Successus informa de medidas de Valeriano y ejecuciones en Roma. Su muerte se narra por separado en Poncio, quien describe arresto, sentencia y ejecución en Cartago desde una memoria cristiana. La secuencia 257–258 usa varias fuentes. Una retirada local ficticia de hogares no rescata a Cipriano ni detiene las medidas."
      },
      "hint": {
        "en": "Stage at least eight original households alive and all four original property chests at the western coordination yard.",
        "es-ES": "Prepara con vida al menos ocho hogares originales y los cuatro cofres originales en el patio occidental."
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

### Independent inland care / Cuidados interiores independientes

EN: Bring each of the two aid crates to its assigned household at independent inland care. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en cuidados interiores independientes. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Help separate households without a clerical-status or conversion requirement.

ES: Ayuda a hogares separados sin exigir condición clerical ni conversión.

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
          "29-bounded-evacuation-carthage.side-2.entity-1",
          "29-bounded-evacuation-carthage.side-2.entity-2"
        ],
        "destinations": {
          "29-bounded-evacuation-carthage.side-2.entity-1": "29-bounded-evacuation-carthage.side-2.zone-1",
          "29-bounded-evacuation-carthage.side-2.entity-2": "29-bounded-evacuation-carthage.side-2.zone-2"
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
        "id": "29-bounded-evacuation-carthage.side-2.entity-1",
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
        "id": "29-bounded-evacuation-carthage.side-2.entity-2",
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
        "id": "29-bounded-evacuation-carthage.side-2.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "29-bounded-evacuation-carthage.side-2.zone-2",
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
      "onceFlag": "29-bounded-evacuation-carthage.side-2.rewarded",
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

### The withdrawal supply shed / El cobertizo de provisiones de retirada

EN: Pay 50 wood and restore the damaged store of the withdrawal supply shed to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de el cobertizo de provisiones de retirada. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Finite repair supplies do not resurrect a lost main identity.

ES: Las provisiones finitas de reparación no resucitan identidades principales perdidas.

```json
{
  "id": "side-3",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "29-bounded-evacuation-carthage.side-3.entity-1",
        "health": "full",
        "paymentReceipt": "29-bounded-evacuation-carthage.side-3.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "29-bounded-evacuation-carthage.side-3.payment",
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
        "id": "29-bounded-evacuation-carthage.side-3.entity-1",
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
        "id": "29-bounded-evacuation-carthage.side-3.zone-1",
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
      "onceFlag": "29-bounded-evacuation-carthage.side-3.rewarded",
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

### The local provision exchange / El intercambio local de provisiones

EN: Escort the trader of the local provision exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de el intercambio local de provisiones hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: Bounded trade never buys a historical evacuation permit or refunds the main payment twice.

ES: El comercio limitado no compra un permiso histórico ni devuelve dos veces el pago principal.

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
          "29-bounded-evacuation-carthage.side-4.entity-1"
        ],
        "destinations": {
          "29-bounded-evacuation-carthage.side-4.entity-1": "29-bounded-evacuation-carthage.side-4.zone-1"
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
        "receipt": "29-bounded-evacuation-carthage.side-4.payment",
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
        "id": "29-bounded-evacuation-carthage.side-4.entity-1",
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
        "id": "29-bounded-evacuation-carthage.side-4.zone-1",
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
      "onceFlag": "29-bounded-evacuation-carthage.side-4.rewarded",
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

### Northern note-circuit viewpoints / Miradores del circuito norte de notas

EN: Scout both marked viewpoints of northern note-circuit viewpoints. Benefit: Mark the surveyed north-road inland circuit once; main receivers remain disclosed without it.

ES: Explora los dos miradores señalados de miradores del circuito norte de notas. Ventaja: Señala una vez el circuito interior trazado north-road; los receptores principales siguen identificados sin él.

EN: Survey a real note route without identifying a bishop’s arrest or execution address.

ES: Reconoce una ruta real de notas sin identificar direcciones de arresto o ejecución del obispo.

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
          "29-bounded-evacuation-carthage.side-5.zone-1",
          "29-bounded-evacuation-carthage.side-5.zone-2"
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
        "id": "29-bounded-evacuation-carthage.side-5.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "29-bounded-evacuation-carthage.side-5.zone-2",
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
      "onceFlag": "29-bounded-evacuation-carthage.side-5.rewarded",
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

### An inland withdrawal guide / Un guía interior de retirada

EN: Escort the local guide of an inland withdrawal guide to the marked road junction. Benefit: Mark the surveyed relief inland circuit once; main receivers remain disclosed without it.

ES: Escolta al guía local de un guía interior de retirada hasta el cruce señalado. Ventaja: Señala una vez el circuito interior trazado relief; los receptores principales siguen identificados sin él.

EN: Marks an open inland circuit and does not create an undocumented sea escape.

ES: Señala un circuito interior abierto y no crea una huida marítima indocumentada.

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
          "29-bounded-evacuation-carthage.side-6.entity-1"
        ],
        "destinations": {
          "29-bounded-evacuation-carthage.side-6.entity-1": "29-bounded-evacuation-carthage.side-6.zone-1"
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
        "id": "29-bounded-evacuation-carthage.side-6.entity-1",
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
        "id": "29-bounded-evacuation-carthage.side-6.zone-1",
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
      "onceFlag": "29-bounded-evacuation-carthage.side-6.rewarded",
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
      "id": "staged-household-priority",
      "optionalObjectives": [
        "side-2",
        "side-6"
      ],
      "costOfOpportunity": "Secure at least eight actual staged identities before dispatch, then use disclosed inland reception.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "split-note-and-property-teams",
      "optionalObjectives": [
        "side-1",
        "side-5"
      ],
      "costOfOpportunity": "Send separate notes north while the convoy stages; preserve fourpropertyidentities and 300 food 100 woodmain reserve.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "finite-supply-support",
      "optionalObjectives": [
        "side-3",
        "side-4"
      ],
      "costOfOpportunity": "Invest in finite repair/trade circuits without consuming protected recovery stock or substituting mainpeople.",
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
      "food": 1418,
      "wood": 808,
      "gold": 204,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 100,
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
      "food": 1370,
      "wood": 780,
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
      "food": 1470,
      "wood": 830,
      "gold": 215,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 100,
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
      "food": 1370,
      "wood": 780,
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
      "food": 1523,
      "wood": 853,
      "gold": 227,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 300,
      "wood": 100,
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
      "food": 1370,
      "wood": 780,
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
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.title / always | none | A Harbour Under Orders | Un puerto bajo órdenes |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.fact-intro / intro first | collection-narrator | Cyprian’s letter to Successus reports Valerian’s measures and executions at Rome. His own death is narrated separately by Pontius, who describes arrest, sentence and execution at Carthage in a Christian commemorative frame. The 257–258 sequence uses multiple sources. A fictional local household withdrawal cannot rescue Cyprian or halt the measures. | La carta de Cipriano a Successus informa de medidas de Valeriano y ejecuciones en Roma. Su muerte se narra por separado en Poncio, quien describe arresto, sentencia y ejecución en Cartago desde una memoria cristiana. La secuencia 257–258 usa varias fuentes. Una retirada local ficticia de hogares no rescata a Cipriano ni detiene las medidas. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.persona-intro / after handover | miriam-archive | A letter written by someone still alive and an account of his death belong on different shelves. My inherited grief wants to read them together too quickly. I stop, name the different voices, and only then return to our imagined neighbors. | La carta escrita por alguien aún vivo y el relato de su muerte pertenecen a estantes distintos. Mi dolor heredado quiere leerlos juntos demasiado deprisa. Me detengo, nombro las voces diferentes y solo entonces vuelvo a nuestros vecinos imaginados. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.route-help / available from start; repeatable without effect | none | Stage at least eight of ten original households and all four property chests at the western yard. Collect three distinct ordinary local work notes. Pay 300 food and 100 wood once there and deliver those notes to the northern court. Bring at least eight actual staged households and all four original chests alive/intact to the eastern inland court. Main travel is disclosed and no army, pardon or bishop rescue is required. | Prepara al menos ocho de los diez hogares originales y los cuatro cofres en el patio occidental. Recoge tres notas ordinarias locales distintas. Paga allí una vez 300 de alimento y 100 de madera y entrega las notas en el patio norte. Lleva al menos ocho hogares realmente preparados y los cuatro cofres originales con vida/intactos al patio interior oriental. El viaje principal está indicado y no exige ejército, indulto ni rescatar a un obispo. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.o1-goal / phase-1 active | none | Stage at least eight original households alive and all four original property chests at the western coordination yard. | Prepara con vida al menos ocho hogares originales y los cuatro cofres originales en el patio occidental. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.o1-receipt / o1 latched once | none | The actual received household group and all four chests are recorded. | Se registran el grupo de hogares recibido realmente y los cuatro cofres. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.o1-reaction / after o1 receipt | miriam-archive | Our local list is invented; it is not a list of historical clergy. | Nuestra lista local es inventada; no es una lista de clérigos históricos. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.o2-goal / phase-2 active | none | Collect three original ordinary local work notes, deliver them to the northern court and pay 300 food 100 wood once at the western yard. | Recoge tres notas ordinarias originales, entrégalas en el patio norte y paga una vez 300 de alimento 100 de madera en el occidental. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.o2-receipt / o2 latched once | none | The independent note circuit and one exact provision payment are complete. | Se han completado el circuito independiente de notas y un pago exacto de provisiones. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.o2-reaction / after o2 receipt | miriam-archive | Ordinary local work notes cannot stand in for an emperor’s rescript. | Las notas locales ordinarias no sustituyen el rescripto de un emperador. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.o3-goal / phase-3 active | none | Bring at least eight members of the actual staged household group and all four original property chests to the eastern inland receiving court. | Lleva al menos ocho miembros del grupo de hogares realmente preparado y los cuatro cofres originales al patio receptor interior oriental. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.o3-receipt / o3 latched once | none | At least eight actual staged households and four original chests reached local reception. | Al menos ocho hogares realmente preparados y cuatro cofres originales llegaron a la recepción local. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.o3-reaction / after o3 receipt | miriam-archive | This imagined arrival changes none of the source’s reported deaths. | Esta llegada imaginada no cambia ninguna muerte relatada por la fuente. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-1-goal / optional list from start | none | Recover both separate copies from two sources on separate shelves and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de dos fuentes en estantes separados y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-1-complete / side-1 completed | none | Two sources on separate shelves completed. Its stated benefit has been granted once. | Dos fuentes en estantes separados: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-1-lost / side-1 failed-optional | none | Two sources on separate shelves is unavailable after the loss of its unique participant or object. The main mission continues. | Dos fuentes en estantes separados: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-2-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at independent inland care. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en cuidados interiores independientes. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-2-complete / side-2 completed | none | Independent inland care completed. Its stated benefit has been granted once. | Cuidados interiores independientes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-2-lost / side-2 failed-optional | none | Independent inland care is unavailable after the loss of its unique participant or object. The main mission continues. | Cuidados interiores independientes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-3-goal / optional list from start | none | Pay 50 wood and restore the damaged store of the withdrawal supply shed to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el cobertizo de provisiones de retirada. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-3-complete / side-3 completed | none | The withdrawal supply shed completed. Its stated benefit has been granted once. | El cobertizo de provisiones de retirada: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-3-lost / side-3 failed-optional | none | The withdrawal supply shed is unavailable after the loss of its unique participant or object. The main mission continues. | El cobertizo de provisiones de retirada: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-4-goal / optional list from start | none | Escort the trader of the local provision exchange to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de el intercambio local de provisiones hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-4-complete / side-4 completed | none | The local provision exchange completed. Its stated benefit has been granted once. | El intercambio local de provisiones: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-4-lost / side-4 failed-optional | none | The local provision exchange is unavailable after the loss of its unique participant or object. The main mission continues. | El intercambio local de provisiones: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-5-goal / optional list from start | none | Scout both marked viewpoints of northern note-circuit viewpoints. Benefit: Mark the surveyed north-road inland circuit once; main receivers remain disclosed without it. | Explora los dos miradores señalados de miradores del circuito norte de notas. Ventaja: Señala una vez el circuito interior trazado north-road; los receptores principales siguen identificados sin él. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-5-complete / side-5 completed | none | Northern note-circuit viewpoints completed. Its stated benefit has been granted once. | Miradores del circuito norte de notas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-5-lost / side-5 failed-optional | none | Northern note-circuit viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores del circuito norte de notas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-6-goal / optional list from start | none | Escort the local guide of an inland withdrawal guide to the marked road junction. Benefit: Mark the surveyed relief inland circuit once; main receivers remain disclosed without it. | Escolta al guía local de un guía interior de retirada hasta el cruce señalado. Ventaja: Señala una vez el circuito interior trazado relief; los receptores principales siguen identificados sin él. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-6-complete / side-6 completed | none | An inland withdrawal guide completed. Its stated benefit has been granted once. | Un guía interior de retirada: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.side-6-lost / side-6 failed-optional | none | An inland withdrawal guide is unavailable after the loss of its unique participant or object. The main mission continues. | Un guía interior de retirada: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.fact-outro / victory first | collection-narrator | At least eight actual staged fictional household identities and four original property chests reached an inland receiving court. This establishes no historically attested evacuation permit, repeal or rescue of Cyprian. Pontius’ reported execution and theological interpretation remain distinguished. | Al menos ocho identidades de hogares ficticios realmente preparados y cuatro cofres originales llegaron a un patio receptor interior. Esto no acredita un permiso histórico de evacuación, una revocación ni un rescate de Cipriano. La ejecución relatada por Poncio y su interpretación teológica permanecen diferenciadas. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.persona-outro / after fact-outro | miriam-archive | I have not carried a bishop away from his death. I have tried to keep our smaller fiction honest and its neighbors distinct. Their story can end here without asking the old account to change its ending. | No he apartado a un obispo de su muerte. He procurado que nuestra ficción menor sea honesta y sus vecinos sean distintos. Su historia puede terminar aquí sin pedirle al relato antiguo que cambie de desenlace. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.faith-origins.29-bounded-evacuation-carthage.odyssey.next-episode / after persona-outro | none | Continue with A Different Dawn. This episode does not complete the campaign. | Continúa con Un alba distinta. Este episodio no termina la campaña. |

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
      "If nine households staged, any eight of those nine may complete; an unstaged tenth cannot substitute.",
      "If exactly eight staged and one is lost, the tenth household cannot replace it.",
      "The same four property identities persist across both receiving courts.",
      "An ordinary local work note cannot count as Cyprian’s autograph or an imperial rescript.",
      "No controllable Cyprian unit or guessed execution address.",
      "Main victory with all optionals skipped must be tested at every difficulty.",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
