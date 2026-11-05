# The Hill and the School / La colina y la escuela

`jewish-tradition/02-the-hill-and-the-school` · c. 200 CE · archive-economy

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/jewish-tradition/02-the-hill-and-the-school.svg)

## Historical frame and outcome

Around the beginning of the third century, Judah the Prince was associated with the redaction of the Mishnah. Its transmission was a collective process.

Tradición de compilación de la Mishná y contexto de Judá el Príncipe; localización/fecha exacta de cada acto de escritura no se afirma.

Los contadores representan logística, no una puntuación de ortodoxia religiosa.

- [UNESCO, Necropolis of Bet Shearim](https://whc.unesco.org/en/list/1471/): Contexto de renovación judía y Judá el Príncipe. Necrópolis y transmisión cultural, no prueba de una aventura del protagonista.
- [Jewish Encyclopedia, Judah I](https://jewishencyclopedia.com/articles/8963-judah-i): Redaction and limits of attribution. Older scholarship; redactor rather than sole author. The precise form and moment of redaction remain qualified.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

My teachers described those older debates without putting a torch to one another’s books. I gave that inherited disagreement its own column.

Mis maestros describían aquellos debates antiguos sin quemar los libros de los demás. Dediqué una columna a esa discrepancia heredada.

## Geography and map construction

Galilee, Sepphoris and Tiberias — 320 × 320 tiles; north-up design controls [35.113, 32.6, 35.65, 32.95].

Galilea con colinas cultivadas y asentamientos; costa del lago interior.

Mar de Galilea al este; Jordán sale hacia sur, no al Mediterráneo.

Seforis al oeste elevada; Tiberíades en costa occidental del lago.

Camino de mesetas hacia Tiberíades y eje de poblados.

Exclude: No mezclar aldeas separadas 30 km como barrio continuo; escala regional comprimida.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Tiberias west shore | [35.531, 32.79] | [238.79, 150.04] |
| Bet Shearim | [35.128, 32.703] | [25.05, 204.92] |
| Sepphoris area | [35.279, 32.754] | [105.13, 172.75] |

```json
{
  "bbox": [
    35.113,
    32.6,
    35.65,
    32.95
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Tiberias west shore",
      "lonLat": [
        35.531,
        32.79
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        238.79,
        150.04
      ]
    },
    {
      "id": "anchor-2",
      "name": "Bet Shearim",
      "lonLat": [
        35.128,
        32.703
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        25.05,
        204.92
      ]
    },
    {
      "id": "anchor-3",
      "name": "Sepphoris area",
      "lonLat": [
        35.279,
        32.754
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        105.13,
        172.75
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-2",
      "centre": [
        25.05,
        204.92
      ],
      "purpose": {
        "en": "Link three settlements to the western archive.",
        "es-ES": "Conecta tres asentamientos con el archivo occidental."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-2",
      "centre": [
        25.05,
        204.92
      ],
      "purpose": {
        "en": "Fund copying with 800 food and 400 gold while keeping village reserves.",
        "es-ES": "Financia la copia con 800 de alimento y 400 de oro conservando reservas aldeanas."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-3",
      "centre": [
        105.13,
        172.75
      ],
      "purpose": {
        "en": "Deliver two completed copies to separate custodians.",
        "es-ES": "Entrega dos copias completas a custodios distintos."
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
          25.05,
          204.92
        ],
        [
          25.05,
          204.92
        ],
        [
          105.13,
          172.75
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          25.05,
          204.92
        ],
        [
          33.05,
          212.92
        ],
        [
          25.05,
          204.92
        ],
        [
          105.13,
          172.75
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        35.55,
        32.85
      ],
      [
        35.58,
        32.83
      ],
      [
        35.59,
        32.77
      ],
      [
        35.56,
        32.72
      ],
      [
        35.54,
        32.73
      ],
      [
        35.53,
        32.8
      ],
      [
        35.55,
        32.85
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "lake-outline"
  },
  "terrainProfile": "galilee",
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
  "asset": "docs/design/maps/jewish-tradition/02-the-hill-and-the-school.svg",
  "mainRouteLengthStraightTiles": 356.25,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        7.05,
        216.92
      ],
      [
        43.05,
        216.92
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
        "en": "Link three settlements to the western archive.",
        "es-ES": "Conecta tres asentamientos con el archivo occidental."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-the-hill-and-the-school.o1",
        "oncePerEntity": true,
        "required": 3
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "connect-settlement",
      "threshold": 3,
      "entities": [
        {
          "id": "02-the-hill-and-the-school.o1.main-access-blocker.1",
          "role": "military-guard",
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
          "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "02-the-hill-and-the-school.o1.main-access-blocker.2",
          "role": "military-guard",
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
          "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "02-the-hill-and-the-school.o1.main-access-blocker.3",
          "role": "military-guard",
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
          "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top",
          "countedOnce": true,
          "atHub": "hub-1"
        },
        {
          "id": "02-the-hill-and-the-school.western-archive-blocker.1",
          "role": "military-guard",
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
          "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top",
          "countedOnce": true,
          "atHub": "hub-1"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "connect-settlement",
        "requiredCount": 3,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "main-access",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "02-the-hill-and-the-school.o1.main-access.1",
              "02-the-hill-and-the-school.o1.main-access.2",
              "02-the-hill-and-the-school.o1.main-access.3"
            ],
            "blockingEnemies": [
              "02-the-hill-and-the-school.o1.main-access-blocker.1",
              "02-the-hill-and-the-school.o1.main-access-blocker.2",
              "02-the-hill-and-the-school.o1.main-access-blocker.3"
            ],
            "requiredCount": 3,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          },
          {
            "id": "western-archive",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "02-the-hill-and-the-school.western-archive.1"
            ],
            "blockingEnemies": [
              "02-the-hill-and-the-school.western-archive-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          }
        ],
        "requiredLedgers": [
          "main-access",
          "western-archive"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Fund copying with 800 food and 400 gold while keeping village reserves.",
        "es-ES": "Financia la copia con 800 de alimento y 400 de oro conservando reservas aldeanas."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-the-hill-and-the-school.o2",
        "oncePerEntity": true,
        "required": 1200
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "resource-delivery",
      "threshold": 1200,
      "entities": [],
      "predicate": {
        "operator": "all",
        "operation": "resource-delivery",
        "requiredCount": 1200,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "food": 800,
          "gold": 400
        },
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "audited-delivery",
            "kind": "resource-transaction",
            "amounts": {
              "food": 800,
              "gold": 400
            },
            "receivingZones": [
              "02-the-hill-and-the-school.o2-supply-district.1"
            ],
            "allocations": {
              "02-the-hill-and-the-school.o2-supply-district.1": {
                "food": 800,
                "gold": 400
              }
            },
            "paidFlag": "02-the-hill-and-the-school.o2.audited-delivery.paid",
            "account": "spendable",
            "atomic": true,
            "once": true,
            "commit": "debit resources AND persist receipt in same guarded transition; repeated arrivals/save cannot repay"
          },
          {
            "id": "keep-stock",
            "kind": "minimum-stock",
            "account": "protected-recovery",
            "amounts": {
              "food": 300,
              "wood": 200,
              "gold": 100,
              "stone": 0
            },
            "evaluate": "at completion; separately reserved, cannot fund mandatory transactions"
          }
        ],
        "requiredLedgers": [
          "audited-delivery",
          "keep-stock"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Deliver two completed copies to separate custodians.",
        "es-ES": "Entrega dos copias completas a custodios distintos."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-the-hill-and-the-school.o3",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-copy",
      "threshold": 2,
      "entities": [
        {
          "id": "02-the-hill-and-the-school.o3.main-entities.1",
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
          "id": "02-the-hill-and-the-school.o3.main-entities.2",
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
        "requiredCount": 2,
        "destination": "hub-3",
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
              "02-the-hill-and-the-school.o3.main-entities.1",
              "02-the-hill-and-the-school.o3.main-entities.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true,
            "destinations": {
              "02-the-hill-and-the-school.o3.main-entities.1": "02-the-hill-and-the-school.separate-custodians.1",
              "02-the-hill-and-the-school.o3.main-entities.2": "02-the-hill-and-the-school.separate-custodians.2"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          }
        ],
        "requiredLedgers": [
          "main-entities"
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
        "id": "02-the-hill-and-the-school.western-archive-blocker.1",
        "role": "military-guard",
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
        "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top"
      },
      {
        "id": "02-the-hill-and-the-school.o3.main-entities.1",
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
        "id": "02-the-hill-and-the-school.o3.main-entities.2",
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
        "id": "02-the-hill-and-the-school.o1.main-access-blocker.1",
        "role": "military-guard",
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
        "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top"
      },
      {
        "id": "02-the-hill-and-the-school.o1.main-access-blocker.2",
        "role": "military-guard",
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
        "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top"
      },
      {
        "id": "02-the-hill-and-the-school.o1.main-access-blocker.3",
        "role": "military-guard",
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
        "rosterSource": "initialEnemy; bind to unique member of existing finite roster, never add on top"
      }
    ],
    "zones": [
      {
        "id": "02-the-hill-and-the-school.western-archive.1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "02-the-hill-and-the-school.o2-supply-district.1",
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
        "id": "02-the-hill-and-the-school.separate-custodians.1",
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
        "id": "02-the-hill-and-the-school.separate-custodians.2",
        "hub": "hub-3",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "02-the-hill-and-the-school.o1.main-access.1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "02-the-hill-and-the-school.o1.main-access.2",
        "hub": "hub-1",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "02-the-hill-and-the-school.o1.main-access.3",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
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
    "enemyCiv": "Byzantines",
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
        "en": "What the Fire Must Not Take — the teaching-copy shelves",
        "es-ES": "Lo que el fuego no debe llevarse — los estantes de copias de enseñanza"
      },
      "subject": {
        "en": "the teaching-copy shelves",
        "es-ES": "los estantes de copias de enseñanza"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Hill and the School supports this bounded fictional local task. It concerns the teaching-copy shelves; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La colina y la escuela permite esta tarea local ficticia y limitada. Se ocupa de los estantes de copias de enseñanza; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Recover both separate copies from the teaching-copy shelves and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.",
        "es-ES": "Recupera las dos copias distintas de los estantes de copias de enseñanza y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal."
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
              "02-the-hill-and-the-school.side-1.entity-1",
              "02-the-hill-and-the-school.side-1.entity-2"
            ],
            "destinations": {
              "02-the-hill-and-the-school.side-1.entity-1": "02-the-hill-and-the-school.side-1.zone-1",
              "02-the-hill-and-the-school.side-1.entity-2": "02-the-hill-and-the-school.side-1.zone-1"
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
            "id": "02-the-hill-and-the-school.side-1.entity-1",
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
            "id": "02-the-hill-and-the-school.side-1.entity-2",
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
            "id": "02-the-hill-and-the-school.side-1.zone-1",
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
          "onceFlag": "02-the-hill-and-the-school.side-1.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "sourceIds": [
            "beth-shearim",
            "judah-mishnah"
          ],
          "historicalNote": {
            "en": "Around the beginning of the third century, Judah the Prince was associated with the redaction of the Mishnah. Its transmission was a collective process.",
            "es-ES": "Tradición de compilación de la Mishná y contexto de Judá el Príncipe; localización/fecha exacta de cada acto de escritura no se afirma."
          },
          "hint": {
            "en": "Link three settlements to the western archive.",
            "es-ES": "Conecta tres asentamientos con el archivo occidental."
          }
        }
      ],
      "completionFlag": "02-the-hill-and-the-school.side-1.completed",
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
      "kind": "repair",
      "title": {
        "en": "Raise the Store Again — the western archive store",
        "es-ES": "Levantar de nuevo el almacén — el almacén del archivo occidental"
      },
      "subject": {
        "en": "the western archive store",
        "es-ES": "el almacén del archivo occidental"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Hill and the School supports this bounded fictional local task. It concerns the western archive store; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La colina y la escuela permite esta tarea local ficticia y limitada. Se ocupa de el almacén del archivo occidental; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Pay 50 wood and restore the damaged store of the western archive store to full health. Benefit: 200 food, 100 wood, once.",
        "es-ES": "Paga 50 de madera y repara por completo el almacén dañado de el almacén del archivo occidental. Ventaja: 200 de alimento, 100 de madera, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-health",
            "entity": "02-the-hill-and-the-school.side-2.entity-1",
            "health": "full",
            "paymentReceipt": "02-the-hill-and-the-school.side-2.payment",
            "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
          },
          {
            "kind": "atomic-payment",
            "resources": {
              "wood": 50
            },
            "receipt": "02-the-hill-and-the-school.side-2.payment",
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
            "id": "02-the-hill-and-the-school.side-2.entity-1",
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
            "id": "02-the-hill-and-the-school.side-2.zone-1",
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
          "onceFlag": "02-the-hill-and-the-school.side-2.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "02-the-hill-and-the-school.side-2.completed",
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
    },
    {
      "id": "side-3",
      "kind": "trade",
      "title": {
        "en": "One Honest Consignment — the Galilean hill road",
        "es-ES": "Una remesa honrada — la calzada de las colinas de Galilea"
      },
      "subject": {
        "en": "the Galilean hill road",
        "es-ES": "la calzada de las colinas de Galilea"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Hill and the School supports this bounded fictional local task. It concerns the Galilean hill road; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La colina y la escuela permite esta tarea local ficticia y limitada. Se ocupa de la calzada de las colinas de Galilea; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the trader of the Galilean hill road to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.",
        "es-ES": "Escolta al comerciante de la calzada de las colinas de Galilea hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez."
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
              "02-the-hill-and-the-school.side-3.entity-1"
            ],
            "destinations": {
              "02-the-hill-and-the-school.side-3.entity-1": "02-the-hill-and-the-school.side-3.zone-1"
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
            "receipt": "02-the-hill-and-the-school.side-3.payment",
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
            "id": "02-the-hill-and-the-school.side-3.entity-1",
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
            "id": "02-the-hill-and-the-school.side-3.zone-1",
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
          "onceFlag": "02-the-hill-and-the-school.side-3.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "02-the-hill-and-the-school.side-3.completed",
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
      "id": "side-4",
      "kind": "guide",
      "title": {
        "en": "The Path Between — the settlement footpaths",
        "es-ES": "El camino entre ambos — las sendas entre poblados"
      },
      "subject": {
        "en": "the settlement footpaths",
        "es-ES": "las sendas entre poblados"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Hill and the School supports this bounded fictional local task. It concerns the settlement footpaths; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La colina y la escuela permite esta tarea local ficticia y limitada. Se ocupa de las sendas entre poblados; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the local guide of the settlement footpaths to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.",
        "es-ES": "Escolta al guía local de las sendas entre poblados hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga."
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
              "02-the-hill-and-the-school.side-4.entity-1"
            ],
            "destinations": {
              "02-the-hill-and-the-school.side-4.entity-1": "02-the-hill-and-the-school.side-4.zone-1"
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
            "id": "02-the-hill-and-the-school.side-4.entity-1",
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
            "id": "02-the-hill-and-the-school.side-4.zone-1",
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
          "onceFlag": "02-the-hill-and-the-school.side-4.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "corridorId": "relief"
        }
      ],
      "completionFlag": "02-the-hill-and-the-school.side-4.completed",
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
      "id": "side-5",
      "kind": "aid",
      "title": {
        "en": "A Place at the Hearth — the study-house households",
        "es-ES": "Un lugar junto al hogar — los hogares de las casas de estudio"
      },
      "subject": {
        "en": "the study-house households",
        "es-ES": "los hogares de las casas de estudio"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Hill and the School supports this bounded fictional local task. It concerns the study-house households; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La colina y la escuela permite esta tarea local ficticia y limitada. Se ocupa de los hogares de las casas de estudio; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Bring each of the two aid crates to its assigned household at the study-house households. Benefit: 100 food, 50 wood, once.",
        "es-ES": "Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares de las casas de estudio. Ventaja: 100 de alimento, 50 de madera, una vez."
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
              "02-the-hill-and-the-school.side-5.entity-1",
              "02-the-hill-and-the-school.side-5.entity-2"
            ],
            "destinations": {
              "02-the-hill-and-the-school.side-5.entity-1": "02-the-hill-and-the-school.side-5.zone-1",
              "02-the-hill-and-the-school.side-5.entity-2": "02-the-hill-and-the-school.side-5.zone-2"
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
            "id": "02-the-hill-and-the-school.side-5.entity-1",
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
            "id": "02-the-hill-and-the-school.side-5.entity-2",
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
            "id": "02-the-hill-and-the-school.side-5.zone-1",
            "hub": "hub-2",
            "offsetTiles": [
              -8,
              0
            ],
            "radiusTiles": 3
          },
          {
            "id": "02-the-hill-and-the-school.side-5.zone-2",
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
          "onceFlag": "02-the-hill-and-the-school.side-5.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "02-the-hill-and-the-school.side-5.completed",
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
      "kind": "scout",
      "title": {
        "en": "The Road Seen First — the lake-facing road junctions",
        "es-ES": "El camino visto primero — los cruces de camino orientados al lago"
      },
      "subject": {
        "en": "the lake-facing road junctions",
        "es-ES": "los cruces de camino orientados al lago"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Hill and the School supports this bounded fictional local task. It concerns the lake-facing road junctions; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de La colina y la escuela permite esta tarea local ficticia y limitada. Se ocupa de los cruces de camino orientados al lago; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Scout both marked viewpoints of the lake-facing road junctions. Benefit: reveal the second reserve approach.",
        "es-ES": "Explora los dos miradores señalados de los cruces de camino orientados al lago. Ventaja: revela la aproximación de la segunda reserva."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "visit-zones",
            "zones": [
              "02-the-hill-and-the-school.side-6.zone-1",
              "02-the-hill-and-the-school.side-6.zone-2"
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
            "id": "02-the-hill-and-the-school.side-6.zone-1",
            "hub": "hub-1",
            "offsetTiles": [
              -8,
              0
            ],
            "radiusTiles": 3
          },
          {
            "id": "02-the-hill-and-the-school.side-6.zone-2",
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
          "kind": "reveal-enemy-approach",
          "target": "wave-2 approach",
          "resources": {},
          "onceFlag": "02-the-hill-and-the-school.side-6.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "rosterIds": [
            "wave-2"
          ],
          "alreadyReleasedPolicy": "reveal current surviving members, never spawn a replacement"
        }
      ],
      "completionFlag": "02-the-hill-and-the-school.side-6.completed",
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
    "fundingPolicy": "replace old generic caches, never stack rewards; withdraw once from reserved gatherable stock; all main goals solvent when every optional goal is skipped",
    "nativeStatus": "design-only; requires certified reusable predicates and native QA"
  },
  "playstyles": [
    {
      "id": "careful-supply",
      "optionalObjectives": [
        "side-2",
        "side-3",
        "side-5"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "informed-movement",
      "optionalObjectives": [
        "side-4",
        "side-6",
        "side-1"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "civilian-and-memory",
      "optionalObjectives": [
        "side-5",
        "side-1",
        "side-4"
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
| easy | 875/625/312/250 | 2685/1075/1528/550 | 16 | 4 + 4 + 4 + 6 = 18 | 120 / 474 |
| standard | 700/500/250/200 | 2620/1100/1430/600 | 12 | 6 + 6 + 6 + 6 = 24 | 90 / 370 |
| hard | 595/425/212/170 | 2605/1125/1388/630 | 10 | 7 + 7 + 7 + 8 = 29 | 75 / 296 |

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
        "food": 2685,
        "wood": 1075,
        "gold": 1528,
        "stone": 550
      },
      "mandatoryDeliveries": {
        "food": 800,
        "wood": 0,
        "gold": 400,
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
      "enemyTotalCap": 18,
      "initialEnemy": 4,
      "waves": [
        {
          "id": "wave-1",
          "count": 4,
          "composition": {
            "militia": 2,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 0
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 474,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 4,
          "composition": {
            "militia": 2,
            "spearman": 1,
            "archer": 1,
            "scoutCavalry": 0
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 948,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 6,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
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
        "militia": 2,
        "spearman": 1,
        "archer": 1,
        "scoutCavalry": 0
      },
      "enemyNominalResourceCost": {
        "food": 760,
        "wood": 200,
        "gold": 360,
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
        "food": 3110,
        "wood": 1500,
        "gold": 1840,
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
        "food": 2620,
        "wood": 1100,
        "gold": 1430,
        "stone": 600
      },
      "mandatoryDeliveries": {
        "food": 800,
        "wood": 0,
        "gold": 400,
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
      "enemyTotalCap": 24,
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
          "offsetSeconds": 370,
          "warningSeconds": 90,
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
          "offsetSeconds": 740,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 6,
          "composition": {
            "militia": 3,
            "spearman": 1,
            "archer": 1,
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
        "militia": 3,
        "spearman": 1,
        "archer": 1,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1180,
        "wood": 200,
        "gold": 420,
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
        "food": 2870,
        "wood": 1400,
        "gold": 1680,
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
        "food": 2605,
        "wood": 1125,
        "gold": 1388,
        "stone": 630
      },
      "mandatoryDeliveries": {
        "food": 800,
        "wood": 0,
        "gold": 400,
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
      "enemyTotalCap": 29,
      "initialEnemy": 7,
      "waves": [
        {
          "id": "wave-1",
          "count": 7,
          "composition": {
            "militia": 4,
            "spearman": 1,
            "archer": 1,
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
          "count": 7,
          "composition": {
            "militia": 4,
            "spearman": 1,
            "archer": 1,
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
          "count": 8,
          "composition": {
            "militia": 3,
            "spearman": 2,
            "archer": 2,
            "scoutCavalry": 1
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 888,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 4,
        "spearman": 1,
        "archer": 1,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1395,
        "wood": 250,
        "gold": 525,
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
        "food": 2750,
        "wood": 1350,
        "gold": 1600,
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
    "worstDeliveryFood": 800,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Phase waves use the separate local phase-two supply circuit, not the whole-map journey. Two round trips +90s loading/reaction fit the floor. Validate actual nav-path/speed and recompute before game approval.",
    "minimumWaveGapSecondsFromProposedGeometry": 296,
    "wholeJourneyDistanceTiles": 86.3,
    "wholeJourneyOneWaySecondsEstimate": 124,
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
    "fundingPolicy": "replace old generic caches, never stack rewards; withdraw once from reserved gatherable stock; all main goals solvent when every optional goal is skipped",
    "nativeStatus": "design-only; requires certified reusable predicates and native QA"
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Dos talleres; perder uno aumenta recorrido y coste limitado. Reservar 400 de alimento para recovery; no convertir al rival como condición.

{
  "plan": "Dos talleres; perder uno aumenta recorrido y coste limitado. Reservar 400 de alimento para recovery; no convertir al rival como condición.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.jewish-tradition.02-the-hill-and-the-school.title` / always | none → next | The Hill and the School | La colina y la escuela |
| `scenario.jewish-tradition.02-the-hill-and-the-school.fact-intro` / intro first | collection-narrator → next | Around the beginning of the third century, Judah the Prince was associated with the redaction of the Mishnah. Its transmission was a collective process. | Tradición de compilación de la Mishná y contexto de Judá el Príncipe; localización/fecha exacta de cada acto de escritura no se afirma. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.personal-intro` / after fact-intro | judith-copyist → next | My teachers described those older debates without putting a torch to one another’s books. I gave that inherited disagreement its own column. | Mis maestros describían aquellos debates antiguos sin quemar los libros de los demás. Dediqué una columna a esa discrepancia heredada. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.objective-1` / phase-1 active | none → hub-1 | Link three settlements to the western archive. | Conecta tres asentamientos con el archivo occidental. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.objective-2` / phase-2 active | none → hub-2 | Fund copying with 800 food and 400 gold while keeping village reserves. | Financia la copia con 800 de alimento y 400 de oro conservando reservas aldeanas. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.objective-3` / phase-3 active | none → hub-3 | Deliver two completed copies to separate custodians. | Entrega dos copias completas a custodios distintos. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.scouts` / scouts panel | none → next | Regional setting: Galilee, Sepphoris and Tiberias. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Galilee, Sepphoris and Tiberias. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.history` / history panel | none → next | Around the beginning of the third century, Judah the Prince was associated with the redaction of the Mishnah. Its transmission was a collective process. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Tradición de compilación de la Mishná y contexto de Judá el Príncipe; localización/fecha exacta de cada acto de escritura no se afirma. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.event-phase-1-complete` / o1 first becomes true | judith-copyist → next | One copy is safe. I prefer a second before congratulating anyone. | Una copia está a salvo. Prefiero una segunda antes de felicitar a nadie. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.event-phase-2-complete` / o2 first becomes true | judith-copyist → next | A margin is not wasted space. Sometimes it holds the disagreement we must keep. | Un margen no es espacio perdido. A veces guarda la discrepancia que debemos conservar. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.event-phase-3-complete` / o3 first becomes true | judith-copyist → next | Send them by separate roads. A living tradition needs more than one keeper. | Envíalas por caminos separados. Una tradición viva necesita más de un guardián. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | judith-copyist → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.victory-fact` / victory latch first | collection-narrator → next | Around the beginning of the third century, Judah the Prince was associated with the redaction of the Mishnah. Its transmission was a collective process. Your mission task is complete; this outcome does not change the documented events. | Los contadores representan logística, no una puntuación de ortodoxia religiosa. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.victory-personal` / after victory-fact | judith-copyist → 03-the-river-quarter | Send them by separate roads. A living tradition needs more than one keeper. | Envíalas por caminos separados. Una tradición viva necesita más de un guardián. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.recovery` / 6 minutes without objective progress | judith-copyist → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-1-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Recover both separate copies from the teaching-copy shelves and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de los estantes de copias de enseñanza y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-1-completed` / 02-the-hill-and-the-school.side-1.completed latched; once | judith-copyist → return-to-game | Optional task completed: What the Fire Must Not Take — the teaching-copy shelves. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: Lo que el fuego no debe llevarse — los estantes de copias de enseñanza. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-1-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-2-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Pay 50 wood and restore the damaged store of the western archive store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el almacén del archivo occidental. Ventaja: 200 de alimento, 100 de madera, una vez. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-2-completed` / 02-the-hill-and-the-school.side-2.completed latched; once | judith-copyist → return-to-game | Optional task completed: Raise the Store Again — the western archive store. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: Levantar de nuevo el almacén — el almacén del archivo occidental. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-2-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-3-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Escort the trader of the Galilean hill road to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de la calzada de las colinas de Galilea hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-3-completed` / 02-the-hill-and-the-school.side-3.completed latched; once | judith-copyist → return-to-game | Optional task completed: One Honest Consignment — the Galilean hill road. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: Una remesa honrada — la calzada de las colinas de Galilea. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-3-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-4-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Escort the local guide of the settlement footpaths to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de las sendas entre poblados hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-4-completed` / 02-the-hill-and-the-school.side-4.completed latched; once | judith-copyist → return-to-game | Optional task completed: The Path Between — the settlement footpaths. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: El camino entre ambos — las sendas entre poblados. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-4-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-5-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Bring each of the two aid crates to its assigned household at the study-house households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares de las casas de estudio. Ventaja: 100 de alimento, 50 de madera, una vez. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-5-completed` / 02-the-hill-and-the-school.side-5.completed latched; once | judith-copyist → return-to-game | Optional task completed: A Place at the Hearth — the study-house households. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: Un lugar junto al hogar — los hogares de las casas de estudio. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-5-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-6-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Scout both marked viewpoints of the lake-facing road junctions. Benefit: reveal the second reserve approach. | Explora los dos miradores señalados de los cruces de camino orientados al lago. Ventaja: revela la aproximación de la segunda reserva. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-6-completed` / 02-the-hill-and-the-school.side-6.completed latched; once | judith-copyist → return-to-game | Optional task completed: The Road Seen First — the lake-facing road junctions. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: El camino visto primero — los cruces de camino orientados al lago. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.02-the-hill-and-the-school.side-6-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |

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
