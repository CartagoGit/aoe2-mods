# The Governor’s Question / La pregunta del gobernador

`faith-origins/03-the-governors-question` · c. 112 CE · administrative-intrigue

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/faith-origins/03-the-governors-question.svg)

## Historical frame and outcome

Around 112, Pliny asked Trajan how to handle accusations against Christians. Their correspondence describes policy, not universal tolerance.

Plinio y Trajano intercambian criterios de persecución. La red de mensajeros y la negociación sobre documentos son ficción acotada.

La correspondencia no impone tolerancia universal; se registra el alcance de la política.

- [Pliny and Trajan, Letters 10.96–97](https://sourcebooks.web.fordham.edu/ancient/pliny-trajan1.asp): Preguntas del gobernador y respuesta imperial. Dos cartas no prueban una persecución uniforme durante tres siglos.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

A governor’s neat question reaches us intact. The anxious voices below it do not. Those voices are the part I must reconstruct.

Nos llega intacta la pregunta pulcra de un gobernador. No las voces inquietas que quedan debajo. Esa parte debo reconstruirla.

## Geography and map construction

Nicomedia and Bithynian roads — 300 × 300 tiles; north-up design controls [29.75, 40.55, 30.25, 40.95].

Valles húmedos con cultivos, bosques periféricos y colinas.

Golfo de Nicomedia al oeste; escorrentías locales sin inventar un gran río.

Laderas norte/sur; paso principal longitudinal.

Nicomedia sobre eje costero; ramal interior separado de costa.

Exclude: Sin autovías ni costa industrial.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Nicomedia regional anchor | [29.924, 40.766] | [111.07, 138.82] |
| Gulf head | [29.91, 40.75] | [104.0, 149.5] |
| Eastern inland road | [30.12, 40.77] | [210.17, 136.15] |

```json
{
  "bbox": [
    29.75,
    40.55,
    30.25,
    40.95
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Nicomedia regional anchor",
      "lonLat": [
        29.924,
        40.766
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        111.07,
        138.82
      ]
    },
    {
      "id": "anchor-2",
      "name": "Gulf head",
      "lonLat": [
        29.91,
        40.75
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        104.0,
        149.5
      ]
    },
    {
      "id": "anchor-3",
      "name": "Eastern inland road",
      "lonLat": [
        30.12,
        40.77
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        210.17,
        136.15
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        210.17,
        136.15
      ],
      "purpose": {
        "en": "Collect the two witness records before the patrol changes.",
        "es-ES": "Recoge los dos testimonios antes del relevo de patrulla."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        111.07,
        138.82
      ],
      "purpose": {
        "en": "Deliver an authenticated petition to the governor’s office.",
        "es-ES": "Entrega una petición autenticada en la oficina del gobernador."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        104.0,
        149.5
      ],
      "purpose": {
        "en": "Lead the households to a protected route without killing the witnesses.",
        "es-ES": "Conduce a las familias a una ruta protegida sin matar a los testigos."
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
          210.17,
          136.15
        ],
        [
          111.07,
          138.82
        ],
        [
          104.0,
          149.5
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          210.17,
          136.15
        ],
        [
          168.62,
          145.49
        ],
        [
          111.07,
          138.82
        ],
        [
          104.0,
          149.5
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
  "terrainProfile": "bithynia",
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
  "asset": "docs/design/maps/faith-origins/03-the-governors-question.svg",
  "mainRouteLengthStraightTiles": 111.94,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        93.07,
        150.82
      ],
      [
        129.07,
        150.82
      ]
    ],
    "widthTiles": 6,
    "distanceTiles": 36.0,
    "placement": "fictional local supply circuit on SAME bank/plateau in receiving district; validate terrain and footprints, no invented river crossing",
    "twoRoundTripFormula": "4 * measured one-way navigable distance / measured convoy speed + loading/reaction allowance"
  },
  "explorationPlan": {
    "classification": "regional sectors for fictional optional activity; not ancient sites or surveyed routes",
    "sectors": [
      {
        "id": "optional-1",
        "centreTiles": [
          80.73,
          80.73
        ],
        "radiusTiles": 30,
        "title": {
          "en": "Old road markers — 1",
          "es-ES": "Hitos del camino antiguo — 1"
        },
        "task": "reveal-reserve-approach",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {},
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": "wave-2 approach",
        "onceFlag": "03-the-governors-question.optional-1.claimed",
        "mandatory": false,
        "narrator": "miriam-archive",
        "response": {
          "en": "A safe path carried more than a letter.",
          "es-ES": "Un camino seguro llevaba más que una carta."
        }
      },
      {
        "id": "optional-2",
        "centreTiles": [
          218.27,
          80.73
        ],
        "radiusTiles": 30,
        "title": {
          "en": "Old road markers — 2",
          "es-ES": "Hitos del camino antiguo — 2"
        },
        "task": "collect-finite-cache",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {
          "food": 300,
          "wood": 150,
          "gold": 75,
          "stone": 0
        },
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": null,
        "onceFlag": "03-the-governors-question.optional-2.claimed",
        "mandatory": false,
        "narrator": "miriam-archive",
        "response": {
          "en": "A safe path carried more than a letter.",
          "es-ES": "Un camino seguro llevaba más que una carta."
        }
      },
      {
        "id": "optional-3",
        "centreTiles": [
          80.73,
          218.27
        ],
        "radiusTiles": 30,
        "title": {
          "en": "Old road markers — 3",
          "es-ES": "Hitos del camino antiguo — 3"
        },
        "task": "reveal-relief-corridor",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {},
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": "relief corridor",
        "onceFlag": "03-the-governors-question.optional-3.claimed",
        "mandatory": false,
        "narrator": "miriam-archive",
        "response": {
          "en": "A safe path carried more than a letter.",
          "es-ES": "Un camino seguro llevaba más que una carta."
        }
      },
      {
        "id": "optional-4",
        "centreTiles": [
          218.27,
          218.27
        ],
        "radiusTiles": 30,
        "title": {
          "en": "Old road markers — 4",
          "es-ES": "Hitos del camino antiguo — 4"
        },
        "task": "collect-finite-cache",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {
          "food": 300,
          "wood": 150,
          "gold": 75,
          "stone": 0
        },
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": null,
        "onceFlag": "03-the-governors-question.optional-4.claimed",
        "mandatory": false,
        "narrator": "miriam-archive",
        "response": {
          "en": "A safe path carried more than a letter.",
          "es-ES": "Un camino seguro llevaba más que una carta."
        }
      }
    ],
    "connectingTrails": "four optional scouting sectors link to main/relief corridors by paths following real terrain. Rest/lookout every25–55 navigable tiles; do not turn the full map into a forced perimeter march.",
    "qualityGate": "architect certifies each sector location against raster terrain, coast and relief; no new historical claim or geography deformation to make a cache reachable"
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
        "en": "Collect the two witness records before the patrol changes.",
        "es-ES": "Recoge los dos testimonios antes del relevo de patrulla."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "03-the-governors-question.o1",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "collect-testimony",
      "threshold": 2,
      "entities": [
        {
          "id": "03-the-governors-question.o1.main-entities.1",
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
          "id": "03-the-governors-question.o1.main-entities.2",
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
        "operation": "collect-testimony",
        "requiredCount": 2,
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
              "03-the-governors-question.o1.main-entities.1",
              "03-the-governors-question.o1.main-entities.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true,
            "destinations": {
              "03-the-governors-question.o1.main-entities.1": "03-the-governors-question.o1.main-entities.receiving-zone",
              "03-the-governors-question.o1.main-entities.2": "03-the-governors-question.o1.main-entities.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "patrol-deadline",
            "kind": "phase-deadline",
            "phase": "phase-1",
            "clock": "relative-to-phase-entry",
            "onExpiry": "declared defeat if objective not yet latched; show explicit countdown and warning, never timer-only victory",
            "secondsByDifficulty": {
              "easy": 1800,
              "standard": 1500,
              "hard": 1200
            },
            "warningSeconds": 120
          }
        ],
        "requiredLedgers": [
          "main-entities",
          "patrol-deadline"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Deliver an authenticated petition to the governor’s office.",
        "es-ES": "Entrega una petición autenticada en la oficina del gobernador."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "03-the-governors-question.o2",
        "oncePerEntity": true,
        "required": 1
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-petition",
      "threshold": 1,
      "entities": [
        {
          "id": "03-the-governors-question.authenticated-petition.1",
          "role": "petition-token",
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
          "id": "03-the-governors-question.o1.main-entities.1",
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
          "id": "03-the-governors-question.o1.main-entities.2",
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
        "operation": "deliver-petition",
        "requiredCount": 1,
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
              "03-the-governors-question.authenticated-petition.1"
            ],
            "requiredCount": 1,
            "oncePerEntity": true,
            "destinations": {
              "03-the-governors-question.authenticated-petition.1": "03-the-governors-question.o2.main-entities.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "authenticated-petition",
            "kind": "entity-state",
            "state": "collected",
            "entities": [
              "03-the-governors-question.o1.main-entities.1",
              "03-the-governors-question.o1.main-entities.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true
          },
          {
            "id": "authenticated-seal",
            "kind": "derived-token",
            "inputEntities": [
              "03-the-governors-question.o1.main-entities.1",
              "03-the-governors-question.o1.main-entities.2"
            ],
            "outputEntities": [
              "03-the-governors-question.authenticated-petition.1"
            ],
            "once": true,
            "deriveWhen": "both witness records collected; output is the petition carrier, no timer"
          }
        ],
        "requiredLedgers": [
          "main-entities",
          "authenticated-petition",
          "authenticated-seal"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Lead the households to a protected route without killing the witnesses.",
        "es-ES": "Conduce a las familias a una ruta protegida sin matar a los testigos."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "03-the-governors-question.o3",
        "oncePerEntity": true,
        "required": 4
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "evacuate-family",
      "threshold": 4,
      "entities": [
        {
          "id": "03-the-governors-question.family.1",
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
          "id": "03-the-governors-question.family.2",
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
          "id": "03-the-governors-question.family.3",
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
          "id": "03-the-governors-question.family.4",
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
          "id": "03-the-governors-question.witness.1",
          "role": "civilian-witness",
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
          "id": "03-the-governors-question.witness.2",
          "role": "civilian-witness",
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
        "operation": "evacuate-family",
        "requiredCount": 4,
        "destination": "hub-3",
        "defeatBelowRemaining": 4,
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "families-arrived",
            "kind": "entity-state",
            "state": "arrived",
            "entities": [
              "03-the-governors-question.family.1",
              "03-the-governors-question.family.2",
              "03-the-governors-question.family.3",
              "03-the-governors-question.family.4"
            ],
            "requiredCount": 4,
            "oncePerEntity": true,
            "destinations": {
              "03-the-governors-question.family.1": "03-the-governors-question.o3.families-arrived.receiving-zone",
              "03-the-governors-question.family.2": "03-the-governors-question.o3.families-arrived.receiving-zone",
              "03-the-governors-question.family.3": "03-the-governors-question.o3.families-arrived.receiving-zone",
              "03-the-governors-question.family.4": "03-the-governors-question.o3.families-arrived.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "witnesses-alive",
            "kind": "entity-state",
            "state": "alive",
            "entities": [
              "03-the-governors-question.witness.1",
              "03-the-governors-question.witness.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true
          }
        ],
        "requiredLedgers": [
          "families-arrived",
          "witnesses-alive"
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
        "id": "03-the-governors-question.o1.main-entities.1",
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
        "id": "03-the-governors-question.o1.main-entities.2",
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
        "id": "03-the-governors-question.authenticated-petition.1",
        "role": "petition-token",
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
        "id": "03-the-governors-question.family.1",
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
        "id": "03-the-governors-question.family.2",
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
        "id": "03-the-governors-question.family.3",
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
        "id": "03-the-governors-question.family.4",
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
        "id": "03-the-governors-question.witness.1",
        "role": "civilian-witness",
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
        "id": "03-the-governors-question.witness.2",
        "role": "civilian-witness",
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
        "id": "03-the-governors-question.o1.main-entities.receiving-zone",
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
        "id": "03-the-governors-question.o2.main-entities.receiving-zone",
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
        "id": "03-the-governors-question.o3.families-arrived.receiving-zone",
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
    "survivorGroups": [
      {
        "entities": [
          "03-the-governors-question.family.1",
          "03-the-governors-question.family.2",
          "03-the-governors-question.family.3",
          "03-the-governors-question.family.4"
        ],
        "minimumAliveOrAlreadySafe": 4,
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
  }
}
```

## Difficulty and finite budget

These are explicit estimates for calibration, not measured wins or evidence of perfect balance. Player starting military is preplaced; enemy initial/waves are one roster with production disabled. Nominal militia/spearman/archer/scout costs audit the plan, not historical army numbers. Resource banks include mandatory delivery, replacement allowance, protected recovery and a surplus.

| Profile | Start F/W/G/S | Gatherable F/W/G/S | Escort | Initial + waves | Warning / gap seconds |
|---|---|---|---:|---|---|
| easy | 875/625/312/250 | 1885/1075/1128/550 | 16 | 4 + 4 + 4 + 6 = 18 | 120 / 474 |
| standard | 700/500/250/200 | 1820/1100/1030/600 | 12 | 6 + 6 + 6 + 6 = 24 | 90 / 370 |
| hard | 595/425/212/170 | 1805/1125/988/630 | 10 | 7 + 7 + 7 + 8 = 29 | 75 / 296 |

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
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts."
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
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts."
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
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts."
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
    "wholeJourneyDistanceTiles": 111.94,
    "wholeJourneyOneWaySecondsEstimate": 160,
    "optionalCacheAllocation": {
      "food": 600,
      "wood": 300,
      "gold": 150,
      "stone": 0
    },
    "solventWithoutOptionalCaches": true
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Petición tiene copia en segundo archivo; intento fallido consume oro, abre ruta más larga con dos escoltas de reserva.

{
  "plan": "Petición tiene copia en segundo archivo; intento fallido consume oro, abre ruta más larga con dos escoltas de reserva.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units.",
  "phaseDeadlines": {
    "en": "Timed phases: o1: 30 / 25 / 20 minutes on Easy / Standard / Hard. The countdown starts when that phase begins; a two-minute warning precedes a loss if its task is unfinished.",
    "es-ES": "Fases con plazo: o1: 30 / 25 / 20 minutos en fácil / estándar / difícil. La cuenta empieza al comenzar esa fase; un aviso de dos minutos precede a la derrota si falta su objetivo."
  }
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.faith-origins.03-the-governors-question.title` / always | none → next | The Governor’s Question | La pregunta del gobernador |
| `scenario.faith-origins.03-the-governors-question.fact-intro` / intro first | collection-narrator → next | Around 112, Pliny asked Trajan how to handle accusations against Christians. Their correspondence describes policy, not universal tolerance. | Plinio y Trajano intercambian criterios de persecución. La red de mensajeros y la negociación sobre documentos son ficción acotada. |
| `scenario.faith-origins.03-the-governors-question.personal-intro` / after fact-intro | miriam-archive → next | A governor’s neat question reaches us intact. The anxious voices below it do not. Those voices are the part I must reconstruct. | Nos llega intacta la pregunta pulcra de un gobernador. No las voces inquietas que quedan debajo. Esa parte debo reconstruirla. |
| `scenario.faith-origins.03-the-governors-question.objective-1` / phase-1 active | none → hub-1 | Collect the two witness records before the patrol changes. | Recoge los dos testimonios antes del relevo de patrulla. |
| `scenario.faith-origins.03-the-governors-question.objective-2` / phase-2 active | none → hub-2 | Deliver an authenticated petition to the governor’s office. | Entrega una petición autenticada en la oficina del gobernador. |
| `scenario.faith-origins.03-the-governors-question.objective-3` / phase-3 active | none → hub-3 | Lead the households to a protected route without killing the witnesses. | Conduce a las familias a una ruta protegida sin matar a los testigos. |
| `scenario.faith-origins.03-the-governors-question.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. Timed phases: o1: 30 / 25 / 20 minutes on Easy / Standard / Hard. The countdown starts when that phase begins; a two-minute warning precedes a loss if its task is unfinished. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. Fases con plazo: o1: 30 / 25 / 20 minutos en fácil / estándar / difícil. La cuenta empieza al comenzar esa fase; un aviso de dos minutos precede a la derrota si falta su objetivo. |
| `scenario.faith-origins.03-the-governors-question.scouts` / scouts panel | none → next | Regional setting: Nicomedia and Bithynian roads. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Nicomedia and Bithynian roads. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.faith-origins.03-the-governors-question.history` / history panel | none → next | Around 112, Pliny asked Trajan how to handle accusations against Christians. Their correspondence describes policy, not universal tolerance. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Plinio y Trajano intercambian criterios de persecución. La red de mensajeros y la negociación sobre documentos son ficción acotada. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.faith-origins.03-the-governors-question.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.faith-origins.03-the-governors-question.event-phase-1-complete` / o1 first becomes true | miriam-archive → next | I have found the first safe address. A letter can travel farther than its writer. | He encontrado la primera dirección segura. Una carta puede viajar más lejos que quien la escribe. |
| `scenario.faith-origins.03-the-governors-question.event-phase-2-complete` / o2 first becomes true | miriam-archive → next | The second bundle weighs little. Protecting it has cost us more than ink. | El segundo legajo pesa poco. Protegerlo nos ha costado más que tinta. |
| `scenario.faith-origins.03-the-governors-question.event-phase-3-complete` / o3 first becomes true | miriam-archive → next | I will record what arrived, and leave a space for what did not. | Registraré lo que llegó y dejaré un espacio para lo que no. |
| `scenario.faith-origins.03-the-governors-question.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | miriam-archive → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.faith-origins.03-the-governors-question.victory-fact` / victory latch first | collection-narrator → next | Around 112, Pliny asked Trajan how to handle accusations against Christians. Their correspondence describes policy, not universal tolerance. Your mission task is complete; this outcome does not change the documented events. | La correspondencia no impone tolerancia universal; se registra el alcance de la política. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.faith-origins.03-the-governors-question.victory-personal` / after victory-fact | miriam-archive → 04-a-different-dawn | I will record what arrived, and leave a space for what did not. | Registraré lo que llegó y dejaré un espacio para lo que no. |
| `scenario.faith-origins.03-the-governors-question.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.faith-origins.03-the-governors-question.recovery` / 6 minutes without objective progress | miriam-archive → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.faith-origins.03-the-governors-question.optional-1` / optional sector observed/cache claimed; once, independent of main phase | miriam-archive → return-to-game | Old road markers — 1: The hidden reserve approach is now marked. A safe path carried more than a letter. | Hitos del camino antiguo — 1: La aproximación de la reserva está señalada. Un camino seguro llevaba más que una carta. |
| `scenario.faith-origins.03-the-governors-question.optional-2` / optional sector observed/cache claimed; once, independent of main phase | miriam-archive → return-to-game | Old road markers — 2: One cache: 300 food, 150 wood and 75 gold. It can be claimed once. A safe path carried more than a letter. | Hitos del camino antiguo — 2: Un depósito: 300 de alimento, 150 de madera y 75 de oro. Solo se puede reclamar una vez. Un camino seguro llevaba más que una carta. |
| `scenario.faith-origins.03-the-governors-question.optional-3` / optional sector observed/cache claimed; once, independent of main phase | miriam-archive → return-to-game | Old road markers — 3: The relief route is now marked. A safe path carried more than a letter. | Hitos del camino antiguo — 3: La ruta alternativa está señalada. Un camino seguro llevaba más que una carta. |
| `scenario.faith-origins.03-the-governors-question.optional-4` / optional sector observed/cache claimed; once, independent of main phase | miriam-archive → return-to-game | Old road markers — 4: One cache: 300 food, 150 wood and 75 gold. It can be claimed once. A safe path carried more than a letter. | Hitos del camino antiguo — 4: Un depósito: 300 de alimento, 150 de madera y 75 de oro. Solo se puede reclamar una vez. Un camino seguro llevaba más que una carta. |

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
