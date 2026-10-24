# The Sealed Copy / La copia sellada

`house-of-ali/03-the-sealed-copy` · 661 CE · archive-evacuation

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/house-of-ali/03-the-sealed-copy.svg)

## Historical frame and outcome

Ali’s death and Hasan’s agreement with Muawiya in 661 were separate developments. The family copies in this mission are fictional.

Muerte de Ali y acuerdo de Hasan con Muawiya son acontecimientos distintos. Diferencias en memorias de las condiciones del pacto se señalan.

Ni rescate del archivo salva retrospectivamente a Ali, ni una facción moderna gana por canonización del pacto.

- [Ismail K. Poonawala, Ali: Life](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Secciones califato, Camello, Siffin y muerte. Distinguir la reconstrucción histórica de las interpretaciones comunitarias.
- [Wilferd Madelung, Hasan b. Ali](https://www.iranicaonline.org/articles/hasan-b-ali/): Negociaciones y renuncia en 661. La conversión 660 de la muerte de Ali en esta página entra en conflicto con su entrada Ali: se registra errata y se usa 661 con contraste.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

At sixteen I knew enough to carry a sealed copy and too little to declare whose account would become the last one.

A los dieciséis sabía lo suficiente para llevar una copia sellada y demasiado poco para declarar qué relato sería el definitivo.

## Geography and map construction

Kufa and Euphrates margin — 320 × 320 tiles; north-up design controls [44.23, 31.93, 44.52, 32.16].

Asentamiento sobre margen de tierras irrigadas; estepa al oeste.

Éufrates al este/noreste según ancla moderna; posición del VII aproximada.

Llano, bancos/drenajes; sin montaña artificial.

Plaza, administración, caminos a Basora y Siria; viviendas abiertas.

Exclude: Sin gran santuario de Najaf posterior ni mezquita actual completa.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Kufa settlement centre | [44.399, 32.03] | [183.07, 176.88] |
| Eastern river margin | [44.422, 32.05] | [205.66, 153.71] |
| Western dry road | [44.32, 32.03] | [105.48, 176.88] |

```json
{
  "bbox": [
    44.23,
    31.93,
    44.52,
    32.16
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Kufa settlement centre",
      "lonLat": [
        44.399,
        32.03
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        183.07,
        176.88
      ]
    },
    {
      "id": "anchor-2",
      "name": "Eastern river margin",
      "lonLat": [
        44.422,
        32.05
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        205.66,
        153.71
      ]
    },
    {
      "id": "anchor-3",
      "name": "Western dry road",
      "lonLat": [
        44.32,
        32.03
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        105.48,
        176.88
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        105.48,
        176.88
      ],
      "purpose": {
        "en": "Recover the two public registers and family copy.",
        "es-ES": "Recupera los dos registros públicos y la copia familiar."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        183.07,
        176.88
      ],
      "purpose": {
        "en": "Escort their custodians to separate departure roads.",
        "es-ES": "Escolta a sus custodios hasta caminos de salida separados."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        205.66,
        153.71
      ],
      "purpose": {
        "en": "Seal the copies and leave provisions for the households remaining in Kufa.",
        "es-ES": "Sella las copias y deja víveres a las familias que permanecen en Kufa."
      },
      "radiusTiles": 14,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    }
  ],
  "corridors": [
    {
      "id": "main",
      "waypoints": [
        [
          105.48,
          176.88
        ],
        [
          183.07,
          176.88
        ],
        [
          205.66,
          153.71
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          105.48,
          176.88
        ],
        [
          152.28,
          184.88
        ],
        [
          183.07,
          176.88
        ],
        [
          205.66,
          153.71
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        44.43,
        32.16
      ],
      [
        44.42,
        32.1
      ],
      [
        44.422,
        32.05
      ],
      [
        44.43,
        32.0
      ],
      [
        44.46,
        31.93
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "kufa",
  "minimumUsableAreaFraction": 0.45,
  "interestSpacingTiles": [
    25,
    55
  ],
  "areaPolicy": "Active core + supply hinterland + optional scouting loops. Place a rest/supply point every 25–55 navigable tiles; rest cannot spawn infinite resources. Bodies of water/steep ground count as geography, not empty playable space.",
  "reliefLevels": {
    "plain": 0,
    "terrace": 1,
    "hill": 3,
    "ridge": 5,
    "cliff": 7
  },
  "rasterisation": "Contemporary coastline and schematic minor-river controls are separate layers. Ancient coast/canal uncertainty is labelled. No automatic land corridor across water; designate an evidenced fixed crossing or a transport segment and require naval capability.",
  "geometryStatus": "georeferenced design controls; corridor traversability not yet game-tested",
  "performanceBudget": {
    "activeMilitaryCap": 240,
    "activeCivilianCap": 80,
    "decorativeObjectsCap": 1600,
    "activeTriggersTargetMax": 350,
    "benchmark": "20-minute crowded corridor replay, 3 passes on documented target PC; simulation slowdown <10% vs reference, measured not presumed"
  },
  "asset": "docs/design/maps/house-of-ali/03-the-sealed-copy.svg",
  "mainRouteLengthStraightTiles": 109.95,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        165.07,
        188.88
      ],
      [
        201.07,
        188.88
      ]
    ],
    "widthTiles": 6,
    "distanceTiles": 36.0,
    "placement": "fictional local supply circuit on SAME bank/plateau in receiving district; validate terrain and footprints, no invented river crossing",
    "twoRoundTripFormula": "4 * measured one-way navigable distance / measured convoy speed + loading/reaction allowance"
  },
  "explorationPlan": {
    "classification": "optional fictional tasks within dated geographic districts; not surveyed ancient locations",
    "sectors": [],
    "secondaryObjectiveIds": [
      "side-1",
      "side-2",
      "side-3",
      "side-4",
      "side-5",
      "side-6"
    ],
    "connectingTrails": "use main/relief corridors to the task districts; optional travel must not create an extra mandatory crossing",
    "qualityGate": "certify each task path, safe delivery zone and footprint at all difficulties; geography remains authoritative"
  }
}
```

## Objectives, entity ledgers and state machine

Every predicate requires the actual world-state operation, not a timer approximating success. Coordinates below specify district plus local offset; validate actual footprint and terrain before assigning engine IDs.

```json
{
  "objectives": [
    {
      "id": "o1",
      "text": {
        "en": "Recover the two public registers and family copy.",
        "es-ES": "Recupera los dos registros públicos y la copia familiar."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "03-the-sealed-copy.o1",
        "oncePerEntity": true,
        "required": 3
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "collect-record",
      "threshold": 3,
      "entities": [
        {
          "id": "03-the-sealed-copy.o1.main-entities.1",
          "role": "record-token",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "03-the-sealed-copy.o1.main-entities.2",
          "role": "record-token",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "03-the-sealed-copy.o1.main-entities.3",
          "role": "record-token",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "collect-record",
        "requiredCount": 3,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "main-entities",
            "kind": "entity-state",
            "state": "collected",
            "entities": [
              "03-the-sealed-copy.o1.main-entities.1",
              "03-the-sealed-copy.o1.main-entities.2",
              "03-the-sealed-copy.o1.main-entities.3"
            ],
            "requiredCount": 3,
            "oncePerEntity": true,
            "destinations": {
              "03-the-sealed-copy.o1.main-entities.1": "03-the-sealed-copy.o1.main-entities.receiving-zone",
              "03-the-sealed-copy.o1.main-entities.2": "03-the-sealed-copy.o1.main-entities.receiving-zone",
              "03-the-sealed-copy.o1.main-entities.3": "03-the-sealed-copy.o1.main-entities.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          }
        ],
        "requiredLedgers": [
          "main-entities"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Escort their custodians to separate departure roads.",
        "es-ES": "Escolta a sus custodios hasta caminos de salida separados."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "03-the-sealed-copy.o2",
        "oncePerEntity": true,
        "required": 3
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "escort-custodian",
      "threshold": 3,
      "entities": [
        {
          "id": "03-the-sealed-copy.o2.main-entities.1",
          "role": "civilian-custodian",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "03-the-sealed-copy.o2.main-entities.2",
          "role": "civilian-custodian",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "03-the-sealed-copy.o2.main-entities.3",
          "role": "civilian-custodian",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "escort-custodian",
        "requiredCount": 3,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "main-entities",
            "kind": "entity-state",
            "state": "arrived",
            "entities": [
              "03-the-sealed-copy.o2.main-entities.1",
              "03-the-sealed-copy.o2.main-entities.2",
              "03-the-sealed-copy.o2.main-entities.3"
            ],
            "requiredCount": 3,
            "oncePerEntity": true,
            "destinations": {
              "03-the-sealed-copy.o2.main-entities.1": "03-the-sealed-copy.separate-custodian-roads.1",
              "03-the-sealed-copy.o2.main-entities.2": "03-the-sealed-copy.separate-custodian-roads.2",
              "03-the-sealed-copy.o2.main-entities.3": "03-the-sealed-copy.separate-custodian-roads.3"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active.",
            "carriedRecords": {
              "03-the-sealed-copy.o2.main-entities.1": [
                "03-the-sealed-copy.o1.main-entities.1"
              ],
              "03-the-sealed-copy.o2.main-entities.2": [
                "03-the-sealed-copy.o1.main-entities.2"
              ],
              "03-the-sealed-copy.o2.main-entities.3": [
                "03-the-sealed-copy.o1.main-entities.3"
              ]
            }
          }
        ],
        "requiredLedgers": [
          "main-entities"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Seal the copies and leave provisions for the households remaining in Kufa.",
        "es-ES": "Sella las copias y deja víveres a las familias que permanecen en Kufa."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "03-the-sealed-copy.o3",
        "oncePerEntity": true,
        "required": 3
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-copy",
      "threshold": 3,
      "entities": [
        {
          "id": "03-the-sealed-copy.o3.main-entities.1",
          "role": "record-token",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "03-the-sealed-copy.o3.main-entities.2",
          "role": "record-token",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "03-the-sealed-copy.o3.main-entities.3",
          "role": "record-token",
          "initialHub": "hub-1",
          "offsetTiles": [
            -8,
            8
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "countedOnce": true,
          "atHub": "hub-1"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "deliver-copy",
        "requiredCount": 3,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "food": 600
        },
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "main-entities",
            "kind": "entity-state",
            "state": "sealed-and-delivered",
            "entities": [
              "03-the-sealed-copy.o3.main-entities.1",
              "03-the-sealed-copy.o3.main-entities.2",
              "03-the-sealed-copy.o3.main-entities.3"
            ],
            "requiredCount": 3,
            "oncePerEntity": true,
            "destinations": {
              "03-the-sealed-copy.o3.main-entities.1": "03-the-sealed-copy.o3.main-entities.receiving-zone",
              "03-the-sealed-copy.o3.main-entities.2": "03-the-sealed-copy.o3.main-entities.receiving-zone",
              "03-the-sealed-copy.o3.main-entities.3": "03-the-sealed-copy.o3.main-entities.receiving-zone"
            },
            "inputRecords": [
              "03-the-sealed-copy.o1.main-entities.1",
              "03-the-sealed-copy.o1.main-entities.2",
              "03-the-sealed-copy.o1.main-entities.3"
            ],
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "household-provisions",
            "kind": "resource-transaction",
            "amounts": {
              "food": 600
            },
            "receivingZones": [
              "03-the-sealed-copy.household-provisions-receiver.1"
            ],
            "allocations": {
              "03-the-sealed-copy.household-provisions-receiver.1": {
                "food": 600
              }
            },
            "paidFlag": "03-the-sealed-copy.o3.household-provisions.paid",
            "account": "spendable",
            "atomic": true,
            "once": true,
            "commit": "debit resources AND persist receipt in same guarded transition; repeated arrivals/save cannot repay"
          }
        ],
        "requiredLedgers": [
          "main-entities",
          "household-provisions"
        ],
        "allRequired": true
      }
    }
  ],
  "worldContract": {
    "version": 1,
    "classification": "authoring specification, not implemented DSL",
    "entities": [
      {
        "id": "03-the-sealed-copy.o1.main-entities.1",
        "role": "record-token",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "03-the-sealed-copy.o1.main-entities.2",
        "role": "record-token",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "03-the-sealed-copy.o1.main-entities.3",
        "role": "record-token",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "03-the-sealed-copy.o2.main-entities.1",
        "role": "civilian-custodian",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "03-the-sealed-copy.o2.main-entities.2",
        "role": "civilian-custodian",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "03-the-sealed-copy.o2.main-entities.3",
        "role": "civilian-custodian",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "03-the-sealed-copy.o3.main-entities.1",
        "role": "record-token",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "03-the-sealed-copy.o3.main-entities.2",
        "role": "record-token",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      },
      {
        "id": "03-the-sealed-copy.o3.main-entities.3",
        "role": "record-token",
        "initialHub": "hub-1",
        "offsetTiles": [
          -8,
          8
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone"
      }
    ],
    "zones": [
      {
        "id": "03-the-sealed-copy.separate-custodian-roads.1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "03-the-sealed-copy.separate-custodian-roads.2",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "03-the-sealed-copy.separate-custodian-roads.3",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "03-the-sealed-copy.household-provisions-receiver.1",
        "hub": "hub-3",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "03-the-sealed-copy.o1.main-entities.receiving-zone",
        "hub": "hub-1",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid ground within geographic district; receiving zone excludes origins",
        "protectedCivilian": false
      },
      {
        "id": "03-the-sealed-copy.o3.main-entities.receiving-zone",
        "hub": "hub-3",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid ground within geographic district; receiving zone excludes origins",
        "protectedCivilian": false
      }
    ],
    "ledgerPolicy": "persist exact object IDs, allocations, receipt flags, pairing and phase. Compound objectives require EVERY listed requirement; shared families/copies retain identity between phases.",
    "resourcePolicy": "protected-recovery is separate from spendable; no double-count in ledgers; no infinite consignment or fifth engine resource",
    "defeatPolicy": "below required possible survivors is unrecoverable; recoverable carriers retain their token via one helper; historical deaths remain narrated, not killable units",
    "earlyDelivery": "Observation is always active. Only phase transition and announced effects are phase-gated. Preserve token origin, owner and already-counted receipt through save/load.",
    "survivorGroups": [],
    "enemyBinding": "Bind every military-guard and military-post entity to a unique initialEnemy roster member. They consume that budget; never add objective guards on top of initial composition."
  },
  "states": {
    "states": [
      "briefing",
      "phase-1",
      "phase-2",
      "phase-3",
      "victory",
      "defeat"
    ],
    "transitions": [
      "briefing → phase-1 after skippable two-voice intro",
      "phase-1 → phase-2 when o1 latched",
      "phase-2 → phase-3 when o2 latched",
      "phase-3 → victory when o3 and all required survivor constraints met",
      "any non-terminal → defeat only on declared unrecoverable constraint"
    ],
    "terminalPriority": "defeat evaluated first; one terminal latch, choice order documented",
    "saveLoad": "Persist phases, delivered entity IDs, paid flags, wave releases, recovered archive flags and terminal latch. Re-entering zone or reloading cannot issue resources twice.",
    "phaseClock": "Relative timer starts on phase entry. Current absolute scenario timers cannot implement this contract; capability proposal required."
  },
  "roster": {
    "player": {
      "fictionalCommander": 0,
      "essentialHeroDefeat": false,
      "escortArchetypes": {
        "militia": 0.5,
        "spearman": 0.25,
        "archer": 0.25
      },
      "villagers": 12,
      "carriers": "one noncombat carrier per task entity, all named fictional",
      "fixedEnemyPosts": 0,
      "preplacedBatteringRams": 0
    },
    "enemyCiv": "Saracens",
    "proxyCautions": "These are engine proxies. No generic religious race, no monks representing forced belief. Enemy units are military/raider gameplay groups, not every neighbouring civilian.",
    "entityRepresentation": {
      "record": "named noncombat carrier with physical copy object/token, no magical relic bonus",
      "wagon": "Trade Cart visual proxy with trading disabled; fixed consignments and no renewable trade gold",
      "family": "named villager groups, no farming/economic AI when representing escorted parties",
      "military-post": "Watch Tower base DE proxy; two objectives have stable unit IDs, unrelated civilians excluded",
      "water": "named noncombat consignment, amount of water is narrative inventory, not an undocumented fifth engine resource",
      "commander": "named fictional Militia proxy, essential only when objective explicitly requires commander; no sacred unit",
      "recovery": "four preplaced guards released once with protected resources, persisting after save/load"
    }
  },
  "secondaryObjectives": [
    {
      "id": "side-1",
      "kind": "copy",
      "title": {
        "en": "What the Fire Must Not Take — the copyists independent spare copies",
        "es-ES": "Lo que el fuego no debe llevarse — las copias de reserva independientes de los copistas"
      },
      "subject": {
        "en": "the copyists independent spare copies",
        "es-ES": "las copias de reserva independientes de los copistas"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Sealed Copy supports this bounded fictional local task. It concerns the copyists independent spare copies; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La copia sellada permite esta tarea local ficticia y limitada. Se ocupa de las copias de reserva independientes de los copistas; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Recover both separate copies from the copyists independent spare copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.",
        "es-ES": "Recupera las dos copias distintas de las copias de reserva independientes de los copistas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-arrival",
            "entities": [
              "03-the-sealed-copy.side-1.entity-1",
              "03-the-sealed-copy.side-1.entity-2"
            ],
            "destinations": {
              "03-the-sealed-copy.side-1.entity-1": "03-the-sealed-copy.side-1.zone-1",
              "03-the-sealed-copy.side-1.entity-2": "03-the-sealed-copy.side-1.zone-1"
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
            "id": "03-the-sealed-copy.side-1.entity-1",
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
            "id": "03-the-sealed-copy.side-1.entity-2",
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
            "id": "03-the-sealed-copy.side-1.zone-1",
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
          "onceFlag": "03-the-sealed-copy.side-1.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "sourceIds": [
            "ali",
            "hasan"
          ],
          "historicalNote": {
            "en": "Ali’s death and Hasan’s agreement with Muawiya in 661 were separate developments. The family copies in this mission are fictional.",
            "es-ES": "Muerte de Ali y acuerdo de Hasan con Muawiya son acontecimientos distintos. Diferencias en memorias de las condiciones del pacto se señalan."
          },
          "hint": {
            "en": "Recover the two public registers and family copy.",
            "es-ES": "Recupera los dos registros públicos y la copia familiar."
          }
        }
      ],
      "completionFlag": "03-the-sealed-copy.side-1.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
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
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-2",
      "kind": "extract",
      "title": {
        "en": "Those Who Choose to Leave — the archive neighbours",
        "es-ES": "Quienes eligen marcharse — los vecinos del archivo"
      },
      "subject": {
        "en": "the archive neighbours",
        "es-ES": "los vecinos del archivo"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Sealed Copy supports this bounded fictional local task. It concerns the archive neighbours; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La copia sellada permite esta tarea local ficticia y limitada. Se ocupa de los vecinos del archivo; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Bring both voluntary evacuee groups from the archive neighbours to the receiving refuge alive. Benefit: 100 food, 25 gold, once.",
        "es-ES": "Lleva con vida los dos grupos de evacuados voluntarios de los vecinos del archivo al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-arrival",
            "entities": [
              "03-the-sealed-copy.side-2.entity-1",
              "03-the-sealed-copy.side-2.entity-2"
            ],
            "destinations": {
              "03-the-sealed-copy.side-2.entity-1": "03-the-sealed-copy.side-2.zone-1",
              "03-the-sealed-copy.side-2.entity-2": "03-the-sealed-copy.side-2.zone-1"
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
            "id": "03-the-sealed-copy.side-2.entity-1",
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
            "id": "03-the-sealed-copy.side-2.entity-2",
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
            "id": "03-the-sealed-copy.side-2.zone-1",
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
          "onceFlag": "03-the-sealed-copy.side-2.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "03-the-sealed-copy.side-2.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
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
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-3",
      "kind": "guide",
      "title": {
        "en": "The Path Between — the civilian archive departure road",
        "es-ES": "El camino entre ambos — el camino de salida del archivo civil"
      },
      "subject": {
        "en": "the civilian archive departure road",
        "es-ES": "el camino de salida del archivo civil"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Sealed Copy supports this bounded fictional local task. It concerns the civilian archive departure road; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La copia sellada permite esta tarea local ficticia y limitada. Se ocupa de el camino de salida del archivo civil; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the local guide of the civilian archive departure road to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.",
        "es-ES": "Escolta al guía local de el camino de salida del archivo civil hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-arrival",
            "entities": [
              "03-the-sealed-copy.side-3.entity-1"
            ],
            "destinations": {
              "03-the-sealed-copy.side-3.entity-1": "03-the-sealed-copy.side-3.zone-1"
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
            "id": "03-the-sealed-copy.side-3.entity-1",
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
            "id": "03-the-sealed-copy.side-3.zone-1",
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
          "onceFlag": "03-the-sealed-copy.side-3.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "corridorId": "relief"
        }
      ],
      "completionFlag": "03-the-sealed-copy.side-3.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
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
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-4",
      "kind": "aid",
      "title": {
        "en": "A Place at the Hearth — the receiving copyists households",
        "es-ES": "Un lugar junto al hogar — los hogares receptores de los copistas"
      },
      "subject": {
        "en": "the receiving copyists households",
        "es-ES": "los hogares receptores de los copistas"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Sealed Copy supports this bounded fictional local task. It concerns the receiving copyists households; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La copia sellada permite esta tarea local ficticia y limitada. Se ocupa de los hogares receptores de los copistas; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Bring each of the two aid crates to its assigned household at the receiving copyists households. Benefit: 100 food, 50 wood, once.",
        "es-ES": "Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares receptores de los copistas. Ventaja: 100 de alimento, 50 de madera, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-arrival",
            "entities": [
              "03-the-sealed-copy.side-4.entity-1",
              "03-the-sealed-copy.side-4.entity-2"
            ],
            "destinations": {
              "03-the-sealed-copy.side-4.entity-1": "03-the-sealed-copy.side-4.zone-1",
              "03-the-sealed-copy.side-4.entity-2": "03-the-sealed-copy.side-4.zone-2"
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
            "id": "03-the-sealed-copy.side-4.entity-1",
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
            "id": "03-the-sealed-copy.side-4.entity-2",
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
            "id": "03-the-sealed-copy.side-4.zone-1",
            "hub": "hub-2",
            "offsetTiles": [
              -8,
              0
            ],
            "radiusTiles": 3
          },
          {
            "id": "03-the-sealed-copy.side-4.zone-2",
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
          "onceFlag": "03-the-sealed-copy.side-4.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "03-the-sealed-copy.side-4.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
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
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-5",
      "kind": "trade",
      "title": {
        "en": "One Honest Consignment — the departure supply post",
        "es-ES": "Una remesa honrada — el puesto de suministros de la salida"
      },
      "subject": {
        "en": "the departure supply post",
        "es-ES": "el puesto de suministros de la salida"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Sealed Copy supports this bounded fictional local task. It concerns the departure supply post; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La copia sellada permite esta tarea local ficticia y limitada. Se ocupa de el puesto de suministros de la salida; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the trader of the departure supply post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.",
        "es-ES": "Escolta al comerciante de el puesto de suministros de la salida hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-arrival",
            "entities": [
              "03-the-sealed-copy.side-5.entity-1"
            ],
            "destinations": {
              "03-the-sealed-copy.side-5.entity-1": "03-the-sealed-copy.side-5.zone-1"
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
            "receipt": "03-the-sealed-copy.side-5.payment",
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
            "id": "03-the-sealed-copy.side-5.entity-1",
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
            "id": "03-the-sealed-copy.side-5.zone-1",
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
          "onceFlag": "03-the-sealed-copy.side-5.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "03-the-sealed-copy.side-5.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
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
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    },
    {
      "id": "side-6",
      "kind": "repair",
      "title": {
        "en": "Raise the Store Again — the receiving store",
        "es-ES": "Levantar de nuevo el almacén — el almacén receptor"
      },
      "subject": {
        "en": "the receiving store",
        "es-ES": "el almacén receptor"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Sealed Copy supports this bounded fictional local task. It concerns the receiving store; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La copia sellada permite esta tarea local ficticia y limitada. Se ocupa de el almacén receptor; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Pay 50 wood and restore the damaged store of the receiving store to full health. Benefit: 200 food, 100 wood, once.",
        "es-ES": "Paga 50 de madera y repara por completo el almacén dañado de el almacén receptor. Ventaja: 200 de alimento, 100 de madera, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-health",
            "entity": "03-the-sealed-copy.side-6.entity-1",
            "health": "full",
            "paymentReceipt": "03-the-sealed-copy.side-6.payment",
            "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
          },
          {
            "kind": "atomic-payment",
            "resources": {
              "wood": 50
            },
            "receipt": "03-the-sealed-copy.side-6.payment",
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
            "id": "03-the-sealed-copy.side-6.entity-1",
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
            "id": "03-the-sealed-copy.side-6.zone-1",
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
          "onceFlag": "03-the-sealed-copy.side-6.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "03-the-sealed-copy.side-6.completed",
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
      "unavailablePolicy": "show failed-optional if its unique entity is lost; no main-goal defeat or restart",
      "terminalPolicy": "optional goals close at main victory/defeat; never delay campaign progression",
      "difficultyPolicy": "same identities, counts and cost in all profiles; no hidden time limit",
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
      },
      "qa": [
        "skip-all-main-still-solvent",
        "complete-in-each-difficulty",
        "save-before-and-after-reward",
        "repeat-arrival-no-double-reward",
        "entity-loss-optional-only",
        "early-main-victory-does-not-wait",
        "no-reward-taken-from-protected-recovery"
      ]
    }
  ],
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
    "fundingPolicy": "replace old generic caches, never stack rewards; withdraw once from reserved gatherable stock; all main goals solvent when every optional goal is skipped",
    "nativeStatus": "design-only; requires certified reusable predicates and native QA"
  },
  "playstyles": [
    {
      "id": "careful-supply",
      "optionalObjectives": [
        "side-6",
        "side-5",
        "side-4"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "informed-movement",
      "optionalObjectives": [
        "side-3",
        "side-1"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "civilian-and-memory",
      "optionalObjectives": [
        "side-2",
        "side-4",
        "side-1"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    }
  ]
}
```

## Difficulty and finite budget

These are explicit estimates for calibration, not measured wins or evidence of perfect balance. Player starting military is preplaced; enemy initial/waves are one roster with production disabled. Nominal militia/spearman/archer/scout costs audit the plan, not historical army numbers. Resource banks include mandatory delivery, replacement allowance, protected recovery and a surplus.

| Profile | Start F/W/G/S | Gatherable F/W/G/S | Escort | Initial + waves | Warning / gap seconds |
|---|---|---|---:|---|---|
| easy | 875/625/312/250 | 2485/1075/1128/550 | 16 | 6 + 6 + 6 + 9 = 27 | 120 / 474 |
| standard | 700/500/250/200 | 2420/1100/1030/600 | 12 | 9 + 9 + 9 + 9 = 36 | 90 / 370 |
| hard | 595/425/212/170 | 2405/1125/988/630 | 10 | 10 + 10 + 10 + 13 = 43 | 75 / 296 |

```json
{
  "profiles": {
    "easy": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 875,
        "wood": 625,
        "gold": 312,
        "stone": 250
      },
      "gatherableBank": {
        "food": 2485,
        "wood": 1075,
        "gold": 1128,
        "stone": 550
      },
      "mandatoryDeliveries": {
        "food": 600,
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
      "maxVillagers": 18,
      "startingEscortCount": 16,
      "playerPopulationCap": 90,
      "enemyTotalCap": 27,
      "initialEnemy": 6,
      "waves": [
        {
          "id": "wave-1",
          "count": 6,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 474,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 6,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 948,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 9,
          "composition": {
            "militia": 4,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1422,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 3,
        "spearman": 1,
        "archer": 1,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1275,
        "wood": 250,
        "gold": 485,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 1560,
        "wood": 1000,
        "gold": 840,
        "stone": 300
      },
      "roughDurationMinutes": [
        25,
        55
      ],
      "objectiveThresholds": "Identical in all difficulties; 6/8 civilian tolerance stays 6/8; no harder historical outcome.",
      "tactics": "one approach at a time; show full route",
      "reactionMarginSeconds": 120,
      "movementSpeed": "native unchanged; no difficulty HP, damage or speed cheats",
      "criticalUnitDefeat": "essential fictional commander only if explicitly named in objective; civilians 6/8 threshold on evacuation missions, courier replacement before defeat otherwise",
      "supplyMargins": {
        "food": 900,
        "wood": 500,
        "gold": 500,
        "stone": 500
      },
      "playerStartingMilitary": {
        "militia": 8,
        "spearman": 4,
        "archer": 4
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts.",
      "accessibleWithoutOptionalRewards": {
        "food": 2810,
        "wood": 1500,
        "gold": 1415,
        "stone": 800
      }
    },
    "standard": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 700,
        "wood": 500,
        "gold": 250,
        "stone": 200
      },
      "gatherableBank": {
        "food": 2420,
        "wood": 1100,
        "gold": 1030,
        "stone": 600
      },
      "mandatoryDeliveries": {
        "food": 600,
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
      "maxVillagers": 18,
      "startingEscortCount": 12,
      "playerPopulationCap": 90,
      "enemyTotalCap": 36,
      "initialEnemy": 9,
      "waves": [
        {
          "id": "wave-1",
          "count": 9,
          "composition": {
            "militia": 4,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 370,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 9,
          "composition": {
            "militia": 4,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 740,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 9,
          "composition": {
            "militia": 4,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1110,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 4,
        "spearman": 2,
        "archer": 2,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1560,
        "wood": 400,
        "gold": 680,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 1320,
        "wood": 900,
        "gold": 680,
        "stone": 300
      },
      "roughDurationMinutes": [
        25,
        55
      ],
      "objectiveThresholds": "Identical in all difficulties; 6/8 civilian tolerance stays 6/8; no harder historical outcome.",
      "tactics": "alternate main and flank; show warning + scoutable approach",
      "reactionMarginSeconds": 90,
      "movementSpeed": "native unchanged; no difficulty HP, damage or speed cheats",
      "criticalUnitDefeat": "essential fictional commander only if explicitly named in objective; civilians 6/8 threshold on evacuation missions, courier replacement before defeat otherwise",
      "supplyMargins": {
        "food": 900,
        "wood": 500,
        "gold": 500,
        "stone": 500
      },
      "playerStartingMilitary": {
        "militia": 6,
        "spearman": 3,
        "archer": 3
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts.",
      "accessibleWithoutOptionalRewards": {
        "food": 2570,
        "wood": 1400,
        "gold": 1255,
        "stone": 800
      }
    },
    "hard": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 595,
        "wood": 425,
        "gold": 212,
        "stone": 170
      },
      "gatherableBank": {
        "food": 2405,
        "wood": 1125,
        "gold": 988,
        "stone": 630
      },
      "mandatoryDeliveries": {
        "food": 600,
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
      "maxVillagers": 18,
      "startingEscortCount": 10,
      "playerPopulationCap": 90,
      "enemyTotalCap": 43,
      "initialEnemy": 10,
      "waves": [
        {
          "id": "wave-1",
          "count": 10,
          "composition": {
            "militia": 5,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 296,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 10,
          "composition": {
            "militia": 5,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 592,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 13,
          "composition": {
            "militia": 5,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 888,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 5,
        "spearman": 2,
        "archer": 2,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1915,
        "wood": 450,
        "gold": 805,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 1200,
        "wood": 850,
        "gold": 600,
        "stone": 300
      },
      "roughDurationMinutes": [
        25,
        55
      ],
      "objectiveThresholds": "Identical in all difficulties; 6/8 civilian tolerance stays 6/8; no harder historical outcome.",
      "tactics": "wave 2 two scoutable approaches, waves remain capped; force escort/reserve split without simultaneous blind spawns",
      "reactionMarginSeconds": 75,
      "movementSpeed": "native unchanged; no difficulty HP, damage or speed cheats",
      "criticalUnitDefeat": "essential fictional commander only if explicitly named in objective; civilians 6/8 threshold on evacuation missions, courier replacement before defeat otherwise",
      "supplyMargins": {
        "food": 900,
        "wood": 500,
        "gold": 500,
        "stone": 500
      },
      "playerStartingMilitary": {
        "militia": 5,
        "spearman": 2,
        "archer": 3
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts.",
      "accessibleWithoutOptionalRewards": {
        "food": 2450,
        "wood": 1350,
        "gold": 1175,
        "stone": 800
      }
    }
  },
  "analysis": {
    "classification": "feasibility envelope, not a combat simulation or proof of balance",
    "startingWorkers": 12,
    "plannedPeakWorkers": 18,
    "effectiveGatherRatePerWorkerResourcePerSecondAssumption": 0.24,
    "walkingAndIdleIncluded": "Assumed rate discounts native gathering for travel/idle; measure actual efficiency in game.",
    "worstDeliveryFood": 600,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Phase waves use the separate local phase-two supply circuit, not the whole-map journey. Two round trips +90s loading/reaction fit the floor. Validate actual nav-path/speed and recompute before game approval.",
    "minimumWaveGapSecondsFromProposedGeometry": 296,
    "wholeJourneyDistanceTiles": 109.95,
    "wholeJourneyOneWaySecondsEstimate": 158,
    "optionalCacheAllocation": {
      "food": 600,
      "wood": 300,
      "gold": 150,
      "stone": 0
    },
    "solventWithoutOptionalCaches": true
  },
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
    "fundingPolicy": "replace old generic caches, never stack rewards; withdraw once from reserved gatherable stock; all main goals solvent when every optional goal is skipped",
    "nativeStatus": "design-only; requires certified reusable predicates and native QA"
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Copia familiar no única; archivista reemplazable por cuidadora ficticia. Dos rutas bloqueables por separado, ninguna exige todas las casas intactas.

{
  "plan": "Copia familiar no única; archivista reemplazable por cuidadora ficticia. Dos rutas bloqueables por separado, ninguna exige todas las casas intactas.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.house-of-ali.03-the-sealed-copy.title` / always | none → next | The Sealed Copy | La copia sellada |
| `scenario.house-of-ali.03-the-sealed-copy.fact-intro` / intro first | collection-narrator → next | Ali’s death and Hasan’s agreement with Muawiya in 661 were separate developments. The family copies in this mission are fictional. | Muerte de Ali y acuerdo de Hasan con Muawiya son acontecimientos distintos. Diferencias en memorias de las condiciones del pacto se señalan. |
| `scenario.house-of-ali.03-the-sealed-copy.personal-intro` / after fact-intro | dina-potter → next | At sixteen I knew enough to carry a sealed copy and too little to declare whose account would become the last one. | A los dieciséis sabía lo suficiente para llevar una copia sellada y demasiado poco para declarar qué relato sería el definitivo. |
| `scenario.house-of-ali.03-the-sealed-copy.objective-1` / phase-1 active | none → hub-1 | Recover the two public registers and family copy. | Recupera los dos registros públicos y la copia familiar. |
| `scenario.house-of-ali.03-the-sealed-copy.objective-2` / phase-2 active | none → hub-2 | Escort their custodians to separate departure roads. | Escolta a sus custodios hasta caminos de salida separados. |
| `scenario.house-of-ali.03-the-sealed-copy.objective-3` / phase-3 active | none → hub-3 | Seal the copies and leave provisions for the households remaining in Kufa. | Sella las copias y deja víveres a las familias que permanecen en Kufa. |
| `scenario.house-of-ali.03-the-sealed-copy.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.house-of-ali.03-the-sealed-copy.scouts` / scouts panel | none → next | Regional setting: Kufa and Euphrates margin. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Kufa and Euphrates margin. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.house-of-ali.03-the-sealed-copy.history` / history panel | none → next | Ali’s death and Hasan’s agreement with Muawiya in 661 were separate developments. The family copies in this mission are fictional. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Muerte de Ali y acuerdo de Hasan con Muawiya son acontecimientos distintos. Diferencias en memorias de las condiciones del pacto se señalan. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.house-of-ali.03-the-sealed-copy.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.house-of-ali.03-the-sealed-copy.event-phase-1-complete` / o1 first becomes true | dina-potter → next | The first household has water. I know the weight of a full jar better than the weight of a title. | La primera familia tiene agua. Conozco mejor el peso de una jarra llena que el de un título. |
| `scenario.house-of-ali.03-the-sealed-copy.event-phase-2-complete` / o2 first becomes true | dina-potter → next | There is another road for the families. Tell them before the dust hides it. | Hay otro camino para las familias. Díselo antes de que lo oculte el polvo. |
| `scenario.house-of-ali.03-the-sealed-copy.event-phase-3-complete` / o3 first becomes true | dina-potter → next | I kept the names. I cannot turn what happened into a kinder ending. | Guardé los nombres. No puedo transformar lo que ocurrió en un final más amable. |
| `scenario.house-of-ali.03-the-sealed-copy.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | dina-potter → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.house-of-ali.03-the-sealed-copy.victory-fact` / victory latch first | collection-narrator → next | Ali’s death and Hasan’s agreement with Muawiya in 661 were separate developments. The family copies in this mission are fictional. Your mission task is complete; this outcome does not change the documented events. | Ni rescate del archivo salva retrospectivamente a Ali, ni una facción moderna gana por canonización del pacto. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.house-of-ali.03-the-sealed-copy.victory-personal` / after victory-fact | dina-potter → 04-the-water-that-remains | I kept the names. I cannot turn what happened into a kinder ending. | Guardé los nombres. No puedo transformar lo que ocurrió en un final más amable. |
| `scenario.house-of-ali.03-the-sealed-copy.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.house-of-ali.03-the-sealed-copy.recovery` / 6 minutes without objective progress | dina-potter → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.house-of-ali.03-the-sealed-copy.side-1-brief` / optional objectives tab, always available | dina-potter → return-to-game | Recover both separate copies from the copyists independent spare copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de las copias de reserva independientes de los copistas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| `scenario.house-of-ali.03-the-sealed-copy.side-1-completed` / 03-the-sealed-copy.side-1.completed latched; once | dina-potter → return-to-game | Optional task completed: What the Fire Must Not Take — the copyists independent spare copies. I would remember the small acts as well. They left marks no seal could make. | Tarea opcional completada: Lo que el fuego no debe llevarse — las copias de reserva independientes de los copistas. También recordaría los actos pequeños. Dejaban marcas que ningún sello podía hacer. |
| `scenario.house-of-ali.03-the-sealed-copy.side-1-unavailable` / unique optional entity irrecoverably lost; once | dina-potter → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.house-of-ali.03-the-sealed-copy.side-2-brief` / optional objectives tab, always available | dina-potter → return-to-game | Bring both voluntary evacuee groups from the archive neighbours to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de los vecinos del archivo al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| `scenario.house-of-ali.03-the-sealed-copy.side-2-completed` / 03-the-sealed-copy.side-2.completed latched; once | dina-potter → return-to-game | Optional task completed: Those Who Choose to Leave — the archive neighbours. I would remember the small acts as well. They left marks no seal could make. | Tarea opcional completada: Quienes eligen marcharse — los vecinos del archivo. También recordaría los actos pequeños. Dejaban marcas que ningún sello podía hacer. |
| `scenario.house-of-ali.03-the-sealed-copy.side-2-unavailable` / unique optional entity irrecoverably lost; once | dina-potter → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.house-of-ali.03-the-sealed-copy.side-3-brief` / optional objectives tab, always available | dina-potter → return-to-game | Escort the local guide of the civilian archive departure road to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de el camino de salida del archivo civil hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| `scenario.house-of-ali.03-the-sealed-copy.side-3-completed` / 03-the-sealed-copy.side-3.completed latched; once | dina-potter → return-to-game | Optional task completed: The Path Between — the civilian archive departure road. I would remember the small acts as well. They left marks no seal could make. | Tarea opcional completada: El camino entre ambos — el camino de salida del archivo civil. También recordaría los actos pequeños. Dejaban marcas que ningún sello podía hacer. |
| `scenario.house-of-ali.03-the-sealed-copy.side-3-unavailable` / unique optional entity irrecoverably lost; once | dina-potter → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.house-of-ali.03-the-sealed-copy.side-4-brief` / optional objectives tab, always available | dina-potter → return-to-game | Bring each of the two aid crates to its assigned household at the receiving copyists households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares receptores de los copistas. Ventaja: 100 de alimento, 50 de madera, una vez. |
| `scenario.house-of-ali.03-the-sealed-copy.side-4-completed` / 03-the-sealed-copy.side-4.completed latched; once | dina-potter → return-to-game | Optional task completed: A Place at the Hearth — the receiving copyists households. I would remember the small acts as well. They left marks no seal could make. | Tarea opcional completada: Un lugar junto al hogar — los hogares receptores de los copistas. También recordaría los actos pequeños. Dejaban marcas que ningún sello podía hacer. |
| `scenario.house-of-ali.03-the-sealed-copy.side-4-unavailable` / unique optional entity irrecoverably lost; once | dina-potter → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.house-of-ali.03-the-sealed-copy.side-5-brief` / optional objectives tab, always available | dina-potter → return-to-game | Escort the trader of the departure supply post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de el puesto de suministros de la salida hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| `scenario.house-of-ali.03-the-sealed-copy.side-5-completed` / 03-the-sealed-copy.side-5.completed latched; once | dina-potter → return-to-game | Optional task completed: One Honest Consignment — the departure supply post. I would remember the small acts as well. They left marks no seal could make. | Tarea opcional completada: Una remesa honrada — el puesto de suministros de la salida. También recordaría los actos pequeños. Dejaban marcas que ningún sello podía hacer. |
| `scenario.house-of-ali.03-the-sealed-copy.side-5-unavailable` / unique optional entity irrecoverably lost; once | dina-potter → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.house-of-ali.03-the-sealed-copy.side-6-brief` / optional objectives tab, always available | dina-potter → return-to-game | Pay 50 wood and restore the damaged store of the receiving store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el almacén receptor. Ventaja: 200 de alimento, 100 de madera, una vez. |
| `scenario.house-of-ali.03-the-sealed-copy.side-6-completed` / 03-the-sealed-copy.side-6.completed latched; once | dina-potter → return-to-game | Optional task completed: Raise the Store Again — the receiving store. I would remember the small acts as well. They left marks no seal could make. | Tarea opcional completada: Levantar de nuevo el almacén — el almacén receptor. También recordaría los actos pequeños. Dejaban marcas que ningún sello podía hacer. |
| `scenario.house-of-ali.03-the-sealed-copy.side-6-unavailable` / unique optional entity irrecoverably lost; once | dina-potter → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |

## Adversarial QA

- `historical-facts` (pending): All narrator facts link to claim/source; uncertainty spoken when essential; fictional dialogue labelled.
- `map-geography` (pending): Landmark banks and coast orientation match regional controls; no anachronisms listed in profile.
- `footprint-and-transport` (pending): Flood fill with unit footprint, bridge/naval checks; land routes cannot jump water; largest convoy reaches all goals.
- `early-completion` (pending): Targets destroyed/archives saved before activation latch and unlock later objectives.
- `save-load-ledger` (pending): Save before/after every delivery and wave; reload cannot duplicate or lose counts.
- `finite-enemy` (pending): Roster initial plus three waves <= cap in each difficulty; all enemy production off.
- `loss-recovery` (pending): Lose one courier/boat or two families; documented fallback exists without repeating payments.
- `difficulty` (pending): Normal success rates 60–80% familiar AoE2 cohort, easy 80–95% learning cohort, hard 35–60% expert blind cohort: hypotheses, not measurements.
- `narration` (pending): General factual brief then campaign person; no omniscience or lived memory before birth.
- `localization` (pending): All screens EN and es-ES, 17 full destination catalogs reviewed for release; no implicit engine fallback.
- `performance` (pending): Recorded 20min crowded replay below frame/simulation degradation budget.
- `continuity` (pending): Fresh/profile one-route/both/unknown/replay preserve cumulative keys and nonblocking static recommendation.
