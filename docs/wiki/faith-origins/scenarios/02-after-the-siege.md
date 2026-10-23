# A Road Beyond the Walls / Un camino más allá de los muros

`faith-origins/02-after-the-siege` · 70 CE · civilian-evacuation

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/faith-origins/02-after-the-siege.svg)

## Historical frame and outcome

Jerusalem and its Temple were destroyed in 70. A later Christian account describes refuge at Pella; its details remain debated.

La destrucción de Jerusalén es histórica; la tradición cristiana sobre Pella es posterior y discutida en sus detalles. El convoy de familias mixtas es dramatización.

La ciudad y el Templo caen; salvar familias ficticias no cambia ese resultado.

- [Eusebius, Church History III](https://www.newadvent.org/fathers/250103.htm): III.5: tradición de Pella; testimonio posterior. La narración de la huida a Pella no acredita la ruta ni a todos los habitantes.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

One bundle names a place of refuge. It does not name everyone who failed to reach it. I will not fill that silence with certainty.

Un legajo nombra un refugio. No nombra a todos los que no llegaron. No llenaré ese silencio con certeza.

## Geography and map construction

Jerusalem and approaches — 320 × 320 tiles; north-up design controls [35.12, 31.7, 35.3, 31.86].

Meseta calcárea mediterránea; olivares discontinuos, no selva.

Valle del Cedrón al este; barranco, no río navegable.

Monte de los Olivos al este; valles al sur y oeste.

Accesos norte, oeste y camino oriental; preservar relación entre meseta y valles.

Exclude: No Cúpula de la Roca antes de 691 ni murallas otomanas de 1537.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Temple platform | [35.235, 31.778] | [197.33, 163.06] |
| Mount of Olives ridge | [35.245, 31.779] | [212.46, 161.28] |
| Southern valley road | [35.23, 31.75] | [189.77, 212.9] |

```json
{
  "bbox": [
    35.12,
    31.7,
    35.3,
    31.86
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Temple platform",
      "lonLat": [
        35.235,
        31.778
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        197.33,
        163.06
      ]
    },
    {
      "id": "anchor-2",
      "name": "Mount of Olives ridge",
      "lonLat": [
        35.245,
        31.779
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        212.46,
        161.28
      ]
    },
    {
      "id": "anchor-3",
      "name": "Southern valley road",
      "lonLat": [
        35.23,
        31.75
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        189.77,
        212.9
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-2",
      "centre": [
        212.46,
        161.28
      ],
      "purpose": {
        "en": "Open the eastern evacuation corridor.",
        "es-ES": "Abre el corredor oriental de evacuación."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-2",
      "centre": [
        212.46,
        161.28
      ],
      "purpose": {
        "en": "Escort at least six of eight family groups to the ridge refuge.",
        "es-ES": "Escolta al menos seis de ocho grupos familiares al refugio de la cresta."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-3",
      "centre": [
        189.77,
        212.9
      ],
      "purpose": {
        "en": "Carry the surviving archive to the road beyond the siege.",
        "es-ES": "Lleva el archivo superviviente al camino más allá del asedio."
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
          212.46,
          161.28
        ],
        [
          212.46,
          161.28
        ],
        [
          189.77,
          212.9
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          212.46,
          161.28
        ],
        [
          220.46,
          169.28
        ],
        [
          212.46,
          161.28
        ],
        [
          189.77,
          212.9
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "jerusalem",
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
  "asset": "docs/design/maps/faith-origins/02-after-the-siege.svg",
  "mainRouteLengthStraightTiles": 65.64,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        194.46,
        173.28
      ],
      [
        230.46,
        173.28
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
        "en": "Open the eastern evacuation corridor.",
        "es-ES": "Abre el corredor oriental de evacuación."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-after-the-siege.o1",
        "oncePerEntity": true,
        "required": 1
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "secure-corridor",
      "threshold": 1,
      "entities": [
        {
          "id": "02-after-the-siege.east-access-blocker.1",
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
          "id": "02-after-the-siege.o1.main-access-blocker.1",
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
        "operation": "secure-corridor",
        "requiredCount": 1,
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
              "02-after-the-siege.o1.main-access.1"
            ],
            "blockingEnemies": [
              "02-after-the-siege.o1.main-access-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          },
          {
            "id": "east-access",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "02-after-the-siege.east-access.1"
            ],
            "blockingEnemies": [
              "02-after-the-siege.east-access-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          }
        ],
        "requiredLedgers": [
          "main-access",
          "east-access"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Escort at least six of eight family groups to the ridge refuge.",
        "es-ES": "Escolta al menos seis de ocho grupos familiares al refugio de la cresta."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-after-the-siege.o2",
        "oncePerEntity": true,
        "required": 6
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "evacuate-family",
      "threshold": 6,
      "entities": [
        {
          "id": "02-after-the-siege.family.1",
          "role": "civilian-party",
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
          "id": "02-after-the-siege.family.2",
          "role": "civilian-party",
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
          "id": "02-after-the-siege.family.3",
          "role": "civilian-party",
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
          "id": "02-after-the-siege.family.4",
          "role": "civilian-party",
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
          "id": "02-after-the-siege.family.5",
          "role": "civilian-party",
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
          "id": "02-after-the-siege.family.6",
          "role": "civilian-party",
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
          "id": "02-after-the-siege.family.7",
          "role": "civilian-party",
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
          "id": "02-after-the-siege.family.8",
          "role": "civilian-party",
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
          "id": "02-after-the-siege.ridge-refuge-blocker.1",
          "role": "military-guard",
          "initialHub": "hub-2",
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
          "atHub": "hub-2"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "evacuate-family",
        "requiredCount": 6,
        "destination": "hub-2",
        "defeatBelowRemaining": 6,
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "families-arrived",
            "kind": "entity-state",
            "state": "arrived",
            "entities": [
              "02-after-the-siege.family.1",
              "02-after-the-siege.family.2",
              "02-after-the-siege.family.3",
              "02-after-the-siege.family.4",
              "02-after-the-siege.family.5",
              "02-after-the-siege.family.6",
              "02-after-the-siege.family.7",
              "02-after-the-siege.family.8"
            ],
            "requiredCount": 6,
            "oncePerEntity": true,
            "destinations": {
              "02-after-the-siege.family.1": "02-after-the-siege.o2.families-arrived.receiving-zone",
              "02-after-the-siege.family.2": "02-after-the-siege.o2.families-arrived.receiving-zone",
              "02-after-the-siege.family.3": "02-after-the-siege.o2.families-arrived.receiving-zone",
              "02-after-the-siege.family.4": "02-after-the-siege.o2.families-arrived.receiving-zone",
              "02-after-the-siege.family.5": "02-after-the-siege.o2.families-arrived.receiving-zone",
              "02-after-the-siege.family.6": "02-after-the-siege.o2.families-arrived.receiving-zone",
              "02-after-the-siege.family.7": "02-after-the-siege.o2.families-arrived.receiving-zone",
              "02-after-the-siege.family.8": "02-after-the-siege.o2.families-arrived.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "ridge-refuge",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "02-after-the-siege.ridge-refuge.1"
            ],
            "blockingEnemies": [
              "02-after-the-siege.ridge-refuge-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          }
        ],
        "requiredLedgers": [
          "families-arrived",
          "ridge-refuge"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Carry the surviving archive to the road beyond the siege.",
        "es-ES": "Lleva el archivo superviviente al camino más allá del asedio."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-after-the-siege.o3",
        "oncePerEntity": true,
        "required": 1
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-record",
      "threshold": 1,
      "entities": [
        {
          "id": "02-after-the-siege.o3.main-entities.1",
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
        "operation": "deliver-record",
        "requiredCount": 1,
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
              "02-after-the-siege.o3.main-entities.1"
            ],
            "requiredCount": 1,
            "oncePerEntity": true,
            "destinations": {
              "02-after-the-siege.o3.main-entities.1": "02-after-the-siege.o3.main-entities.receiving-zone"
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
        "id": "02-after-the-siege.east-access-blocker.1",
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
        "id": "02-after-the-siege.family.1",
        "role": "civilian-party",
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
        "id": "02-after-the-siege.family.2",
        "role": "civilian-party",
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
        "id": "02-after-the-siege.family.3",
        "role": "civilian-party",
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
        "id": "02-after-the-siege.family.4",
        "role": "civilian-party",
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
        "id": "02-after-the-siege.family.5",
        "role": "civilian-party",
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
        "id": "02-after-the-siege.family.6",
        "role": "civilian-party",
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
        "id": "02-after-the-siege.family.7",
        "role": "civilian-party",
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
        "id": "02-after-the-siege.family.8",
        "role": "civilian-party",
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
        "id": "02-after-the-siege.ridge-refuge-blocker.1",
        "role": "military-guard",
        "initialHub": "hub-2",
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
        "id": "02-after-the-siege.o3.main-entities.1",
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
        "id": "02-after-the-siege.o1.main-access-blocker.1",
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
        "id": "02-after-the-siege.east-access.1",
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
        "id": "02-after-the-siege.ridge-refuge.1",
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
        "id": "02-after-the-siege.o2.families-arrived.receiving-zone",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid ground within geographic district; receiving zone excludes origins",
        "protectedCivilian": false
      },
      {
        "id": "02-after-the-siege.o3.main-entities.receiving-zone",
        "hub": "hub-3",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid ground within geographic district; receiving zone excludes origins",
        "protectedCivilian": false
      },
      {
        "id": "02-after-the-siege.o1.main-access.1",
        "hub": "hub-1",
        "offsetTiles": [
          -8,
          -4
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
    "survivorGroups": [
      {
        "entities": [
          "02-after-the-siege.family.1",
          "02-after-the-siege.family.2",
          "02-after-the-siege.family.3",
          "02-after-the-siege.family.4",
          "02-after-the-siege.family.5",
          "02-after-the-siege.family.6",
          "02-after-the-siege.family.7",
          "02-after-the-siege.family.8"
        ],
        "minimumAliveOrAlreadySafe": 6,
        "loss": "defeat only when live + already safely delivered distinct IDs fall below minimum"
      }
    ],
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
      "kind": "extract",
      "title": {
        "en": "Those Who Choose to Leave — the eastern refuge quarter",
        "es-ES": "Quienes eligen marcharse — el barrio del refugio oriental"
      },
      "subject": {
        "en": "the eastern refuge quarter",
        "es-ES": "el barrio del refugio oriental"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of A Road Beyond the Walls supports this bounded fictional local task. It concerns the eastern refuge quarter; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Un camino más allá de los muros permite esta tarea local ficticia y limitada. Se ocupa de el barrio del refugio oriental; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Bring both voluntary evacuee groups from the eastern refuge quarter to the receiving refuge alive. Benefit: 100 food, 25 gold, once.",
        "es-ES": "Lleva con vida los dos grupos de evacuados voluntarios de el barrio del refugio oriental al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez."
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
              "02-after-the-siege.side-1.entity-1",
              "02-after-the-siege.side-1.entity-2"
            ],
            "destinations": {
              "02-after-the-siege.side-1.entity-1": "02-after-the-siege.side-1.zone-1",
              "02-after-the-siege.side-1.entity-2": "02-after-the-siege.side-1.zone-1"
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
            "id": "02-after-the-siege.side-1.entity-1",
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
            "id": "02-after-the-siege.side-1.entity-2",
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
            "id": "02-after-the-siege.side-1.zone-1",
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
          "onceFlag": "02-after-the-siege.side-1.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "02-after-the-siege.side-1.completed",
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
      "kind": "aid",
      "title": {
        "en": "A Place at the Hearth — the displaced households",
        "es-ES": "Un lugar junto al hogar — los hogares desplazados"
      },
      "subject": {
        "en": "the displaced households",
        "es-ES": "los hogares desplazados"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of A Road Beyond the Walls supports this bounded fictional local task. It concerns the displaced households; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Un camino más allá de los muros permite esta tarea local ficticia y limitada. Se ocupa de los hogares desplazados; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Bring each of the two aid crates to its assigned household at the displaced households. Benefit: 100 food, 50 wood, once.",
        "es-ES": "Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares desplazados. Ventaja: 100 de alimento, 50 de madera, una vez."
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
              "02-after-the-siege.side-2.entity-1",
              "02-after-the-siege.side-2.entity-2"
            ],
            "destinations": {
              "02-after-the-siege.side-2.entity-1": "02-after-the-siege.side-2.zone-1",
              "02-after-the-siege.side-2.entity-2": "02-after-the-siege.side-2.zone-2"
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
            "id": "02-after-the-siege.side-2.entity-1",
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
            "id": "02-after-the-siege.side-2.entity-2",
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
            "id": "02-after-the-siege.side-2.zone-1",
            "hub": "hub-2",
            "offsetTiles": [
              -8,
              0
            ],
            "radiusTiles": 3
          },
          {
            "id": "02-after-the-siege.side-2.zone-2",
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
          "onceFlag": "02-after-the-siege.side-2.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "02-after-the-siege.side-2.completed",
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
      "id": "side-3",
      "kind": "copy",
      "title": {
        "en": "What the Fire Must Not Take — the family-name archive",
        "es-ES": "Lo que el fuego no debe llevarse — el archivo de nombres familiares"
      },
      "subject": {
        "en": "the family-name archive",
        "es-ES": "el archivo de nombres familiares"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of A Road Beyond the Walls supports this bounded fictional local task. It concerns the family-name archive; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Un camino más allá de los muros permite esta tarea local ficticia y limitada. Se ocupa de el archivo de nombres familiares; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Recover both separate copies from the family-name archive and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.",
        "es-ES": "Recupera las dos copias distintas de el archivo de nombres familiares y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal."
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
              "02-after-the-siege.side-3.entity-1",
              "02-after-the-siege.side-3.entity-2"
            ],
            "destinations": {
              "02-after-the-siege.side-3.entity-1": "02-after-the-siege.side-3.zone-1",
              "02-after-the-siege.side-3.entity-2": "02-after-the-siege.side-3.zone-1"
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
            "id": "02-after-the-siege.side-3.entity-1",
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
            "id": "02-after-the-siege.side-3.entity-2",
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
            "id": "02-after-the-siege.side-3.zone-1",
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
          "onceFlag": "02-after-the-siege.side-3.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "sourceIds": [
            "eusebius-iii"
          ],
          "historicalNote": {
            "en": "Jerusalem and its Temple were destroyed in 70. A later Christian account describes refuge at Pella; its details remain debated.",
            "es-ES": "La destrucción de Jerusalén es histórica; la tradición cristiana sobre Pella es posterior y discutida en sus detalles. El convoy de familias mixtas es dramatización."
          },
          "hint": {
            "en": "Open the eastern evacuation corridor.",
            "es-ES": "Abre el corredor oriental de evacuación."
          }
        }
      ],
      "completionFlag": "02-after-the-siege.side-3.completed",
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
      "id": "side-4",
      "kind": "guide",
      "title": {
        "en": "The Path Between — the eastern hillside",
        "es-ES": "El camino entre ambos — la ladera oriental"
      },
      "subject": {
        "en": "the eastern hillside",
        "es-ES": "la ladera oriental"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of A Road Beyond the Walls supports this bounded fictional local task. It concerns the eastern hillside; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Un camino más allá de los muros permite esta tarea local ficticia y limitada. Se ocupa de la ladera oriental; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the local guide of the eastern hillside to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.",
        "es-ES": "Escolta al guía local de la ladera oriental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga."
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
              "02-after-the-siege.side-4.entity-1"
            ],
            "destinations": {
              "02-after-the-siege.side-4.entity-1": "02-after-the-siege.side-4.zone-1"
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
            "id": "02-after-the-siege.side-4.entity-1",
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
            "id": "02-after-the-siege.side-4.zone-1",
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
          "onceFlag": "02-after-the-siege.side-4.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "corridorId": "relief"
        }
      ],
      "completionFlag": "02-after-the-siege.side-4.completed",
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
      "kind": "watch",
      "title": {
        "en": "Eyes Beyond the Gate — the city approaches",
        "es-ES": "Ojos más allá de la puerta — las aproximaciones a la ciudad"
      },
      "subject": {
        "en": "the city approaches",
        "es-ES": "las aproximaciones a la ciudad"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of A Road Beyond the Walls supports this bounded fictional local task. It concerns the city approaches; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Un camino más allá de los muros permite esta tarea local ficticia y limitada. Se ocupa de las aproximaciones a la ciudad; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Visit both observation posts overlooking the city approaches. Benefit: reveal the first and last reserve approaches.",
        "es-ES": "Visita los dos puestos de observación sobre las aproximaciones a la ciudad. Ventaja: revela las aproximaciones de la primera y la última reserva."
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
              "02-after-the-siege.side-5.zone-1",
              "02-after-the-siege.side-5.zone-2"
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
            "id": "02-after-the-siege.side-5.zone-1",
            "hub": "hub-2",
            "offsetTiles": [
              0,
              -8
            ],
            "radiusTiles": 3
          },
          {
            "id": "02-after-the-siege.side-5.zone-2",
            "hub": "hub-3",
            "offsetTiles": [
              0,
              8
            ],
            "radiusTiles": 3
          }
        ]
      },
      "effects": [
        {
          "kind": "reveal-enemy-approach",
          "target": "wave-1 and wave-3 approaches",
          "resources": {},
          "onceFlag": "02-after-the-siege.side-5.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "rosterIds": [
            "wave-1",
            "wave-3"
          ],
          "alreadyReleasedPolicy": "reveal current surviving members, never spawn a replacement"
        }
      ],
      "completionFlag": "02-after-the-siege.side-5.completed",
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
    },
    {
      "id": "side-6",
      "kind": "trade",
      "title": {
        "en": "One Honest Consignment — the refuge supply post",
        "es-ES": "Una remesa honrada — el puesto de suministros del refugio"
      },
      "subject": {
        "en": "the refuge supply post",
        "es-ES": "el puesto de suministros del refugio"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of A Road Beyond the Walls supports this bounded fictional local task. It concerns the refuge supply post; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Un camino más allá de los muros permite esta tarea local ficticia y limitada. Se ocupa de el puesto de suministros del refugio; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the trader of the refuge supply post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.",
        "es-ES": "Escolta al comerciante de el puesto de suministros del refugio hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez."
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
              "02-after-the-siege.side-6.entity-1"
            ],
            "destinations": {
              "02-after-the-siege.side-6.entity-1": "02-after-the-siege.side-6.zone-1"
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
            "receipt": "02-after-the-siege.side-6.payment",
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
            "id": "02-after-the-siege.side-6.entity-1",
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
            "id": "02-after-the-siege.side-6.zone-1",
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
          "onceFlag": "02-after-the-siege.side-6.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "02-after-the-siege.side-6.completed",
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
    }
  ],
  "secondaryBudget": {
    "reservedRewards": {
      "food": 350,
      "wood": 100,
      "gold": 25,
      "stone": 0
    },
    "maxOptionalCosts": {
      "food": 0,
      "wood": 0,
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
        "side-2",
        "side-1"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "informed-movement",
      "optionalObjectives": [
        "side-4",
        "side-5",
        "side-3"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "civilian-and-memory",
      "optionalObjectives": [
        "side-1",
        "side-2",
        "side-3"
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
| easy | 875/625/312/250 | 1885/1075/1128/550 | 16 | 15 + 15 + 15 + 18 = 63 | 120 / 474 |
| standard | 700/500/250/200 | 1820/1100/1030/600 | 12 | 21 + 21 + 21 + 21 = 84 | 90 / 370 |
| hard | 595/425/212/170 | 1805/1125/988/630 | 10 | 25 + 25 + 25 + 26 = 101 | 75 / 296 |

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
        "food": 1885,
        "wood": 1075,
        "gold": 1128,
        "stone": 550
      },
      "mandatoryDeliveries": {
        "food": 0,
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
      "enemyTotalCap": 63,
      "initialEnemy": 15,
      "waves": [
        {
          "id": "wave-1",
          "count": 15,
          "composition": {
            "militia": 7,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 474,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 15,
          "composition": {
            "militia": 7,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 948,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 18,
          "composition": {
            "militia": 7,
            "spearman": 4,
            "archer": 4,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1422,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 7,
        "spearman": 3,
        "archer": 3,
        "scoutCavalry": 2
      },
      "enemyNominalResourceCost": {
        "food": 2855,
        "wood": 650,
        "gold": 1145,
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
        "food": 2410,
        "wood": 1600,
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
        "food": 1820,
        "wood": 1100,
        "gold": 1030,
        "stone": 600
      },
      "mandatoryDeliveries": {
        "food": 0,
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
      "enemyTotalCap": 84,
      "initialEnemy": 21,
      "waves": [
        {
          "id": "wave-1",
          "count": 21,
          "composition": {
            "militia": 8,
            "spearman": 5,
            "archer": 5,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 370,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 21,
          "composition": {
            "militia": 8,
            "spearman": 5,
            "archer": 5,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 740,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 21,
          "composition": {
            "militia": 8,
            "spearman": 5,
            "archer": 5,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1110,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 8,
        "spearman": 5,
        "archer": 5,
        "scoutCavalry": 3
      },
      "enemyNominalResourceCost": {
        "food": 3580,
        "wood": 1000,
        "gold": 1540,
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
        "food": 2170,
        "wood": 1500,
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
        "food": 1805,
        "wood": 1125,
        "gold": 988,
        "stone": 630
      },
      "mandatoryDeliveries": {
        "food": 0,
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
      "enemyTotalCap": 101,
      "initialEnemy": 25,
      "waves": [
        {
          "id": "wave-1",
          "count": 25,
          "composition": {
            "militia": 9,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 296,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 25,
          "composition": {
            "militia": 9,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 592,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 26,
          "composition": {
            "militia": 10,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 888,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 9,
        "spearman": 6,
        "archer": 6,
        "scoutCavalry": 4
      },
      "enemyNominalResourceCost": {
        "food": 4340,
        "wood": 1200,
        "gold": 1820,
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
        "food": 2050,
        "wood": 1450,
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
    "worstDeliveryFood": 0,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Phase waves use the separate local phase-two supply circuit, not the whole-map journey. Two round trips +90s loading/reaction fit the floor. Validate actual nav-path/speed and recompute before game approval.",
    "minimumWaveGapSecondsFromProposedGeometry": 296,
    "wholeJourneyDistanceTiles": 56.39,
    "wholeJourneyOneWaySecondsEstimate": 81,
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
      "food": 350,
      "wood": 100,
      "gold": 25,
      "stone": 0
    },
    "maxOptionalCosts": {
      "food": 0,
      "wood": 0,
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

Dos salidas: puerta oriental y senda sur. Pérdida de dos grupos tolerada en todos los niveles; archivo tiene una copia secundaria visible.

{
  "plan": "Dos salidas: puerta oriental y senda sur. Pérdida de dos grupos tolerada en todos los niveles; archivo tiene una copia secundaria visible.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.faith-origins.02-after-the-siege.title` / always | none → next | A Road Beyond the Walls | Un camino más allá de los muros |
| `scenario.faith-origins.02-after-the-siege.fact-intro` / intro first | collection-narrator → next | Jerusalem and its Temple were destroyed in 70. A later Christian account describes refuge at Pella; its details remain debated. | La destrucción de Jerusalén es histórica; la tradición cristiana sobre Pella es posterior y discutida en sus detalles. El convoy de familias mixtas es dramatización. |
| `scenario.faith-origins.02-after-the-siege.personal-intro` / after fact-intro | miriam-archive → next | One bundle names a place of refuge. It does not name everyone who failed to reach it. I will not fill that silence with certainty. | Un legajo nombra un refugio. No nombra a todos los que no llegaron. No llenaré ese silencio con certeza. |
| `scenario.faith-origins.02-after-the-siege.objective-1` / phase-1 active | none → hub-1 | Open the eastern evacuation corridor. | Abre el corredor oriental de evacuación. |
| `scenario.faith-origins.02-after-the-siege.objective-2` / phase-2 active | none → hub-2 | Escort at least six of eight family groups to the ridge refuge. | Escolta al menos seis de ocho grupos familiares al refugio de la cresta. |
| `scenario.faith-origins.02-after-the-siege.objective-3` / phase-3 active | none → hub-3 | Carry the surviving archive to the road beyond the siege. | Lleva el archivo superviviente al camino más allá del asedio. |
| `scenario.faith-origins.02-after-the-siege.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.faith-origins.02-after-the-siege.scouts` / scouts panel | none → next | Regional setting: Jerusalem and approaches. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Jerusalem and approaches. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.faith-origins.02-after-the-siege.history` / history panel | none → next | Jerusalem and its Temple were destroyed in 70. A later Christian account describes refuge at Pella; its details remain debated. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | La destrucción de Jerusalén es histórica; la tradición cristiana sobre Pella es posterior y discutida en sus detalles. El convoy de familias mixtas es dramatización. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.faith-origins.02-after-the-siege.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.faith-origins.02-after-the-siege.event-phase-1-complete` / o1 first becomes true | miriam-archive → next | I have found the first safe address. A letter can travel farther than its writer. | He encontrado la primera dirección segura. Una carta puede viajar más lejos que quien la escribe. |
| `scenario.faith-origins.02-after-the-siege.event-phase-2-complete` / o2 first becomes true | miriam-archive → next | The second bundle weighs little. Protecting it has cost us more than ink. | El segundo legajo pesa poco. Protegerlo nos ha costado más que tinta. |
| `scenario.faith-origins.02-after-the-siege.event-phase-3-complete` / o3 first becomes true | miriam-archive → next | I will record what arrived, and leave a space for what did not. | Registraré lo que llegó y dejaré un espacio para lo que no. |
| `scenario.faith-origins.02-after-the-siege.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | miriam-archive → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.faith-origins.02-after-the-siege.victory-fact` / victory latch first | collection-narrator → next | Jerusalem and its Temple were destroyed in 70. A later Christian account describes refuge at Pella; its details remain debated. Your mission task is complete; this outcome does not change the documented events. | La ciudad y el Templo caen; salvar familias ficticias no cambia ese resultado. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.faith-origins.02-after-the-siege.victory-personal` / after victory-fact | miriam-archive → 03-the-governors-question | I will record what arrived, and leave a space for what did not. | Registraré lo que llegó y dejaré un espacio para lo que no. |
| `scenario.faith-origins.02-after-the-siege.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.faith-origins.02-after-the-siege.recovery` / 6 minutes without objective progress | miriam-archive → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.faith-origins.02-after-the-siege.side-1-brief` / optional objectives tab, always available | miriam-archive → return-to-game | Bring both voluntary evacuee groups from the eastern refuge quarter to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de el barrio del refugio oriental al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| `scenario.faith-origins.02-after-the-siege.side-1-completed` / 02-after-the-siege.side-1.completed latched; once | miriam-archive → return-to-game | Optional task completed: Those Who Choose to Leave — the eastern refuge quarter. A name, a road, a household: these were the margins I learned to read. | Tarea opcional completada: Quienes eligen marcharse — el barrio del refugio oriental. Un nombre, un camino, un hogar: esos eran los márgenes que aprendí a leer. |
| `scenario.faith-origins.02-after-the-siege.side-1-unavailable` / unique optional entity irrecoverably lost; once | miriam-archive → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.faith-origins.02-after-the-siege.side-2-brief` / optional objectives tab, always available | miriam-archive → return-to-game | Bring each of the two aid crates to its assigned household at the displaced households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares desplazados. Ventaja: 100 de alimento, 50 de madera, una vez. |
| `scenario.faith-origins.02-after-the-siege.side-2-completed` / 02-after-the-siege.side-2.completed latched; once | miriam-archive → return-to-game | Optional task completed: A Place at the Hearth — the displaced households. A name, a road, a household: these were the margins I learned to read. | Tarea opcional completada: Un lugar junto al hogar — los hogares desplazados. Un nombre, un camino, un hogar: esos eran los márgenes que aprendí a leer. |
| `scenario.faith-origins.02-after-the-siege.side-2-unavailable` / unique optional entity irrecoverably lost; once | miriam-archive → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.faith-origins.02-after-the-siege.side-3-brief` / optional objectives tab, always available | miriam-archive → return-to-game | Recover both separate copies from the family-name archive and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de el archivo de nombres familiares y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| `scenario.faith-origins.02-after-the-siege.side-3-completed` / 02-after-the-siege.side-3.completed latched; once | miriam-archive → return-to-game | Optional task completed: What the Fire Must Not Take — the family-name archive. A name, a road, a household: these were the margins I learned to read. | Tarea opcional completada: Lo que el fuego no debe llevarse — el archivo de nombres familiares. Un nombre, un camino, un hogar: esos eran los márgenes que aprendí a leer. |
| `scenario.faith-origins.02-after-the-siege.side-3-unavailable` / unique optional entity irrecoverably lost; once | miriam-archive → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.faith-origins.02-after-the-siege.side-4-brief` / optional objectives tab, always available | miriam-archive → return-to-game | Escort the local guide of the eastern hillside to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de la ladera oriental hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| `scenario.faith-origins.02-after-the-siege.side-4-completed` / 02-after-the-siege.side-4.completed latched; once | miriam-archive → return-to-game | Optional task completed: The Path Between — the eastern hillside. A name, a road, a household: these were the margins I learned to read. | Tarea opcional completada: El camino entre ambos — la ladera oriental. Un nombre, un camino, un hogar: esos eran los márgenes que aprendí a leer. |
| `scenario.faith-origins.02-after-the-siege.side-4-unavailable` / unique optional entity irrecoverably lost; once | miriam-archive → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.faith-origins.02-after-the-siege.side-5-brief` / optional objectives tab, always available | miriam-archive → return-to-game | Visit both observation posts overlooking the city approaches. Benefit: reveal the first and last reserve approaches. | Visita los dos puestos de observación sobre las aproximaciones a la ciudad. Ventaja: revela las aproximaciones de la primera y la última reserva. |
| `scenario.faith-origins.02-after-the-siege.side-5-completed` / 02-after-the-siege.side-5.completed latched; once | miriam-archive → return-to-game | Optional task completed: Eyes Beyond the Gate — the city approaches. A name, a road, a household: these were the margins I learned to read. | Tarea opcional completada: Ojos más allá de la puerta — las aproximaciones a la ciudad. Un nombre, un camino, un hogar: esos eran los márgenes que aprendí a leer. |
| `scenario.faith-origins.02-after-the-siege.side-5-unavailable` / unique optional entity irrecoverably lost; once | miriam-archive → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.faith-origins.02-after-the-siege.side-6-brief` / optional objectives tab, always available | miriam-archive → return-to-game | Escort the trader of the refuge supply post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de el puesto de suministros del refugio hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| `scenario.faith-origins.02-after-the-siege.side-6-completed` / 02-after-the-siege.side-6.completed latched; once | miriam-archive → return-to-game | Optional task completed: One Honest Consignment — the refuge supply post. A name, a road, a household: these were the margins I learned to read. | Tarea opcional completada: Una remesa honrada — el puesto de suministros del refugio. Un nombre, un camino, un hogar: esos eran los márgenes que aprendí a leer. |
| `scenario.faith-origins.02-after-the-siege.side-6-unavailable` / unique optional entity irrecoverably lost; once | miriam-archive → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |

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
