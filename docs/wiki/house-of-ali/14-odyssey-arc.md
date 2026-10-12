# The River Remembers / El río recuerda

`house-of-ali` · CDF-I03 · 30 selected episodes · source locale `en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

```json
{
  "editorial": {
    "campaignTitle": {
      "en": "The River Remembers",
      "es-ES": "El río recuerda"
    },
    "publicId": "CDF-I03",
    "internalName": "CDF_HouseOfAli",
    "sourceLocale": "en",
    "targetEpisodeCount": 30,
    "narratorId": "dina-potter",
    "personaLens": {
      "en": "Hands, clay, family stories and the weight of water",
      "es-ES": "Manos, barro, historias familiares y el peso del agua"
    },
    "deliveryTone": {
      "en": "domestic humour yielding to restrained mourning",
      "es-ES": "humor doméstico que cede a duelo sobrio"
    },
    "sequence": [
      {
        "speaker": "collection-narrator",
        "mode": "sober source-qualified historical fact",
        "causePolicy": "attribute motives, miracles and sectarian judgements to their sources; no single moral or theological verdict"
      },
      {
        "speaker": "dina-potter",
        "mode": "fictional personal interpretation with explicit witness basis"
      }
    ],
    "baselineSemanticIdsPreserved": [
      "01-the-kufan-hearth",
      "02-a-cup-at-siffin",
      "03-the-sealed-copy",
      "04-the-water-that-remains"
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
    "recommendedPrevious": [
      {
        "campaignId": "first-fitna",
        "route": "ali-perspective"
      }
    ],
    "nextRoutes": [
      {
        "id": "completed",
        "key": "progress.house-of-ali.completed",
        "next": null
      }
    ],
    "chronologyWarning": "Any predecessor-dependent campaign remains independently playable; show recommendation and recap, preserve all route keys, and disclose overlap when changing perspective.",
    "terminalScreenRule": "show successor English/Spanish title plus public ID for the chosen route; no automatic launching and no requirement lock",
    "proceedWithoutPredecessor": true
  }
}
```

Only the final expanded episode may complete this campaign or present the successor recommendation. Former baseline finales become intermediate episodes when later episodes exist. Preserve every existing semantic scenario ID; display order is a separate field.

## act-1: Clay in an Uneasy City / Barro en una ciudad inquieta

Historical year band: [656, 656]. Dina niña recibe historias de su tío; hogares deKufa y redes políticas no sustituyen fuentes históricas.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 1 / 01-witness-and-transition-records-medina | A Promise in Medina / Una promesa en Medina | 656 CE | medina | witness-and-transition-records |
| 2 / 02-civilian-refuge-and-petition-basra | The Doors before the Battle / Las puertas antes de la batalla | 656 CE | basra | civilian-refuge-and-petition |
| 3 / 03-finite-battle-withdrawal-and-care-basra | The Dust beyond Basra / El polvo más allá de Basora | 656 CE | basra | finite-battle-withdrawal-and-care |
| 4 / 01-the-kufan-hearth | The Kufan Hearth / El hogar de Kufa | 656/657 CE | kufa | household-reception-and-workshop-supply |
| 5 / 05-off-map-dispatch-and-source-comparison-fustat | The Egyptian Letter / La carta egipcia | c.656–657 CE; Kharbitareports, settlementnotfalselylocated | fustat | off-map-dispatch-and-source-comparison |

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

## act-2: Two Banks, One Cup / Dos riberas, una copa

Historical year band: [657, 657]. Siffin desde cuidado y abastecimiento; mismoscarros y registros reales, sin prodigios de curación.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 6 / 02-a-cup-at-siffin | A Cup at Siffin / Una taza en Siffin | 657 CE | siffin | finite-water-and-care-corridor |
| 7 / 07-ceasefire-withdrawal-and-records-siffin | The Leaves above the Spears / Las hojas sobre las lanzas | 657 CE; attributedchronicleaccount | siffin | ceasefire-withdrawal-and-records |
| 8 / 08-paired-protocol-delivery-siffin | The Reply beside the Water / La respuesta junto al agua | 657 CE | siffin | paired-protocol-delivery |
| 9 / 09-witness-and-text-comparison-kufa | The Names in the Copied Terms / Los nombres en las condiciones copiadas | 657/658 CE | kufa | witness-and-text-comparison |
| 10 / 10-voluntary-household-relocation-harura | A House on the Harura Road / Una casa en el camino de Harura | 657/658 CE; Nahrawanlateroff-map | harura | voluntary-household-relocation |

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

## act-3: A Seal and a Farewell / Un sello y una despedida

Historical year band: [658, 661]. Desacuerdos, muerte deAli y Hasan; no confundir rendición decontrol político con renuncia a toda identidad religiosa.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 11 / 11-finite-civilian-withdrawal-and-care-nahrawan | Beyond the Canal's Silence / Más allá del silencio del canal | 658 CE | nahrawan | finite-civilian-withdrawal-and-care |
| 12 / 12-delegation-and-source-comparison-adhruh | Reports from the Empty Seat / Partes desde el asiento vacío | 659 CE | adhruh | delegation-and-source-comparison |
| 13 / 03-the-sealed-copy | The Seal after Ali / El sello después de Alí | 661 CE | kufa | administrative-transition-and-copying |
| 14 / 14-paired-protocol-and-negotiation-kufa | The Letter with Room for Terms / La carta con espacio para condiciones | 661 CE | kufa | paired-protocol-and-negotiation |
| 15 / 15-finite-distribution-and-receipts-kufa | The Oath That Changed the Road / El juramento que cambió el camino | August661 approximate | kufa | finite-distribution-and-receipts |
| 16 / 16-ceremony-and-record-preservation-kufa | The Assembly's Last Account / La última cuenta de la asamblea | 661 CE; publictransferattributed | kufa | ceremony-and-record-preservation |

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

## act-4: Letters Without a Safe Road / Cartas sin camino seguro

Historical year band: [661, 680]. Muerte deHasan con año discutido, sucesión deYazid y cartas deKufa; la alfarera sigue a familias ficticias distintas del círculo histórico.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 17 / 17-returning-household-and-workshop-supply-medina | A Household Returned to Medina / Un hogar que volvió a Medina | 661 CE; separatelocalreturn, notsecondtransfer | medina | returning-household-and-workshop-supply |
| 18 / 18-mourning-and-witness-preservation-medina | The Record after Hasan / El registro después de Hasan | 669/670 CE; disputeddateandpoisoningclaims | medina | mourning-and-witness-preservation |
| 19 / 19-off-map-succession-dispatch-medina | A New Name from Damascus / Un nombre nuevo desde Damasco | 680 CE; YazidsuccessionDamascusreported | medina | off-map-succession-dispatch |
| 20 / 20-finite-household-departure-medina | The Road out of Medina / El camino de salida de Medina | 680 CE; historicalfiguresoff-map | medina | finite-household-departure |
| 21 / 21-two-way-correspondence-and-witnesses-mecca | Letters Reaching Mecca / Cartas que alcanzaban La Meca | June680 approximate; calendarconversionqualified | mecca | two-way-correspondence-and-witnesses |
| 22 / 22-delegation-reception-and-support-records-kufa | The Emissary in Kufa / El emisario en Kufa | 680 CE | kufa | delegation-reception-and-support-records |
| 23 / 23-civilian-refuge-and-record-extraction-kufa | The City after the Arrests / La ciudad después de los arrestos | 680 CE; executionsreportednotplayergoal | kufa | civilian-refuge-and-record-extraction |

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

## act-5: The River Remembers / El río recuerda

Historical year band: [680, 680]. Rutas cerradas yKarbala; la misión deauxilio no evita la tragedia ni rescata ficticiamente a figuras cuyo destino se conoce.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 24 / 24-finite-caravan-consignments-mecca | Before the News Could Catch the Road / Antes de que las noticias alcanzasen el camino | September680 approximate; exitdatevariants | mecca | finite-caravan-consignments |
| 25 / 25-bounded-civilian-route-and-care-qadisiyya | The Closed Roads of Qadisiyya / Los caminos cerrados de Qadisiyya | 680 CE | qadisiyya | bounded-civilian-route-and-care |
| 26 / 26-source-comparison-and-voluntary-return-zubala | A Dispatch at Zubala / Un despacho en Zubala | 680 CE; Thalabiyyaseparatepriorreport, notsameplace | zubala | source-comparison-and-voluntary-return |
| 27 / 27-off-map-dispatch-and-route-replanning-qadisiyya | Where the Road Turned Away / Donde el camino se desvió | 680 CE; DhuHusamencounterreported, exactsiteunresolved | qadisiyya | off-map-dispatch-and-route-replanning |
| 28 / 28-finite-camp-and-household-provision-karbala | The Camp on the Open Plain / El campamento en la llanura abierta | earlyOctober680 conventional | karbala | finite-camp-and-household-provision |
| 29 / 29-separate-reception-and-record-escort-karbala | Messages before the River Closed / Mensajes antes de que se cerrara el río | earlyOctober680 conventional | karbala | separate-reception-and-record-escort |
| 30 / 04-the-water-that-remains | The Water That Remains / El agua que permanece | October680 conventional; battle262historicaloutcomeinfinale | karbala | bounded-water-and-civilian-extraction |

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

### 1. A Promise in Medina

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 60; invitation and acceptance

Research candidate (not yet approved narration): Ali acepta el califato tras vacilar varios días.

No fijar día exacto.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 2. The Doors before the Battle

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 66; occupation of Basra

Research candidate (not yet approved narration): Las fuerzas de oposición ocupan Basra.

Informe sumario, sin cifras fiables.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 3. The Dust beyond Basra

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 67; Battle of the Camel

Research candidate (not yet approved narration): Batalla del Camello.

Pelea entre musulmanes; no representar civiles/unidades religiosas como blancos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 4. The Kufan Hearth

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 68; move to Kufa

Research candidate (not yet approved narration): El centro político de Ali se establece en Kufa.

Fecha convencional 657; proceso, no fundación urbana.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 5. The Egyptian Letter

[Candidate source](https://fliphtml5.com/qzpe/qric/History_of_Al_Tabari_-_Vol_16/): Al-Ṭabarī, History, vol. 16, events of year 36, account of the Egyptian governor and the Kharbita opposition; compare vol. 17, “Events of the Year 38,” where the 658 loss of Egypt and death of Muḥammad b. Abī Bakr is reported: https://www.jstor.org/stable/jj.18252726.8.

Research candidate (not yet approved narration): Opponents based at Kharbita resist ʿAlī’s governor in Egypt; expeditions sent by Muḥammad ibn Abī Bakr fail, weakening his hold on the province.

The accounts are later transmitted chronicles and give partisan framings. This candidate is specifically the local resistance at Kharbita, not the later capture of Fustat or the killing of Muḥammad; keep those later events separate and do not imply that the killing happened at Kharbita.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 6. A Cup at Siffin

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 73; armies meet at Siffin

Research candidate (not yet approved narration): Los ejércitos se concentran en la llanura de Siffin.

Ubicación regional; no inferir coordenadas del campamento.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 7. The Leaves above the Spears

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 74–76; maṣāḥef on spearheads

Research candidate (not yet approved narration): Se exhiben folios/códices coránicos en lanzas para detener la batalla, según las crónicas.

Episodio transmitido por historiografía posterior; evitar recrear objetos o motivaciones como certeza.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 8. The Reply beside the Water

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 75–80; arbitration

Research candidate (not yet approved narration): El campamento de Ali acepta someter la disputa a arbitraje.

Decisión atribuida a presión interna del ejército.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 9. The Names in the Copied Terms

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 78–81; dispute over arbiter

Research candidate (not yet approved narration): La elección de Abu Musa como árbitro suscita divisiones en el campamento de Ali.

Nombres y motivaciones tal como aparecen en tradición narrativa.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 10. A House on the Harura Road

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 82–85; secession

Research candidate (not yet approved narration): Un grupo contrario al arbitraje se aparta en Harura y luego se dirige a Nahrawan.

La identidad jariyí se desarrolla en el conflicto; evitar retroproyectar secta consolidada.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 11. Beyond the Canal's Silence

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 88; Nahrawan

Research candidate (not yet approved narration): Campaña contra el grupo disidente y batalla de Nahrawan.

Fecha convencional; cifras de muertos y detalles son dudosos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 12. Reports from the Empty Seat

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 89; arbiters and notables meet

Research candidate (not yet approved narration): Nueva reunión de arbitraje en Adhruh, sin delegados de Ali según Poonawala.

Fecha tradicional y resultado controvertido.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 13. The Seal after Ali

[Candidate source](https://www.iranicaonline.org/articles/hasan-b-ali/): Secciones iniciales del artículo sobre califato de Hasan

Research candidate (not yet approved narration): Hasan asume el control de la comunidad en Iraq tras la muerte de Ali.

Fecha de proclamación suele expresarse 661, pero puede caer en 40/41 AH.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 14. The Letter with Room for Terms

[Candidate source](https://www.iranicaonline.org/articles/hasan-b-ali/): PDF pp. 2–3, párrs. 96–110

Research candidate (not yet approved narration): Muawiya envía propuestas de pacto a Hasan; una carta con sello permite a Hasan proponer condiciones.

Términos concretos son transmitidos en fuentes posteriores y difieren entre cronistas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 15. The Oath That Changed the Road

[Candidate source](https://www.iranicaonline.org/articles/hasan-b-ali/): PDF p. 3, párr. 111

Research candidate (not yet approved narration): Hasan cede el control de Iraq a Muawiya tras siete meses.

La fecha gregoriana/lunar puede variar por conversión.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 16. The Assembly's Last Account

[Candidate source](https://www.iranicaonline.org/articles/hasan-b-ali/): PDF pp. 3–4, párrs. 113–127

Research candidate (not yet approved narration): Ceremonia pública de transferencia en Kufa; Hasan regresa con su familia a Medina.

Madelung cita a Baladhuri; el discurso atribuido a Muawiya no es transcripción contemporánea.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 17. A Household Returned to Medina

[Candidate source](https://www.iranicaonline.org/articles/hasan-b-ali/): PDF pp. 3–4, párrs. 113–127

Research candidate (not yet approved narration): Ceremonia pública de transferencia en Kufa; Hasan regresa con su familia a Medina.

Madelung cita a Baladhuri; el discurso atribuido a Muawiya no es transcripción contemporánea.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 18. The Record after Hasan

[Candidate source](https://www.iranicaonline.org/articles/hasan-b-ali/): Sección final sobre muerte y entierro

Research candidate (not yet approved narration): Hasan muere en Medina; algunas tradiciones atribuyen la muerte a envenenamiento.

Envenenamiento no comprobado; usar “según algunas fuentes” si se incluye.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 19. A New Name from Damascus

[Candidate source](https://www.iranicaonline.org/articles/asura/): Entrada ʿĀšūrāʾ; opening lines

Research candidate (not yet approved narration): Muawiya muere y Yazid asume el califato mediante sucesión designada.

La fecha de muerte se expresa como primavera de 680; interpretación del mecanismo político debe calificarse.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 20. The Road out of Medina

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párrs. 53–56; refusal and arrival in Mecca

Research candidate (not yet approved narration): Husayn rehúsa jurar lealtad a Yazid y viaja de Medina a La Meca.

Fechas de salida varían entre informes.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 21. Letters Reaching Mecca

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párrs. 57–58; Kufan letters

Research candidate (not yet approved narration): Llegan a La Meca las primeras cartas de líderes de Kufa invitando a Husayn.

Fechas convertidas aproximadas; “Shiʿa” aquí describe partidarios de Ali, no secta contemporánea uniforme.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 22. The Emissary in Kufa

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párr. 64; mission of Muslim b. Aqil

Research candidate (not yet approved narration): Muslim b. Aqil viaja a Kufa como emisario de Husayn y obtiene apoyo inicial reportado.

Cifra de 18,000 es tradición cronística y no censo.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 23. The City after the Arrests

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párrs. 64, 71–72

Research candidate (not yet approved narration): Yazid sustituye al gobernador de Kufa por Ubayd Allah b. Ziyad; Muslim b. Aqil y Hani b. Urwa son ejecutados.

Cronología aproximada; detalles son narración medieval.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 24. Before the News Could Catch the Road

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párr. 66; departure

Research candidate (not yet approved narration): Husayn deja La Meca rumbo a Iraq antes de recibir noticias completas de Kufa.

La propia fuente da dos fechas posibles.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 25. The Closed Roads of Qadisiyya

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párr. 71; roadblock order

Research candidate (not yet approved narration): Las fuerzas de Ubayd Allah bloquean rutas entre Hijaz e Iraq en Qadisiyya.

No confundir esta Qadisiyya de 680 con la batalla del siglo VII temprano.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 26. A Dispatch at Zubala

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párrs. 71–73

Research candidate (not yet approved narration): Husayn recibe noticia de la ejecución de Muslim b. Aqil y de que el levantamiento kufano fracasó.

La secuencia de lugares procede de itinerario narrado; identificaciones modernas no exactas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 27. Where the Road Turned Away

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párrs. 74–77

Research candidate (not yet approved narration): Husayn se encuentra con la tropa de Hurr; las rutas hacia Kufa y Medina quedan cerradas.

Ubicaciones de la ruta se identifican tradicionalmente; no fijar coordenadas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 28. The Camp on the Open Plain

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párr. 78; camp established

Research candidate (not yet approved narration): Husayn establece campamento en la llanura de Karbala.

Conversión gregoriana aproximada; ciudad actual no equivale al punto exacto del campo.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 29. Messages before the River Closed

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párr. 79; army arrives

Research candidate (not yet approved narration): Llega el ejército de Umar b. Saʿd, enviado por el gobernador de Kufa.

Cifra de 4,000 según tradición, no verificada.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 30. The Water That Remains

[Candidate source](https://www.iranicaonline.org/articles/hosayn-b-ali-i/): Párrs. 81–82

Research candidate (not yet approved narration): Las fuerzas de Umar b. Saʿd impiden el acceso regular al Éufrates.

Do not claim that every companion or family member died. Captivity and survival must be represented with dated source attribution; sacred inner-camp participants are not playable proxies.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Accounts describe restricted water access before Karbala. Husayn and many companions were killed, and survivors from his family were taken captive; the player’s fictional civilian task cannot prevent that outcome.

ES: Las fuentes describen restricciones de acceso al agua antes de Karbala. Husayn y muchos de sus acompañantes murieron, y supervivientes de su familia fueron capturados; la tarea civil ficticia del jugador no puede impedir ese desenlace.
