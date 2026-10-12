# The Shattered Oath / El juramento quebrado

`first-fitna` · CDF-I01 · 28 selected episodes · source locale`en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

```json
{
  "editorial": {
    "campaignTitle": {
      "en": "The Shattered Oath",
      "es-ES": "El juramento quebrado"
    },
    "publicId": "CDF-I01",
    "internalName": "CDF_FirstFitna",
    "sourceLocale": "en",
    "targetEpisodeCount": 28,
    "narratorId": "farid-field-medic",
    "personaLens": {
      "en": "Care, names of the hurt and contradictory dispatches",
      "es-ES": "Cuidados, nombres de heridos y despachos contradictorios"
    },
    "deliveryTone": {
      "en": "contained fatigue, distrust of slogans",
      "es-ES": "cansancio contenido, desconfianza de consignas"
    },
    "sequence": [
      {
        "speaker": "collection-narrator",
        "mode": "sober source-qualified historical fact",
        "causePolicy": "attribute motives, miracles and sectarian judgements to their sources; no single moral or theological verdict"
      },
      {
        "speaker": "farid-field-medic",
        "mode": "fictional personal interpretation with explicit witness basis"
      }
    ],
    "baselineSemanticIdsPreserved": [
      "01-news-from-medina",
      "02-between-the-camps",
      "03-water-and-words",
      "04-the-canal-road",
      "05-two-archives"
    ],
    "orderingPolicy": "order is a separate integer; existing semantic IDs and public/progress IDs remain stable",
    "progressPolicy": "only the actual final odyssey episode offers terminal route write; every former last baseline mission becomes nonterminal when followed by new episodes",
    "sourceAuditStatus": "candidate chronologies reviewed for errors; individual episode historical approval pending",
    "coreMechanicPolicy": "at least four mission-core families in each odyssey; no more than two consecutive identical core families without authored reason; side-objective variety does not excuse identical main missions",
    "selectedEpisodeCount": 28,
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
        "campaignId": "first-caliphs",
        "route": "completed"
      }
    ],
    "nextRoutes": [
      {
        "id": "muawiya-perspective",
        "key": "progress.first-fitna.muawiya-perspective",
        "next": "umayyads"
      },
      {
        "id": "ali-perspective",
        "key": "progress.first-fitna.ali-perspective",
        "next": "house-of-ali"
      }
    ],
    "chronologyWarning": "Any predecessor-dependent campaign remains independently playable; show recommendation and recap, preserve all route keys, and disclose overlap when changing perspective.",
    "terminalScreenRule": "show successor English/Spanish title plus public ID for the chosen route; no automatic launching and no requirement lock",
    "proceedWithoutPredecessor": true
  }
}
```

Only the final expanded episode may complete this campaign or present the successor recommendation. Former baseline finales become intermediate episodes when later episodes exist. Preserve every existing semantic scenario ID; display order is a separate field.

## act-1: Dispatches Before the Storm / Despachos antes de la tormenta

Historical year band: [656, 656]. Oposición, asesinato y reconocimiento disputado; Farid separa relatos de facción y cuidados reales ficticios.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 1 / 01-news-from-medina | News from Medina / Noticias desde Medina | mid656 CE | medina | delegation-reception-and-household-aid |
| 2 / 02-civilian-refuge-and-record-preservation-medina | After the Sealed Door / Después de la puerta sellada | 656 CE; murder is reported, not playable | medina | civilian-refuge-and-record-preservation |
| 3 / 03-administrative-transition-medina | A Seal Accepted in Uncertainty / Un sello aceptado en la incertidumbre | 656 CE; motives attributed | medina | administrative-transition |
| 4 / 04-disputed-correspondence-mecca | The Message on the Pilgrim Road / El mensaje en el camino peregrino | 656 CE | mecca | disputed-correspondence |
| 5 / 05-rival-petition-and-witness-records-medina | Two Names in the Dispatch / Dos nombres en el despacho | 656 CE | medina | rival-petition-and-witness-records |

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

## act-2: The City Between the Camps / La ciudad entre los campamentos

Historical year band: [656, 657]. Basra y Kufa entre movilización, batalla y asistencia civil; no simplificar culpabilidad como misión a eliminar.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 6 / 06-arriving-delegation-and-supply-basra | Toward the River City / Hacia la ciudad del río | 656 CE; travelArabiaoff-map | basra | arriving-delegation-and-supply |
| 7 / 07-civilian-extraction-under-unrest-basra | The Streets between the Camps / Las calles entre los campamentos | 656 CE | basra | civilian-extraction-under-unrest |
| 8 / 02-between-the-camps | Between the Camps / Entre los campamentos | 656 CE | basra | finite-field-battle-and-care |
| 9 / 09-bounded-distribution-and-receipts-basra | Accounts after the Battle / Cuentas después de la batalla | 656 CE; distribution accounts attributed | basra | bounded-distribution-and-receipts |
| 10 / 10-camp-and-household-reception-kufa | The Quarter on the Kufa Road / El barrio en el camino de Kufa | 656/657 CE | kufa | camp-and-household-reception |
| 11 / 11-two-way-correspondence-kufa | Words across a Divided Road / Palabras sobre un camino dividido | 656–657 CE | kufa | two-way-correspondence |

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

## act-3: Water and Broken Words / Agua y palabras quebradas

Historical year band: [657, 657]. Siffin, agua, combate y arbitraje; decisiones jugables logísticas no revierten la crisis histórica.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 12 / 12-rival-claims-and-dispatch-comparison-damascus | A Reply from Damascus / Una respuesta desde Damasco | 656–657 CE | damascus | rival-claims-and-dispatch-comparison |
| 13 / 03-water-and-words | Water and Words / Agua y palabras | 657 CE; fiercefighting191integrated | siffin | finite-river-battle-and-care |
| 14 / 14-ceasefire-withdrawal-and-care-siffin | When the Fighting Was Stopped / Cuando se detuvo la lucha | 657 CE; Qur'an-folioaccount192attributed | siffin | ceasefire-withdrawal-and-care |
| 15 / 15-paired-protocol-delivery-siffin | Terms beside the River / Condiciones junto al río | 657 CE | siffin | paired-protocol-delivery |
| 16 / 16-witness-and-record-comparison-kufa | The Names Chosen for Arbitration / Los nombres elegidos para el arbitraje | 657/658 CE | kufa | witness-and-record-comparison |

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

## act-4: The Price of Arbitration / El precio del arbitraje

Historical year band: [658, 660]. Harura, Nahrawan, reuniones y pérdida de apoyos; dataciones alternativas y relatos tendenciosos visibles.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 17 / 17-voluntary-household-relocation-harura | The Road through Harura / El camino por Harura | 657/658 CE | harura | voluntary-household-relocation |
| 18 / 18-separate-delegation-logistics-dumat-al-jandal | Papers at Dumat al-Jandal / Documentos en Dumat al-Jandal | February658 approximate; Ramadan37AHaccordingPoonawala | dumat-al-jandal | separate-delegation-logistics |
| 19 / 19-disputed-correspondence-and-provision-kufa | The Reply That Would Not Settle / La respuesta que no resolvía | 658 CE | kufa | disputed-correspondence-and-provision |
| 20 / 04-the-canal-road | The Canal Road / El camino del canal | 658 CE conventional | nahrawan | finite-withdrawal-and-civilian-refuge |
| 21 / 21-civilian-record-preservation-fustat | The Egyptian Dispatch / El despacho egipcio | 658 CE; Egyptloss not660; correctionrequiresexactpassage | fustat | civilian-record-preservation |
| 22 / 22-delegate-reception-and-source-comparison-adhruh | A Seat Empty at Adhruh / Un asiento vacío en Adhruh | January659 approximate; Shaban38AHaccordingPoonawala | adhruh | delegate-reception-and-source-comparison |
| 23 / 23-bounded-rural-relief-kufa | The Farms beyond the Patrols / Las granjas más allá de las patrullas | 659–660 CE; onefictionallocalraid, remoteincursionsreported | kufa | bounded-rural-relief |

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

## act-5: The Oath That Could Not Hold / El juramento que no pudo durar

Historical year band: [661, 661]. Muerte deAli, Hasan y pacto; el final deja escoger perspectiva omeya o de la casa deAli sin declarar vencedor moral.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 24 / 24-civilian-refuge-and-dispatch-medina | News from the Hijaz Roads / Noticias desde los caminos del Hiyaz | 660 CE; BusrraidsseparatefromEgypt658 | medina | civilian-refuge-and-dispatch |
| 25 / 25-care-and-record-preservation-kufa | The Night of the Last Report / La noche del último parte | January661 approximate; woundanddeath204consolidated | kufa | care-and-record-preservation |
| 26 / 26-administrative-transition-and-household-supply-kufa | The Seal after the Loss / El sello después de la pérdida | 661 CE | kufa | administrative-transition-and-household-supply |
| 27 / 27-paired-protocol-and-bounded-negotiation-kufa | A Letter with an Open Seal / Una carta con un sello abierto | 661 CE | kufa | paired-protocol-and-bounded-negotiation |
| 28 / 05-two-archives | Two Archives beneath One Roof / Dos archivos bajo un techo | August661 approximate; RabiII41AH | kufa | archive-and-final-perspective |

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

### 1. News from Medina

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 52; provincial opposition arrives

Research candidate (not yet approved narration): Grupos provinciales de Egipto, Kufa y Basra llegan a Medina en medio del descontento contra Uthman.

Las fuentes divergen sobre actores, motivaciones y secuencia del sitio.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 2. After the Sealed Door

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 60; aftermath of Uthman’s murder

Research candidate (not yet approved narration): Uthman es asesinado; los omeyas abandonan Medina y grupos provinciales dominan la situación.

La responsabilidad individual y detalles del asesinato están disputados.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 3. A Seal Accepted in Uncertainty

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 60; invitation and acceptance

Research candidate (not yet approved narration): Ali acepta el califato tras vacilar varios días.

No fijar día exacto.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 4. The Message on the Pilgrim Road

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 63; Aisha returns to Mecca

Research candidate (not yet approved narration): Aisha regresa a La Meca y se incorpora a la oposición a Ali.

Motivación personal reportada por fuentes sesgadas, no presentar como certeza.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 5. Two Names in the Dispatch

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 64–65; departure and accusation

Research candidate (not yet approved narration): Talha y Zubayr rompen con Ali y responsabilizan a su gobierno por no procesar a los asesinos de Uthman.

Causalidad y negociación se transmiten por relatos retrospectivos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 6. Toward the River City

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 66; march to Basra

Research candidate (not yet approved narration): Talha y Zubayr avanzan hacia Basra buscando respaldo político y militar.

Ruta aproximada.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 7. The Streets between the Camps

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 66; rebels occupy Basra

Research candidate (not yet approved narration): Los rebeldes toman Basra y ocurre violencia en la ciudad.

Las cifras y el orden de incidentes son inciertos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 8. Between the Camps

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 67; Battle of the Camel

Research candidate (not yet approved narration): Batalla del Camello entre Ali y las fuerzas reunidas en torno a Aisha, Talha y Zubayr.

El nombre alude al camello de Aisha en el centro; no convertir relatos heroicos en hechos precisos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 9. Accounts after the Battle

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 68; entry into Basra and bayt al-mal

Research candidate (not yet approved narration): Ali entra en Basra y distribuye por partes iguales el tesoro público entre sus partidarios.

La fuente presenta una política atribuida a Ali; no usar como dato cuantitativo.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 10. The Quarter on the Kufa Road

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 68; move to Kufa

Research candidate (not yet approved narration): Ali se traslada a Kufa para reforzar su base frente a Muawiya.

Cronología convencional 657; el traslado fue un proceso.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 11. Words across a Divided Road

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 71; opening negotiations

Research candidate (not yet approved narration): Ali abre negociaciones con Muawiya para obtener su reconocimiento.

Correspondencia transmitida en fuentes posteriores.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 12. A Reply from Damascus

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 71–72; Muawiya’s position

Research candidate (not yet approved narration): Muawiya exige autonomía siria y reclama castigo por el asesinato de Uthman; no jura lealtad a Ali.

Explicación política transmitida por historiografía retrospectiva.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 13. Water and Words

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 73; armies meet at Siffin

Research candidate (not yet approved narration): Los ejércitos se concentran en la llanura de Siffin.

Ubicación regional; no inferir coordenadas del campamento.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 14. When the Fighting Was Stopped

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 75–77; acceptance of arbitration

Research candidate (not yet approved narration): La mayoría de la fuerza de Ali impone aceptar arbitraje; Ali detiene el combate.

Atribuciones de diálogos no son citas verificables.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 15. Terms beside the River

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 77–80; arbitration terms

Research candidate (not yet approved narration): Se acuerda que cada lado nombre un árbitro y que se use el Corán como marco.

Términos transmitidos por historiadores posteriores.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 16. The Names Chosen for Arbitration

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 78–81; dispute over arbiter

Research candidate (not yet approved narration): La elección de Abu Musa como árbitro suscita divisiones en el campamento de Ali.

Nombres y motivaciones tal como aparecen en tradición narrativa.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 17. The Road through Harura

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 82–85; secession and Harura

Research candidate (not yet approved narration): Opositores al arbitraje se separan y se reúnen en Harura.

La etiqueta jariyí se consolida retrospectivamente; no tratar como secta madura ya constituida.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 18. Papers at Dumat al-Jandal

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 86; first meeting appears to occur

Research candidate (not yet approved narration): Primera reunión de árbitros en Dumat al-Jandal según el relato citado por Poonawala.

El artículo dice “appears”; fecha gregoriana aproximada y resultado no público.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 19. The Reply That Would Not Settle

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 87; Ali protests arbitration result

Research candidate (not yet approved narration): Ali rechaza el resultado atribuido a la reunión de árbitros y trata de reunir otra fuerza.

No hubo un resultado aceptado uniformemente.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 20. The Canal Road

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 88; Nahrawan campaign

Research candidate (not yet approved narration): Ali marcha contra los disidentes reunidos en Nahrawan y vence; se producen deserciones de su ejército.

Fecha 658 convencional; cifras y detalles de la matanza dependen de tradición y son discutidos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 21. The Egyptian Dispatch

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 91; loss of Egypt and Hijaz

Research candidate (not yet approved narration): Ali pierde el control de Egipto y del Hijaz ante el avance de Muawiya.

Original candidate202combines distinct places and dates incorrectly. Use selectedClaim only after checking the exact Iranica/Tabari passage; source audit remains pending.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Ali’s administration lost Egypt in658; raids in the Hijaz in660 belong to a different phase.

ES: La administración de Alí perdió Egipto en658; las incursiones en el Hiyaz en660 corresponden a una fase distinta.

### 22. A Seat Empty at Adhruh

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párrs. 89–90; meeting at Adhruh

Research candidate (not yet approved narration): Árbitros y notables se reúnen en Adhruh; Ali no tiene representantes presentes según Poonawala.

Resultado público discrepante en las fuentes; ubicación se identifica tradicionalmente.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 23. The Farms beyond the Patrols

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 91; incursions

Research candidate (not yet approved narration): Muawiya efectúa incursiones en zonas de Iraq y Arabia.

Proceso con varios episodios; no localizable como una batalla singular.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 24. News from the Hijaz Roads

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 91; loss of Egypt and Hijaz

Research candidate (not yet approved narration): Ali pierde el control de Egipto y del Hijaz ante el avance de Muawiya.

Original candidate202combines distinct places and dates incorrectly. Use selectedClaim only after checking the exact Iranica/Tabari passage; source audit remains pending.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Busr’s incursions in the Hijaz belong to660; they are not a simultaneous conquest of Egypt, whose administration had been lost in658.

ES: Las incursiones de Busr en el Hiyaz corresponden a660; no son una conquista simultánea de Egipto, cuya administración se había perdido en658.

### 25. The Night of the Last Report

[Candidate source](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): Párr. 91; attack in mosque

Research candidate (not yet approved narration): Ali es herido por Abd al-Rahman b. Muljam mientras reza en una mezquita de Kufa.

La identidad y motivación se transmiten por fuentes medievales.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 26. The Seal after the Loss

[Candidate source](https://www.iranicaonline.org/articles/hasan-b-ali/): Secciones iniciales del artículo sobre califato de Hasan

Research candidate (not yet approved narration): Hasan asume el control de la comunidad en Iraq tras la muerte de Ali.

Fecha de proclamación suele expresarse 661, pero puede caer en 40/41 AH.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 27. A Letter with an Open Seal

[Candidate source](https://www.iranicaonline.org/articles/hasan-b-ali/): PDF pp. 2–3, párrs. 96–110

Research candidate (not yet approved narration): Muawiya envía propuestas de pacto a Hasan; una carta con sello permite a Hasan proponer condiciones.

Términos concretos son transmitidos en fuentes posteriores y difieren entre cronistas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 28. Two Archives beneath One Roof

[Candidate source](https://www.iranicaonline.org/articles/hasan-b-ali/): PDF p. 3, párr. 111

Research candidate (not yet approved narration): Hasan cede el control de Iraq a Muawiya tras siete meses.

La fecha gregoriana/lunar puede variar por conversión.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending
