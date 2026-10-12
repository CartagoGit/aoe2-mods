# The Water That Remains / El agua que queda

`house-of-ali/04-the-water-that-remains` · 680 CE · civilian-witness-withdrawal

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/house-of-ali/04-the-water-that-remains.svg)

## Historical frame and outcome

Husayn was killed at Karbala in 680. The player assists fictional travelling families; their escape does not change that historical outcome.

Husayn muere en Karbala; números/discursos y motivos detallados varían según transmisión. Misión acompaña viajeros ficticios fuera del campamento histórico, no recrea el martirio como espectáculo.

Narrador común expone la muerte documentada sobriamente; Dina cierra su experiencia ficticia sin atribuirse diálogos de Husayn. Memoria posterior se contextualiza.

- [Wilferd Madelung, Husayn: Life and Significance](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Viaje y muerte en Karbala. Las escenas domésticas del narrador son ficticias, no citas de Husayn.
- [Encyclopaedia Iranica, Karbala](https://www.iranicaonline.org/articles/karbala/): Memoria, enterramiento y visitas posteriores. El santuario moderno no pertenece al paisaje de 680.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

I was old enough now to know a road could close. I filled the jars before asking which story would be told about the men beyond it.

Ahora tenía edad para saber que un camino podía cerrarse. Llené las vasijas antes de preguntar qué historia se contaría de los hombres que quedaban al otro lado.

## Geography and map construction

Karbala plain — 360 × 360 tiles; north-up design controls [43.85, 32.4, 44.15, 32.7].

Llanura seca al oeste del eje del Éufrates con accesos a cultivos y agua.

Río/canales al este; conexión de 680 reconstruida con cautela.

Relieve prácticamente llano; no dunas gigantes bloqueando una ciudad.

Ruta hacia Kufa al sureste; campamento fuera de santuario moderno.

Exclude: No cúpulas doradas/santuario actual ni caricaturas de figuras veneradas.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Karbala regional locality | [44.025, 32.616] | [202.02, 108.98] |
| Eastern watered margin | [44.105, 32.62] | [274.07, 104.71] |
| Southeast Kufa road | [44.095, 32.5] | [265.06, 232.92] |

```json
{
  "bbox": [
    43.85,
    32.4,
    44.15,
    32.7
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Karbala regional locality",
      "lonLat": [
        44.025,
        32.616
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        202.02,
        108.98
      ]
    },
    {
      "id": "anchor-2",
      "name": "Eastern watered margin",
      "lonLat": [
        44.105,
        32.62
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        274.07,
        104.71
      ]
    },
    {
      "id": "anchor-3",
      "name": "Southeast Kufa road",
      "lonLat": [
        44.095,
        32.5
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        265.06,
        232.92
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        265.06,
        232.92
      ],
      "purpose": {
        "en": "Mark the two civilian withdrawal paths east of the dry camp.",
        "es-ES": "Señala los dos caminos civiles de retirada al este del campamento seco."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        202.02,
        108.98
      ],
      "purpose": {
        "en": "Carry the water and records to six of eight travelling family groups.",
        "es-ES": "Lleva el agua y los registros a seis de ocho grupos familiares viajeros."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        274.07,
        104.71
      ],
      "purpose": {
        "en": "Withdraw the families and preserve the two testimony copies.",
        "es-ES": "Retira a las familias y conserva las dos copias de los testimonios."
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
          265.06,
          232.92
        ],
        [
          202.02,
          108.98
        ],
        [
          274.07,
          104.71
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          265.06,
          232.92
        ],
        [
          217.54000000000002,
          154.95
        ],
        [
          202.02,
          108.98
        ],
        [
          274.07,
          104.71
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        44.1,
        32.7
      ],
      [
        44.105,
        32.62
      ],
      [
        44.13,
        32.5
      ],
      [
        44.15,
        32.4
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "karbala",
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
  "asset": "docs/design/maps/house-of-ali/04-the-water-that-remains.svg",
  "mainRouteLengthStraightTiles": 211.23
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
        "en": "Mark the two civilian withdrawal paths east of the dry camp.",
        "es-ES": "Señala los dos caminos civiles de retirada al este del campamento seco."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-1",
        "oncePerEntity": true,
        "required": "Mark the two civilian withdrawal paths east of the dry camp."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "scout-corridor",
      "threshold": 2,
      "entities": [
        {
          "id": "04-the-water-that-remains-o1-entity-1",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "scout-corridor",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-water-that-remains-o1-entity-2",
          "atHub": "hub-1",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "scout-corridor",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "scout-corridor",
        "requiredCount": 2,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Mark the two civilian withdrawal paths east of the dry camp.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Carry the water and records to six of eight travelling family groups.",
        "es-ES": "Lleva el agua y los registros a seis de ocho grupos familiares viajeros."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-2",
        "oncePerEntity": true,
        "required": "Carry the water and records to six of eight travelling family groups."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "evacuate-family",
      "threshold": 6,
      "entities": [
        {
          "id": "04-the-water-that-remains-o2-entity-1",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-water-that-remains-o2-entity-2",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-water-that-remains-o2-entity-3",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-water-that-remains-o2-entity-4",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-water-that-remains-o2-entity-5",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-water-that-remains-o2-entity-6",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-water-that-remains-o2-entity-7",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-water-that-remains-o2-entity-8",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "evacuate-family",
        "requiredCount": 6,
        "destination": "hub-2",
        "defeatBelowRemaining": 6,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Carry the water and records to six of eight travelling family groups.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Withdraw the families and preserve the two testimony copies.",
        "es-ES": "Retira a las familias y conserva las dos copias de los testimonios."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-3",
        "oncePerEntity": true,
        "required": "Withdraw the families and preserve the two testimony copies."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-copy",
      "threshold": 2,
      "entities": [
        {
          "id": "04-the-water-that-remains-o3-entity-1",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "deliver-copy",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-the-water-that-remains-o3-entity-2",
          "atHub": "hub-3",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "deliver-copy",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "deliver-copy",
        "requiredCount": 2,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Withdraw the families and preserve the two testimony copies.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    }
  ],
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
| easy | 875/625/312/250 | 1885/1075/1128/550 | 16 | 18 + 18 + 18 + 18 = 72 | 120 / 694 |
| standard | 700/500/250/200 | 1820/1100/1030/600 | 12 | 24 + 24 + 24 + 24 = 96 | 90 / 694 |
| hard | 595/425/212/170 | 1805/1125/988/630 | 10 | 28 + 28 + 28 + 31 = 115 | 75 / 694 |

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
      "enemyTotalCap": 72,
      "initialEnemy": 18,
      "waves": [
        {
          "id": "wave-1",
          "count": 18,
          "composition": {
            "militia": 7,
            "spearman": 4,
            "archer": 4,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 694,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 18,
          "composition": {
            "militia": 7,
            "spearman": 4,
            "archer": 4,
            "scoutCavalry": 3
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1388,
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
          "offsetSeconds": 2082,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 7,
        "spearman": 4,
        "archer": 4,
        "scoutCavalry": 3
      },
      "enemyNominalResourceCost": {
        "food": 3200,
        "wood": 800,
        "gold": 1280,
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
        45
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
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
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
      "enemyTotalCap": 96,
      "initialEnemy": 24,
      "waves": [
        {
          "id": "wave-1",
          "count": 24,
          "composition": {
            "militia": 8,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 694,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 24,
          "composition": {
            "militia": 8,
            "spearman": 6,
            "archer": 6,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1388,
          "warningSeconds": 90,
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
          "offsetSeconds": 2082,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 8,
        "spearman": 6,
        "archer": 6,
        "scoutCavalry": 4
      },
      "enemyNominalResourceCost": {
        "food": 4040,
        "wood": 1200,
        "gold": 1720,
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
        45
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
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
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
      "enemyTotalCap": 115,
      "initialEnemy": 28,
      "waves": [
        {
          "id": "wave-1",
          "count": 28,
          "composition": {
            "militia": 10,
            "spearman": 7,
            "archer": 7,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 694,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 28,
          "composition": {
            "militia": 10,
            "spearman": 7,
            "archer": 7,
            "scoutCavalry": 4
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1388,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 31,
          "composition": {
            "militia": 12,
            "spearman": 7,
            "archer": 7,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 2082,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 10,
        "spearman": 7,
        "archer": 7,
        "scoutCavalry": 4
      },
      "enemyNominalResourceCost": {
        "food": 4860,
        "wood": 1400,
        "gold": 2100,
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
        45
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
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
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
    "travelTime": "Measure nav-path length in tiles / actual convoy speed plus loading/unloading; two round trips must fit between phase waves. If not, adjust announced gap or move receiving point within same documented district; architect approval for footprint drift.",
    "minimumWaveGapSecondsFromProposedGeometry": 694
  }
}
```

## Choice, failure and recovery

Salvar más familias o recuperar segundo testimonio como bonus: ninguno cambia 680 ni desbloquea una religión. Recomendar I02 para perspectiva política paralela.

Personajes venerados fuera de mapa/no derrotables; convoy de familias ficticias. Dos pozos/rutas con presupuesto visible y un último relevo limitado; sin final histórico alternativo.

{
  "plan": "Personajes venerados fuera de mapa/no derrotables; convoy de familias ficticias. Dos pozos/rutas con presupuesto visible y un último relevo limitado; sin final histórico alternativo.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.house-of-ali.04-the-water-that-remains.title` / always | none → next | The Water That Remains | El agua que queda |
| `scenario.house-of-ali.04-the-water-that-remains.fact-intro` / intro first | collection-narrator → next | Husayn was killed at Karbala in 680. The player assists fictional travelling families; their escape does not change that historical outcome. | Husayn muere en Karbala; números/discursos y motivos detallados varían según transmisión. Misión acompaña viajeros ficticios fuera del campamento histórico, no recrea el martirio como espectáculo. |
| `scenario.house-of-ali.04-the-water-that-remains.personal-intro` / after fact-intro | dina-potter → next | I was old enough now to know a road could close. I filled the jars before asking which story would be told about the men beyond it. | Ahora tenía edad para saber que un camino podía cerrarse. Llené las vasijas antes de preguntar qué historia se contaría de los hombres que quedaban al otro lado. |
| `scenario.house-of-ali.04-the-water-that-remains.objective-1` / phase-1 active | none → hub-1 | Mark the two civilian withdrawal paths east of the dry camp. | Señala los dos caminos civiles de retirada al este del campamento seco. |
| `scenario.house-of-ali.04-the-water-that-remains.objective-2` / phase-2 active | none → hub-2 | Carry the water and records to six of eight travelling family groups. | Lleva el agua y los registros a seis de ocho grupos familiares viajeros. |
| `scenario.house-of-ali.04-the-water-that-remains.objective-3` / phase-3 active | none → hub-3 | Withdraw the families and preserve the two testimony copies. | Retira a las familias y conserva las dos copias de los testimonios. |
| `scenario.house-of-ali.04-the-water-that-remains.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.house-of-ali.04-the-water-that-remains.scouts` / scouts panel | none → next | Regional setting: Karbala plain. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Karbala plain. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.house-of-ali.04-the-water-that-remains.history` / history panel | none → next | Husayn was killed at Karbala in 680. The player assists fictional travelling families; their escape does not change that historical outcome. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Husayn muere en Karbala; números/discursos y motivos detallados varían según transmisión. Misión acompaña viajeros ficticios fuera del campamento histórico, no recrea el martirio como espectáculo. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.house-of-ali.04-the-water-that-remains.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.house-of-ali.04-the-water-that-remains.event-phase-1-complete` / o1 first becomes true | dina-potter → next | The first household has water. I know the weight of a full jar better than the weight of a title. | La primera familia tiene agua. Conozco mejor el peso de una jarra llena que el de un título. |
| `scenario.house-of-ali.04-the-water-that-remains.event-phase-2-complete` / o2 first becomes true | dina-potter → next | There is another road for the families. Tell them before the dust hides it. | Hay otro camino para las familias. Díselo antes de que lo oculte el polvo. |
| `scenario.house-of-ali.04-the-water-that-remains.event-phase-3-complete` / o3 first becomes true | dina-potter → next | I kept the names. I cannot turn what happened into a kinder ending. | Guardé los nombres. No puedo transformar lo que ocurrió en un final más amable. |
| `scenario.house-of-ali.04-the-water-that-remains.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | dina-potter → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.house-of-ali.04-the-water-that-remains.victory-fact` / victory latch first | collection-narrator → next | Husayn was killed at Karbala in 680. The player assists fictional travelling families; their escape does not change that historical outcome. Your mission task is complete; this outcome does not change the documented events. | Narrador común expone la muerte documentada sobriamente; Dina cierra su experiencia ficticia sin atribuirse diálogos de Husayn. Memoria posterior se contextualiza. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.house-of-ali.04-the-water-that-remains.victory-personal` / after victory-fact | dina-potter → campaign ending | I kept the names. I cannot turn what happened into a kinder ending. | Guardé los nombres. No puedo transformar lo que ocurrió en un final más amable. |
| `scenario.house-of-ali.04-the-water-that-remains.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.house-of-ali.04-the-water-that-remains.recovery` / 6 minutes without objective progress | dina-potter → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |

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
