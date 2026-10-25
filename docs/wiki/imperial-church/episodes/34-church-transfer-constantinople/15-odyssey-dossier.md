# 33. The Doors of New Rome

authored-dossier; source approval, map geometry, native capabilities and game balance pending

Design-only draft. Historical, geographic, native and game review remain pending; this typed projection is not an implemented map or played route.

CDF-C01 · `34-church-transfer-constantinople` · November380 CE; arrival and church transfer are distinct source dates · 400×400

## Historical frame and source record

EN: In late 380, Theodosius entered Constantinople and ordered changes in church possession. Socrates places the arrival and transfer on separate November days; Marcellinus records the restoration he favored in December. These later accounts do not establish what every inhabitant believed. The following local service story is invented.

ES: A finales de 380, Teodosio entró en Constantinopla y ordenó cambios en la posesión de iglesias. Sócrates sitúa la llegada y el traspaso en días distintos de noviembre; Marcelino fecha en diciembre la restauración que favorecía. Estos relatos posteriores no establecen qué creía cada habitante. La siguiente historia asistencial local es inventada.

EN: Both invented local services have been completed with their original recipients. This does not explain, approve or reverse the imperial change in church possession. The next episode concerns the council of 381 and the disputes that continued.

ES: Ambos servicios locales inventados se han completado con sus destinatarios originales. Esto no explica, aprueba ni revierte el cambio imperial de posesión de iglesias. El siguiente episodio trata del concilio de 381 y de las disputas que continuaron.

EN: The local service workers, recipients, outputs, households, courts and optional activities are fictional. Their voluntary care does not cause, reverse, justify or prove the imperial change in church possession, a legal title or anyone's convictions. Marcus is a fictional clerk; no quoted speech or authentic voice is supplied.

ES: Los trabajadores, destinatarios, resultados, hogares, patios y actividades secundarias asistenciales son ficticios. Su ayuda voluntaria no causa, revierte, justifica ni acredita el cambio imperial en la posesión de iglesias, un título legal o las convicciones de nadie. Marco es un escribiente ficticio; no se aportan discursos citados ni una voz auténtica.

```json
{
  "sourcePassages": [
    {
      "classification": "architect interpretation; independent historical approval pending",
      "selectedClaim": {
        "en": "Socrates separately narrates Theodosius’ arrival and church-possession changes at Constantinople. His theological framing is attributed; it is not automatic implementation of the February law.",
        "es-ES": "Sócrates narra por separado la llegada de Teodosio y los cambios de posesión de iglesias en Constantinopla. Su interpretación teológica queda atribuida; no es cumplimiento automático de la ley de febrero."
      },
      "architectCorrection": {
        "date": "2026-10-17",
        "author": "gpt-6",
        "reason": "Socrates V.6 reports arrival24November and V.7 church possession26November380 as separate events; Marcellinus380 instead places church restoration inDecember. Preserve the discrepancy, not a harmonized exact calendar. Sozomen’s later enlarged Anastasia building and attributed miracles do not certify the380venue or terrain. Gregory’s later resignation and381council must remain distinct fromNovember380. No exact church footprint, universal compliance or playable forced conversion follows.",
        "approval": "independent review pending"
      }
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/26015.htm",
      "passage": "Socrates HE V.6–7",
      "status": "consulted as bounded source collection; full dossier pending",
      "consultationDate": "2026-10-15",
      "coverageActuallyRead": "Root selected reading and the separately attributed Luna passage audit are documented in imperial363-380-primary-audit.json and imperial-coverage-amendment.md; no manuscript or complete critical apparatus inspected.",
      "limitations": "Keep November24arrival and November26transfer as separately reported dates; no universal compliance, modern denominational schism, certified church parcel or playable forced conversion.",
      "approval": "collection and architect selection only; no historical/game approval"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/26015.htm",
      "passage": "Socrates HE V.6–8, especiallyV.6arrival andV.7transfer",
      "coverageActuallyRead": "Root read selected complete arrival, church-transfer and council chapters in NPNF English translation; no Greek apparatus or Gregory’s poem.",
      "limitations": "Retrospective Nicene framing. The narrator’s peace/orthodoxy judgments and reported speeches are not an objective moral verdict or independently authenticated verbatim dialogue. V.7also places a resignation of Gregory in its narrative sequence; do not automatically date every episcopal action toNovember380without comparing chronology and381council evidence.",
      "consultationDate": "2026-10-17",
      "approval": "bounded architect collection; independent historical review pending"
    },
    {
      "consultedUrl": "https://www.newadvent.org/fathers/26027.htm",
      "passage": "Sozomen HE VII.4–5, withVII.7–8as council context",
      "coverageActuallyRead": "Root read selected law/arrival/transfer paragraphs and selected later council context, distinguishing earlier private oratory from later monumental building descriptions.",
      "limitations": "No independent eyewitness proof or complete urban transfer register. Miracles and the etymology of Anastasia are attributed beliefs/traditions, not geographic proof or mandatory gameplay powers. Later magnificent church fabric cannot be pasted onto380. Law, arrival and physical possession are not one single instant.",
      "consultationDate": "2026-10-17",
      "approval": "bounded architect collection; independent historical review pending"
    },
    {
      "consultedUrl": "https://www.thelatinlibrary.com/marcellinus1.html",
      "passage": "Marcellinus Comes Chronicon380entry, labelled MommsenChronicaMinoraII1894",
      "coverageActuallyRead": "Root read the complete selected Latin380entry in the web transcription; no facsimile manuscript or critical apparatus freshly inspected.",
      "limitations": "That month differs from Socrates’Novemberreport. Do not relabel it November, claim all chronicles agree, or assign the exact same dated transfer from modern harmonization alone. Its favorable confessional language remains attributed.",
      "consultationDate": "2026-10-17",
      "approval": "bounded architect collection; independent historical review pending"
    }
  ],
  "knowledgeBasis": {
    "speaker": "imperial-clerk",
    "proposedLifespan": "c.334–403",
    "mode": "fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports",
    "noOmniscience": true
  }
}
```

## Shared objective and typed profile

### attend-meal-court / phase-1

EN: Bring the meal recipient to the receiving court.

ES: Lleva al destinatario de la comida al patio receptor.

```json
{
  "operator": "all",
  "operation": "attend-meal-court",
  "requiredCount": 1,
  "defeatBelowRemaining": null,
  "resourceAmounts": {},
  "phaseGated": true,
  "neverUseTimerInstead": true,
  "requirements": [
    {
      "id": "meal-recipient-arrival",
      "kind": "entity-state",
      "state": "arrived",
      "entities": [
        "imperial-church.34-church-transfer-constantinople.meal-recipient"
      ],
      "requiredCount": 1,
      "oncePerEntity": true,
      "destinations": {
        "imperial-church.34-church-transfer-constantinople.meal-recipient": "imperial-church.34-church-transfer-constantinople.meal-reception.zone"
      }
    },
    {
      "id": "meal-recipient-current",
      "kind": "current-entity-presence",
      "entities": [
        "imperial-church.34-church-transfer-constantinople.meal-recipient"
      ],
      "destinations": {
        "imperial-church.34-church-transfer-constantinople.meal-recipient": "imperial-church.34-church-transfer-constantinople.meal-reception.zone"
      },
      "requiredCount": 1
    }
  ],
  "requiredLedgers": [
    "meal-recipient-arrival",
    "meal-recipient-current"
  ],
  "allRequired": true
}
```

## Alternative services

A selection is one authored recipe per service. Costs are alternatives and are never lowered to simultaneous fixed-payment predicates.

### meal-service

Goal screen: `meal-service-goal` · completion screen: `meal-received`

#### meal-direct — Prepared Provisions

EN: Prepared Provisions

ES: Provisiones preparadas

Work point `meal-direct-source` → reception point `meal-reception`; worker `imperial-church.34-church-transfer-constantinople.meal-worker`; output `imperial-church.34-church-transfer-constantinople.meal-direct-output`; recipients: `imperial-church.34-church-transfer-constantinople.meal-recipient`.

Cost: `{"food": 240, "gold": 0, "stone": 0, "wood": 40}`.

#### meal-shared-hearth — At the Shared Hearth

EN: At the Shared Hearth

ES: Junto al fogón compartido

Work point `hearth-worksite` → reception point `meal-reception`; worker `imperial-church.34-church-transfer-constantinople.meal-worker`; output `imperial-church.34-church-transfer-constantinople.meal-shared-hearth-output`; recipients: `imperial-church.34-church-transfer-constantinople.meal-recipient`.

Cost: `{"food": 160, "gold": 0, "stone": 0, "wood": 140}`.

#### meal-purchased — A Merchant's Consignment

EN: A Merchant's Consignment

ES: La remesa del mercader

Work point `merchant-worksite` → reception point `meal-reception`; worker `imperial-church.34-church-transfer-constantinople.meal-worker`; output `imperial-church.34-church-transfer-constantinople.meal-purchased-output`; recipients: `imperial-church.34-church-transfer-constantinople.meal-recipient`.

Cost: `{"food": 100, "gold": 100, "stone": 0, "wood": 40}`.

### shelter-service

Goal screen: `shelter-service-goal` · completion screen: `shelter-received`

#### shelter-materials — Build from Delivered Materials

EN: Build from Delivered Materials

ES: Preparar con materiales entregados

Work point `materials-source` → reception point `materials-court`; worker `imperial-church.34-church-transfer-constantinople.shelter-worker`; output `imperial-church.34-church-transfer-constantinople.shelter-materials-output`; recipients: `imperial-church.34-church-transfer-constantinople.household-a`, `imperial-church.34-church-transfer-constantinople.household-b`.

Cost: `{"food": 80, "gold": 0, "stone": 0, "wood": 200}`.

#### shelter-local-kit — Prepare a Local Kit

EN: Prepare a Local Kit

ES: Preparar un equipo local

Work point `kit-worksite` → reception point `kit-court`; worker `imperial-church.34-church-transfer-constantinople.shelter-worker`; output `imperial-church.34-church-transfer-constantinople.shelter-local-kit-output`; recipients: `imperial-church.34-church-transfer-constantinople.household-a`, `imperial-church.34-church-transfer-constantinople.household-b`.

Cost: `{"food": 100, "gold": 20, "stone": 0, "wood": 120}`.

#### shelter-rented — A Willing Host

EN: A Willing Host

ES: Un anfitrión dispuesto

Work point `host-worksite` → reception point `host-court`; worker `imperial-church.34-church-transfer-constantinople.shelter-worker`; output `imperial-church.34-church-transfer-constantinople.shelter-rented-output`; recipients: `imperial-church.34-church-transfer-constantinople.household-a`, `imperial-church.34-church-transfer-constantinople.household-b`.

Cost: `{"food": 60, "gold": 110, "stone": 0, "wood": 60}`.

## Difficulty accounting

Finite selection arithmetic only; it is not resource gathering, a schedule or a playthrough.

### easy

Accounts:

```json
{
  "spendable": {
    "food": 420,
    "wood": 380,
    "gold": 260,
    "stone": 0
  },
  "protectedRecovery": {
    "food": 0,
    "wood": 0,
    "gold": 0,
    "stone": 0
  },
  "optionalReserve": {
    "food": 400,
    "wood": 150,
    "gold": 25,
    "stone": 0
  }
}
```

Before main funding: 128 of 128 optional subsets are reachable from initial spendable stock; all optional tasks are reachable in that prefix: True. This prefix does not include a service selection.

After main funding: 9 of 9 recipe selections are affordable from initial spendable stock; 9 affordable selections permit all optional tasks in an affordable prefix. Unaffordable selections have no after-funding witness. These are finite accounting cases and assume spatial predicates and actor availability succeed.

| Recipe selection | Total cost | Main affordable | Spendable stock after main selection | Reachable optional subsets after funding | All optional tasks affordable after funding |
|---|---|---:|---|---:|---|
| `meal-direct`, `shelter-materials` | `{"food": 320, "gold": 0, "stone": 0, "wood": 240}` | True | `{"food": 100, "gold": 260, "stone": 0, "wood": 140}` | 128 | True |
| `meal-direct`, `shelter-local-kit` | `{"food": 340, "gold": 20, "stone": 0, "wood": 160}` | True | `{"food": 80, "gold": 240, "stone": 0, "wood": 220}` | 128 | True |
| `meal-direct`, `shelter-rented` | `{"food": 300, "gold": 110, "stone": 0, "wood": 100}` | True | `{"food": 120, "gold": 150, "stone": 0, "wood": 280}` | 128 | True |
| `meal-shared-hearth`, `shelter-materials` | `{"food": 240, "gold": 0, "stone": 0, "wood": 340}` | True | `{"food": 180, "gold": 260, "stone": 0, "wood": 40}` | 96 | True |
| `meal-shared-hearth`, `shelter-local-kit` | `{"food": 260, "gold": 20, "stone": 0, "wood": 260}` | True | `{"food": 160, "gold": 240, "stone": 0, "wood": 120}` | 128 | True |
| `meal-shared-hearth`, `shelter-rented` | `{"food": 220, "gold": 110, "stone": 0, "wood": 200}` | True | `{"food": 200, "gold": 150, "stone": 0, "wood": 180}` | 128 | True |
| `meal-purchased`, `shelter-materials` | `{"food": 180, "gold": 100, "stone": 0, "wood": 240}` | True | `{"food": 240, "gold": 160, "stone": 0, "wood": 140}` | 128 | True |
| `meal-purchased`, `shelter-local-kit` | `{"food": 200, "gold": 120, "stone": 0, "wood": 160}` | True | `{"food": 220, "gold": 140, "stone": 0, "wood": 220}` | 128 | True |
| `meal-purchased`, `shelter-rented` | `{"food": 160, "gold": 210, "stone": 0, "wood": 100}` | True | `{"food": 260, "gold": 50, "stone": 0, "wood": 280}` | 128 | True |

### standard

Accounts:

```json
{
  "spendable": {
    "food": 340,
    "wood": 280,
    "gold": 150,
    "stone": 0
  },
  "protectedRecovery": {
    "food": 0,
    "wood": 0,
    "gold": 0,
    "stone": 0
  },
  "optionalReserve": {
    "food": 400,
    "wood": 150,
    "gold": 25,
    "stone": 0
  }
}
```

Before main funding: 128 of 128 optional subsets are reachable from initial spendable stock; all optional tasks are reachable in that prefix: True. This prefix does not include a service selection.

After main funding: 7 of 9 recipe selections are affordable from initial spendable stock; 7 affordable selections permit all optional tasks in an affordable prefix. Unaffordable selections have no after-funding witness. These are finite accounting cases and assume spatial predicates and actor availability succeed.

| Recipe selection | Total cost | Main affordable | Spendable stock after main selection | Reachable optional subsets after funding | All optional tasks affordable after funding |
|---|---|---:|---|---:|---|
| `meal-direct`, `shelter-materials` | `{"food": 320, "gold": 0, "stone": 0, "wood": 240}` | True | `{"food": 20, "gold": 150, "stone": 0, "wood": 40}` | 96 | True |
| `meal-direct`, `shelter-local-kit` | `{"food": 340, "gold": 20, "stone": 0, "wood": 160}` | True | `{"food": 0, "gold": 130, "stone": 0, "wood": 120}` | 128 | True |
| `meal-direct`, `shelter-rented` | `{"food": 300, "gold": 110, "stone": 0, "wood": 100}` | True | `{"food": 40, "gold": 40, "stone": 0, "wood": 180}` | 128 | True |
| `meal-shared-hearth`, `shelter-materials` | `{"food": 240, "gold": 0, "stone": 0, "wood": 340}` | False | `—` | — | — |
| `meal-shared-hearth`, `shelter-local-kit` | `{"food": 260, "gold": 20, "stone": 0, "wood": 260}` | True | `{"food": 80, "gold": 130, "stone": 0, "wood": 20}` | 96 | True |
| `meal-shared-hearth`, `shelter-rented` | `{"food": 220, "gold": 110, "stone": 0, "wood": 200}` | True | `{"food": 120, "gold": 40, "stone": 0, "wood": 80}` | 128 | True |
| `meal-purchased`, `shelter-materials` | `{"food": 180, "gold": 100, "stone": 0, "wood": 240}` | True | `{"food": 160, "gold": 50, "stone": 0, "wood": 40}` | 96 | True |
| `meal-purchased`, `shelter-local-kit` | `{"food": 200, "gold": 120, "stone": 0, "wood": 160}` | True | `{"food": 140, "gold": 30, "stone": 0, "wood": 120}` | 128 | True |
| `meal-purchased`, `shelter-rented` | `{"food": 160, "gold": 210, "stone": 0, "wood": 100}` | False | `—` | — | — |

### hard

Accounts:

```json
{
  "spendable": {
    "food": 300,
    "wood": 220,
    "gold": 120,
    "stone": 0
  },
  "protectedRecovery": {
    "food": 0,
    "wood": 0,
    "gold": 0,
    "stone": 0
  },
  "optionalReserve": {
    "food": 400,
    "wood": 150,
    "gold": 25,
    "stone": 0
  }
}
```

Before main funding: 128 of 128 optional subsets are reachable from initial spendable stock; all optional tasks are reachable in that prefix: True. This prefix does not include a service selection.

After main funding: 3 of 9 recipe selections are affordable from initial spendable stock; 3 affordable selections permit all optional tasks in an affordable prefix. Unaffordable selections have no after-funding witness. These are finite accounting cases and assume spatial predicates and actor availability succeed.

| Recipe selection | Total cost | Main affordable | Spendable stock after main selection | Reachable optional subsets after funding | All optional tasks affordable after funding |
|---|---|---:|---|---:|---|
| `meal-direct`, `shelter-materials` | `{"food": 320, "gold": 0, "stone": 0, "wood": 240}` | False | `—` | — | — |
| `meal-direct`, `shelter-local-kit` | `{"food": 340, "gold": 20, "stone": 0, "wood": 160}` | False | `—` | — | — |
| `meal-direct`, `shelter-rented` | `{"food": 300, "gold": 110, "stone": 0, "wood": 100}` | True | `{"food": 0, "gold": 10, "stone": 0, "wood": 120}` | 128 | True |
| `meal-shared-hearth`, `shelter-materials` | `{"food": 240, "gold": 0, "stone": 0, "wood": 340}` | False | `—` | — | — |
| `meal-shared-hearth`, `shelter-local-kit` | `{"food": 260, "gold": 20, "stone": 0, "wood": 260}` | False | `—` | — | — |
| `meal-shared-hearth`, `shelter-rented` | `{"food": 220, "gold": 110, "stone": 0, "wood": 200}` | True | `{"food": 80, "gold": 10, "stone": 0, "wood": 20}` | 96 | True |
| `meal-purchased`, `shelter-materials` | `{"food": 180, "gold": 100, "stone": 0, "wood": 240}` | False | `—` | — | — |
| `meal-purchased`, `shelter-local-kit` | `{"food": 200, "gold": 120, "stone": 0, "wood": 160}` | True | `{"food": 100, "gold": 0, "stone": 0, "wood": 60}` | 128 | True |
| `meal-purchased`, `shelter-rented` | `{"food": 160, "gold": 210, "stone": 0, "wood": 100}` | False | `—` | — | — |

## Optional objectives

The exact authored v3 contracts follow; their presence does not establish task reachability in the game.

```json
[
  {
    "id": "side-1",
    "kind": "aid",
    "title": {
      "en": "A Table Kept Open",
      "es-ES": "Una mesa que sigue abierta"
    },
    "subject": {
      "en": "two household collection posts",
      "es-ES": "dos puestos de recogida de hogares"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Two separately identified consignments reach separately marked collection posts assigned to fictional consenting households. Household members remain off scene; this task checks the crates at their assigned posts, not recipient presence. No creed eligibility.",
      "es-ES": "Dos remesas con identidades distintas llegan a puestos de recogida señalados por separado para hogares ficticios voluntarios. Sus miembros quedan fuera de escena; la tarea comprueba las cajas en sus puestos asignados, no la presencia de destinatarios. Sin requisitos de credo."
    },
    "text": {
      "en": "Bring each marked aid crate to its own marked household collection post in the Northern Reception Yard. Household members are off scene; the two crate arrivals complete this task. Benefit: 100 food, 50 wood, once.",
      "es-ES": "Lleva cada caja de ayuda señalada a su puesto de recogida de hogar correspondiente, también señalado, en el patio receptor del norte. Los miembros de esos hogares quedan fuera de escena; las dos llegadas de cajas completan esta tarea. Ventaja: 100 de alimento, 50 de madera, una vez."
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
            "34-church-transfer-constantinople.side-1.entity-1",
            "34-church-transfer-constantinople.side-1.entity-2"
          ],
          "destinations": {
            "34-church-transfer-constantinople.side-1.entity-1": "34-church-transfer-constantinople.side-1.zone-1",
            "34-church-transfer-constantinople.side-1.entity-2": "34-church-transfer-constantinople.side-1.zone-2"
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
          "id": "34-church-transfer-constantinople.side-1.entity-1",
          "role": "aid",
          "initialHub": "north-care-yard",
          "offsetTiles": [
            -6,
            3
          ],
          "identity": "Fictional stable optional identity: 34-church-transfer-constantinople.side-1.entity-1; preserve this exact actor identity.",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        },
        {
          "id": "34-church-transfer-constantinople.side-1.entity-2",
          "role": "aid",
          "initialHub": "north-care-yard",
          "offsetTiles": [
            -6,
            6
          ],
          "identity": "Fictional stable optional identity: 34-church-transfer-constantinople.side-1.entity-2; preserve this exact actor identity.",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "34-church-transfer-constantinople.side-1.zone-1",
          "hub": "north-reception",
          "offsetTiles": [
            -8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        },
        {
          "id": "34-church-transfer-constantinople.side-1.zone-2",
          "hub": "north-reception",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
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
        "onceFlag": "34-church-transfer-constantinople.side-1.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false
      }
    ],
    "completionFlag": "34-church-transfer-constantinople.side-1.completed",
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
      "originHub": "north-care-yard",
      "receivingHub": "north-reception",
      "corridorIds": [
        "north-care-loop",
        "north-reader-link",
        "north-reception-link"
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
      "en": "The Longer Way Home",
      "es-ES": "El camino largo a casa"
    },
    "subject": {
      "en": "two voluntary neighboring groups",
      "es-ES": "dos grupos vecinos voluntarios"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "These optional originals are distinct from the two main-service households.",
      "es-ES": "Estos originales opcionales son distintos de los dos hogares del servicio principal."
    },
    "text": {
      "en": "Bring both marked voluntary groups alive from the Northern Supply Yard to the Western Shelter Yard. Benefit: 100 food, 25 gold, once.",
      "es-ES": "Lleva con vida a los dos grupos voluntarios señalados desde el patio de suministros del norte hasta el patio de refugio occidental. Ventaja: 100 de alimento, 25 de oro, una vez."
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
            "34-church-transfer-constantinople.side-2.entity-1",
            "34-church-transfer-constantinople.side-2.entity-2"
          ],
          "destinations": {
            "34-church-transfer-constantinople.side-2.entity-1": "34-church-transfer-constantinople.side-2.zone-1",
            "34-church-transfer-constantinople.side-2.entity-2": "34-church-transfer-constantinople.side-2.zone-1"
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
          "id": "34-church-transfer-constantinople.side-2.entity-1",
          "role": "extract",
          "initialHub": "north-care-yard",
          "offsetTiles": [
            -9,
            3
          ],
          "identity": "Fictional stable optional identity: 34-church-transfer-constantinople.side-2.entity-1; preserve this exact actor identity.",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        },
        {
          "id": "34-church-transfer-constantinople.side-2.entity-2",
          "role": "extract",
          "initialHub": "north-care-yard",
          "offsetTiles": [
            -9,
            7
          ],
          "identity": "Fictional stable optional identity: 34-church-transfer-constantinople.side-2.entity-2; preserve this exact actor identity.",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "34-church-transfer-constantinople.side-2.zone-1",
          "hub": "materials-court",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
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
        "onceFlag": "34-church-transfer-constantinople.side-2.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false
      }
    ],
    "completionFlag": "34-church-transfer-constantinople.side-2.completed",
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
      "originHub": "north-care-yard",
      "receivingHub": "materials-court",
      "corridorIds": [
        "north-care-approach",
        "western-reception"
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
      "en": "Two Dates in the Margin",
      "es-ES": "Dos fechas al margen"
    },
    "subject": {
      "en": "two fictional working copies",
      "es-ES": "dos copias de trabajo ficticias"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Deliver both copies. The unlocked source comparison is retrospective collection commentary for the player, never a fifth/sixth-century text held or quoted by Marcus in380. The reader is off scene; this task checks two originals at a collection desk, not a reader actor.",
      "es-ES": "Entrega ambas copias. La comparación desbloqueada es un comentario retrospectivo de colección para el jugador; Marcus no posee ni cita en380 un texto de los siglosV/VI. El lector queda fuera de escena; la tarea comprueba dos originales en una mesa receptora, no un actor lector."
    },
    "text": {
      "en": "Recover the two marked working copies at the Reader's Shelter and place both at the marked collection desk beside the Shared Hearth. The reader is off scene; both copy arrivals complete this task. Benefit: unlock a historical note and an explicit main-goal hint.",
      "es-ES": "Recupera las dos copias de trabajo señaladas en el refugio del lector y deposita ambas en la mesa receptora señalada junto al fogón compartido. El lector queda fuera de escena; las dos llegadas de copias completan esta tarea. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal."
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
            "34-church-transfer-constantinople.side-3.entity-1",
            "34-church-transfer-constantinople.side-3.entity-2"
          ],
          "destinations": {
            "34-church-transfer-constantinople.side-3.entity-1": "34-church-transfer-constantinople.side-3.zone-1",
            "34-church-transfer-constantinople.side-3.entity-2": "34-church-transfer-constantinople.side-3.zone-1"
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
          "id": "34-church-transfer-constantinople.side-3.entity-1",
          "role": "copy",
          "initialHub": "north-reader",
          "offsetTiles": [
            -6,
            3
          ],
          "identity": "Fictional stable optional identity: 34-church-transfer-constantinople.side-3.entity-1; preserve this exact actor identity.",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        },
        {
          "id": "34-church-transfer-constantinople.side-3.entity-2",
          "role": "copy",
          "initialHub": "north-reader",
          "offsetTiles": [
            -6,
            6
          ],
          "identity": "Fictional stable optional identity: 34-church-transfer-constantinople.side-3.entity-2; preserve this exact actor identity.",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "34-church-transfer-constantinople.side-3.zone-1",
          "hub": "hearth-worksite",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "unlock-context-and-hint",
        "target": "documented context and a main-goal hint",
        "resources": {},
        "onceFlag": "34-church-transfer-constantinople.side-3.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false,
        "sourceIds": [
          "odyssey-source.imperial-church.34-church-transfer-constantinople"
        ],
        "historicalNote": {
          "en": "Late 380 church possession changed under imperial power; surviving accounts differ on the month. This is retrospective collection commentary, not a document available to the persona in 380.",
          "es-ES": "A finales de 380 cambió la posesión de iglesias por el poder imperial; los relatos conservados difieren en el mes. Este comentario retrospectivo de colección no es un documento disponible para la persona en 380."
        },
        "hint": {
          "en": "Complete both voluntary services with one funded plan and the same original living recipients.",
          "es-ES": "Completa ambos servicios voluntarios con un plan financiado y los mismos destinatarios originales vivos."
        }
      }
    ],
    "completionFlag": "34-church-transfer-constantinople.side-3.completed",
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
      "originHub": "north-reader",
      "receivingHub": "hearth-worksite",
      "corridorIds": [
        "north-reader-link",
        "north-care-loop",
        "north-care-approach",
        "western-trade",
        "west-supply",
        "ridge-junction"
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
      "en": "A Neighbor's Route",
      "es-ES": "La ruta de un vecino"
    },
    "subject": {
      "en": "one local guide",
      "es-ES": "un guía local"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Escort the same original guide and mark the already proposed western supply connection; no road opens.",
      "es-ES": "Escolta al mismo guía original y señala la conexión occidental de suministro ya propuesta; no se abre ningún camino."
    },
    "text": {
      "en": "Escort the marked local guide to the Western Turn. Benefit: Mark the existing western supply link and its actual work-site target.",
      "es-ES": "Escolta al guía local señalado hasta el desvío occidental. Ventaja: Señala la conexión occidental existente y su punto de trabajo real."
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
            "34-church-transfer-constantinople.side-4.entity-1"
          ],
          "destinations": {
            "34-church-transfer-constantinople.side-4.entity-1": "34-church-transfer-constantinople.side-4.zone-1"
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
          "id": "34-church-transfer-constantinople.side-4.entity-1",
          "role": "guide",
          "initialHub": "western-guide",
          "offsetTiles": [
            -5,
            2
          ],
          "identity": "Fictional stable optional identity: 34-church-transfer-constantinople.side-4.entity-1; preserve this exact actor identity.",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "playerControllable": true,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "34-church-transfer-constantinople.side-4.zone-1",
          "hub": "western-junction",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "mark-alternative-route",
        "target": "west-supply",
        "resources": {},
        "onceFlag": "34-church-transfer-constantinople.side-4.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false,
        "corridorId": "west-supply"
      }
    ],
    "completionFlag": "34-church-transfer-constantinople.side-4.completed",
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
      "originHub": "western-guide",
      "receivingHub": "western-junction",
      "corridorIds": [
        "guide-link",
        "west-supply"
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
    "kind": "scout",
    "title": {
      "en": "Above the Waterline",
      "es-ES": "Por encima del agua"
    },
    "subject": {
      "en": "two interior viewpoints",
      "es-ES": "dos miradores interiores"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Observe both authored sites; reveal the existing northern care circuit rather than enemies, a new path or ancient shoreline certainty.",
      "es-ES": "Observa ambos lugares diseñados; señala el circuito asistencial norte existente, sin enemigos, caminos nuevos ni certeza sobre la costa antigua."
    },
    "text": {
      "en": "Visit both marked interior viewpoints: the Upper Viewpoint and the Southern Viewpoint. Benefit: Mark the existing care loop; all costs and destinations remain available without this task.",
      "es-ES": "Visita los dos miradores interiores señalados: el mirador alto y el mirador sur. Ventaja: Señala el circuito asistencial existente; costes y destinos siguen disponibles aunque omitas esta tarea."
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
            "34-church-transfer-constantinople.side-5.zone-1",
            "34-church-transfer-constantinople.side-5.zone-2"
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
          "id": "34-church-transfer-constantinople.side-5.zone-1",
          "hub": "north-viewpoint",
          "offsetTiles": [
            -8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        },
        {
          "id": "34-church-transfer-constantinople.side-5.zone-2",
          "hub": "south-viewpoint",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "mark-alternative-route",
        "target": "north-care-loop",
        "resources": {},
        "onceFlag": "34-church-transfer-constantinople.side-5.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false,
        "corridorId": "north-care-loop"
      }
    ],
    "completionFlag": "34-church-transfer-constantinople.side-5.completed",
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
      "originHub": "starting-court",
      "receivingHub": "north-viewpoint",
      "corridorIds": [
        "ridge-hearth",
        "ridge-junction",
        "west-supply",
        "western-trade",
        "western-reception",
        "north-view",
        "southern-host",
        "southern-view"
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
    "kind": "watch",
    "title": {
      "en": "Room for the Next Household",
      "es-ES": "Sitio para el siguiente hogar"
    },
    "subject": {
      "en": "two service approaches",
      "es-ES": "dos accesos de servicio"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "Visit separate observation circles outside both real receiving circles to distinguish alternative shelter courts; a past visit cannot substitute for required current recipients.",
      "es-ES": "Visita círculos de observación separados de los receptores para distinguir patios alternativos; una visita pasada no sustituye la presencia actual de destinatarios."
    },
    "text": {
      "en": "Visit both marked observation spots beside the Western Shelter Yard and the Southern Host's Courtyard. Benefit: Mark the existing southern host approach and explain the selected-court requirement.",
      "es-ES": "Visita los dos puntos de observación señalados junto al patio de refugio occidental y al patio del anfitrión del sur. Ventaja: Señala el acceso sur existente y explica que cuenta únicamente el patio seleccionado."
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
            "34-church-transfer-constantinople.side-6.zone-1",
            "34-church-transfer-constantinople.side-6.zone-2"
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
          "id": "34-church-transfer-constantinople.side-6.zone-1",
          "hub": "materials-court",
          "offsetTiles": [
            0,
            -8
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        },
        {
          "id": "34-church-transfer-constantinople.side-6.zone-2",
          "hub": "host-court",
          "offsetTiles": [
            0,
            8
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
        }
      ]
    },
    "effects": [
      {
        "kind": "mark-alternative-route",
        "target": "southern-host",
        "resources": {},
        "onceFlag": "34-church-transfer-constantinople.side-6.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false,
        "corridorId": "southern-host"
      }
    ],
    "completionFlag": "34-church-transfer-constantinople.side-6.completed",
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
      "originHub": "starting-court",
      "receivingHub": "host-court",
      "corridorIds": [
        "ridge-hearth",
        "ridge-junction",
        "west-supply",
        "western-trade",
        "western-reception",
        "southern-host"
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
    "id": "side-7",
    "kind": "repair",
    "title": {
      "en": "Timber Put to Use",
      "es-ES": "Madera bien empleada"
    },
    "subject": {
      "en": "one fictional damaged civilian store",
      "es-ES": "un almacén civil dañado ficticio"
    },
    "classification": "fictional local activity anchored to the documented scenario; not an asserted ancient event",
    "rationale": {
      "en": "A50wood atomic restoration and actual full-health receipt precede its funded reward. Prior damage is fiction, not an ancient disaster.",
      "es-ES": "Una restauración atómica de50madera y su recibo real de salud completa preceden la recompensa financiada. El daño previo es ficción, no un desastre antiguo."
    },
    "text": {
      "en": "Restore the marked damaged store to full health through its single 50-wood repair action. Benefit: 200 food, 100 wood, once.",
      "es-ES": "Restaura por completo el almacén dañado señalado mediante su única acción de reparación de 50 de madera. Ventaja: 200 de alimento, 100 de madera, una vez."
    },
    "mandatory": false,
    "activation": "available from scenario start; known requirement and benefit shown in optional goals",
    "dependencies": [],
    "predicate": {
      "operator": "all",
      "requirements": [
        {
          "kind": "entity-health",
          "entity": "34-church-transfer-constantinople.side-7.entity-1",
          "health": "full",
          "paymentReceipt": "34-church-transfer-constantinople.side-7.payment",
          "restoration": "atomic 50-wood repair transaction restores full health; no additional engine repair charge"
        },
        {
          "kind": "atomic-payment",
          "resources": {
            "wood": 50
          },
          "receipt": "34-church-transfer-constantinople.side-7.payment",
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
          "id": "34-church-transfer-constantinople.side-7.entity-1",
          "role": "repair",
          "initialHub": "north-store",
          "offsetTiles": [
            -4,
            -4
          ],
          "identity": "Fictional stable optional identity: 34-church-transfer-constantinople.side-7.entity-1; preserve this exact actor identity.",
          "finite": true,
          "replacement": "none; no substitution of unique original identity",
          "initiallyDelivered": false,
          "originRule": "Authored initial position creates no completed visit or delivery.",
          "initialHealthFraction": 0.5,
          "damageSource": "fictional prior damage",
          "playerControllable": false,
          "historicalPerson": false
        }
      ],
      "zones": [
        {
          "id": "34-church-transfer-constantinople.side-7.zone-1",
          "hub": "north-store",
          "offsetTiles": [
            8,
            0
          ],
          "radiusTiles": 3,
          "placement": "Fictional optional activity zone at the authored hub and offset; native footprint pending.",
          "protectedCivilian": false
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
        "onceFlag": "34-church-transfer-constantinople.side-7.rewarded",
        "funding": "reserved-optional-stock",
        "changesHistoricalOutcome": false
      }
    ],
    "completionFlag": "34-church-transfer-constantinople.side-7.completed",
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
      "originHub": "north-store",
      "receivingHub": "north-store",
      "corridorIds": [
        "ridge-hearth",
        "ridge-junction",
        "west-supply",
        "western-trade",
        "north-care-approach",
        "north-care-loop"
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
]
```

## Geography and map controls

[Proposed map](../../../../design/maps/imperial-church/odyssey/34-church-transfer-constantinople.svg)

```json
{
  "bbox": [
    28.941,
    41.009,
    28.986,
    41.036
  ],
  "terrainProfile": "constantinople",
  "orientation": "north-up; Golden Horn north, Bosporus east, Propontis south, land approaches west; game camera calibration pending",
  "projection": "WGS84, cosine-corrected longitude, square padding through the existing geographic frame helper",
  "hubs": [
    {
      "id": "starting-court",
      "centre": [
        265.21,
        283.45
      ],
      "lonLat": [
        28.9718,
        41.0145
      ],
      "name": {
        "en": "The Clerk's Courtyard",
        "es-ES": "El patio del escribiente"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "meal-reception",
      "centre": [
        254.92,
        280.3
      ],
      "lonLat": [
        28.9705,
        41.0148
      ],
      "name": {
        "en": "The Neighbors' Table",
        "es-ES": "La mesa de los vecinos"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "materials-court",
      "centre": [
        136.17,
        227.83
      ],
      "lonLat": [
        28.9555,
        41.0198
      ],
      "name": {
        "en": "The Western Shelter Yard",
        "es-ES": "El patio de refugio occidental"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "kit-court",
      "centre": [
        163.88,
        260.36
      ],
      "lonLat": [
        28.959,
        41.0167
      ],
      "name": {
        "en": "The Interior Shelter Yard",
        "es-ES": "El patio de refugio interior"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "host-court",
      "centre": [
        236.71,
        325.42
      ],
      "lonLat": [
        28.9682,
        41.0105
      ],
      "name": {
        "en": "The Southern Host's Courtyard",
        "es-ES": "El patio del anfitrión del sur"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "meal-direct-source",
      "centre": [
        322.21,
        330.67
      ],
      "lonLat": [
        28.979,
        41.01
      ],
      "name": {
        "en": "The Prepared Consignment",
        "es-ES": "La remesa preparada"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "hearth-worksite",
      "centre": [
        195.54,
        276.1
      ],
      "lonLat": [
        28.963,
        41.0152
      ],
      "name": {
        "en": "The Shared Hearth",
        "es-ES": "El fogón compartido"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "merchant-worksite",
      "centre": [
        83.12,
        217.34
      ],
      "lonLat": [
        28.9488,
        41.0208
      ],
      "name": {
        "en": "The Western Merchant",
        "es-ES": "El mercader occidental"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "materials-source",
      "centre": [
        72.83,
        248.82
      ],
      "lonLat": [
        28.9475,
        41.0178
      ],
      "name": {
        "en": "The Timber Yard",
        "es-ES": "El depósito de madera"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "kit-worksite",
      "centre": [
        239.08,
        297.09
      ],
      "lonLat": [
        28.9685,
        41.0132
      ],
      "name": {
        "en": "The Local Workshop",
        "es-ES": "El taller local"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "host-worksite",
      "centre": [
        306.38,
        299.19
      ],
      "lonLat": [
        28.977,
        41.013
      ],
      "name": {
        "en": "The Host's Meeting Place",
        "es-ES": "El lugar de encuentro con el anfitrión"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "western-junction",
      "centre": [
        148.04,
        272.95
      ],
      "lonLat": [
        28.957,
        41.0155
      ],
      "name": {
        "en": "The Western Turn",
        "es-ES": "El desvío occidental"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "north-viewpoint",
      "centre": [
        116.38,
        209.99
      ],
      "lonLat": [
        28.953,
        41.0215
      ],
      "name": {
        "en": "The Upper Viewpoint",
        "es-ES": "El mirador alto"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "south-viewpoint",
      "centre": [
        215.33,
        341.16
      ],
      "lonLat": [
        28.9655,
        41.009
      ],
      "name": {
        "en": "The Southern Viewpoint",
        "es-ES": "El mirador sur"
      },
      "radiusTiles": 3,
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "north-care-yard",
      "centre": [
        64.92,
        162.77
      ],
      "lonLat": [
        28.9465,
        41.026
      ],
      "name": {
        "en": "The Northern Supply Yard",
        "es-ES": "El patio de suministros del norte"
      },
      "radiusTiles": 3,
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    },
    {
      "id": "north-store",
      "centre": [
        92.62,
        147.03
      ],
      "lonLat": [
        28.95,
        41.0275
      ],
      "name": {
        "en": "The Damaged Store",
        "es-ES": "El almacén dañado"
      },
      "radiusTiles": 3,
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    },
    {
      "id": "north-reader",
      "centre": [
        96.58,
        120.8
      ],
      "lonLat": [
        28.9505,
        41.03
      ],
      "name": {
        "en": "The Reader's Shelter",
        "es-ES": "El refugio del lector"
      },
      "radiusTiles": 3,
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    },
    {
      "id": "north-reception",
      "centre": [
        124.29,
        173.27
      ],
      "lonLat": [
        28.954,
        41.025
      ],
      "name": {
        "en": "The Northern Reception Yard",
        "es-ES": "El patio receptor del norte"
      },
      "radiusTiles": 3,
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    },
    {
      "id": "western-guide",
      "centre": [
        41.17,
        194.25
      ],
      "lonLat": [
        28.9435,
        41.023
      ],
      "name": {
        "en": "The Waiting Guide",
        "es-ES": "El guía que espera"
      },
      "radiusTiles": 3,
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    }
  ],
  "points": [
    {
      "id": "starting-court",
      "lonLat": [
        28.9718,
        41.0145
      ],
      "tile": [
        265.21,
        283.45
      ],
      "name": {
        "en": "The Clerk's Courtyard",
        "es-ES": "El patio del escribiente"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "meal-reception",
      "lonLat": [
        28.9705,
        41.0148
      ],
      "tile": [
        254.92,
        280.3
      ],
      "name": {
        "en": "The Neighbors' Table",
        "es-ES": "La mesa de los vecinos"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "materials-court",
      "lonLat": [
        28.9555,
        41.0198
      ],
      "tile": [
        136.17,
        227.83
      ],
      "name": {
        "en": "The Western Shelter Yard",
        "es-ES": "El patio de refugio occidental"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "kit-court",
      "lonLat": [
        28.959,
        41.0167
      ],
      "tile": [
        163.88,
        260.36
      ],
      "name": {
        "en": "The Interior Shelter Yard",
        "es-ES": "El patio de refugio interior"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "host-court",
      "lonLat": [
        28.9682,
        41.0105
      ],
      "tile": [
        236.71,
        325.42
      ],
      "name": {
        "en": "The Southern Host's Courtyard",
        "es-ES": "El patio del anfitrión del sur"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "meal-direct-source",
      "lonLat": [
        28.979,
        41.01
      ],
      "tile": [
        322.21,
        330.67
      ],
      "name": {
        "en": "The Prepared Consignment",
        "es-ES": "La remesa preparada"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "hearth-worksite",
      "lonLat": [
        28.963,
        41.0152
      ],
      "tile": [
        195.54,
        276.1
      ],
      "name": {
        "en": "The Shared Hearth",
        "es-ES": "El fogón compartido"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "merchant-worksite",
      "lonLat": [
        28.9488,
        41.0208
      ],
      "tile": [
        83.12,
        217.34
      ],
      "name": {
        "en": "The Western Merchant",
        "es-ES": "El mercader occidental"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "materials-source",
      "lonLat": [
        28.9475,
        41.0178
      ],
      "tile": [
        72.83,
        248.82
      ],
      "name": {
        "en": "The Timber Yard",
        "es-ES": "El depósito de madera"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "kit-worksite",
      "lonLat": [
        28.9685,
        41.0132
      ],
      "tile": [
        239.08,
        297.09
      ],
      "name": {
        "en": "The Local Workshop",
        "es-ES": "El taller local"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "host-worksite",
      "lonLat": [
        28.977,
        41.013
      ],
      "tile": [
        306.38,
        299.19
      ],
      "name": {
        "en": "The Host's Meeting Place",
        "es-ES": "El lugar de encuentro con el anfitrión"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "western-junction",
      "lonLat": [
        28.957,
        41.0155
      ],
      "tile": [
        148.04,
        272.95
      ],
      "name": {
        "en": "The Western Turn",
        "es-ES": "El desvío occidental"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "north-viewpoint",
      "lonLat": [
        28.953,
        41.0215
      ],
      "tile": [
        116.38,
        209.99
      ],
      "name": {
        "en": "The Upper Viewpoint",
        "es-ES": "El mirador alto"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "south-viewpoint",
      "lonLat": [
        28.9655,
        41.009
      ],
      "tile": [
        215.33,
        341.16
      ],
      "name": {
        "en": "The Southern Viewpoint",
        "es-ES": "El mirador sur"
      },
      "certainty": "fictional activity-site proposal within real peninsula; no excavated address"
    },
    {
      "id": "north-care-yard",
      "lonLat": [
        28.9465,
        41.026
      ],
      "tile": [
        64.92,
        162.77
      ],
      "name": {
        "en": "The Northern Supply Yard",
        "es-ES": "El patio de suministros del norte"
      },
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    },
    {
      "id": "north-store",
      "lonLat": [
        28.95,
        41.0275
      ],
      "tile": [
        92.62,
        147.03
      ],
      "name": {
        "en": "The Damaged Store",
        "es-ES": "El almacén dañado"
      },
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    },
    {
      "id": "north-reader",
      "lonLat": [
        28.9505,
        41.03
      ],
      "tile": [
        96.58,
        120.8
      ],
      "name": {
        "en": "The Reader's Shelter",
        "es-ES": "El refugio del lector"
      },
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    },
    {
      "id": "north-reception",
      "lonLat": [
        28.954,
        41.025
      ],
      "tile": [
        124.29,
        173.27
      ],
      "name": {
        "en": "The Northern Reception Yard",
        "es-ES": "El patio receptor del norte"
      },
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    },
    {
      "id": "western-guide",
      "lonLat": [
        28.9435,
        41.023
      ],
      "tile": [
        41.17,
        194.25
      ],
      "name": {
        "en": "The Waiting Guide",
        "es-ES": "El guía que espera"
      },
      "certainty": "fictional optional activity-site proposal; not an excavated late-Roman address"
    }
  ],
  "corridors": [
    {
      "id": "central-court",
      "hubOrder": [
        "starting-court",
        "host-worksite"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "east-source",
      "hubOrder": [
        "host-worksite",
        "meal-direct-source"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "east-return",
      "hubOrder": [
        "host-worksite",
        "meal-reception"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "central-reception",
      "hubOrder": [
        "starting-court",
        "meal-reception"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "ridge-hearth",
      "hubOrder": [
        "starting-court",
        "hearth-worksite"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "ridge-junction",
      "hubOrder": [
        "hearth-worksite",
        "western-junction"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "west-supply",
      "hubOrder": [
        "western-junction",
        "materials-source"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "western-trade",
      "hubOrder": [
        "materials-source",
        "merchant-worksite"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "western-reception",
      "hubOrder": [
        "merchant-worksite",
        "materials-court"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "interior-kit",
      "hubOrder": [
        "hearth-worksite",
        "kit-court"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "kit-source",
      "hubOrder": [
        "starting-court",
        "kit-worksite"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "kit-to-hearth",
      "hubOrder": [
        "kit-worksite",
        "hearth-worksite"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "southern-host",
      "hubOrder": [
        "starting-court",
        "host-court"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "southern-view",
      "hubOrder": [
        "host-court",
        "south-viewpoint"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "north-view",
      "hubOrder": [
        "materials-court",
        "north-viewpoint"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "north-care-approach",
      "hubOrder": [
        "merchant-worksite",
        "north-care-yard"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "north-care-loop",
      "hubOrder": [
        "north-care-yard",
        "north-store"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "north-reader-link",
      "hubOrder": [
        "north-store",
        "north-reader"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "north-reception-link",
      "hubOrder": [
        "north-reader",
        "north-reception"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "north-return",
      "hubOrder": [
        "north-reception",
        "north-viewpoint"
      ],
      "mode": "land",
      "widthTiles": 6
    },
    {
      "id": "guide-link",
      "hubOrder": [
        "western-guide",
        "materials-source"
      ],
      "mode": "land",
      "widthTiles": 6
    }
  ],
  "terrainInstructions": "Golden Horn north; peninsula activities remain on south bank. Positive DSM samples alone cannot identify the bank or prove land.\n\nPreserve broad peninsula hills; do not convert building-inclusive DSM heights directly to ancient ground or flat AoE platforms.\n\nDo not copy later Theodosian walls, 537 Hagia Sophia, later monumental Anastasia, Ottoman fabric, modern quays or bridges.\n\nWork yards, receiving courts and paths are declared fiction. No gate, church parcel, ancient street width or local residence is authenticated by its marker.\n\nProtect the uncertain Yenikapi coastal zone; no mission uses the harbor as an authenticated380landing.\n\nFull-width candidate corridors still require dated feature/land checks, building footprints, recovery and game navigation.\n\nDetailed OSM current shoreline now supplements the generalized NaturalEarth control; the blank plot remains unclassified and neither source is a380shoreline. All21candidate buffers avoid the retained current line, but no land mask, footprints, slope or ancient-route proof follows.",
  "geographicLayers": [
    {
      "assetId": "ne-odyssey-coastline",
      "interpretation": "generalized modern orientation; not the coast of 380"
    },
    {
      "assetId": "constantinople-modern-osm-coastline-geojson",
      "interpretation": "detailed current mapped coastline; no land mask or ancient shoreline"
    },
    {
      "assetId": "constantinople-modern-dsm-reference",
      "interpretation": "modern surface heights including possible buildings and vegetation; not bare earth or ancient ground"
    }
  ],
  "geometryStatus": "authored georeferenced candidate; modern coastline-line clearance checked separately; ancient shore, footprints, land mask, slopes and native navigation pending",
  "asset": "docs/design/maps/imperial-church/odyssey/34-church-transfer-constantinople.svg",
  "corridorStraightLengthsTiles": {
    "central-court": 44.076,
    "east-source": 35.236,
    "east-return": 54.818,
    "central-reception": 10.761,
    "ridge-hearth": 70.057,
    "ridge-junction": 47.604,
    "west-supply": 78.986,
    "western-trade": 33.119,
    "western-reception": 54.077,
    "interior-kit": 35.357,
    "kit-source": 29.476,
    "kit-to-hearth": 48.335,
    "southern-host": 50.732,
    "southern-view": 26.549,
    "north-view": 26.644,
    "north-care-approach": 57.525,
    "north-care-loop": 31.86,
    "north-reader-link": 26.527,
    "north-reception-link": 59.338,
    "north-return": 37.562,
    "guide-link": 63.089
  },
  "activeAreaPolicy": "Nineteen authored local points and twenty-one finite walking connections cover work, reception and seven optional tasks. Keep the quiet unused frame as context; do not fill it with invented armies, random errands or authenticated ancient buildings. Inspect every full-width route before approval.",
  "sourceBindings": [
    {
      "path": "docs/design/episode-plans/imperial-church/34-constantinople-world-plan.json",
      "sha256": "9e93ba37d40f9fa81c5a7722e4a04aa307e59c7442f5bd2c51d779747ed4c178",
      "meaning": "Original source retains full point geography/modern DSM samples, route qualifications, 45 authored screens and historical uncertainty."
    },
    {
      "path": "docs/design/episode-plans/imperial-church/34-profile-ui-supplement.json",
      "sha256": "5e35b496c3140045c580c1ba48db71af6015b50bb6651c0c2cb0347fd372528b"
    },
    {
      "path": "docs/design/episode-plans/imperial-church/34-reference-profile-bindings.json",
      "sha256": "a9921fc3d323d4242ab46fce53feaf6b9096545d3dcc6741da3dc64122b87c6d",
      "meaning": "Retains source hashes, original slot IDs, full geographic records and route annotations outside the strict runtime profile."
    }
  ]
}
```

## Authored presentation

### title (title)

EN: The Doors of New Rome

ES: Las puertas de Nueva Roma

Condition: before fact-intro · narrator: none · native surface: pending certified SequenceItems/message adapter.

### fact-intro (factualIntro)

EN: In late 380, Theodosius entered Constantinople and ordered changes in church possession. Socrates places the arrival and transfer on separate November days; Marcellinus records the restoration he favored in December. These later accounts do not establish what every inhabitant believed. The following local service story is invented.

ES: A finales de 380, Teodosio entró en Constantinopla y ordenó cambios en la posesión de iglesias. Sócrates sitúa la llegada y el traspaso en días distintos de noviembre; Marcelino fecha en diciembre la restauración que favorecía. Estos relatos posteriores no establecen qué creía cada habitante. La siguiente historia asistencial local es inventada.

Condition: before personal introduction · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### handover (handover)

EN: Marcus, the clerk whose account accompanies this campaign, now describes a day among fictional neighbors. His judgments are his own.

ES: Marcus, el escribiente cuyo relato acompaña esta campaña, describe ahora una jornada entre vecinos ficticios. Sus juicios le pertenecen.

Condition: after factual introduction · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### personal-intro (personalIntro)

EN: I had written a fine heading about concord. My neighbor read it upside down and asked where her mother could sit that evening. I explained what I thought the emperor intended. She asked again about the chair. I turned the sheet over and began a different list.

ES: Había escrito un encabezamiento solemne sobre la concordia. Mi vecina lo leyó del revés y preguntó dónde podría sentarse su madre aquella tarde. Le expliqué lo que yo creía que pretendía el emperador. Volvió a preguntar por la silla. Di la vuelta a la hoja y empecé otra lista.

Condition: after handover · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### main-goal (unassigned authored screen)

EN: Arrange a meal for its original recipient and shelter for the two original households. Choose one method for each service, fund the complete plan, carry out its work and bring each selected result to its own court. Keep all three original recipients alive and present at their respective courts at the end.

ES: Organiza una comida para su destinatario original y alojamiento para los dos hogares originales. Elige un método por servicio, financia el plan completo, realiza su trabajo y lleva cada resultado seleccionado a su patio correspondiente. Conserva vivos y presentes a los tres destinatarios originales en sus respectivos patios al final.

Condition: main objective list · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### shared-attendance-goal (unassigned authored screen)

EN: Bring the original meal recipient to the receiving court. This attendance does not complete either service. The same recipient must be alive at that court again when the whole plan ends.

ES: Lleva al destinatario original de la comida al patio receptor. Esta presencia no completa ninguno de los servicios. Ese mismo destinatario deberá estar vivo en el patio cuando termine el plan completo.

Condition: phase-1 active; shared attendance not yet latched; never a service receipt · narrator: none · native surface: pending certified SequenceItems/message adapter.

### meal-service-goal (unassigned authored screen)

EN: Complete the selected meal method, then bring its own result and the original recipient to The Neighbors' Table. A receipt alone is insufficient if either is absent at the end.

ES: Completa el método de comida elegido y lleva su resultado propio y al destinatario original a la mesa de los vecinos. El recibo no basta si alguno está ausente al final.

Condition: phase-1 active; meal-service goal; only its selected recipe may complete it · narrator: none · native surface: pending certified SequenceItems/message adapter.

### shelter-service-goal (unassigned authored screen)

EN: Complete the selected shelter method, then bring its own result and both original households to that method's receiving court. Another court, another result or substitute households do not count. All must be alive there at the end.

ES: Completa el método de alojamiento elegido y lleva su resultado propio y a ambos hogares originales al patio receptor de ese método. No cuentan otro patio, otro resultado ni hogares sustitutos. Todos deberán estar vivos allí al final.

Condition: phase-1 active; shelter-service goal; only its selected recipe may complete it · narrator: none · native surface: pending certified SequenceItems/message adapter.

### preview-help (unassigned authored screen)

EN: Compare the joint cost, the remaining supplies and both work routes before confirming. Preview is free. The three meal methods lead to one reception; each shelter method has its own receiving court. All main destinations and costs are visible without optional tasks.

ES: Compara el coste conjunto, los suministros restantes y ambos recorridos antes de confirmar. La consulta es gratuita. Los tres métodos de comida llevan a una recepción; cada método de alojamiento tiene su propio patio receptor. Los destinos y costes principales están visibles aunque omitas los secundarios.

Condition: first plan preview or help · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### budget-help (unassigned authored screen)

EN: Your operating allocation is finite. Easy: 420 food, 380 wood and 260 gold. Standard: 340 food, 280 wood and 150 gold. Hard: 300 food, 220 wood and 120 gold. Optional rewards remain separate until earned. Every difficulty can be completed without any optional task.

ES: Tu asignación operativa es finita. Fácil: 420 de alimento, 380 de madera y 260 de oro. Normal: 340 de alimento, 280 de madera y 150 de oro. Difícil: 300 de alimento, 220 de madera y 120 de oro. Las recompensas opcionales permanecen separadas hasta ganarlas. Todas las dificultades permiten terminar sin hacer tareas opcionales.

Condition: economy help · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### unaffordable-plan (unassigned authored screen)

EN: The complete plan costs more than your available allocation. Nothing has been charged. Choose another pair or earn optional assistance before funding. A reward cannot pay its own upfront cost.

ES: El plan completo cuesta más que tu asignación disponible. No se ha cobrado nada. Elige otra pareja o consigue ayuda opcional antes de financiarlo. Una recompensa no puede pagar su propio coste inicial.

Condition: failed whole-plan affordability check · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### reservation-help (unassigned authored screen)

EN: You may cancel and choose again before any selected work begins. Cancellation returns only the reserved plan cost. Once work starts, the selected methods are fixed; no free refund, replacement household or substitute result is available.

ES: Puedes cancelar y volver a elegir antes de que empiece cualquier trabajo seleccionado. La cancelación devuelve únicamente el coste reservado del plan. Una vez iniciado el trabajo, los métodos quedan fijados: no hay devolución gratuita, hogar de reemplazo ni resultado sustituto.

Condition: before confirmation and on help · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### plan-reserved (unassigned authored screen)

EN: The full cost of both selected services is reserved. No work has been recorded and neither service is complete. Before committing, you may cancel and recover that exact reserve; the rest of your supplies remain separate.

ES: El coste completo de los dos servicios elegidos queda reservado. No se ha registrado trabajo ni se ha completado ningún servicio. Antes del compromiso puedes cancelar y recuperar esa reserva exacta; el resto de tus suministros permanece separado.

Condition: after successful reserve; while reserved; never after failed reserve or commitment · narrator: none · native surface: pending certified SequenceItems/message adapter.

### plan-committed (unassigned authored screen)

EN: Your chosen plan is committed. Its reserved supplies have been spent once. Send the assigned workers to their selected work sites; work and delivery are still required. The methods can no longer be changed or cancelled.

ES: El plan elegido queda comprometido. Sus suministros reservados se han gastado una vez. Envía a los trabajadores asignados a sus lugares de trabajo elegidos; aún faltan el trabajo y la entrega. Ya no se pueden cambiar ni cancelar los métodos.

Condition: after successful irreversible commitment; work/output receipts are not implied · narrator: none · native surface: pending certified SequenceItems/message adapter.

### cancelled (unassigned authored screen)

EN: A crossed-out estimate is cheaper than a promise already put to work. We can choose again.

ES: Un presupuesto tachado cuesta menos que una promesa que ya se ha puesto en marcha. Podemos volver a elegir.

Condition: successful pre-work cancellation · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### work-help (unassigned authored screen)

EN: Send each assigned worker to the selected work site. After the work is recorded, take that method's own result to its receiving court. Paying, visiting the wrong site or delivering another method's result does not complete a service.

ES: Envía a cada trabajador asignado al lugar de trabajo seleccionado. Tras registrar el trabajo, lleva el resultado propio de ese método a su patio receptor. Pagar, visitar otro lugar o entregar el resultado de otro método no completa un servicio.

Condition: after whole-plan funding · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### work-meal-direct (unassigned authored screen)

EN: Selected method: Prepared Provisions. Cost: 240 food, 40 wood. Work at The Prepared Consignment; then take the result to The Neighbors' Table. The assigned worker must reach the work site before its own result is available.

ES: Método seleccionado: Provisiones preparadas. Coste: 240 de alimento, 40 de madera. Trabaja en La remesa preparada; después lleva el resultado a La mesa de los vecinos. El trabajador asignado debe llegar al lugar de trabajo antes de que esté disponible su resultado propio.

Condition: instructions for the actual selected recipe · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### work-meal-shared-hearth (unassigned authored screen)

EN: Selected method: At the Shared Hearth. Cost: 160 food, 140 wood. Work at The Shared Hearth; then take the result to The Neighbors' Table. The assigned worker must reach the work site before its own result is available.

ES: Método seleccionado: Junto al fogón compartido. Coste: 160 de alimento, 140 de madera. Trabaja en El fogón compartido; después lleva el resultado a La mesa de los vecinos. El trabajador asignado debe llegar al lugar de trabajo antes de que esté disponible su resultado propio.

Condition: instructions for the actual selected recipe · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### work-meal-purchased (unassigned authored screen)

EN: Selected method: A Merchant's Consignment. Cost: 100 food, 40 wood, 100 gold. Work at The Western Merchant; then take the result to The Neighbors' Table. The assigned worker must reach the work site before its own result is available.

ES: Método seleccionado: La remesa del mercader. Coste: 100 de alimento, 40 de madera, 100 de oro. Trabaja en El mercader occidental; después lleva el resultado a La mesa de los vecinos. El trabajador asignado debe llegar al lugar de trabajo antes de que esté disponible su resultado propio.

Condition: instructions for the actual selected recipe · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### work-shelter-materials (unassigned authored screen)

EN: Selected method: Build from Delivered Materials. Cost: 80 food, 200 wood. Work at The Timber Yard; then take the result to The Western Shelter Yard. The assigned worker must reach the work site before its own result is available.

ES: Método seleccionado: Preparar con materiales entregados. Coste: 80 de alimento, 200 de madera. Trabaja en El depósito de madera; después lleva el resultado a El patio de refugio occidental. El trabajador asignado debe llegar al lugar de trabajo antes de que esté disponible su resultado propio.

Condition: instructions for the actual selected recipe · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### work-shelter-local-kit (unassigned authored screen)

EN: Selected method: Prepare a Local Kit. Cost: 100 food, 120 wood, 20 gold. Work at The Local Workshop; then take the result to The Interior Shelter Yard. The assigned worker must reach the work site before its own result is available.

ES: Método seleccionado: Preparar un equipo local. Coste: 100 de alimento, 120 de madera, 20 de oro. Trabaja en El taller local; después lleva el resultado a El patio de refugio interior. El trabajador asignado debe llegar al lugar de trabajo antes de que esté disponible su resultado propio.

Condition: instructions for the actual selected recipe · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### work-shelter-rented (unassigned authored screen)

EN: Selected method: A Willing Host. Cost: 60 food, 60 wood, 110 gold. Work at The Host's Meeting Place; then take the result to The Southern Host's Courtyard. The assigned worker must reach the work site before its own result is available.

ES: Método seleccionado: Un anfitrión dispuesto. Coste: 60 de alimento, 60 de madera, 110 de oro. Trabaja en El lugar de encuentro con el anfitrión; después lleva el resultado a El patio del anfitrión del sur. El trabajador asignado debe llegar al lugar de trabajo antes de que esté disponible su resultado propio.

Condition: instructions for the actual selected recipe · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### meal-received (unassigned authored screen)

EN: One line has become a meal at the right table. Keep its recipient here while we finish the other service.

ES: Una línea se ha convertido en una comida en la mesa adecuada. Mantén aquí a su destinatario mientras terminamos el otro servicio.

Condition: qualified meal output receipt · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### shelter-received (unassigned authored screen)

EN: The same two households, at the court we actually arranged. I shall not replace either name with a convenient mark.

ES: Los mismos dos hogares, en el patio que hemos preparado de verdad. No sustituiré ninguno de sus nombres por una marca cómoda.

Condition: qualified shelter output receipt · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### final-presence-help (unassigned authored screen)

EN: Both receipts remain recorded, but success also requires every original recipient alive at its selected court now. A past arrival does not count as current presence. Return a departing recipient before completing the other service.

ES: Ambos recibos quedan registrados, pero el éxito también exige que cada destinatario original esté vivo ahora en su patio seleccionado. Una llegada pasada no cuenta como presencia actual. Haz regresar a quien se aleje antes de completar el otro servicio.

Condition: receipt exists but final living presence not satisfied · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### offer-neighbor-provisions (unassigned authored screen)

EN: Bring each marked aid crate to its own marked household collection post in the Northern Reception Yard. Household members are off scene; the two crate arrivals complete this task. Benefit: 100 food, 50 wood, once.

ES: Lleva cada caja de ayuda señalada a su puesto de recogida de hogar correspondiente, también señalado, en el patio receptor del norte. Los miembros de esos hogares quedan fuera de escena; las dos llegadas de cajas completan esta tarea. Ventaja: 100 de alimento, 50 de madera, una vez.

Condition: optional objective offered from start · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### complete-neighbor-provisions (unassigned authored screen)

EN: Two crates, two marked collection posts. The households can collect them later. The spare timber is real enough; the generous heading may wait.

ES: Dos cajas, dos puestos de recogida señalados. Los hogares podrán recogerlas después. La madera que queda es bastante real; el encabezamiento generoso puede esperar.

Condition: optional predicate and atomic reward completed once · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### unavailable-neighbor-provisions (unassigned authored screen)

EN: The missing consignment cannot be wished into the other crate. This aid task closes; our main services remain possible.

ES: La remesa perdida no aparece por desearla en la otra caja. Esta ayuda se cierra; los servicios principales siguen siendo posibles.

Condition: unique optional identity lost, or terminal closes an incomplete observation task; no main defeat · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### offer-voluntary-household-return (unassigned authored screen)

EN: Bring both marked voluntary groups alive from the Northern Supply Yard to the Western Shelter Yard. Benefit: 100 food, 25 gold, once.

ES: Lleva con vida a los dos grupos voluntarios señalados desde el patio de suministros del norte hasta el patio de refugio occidental. Ventaja: 100 de alimento, 25 de oro, una vez.

Condition: optional objective offered from start · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### complete-voluntary-household-return (unassigned authored screen)

EN: They chose the receiving yard and reached it together. These are their names, not substitutes for another family.

ES: Eligieron el patio receptor y llegaron juntos. Estos son sus nombres, no sustitutos de otra familia.

Condition: optional predicate and atomic reward completed once · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### unavailable-voluntary-household-return (unassigned authored screen)

EN: We cannot repeat their journey with strangers and call it the same arrival. This optional task has ended.

ES: No podemos repetir su recorrido con desconocidos y llamarlo la misma llegada. Esta tarea opcional ha terminado.

Condition: unique optional identity lost, or terminal closes an incomplete observation task; no main defeat · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### offer-source-comparison (unassigned authored screen)

EN: Recover the two marked working copies at the Reader's Shelter and place both at the marked collection desk beside the Shared Hearth. The reader is off scene; both copy arrivals complete this task. Benefit: unlock a historical note and an explicit main-goal hint.

ES: Recupera las dos copias de trabajo señaladas en el refugio del lector y deposita ambas en la mesa receptora señalada junto al fogón compartido. El lector queda fuera de escena; las dos llegadas de copias completan esta tarea. Ventaja: desbloquea una nota histórica y una pista explícita del objetivo principal.

Condition: optional objective offered from start · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### complete-source-comparison (unassigned authored screen)

EN: Both working copies are on the collection desk. Two separate sheets deserve two separate entries; the reader need not stand here for me to record their arrival.

ES: Ambas copias de trabajo están en la mesa receptora. Dos hojas distintas merecen dos anotaciones distintas; no hace falta que el lector esté aquí para que registre su llegada.

Condition: optional predicate and atomic reward completed once · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### unavailable-source-comparison (unassigned authored screen)

EN: One working copy is missing. Leave that line incomplete; do not make a second original out of the first.

ES: Falta una copia de trabajo. Deja esa línea incompleta; no conviertas la primera en un segundo original.

Condition: unique optional identity lost, or terminal closes an incomplete observation task; no main defeat · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### offer-local-wayfinding (unassigned authored screen)

EN: Escort the marked local guide to the Western Turn. Benefit: Mark the existing western supply link and its actual work-site target.

ES: Escolta al guía local señalado hasta el desvío occidental. Ventaja: Señala la conexión occidental existente y su punto de trabajo real.

Condition: optional objective offered from start · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### complete-local-wayfinding (unassigned authored screen)

EN: The guide has shown the existing turn. Ink can mark a road; it cannot build one.

ES: El guía ha señalado el desvío existente. La tinta puede marcar un camino; no construirlo.

Condition: optional predicate and atomic reward completed once · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### unavailable-local-wayfinding (unassigned authored screen)

EN: We have lost this guide's help. The western connection still exists; the main destinations are still marked.

ES: Hemos perdido la ayuda de este guía. La conexión occidental sigue existiendo; los destinos principales continúan señalados.

Condition: unique optional identity lost, or terminal closes an incomplete observation task; no main defeat · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### offer-slope-survey (unassigned authored screen)

EN: Visit both marked interior viewpoints: the Upper Viewpoint and the Southern Viewpoint. Benefit: Mark the existing care loop; all costs and destinations remain available without this task.

ES: Visita los dos miradores interiores señalados: el mirador alto y el mirador sur. Ventaja: Señala el circuito asistencial existente; costes y destinos siguen disponibles aunque omitas esta tarea.

Condition: optional objective offered from start · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### complete-slope-survey (unassigned authored screen)

EN: Both viewpoints are recorded. The long circuit is still long, but we can see what it serves.

ES: Ambos miradores quedan registrados. El circuito largo sigue siendo largo, pero vemos a qué sirve.

Condition: optional predicate and atomic reward completed once · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### unavailable-slope-survey (unassigned authored screen)

EN: This survey closes with the other unfinished tasks. It grants no late supplies and changes no road.

ES: Esta exploración se cierra con las demás tareas sin terminar. No concede suministros tardíos ni cambia ningún camino.

