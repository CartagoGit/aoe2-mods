# Winter at the Walls / Invierno ante las murallas

`new-rome/04-winter-at-the-walls` · 717–718 CE · siege-and-supply

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/new-rome/04-winter-at-the-walls.svg)

## Historical frame and outcome

The Umayyad siege of Constantinople in 717–718 failed. The three attacks in this scenario compress a much longer campaign.

Asedio árabe de Constantinopla: defensa y abastecimiento del recinto. Fechas generales sólidas; detalles de tormentas/efectivos requieren contraste específico.

Retirada de sitiadores se explica como proceso; temporizador no reemplaza éxito de defensa y suministro.

- [The Met, Byzantium (ca. 330–1453)](https://www.metmuseum.org/essays/byzantium-ca-330-1453): Períodos y cultura material. Ensayo de museo de síntesis, no plano arqueológico ni cronología militar completa.
- [UNESCO, Historic Areas of Istanbul](https://whc.unesco.org/en/list/356/): Península, murallas y monumentos. Paisaje de varias épocas: filtrar fecha de cada edificio.
- [E. W. Brooks, The Campaign of 716–718, from Arabic Sources (1899)](https://www.cambridge.org/core/journals/journal-of-hellenic-studies/article/abs/campaign-of-716718-from-arabic-sources/7FA64C84BFD76CECFF0AB6C528D6C854): Published extract and source discussion. Only the accessible extract was consulted, not the paywalled full paper.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

The wall in my lesson book was a line. The wall I repaired had drains, loose stone and men who needed to sleep.

La muralla del libro de aprendizaje era una línea. La que reparé tenía desagües, piedras sueltas y hombres que necesitaban dormir.

## Geography and map construction

Byzantion / Constantinople peninsula — 400 × 400 tiles; north-up design controls [28.88, 40.96, 29.04, 41.07].

Península urbana y huertas de Tracia al oeste.

Cuerno de Oro al norte; Bósforo al este; Propóntide al sur.

Lomas de península, sin montañas interiores.

Accesos terrestres desde oeste; puertos al sur/norte.

Exclude: Antes 413 no muralla teodosiana; antes 537 no Hagia Sophia actual; sin minaretes ni puente moderno del Bósforo.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Historic peninsula core | [28.978, 41.009] | [239.58, 217.21] |
| Land wall corridor | [28.925, 41.025] | [121.57, 169.99] |
| Golden Horn quay | [28.965, 41.024] | [210.63, 172.94] |

```json
{
  "bbox": [
    28.88,
    40.96,
    29.04,
    41.07
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Historic peninsula core",
      "lonLat": [
        28.978,
        41.009
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        239.58,
        217.21
      ]
    },
    {
      "id": "anchor-2",
      "name": "Land wall corridor",
      "lonLat": [
        28.925,
        41.025
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        121.57,
        169.99
      ]
    },
    {
      "id": "anchor-3",
      "name": "Golden Horn quay",
      "lonLat": [
        28.965,
        41.024
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        210.63,
        172.94
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        210.63,
        172.94
      ],
      "purpose": {
        "en": "Secure the land-wall repair depots and northern harbour.",
        "es-ES": "Asegura los depósitos de reparación del muro terrestre y el puerto norte."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        239.58,
        217.21
      ],
      "purpose": {
        "en": "Withstand three announced siege efforts while keeping two supply routes.",
        "es-ES": "Resiste tres esfuerzos de asedio anunciados conservando dos rutas de suministro."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-2",
      "centre": [
        121.57,
        169.99
      ],
      "purpose": {
        "en": "Deliver the final winter convoy and hold the designated western gate.",
        "es-ES": "Entrega el último convoy invernal y conserva la puerta occidental designada."
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
          210.63,
          172.94
        ],
        [
          239.58,
          217.21
        ],
        [
          121.57,
          169.99
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          210.63,
          172.94
        ],
        [
          209.10500000000002,
          179.075
        ],
        [
          239.58,
          217.21
        ],
        [
          121.57,
          169.99
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
  "terrainProfile": "constantinople",
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
  "asset": "docs/design/maps/new-rome/04-winter-at-the-walls.svg",
  "mainRouteLengthStraightTiles": 180.0
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
        "en": "Secure the land-wall repair depots and northern harbour.",
        "es-ES": "Asegura los depósitos de reparación del muro terrestre y el puerto norte."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-1",
        "oncePerEntity": true,
        "required": "Secure the land-wall repair depots and northern harbour."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "restore-depot",
      "threshold": 2,
      "entities": [
        {
          "id": "04-winter-at-the-walls-o1-entity-1",
          "atHub": "hub-1",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "restore-depot",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-winter-at-the-walls-o1-entity-2",
          "atHub": "hub-1",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "restore-depot",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "restore-depot",
        "requiredCount": 2,
        "destination": "hub-1",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Secure the land-wall repair depots and northern harbour.",
        "phaseGated": true,
        "neverUseTimerInstead": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Withstand three announced siege efforts while keeping two supply routes.",
        "es-ES": "Resiste tres esfuerzos de asedio anunciados conservando dos rutas de suministro."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-2",
        "oncePerEntity": true,
        "required": "Withstand three announced siege efforts while keeping two supply routes."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "survive-finite-waves",
      "threshold": 3,
      "entities": [
        {
          "id": "04-winter-at-the-walls-o2-entity-1",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "survive-finite-waves",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-winter-at-the-walls-o2-entity-2",
          "atHub": "hub-2",
          "offsetTiles": [
            6,
            -6
          ],
          "role": "survive-finite-waves",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        },
        {
          "id": "04-winter-at-the-walls-o2-entity-3",
          "atHub": "hub-2",
          "offsetTiles": [
            -6,
            -2
          ],
          "role": "survive-finite-waves",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "survive-finite-waves",
        "requiredCount": 3,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "criticalSecondaryRequirements": "Withstand three announced siege efforts while keeping two supply routes.",
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "supplyRoutesRequired": 2
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Deliver the final winter convoy and hold the designated western gate.",
        "es-ES": "Entrega el último convoy invernal y conserva la puerta occidental designada."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "ledger-3",
        "oncePerEntity": true,
        "required": "Deliver the final winter convoy and hold the designated western gate."
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "deliver-convoy-and-hold",
      "threshold": 1,
      "entities": [
        {
          "id": "04-winter-at-the-walls-o3-entity-1",
          "atHub": "hub-3",
          "offsetTiles": [
            -6,
            -6
          ],
          "role": "deliver-convoy-and-hold",
          "countedOnce": true,
          "historicalIdentity": "fictional gameplay object; no impersonated historical authority"
        }
      ],
      "predicate": {
        "operator": "all-required-ledgers-latched",
        "operation": "deliver-convoy-and-hold",
        "requiredCount": 1,
        "destination": "hub-3",
        "defeatBelowRemaining": null,
        "resourceAmounts": {
          "food": 400
        },
        "criticalSecondaryRequirements": "Deliver the final winter convoy and hold the designated western gate.",
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "foodConsignment": 400,
        "holdSecondsRelative": 180
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
| easy | 1125/875/500/250 | 2755/1125/1420/550 | 28 | 33 + 33 + 33 + 36 = 135 | 120 / 605 |
| standard | 900/700/400/200 | 2740/1200/1360/600 | 24 | 45 + 45 + 45 + 45 = 180 | 90 / 605 |
| hard | 765/595/340/170 | 2635/1205/1260/630 | 20 | 54 + 54 + 54 + 54 = 216 | 75 / 605 |

```json
{
  "profiles": {
    "easy": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 1125,
        "wood": 875,
        "gold": 500,
        "stone": 250
      },
      "gatherableBank": {
        "food": 2755,
        "wood": 1125,
        "gold": 1420,
        "stone": 550
      },
      "mandatoryDeliveries": {
        "food": 400,
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
      "maxVillagers": 24,
      "startingEscortCount": 28,
      "playerPopulationCap": 140,
      "enemyTotalCap": 135,
      "initialEnemy": 33,
      "waves": [
        {
          "id": "wave-1",
          "count": 33,
          "composition": {
            "militia": 12,
            "spearman": 8,
            "archer": 8,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 605,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 33,
          "composition": {
            "militia": 12,
            "spearman": 8,
            "archer": 8,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1210,
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
          "offsetSeconds": 1815,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 12,
        "spearman": 8,
        "archer": 8,
        "scoutCavalry": 5
      },
      "enemyNominalResourceCost": {
        "food": 5715,
        "wood": 1650,
        "gold": 2445,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 2280,
        "wood": 1300,
        "gold": 1320,
        "stone": 300
      },
      "roughDurationMinutes": [
        30,
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
        "militia": 14,
        "spearman": 7,
        "archer": 7
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
    },
    "standard": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 900,
        "wood": 700,
        "gold": 400,
        "stone": 200
      },
      "gatherableBank": {
        "food": 2740,
        "wood": 1200,
        "gold": 1360,
        "stone": 600
      },
      "mandatoryDeliveries": {
        "food": 400,
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
      "maxVillagers": 24,
      "startingEscortCount": 24,
      "playerPopulationCap": 140,
      "enemyTotalCap": 180,
      "initialEnemy": 45,
      "waves": [
        {
          "id": "wave-1",
          "count": 45,
          "composition": {
            "militia": 16,
            "spearman": 11,
            "archer": 11,
            "scoutCavalry": 7
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 605,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 45,
          "composition": {
            "militia": 16,
            "spearman": 11,
            "archer": 11,
            "scoutCavalry": 7
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1210,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 45,
          "composition": {
            "militia": 16,
            "spearman": 11,
            "archer": 11,
            "scoutCavalry": 7
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1815,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 16,
        "spearman": 11,
        "archer": 11,
        "scoutCavalry": 7
      },
      "enemyNominalResourceCost": {
        "food": 7620,
        "wood": 2200,
        "gold": 3260,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 2040,
        "wood": 1200,
        "gold": 1160,
        "stone": 300
      },
      "roughDurationMinutes": [
        30,
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
        "militia": 12,
        "spearman": 6,
        "archer": 6
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
    },
    "hard": {
      "basis": "estimated; must be calibrated in AoE2 before GAME VERIFIED",
      "startingResources": {
        "food": 765,
        "wood": 595,
        "gold": 340,
        "stone": 170
      },
      "gatherableBank": {
        "food": 2635,
        "wood": 1205,
        "gold": 1260,
        "stone": 630
      },
      "mandatoryDeliveries": {
        "food": 400,
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
      "maxVillagers": 24,
      "startingEscortCount": 20,
      "playerPopulationCap": 140,
      "enemyTotalCap": 216,
      "initialEnemy": 54,
      "waves": [
        {
          "id": "wave-1",
          "count": 54,
          "composition": {
            "militia": 19,
            "spearman": 13,
            "archer": 13,
            "scoutCavalry": 9
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 605,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 54,
          "composition": {
            "militia": 19,
            "spearman": 13,
            "archer": 13,
            "scoutCavalry": 9
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1210,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 54,
          "composition": {
            "militia": 19,
            "spearman": 13,
            "archer": 13,
            "scoutCavalry": 9
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1815,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 19,
        "spearman": 13,
        "archer": 13,
        "scoutCavalry": 9
      },
      "enemyNominalResourceCost": {
        "food": 9260,
        "wood": 2600,
        "gold": 3860,
        "stone": 0
      },
      "enemyProduction": false,
      "regeneratingResources": false,
      "replacementBudget": {
        "food": 1800,
        "wood": 1100,
        "gold": 1000,
        "stone": 300
      },
      "roughDurationMinutes": [
        30,
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
        "militia": 10,
        "spearman": 5,
        "archer": 5
      },
      "recoveryEscortCount": 4,
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn."
    }
  },
  "analysis": {
    "classification": "feasibility envelope, not a combat simulation or proof of balance",
    "startingWorkers": 12,
    "plannedPeakWorkers": 24,
    "effectiveGatherRatePerWorkerResourcePerSecondAssumption": 0.24,
    "walkingAndIdleIncluded": "Assumed rate discounts native gathering for travel/idle; measure actual efficiency in game.",
    "worstDeliveryFood": 400,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Measure nav-path length in tiles / actual convoy speed plus loading/unloading; two round trips must fit between phase waves. If not, adjust announced gap or move receiving point within same documented district; architect approval for footprint drift.",
    "minimumWaveGapSecondsFromProposedGeometry": 605
  }
}
```

## Choice, failure and recovery

Escoger ruta principal o alternativa: el hecho histórico y objetivos principales permanecen.

Depósitos oeste/norte; reparar consume reserva visible. No fuego griego como instantkill: perfil de arma pendiente de soporte; ruta naval necesita pruebas reales.

{
  "plan": "Depósitos oeste/norte; reparar consume reserva visible. No fuego griego como instantkill: perfil de arma pendiente de soporte; ruta naval necesita pruebas reales.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.new-rome.04-winter-at-the-walls.title` / always | none → next | Winter at the Walls | Invierno ante las murallas |
| `scenario.new-rome.04-winter-at-the-walls.fact-intro` / intro first | collection-narrator → next | The Umayyad siege of Constantinople in 717–718 failed. The three attacks in this scenario compress a much longer campaign. | Asedio árabe de Constantinopla: defensa y abastecimiento del recinto. Fechas generales sólidas; detalles de tormentas/efectivos requieren contraste específico. |
| `scenario.new-rome.04-winter-at-the-walls.personal-intro` / after fact-intro | anna-mosaicist → next | The wall in my lesson book was a line. The wall I repaired had drains, loose stone and men who needed to sleep. | La muralla del libro de aprendizaje era una línea. La que reparé tenía desagües, piedras sueltas y hombres que necesitaban dormir. |
| `scenario.new-rome.04-winter-at-the-walls.objective-1` / phase-1 active | none → hub-1 | Secure the land-wall repair depots and northern harbour. | Asegura los depósitos de reparación del muro terrestre y el puerto norte. |
| `scenario.new-rome.04-winter-at-the-walls.objective-2` / phase-2 active | none → hub-2 | Withstand three announced siege efforts while keeping two supply routes. | Resiste tres esfuerzos de asedio anunciados conservando dos rutas de suministro. |
| `scenario.new-rome.04-winter-at-the-walls.objective-3` / phase-3 active | none → hub-3 | Deliver the final winter convoy and hold the designated western gate. | Entrega el último convoy invernal y conserva la puerta occidental designada. |
| `scenario.new-rome.04-winter-at-the-walls.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.new-rome.04-winter-at-the-walls.scouts` / scouts panel | none → next | Regional setting: Byzantion / Constantinople peninsula. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Byzantion / Constantinople peninsula. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.new-rome.04-winter-at-the-walls.history` / history panel | none → next | The Umayyad siege of Constantinople in 717–718 failed. The three attacks in this scenario compress a much longer campaign. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Asedio árabe de Constantinopla: defensa y abastecimiento del recinto. Fechas generales sólidas; detalles de tormentas/efectivos requieren contraste específico. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.new-rome.04-winter-at-the-walls.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.new-rome.04-winter-at-the-walls.event-phase-1-complete` / o1 first becomes true | anna-mosaicist → next | The first piece is in place. A city is harder to mend than a mosaic. | La primera pieza está en su sitio. Una ciudad es más difícil de reparar que un mosaico. |
| `scenario.new-rome.04-winter-at-the-walls.event-phase-2-complete` / o2 first becomes true | anna-mosaicist → next | I used to notice only the broken images. Now I notice who carries them. | Antes solo veía las imágenes rotas. Ahora veo quién las lleva. |
| `scenario.new-rome.04-winter-at-the-walls.event-phase-3-complete` / o3 first becomes true | anna-mosaicist → next | Keep the inventory beside the pieces. Memory should not become another excuse to destroy. | Guarda el inventario junto a las piezas. La memoria no debe ser otra excusa para destruir. |
| `scenario.new-rome.04-winter-at-the-walls.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | anna-mosaicist → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.new-rome.04-winter-at-the-walls.victory-fact` / victory latch first | collection-narrator → next | The Umayyad siege of Constantinople in 717–718 failed. The three attacks in this scenario compress a much longer campaign. Your mission task is complete; this outcome does not change the documented events. | Retirada de sitiadores se explica como proceso; temporizador no reemplaza éxito de defensa y suministro. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.new-rome.04-winter-at-the-walls.victory-personal` / after victory-fact | anna-mosaicist → 05-pieces-of-a-memory | Keep the inventory beside the pieces. Memory should not become another excuse to destroy. | Guarda el inventario junto a las piezas. La memoria no debe ser otra excusa para destruir. |
| `scenario.new-rome.04-winter-at-the-walls.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.new-rome.04-winter-at-the-walls.recovery` / 6 minutes without objective progress | anna-mosaicist → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |

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
