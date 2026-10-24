# The Keys of the Eternal City / Las llaves de la Ciudad Eterna

`church-of-rome` · CDF-C03 · 32 selected episodes · source locale `en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

[Expanded narrator bible and per-episode knowledge framing](../../design/voices/church-of-rome.md) — fictional biography; independent approval pending.

```json
{
  "editorial": {
    "campaignTitle": {
      "en": "The Keys of the Eternal City",
      "es-ES": "Las llaves de la Ciudad Eterna"
    },
    "publicId": "CDF-C03",
    "internalName": "CDF_ChurchOfRome",
    "sourceLocale": "en",
    "targetEpisodeCount": 32,
    "narratorId": "leo-road-singer",
    "personaLens": {
      "en": "A road singer among hospices and archives",
      "es-ES": "Un cantor de caminos entre hospicios y archivos"
    },
    "deliveryTone": {
      "en": "warm rhythms, grief beneath a refrain",
      "es-ES": "ritmos cálidos, duelo bajo el estribillo"
    },
    "sequence": [
      {
        "speaker": "collection-narrator",
        "mode": "sober source-qualified historical fact",
        "causePolicy": "attribute motives, miracles and sectarian judgements to their sources; no single moral or theological verdict"
      },
      {
        "speaker": "leo-road-singer",
        "mode": "fictional personal interpretation with explicit witness basis"
      }
    ],
    "baselineSemanticIdsPreserved": [
      "01-bread-beyond-the-gates",
      "02-the-price-of-peace",
      "03-roads-to-pavia",
      "04-a-crown-at-dawn"
    ],
    "orderingPolicy": "order is a separate integer; existing semantic IDs and public/progress IDs remain stable",
    "progressPolicy": "only the actual final odyssey episode offers terminal route write; every former last baseline mission becomes nonterminal when followed by new episodes",
    "sourceAuditStatus": "candidate chronologies reviewed for errors; individual episode historical approval pending",
    "coreMechanicPolicy": "at least four mission-core families in each odyssey; no more than two consecutive identical core families without authored reason; side-objective variety does not excuse identical main missions",
    "selectedEpisodeCount": 32,
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
        "campaignId": "imperial-church",
        "route": "western-perspective"
      }
    ],
    "nextRoutes": [
      {
        "id": "completed",
        "key": "progress.church-of-rome.completed",
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

## act-1: Two Claims to One City / Dos pretensiones sobre una ciudad

Historical year band: [339, 390]. Apoyos episcopales, concilios y violencia sucesoria; ninguna supremacía universal se da por consumada.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 1 / 01-refuge-and-petition-reception-rome-ostia | A Stranger at the Roman Door / Un extranjero a la puerta de Roma | 339–340 CE | rome-ostia | refuge-and-petition-reception |
| 2 / 02-separate-delegation-logistics-sardica | A Road to Two Councils / Un camino hacia dos concilios | 343 CE; chronology qualified | sardica | separate-delegation-logistics |
| 3 / 03-exile-supply-and-correspondence-beroea-thrace | Letters to a Distant Bishop / Cartas a un obispo lejano | 355–357 CE | beroea-thrace | exile-supply-and-correspondence |
| 4 / 04-draft-and-delegate-network-rimini | The Formula by the Sea / La fórmula junto al mar | 359 CE | rimini | draft-and-delegate-network |
| 5 / 05-neutral-civilian-extraction-rome-ostia | Two Names for the Same Chair / Dos nombres para la misma sede | 366–367 CE; factional violence | rome-ostia | neutral-civilian-extraction |
| 6 / 06-petition-and-accountability-records-milan | The Door That Stayed Closed / La puerta que siguió cerrada | 390 CE; massacre in Thessalonica reported off-map | milan | petition-and-accountability-records |

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

## act-2: Bread After the Empire / Pan después del imperio

Historical year band: [410, 526]. Auxilio tras el saqueo, gobiernos italianos y relaciones entre cortes; Leo canta archivos ajenos.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 7 / 01-bread-beyond-the-gates | Bread beyond the Gates / Pan más allá de las puertas | 410 CE | rome-ostia | sanctuary-supply-and-evacuation |
| 8 / 08-administrative-transition-ravenna | The Court after the Last Emperor / La corte después del último emperador | 476 CE | ravenna | administrative-transition |
| 9 / 09-civilian-record-preservation-ravenna | The Banquet's Long Shadow / La larga sombra del banquete | 493 CE; killing reported, not rewarded | ravenna | civilian-record-preservation |
| 10 / 10-correspondence-consignment-rome-ostia | Two Powers in One Letter / Dos poderes en una carta | 494 CE | rome-ostia | correspondence-consignment |
| 11 / 11-reconciliation-document-logistics-constantinople | Across the Old Division / Al otro lado de la antigua división | 519 CE | constantinople | reconciliation-document-logistics |
| 12 / 12-returning-delegation-aid-ravenna | An Embassy without a Safe Return / Una embajada sin regreso seguro | 525–526 CE; embassyConstantinople reported | ravenna | returning-delegation-aid |

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

## act-3: Through the Gothic Ashes / Entre las cenizas godas

Historical year band: [536, 597]. Guerras y abastecimiento de Roma; Gregorio combina cuidados, negociaciones y enlaces exteriores.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 13 / 13-district-supply-under-occupation-rome-ostia | An Army through the Gates / Un ejército por las puertas | 536 CE | rome-ostia | district-supply-under-occupation |
| 14 / 14-finite-siege-and-urban-relief-rome-ostia | The Year outside the Walls / El año fuera de las murallas | 537–538 CE | rome-ostia | finite-siege-and-urban-relief |
| 15 / 15-archive-extraction-and-refuge-rome-ostia | The Empty Streets of Rome / Las calles vacías de Roma | 546 CE | rome-ostia | archive-extraction-and-refuge |
| 16 / 16-return-and-repair-rome-ostia | Dispatches after the Gothic War / Despachos tras la guerra gótica | 552–553 CE; Taginae reported off-map | rome-ostia | return-and-repair |
| 17 / 02-the-price-of-peace | The Price of Peace / El precio de la paz | 593–595 CE; Gregory590as prologue | rome-ostia | finite-payment-and-relief |
| 18 / 18-hospitality-and-mission-supply-kent | The Road beyond the Channel / El camino más allá del canal | 596–597 CE; Rome dispatch prologue | kent | hospitality-and-mission-supply |

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

## act-4: Keys Between Two Courts / Llaves entre dos cortes

Historical year band: [609, 731]. Reutilización del Panteón, sínodos, exilios y tensión con Constantinopla; fechas disputadas explícitas.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 19 / 19-finite-building-conversion-rome-ostia | A Roof for Older Stones / Un techo para piedras antiguas | 609 or613 CE; exact dedication debated | rome-ostia | finite-building-conversion |
| 20 / 20-council-record-comparison-rome-ostia | The Words at the Lateran / Las palabras en Letrán | October649 CE | rome-ostia | council-record-comparison |
| 21 / 21-exile-relief-and-copying-cherson | Letters from the Cold Shore / Cartas desde la costa fría | 655 CE; death655/656qualified | cherson | exile-relief-and-copying |
| 22 / 22-finite-material-records-rome-ostia | Bronze Leaving the City / El bronce que salía de la ciudad | 663 CE | rome-ostia | finite-material-records |
| 23 / 23-delegation-and-document-escort-constantinople | The Legates across the Water / Los legados al otro lado del agua | 680–681 CE | constantinople | delegation-and-document-escort |
| 24 / 24-disputed-document-reception-rome-ostia | Canons at the Roman Door / Cánones a la puerta de Roma | 692 CE | rome-ostia | disputed-document-reception |
| 25 / 25-artisan-and-council-logistics-rome-ostia | Images before the Synod / Imágenes ante el sínodo | 731 CE | rome-ostia | artisan-and-council-logistics |

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

## act-5: The Crown and the Road / La corona y el camino

Historical year band: [754, 800]. Protección franca, territorios y crisis de799; Leo llega a su tiempo y cierra ante la coronación.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 26 / 26-delegate-and-oath-logistics-saint-denis | Beyond the Alpine Promise / Más allá de la promesa alpina | 754 CE; Saint-Denis local focus | saint-denis | delegate-and-oath-logistics |
| 27 / 03-roads-to-pavia | The Roads to Pavia / Los caminos hacia Pavía | 754–756 CE | pavia | finite-campaign-supply |
| 28 / 28-finite-siege-and-civilian-withdrawal-pavia | At the Lombard Gate / Ante la puerta lombarda | 773–774 CE; earlier768context only | pavia | finite-siege-and-civilian-withdrawal |
| 29 / 29-delegate-logistics-and-copying-nicaea | Roman Letters beside the Lake / Cartas romanas junto al lago | 787 CE | nicaea | delegate-logistics-and-copying |
| 30 / 30-symbolic-consignment-and-couriers-rome-ostia | Keys Sent down the Road / Llaves enviadas por el camino | 795 CE | rome-ostia | symbolic-consignment-and-couriers |
| 31 / 31-refuge-and-petition-escort-paderborn | A Refuge at the Northern Court / Un refugio en la corte del norte | 799 CE | paderborn | refuge-and-petition-escort |
| 32 / 04-a-crown-at-dawn | A Crown at Dawn / Una corona al alba | 25 December800 CE | rome-ostia | ceremony-supply-and-final-perspective |

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

### 1. A Stranger at the Roman Door

[Candidate source](https://www.newadvent.org/fathers/2813.htm): Athanasius, Apologia ad Constantium; exact arrival year varies in scholarship.

Research candidate (not yet approved narration): Athanasius, expelled from Alexandria, reaches Rome and seeks support from Bishop Julius.

Primary apologetic account; date commonly 339/340, not a precise travel record.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/2813.htm): Athanasius, Apologia contra Arianos, §§20–21 (asamblea romana) y §§29–35 (Sardica; viaje).

Athanasius fue a Roma durante su exilio y presentó su caso a la iglesia romana; más tarde acudió a Sardica.

Limit: URL original Apologia ad Constantium no basta para justificar llegada: §4 sí dice que al salir de Alejandría fue «only to Rome», pero no fecha el año. El rango 339–340 procede de cronología moderna (Sardica suele fecharse 343/344; llegada suele ubicarse c.339/340) y debe presentarse como reconstrucción, no como fecha del testimonio.

Coverage: Consultado texto traducido de Apologia ad Constantium §4 y resumen cronológico académico de Universität Erlangen sobre corpus/cronología; Presbyters Project muestra sínodo romano 339/340.

### 2. A Road to Two Councils

[Candidate source](https://www.newadvent.org/fathers/3815.htm): Council of Sardica; historical note places synod in 343, potentially autumn.

Research candidate (not yet approved narration): Athanasius leaves Rome for the Council of Sardica, where eastern and western bishops meet separately after dispute.

Some older chronologies label the council 344; source notes uncertainty.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/3815.htm): Council of Sardica, chronological introduction lines 10–19; canons in remainder

Supports date debate between 343/344 (some older sources said 347), Athanasius at Rome c.340–343, and his journey from Milan via Gaul to Sardica; eastern bishops separated from western proceedings is covered in later page.

Limit: The page itself is 19th-century Catholic scholarship. Do not state 343 as certain; prefer c.343/344. Corpus wording says “leaves Rome for Sardica” although chronology in source says summoned from Rome to Milan then via Gaul.

Coverage: Opened source lines 10–19; inspected date argument and route summary; not underlying primary chronicles.

### 3. Letters to a Distant Bishop

[Candidate source](https://en.wikisource.org/wiki/Nicene_and_Post-Nicene_Fathers:_Series_II/Volume_II/Sozomen/Book_IV/Chapter_11): Sozomeno, Historia eclesiástica IV.11, especialmente pasajes consultados en líneas 102 y 106–109. Debate cronológico y testimonial: https://www.cambridge.org/core/journals/journal-of-ecclesiastical-history/article/liberius-athanasius-and-the-roman-synod/67FF35EAED46A369C33FCFD72FAC1775.

Research candidate (not yet approved narration): Constancio II destierra al obispo Liberio de Roma a Beroea después de que rechaza la fórmula doctrinal que el emperador intenta imponer; Sozomeno atribuye también importancia a su vínculo con Atanasio.

Sozomeno escribe en el siglo V y organiza retrospectivamente los sucesos; la datación del exilio varía, comúnmente 355–357. Evitar convertir su retrato ejemplar de Liberio en transcripción neutral de una negociación.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 4. The Formula by the Sea

[Candidate source](https://www.newadvent.org/fathers/28153.htm): Athanasius, History of the Arians, §33 and surrounding account

Research candidate (not yet approved narration): Bishops meet at Rimini amid imperial pressure for a formula on the Arian controversy.

Athanasius is a Nicene partisan; avoid suggesting one uniform decision or response.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/2817.htm): Athanasius, De Synodis §§1–2, 8–10; New Advent text explicitly names Ariminum and Seleucia and narrates the council at Ariminum.

Hubo sínodos en Ariminum (Rimini) y Seleucia en 359, con conflicto sobre fórmula doctrinal y presión imperial.

Limit: El locator original «History of the Arians §33» no concordaba con el título/URL. De Synodis §8 confirma 400+ reunidos en Ariminum; §10 da la carta del consejo. Athanasius es polemista Niceno, así que su evaluación de los participantes no es neutral. Año 359 requiere consular chronology / academic context.

Coverage: New Advent De Synodis §§1–2 y 8–10 abiertos y leídos por extracto; Presbyters Project source record consulted. No se leyó el tratado completo.

### 5. Two Names for the Same Chair

[Candidate source](https://www.presbytersproject.ihuw.pl/index.php?SourceID=523&id=6): Presbyters Project, Liber Pontificalis source record for the contested election of 366.

Research candidate (not yet approved narration): Damasus and Ursinus are elected by rival factions; street violence follows the contested Roman succession.

Liber Pontificalis account is later; Ammianus 27.3.12–13 is an independent contemporary narrative.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 6. The Door That Stayed Closed

[Candidate source](https://earlychurchtexts.com/main/ambrose/to_theodosius_on_thessalonica_massacre_01.shtml): Ambrose, Letter 51

Research candidate (not yet approved narration): After the massacre at Thessalonica, Ambrose bars Theodosius from communion until public penance.

Ambrose’s letter is contemporary but does not state the event’s year; 390 is conventional, exact date disputed.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/340951.htm): Ambrose, Letter 51, §§6–15

Supports Ambrose’s letter to Theodosius after the Thessalonian slaughter: recounts a massacre, demands penitence, and says he would not offer the Eucharist if the emperor were present.

Limit: The letter is not a narrated scene of physically barring Theodosius at church; that vivid episode comes from later Theodoret HE V.17–18. Avoid staging the letter itself as eyewitness account of a formal excommunication.

Coverage: Opened and read the letter §§6–15; compared the later Theodoret episode only via Fordham search excerpt.

### 7. Bread beyond the Gates

[Candidate source](https://www.newadvent.org/fathers/120101.htm): I.1: santuarios y saqueo de Roma

Research candidate (not yet approved narration): Saqueo de Roma; Agustín escribe sobre protección en ciertos santuarios. Ruta de víveres y familias del jugador son dramatización.

Saqueo de Roma; Agustín escribe sobre protección en ciertos santuarios. Ruta de víveres y familias del jugador son dramatización.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 8. The Court after the Last Emperor

[Candidate source](https://www.britannica.com/event/fall-of-Rome): Fall of Western Roman Empire overview

Research candidate (not yet approved narration): Odoacer deposes Romulus Augustulus; Roman ecclesiastical institutions continue under a new Italian kingdom.

The date marks a political transition, not the end of Rome or its church.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.britannica.com/event/fall-of-Rome): Síntesis de la caída del Imperio romano occidental.

Odoacro depuso a Rómulo Augústulo en 476.

Limit: Enlace terciario y título «fall of Rome» induce a una ruptura total; el evento no acabó las instituciones eclesiásticas romanas, pero esa continuidad necesita fuente diferente. Mejor sumar fuente primaria contemporánea (p.ej., Malchus fr. 10 o Marcellinus Comes s.a. 476) y explicitar el alcance político.

Coverage: Página de Britannica referida por corpus; contenido/pasaje no comprobado en esta pasada.

### 9. The Banquet's Long Shadow

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Excerpta_Valesiana/2*.html): Anonymus Valesianus, pars posterior §§55–57

Research candidate (not yet approved narration): Theodoric kills Odoacer at Ravenna and establishes Ostrogothic rule in Italy.

Narrative source; Theodoric’s later visit to Rome was in 500, not 493.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/thayer/e/roman/texts/excerpta_valesiana/2%2A.html): Anonymus Valesianus II, §§55–57

Supports Theoderic’s entry into Ravenna, killing of Odoacer and succession as king. The source reports the killing as a personal act and subsequent killing of Odoacer’s household/army.

Limit: This is a later, anonymous narrative with an Italian/Ravenna viewpoint; it does not establish a simple immediate formal “kingdom of Italy” constitutional change. Event’s narrow claim is supported.

Coverage: Opened text and read §§55–57 and editor’s note on location “Laurel Grove”; not critical edition.

### 10. Two Powers in One Letter

[Candidate source](https://assets-us-01.kc-usercontent.com/c7bb3f89-eb78-007e-971a-d5864cf7a236/28069a1b-8c16-4f91-8bd6-e69c3eb898f0/Letter-to-Anastasius-I.pdf): Gelasius I, Famuli vestrae pietatis, 494

Research candidate (not yet approved narration): Gelasius writes to Anastasius on the distinct responsibilities of priestly and imperial authority.

Gelasius was bishop of Rome 492–496; the letter is a situated argument, not a timeless constitutional settlement.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://assets-us-01.kc-usercontent.com/c7bb3f89-eb78-007e-971a-d5864cf7a236/28069a1b-8c16-4f91-8bd6-e69c3eb898f0/Letter-to-Anastasius-I.pdf): Gelasius I, Famuli vestrae pietatis, carta a Anastasio I (494), especialmente «Duo sunt» / §§? verificar edición.

Gelasius formula dos autoridades —sacerdotal y real— y su distinta responsabilidad.

Limit: El pontificado correcto es 492–496; «494» para la carta es la fecha convencional de la carta, no 483–492. Número de sección/párrafo depende de edición y no debe inventarse. PDF directo puede ser traducción/edición moderna; identificar editor en cita final.

Coverage: La existencia, destinatario y fecha 494 se contrastaron en fuentes de referencia; PDF enlazado no se abrió/leyó en esta pasada.

### 11. Across the Old Division

[Candidate source](https://www.newadvent.org/cathen/07218b.htm): Catholic Encyclopedia, Acacian Schism; Hormisdas formula and 519 settlement

Research candidate (not yet approved narration): The Acacian schism ends as Rome and Constantinople reconcile under Justin I and Pope Hormisdas.

The source is an older reference work; reconciliation did not erase all doctrinal or jurisdictional tensions.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.ccel.org/s/schaff/encyc07/htm/ii.xii.xvi.viii.htm): Schaff, History of the Christian Church, section on end of Acacian schism; formula preserved in “Documents Illustrative of the History of the Church”

Supports 519 reconciliation process, formula’s signature by Patriarch John/Epiphanius and removal of names from diptychs, as summarized by 19th-century secondary history.

Limit: For exact settlement date sources differ slightly in modern summaries: Holy Thursday 28 Mar vs Easter 24 Mar; don’t force one date from this reference. Textual formula and acceptance are better supported than a simple institutional “unity restored” claim.

Coverage: Read search result extract and consulted scholarly/edited source excerpt; not full monograph or critical letters.

### 12. An Embassy without a Safe Return

[Candidate source](https://text.egwwritings.org/amp/read/988.935): Historical narrative chapter on John I’s embassy

Research candidate (not yet approved narration): Theodoric sends Pope John I to Constantinople on an embassy; John dies imprisoned at Ravenna after returning.

Retrospective confessional narrative; specify that Theodoric’s motives and John’s treatment are source-mediated.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Excerpta_Valesiana/home.html): Fuentes primarias preferidas: Anonymus Valesianus, pars posterior §§90–96 (numeración varía por edición); Liber Pontificalis, Vita Iohannis I. Texto LP: https://archive.org/details/bookofpopesliber01loui/page/146/mode/2up

Teodorico envió al papa Juan I en embajada a Constantinopla; retornó y murió preso en Rávena en 526.

Limit: Retirar egwwritings: no es fuente primaria/académica. Sustituir por Anonymus Valesianus y/o Liber Pontificalis, teniendo en cuenta que son narraciones con agenda/conflicto confesional y no una descripción neutral. La fecha exacta de muerte no se desprende necesariamente del pasaje; campaña solo necesita 525–526.

Coverage: Extracto de Liber Pontificalis consultado vía edición inglesa escaneada (Internet Archive / traducción de Davis); Anonymus Valesianus no verificado línea a línea todavía.

### 13. An Army through the Gates

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/War/5A*.html): Procopius, Wars V, entry into Rome

Research candidate (not yet approved narration): Belisarius enters Rome during Justinian’s Gothic War; the Ostrogoths withdraw north.

Procopius is an eastern imperial historian; later fighting devastated the city.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/Wars/5C%2A.html): Procopius, Wars V (Gothic War I) 14.14–17

Supports Belisarius entering through Asinarian Gate as Goths leave through Flaminian Gate; Procopius dates it the ninth day of December in Justinian’s eleventh regnal year (9 Dec 536).

Limit: Primary narrative gives regnal dating; 9 Dec 536 is modern conversion. Procopius is imperial campaign historian. Correct corpus URL path from War/5A to Wars/5C.

Coverage: Opened Book I chapters 14–23 and read §§14–17; used UW Madison dissertation search extract for modern date conversion.

### 14. The Year outside the Walls

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/War/5A*.html): Procopius, Wars V–VI, siege narrative

Research candidate (not yet approved narration): Vitiges besieges Rome; Belisarius holds the city through a long siege.

Exact day counts differ in modern accounts; avoid unsupported casualty totals.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/Wars/5C%2A.html): Procopius, Wars V (Gothic War I) 19 onward; siege account continues in Wars VI

Supports prolonged Gothic siege of Rome under Vitiges after Belisarius fortifies city, not precise modern date range alone. Scholarly chronology places siege Feb 537–Mar 538.

Limit: Add explicit date range c. Feb 537–Mar 538 from modern scholarship; the page’s opening passage establishes late-536 context. Avoid unsupported force/casualty numbers.

Coverage: Opened Procopius page; read entry and fortification context; UW Madison dissertation search extract states Feb 537–Mar 538.

### 15. The Empty Streets of Rome

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/War/7A*.html): Procopius, Wars VII, capture of Rome

Research candidate (not yet approved narration): Totila captures Rome during the Gothic War; much of its population has fled or suffered hardship.

Procopius’ dramatic details and population figures require caution.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/Wars/7D%2A.html): Procopius, Wars VII (Gothic War III) 20.4–16

Supports Totila gaining entry to Rome through the Asinarian Gate after Isaurian guards defected, and capturing the city.

Limit: Procopius passage establishes capture narrative; 546 date depends on chronological reconstruction/secondary source. Do not present his numbers or dramatic embellishments as independently verified.

Coverage: Opened Book VII and read III.20.4–16; modern date only checked in UW Madison dissertation search result (December 546), not full thesis.

### 16. Dispatches after the Gothic War

[Candidate source](https://www.britannica.com/event/Gothic-War-535-554): Gothic War chronology and final campaigns

Research candidate (not yet approved narration): Narses defeats the Ostrogoths and restores imperial control over Rome and Italy.

The final consolidation occurred over several years; do not imply a single definitive capture in 553.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Procopius/Wars/8J%2A.html): Procopius, Wars VIII (Gothic War IV) 33.26; VIII 35 for later end

Supports Narses’ 552 campaign/capture of Rome within the Gothic War; not a one-event “restoration of Italy” completed in 553.

Limit: Narses’ capture of Rome and the later defeat/end of the Gothic war are distinct; Italy’s consolidation is not equivalent to a single restored event. July 552 often inferred from campaign-year chronology, not precise passage date.

Coverage: Opened/search-checked Procopius VIII 33–35; consulted a scholarly article search extract identifying Wars 8.33.26 and date interval Apr 552–Mar 553; not full article.

### 17. The Price of Peace

[Candidate source](https://www.newadvent.org/fathers/360205036.htm): V.36: arbitraje con Agilulfo y exarca

Research candidate (not yet approved narration): Gregorio negocia paz y arbitraje con poderes lombardos e imperiales; no consenso religioso universal.

Gregorio negocia paz y arbitraje con poderes lombardos e imperiales; no consenso religioso universal.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 18. The Road beyond the Channel

[Candidate source](https://sourcebooks.fordham.edu/source/gregory1.asp): Gregory’s letters concerning Augustine’s mission

Research candidate (not yet approved narration): Gregory sends Augustine’s mission to Kent, extending Roman ecclesiastical contacts in Britain.

Mission and conversion were gradual; do not present England as converted in a single event.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/360206051.htm): Gregory the Great, Registrum Epistolarum VI.51, “To the brethren going to England,” dated 23 July in 14th year Maurice / indiction 14

Supports Gregory writing to missionaries in England and directing them to obey Augustine, who is returning to them; by then the mission was underway.

Limit: This letter alone does not establish dispatch date as 596, nor give the full initial journey; date conversion is usually 596 and needs scholarly chronology. It supports mission continuation/contact, not a precise first arrival at Kent.

Coverage: Opened text and read addressee/body/date; English translation, no full critical edition.

### 19. A Roof for Older Stones

[Candidate source](https://portal.sds.ox.ac.uk/articles/online_resource/E01429_The_short_Life_of_Boniface_IV_bishop_of_Rome_ob_615_S00841_in_the_Liber_Pontificalis_written_in_Latin_in_Rome_early_in_the_7th_c_mentions_his_conversion_of_the_Pantheon_into_the_church_of_the_blessed_Mary_ever-virgin_S00033_and_of_Al/13807430): Liber Pontificalis, Vita Bonifatii IV, c.69, texto latino y traducción reproducidos por Oxford University, Cult of Saints in Late Antiquity; fecha de la cesión/conversión discutida por la bibliografía.

Research candidate (not yet approved narration): Bonifacio IV obtiene del emperador Focas el edificio del Panteón y lo convierte en la iglesia de Santa María y los Mártires.

El Liber Pontificalis confirma la conversión, pero no da en este pasaje un año exacto. Una lectura académica reciente propone 13 de mayo de 613 frente a la datación tradicional de 609; no presentar “609” como certeza.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 20. The Words at the Lateran

[Candidate source](https://www.jstor.org/stable/jj.38238618): The Acts of the Lateran Synod of 649, edición y traducción de Richard Price; introducción sobre el sínodo y las versiones contemporáneas de las actas, secciones III–IV.

Research candidate (not yet approved narration): Martín I convoca un sínodo en la basílica de Letrán; 106 obispos debaten las fórmulas imperiales sobre las voluntades y operaciones de Cristo y condenan el monotelismo.

Las actas son evidencia cercana al evento, pero la introducción historiográfica advierte que la interpretación tradicional como una lucha simple entre “ortodoxia” y compromiso imperial simplifica motivos y debates. El sínodo no implica supremacía romana inevitable.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 21. Letters from the Cold Shore

[Candidate source](https://www.myriobiblos.gr/texts/english/allenneil_maximus_7.html): Allen y Neil, Maximus the Confessor and his Companions, extracto de OUP, sección 7, especialmente párrafos que sitúan juicio en Constantinopla y llegada de Martín a Cherson en mayo de 655; notas 4–5 discuten discrepancia de su fecha de muerte.

Research candidate (not yet approved narration): Tras ser arrestado en Roma en 653 y juzgado en Constantinopla, Martín I recibe una condena de muerte conmutada por exilio; muere en Cherson.

El extracto consultado identifica discrepancias entre fuentes sobre la muerte: 16 de septiembre de 655 o 13 de abril de 656. El episodio debe enfocarse en el exilio y no presentar una fecha final segura.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 22. Bronze Leaving the City

[Candidate source](https://www.newadvent.org/cathen/04295a.htm): Catholic Encyclopedia, Constans II; account of visit to Rome

Research candidate (not yet approved narration): Constans II visits Rome and removes bronze from the Pantheon during his Italian expedition.

Older secondary reference; visit is attested, but the claim that all bronze roof tiles were removed is often exaggerated.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://upload.wikimedia.org/wikipedia/commons/2/23/The_book_of_the_popes_%28Liber_pontificalis%29_I-_%28IA_cu31924006163897%29.pdf): Liber Pontificalis, Vita Vitaliani, chapter XI, account of Constans II’s visit to Rome

The source text quoted in search excerpt says Constans arrived via Naples, was met by Pope Vitalian at Rome’s sixth milestone, stayed twelve days, removed bronze decoration including Pantheon roof tiles, and sent material to Constantinople.

Limit: Liber Pontificalis is a Roman papal biography with hostile presentation (“afflictions”); it supports a reported removal, not verified destination of every piece. The existing New Advent encyclopedia is secondary.

Coverage: Read specific quoted LP excerpt in search result and checked scan source; PDF full text was not downloaded/read.

### 23. The Legates across the Water

[Candidate source](https://www.newadvent.org/fathers/3813.htm): Acts of Constantinople III; letters of Agatho and Roman legates.

Research candidate (not yet approved narration): El Tercer Concilio de Constantinopla condena el monotelismo; el papa Agatón participa por cartas y legados.

La recepción y terminología fueron disputadas; no proyectar categorías confesionales posteriores.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/3813.htm): Acts of Constantinople III, Sessions I, IV and XIII; Agatho letter and synodal decision

Supports Roman envoys and Agatho’s synodal letter, council’s Christological debate on one/two wills and operations, and condemnation of Honorius in Session XIII.

Limit: A council text and a 1900 translation/editorial framing. Do not simplify its theological definitions into modern denominational divisions; participation by papal envoys is supported.

Coverage: Opened Acts, read lines 11–25 and condemnation §§165–168; not Greek/Latin critical apparatus.

### 24. Canons at the Roman Door

[Candidate source](https://www.myriobiblos.gr/texts/english/milton1_11.html): Milton V. Anastos, “The Constantinopolitan Council in Trullo (692)”

Research candidate (not yet approved narration): The Quinisext Council issues disciplinary canons; Pope Sergius refuses to sign the canons sent to Rome.

Western reception was contested and later varied; do not treat the council’s status as universally agreed.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/3814.htm): Quinisext Council in Trullo, canon 36; compare canons 13 and 55 for Roman custom conflict

Supports canon 36’s explicit order: Constantinople “equal privileges” with Old Rome and second after it, followed by Alexandria, Antioch and Jerusalem.

Limit: Canon’s normative language is not proof of Western acceptance. The report that Sergius rejected the canons must be sourced to separate correspondence/biography; current canon page alone does not establish his refusal.

Coverage: Opened council page and read canon 36; no papal correspondence reviewed.

### 25. Images before the Synod

[Candidate source](https://www.treccani.it/enciclopedia/iconoclastia-o-iconoclasmo_%28Enciclopedia-Italiana%29/): Treccani, Iconoclastia, account of Gregory III’s Roman council

Research candidate (not yet approved narration): A Roman synod under Gregory III condemns attacks on images.

The source notes limits to claims of systematic image destruction under Leo III.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 26. Beyond the Alpine Promise

[Candidate source](https://sourcebooks.web.fordham.edu/source/donatconst.asp): Fordham Sourcebook introduction, Pepin and Stephen II

Research candidate (not yet approved narration): Stephen II crosses the Alps and anoints Pepin, securing Frankish protection against Lombard pressure.

The 754 promise and 756 territorial transfer are known through papal narrative; the treaty text is not extant.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://sourcebooks.web.fordham.edu/source/donatconst.asp): Fordham Medieval Sourcebook, intro to Donation of Constantine; notes on Stephen II/Pepin 754

Supports as secondary overview that Stephen crossed the Alps and anointed Pepin in 754 and Pepin promised Lombard-held lands; page says promise fulfilled in 756.

Limit: Original reference is misleadingly named “Donation of Constantine” and is not primary evidence for Pepin. Promise boundaries and formal anointing are described in later papal accounts; use LP/MGH direct text for a final chronology.

Coverage: Opened sourcebook lines 18–23; read overview and forgery context, not underlying Pepin donation text.

### 27. The Roads to Pavia

[Candidate source](https://sourcebooks.web.fordham.edu/basis/einhard.asp): 6: campañas italianas; 28: coronación

Research candidate (not yet approved narration): Intervenciones francas de Pipino en Italia y acuerdos con el papado; los límites exactos de transferencias se documentan antes de representarlos.

Intervenciones francas de Pipino en Italia y acuerdos con el papado; los límites exactos de transferencias se documentan antes de representarlos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 28. At the Lombard Gate

[Candidate source](https://www.ancienttexts.org/library/latinlibrary/ein.html): Einhard, Life of Charlemagne, chapters 6 and 27

Research candidate (not yet approved narration): The Carolingian rulers consolidate power; Charlemagne’s campaigns against the Lombards bring Rome a new protector.

Einhard’s retrospective court biography is selective; the decisive Italian campaign was 773–774.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 29. Roman Letters beside the Lake

[Candidate source](https://www.newadvent.org/fathers/3819.htm): Acts of Nicaea II and Hadrian’s letter

Research candidate (not yet approved narration): Pope Hadrian I sends legates to the Second Council of Nicaea, which restores the veneration of icons.

Council texts survive through later transmission; distinguish veneration from worship.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.newadvent.org/fathers/3819.htm): Acts of Nicaea II, Hadrian’s letter and council definition (sessions 2 and 7)

Supports Pope Hadrian’s letter being read and the council’s endorsement of veneration/salutation of icons while distinguishing this from worship/service due to God alone.

Limit: The translated acts have ecclesiastical/editorial framing; use “veneration” with care and do not state that all imperial subjects immediately accepted the settlement.

Coverage: Opened acts and read the letter excerpt and definition passages on images; not manuscript history.

### 30. Keys Sent down the Road

[Candidate source](https://ccel.org/ccel/schaff/hcc4/hcc4.i.iv.x.html): Schaff, History of the Christian Church IV, section on Leo III

Research candidate (not yet approved narration): Leo III succeeds Hadrian I and sends the keys and banners of Rome to Charlemagne.

Secondary 19th-century account; diplomatic symbolism should not be read as a formal transfer of sovereignty.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 31. A Refuge at the Northern Court

[Candidate source](https://www.ancienttexts.org/library/latinlibrary/ein.html): Einhard, Life of Charlemagne 28; Royal Frankish Annals 799

Research candidate (not yet approved narration): Leo III is attacked in Rome and seeks Charlemagne’s protection.

Einhard’s report is retrospective; allegations against Leo and the assault’s details are politically charged.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 32. A Crown at Dawn

[Candidate source](https://www.ancienttexts.org/library/latinlibrary/ein.html): Einhard, Life of Charlemagne 28

Research candidate (not yet approved narration): Leo III crowns Charlemagne emperor at St Peter’s on Christmas Day.

Einhard says Charles claimed surprise; this may serve a literary/political purpose and should not be treated as certain.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending
