# 5. The Road to Arles

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `05-delegate-logistics-arles` · 314 CE · 400×400

## Historical frame and fixed outcome

EN: A transmitted imperial invitation calls bishops to Arles and provides public conveyance for Chrestus and his companions. The preserved synodal letter describes decisions and addresses Sylvester, who was absent. These texts frame a council in 314; prescriptions and polemical judgments are not evidence of every traveler’s actual route or universal compliance. Our three reception posts and local helpers are fictional, with no reenacted private council session.

ES: Una invitación imperial transmitida convoca obispos a Arlés y dispone transporte público para Cresto y sus acompañantes. La carta sinodal conservada describe decisiones y se dirige a Silvestre, ausente. Estos textos enmarcan un concilio en 314; prescripciones y juicios polémicos no prueban la ruta real de cada viajero ni cumplimiento universal. Nuestros tres puestos receptores y ayudantes locales son ficticios, sin recrear una sesión privada del concilio.

EN: Six original fictional helpers reached three assigned posts, each post received its own food allocation, and three separate local notes supported one funded working register. This bounded hospitality scene is not the journey of Chrestus, the council’s acta or evidence that its decisions ended the controversy. The synodal letter’s judgments remain attributed; subsequent political conflict has a separate local map.

ES: Seis ayudantes ficticios originales llegaron a tres puestos asignados, cada puesto recibió su propia asignación de alimento y tres notas locales separadas sustentaron un registro de trabajo financiado. Esta escena acotada de hospitalidad no es el viaje de Cresto, las actas del concilio ni prueba de que sus decisiones acabaran la controversia. Los juicios de la carta sinodal siguen atribuidos; el conflicto político posterior tiene otro mapa local.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "The transmitted invitation prescribes travel to Arles, public conveyance and arrival before the August date. The preserved synodal letter addresses absent Sylvester and states decisions. Neither document proves every route, Constantine’s presence or universal compliance.",
        "es-ES": "La invitación transmitida prescribe viaje a Arlés, transporte público y llegada antes de la fecha de agosto. La carta sinodal conservada se dirige a Silvestre ausente y expresa decisiones. Ningún documento prueba todas las rutas, la presencia de Constantino ni cumplimiento universal."
      },
      "architectCorrection": {
        "date": "2026-10-13",
        "author": "gpt-6",
        "approval": "independent historical review pending",
        "reason": "Direct primary passages replace candidate conflations; all gameplay participants and work outputs remain explicit fiction."
      }
    },
    {
      "consultedUrl": "https://christearlychurch.co.uk/text/the-acts-of-the-council-of-arles/",
      "passage": "Council of Arles page, introductory lines 16–17 and references to canons 1, 8, 20.",
      "limitations": "Page’s narrative introduction is modern editorial framing; it gives 1 August 314, while precise dating derives from scholarly reconstruction. Checked summary, not full canonical text.",
      "status": "consulted",
      "supportedClaim": "Supports a 314 council convened after the Caecilian/Donatist dispute, with canons addressing Pascha, baptism and episcopal consecration. / Respalda un concilio de 314 convocado tras la disputa de Ceciliano y los donatistas, con cánones sobre Pascua, bautismo y consagraciones episcopales.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "Editorial introduction and canon summary only.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/250110.htm",
      "passage": "Eusebius HE X.5.21–24",
      "coverageActuallyRead": "Complete displayed letter to Chrestus with Arles destination, vehicle/companions and arrival instruction.",
      "limitations": "Normative transmitted invitation, not observed itinerary; no exact council venue or native timed travel.",
      "consultationDate": "2026-10-13",
      "approval": "architect interpretation; independent approval pending"
    },
    {
      "consultedUrl": "https://www.tertullian.org/fathers/optatus_11_appendices.htm",
      "passage": "Appendix IV synodal letter to Sylvester, displayed pp389–393",
      "coverageActuallyRead": "Read complete displayed letter, absent addressee, attributed judgments, common Pascha prescription and disciplinary passages; ending has transmission break/narrative fragment.",
      "limitations": "Did not read Munier critical edition or a complete separately numbered22-canon collection. Modern page claims Constantine attended; not adopted as verified fact.",
      "consultationDate": "2026-10-13",
      "approval": "architect interpretation; independent approval pending"
    }
  ],
  "knowledgeBasis": {
    "speaker": "imperial-clerk",
    "proposedLifespan": "c.334–403",
    "mode": "inherited family papers, not direct adult memory",
    "noOmniscience": true
  }
}
```

## Main objectives and individual contracts

### o1 / phase-1

EN: Visit all three reception posts and pay one 100 wood preparation allocation: 40 north, 30 east and 30 south.

ES: Visita los tres puestos receptores y paga una asignación única de preparación de 100 de madera: 40 norte, 30 este y 30 sur.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "area-state",
      "requiredCount": 3,
      "state": "visited-and-passable",
      "blockingEnemies": [],
      "id": "req-1",
      "zones": [
        "imperial-church.05-delegate-logistics-arles.destination-1",
        "imperial-church.05-delegate-logistics-arles.destination-3",
        "imperial-church.05-delegate-logistics-arles.destination-4"
      ]
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 100
      },
      "id": "req-2",
      "receivingZones": [
        "imperial-church.05-delegate-logistics-arles.destination-1",
        "imperial-church.05-delegate-logistics-arles.destination-3",
        "imperial-church.05-delegate-logistics-arles.destination-4"
      ],
      "allocations": {
        "imperial-church.05-delegate-logistics-arles.destination-1": {
          "wood": 40
        },
        "imperial-church.05-delegate-logistics-arles.destination-3": {
          "wood": 30
        },
        "imperial-church.05-delegate-logistics-arles.destination-4": {
          "wood": 30
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.05-delegate-logistics-arles.o1.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three actual post visits and one distributed preparation receipt are recorded.

ES: Se registran tres visitas reales y un recibo de preparación distribuida.

EN: The invitation gives a destination. These smaller work posts belong to our fiction.

ES: La invitación da un destino. Estos puestos menores de trabajo pertenecen a nuestra ficción.

### o2 / phase-2

EN: Escort six original local helpers to their assigned posts, two per post; pay 120 food to each post once.

ES: Escolta seis ayudantes locales originales a sus puestos asignados, dos por puesto; paga una vez 120 de alimento a cada puesto.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "imperial-church.05-delegate-logistics-arles.local-helpers-1",
        "imperial-church.05-delegate-logistics-arles.local-helpers-2",
        "imperial-church.05-delegate-logistics-arles.local-helpers-3",
        "imperial-church.05-delegate-logistics-arles.local-helpers-4",
        "imperial-church.05-delegate-logistics-arles.local-helpers-5",
        "imperial-church.05-delegate-logistics-arles.local-helpers-6"
      ],
      "destinations": {
        "imperial-church.05-delegate-logistics-arles.local-helpers-1": "imperial-church.05-delegate-logistics-arles.destination-1",
        "imperial-church.05-delegate-logistics-arles.local-helpers-2": "imperial-church.05-delegate-logistics-arles.destination-1",
        "imperial-church.05-delegate-logistics-arles.local-helpers-3": "imperial-church.05-delegate-logistics-arles.destination-3",
        "imperial-church.05-delegate-logistics-arles.local-helpers-4": "imperial-church.05-delegate-logistics-arles.destination-3",
        "imperial-church.05-delegate-logistics-arles.local-helpers-5": "imperial-church.05-delegate-logistics-arles.destination-4",
        "imperial-church.05-delegate-logistics-arles.local-helpers-6": "imperial-church.05-delegate-logistics-arles.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 360
      },
      "id": "req-2",
      "receivingZones": [
        "imperial-church.05-delegate-logistics-arles.destination-1",
        "imperial-church.05-delegate-logistics-arles.destination-3",
        "imperial-church.05-delegate-logistics-arles.destination-4"
      ],
      "allocations": {
        "imperial-church.05-delegate-logistics-arles.destination-1": {
          "food": 120
        },
        "imperial-church.05-delegate-logistics-arles.destination-3": {
          "food": 120
        },
        "imperial-church.05-delegate-logistics-arles.destination-4": {
          "food": 120
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.05-delegate-logistics-arles.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All six assigned helpers arrived and every post has its own food allocation.

ES: Llegaron los seis ayudantes asignados y cada puesto tiene su propia asignación de alimento.

EN: A full northern table cannot feed the southern one by arithmetic alone.

ES: Una mesa norteña llena no alimenta la sureña solo por aritmética.

### o3 / phase-3

EN: Collect the three distinct ordinary post notes and deliver all three to the central work yard.

ES: Recoge las tres notas ordinarias distintas de los puestos y entrega las tres en el patio central.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-1",
      "entities": [
        "imperial-church.05-delegate-logistics-arles.north-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.05-delegate-logistics-arles.north-note-1"
      ],
      "destinations": {
        "imperial-church.05-delegate-logistics-arles.north-note-1": "imperial-church.05-delegate-logistics-arles.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.05-delegate-logistics-arles.east-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "imperial-church.05-delegate-logistics-arles.east-note-1"
      ],
      "destinations": {
        "imperial-church.05-delegate-logistics-arles.east-note-1": "imperial-church.05-delegate-logistics-arles.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-5",
      "entities": [
        "imperial-church.05-delegate-logistics-arles.south-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-6",
      "entities": [
        "imperial-church.05-delegate-logistics-arles.south-note-1"
      ],
      "destinations": {
        "imperial-church.05-delegate-logistics-arles.south-note-1": "imperial-church.05-delegate-logistics-arles.destination-2"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: One distinct local note from each post reached the central yard.

ES: Llegó al patio central una nota local distinta de cada puesto.

EN: The third note completes our local count; it adds no vote to the council.

ES: La tercera nota completa nuestra cuenta local; no añade voto al concilio.

### o4 / phase-4

EN: Pay 80 wood and 30 gold once, prepare one working register from all three collected notes, and deliver it to the eastern archive.

ES: Paga una vez 80 de madera y 30 de oro, prepara un registro con las tres notas recogidas y entrégalo en el archivo oriental.

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
        "imperial-church.05-delegate-logistics-arles.destination-2"
      ],
      "allocations": {
        "imperial-church.05-delegate-logistics-arles.destination-2": {
          "wood": 80,
          "gold": 30
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.05-delegate-logistics-arles.o4.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "imperial-church.05-delegate-logistics-arles.north-note-1",
        "imperial-church.05-delegate-logistics-arles.east-note-1",
        "imperial-church.05-delegate-logistics-arles.south-note-1"
      ],
      "outputEntities": [
        "imperial-church.05-delegate-logistics-arles.working-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.05-delegate-logistics-arles.o4.req-1.paid",
          "fromObjective": "o4",
          "amounts": {
            "wood": 80,
            "gold": 30
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "imperial-church.05-delegate-logistics-arles.working-register-1"
      ],
      "destinations": {
        "imperial-church.05-delegate-logistics-arles.working-register-1": "imperial-church.05-delegate-logistics-arles.destination-5"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The funded fictional register reached the eastern local archive once.

ES: El registro ficticio financiado llegó una vez al archivo local oriental.

EN: A register of hospitality is enough for this yard. The council’s letter remains a different document.

ES: Un registro de hospitalidad basta para este patio. La carta del concilio sigue siendo otro documento.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/05-delegate-logistics-arles.svg)

```json
{
  "bbox": [
    4.605,
    43.654,
    4.67,
    43.71
  ],
  "terrainProfile": "arles",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        215.6,
        123.16
      ],
      "lonLat": [
        4.641,
        43.694
      ],
      "name": {
        "en": "Northern fictional reception post",
        "es-ES": "Puesto receptor ficticio norteño"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        215.6,
        212.22
      ],
      "lonLat": [
        4.641,
        43.68
      ],
      "name": {
        "en": "Central fictional work yard",
        "es-ES": "Patio ficticio central de trabajo"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        289.21,
        212.22
      ],
      "lonLat": [
        4.657,
        43.68
      ],
      "name": {
        "en": "Eastern fictional reception post",
        "es-ES": "Puesto receptor ficticio oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        201.8,
        320.37
      ],
      "lonLat": [
        4.638,
        43.663
      ],
      "name": {
        "en": "Southern fictional reception post",
        "es-ES": "Puesto receptor ficticio sureño"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        284.61,
        294.92
      ],
      "lonLat": [
        4.656,
        43.667
      ],
      "name": {
        "en": "Eastern fictional local archive",
        "es-ES": "Archivo local ficticio oriental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "north-hospitality",
      "hubOrder": [
        "hub-2",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "east-hospitality",
      "hubOrder": [
        "hub-2",
        "hub-3",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "south-hospitality",
      "hubOrder": [
        "hub-2",
        "hub-4",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "outer-reception-link",
      "hubOrder": [
        "hub-1",
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 6
    }
  ],
  "terrainInstructions": "Local Arelate/Rhône regional crop with all five fictional hospitality courts on city-side left/east-bank land. Trinquetaille and major fluvio-maritime port remains lie across the Rhône; no mandatory ferry, bridge or invented ford links this mission. Ancient boat-bridge chronology/phase differs between institutional accounts, so do not use a current or guessed Roman crossing to route delegates. No medieval Saint-Trophime façade, modern Rhône embankments/rail bridge, Arles–Fos canal or modern industrial docks. The actual council venue, local delegate lodgings and exact ancient streets are not substantiated here. Long-distance public travel is contextual narration, not a miniature Sicily-to-Arles map.",
  "corridorStraightLengthsTiles": {
    "north-hospitality": 89.06,
    "east-hospitality": 156.44,
    "south-hospitality": 195.66,
    "outer-reception-link": 254.6
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
        4.625,
        43.71
      ],
      [
        4.625,
        43.69
      ],
      [
        4.622,
        43.68
      ],
      [
        4.615,
        43.67
      ],
      [
        4.61,
        43.65
      ]
    ],
    "certainty": "architect schematic modern Rhône regional control; not dated314 banks or bridge footprint",
    "renderAs": "river-line"
  },
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/imperial-church/odyssey/05-delegate-logistics-arles.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.05-delegate-logistics-arles.local-helpers-1",
      "role": "fictional-voluntary-reception-helper",
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
      "id": "imperial-church.05-delegate-logistics-arles.local-helpers-2",
      "role": "fictional-voluntary-reception-helper",
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
      "id": "imperial-church.05-delegate-logistics-arles.local-helpers-3",
      "role": "fictional-voluntary-reception-helper",
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
    },
    {
      "id": "imperial-church.05-delegate-logistics-arles.local-helpers-4",
      "role": "fictional-voluntary-reception-helper",
      "initialHub": "hub-2",
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
      "id": "imperial-church.05-delegate-logistics-arles.local-helpers-5",
      "role": "fictional-voluntary-reception-helper",
      "initialHub": "hub-2",
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
      "id": "imperial-church.05-delegate-logistics-arles.local-helpers-6",
      "role": "fictional-voluntary-reception-helper",
      "initialHub": "hub-2",
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
      "id": "imperial-church.05-delegate-logistics-arles.north-note-1",
      "role": "fictional-local-reception-note",
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
      "id": "imperial-church.05-delegate-logistics-arles.east-note-1",
      "role": "fictional-local-reception-note",
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
      "id": "imperial-church.05-delegate-logistics-arles.south-note-1",
      "role": "fictional-local-reception-note",
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
      "id": "imperial-church.05-delegate-logistics-arles.working-register-1",
      "role": "fictional-labelled-local-register",
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
    }
  ],
  "zones": [
    {
      "id": "imperial-church.05-delegate-logistics-arles.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.05-delegate-logistics-arles.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.05-delegate-logistics-arles.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.05-delegate-logistics-arles.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.05-delegate-logistics-arles.destination-5",
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
    "local-helpers": [
      "imperial-church.05-delegate-logistics-arles.local-helpers-1",
      "imperial-church.05-delegate-logistics-arles.local-helpers-2",
      "imperial-church.05-delegate-logistics-arles.local-helpers-3",
      "imperial-church.05-delegate-logistics-arles.local-helpers-4",
      "imperial-church.05-delegate-logistics-arles.local-helpers-5",
      "imperial-church.05-delegate-logistics-arles.local-helpers-6"
    ],
    "north-note": [
      "imperial-church.05-delegate-logistics-arles.north-note-1"
    ],
    "east-note": [
      "imperial-church.05-delegate-logistics-arles.east-note-1"
    ],
    "south-note": [
      "imperial-church.05-delegate-logistics-arles.south-note-1"
    ],
    "working-register": [
      "imperial-church.05-delegate-logistics-arles.working-register-1"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.05-delegate-logistics-arles.local-helpers-1",
        "imperial-church.05-delegate-logistics-arles.local-helpers-2",
        "imperial-church.05-delegate-logistics-arles.local-helpers-3",
        "imperial-church.05-delegate-logistics-arles.local-helpers-4",
        "imperial-church.05-delegate-logistics-arles.local-helpers-5",
        "imperial-church.05-delegate-logistics-arles.local-helpers-6"
      ],
      "minimumAliveOrAlreadySafe": 6
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Survey the outer reception circuit / Reconoce el circuito receptor exterior

EN: Scout both marked viewpoints of survey the outer reception circuit. Benefit: Mark the proposed outer-reception-link local land circuit once. All mandatory receivers are already disclosed.

ES: Explora los dos miradores señalados de reconoce el circuito receptor exterior. Ventaja: Señala una vez el circuito terrestre local propuesto outer-reception-link. Todos los receptores obligatorios ya se indican.

EN: Marks a proposed east-bank land circuit; no asserted Roman bridge access.

ES: Señala un circuito terrestre propuesto de la ribera oriental; no afirma acceso por puente romano.

```json
{
  "id": "side-1",
  "kind": "scout",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "visit-zones",
        "zones": [
          "05-delegate-logistics-arles.side-1.zone-1",
          "05-delegate-logistics-arles.side-1.zone-2"
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
        "id": "05-delegate-logistics-arles.side-1.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "05-delegate-logistics-arles.side-1.zone-2",
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
      "target": "outer-reception-link proposed local land approach",
      "resources": {},
      "onceFlag": "05-delegate-logistics-arles.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "outer-reception-link"
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
      "north-hospitality",
      "east-hospitality",
      "south-hospitality",
      "outer-reception-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Invitation and decision on separate labels / Invitación y decisión en etiquetas separadas

EN: Recover both separate copies from invitation and decision on separate labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de invitación y decisión en etiquetas separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Optional context separates an order to travel from a transmitted decision and its historical enforcement.

ES: El contexto opcional distingue una orden de viaje de una decisión transmitida y su aplicación histórica.

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
          "05-delegate-logistics-arles.side-2.entity-1",
          "05-delegate-logistics-arles.side-2.entity-2"
        ],
        "destinations": {
          "05-delegate-logistics-arles.side-2.entity-1": "05-delegate-logistics-arles.side-2.zone-1",
          "05-delegate-logistics-arles.side-2.entity-2": "05-delegate-logistics-arles.side-2.zone-1"
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
        "id": "05-delegate-logistics-arles.side-2.entity-1",
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
        "id": "05-delegate-logistics-arles.side-2.entity-2",
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
        "id": "05-delegate-logistics-arles.side-2.zone-1",
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
      "onceFlag": "05-delegate-logistics-arles.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.05-delegate-logistics-arles"
      ],
      "historicalNote": {
        "en": "A transmitted imperial invitation calls bishops to Arles and provides public conveyance for Chrestus and his companions. The preserved synodal letter describes decisions and addresses Sylvester, who was absent. These texts frame a council in 314; prescriptions and polemical judgments are not evidence of every traveler’s actual route or universal compliance. Our three reception posts and local helpers are fictional, with no reenacted private council session.",
        "es-ES": "Una invitación imperial transmitida convoca obispos a Arlés y dispone transporte público para Cresto y sus acompañantes. La carta sinodal conservada describe decisiones y se dirige a Silvestre, ausente. Estos textos enmarcan un concilio en 314; prescripciones y juicios polémicos no prueban la ruta real de cada viajero ni cumplimiento universal. Nuestros tres puestos receptores y ayudantes locales son ficticios, sin recrear una sesión privada del concilio."
      },
      "hint": {
        "en": "Visit all three reception posts and pay one 100 wood preparation allocation: 40 north, 30 east and 30 south.",
        "es-ES": "Visita los tres puestos receptores y paga una asignación única de preparación de 100 de madera: 40 norte, 30 este y 30 sur."
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
      "north-hospitality",
      "east-hospitality",
      "south-hospitality",
      "outer-reception-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### The hosts’ ordinary households / Los hogares ordinarios de los anfitriones

EN: Bring each of the two aid crates to its assigned household at the hosts’ ordinary households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares ordinarios de los anfitriones. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Independent aid does not replace the three mandatory 120-food allocations.

ES: La ayuda independiente no sustituye las tres asignaciones obligatorias de 120 de alimento.

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
          "05-delegate-logistics-arles.side-3.entity-1",
          "05-delegate-logistics-arles.side-3.entity-2"
        ],
        "destinations": {
          "05-delegate-logistics-arles.side-3.entity-1": "05-delegate-logistics-arles.side-3.zone-1",
          "05-delegate-logistics-arles.side-3.entity-2": "05-delegate-logistics-arles.side-3.zone-2"
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
        "id": "05-delegate-logistics-arles.side-3.entity-1",
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
        "id": "05-delegate-logistics-arles.side-3.entity-2",
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
        "id": "05-delegate-logistics-arles.side-3.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "05-delegate-logistics-arles.side-3.zone-2",
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
      "onceFlag": "05-delegate-logistics-arles.side-3.rewarded",
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
      "north-hospitality",
      "east-hospitality",
      "south-hospitality",
      "outer-reception-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### An independent guest shelter / Un cobertizo independiente para huéspedes

EN: Pay 50 wood and restore the damaged store of an independent guest shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de un cobertizo independiente para huéspedes. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Ordinary shelter repair is fictional and does not reconstruct the council venue.

ES: La reparación ordinaria es ficticia y no reconstruye la sede del concilio.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "05-delegate-logistics-arles.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "05-delegate-logistics-arles.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "05-delegate-logistics-arles.side-4.payment",
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
        "id": "05-delegate-logistics-arles.side-4.entity-1",
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
        "id": "05-delegate-logistics-arles.side-4.zone-1",
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
      "onceFlag": "05-delegate-logistics-arles.side-4.rewarded",
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
      "north-hospitality",
      "east-hospitality",
      "south-hospitality",
      "outer-reception-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### A finite hospitality consignment / Una remesa finita de hospitalidad

EN: Escort the trader of a finite hospitality consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de una remesa finita de hospitalidad hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One bounded exchange supports local work without buying doctrine, communion or imperial transport rights.

ES: Un intercambio limitado apoya trabajo local sin comprar doctrina, comunión ni derechos imperiales de transporte.

```json
{
  "id": "side-5",
  "kind": "trade",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-arrival",
        "entities": [
          "05-delegate-logistics-arles.side-5.entity-1"
        ],
        "destinations": {
          "05-delegate-logistics-arles.side-5.entity-1": "05-delegate-logistics-arles.side-5.zone-1"
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
        "receipt": "05-delegate-logistics-arles.side-5.payment",
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
        "id": "05-delegate-logistics-arles.side-5.entity-1",
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
        "id": "05-delegate-logistics-arles.side-5.zone-1",
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
      "onceFlag": "05-delegate-logistics-arles.side-5.rewarded",
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
      "north-hospitality",
      "east-hospitality",
      "south-hospitality",
      "outer-reception-link"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Guide to the southern post / Guía al puesto sureño

EN: Escort the local guide of guide to the southern post to the marked road junction. Benefit: Mark the proposed south-hospitality local land circuit once. All mandatory receivers are already disclosed.

ES: Escolta al guía local de guía al puesto sureño hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local propuesto south-hospitality. Todos los receptores obligatorios ya se indican.

EN: Marks the disclosed southern local approach, never the actual complete itinerary of a bishop.

ES: Señala el acceso local sureño indicado, nunca el itinerario real completo de un obispo.

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
          "05-delegate-logistics-arles.side-6.entity-1"
        ],
        "destinations": {
          "05-delegate-logistics-arles.side-6.entity-1": "05-delegate-logistics-arles.side-6.zone-1"
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
        "id": "05-delegate-logistics-arles.side-6.entity-1",
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
        "id": "05-delegate-logistics-arles.side-6.zone-1",
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
      "target": "south-hospitality proposed local land approach",
      "resources": {},
      "onceFlag": "05-delegate-logistics-arles.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "south-hospitality"
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
      "north-hospitality",
      "east-hospitality",
      "south-hospitality",
      "outer-reception-link"
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
      "id": "three-team-hospitality",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Visit/prepare three posts and split six helpers into their assigned pairs; invest in land-route information.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "workshop-before-archive",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Prepare separate context and shelter while reserving the 180 wood/30 gold mandatory total.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "hosts-and-consignments",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Run separate household care and finite exchange while supplying120 food to each mandatory post.",
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
      "food": 1478,
      "wood": 888,
      "gold": 234,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 360,
      "wood": 180,
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
      "food": 1430,
      "wood": 860,
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
      "food": 1530,
      "wood": 910,
      "gold": 245,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 360,
      "wood": 180,
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
      "food": 1430,
      "wood": 860,
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
      "food": 1583,
      "wood": 933,
      "gold": 257,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 360,
      "wood": 180,
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
      "food": 1430,
      "wood": 860,
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
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.title / always | none | The Road to Arles | El camino hacia Arlés |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.fact-intro / intro first | collection-narrator | A transmitted imperial invitation calls bishops to Arles and provides public conveyance for Chrestus and his companions. The preserved synodal letter describes decisions and addresses Sylvester, who was absent. These texts frame a council in 314; prescriptions and polemical judgments are not evidence of every traveler’s actual route or universal compliance. Our three reception posts and local helpers are fictional, with no reenacted private council session. | Una invitación imperial transmitida convoca obispos a Arlés y dispone transporte público para Cresto y sus acompañantes. La carta sinodal conservada describe decisiones y se dirige a Silvestre, ausente. Estos textos enmarcan un concilio en 314; prescripciones y juicios polémicos no prueban la ruta real de cada viajero ni cumplimiento universal. Nuestros tres puestos receptores y ayudantes locales son ficticios, sin recrear una sesión privada del concilio. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.persona-intro / after handover | imperial-clerk | A traveling party can fill three entries before it fills one chair. That is the sort of detail my inherited invitation makes me notice. I once counted a successful reception as a successful agreement. The later papers taught me to distinguish them. These imagined hosts need food and preparation; the old dispute does not need me to invent a tidy ending. | Un grupo viajero puede llenar tres apuntes antes de llenar una silla. Es el detalle que me hace notar la invitación heredada. Una vez conté una recepción lograda como acuerdo logrado. Los papeles posteriores me enseñaron a distinguirlos. Estos anfitriones imaginados necesitan alimento y preparación; la vieja disputa no necesita que invente un final ordenado. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.route-help / available from start; repeatable without effect | none | Physically visit the north, east and south reception posts and fund their preparation with one 100 wood payment: 40 north, 30 east and 30 south. Escort six original fictional helpers to their assigned posts, two per post, and supply each post with exactly 120 food. Collect one ordinary local note from each post and deliver all three to the central work yard. Pay 80 wood and 30 gold there once, prepare one labelled working register and deliver it to the eastern archive. All three posts are disclosed; no real council vote or river crossing is required. | Visita físicamente los puestos receptores norte, este y sur y financia su preparación con un pago único de 100 de madera: 40 norte, 30 este y 30 sur. Escolta seis ayudantes ficticios originales a sus puestos asignados, dos por puesto, y suministra exactamente 120 de alimento a cada puesto. Recoge una nota ordinaria local de cada puesto y entrega las tres en el patio central. Paga allí una vez 80 de madera y 30 de oro, prepara un registro de trabajo etiquetado y entrégalo en el archivo oriental. Los tres puestos se indican; no se exige voto real del concilio ni cruce del río. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o1-goal / phase-1 active | none | Visit all three reception posts and pay one 100 wood preparation allocation: 40 north, 30 east and 30 south. | Visita los tres puestos receptores y paga una asignación única de preparación de 100 de madera: 40 norte, 30 este y 30 sur. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o1-receipt / o1 latched once | none | Three actual post visits and one distributed preparation receipt are recorded. | Se registran tres visitas reales y un recibo de preparación distribuida. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o1-reaction / after o1 receipt | imperial-clerk | The invitation gives a destination. These smaller work posts belong to our fiction. | La invitación da un destino. Estos puestos menores de trabajo pertenecen a nuestra ficción. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o2-goal / phase-2 active | none | Escort six original local helpers to their assigned posts, two per post; pay 120 food to each post once. | Escolta seis ayudantes locales originales a sus puestos asignados, dos por puesto; paga una vez 120 de alimento a cada puesto. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o2-receipt / o2 latched once | none | All six assigned helpers arrived and every post has its own food allocation. | Llegaron los seis ayudantes asignados y cada puesto tiene su propia asignación de alimento. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o2-reaction / after o2 receipt | imperial-clerk | A full northern table cannot feed the southern one by arithmetic alone. | Una mesa norteña llena no alimenta la sureña solo por aritmética. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o3-goal / phase-3 active | none | Collect the three distinct ordinary post notes and deliver all three to the central work yard. | Recoge las tres notas ordinarias distintas de los puestos y entrega las tres en el patio central. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o3-receipt / o3 latched once | none | One distinct local note from each post reached the central yard. | Llegó al patio central una nota local distinta de cada puesto. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o3-reaction / after o3 receipt | imperial-clerk | The third note completes our local count; it adds no vote to the council. | La tercera nota completa nuestra cuenta local; no añade voto al concilio. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o4-goal / phase-4 active | none | Pay 80 wood and 30 gold once, prepare one working register from all three collected notes, and deliver it to the eastern archive. | Paga una vez 80 de madera y 30 de oro, prepara un registro con las tres notas recogidas y entrégalo en el archivo oriental. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o4-receipt / o4 latched once | none | The funded fictional register reached the eastern local archive once. | El registro ficticio financiado llegó una vez al archivo local oriental. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.o4-reaction / after o4 receipt | imperial-clerk | A register of hospitality is enough for this yard. The council’s letter remains a different document. | Un registro de hospitalidad basta para este patio. La carta del concilio sigue siendo otro documento. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of survey the outer reception circuit. Benefit: Mark the proposed outer-reception-link local land circuit once. All mandatory receivers are already disclosed. | Explora los dos miradores señalados de reconoce el circuito receptor exterior. Ventaja: Señala una vez el circuito terrestre local propuesto outer-reception-link. Todos los receptores obligatorios ya se indican. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-1-complete / side-1 completed | none | Survey the outer reception circuit completed. Its stated benefit has been granted once. | Reconoce el circuito receptor exterior: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-1-lost / side-1 failed-optional | none | Survey the outer reception circuit is unavailable after the loss of its unique participant or object. The main mission continues. | Reconoce el circuito receptor exterior: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from invitation and decision on separate labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de invitación y decisión en etiquetas separadas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-2-complete / side-2 completed | none | Invitation and decision on separate labels completed. Its stated benefit has been granted once. | Invitación y decisión en etiquetas separadas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-2-lost / side-2 failed-optional | none | Invitation and decision on separate labels is unavailable after the loss of its unique participant or object. The main mission continues. | Invitación y decisión en etiquetas separadas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at the hosts’ ordinary households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares ordinarios de los anfitriones. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-3-complete / side-3 completed | none | The hosts’ ordinary households completed. Its stated benefit has been granted once. | Los hogares ordinarios de los anfitriones: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-3-lost / side-3 failed-optional | none | The hosts’ ordinary households is unavailable after the loss of its unique participant or object. The main mission continues. | Los hogares ordinarios de los anfitriones: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of an independent guest shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de un cobertizo independiente para huéspedes. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-4-complete / side-4 completed | none | An independent guest shelter completed. Its stated benefit has been granted once. | Un cobertizo independiente para huéspedes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-4-lost / side-4 failed-optional | none | An independent guest shelter is unavailable after the loss of its unique participant or object. The main mission continues. | Un cobertizo independiente para huéspedes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-5-goal / optional list from start | none | Escort the trader of a finite hospitality consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de una remesa finita de hospitalidad hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-5-complete / side-5 completed | none | A finite hospitality consignment completed. Its stated benefit has been granted once. | Una remesa finita de hospitalidad: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-5-lost / side-5 failed-optional | none | A finite hospitality consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Una remesa finita de hospitalidad: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-6-goal / optional list from start | none | Escort the local guide of guide to the southern post to the marked road junction. Benefit: Mark the proposed south-hospitality local land circuit once. All mandatory receivers are already disclosed. | Escolta al guía local de guía al puesto sureño hasta el cruce señalado. Ventaja: Señala una vez el circuito terrestre local propuesto south-hospitality. Todos los receptores obligatorios ya se indican. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-6-complete / side-6 completed | none | Guide to the southern post completed. Its stated benefit has been granted once. | Guía al puesto sureño: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.side-6-lost / side-6 failed-optional | none | Guide to the southern post is unavailable after the loss of its unique participant or object. The main mission continues. | Guía al puesto sureño: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.fact-outro / victory first | collection-narrator | Six original fictional helpers reached three assigned posts, each post received its own food allocation, and three separate local notes supported one funded working register. This bounded hospitality scene is not the journey of Chrestus, the council’s acta or evidence that its decisions ended the controversy. The synodal letter’s judgments remain attributed; subsequent political conflict has a separate local map. | Seis ayudantes ficticios originales llegaron a tres puestos asignados, cada puesto recibió su propia asignación de alimento y tres notas locales separadas sustentaron un registro de trabajo financiado. Esta escena acotada de hospitalidad no es el viaje de Cresto, las actas del concilio ni prueba de que sus decisiones acabaran la controversia. Los juicios de la carta sinodal siguen atribuidos; el conflicto político posterior tiene otro mapa local. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.persona-outro / after fact-outro | imperial-clerk | All three posts are fed. I can say that plainly. I cannot say the same plain thing about agreement between people whose names I know only through surviving papers. It is a useful limit for a clerk, though not a comfortable one. | Los tres puestos están alimentados. Puedo decirlo sin rodeos. No puedo decir algo igual de sencillo del acuerdo entre personas cuyos nombres solo conozco por los papeles conservados. Es un límite útil para un escribiente, aunque no cómodo. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.05-delegate-logistics-arles.odyssey.next-episode / after persona-outro | none | Continue with The Field between Two Eagles. This episode does not complete the campaign. | Continúa con El campo entre dos águilas. Este episodio no termina la campaña. |

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
      "status": "reference implemented; native observers and real navigation pending"
    }
  ],
  "artDirection": {
    "style": "sober late Roman local working districts and ordinary hospitality",
    "historicalControls": "fictional work courts, not a reconstructed hearing room or council basilica; modern theatre/arena conservation and Rhône bridge/tower are research context only, never exact314scene",
    "referenceAssets": [
      "arles-theatre-modern",
      "arles-amphitheatre-modern",
      "arles-rhone-modern"
    ],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "all three distinct posts require actual visits",
      "100-wood payment requires40/30/30 receiver allocation once",
      "all six helpers have individual assigned destinations; putting all six at one post fails",
      "all three food receivers require 120 each; total 360 at one receiver fails",
      "optional household aid cannot pay main post allocations",
      "three notes remain distinct and cannot be replaced by copies",
      "one working output cannot generate before its own exact o4 payment or be delivered before generation",
      "no historical Chrestus unit or guessed council venue",
      "no Constantine personal presence inferred from the modern summary",
      "no universal Pascha agreement or enforcement proved by successful local logistics",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
