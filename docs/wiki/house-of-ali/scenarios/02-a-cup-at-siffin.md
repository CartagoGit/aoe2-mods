# A Cup at Siffin / Un cuenco en Siffin

`house-of-ali/02-a-cup-at-siffin` · 657 CE · aid-corridor

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/house-of-ali/02-a-cup-at-siffin.svg)

## Historical frame and outcome

Siffin in 657 divided armies and communities. The aid convoy in this scenario offers a different personal perspective on the same conflict.

Mismo marco de Siffin que I01 con otro objetivo y enfoque; no otro resultado histórico ni contradicción entre las campañas.

Dina no es testigo adulto de batalla; las versiones se atribuyen. No efecto mágico de manuscritos religiosos.

- [Ismail K. Poonawala, Ali: Life](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Secciones califato, Camello, Siffin y muerte. Distinguir la reconstrucción histórica de las interpretaciones comunitarias.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

My uncle brought back a chipped cup and three versions of a single afternoon. I kept the cup; I learned to name the versions.

Mi tío volvió con un cuenco roto y tres versiones de una misma tarde. Guardé el cuenco; aprendí a nombrar las versiones.

## Geography and map construction

Siffin / Euphrates near Raqqa — 360 × 360 tiles; north-up design controls [38.55, 35.6, 39.2, 36.05].

Llanura seca junto a Éufrates; acantilados bajos y acceso a agua.

Éufrates atraviesa valle de noroeste a sureste; accesos de ambas fuerzas cerca del cauce.

Terrazas alejadas del río; no montaña central que parta el valle.

Ruta Siria desde oeste y ruta Iraq desde sureste; campamentos ubicación hipotética.

Exclude: No fijar campamentos exactos ni episodios de textos sagrados como mecanismo mágico.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Traditional Siffin corridor, uncertain | [38.7, 35.72] | [93.2, 243.36] |
| Raqqa regional river control | [39.01, 35.92] | [246.07, 121.72] |
| Iraqi southeast approach | [39.03, 35.69] | [255.94, 261.61] |

```json
{
  "bbox": [
    38.55,
    35.6,
    39.2,
    36.05
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Traditional Siffin corridor, uncertain",
      "lonLat": [
        38.7,
        35.72
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        93.2,
        243.36
      ]
    },
    {
      "id": "anchor-2",
      "name": "Raqqa regional river control",
      "lonLat": [
        39.01,
        35.92
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        246.07,
        121.72
      ]
    },
    {
      "id": "anchor-3",
      "name": "Iraqi southeast approach",
      "lonLat": [
        39.03,
        35.69
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        255.94,
        261.61
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        255.94,
        261.61
      ],
      "purpose": {
        "en": "Prepare the two aid wagons on the Iraqi approach.",
        "es-ES": "Prepara los dos carros de auxilio en el acceso iraquí."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        93.2,
        243.36
      ],
      "purpose": {
        "en": "Carry the supplies to both appointed truce points.",
        "es-ES": "Lleva los suministros a los dos puntos de tregua designados."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        246.07,
        121.72
      ],
      "purpose": {
        "en": "Return the receiving records and six civilian parties.",
        "es-ES": "Devuelve los recibos y seis grupos civiles."
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
          255.94,
          261.61
        ],
        [
          93.2,
          243.36
        ],
        [
          246.07,
          121.72
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          255.94,
          261.61
        ],
        [
          182.57,
          260.49
        ],
        [
          93.2,
          243.36
        ],
        [
          246.07,
          121.72
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        38.55,
        35.72
      ],
      [
        38.7,
        35.73
      ],
      [
        38.8,
        35.79
      ],
      [
        38.9,
        35.85
      ],
      [
        39.01,
        35.92
      ],
      [
        39.14,
        35.8
      ],
      [
        39.2,
        35.73
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "siffin",
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
  "asset": "docs/design/maps/house-of-ali/02-a-cup-at-siffin.svg",
  "mainRouteLengthStraightTiles": 359.12,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        75.2,
        255.36
      ],
      [
        111.2,
        255.36
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
          96.93,
          96.93
        ],
        "radiusTiles": 30,
        "title": {
          "en": "The neighbours’ provisions — 1",
          "es-ES": "Las provisiones de los vecinos — 1"
        },
        "task": "reveal-reserve-approach",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {},
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": "wave-2 approach",
        "onceFlag": "02-a-cup-at-siffin.optional-1.claimed",
        "mandatory": false,
        "narrator": "dina-potter",
        "response": {
          "en": "I kept a cup aside for whoever came after us.",
          "es-ES": "Guardé una taza para quien llegara después."
        }
      },
      {
        "id": "optional-2",
        "centreTiles": [
          262.07,
          96.93
        ],
        "radiusTiles": 30,
        "title": {
          "en": "The neighbours’ provisions — 2",
          "es-ES": "Las provisiones de los vecinos — 2"
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
        "onceFlag": "02-a-cup-at-siffin.optional-2.claimed",
        "mandatory": false,
        "narrator": "dina-potter",
        "response": {
          "en": "I kept a cup aside for whoever came after us.",
          "es-ES": "Guardé una taza para quien llegara después."
        }
      },
      {
        "id": "optional-3",
        "centreTiles": [
          96.93,
          262.07
        ],
        "radiusTiles": 30,
        "title": {
          "en": "The neighbours’ provisions — 3",
          "es-ES": "Las provisiones de los vecinos — 3"
        },
        "task": "reveal-relief-corridor",
        "activation": "scout the sector; mark one finite landmark/cache on valid accessible terrain",
        "terrainPolicy": "use region terrain/hydrology and dated reconstruction; water sector can be observed from nearest navigable bank. No mandatory path or invented settlement here.",
        "reward": {},
        "rewardSource": "deduct this allocation from gatherableBank, never add on top. Optional caches fit inside surplus; all mandatory tasks remain solvent without them.",
        "revealTarget": "relief corridor",
        "onceFlag": "02-a-cup-at-siffin.optional-3.claimed",
        "mandatory": false,
        "narrator": "dina-potter",
        "response": {
          "en": "I kept a cup aside for whoever came after us.",
          "es-ES": "Guardé una taza para quien llegara después."
        }
      },
      {
        "id": "optional-4",
        "centreTiles": [
          262.07,
          262.07
        ],
        "radiusTiles": 30,
        "title": {
          "en": "The neighbours’ provisions — 4",
          "es-ES": "Las provisiones de los vecinos — 4"
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
        "onceFlag": "02-a-cup-at-siffin.optional-4.claimed",
        "mandatory": false,
        "narrator": "dina-potter",
        "response": {
          "en": "I kept a cup aside for whoever came after us.",
          "es-ES": "Guardé una taza para quien llegara después."
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
        "en": "Prepare the two aid wagons on the Iraqi approach.",
        "es-ES": "Prepara los dos carros de auxilio en el acceso iraquí."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-a-cup-at-siffin.o1",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "prepare-wagon",
      "threshold": 2,
      "entities": [
        {
          "id": "02-a-cup-at-siffin.o1.main-entities.1",
          "role": "aid-wagon",
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
          "id": "02-a-cup-at-siffin.o1.main-entities.2",
          "role": "aid-wagon",
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
        "operation": "prepare-wagon",
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
            "state": "prepared",
            "entities": [
              "02-a-cup-at-siffin.o1.main-entities.1",
              "02-a-cup-at-siffin.o1.main-entities.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true,
            "destinations": {
              "02-a-cup-at-siffin.o1.main-entities.1": "02-a-cup-at-siffin.o1.main-entities.receiving-zone",
              "02-a-cup-at-siffin.o1.main-entities.2": "02-a-cup-at-siffin.o1.main-entities.receiving-zone"
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
        "en": "Carry the supplies to both appointed truce points.",
        "es-ES": "Lleva los suministros a los dos puntos de tregua designados."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-a-cup-at-siffin.o2",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-truce-message",
      "threshold": 2,
      "entities": [
        {
          "id": "02-a-cup-at-siffin.o1.main-entities.1",
          "role": "aid-wagon",
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
          "id": "02-a-cup-at-siffin.o1.main-entities.2",
          "role": "aid-wagon",
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
        "operation": "deliver-truce-message",
        "requiredCount": 2,
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
              "02-a-cup-at-siffin.o1.main-entities.1",
              "02-a-cup-at-siffin.o1.main-entities.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true,
            "destinations": {
              "02-a-cup-at-siffin.o1.main-entities.1": "02-a-cup-at-siffin.truce-point.1",
              "02-a-cup-at-siffin.o1.main-entities.2": "02-a-cup-at-siffin.truce-point.2"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active.",
            "distinctDestinationCount": 2,
            "minimumPerDestination": 1
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
        "en": "Return the receiving records and six civilian parties.",
        "es-ES": "Devuelve los recibos y seis grupos civiles."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "02-a-cup-at-siffin.o3",
        "oncePerEntity": true,
        "required": 6
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "evacuate-family",
      "threshold": 6,
      "entities": [
        {
          "id": "02-a-cup-at-siffin.family.1",
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
          "id": "02-a-cup-at-siffin.family.2",
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
          "id": "02-a-cup-at-siffin.family.3",
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
          "id": "02-a-cup-at-siffin.family.4",
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
          "id": "02-a-cup-at-siffin.family.5",
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
          "id": "02-a-cup-at-siffin.family.6",
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
          "id": "02-a-cup-at-siffin.family.7",
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
          "id": "02-a-cup-at-siffin.family.8",
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
          "id": "02-a-cup-at-siffin.o3.receiving-records.1",
          "role": "record-token",
          "initialHub": "hub-2",
          "offsetTiles": [
            -8,
            -4
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "initiallyAvailable": false,
          "unlockByReceipt": {
            "output": "02-a-cup-at-siffin.o3.receiving-records.1",
            "fromObjective": "o2",
            "fromRequirement": "main-entities",
            "receivedEntity": "02-a-cup-at-siffin.o1.main-entities.1",
            "destination": "02-a-cup-at-siffin.truce-point.1"
          },
          "countedOnce": true,
          "atHub": "hub-2"
        },
        {
          "id": "02-a-cup-at-siffin.o3.receiving-records.2",
          "role": "record-token",
          "initialHub": "hub-2",
          "offsetTiles": [
            8,
            0
          ],
          "identity": "fictional gameplay object",
          "finite": true,
          "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
          "initiallyDelivered": false,
          "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
          "initiallyAvailable": false,
          "unlockByReceipt": {
            "output": "02-a-cup-at-siffin.o3.receiving-records.2",
            "fromObjective": "o2",
            "fromRequirement": "main-entities",
            "receivedEntity": "02-a-cup-at-siffin.o1.main-entities.2",
            "destination": "02-a-cup-at-siffin.truce-point.2"
          },
          "countedOnce": true,
          "atHub": "hub-2"
        }
      ],
      "predicate": {
        "operator": "all",
        "operation": "evacuate-family",
        "requiredCount": 6,
        "destination": "hub-3",
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
              "02-a-cup-at-siffin.family.1",
              "02-a-cup-at-siffin.family.2",
              "02-a-cup-at-siffin.family.3",
              "02-a-cup-at-siffin.family.4",
              "02-a-cup-at-siffin.family.5",
              "02-a-cup-at-siffin.family.6",
              "02-a-cup-at-siffin.family.7",
              "02-a-cup-at-siffin.family.8"
            ],
            "requiredCount": 6,
            "oncePerEntity": true,
            "destinations": {
              "02-a-cup-at-siffin.family.1": "02-a-cup-at-siffin.o3.families-arrived.receiving-zone",
              "02-a-cup-at-siffin.family.2": "02-a-cup-at-siffin.o3.families-arrived.receiving-zone",
              "02-a-cup-at-siffin.family.3": "02-a-cup-at-siffin.o3.families-arrived.receiving-zone",
              "02-a-cup-at-siffin.family.4": "02-a-cup-at-siffin.o3.families-arrived.receiving-zone",
              "02-a-cup-at-siffin.family.5": "02-a-cup-at-siffin.o3.families-arrived.receiving-zone",
              "02-a-cup-at-siffin.family.6": "02-a-cup-at-siffin.o3.families-arrived.receiving-zone",
              "02-a-cup-at-siffin.family.7": "02-a-cup-at-siffin.o3.families-arrived.receiving-zone",
              "02-a-cup-at-siffin.family.8": "02-a-cup-at-siffin.o3.families-arrived.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "receiving-records",
            "kind": "entity-state",
            "state": "arrived",
            "entities": [
              "02-a-cup-at-siffin.o3.receiving-records.1",
              "02-a-cup-at-siffin.o3.receiving-records.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true,
            "destinations": {
              "02-a-cup-at-siffin.o3.receiving-records.1": "02-a-cup-at-siffin.o3.receiving-records.receiving-zone",
              "02-a-cup-at-siffin.o3.receiving-records.2": "02-a-cup-at-siffin.o3.receiving-records.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active.",
            "generatedByReceipts": [
              {
                "output": "02-a-cup-at-siffin.o3.receiving-records.1",
                "fromObjective": "o2",
                "fromRequirement": "main-entities",
                "receivedEntity": "02-a-cup-at-siffin.o1.main-entities.1",
                "destination": "02-a-cup-at-siffin.truce-point.1"
              },
              {
                "output": "02-a-cup-at-siffin.o3.receiving-records.2",
                "fromObjective": "o2",
                "fromRequirement": "main-entities",
                "receivedEntity": "02-a-cup-at-siffin.o1.main-entities.2",
                "destination": "02-a-cup-at-siffin.truce-point.2"
              }
            ],
            "originRule": "issued once by named truce-point receiver only after THAT wagon delivers; record returns from that same point, never pre-delivered at hub-1"
          }
        ],
        "requiredLedgers": [
          "families-arrived",
          "receiving-records"
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
        "id": "02-a-cup-at-siffin.o1.main-entities.1",
        "role": "aid-wagon",
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
        "id": "02-a-cup-at-siffin.o1.main-entities.2",
        "role": "aid-wagon",
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
        "id": "02-a-cup-at-siffin.family.1",
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
        "id": "02-a-cup-at-siffin.family.2",
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
        "id": "02-a-cup-at-siffin.family.3",
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
        "id": "02-a-cup-at-siffin.family.4",
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
        "id": "02-a-cup-at-siffin.family.5",
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
        "id": "02-a-cup-at-siffin.family.6",
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
        "id": "02-a-cup-at-siffin.family.7",
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
        "id": "02-a-cup-at-siffin.family.8",
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
        "id": "02-a-cup-at-siffin.o3.receiving-records.1",
        "role": "record-token",
        "initialHub": "hub-2",
        "offsetTiles": [
          -8,
          -4
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
        "initiallyAvailable": false,
        "unlockByReceipt": {
          "output": "02-a-cup-at-siffin.o3.receiving-records.1",
          "fromObjective": "o2",
          "fromRequirement": "main-entities",
          "receivedEntity": "02-a-cup-at-siffin.o1.main-entities.1",
          "destination": "02-a-cup-at-siffin.truce-point.1"
        }
      },
      {
        "id": "02-a-cup-at-siffin.o3.receiving-records.2",
        "role": "record-token",
        "initialHub": "hub-2",
        "offsetTiles": [
          8,
          0
        ],
        "identity": "fictional gameplay object",
        "finite": true,
        "replacement": "one recovery carrier may inherit the SAME token ID; never mint another counted object",
        "initiallyDelivered": false,
        "originRule": "one distinct pickup position per token in its initial district; carriers separated by 1–2 tiles within allowed footprint; no origin inside receiving zone",
        "initiallyAvailable": false,
        "unlockByReceipt": {
          "output": "02-a-cup-at-siffin.o3.receiving-records.2",
          "fromObjective": "o2",
          "fromRequirement": "main-entities",
          "receivedEntity": "02-a-cup-at-siffin.o1.main-entities.2",
          "destination": "02-a-cup-at-siffin.truce-point.2"
        }
      }
    ],
    "zones": [
      {
        "id": "02-a-cup-at-siffin.o1.main-entities.receiving-zone",
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
        "id": "02-a-cup-at-siffin.o3.families-arrived.receiving-zone",
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
        "id": "02-a-cup-at-siffin.o3.receiving-records.receiving-zone",
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
        "id": "02-a-cup-at-siffin.truce-point.1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid ground within geographic district; receiving zone excludes origins",
        "protectedCivilian": false
      },
      {
        "id": "02-a-cup-at-siffin.truce-point.2",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          0
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
          "02-a-cup-at-siffin.family.1",
          "02-a-cup-at-siffin.family.2",
          "02-a-cup-at-siffin.family.3",
          "02-a-cup-at-siffin.family.4",
          "02-a-cup-at-siffin.family.5",
          "02-a-cup-at-siffin.family.6",
          "02-a-cup-at-siffin.family.7",
          "02-a-cup-at-siffin.family.8"
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
  }
}
```

## Difficulty and finite budget

These are explicit estimates for calibration, not measured wins or evidence of perfect balance. Player starting military is preplaced; enemy initial/waves are one roster with production disabled. Nominal militia/spearman/archer/scout costs audit the plan, not historical army numbers. Resource banks include mandatory delivery, replacement allowance, protected recovery and a surplus.

| Profile | Start F/W/G/S | Gatherable F/W/G/S | Escort | Initial + waves | Warning / gap seconds |
|---|---|---|---:|---|---|
| easy | 875/625/312/250 | 1885/1075/1128/550 | 16 | 22 + 22 + 22 + 24 = 90 | 120 / 474 |
| standard | 700/500/250/200 | 1820/1100/1030/600 | 12 | 30 + 30 + 30 + 30 = 120 | 90 / 370 |
| hard | 595/425/212/170 | 1805/1125/988/630 | 10 | 36 + 36 + 36 + 36 = 144 | 75 / 296 |

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
      "enemyTotalCap": 90,
      "initialEnemy": 22,
      "waves": [
        {
          "id": "wave-1",
          "count": 22,
          "composition": {
            "militia": 9,
            "spearman": 5,
            "archer": 5,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 474,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 22,
          "composition": {
            "militia": 9,
            "spearman": 5,
            "archer": 5,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 948,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 24,
          "composition": {
            "militia": 8,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1422,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 9,
        "spearman": 5,
        "archer": 5,
        "scoutCavalry": 3
      },
      "enemyNominalResourceCost": {
        "food": 3875,
        "wood": 1050,
        "gold": 1645,
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
      "enemyTotalCap": 120,
      "initialEnemy": 30,
      "waves": [
        {
          "id": "wave-1",
          "count": 30,
          "composition": {
            "militia": 11,
            "spearman": 7,
            "archer": 7,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 370,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 30,
          "composition": {
            "militia": 11,
            "spearman": 7,
            "archer": 7,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 740,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 30,
          "composition": {
            "militia": 11,
            "spearman": 7,
            "archer": 7,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1110,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 11,
        "spearman": 7,
        "archer": 7,
        "scoutCavalry": 5
      },
      "enemyNominalResourceCost": {
        "food": 5220,
        "wood": 1400,
        "gold": 2140,
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
      "enemyTotalCap": 144,
      "initialEnemy": 36,
      "waves": [
        {
          "id": "wave-1",
          "count": 36,
          "composition": {
            "militia": 12,
            "spearman": 9,
            "archer": 9,
            "scoutCavalry": 6
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 296,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 36,
          "composition": {
            "militia": 12,
            "spearman": 9,
            "archer": 9,
            "scoutCavalry": 6
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 592,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 36,
          "composition": {
            "militia": 12,
            "spearman": 9,
            "archer": 9,
            "scoutCavalry": 6
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 888,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 12,
        "spearman": 9,
        "archer": 9,
        "scoutCavalry": 6
      },
      "enemyNominalResourceCost": {
        "food": 6060,
        "wood": 1800,
        "gold": 2580,
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
    "wholeJourneyDistanceTiles": 359.12,
    "wholeJourneyOneWaySecondsEstimate": 514,
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

No atacar ambos campamentos para curar aliados. Un convoy de reserva limitado; tregua local necesita soporte acreditado; rutas a puntos distintos sin negar agua a civiles.

{
  "plan": "No atacar ambos campamentos para curar aliados. Un convoy de reserva limitado; tregua local necesita soporte acreditado; rutas a puntos distintos sin negar agua a civiles.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.house-of-ali.02-a-cup-at-siffin.title` / always | none → next | A Cup at Siffin | Un cuenco en Siffin |
| `scenario.house-of-ali.02-a-cup-at-siffin.fact-intro` / intro first | collection-narrator → next | Siffin in 657 divided armies and communities. The aid convoy in this scenario offers a different personal perspective on the same conflict. | Mismo marco de Siffin que I01 con otro objetivo y enfoque; no otro resultado histórico ni contradicción entre las campañas. |
| `scenario.house-of-ali.02-a-cup-at-siffin.personal-intro` / after fact-intro | dina-potter → next | My uncle brought back a chipped cup and three versions of a single afternoon. I kept the cup; I learned to name the versions. | Mi tío volvió con un cuenco roto y tres versiones de una misma tarde. Guardé el cuenco; aprendí a nombrar las versiones. |
| `scenario.house-of-ali.02-a-cup-at-siffin.objective-1` / phase-1 active | none → hub-1 | Prepare the two aid wagons on the Iraqi approach. | Prepara los dos carros de auxilio en el acceso iraquí. |
| `scenario.house-of-ali.02-a-cup-at-siffin.objective-2` / phase-2 active | none → hub-2 | Carry the supplies to both appointed truce points. | Lleva los suministros a los dos puntos de tregua designados. |
| `scenario.house-of-ali.02-a-cup-at-siffin.objective-3` / phase-3 active | none → hub-3 | Return the receiving records and six civilian parties. | Devuelve los recibos y seis grupos civiles. |
| `scenario.house-of-ali.02-a-cup-at-siffin.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.house-of-ali.02-a-cup-at-siffin.scouts` / scouts panel | none → next | Regional setting: Siffin / Euphrates near Raqqa. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Siffin / Euphrates near Raqqa. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.house-of-ali.02-a-cup-at-siffin.history` / history panel | none → next | Siffin in 657 divided armies and communities. The aid convoy in this scenario offers a different personal perspective on the same conflict. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Mismo marco de Siffin que I01 con otro objetivo y enfoque; no otro resultado histórico ni contradicción entre las campañas. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.house-of-ali.02-a-cup-at-siffin.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.house-of-ali.02-a-cup-at-siffin.event-phase-1-complete` / o1 first becomes true | dina-potter → next | The first household has water. I know the weight of a full jar better than the weight of a title. | La primera familia tiene agua. Conozco mejor el peso de una jarra llena que el de un título. |
| `scenario.house-of-ali.02-a-cup-at-siffin.event-phase-2-complete` / o2 first becomes true | dina-potter → next | There is another road for the families. Tell them before the dust hides it. | Hay otro camino para las familias. Díselo antes de que lo oculte el polvo. |
| `scenario.house-of-ali.02-a-cup-at-siffin.event-phase-3-complete` / o3 first becomes true | dina-potter → next | I kept the names. I cannot turn what happened into a kinder ending. | Guardé los nombres. No puedo transformar lo que ocurrió en un final más amable. |
| `scenario.house-of-ali.02-a-cup-at-siffin.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | dina-potter → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.house-of-ali.02-a-cup-at-siffin.victory-fact` / victory latch first | collection-narrator → next | Siffin in 657 divided armies and communities. The aid convoy in this scenario offers a different personal perspective on the same conflict. Your mission task is complete; this outcome does not change the documented events. | Dina no es testigo adulto de batalla; las versiones se atribuyen. No efecto mágico de manuscritos religiosos. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.house-of-ali.02-a-cup-at-siffin.victory-personal` / after victory-fact | dina-potter → 03-the-sealed-copy | I kept the names. I cannot turn what happened into a kinder ending. | Guardé los nombres. No puedo transformar lo que ocurrió en un final más amable. |
| `scenario.house-of-ali.02-a-cup-at-siffin.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.house-of-ali.02-a-cup-at-siffin.recovery` / 6 minutes without objective progress | dina-potter → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.house-of-ali.02-a-cup-at-siffin.optional-1` / optional sector observed/cache claimed; once, independent of main phase | dina-potter → return-to-game | The neighbours’ provisions — 1: The hidden reserve approach is now marked. I kept a cup aside for whoever came after us. | Las provisiones de los vecinos — 1: La aproximación de la reserva está señalada. Guardé una taza para quien llegara después. |
| `scenario.house-of-ali.02-a-cup-at-siffin.optional-2` / optional sector observed/cache claimed; once, independent of main phase | dina-potter → return-to-game | The neighbours’ provisions — 2: One cache: 300 food, 150 wood and 75 gold. It can be claimed once. I kept a cup aside for whoever came after us. | Las provisiones de los vecinos — 2: Un depósito: 300 de alimento, 150 de madera y 75 de oro. Solo se puede reclamar una vez. Guardé una taza para quien llegara después. |
| `scenario.house-of-ali.02-a-cup-at-siffin.optional-3` / optional sector observed/cache claimed; once, independent of main phase | dina-potter → return-to-game | The neighbours’ provisions — 3: The relief route is now marked. I kept a cup aside for whoever came after us. | Las provisiones de los vecinos — 3: La ruta alternativa está señalada. Guardé una taza para quien llegara después. |
| `scenario.house-of-ali.02-a-cup-at-siffin.optional-4` / optional sector observed/cache claimed; once, independent of main phase | dina-potter → return-to-game | The neighbours’ provisions — 4: One cache: 300 food, 150 wood and 75 gold. It can be claimed once. I kept a cup aside for whoever came after us. | Las provisiones de los vecinos — 4: Un depósito: 300 de alimento, 150 de madera y 75 de oro. Solo se puede reclamar una vez. Guardé una taza para quien llegara después. |

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
