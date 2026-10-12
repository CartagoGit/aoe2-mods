# Beneath the Desert Stars / Bajo las estrellas del desierto

`first-caliphs` · CDF-I00 · 30 selected episodes · source locale `en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

```json
{
  "editorial": {
    "campaignTitle": {
      "en": "Beneath the Desert Stars",
      "es-ES": "Bajo las estrellas del desierto"
    },
    "publicId": "CDF-I00",
    "internalName": "CDF_FirstCaliphs",
    "sourceLocale": "en",
    "targetEpisodeCount": 30,
    "narratorId": "salim-caravan-scribe",
    "personaLens": {
      "en": "Wells, caravan measures and reports from travellers",
      "es-ES": "Pozos, medidas de caravana y relatos de viajeros"
    },
    "deliveryTone": {
      "en": "hospitality and wonder shading into concern",
      "es-ES": "hospitalidad y asombro que se vuelven preocupación"
    },
    "sequence": [
      {
        "speaker": "collection-narrator",
        "mode": "sober source-qualified historical fact",
        "causePolicy": "attribute motives, miracles and sectarian judgements to their sources; no single moral or theological verdict"
      },
      {
        "speaker": "salim-caravan-scribe",
        "mode": "fictional personal interpretation with explicit witness basis"
      }
    ],
    "baselineSemanticIdsPreserved": [
      "01-the-oasis-road",
      "02-the-roads-of-yamama",
      "03-the-edge-of-the-river",
      "04-fields-of-the-sawad",
      "05-a-camp-beside-the-nile"
    ],
    "orderingPolicy": "order is a separate integer; existing semantic IDs and public/progress IDs remain stable",
    "progressPolicy": "only the actual final odyssey episode offers terminal route write; every former last baseline mission becomes nonterminal when followed by new episodes",
    "sourceAuditStatus": "candidate chronologies reviewed for errors; individual episode historical approval pending",
    "coreMechanicPolicy": "at least four mission-core families in each odyssey; no more than two consecutive identical core families without authored reason; side-objective variety does not excuse identical main missions",
    "selectedEpisodeCount": 30,
    "selectionNotes": [
      "Act counts are subordinate to source chronology and are not filler quotas.",
      "Scene location fixes the local player adventure; remote event claims remain explicitly off-map reports.",
      "Repeated core families require episode-specific world layout, counts and choice tradeoffs before authoring assignment.",
      "Archaeology is dated by phases; a modern artifact is not proof of a precise ancient dedication date."
    ]
  },
  "continuity": {
    "recommendedPrevious": [],
    "nextRoutes": [
      {
        "id": "completed",
        "key": "progress.first-caliphs.completed",
        "next": "first-fitna"
      }
    ],
    "chronologyWarning": "Any predecessor-dependent campaign remains independently playable; show recommendation and recap, preserve all route keys, and disclose overlap when changing perspective.",
    "terminalScreenRule": "show successor English/Spanish title plus public ID for the chosen route; no automatic launching and no requirement lock",
    "proceedWithoutPredecessor": true
  }
}
```

Only the final expanded episode may complete this campaign or present the successor recommendation. Former baseline finales become intermediate episodes when later episodes exist. Preserve every existing semantic scenario ID; display order is a separate field.

## act-1: Voices of the Meccan Roads / Voces de los caminos de La Meca

Historical year band: [610, 622]. Predicación según tradición, migraciones y pactos; Salim es niño y conoce relatos heredados.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 1 / 01-testimony-and-household-supply-mecca | The Mountain in the Remembered Story / La montaña en el relato recordado | c.610 CE; revelation belongs to attributed tradition | mecca | testimony-and-household-supply |
| 2 / 02-civilian-network-and-records-mecca | Voices among the Market Stalls / Voces entre los puestos del mercado | 610s CE; public preaching conventionallyc.613 | mecca | civilian-network-and-records |
| 3 / 03-finite-emigration-consignments-mecca | A Passage across the Red Sea / Un pasaje por el mar Rojo | c.615 CE; Aksum destination off-map and uncertain | mecca | finite-emigration-consignments |
| 4 / 04-bounded-household-provision-mecca | The Houses under the Boycott / Las casas bajo el boicot | c.616–619 CE; transmitted chronology uncertain | mecca | bounded-household-provision |
| 5 / 05-delegate-logistics-and-receipts-mina-aqaba | The First Promise at Aqaba / La primera promesa en Aqaba | 621 CE traditional; firstpledge, notsecond | mina-aqaba | delegate-logistics-and-receipts |
| 6 / 06-bounded-reception-planning-mina-aqaba | A Road Promised to Strangers / Un camino prometido a extranjeros | 622 CE; conventionally secondpledge | mina-aqaba | bounded-reception-planning |
| 7 / 01-the-oasis-road | The Oasis Road / El camino del oasis | 622 CE | medina | migration-and-refuge |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.63,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 0.76,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 0.9,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## act-2: The Oasis and the Pact / El oasis y el pacto

Historical year band: [622, 632]. Comunidad de Medina, defensa y acuerdos; las figuras veneradas se narran fuera de mapa sin unidades atacables.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 8 / 08-finite-battle-supply-and-withdrawal-badr | Water before the First Battle / Agua antes de la primera batalla | 624 CE | badr | finite-battle-supply-and-withdrawal |
| 9 / 09-finite-withdrawal-and-care-uhud | Below the Broken Ridge / Bajo la cresta quebrada | 625 CE | uhud | finite-withdrawal-and-care |
| 10 / 10-finite-defence-and-trench-supply-medina | The Ditch before the Oasis / El foso ante el oasis | 627 CE conventional | medina | finite-defence-and-trench-supply |
| 11 / 11-bounded-negotiation-and-supply-hudaybiyya | A Truce at the Road's End / Una tregua al final del camino | March628 CE;6AH | hudaybiyya | bounded-negotiation-and-supply |
| 12 / 12-finite-siege-and-civilian-extraction-khaybar | The Forts among the Palms / Los fuertes entre las palmeras | 628 CE conventional | khaybar | finite-siege-and-civilian-extraction |
| 13 / 13-civilian-provision-under-entry-mecca | The Open Road to Mecca / El camino abierto hacia La Meca | 630 CE; Hunayn andTaif reported inaftermath | mecca | civilian-provision-under-entry |
| 14 / 14-witness-and-transition-records-medina | A Community without Its Messenger / Una comunidad sin su mensajero | 632 CE | medina | witness-and-transition-records |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.71,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 0.82,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 0.95,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## act-3: Roads Beyond Arabia / Caminos más allá de Arabia

Historical year band: [632, 638]. Sucesión y campañas; retirada también es misión legítima y no puede ganar una derrota histórica.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 15 / 15-disputed-tax-and-provincial-records-medina | Dispatches from a Divided Peninsula / Despachos desde una península dividida | 632–634 CE; campaigns reported off-map | medina | disputed-tax-and-provincial-records |
| 16 / 02-the-roads-of-yamama | The Roads of Yamama / Los caminos de Yamama | 632–633 CE probable | yamama | finite-field-supply-and-refuge |
| 17 / 17-finite-river-withdrawal-kufa-euphrates | The Bridge That Could Not Hold / El puente que no pudo resistir | October634 CE approximate | kufa-euphrates | finite-river-withdrawal |
| 18 / 18-surrender-and-civilian-records-damascus | The Gates of Damascus / Las puertas de Damasco | 635 CE conventional; terms traditions compared | damascus | surrender-and-civilian-records |
| 19 / 03-the-edge-of-the-river | The Edge of the River / El borde del río | 636 CE | yarmuk | ravine-battle-and-supply |
| 20 / 04-fields-of-the-sawad | Fields of the Sawad / Campos del Sawad | 634/635–637/638 CE; conventional636/637 | qadisiyya | finite-marsh-battle-and-relief |
| 21 / 21-finite-river-crossing-and-civilian-records-ctesiphon | The Court beyond the Tigris / La corte más allá del Tigris | 637 CE conventional; Nihavand later reported | ctesiphon | finite-river-crossing-and-civilian-records |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.79,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 0.88,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 1.0,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## act-4: Rivers and New Ledgers / Ríos y nuevos registros

Historical year band: [637, 649]. Egipto, Iraq y regiones vecinas con capitulaciones y convivencia local diferenciadas, sin fronteras modernas falsas.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 22 / 22-property-and-surrender-records-jerusalem | Terms beside the Old Walls / Condiciones junto a las murallas antiguas | 637/638 CE; capitulation chronology qualified | jerusalem | property-and-surrender-records |
| 23 / 23-peaceful-supply-and-record-reception-antioch | The Road after the Truce / El camino después de la tregua | 638 CE; cited source reports no armed resistance | antioch | peaceful-supply-and-record-reception |
| 24 / 05-a-camp-beside-the-nile | A Camp beside the Nile / Un campamento junto al Nilo | 641–642 CE; precedingcampaign639–642 | fustat | camp-and-river-supply |
| 25 / 25-bounded-harbour-withdrawal-and-receipts-alexandria | Letters from the Alexandrian Harbour / Cartas desde el puerto alejandrino | 641/642 CE traditional | alexandria | bounded-harbour-withdrawal-and-receipts |
| 26 / 26-administrative-transition-and-care-medina | Another Seal in Medina / Otro sello en Medina | 644 CE | medina | administrative-transition-and-care |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.87,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 0.94,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 1.05,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## act-5: A Horizon Divided / Un horizonte dividido

Historical year band: [651, 656]. Cambios imperiales y nuevas rutas navales culminan en crisis deMedina; la continuidad invita a First Fitna.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 27 / 27-finite-coastal-expedition-and-supply-cyprus | The Island beyond the Horizon / La isla más allá del horizonte | 649 CE conventional | cyprus | finite-coastal-expedition-and-supply |
| 28 / 28-civilian-refuge-and-source-comparison-merv | The Last Dispatch from Marw / El último despacho desde Marw | 651/652 CE; death reported, not an assassination objective | merv | civilian-refuge-and-source-comparison |
| 29 / 29-finite-naval-withdrawal-and-care-finike | Masts off the Lycian Shore / Mástiles frente a la costa licia | 654–655 CE; conversion variants | finike | finite-naval-withdrawal-and-care |
| 30 / 30-civilian-records-and-final-perspective-medina | The House behind the Dispatches / La casa detrás de los despachos | mid656 CE | medina | civilian-records-and-final-perspective |

The proposed act curve is a calibration hypothesis. It cannot add fictional military opposition to a peaceful event or change a documented outcome.

```json
{
  "easy": {
    "militaryPressureMultiplier": 0.95,
    "logisticsWindowMultiplier": 1.7,
    "recoveryBudgetMultiplier": 1.5
  },
  "standard": {
    "militaryPressureMultiplier": 1.0,
    "logisticsWindowMultiplier": 1.3,
    "recoveryBudgetMultiplier": 1.25
  },
  "hard": {
    "militaryPressureMultiplier": 1.1,
    "logisticsWindowMultiplier": 1.0,
    "recoveryBudgetMultiplier": 1.0
  },
  "interpretation": "estimated curve applied to an authored event-specific base; military multiplier applies only when the episode has military pressure; never introduces an enemy into a peaceful event; explicit integer episode budgets override rounded curve",
  "qaStatus": "pending cohort calibration"
}
```

## Episode source and knowledge ledger

### 1. The Mountain in the Remembered Story

[Candidate source](https://assets.cambridge.org/97805217/13726/excerpt/9780521713726_excerpt.pdf): Jonathan E. Brockopp (ed.), The Cambridge Companion to Muhammad, Introduction, excerpt p. 4 / PDF lines 128–149: the account places meditation outside Mecca in 610 and frames the revelation and Gabriel as the Muslim narrative; it dates the Meccan period 610–622.

Research candidate (not yet approved narration): Islamic biographical tradition places Muhammad's first revelatory experience around this year. Historical reporting can document that this is the tradition, not establish an angelic visitation or revelation as an objective event.

The date and setting are reported through later religious biography. Phrase as 'tradition dates/recounts'; do not narrate revelation, divine speech, or supernatural claims as independently verified fact.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 2. Voices among the Market Stalls

[Candidate source](https://www.cambridge.org/highereducation/books/the-formation-of-islam/0C58C7DC69FC4FFE20933C00B54D839F/the-origins-of-the-muslim-community/86DD5D5461286D6EA3B6EB4B9A120B5E): Gerald R. Hawting, The Formation of Islam, chapter “The Origins of the Muslim Community,” lines 279–282: explicitly situates the early prophetic career in the Muslim narrative and the origins of the community in Arabia. Compare Brockopp, Introduction, pp. 4–5, which notes uncertainty over who first joined Muhammad's intimate circle (PDF lines 471–480).

Research candidate (not yet approved narration): A small circle of followers formed around Muhammad's preaching in Mecca; the exact chronology and first adherents are disputed in the transmitted accounts.

The Cambridge chapter is an overview and explicitly attributes its account to Muslim origin narratives; it supports a cautious broad milestone, not a precise year, headcount, or fully settled institutional community.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 3. A Passage across the Red Sea

[Candidate source](https://api.pageplace.de/preview/DT0400.9781139798792_A23868983/preview-9781139798792_A23868983.pdf): Jonathan E. Brockopp (ed.), The Cambridge Companion to Muhammad, Introduction, pp. 7–8 / PDF lines 496–502: describes emigration to Christian Abyssinia as part of the traditional evidence for increasing conflict and notes that the tradition preserves accounts of hardship.

Research candidate (not yet approved narration): Some early followers are reported to have emigrated from Mecca to the Christian kingdom of Aksum/Abyssinia amid worsening hostility.

The consulted scholarly passage confirms the episode but does not establish 615 as an exact date. The motive, group size, routes, and sequence are known through later Muslim reports; avoid precise numbers and dramatized speeches.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 4. The Houses under the Boycott

[Candidate source](https://api.pageplace.de/preview/DT0400.9781139798792_A23868983/preview-9781139798792_A23868983.pdf): Brockopp (ed.), The Cambridge Companion to Muhammad, Introduction, pp. 7–8 / PDF lines 496–502: identifies a boycott against Muhammad's clan and explicitly frames suffering accounts as tradition.

Research candidate (not yet approved narration): Later Muslim accounts describe a social and commercial boycott against Muhammad's clan, which continued protecting him; Cambridge's scholarly synthesis identifies a boycott against his clan but does not certify all later details of its duration or terms.

Use 'later accounts report' and avoid asserting the exact 616–619 span, specific written pact details, or the valley's precise archaeological location as settled facts; those details are not established by the consulted passage.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 5. The First Promise at Aqaba

[Candidate source](https://escholarship.org/uc/item/87q494b4): Shuayb, dissertation, Aqaba pledges discussion: the next year's group is described as twelve men, including Aws and Khazraj members, with Mus'ab ibn Umayr sent to Yathrib; source labels the first two pledge traditions and their sequence.

Research candidate (not yet approved narration): A second reported Aqaba pledge involved a larger group from Yathrib; traditional accounts say Muhammad sent Mus'ab ibn Umayr to teach the new adherents there.

Raw candidate calls this second pledge incorrectly. Numbering and transmitted chronology require attribution; neither revelation nor divine causation is agnostic-narrator fact.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Traditional chronology places the first Aqaba pledge in621and Musab’s subsequent mission to Yathrib; the second pledge belongs to622.

ES: La cronología tradicional sitúa la primera promesa de Aqaba en621y la misión posterior de Musab a Yathrib; la segunda promesa corresponde a622.

### 6. A Road Promised to Strangers

[Candidate source](https://escholarship.org/uc/item/87q494b4): Shuayb, dissertation, Aqaba pledges discussion: describes the next Hajj-season gathering as a group of roughly seventy Medinans and notes that scholars differ on whether pledge traditions should be counted as two or three.

Research candidate (not yet approved narration): A further reported agreement at Aqaba connected the Yathrib group with a commitment to receive and protect Muhammad and his followers; its precise form and numbering vary across accounts and scholarship.

Use the conventional label only with an attribution such as 'the pledge known in the traditional chronology as the second Aqaba pledge.' Its details are transmitted reports, not an independently preserved treaty text.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 7. The Oasis Road

[Candidate source](https://www.iranicaonline.org/articles/chronology-of-iranian-history-part-1/): “Chronology…” entry 622; “Calendars,” Iranica (https://www.iranicaonline.org/articles/calendars/)

Research candidate (not yet approved narration): Muhammad emigra de La Meca a Medina; el año de la Hégira se convierte luego en punto de partida del calendario islámico.

La cronología islámica se fijó después; no asignar al viaje un único día gregoriano sin precisar fuente.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 8. Water before the First Battle

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Poonawala, “Ali: Life,” sección sobre expediciones y referencia a Ibn Hisham/Waqidi

Research candidate (not yet approved narration): Batalla de Badr, uno de los primeros enfrentamientos entre la comunidad de Medina y La Meca.

El artículo resume tradiciones biográficas posteriores; detalles heroicos de Ali son legendarios.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 9. Below the Broken Ridge

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): “Ali: Life,” pasaje sobre defensa en Uhud y bibliografía de Ibn Hisham/Waqidi

Research candidate (not yet approved narration): Batalla de Uhud.

Resumen de tradición biográfica; cifras no verificadas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 10. The Ditch before the Oasis

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): “Ali: Life,” sección de expediciones; referencias a Ibn Hisham

Research candidate (not yet approved narration): Defensa de Medina en la llamada batalla del Foso/Trinchera.

La fuente consultada menciona actividad militar; fecha convencional.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 11. A Truce at the Road's End

[Candidate source](https://islamansiklopedisi.org.tr/hudeybiye-antlasmasi): TDV İslâm Ansiklopedisi, “Hudeybiye Antlaşması,” pasajes sobre la salida desde Medina para la ʿumra y la negociación del acuerdo (6/628); artículo sitúa Hudaybiyya al oeste de La Meca.

Research candidate (not yet approved narration): Acuerdo de Hudaybiyya entre Muhammad y representantes de Quraysh.

Fecha gregoriana aproximada; fuente académica enciclopédica moderna que cita estudios de Hawting y Görke. El tratado no debe convertirse en cita literal de sus participantes.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 12. The Forts among the Palms

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): “Ali: Life,” referencias a Ibn Hisham II, pp. 349–350; Waqidi

Research candidate (not yet approved narration): Toma de Khaybar tras campaña contra los oasis fortificados.

Relatos de hazañas individuales no tomar al pie de la letra.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 13. The Open Road to Mecca

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” pasaje sobre caída de La Meca en 8/630

Research candidate (not yet approved narration): Las fuerzas de Muhammad entran en La Meca.

Artículo centrado en Irán, resumen contextual.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 14. A Community without Its Messenger

[Candidate source](https://www.iranicaonline.org/articles/chronology-of-iranian-history-part-1/): “Chronology…” entry 632

Research candidate (not yet approved narration): Muhammad muere y comienza la disputa política sobre su sucesión.

No convertir ninguna tradición sucesoria confesional en voz neutral.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 15. Dispatches from a Divided Peninsula

[Candidate source](https://www.iranicaonline.org/articles/chronology-of-iranian-history-part-1/): “Chronology…”; “Islam in Iran XI. Jihad in Islam” (https://www.iranicaonline.org/articles/islam-in-iran-xi-jihad-in-islam/), apartado inicial

Research candidate (not yet approved narration): Abu Bakr ocupa el califato y se enfrenta a movimientos de oposición y rechazo tributario (guerras Ridda).

La categoría “apostasía” es una interpretación de fuentes del bando vencedor; incluir también resistencia política/fiscal.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 16. The Roads of Yamama

[Candidate source](https://www.iranicaonline.org/articles/chronology-of-iranian-history-part-1/): “Chronology…” no detalla Yamama; fuentes tardías de Ridda referidas por “Islam in Iran XI”

Research candidate (not yet approved narration): Campaña de Yamama contra Musaylima, dentro de las guerras Ridda.

Esta entrada se basa en cronología estándar secundaria y requiere revisión de una fuente específica antes de fijar hito narrativo; fecha aproximada.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 17. The Bridge That Could Not Hold

[Candidate source](https://www.iranicaonline.org/articles/arab-ii/): “Arab ii,” episodio de la batalla del puente (Shaban 13/Oct 634)

Research candidate (not yet approved narration): Derrota musulmana en la batalla del Puente.

Lugar/táctica y conversión de fecha son aproximados.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 18. The Gates of Damascus

[Candidate source](https://www.iranicaonline.org/articles/chronology-of-iranian-history-part-1/): “Chronology…” entry 635, capture of Damascus

Research candidate (not yet approved narration): Damasco pasa a manos de ejércitos árabes.

La cronología general no describe términos de capitulación.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 19. The Edge of the River

[Candidate source](https://sourcebooks.web.fordham.edu/source/yarmuk.asp): Al-Baladhuri, “The Battle of Yarmuk,” relato de batalla

Research candidate (not yet approved narration): Batalla de Yarmuk contra el Imperio bizantino.

Relato historiográfico posterior; cifras y secuencia de maniobras tienen incertidumbre.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 20. Fields of the Sawad

[Candidate source](https://www.iranicaonline.org/articles/qadesiya-battle/): Lewental, “Qādesiya, Battle of,” párrs. iniciales

Research candidate (not yet approved narration): Batalla de Qādesiya derrota fuerzas sasánidas y abre avance hacia Iraq central.

Fecha, número de tropas y localización exacta son inciertos; propuestas de 634/35 a 637/38.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 21. The Court beyond the Tigris

[Candidate source](https://www.iranicaonline.org/articles/ctesiphon/): “Ctesiphon,” párrafo sobre conquista de marzo 637

Research candidate (not yet approved narration): Ctesifonte/Mada’in es tomada; la familia real sasánida y la corte se retiran.

Las crónicas describen botín con motivos literarios; el hecho de la toma tiene mejor respaldo.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 22. Terms beside the Old Walls

[Candidate source](https://www.cambridge.org/core/books/abs/christian-communities-of-palestine-from-byzantine-to-islamic-rule/islamic-conquest-the-mid630s-to-640/75A757E519D6EF48BD198F3BDBAFADC3): Robert Schick, “The Islamic Conquest,” summary: “Jerusalem arranged terms of surrender, perhaps in 17/638.”

Research candidate (not yet approved narration): Jerusalem arranges terms of surrender to Muslim forces.

The scholar explicitly marks the date as probable; traditions also place the surrender in 637.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 23. The Road after the Truce

[Candidate source](https://almuslih.org/wp-content/uploads/Library/Kaegi%2C%20W%20-%20Byzantium.pdf): Walter E. Kaegi, Byzantium and the Early Islamic Conquests (1992), p. 158: passage on the 638 occupation of Antioch and other northern Syrian cities after the truce.

Research candidate (not yet approved narration): After the northern Syrian truce expired, Muslim forces occupied Antioch; Kaegi reports no armed resistance at the city.

Year and sequence are supported; no exact day is given. The passage describes occupation without armed resistance, not a battle at Antioch.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 24. A Camp beside the Nile

[Candidate source](https://sourcebooks.web.fordham.edu/source/642Egypt-conq2.asp): “Accounts of the Arab Conquest of Egypt,” secciones sobre fortress and capitulation

Research candidate (not yet approved narration): Campaña árabe en Egipto bajo Amr b. al-As; Fustat se establece junto a la fortaleza de Babilonia.

Narraciones de al-Baladhuri y patriarcas son posteriores y divergen en secuencia.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 25. Letters from the Alexandrian Harbour

[Candidate source](https://sourcebooks.web.fordham.edu/source/642Egypt-conq2.asp): Misma selección, pasaje de capitulación de Alejandría

Research candidate (not yet approved narration): Alejandría capitula tras la campaña egipcia.

Fecha exacta y términos de tratado varían entre cronistas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 26. Another Seal in Medina

[Candidate source](https://www.iranicaonline.org/articles/chronology-of-iranian-history-part-1/): “Chronology…” entries 644

Research candidate (not yet approved narration): Omar es asesinado y Uthman accede al califato.

La cronología ofrece una síntesis; autoría/participación en el asesinato requiere fuente adicional.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 27. The Island beyond the Horizon

[Candidate source](https://www.cambridge.org/core/journals/byzantine-and-modern-greek-studies/article/abs/sebeos-account-of-an-arab-attack-on-constantinople-in-654/B067CB79A2ADF5B9A47165D72E00737D): Article note 40: sources and the basilica inscription at Soli attest first attacks dated 649 and 650; location of any garrison is unknown.

Research candidate (not yet approved narration): An Arab naval expedition attacks Cyprus during Uthman’s caliphate.

The article discusses conflict in the source chronology; precise landing/campaign details and later occupation are uncertain.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 28. The Last Dispatch from Marw

[Candidate source](https://www.iranicaonline.org/articles/khorasan-iv-the-arab-conquest-and-omayyad-period/): “Khorasan iv,” resumen inicial cita Ṭabari para asesinato en 31/652; “Chronology…” da 651

Research candidate (not yet approved narration): Yazdegerd III es asesinado en Marw; fin de la monarquía sasánida.

Fuentes difieren 651 vs. 652; evitar fecha diaria.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 29. Masts off the Lycian Shore

[Candidate source](https://www.cambridge.org/core/journals/byzantine-and-modern-greek-studies/article/abs/sebeos-account-of-an-arab-attack-on-constantinople-in-654/B067CB79A2ADF5B9A47165D72E00737D): Article notes 35, 41–42: al-Tabari dates the Battle of the Masts to 34 AH; the article discusses competing accounts and dates.

Research candidate (not yet approved narration): Battle of Phoenix, also called the Battle of the Masts, pits the Arab fleet against Byzantine naval forces.

The date spans 654–655 in sources; fleet totals and strategic outcome are contested, and the source cautions that several reports conflict.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 30. The House behind the Dispatches

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): “Ali: Life,” párrs. 52–60

Research candidate (not yet approved narration): Oposición provincial llega a Medina y Uthman muere durante el sitio de su residencia.

Circunstancias y culpabilidad disputadas; evento marca fin del rango de campaña.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending
