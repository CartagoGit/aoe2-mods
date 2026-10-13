# Embers of the Covenant / Las brasas de la alianza

`faith-origins` · CDF-C00 · 30 selected episodes · source locale `en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

[Expanded narrator bible and per-episode knowledge framing](../../design/voices/faith-origins.md) — fictional biography; independent approval pending.

```json
{
  "editorial": {
    "campaignTitle": {
      "en": "Embers of the Covenant",
      "es-ES": "Las brasas de la alianza"
    },
    "publicId": "CDF-C00",
    "internalName": "CDF_FaithOrigins",
    "sourceLocale": "en",
    "targetEpisodeCount": 30,
    "narratorId": "miriam-archive",
    "personaLens": {
      "en": "Comparison, gaps, household memory",
      "es-ES": "Comparación, huecos y memoria doméstica"
    },
    "deliveryTone": {
      "en": "quiet precision, reluctant hope",
      "es-ES": "precisión serena, esperanza cauta"
    },
    "sequence": [
      {
        "speaker": "collection-narrator",
        "mode": "sober source-qualified historical fact",
        "causePolicy": "attribute motives, miracles and sectarian judgements to their sources; no single moral or theological verdict"
      },
      {
        "speaker": "miriam-archive",
        "mode": "fictional personal interpretation with explicit witness basis"
      }
    ],
    "baselineSemanticIdsPreserved": [
      "01-roads-of-antioch",
      "02-after-the-siege",
      "03-the-governors-question",
      "04-a-different-dawn"
    ],
    "orderingPolicy": "order is a separate integer; existing semantic IDs and public/progress IDs remain stable",
    "progressPolicy": "only the actual final odyssey episode offers terminal route write; every former last baseline mission becomes nonterminal when followed by new episodes",
    "sourceAuditStatus": "30 per-episode consultations recorded; limits retained; independent historical approval pending",
    "coreMechanicPolicy": "at least four mission-core families in each odyssey; no more than two consecutive identical core families without authored reason; side-objective variety does not excuse identical main missions",
    "selectedEpisodeCount": 30,
    "selectionNotes": [
      "The two Jerusalem meeting candidates 0/30 are consolidated; their identification remains disputed.",
      "The disputed imprisonment-letter candidate 7 is contextual evidence, not an extra mission.",
      "Repeated copying families are separated by civic rescue, provisioning, production, legal procedure and hospitality; complete gameplay contracts remain pending.",
      "Act targets are editorial guides: this selection follows sourced chronology rather than forcing six episodes into every act.",
      "Milan 313 is a local fictional archive setting; do not claim every prior persecution took place in Milan."
    ],
    "authoredDossierCount": 25
  },
  "continuity": {
    "recommendedPrevious": [],
    "nextRoutes": [
      {
        "id": "christian-perspective",
        "key": "progress.faith-origins.christian-perspective",
        "next": "imperial-church"
      },
      {
        "id": "jewish-perspective",
        "key": "progress.faith-origins.jewish-perspective",
        "next": "jewish-tradition"
      }
    ],
    "chronologyWarning": "Any predecessor-dependent campaign remains independently playable; show recommendation and recap, preserve all route keys, and disclose overlap when changing perspective.",
    "terminalScreenRule": "show successor English/Spanish title plus public ID for the chosen route; no automatic launching and no requirement lock",
    "proceedWithoutPredecessor": true
  }
}
```

Only the final expanded episode may complete this campaign or present the successor recommendation. Former baseline finales become intermediate episodes when later episodes exist. Preserve every existing semantic scenario ID; display order is a separate field.

## act-1: Names Before the Ashes / Nombres antes de las cenizas

Historical year band: [27, 50]. De las fuentes sobre Jesús a comunidades diversas, sin tratar relatos de fe como hechos sobrenaturales comprobados.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 1 / 01-administrative-records-caesarea | Stone Beneath the Prefect's Name / Piedra bajo el nombre del prefecto | 27–36 CE | caesarea | administrative-records |
| 2 / 02-civilian-refuge-jerusalem | When the City Held Its Breath / Cuando la ciudad contuvo el aliento | c. 30–33 CE | jerusalem | civilian-refuge |
| 3 / 03-shared-provision-jerusalem | A Table in Jerusalem / Una mesa en Jerusalén | c. 30–40 CE | jerusalem | shared-provision |
| 4 / 04-testimony-relay-damascus | The Road He Remembered / El camino que recordaba | c. 33–36 CE | damascus | testimony-relay |
| 5 / 05-witness-comparison-jerusalem | Fifteen Days, Many Voices / Quince días, muchas voces | c. 36–40 CE | jerusalem | witness-comparison |
| 6 / 01-roads-of-antioch | Letters on the Orontes / Cartas sobre el Orontes | c. 40–49 CE; conventional early-network reconstruction | antioch | network-escort |
| 7 / 07-household-relocation-rome-ostia | The Doors That Closed / Las puertas que se cerraron | c. 49 CE | rome-ostia | household-relocation |
| 8 / 08-delegate-logistics-jerusalem | A Place for the Stranger / Un lugar para el extranjero | c. 49–50 CE; identification of meetings disputed | jerusalem | delegate-logistics |

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

## act-2: Across the Many Roads / Por tantos caminos

Historical year band: [50, 64]. Cartas, trabajo y redes urbanas; las disputas de pertenencia no se resuelven mediante conquistar una facción.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 9 / 09-district-production-corinth | The Weaver's Harbour / El puerto del tejedor | c. 50–52 CE | corinth | district-production |
| 10 / 10-copy-and-relay-corinth | Before the First Letter Faded / Antes de que se borrase la primera carta | c. 50–51 CE | corinth | copy-and-relay |
| 11 / 11-distributed-preservation-ephesus | The Argument Across the Water / La disputa al otro lado del agua | c. 54–55 CE; writing location uncertain | ephesus | distributed-preservation |
| 12 / 12-bounded-community-aid-ephesus | Many Hands in One House / Muchas manos en una casa | c. 54–55 CE | ephesus | bounded-community-aid |
| 13 / 13-consignment-and-correspondence-corinth | Words for a Distant City / Palabras para una ciudad lejana | c. 56–58 CE | corinth | consignment-and-correspondence |
| 14 / 14-administrative-intrigue-caesarea | The Appeal Beside the Sea / La apelación junto al mar | c. 57–60 CE | caesarea | administrative-intrigue |
| 15 / 15-evacuation-and-recovery-rome-ostia | Ash over the Seven Hills / Ceniza sobre las siete colinas | 64 CE | rome-ostia | evacuation-and-recovery |

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

## act-3: Under a Broken Roof / Bajo un techo quebrado

Historical year band: [65, 150]. Destrucción del Templo y transmisión diversa; no presentar judaísmo y cristianismo como bloques ya uniformes.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 16 / 16-comparative-copying-antioch | A Story in the Shadow of War / Un relato a la sombra de la guerra | c. 65–70 CE; authorial location not known | antioch | comparative-copying |
| 17 / 02-after-the-siege | The Names Beyond the Siege / Los nombres más allá del asedio | 70 CE | jerusalem | civilian-evacuation |
| 18 / 18-parallel-archive-logistics-antioch | Two Voices, Unfinished Margins / Dos voces, márgenes sin terminar | c. 80–90 CE; location is fictional local circulation, not authorial provenance | antioch | parallel-archive-logistics |
| 19 / 19-hospitality-network-antioch | The House Before the Road / La casa antes del camino | c. 90–100 CE; Syrian provenance proposed | antioch | hospitality-network |
| 20 / 20-reconciliation-deliveries-rome-ostia | A Letter Across the Divide / Una carta sobre la división | c. 95 CE | rome-ostia | reconciliation-deliveries |
| 21 / 03-the-governors-question | The Governor's Question / La pregunta del gobernador | c. 112 CE | bithynia | administrative-intrigue |

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

## act-4: Voices Before the Tribunal / Voces ante el tribunal

Historical year band: [150, 203]. Apologías, auxilio y medidas represivas locales; evitar el mito de persecución continua uniforme.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 22 / 22-reading-and-relief-rome-ostia | Bread Read Aloud / Pan leído en voz alta | c. 150–160 CE | rome-ostia | reading-and-relief |
| 23 / 23-petition-escort-sardes | A Petition from Sardes / Una petición desde Sardes | c. 170–180 CE | sardes | petition-escort |
| 24 / 24-witness-and-evacuation-lyon | The River Kept Their Names / El río conservó sus nombres | 177 CE | lyon | witness-and-evacuation |
| 25 / 25-archive-comparison-lyon | Voices Against the Fragments / Voces frente a los fragmentos | c. 180–200 CE | lyon | archive-comparison |
| 26 / 26-legal-record-network-carthage | The Advocate's Harbour / El puerto del defensor | c. 197 CE | carthage | legal-record-network |
| 27 / 27-household-aid-and-memory-carthage | What the Record Cannot Hold / Lo que el registro no puede guardar | 203 CE | carthage | household-aid-and-memory |

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

## act-5: The Archive and the Dawn / El archivo y el alba

Historical year band: [249, 313]. El mundo vivido por Miriam conecta copias heredadas con persecución y restitución; el cierre conduce a la bifurcación de perspectiva.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 28 / 28-certificate-and-refuge-egypt-middle-nile | The Seal on the Certificate / El sello del certificado | 249–251 CE | egypt-middle-nile | certificate-and-refuge |
| 29 / 29-bounded-evacuation-carthage | A Harbour Under Orders / Un puerto bajo órdenes | 257–258 CE | carthage | bounded-evacuation |
| 30 / 04-a-different-dawn | A Different Dawn / Un alba distinta | 303–313 CE; Milan local archive is dramatization, persecution and restitution vary regionally | milan | supply-and-testimony |

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

### 1. Stone Beneath the Prefect's Name

[Candidate source](https://cojs.org/pontius_pilate-s_tiberium_inscription-_26-36_ce/): Inscripción del Tiberieum; ficha del Center for Online Judaic Studies, procedencia Cesarea y cargo de Pilato.

Research candidate (not yet approved narration): La inscripción de Cesarea documenta a Pontius Pilatus con el título de prefecto de Judea durante su administración.

La piedra está fragmentada y reutilizada; prueba el cargo y actividad edilicia, no el proceso de Jesús. El rango 27–36 recorta el mandato convencional 26–36 al periodo de campaña.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/01-administrative-records-caesarea/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The Caesarea inscription attests Pilate's title and a building dedication; it does not attest the trial of Jesus.

ES: La inscripción de Cesarea acredita el título de Pilato y una dedicación edilicia; no documenta el proceso de Jesús.

[Consulted source](https://cojs.org/pontius_pilate-s_tiberium_inscription-_26-36_ce/): COJS entry, paragraphs describing findspot, reused block, dedication and titulature; inscription translation names Pontius Pilate as prefect of Judea.

Limit: Fragmentary stone reused in a stairway; COJS is a secondary catalog entry. The campaign's 27–36 range is an editorial slice of the conventional prefecture dates, not the inscription's date.

Status: consulted

### 2. When the City Held Its Breath

[Candidate source](https://www.perseus.tufts.edu/hopper/text?doc=Tac.+Ann.+15.44): Tacitus, Annals 15.44; Cambridge, ‘Dating the Death of Jesus’ (discute el 30 preferido por muchos y la imposibilidad de recuperar fecha exacta): https://www.cambridge.org/core/journals/new-testament-studies/article/dating-the-death-of-jesus-memory-and-the-religious-imagination/0458FC0CA55BEF810BCC411AC2765860

Research candidate (not yet approved narration): Fuentes cristianas sitúan la ejecución de Jesús bajo Pilato; Tacito, décadas después, también atribuye su ejecución a Pilato bajo Tiberio.

Tacito escribe a comienzos del siglo II, no es testigo. El rango 30–33 es estimación moderna; no incorporar resurrección o milagros como hechos verificables.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/02-civilian-refuge-jerusalem/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Tacitus, writing decades later, says Christus was executed under Tiberius by Pontius Pilate. The passage does not place the execution in a specific year or record a refuge episode.

ES: Tácito, décadas después, dice que Christus fue ejecutado bajo Tiberio por Poncio Pilato. El pasaje no fija un año concreto ni registra un episodio de refugio.

[Consulted source](https://dcc.dickinson.edu/tacitus-annals/15-44): Tacitus, Annals 15.44, passage on Christus and the Neronian punishments; DCC notes distinguish Tacitus' report from other evidence and observe Christian sources do not mention an arson charge.

Limit: Retrospective Roman literary testimony, not eyewitness evidence. The 30–33 date is a modern estimate; the episode candidate's 'Christian sources' wording should cite those separately if retained.

Status: consulted

### 3. A Table in Jerusalem

[Candidate source](https://www.biblegateway.com/passage/?search=Acts+2%3A42-47&version=NRSVUE): Acts 2:42–47; communal meals and distribution as portrayed by Acts

Research candidate (not yet approved narration): Hechos presenta comidas y bienes compartidos en la comunidad de Jerusalén.

Relato literario cristiano; no censo, cantidades ni uniformidad social comprobados. Las tareas domésticas del mapa son ficticias.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/03-shared-provision-jerusalem/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Acts portrays teaching, meals and sharing within the early Jerusalem community. This is the book’s account, not an independent census or proof that every household lived alike.

ES: Hechos describe enseñanza, comidas y bienes compartidos en la primera comunidad de Jerusalén. Es el relato del libro, no un censo independiente ni una prueba de que todos los hogares vivieran igual.

[Consulted source](https://www.biblegateway.com/passage/?search=Acts+2%3A42-47&version=NRSVUE): Acts 2:42–47; communal meals and distribution as portrayed by Acts

Limit: Relato literario cristiano; no censo, cantidades ni uniformidad social comprobados. Las tareas domésticas del mapa son ficticias.

Status: consulted by gpt-6; independent approval pending

### 4. The Road He Remembered

[Candidate source](https://www.biblegateway.com/passage/?search=Galatians+1&version=NIV): Pablo, Gálatas 1:13–17; fecha aproximada contextualizada por Cambridge, Dating the Death of Jesus, y la cronología paulina anclada en Galión.

Research candidate (not yet approved narration): Pablo recuerda que pasó de perseguir a los grupos seguidores de Jesús a proclamarlos; describe su cambio como una revelación recibida, en sus propios términos.

‘Revelación’ es la descripción autobiográfica de Pablo, no una afirmación historiográfica sobre una aparición sobrenatural. El año exacto de su cambio no puede fijarse.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/04-testimony-relay-damascus/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Paul says he persecuted the assembly of God and describes his change as a revelation and commission; he names Arabia and Damascus but gives no complete itinerary or exact year.

ES: Pablo dice que persiguió a la asamblea de Dios y describe su cambio como revelación y encargo; nombra Arabia y Damasco, pero no ofrece itinerario completo ni año exacto.

[Consulted source](https://www.biblegateway.com/passage/?search=Galatians+1%3A13-17&version=NRSVUE): Galatians 1:13–17: Paul recalls persecution, a divine revelation/commission, Arabia, and return to Damascus.

Limit: The revelation is Paul's theological account, not an independently verifiable supernatural event. Year range c.33–36 is reconstructed; do not stage an unreported journey.

Status: consulted

### 5. Fifteen Days, Many Voices

[Candidate source](https://www.biblegateway.com/passage/?search=Galatians+1%3A18-19&version=NIV%3BNRSVUE%3BKJV%3BNKJV): Pablo, Gálatas 1:18–19; Yale Bible Study, Paul’s chronology anchored by the Delphi/Gallio inscription: https://yalebiblestudy.org/courses/acts-of-the-apostles/lessons/co-operative-ministry-study-guide/

Research candidate (not yet approved narration): Pablo visita Jerusalén y se entrevista con Cefas y Santiago; afirma que permaneció allí quince días.

El intervalo ‘tres años’ admite cómputos inclusivos distintos y la fecha de la llamada de Pablo es incierta. Gálatas es una carta polémica escrita para defender su autoridad.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/05-witness-comparison-jerusalem/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Paul reports a Jerusalem visit, a fifteen-day stay with Cephas, and seeing James.

ES: Pablo informa de una visita a Jerusalén, una estancia de quince días con Cefas y un encuentro con Santiago.

[Consulted source](https://www.biblegateway.com/passage/?search=Galatians+1%3A18-19&version=NRSVUE): Galatians 1:18–19, especially Paul's 'fifteen days' and named contacts; Yale Bible Study chronology page consulted for the broader chronology anchor (Gallio/Delphi).

Limit: This repeats the preceding episode's source/event and should be made a distinct editorial angle or treated as duplicate. Relative interval and date of Paul's call remain uncertain; the Yale overview does not make the exact year certain.

Status: consulted

### 6. Letters on the Orontes

[Candidate source](https://www.biblegateway.com/passage/?search=Acts+11%3A19-30&version=NRSVUE): Acts 11:19–30; Antioch community and narrated aid to Judea

Research candidate (not yet approved narration): Hechos narra una comunidad en Antioquía y el envío de ayuda a Judea.

Relato literario cristiano; fechas y cifras no se fijan en el pasaje. Gal2:11–14 se conserva como contexto posterior de disenso, no se sitúa antes de su relato de visita a Jerusalén.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/01-roads-of-antioch/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Acts describes a community at Antioch and an aid shipment to Judea. Its travelers and charitable network provide the narrative context; this local courier circuit is fictional and its conventional dating is reconstructed.

ES: Hechos describe una comunidad en Antioquía y una remesa de ayuda a Judea. Sus viajeros y su red de auxilio aportan el contexto narrativo; el circuito local de correos es ficticio y su fecha convencional se reconstruye.

[Consulted source](https://www.biblegateway.com/passage/?search=Acts+11%3A19-30&version=NRSVUE): Acts 11:19–30; Antioch community and narrated aid to Judea

Limit: Relato literario cristiano; fechas y cifras no se fijan en el pasaje. Gal2:11–14 se conserva como contexto posterior de disenso, no se sitúa antes de su relato de visita a Jerusalén.

Status: consulted by gpt-6; independent approval pending

### 7. The Doors That Closed

[Candidate source](https://lexundria.com/suet_cl/25.4/r): Suetonius, Claudius 25.4; Cambridge Companion to the Age of Nero contextualiza probablemente ca. 49: https://doi.org/10.1017/9781107280489.016

Research candidate (not yet approved narration): Suetonio informa que Claudio expulsó de Roma a judíos implicados en disturbios ‘impulsore Chresto’; el pasaje puede reflejar conflicto dentro de comunidades judías y cristianas incipientes.

Suetonio no explica quién fue Chrestus; la identificación con Christus/Jesús es una hipótesis, no un dato explícito. La fecha exacta de la expulsión se discute.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/07-household-relocation-rome-ostia/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Suetonius reports disturbances among Jews in Rome and an expulsion under Claudius, mentioning 'Chrestus'.

ES: Suetonio informa de disturbios entre judíos de Roma y una expulsión bajo Claudio, y menciona a «Chrestus».

[Consulted source](https://lexundria.com/suet_cl/25.4/r): Suetonius, Claudius 25.4: Claudius expels Jews from Rome after disturbances 'impulsore Chresto'. Cambridge scholarly article search result notes scholarly disagreement in dating this incident (41 vs c.49).

Limit: The text does not identify Chrestus with Jesus/Christ, specify a year, or show that Christians were the only people expelled. The c.49 date is conventional and debated; this candidate's Christian-conflict reading is a hypothesis.

Status: disputed

### 8. A Place for the Stranger

[Candidate source](https://academic.oup.com/edited-volume/37088/chapter/323184625): Oxford Handbook, Chronology; Hechos 15 / Gálatas 2

Research candidate (not yet approved narration): La asamblea de Jerusalén discute la admisión de gentiles y la circuncisión.

La relación entre las versiones de Hechos y Pablo es debatida.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/08-delegate-logistics-jerusalem/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Acts narrates a Jerusalem debate about gentile inclusion and circumcision; Paul independently describes a Jerusalem visit and agreement about mission in Galatians 2.

ES: Hechos narra un debate en Jerusalén sobre la inclusión gentil y la circuncisión; Pablo describe por separado una visita y un acuerdo sobre la misión en Gálatas 2.

[Consulted source](https://www.biblegateway.com/passage/?search=Acts+15&version=NRSVUE): Acts 15:1–29: narrative of a Jerusalem meeting debating circumcision of gentile adherents and a set of requirements; compare Paul's distinct account in Galatians 2:1–10.

Limit: Acts and Galatians cannot be harmonized into one securely identified meeting without argument; date c.49–50 is reconstructed. The Oxford Handbook page is an overview, not primary evidence; source selection should cite both accounts and signal disagreement.

Status: disputed

[Additional consulted passage](https://www.biblegateway.com/passage/?search=Galatians+2%3A1-10&version=NRSVUE): Galatians 2:1–10

Limit: A retrospective Pauline account; no composition date is asserted. It does not independently establish that this is the same meeting narrated in Acts15 or a transcript of that meeting. Not a physical game object in c49–50.

### 9. The Weaver's Harbour

[Candidate source](https://dcc.dickinson.edu/greek-new-testament/acts/18): Acts 18; ancla cronológica: inscripción de Galión en Delfos

Research candidate (not yet approved narration): Pablo establece una comunidad en Corinto y trabaja con Prisca y Aquila.

La fecha depende de reconstrucción; Hechos es narrativa teológica.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/09-district-production-corinth/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Acts reports Paul working with Prisca and Aquila in Corinth and staying there eighteen months; the Gallio episode provides a chronological anchor.

ES: Hechos informa que Pablo trabajó con Prisca y Aquila en Corinto y permaneció allí dieciocho meses; el episodio de Galión sirve de ancla cronológica.

[Consulted source](https://www.biblegateway.com/passage/?search=Acts+18&version=NRSVUE): Acts 18:1–18: Paul meets Prisca and Aquila in Corinth, stays eighteen months, and is brought before Gallio; compare Gallio inscription for the proconsul's tenure.

Limit: Narrative source, not a contemporary record of founding. Exact 50–52 dating depends on the Delphi inscription's date and chronology reconstruction; DCC URL listed in selection was unavailable in the earlier consultation.

Status: consulted

### 10. Before the First Letter Faded

[Candidate source](https://academic.oup.com/book/3544): Oxford, New Testament Christianity in the Roman World, abstract consulted

Research candidate (not yet approved narration): Pablo escribe 1 Tesalonicenses, uno de los textos cristianos conservados más tempranos.

Ciudad de composición probable, no segura.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/10-copy-and-relay-corinth/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: 1 Thessalonians is commonly dated around 50 CE and is the earliest surviving Pauline letter.

ES: 1 Tesalonicenses suele fecharse hacia el año 50 y es la carta paulina conservada más antigua.

[Consulted source](https://citer.ucp.pt/sites/default/files/2024-03/citer-catedra-abravanel-de-gois-amy-jill-levine-and-marc-zvi-brettler-the-jewish-annotated-new-testament.pdf): Jewish Annotated New Testament introduction to 1 Thessalonians: dates ca. 50 CE and calls it earliest extant Pauline writing; contrast primary letter itself.

Limit: The source is scholarly commentary; this supports conventional date/order, not that the letter was written in Corinth. The dossier's OUP source was only an abstract and should not be represented as full-book consultation.

Status: consulted

### 11. The Argument Across the Water

[Candidate source](https://www.bibleodyssey.org/articles/galatians/): Society of Biblical Literature, Galatians overview

Research candidate (not yet approved narration): La carta a los Gálatas evidencia disputa sobre identidad, ley y pertenencia gentil.

Lugar y fecha dependen de la hipótesis sobre destinatarios.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/11-distributed-preservation-ephesus/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Galatians preserves a dispute over gentile belonging, circumcision, and the law as argued by Paul.

ES: Gálatas conserva una disputa sobre la pertenencia gentil, la circuncisión y la ley tal como la argumenta Pablo.

[Consulted source](https://www.biblegateway.com/passage/?search=Galatians&version=NRSVUE): Galatians 1–2 and 3:1–5: Paul's argument about his commission, Abraham, law, and gentile belonging; SBL Bible Odyssey link listed in dossier was unavailable in prior consultation.

Limit: The letter itself supports the dispute; neither its place of composition nor c.54–55 is established by these chapters. Ephesus is not securely documented as the writing location.

Status: consulted

### 12. Many Hands in One House

[Candidate source](https://academic.oup.com/book/3544): Oxford abstract; 1 Corinthians 1–16

Research candidate (not yet approved narration): Pablo escribe 1 Corintios y responde a conflictos y prácticas de una comunidad urbana diversa.

Fecha/lugar convencionales, discutibles.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/12-bounded-community-aid-ephesus/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: 1 Corinthians addresses multiple community disputes and practices at Corinth.

ES: 1 Corintios aborda diversas disputas y prácticas comunitarias en Corinto.

[Consulted source](https://www.biblegateway.com/passage/?search=1+Corinthians&version=NRSVUE): 1 Corinthians 1–16: Paul addresses factions, food, lawsuits, worship, gifts, collection and resurrection in a community he addresses as Corinth.

Limit: Primary letter supports the topics but not the selection's c.54–55 date or Ephesus writing location by itself. OUP abstract is not full-text evidence and should be described only as abstract consulted.

Status: consulted

[Additional consulted passage](https://www.biblegateway.com/passage/?search=1+Corinthians+16%3A5-9&version=NRSVUE): 1Cor16:5–9;16:8 stated stay at Ephesus

Limit: Direct authorial statement; exact date and archaeological house not established. Source concerns addressed Corinthian community; playable local Ephesian network fictional.

### 13. Words for a Distant City

[Candidate source](https://academic.oup.com/book/3544): Oxford abstract; Romans 16

Research candidate (not yet approved narration): Pablo escribe Romanos y describe una comunidad que no fundó.

La fecha y ubicación se reconstruyen por indicios internos.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/13-consignment-and-correspondence-corinth/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Romans 16 attests a network of people and communities in Rome and Phoebe's connection to Cenchreae; Paul says he had not yet visited Rome.

ES: Romanos 16 acredita una red de personas y comunidades en Roma y el vínculo de Febe con Cencreas; Pablo dice que aún no había visitado Roma.

[Consulted source](https://www.biblegateway.com/passage/?search=Romans+16&version=NRSVUE): Romans 16: Paul commends Phoebe of Cenchreae, greets multiple named people, and mentions a house-church; Romans 1:13 says Paul had often intended to visit Rome.

Limit: It does not itself give composition date/place. Corinth is a scholarly inference; the dossier's Oxford source was an abstract only. The claim 'community he did not found' is supported by Romans 1:13, not chapter 16 alone.

Status: consulted

### 14. The Appeal Beside the Sea

[Candidate source](https://www.perseus.tufts.edu/hopper/text?doc=Acts+21): Acts 21–26, texto antiguo consultable

Research candidate (not yet approved narration): Pablo es detenido tras tensiones en Jerusalén y apela al emperador según Hechos.

Relato de Hechos no equivale a registro judicial independiente.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/14-administrative-intrigue-caesarea/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: In Acts' narrative, Paul appeals to Caesar before Festus while held at Caesarea.

ES: En el relato de Hechos, Pablo apela al César ante Festo mientras está detenido en Cesarea.

[Corrected primary passage](https://www.biblegateway.com/passage/?search=Acts%2025%3A10-12&version=NRSVUE): Acts 25:10–12, appeal to Caesar; Acts 21–26 supplies the narrative setting. Acts is a literary narrative composed later, not a verbatim court transcript; local courier story is fiction.

[Consulted source](https://www.biblegateway.com/passage/?search=Acts+25%3A10-12&version=NRSVUE): Acts 25:10–12: Paul invokes his appeal to Caesar before Festus; Acts 21–26 gives the preceding detention narrative.

Limit: This is a theological narrative, not a surviving court transcript. The appeal passage supports the appeal, not every claim about causes, dates, or legal procedure; use Caesarea as scene, not Jerusalem after departure.

Status: consulted

### 15. Ash over the Seven Hills

[Candidate source](https://www.perseus.tufts.edu/hopper/text?doc=Tac.+Ann.+15.44): Tacitus, Annals 15.44

Research candidate (not yet approved narration): Tras el incendio de Roma, Nerón castiga a cristianos en la ciudad, según Tácito.

Testimonio romano retrospectivo y hostil; no persecución imperial general.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/15-evacuation-and-recovery-rome-ostia/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Tacitus reports that after the Rome fire Nero punished people called Christians and describes Christus' execution under Pilate.

ES: Tácito informa de que, tras el incendio de Roma, Nerón castigó a personas llamadas cristianas y describe la ejecución de Christus bajo Pilato.

[Consulted source](https://dcc.dickinson.edu/tacitus-annals/15-44): Tacitus, Annals 15.44, relating the Rome fire, Nero's response, and punishments of Christians; DCC notes source limits and comparison with Suetonius/Pliny.

Limit: Tacitus wrote decades later and is not an eyewitness to the punishment. His account does not prove Christians caused the fire; indeed he portrays the arson charge as a scapegoating measure. No separately documented evacuation/recovery episode.

Status: consulted

### 16. A Story in the Shadow of War

[Candidate source](https://academic.oup.com/book/3544): Oxford abstract; Gospel of Mark

Research candidate (not yet approved narration): Marcos transmite una narración sobre Jesús en contexto de guerra y crisis del Segundo Templo.

Datación y lugar siguen debatidos.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/16-comparative-copying-antioch/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The Gospel of Mark presents a narrative about Jesus and locates its opening in a Second Temple Jewish setting.

ES: El Evangelio de Marcos presenta un relato sobre Jesús y sitúa su comienzo en el contexto judío del Segundo Templo.

[Consulted source](https://www.biblegateway.com/passage/?search=Mark+1&version=NRSVUE): Mark 1:1–15 as opening and narrative evidence for the Gospel's representation of Jesus; Oxford title page is metadata/abstract only, not full-text chapter evidence.

Limit: Mark's date is commonly placed around the Jewish War but debated; text does not identify its author or place of composition. Do not state that this source proves it was written during the war or in Antioch.

Status: disputed

[Additional consulted passage](https://www.biblegateway.com/passage/?search=Mark+1&version=NRSVUE): Mark1; architect read chapter and footnotes

Limit: Textual opening and attributed ministry narrative; not composition date/place, local Antioch manuscript, or proof of every miracle.

### 17. The Names Beyond the Siege

[Candidate source](https://www.livius.org/articles/place/jerusalem/jerusalem-70/): Josephus, Jewish War 6; síntesis de Livius

Research candidate (not yet approved narration): Las legiones romanas destruyen el Templo de Jerusalén tras la revuelta.

Josefo participó en la guerra y escribe bajo patronazgo romano.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/02-after-the-siege/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Josephus narrates the Roman capture and destruction of the Jerusalem Temple in 70 CE.

ES: Josefo narra la toma romana y destrucción del Templo de Jerusalén en el año 70.

[Consulted source](https://www.livius.org/articles/place/jerusalem/jerusalem-70/): Livius summary explicitly cites Josephus, Jewish War 6; primary source locator: Josephus, War 6.4.5–7.1.1 (Temple fire/destruction and capture).

Limit: Josephus is a near-contemporary participant writing under Roman patronage; casualty totals and speeches are rhetorically shaped. Livius is a secondary summary, not the primary source itself.

Status: consulted

[Additional consulted passage](https://earlyjewishwritings.com/text/josephus/war6.html): Jewish War VI.4.5–7, temple fire; VI.1.1 landscape description

Limit: Whiston translation consulted, not a Greek critical text. Fire chain and Titus’ intent favor Roman command; speeches, theology and casualty figures are not neutral proof or demographic counts. Regional tree-clearance language is not a precise vegetation raster.

[Additional consulted passage](https://earlyjewishwritings.com/text/josephus/war7.html): Jewish War VII.1.1–2, demolition, surviving towers/west wall and garrison

Limit: Demolition and Tenth Legion presence narrated; no local ten-household escape, patrol number, route or permission is documented. Dramatic extent and speeches remain attributed.

[Additional consulted passage](https://www.newadvent.org/fathers/250103.htm): Ecclesiastical History III.5.3–4, later Pella report

Limit: Fourth-century account reports departure before war, not a contemporary post-fall evacuation record. Revelation and divine/collective punishment rhetoric are attributed authorial claims and never neutral causation. Pella is outside this map.

[Source-audit passage](https://penelope.uchicago.edu/josephus/war-6.html): Josephus, Jewish War VI, especially §§4–5 (temple fire and fall); Book VI chronology

Josephus narrates Roman capture/destruction of the Temple in Jerusalem in 70, including the 10th of Lous/Av as the day the fire began in his version.

Limit: The exact accidental/command chain behind the fire is disputed in the narrative itself; Josephus is a participant writing under Flavian patronage and frames culpability. Do not narrate his theological causation as fact.

Coverage: Opened translation; read Book VI siege/fire passage and editorial notes. Translation is Whiston, not Greek apparatus.

### 18. Two Voices, Unfinished Margins

[Candidate source](https://academic.oup.com/book/3544): Oxford abstract; evangelios

Research candidate (not yet approved narration): Mateo y Lucas reelaboran tradiciones sobre Jesús para comunidades distintas.

No se fija el lugar como hecho.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/18-parallel-archive-logistics-antioch/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Matthew and Luke preserve distinct narrative presentations of Jesus; their texts can be compared for differing genealogies and infancy narratives.

ES: Mateo y Lucas conservan presentaciones narrativas distintas de Jesús; sus textos permiten comparar genealogías y relatos de infancia diferentes.

[Consulted source](https://www.biblegateway.com/passage/?search=Matthew+1&version=NRSVUE): Matthew 1 and Luke 1 as distinct narrative openings; Oxford resource supplied only as abstract/metadata, not evidence for audience reconstruction.

Limit: The claim that they were tailored for distinct communities is scholarly inference; neither texts nor Oxford abstract consulted here proves specific communities or provenance in Antioch.

Status: disputed

[Additional consulted passage](https://www.biblegateway.com/passage/?search=Matthew+1&version=NRSVUE): Matthew1; architect read genealogy and birth narrative

Limit: Different textual genealogy; not proof of a specific Antioch audience or authorial location.

[Additional consulted passage](https://www.biblegateway.com/passage/?search=Luke+3:23-38&version=NRSVUE): Luke3:23–38; architect read displayed genealogy and footnotes

Limit: Genealogy differs fromMatthew1; no harmonization, audience/place inference or use of modern translation as physical ancient object.

### 19. The House Before the Road

[Candidate source](https://www.earlychristianwritings.com/didache.html): Didache, texto y notas de datación

Research candidate (not yet approved narration): La Didaché conserva instrucción comunitaria, ética, bautismo y organización itinerante.

Fecha y lugar amplios; texto compuesto.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/19-hospitality-network-antioch/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The Didache contains instructions on baptism, communal prayer, itinerant teachers, and local leadership.

ES: La Didaché contiene instrucciones sobre bautismo, oración comunitaria, maestros itinerantes y liderazgo local.

[Consulted source](https://www.earlychristianwritings.com/didache.html): Didache, especially chapters 7 (baptism), 9–10 (prayers), 11–13 (itinerant teachers/prophets), and 14–15 (assembly and local officers); academic discussion of composite date and provenance consulted via Cambridge HTR abstract.

Limit: Its date and place of composition remain disputed; Syrian provenance is a proposal, not established fact. The earlychristianwritings page is an edition/translation resource, while the Cambridge source is abstract only.

Status: consulted

[Additional consulted passage](https://www.earlychristianwritings.com/text/didache-hoole.html): Didache11–13; architect read itinerant/settled visitor instructions

Limit: Normative text, not universal practice or securely dated Antioch institution; text not copied verbatim into player dialogue.

### 20. A Letter Across the Divide

[Candidate source](https://www.earlychristianwritings.com/1clement.html): 1 Clement, texto

Research candidate (not yet approved narration): 1 Clemente interviene en conflicto de liderazgo en Corinto desde la iglesia de Roma.

La datación alrededor de 96 es aproximada.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/20-reconciliation-deliveries-rome-ostia/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: 1 Clement is a Roman church's letter urging reconciliation in a leadership conflict at Corinth.

ES: 1 Clemente es una carta de la iglesia de Roma que pide reconciliación en un conflicto de liderazgo en Corinto.

[Consulted source](https://www.earlychristianwritings.com/1clement.html): 1 Clement 1–3 and 47–59: letter addresses the Corinthian church, laments dissension and removal of presbyters, and urges restoration.

Limit: The opening directly identifies the Roman sender and Corinthian addressee. The text does not name Clement as author; c.95 is conventional and not stated in the letter. A particular Roman copying address remains fiction.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/1010.htm): 1Clement opening and44–48; architect read sender/addressee, ministers removed and appeal for concord

Limit: Author unnamed in the text, datec95 conventional; advocacy not proof of restored peace or exact Roman writing address. This older translation/page numbers differ from some modern chapter divisions; no authentic dialogue or manuscript placed.

### 21. The Governor's Question

[Candidate source](https://faculty.georgetown.edu/jod/texts/pliny.html): Pliny, Letters 10.96–97

Research candidate (not yet approved narration): Plinio consulta a Trajano sobre juicios a cristianos y describe reuniones antes del alba.

Correspondencia provincial; no prueba política uniforme.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/03-the-governors-question/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Pliny asks Trajan about proceedings against accused Christians and reports their pre-dawn meeting and practices.

ES: Plinio consulta a Trajano sobre los procesos contra acusados de cristianismo e informa de sus reuniones antes del alba y prácticas.

[Consulted source](https://faculty.georgetown.edu/jod/texts/pliny.html): Pliny, Letters 10.96–97: Pliny asks Trajan how to handle accused Christians; reports morning meeting, ethical pledge, and meal; Trajan replies not to seek them out.

Limit: Governor's correspondence, not a neutral ethnography; evidence is for Bithynia-Pontus, not a general empire-wide policy. c.112 is inferred from correspondence chronology.

Status: consulted

[Additional consulted passage](https://faculty.georgetown.edu/jod/texts/pliny.html): Pliny, Letters10.96–97; architect read both complete displayed letters

Limit: Governor correspondence and attributed interrogated testimony, not neutral ethnography; executions/torture not playable choices. Trajan does not grant religious liberty or general uniform rules. Local Nicomedia activity and receipt are fiction, not an attested tribunal or emperor reply.

### 22. Bread Read Aloud

[Candidate source](https://www.newadvent.org/fathers/0126.htm): Justin, First Apology 65–67

Research candidate (not yet approved narration): Justino enseña y escribe defensas cristianas en Roma; describe lectura y colectas dominicales.

Apología normativa, no censo de práctica.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/22-reading-and-relief-rome-ostia/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Justin describes Sunday gatherings, readings, prayer, Eucharist, and collections for people in need.

ES: Justino describe reuniones dominicales, lecturas, oración, eucaristía y colectas para personas necesitadas.

[Consulted source](https://www.newadvent.org/fathers/0126.htm): Justin, First Apology 65–67, especially 67: Sunday assembly, apostolic memoirs/prophets read, instruction, prayer, bread/wine, collection for those in need.

Limit: The passage describes Christian practice in general terms; it does not itself establish Justin's teaching location or prove these exact practices were unique to Rome. Apologetic self-description, not a neutral census.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/0126.htm): Justin, First Apology65–67; architect read rites, reading and giving descriptions

Limit: Apologetic self-description, not a universal census or precise Roman congregation address. Ordinary local reading-work notes and household logistics are fictional, theological assertions not objective facts or mechanical meters.

### 23. A Petition from Sardes

[Candidate source](https://www.earlychristianwritings.com/melito.html): Melito, Apology fragments

Research candidate (not yet approved narration): Melitón de Sardes denuncia medidas contra cristianos ante Marco Aurelio.

Fragmentario; fecha aproximada.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/23-petition-escort-sardes/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Eusebius preserves fragments of a work attributed to Melito and addressed to an emperor, arguing that Christian teaching had benefited the empire.

ES: Eusebio conserva fragmentos de una obra atribuida a Melitón y dirigida a un emperador, donde sostiene que la enseñanza cristiana benefició al imperio.

[Consulted source](https://jerihna.sourceschretiennes.org/en/work-editions/apologia-ad-marcum-aurelium-/oxford-early-christian-texts): Melito, Apology fragments preserved at Eusebius, Ecclesiastical History 4.26.5–11; source record gives fragment provenance and bibliographic editions.

Limit: The fragment does not simply 'denounce measures' in the form asserted by the candidate; it asks the emperor to examine recent anti-Christian measures and appeals to imperial justice. The surviving text is fragmentary, mediated by Eusebius, and date/address details are debated.

Status: disputed

[Additional consulted passage](https://en.wikisource.org/wiki/Nicene_and_Post-Nicene_Fathers:_Series_II/Volume_I/Church_History_of_Eusebius/Book_IV/Chapter_26): HEIV26.5–11; architect read appeal, alleged plundering, request to examine measures and rhetoric of imperial favor

Limit: Old public-domain translation mediated by Eusebius; fragmentary advocacy, no proved answer, repeal or exact local address. New Advent bookIV repeatedly timed out; not claimed as consulted full text.

### 24. The River Kept Their Names

[Candidate source](https://www.newadvent.org/fathers/250106.htm): Eusebius, HE 5.1

Research candidate (not yet approved narration): Violencia y procesos contra cristianos de Lyon y Vienne quedan en carta preservada por Eusebio.

Relato martirial y memoria comunitaria; escala local.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/24-witness-and-evacuation-lyon/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Eusebius preserves a letter reporting trials and violence against Christians at Lyon and Vienne.

ES: Eusebio conserva una carta que informa de procesos y violencia contra cristianos en Lyon y Vienne.

[Corrected primary passage](https://www.newadvent.org/fathers/250105.htm): Eusebius, Ecclesiastical History V.1, transmitted letter of the communities of Lyon and Vienne. The letter is preserved in a later ecclesiastical history; theological explanations and miracles are attributed to the source, not objective causation.

[Consulted source](https://www.newadvent.org/fathers/250105.htm): Eusebius, Ecclesiastical History 5.1: preserved letter from Christians of Vienne and Lugdunum to Asian and Phrygian communities; narratives of arrest, trial, and deaths.

Limit: Eusebius is later than the events and transmits a community letter; date 177 is inferred. The letter has theological rhetoric, visions and miracles that must remain source-attributed, not asserted as verified events.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/250105.htm): HEV1.1–63; architect read communal letter, arrests, interrogations, deaths of Pothinus/Blandina/Ponticus and destruction of remains

Limit: Letter transmitted by later historian. Religious explanations, healing and private motives remain attributed, not neutral causation. Household convoy and local work notes are declared fiction; no historical martyr rescue or recovered ashes.

### 25. Voices Against the Fragments

[Candidate source](https://www.newadvent.org/fathers/0103.htm): Irenaeus, Against Heresies

Research candidate (not yet approved narration): Ireneo compone Contra las herejías y describe redes episcopales y debates sobre tradición.

Polemista contra grupos rivales.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Authored episode dossier](episodes/25-archive-comparison-lyon/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Irenaeus' polemic argues from inherited teaching and episcopal succession, using Rome as an example.

ES: La polémica de Ireneo argumenta desde la enseñanza heredada y la sucesión episcopal, y usa Roma como ejemplo.

[Consulted source](https://www.newadvent.org/fathers/0103.htm): Irenaeus, Against Heresies 3.3.2–3: Roman episcopal succession argument; Book I preface and Book III identify polemical target and tradition claims.

Limit: This is a theological polemic, not a neutral account of all communities or uncontested institutional history. It supports debate over authority/tradition, not a specific Lyon archival event; composition c.180–200 is external dating.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/0103303.htm): Against HeresiesIII3.1–4; architect read succession argument, Roman example and attributed memories of Polycarp

Limit: Polemical advocacy, not neutral ethnography or independent consensus; exact Lyon archival exercise and opponent quotations are not documented. Local two-register comparison is fictional and awards no doctrinal truth.

### 26. The Advocate's Harbour

[Candidate source](https://tertullian.org/works/apologeticum.htm): Apologeticum, prólogo y capítulos 39–42

Research candidate (not yet approved narration): Tertuliano escribe una Apología que denuncia condenas sin investigación y expone prácticas comunitarias.

Defensa retórica, no descripción neutral.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Tertullian protests condemnation without inquiry and describes communal worship and care practices.

ES: Tertuliano protesta contra condenas sin investigación y describe culto comunitario y prácticas de asistencia.

[Consulted source](https://www.tertullian.org/works/apologeticum.htm): Tertullian, Apologeticum prologue §§1–3 on uninvestigated condemnation; ch.39 on Christian assembly/charity and chs.40–42 on social practice.

Limit: The Apology is forensic rhetoric and advocacy, not a neutral legal register. The selection's c.197 date is conventional; ch.39 does not prove specific locations or every practice across Christians.

Status: consulted

### 27. What the Record Cannot Hold

[Candidate source](https://www.earlychristianwritings.com/text/perpetua.html): Passion of Perpetua and Felicity

Research candidate (not yet approved narration): Perpetua y Felicidad son ejecutadas; su pasión conserva memoria de mujeres cristianas.

Texto compuesto; fecha cercana al evento, autoría discutida.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: The Passion preserves a near-contemporary Christian account of Perpetua and Felicity's imprisonment and execution at Carthage.

ES: La Pasión conserva un relato cristiano cercano a los hechos sobre el encarcelamiento y ejecución de Perpetua y Felicidad en Cartago.

[Consulted source](https://www.earlychristianwritings.com/text/perpetua.html): Passion of Perpetua and Felicity §§3–10 (first-person prison visions) and §§16–21 (trial/execution); page introduction dates event 203.

Limit: The work has a complex literary/redactional history and theological vision material; date 203 is conventional and the page's introductory header is secondary. Treat visions as the text's claims, not verified supernatural events.

Status: consulted

### 28. The Seal on the Certificate

[Candidate source](https://www.papyrology.ox.ac.uk/POxy/): P.Oxy. 1464 y otros libelli

Research candidate (not yet approved narration): Decio exige sacrificios públicos; certificados egipcios documentan cumplimiento individual.

La aplicación varió localmente; papiros son testimonio regional.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: A surviving Egyptian certificate records a household's sacrifice during Decius' reign, demonstrating documentary compliance with a sacrifice requirement.

ES: Un certificado egipcio conservado registra el sacrificio de una familia durante el reinado de Decio y documenta el cumplimiento de un requisito sacrificial.

[Consulted source](https://searcharchives.bl.uk/catalog/040-002105490): British Library Archives catalogue, Papyrus 2457 / P.Oxy. XII 1464 description: a libellus records Aurelius Gaion, wife, and children performing sacrifice and libation before officials at Oxyrhynchus under Decius.

Limit: The papyrus records this named household only; it does not prove a uniform empire-wide edict or universal enforcement, nor persecution of Christians specifically. Official catalog describes artifact; earlier P.Oxy project URL is broad and did not establish P.Oxy.1464.

Status: consulted

### 29. A Harbour Under Orders

[Candidate source](https://www.newadvent.org/fathers/050602.htm): Cyprian, Epistles 80–81

Research candidate (not yet approved narration): Valeriano ordena medidas contra clero y élites cristianas; Cipriano muere en Cartago.

Cartas cristianas comprometidas; alcance regional.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Cyprian reports Valerian's anti-clerical order and Roman executions; Pontius narrates Cyprian's arrest, sentence, and execution at Carthage.

ES: Cipriano informa de la orden de Valeriano contra el clero y de ejecuciones en Roma; Poncio narra el arresto, sentencia y ejecución de Cipriano en Cartago.

[Corrected primary passage](https://www.newadvent.org/fathers/050681.htm): Cyprian, Epistle 81 in this edition (80 in some editions), to Successus, §§1–2. Reports the Valerian rescript and Roman executions; does not itself document Cyprian’s own execution.

[Corrected primary passage](https://www.newadvent.org/fathers/0505.htm): Pontius, Life and Passion of Cyprian, §§15–18. Near-contemporary hagiographic witness tradition; visions, divine causes and exemplary characterization remain attributed, not agnostic-narrator facts.

[Consulted source](https://www.newadvent.org/fathers/050681.htm): Cyprian, Epistle 81 §§1–2 (New Advent numbering; also catalogued as Epistle 80): report of Valerian's rescript and executions at Rome; for Cyprian's own arrest/sentence/death consult Pontius, Life and Passion §§15–18, https://www.newadvent.org/fathers/0505.htm.

Limit: The letter does not itself attest Cyprian's own death; Pontius' near-contemporary Life/Passion is hagiographic and presents providential framing. Exact 257–258 sequence reconstructed from multiple sources; distinguish exile/first edict from execution under second edict.

Status: consulted

### 30. A Different Dawn

[Candidate source](https://www.newadvent.org/fathers/250108.htm): Eusebius, HE 8

Research candidate (not yet approved narration): La Gran Persecución destruye iglesias y textos y exige sacrificios, con aplicación desigual.

Eusebio escribe como superviviente; intensidad diversa por región.

Knowledge: fictional personal local experience plus sourced reports from other regions. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Eusebius records the Great Persecution's measures against churches and Christian texts and reports punishments in several provinces.

ES: Eusebio registra medidas de la Gran Persecución contra iglesias y textos cristianos, e informa de castigos en varias provincias.

[Consulted source](https://www.newadvent.org/fathers/250108.htm): Eusebius, Ecclesiastical History 8.2–3 and 8.5: orders against churches/scriptures and subsequent punishments, with Eusebius' explicitly Christian narrative frame.

Limit: Eusebius is a Christian historian and his rhetoric interprets events providentially; implementation differed by region and date. This source does not document a specific Milan archive or single uniform local event, nor all the 303–313 range.

Status: consulted
