# Keepers of the Unbroken Word / Guardianes de la palabra viva

`jewish-tradition` · CDF-C02 · 30 selected episodes · source locale `en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

[Expanded narrator bible and per-episode knowledge framing](../../design/voices/jewish-tradition.md) — fictional biography; independent approval pending.

```json
{
  "editorial": {
    "campaignTitle": {
      "en": "Keepers of the Unbroken Word",
      "es-ES": "Guardianes de la palabra viva"
    },
    "publicId": "CDF-C02",
    "internalName": "CDF_JewishTradition",
    "sourceLocale": "en",
    "targetEpisodeCount": 30,
    "narratorId": "judith-copyist",
    "personaLens": {
      "en": "Names, disagreements and careful copies",
      "es-ES": "Nombres, desacuerdos y copias cuidadosas"
    },
    "deliveryTone": {
      "en": "dry wit, stubborn patience",
      "es-ES": "humor seco, paciencia obstinada"
    },
    "sequence": [
      {
        "speaker": "collection-narrator",
        "mode": "sober source-qualified historical fact",
        "causePolicy": "attribute motives, miracles and sectarian judgements to their sources; no single moral or theological verdict"
      },
      {
        "speaker": "judith-copyist",
        "mode": "fictional personal interpretation with explicit witness basis"
      }
    ],
    "baselineSemanticIdsPreserved": [
      "01-a-city-of-names",
      "02-the-hill-and-the-school",
      "03-the-river-quarter",
      "04-the-living-margin"
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
        "campaignId": "faith-origins",
        "route": "jewish-perspective"
      }
    ],
    "nextRoutes": [
      {
        "id": "completed",
        "key": "progress.jewish-tradition.completed",
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

## act-1: After the House Fell / Tras la caída de la Casa

Historical year band: [70, 117]. Familias y diversidad pos-Templo; Yavneh no es un concilio canónico universal certificado.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 1 / 01-a-city-of-names | Names beyond the Fallen House / Nombres más allá de la casa caída | 70 CE | jerusalem | civilian-evacuation |
| 2 / 02-refuge-and-school-supply-yavneh | A School without Walls / Una escuela sin murallas | c.70–80 CE | yavneh | refuge-and-school-supply |
| 3 / 03-distributed-study-network-yavneh | The Questions We Carried / Las preguntas que llevábamos | c.80–100 CE | yavneh | distributed-study-network |
| 4 / 04-witness-comparison-yavneh | Words Still under Discussion / Palabras todavía en discusión | c.90–100 CE; later rabbinic traditions | yavneh | witness-comparison |
| 5 / 05-fiscal-record-reconciliation-rome-ostia | The Weight of a Roman Receipt / El peso de un recibo romano | 96 CE; reform scope qualified | rome-ostia | fiscal-record-reconciliation |

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

## act-2: Names in the Wilderness / Nombres en el desierto

Historical year band: [100, 180]. Revuelta, documentación y enseñanza; Akiva no actúa después de su muerte convencional135.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 6 / 06-teaching-record-escort-lod | The Teacher in the Unfinished Line / El maestro en la línea incompleta | c.100–135 CE; Akiva traditionally diesc.135, not150–180 | lod | teaching-record-escort |
| 7 / 07-civilian-refuge-cyrene | Across the Cyrenaican Roads / Por los caminos de Cirenaica | 115–117 CE; local reconstruction | cyrene | civilian-refuge |
| 8 / 08-harbour-supply-and-witnesses-alexandria | The Harbour That Heard the War / El puerto que oyó la guerra | 115–117 CE; Egyptian local reconstruction | alexandria | harbour-supply-and-witnesses |
| 9 / 09-administrative-records-jerusalem | The City's Other Name / El otro nombre de la ciudad | c.130–132 CE; chronology of colonial refoundation disputed | jerusalem | administrative-records |
| 10 / 10-finite-mint-consignments-judean-hills | Silver beneath the Desert Sky / Plata bajo el cielo del desierto | 132–135 CE | judean-hills | finite-mint-consignments |
| 11 / 11-archive-extraction-judean-desert | Letters at the Desert Edge / Cartas en el borde del desierto | 132–135 CE; cave records, not an invented battle | judean-desert | archive-extraction |
| 12 / 12-household-relocation-jerusalem | After the Last Stronghold / Después del último bastión | 135 CE; administrative dates qualified | jerusalem | household-relocation |

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

## act-3: Schools Beyond the River / Escuelas más allá del río

Historical year band: [190, 300]. Mishnah, escuelas y comunidad de Dura; no fijar cierre temprano del Talmud babilónico.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 13 / 02-the-hill-and-the-school | The Hill and the School / La colina y la escuela | c.190–220 CE | galilee | distributed-copy-and-provision |
| 14 / 14-citizenship-copy-and-receipts-galilee | A New Name in the Register / Un nombre nuevo en el registro | 212 CE; local circulation reconstruction | galilee | citizenship-copy-and-receipts |
| 15 / 15-study-and-supply-allocation-galilee | Margins beside the Lake / Márgenes junto al lago | c.220–250 CE | galilee | study-and-supply-allocation |
| 16 / 03-the-river-quarter | The Painted River Quarter / El barrio pintado del río | c.244 CE | dura | artisan-and-river-trade |
| 17 / 17-cross-river-study-logistics-pumbedita | Questions beyond the Euphrates / Preguntas más allá del Éufrates | c.250–300 CE; precise institutional chronology qualified | pumbedita | cross-river-study-logistics |

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

## act-4: Stone, Law, and Memory / Piedra, ley y memoria

Historical year band: [300, 400]. Comunidades palestinas y babilonias, imágenes locales y legislación ambivalente; separar ley y cumplimiento.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 18 / 18-finite-mosaic-works-hammath-tiberias | The Zodiac on the Floor / El zodiaco en el pavimento | 4th century CE; archaeological range, not an exact dedication | hammath-tiberias | finite-mosaic-works |
| 19 / 19-bounded-civilian-withdrawal-sepphoris | The Roads after Diocaesarea / Los caminos después de Diocesarea | 351/352 CE; late partisan reports and scale disputed | sepphoris | bounded-civilian-withdrawal |
| 20 / 20-parallel-text-preservation-galilee | The Arguments beside the Water / Los argumentos junto al agua | c.350–400 CE; compilation process, no single closing date | galilee | parallel-text-preservation |
| 21 / 21-finite-works-and-safe-withdrawal-jerusalem | Foundations That Remained / Cimientos que permanecieron | 363 CE; failed rebuilding initiative | jerusalem | finite-works-and-safe-withdrawal |
| 22 / 22-law-and-community-records-thessalonica | A Boundary Written in Law / Una frontera escrita en la ley | 14 March388 CE | thessalonica | law-and-community-records |
| 23 / 23-petition-and-restoration-records-constantinople | An Order to Protect the Doors / Una orden para proteger las puertas | 29 September393 CE | constantinople | petition-and-restoration-records |
| 24 / 24-epigraphic-donor-logistics-aphrodisias | The Names on Two Faces / Los nombres en dos caras | late4th century CE; dating debated | aphrodisias | epigraphic-donor-logistics |

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

## act-5: The Word Without a Throne / La palabra sin trono

Historical year band: [399, 425]. Privilegios fiscales revocados/restaurados, límites al patriarcado y preservación distribuida; la tradición sigue viva.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 25 / 25-bounded-fiscal-transition-milan | The Sealed Collection / La recaudación sellada | 11 April399 CE | milan | bounded-fiscal-transition |
| 26 / 26-finite-community-construction-huqoq | Stone for the Village / Piedra para la aldea | late4th–early5th century CE; c.400 | huqoq | finite-community-construction |
| 27 / 27-courier-and-account-restoration-rome-ostia | The Receipt Restored / El recibo restituido | 25 July404 CE | rome-ostia | courier-and-account-restoration |
| 28 / 28-authority-and-witness-records-constantinople | An Honour Removed / Un honor retirado | 20 October415 CE | constantinople | authority-and-witness-records |
| 29 / 29-repair-within-restrictions-constantinople | The Existing Doors / Las puertas que ya estaban | 15 February423 CE; CTh16.8.25 | constantinople | repair-within-restrictions |
| 30 / 04-the-living-margin | The Living Margin / El margen vivo | c.425 CE; editorial limit, patriarchate end approximate | galilee | archive-and-final-perspective |

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

### 1. Names beyond the Fallen House

[Candidate source](https://www.livius.org/articles/place/jerusalem/jerusalem-70/): Josephus, Jewish War 6; síntesis de Livius

Research candidate (not yet approved narration): Las legiones romanas destruyen el Templo de Jerusalén tras la revuelta.

Josefo participó en la guerra y escribe bajo patronazgo romano.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/josephus/war-6.html): Josephus, Jewish War VI, especially §§4–5 (temple fire and fall); Book VI chronology

Josephus narrates Roman capture/destruction of the Temple in Jerusalem in 70, including the 10th of Lous/Av as the day the fire began in his version.

Limit: The exact accidental/command chain behind the fire is disputed in the narrative itself; Josephus is a participant writing under Flavian patronage and frames culpability. Do not narrate his theological causation as fact.

Coverage: Opened translation; read Book VI siege/fire passage and editorial notes. Translation is Whiston, not Greek apparatus.

### 2. A School without Walls

[Candidate source](https://www.jewishvirtuallibrary.org/yavneh): Fuentes rabínicas compiladas después; overview

Research candidate (not yet approved narration): Yohanan ben Zakkai y estudiosos se asocian con actividad rabínica en Yavneh.

No presentar como concilio que cerró canon o expulsó cristianos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://cojs.org/tannaitic_literature_-circa_70-3rd_century_ce/): COJS, Tannaitic Literature, lines 23–30: after temple destruction tannaitic activity is associated with Yavneh, Usha, Beth Shearim, Sepphoris; later tradition ties Akiva to Yavneh.

Según el resumen/localizador actualmente atribuido en corpus: Yohanan ben Zakkai y estudiosos se asocian con actividad rabínica en Yavneh.

Limit: The source supports Yavneh as one center of post-destruction transmission, not a dated 70–80 meeting/academy narrative for named Yohanan ben Zakkai. The original Jewish Virtual Library page consulted is an Encyclopaedia Judaica-derived town entry and does not document the academy claim. Avoid implying a formal academy’s exact founding/date.

Coverage: COJS extract lines 19–30 read; JVL Yavneh entry lines 23–30 read. Neither full book nor underlying rabbinic sources read.

### 3. The Questions We Carried

[Candidate source](https://cojs.org/tannaitic_literature_-circa_70-3rd_century_ce/): Literatura tannaita; síntesis académica

Research candidate (not yet approved narration): Las academias y tradiciones legales sostienen vida judía sin templo central.

Las narraciones rabínicas se editaron siglos después.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://cojs.org/tannaitic_literature_-circa_70-3rd_century_ce/): COJS, Tannaitic Literature, lines 19–26.

Según el resumen/localizador actualmente atribuido en corpus: Las academias y tradiciones legales sostienen vida judía sin templo central.

Limit: Broad claim of post-70 oral/legal transmission and divergent views is supported as synthesis; source says materials moved among Yavneh, Usha, Beth Shearim, Sepphoris, not that named institutions or a uniform academy network existed exactly c.80–100.

Coverage: COJS excerpt lines 19–27 read; source is an excerpt from Schiffman, From Text to Tradition, not whole book.

### 4. Words Still under Discussion

[Candidate source](https://czasopisma.kul.pl/index.php/vv/article/view/14060): Artículo sobre el mito del sínodo de Jamnia

Research candidate (not yet approved narration): Debates sobre Eclesiastés y Cantar de los Cantares aparecen en tradiciones rabínicas.

No evidencia de una sesión única ni cierre del canon.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 5. The Weight of a Roman Receipt

[Candidate source](https://www.perseus.tufts.edu/hopper/text?doc=Suet.+Dom.+12): Suetonius, Domitian 12.2; Nerva coin legend FISCI IVDAICI CALVMNIA SVBLATA requires separate numismatic corroboration

Research candidate (not yet approved narration): Nerva advertised the removal of abuse in the Jewish tax; Suetonius describes intrusive enforcement under Domitian.

This corrects candidate66: Claudius25 concerns49, not an event90–110. Select a local fictional fiscal archive; do not claim Nerva abolished the tax. Exact primary and coin pages pending audit.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 6. The Teacher in the Unfinished Line

[Candidate source](https://cojs.org/tannaitic_literature_-circa_70-3rd_century_ce/): Literatura tannaita, visión general

Research candidate (not yet approved narration): Rabí Akiva y colegas transmiten tradiciones legales y litúrgicas tannaitas.

Raw150–180date rejected. Scholarly extract situates teachingc.80–132; complete chronology and martyrdom stories remain attributed.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Rabbinic tradition places Akiva’s teaching before the end of the Bar Kokhba revolt, with his death commonly dated around135; recollections of his teaching were compiled later.

ES: La tradición rabínica sitúa la enseñanza de Akiva antes del final de la revuelta de Bar Kojba y fecha habitualmente su muerte hacia135; los recuerdos de sus enseñanzas se recopilaron después.

[Source-audit passage](https://cojs.org/tannaitic_literature_-circa_70-3rd_century_ce/): COJS, Tannaitic Literature, lines 28–30.

The originally claimed c.150–180 Akiva activity is contradicted by the consulted overview; it places his floruit c.80–132.

Limit: COJS dates Akiva’s floruit around 80–132 CE and says precision about responsibility for the subject-classification system is impossible.

Coverage: Direct extract read; secondary overview, not a primary biographical record.

### 7. Across the Cyrenaican Roads

[Candidate source](https://www.livius.org/articles/concept/jewish-war/jewish-war-115-117/): Dio Cassius 68.32; síntesis de fuentes

Research candidate (not yet approved narration): Revueltas judías de la diáspora sacuden Cirenaica, Egipto y Chipre durante guerra de Trajano.

Cifras antiguas de víctimas no fiables.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.posenlibrary.com/entry/jewish-rebellion-cyrene): Cassius Dio, Roman History 68.32.1–3, Cary translation (entry lines 43–51)

Supports Jewish uprising participation across Cyrene, Egypt, and Cyprus in 115–117 and Roman suppression; Posen reproduces the source passage and cites Loeb.

Limit: Dio survives here as a late author’s account/epitome, with highly charged atrocity claims and suspect casualty numbers; keep those out of factual description. Livius original page can be replaced by this source text and its citation.

Coverage: Read source excerpt, intro and Loeb citation lines 43–51; not full Dio.

### 8. The Harbour That Heard the War

[Candidate source](https://www.livius.org/articles/concept/jewish-war/jewish-war-115-117/): Dio Cassius 68.32; síntesis de fuentes

Research candidate (not yet approved narration): Revueltas judías de la diáspora sacuden Cirenaica, Egipto y Chipre durante guerra de Trajano.

Cifras antiguas de víctimas no fiables.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.posenlibrary.com/entry/jewish-rebellion-cyrene): Cassius Dio, Roman History 68.32.1–3, Cary translation (entry lines 43–51)

Supports Jewish uprising participation across Cyrene, Egypt, and Cyprus in 115–117 and Roman suppression; Posen reproduces the source passage and cites Loeb.

Limit: Dio survives here as a late author’s account/epitome, with highly charged atrocity claims and suspect casualty numbers; keep those out of factual description. Livius original page can be replaced by this source text and its citation.

Coverage: Read source excerpt, intro and Loeb citation lines 43–51; not full Dio.

### 9. The City's Other Name

[Candidate source](https://www.britannica.com/place/Jerusalem/History): Cassius Dio 69.12–14

Research candidate (not yet approved narration): Adriano visita Judea y promueve colonia romana en Jerusalén, según tradición historiográfica.

El vínculo causal directo con la revuelta sigue discutido.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/69%2A.html): Cassius Dio, Roman History 69.12.1–2; English translation excerpt mirrored at Livius

Supports Hadrian’s foundation of Aelia Capitolina at Jerusalem, a Jupiter temple, and Dio’s claimed connection to revolt.

Limit: Dio gives a retrospective causal account; specific foundation date is debated and is not established by this passage alone. Do not treat the sequence as uncontested.

Coverage: Opened Livius translation of Dio 69.12.1–3, checked exact text; primary Perseus/Chicago route available via source link but not separately read.

### 10. Silver beneath the Desert Sky

[Candidate source](https://www.imj.org.il/en/wings/shrine-book/bar-kochba-revolt): Museo de Israel, monedas y documentos

Research candidate (not yet approved narration): Revuelta de Bar Kojba contra Roma; acuñación rebelde y documentos del desierto reflejan administración.

La cronología y nombre del líder dependen de fuentes diversas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.imj.org.il/en/wings/shrine-book/bar-kochba-revolt): Israel Museum, Shrine of the Book, “Bar Kochba Revolt”; cross-check Cassius Dio 69.12–14

Museum overview supports revolt context and material evidence of Bar Kokhba-period documents/coins; Dio 69.12–14 narrates resistance, hideouts and Roman suppression.

Limit: Do not claim a specific document or coin without item-level catalog and findspot. Dio’s account of causation and scale is Roman retrospective narrative.

Coverage: Read museum overview/search-indexed page and Livius-translated Dio 69.12–14 lines 15 onward; not artifact catalog records.

### 11. Letters at the Desert Edge

[Candidate source](https://www.imj.org.il/en/wings/shrine-book/bar-kochba-revolt): Museo de Israel, monedas y documentos

Research candidate (not yet approved narration): Revuelta de Bar Kojba contra Roma; acuñación rebelde y documentos del desierto reflejan administración.

La cronología y nombre del líder dependen de fuentes diversas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.imj.org.il/en/wings/shrine-book/bar-kochba-revolt): Israel Museum, Shrine of the Book, “Bar Kochba Revolt”; cross-check Cassius Dio 69.12–14

Museum overview supports revolt context and material evidence of Bar Kokhba-period documents/coins; Dio 69.12–14 narrates resistance, hideouts and Roman suppression.

Limit: Do not claim a specific document or coin without item-level catalog and findspot. Dio’s account of causation and scale is Roman retrospective narrative.

Coverage: Read museum overview/search-indexed page and Livius-translated Dio 69.12–14 lines 15 onward; not artifact catalog records.

### 12. After the Last Stronghold

[Candidate source](https://www.britannica.com/place/Jerusalem/History): Cassius Dio 69.14; overview

Research candidate (not yet approved narration): Roma derrota la revuelta y reorganiza la provincia como Siria Palestina; acceso judío a Jerusalén queda restringido.

Alcance de prohibición y continuidad local complejos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/69%2A.html): Cassius Dio, Roman History 69.13–14 (Roman suppression; Bar Kokhba war)

Supports Roman forces suppressing a major revolt across Judaea and Dio’s account of postwar restrictions; use his specific claim about Jerusalem only if the relevant 69.14 passage is quoted directly.

Limit: “Syria Palaestina” renaming and Jewish exclusion from Jerusalem need separate direct sources; don’t bundle all consequences from an imprecise Dio locator. Current consulted Livius excerpt covers 69.12–13 only.

Coverage: Read translated Dio 69.12–13; 69.14 remains unchecked in full. Keep the specific province renaming/exclusion detail pending.

### 13. The Hill and the School

[Candidate source](https://academic.oup.com/book/3559/chapter-abstract/144825364): Oxford, The Age of the Talmud

Research candidate (not yet approved narration): Judas ha-Nasi organiza la Mishnah, compilación de tradiciones legales.

Fecha aproximada y grado de autoría/redacción debatidos.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://cojs.org/tannaitic_literature_-circa_70-3rd_century_ce/): COJS, Tannaitic Literature, lines 19–21, 30–33.

Según el resumen/localizador actualmente atribuido en corpus: Judas ha-Nasi organiza la Mishnah, compilación de tradiciones legales.

Limit: Schiffman excerpt states redaction by Judah the Prince around 200 CE and notes scholarly debate about nature/history and degree of his contribution.

Coverage: Direct excerpt read; Oxford chapter link from corpus not accessible in browser, so COJS is substitute contextual source, not replacement for full specialist scholarship.

### 14. A New Name in the Register

[Candidate source](https://www.britishmuseum.org/collection/object/G_1894-10-14-1): Edicto de Caracalla, P.Giss. 40

Research candidate (not yet approved narration): Constitutio Antoniniana extiende ciudadanía romana a la mayoría de habitantes libres; cambia marco jurídico judío.

Excepciones legales y aplicación requieren cautela.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://www.uni-giessen.de/ub/de/ueber-uns/sam/papyri-ostraka-keilschrifttafeln/papyri): Colección de papiros de Giessen: P.Giss. 40 / P.Giss. inv. 15; ver también https://www.constitutio.de/en/papyrus/known-history-of-the-constitutio-antoniniana

P.Giss. 40 es el testimonio papiráceo griego asociado a la Constitutio Antoniniana; emisión convencional 212/213, papiro escrito c.215.

Limit: URL original del British Museum no corresponde a este papiro; el objeto pertenece a la colección universitaria de Giessen. La inscripción textual está severamente fragmentada y su interpretación/relación exacta con el edicto sigue debatida. La ampliación de ciudadanía no debe presentarse como cambio específicamente judío.

Coverage: Leída página de la biblioteca universitaria de Giessen y página del proyecto Constitutio.de sobre historia del objeto y fecha; extracto académico Imrie 2015 sobre el estado fragmentario y debate.

### 15. Margins beside the Lake

[Candidate source](https://academic.oup.com/book/3559/chapter-abstract/144825364): Oxford, The Age of the Talmud

Research candidate (not yet approved narration): Amoraim palestinos discuten y transmiten la Mishnah en círculos de estudio.

Las atribuciones personales de compilaciones no son transcripciones contemporáneas.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://academic.oup.com/book/3559/chapter-abstract/144825364): Catherine Hezser, An Introduction to the History and Sources of Jewish Law, ch. “The Age of the Talmud”, abstract

Supports broad period framing of Palestinian/Babylonian rabbinic scholarship and the Mishnah-to-Talmud transition; it does not support a specific named circle/date or claim that Mishnah was being “transmitted” as an event.

Limit: Abstract only; citation is not evidence for a specific local scene or the full range of Jewish community practice. Phrase as scholarly traditions, not all Jews.

Coverage: Read accessible chapter abstract/search extract, not paywalled chapter.

### 16. The Painted River Quarter

[Candidate source](https://www.iranicaonline.org/articles/dura-europos/): Emplazamiento y arqueología

Research candidate (not yet approved narration): Sinagoga y diversidad material documentadas en Dura-Europos; red comercial del jugador reconstruida. La ciudad no se ubica en orilla izquierda.

Sinagoga y diversidad material documentadas en Dura-Europos; red comercial del jugador reconstruida. La ciudad no se ubica en orilla izquierda.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 17. Questions beyond the Euphrates

[Candidate source](https://academic.oup.com/book/4297): Halivni, Formation of Babylonian Talmud, abstract

Research candidate (not yet approved narration): Centros rabínicos de Babilonia crecen bajo los sasánidas.

Los detalles institucionales proceden de tradiciones posteriores.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://academic.oup.com/book/4297): David Weiss Halivni, The Formation of the Babylonian Talmud, book overview

May support a long-term process of Bavli formation and Babylonian rabbinic activity, but accessible book page does not establish a discrete “growth of centers” event or a dated academy scene.

Limit: Formal Sura/Pumbedita academy institutions are often projected backward from later geonic sources; do not assert a mature institutional network c.4th century from this citation alone.

Coverage: Only book metadata/abstract available, not the protected book; claim remains under-supported.

### 18. The Zodiac on the Floor

[Candidate source](https://cja.huji.ac.il/browser.php?id=644&mode=alone): Hebrew University Center for Jewish Art, object record “Hammath Tiberias Synagogue”; Oxford chapter “Ancient Synagogues in Palestine: An Overview” discusses a fourth-century date and competing early/late-fourth-century datings: https://academic.oup.com/british-academy-scholarship-online/book/57508/chapter/467272283.

Research candidate (not yet approved narration): The synagogue at Hammath Tiberias receives a mosaic floor combining a Torah shrine and menorahs with a zodiac and Helios panel.

The floor is usually dated to the fourth century, but exact dating varies within that century. This is a site-specific artifact and could enrich, rather than duplicate as a separate mission, corpus event 76 on Galilean synagogue mosaics. The imagery is evidence of local visual practice, not proof that all Jews accepted one theology or interpreted Helios literally.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 19. The Roads after Diocaesarea

[Candidate source](https://en.wikisource.org/wiki/Ecclesiastical_history_(Socrates_Scholasticus)/Book_II/Chapter_XXXIII): Socrates Scholasticus, Ecclesiastical History II.33, “Of the Jews inhabiting Dio-Cæsarea in Palestine”; parallel report: Sozomen, Ecclesiastical History IV.7, https://orthodoxchurchfathers.com/fathers/npnf202/npnf2031.html.

Research candidate (not yet approved narration): Rebel forces in Diocaesarea (Sepphoris) and other Palestinian towns are suppressed by Ursicinus during Gallus’s Caesarship.

Socrates and Sozomen are later Christian historians, not contemporary witnesses; their reports differ in framing and likely magnify the episode. Ammianus does not mention it. Sepphoris is named in the account, but exact battle sequence, named leaders, scale, and destruction date should not be asserted as settled.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 20. The Arguments beside the Water

[Candidate source](https://academic.oup.com/book/3559/chapter-abstract/144825364): Oxford, Age of Talmud

Research candidate (not yet approved narration): El Talmud de Jerusalén toma forma a través de generaciones de estudio y edición.

No hay fecha puntual de cierre consensuada.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://academic.oup.com/book/3559/chapter-abstract/144825364): Hezser, “The Age of the Talmud,” abstract

Supports the Jerusalem/Palestinian Talmud as a later halakhic work composed after Mishnah and a period of rabbinic legal activity in the Land of Israel.

Limit: Does not date a final redaction event precisely; broader scholarship treats its formation as complex and chronology uncertain. Avoid saying Tiberias alone authored it or assigning an exact completion year.

Coverage: Abstract only, not chapter text.

### 21. Foundations That Remained

[Candidate source](https://www.livius.org/articles/person/julian-the-apostate/julian-and-the-jews/): Ammianus Marcellinus 23.1.2–3

Research candidate (not yet approved narration): Juliano permite y apoya el proyecto de reconstrucción del Templo de Jerusalén, que se interrumpe.

Fuentes cristianas y paganas divergen sobre causa de interrupción.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/23%2A.html): Ammianus Marcellinus, Res Gestae 23.1.2–3

Supports Julian planned a costly restoration of the Jerusalem Temple under Alypius of Antioch; Ammianus says fiery bursts near foundations halted work and some workers died.

Limit: Ammianus is a contemporary but Christian Roman author; the supernatural explanation is his account, not independently established cause. Do not add “permission to rebuild” as a formal edict unless separately sourced.

Coverage: Opened and read §§2–3 directly; single source passage, no archaeological corroboration consulted.

### 22. A Boundary Written in Law

[Candidate source](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/Thessalonique.htm): Codex Theodosianus 3.7.2; texto latino y fecha fija 14/03/388. Contexto consultado: https://files.znu.edu.ua/files/Bibliobooks/Kushynova/0034719.pdf, sección CTh 3.7.2 / 9.7.5.

Research candidate (not yet approved narration): Una constitución de Teodosio I, Valentiniano II y Arcadio prohíbe el matrimonio entre judíos y cristianos y equipara esa unión con adulterio en la sanción legal.

La ley muestra una frontera jurídica que el poder imperial quiso imponer; su promulgación no demuestra aplicación uniforme ni permite inferir que todos los matrimonios mixtos cesaran.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 23. An Order to Protect the Doors

[Candidate source](https://www.thelatinlibrary.com/theodosius/theod16.shtml): Codex Theodosianus 16.8.9, líneas 817–818 de la página consultada; la constitución ordena al comes y magister militum de Oriente proteger reuniones y sinagogas. Contexto: https://academic.oup.com/book/32151/chapter-abstract/268116920.

Research candidate (not yet approved narration): Teodosio I afirma que el judaísmo no está prohibido por ley y ordena contener a quienes, bajo el nombre del cristianismo, destruyen o saquean sinagogas.

Es una orden normativa, no una medición de cumplimiento. Leída junto con las restricciones de 388 y 423, evidencia políticas imperiales ambivalentes, no tolerancia constante.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 24. The Names on Two Faces

[Candidate source](https://aphrodisias.classics.ox.ac.uk/tr/tr-jewishcom.html): Oxford Aphrodisias Excavations, “Jewish Community List”; inscripción monumental de 2,8 m, descripción de las listas en las líneas 39–41 de la página. Contexto de los problemas de datación: https://archiv.ub.uni-heidelberg.de/propylaeumdok/667/1/Chaniotis_The_Jews_of_Aphrodisias_2002.pdf.

Research candidate (not yet approved narration): Una columna inscrita enumera miembros y benefactores asociados con la comunidad judía local; las dos caras contienen listas de nombres que documentan vida comunitaria y vínculos con la sinagoga.

La página de excavación la atribuye a finales del siglo IV; la bibliografía discute la datación paleográfica y la contemporaneidad de ambas caras. La lista conserva nombres de varones y no equivale a un censo completo de la comunidad.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 25. The Sealed Collection

[Candidate source](https://www.thelatinlibrary.com/theodosius/theod16.shtml): Codex Theodosianus 16.8.14, entrada fechada 11 de abril de 399 (en la página consultada; confirmar sección 16.8.14). Contexto consultado: https://study.sci.house/roman-law/prohibition-collecting-tax-the-111576.html.

Research candidate (not yet approved narration): Una ley de Arcadio y Honorio prohíbe que los enviados del patriarca judío sigan recaudando aportes en las sinagogas; las sumas ya reunidas se redirigen al tesoro imperial.

La constitución se dirige al prefecto pretoriano de Italia y usa lenguaje hostil sobre el patriarca; describe una medida fiscal-administrativa y no prueba que todas las comunidades dejaran de contribuir de inmediato.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 26. Stone for the Village

[Candidate source](https://pmc.ncbi.nlm.nih.gov/articles/PMC11813141/): Magness et al., “Understanding the history of the late Roman synagogue at Huqoq in Israel’s Galilee through radiocarbon dating and observations on site formation,” PLOS ONE 20.2 (2025), especially abstract and sections “Late Roman synagogue” and “Conclusion” (construction around end 4th/beginning 5th c.; lines 130, 145, 300–312 in consulted version).

Research candidate (not yet approved narration): A monumental basilica synagogue is constructed at Huqoq; its later mosaic program includes biblical narrative panels such as Samson carrying Gaza’s gate.

Recent pottery and radiocarbon work places construction around c.400; the site’s exact use-life is poorly preserved. Do not assign all mosaics to the initial construction phase or use the famous panels as evidence of the building’s exact opening date. It is a distinct village/site and visual program, although it overlaps thematically with the broad synagogue-art entry 76.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 27. The Receipt Restored

[Candidate source](https://www.thelatinlibrary.com/theodosius/theod16.shtml): Codex Theodosianus16.8.17, Rome25July404

Research candidate (not yet approved narration): A constitution revokes the ban on collection by the Jewish patriarch’s agents and restores the earlier privileges.

Normative restoration does not prove universal compliance. The player delivers a fictional local copy; no edict is rewritten.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 28. An Honour Removed

[Candidate source](https://www.thelatinlibrary.com/theodosius/theod16.shtml): Codex Theodosianus 16.8.22; página consultada, líneas 863–866, fecha 20 de octubre de 415. Texto secundario descriptivo: https://study.sci.house/roman-law/interdiction-marriage-between-christians-and-111564.html.

Research candidate (not yet approved narration): Una constitución imperial remueve a Gamaliel de su prefectura honoraria y limita su autoridad: le prohíbe establecer nuevas sinagogas y decidir litigios entre judíos y cristianos.

La medida refleja una disputa sobre privilegio e intermediación del patriarca. No equivale por sí sola a la desaparición inmediata del patriarcado; el hito actual de c.425 aborda esa fase posterior.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

### 29. The Existing Doors

[Candidate source](https://academic.oup.com/book/32151/chapter-abstract/268117453): CTh 16.8.25; Oxford chapter abstract

Research candidate (not yet approved narration): Teodosio II restringe construcción de nuevas sinagogas.

La aplicación local no se infiere automáticamente del texto legal.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Source-audit passage](https://sourcebooks.web.fordham.edu/source/300-800-laws-jews.asp): Theodosian Code 16.8.25–26; Fordham legal-source index, lines 73–80

CTh 16.8.25 (15 Feb 423) orders protection against attacks and synagogue burning; CTh 16.8.26 (9 Apr 423) prohibits building new synagogues while forbidding destruction/confiscation of existing ones.

Limit: Corpus claims a restriction but may compress two laws. This is not a total ban on Judaism or all synagogues; distinguish new construction from protection of existing buildings. Fordham provides citations/index rather than full Latin law text.

Coverage: Opened legal timeline and checked law references/dates lines 73–80; only index/summary, not complete legal text.

### 30. The Living Margin

[Candidate source](https://whc.unesco.org/en/list/1471/): Contexto de renovación judía y Judá el Príncipe

Research candidate (not yet approved narration): Galilea sigue siendo un centro de aprendizaje. Fecha exacta de cierre del Talmud de Jerusalén discutida; el final del juego es límite editorial.

Galilea sigue siendo un centro de aprendizaje. Fecha exacta de cierre del Talmud de Jerusalén discutida; el final del juego es límite editorial.

Knowledge: inherited sources unless the complete dossier dates a plausible fictional local experience within the narrator’s lifespan; distant affairs remain attributed reports. one local map; distant events use attributed reports; city locations are not inferred precise ancient building or battle footprints

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending
