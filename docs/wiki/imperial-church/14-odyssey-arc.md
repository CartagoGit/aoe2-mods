# The Eagle and the Cross / El águila y la cruz

`imperial-church` · CDF-C01 · 29 selected episodes · source locale `en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

```json
{
  "editorial": {
    "campaignTitle": {
      "en": "The Eagle and the Cross",
      "es-ES": "El águila y la cruz"
    },
    "publicId": "CDF-C01",
    "internalName": "CDF_ImperialChurch",
    "sourceLocale": "en",
    "targetEpisodeCount": 29,
    "narratorId": "imperial-clerk",
    "personaLens": {
      "en": "Supply clerks and inherited state papers",
      "es-ES": "Intendencia y expedientes de familia"
    },
    "deliveryTone": {
      "en": "dry irony turning to uneasy loyalty",
      "es-ES": "ironía seca que acaba en lealtad inquieta"
    },
    "sequence": [
      {
        "speaker": "collection-narrator",
        "mode": "sober source-qualified historical fact",
        "causePolicy": "attribute motives, miracles and sectarian judgements to their sources; no single moral or theological verdict"
      },
      {
        "speaker": "imperial-clerk",
        "mode": "fictional personal interpretation with explicit witness basis"
      }
    ],
    "baselineSemanticIdsPreserved": [
      "01-milvian-bridge",
      "02-nicaea",
      "03-new-capital"
    ],
    "orderingPolicy": "order is a separate integer; existing semantic IDs and public/progress IDs remain stable",
    "progressPolicy": "only the actual final odyssey episode offers terminal route write; every former last baseline mission becomes nonterminal when followed by new episodes",
    "sourceAuditStatus": "candidate chronologies reviewed for errors; individual episode historical approval pending",
    "coreMechanicPolicy": "at least four mission-core families in each odyssey; no more than two consecutive identical core families without authored reason; side-objective variety does not excuse identical main missions",
    "narratorMigration": {
      "proposedLifespan": "c.334–403",
      "replaces": "c.290–350",
      "reason": "extend arc to381 without an implausibly long-lived omniscient clerk",
      "knowledge": "312–337 inherited documents; early childhood never adult eyewitness; later dated visits explicitly recorded episode by episode",
      "status": "authored decision; baseline catalogue/voice bible migration occurs with expanded campaign dossier"
    },
    "selectedEpisodeCount": 29,
    "selectionNotes": [
      "Helena death328–330andCrispus/Fausta326remain cautious background, not invented detective missions at uncertain locations.",
      "Paschal decisions are integrated withNicea; capital expansion is integrated with330.",
      "Adrianople/Chrysopolis andMilan/Alexandria are separate local episodes because they involve different places and operations.",
      "Sole rule is not asserted in350: Magnentius survives until353.",
      "Rome/eastern successors open337 and disclose the return in chronology after the381finale."
    ]
  },
  "continuity": {
    "recommendedPrevious": [
      {
        "campaignId": "faith-origins",
        "route": "christian-perspective"
      }
    ],
    "nextRoutes": [
      {
        "id": "western-perspective",
        "key": "progress.imperial-church.western-perspective",
        "next": "church-of-rome"
      },
      {
        "id": "eastern-perspective",
        "key": "progress.imperial-church.eastern-perspective",
        "next": "new-rome"
      }
    ],
    "chronologyWarning": "Western/eastern sequels start in337 and revisit events already covered up to381. Present a sober recap and name the selected successor explicitly.",
    "terminalScreenRule": "show successor English/Spanish title plus public ID for the chosen route; no automatic launching and no requirement lock",
    "proceedWithoutPredecessor": true
  }
}
```

Only the final expanded episode may complete this campaign or present the successor recommendation. Former baseline finales become intermediate episodes when later episodes exist. Preserve every existing semantic scenario ID; display order is a separate field.

## act-1: Eagle Over the River / El águila sobre el río

Historical year band: [312, 317]. Victoria militar, restitución y conflictos africanos; la política de313 no convierte la fe en religión oficial.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 1 / 01-milvian-bridge | The River beneath the Eagle / El río bajo el águila | 28 October 312 CE | milvio | river-battle |
| 2 / 02-bounded-negotiation-milan | Promises in the Winter Court / Promesas en la corte de invierno | 313 CE | milan | bounded-negotiation |
| 3 / 03-property-and-record-restoration-nicomedia | The Doors Returned / Las puertas restituidas | 13 June 313 CE | nicomedia | property-and-record-restoration |
| 4 / 04-rival-delegation-reception-rome-ostia | The African Petition / La petición africana | 313–314 CE; Roman hearing focus | rome-ostia | rival-delegation-reception |
| 5 / 05-delegate-logistics-arles | The Road to Arles / El camino hacia Arlés | 314 CE | arles | delegate-logistics |
| 6 / 06-finite-field-withdrawal-cibalae | The Field between Two Eagles / El campo entre dos águilas | 314 or 316 CE; dating disputed | cibalae | finite-field-withdrawal |

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

## act-2: A Creed in Many Tongues / Un credo en muchas lenguas

Historical year band: [321, 325]. Fiscalidad, controversias y logística conciliar; distinguir decretos, acuerdos y resistencia posterior.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 7 / 07-court-record-logistics-rome-ostia | A Day beneath the Law / Un día bajo la ley | 321 CE; distinguish judicial rule from agricultural exception | rome-ostia | court-record-logistics |
| 8 / 08-disputed-correspondence-alexandria | Words over Alexandria / Palabras sobre Alejandría | 324–325 CE | alexandria | disputed-correspondence |
| 9 / 09-crossing-and-supply-adrianople | The Maritsa Crossing / El paso del Maritsa | 3 July 324 CE, conventional | adrianople | crossing-and-supply |
| 10 / 10-land-and-strait-logistics-chrysopolis | Across the Bright Shore / Al otro lado de la costa luminosa | 18 September 324 CE, conventional | chrysopolis | land-and-strait-logistics |
| 11 / 11-council-record-escort-antioch | Before the Lakeside Council / Antes del concilio junto al lago | 325 CE | antioch | council-record-escort |
| 12 / 02-nicaea | Many Voices beside the Lake / Muchas voces junto al lago | 325 CE | nicaea | delegate-logistics |

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

## act-3: Stone and Succession / Piedra y sucesión

Historical year band: [326, 337]. Patrocinio y capital; incertidumbres privadas permanecen abiertas y el fin de Constantino no cierra la historia.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 13 / 13-finite-works-logistics-jerusalem | Stone above the Old City / Piedra sobre la ciudad antigua | 326–330 CE; individual works dates qualified | jerusalem | finite-works-logistics |
| 14 / 03-new-capital | A City beneath a New Sky / Una ciudad bajo un cielo nuevo | 11 May 330 CE; fictional works approach before dedication | constantinople | urban-logistics |
| 15 / 15-long-distance-dispatch-nicomedia | A Letter beyond the Frontier / Una carta más allá de la frontera | c. 332–333 CE; destination off-map | nicomedia | long-distance-dispatch |
| 16 / 16-witness-record-comparison-tyre | The Council on the Shore / El concilio en la costa | 335 CE; Tyre council focus | tyre | witness-record-comparison |
| 17 / 17-rumour-and-source-investigation-constantinople | The Empty Appointment / La cita vacía | 336 CE | constantinople | rumour-and-source-investigation |
| 18 / 18-administrative-transition-nicomedia | The Court without Its Emperor / La corte sin su emperador | 22 May 337 CE | nicomedia | administrative-transition |
| 19 / 19-competing-dispatches-constantinople | Three Seals, One Inheritance / Tres sellos, una herencia | 337 CE; eastern court focus, not a map of the whole empire | constantinople | competing-dispatches |

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

## act-4: Councils Without Concord / Concilios sin concordia

Historical year band: [343, 359]. Sardica, exilios y fórmulas rivales; Marcus crece entre papeles familiares y empieza a trabajar.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 20 / 20-separate-reception-logistics-sardica | The Council That Divided / El concilio que se dividió | 343 CE; alternative342/344not excluded | sardica | separate-reception-logistics |
| 21 / 21-returning-households-escort-alexandria | The Road Back to Alexandria / El camino de vuelta a Alejandría | 21 October 346 CE | alexandria | returning-households-escort |
| 22 / 22-civilian-record-preservation-milan | The Dispatch from Gaul / El despacho desde la Galia | 350 CE; reception of news, killing site not asserted; Constantius not yet sole emperor | milan | civilian-record-preservation |
| 23 / 23-bounded-political-pressure-milan | Seals at the Western Synod / Sellos en el sínodo occidental | 355 CE; Milan hearing focus | milan | bounded-political-pressure |
| 24 / 24-night-civilian-withdrawal-alexandria | The Night of the Open Doors / La noche de las puertas abiertas | 356 CE; Alexandria local event, no omniscient private dialogue | alexandria | night-civilian-withdrawal |
| 25 / 25-delegate-and-draft-network-rimini | A Formula on the Adriatic Road / Una fórmula en la calzada del Adriático | 359 CE; Western council, Seleucia off-map comparison | rimini | delegate-and-draft-network |

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

## act-5: The Weight of Orthodoxy / El peso de la ortodoxia

Historical year band: [361, 381]. Juliano, ley de380 y concilio de381; el poder prescribe una norma sin probar su aceptación uniforme.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 26 / 26-plural-civic-logistics-constantinople | The Temples Open Again / Los templos vuelven a abrirse | 361 CE | constantinople | plural-civic-logistics |
| 27 / 27-return-and-departure-records-alexandria | The Return That Did Not Last / El regreso que no duró | 362–363 CE; exile policies focus, Persian campaign reported off-map | alexandria | return-and-departure-records |
| 28 / 28-law-and-local-reception-thessalonica | The Weight of an Imperial Word / El peso de una palabra imperial | 27 February 380 CE | thessalonica | law-and-local-reception |
| 29 / 29-council-and-final-perspective-constantinople | Under the Same Eastern Sky / Bajo el mismo cielo oriental | 381 CE | constantinople | council-and-final-perspective |

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

### 1. The River beneath the Eagle

[Candidate source](https://www.newadvent.org/fathers/25021.htm): Eusebius, Life of Constantine I.28–38; Lactantius 44

Research candidate (not yet approved narration): Constantino derrota a Majencio en Puente Milvio y entra en Roma.

Relatos cristianos difieren en visión y cronología.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 2. Promises in the Winter Court

[Candidate source](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/ed_tolerat1.htm): Lactantius, De mortibus persecutorum 48

Research candidate (not yet approved narration): Constantino y Licinio negocian tolerancia religiosa en Milán.

“Edicto de Milán” es rótulo moderno; texto conservado es rescripto oriental.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 3. The Doors Returned

[Candidate source](https://sourcebooks.fordham.edu/source/edict-milan.asp): Lactantius 48; texto del rescripto

Research candidate (not yet approved narration): Licinio publica en Nicomedia la política de libertad y restitución de propiedades.

No establece aún cristianismo como religión oficial.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 4. The African Petition

[Candidate source](https://www.fourthcentury.com/donatist-controversy/): Eusebius HE 10; Optatus, Against the Donatists

Research candidate (not yet approved narration): La disputa donatista llega a audiencias imperiales y sínodos regionales.

Fuentes adversarias y posteriores; no simplificar causas sociales.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 5. The Road to Arles

[Candidate source](https://www.fourthcentury.com/early-church-councils/): Canones de Arlés, colección de fuentes

Research candidate (not yet approved narration): Concilio de Arlés aborda donatismo, disciplina y fecha de Pascua.

Actas fragmentarias.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 6. The Field between Two Eagles

[Candidate source](https://www.britannica.com/biography/Constantine-I-Roman-emperor): Britannica, Constantine, chronology

Research candidate (not yet approved narration): Constantino y Licinio libran guerra en Cibalae; pactan reparto territorial en 317.

The battle is usually dated 316, though some chronologies place it in 314; the conflict was dynastic/political, not simply religious.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 7. A Day beneath the Law

[Candidate source](https://www.fourthcentury.com/constantine-321-sunday-law/): Codex Theodosianus 2.8.1

Research candidate (not yet approved narration): Una ley imperial limita actividad judicial dominical y permite labor agrícola.

No fue cierre total del trabajo.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Corrected primary passage](https://droitromain.univ-grenoble-alpes.fr/Corpus/CJ3.htm): Codex Justinianus 3.12.2 (3.12.3 in older numbering), Constantine to Helpidius. Later codification preserves a 321 constitution. City rest and rural agricultural exception differ from the June permission for manumission in CTh 2.8.1. No uniform compliance or mandated conversion follows from the text.

### 8. Words over Alexandria

[Candidate source](https://www.newadvent.org/fathers/25021.htm): Eusebius, Life of Constantine II.64–73

Research candidate (not yet approved narration): Controversia entre Alejandro de Alejandría y Arrio se extiende por redes episcopales.

Relato de Eusebio presenta el conflicto como problema de unidad.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 9. The Maritsa Crossing

[Candidate source](https://www.britannica.com/biography/Constantine-I-Roman-emperor): Eusebius VC II; resumen cronológico

Research candidate (not yet approved narration): Constantino derrota a Licinio en Adrianópolis y Chrysopolis; queda como único emperador.

La fuente panegírica de Eusebio requiere cautela.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 10. Across the Bright Shore

[Candidate source](https://www.britannica.com/biography/Constantine-I-Roman-emperor): Eusebius VC II; resumen cronológico

Research candidate (not yet approved narration): Constantino derrota a Licinio en Adrianópolis y Chrysopolis; queda como único emperador.

La fuente panegírica de Eusebio requiere cautela.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 11. Before the Lakeside Council

[Candidate source](https://onlinelibrary.wiley.com/doi/10.1111/erev.12782): Kinzig, “The Creed of Nicaea,” sección sobre sínodo

Research candidate (not yet approved narration): Sínodo regional de Antioquía suspende a obispos en antesala de Nicea.

Cronología reconstruida; evidencia transmitida por fuentes posteriores.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 12. Many Voices beside the Lake

[Candidate source](https://www.newadvent.org/fathers/3801.htm): Credo y cánones de Nicea

Research candidate (not yet approved narration): Concilio de Nicea acuerda un credo y cánones sobre doctrina y disciplina.

No creó las iglesias católica y ortodoxa modernas.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 13. Stone above the Old City

[Candidate source](https://www.newadvent.org/fathers/25023.htm): Eusebius, Life of Constantine III.25–40

Research candidate (not yet approved narration): Constantino patrocina iglesias y obras en los lugares santos de Jerusalén.

La obra se inició en algún momento del periodo; no fechar automáticamente por viaje de Helena.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 14. A City beneath a New Sky

[Candidate source](https://www.britannica.com/place/Istanbul/History): Chronicon Paschale, annal 330; overview

Research candidate (not yet approved narration): Constantinopla recibe dedicación ceremonial y juegos fundacionales.

Fecha tradicional, ceremonia sobre proceso urbano anterior.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 15. A Letter beyond the Frontier

[Candidate source](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.8–13

Research candidate (not yet approved narration): Constantino escribe a Shapur II sobre cristianos en el imperio persa, según Eusebio.

Eusebio presenta al emperador como protector universal; sesgo panegírico.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 16. The Council on the Shore

[Candidate source](https://www.newadvent.org/fathers/25023.htm): Eusebius, Life of Constantine IV.41–47; III.28

Research candidate (not yet approved narration): Sínodo de Tiro juzga a Atanasio; poco después se consagra el complejo de la Resurrección.

Narrativas de sínodo y consagración son interesadas.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Corrected primary passage](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.41–47. Book III URL in raw candidate does not contain this locator. Eusebius is a partisan biographer.

### 17. The Empty Appointment

[Candidate source](https://www.newadvent.org/fathers/26023.htm): Sozomen, HE II.29

Research candidate (not yet approved narration): Arrio muere en Constantinopla antes de una readmisión prevista.

Relatos sobre circunstancias milagrosas son polémicos.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 18. The Court without Its Emperor

[Candidate source](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.61–64

Research candidate (not yet approved narration): Constantino recibe bautismo de Eusebio de Nicomedia y muere en Nicomedia.

Bautismo de Silvestre es leyenda posterior.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 19. Three Seals, One Inheritance

[Candidate source](https://www.newadvent.org/fathers/26012.htm): Socrates Scholasticus, Ecclesiastical History II.1 y 2.25; fuente narrativa de siglo V, no contemporánea.

Research candidate (not yet approved narration): Tras la muerte de Constantino, sus hijos toman el poder imperial; las disputas sucesorias y la distribución de territorios preceden nuevas intervenciones en asuntos eclesiásticos.

La sucesión estuvo marcada por violencia contra miembros de la familia imperial; evitar presentar la división territorial como una partición constitucional permanente ya fijada en 337.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 20. The Council That Divided

[Candidate source](https://www.newadvent.org/fathers/3815.htm): Council of Sardica: introducción y cánones; síntesis contextual académica de Milton V. Anastos: https://www.myriobiblos.gr/texts/english/milton1_5.html

Research candidate (not yet approved narration): Obispos occidentales y orientales se reúnen en Sardica; el desacuerdo por Atanasio produce sesiones y decisiones separadas.

La fecha exacta se debate entre 342–344, con 343 habitual. Los cánones sobrevivieron en tradiciones griega y latina con diferencias interpretativas.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 21. The Road Back to Alexandria

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Athanasius, Historia Acephala §§1–2; Socrates, Ecclesiastical History II, regreso y carta imperial: https://www.newadvent.org/fathers/26012.htm

Research candidate (not yet approved narration): Atanasio vuelve a Alejandría tras su exilio, respaldado por cartas de Constancio II y Constante.

La Historia Acephala conserva cronología alejandrina valiosa; sus lagunas y transmisión fragmentaria aconsejan mantener fecha como día calendárico convertido desde el calendario local.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 22. The Dispatch from Gaul

[Candidate source](https://www.newadvent.org/fathers/26012.htm): Socrates, Ecclesiastical History II.25–26; contexto secundario en CCEL, Socrates and Sozomen, Book IV.1: https://www.ccel.org/ccel/schaff/npnf202.iii.ix.i.html

Research candidate (not yet approved narration): Constante es asesinado en la Galia durante la usurpación de Magnencio; Constancio II queda como único emperador y el equilibrio que había favorecido a Atanasio desaparece.

Socrates vincula el cambio político con nuevos conflictos eclesiásticos, pero no reducir toda la guerra civil a una disputa teológica.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 23. Seals at the Western Synod

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Athanasius, Historia Acephala (entrada de tropas, 6–9 Feb 356); su relato defensivo: Apologia de Fuga https://www.newadvent.org/fathers/2814.htm

Research candidate (not yet approved narration): Tras presión imperial en sínodos occidentales, Atanasio es perseguido; tropas entran en una iglesia de Alejandría durante la noche y él escapa.

La cronología de la Historia Acephala sitúa el ataque en febrero de 356. Atanasio escribe como parte enfrentada; sus cifras y caracterización de adversarios requieren cautela.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 24. The Night of the Open Doors

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Athanasius, Historia Acephala (entrada de tropas, 6–9 Feb 356); su relato defensivo: Apologia de Fuga https://www.newadvent.org/fathers/2814.htm

Research candidate (not yet approved narration): Tras presión imperial en sínodos occidentales, Atanasio es perseguido; tropas entran en una iglesia de Alejandría durante la noche y él escapa.

La cronología de la Historia Acephala sitúa el ataque en febrero de 356. Atanasio escribe como parte enfrentada; sus cifras y caracterización de adversarios requieren cautela.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 25. A Formula on the Adriatic Road

[Candidate source](https://www.newadvent.org/fathers/26012.htm): Socrates, Ecclesiastical History II.37–41; la cronología secundaria alojada por CCEL también registra 359: https://www.ccel.org/ccel/s/schaff/npnf202/cache/npnf202.pdf

Research candidate (not yet approved narration): Constancio convoca simultáneamente un concilio occidental en Rimini y uno oriental en Seleucia para buscar una fórmula doctrinal común; ambos producen controversias y no una unidad estable.

Socrates escribe en el siglo V y es pro-niceno. Los sínodos no fueron una única reunión ni una decisión idéntica; evitar etiquetar a todos los participantes con categorías posteriores simplificadas.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 26. The Temples Open Again

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/22*.html): Ammianus Marcellinus, Res Gestae XXII.2; fuente de un contemporáneo pagano que sirvió en la campaña persa.

Research candidate (not yet approved narration): Juliano entra en Constantinopla tras la muerte de Constancio II y asume el gobierno único; reabre templos y restablece sacrificios públicos.

Ammiano admira a Juliano. Las prácticas religiosas se reanudaron por decreto y patronazgo, pero no toda la población cambió de culto ni se revirtió de inmediato la infraestructura cristiana.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 27. The Return That Did Not Last

[Candidate source](https://romanletters.org/letters/julian_emperor/24/): Julian, Letter 24 to the Alexandrians (362), sobre el retorno de Atanasio; Ammianus, Res Gestae XXIII–XXV, campaña y muerte en 363: https://tertullian.org/fathers/ammianus_25_book25.htm

Research candidate (not yet approved narration): Juliano permite el regreso de obispos exiliados y luego vuelve a expulsar a Atanasio de Alejandría; su campaña contra Persia termina con su muerte en Mesopotamia.

Juliano presenta su conducta como aplicación de la ley; cartas imperiales son retóricas oficiales. Las circunstancias exactas de su herida mortal son inciertas.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 28. The Weight of an Imperial Word

[Candidate source](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/Thessalonique.htm): Codex Theodosianus 16.1.2, Edictum de fide catholica; edición de texto latino y encabezamiento consultados.

Research candidate (not yet approved narration): Graciano, Valentiniano II y Teodosio publican en Tesalónica una constitución que prescribe la fe nicena para los pueblos bajo su gobierno y clasifica a otros grupos como herejes.

Es una norma legal dirigida a Constantinopla, no prueba de cumplimiento uniforme inmediato ni de la desaparición de otras religiones. Evitar llamarla, sin matices, conversión instantánea del imperio.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 29. Under the Same Eastern Sky

[Candidate source](https://www.papalencyclicals.net/councils/ecum02.htm): Credo y cánones del Concilio de Constantinopla I; la página señala el problema de la transmisión del credo y el estatus inicialmente limitado del concilio.

Research candidate (not yet approved narration): Un concilio en Constantinopla reafirma la fe nicena, trata controversias sobre el Espíritu y fija en canon 3 la precedencia honorífica del obispo de Constantinopla después de Roma.

El credo conocido como niceno-constantinopolitano se atestigua textualmente en Calcedonia (451); no atribuir sin reservas toda su forma conservada a actas contemporáneas de 381. El canon 3 trata rango, no una división moderna entre católicos y ortodoxos.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.papalencyclicals.net/councils/ecum02.htm): Constantinople I: canon 3; creed and canons, but status/transmission caveat

The source text supports a council traditionally dated 381 and canon 3 giving Constantinople honor after Rome because it is New Rome; creed transmission/history is separate from these canons.

Limit: Canon 3 does not establish papal/imperial jurisdiction or later East-West schism. Page is a compiled translation; it acknowledges transmission complexity.

Coverage: Opened council page and checked canon 3 and creed section; not manuscript apparatus.
