# Fields of the Sawad / Los campos del Sawad

`first-caliphs/04-fields-of-the-sawad` · mid-630s; conventional 636/637 · irrigation-front-battle

[Campaign contract](../12-production-blueprint.md) · [Narrator](../13-narrator-bible.md) · [Geographic plan](../../../design/maps/first-caliphs/04-fields-of-the-sawad.svg)

## Historical frame and outcome

The battle conventionally dated to 636 or 637 at Qadisiyya contributed to the loss of Sasanian control in Iraq. Its date and battlefield details are debated.

Qadisiyya enfrenta fuerzas árabes y sasánidas; fecha y sitio precisos son discutidos. Se conserva resultado general sin inventar orden de batalla seguro.

Cambios políticos tras victoria; no presentar conversiones iraníes como instantáneas ni batalla étnica eterna.

- [D. Gershon Lewental, Qadesiya, Battle of](https://www.iranicaonline.org/articles/qadesiya-battle/): Cronología, lugar y discusión de las fuentes. 636/637 es la banda convencional; hay propuestas 634/635. Posición del campo y cifras no se fijan como certeza.

Invented couriers, neighbourhood dialogue, convoys and deployments are dramatization. Neither a personal narrator nor a tactical route can overturn the documented event. Exact battle coordinates and chroniclers’ force totals remain qualified.

## Personal voice

The channels were new to me. I asked the people who worked them where a cart could cross; a soldier’s sketch alone would have drowned the load.

Los canales eran nuevos para mí. Pregunté dónde podía cruzar un carro a quienes los trabajaban; un dibujo militar habría hundido la carga.

## Geography and map construction

Qadisiyya / Sawad approaches — 360 × 360 tiles; north-up design controls [43.75, 31.65, 44.65, 32.3].

Frontera entre estepa occidental y tierras irrigadas iraquíes.

Canales/cauces en este; paleohidrografía incierta, no usar cauce moderno como prueba de 637.

Relieve muy llano; no crear cordilleras en el Sawad.

Ruta de al-Hira y campos; emplazamiento de batalla aproximado.

Exclude: Sitio y fecha discutidos; mapa se titula reconstrucción regional.

Solid-blue map layers are modern Natural Earth data; dashed waterways are architect schematics. Brown/purple routes are proposed tactical corridors and require full footprint and transport QA. Objective districts are fixed to geographic controls; any local adjustment stays within 12 tiles and on appropriate terrain. Ancient shore/canal uncertainty is documented, not silently traced as certain.

| Control | WGS84 longitude,latitude | Tile x,y |
|---|---|---|
| Traditional battle region, uncertain | [44.22, 31.98] | [186.62, 177.4] |
| Al Hira regional control | [44.36, 31.89] | [236.48, 215.19] |
| Western dry approach | [44.03, 31.98] | [118.95, 177.4] |
| Northern withdrawal corridor, regional reconstruction | [44.3, 32.2] | [215.12, 85.03] |

```json
{
  "bbox": [
    43.75,
    31.65,
    44.65,
    32.3
  ],
  "orientation": "north-up geography plan; engine x/y camera orientation separately calibrated, never mirror banks",
  "projection": "WGS84 north-up, cosine corrected longitude, padded square viewport; tile conversion explicitly recorded",
  "landmarks": [
    {
      "id": "anchor-1",
      "name": "Traditional battle region, uncertain",
      "lonLat": [
        44.22,
        31.98
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        186.62,
        177.4
      ]
    },
    {
      "id": "anchor-2",
      "name": "Al Hira regional control",
      "lonLat": [
        44.36,
        31.89
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        236.48,
        215.19
      ]
    },
    {
      "id": "anchor-3",
      "name": "Western dry approach",
      "lonLat": [
        44.03,
        31.98
      ],
      "certainty": "approximate-modern-location; no exact ancient footprint or troop position asserted",
      "tile": [
        118.95,
        177.4
      ]
    },
    {
      "id": "anchor-4",
      "name": "Northern withdrawal corridor, regional reconstruction",
      "lonLat": [
        44.3,
        32.2
      ],
      "certainty": "approximate regional control; fictional receiving point, no historical troop footprint asserted",
      "tile": [
        215.12,
        85.03
      ]
    }
  ],
  "hubs": [
    {
      "id": "hub-1",
      "anchor": "anchor-3",
      "centre": [
        118.95,
        177.4
      ],
      "purpose": {
        "en": "Secure the dry approach and canal crossing.",
        "es-ES": "Asegura el acceso seco y el paso del canal."
      },
      "radiusTiles": 10,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-2",
      "anchor": "anchor-1",
      "centre": [
        186.62,
        177.4
      ],
      "purpose": {
        "en": "Disable two military supply posts while preserving the farms.",
        "es-ES": "Inutiliza dos puestos de suministro militar preservando las granjas."
      },
      "radiusTiles": 12,
      "placement": "objective compound within 12 tiles of centre, on valid land; exact footprint checked after rasterisation"
    },
    {
      "id": "hub-3",
      "anchor": "anchor-4",
      "centre": [
        215.12,
        85.03
      ],
      "purpose": {
        "en": "Open the northern route and protect the retreating civilian carriers.",
        "es-ES": "Abre la ruta norte y protege a los porteadores civiles que se retiran."
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
          118.95,
          177.4
        ],
        [
          186.62,
          177.4
        ],
        [
          215.12,
          85.03
        ]
      ],
      "widthTiles": 10,
      "mode": "land"
    },
    {
      "id": "relief",
      "waypoints": [
        [
          118.95,
          177.4
        ],
        [
          160.78,
          185.4
        ],
        [
          186.62,
          177.4
        ],
        [
          215.12,
          85.03
        ]
      ],
      "widthTiles": 6,
      "mode": "land"
    }
  ],
  "controlLine": {
    "coordinates": [
      [
        44.4,
        32.3
      ],
      [
        44.4,
        32.1
      ],
      [
        44.37,
        31.95
      ],
      [
        44.4,
        31.8
      ]
    ],
    "certainty": "architect schematic based on regional geography; not surveyed ancient hydrology",
    "renderAs": "river-line"
  },
  "terrainProfile": "qadisiyya",
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
  "asset": "docs/design/maps/first-caliphs/04-fields-of-the-sawad.svg",
  "mainRouteLengthStraightTiles": 130.23,
  "phaseSupply": {
    "phase": "phase-2",
    "receivingHub": "hub-2",
    "waypoints": [
      [
        168.62,
        189.4
      ],
      [
        204.62,
        189.4
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
        "en": "Secure the dry approach and canal crossing.",
        "es-ES": "Asegura el acceso seco y el paso del canal."
      },
      "after": [],
      "targetHub": "hub-1",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "04-fields-of-the-sawad.o1",
        "oncePerEntity": true,
        "required": 1
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o1=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "secure-crossing",
      "threshold": 1,
      "entities": [
        {
          "id": "04-fields-of-the-sawad.dry-approach-blocker.1",
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
          "id": "04-fields-of-the-sawad.o1.main-access-blocker.1",
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
        "operation": "secure-crossing",
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
              "04-fields-of-the-sawad.o1.main-access.1"
            ],
            "blockingEnemies": [
              "04-fields-of-the-sawad.o1.main-access-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          },
          {
            "id": "dry-approach",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "04-fields-of-the-sawad.dry-approach.1"
            ],
            "blockingEnemies": [
              "04-fields-of-the-sawad.dry-approach-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          }
        ],
        "requiredLedgers": [
          "main-access",
          "dry-approach"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o2",
      "text": {
        "en": "Disable two military supply posts while preserving the farms.",
        "es-ES": "Inutiliza dos puestos de suministro militar preservando las granjas."
      },
      "after": [
        "o1"
      ],
      "targetHub": "hub-2",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "04-fields-of-the-sawad.o2",
        "oncePerEntity": true,
        "required": 2
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o2=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "destroy-military-post",
      "threshold": 2,
      "entities": [
        {
          "id": "04-fields-of-the-sawad.o2-post.1",
          "role": "military-post",
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
        },
        {
          "id": "04-fields-of-the-sawad.o2-post.2",
          "role": "military-post",
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
        "operation": "destroy-military-post",
        "requiredCount": 2,
        "destination": "hub-2",
        "defeatBelowRemaining": null,
        "resourceAmounts": {},
        "phaseGated": true,
        "neverUseTimerInstead": true,
        "requirements": [
          {
            "id": "defeated-posts",
            "kind": "entity-state",
            "state": "destroyed",
            "entities": [
              "04-fields-of-the-sawad.o2-post.1",
              "04-fields-of-the-sawad.o2-post.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true
          },
          {
            "id": "protect-farms",
            "kind": "civilian-protection",
            "zones": [
              "04-fields-of-the-sawad.protect-farms.1",
              "04-fields-of-the-sawad.protect-farms.2"
            ],
            "rule": "no player damage, seizure or conversion of protected civilian sites",
            "implementation": "neutral diplomacy + disable conversion/capture; illegal player attack order refused; do not fail for AI collateral",
            "activeFrom": "briefing",
            "activeUntil": "victory"
          }
        ],
        "requiredLedgers": [
          "defeated-posts",
          "protect-farms"
        ],
        "allRequired": true
      }
    },
    {
      "id": "o3",
      "text": {
        "en": "Open the northern route and protect the retreating civilian carriers.",
        "es-ES": "Abre la ruta norte y protege a los porteadores civiles que se retiran."
      },
      "after": [
        "o2"
      ],
      "targetHub": "hub-3",
      "completion": "Latched world-state predicate for listed deliveries, escort arrivals, records or military outposts. A moved unit is not a completed delivery until it enters destination zone and is counted once.",
      "countLedger": {
        "id": "04-fields-of-the-sawad.o3",
        "oncePerEntity": true,
        "required": 1
      },
      "earlyCompletion": "Capture persistent destroyed/arrived/paid state before phase activation; never require event to occur twice.",
      "effect": "latch o3=1; enable next phase once; show objective text and campaign narrator reaction",
      "capability": "zone-membership + unique entity counter + audited resource transaction; military units require actual destroyed/captured predicate, never elapsed-time substitute",
      "operation": "withdraw-escort",
      "threshold": 1,
      "entities": [
        {
          "id": "04-fields-of-the-sawad.northern-route-blocker.1",
          "role": "military-guard",
          "initialHub": "hub-3",
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
          "atHub": "hub-3"
        },
        {
          "id": "04-fields-of-the-sawad.o3.civilian-carriers.1",
          "role": "civilian-carrier",
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
          "id": "04-fields-of-the-sawad.o3.civilian-carriers.2",
          "role": "civilian-carrier",
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
          "id": "04-fields-of-the-sawad.o3.main-entities.1",
          "role": "escort",
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
        "operation": "withdraw-escort",
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
              "04-fields-of-the-sawad.o3.main-entities.1"
            ],
            "requiredCount": 1,
            "oncePerEntity": true,
            "destinations": {
              "04-fields-of-the-sawad.o3.main-entities.1": "04-fields-of-the-sawad.o3.main-entities.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          },
          {
            "id": "northern-route",
            "kind": "area-state",
            "state": "controlled-and-passable",
            "zones": [
              "04-fields-of-the-sawad.northern-route.1"
            ],
            "blockingEnemies": [
              "04-fields-of-the-sawad.northern-route-blocker.1"
            ],
            "requiredCount": 1,
            "proof": "player scout/escort has traversed each zone and designated blockers are dead or outside it; no elapsed-time substitute",
            "mustRemainUntilObjective": "o3"
          },
          {
            "id": "civilian-carriers",
            "kind": "entity-state",
            "state": "arrived",
            "entities": [
              "04-fields-of-the-sawad.o3.civilian-carriers.1",
              "04-fields-of-the-sawad.o3.civilian-carriers.2"
            ],
            "requiredCount": 2,
            "oncePerEntity": true,
            "destinations": {
              "04-fields-of-the-sawad.o3.civilian-carriers.1": "04-fields-of-the-sawad.o3.civilian-carriers.receiving-zone",
              "04-fields-of-the-sawad.o3.civilian-carriers.2": "04-fields-of-the-sawad.o3.civilian-carriers.receiving-zone"
            },
            "arrivalRule": "same token picked up/assigned to carrier before crossing receiving boundary; mere initial presence never delivers. Persist arrival even if phase is not active."
          }
        ],
        "requiredLedgers": [
          "main-entities",
          "northern-route",
          "civilian-carriers"
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
        "id": "04-fields-of-the-sawad.dry-approach-blocker.1",
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
        "id": "04-fields-of-the-sawad.o2-post.1",
        "role": "military-post",
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
        "id": "04-fields-of-the-sawad.o2-post.2",
        "role": "military-post",
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
        "id": "04-fields-of-the-sawad.o3.main-entities.1",
        "role": "escort",
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
        "id": "04-fields-of-the-sawad.northern-route-blocker.1",
        "role": "military-guard",
        "initialHub": "hub-3",
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
        "id": "04-fields-of-the-sawad.o3.civilian-carriers.1",
        "role": "civilian-carrier",
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
        "id": "04-fields-of-the-sawad.o3.civilian-carriers.2",
        "role": "civilian-carrier",
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
        "id": "04-fields-of-the-sawad.o1.main-access-blocker.1",
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
        "id": "04-fields-of-the-sawad.dry-approach.1",
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
        "id": "04-fields-of-the-sawad.protect-farms.1",
        "hub": "hub-2",
        "offsetTiles": [
          -8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": true
      },
      {
        "id": "04-fields-of-the-sawad.protect-farms.2",
        "hub": "hub-2",
        "offsetTiles": [
          8,
          -4
        ],
        "radiusTiles": 4,
        "placement": "valid terrain within 12 tiles of geographic hub; keep labelled bank/ridge/road",
        "protectedCivilian": true
      },
      {
        "id": "04-fields-of-the-sawad.northern-route.1",
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
        "id": "04-fields-of-the-sawad.o3.main-entities.receiving-zone",
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
        "id": "04-fields-of-the-sawad.o3.civilian-carriers.receiving-zone",
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
        "id": "04-fields-of-the-sawad.o1.main-access.1",
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
      "fixedEnemyPosts": 2,
      "preplacedBatteringRams": 2
    },
    "enemyCiv": "Persians",
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
      "kind": "guide",
      "title": {
        "en": "The Path Between — the canal-side dry road",
        "es-ES": "El camino entre ambos — el camino seco junto al canal"
      },
      "subject": {
        "en": "the canal-side dry road",
        "es-ES": "el camino seco junto al canal"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of Fields of the Sawad supports this bounded fictional local task. It concerns the canal-side dry road; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Los campos del Sawad permite esta tarea local ficticia y limitada. Se ocupa de el camino seco junto al canal; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the local guide of the canal-side dry road to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged.",
        "es-ES": "Escolta al guía local de el camino seco junto al canal hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga."
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
              "04-fields-of-the-sawad.side-1.entity-1"
            ],
            "destinations": {
              "04-fields-of-the-sawad.side-1.entity-1": "04-fields-of-the-sawad.side-1.zone-1"
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
            "id": "04-fields-of-the-sawad.side-1.entity-1",
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
            "id": "04-fields-of-the-sawad.side-1.zone-1",
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
          "onceFlag": "04-fields-of-the-sawad.side-1.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "corridorId": "relief"
        }
      ],
      "completionFlag": "04-fields-of-the-sawad.side-1.completed",
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
      "id": "side-2",
      "kind": "scout",
      "title": {
        "en": "The Road Seen First — the canal crossing approaches",
        "es-ES": "El camino visto primero — las aproximaciones al paso del canal"
      },
      "subject": {
        "en": "the canal crossing approaches",
        "es-ES": "las aproximaciones al paso del canal"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of Fields of the Sawad supports this bounded fictional local task. It concerns the canal crossing approaches; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Los campos del Sawad permite esta tarea local ficticia y limitada. Se ocupa de las aproximaciones al paso del canal; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Scout both marked viewpoints of the canal crossing approaches. Benefit: reveal the second reserve approach.",
        "es-ES": "Explora los dos miradores señalados de las aproximaciones al paso del canal. Ventaja: revela la aproximación de la segunda reserva."
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
              "04-fields-of-the-sawad.side-2.zone-1",
              "04-fields-of-the-sawad.side-2.zone-2"
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
            "id": "04-fields-of-the-sawad.side-2.zone-1",
            "hub": "hub-1",
            "offsetTiles": [
              -8,
              0
            ],
            "radiusTiles": 3
          },
          {
            "id": "04-fields-of-the-sawad.side-2.zone-2",
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
          "onceFlag": "04-fields-of-the-sawad.side-2.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "rosterIds": [
            "wave-2"
          ],
          "alreadyReleasedPolicy": "reveal current surviving members, never spawn a replacement"
        }
      ],
      "completionFlag": "04-fields-of-the-sawad.side-2.completed",
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
      "id": "side-3",
      "kind": "repair",
      "title": {
        "en": "Raise the Store Again — the dry-bank supply store",
        "es-ES": "Levantar de nuevo el almacén — el almacén de suministros de la ribera seca"
      },
      "subject": {
        "en": "the dry-bank supply store",
        "es-ES": "el almacén de suministros de la ribera seca"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of Fields of the Sawad supports this bounded fictional local task. It concerns the dry-bank supply store; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Los campos del Sawad permite esta tarea local ficticia y limitada. Se ocupa de el almacén de suministros de la ribera seca; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Pay 50 wood and restore the damaged store of the dry-bank supply store to full health. Benefit: 200 food, 100 wood, once.",
        "es-ES": "Paga 50 de madera y repara por completo el almacén dañado de el almacén de suministros de la ribera seca. Ventaja: 200 de alimento, 100 de madera, una vez."
      },
      "mandatory": false,
      "activation": "available from scenario start; known requirement and benefit shown in optional goals",
      "dependencies": [],
      "predicate": {
        "operator": "all",
        "requirements": [
          {
            "kind": "entity-health",
            "entity": "04-fields-of-the-sawad.side-3.entity-1",
            "health": "full",
            "paymentReceipt": "04-fields-of-the-sawad.side-3.payment",
            "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
          },
          {
            "kind": "atomic-payment",
            "resources": {
              "wood": 50
            },
            "receipt": "04-fields-of-the-sawad.side-3.payment",
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
            "id": "04-fields-of-the-sawad.side-3.entity-1",
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
            "id": "04-fields-of-the-sawad.side-3.zone-1",
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
          "onceFlag": "04-fields-of-the-sawad.side-3.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "04-fields-of-the-sawad.side-3.completed",
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
        "en": "A Place at the Hearth — the canal-side households",
        "es-ES": "Un lugar junto al hogar — los hogares junto al canal"
      },
      "subject": {
        "en": "the canal-side households",
        "es-ES": "los hogares junto al canal"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of Fields of the Sawad supports this bounded fictional local task. It concerns the canal-side households; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Los campos del Sawad permite esta tarea local ficticia y limitada. Se ocupa de los hogares junto al canal; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Bring each of the two aid crates to its assigned household at the canal-side households. Benefit: 100 food, 50 wood, once.",
        "es-ES": "Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares junto al canal. Ventaja: 100 de alimento, 50 de madera, una vez."
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
              "04-fields-of-the-sawad.side-4.entity-1",
              "04-fields-of-the-sawad.side-4.entity-2"
            ],
            "destinations": {
              "04-fields-of-the-sawad.side-4.entity-1": "04-fields-of-the-sawad.side-4.zone-1",
              "04-fields-of-the-sawad.side-4.entity-2": "04-fields-of-the-sawad.side-4.zone-2"
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
            "id": "04-fields-of-the-sawad.side-4.entity-1",
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
            "id": "04-fields-of-the-sawad.side-4.entity-2",
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
            "id": "04-fields-of-the-sawad.side-4.zone-1",
            "hub": "hub-2",
            "offsetTiles": [
              -8,
              0
            ],
            "radiusTiles": 3
          },
          {
            "id": "04-fields-of-the-sawad.side-4.zone-2",
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
          "onceFlag": "04-fields-of-the-sawad.side-4.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "04-fields-of-the-sawad.side-4.completed",
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
        "en": "One Honest Consignment — the irrigation-road post",
        "es-ES": "Una remesa honrada — el puesto de la calzada de riego"
      },
      "subject": {
        "en": "the irrigation-road post",
        "es-ES": "el puesto de la calzada de riego"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of Fields of the Sawad supports this bounded fictional local task. It concerns the irrigation-road post; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Los campos del Sawad permite esta tarea local ficticia y limitada. Se ocupa de el puesto de la calzada de riego; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Escort the trader of the irrigation-road post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once.",
        "es-ES": "Escolta al comerciante de el puesto de la calzada de riego hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez."
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
              "04-fields-of-the-sawad.side-5.entity-1"
            ],
            "destinations": {
              "04-fields-of-the-sawad.side-5.entity-1": "04-fields-of-the-sawad.side-5.zone-1"
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
            "receipt": "04-fields-of-the-sawad.side-5.payment",
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
            "id": "04-fields-of-the-sawad.side-5.entity-1",
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
            "id": "04-fields-of-the-sawad.side-5.zone-1",
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
          "onceFlag": "04-fields-of-the-sawad.side-5.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false
        }
      ],
      "completionFlag": "04-fields-of-the-sawad.side-5.completed",
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
      "kind": "copy",
      "title": {
        "en": "What the Fire Must Not Take — the local supply accounts",
        "es-ES": "Lo que el fuego no debe llevarse — las cuentas locales de suministros"
      },
      "subject": {
        "en": "the local supply accounts",
        "es-ES": "las cuentas locales de suministros"
      },
      "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
      "rationale": {
        "en": "The documented setting of Fields of the Sawad supports this bounded fictional local task. It concerns the local supply accounts; it grants the stated tactical or contextual benefit without reversing the historical outcome. It introduces no named historical casualty or private dialogue.",
        "es-ES": "El contexto documentado de Los campos del Sawad permite esta tarea local ficticia y limitada. Se ocupa de las cuentas locales de suministros; ofrece la ventaja táctica o contextual indicada sin alterar el desenlace histórico. No introduce bajas históricas concretas ni diálogos privados."
      },
      "text": {
        "en": "Recover both separate copies from the local supply accounts and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint.",
        "es-ES": "Recupera las dos copias distintas de las cuentas locales de suministros y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal."
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
              "04-fields-of-the-sawad.side-6.entity-1",
              "04-fields-of-the-sawad.side-6.entity-2"
            ],
            "destinations": {
              "04-fields-of-the-sawad.side-6.entity-1": "04-fields-of-the-sawad.side-6.zone-1",
              "04-fields-of-the-sawad.side-6.entity-2": "04-fields-of-the-sawad.side-6.zone-1"
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
            "id": "04-fields-of-the-sawad.side-6.entity-1",
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
            "id": "04-fields-of-the-sawad.side-6.entity-2",
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
            "id": "04-fields-of-the-sawad.side-6.zone-1",
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
          "onceFlag": "04-fields-of-the-sawad.side-6.rewarded",
          "funding": "reserved-optional-stock",
          "changesHistoricalOutcome": false,
          "sourceIds": [
            "qadisiyya"
          ],
          "historicalNote": {
            "en": "The battle conventionally dated to 636 or 637 at Qadisiyya contributed to the loss of Sasanian control in Iraq. Its date and battlefield details are debated.",
            "es-ES": "Qadisiyya enfrenta fuerzas árabes y sasánidas; fecha y sitio precisos son discutidos. Se conserva resultado general sin inventar orden de batalla seguro."
          },
          "hint": {
            "en": "Secure the dry approach and canal crossing.",
            "es-ES": "Asegura el acceso seco y el paso del canal."
          }
        }
      ],
      "completionFlag": "04-fields-of-the-sawad.side-6.completed",
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
        "side-1",
        "side-2",
        "side-6"
      ],
      "mainObjectivesUnchanged": true,
      "historicalOutcomeUnchanged": true,
      "tradeoff": "optional travel/action consumes time and discretionary resources; reward and route information are bounded; no side route is a mandatory solution"
    },
    {
      "id": "civilian-and-memory",
      "optionalObjectives": [
        "side-4",
        "side-6",
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
| easy | 1125/875/500/250 | 2355/1125/1420/550 | 28 | 31 + 31 + 31 + 33 = 126 | 120 / 474 |
| standard | 900/700/400/200 | 2340/1200/1360/600 | 24 | 42 + 42 + 42 + 42 = 168 | 90 / 370 |
| hard | 765/595/340/170 | 2235/1205/1260/630 | 20 | 50 + 50 + 50 + 52 = 202 | 75 / 296 |

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
        "food": 2355,
        "wood": 1125,
        "gold": 1420,
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
      "maxVillagers": 24,
      "startingEscortCount": 28,
      "playerPopulationCap": 140,
      "enemyTotalCap": 126,
      "initialEnemy": 31,
      "waves": [
        {
          "id": "wave-1",
          "count": 31,
          "composition": {
            "militia": 12,
            "spearman": 7,
            "archer": 7,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 474,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 31,
          "composition": {
            "militia": 12,
            "spearman": 7,
            "archer": 7,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 948,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 33,
          "composition": {
            "militia": 12,
            "spearman": 8,
            "archer": 8,
            "scoutCavalry": 5
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1422,
          "warningSeconds": 120,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 12,
        "spearman": 7,
        "archer": 7,
        "scoutCavalry": 5
      },
      "enemyNominalResourceCost": {
        "food": 5495,
        "wood": 1450,
        "gold": 2265,
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
        60
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
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts.",
      "accessibleWithoutOptionalRewards": {
        "food": 3030,
        "wood": 1800,
        "gold": 1920,
        "stone": 800
      }
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
        "food": 2340,
        "wood": 1200,
        "gold": 1360,
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
      "maxVillagers": 24,
      "startingEscortCount": 24,
      "playerPopulationCap": 140,
      "enemyTotalCap": 168,
      "initialEnemy": 42,
      "waves": [
        {
          "id": "wave-1",
          "count": 42,
          "composition": {
            "militia": 15,
            "spearman": 10,
            "archer": 10,
            "scoutCavalry": 7
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 370,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 42,
          "composition": {
            "militia": 15,
            "spearman": 10,
            "archer": 10,
            "scoutCavalry": 7
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 740,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 42,
          "composition": {
            "militia": 15,
            "spearman": 10,
            "archer": 10,
            "scoutCavalry": 7
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 1110,
          "warningSeconds": 90,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 15,
        "spearman": 10,
        "archer": 10,
        "scoutCavalry": 7
      },
      "enemyNominalResourceCost": {
        "food": 7240,
        "wood": 2000,
        "gold": 3000,
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
        60
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
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts.",
      "accessibleWithoutOptionalRewards": {
        "food": 2790,
        "wood": 1700,
        "gold": 1760,
        "stone": 800
      }
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
        "food": 2235,
        "wood": 1205,
        "gold": 1260,
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
      "maxVillagers": 24,
      "startingEscortCount": 20,
      "playerPopulationCap": 140,
      "enemyTotalCap": 202,
      "initialEnemy": 50,
      "waves": [
        {
          "id": "wave-1",
          "count": 50,
          "composition": {
            "militia": 18,
            "spearman": 12,
            "archer": 12,
            "scoutCavalry": 8
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 296,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-2",
          "count": 50,
          "composition": {
            "militia": 18,
            "spearman": 12,
            "archer": 12,
            "scoutCavalry": 8
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 592,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        },
        {
          "id": "wave-3",
          "count": 52,
          "composition": {
            "militia": 18,
            "spearman": 13,
            "archer": 13,
            "scoutCavalry": 8
          },
          "release": "latched phase-2 entry + phase clock",
          "offsetSeconds": 888,
          "warningSeconds": 75,
          "repeat": false,
          "source": "finite preplaced reserve; release movement once, never create unaccounted replacements"
        }
      ],
      "initialComposition": {
        "militia": 18,
        "spearman": 12,
        "archer": 12,
        "scoutCavalry": 8
      },
      "enemyNominalResourceCost": {
        "food": 8595,
        "wood": 2450,
        "gold": 3645,
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
        60
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
      "finitePlayerRosterNote": "Starting military and four recovery guards are preplaced; replacementBudget audits further training. No free recurring respawn.",
      "wavePolicy": "If not an explicit siege objective, unreleased waves remain reserved at terminal victory; every released wave still counts against finite cap. Three waves mandatory only for finite-siege-efforts.",
      "accessibleWithoutOptionalRewards": {
        "food": 2550,
        "wood": 1600,
        "gold": 1600,
        "stone": 800
      }
    }
  },
  "analysis": {
    "classification": "feasibility envelope, not a combat simulation or proof of balance",
    "startingWorkers": 12,
    "plannedPeakWorkers": 24,
    "effectiveGatherRatePerWorkerResourcePerSecondAssumption": 0.24,
    "walkingAndIdleIncluded": "Assumed rate discounts native gathering for travel/idle; measure actual efficiency in game.",
    "worstDeliveryFood": 0,
    "sensitivity": "At 50% of assumed efficiency recompute delivery window; do not spawn hidden resources. Split workers 50%food/25%wood/20%gold/5%stone, change allocation when a specified delivery requires stone.",
    "travelTime": "Phase waves use the separate local phase-two supply circuit, not the whole-map journey. Two round trips +90s loading/reaction fit the floor. Validate actual nav-path/speed and recompute before game approval.",
    "minimumWaveGapSecondsFromProposedGeometry": 296,
    "wholeJourneyDistanceTiles": 164.34,
    "wholeJourneyOneWaySecondsEstimate": 235,
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

Canal estrecho con dos pasos de 10+casillas. Elefantes solo si se justifican por fuente y catálogo; retirada por diagonal seca siempre abierta.

{
  "plan": "Canal estrecho con dos pasos de 10+casillas. Elefantes solo si se justifican por fuente y catálogo; retirada por diagonal seca siempre abierta.",
  "budget": "One reserve escort only, drawn from protected stock and accounted starting reserve; no infinite recruit loop.",
  "notDefeat": "Historical fall, sack, defeat or death of an off-map documented figure is narrative context. Player defeat is failing this mission’s rescue/supply/tactical task.",
  "deadlockDetection": "No objective progress for 6 game minutes shows the exact outstanding goal and route, with optional recovery reminder. No automatic victory.",
  "abuse": "Killing civilian neighbours gives no gold/score. Essential historical figures are off-map narrative subjects, never convertable units."
}

## Events and every player-facing screen

The common narrator speaks first in historical intro/outro; campaign-person reactions describe fictional gameplay. Each key has EN and es-ES. The same geographically appropriate map illustrates this scenario. Reference photos never serve as unlabelled ancient scenes. Each long voiced paragraph is split into consecutive ≤32-word captions, in order; native template/audio support is gated.

| Key / condition | Narrator → destination | English | Español |
|---|---|---|---|
| `scenario.first-caliphs.04-fields-of-the-sawad.title` / always | none → next | Fields of the Sawad | Los campos del Sawad |
| `scenario.first-caliphs.04-fields-of-the-sawad.fact-intro` / intro first | collection-narrator → next | The battle conventionally dated to 636 or 637 at Qadisiyya contributed to the loss of Sasanian control in Iraq. Its date and battlefield details are debated. | Qadisiyya enfrenta fuerzas árabes y sasánidas; fecha y sitio precisos son discutidos. Se conserva resultado general sin inventar orden de batalla seguro. |
| `scenario.first-caliphs.04-fields-of-the-sawad.personal-intro` / after fact-intro | salim-caravan-scribe → next | The channels were new to me. I asked the people who worked them where a cart could cross; a soldier’s sketch alone would have drowned the load. | Los canales eran nuevos para mí. Pregunté dónde podía cruzar un carro a quienes los trabajaban; un dibujo militar habría hundido la carga. |
| `scenario.first-caliphs.04-fields-of-the-sawad.objective-1` / phase-1 active | none → hub-1 | Secure the dry approach and canal crossing. | Asegura el acceso seco y el paso del canal. |
| `scenario.first-caliphs.04-fields-of-the-sawad.objective-2` / phase-2 active | none → hub-2 | Disable two military supply posts while preserving the farms. | Inutiliza dos puestos de suministro militar preservando las granjas. |
| `scenario.first-caliphs.04-fields-of-the-sawad.objective-3` / phase-3 active | none → hub-3 | Open the northern route and protect the retreating civilian carriers. | Abre la ruta norte y protege a los porteadores civiles que se retiran. |
| `scenario.first-caliphs.04-fields-of-the-sawad.instructions` / instructions panel | none → next | Complete the listed tasks in order. Deliveries count once at their marked receiving points. Scout both routes before moving the carriers. | Completa las tareas indicadas en orden. Las entregas cuentan una vez en los puntos de recepción señalados. Explora ambas rutas antes de mover a los porteadores. |
| `scenario.first-caliphs.04-fields-of-the-sawad.scouts` / scouts panel | none → next | Regional setting: Qadisiyya / Sawad approaches. Follow the marked control points and check the alternate corridor. This is a compressed reconstruction, not a surveyed battlefield. | Entorno regional: Qadisiyya / Sawad approaches. Sigue los puntos señalados y comprueba el corredor alternativo. Es una reconstrucción comprimida, no un campo de batalla topografiado. |
| `scenario.first-caliphs.04-fields-of-the-sawad.history` / history panel | none → next | The battle conventionally dated to 636 or 637 at Qadisiyya contributed to the loss of Sasanian control in Iraq. Its date and battlefield details are debated. The convoy, personal dialogue and tactical layout are fictional; consult the campaign wiki for source qualifications. | Qadisiyya enfrenta fuerzas árabes y sasánidas; fecha y sitio precisos son discutidos. Se conserva resultado general sin inventar orden de batalla seguro. El convoy, los diálogos personales y la disposición táctica son ficción; consulta las cautelas de las fuentes en la wiki. |
| `scenario.first-caliphs.04-fields-of-the-sawad.hints` / easy hint + optional hints panel | none → next | If a corridor is blocked, scout the relief path. Keep the protected recovery stock; a copied record or replacement courier can be used only as specified. | Si se bloquea un corredor, explora el camino de auxilio. Conserva la reserva de recuperación: la copia de un registro o el correo de reemplazo solo se usan como se indica. |
| `scenario.first-caliphs.04-fields-of-the-sawad.event-phase-1-complete` / o1 first becomes true | salim-caravan-scribe → next | The first store is accounted for. Leave enough water for the return. | La primera reserva está registrada. Deja agua suficiente para la vuelta. |
| `scenario.first-caliphs.04-fields-of-the-sawad.event-phase-2-complete` / o2 first becomes true | salim-caravan-scribe → next | A road on my ledger is a journey for someone else. Keep the escort close. | Un camino en mi registro es el viaje de otra persona. Mantén cerca la escolta. |
| `scenario.first-caliphs.04-fields-of-the-sawad.event-phase-3-complete` / o3 first becomes true | salim-caravan-scribe → next | I have counted the arriving loads. I will not pretend that a ledger counts every loss. | He contado las cargas que llegan. No fingiré que un registro cuenta todas las pérdidas. |
| `scenario.first-caliphs.04-fields-of-the-sawad.event-reinforcement-warning` / phase-2 clock reaches release minus warning lead; once per wave | salim-caravan-scribe → next | A finite enemy reserve is approaching along the marked road. Withdraw the carriers or prepare the escort. | Se acerca una reserva enemiga finita por el camino señalado. Retira a los porteadores o prepara la escolta. |
| `scenario.first-caliphs.04-fields-of-the-sawad.victory-fact` / victory latch first | collection-narrator → next | The battle conventionally dated to 636 or 637 at Qadisiyya contributed to the loss of Sasanian control in Iraq. Its date and battlefield details are debated. Your mission task is complete; this outcome does not change the documented events. | Cambios políticos tras victoria; no presentar conversiones iraníes como instantáneas ni batalla étnica eterna. Has completado la tarea de la misión; el resultado no altera los hechos documentados. |
| `scenario.first-caliphs.04-fields-of-the-sawad.victory-personal` / after victory-fact | salim-caravan-scribe → 05-a-camp-beside-the-nile | I have counted the arriving loads. I will not pretend that a ledger counts every loss. | He contado las cargas que llegan. No fingiré que un registro cuenta todas las pérdidas. |
| `scenario.first-caliphs.04-fields-of-the-sawad.loss` / declared irreversible loss | collection-narrator → load/restart | The mission’s required escort or delivery can no longer be completed. The historical account remains unchanged. Reload a save or restart to try the other route. | Ya no se puede completar la escolta o entrega exigida. El relato histórico permanece igual. Carga una partida o reinicia para probar la otra ruta. |
| `scenario.first-caliphs.04-fields-of-the-sawad.recovery` / 6 minutes without objective progress | salim-caravan-scribe → current objective | Check the remaining objective and the relief corridor. Recovery is finite; use the reserve escort or archive copy only once. | Comprueba el objetivo pendiente y el corredor de auxilio. La recuperación es finita: usa la escolta de reserva o copia del archivo una sola vez. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-1-brief` / optional objectives tab, always available | salim-caravan-scribe → return-to-game | Escort the local guide of the canal-side dry road to the marked road junction. Benefit: mark the surveyed alternative corridor; terrain and enemy strength remain unchanged. | Escolta al guía local de el camino seco junto al canal hasta el cruce señalado. Ventaja: señala el corredor alternativo trazado; no cambia el terreno ni la fuerza enemiga. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-1-completed` / 04-fields-of-the-sawad.side-1.completed latched; once | salim-caravan-scribe → return-to-game | Optional task completed: The Path Between — the canal-side dry road. A caravan ledger starts with goods; the road teaches you to count people. | Tarea opcional completada: El camino entre ambos — el camino seco junto al canal. Un libro de caravanas empieza por las mercancías; el camino enseña a contar personas. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-1-unavailable` / unique optional entity irrecoverably lost; once | salim-caravan-scribe → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-2-brief` / optional objectives tab, always available | salim-caravan-scribe → return-to-game | Scout both marked viewpoints of the canal crossing approaches. Benefit: reveal the second reserve approach. | Explora los dos miradores señalados de las aproximaciones al paso del canal. Ventaja: revela la aproximación de la segunda reserva. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-2-completed` / 04-fields-of-the-sawad.side-2.completed latched; once | salim-caravan-scribe → return-to-game | Optional task completed: The Road Seen First — the canal crossing approaches. A caravan ledger starts with goods; the road teaches you to count people. | Tarea opcional completada: El camino visto primero — las aproximaciones al paso del canal. Un libro de caravanas empieza por las mercancías; el camino enseña a contar personas. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-2-unavailable` / unique optional entity irrecoverably lost; once | salim-caravan-scribe → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-3-brief` / optional objectives tab, always available | salim-caravan-scribe → return-to-game | Pay 50 wood and restore the damaged store of the dry-bank supply store to full health. Benefit: 200 food, 100 wood, once. | Paga 50 de madera y repara por completo el almacén dañado de el almacén de suministros de la ribera seca. Ventaja: 200 de alimento, 100 de madera, una vez. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-3-completed` / 04-fields-of-the-sawad.side-3.completed latched; once | salim-caravan-scribe → return-to-game | Optional task completed: Raise the Store Again — the dry-bank supply store. A caravan ledger starts with goods; the road teaches you to count people. | Tarea opcional completada: Levantar de nuevo el almacén — el almacén de suministros de la ribera seca. Un libro de caravanas empieza por las mercancías; el camino enseña a contar personas. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-3-unavailable` / unique optional entity irrecoverably lost; once | salim-caravan-scribe → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-4-brief` / optional objectives tab, always available | salim-caravan-scribe → return-to-game | Bring each of the two aid crates to its assigned household at the canal-side households. Benefit: 100 food, 50 wood, once. | Lleva cada una de las dos cajas de ayuda a su hogar asignado en los hogares junto al canal. Ventaja: 100 de alimento, 50 de madera, una vez. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-4-completed` / 04-fields-of-the-sawad.side-4.completed latched; once | salim-caravan-scribe → return-to-game | Optional task completed: A Place at the Hearth — the canal-side households. A caravan ledger starts with goods; the road teaches you to count people. | Tarea opcional completada: Un lugar junto al hogar — los hogares junto al canal. Un libro de caravanas empieza por las mercancías; el camino enseña a contar personas. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-4-unavailable` / unique optional entity irrecoverably lost; once | salim-caravan-scribe → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-5-brief` / optional objectives tab, always available | salim-caravan-scribe → return-to-game | Escort the trader of the irrigation-road post to the receiving post, then pay 50 gold for one consignment. Benefit: 150 food, 50 wood, once. | Escolta al comerciante de el puesto de la calzada de riego hasta el puesto receptor y paga 50 de oro por una sola remesa. Ventaja: 150 de alimento, 50 de madera, una vez. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-5-completed` / 04-fields-of-the-sawad.side-5.completed latched; once | salim-caravan-scribe → return-to-game | Optional task completed: One Honest Consignment — the irrigation-road post. A caravan ledger starts with goods; the road teaches you to count people. | Tarea opcional completada: Una remesa honrada — el puesto de la calzada de riego. Un libro de caravanas empieza por las mercancías; el camino enseña a contar personas. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-5-unavailable` / unique optional entity irrecoverably lost; once | salim-caravan-scribe → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-6-brief` / optional objectives tab, always available | salim-caravan-scribe → return-to-game | Recover both separate copies from the local supply accounts and deliver them to the copyist. Benefit: unlock a historical note and an explicit main-goal hint. | Recupera las dos copias distintas de las cuentas locales de suministros y entrégalas al copista. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-6-completed` / 04-fields-of-the-sawad.side-6.completed latched; once | salim-caravan-scribe → return-to-game | Optional task completed: What the Fire Must Not Take — the local supply accounts. A caravan ledger starts with goods; the road teaches you to count people. | Tarea opcional completada: Lo que el fuego no debe llevarse — las cuentas locales de suministros. Un libro de caravanas empieza por las mercancías; el camino enseña a contar personas. |
| `scenario.first-caliphs.04-fields-of-the-sawad.side-6-unavailable` / unique optional entity irrecoverably lost; once | salim-caravan-scribe → return-to-game | This optional task is no longer available. The main objectives remain active. | Esta tarea opcional ya no está disponible. Los objetivos principales siguen activos. |

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
