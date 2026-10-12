# Embers of the Covenant / Las brasas de la alianza

`faith-origins` · CDF-C00 · 30 selected episodes · source locale`en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

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
    "sourceAuditStatus": "candidate chronologies reviewed for errors; individual episode historical approval pending",
    "coreMechanicPolicy": "at least four mission-core families in each odyssey; no more than two consecutive identical core families without authored reason; side-objective variety does not excuse identical main missions",
    "selectedEpisodeCount": 30,
    "selectionNotes": [
      "The two Jerusalem meeting candidates 0/30 are consolidated; their identification remains disputed.",
      "The disputed imprisonment-letter candidate 7 is contextual evidence, not an extra mission.",
      "Repeated copying families are separated by civic rescue, provisioning, production, legal procedure and hospitality; complete gameplay contracts remain pending.",
      "Act targets are editorial guides: this selection follows sourced chronology rather than forcing six episodes into every act.",
      "Milano313is a local fictional archive setting; do not claim every prior persecution took place inMilan."
    ]
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
| 6 / 01-roads-of-antioch | Letters on the Orontes / Cartas sobre el Orontes | c. 40–50 CE; local courier reconstruction | antioch | network-escort |
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

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 2. When the City Held Its Breath

[Candidate source](https://www.perseus.tufts.edu/hopper/text?doc=Tac.+Ann.+15.44): Tacitus, Annals 15.44; Cambridge, ‘Dating the Death of Jesus’ (discute el 30 preferido por muchos y la imposibilidad de recuperar fecha exacta): https://www.cambridge.org/core/journals/new-testament-studies/article/dating-the-death-of-jesus-memory-and-the-religious-imagination/0458FC0CA55BEF810BCC411AC2765860

Research candidate (not yet approved narration): Fuentes cristianas sitúan la ejecución de Jesús bajo Pilato; Tacito, décadas después, también atribuye su ejecución a Pilato bajo Tiberio.

Tacito escribe a comienzos del siglo II, no es testigo. El rango 30–33 es estimación moderna; no incorporar resurrección o milagros como hechos verificables.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 3. A Table in Jerusalem

[Candidate source](https://www.biblegateway.com/passage/?search=Galatians+1%3A18-19&version=NIV%3BNRSVUE%3BKJV%3BNKJV): Pablo, Gálatas 1:18–19; su visita ocurrió ‘después de tres años’, según su propio cómputo.

Research candidate (not yet approved narration): Tras la muerte de Jesús, un grupo de seguidores permanece en Jerusalén; Pablo más tarde recuerda allí a Cefas y a Santiago, hermano del Señor.

La carta es testimonio retrospectivo de Pablo. No permite reconstruir tamaño, estructura o uniformidad de la comunidad.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 4. The Road He Remembered

[Candidate source](https://www.biblegateway.com/passage/?search=Galatians+1&version=NIV): Pablo, Gálatas 1:13–17; fecha aproximada contextualizada por Cambridge, Dating the Death of Jesus, y la cronología paulina anclada en Galión.

Research candidate (not yet approved narration): Pablo recuerda que pasó de perseguir a los grupos seguidores de Jesús a proclamarlos; describe su cambio como una revelación recibida, en sus propios términos.

‘Revelación’ es la descripción autobiográfica de Pablo, no una afirmación historiográfica sobre una aparición sobrenatural. El año exacto de su cambio no puede fijarse.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Paul describes a revelation of Christ and a commission to proclaim him among the Gentiles; his account does not supply a complete itinerary.

ES: Pablo describe una revelación de Cristo y el encargo de anunciarlo entre los gentiles; su relato no ofrece un itinerario completo.

### 5. Fifteen Days, Many Voices

[Candidate source](https://www.biblegateway.com/passage/?search=Galatians+1%3A18-19&version=NIV%3BNRSVUE%3BKJV%3BNKJV): Pablo, Gálatas 1:18–19; Yale Bible Study, Paul’s chronology anchored by the Delphi/Gallio inscription: https://yalebiblestudy.org/courses/acts-of-the-apostles/lessons/co-operative-ministry-study-guide/

Research candidate (not yet approved narration): Pablo visita Jerusalén y se entrevista con Cefas y Santiago; afirma que permaneció allí quince días.

El intervalo ‘tres años’ admite cómputos inclusivos distintos y la fecha de la llamada de Pablo es incierta. Gálatas es una carta polémica escrita para defender su autoridad.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 6. Letters on the Orontes

[Candidate source](https://www.biblegateway.com/passage/?search=Galatians+2&version=NIV): Pablo, Gálatas 2:11–14; Yale Divinity School, commentary on Galatians 1–2: https://divinity.yale.edu/sites/default/files/galatians-1-2.pdf

Research candidate (not yet approved narration): Pablo describe comunidades mixtas y una disputa de mesa en Antioquía: Cefas deja de comer con gentiles cuando llegan enviados relacionados con Santiago.

Sólo poseemos aquí la narración de Pablo; no sabemos el desenlace ni podemos igualar sin argumento este incidente con la reunión de Hechos 15.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 7. The Doors That Closed

[Candidate source](https://lexundria.com/suet_cl/25.4/r): Suetonius, Claudius 25.4; Cambridge Companion to the Age of Nero contextualiza probablemente ca. 49: https://doi.org/10.1017/9781107280489.016

Research candidate (not yet approved narration): Suetonio informa que Claudio expulsó de Roma a judíos implicados en disturbios ‘impulsore Chresto’; el pasaje puede reflejar conflicto dentro de comunidades judías y cristianas incipientes.

Suetonio no explica quién fue Chrestus; la identificación con Christus/Jesús es una hipótesis, no un dato explícito. La fecha exacta de la expulsión se discute.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 8. A Place for the Stranger

[Candidate source](https://academic.oup.com/edited-volume/37088/chapter/323184625): Oxford Handbook, Chronology; Hechos 15 / Gálatas 2

Research candidate (not yet approved narration): La asamblea de Jerusalén discute la admisión de gentiles y la circuncisión.

La relación entre las versiones de Hechos y Pablo es debatida.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 9. The Weaver's Harbour

[Candidate source](https://dcc.dickinson.edu/greek-new-testament/acts/18): Acts 18; ancla cronológica: inscripción de Galión en Delfos

Research candidate (not yet approved narration): Pablo establece una comunidad en Corinto y trabaja con Prisca y Aquila.

La fecha depende de reconstrucción; Hechos es narrativa teológica.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 10. Before the First Letter Faded

[Candidate source](https://academic.oup.com/book/3544): Oxford, New Testament Christianity in the Roman World, abstract consulted

Research candidate (not yet approved narration): Pablo escribe 1 Tesalonicenses, uno de los textos cristianos conservados más tempranos.

Ciudad de composición probable, no segura.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 11. The Argument Across the Water

[Candidate source](https://www.bibleodyssey.org/articles/galatians/): Society of Biblical Literature, Galatians overview

Research candidate (not yet approved narration): La carta a los Gálatas evidencia disputa sobre identidad, ley y pertenencia gentil.

Lugar y fecha dependen de la hipótesis sobre destinatarios.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 12. Many Hands in One House

[Candidate source](https://academic.oup.com/book/3544): Oxford abstract; 1 Corinthians 1–16

Research candidate (not yet approved narration): Pablo escribe 1 Corintios y responde a conflictos y prácticas de una comunidad urbana diversa.

Fecha/lugar convencionales, discutibles.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 13. Words for a Distant City

[Candidate source](https://academic.oup.com/book/3544): Oxford abstract; Romans 16

Research candidate (not yet approved narration): Pablo escribe Romanos y describe una comunidad que no fundó.

La fecha y ubicación se reconstruyen por indicios internos.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 14. The Appeal Beside the Sea

[Candidate source](https://www.perseus.tufts.edu/hopper/text?doc=Acts+21): Acts 21–26, texto antiguo consultable

Research candidate (not yet approved narration): Pablo es detenido tras tensiones en Jerusalén y apela al emperador según Hechos.

Relato de Hechos no equivale a registro judicial independiente.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Corrected primary passage](https://www.biblegateway.com/passage/?search=Acts%2025%3A10-12&version=NRSVUE): Acts 25:10–12, appeal to Caesar; Acts 21–26 supplies the narrative setting. Acts is a literary narrative composed later, not a verbatim court transcript; local courier story is fiction.

### 15. Ash over the Seven Hills

[Candidate source](https://www.perseus.tufts.edu/hopper/text?doc=Tac.+Ann.+15.44): Tacitus, Annals 15.44

Research candidate (not yet approved narration): Tras el incendio de Roma, Nerón castiga a cristianos en la ciudad, según Tácito.

Testimonio romano retrospectivo y hostil; no persecución imperial general.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 16. A Story in the Shadow of War

[Candidate source](https://academic.oup.com/book/3544): Oxford abstract; Gospel of Mark

Research candidate (not yet approved narration): Marcos transmite una narración sobre Jesús en contexto de guerra y crisis del Segundo Templo.

Datación y lugar siguen debatidos.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 17. The Names Beyond the Siege

[Candidate source](https://www.livius.org/articles/place/jerusalem/jerusalem-70/): Josephus, Jewish War 6; síntesis de Livius

Research candidate (not yet approved narration): Las legiones romanas destruyen el Templo de Jerusalén tras la revuelta.

Josefo participó en la guerra y escribe bajo patronazgo romano.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

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

### 19. The House Before the Road

[Candidate source](https://www.earlychristianwritings.com/didache.html): Didache, texto y notas de datación

Research candidate (not yet approved narration): La Didaché conserva instrucción comunitaria, ética, bautismo y organización itinerante.

Fecha y lugar amplios; texto compuesto.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 20. A Letter Across the Divide

[Candidate source](https://www.earlychristianwritings.com/1clement.html): 1 Clement, texto

Research candidate (not yet approved narration): 1 Clemente interviene en conflicto de liderazgo en Corinto desde la iglesia de Roma.

La datación alrededor de 96 es aproximada.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 21. The Governor's Question

[Candidate source](https://faculty.georgetown.edu/jod/texts/pliny.html): Pliny, Letters 10.96–97

Research candidate (not yet approved narration): Plinio consulta a Trajano sobre juicios a cristianos y describe reuniones antes del alba.

Correspondencia provincial; no prueba política uniforme.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 22. Bread Read Aloud

[Candidate source](https://www.newadvent.org/fathers/0126.htm): Justin, First Apology 65–67

Research candidate (not yet approved narration): Justino enseña y escribe defensas cristianas en Roma; describe lectura y colectas dominicales.

Apología normativa, no censo de práctica.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 23. A Petition from Sardes

[Candidate source](https://www.earlychristianwritings.com/melito.html): Melito, Apology fragments

Research candidate (not yet approved narration): Melitón de Sardes denuncia medidas contra cristianos ante Marco Aurelio.

Fragmentario; fecha aproximada.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 24. The River Kept Their Names

[Candidate source](https://www.newadvent.org/fathers/250106.htm): Eusebius, HE 5.1

Research candidate (not yet approved narration): Violencia y procesos contra cristianos de Lyon y Vienne quedan en carta preservada por Eusebio.

Relato martirial y memoria comunitaria; escala local.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Corrected primary passage](https://www.newadvent.org/fathers/250105.htm): Eusebius, Ecclesiastical History V.1, transmitted letter of the communities of Lyon and Vienne. The letter is preserved in a later ecclesiastical history; theological explanations and miracles are attributed to the source, not objective causation.

### 25. Voices Against the Fragments

[Candidate source](https://www.newadvent.org/fathers/0103.htm): Irenaeus, Against Heresies

Research candidate (not yet approved narration): Ireneo compone Contra las herejías y describe redes episcopales y debates sobre tradición.

Polemista contra grupos rivales.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 26. The Advocate's Harbour

[Candidate source](https://tertullian.org/works/apologeticum.htm): Apologeticum, prólogo y capítulos 39–42

Research candidate (not yet approved narration): Tertuliano escribe una Apología que denuncia condenas sin investigación y expone prácticas comunitarias.

Defensa retórica, no descripción neutral.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 27. What the Record Cannot Hold

[Candidate source](https://www.earlychristianwritings.com/text/perpetua.html): Passion of Perpetua and Felicity

Research candidate (not yet approved narration): Perpetua y Felicidad son ejecutadas; su pasión conserva memoria de mujeres cristianas.

Texto compuesto; fecha cercana al evento, autoría discutida.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 28. The Seal on the Certificate

[Candidate source](https://www.papyrology.ox.ac.uk/POxy/): P.Oxy. 1464 y otros libelli

Research candidate (not yet approved narration): Decio exige sacrificios públicos; certificados egipcios documentan cumplimiento individual.

La aplicación varió localmente; papiros son testimonio regional.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 29. A Harbour Under Orders

[Candidate source](https://www.newadvent.org/fathers/050602.htm): Cyprian, Epistles 80–81

Research candidate (not yet approved narration): Valeriano ordena medidas contra clero y élites cristianas; Cipriano muere en Cartago.

Cartas cristianas comprometidas; alcance regional.

Knowledge: inherited letters and later sources. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Corrected primary passage](https://www.newadvent.org/fathers/050681.htm): Cyprian, Epistle 81 in this edition (80 in some editions), to Successus, §§1–2. Reports the Valerian rescript and Roman executions; does not itself document Cyprian’s own execution.

[Corrected primary passage](https://www.newadvent.org/fathers/0505.htm): Pontius, Life and Passion of Cyprian, §§15–18. Near-contemporary hagiographic witness tradition; visions, divine causes and exemplary characterization remain attributed, not agnostic-narrator facts.

### 30. A Different Dawn

[Candidate source](https://www.newadvent.org/fathers/250108.htm): Eusebius, HE 8

Research candidate (not yet approved narration): La Gran Persecución destruye iglesias y textos y exige sacrificios, con aplicación desigual.

Eusebio escribe como superviviente; intensidad diversa por región.

Knowledge: fictional personal local experience plus sourced reports from other regions. one local map; uncertain authorial provenance is not asserted by the map; letters travel off-map between regional scenes

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending
