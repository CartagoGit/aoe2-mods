# 17. The Empty Appointment

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `17-rumour-and-source-investigation-constantinople` · 336 CE · 400×400

## Historical frame and fixed outcome

EN: Later church histories place Arius’s death at Constantinople before an anticipated readmission.336 is one defended chronology; Sozomen gives no numbered year and preserves competing explanations. Exact place and cause remain uncertain. This exercise tracks fictional local reports. It does not stage the death, locate its latrine or turn a religious interpretation into a verified cause.

ES: Historias eclesiásticas posteriores sitúan la muerte de Arrio en Constantinopla antes de una readmisión prevista.336 es una cronología defendida; Sozomeno no numera el año y conserva explicaciones contrapuestas. Lugar exacto y causa siguen inciertos. Este ejercicio sigue informes locales ficticios. No escenifica la muerte, localiza su letrina ni convierte una interpretación religiosa en causa acreditada.

EN: The three fictional report categories reached separate shelves and a qualified local register was preserved. No evidence score resolved Arius’s cause of death. The later literary tradition remains attributed;336 remains a defended dating. The next episode concerns Constantine’s final illness, baptism and death in 337, with Nicomedia’s suburbs reported by Eusebius.

ES: Las tres categorías ficticias de informes llegaron a estantes separados y se conservó un registro local cualificado. Ninguna puntuación de pruebas resolvió la causa de la muerte de Arrio. La tradición literaria posterior sigue atribuida;336 continúa siendo una datación defendida. El siguiente episodio trata de la enfermedad final, bautismo y muerte de Constantino en 337, con los alrededores de Nicomedia referidos por Eusebio.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "consultedUrl": "https://www.newadvent.org/fathers/26022.htm",
      "passage": "Sozomen HE II.30 (New Advent 26022), account of Arius’ death.",
      "limitations": "Sozomen presents the death as providential punishment and explicitly reports hearsay; date 336 is not established by this passage. The cited dossier URL 26023 is Book III and is wrong for II.29.",
      "status": "disputed",
      "supportedClaim": "Supports a later tradition that Arius died at Constantinople on the eve of a planned readmission. / Respalda una tradición posterior según la cual Arrio murió en Constantinopla la víspera de una readmisión prevista.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "Chapter 30 lines found/read; polemical account, not contemporary evidence.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/26022.htm",
      "passage": "SozomenHEII29–30",
      "coverageActuallyRead": "Architect directly read full displayed two chapters through ordinary HTML retrieval after browser timeout; not complete book.",
      "limitations": "Fifth-century providential author; reports competing explanations and embeds Athanasius account. Not contemporary neutral medical/venue evidence, no numbered336 date. Candidate26023 is wrong book.",
      "consultationDate": "2026-10-14",
      "approval": "independent review pending"
    },
    {
      "consultedUrl": "https://academic.oup.com/past/issue/227/1",
      "passage": "Publisher issue metadata; EllenMuehlberger2015, Past&Present227(1):3–29, DOI10.1093/pastj/gtu042",
      "coverageActuallyRead": "Architect verified author/title/pages against publisher issue. Selected indexed original-paper discussion printed13 was read; article full HTML/PDF access subsequently failed403/redirect and no full-paper consultation claimed.",
      "limitations": "Initial delegated author SarahBond was wrong and is corrected. Paper examines legendary/rumour development and later represented space; does not establish actual336 latrine coordinates or death cause. No figure/PDF copied.",
      "consultationDate": "2026-10-14",
      "approval": "independent review pending"
    },
    {
      "consultedUrl": "https://academic.oup.com/jts/article-abstract/60/1/109/1684824",
      "passage": "TimothyBarnes2009, TheExileandRecallsofArius, abstract, DOI10.1093/jts/flp003",
      "coverageActuallyRead": "Architect read publisher-indexed abstract only; full article not accessed.",
      "limitations": "Argues335 recall/336 death against earlier dating. Supports a defended chronology rather than unquestioned precise date or graphic narrative.",
      "consultationDate": "2026-10-14",
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

EN: Observe the western and eastern proposed inland approaches, collect the three distinct appointment, cancellation and interpretation contexts, and bring all originals to sorting.

ES: Observa los accesos interiores propuestos occidental y oriental, recoge los tres contextos distintos de cita, cancelación e interpretación y lleva todos los originales a clasificación.

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
        "imperial-church.17-rumour-and-source-investigation-constantinople.destination-2",
        "imperial-church.17-rumour-and-source-investigation-constantinople.destination-4"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-4",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-5",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-6",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-7",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-1"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All three exact fictional contexts reached sorting; observation did not certify a death site.

ES: Los tres contextos ficticios exactos llegaron a clasificación; la observación no acreditó un lugar de muerte.

EN: A report’s label is not its proof.

ES: La etiqueta de un informe no es su prueba.

### o2 / phase-2

EN: Pay 40 wood once at the separate-label shelving court and bring all three original contexts there. Keep appointment, cancellation and interpretation labels distinct; three copies of one category cannot substitute.

ES: Paga una vez 40 de madera en el patio de estantes de etiquetas separadas y lleva allí los tres contextos originales. Conserva distintas las etiquetas de cita, cancelación e interpretación; tres copias de una categoría no las sustituyen.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 40
      },
      "id": "req-1",
      "receivingZones": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.destination-6"
      ],
      "allocations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.destination-6": {
          "wood": 40
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.17-rumour-and-source-investigation-constantinople.o2.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-2",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-6"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-3",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-6"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-6"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: All three distinct report categories are preserved with separate labels at the shelving court. Their presence does not settle the cause of death.

ES: Las tres categorías distintas de informes se conservan con etiquetas separadas en el patio de estantes. Su presencia no resuelve la causa de muerte.

EN: Keep the cancellation separate from the explanation.

ES: Separa la cancelación de la explicación.

### o3 / phase-3

EN: Pay 80 wood and 20 gold once at sorting. Prepare a qualified local register from all three original contexts, keeping each attribution and the cause of death unresolved.

ES: Paga una vez 80 de madera y 20 de oro en clasificación. Prepara un registro local cualificado de los tres contextos originales, conservando cada atribución y dejando sin resolver la causa de muerte.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "resource-transaction",
      "amounts": {
        "wood": 80,
        "gold": 20
      },
      "id": "req-1",
      "receivingZones": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.destination-1"
      ],
      "allocations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.destination-1": {
          "wood": 80,
          "gold": 20
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.17-rumour-and-source-investigation-constantinople.o3.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1",
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1",
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1"
      ],
      "outputEntities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.qualified-local-register-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.17-rumour-and-source-investigation-constantinople.o3.req-1.paid",
          "fromObjective": "o3",
          "amounts": {
            "wood": 80,
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

EN: One paid qualified register exists; uncertainty remains fixed in its authored narration.

ES: Existe un registro cualificado financiado; su narración conserva la incertidumbre fijada.

EN: I can close a working entry and leave its cause open.

ES: Puedo cerrar un asiento de trabajo y dejar abierta su causa.

### o4 / phase-4

EN: Preserve that exact qualified register northwest. Bring the three original contexts back to sorting only after their own shelving receipts and phase-active observed departures.

ES: Conserva ese registro cualificado exacto al noroeste. Devuelve los tres contextos originales a clasificación solo tras sus propios recibos de estantes y salidas observadas con esta fase activa.

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
        "imperial-church.17-rumour-and-source-investigation-constantinople.qualified-local-register-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.qualified-local-register-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "ordered-departure",
      "receiptObjective": "o2",
      "receiptRequirement": "req-2",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-2",
      "departingEntities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-2"
      },
      "id": "req-3",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "ordered-departure",
      "receiptObjective": "o2",
      "receiptRequirement": "req-3",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-4",
      "departingEntities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-4"
      },
      "id": "req-5",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "ordered-departure",
      "receiptObjective": "o2",
      "receiptRequirement": "req-4",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-6",
      "departingEntities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-6"
      },
      "id": "req-7",
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1"
      ],
      "destinations": {
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-1"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The qualified register and three causally returned originals are preserved separately. No interpretation was selected as historical truth.

ES: El registro cualificado y los tres originales devueltos causalmente se conservan separados. Ninguna interpretación se eligió como verdad histórica.

EN: Three papers stay three papers.

ES: Tres papeles siguen siendo tres papeles.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/17-rumour-and-source-investigation-constantinople.svg)

```json
{
  "bbox": [
    28.942,
    41.0,
    28.986,
    41.029
  ],
  "terrainProfile": "constantinople",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        159.02,
        140.48
      ],
      "lonLat": [
        28.959,
        41.02
      ],
      "name": {
        "en": "Fictional inland report sorting court",
        "es-ES": "Patio ficticio interior de clasificación de informes"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        69.95,
        204.87
      ],
      "lonLat": [
        28.948,
        41.014
      ],
      "name": {
        "en": "Fictional western appointment-notice shelter",
        "es-ES": "Refugio ficticio occidental de avisos de cita"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        167.11,
        290.71
      ],
      "lonLat": [
        28.96,
        41.006
      ],
      "name": {
        "en": "Fictional southern cancellation-report yard",
        "es-ES": "Patio ficticio meridional de informes de cancelación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        296.66,
        237.06
      ],
      "lonLat": [
        28.976,
        41.011
      ],
      "name": {
        "en": "Fictional eastern interpretation-report court",
        "es-ES": "Patio ficticio oriental de informes de interpretación"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        110.44,
        97.56
      ],
      "lonLat": [
        28.953,
        41.024
      ],
      "name": {
        "en": "Fictional northwest qualified archive",
        "es-ES": "Archivo ficticio cualificado noroeste"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-6",
      "centre": [
        239.98,
        161.94
      ],
      "lonLat": [
        28.969,
        41.018
      ],
      "name": {
        "en": "Fictional central separate-label shelving",
        "es-ES": "Estantes ficticios centrales de etiquetas separadas"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "western-notice-approach",
      "hubOrder": [
        "hub-2",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "southern-cancellation-loop",
      "hubOrder": [
        "hub-3",
        "hub-6",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "eastern-interpretation-loop",
      "hubOrder": [
        "hub-4",
        "hub-6",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "northwest-qualified-archive",
      "hubOrder": [
        "hub-1",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "central-shelving-connection",
      "hubOrder": [
        "hub-1",
        "hub-6"
      ],
      "mode": "land",
      "widthTiles": 8
    }
  ],
  "terrainInstructions": "European peninsula of Constantinople, with inland ordinary report courts and work gardens. These fictional addresses do not identify Arius death site, a public latrine, forum archaeology or a private ecclesiastical hearing. All circuits remain proposed inland, with GoldenHorn north and Marmara south/Bosphorus east as regional context. Coarse modern shoreline is incomplete and is not a filled land mask; slopes, springs, water polygons and full-width streets require dated controls. Do not place any contemporary witness at a later legendary latrine. No Theodosian walls, later churches, Justinianic structures, Ottoman mosques, modern bridges or dense later neighborhoods imported. Existing Byzantine map is a mixed-period research lead only.",
  "corridorStraightLengthsTiles": {
    "western-notice-approach": 109.91,
    "southern-cancellation-loop": 231.71,
    "eastern-interpretation-loop": 177.86,
    "northwest-qualified-archive": 64.82,
    "central-shelving-connection": 83.76
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
  "asset": "docs/design/maps/imperial-church/odyssey/17-rumour-and-source-investigation-constantinople.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1",
      "role": "fictional-local-appointment-note",
      "initialHub": "hub-2",
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
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1",
      "role": "fictional-local-cancellation-note",
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
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1",
      "role": "fictional-local-attributed-interpretation",
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
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.qualified-local-register-1",
      "role": "fictional-qualified-local-register",
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
      "generationPolicy": "created once from collected inputs and explicitly declared exact payment receipts in its active phase",
      "historicalMaterialPolicy": "fictional local participants or working items; no canonical autograph, authentic quotation or independent historical witness"
    }
  ],
  "zones": [
    {
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-5",
      "hub": "hub-5",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.17-rumour-and-source-investigation-constantinople.destination-6",
      "hub": "hub-6",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    }
  ],
  "objectGroups": {
    "appointment-context": [
      "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1"
    ],
    "cancellation-context": [
      "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1"
    ],
    "interpretation-context": [
      "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1"
    ],
    "qualified-local-register": [
      "imperial-church.17-rumour-and-source-investigation-constantinople.qualified-local-register-1"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.appointment-context-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    },
    {
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.cancellation-context-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    },
    {
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.interpretation-context-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    },
    {
      "entities": [
        "imperial-church.17-rumour-and-source-investigation-constantinople.qualified-local-register-1"
      ],
      "minimumAliveOrAlreadySafe": 1
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Inland shelving approaches / Accesos interiores a los estantes

EN: Scout both marked viewpoints of inland shelving approaches. Benefit: Mark the proposed eastern-interpretation-loop once; all main receivers remain disclosed without this optional task.

ES: Explora los dos miradores señalados de accesos interiores a los estantes. Ventaja: Señala una vez eastern-interpretation-loop propuesto; todos los receptores principales siguen indicados sin este objetivo opcional.

EN: Observations mark ordinary routes, not the archaeological location of a death.

ES: Las observaciones señalan rutas ordinarias, no el lugar arqueológico de una muerte.

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
          "17-rumour-and-source-investigation-constantinople.side-1.zone-1",
          "17-rumour-and-source-investigation-constantinople.side-1.zone-2"
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
        "id": "17-rumour-and-source-investigation-constantinople.side-1.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "17-rumour-and-source-investigation-constantinople.side-1.zone-2",
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
      "target": "eastern-interpretation-loop",
      "resources": {},
      "onceFlag": "17-rumour-and-source-investigation-constantinople.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "eastern-interpretation-loop"
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
      "western-notice-approach",
      "southern-cancellation-loop",
      "eastern-interpretation-loop",
      "northwest-qualified-archive",
      "central-shelving-connection"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Attribution notes / Notas de atribución

EN: Recover both separate copies from attribution notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de notas de atribución y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: A local optional annotation distinguishes claims and interpretations without becoming another independent ancient witness.

ES: Una anotación local opcional distingue afirmaciones e interpretaciones sin convertirse en otro testigo antiguo independiente.

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
          "17-rumour-and-source-investigation-constantinople.side-2.entity-1",
          "17-rumour-and-source-investigation-constantinople.side-2.entity-2"
        ],
        "destinations": {
          "17-rumour-and-source-investigation-constantinople.side-2.entity-1": "17-rumour-and-source-investigation-constantinople.side-2.zone-1",
          "17-rumour-and-source-investigation-constantinople.side-2.entity-2": "17-rumour-and-source-investigation-constantinople.side-2.zone-1"
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
        "id": "17-rumour-and-source-investigation-constantinople.side-2.entity-1",
        "role": "copy",
        "initialHub": "hub-6",
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
        "id": "17-rumour-and-source-investigation-constantinople.side-2.entity-2",
        "role": "copy",
        "initialHub": "hub-6",
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
        "id": "17-rumour-and-source-investigation-constantinople.side-2.zone-1",
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
      "onceFlag": "17-rumour-and-source-investigation-constantinople.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.17-rumour-and-source-investigation-constantinople"
      ],
      "historicalNote": {
        "en": "Later church histories place Arius’s death at Constantinople before an anticipated readmission.336 is one defended chronology; Sozomen gives no numbered year and preserves competing explanations. Exact place and cause remain uncertain. This exercise tracks fictional local reports. It does not stage the death, locate its latrine or turn a religious interpretation into a verified cause.",
        "es-ES": "Historias eclesiásticas posteriores sitúan la muerte de Arrio en Constantinopla antes de una readmisión prevista.336 es una cronología defendida; Sozomeno no numera el año y conserva explicaciones contrapuestas. Lugar exacto y causa siguen inciertos. Este ejercicio sigue informes locales ficticios. No escenifica la muerte, localiza su letrina ni convierte una interpretación religiosa en causa acreditada."
      },
      "hint": {
        "en": "Observe the western and eastern proposed inland approaches, collect the three distinct appointment, cancellation and interpretation contexts, and bring all originals to sorting.",
        "es-ES": "Observa los accesos interiores propuestos occidental y oriental, recoge los tres contextos distintos de cita, cancelación e interpretación y lleva todos los originales a clasificación."
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
    "originHub": "hub-6",
    "receivingHub": "hub-1",
    "corridorIds": [
      "western-notice-approach",
      "southern-cancellation-loop",
      "eastern-interpretation-loop",
      "northwest-qualified-archive",
      "central-shelving-connection"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Families beside the sorting yard / Familias junto al patio de clasificación

EN: Bring each of the two aid crates to its assigned household at families beside the sorting yard. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en familias junto al patio de clasificación. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Voluntary ordinary support does not endorse a doctrinal camp or alter the death.

ES: El auxilio ordinario voluntario no respalda un bando doctrinal ni altera la muerte.

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
          "17-rumour-and-source-investigation-constantinople.side-3.entity-1",
          "17-rumour-and-source-investigation-constantinople.side-3.entity-2"
        ],
        "destinations": {
          "17-rumour-and-source-investigation-constantinople.side-3.entity-1": "17-rumour-and-source-investigation-constantinople.side-3.zone-1",
          "17-rumour-and-source-investigation-constantinople.side-3.entity-2": "17-rumour-and-source-investigation-constantinople.side-3.zone-2"
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
        "id": "17-rumour-and-source-investigation-constantinople.side-3.entity-1",
        "role": "aid",
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
        "id": "17-rumour-and-source-investigation-constantinople.side-3.entity-2",
        "role": "aid",
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
        "id": "17-rumour-and-source-investigation-constantinople.side-3.zone-1",
        "hub": "hub-5",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "17-rumour-and-source-investigation-constantinople.side-3.zone-2",
        "hub": "hub-5",
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
      "onceFlag": "17-rumour-and-source-investigation-constantinople.side-3.rewarded",
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
    "receivingHub": "hub-5",
    "corridorIds": [
      "western-notice-approach",
      "southern-cancellation-loop",
      "eastern-interpretation-loop",
      "northwest-qualified-archive",
      "central-shelving-connection"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Separate-label shelter / Refugio de etiquetas separadas

EN: Pay 50 wood and restore the damaged store of separate-label shelter to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de refugio de etiquetas separadas. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: Finite ordinary maintenance protects work stock without proving a report true.

ES: El mantenimiento ordinario finito protege existencias sin probar verdadero un informe.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "17-rumour-and-source-investigation-constantinople.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "17-rumour-and-source-investigation-constantinople.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "17-rumour-and-source-investigation-constantinople.side-4.payment",
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
        "id": "17-rumour-and-source-investigation-constantinople.side-4.entity-1",
        "role": "repair",
        "initialHub": "hub-1",
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
        "id": "17-rumour-and-source-investigation-constantinople.side-4.zone-1",
        "hub": "hub-6",
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
      "onceFlag": "17-rumour-and-source-investigation-constantinople.side-4.rewarded",
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
    "receivingHub": "hub-6",
    "corridorIds": [
      "western-notice-approach",
      "southern-cancellation-loop",
      "eastern-interpretation-loop",
      "northwest-qualified-archive",
      "central-shelving-connection"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Archival work supplies / Suministros de trabajo de archivo

EN: Escort the trader of archival work supplies to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de suministros de trabajo de archivo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: One bounded exchange supports preservation, not a purchase of credibility.

ES: Un intercambio limitado apoya conservación, no compra credibilidad.

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
          "17-rumour-and-source-investigation-constantinople.side-5.entity-1"
        ],
        "destinations": {
          "17-rumour-and-source-investigation-constantinople.side-5.entity-1": "17-rumour-and-source-investigation-constantinople.side-5.zone-1"
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
        "receipt": "17-rumour-and-source-investigation-constantinople.side-5.payment",
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
        "id": "17-rumour-and-source-investigation-constantinople.side-5.entity-1",
        "role": "trade",
        "initialHub": "hub-4",
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
        "id": "17-rumour-and-source-investigation-constantinople.side-5.zone-1",
        "hub": "hub-5",
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
      "onceFlag": "17-rumour-and-source-investigation-constantinople.side-5.rewarded",
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
    "originHub": "hub-4",
    "receivingHub": "hub-5",
    "corridorIds": [
      "western-notice-approach",
      "southern-cancellation-loop",
      "eastern-interpretation-loop",
      "northwest-qualified-archive",
      "central-shelving-connection"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Northern archive guide / Guía del archivo norte

EN: Escort the local guide of northern archive guide to the marked road junction. Benefit: Mark the proposed northwest-qualified-archive once; all main receivers remain disclosed without this optional task.

ES: Escolta al guía local de guía del archivo norte hasta el cruce señalado. Ventaja: Señala una vez northwest-qualified-archive propuesto; todos los receptores principales siguen indicados sin este objetivo opcional.

EN: Marks the local archive approach; no miracle route, hidden witness or latrine revelation.

ES: Señala el acceso al archivo local; no revela ruta milagrosa, testigo oculto ni letrina.

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
          "17-rumour-and-source-investigation-constantinople.side-6.entity-1"
        ],
        "destinations": {
          "17-rumour-and-source-investigation-constantinople.side-6.entity-1": "17-rumour-and-source-investigation-constantinople.side-6.zone-1"
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
        "id": "17-rumour-and-source-investigation-constantinople.side-6.entity-1",
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
        "id": "17-rumour-and-source-investigation-constantinople.side-6.zone-1",
        "hub": "hub-5",
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
      "target": "northwest-qualified-archive",
      "resources": {},
      "onceFlag": "17-rumour-and-source-investigation-constantinople.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "northwest-qualified-archive"
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
    "receivingHub": "hub-5",
    "corridorIds": [
      "western-notice-approach",
      "southern-cancellation-loop",
      "eastern-interpretation-loop",
      "northwest-qualified-archive",
      "central-shelving-connection"
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
      "id": "survey-and-classification",
      "optionalObjectives": [
        "side-1",
        "side-2"
      ],
      "costOfOpportunity": "Survey the two land approaches and preserve attributed categories before shelving.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "preservation-investment",
      "optionalObjectives": [
        "side-4",
        "side-5"
      ],
      "costOfOpportunity": "Reserve the120 wood/20 gold main allocations before finite shelter/procurement investments.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "households-and-guidance",
      "optionalObjectives": [
        "side-3",
        "side-6"
      ],
      "costOfOpportunity": "A separate team supports voluntary households and archive guidance while all original contexts stay mandatory.",
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
      "food": 345,
      "wood": 103,
      "gold": 69,
      "stone": 40
    },
    "gatherableBank": {
      "food": 1125,
      "wood": 857,
      "gold": 211,
      "stone": 120
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 120,
      "gold": 20,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 250,
      "wood": 160,
      "gold": 70,
      "stone": 60
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
      "food": 1020,
      "wood": 760,
      "gold": 280,
      "stone": 160
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
      "food": 300,
      "wood": 90,
      "gold": 60,
      "stone": 35
    },
    "gatherableBank": {
      "food": 1170,
      "wood": 870,
      "gold": 220,
      "stone": 125
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 120,
      "gold": 20,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 250,
      "wood": 160,
      "gold": 70,
      "stone": 60
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
      "food": 1020,
      "wood": 760,
      "gold": 280,
      "stone": 160
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
      "food": 255,
      "wood": 76,
      "gold": 51,
      "stone": 29
    },
    "gatherableBank": {
      "food": 1215,
      "wood": 884,
      "gold": 229,
      "stone": 131
    },
    "mandatoryDeliveries": {
      "food": 0,
      "wood": 120,
      "gold": 20,
      "stone": 0
    },
    "protectedRecoveryStock": {
      "food": 250,
      "wood": 160,
      "gold": 70,
      "stone": 60
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
      "food": 1020,
      "wood": 760,
      "gold": 280,
      "stone": 160
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
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.title / always | none | The Empty Appointment | La cita vacía |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.fact-intro / intro first | collection-narrator | Later church histories place Arius’s death at Constantinople before an anticipated readmission.336 is one defended chronology; Sozomen gives no numbered year and preserves competing explanations. Exact place and cause remain uncertain. This exercise tracks fictional local reports. It does not stage the death, locate its latrine or turn a religious interpretation into a verified cause. | Historias eclesiásticas posteriores sitúan la muerte de Arrio en Constantinopla antes de una readmisión prevista.336 es una cronología defendida; Sozomeno no numera el año y conserva explicaciones contrapuestas. Lugar exacto y causa siguen inciertos. Este ejercicio sigue informes locales ficticios. No escenifica la muerte, localiza su letrina ni convierte una interpretación religiosa en causa acreditada. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.persona-intro / after handover | imperial-clerk | I was too young to keep this day in memory. Father’s bundle has a meeting notice, a cancellation report and an argument somebody wanted repeated. Three papers, three different jobs. The cancellation tells me someone did not come. The argument tells me what its writer wanted the absence to mean. I will not pretend those are the same thing. | Yo era demasiado pequeño para recordar aquel día. El legajo de mi padre guarda un aviso de reunión, un informe de cancelación y un argumento que alguien quería repetir. Tres papeles, tres tareas distintas. La cancelación me dice que alguien no vino. El argumento dice qué quería su autor que significara esa ausencia. No fingiré que son lo mismo. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.route-help / available from start; repeatable without effect | none | Bring the appointment notice, cancellation report and attributed interpretation to sorting, then move all three originals to the shelving court and pay 40 wood there once. Keep their labels separate. Prepare the qualified register at sorting after its 80 wood/20 gold payment. Finally preserve it northwest, and bring the three original contexts back to sorting after each has actually left the shelving court during the return task. An early sorting visit does not complete that return. These reports do not prove a cause of death. | Lleva aviso de cita, informe de cancelación e interpretación atribuida a clasificación; traslada los tres originales al patio de estantes y paga allí una vez 40 de madera. Conserva sus etiquetas separadas. Prepara el registro cualificado en clasificación tras pagar sus 80 de madera/20 de oro. Por último, consérvalo al noroeste y devuelve los tres contextos originales a clasificación después de que cada uno haya salido realmente de los estantes durante la tarea de regreso. Una visita temprana a clasificación no completa ese regreso. Estos informes no prueban una causa de muerte. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o1-goal / phase-1 active | none | Observe the western and eastern proposed inland approaches, collect the three distinct appointment, cancellation and interpretation contexts, and bring all originals to sorting. | Observa los accesos interiores propuestos occidental y oriental, recoge los tres contextos distintos de cita, cancelación e interpretación y lleva todos los originales a clasificación. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o1-receipt / o1 latched once | none | All three exact fictional contexts reached sorting; observation did not certify a death site. | Los tres contextos ficticios exactos llegaron a clasificación; la observación no acreditó un lugar de muerte. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o1-reaction / after o1 receipt | imperial-clerk | A report’s label is not its proof. | La etiqueta de un informe no es su prueba. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o2-goal / phase-2 active | none | Pay 40 wood once at the separate-label shelving court and bring all three original contexts there. Keep appointment, cancellation and interpretation labels distinct; three copies of one category cannot substitute. | Paga una vez 40 de madera en el patio de estantes de etiquetas separadas y lleva allí los tres contextos originales. Conserva distintas las etiquetas de cita, cancelación e interpretación; tres copias de una categoría no las sustituyen. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o2-receipt / o2 latched once | none | All three distinct report categories are preserved with separate labels at the shelving court. Their presence does not settle the cause of death. | Las tres categorías distintas de informes se conservan con etiquetas separadas en el patio de estantes. Su presencia no resuelve la causa de muerte. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o2-reaction / after o2 receipt | imperial-clerk | Keep the cancellation separate from the explanation. | Separa la cancelación de la explicación. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o3-goal / phase-3 active | none | Pay 80 wood and 20 gold once at sorting. Prepare a qualified local register from all three original contexts, keeping each attribution and the cause of death unresolved. | Paga una vez 80 de madera y 20 de oro en clasificación. Prepara un registro local cualificado de los tres contextos originales, conservando cada atribución y dejando sin resolver la causa de muerte. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o3-receipt / o3 latched once | none | One paid qualified register exists; uncertainty remains fixed in its authored narration. | Existe un registro cualificado financiado; su narración conserva la incertidumbre fijada. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o3-reaction / after o3 receipt | imperial-clerk | I can close a working entry and leave its cause open. | Puedo cerrar un asiento de trabajo y dejar abierta su causa. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o4-goal / phase-4 active | none | Preserve that exact qualified register northwest. Bring the three original contexts back to sorting only after their own shelving receipts and phase-active observed departures. | Conserva ese registro cualificado exacto al noroeste. Devuelve los tres contextos originales a clasificación solo tras sus propios recibos de estantes y salidas observadas con esta fase activa. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o4-receipt / o4 latched once | none | The qualified register and three causally returned originals are preserved separately. No interpretation was selected as historical truth. | El registro cualificado y los tres originales devueltos causalmente se conservan separados. Ninguna interpretación se eligió como verdad histórica. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.o4-reaction / after o4 receipt | imperial-clerk | Three papers stay three papers. | Tres papeles siguen siendo tres papeles. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of inland shelving approaches. Benefit: Mark the proposed eastern-interpretation-loop once; all main receivers remain disclosed without this optional task. | Explora los dos miradores señalados de accesos interiores a los estantes. Ventaja: Señala una vez eastern-interpretation-loop propuesto; todos los receptores principales siguen indicados sin este objetivo opcional. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-1-complete / side-1 completed | none | Inland shelving approaches completed. Its stated benefit has been granted once. | Accesos interiores a los estantes: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-1-lost / side-1 failed-optional | none | Inland shelving approaches is unavailable after the loss of its unique participant or object. The main mission continues. | Accesos interiores a los estantes: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from attribution notes and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de notas de atribución y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-2-complete / side-2 completed | none | Attribution notes completed. Its stated benefit has been granted once. | Notas de atribución: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-2-lost / side-2 failed-optional | none | Attribution notes is unavailable after the loss of its unique participant or object. The main mission continues. | Notas de atribución: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at families beside the sorting yard. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en familias junto al patio de clasificación. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-3-complete / side-3 completed | none | Families beside the sorting yard completed. Its stated benefit has been granted once. | Familias junto al patio de clasificación: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-3-lost / side-3 failed-optional | none | Families beside the sorting yard is unavailable after the loss of its unique participant or object. The main mission continues. | Familias junto al patio de clasificación: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of separate-label shelter to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de refugio de etiquetas separadas. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-4-complete / side-4 completed | none | Separate-label shelter completed. Its stated benefit has been granted once. | Refugio de etiquetas separadas: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-4-lost / side-4 failed-optional | none | Separate-label shelter is unavailable after the loss of its unique participant or object. The main mission continues. | Refugio de etiquetas separadas: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-5-goal / optional list from start | none | Escort the trader of archival work supplies to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de suministros de trabajo de archivo hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-5-complete / side-5 completed | none | Archival work supplies completed. Its stated benefit has been granted once. | Suministros de trabajo de archivo: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-5-lost / side-5 failed-optional | none | Archival work supplies is unavailable after the loss of its unique participant or object. The main mission continues. | Suministros de trabajo de archivo: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-6-goal / optional list from start | none | Escort the local guide of northern archive guide to the marked road junction. Benefit: Mark the proposed northwest-qualified-archive once; all main receivers remain disclosed without this optional task. | Escolta al guía local de guía del archivo norte hasta el cruce señalado. Ventaja: Señala una vez northwest-qualified-archive propuesto; todos los receptores principales siguen indicados sin este objetivo opcional. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-6-complete / side-6 completed | none | Northern archive guide completed. Its stated benefit has been granted once. | Guía del archivo norte: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.side-6-lost / side-6 failed-optional | none | Northern archive guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del archivo norte: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.fact-outro / victory first | collection-narrator | The three fictional report categories reached separate shelves and a qualified local register was preserved. No evidence score resolved Arius’s cause of death. The later literary tradition remains attributed;336 remains a defended dating. The next episode concerns Constantine’s final illness, baptism and death in 337, with Nicomedia’s suburbs reported by Eusebius. | Las tres categorías ficticias de informes llegaron a estantes separados y se conservó un registro local cualificado. Ninguna puntuación de pruebas resolvió la causa de la muerte de Arrio. La tradición literaria posterior sigue atribuida;336 continúa siendo una datación defendida. El siguiente episodio trata de la enfermedad final, bautismo y muerte de Constantino en 337, con los alrededores de Nicomedia referidos por Eusebio. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.persona-outro / after fact-outro | imperial-clerk | The appointment stayed empty. I wrote down the notice, the cancellation and the interpretation without making one swallow the others. A missing name can tempt a clerk to invent a conclusion. The next bundle has an emperor’s last arrangements. There will be enough temptation there without adding our own certainty. | La cita quedó vacía. Anoté el aviso, la cancelación y la interpretación sin dejar que uno devorara a los demás. Un nombre ausente puede tentar a un escribiente a inventar una conclusión. El siguiente legajo contiene los últimos arreglos de un emperador. Habrá tentación suficiente sin añadir nuestra certeza. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.17-rumour-and-source-investigation-constantinople.odyssey.next-episode / after persona-outro | none | Continue with The Court without Its Emperor. This episode does not complete the campaign. | Continúa con La corte sin su emperador. Este episodio no termina la campaña. |

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
    "style": "restrained ordinary urban work shelves and gardens; no graphic death recreation",
    "historicalControls": "No located latrine, divine-punishment animation, medical cure or later books in336. Mixed-period city map phase-filtered only as research.",
    "referenceAssets": [
      "byzantine-constantinople-composite"
    ],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "Three copies of one interpretation cannot satisfy three distinct context categories.",
      "Visual shelf slots are not a typed per-slot predicate; do not invent native slot matching as already implemented.",
      "Derived register requires exact three collected contexts and oneo3 req1 payment;40W shelving receipt cannot substitute.",
      "Final return requires each context’s owno2 req2/3/4 receipt, never another context, and final phase observed departure.",
      "No main medical conclusion, prayer-kill, rescue-Arius condition, credibility score or death-site reveal is generated.",
      "Both route observations and all main identities/payments remain mandatory with all optional rewards skipped.",
      "Later writers/modern criticism belong to common narration and research, never physical336 objects.",
      "Marcus inherited papers, not personal eyewitness of toddler years; no direct quote claimed.",
      "Coarse peninsula shore and absent water controls are not ancient land-mask or native pathfinding proof.",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
