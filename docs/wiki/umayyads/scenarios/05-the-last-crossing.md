# The Last Crossing / El último cruce

`umayyads/05-the-last-crossing` · 750 CE · army-withdrawal

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/umayyads/05-the-last-crossing.svg)

## Historical frame and outcome

The Abbasid transition of 750 ended the Umayyad caliphate in the east. This scenario reconstructs a retreat in the Great Zab region; its exact camp layout is uncertain.

La derrota omeya y ascenso abasí cierran gobierno de Damasco. El escape del jugador es de personajes ficticios; no revierte el desenlace.

750 derrota fija; 756 se menciona como otro arco. CDF-I03 ofrece perspectiva familiar paralela de 656–680.

- [The Met, Art of the Umayyad Period](https://www.metmuseum.org/essays/the-art-of-the-umayyad-period-661-750): Dinastía y arquitectura. Referencia material; una construcción no mide la fe de sus habitantes.
- [C. E. Bosworth, Abbasid Caliphate](https://www.iranicaonline.org/articles/abbasid-caliphate/): Establishment in 750. Supports dynastic transition; does not authenticate our tactical retreat, camp coordinates or unit counts.
- [El-Hussein A. Y. Aly, The Graeco-Arabic Translation Movement, publisher excerpt](https://assets.cambridge.org/97810093/85602/excerpt/9781009385602_excerpt.pdf): Introduction, historical Umayyad context: Great Zab750. Accessible publisher excerpt downloaded temporarily and read, not whole monograph. Narrow chronology only; deployments remain fictional.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

At last this is a page I wrote myself. I had learned the price of success; the river taught me the weight of what could still be carried away.

Por fin esta página la escribí yo. Había aprendido el precio del éxito; el río me enseñó el peso de lo que aún podía sacarse de allí.

## Geography and map construction

Great Zab / northern Iraq — 400 × 400 tiles; north-up design controls [43.05, 35.7, 43.75, 36.3].

Llanuras y estribaciones septentrionales iraquíes.

Gran Zab desciende de noreste hacia Tigris al suroeste; localización de combate aproximada.

Colinas al noreste; llano para convoyes cerca de río.

Pasos y rutas hacia Mosul/oeste; Siria fuera del mapa.

Exclude: Sin castillos medievales tardíos ni plantear una victoria omeya histórica en 750.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Great Zab regional crossing, uncertain | [43.49, 36.06] | [242.73, 163.87] |
| Northeast river corridor | [43.7, 36.25] | [343.61, 51.06] |
| Southern withdrawal approach | [43.41, 35.88] | [204.3, 270.75] |

```json
{
  "bbox": [
    43.05,
    35.7,
    43.75,
    36.3
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Great Zab regional crossing, uncertain",
      "lonLat": [
        43.49,
        36.06
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        242.73,
        163.87
      ]
    },
    {
      "id": "anchor-2",
      "name": "Northeast river corridor",
      "lonLat": [
        43.7,
        36.25
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        343.61,
        51.06
      ]
    },
    {
      "id": "anchor-3",
      "name": "Southern withdrawal approach",
      "lonLat": [
        43.41,
        35.88
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        204.3,
        270.75
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-2",
      "centre": [
        343.61,
        51.06
      ],
      "purpose": {
        "en": "Open the southern retreat crossing before the reserve arrives.",
        "es-ES": "Abre el paso meridional de retirada antes de que llegue la reserva."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        242.73,
        163.87
      ],
      "purpose": {
        "en": "Recover the two supply wagons and surviving carriers.",
        "es-ES": "Recupera los dos carros de víveres y los porteadores supervivientes."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-3",
      "centre": [
        204.3,
        270.75
      ],
      "purpose": {
        "en": "Withdraw at least six of eight civilian parties with the family ledger.",
        "es-ES": "Retira al menos seis de ocho grupos civiles con el registro familiar."
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
          343.61,
          51.06
        ],
        [
          242.73,
          163.87
        ],
        [
          204.3,
          270.75
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          343.61,
          51.06
        ],
        [
          309.17,
          123.465
        ],
        [
          242.73,
          163.87
        ],
        [
          204.3,
          270.75
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        43.75,
        36.3
      ],
      [
        43.7,
        36.25
      ],
      [
        43.6,
        36.16
      ],
      [
        43.49,
        36.06
      ],
      [
        43.43,
        35.97
      ],
      [
        43.3,
        35.9
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "zab",
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
  "asset": "docs/design/maps/umayyads/05-the-last-crossing.svg",
  "mainRouteLengthStraightTiles": 264.92
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
        "en": "Open the southern retreat crossing before the reserve arrives.",
        "es-ES": "Abre el paso meridional de retirada antes de que llegue la reserva."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-1",
        "oncePerEntity": true,
        "required": "Open the southern retreat crossing before the reserve arrives."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "secure-crossing",
      "threshold": 1,
      "entities": [
        {
          "id": "05-the-last-crossing-o1-entity-1",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "secure-crossing",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "secure-crossing",
        "requiredCount": 1,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Open the southern retreat crossing before the reserve arrives.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Recover the two supply wagons and surviving carriers.",
        "es-ES": "Recupera los dos carros de víveres y los porteadores supervivientes."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-2",
        "oncePerEntity": true,
        "required": "Recover the two supply wagons and surviving carriers."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "recover-wagon",
      "threshold": 2,
      "entities": [
        {
          "id": "05-the-last-crossing-o2-entity-1",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "recover-wagon",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-the-last-crossing-o2-entity-2",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "recover-wagon",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "recover-wagon",
        "requiredCount": 2,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Recover the two supply wagons and surviving carriers.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Withdraw at least six of eight civilian parties with the family ledger.",
        "es-ES": "Retira al menos seis de ocho grupos civiles con el registro familiar."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-3",
        "oncePerEntity": true,
        "required": "Withdraw at least six of eight civilian parties with the family ledger."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "evacuate-family",
      "threshold": 6,
      "entities": [
        {
          "id": "05-the-last-crossing-o3-entity-1",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-the-last-crossing-o3-entity-2",
          "atHub": "hub-3",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-the-last-crossing-o3-entity-3",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            -2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-the-last-crossing-o3-entity-4",
          "atHub": "hub-3",
          "offsetTiles": [
            6,
            -2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-the-last-crossing-o3-entity-5",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-the-last-crossing-o3-entity-6",
          "atHub": "hub-3",
          "offsetTiles": [
            6,
            2
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-the-last-crossing-o3-entity-7",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            6
          ],
          "role": "evacuate-family",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "05-the-last-crossing-o3-entity-8",
          "atHub": "hub-3",
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
        "destination": "hub-3",
        "defeatBelowRemaining": 6,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Withdraw at least six of eight civilian parties with the family ledger.",
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
| easy | 875/625/312/250 | 1885/1075/1128/550 | 16 | 36 + 36 + 36 + 36 = 144 | 120 / 847 |
| standard | 700/500/250/200 | 1820/1100/1030/600 | 12 | 48 + 48 + 48 + 48 = 192 | 90 / 847 |
| hard | 595/425/212/170 | 1805/1125/988/630 | 10 | 57 + 57 + 57 + 59 = 230 | 75 / 847 |

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
          "offsetSeconds": 847,
          "warningSeconds": 120,
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
          "offsetSeconds": 1694,
          "warningSeconds": 120,
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
          "offsetSeconds": 2541,
          "warningSeconds": 120,
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
      "enemyTotalCap": 192,
      "initialEnemy": 48,
      "waves": [
        {
          "id": "wave-1",
          "count": 48,
          "composition": {
            "militia": 16,
            "spearman": 12,
            "archer": 12,
            "scoutCavalry": 8
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 847,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 48,
          "composition": {
            "militia": 16,
            "spearman": 12,
            "archer": 12,
            "scoutCavalry": 8
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1694,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 48,
          "composition": {
            "militia": 16,
            "spearman": 12,
            "archer": 12,
            "scoutCavalry": 8
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 2541,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 16,
        "spearman": 12,
        "archer": 12,
        "scoutCavalry": 8
      },
      "enemyNominalResourceCost": {
        "food": 8080,
        "wood": 2400,
        "gold": 3440,
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
      "enemyTotalCap": 230,
      "initialEnemy": 57,
      "waves": [
        {
          "id": "wave-1",
          "count": 57,
          "composition": {
            "militia": 20,
            "spearman": 14,
            "archer": 14,
            "scoutCavalry": 9
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 847,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 57,
          "composition": {
            "militia": 20,
            "spearman": 14,
            "archer": 14,
            "scoutCavalry": 9
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1694,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 59,
          "composition": {
            "militia": 22,
            "spearman": 14,
            "archer": 14,
            "scoutCavalry": 9
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 2541,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 20,
        "spearman": 14,
        "archer": 14,
        "scoutCavalry": 9
      },
      "enemyNominalResourceCost": {
        "food": 9760,
        "wood": 2800,
        "gold": 4160,
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
    "minimumWaveGapSecondsFromProposedGeometry": 847
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Cruce secundario y camino de margen; no instantkill al cargador de registro sin advertencia. Un registro recuperable en carro alternativo, olas finitas se agotan.

{
  "plan": "Cruce secundario y camino de margen; no instantkill al cargador de registro sin advertencia. Un registro recuperable en carro alternativo, olas finitas se agotan.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.umayyads.05-the-last-crossing.title` / always | none → next | The Last Crossing | El último cruce |
| `scenario.umayyads.05-the-last-crossing.fact-intro` / intro first | collection-narrator → next | The Abbasid transition of 750 ended the Umayyad caliphate in the east. This scenario reconstructs a retreat in the Great Zab region; its exact camp layout is uncertain. | La derrota omeya y ascenso abasí cierran gobierno de Damasco. El escape del jugador es de personajes ficticios; no revierte el desenlace. |
| `scenario.umayyads.05-the-last-crossing.personal-intro` / after fact-intro | yasir-cloth-merchant → next | At last this is a page I wrote myself. I had learned the price of success; the river taught me the weight of what could still be carried away. | Por fin esta página la escribí yo. Había aprendido el precio del éxito; el río me enseñó el peso de lo que aún podía sacarse de allí. |
| `scenario.umayyads.05-the-last-crossing.objective-1` / phase-1 active | none → hub-1 | Open the southern retreat crossing before the reserve arrives. | Abre el paso meridional de retirada antes de que llegue la reserva. |
| `scenario.umayyads.05-the-last-crossing.objective-2` / phase-2 active | none → hub-2 | Recover the two supply wagons and surviving carriers. | Recupera los dos carros de víveres y los porteadores supervivientes. |
| `scenario.umayyads.05-the-last-crossing.objective-3` / phase-3 active | none → hub-3 | Withdraw at least six of eight civilian parties with the family ledger. | Retira al menos seis de ocho grupos civiles con el registro familiar. |
| `scenario.umayyads.05-the-last-crossing.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.umayyads.05-the-last-crossing.scouts` / scouts panel | none → next | Regional setting: Great Zab / northern Iraq. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Great Zab / northern Iraq. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.umayyads.05-the-last-crossing.history` / history panel | none → next | The Abbasid transition of 750 ended the Umayyad caliphate in the east. This scenario reconstructs a retreat in the Great Zab region; its exact camp layout is uncertain. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | La derrota omeya y ascenso abasí cierran gobierno de Damasco. El escape del jugador es de personajes ficticios; no revierte el desenlace. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.umayyads.05-the-last-crossing.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.umayyads.05-the-last-crossing.event-phase-1-complete` / o1 first becomes true | yasir-cloth-merchant → next | The first load arrived. My family’s old accounts rarely mention the people who carried it. | La primera carga ha llegado. Las cuentas antiguas de mi familia apenas nombran a quienes la llevaron. |
| `scenario.umayyads.05-the-last-crossing.event-phase-2-complete` / o2 first becomes true | yasir-cloth-merchant → next | Keep the shore store supplied. An ambitious road still needs somewhere to return. | Mantén abastecido el almacén de la costa. Hasta un camino ambicioso necesita un lugar al que volver. |
| `scenario.umayyads.05-the-last-crossing.event-phase-3-complete` / o3 first becomes true | yasir-cloth-merchant → next | The ledger survived. That is less than victory, and more than nothing. | El registro sobrevivió. Es menos que una victoria y más que nada. |
| `scenario.umayyads.05-the-last-crossing.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | yasir-cloth-merchant → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.umayyads.05-the-last-crossing.victory-fact` / victory latch first | collection-narrator → next | The Abbasid transition of 750 ended the Umayyad caliphate in the east. This scenario reconstructs a retreat in the Great Zab region; its exact camp layout is uncertain. Your mission task is complete; this outcome does not change the documented events. | 750 derrota fija; 756 se menciona como otro arco. CDF-I03 ofrece perspectiva familiar paralela de 656–680. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.umayyads.05-the-last-crossing.victory-personal` / after victory-fact | yasir-cloth-merchant → campaign ending | The ledger survived. That is less than victory, and more than nothing. | El registro sobrevivió. Es menos que una victoria y más que nada. |
| `scenario.umayyads.05-the-last-crossing.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.umayyads.05-the-last-crossing.recovery` / 6 minutes without objective progress | yasir-cloth-merchant → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |

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
