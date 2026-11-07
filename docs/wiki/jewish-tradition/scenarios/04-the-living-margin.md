# The Living Margin / El margen vivo

`jewish-tradition/04-the-living-margin` · c. 400–425 CE · distributed-preservation

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/jewish-tradition/04-the-living-margin.svg)

## Historical frame and outcome

Late antique Galilee was a centre of Jewish learning and transmission. The formation of its texts cannot be reduced to a single securely dated closing ceremony.

Galilea sigue siendo un centro de aprendizaje. Fecha exacta de cierre del Talmud de Jerusalén discutida; el final del juego es límite editorial.

Termina un volumen; se ofrece volver a C00 o perspectivas paralelas C01, sin una sucesora judía ya autorizada.

- [UNESCO, Necropolis of Bet Shearim](https://whc.unesco.org/en/list/1471/): Contexto de renovación judía y Judá el Príncipe. Necrópolis y transmisión cultural, no prueba de una aventura del protagonista.
- [Wilhelm Bacher, Talmud (Jewish Encyclopedia)](https://www.jewishencyclopedia.com/articles/14213-talmud): Palestinian Talmud and Date of Redaction sections. Older synthesis; competing stages/redactions must not become an exact universally agreed closing date.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

This shore is the one I know. Even here, I can promise only what I have copied—not the final word of everyone who studied beside it.

Esta orilla sí la conozco. Incluso aquí solo respondo de lo que he copiado, no de la última palabra de todos los que estudiaron a su lado.

## Geography and map construction

Galilee, Sepphoris and Tiberias — 360 × 360 tiles; north-up design controls [35.113, 32.6, 35.65, 32.95].

Galilea con colinas cultivadas y asentamientos; costa del lago interior.

Mar de Galilea al este; Jordán sale hacia sur, no al Mediterráneo.

Seforis al oeste elevada; Tiberíades en costa occidental del lago.

Camino de mesetas hacia Tiberíades y eje de poblados.

Exclude: No mezclar aldeas separadas 30 km como barrio continuo; escala regional comprimida.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Tiberias west shore | [35.531, 32.79] | [268.74, 168.85] |
| Bet Shearim | [35.128, 32.703] | [28.19, 230.61] |
| Sepphoris area | [35.279, 32.754] | [118.32, 194.41] |

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
        268.74,
        168.85
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
        28.19,
        230.61
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
        118.32,
        194.41
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        118.32,
        194.41
      ],
      "purpose": {
        "en": "Establish two safe routes between the lake archive and hill settlements.",
        "es-ES": "Establece dos rutas seguras entre el archivo del lago y las poblaciones de las colinas."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        268.74,
        168.85
      ],
      "purpose": {
        "en": "Prepare three independent copies and provisions for their carriers.",
        "es-ES": "Prepara tres copias independientes y víveres para sus portadores."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        28.19,
        230.61
      ],
      "purpose": {
        "en": "Send the copies to three destinations without exhausting the home settlement.",
        "es-ES": "Envía las copias a tres destinos sin agotar el asentamiento de origen."
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
          118.32,
          194.41
        ],
        [
          268.74,
          168.85
        ],
        [
          28.19,
          230.61
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          118.32,
          194.41
        ],
        [
          201.53,
          189.63
        ],
        [
          268.74,
          168.85
        ],
        [
          28.19,
          230.61
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
  "asset": "docs/design/maps/jewish-tradition/04-the-living-margin.svg",
  "mainRouteLengthStraightTiles": 400.93,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        250.74,
        180.85
      ],
      [
        286.74,
        180.85
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
        "en": "Establish two safe routes between the lake archive and hill settlements.",
        "es-ES": "Establece dos rutas seguras entre el archivo del lago y las poblaciones de las colinas."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "04-the-living-margin.o1",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "secure-corridor",
      "threshold": 2,
      "entities": [
        {
          "id": "04-the-living-margin.o1.main-access-blocker.1",
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
          "id": "04-the-living-margin.o1.main-access-blocker.2",
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
        "requiredCount": 2,
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
              "04-the-living-margin.o1.main-access.1",
              "04-the-living-margin.o1.main-access.2"
            ],
            "blockingEnemies": [
              "04-the-living-margin.o1.main-access-blocker.1",
              "04-the-living-margin.o1.main-access-blocker.2"
            ],
            "requiredCount": 2,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          }
        ],
        "requiredLedgers": [
          "main-access"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Prepare three independent copies and provisions for their carriers.",
        "es-ES": "Prepara tres copias independientes y víveres para sus portadores."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "04-the-living-margin.o2",
        "oncePerEntity": true,
        "required": 3
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "prepare-copy",
      "threshold": 3,
      "entities": [
        {
          "id": "04-the-living-margin.o2.main-entities.1",
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
          "id": "04-the-living-margin.o2.main-entities.2",
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
          "id": "04-the-living-margin.o2.main-entities.3",
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
        "operation": "prepare-copy",
        "requiredCount": 3,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "food": 900
        },
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "main-entities",
            "kind": "entity-state",
            "state": "prepared",
            "entities": [
              "04-the-living-margin.o2.main-entities.1",
              "04-the-living-margin.o2.main-entities.2",
              "04-the-living-margin.o2.main-entities.3"
            ],
            "requiredCount": 3,
            "oncePerEntity": true,
            "destinations": {
              "04-the-living-margin.o2.main-entities.1": "04-the-living-margin.o2.main-entities.receiving-zone",
              "04-the-living-margin.o2.main-entities.2": "04-the-living-margin.o2.main-entities.receiving-zone",
              "04-the-living-margin.o2.main-entities.3": "04-the-living-margin.o2.main-entities.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "carrier-provisions",
            "kind": "resource-transaction",
            "amounts": {
              "food": 900
            },
            "receivingZones": [
              "04-the-living-margin.carrier-provisions-receiver.1"
            ],
            "allocations": {
              "04-the-living-margin.carrier-provisions-receiver.1": {
                "food": 900
              }
            },
            "paidFlag": "04-the-living-margin.o2.carrier-provisions.paid",
            "account": "spendable",
            "atomic": true,
            "once": true,
            "commit": "debit resources AND persist receipt in same guarded transition; repeated arrivals/save cannot repay"
          }
        ],
        "requiredLedgers": [
          "main-entities",
          "carrier-provisions"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Send the copies to three destinations without exhausting the home settlement.",
        "es-ES": "Envía las copias a tres destinos sin agotar el asentamiento de origen."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "04-the-living-margin.o3",
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
          "id": "04-the-living-margin.o2.main-entities.1",
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
          "id": "04-the-living-margin.o2.main-entities.2",
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
          "id": "04-the-living-margin.o2.main-entities.3",
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
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "main-entities",
            "kind": "entity-state",
            "state": "arrived",
            "entities": [
              "04-the-living-margin.o2.main-entities.1",
              "04-the-living-margin.o2.main-entities.2",
              "04-the-living-margin.o2.main-entities.3"
            ],
            "requiredCount": 3,
            "oncePerEntity": true,
            "destinations": {
              "04-the-living-margin.o2.main-entities.1": "04-the-living-margin.three-copy-destinations.1",
              "04-the-living-margin.o2.main-entities.2": "04-the-living-margin.three-copy-destinations.2",
              "04-the-living-margin.o2.main-entities.3": "04-the-living-margin.three-copy-destinations.3"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
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
          "main-entities",
          "keep-stock"
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
        "id": "04-the-living-margin.o2.main-entities.1",
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
        "id": "04-the-living-margin.o2.main-entities.2",
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
        "id": "04-the-living-margin.o2.main-entities.3",
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
        "id": "04-the-living-margin.o1.main-access-blocker.1",
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
        "id": "04-the-living-margin.o1.main-access-blocker.2",
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
        "id": "04-the-living-margin.carrier-provisions-receiver.1",
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
        "id": "04-the-living-margin.three-copy-destinations.1",
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
        "id": "04-the-living-margin.three-copy-destinations.2",
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
        "id": "04-the-living-margin.three-copy-destinations.3",
        "hub": "hub-3",
        "offsetTiles": [
          -8,
          0
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": false
      },
      {
        "id": "04-the-living-margin.o2.main-entities.receiving-zone",
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
        "id": "04-the-living-margin.o1.main-access.1",
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
        "id": "04-the-living-margin.o1.main-access.2",
        "hub": "hub-1",
        "offsetTiles": [
          8,
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
        "en": "What the Fire Must Not Take — the dispersed teaching copies",
        "es-ES": "Lo que el fuego no debe llevarse — las copias de enseñanza dispersas"
      },
      "subject": {
        "en": "the dispersed teaching copies",
        "es-ES": "las copias de enseñanza dispersas"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Living Margin supports this bounded fictional local task. It concerns the dispersed teaching copies; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El margen vivo permite esta tarea local ficticia y limitada. Se ocupa de las copias de enseñanza dispersas; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Recover both separate copies from the dispersed teaching copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.",
        "es-ES": "Recupera las dos copias distintas de las copias de enseñanza dispersas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal."
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
              "04-the-living-margin.side-1.entity-1",
              "04-the-living-margin.side-1.entity-2"
            ],
            "destinations": {
              "04-the-living-margin.side-1.entity-1": "04-the-living-margin.side-1.zone-1",
              "04-the-living-margin.side-1.entity-2": "04-the-living-margin.side-1.zone-1"
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
            "id": "04-the-living-margin.side-1.entity-1",
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
            "id": "04-the-living-margin.side-1.entity-2",
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
            "id": "04-the-living-margin.side-1.zone-1",
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
          "onceFlag": "04-the-living-margin.side-1.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "sourceIds": [
            "beth-shearim",
            "talmud-transmission"
          ],
          "historicalNote": {
            "en": "Late antique Galilee was a centre of Jewish learning and transmission. The formation of its texts cannot be reduced to a single securely dated closing ceremony.",
            "es-ES": "Galilea sigue siendo un centro de aprendizaje. Fecha exacta de cierre del Talmud de Jerusalén discutida; el final del juego es límite editorial."
          },
          "hint": {
            "en": "Establish two safe routes between the lake archive and hill settlements.",
            "es-ES": "Establece dos rutas seguras entre el archivo del lago y las poblaciones de las colinas."
          }
        }
      ],
      "completionFlag": "04-the-living-margin.side-1.completed",
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
      "kind": "guide",
      "title": {
        "en": "The Path Between — the lake-to-hill path",
        "es-ES": "El camino entre ambos — la senda del lago a las colinas"
      },
      "subject": {
        "en": "the lake-to-hill path",
        "es-ES": "la senda del lago a las colinas"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Living Margin supports this bounded fictional local task. It concerns the lake-to-hill path; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El margen vivo permite esta tarea local ficticia y limitada. Se ocupa de la senda del lago a las colinas; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the local guide of the lake-to-hill path to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.",
        "es-ES": "Escolta al guía local de la senda del lago a las colinas hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga."
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
              "04-the-living-margin.side-2.entity-1"
            ],
            "destinations": {
              "04-the-living-margin.side-2.entity-1": "04-the-living-margin.side-2.zone-1"
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
            "id": "04-the-living-margin.side-2.entity-1",
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
            "id": "04-the-living-margin.side-2.zone-1",
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
          "onceFlag": "04-the-living-margin.side-2.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "corridorId": "relief"
        }
      ],
      "completionFlag": "04-the-living-margin.side-2.completed",
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
      "id": "side-3",
      "kind": "repair",
      "title": {
        "en": "Raise the Store Again — the hill archive store",
        "es-ES": "Levantar de nuevo el almacén — el almacén del archivo de las colinas"
      },
      "subject": {
        "en": "the hill archive store",
        "es-ES": "el almacén del archivo de las colinas"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Living Margin supports this bounded fictional local task. It concerns the hill archive store; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El margen vivo permite esta tarea local ficticia y limitada. Se ocupa de el almacén del archivo de las colinas; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Pay 50 wood and restore the damaged store of the hill archive store to full health. Benefit: 200 food, 100 wood, once.",
        "es-ES": "Paga 50 de madera y repara por completo el almacén dañado de el almacén del archivo de las colinas. Ventaja: 200 de alimento, 100 de madera, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-health",
            "entity": "04-the-living-margin.side-3.entity-1",
            "health": "full",
            "paymentReceipt": "04-the-living-margin.side-3.payment",
            "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
          },
          {
            "kind": "atomic-payment",
            "resources": {
              "wood": 50
            },
            "receipt": "04-the-living-margin.side-3.payment",
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
            "id": "04-the-living-margin.side-3.entity-1",
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
            "id": "04-the-living-margin.side-3.zone-1",
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
          "onceFlag": "04-the-living-margin.side-3.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "04-the-living-margin.side-3.completed",
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
      "id": "side-4",
      "kind": "aid",
      "title": {
        "en": "A Place at the Hearth — the lake households",
        "es-ES": "Un lugar junto al hogar — los hogares del lago"
      },
      "subject": {
        "en": "the lake households",
        "es-ES": "los hogares del lago"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Living Margin supports this bounded fictional local task. It concerns the lake households; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El margen vivo permite esta tarea local ficticia y limitada. Se ocupa de los hogares del lago; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Bring each of the two aid crates to its assigned household at the lake households. Benefit: 100 food, 50 wood, once.",
        "es-ES": "Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares del lago. Ventaja: 100 de alimento, 50 de madera, una vez."
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
              "04-the-living-margin.side-4.entity-1",
              "04-the-living-margin.side-4.entity-2"
            ],
            "destinations": {
              "04-the-living-margin.side-4.entity-1": "04-the-living-margin.side-4.zone-1",
              "04-the-living-margin.side-4.entity-2": "04-the-living-margin.side-4.zone-2"
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
            "id": "04-the-living-margin.side-4.entity-1",
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
            "id": "04-the-living-margin.side-4.entity-2",
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
            "id": "04-the-living-margin.side-4.zone-1",
            "hub": "hub-2",
            "offsetTiles": [
              -8,
              0
            ],
            "radiusTiles": 3
          },
          {
            "id": "04-the-living-margin.side-4.zone-2",
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
          "onceFlag": "04-the-living-margin.side-4.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "04-the-living-margin.side-4.completed",
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
        "en": "One Honest Consignment — the hill settlement post",
        "es-ES": "Una remesa honrada — el puesto del poblado de las colinas"
      },
      "subject": {
        "en": "the hill settlement post",
        "es-ES": "el puesto del poblado de las colinas"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Living Margin supports this bounded fictional local task. It concerns the hill settlement post; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El margen vivo permite esta tarea local ficticia y limitada. Se ocupa de el puesto del poblado de las colinas; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the trader of the hill settlement post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.",
        "es-ES": "Escolta al comerciante de el puesto del poblado de las colinas hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez."
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
              "04-the-living-margin.side-5.entity-1"
            ],
            "destinations": {
              "04-the-living-margin.side-5.entity-1": "04-the-living-margin.side-5.zone-1"
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
            "receipt": "04-the-living-margin.side-5.payment",
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
            "id": "04-the-living-margin.side-5.entity-1",
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
            "id": "04-the-living-margin.side-5.zone-1",
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
          "onceFlag": "04-the-living-margin.side-5.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "04-the-living-margin.side-5.completed",
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
      "kind": "extract",
      "title": {
        "en": "Those Who Choose to Leave — the travelling copyists families",
        "es-ES": "Quienes eligen marcharse — las familias de copistas itinerantes"
      },
      "subject": {
        "en": "the travelling copyists families",
        "es-ES": "las familias de copistas itinerantes"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of The Living Margin supports this bounded fictional local task. It concerns the travelling copyists families; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de El margen vivo permite esta tarea local ficticia y limitada. Se ocupa de las familias de copistas itinerantes; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Bring both voluntary evacuee groups from the travelling copyists families to the receiving refuge alive. Benefit: 100 food, 25 gold, once.",
        "es-ES": "Lleva con vida los dos grupos de evacuados voluntarios de las familias de copistas itinerantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez."
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
              "04-the-living-margin.side-6.entity-1",
              "04-the-living-margin.side-6.entity-2"
            ],
            "destinations": {
              "04-the-living-margin.side-6.entity-1": "04-the-living-margin.side-6.zone-1",
              "04-the-living-margin.side-6.entity-2": "04-the-living-margin.side-6.zone-1"
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
            "id": "04-the-living-margin.side-6.entity-1",
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
            "id": "04-the-living-margin.side-6.entity-2",
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
            "id": "04-the-living-margin.side-6.zone-1",
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
          "onceFlag": "04-the-living-margin.side-6.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "04-the-living-margin.side-6.completed",
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
        "side-3",
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
        "side-2",
        "side-1"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "civilian-and-memory",
      "optionalObjectives": [
        "side-6",
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
| easy | 875/625/312/250 | 2785/1075/1128/550 | 16 | 8 + 8 + 8 + 8 = 32 | 120 / 474 |
| standard | 700/500/250/200 | 2720/1100/1030/600 | 12 | 10 + 10 + 10 + 12 = 42 | 90 / 370 |
| hard | 595/425/212/170 | 2705/1125/988/630 | 10 | 12 + 12 + 12 + 14 = 50 | 75 / 296 |

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
        "food": 2785,
        "wood": 1075,
        "gold": 1128,
        "stone": 550
      },
      "mandatoryDeliveries": {
        "food": 900,
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
      "enemyTotalCap": 32,
      "initialEnemy": 8,
      "waves": [
        {
          "id": "wave-1",
          "count": 8,
          "composition": {
            "militia": 3,
            "spearman": 2,
            "archer": 2,
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
          "count": 8,
          "composition": {
            "militia": 3,
            "spearman": 2,
            "archer": 2,
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
          "count": 8,
          "composition": {
            "militia": 3,
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
        "spearman": 2,
        "archer": 2,
        "scoutCavalry": 1
      },
      "enemyNominalResourceCost": {
        "food": 1320,
        "wood": 400,
        "gold": 600,
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
        30,
        65
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
        "food": 2720,
        "wood": 1100,
        "gold": 1030,
        "stone": 600
      },
      "mandatoryDeliveries": {
        "food": 900,
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
      "enemyTotalCap": 42,
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
          "offsetSeconds": 370,
          "warningSeconds": 90,
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
          "offsetSeconds": 740,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 12,
          "composition": {
            "militia": 4,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1110,
          "warningSeconds": 90,
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
        "food": 1855,
        "wood": 450,
        "gold": 785,
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
        30,
        65
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
        "food": 2705,
        "wood": 1125,
        "gold": 988,
        "stone": 630
      },
      "mandatoryDeliveries": {
        "food": 900,
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
      "enemyTotalCap": 50,
      "initialEnemy": 12,
      "waves": [
        {
          "id": "wave-1",
          "count": 12,
          "composition": {
            "militia": 4,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 296,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 12,
          "composition": {
            "militia": 4,
            "spearman": 3,
            "archer": 3,
            "scoutCavalry": 2
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 592,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 14,
          "composition": {
            "militia": 6,
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
        "militia": 4,
        "spearman": 3,
        "archer": 3,
        "scoutCavalry": 2
      },
      "enemyNominalResourceCost": {
        "food": 2140,
        "wood": 600,
        "gold": 900,
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
        30,
        65
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
    "worstDeliveryFood": 900,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Phase waves use the separate local phase-two supply circuit, not the whole-map journey. Two round trips +90s loading/reaction fit the floor. Validate actual nav-path/speed and recompute before game approval.",
    "minimumWaveGapSecondsFromProposedGeometry": 296,
    "wholeJourneyDistanceTiles": 400.93,
    "wholeJourneyOneWaySecondsEstimate": 573,
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

Copias no desaparecen por idioma ni orden de entrega. Ruta terrestre alternativa a muelle; al menos dos centros productivos disponibles.

{
  "plan": "Copias no desaparecen por idioma ni orden de entrega. Ruta terrestre alternativa a muelle; al menos dos centros productivos disponibles.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.jewish-tradition.04-the-living-margin.title` / always | none → next | The Living Margin | El margen vivo |
| `scenario.jewish-tradition.04-the-living-margin.fact-intro` / intro first | collection-narrator → next | Late antique Galilee was a centre of Jewish learning and transmission. The formation of its texts cannot be reduced to a single securely dated closing ceremony. | Galilea sigue siendo un centro de aprendizaje. Fecha exacta de cierre del Talmud de Jerusalén discutida; el final del juego es límite editorial. |
| `scenario.jewish-tradition.04-the-living-margin.personal-intro` / after fact-intro | judith-copyist → next | This shore is the one I know. Even here, I can promise only what I have copied—not the final word of everyone who studied beside it. | Esta orilla sí la conozco. Incluso aquí solo respondo de lo que he copiado, no de la última palabra de todos los que estudiaron a su lado. |
| `scenario.jewish-tradition.04-the-living-margin.objective-1` / phase-1 active | none → hub-1 | Establish two safe routes between the lake archive and hill settlements. | Establece dos rutas seguras entre el archivo del lago y las poblaciones de las colinas. |
| `scenario.jewish-tradition.04-the-living-margin.objective-2` / phase-2 active | none → hub-2 | Prepare three independent copies and provisions for their carriers. | Prepara tres copias independientes y víveres para sus portadores. |
| `scenario.jewish-tradition.04-the-living-margin.objective-3` / phase-3 active | none → hub-3 | Send the copies to three destinations without exhausting the home settlement. | Envía las copias a tres destinos sin agotar el asentamiento de origen. |
| `scenario.jewish-tradition.04-the-living-margin.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.jewish-tradition.04-the-living-margin.scouts` / scouts panel | none → next | Regional setting: Galilee, Sepphoris and Tiberias. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Galilee, Sepphoris and Tiberias. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.jewish-tradition.04-the-living-margin.history` / history panel | none → next | Late antique Galilee was a centre of Jewish learning and transmission. The formation of its texts cannot be reduced to a single securely dated closing ceremony. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Galilea sigue siendo un centro de aprendizaje. Fecha exacta de cierre del Talmud de Jerusalén discutida; el final del juego es límite editorial. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.jewish-tradition.04-the-living-margin.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.jewish-tradition.04-the-living-margin.event-phase-1-complete` / o1 first becomes true | judith-copyist → next | One copy is safe. I prefer a second before congratulating anyone. | Una copia está a salvo. Prefiero una segunda antes de felicitar a nadie. |
| `scenario.jewish-tradition.04-the-living-margin.event-phase-2-complete` / o2 first becomes true | judith-copyist → next | A margin is not wasted space. Sometimes it holds the disagreement we must keep. | Un margen no es espacio perdido. A veces guarda la discrepancia que debemos conservar. |
| `scenario.jewish-tradition.04-the-living-margin.event-phase-3-complete` / o3 first becomes true | judith-copyist → next | Send them by separate roads. A living tradition needs more than one keeper. | Envíalas por caminos separados. Una tradición viva necesita más de un guardián. |
| `scenario.jewish-tradition.04-the-living-margin.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | judith-copyist → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.jewish-tradition.04-the-living-margin.victory-fact` / victory latch first | collection-narrator → next | Late antique Galilee was a centre of Jewish learning and transmission. The formation of its texts cannot be reduced to a single securely dated closing ceremony. Your mission task is complete; this outcome does not change the documented events. | Termina un volumen; se ofrece volver a C00 o perspectivas paralelas C01, sin una sucesora judía ya autorizada. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.jewish-tradition.04-the-living-margin.victory-personal` / after victory-fact | judith-copyist → campaign ending | Send them by separate roads. A living tradition needs more than one keeper. | Envíalas por caminos separados. Una tradición viva necesita más de un guardián. |
| `scenario.jewish-tradition.04-the-living-margin.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.jewish-tradition.04-the-living-margin.recovery` / 6 minutes without objective progress | judith-copyist → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.jewish-tradition.04-the-living-margin.side-1-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Recover both separate copies from the dispersed teaching copies and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de las copias de enseñanza dispersas y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| `scenario.jewish-tradition.04-the-living-margin.side-1-completed` / 04-the-living-margin.side-1.completed latched; once | judith-copyist → return-to-game | Optional task completed: What the Fire Must Not Take — the dispersed teaching copies. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: Lo que el fuego no debe llevarse — las copias de enseñanza dispersas. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.04-the-living-margin.side-1-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.04-the-living-margin.side-2-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Escort the local guide of the lake-to-hill path to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de la senda del lago a las colinas hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| `scenario.jewish-tradition.04-the-living-margin.side-2-completed` / 04-the-living-margin.side-2.completed latched; once | judith-copyist → return-to-game | Optional task completed: The Path Between — the lake-to-hill path. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: El camino entre ambos — la senda del lago a las colinas. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.04-the-living-margin.side-2-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.04-the-living-margin.side-3-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Pay 50 wood and restore the damaged store of the hill archive store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el almacén del archivo de las colinas. Ventaja: 200 de alimento, 100 de madera, una vez. |
| `scenario.jewish-tradition.04-the-living-margin.side-3-completed` / 04-the-living-margin.side-3.completed latched; once | judith-copyist → return-to-game | Optional task completed: Raise the Store Again — the hill archive store. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: Levantar de nuevo el almacén — el almacén del archivo de las colinas. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.04-the-living-margin.side-3-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.04-the-living-margin.side-4-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Bring each of the two aid crates to its assigned household at the lake households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares del lago. Ventaja: 100 de alimento, 50 de madera, una vez. |
| `scenario.jewish-tradition.04-the-living-margin.side-4-completed` / 04-the-living-margin.side-4.completed latched; once | judith-copyist → return-to-game | Optional task completed: A Place at the Hearth — the lake households. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: Un lugar junto al hogar — los hogares del lago. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.04-the-living-margin.side-4-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.04-the-living-margin.side-5-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Escort the trader of the hill settlement post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de el puesto del poblado de las colinas hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| `scenario.jewish-tradition.04-the-living-margin.side-5-completed` / 04-the-living-margin.side-5.completed latched; once | judith-copyist → return-to-game | Optional task completed: One Honest Consignment — the hill settlement post. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: Una remesa honrada — el puesto del poblado de las colinas. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.04-the-living-margin.side-5-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.jewish-tradition.04-the-living-margin.side-6-brief` / optional objectives tab, always available | judith-copyist → return-to-game | Bring both voluntary evacuee groups from the travelling copyists families to the receiving refuge alive. Benefit: 100 food, 25 gold, once. | Lleva con vida los dos grupos de evacuados voluntarios de las familias de copistas itinerantes al refugio receptor. Ventaja: 100 de alimento, 25 de oro, una vez. |
| `scenario.jewish-tradition.04-the-living-margin.side-6-completed` / 04-the-living-margin.side-6.completed latched; once | judith-copyist → return-to-game | Optional task completed: Those Who Choose to Leave — the travelling copyists families. A spare copy is less impressive than a monument. It can last longer. | Tarea opcional completada: Quienes eligen marcharse — las familias de copistas itinerantes. Una copia de reserva impresiona menos que un monumento. Puede durar más. |
| `scenario.jewish-tradition.04-the-living-margin.side-6-unavailable` / unique optional entity irrecoverably lost; once | judith-copyist → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |

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
