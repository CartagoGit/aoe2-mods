# 12. Many Voices beside the Lake

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. MiniMax cannot author this scenario until independent source approval, geographic footprint checks and its required native capabilities are closed. Static solvency does not prove difficulty or enjoyment.

CDF-C01 · `02-nicaea` · 325 CE · 400×400

## Historical frame and fixed outcome

EN: In 325 the council at Nicaea issued a creed and disciplinary canons and reported agreement on Easter. Eusebius describes imperial travel support, provision and a farewell. His praise of unity is not evidence that disputes ended. The precise meeting buildings remain uncertain. This local hospitality circuit and its six attendants are fictional; the player neither chooses doctrine nor creates a biblical canon.

ES: En 325 el concilio de Nicea emitió un credo y cánones disciplinarios y comunicó un acuerdo sobre Pascua. Eusebio describe apoyo imperial al viaje, manutención y despedida. Su elogio de la unidad no prueba que terminaran las disputas. Los edificios exactos de reunión siguen inciertos. Este circuito local de hospitalidad y sus seis asistentes son ficticios; el jugador no elige doctrina ni crea un canon bíblico.

EN: The council’s creed, disciplinary rules and reported Easter agreement remain separate historical results. The local service does not certify universal observance, determine the meeting site or end subsequent controversy. The next act follows building patronage and imperial succession.

ES: El credo, las normas disciplinarias y el acuerdo pascual comunicado permanecen como resultados históricos distintos. El servicio local no acredita observancia universal ni determina la sede ni termina la controversia posterior. El siguiente acto sigue el patrocinio de obras y la sucesión imperial.

EN: The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration.

ES: Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "The council at Nicaea in 325 issued a creed and disciplinary canons and reported a common Easter agreement. These are distinct matters; neither a biblical canon nor the creation of modern Catholic and Orthodox churches.",
        "es-ES": "El concilio de Nicea de 325 emitió un credo y cánones disciplinarios y comunicó un acuerdo sobre Pascua. Son asuntos distintos; no un canon bíblico ni la creación de las iglesias católica y ortodoxa modernas."
      },
      "architectCorrection": {
        "date": "2026-10-13",
        "author": "gpt-6",
        "approval": "independent review pending",
        "reason": "Read primary creed, disciplinary canons and synodal letter separately from Eusebius council/hospitality narrative. Council results stay attributed; building location is not resolved."
      }
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/3801.htm",
      "passage": "Nicaea page: canon 20; post-council letter paragraph on Easter (lines 93–95).",
      "limitations": "Canon 20 is not an Easter-calendar canon. The surviving letter is a post-council report; it does not supply a detailed computational rule or prove uniform compliance.",
      "status": "consulted",
      "supportedClaim": "Supports council canons including Sunday/Pentecost prayer posture and a reported agreement to celebrate Easter together. / Respalda cánones como la postura de oración en domingo/Pentecostés y un acuerdo comunicado sobre la celebración común de Pascua.",
      "consultationDate": "2026-10-12",
      "coverageActuallyRead": "Canon 20 and letter passage checked, not manuscript history.",
      "approval": "collection only; exact claim still requires architect and independent review"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/3801.htm",
      "passage": "Creed; canons 1–20, especially 4–7 and 20; synodal letter",
      "coverageActuallyRead": "Architect read the displayed creed, twenty canons and letter; no manuscript collation.",
      "limitations": "Disciplinary canons are normative, not proof of universal practice. Canon 20 concerns standing prayer, not an Easter computation. Creed of 325 is not silently replaced with the later liturgical expansion. Letter reports agreement, not an algorithm or universal compliance.",
      "consultationDate": "2026-10-13",
      "approval": "independent review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/25023.htm",
      "passage": "Eusebius VC III.6–23",
      "coverageActuallyRead": "Architect read these council, hospitality, correspondence and departure sections; not the entire book.",
      "limitations": "Pro-imperial narrative; logistical details are attributed. III.7 prayer-house and III.10 palace hall do not locate excavated buildings. Reported unanimity is rhetoric, not proof that later controversy ceased; III.23 itself reports renewed Egyptian contention. No exact guest count or cost is derived from this text.",
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

EN: Collect the three distinct local context notes and deliver each to common copying.