Condition: unique optional identity lost, or terminal closes an incomplete observation task; no main defeat · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### offer-service-observation (unassigned authored screen)

EN: Visit both marked observation spots beside the Western Shelter Yard and the Southern Host's Courtyard. Benefit: Mark the existing southern host approach and explain the selected-court requirement.

ES: Visita los dos puntos de observación señalados junto al patio de refugio occidental y al patio del anfitrión del sur. Ventaja: Señala el acceso sur existente y explica que cuenta únicamente el patio seleccionado.

Condition: optional objective offered from start · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### complete-service-observation (unassigned authored screen)

EN: Two approaches, different courts. The word shelter no longer hides which door we mean.

ES: Dos accesos, patios distintos. La palabra alojamiento ya no oculta a qué puerta nos referimos.

Condition: optional predicate and atomic reward completed once · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### unavailable-service-observation (unassigned authored screen)

EN: The observation remains incomplete. Use the already visible selected court; no service depends on this note.

ES: La observación queda incompleta. Usa el patio seleccionado que ya está visible; ningún servicio depende de esta nota.

Condition: unique optional identity lost, or terminal closes an incomplete observation task; no main defeat · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### offer-damaged-civilian-store (unassigned authored screen)

EN: Restore the marked damaged store to full health through its single 50-wood repair action. Benefit: 200 food, 100 wood, once.

ES: Restaura por completo el almacén dañado señalado mediante su única acción de reparación de 50 de madera. Ventaja: 200 de alimento, 100 de madera, una vez.

Condition: optional objective offered from start · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### complete-damaged-civilian-store (unassigned authored screen)

EN: The store is restored, and its reserved supplies can be issued once. A payment without the work would have repaired only my accounts.

ES: El almacén está restaurado y sus suministros reservados pueden entregarse una vez. Un pago sin trabajo sólo habría reparado mis cuentas.

Condition: optional predicate and atomic reward completed once · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### unavailable-damaged-civilian-store (unassigned authored screen)

EN: The store can no longer be restored in this task. Its reserved stock remains unearned; the main services do not fail with it.

ES: Ya no se puede restaurar el almacén en esta tarea. Sus existencias reservadas siguen sin ganarse; los servicios principales no fracasan por ello.

Condition: unique optional identity lost, or terminal closes an incomplete observation task; no main defeat · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### retrospective-source-note (unassigned authored screen)

EN: The work copies in this fictional 380 scene are not the books of Socrates or Marcellinus. Those later writers place the possession change in different months. Their disagreement is retained for the player; Marcus does not read these later works in 380.

ES: Las copias de trabajo de esta escena ficticia de 380 no son los libros de Sócrates ni Marcelino. Esos autores posteriores sitúan el cambio de posesión en meses distintos. Su discrepancia se conserva para el jugador; Marcus no lee estas obras posteriores en 380.

Condition: source-comparison contextual note; outside persona knowledge · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### main-defeat (defeat)

EN: A required original recipient, a selected result after commitment, or an assigned worker before completing its work has been lost. This local plan cannot be completed with replacements. Load an earlier save or restart. A worker lost after completing its work does not undo that result; the historical account is unchanged.

ES: Se ha perdido un destinatario original obligatorio, un resultado seleccionado después del compromiso o un trabajador asignado antes de completar su trabajo. Este plan local no se puede terminar con reemplazos. Carga una partida anterior o reinicia. Perder a un trabajador después de completar su trabajo no anula ese resultado; el relato histórico no cambia.

Condition: required terminal loss; death checked before simultaneous success · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### victory-fact (factualOutro)

EN: Both invented local services have been completed with their original recipients. This does not explain, approve or reverse the imperial change in church possession. The next episode concerns the council of 381 and the disputes that continued.

ES: Ambos servicios locales inventados se han completado con sus destinatarios originales. Esto no explica, aprueba ni revierte el cambio imperial de posesión de iglesias. El siguiente episodio trata del concilio de 381 y de las disputas que continuaron.

Condition: both qualified services and fresh living-recipient presence, before victory · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

### victory-personal (personalOutro)

EN: My heading still said concord. Beneath it were two completed services and names I had nearly reduced to a phrase. I kept the heading, crossed it out, and left the rest legible.

ES: Mi encabezamiento seguía diciendo concordia. Debajo había dos servicios cumplidos y nombres que casi había reducido a una frase. Conservé el encabezamiento, lo taché y dejé legible lo demás.

Condition: after factual outcome · narrator: imperial-clerk · native surface: pending certified SequenceItems/message adapter.

### continue-next (continuation)

EN: Next is episode 34, Under the Same Eastern Sky, set in 381: the finale of The Eagle and the Cross. Recommendations for other odysseys appear after completing that finale.

ES: El siguiente es el episodio 34, Bajo el mismo cielo oriental, ambientado en 381: el final de El águila y la cruz. Las recomendaciones de otras odiseas aparecen después de completar ese episodio final.

Condition: after personal outcome; before normal episode victory/menu return · narrator: collection-narrator · native surface: pending certified SequenceItems/message adapter.

## QA and capability limits

```json
{
  "qa": {
    "staticStatus": "typed v3 profile and dossier bindings checked",
    "nativeStatus": "pending",
    "gameVerified": false,
    "cases": [
      "For each difficulty, enumerate all nine complete recipe selections and distinguish the 9/7/3 affordable rows without counting optional rewards.",
      "For every affordable selection, test reserve, cancel before commitment and irreversible commitment with exact selected costs, preserving all isolated account balances.",
      "Payment or shared attendance alone must not complete either selected service. Confirm selected work, genuine generation, correct output and original recipient reception separately.",
      "At final evaluation require the selected output and original living recipients freshly present at that recipe's own court; reject wrong recipe, stale receipt, substitute or wrong court.",
      "Observe simultaneous required loss and potential victory in both input orders; required defeat must win. Preserve valid recorded work when only its former worker is lost afterward.",
      "Skip all seven secondaries and complete the main plan in each difficulty; separately test all-complete and the three authored portfolios with actual travel and reachable payment prefixes.",
      "On Hard, shared-hearth plus rented shelter leaves 20 wood: repair cannot pay its 50-wood cost before suitable earned aid; no reward may pay its own prerequisite debit.",
      "Verify all nineteen point centres, ten main circles and full widths of all twenty-one connections against terrain/building footprints; modern coastline clearance alone cannot pass land or ancient geography.",
      "Save/load before and after reservation, cancellation, commitment, each work/generation/reception, each optional reward and final terminal evaluation.",
      "Verify the 51 authored screen records in EN/es-ES, factual-to-personal opening, disputed dates, service choice and clear unaffordable/cancel/commit/recovery messages.",
      "Complete this intermediate episode and recommend only the existing 381 council finale; do not write campaign completion or offer successor campaigns early."
    ]
  },
  "requiredCapabilities": [
    {
      "id": "composed-world-ledger",
      "status": "reference model implemented; native composition, observations and save/load QA pending"
    },
    {
      "id": "alternative-fulfillment-v3",
      "status": "reference model implemented; native joint selector, escrow, work, generation and selected reception pending"
    },
    {
      "id": "live-entity-presence",
      "status": "reference model implemented; native fresh living presence observations and terminal batching pending"
    },
    {
      "id": "geographic-land-corridors",
      "status": "authored candidate geometry; ancient shoreline, footprints, slopes and pathfinding pending"
    },
    {
      "id": "two-narrator-sequence",
      "status": "EN/es-ES source text authored; editorial, native sequence/captions and localization QA pending"
    },
    {
      "id": "optional-secondary-contracts",
      "status": "strict reference contracts authored; native predicates, once-only rewards, failure presentation and save/load QA pending"
    }
  ],
  "continuation": {
    "nextEpisodeId": "29-council-and-final-perspective-constantinople",
    "campaignComplete": false,
    "sourceScreenId": "continue-next"
  },
  "gameplayIdentity": {
    "problem": "Choose one meal method and one shelter method under finite joint accounts, then perform their actual selected work and receptions for distinct fictional original people.",
    "decision": "Compare resource composition, local travel and optional information/aid before irreversible commitment. The 9/7/3 affordable sets provide increasingly constrained choices without a fabricated riot, clock or enemy army.",
    "density": "Nineteen local places, six work/output methods, three shelter receiving courts, one meal court and seven distinct optional tasks; avoid making the giant frame a compulsory empty walking tour.",
    "replay": "The historical possession change remains fixed. Replay varies the chosen pair, approach/return routes and the three combinable optional portfolios.",
    "pacing": "Reflective civic episode between the Thessalonica law and the 381 council finale. Hard is an uncalibrated allocation/travel hypothesis; fewer workers and waiting are not advertised as the challenge.",
    "limits": "No measured duration or native difficulty approval; conduct full-width navigation and per-difficulty playtests before mechanical historical authoring."
  },
  "failureRecovery": {
    "beforeCommit": "Preview is free. An unaffordable confirmation changes no account. A complete reserved plan can be cancelled before irreversible commitment, refunding only its escrow; compare and reserve again.",
    "afterCommit": "Costs are paid once and methods remain locked. An incorrect destination or absent recipient creates no service receipt: direct the same living original output and recipients to the selected court and obtain fresh observations. No timer substitutes for work or arrival.",
    "mainIdentityLoss": "Loss of a required original recipient, loss of the selected worker before recorded work, or destruction of a genuinely generated selected output causes defeat under the existing reference rules. No free resurrection or hidden grace period is promised. A worker lost after recorded work adds no new worker-return condition.",
    "optionalIdentityLoss": "Only the corresponding optional fails; no main defeat, late reward or campaign restart. Main victory closes unfinished optionals.",
    "resources": "At least one complete plan remains affordable in each difficulty with all optionals skipped. Optional stock and protected recovery cannot fund the main reservation; there is no gathering, regeneration, passive income or replacement purchase in this reference design.",
    "nativeStatus": "All recovery descriptions still require native input/template, save/load and game checks; reference behavior alone is not an engine implementation."
  }
}
```

A reference-profile projection is not native support. Native rendering, actual UI, audio, world footprints, pathfinding, difficulty, engine behavior and historical approval remain separate gates.
