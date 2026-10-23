# 13. Stone above the Old City

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `13-finite-works-logistics-jerusalem` · 326–330 CE; individual works dates qualified · 400×400

## Historical frame and fixed outcome

EN: Eusebius attributes Jerusalem church works to Constantine and transmits requests for workers and materials. He does not give their exact start year. This episode uses a fictional preparatory work circuit within an editorial 326–330 frame; it does not complete the complex or stage its later dedication. The source’s sacred identification remains attributed, and archaeological phases are not all contemporary.

ES: Eusebio atribuye obras eclesiales de Jerusalén a Constantino y transmite peticiones de trabajadores y materiales. No da su año exacto de inicio. Este episodio usa un circuito ficticio de preparación dentro de un marco editorial de 326–330; no completa el complejo ni representa su dedicación posterior. La identificación sagrada de la fuente permanece atribuida y las fases arqueológicas no son todas contemporáneas.

EN: The fictional preparation is complete; it certifies no finished basilica, Rotunda, sacred discovery or exact ancient workforce. The historical building process continued beyond this frame. The next episode turns to the new imperial city.

ES: La preparación ficticia está completada; no acredita una basílica o Rotonda terminadas, un hallazgo sagrado ni una plantilla antigua exacta. El proceso histórico de obras continuó más allá de este marco. El próximo episodio se dirige a la nueva ciudad imperial.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "Eusebius reports Constantine’s patronage, work orders and requests for labor and materials at Jerusalem. The precise commencement year is not stated; the 326–330 preparation window is editorial. Site identification remains attributed and later building phases stay separate.",
        "es-ES": "Eusebio refiere patrocinio de Constantino, órdenes de obra y peticiones de trabajadores y materiales en Jerusalén. No indica el año exacto de inicio; el marco de preparación 326–330 es editorial. La identificación del lugar permanece atribuida y las fases de obras posteriores se mantienen separadas."
      },
      "architectCorrection": {
        "date": "2026-10-14",
        "author": "gpt-6",
        "approval": "independent review pending",
        "reason": "Read Eusebius III.25–40 and current institutional preliminary archaeology; isolate a fictional preparatory works slice inside the editorial 326–330 frame, without assigning an exact start or completed rotunda."
      }
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/25023.htm",
      "passage": "Eusebius VC III.25–40 checked for imperial church-building at Jerusalem.",
      "limitations": "Eusebius is a Christian panegyrist; source establishes patronage and his identification, not independent proof of the biblical site or the exact dating of each work.",
      "status": "consulted",
      "supportedClaim": "Supports Constantine’s sponsored construction at Jerusalem, including the church complex associated with the tomb of Jesus in Eusebius’ account. / Respalda el patrocinio de construcciones constantinianas en Jerusalén, incluido el complejo asociado al sepulcro según Eusebio.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "VC III.25–40 read in relevant sections.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/25023.htm",
      "passage": "VC III.25–40, especially letter III.30–32",
      "coverageActuallyRead": "Architect read this complete chapter span; source is translated literary testimony, not field geometry.",
      "limitations": "Panegyric attributes patronage and requests for workers/materials. Exact commencement year, construction log and quantities absent. Site identification and cult motives remain attributed; no Helena or Cross discovery in this span.",
      "consultationDate": "2026-10-13",
      "approval": "independent review pending"
    },
    {
      "consultedUrl": "https://hadashot.iaa.org.il/Report_Detail_Eng.aspx?id=26542",
      "passage": "Stasolla preliminary report published 1 September 2024, 2022 excavation; pre-Christian and early-Christian phases",
      "coverageActuallyRead": "Architect read report page, particularly quarry, topography, phased building, reused stone and later coin contexts; no image geometry certified.",
      "limitations": "Small sampled areas, preliminary interpretation; fourth-century remains include later decades and cannot be flattened into a 326–330 complex. No independent verification of sacred identification.",
      "consultationDate": "2026-10-13",
      "approval": "independent review pending"
    },
    {
      "consultedUrl": "https://www.custodia.org/wp-content/uploads/2024/11/Comunicato.pdf",
      "passage": "Sapienza preliminary November2024 report, Italian pp.1–3 and English pp.4–6",
      "coverageActuallyRead": "Architect read displayed bilingual report; no ancient plan reconstructed from it.",
      "limitations": "Preliminary phases include end-fourth-century Rotunda work. Cult structure interpretation differs from an earlier reconstruction; its footprint/identity and exact phase require separate review. Figures/translation not copied into production.",
      "consultationDate": "2026-10-13",
      "approval": "independent review pending"
    },
    {
      "consultedUrl": "https://www.custodia.org/en/news/excavations-at-the-holy-sepulcher-the-first-volume-of-the-hagia-polis-project-at-sapienza-university/",
      "passage": "19 September2026 volume presentation announcement",
      "coverageActuallyRead": "Architect read announcement, not the full Hagia Polis volume.",
      "limitations": "Publication existence and project status only; no detailed plans or new dating inferred from unread book. Explicit image/text reuse restrictions remain respected.",
      "consultationDate": "2026-10-13",
      "approval": "independent review pending"
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

EN: Inspect the disclosed work reception and northern account shelter. Identify the three original stone loads, two timber loads and two binder loads at their separate stock yards.

ES: Inspecciona la recepción de obras y el refugio septentrional de cuentas indicados. Identifica las tres remesas originales de piedra, dos de madera y dos de aglutinante en sus patios de reserva separados.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "area-state",
      "requiredCount": 2,
      "state": "visited-and-passable",
      "blockingEnemies": [],
      "id": "req-1",
      "zones": [
        "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.destination-5"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 3,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-3"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-2"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "collected",
      "id": "req-4",
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-2"
      ],
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both work districts and all seven original load identities are registered.

ES: Ambos distritos de trabajo y las siete identidades originales de remesa están registrados.

EN: Count the loads before naming the building.

ES: Cuenta las remesas antes de dar nombre al edificio.

### o2 / phase-2

EN: Bring all three original stone loads to work reception and pay its 120 stone and 60 wood foundation-preparation allocation once.

ES: Lleva las tres remesas originales de piedra a recepción de obras y paga una vez su asignación de preparación de cimientos: 120 de piedra y 60 de madera.

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
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-3"
      ],
      "destinations": {
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-1": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-2": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-3": "imperial-church.13-finite-works-logistics-jerusalem.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "stone": 120,
        "wood": 60
      },
      "id": "req-2",
      "receivingZones": [
        "imperial-church.13-finite-works-logistics-jerusalem.destination-2"
      ],
      "allocations": {
        "imperial-church.13-finite-works-logistics-jerusalem.destination-2": {
          "stone": 120,
          "wood": 60
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.13-finite-works-logistics-jerusalem.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three stone-load proxies arrived and the foundation-preparation budget was funded once. No finished structure is certified.

ES: Llegaron tres remesas representadas de piedra y se financió una vez la preparación de cimientos. No acredita una estructura terminada.

EN: The receipt has a weight. It has no dome.

ES: El recibo tiene peso. No tiene cúpula.

### o3 / phase-3

EN: Bring both original timber loads to the same work reception and pay 180 wood for its separate timber-and-scaffold preparation.

ES: Lleva ambas remesas originales de madera a la misma recepción de obras y paga 180 de madera por su preparación separada de madera y andamios.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-2"
      ],
      "destinations": {
        "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-1": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-2": "imperial-church.13-finite-works-logistics-jerusalem.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 180
      },
      "id": "req-2",
      "receivingZones": [
        "imperial-church.13-finite-works-logistics-jerusalem.destination-2"
      ],
      "allocations": {
        "imperial-church.13-finite-works-logistics-jerusalem.destination-2": {
          "wood": 180
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.13-finite-works-logistics-jerusalem.o3.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The two timber loads and their separate timber allocation are recorded.

ES: Quedan registradas las dos remesas de madera y su asignación maderera separada.

EN: A column’s beauty never relieved a worker of finding somewhere to stand.

ES: La belleza de una columna nunca libró a un trabajador de buscar dónde apoyarse.

### o4 / phase-4

EN: Bring both original binder loads and all six original workers to work reception. Pay its 180 food and 40 gold work-preparation allocation once.

ES: Lleva las dos remesas originales de aglutinante y los seis trabajadores originales a recepción de obras. Paga una vez su asignación de preparación del trabajo: 180 de alimento y 40 de oro.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "entity-state",
      "requiredCount": 2,
      "state": "arrived",
      "id": "req-1",
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-2"
      ],
      "destinations": {
        "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-1": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-2": "imperial-church.13-finite-works-logistics-jerusalem.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-3",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-4",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-5",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-6"
      ],
      "destinations": {
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-1": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-2": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-3": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-4": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-5": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-6": "imperial-church.13-finite-works-logistics-jerusalem.destination-2"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 180,
        "gold": 40
      },
      "id": "req-3",
      "receivingZones": [
        "imperial-church.13-finite-works-logistics-jerusalem.destination-2"
      ],
      "allocations": {
        "imperial-church.13-finite-works-logistics-jerusalem.destination-2": {
          "food": 180,
          "gold": 40
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.13-finite-works-logistics-jerusalem.o4.req-3.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The seven load proxies and six original workers completed this finite preparatory circuit. The historical complex remains under construction.

ES: Las siete remesas representadas y los seis trabajadores originales completaron este circuito finito de preparación. El complejo histórico sigue en construcción.

EN: Six names, not six empty places in an account.

ES: Seis nombres, no seis lugares vacíos en una cuenta.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/13-finite-works-logistics-jerusalem.svg)

```json
{
  "bbox": [
    35.213,
    31.771,
    35.235,
    31.794
  ],
  "terrainProfile": "jerusalem",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        120.5,
        98.82
      ],
      "lonLat": [
        35.218,
        31.789
      ],
      "name": {
        "en": "Fictional northwestern material staging yard",
        "es-ES": "Patio ficticio noroccidental de preparación de materiales"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        225.83,
        253.71
      ],
      "lonLat": [
        35.226,
        31.779
      ],
      "name": {
        "en": "Fictional work reception west of the monument district",
        "es-ES": "Recepción ficticia de obras al oeste del distrito monumental"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        304.83,
        114.31
      ],
      "lonLat": [
        35.232,
        31.788
      ],
      "name": {
        "en": "Fictional northeastern timber receiving stock",
        "es-ES": "Reserva ficticia nororiental de recepción de madera"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        173.17,
        331.16
      ],
      "lonLat": [
        35.222,
        31.774
      ],
      "name": {
        "en": "Fictional southern binder preparation yard",
        "es-ES": "Patio ficticio meridional de preparación de aglutinante"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        239.0,
        52.35
      ],
      "lonLat": [
        35.227,
        31.792
      ],
      "name": {
        "en": "Fictional northern work and account shelter",
        "es-ES": "Refugio ficticio septentrional de trabajo y cuentas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "western-work-approach",
      "hubOrder": [
        "hub-1",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "northern-stock-loop",
      "hubOrder": [
        "hub-1",
        "hub-5",
        "hub-3",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "southern-binder-link",
      "hubOrder": [
        "hub-4",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "western-supply-alternative",
      "hubOrder": [
        "hub-1",
        "hub-4",
        "hub-2"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "northern-account-return",
      "hubOrder": [
        "hub-2",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 8
    }
  ],
  "terrainInstructions": "Local northwestern Aelia Capitolina/Jerusalem plateau, west of the Kidron valley and Temple platform. Quarried limestone, uneven work ground and sparse Mediterranean gardens; not a flat desert or tropical forest. Kidron is a valley, not a navigable river, and mostly off-frame. The receiving yard is fictional and does not locate the ancient church boundary. Exact quarry cuts, Roman street alignment, local drainage and slopes require dated footprints/DEM; modern Old City lanes, Ottoman walls, Dome of the Rock and medieval Holy Sepulchre fabric are excluded. No complete fourth-century Rotunda at this early works phase.",
  "corridorStraightLengthsTiles": {
    "western-work-approach": 187.31,
    "northern-stock-loop": 377.92,
    "southern-binder-link": 93.66,
    "western-supply-alternative": 331.89,
    "northern-account-return": 201.79
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
  "asset": "docs/design/maps/imperial-church/odyssey/13-finite-works-logistics-jerusalem.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-1",
      "role": "fictional-local-material-load-proxy",
      "initialHub": "hub-1",
      "offsetTiles": [
        -14,
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-2",
      "role": "fictional-local-material-load-proxy",
      "initialHub": "hub-1",
      "offsetTiles": [
        -12,
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-3",
      "role": "fictional-local-material-load-proxy",
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-1",
      "role": "fictional-local-material-load-proxy",
      "initialHub": "hub-3",
      "offsetTiles": [
        0,
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-2",
      "role": "fictional-local-material-load-proxy",
      "initialHub": "hub-3",
      "offsetTiles": [
        2,
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-1",
      "role": "fictional-local-material-load-proxy",
      "initialHub": "hub-4",
      "offsetTiles": [
        14,
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-2",
      "role": "fictional-local-material-load-proxy",
      "initialHub": "hub-4",
      "offsetTiles": [
        16,
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-1",
      "role": "fictional-local-worker",
      "initialHub": "hub-1",
      "offsetTiles": [
        -14,
        22
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-2",
      "role": "fictional-local-worker",
      "initialHub": "hub-1",
      "offsetTiles": [
        -12,
        22
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-3",
      "role": "fictional-local-worker",
      "initialHub": "hub-1",
      "offsetTiles": [
        -10,
        22
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-4",
      "role": "fictional-local-worker",
      "initialHub": "hub-1",
      "offsetTiles": [
        -8,
        22
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-5",
      "role": "fictional-local-worker",
      "initialHub": "hub-1",
      "offsetTiles": [
        -14,
        24
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-6",
      "role": "fictional-local-worker",
      "initialHub": "hub-1",
      "offsetTiles": [
        -12,
        24
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
      "id": "imperial-church.13-finite-works-logistics-jerusalem.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.13-finite-works-logistics-jerusalem.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.13-finite-works-logistics-jerusalem.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.13-finite-works-logistics-jerusalem.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.13-finite-works-logistics-jerusalem.destination-5",
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
    "original-stone-loads": [
      "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-1",
      "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-2",
      "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-3"
    ],
    "original-timber-loads": [
      "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-1",
      "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-2"
    ],
    "original-binder-loads": [
      "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-1",
      "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-2"
    ],
    "original-work-team": [
      "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-1",
      "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-2",
      "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-3",
      "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-4",
      "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-5",
      "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-6"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-stone-loads-3"
      ],
      "minimumAliveOrAlreadySafe": 3
    },
    {
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-timber-loads-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    },
    {
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-binder-loads-2"
      ],
      "minimumAliveOrAlreadySafe": 2
    },
    {
      "entities": [
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-1",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-2",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-3",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-4",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-5",
        "imperial-church.13-finite-works-logistics-jerusalem.original-work-team-6"
      ],
      "minimumAliveOrAlreadySafe": 6
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Plateau work viewpoints / Miradores de trabajo de la meseta

EN: Scout both marked viewpoints of plateau work viewpoints. Benefit: Mark the proposed northern-stock-loop once; main stock yards and receivers remain disclosed without this task.

ES: Explora los dos miradores señalados de miradores de trabajo de la meseta. Ventaja: Señala una vez northern-stock-loop propuesto; los patios principales y receptores siguen indicados sin esta tarea.

EN: Two observations mark stock approaches without claiming an excavated road or miraculous site proof.

ES: Dos observaciones señalan accesos a reservas sin acreditar una vía excavada ni probar un lugar milagroso.

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
          "13-finite-works-logistics-jerusalem.side-1.zone-1",
          "13-finite-works-logistics-jerusalem.side-1.zone-2"
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
        "id": "13-finite-works-logistics-jerusalem.side-1.zone-1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "13-finite-works-logistics-jerusalem.side-1.zone-2",
        "hub": "hub-4",
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
      "target": "northern-stock-loop plateau approach",
      "resources": {},
      "onceFlag": "13-finite-works-logistics-jerusalem.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "northern-stock-loop"
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
      "western-work-approach",
      "northern-stock-loop",
      "southern-binder-link",
      "western-supply-alternative",
      "northern-account-return"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Distinct labor and material lists / Listas distintas de trabajadores y materiales

EN: Recover both separate copies from distinct labor and material lists and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de listas distintas de trabajadores y materiales y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Fictional copies explain why the source’s requests do not give this exact workforce or start date.

ES: Copias ficticias explican por qué las peticiones de la fuente no dan esta plantilla exacta ni la fecha de inicio.

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
          "13-finite-works-logistics-jerusalem.side-2.entity-1",
          "13-finite-works-logistics-jerusalem.side-2.entity-2"
        ],
        "destinations": {
          "13-finite-works-logistics-jerusalem.side-2.entity-1": "13-finite-works-logistics-jerusalem.side-2.zone-1",
          "13-finite-works-logistics-jerusalem.side-2.entity-2": "13-finite-works-logistics-jerusalem.side-2.zone-1"
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
        "id": "13-finite-works-logistics-jerusalem.side-2.entity-1",
        "role": "copy",
        "initialHub": "hub-5",
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
        "id": "13-finite-works-logistics-jerusalem.side-2.entity-2",
        "role": "copy",
        "initialHub": "hub-5",
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
        "id": "13-finite-works-logistics-jerusalem.side-2.zone-1",
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
      "kind": "unlock-context-and-hint",
      "target": "documented context and a main-goal hint",
      "resources": {},
      "onceFlag": "13-finite-works-logistics-jerusalem.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.13-finite-works-logistics-jerusalem"
      ],
      "historicalNote": {
        "en": "Eusebius attributes Jerusalem church works to Constantine and transmits requests for workers and materials. He does not give their exact start year. This episode uses a fictional preparatory work circuit within an editorial 326–330 frame; it does not complete the complex or stage its later dedication. The source’s sacred identification remains attributed, and archaeological phases are not all contemporary.",
        "es-ES": "Eusebio atribuye obras eclesiales de Jerusalén a Constantino y transmite peticiones de trabajadores y materiales. No da su año exacto de inicio. Este episodio usa un circuito ficticio de preparación dentro de un marco editorial de 326–330; no completa el complejo ni representa su dedicación posterior. La identificación sagrada de la fuente permanece atribuida y las fases arqueológicas no son todas contemporáneas."
      },
      "hint": {
        "en": "Inspect the disclosed work reception and northern account shelter. Identify the three original stone loads, two timber loads and two binder loads at their separate stock yards.",
        "es-ES": "Inspecciona la recepción de obras y el refugio septentrional de cuentas indicados. Identifica las tres remesas originales de piedra, dos de madera y dos de aglutinante en sus patios de reserva separados."
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
    "originHub": "hub-5",
    "receivingHub": "hub-2",
    "corridorIds": [
      "western-work-approach",
      "northern-stock-loop",
      "southern-binder-link",
      "western-supply-alternative",
      "northern-account-return"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Quarry-side households / Hogares próximos a la cantera

EN: Bring each of the two aid crates to its assigned household at quarry-side households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares próximos a la cantera. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Voluntary aid stays separate from removal of cult buildings or religious compliance.

ES: La ayuda voluntaria permanece separada de retirar edificios de culto o del cumplimiento religioso.

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
          "13-finite-works-logistics-jerusalem.side-3.entity-1",
          "13-finite-works-logistics-jerusalem.side-3.entity-2"
        ],
        "destinations": {
          "13-finite-works-logistics-jerusalem.side-3.entity-1": "13-finite-works-logistics-jerusalem.side-3.zone-1",
          "13-finite-works-logistics-jerusalem.side-3.entity-2": "13-finite-works-logistics-jerusalem.side-3.zone-2"
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
        "id": "13-finite-works-logistics-jerusalem.side-3.entity-1",
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
        "id": "13-finite-works-logistics-jerusalem.side-3.entity-2",
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
        "id": "13-finite-works-logistics-jerusalem.side-3.zone-1",
        "hub": "hub-4",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "13-finite-works-logistics-jerusalem.side-3.zone-2",
        "hub": "hub-4",
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
      "onceFlag": "13-finite-works-logistics-jerusalem.side-3.rewarded",
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
    "receivingHub": "hub-4",
    "corridorIds": [
      "western-work-approach",
      "northern-stock-loop",
      "southern-binder-link",
      "western-supply-alternative",
      "northern-account-return"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Northern tool store / Almacén septentrional de herramientas

EN: Pay 50 wood and restore the damaged store of northern tool store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén septentrional de herramientas. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: One ordinary tool-store repair supplies finite stock; it is not church construction or a sacred-site discovery.

ES: Una reparación ordinaria de almacén de herramientas aporta reserva finita; no es construir la iglesia ni descubrir un lugar sagrado.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "13-finite-works-logistics-jerusalem.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "13-finite-works-logistics-jerusalem.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "13-finite-works-logistics-jerusalem.side-4.payment",
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
        "id": "13-finite-works-logistics-jerusalem.side-4.entity-1",
        "role": "repair",
        "initialHub": "hub-5",
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
        "id": "13-finite-works-logistics-jerusalem.side-4.zone-1",
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
      "onceFlag": "13-finite-works-logistics-jerusalem.side-4.rewarded",
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
    "originHub": "hub-5",
    "receivingHub": "hub-2",
    "corridorIds": [
      "western-work-approach",
      "northern-stock-loop",
      "southern-binder-link",
      "western-supply-alternative",
      "northern-account-return"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Local supply consignment / Remesa local de suministros

EN: Escort the trader of local supply consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de remesa local de suministros hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A fictional finite purchase supports the work circuit without asserting an ancient price list.

ES: Una compra ficticia finita apoya el circuito sin afirmar una lista antigua de precios.

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
          "13-finite-works-logistics-jerusalem.side-5.entity-1"
        ],
        "destinations": {
          "13-finite-works-logistics-jerusalem.side-5.entity-1": "13-finite-works-logistics-jerusalem.side-5.zone-1"
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
        "receipt": "13-finite-works-logistics-jerusalem.side-5.payment",
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
        "id": "13-finite-works-logistics-jerusalem.side-5.entity-1",
        "role": "trade",
        "initialHub": "hub-3",
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
        "id": "13-finite-works-logistics-jerusalem.side-5.zone-1",
        "hub": "hub-4",
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
      "onceFlag": "13-finite-works-logistics-jerusalem.side-5.rewarded",
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
    "receivingHub": "hub-4",
    "corridorIds": [
      "western-work-approach",
      "northern-stock-loop",
      "southern-binder-link",
      "western-supply-alternative",
      "northern-account-return"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Western work-path guide / Guía occidental de accesos a las obras

EN: Escort the local guide of western work-path guide to the marked road junction. Benefit: Mark the proposed western-supply-alternative once; main stock yards and receivers remain disclosed without this task.

ES: Escolta al guía local de guía occidental de accesos a las obras hasta el cruce señalado. Ventaja: Señala una vez western-supply-alternative propuesto; los patios principales y receptores siguen indicados sin esta tarea.

EN: Shows a proposed alternative on the plateau; no instant bridge, quarry flattening or ancient route certainty.

ES: Muestra una alternativa propuesta en la meseta; no da un puente instantáneo ni allana cantera ni acredita una vía antigua.

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
          "13-finite-works-logistics-jerusalem.side-6.entity-1"
        ],
        "destinations": {
          "13-finite-works-logistics-jerusalem.side-6.entity-1": "13-finite-works-logistics-jerusalem.side-6.zone-1"
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
        "id": "13-finite-works-logistics-jerusalem.side-6.entity-1",
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
        "id": "13-finite-works-logistics-jerusalem.side-6.zone-1",
        "hub": "hub-4",
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
      "target": "western-supply-alternative plateau approach",
      "resources": {},
      "onceFlag": "13-finite-works-logistics-jerusalem.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "western-supply-alternative"
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
    "receivingHub": "hub-4",
    "corridorIds": [
      "western-work-approach",
      "northern-stock-loop",
      "southern-binder-link",
      "western-supply-alternative",
      "northern-account-return"
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
      "id": "parallel-staging",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Split ordinary collection/gathering teams among three origins and stage later loads before their active delivery phase; every cost stays disclosed.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "records-and-tools",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Spend a work detour and 50 wood to gain a context note and finite material stock; no cheaper invented construction stage.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "household-and-supply",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Voluntary aid and a 50-gold consignment provide bounded supplies; optional failure never closes ordinary gathering access.",
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
      "wood": 184,
      "gold": 103,
      "stone": 92
    },
    "gatherableBank": {
      "food": 1298,
      "wood": 936,
      "gold": 227,
      "stone": 208
    },
    "mandatoryDeliveries": {
      "food": 180,
      "wood": 240,
      "gold": 40,
      "stone": 120
    },
    "protectedRecoveryStock": {
      "food": 300,
      "wood": 200,
      "gold": 100,
      "stone": 80
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
      "food": 1250,
      "wood": 920,
      "gold": 330,
      "stone": 300
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
      "wood": 160,
      "gold": 90,
      "stone": 80
    },
    "gatherableBank": {
      "food": 1350,
      "wood": 960,
      "gold": 240,
      "stone": 220
    },
    "mandatoryDeliveries": {
      "food": 180,
      "wood": 240,
      "gold": 40,
      "stone": 120
    },
    "protectedRecoveryStock": {
      "food": 300,
      "wood": 200,
      "gold": 100,
      "stone": 80
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
      "food": 1250,
      "wood": 920,
      "gold": 330,
      "stone": 300
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
      "wood": 136,
      "gold": 76,
      "stone": 68
    },
    "gatherableBank": {
      "food": 1403,
      "wood": 984,
      "gold": 254,
      "stone": 232
    },
    "mandatoryDeliveries": {
      "food": 180,
      "wood": 240,
      "gold": 40,
      "stone": 120
    },
    "protectedRecoveryStock": {
      "food": 300,
      "wood": 200,
      "gold": 100,
      "stone": 80
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
      "food": 1250,
      "wood": 920,
      "gold": 330,
      "stone": 300
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
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.title / always | none | Stone above the Old City | Piedra sobre la ciudad antigua |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.fact-intro / intro first | collection-narrator | Eusebius attributes Jerusalem church works to Constantine and transmits requests for workers and materials. He does not give their exact start year. This episode uses a fictional preparatory work circuit within an editorial 326–330 frame; it does not complete the complex or stage its later dedication. The source’s sacred identification remains attributed, and archaeological phases are not all contemporary. | Eusebio atribuye obras eclesiales de Jerusalén a Constantino y transmite peticiones de trabajadores y materiales. No da su año exacto de inicio. Este episodio usa un circuito ficticio de preparación dentro de un marco editorial de 326–330; no completa el complejo ni representa su dedicación posterior. La identificación sagrada de la fuente permanece atribuida y las fases arqueológicas no son todas contemporáneas. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.persona-intro / after handover | imperial-clerk | The family papers reached my desk long after these first works. One page asked for fine columns. The next asked how many hands would be needed. I have learned to read the second before admiring the first. A splendid plan weighs very little; the road beneath a laden worker does not. | Los papeles familiares llegaron a mi mesa mucho después de estas primeras obras. Una página pedía columnas hermosas. La siguiente preguntaba cuántas manos harían falta. Aprendí a leer la segunda antes de admirar la primera. Un plano espléndido pesa muy poco; el camino bajo un trabajador cargado no. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.route-help / available from start; repeatable without effect | none | Inspect work reception and the account shelter, then collect the seven distinct original loads at three yards. Stage later loads early if useful. Fund the stone, timber and worker preparations separately at work reception; a stone receipt cannot pay a timber allocation. Gather the disclosed ordinary stock when starting supplies fall short. Bring the same six original workers for the final preparation. Load proxies and debited resources are separate observations: this does not prove held cargo inventory or a completed building. No enemy army or ritual is required. | Inspecciona recepción de obras y el refugio de cuentas y recoge las siete remesas originales distintas en tres patios. Prepara pronto las remesas posteriores si conviene. Financia por separado la preparación de piedra, madera y trabajadores en recepción; un recibo de piedra no paga la asignación maderera. Recoge las reservas ordinarias señaladas cuando falten suministros iniciales. Lleva a los mismos seis trabajadores originales para la preparación final. Remesas representadas y recursos pagados son observaciones separadas: no prueba inventario de carga ni un edificio terminado. No exige ejército enemigo ni ritual. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o1-goal / phase-1 active | none | Inspect the disclosed work reception and northern account shelter. Identify the three original stone loads, two timber loads and two binder loads at their separate stock yards. | Inspecciona la recepción de obras y el refugio septentrional de cuentas indicados. Identifica las tres remesas originales de piedra, dos de madera y dos de aglutinante en sus patios de reserva separados. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o1-receipt / o1 latched once | none | Both work districts and all seven original load identities are registered. | Ambos distritos de trabajo y las siete identidades originales de remesa están registrados. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o1-reaction / after o1 receipt | imperial-clerk | Count the loads before naming the building. | Cuenta las remesas antes de dar nombre al edificio. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o2-goal / phase-2 active | none | Bring all three original stone loads to work reception and pay its 120 stone and 60 wood foundation-preparation allocation once. | Lleva las tres remesas originales de piedra a recepción de obras y paga una vez su asignación de preparación de cimientos: 120 de piedra y 60 de madera. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o2-receipt / o2 latched once | none | Three stone-load proxies arrived and the foundation-preparation budget was funded once. No finished structure is certified. | Llegaron tres remesas representadas de piedra y se financió una vez la preparación de cimientos. No acredita una estructura terminada. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o2-reaction / after o2 receipt | imperial-clerk | The receipt has a weight. It has no dome. | El recibo tiene peso. No tiene cúpula. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o3-goal / phase-3 active | none | Bring both original timber loads to the same work reception and pay 180 wood for its separate timber-and-scaffold preparation. | Lleva ambas remesas originales de madera a la misma recepción de obras y paga 180 de madera por su preparación separada de madera y andamios. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o3-receipt / o3 latched once | none | The two timber loads and their separate timber allocation are recorded. | Quedan registradas las dos remesas de madera y su asignación maderera separada. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o3-reaction / after o3 receipt | imperial-clerk | A column’s beauty never relieved a worker of finding somewhere to stand. | La belleza de una columna nunca libró a un trabajador de buscar dónde apoyarse. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o4-goal / phase-4 active | none | Bring both original binder loads and all six original workers to work reception. Pay its 180 food and 40 gold work-preparation allocation once. | Lleva las dos remesas originales de aglutinante y los seis trabajadores originales a recepción de obras. Paga una vez su asignación de preparación del trabajo: 180 de alimento y 40 de oro. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o4-receipt / o4 latched once | none | The seven load proxies and six original workers completed this finite preparatory circuit. The historical complex remains under construction. | Las siete remesas representadas y los seis trabajadores originales completaron este circuito finito de preparación. El complejo histórico sigue en construcción. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.o4-reaction / after o4 receipt | imperial-clerk | Six names, not six empty places in an account. | Seis nombres, no seis lugares vacíos en una cuenta. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of plateau work viewpoints. Benefit: Mark the proposed northern-stock-loop once; main stock yards and receivers remain disclosed without this task. | Explora los dos miradores señalados de miradores de trabajo de la meseta. Ventaja: Señala una vez northern-stock-loop propuesto; los patios principales y receptores siguen indicados sin esta tarea. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-1-complete / side-1 completed | none | Plateau work viewpoints completed. Its stated benefit has been granted once. | Miradores de trabajo de la meseta: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-1-lost / side-1 failed-optional | none | Plateau work viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores de trabajo de la meseta: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from distinct labor and material lists and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de listas distintas de trabajadores y materiales y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-2-complete / side-2 completed | none | Distinct labor and material lists completed. Its stated benefit has been granted once. | Listas distintas de trabajadores y materiales: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-2-lost / side-2 failed-optional | none | Distinct labor and material lists is unavailable after the loss of its unique participant or object. The main mission continues. | Listas distintas de trabajadores y materiales: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at quarry-side households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares próximos a la cantera. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-3-complete / side-3 completed | none | Quarry-side households completed. Its stated benefit has been granted once. | Hogares próximos a la cantera: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-3-lost / side-3 failed-optional | none | Quarry-side households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares próximos a la cantera: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of northern tool store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén septentrional de herramientas. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-4-complete / side-4 completed | none | Northern tool store completed. Its stated benefit has been granted once. | Almacén septentrional de herramientas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-4-lost / side-4 failed-optional | none | Northern tool store is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén septentrional de herramientas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-5-goal / optional list from start | none | Escort the trader of local supply consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de remesa local de suministros hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-5-complete / side-5 completed | none | Local supply consignment completed. Its stated benefit has been granted once. | Remesa local de suministros: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-5-lost / side-5 failed-optional | none | Local supply consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Remesa local de suministros: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-6-goal / optional list from start | none | Escort the local guide of western work-path guide to the marked road junction. Benefit: Mark the proposed western-supply-alternative once; main stock yards and receivers remain disclosed without this task. | Escolta al guía local de guía occidental de accesos a las obras hasta el cruce señalado. Ventaja: Señala una vez western-supply-alternative propuesto; los patios principales y receptores siguen indicados sin esta tarea. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-6-complete / side-6 completed | none | Western work-path guide completed. Its stated benefit has been granted once. | Guía occidental de accesos a las obras: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.side-6-lost / side-6 failed-optional | none | Western work-path guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía occidental de accesos a las obras: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.fact-outro / victory first | collection-narrator | The fictional preparation is complete; it certifies no finished basilica, Rotunda, sacred discovery or exact ancient workforce. The historical building process continued beyond this frame. The next episode turns to the new imperial city. | La preparación ficticia está completada; no acredita una basílica o Rotonda terminadas, un hallazgo sagrado ni una plantilla antigua exacta. El proceso histórico de obras continuó más allá de este marco. El próximo episodio se dirige a la nueva ciudad imperial. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.persona-outro / after fact-outro | imperial-clerk | The lists agree at last: stone, timber, binder, six names. I shall leave a blank line for the work still ahead. It is a better ending than pretending the dust has settled. The next bundle has a city’s new name on its cover. | Las listas por fin coinciden: piedra, madera, aglutinante, seis nombres. Dejaré una línea en blanco para el trabajo pendiente. Es un final mejor que fingir que el polvo se ha asentado. El siguiente legajo lleva en la cubierta el nombre nuevo de una ciudad. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.13-finite-works-logistics-jerusalem.odyssey.next-episode / after persona-outro | none | Continue with A City beneath a New Sky. This episode does not complete the campaign. | Continúa con Una ciudad bajo un cielo nuevo. Este episodio no termina la campaña. |

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
      "status": "caption text authored; certified native Sequence Items pending"
    },
    {
      "id": "receipt-gated-ordered-departure",
      "status": "reference implemented; native observers and real navigation pending"
    }
  ],
  "artDirection": {
    "style": "sober limestone work yards, modest scaffolding context and Mediterranean gardens; only phase-reviewed ancient architecture",
    "historicalControls": "Research Roman Jerusalem SVG is a modern Hadrianic schematic, not a certified 326–330 map. No military camp, Venus attribution or street footprint accepted from the schematic alone.",
    "referenceAssets": [
      "roman-jerusalem-schematic"
    ],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "The three stone, two timber and two binder original groups cannot substitute for each other or for optional crates.",
      "All six original workers are essential; optional guide and hired side actors never fill a lost original identity.",
      "The o2 stone/wood payment, o3 timber payment and o4 food/gold payment have distinct exact receipts; one receipt never pays two allocations.",
      "Arrived load proxies and resource debits do not prove physical carrier inventory; never claim native cargo or construction completion from these predicates.",
      "Main remains feasible in each difficulty with every optional skipped and with the starting stone shortfall covered by ordinary finite gathering.",
      "No repeatable shop/restoration profit, free main replacement or time-based fake completion.",
      "Receiver radii and full-width roads avoid quarry cliffs/drainage; native relief and exact ancient roads remain required checks.",
      "No modern Dome of the Rock, Ottoman walls, Crusader church facade or completed later Rotunda in the early works phase.",
      "No Helena/Cross discovery inserted into Eusebius III.25–40, no exact start year from silence and no335 dedication in this episode.",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