ES: Recoge las tres notas locales de contexto distintas y entrega cada una al taller común.

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
        "imperial-church.02-nicaea.creed-context-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-2",
      "entities": [
        "imperial-church.02-nicaea.discipline-context-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "collected",
      "id": "req-3",
      "entities": [
        "imperial-church.02-nicaea.feast-context-note-1"
      ],
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-4",
      "entities": [
        "imperial-church.02-nicaea.creed-context-note-1"
      ],
      "destinations": {
        "imperial-church.02-nicaea.creed-context-note-1": "imperial-church.02-nicaea.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-5",
      "entities": [
        "imperial-church.02-nicaea.discipline-context-note-1"
      ],
      "destinations": {
        "imperial-church.02-nicaea.discipline-context-note-1": "imperial-church.02-nicaea.destination-4"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-6",
      "entities": [
        "imperial-church.02-nicaea.feast-context-note-1"
      ],
      "destinations": {
        "imperial-church.02-nicaea.feast-context-note-1": "imperial-church.02-nicaea.destination-4"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three different subjects are ready at the workshop.

ES: Tres asuntos diferentes están preparados en el taller.

EN: A rule for prayer is not a calendar, and neither will feed a guest.

ES: Una regla de oración no es un calendario, y ninguno dará de comer a un huésped.

### o2 / phase-2

EN: Receive three original attendants at each hospitality court and fund each court with 120 food.

ES: Recibe tres asistentes originales en cada patio de hospitalidad y financia cada patio con 120 de alimento.

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
        "imperial-church.02-nicaea.original-attendants-1",
        "imperial-church.02-nicaea.original-attendants-2",
        "imperial-church.02-nicaea.original-attendants-3",
        "imperial-church.02-nicaea.original-attendants-4",
        "imperial-church.02-nicaea.original-attendants-5",
        "imperial-church.02-nicaea.original-attendants-6"
      ],
      "destinations": {
        "imperial-church.02-nicaea.original-attendants-1": "imperial-church.02-nicaea.destination-2",
        "imperial-church.02-nicaea.original-attendants-2": "imperial-church.02-nicaea.destination-2",
        "imperial-church.02-nicaea.original-attendants-3": "imperial-church.02-nicaea.destination-2",
        "imperial-church.02-nicaea.original-attendants-4": "imperial-church.02-nicaea.destination-3",
        "imperial-church.02-nicaea.original-attendants-5": "imperial-church.02-nicaea.destination-3",
        "imperial-church.02-nicaea.original-attendants-6": "imperial-church.02-nicaea.destination-3"
      },
      "oncePerEntity": true
    },
    {
      "kind": "resource-transaction",
      "amounts": {
        "food": 240
      },
      "id": "req-2",
      "receivingZones": [
        "imperial-church.02-nicaea.destination-2",
        "imperial-church.02-nicaea.destination-3"
      ],
      "allocations": {
        "imperial-church.02-nicaea.destination-2": {
          "food": 120
        },
        "imperial-church.02-nicaea.destination-3": {
          "food": 120
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.02-nicaea.o2.req-2.paid",
      "once": true,
      "atomic": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Both courts received their own three attendants and their own funded allotment.

ES: Ambos patios recibieron sus propios tres asistentes y su propia asignación financiada.

EN: Three extra people at one table cannot fill the empty places at the other.

ES: Tres personas de más en una mesa no llenan los lugares vacíos de la otra.

### o3 / phase-3

EN: Pay 90 wood and 30 gold once, prepare each notice from its own note, then deliver creed context to farewell, discipline to the southeastern receiver and feast context to the southern receiver.

ES: Paga una vez 90 de madera y 30 de oro, prepara cada aviso con su propia nota y entrega el contexto del credo en despedida, el disciplinario al receptor sudoriental y el festivo al meridional.

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
        "imperial-church.02-nicaea.destination-4"
      ],
      "allocations": {
        "imperial-church.02-nicaea.destination-4": {
          "wood": 90,
          "gold": 30
        }
      },
      "account": "spendable",
      "paidFlag": "imperial-church.02-nicaea.o3.req-1.paid",
      "once": true,
      "atomic": true
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-2",
      "inputEntities": [
        "imperial-church.02-nicaea.creed-context-note-1"
      ],
      "outputEntities": [
        "imperial-church.02-nicaea.creed-working-notice-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.02-nicaea.o3.req-1.paid",
          "fromObjective": "o3",
          "amounts": {
            "wood": 90,
            "gold": 30
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-3",
      "inputEntities": [
        "imperial-church.02-nicaea.discipline-context-note-1"
      ],
      "outputEntities": [
        "imperial-church.02-nicaea.discipline-working-notice-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.02-nicaea.o3.req-1.paid",
          "fromObjective": "o3",
          "amounts": {
            "wood": 90,
            "gold": 30
          },
          "newDebit": false
        }
      ]
    },
    {
      "kind": "derived-token",
      "once": true,
      "deriveWhen": "collected local working identities and exact funded receipt in active phase",
      "id": "req-4",
      "inputEntities": [
        "imperial-church.02-nicaea.feast-context-note-1"
      ],
      "outputEntities": [
        "imperial-church.02-nicaea.feast-working-notice-1"
      ],
      "requiredPaymentReceipts": [
        {
          "flag": "imperial-church.02-nicaea.o3.req-1.paid",
          "fromObjective": "o3",
          "amounts": {
            "wood": 90,
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
      "id": "req-5",
      "entities": [
        "imperial-church.02-nicaea.creed-working-notice-1"
      ],
      "destinations": {
        "imperial-church.02-nicaea.creed-working-notice-1": "imperial-church.02-nicaea.destination-1"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-6",
      "entities": [
        "imperial-church.02-nicaea.discipline-working-notice-1"
      ],
      "destinations": {
        "imperial-church.02-nicaea.discipline-working-notice-1": "imperial-church.02-nicaea.destination-5"
      },
      "oncePerEntity": true
    },
    {
      "kind": "entity-state",
      "requiredCount": 1,
      "state": "arrived",
      "id": "req-7",
      "entities": [
        "imperial-church.02-nicaea.feast-working-notice-1"
      ],
      "destinations": {
        "imperial-church.02-nicaea.feast-working-notice-1": "imperial-church.02-nicaea.destination-6"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: Three different notices reached their assigned receivers; the workshop payment was charged once.

ES: Tres avisos diferentes llegaron a sus receptores asignados; el taller cobró el pago una vez.

EN: The labels are modest. That leaves less room for a splendid mistake.

ES: Las etiquetas son modestas. Así queda menos sitio para un error espléndido.

### o4 / phase-4

EN: After each original attendant’s own hospitality receipt, observe their departures and bring those same six attendants to the farewell yard.

ES: Tras el recibo propio de hospitalidad de cada asistente original, observa sus salidas y lleva a esos mismos seis asistentes al patio de despedida.

```json
{
  "operator": "all",
  "requirements": [
    {
      "kind": "ordered-departure",
      "receiptObjective": "o2",
      "receiptRequirement": "req-1",
      "departureEnabledOnlyAfterReceipt": true,
      "id": "req-1",
      "departingEntities": [
        "imperial-church.02-nicaea.original-attendants-1",
        "imperial-church.02-nicaea.original-attendants-2",
        "imperial-church.02-nicaea.original-attendants-3",
        "imperial-church.02-nicaea.original-attendants-4",
        "imperial-church.02-nicaea.original-attendants-5",
        "imperial-church.02-nicaea.original-attendants-6"
      ]
    },
    {
      "kind": "entity-state",
      "requiredCount": 6,
      "state": "arrived",
      "arrivalAfterDeparture": {
        "objective": "o4",
        "requirement": "req-1"
      },
      "id": "req-2",
      "entities": [
        "imperial-church.02-nicaea.original-attendants-1",
        "imperial-church.02-nicaea.original-attendants-2",
        "imperial-church.02-nicaea.original-attendants-3",
        "imperial-church.02-nicaea.original-attendants-4",
        "imperial-church.02-nicaea.original-attendants-5",
        "imperial-church.02-nicaea.original-attendants-6"
      ],
      "destinations": {
        "imperial-church.02-nicaea.original-attendants-1": "imperial-church.02-nicaea.destination-1",
        "imperial-church.02-nicaea.original-attendants-2": "imperial-church.02-nicaea.destination-1",
        "imperial-church.02-nicaea.original-attendants-3": "imperial-church.02-nicaea.destination-1",
        "imperial-church.02-nicaea.original-attendants-4": "imperial-church.02-nicaea.destination-1",
        "imperial-church.02-nicaea.original-attendants-5": "imperial-church.02-nicaea.destination-1",
        "imperial-church.02-nicaea.original-attendants-6": "imperial-church.02-nicaea.destination-1"
      },
      "oncePerEntity": true
    }
  ],
  "neverUseTimerInstead": true
}
```

EN: The six original attendants reached farewell after their own hosted-court departures.

ES: Los seis asistentes originales llegaron a despedida tras sus propias salidas de los patios de acogida.

EN: They may leave with different opinions. My list needs their names, not one borrowed voice.

ES: Pueden marcharse con opiniones distintas. Mi lista necesita sus nombres, no una sola voz prestada.

## Geographic districts and routes

[Own geographic control plan](../../../../design/maps/imperial-church/odyssey/02-nicaea.svg)

```json
{
  "bbox": [
    29.708,
    40.407,
    29.763,
    40.455
  ],
  "terrainProfile": "nicaea",
  "orientation": "north-up; AoE2 camera calibration separate; never mirror banks",
  "projection": "WGS84, cosine-corrected longitude, square padding",
  "hubs": [
    {
      "id": "hub-1",
      "centre": [
        213.62,
        73.33
      ],
      "lonLat": [
        29.738,
        40.448
      ],
      "name": {
        "en": "Fictional northeastern arrival and farewell yard",
        "es-ES": "Patio ficticio nororiental de llegada y despedida"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-2",
      "centre": [
        134.53,
        125.28
      ],
      "lonLat": [
        29.724,
        40.441
      ],
      "name": {
        "en": "Fictional northwestern hospitality court",
        "es-ES": "Patio ficticio noroccidental de hospitalidad"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-3",
      "centre": [
        270.12,
        117.86
      ],
      "lonLat": [
        29.748,
        40.442
      ],
      "name": {
        "en": "Fictional eastern hospitality court",
        "es-ES": "Patio ficticio oriental de hospitalidad"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-4",
      "centre": [
        219.27,
        206.92
      ],
      "lonLat": [
        29.739,
        40.43
      ],
      "name": {
        "en": "Local common copying workshop",
        "es-ES": "Taller local común de copias"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-5",
      "centre": [
        275.77,
        288.56
      ],
      "lonLat": [
        29.749,
        40.419
      ],
      "name": {
        "en": "Fictional southeastern disciplinary notice receiver",
        "es-ES": "Receptor ficticio sudoriental del aviso disciplinario"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    },
    {
      "id": "hub-6",
      "centre": [
        151.48,
        318.25
      ],
      "lonLat": [
        29.727,
        40.415
      ],
      "name": {
        "en": "Fictional southern feast notice receiver",
        "es-ES": "Receptor ficticio meridional del aviso festivo"
      },
      "radiusTiles": 12,
      "certainty": "architect fictional activity district within real geography; footprint pending"
    }
  ],
  "corridors": [
    {
      "id": "western-host-loop",
      "hubOrder": [
        "hub-1",
        "hub-2",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "eastern-host-loop",
      "hubOrder": [
        "hub-1",
        "hub-3",
        "hub-4"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "common-farewell-link",
      "hubOrder": [
        "hub-4",
        "hub-1"
      ],
      "mode": "land",
      "widthTiles": 10
    },
    {
      "id": "southern-notice-loop",
      "hubOrder": [
        "hub-4",
        "hub-6",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 8
    },
    {
      "id": "eastern-notice-loop",
      "hubOrder": [
        "hub-4",
        "hub-3",
        "hub-5"
      ],
      "mode": "land",
      "widthTiles": 8
    }
  ],
  "terrainInstructions": "Eastern Ascanian/Iznik lake city and cultivated lowland frame. Every fictional activity court and land circuit stays east of the schematic lake outline. No mandatory boat journey or harbor crossing. The exact palace, prayer-house, submerged basilica and 325 shore are unresolved. Do not reproduce modern shore fill/park, Ottoman tile kilns or mosques, later gate fabric or medieval fortification phases as 325. Period structures and peripheral relief require dated evidence and native footprint/DEM checks.",
  "corridorStraightLengthsTiles": {
    "western-host-loop": 212.29,
    "eastern-host-loop": 174.49,
    "common-farewell-link": 133.71,
    "southern-notice-loop": 258.13,
    "eastern-notice-loop": 273.35
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
        29.6,
        40.43
      ],
      [
        29.65,
        40.445
      ],
      [
        29.7,
        40.44
      ],
      [
        29.712,
        40.425
      ],
      [
        29.695,
        40.4
      ],
      [
        29.63,
        40.39
      ],
      [
        29.6,
        40.41
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "lake-outline"
  },
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmarkStatus": "pending game measurement"
  },
  "asset": "docs/design/maps/imperial-church/odyssey/02-nicaea.svg"
}
```

## Finite world identities

```json
{
  "version": 1,
  "classification": "authored design specification; not native implementation",
  "entities": [
    {
      "id": "imperial-church.02-nicaea.original-attendants-1",
      "role": "fictional-local-attendant",
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
      "id": "imperial-church.02-nicaea.original-attendants-2",
      "role": "fictional-local-attendant",
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
      "id": "imperial-church.02-nicaea.original-attendants-3",
      "role": "fictional-local-attendant",
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
      "id": "imperial-church.02-nicaea.original-attendants-4",
      "role": "fictional-local-attendant",
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
      "id": "imperial-church.02-nicaea.original-attendants-5",
      "role": "fictional-local-attendant",
      "initialHub": "hub-1",
      "offsetTiles": [
        -14,
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
      "id": "imperial-church.02-nicaea.original-attendants-6",
      "role": "fictional-local-attendant",
      "initialHub": "hub-1",
      "offsetTiles": [
        -12,
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
      "id": "imperial-church.02-nicaea.creed-context-note-1",
      "role": "fictional-local-context-note",
      "initialHub": "hub-1",
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
      "id": "imperial-church.02-nicaea.discipline-context-note-1",
      "role": "fictional-local-context-note",
      "initialHub": "hub-3",
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
      "id": "imperial-church.02-nicaea.feast-context-note-1",
      "role": "fictional-local-context-note",
      "initialHub": "hub-6",
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
      "id": "imperial-church.02-nicaea.creed-working-notice-1",
      "role": "fictional-derived-local-summary",
      "initialHub": "hub-4",
      "offsetTiles": [
        0,
        22
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
      "id": "imperial-church.02-nicaea.discipline-working-notice-1",
      "role": "fictional-derived-local-summary",
      "initialHub": "hub-4",
      "offsetTiles": [
        14,
        22
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
      "id": "imperial-church.02-nicaea.feast-working-notice-1",
      "role": "fictional-derived-local-summary",
      "initialHub": "hub-4",
      "offsetTiles": [
        -14,
        36
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
      "id": "imperial-church.02-nicaea.destination-1",
      "hub": "hub-1",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.02-nicaea.destination-2",
      "hub": "hub-2",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.02-nicaea.destination-3",
      "hub": "hub-3",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.02-nicaea.destination-4",
      "hub": "hub-4",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.02-nicaea.destination-5",
      "hub": "hub-5",
      "offsetTiles": [
        0,
        0
      ],
      "radiusTiles": 3,
      "purpose": "fictional receiving district; not an excavated ancient address"
    },
    {
      "id": "imperial-church.02-nicaea.destination-6",
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
    "original-attendants": [
      "imperial-church.02-nicaea.original-attendants-1",
      "imperial-church.02-nicaea.original-attendants-2",
      "imperial-church.02-nicaea.original-attendants-3",
      "imperial-church.02-nicaea.original-attendants-4",
      "imperial-church.02-nicaea.original-attendants-5",
      "imperial-church.02-nicaea.original-attendants-6"
    ],
    "creed-context-note": [
      "imperial-church.02-nicaea.creed-context-note-1"
    ],
    "discipline-context-note": [
      "imperial-church.02-nicaea.discipline-context-note-1"
    ],
    "feast-context-note": [
      "imperial-church.02-nicaea.feast-context-note-1"
    ],
    "creed-working-notice": [
      "imperial-church.02-nicaea.creed-working-notice-1"
    ],
    "discipline-working-notice": [
      "imperial-church.02-nicaea.discipline-working-notice-1"
    ],
    "feast-working-notice": [
      "imperial-church.02-nicaea.feast-working-notice-1"
    ]
  },
  "survivorGroups": [
    {
      "entities": [
        "imperial-church.02-nicaea.original-attendants-1",
        "imperial-church.02-nicaea.original-attendants-2",
        "imperial-church.02-nicaea.original-attendants-3",
        "imperial-church.02-nicaea.original-attendants-4",
        "imperial-church.02-nicaea.original-attendants-5",
        "imperial-church.02-nicaea.original-attendants-6"
      ],
      "minimumAliveOrAlreadySafe": 6
    }
  ],
  "entityIdentityPolicy": "same explicit identity persists across all phases and save/load; no substitution by a similarly named unit"
}
```

## Optional tasks and combinable playstyles

### Eastern garden viewpoints / Miradores de huertos orientales

EN: Scout both marked viewpoints of eastern garden viewpoints. Benefit: Mark the proposed eastern-notice-loop once; ordinary main access remains known without this task.

ES: Explora los dos miradores señalados de miradores de huertos orientales. Ventaja: Señala una vez el circuito propuesto eastern-notice-loop; el acceso principal normal sigue siendo conocido sin esta tarea.

EN: Two inland observations show the work circuits without inventing military scouting.

ES: Dos observaciones interiores muestran los circuitos sin inventar exploración militar.

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
          "02-nicaea.side-1.zone-1",
          "02-nicaea.side-1.zone-2"
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
        "id": "02-nicaea.side-1.zone-1",
        "hub": "hub-3",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "02-nicaea.side-1.zone-2",
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
      "target": "eastern-notice-loop inland circuit",
      "resources": {},
      "onceFlag": "02-nicaea.side-1.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "eastern-notice-loop"
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
      "western-host-loop",
      "eastern-host-loop",
      "common-farewell-link",
      "southern-notice-loop",
      "eastern-notice-loop"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Separate house labels / Rótulos domésticos separados

EN: Recover both separate copies from separate house labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias distintas de rótulos domésticos separados y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

EN: Fictional copies unlock a note distinguishing disciplinary canons from biblical canon formation.

ES: Copias ficticias abren una nota que distingue cánones disciplinarios de formación del canon bíblico.

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
          "02-nicaea.side-2.entity-1",
          "02-nicaea.side-2.entity-2"
        ],
        "destinations": {
          "02-nicaea.side-2.entity-1": "02-nicaea.side-2.zone-1",
          "02-nicaea.side-2.entity-2": "02-nicaea.side-2.zone-1"
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
        "id": "02-nicaea.side-2.entity-1",
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
        "id": "02-nicaea.side-2.entity-2",
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
        "id": "02-nicaea.side-2.zone-1",
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
      "kind": "unlock-context-and-hint",
      "target": "documented context and a main-goal hint",
      "resources": {},
      "onceFlag": "02-nicaea.side-2.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "sourceIds": [
        "odyssey-source.imperial-church.02-nicaea"
      ],
      "historicalNote": {
        "en": "In 325 the council at Nicaea issued a creed and disciplinary canons and reported agreement on Easter. Eusebius describes imperial travel support, provision and a farewell. His praise of unity is not evidence that disputes ended. The precise meeting buildings remain uncertain. This local hospitality circuit and its six attendants are fictional; the player neither chooses doctrine nor creates a biblical canon.",
        "es-ES": "En 325 el concilio de Nicea emitió un credo y cánones disciplinarios y comunicó un acuerdo sobre Pascua. Eusebio describe apoyo imperial al viaje, manutención y despedida. Su elogio de la unidad no prueba que terminaran las disputas. Los edificios exactos de reunión siguen inciertos. Este circuito local de hospitalidad y sus seis asistentes son ficticios; el jugador no elige doctrina ni crea un canon bíblico."
      },
      "hint": {
        "en": "Collect the three distinct local context notes and deliver each to common copying.",
        "es-ES": "Recoge las tres notas locales de contexto distintas y entrega cada una al taller común."
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
    "receivingHub": "hub-4",
    "corridorIds": [
      "western-host-loop",
      "eastern-host-loop",
      "common-farewell-link",
      "southern-notice-loop",
      "eastern-notice-loop"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Waiting households / Hogares en espera

EN: Bring each of the two aid crates to its assigned household at waiting households. Benefit: 100 food, 50 wood, once.

ES: Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares en espera. Ventaja: 100 de alimento, 50 de madera, una vez.

EN: Voluntary local aid is independent of doctrinal agreement or council rank.

ES: La ayuda local voluntaria es independiente del acuerdo doctrinal o del rango conciliar.

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
          "02-nicaea.side-3.entity-1",
          "02-nicaea.side-3.entity-2"
        ],
        "destinations": {
          "02-nicaea.side-3.entity-1": "02-nicaea.side-3.zone-1",
          "02-nicaea.side-3.entity-2": "02-nicaea.side-3.zone-2"
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
        "id": "02-nicaea.side-3.entity-1",
        "role": "aid",
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
        "id": "02-nicaea.side-3.entity-2",
        "role": "aid",
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
        "id": "02-nicaea.side-3.zone-1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 3
      },
      {
        "id": "02-nicaea.side-3.zone-2",
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
      "onceFlag": "02-nicaea.side-3.rewarded",
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
    "originHub": "hub-6",
    "receivingHub": "hub-2",
    "corridorIds": [
      "western-host-loop",
      "eastern-host-loop",
      "common-farewell-link",
      "southern-notice-loop",
      "eastern-notice-loop"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Southern work store / Almacén de trabajo meridional

EN: Pay 50 wood and restore the damaged store of southern work store to full health. Benefit: 200 food, 100 wood, once.

ES: Paga 50 de madera y repara por completo el almacén dañado de almacén de trabajo meridional. Ventaja: 200 de alimento, 100 de madera, una vez.

EN: One local repair opens finite supplies, not an excavated palace or guaranteed council site.

ES: Una reparación local abre suministros finitos, no un palacio excavado ni una sede garantizada.

```json
{
  "id": "side-4",
  "kind": "repair",
  "predicate": {
    "operator": "all",
    "requirements": [
      {
        "kind": "entity-health",
        "entity": "02-nicaea.side-4.entity-1",
        "health": "full",
        "paymentReceipt": "02-nicaea.side-4.payment",
        "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
      },
      {
        "kind": "atomic-payment",
        "resources": {
          "wood": 50
        },
        "receipt": "02-nicaea.side-4.payment",
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
        "id": "02-nicaea.side-4.entity-1",
        "role": "repair",
        "initialHub": "hub-6",
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
        "id": "02-nicaea.side-4.zone-1",
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
        "food": 200,
        "wood": 100
      },
      "onceFlag": "02-nicaea.side-4.rewarded",
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
    "originHub": "hub-6",
    "receivingHub": "hub-4",
    "corridorIds": [
      "western-host-loop",
      "eastern-host-loop",
      "common-farewell-link",
      "southern-notice-loop",
      "eastern-notice-loop"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Garden market consignment / Remesa del mercado de huertos

EN: Escort the trader of garden market consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.

ES: Escolta al comerciante de remesa del mercado de huertos hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez.

EN: A finite consignment supports distribution; no invented imperial gifts tariff.

ES: Una remesa finita apoya la distribución; no inventa una tarifa de regalos imperiales.

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
          "02-nicaea.side-5.entity-1"
        ],
        "destinations": {
          "02-nicaea.side-5.entity-1": "02-nicaea.side-5.zone-1"
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
        "receipt": "02-nicaea.side-5.payment",
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
        "id": "02-nicaea.side-5.entity-1",
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
        "id": "02-nicaea.side-5.zone-1",
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
      "onceFlag": "02-nicaea.side-5.rewarded",
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
    "receivingHub": "hub-5",
    "corridorIds": [
      "western-host-loop",
      "eastern-host-loop",
      "common-farewell-link",
      "southern-notice-loop",
      "eastern-notice-loop"
    ],
    "maxRequiredRoundTrips": 1,
    "spawnOutsideReceivingZone": true,
    "placementGate": "certify land/transport path and footprints in native map; relocate within same historical district, never alter river"
  }
}
```

### Inland loop guide / Guía del circuito interior

EN: Escort the local guide of inland loop guide to the marked road junction. Benefit: Mark the proposed southern-notice-loop once; ordinary main access remains known without this task.

ES: Escolta al guía local de guía del circuito interior hasta el cruce señalado. Ventaja: Señala una vez el circuito propuesto southern-notice-loop; el acceso principal normal sigue siendo conocido sin esta tarea.

EN: The guide marks an existing land approach; the lake never becomes passable land.

ES: El guía señala un acceso terrestre existente; el lago no se convierte en tierra transitable.

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
          "02-nicaea.side-6.entity-1"
        ],
        "destinations": {
          "02-nicaea.side-6.entity-1": "02-nicaea.side-6.zone-1"
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
        "id": "02-nicaea.side-6.entity-1",
        "role": "guide",
        "initialHub": "hub-2",
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
        "id": "02-nicaea.side-6.zone-1",
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
      "kind": "mark-alternative-route",
      "target": "southern-notice-loop inland circuit",
      "resources": {},
      "onceFlag": "02-nicaea.side-6.rewarded",
      "funding": "reserved-optional-stock",
      "changesHistoricalOutcome": false,
      "corridorId": "southern-notice-loop"
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
    "receivingHub": "hub-6",
    "corridorIds": [
      "western-host-loop",
      "eastern-host-loop",
      "common-farewell-link",
      "southern-notice-loop",
      "eastern-notice-loop"
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
      "id": "split-hosting",
      "optionalObjectives": [
        "side-1",
        "side-6"
      ],
      "costOfOpportunity": "Two independent hospitality teams reduce backtracking; optional observations reveal only authored route information.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "records-and-departure",
      "optionalObjectives": [
        "side-2",
        "side-4"
      ],
      "costOfOpportunity": "Prioritize distinct note collection, then finite copying/repair help; essential costs and receivers remain disclosed.",
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true
    },
    {
      "id": "household-and-market",
      "optionalObjectives": [
        "side-3",
        "side-5"
      ],
      "costOfOpportunity": "Volunteer aid and a finite consignment spend time/50 gold for bounded stocks; main can finish without either.",
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
      "food": 517,
      "wood": 184,
      "gold": 92,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1243,
      "wood": 786,
      "gold": 228,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
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
      "food": 1310,
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
      "food": 450,
      "wood": 160,
      "gold": 80,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1310,
      "wood": 810,
      "gold": 240,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
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
      "food": 1310,
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
      "food": 382,
      "wood": 136,
      "gold": 68,
      "stone": 0
    },
    "gatherableBank": {
      "food": 1378,
      "wood": 834,
      "gold": 252,
      "stone": 100
    },
    "mandatoryDeliveries": {
      "food": 240,
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
      "food": 1310,
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
| scenario.imperial-church.02-nicaea.odyssey.title / always | none | Many Voices beside the Lake | Muchas voces junto al lago |
| scenario.imperial-church.02-nicaea.odyssey.fact-intro / intro first | collection-narrator | In 325 the council at Nicaea issued a creed and disciplinary canons and reported agreement on Easter. Eusebius describes imperial travel support, provision and a farewell. His praise of unity is not evidence that disputes ended. The precise meeting buildings remain uncertain. This local hospitality circuit and its six attendants are fictional; the player neither chooses doctrine nor creates a biblical canon. | En 325 el concilio de Nicea emitió un credo y cánones disciplinarios y comunicó un acuerdo sobre Pascua. Eusebio describe apoyo imperial al viaje, manutención y despedida. Su elogio de la unidad no prueba que terminaran las disputas. Los edificios exactos de reunión siguen inciertos. Este circuito local de hospitalidad y sus seis asistentes son ficticios; el jugador no elige doctrina ni crea un canon bíblico. |
| scenario.imperial-church.02-nicaea.odyssey.handover / after fact-intro | collection-narrator | The campaign narrator now speaks from inherited records and accounts. | El narrador de la campaña toma la palabra a partir de escritos y relatos heredados. |
| scenario.imperial-church.02-nicaea.odyssey.persona-intro / after handover | imperial-clerk | My father kept the grand account above a bundle of household costs. Someone had written “agreement” across the first. Someone else had counted bowls beneath it. I was born later, but learned the smaller lesson early: a proclamation can finish while hungry guests are still waiting at the wrong door. | Mi padre guardaba el gran relato sobre un manojo de gastos domésticos. Alguien había escrito «acuerdo» en el primero. Otro había contado cuencos debajo. Yo nací después, pero aprendí pronto la lección pequeña: una proclamación puede terminar mientras los huéspedes hambrientos aún esperan ante la puerta equivocada. |
| scenario.imperial-church.02-nicaea.odyssey.historical-license / after persona-intro | none | The gameplay participants, records, quantities and routes are fictional local reconstruction. Later writings inform the narrators; no copy of those later books is placed inside this earlier setting. Historical persons remain in attributed narration. | Los participantes, registros, cantidades y rutas jugables son una reconstrucción local ficticia. Los escritos posteriores informan a los narradores; sus libros no aparecen como objetos en este escenario anterior. Las personas históricas permanecen en la narración atribuida. |
| scenario.imperial-church.02-nicaea.odyssey.route-help / available from start; repeatable without effect | none | The three context notes have different subjects. Deliver them to common copying. Split the six original attendants: the first three to the northwestern court, the other three to the eastern court. Each court needs 120 food. One workshop payment prepares three labelled notices with different destinations. Finally bring the same six attendants from their own host courts to farewell; a visit there before hosting does not count. All routes stay on the landward side of the lake. No votes or forced confession are required. | Las tres notas de contexto tratan asuntos distintos. Entrégalas al taller común. Divide los seis asistentes originales: los tres primeros al patio noroccidental y los otros tres al oriental. Cada patio necesita 120 de alimento. Un pago de taller prepara tres avisos rotulados con destinos diferentes. Por último, lleva a esos mismos seis asistentes desde sus patios de acogida a despedida; una visita anterior a la acogida no cuenta. Todas las rutas quedan del lado terrestre del lago. No exige votaciones ni confesiones forzosas. |
| scenario.imperial-church.02-nicaea.odyssey.economy-help / always | none | Optional rewards are unnecessary for the main goals. Recovery supplies and reward stock are reserved; payments are charged once. | Las recompensas opcionales no son necesarias para los objetivos principales. Los suministros de recuperación y las recompensas están reservados; cada pago se cobra una vez. |
| scenario.imperial-church.02-nicaea.odyssey.o1-goal / phase-1 active | none | Collect the three distinct local context notes and deliver each to common copying. | Recoge las tres notas locales de contexto distintas y entrega cada una al taller común. |
| scenario.imperial-church.02-nicaea.odyssey.o1-receipt / o1 latched once | none | Three different subjects are ready at the workshop. | Tres asuntos diferentes están preparados en el taller. |
| scenario.imperial-church.02-nicaea.odyssey.o1-reaction / after o1 receipt | imperial-clerk | A rule for prayer is not a calendar, and neither will feed a guest. | Una regla de oración no es un calendario, y ninguno dará de comer a un huésped. |
| scenario.imperial-church.02-nicaea.odyssey.o2-goal / phase-2 active | none | Receive three original attendants at each hospitality court and fund each court with 120 food. | Recibe tres asistentes originales en cada patio de hospitalidad y financia cada patio con 120 de alimento. |
| scenario.imperial-church.02-nicaea.odyssey.o2-receipt / o2 latched once | none | Both courts received their own three attendants and their own funded allotment. | Ambos patios recibieron sus propios tres asistentes y su propia asignación financiada. |
| scenario.imperial-church.02-nicaea.odyssey.o2-reaction / after o2 receipt | imperial-clerk | Three extra people at one table cannot fill the empty places at the other. | Tres personas de más en una mesa no llenan los lugares vacíos de la otra. |
| scenario.imperial-church.02-nicaea.odyssey.o3-goal / phase-3 active | none | Pay 90 wood and 30 gold once, prepare each notice from its own note, then deliver creed context to farewell, discipline to the southeastern receiver and feast context to the southern receiver. | Paga una vez 90 de madera y 30 de oro, prepara cada aviso con su propia nota y entrega el contexto del credo en despedida, el disciplinario al receptor sudoriental y el festivo al meridional. |
| scenario.imperial-church.02-nicaea.odyssey.o3-receipt / o3 latched once | none | Three different notices reached their assigned receivers; the workshop payment was charged once. | Tres avisos diferentes llegaron a sus receptores asignados; el taller cobró el pago una vez. |
| scenario.imperial-church.02-nicaea.odyssey.o3-reaction / after o3 receipt | imperial-clerk | The labels are modest. That leaves less room for a splendid mistake. | Las etiquetas son modestas. Así queda menos sitio para un error espléndido. |
| scenario.imperial-church.02-nicaea.odyssey.o4-goal / phase-4 active | none | After each original attendant’s own hospitality receipt, observe their departures and bring those same six attendants to the farewell yard. | Tras el recibo propio de hospitalidad de cada asistente original, observa sus salidas y lleva a esos mismos seis asistentes al patio de despedida. |
| scenario.imperial-church.02-nicaea.odyssey.o4-receipt / o4 latched once | none | The six original attendants reached farewell after their own hosted-court departures. | Los seis asistentes originales llegaron a despedida tras sus propias salidas de los patios de acogida. |
| scenario.imperial-church.02-nicaea.odyssey.o4-reaction / after o4 receipt | imperial-clerk | They may leave with different opinions. My list needs their names, not one borrowed voice. | Pueden marcharse con opiniones distintas. Mi lista necesita sus nombres, no una sola voz prestada. |
| scenario.imperial-church.02-nicaea.odyssey.side-1-goal / optional list from start | none | Scout both marked viewpoints of eastern garden viewpoints. Benefit: Mark the proposed eastern-notice-loop once; ordinary main access remains known without this task. | Explora los dos miradores señalados de miradores de huertos orientales. Ventaja: Señala una vez el circuito propuesto eastern-notice-loop; el acceso principal normal sigue siendo conocido sin esta tarea. |
| scenario.imperial-church.02-nicaea.odyssey.side-1-complete / side-1 completed | none | Eastern garden viewpoints completed. Its stated benefit has been granted once. | Miradores de huertos orientales: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-nicaea.odyssey.side-1-lost / side-1 failed-optional | none | Eastern garden viewpoints is unavailable after the loss of its unique participant or object. The main mission continues. | Miradores de huertos orientales: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-nicaea.odyssey.side-2-goal / optional list from start | none | Recover both separate copies from separate house labels and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de rótulos domésticos separados y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| scenario.imperial-church.02-nicaea.odyssey.side-2-complete / side-2 completed | none | Separate house labels completed. Its stated benefit has been granted once. | Rótulos domésticos separados: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-nicaea.odyssey.side-2-lost / side-2 failed-optional | none | Separate house labels is unavailable after the loss of its unique participant or object. The main mission continues. | Rótulos domésticos separados: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-nicaea.odyssey.side-3-goal / optional list from start | none | Bring each of the two aid crates to its assigned household at waiting households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en hogares en espera. Ventaja: 100 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.02-nicaea.odyssey.side-3-complete / side-3 completed | none | Waiting households completed. Its stated benefit has been granted once. | Hogares en espera: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-nicaea.odyssey.side-3-lost / side-3 failed-optional | none | Waiting households is unavailable after the loss of its unique participant or object. The main mission continues. | Hogares en espera: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-nicaea.odyssey.side-4-goal / optional list from start | none | Pay 50 wood and restore the damaged store of southern work store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de almacén de trabajo meridional. Ventaja: 200 de alimento, 100 de madera, una vez. |
| scenario.imperial-church.02-nicaea.odyssey.side-4-complete / side-4 completed | none | Southern work store completed. Its stated benefit has been granted once. | Almacén de trabajo meridional: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-nicaea.odyssey.side-4-lost / side-4 failed-optional | none | Southern work store is unavailable after the loss of its unique participant or object. The main mission continues. | Almacén de trabajo meridional: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-nicaea.odyssey.side-5-goal / optional list from start | none | Escort the trader of garden market consignment to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de remesa del mercado de huertos hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| scenario.imperial-church.02-nicaea.odyssey.side-5-complete / side-5 completed | none | Garden market consignment completed. Its stated benefit has been granted once. | Remesa del mercado de huertos: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-nicaea.odyssey.side-5-lost / side-5 failed-optional | none | Garden market consignment is unavailable after the loss of its unique participant or object. The main mission continues. | Remesa del mercado de huertos: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-nicaea.odyssey.side-6-goal / optional list from start | none | Escort the local guide of inland loop guide to the marked road junction. Benefit: Mark the proposed southern-notice-loop once; ordinary main access remains known without this task. | Escolta al guía local de guía del circuito interior hasta el cruce señalado. Ventaja: Señala una vez el circuito propuesto southern-notice-loop; el acceso principal normal sigue siendo conocido sin esta tarea. |
| scenario.imperial-church.02-nicaea.odyssey.side-6-complete / side-6 completed | none | Inland loop guide completed. Its stated benefit has been granted once. | Guía del circuito interior: completado. Su ventaja indicada se ha concedido una vez. |
| scenario.imperial-church.02-nicaea.odyssey.side-6-lost / side-6 failed-optional | none | Inland loop guide is unavailable after the loss of its unique participant or object. The main mission continues. | Guía del circuito interior: no disponible tras perder a su participante u objeto único. La misión principal continúa. |
| scenario.imperial-church.02-nicaea.odyssey.fact-outro / victory first | collection-narrator | The council’s creed, disciplinary rules and reported Easter agreement remain separate historical results. The local service does not certify universal observance, determine the meeting site or end subsequent controversy. The next act follows building patronage and imperial succession. | El credo, las normas disciplinarias y el acuerdo pascual comunicado permanecen como resultados históricos distintos. El servicio local no acredita observancia universal ni determina la sede ni termina la controversia posterior. El siguiente acto sigue el patrocinio de obras y la sucesión imperial. |
| scenario.imperial-church.02-nicaea.odyssey.persona-outro / after fact-outro | imperial-clerk | Six names returned to the departure list. Three notices found three doors. I shall leave the bowls on the lower shelf: a visitor who cannot eat a grand conclusion may still find them useful. The next family bundle smells of stone dust. | Seis nombres volvieron a la lista de salida. Tres avisos encontraron tres puertas. Dejaré los cuencos en el estante inferior: un visitante que no pueda comer una gran conclusión aún puede encontrarles utilidad. El siguiente legajo familiar huele a polvo de piedra. |
| scenario.imperial-church.02-nicaea.odyssey.defeat / main defeat; close side rewards first | none | The main delivery or survival contract is no longer achievable. Optional losses alone never cause this defeat. | El contrato principal de entrega o supervivencia ya no puede cumplirse. Las pérdidas opcionales por sí solas nunca causan esta derrota. |
| scenario.imperial-church.02-nicaea.odyssey.recovery-help / help; never implies an unsupported recovery action | none | Recovery stock is protected. This design does not authorize free replacement of a lost unique person or object; restart from a save if an essential identity is irrecoverably lost. | La reserva de recuperación está protegida. Este diseño no autoriza reemplazar gratis una persona u objeto únicos perdidos; vuelve a un guardado si una identidad esencial se pierde de forma irrecuperable. |
| scenario.imperial-church.02-nicaea.odyssey.next-episode / after persona-outro | none | Continue with Stone above the Old City. This episode does not complete the campaign. | Continúa con Piedra sobre la ciudad antigua. Este episodio no termina la campaña. |
| scenario.imperial-church.02-nicaea.odyssey.act-turning-point / after next-episode | collection-narrator | Act III: Stone and Succession. Continue with Stone above the Old City, a separate Jerusalem works frame. This act boundary changes place and focus; the council’s agreement did not end every controversy or complete this campaign. | Acto III: Piedra y sucesión. Continúa con Piedra sobre la ciudad antigua, un marco separado de obras en Jerusalén. Este límite de acto cambia el lugar y el foco; el acuerdo conciliar no terminó toda controversia ni completó esta campaña. |

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
    "style": "sober Roman-era inland Nicaea work courtyards; lake and gardens as context",
    "historicalControls": "No exact palace/prayer-house identification, Ottoman tiles, later mosques or modern excavation display. Six attendants are fictional, not the historical council roster.",
    "referenceAssets": [
      "iznik-lake"
    ],
    "productionApproved": false
  },
  "qa": {
    "staticStatus": "checked separately by dossier validator",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "All six original attendants remain indispensable; optional guide or household members never replace them.",
      "Three identities per assigned court, not six at one court; 120 food per court, not 240 at either court.",
      "Each notice requires its own collected note and the exact single o3 funding receipt; repeat derivation/arrival cannot duplicate payments or outputs.",
      "A notice receipt cannot authorize an attendant departure; each departure uses the same attendant and its own o2 court receipt.",
      "Initial or buffered farewell arrival cannot complete the final return; departure and guarded arrival are scoped to o4 and persist across saves.",
      "No Easter computation is invented from canon 20; 325 creed is not substituted with a later liturgical version.",
      "No player-selected doctrine, coerced confession, enemy army, bishop assassination or total population conversion.",
      "All full-width land approaches and receiver radii must avoid lake water and unresolved local drainage.",
      "Never identify the submerged basilica or the modern Senate Palace park as a settled 325 venue.",
      "No intermediate act completion flag or automatic Jerusalem launch; campaign successor recommendation belongs only to the final expanded episode.",
      "skip all optional objectives and win at each difficulty",
      "complete all optionals at each difficulty without spending protected recovery stock",
      "save/load before and after every delivery, payment, optional reward and terminal latch",
      "lose an optional identity: only that task fails",
      "test every corridor and receiving footprint in the real map"
    ]
  }
}
```
