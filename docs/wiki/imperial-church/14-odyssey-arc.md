# The Eagle and the Cross / El águila y la cruz

`imperial-church` · CDF-C01 · 29 selected episodes · source locale `en`

**Status:** chronological selections and main-mechanic choices authored. Complete expanded dossiers, playable maps and measured balancing are pending. Do not assign these selections to MiniMax as completed authoring briefs.

## Campaign voice and continuity

[Expanded narrator bible and per-episode knowledge framing](../../design/voices/imperial-church.md) — fictional biography; independent approval pending.

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
    "sourceAuditStatus": "29 consultations attached; corrected selected claims prevail over conflicting raw candidates; independent historical approval pending",
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
    ],
    "authoredDossierCount": 12
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
| 3 / 03-property-and-record-restoration-nicomedia | The Doors Returned / Las puertas restituidas | 13 June 313 CE | bithynia | property-and-record-restoration |
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
| 8 / 09-crossing-and-supply-adrianople | The Maritsa Crossing / El paso del Maritsa | 3 July 324 CE, conventional | adrianople | crossing-and-supply |
| 9 / 10-land-and-strait-logistics-chrysopolis | Across the Bright Shore / Al otro lado de la costa luminosa | 18 September 324 CE, conventional | chrysopolis | land-and-strait-logistics |
| 10 / 08-disputed-correspondence-alexandria | Words over Alexandria / Palabras sobre Alejandría | 324–325 CE | alexandria | disputed-correspondence |
| 11 / 11-council-record-escort-antioch | Before the Lakeside Council / Antes del concilio junto al lago | c.324–325 CE; exact date and order relative to the imperial letter debated | antioch | council-record-escort |
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

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/01-milvian-bridge/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Constantine defeated Maxentius near Rome in 312; Christian accounts give differing signs and retreat narratives. The conventional 28 October date is supported by the Capitoline institutional guide, while the consulted Latin Lactantius 44.4 has 27 October. No exact deployment, active bridge geometry, divine causation or religious troop affiliation is established for our fictional tactical pocket.

ES: Constantino derrotó a Majencio cerca de Roma en 312; los relatos cristianos presentan signos y retiradas distintos. La guía institucional capitolina respalda el 28 de octubre convencional, mientras el latín consultado de Lactancio 44.4 contiene el 27. No acredita despliegue exacto, geometría de un puente operativo, causalidad divina ni afiliación religiosa de las tropas de nuestro sector táctico ficticio.

[Consulted source](https://www.newadvent.org/fathers/25021.htm): Eusebius VC I.35–38; checked narrative of final advance and Maxentius’ death near Rome; Lactantius 44 not consulted directly in this pass.

Limit: No exact 28 October date established by checked Eusebius passage; victory/bridge details are framed as Christian providence in a panegyric.

Status: disputed

[Additional consulted passage](https://bkv.unifr.ch/de/works/cpl-91/compare/von-den-todesarten-der-verfolger-bkv/45/de-mortibus-persecutorum): Lactantius DMP44.1–12, complete displayed Latin

Limit: Christian providential framing; critical date apparatus not read.

[Additional consulted passage](https://www.newadvent.org/fathers/25021.htm): Eusebius VC I.28–39

Limit: Panegyric; no verified divine cause, precise troop roster or mandatory intact bridge.

[Additional consulted passage](https://www.museiincomuneroma.it/sites/default/files/storage/original/application/d9bc0a70352f82f608abb2ce3673450b.pdf): page1 introductory battle date (PDF page index0)

Limit: Teaching guide, not critical Lactantius edition; does not resolve conflicting day wording. No source image copied.

[Additional consulted passage](https://www.sovraintendenzaroma.it/node/4280): Ponte Milvio monument history

Limit: No312 battlefield footprint or ancient river elevation.

### 2. Promises in the Winter Court

[Candidate source](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/ed_tolerat1.htm): Lactantius, De mortibus persecutorum 48

Research candidate (not yet approved narration): Constantino y Licinio negocian tolerancia religiosa en Milán.

“Edicto de Milán” es rótulo moderno; texto conservado es rescripto oriental.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/02-bounded-negotiation-milan/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Lactantius 48 transmits a letter referring to the Milan agreement on religious choice and Christian communal-property restitution; its preface reports publication at Nicomedia on 13 June 313.

ES: Lactancio 48 transmite una carta que alude al acuerdo de Milán sobre elección religiosa y restitución de bienes comunitarios cristianos; su preámbulo relata publicación en Nicomedia el13de junio de313.

[Consulted source](https://www.newadvent.org/fathers/200110.htm): Eusebius HE X.5 / Fordham translation of rescript; checked editorial note describing Milan meeting.

Limit: The “negotiation” phrasing is an inference; surviving text is later rescript, not minutes of a conversation. Lactantius page URL in dossier was not opened.

Status: consulted

[Additional consulted passage](https://bkv.unifr.ch/en/works/cpl-91/compare/von-den-todesarten-der-verfolger-bkv/49/de-mortibus-persecutorum): DMP48.1–13 complete Latin text, root read2026-10-13

Limit: Milan agreement versus Nicomedia publication; transmitted legal text, no minutes of a negotiation or proven local property delivery.

### 3. The Doors Returned

[Candidate source](https://sourcebooks.fordham.edu/source/edict-milan.asp): Lactantius 48; texto del rescripto

Research candidate (not yet approved narration): Licinio publica en Nicomedia la política de libertad y restitución de propiedades.

No establece aún cristianismo como religión oficial.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/03-property-and-record-restoration-nicomedia/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Lactantius 48 transmits a letter referring to the Milan agreement on religious choice and Christian communal-property restitution; its preface reports publication at Nicomedia on 13 June 313.

ES: Lactancio 48 transmite una carta que alude al acuerdo de Milán sobre elección religiosa y restitución de bienes comunitarios cristianos; su preámbulo relata publicación en Nicomedia el13de junio de313.

[Consulted source](https://sourcebooks.fordham.edu/source/edict-milan.asp): Eusebius HE X.5 as reproduced in Fordham; lines on Nicomedia and restitution.

Limit: The text is not the original Milan instrument; legal order is not proof of uniform practical restitution.

Status: consulted

[Additional consulted passage](https://bkv.unifr.ch/en/works/cpl-91/compare/von-den-todesarten-der-verfolger-bkv/49/de-mortibus-persecutorum): DMP48.1–13 complete Latin text, root read2026-10-13

Limit: Milan agreement versus Nicomedia publication; transmitted legal text, no minutes of a negotiation or proven local property delivery.

### 4. The African Petition

[Candidate source](https://www.fourthcentury.com/donatist-controversy/): Eusebius HE 10; Optatus, Against the Donatists

Research candidate (not yet approved narration): La disputa donatista llega a audiencias imperiales y sínodos regionales.

Fuentes adversarias y posteriores; no simplificar causas sociales.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/04-rival-delegation-reception-rome-ostia/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The transmitted letter directs the African dispute to Rome; Optatus later gives a Roman hearing and decision for Caecilian. Ostia is an attendee’s see, not an attested hearing venue. Polemical framing, consular wording and party identity require comparison.

ES: La carta transmitida remite la disputa africana a Roma; Optato relata después una audiencia romana y decisión favorable a Ceciliano. Ostia es sede de un participante, no sede documentada de audiencia. El marco polémico, la fórmula consular y la identidad de la parte requieren contraste.

Source consultation pending: No exact passage directly consulted for the dossier’s Rome/Ostia hearings; Eusebius HE X.5 mentions a Roman decision only indirectly in the contextual tradition.

Limit: Dossier URLs (Fourth Century/Optatus) not opened in this pass; Rome/Ostia may conflate distinct hearings. Needs primary passage before treating as established.

Status: unavailable

[Additional consulted passage](https://www.newadvent.org/fathers/250110.htm): Eusebius HE X.5.18–20

Limit: Transmitted legal invitation, not private deliberation or proof of fairness.

[Additional consulted passage](https://www.tertullian.org/fathers/optatus_01_book1.htm): Optatus I.22–25 and edition notes188–192

Limit: Retrospective polemic; note190 contrasts consular wording with Augustine. No Ostia hearing or exact playable room follows.

### 5. The Road to Arles

[Candidate source](https://www.fourthcentury.com/early-church-councils/): Canones de Arlés, colección de fuentes

Research candidate (not yet approved narration): Concilio de Arlés aborda donatismo, disciplina y fecha de Pascua.

Actas fragmentarias.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/05-delegate-logistics-arles/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The transmitted invitation prescribes travel to Arles, public conveyance and arrival before the August date. The preserved synodal letter addresses absent Sylvester and states decisions. Neither document proves every route, Constantine’s presence or universal compliance.

ES: La invitación transmitida prescribe viaje a Arlés, transporte público y llegada antes de la fecha de agosto. La carta sinodal conservada se dirige a Silvestre ausente y expresa decisiones. Ningún documento prueba todas las rutas, la presencia de Constantino ni cumplimiento universal.

[Consulted source](https://christearlychurch.co.uk/text/the-acts-of-the-council-of-arles/): Council of Arles page, introductory lines 16–17 and references to canons 1, 8, 20.

Limit: Page’s narrative introduction is modern editorial framing; it gives 1 August 314, while precise dating derives from scholarly reconstruction. Checked summary, not full canonical text.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/250110.htm): Eusebius HE X.5.21–24

Limit: Normative transmitted invitation, not observed itinerary; no exact council venue or native timed travel.

[Additional consulted passage](https://www.tertullian.org/fathers/optatus_11_appendices.htm): Appendix IV synodal letter to Sylvester, displayed pp389–393

Limit: Did not read Munier critical edition or a complete separately numbered22-canon collection. Modern page claims Constantine attended; not adopted as verified fact.

### 6. The Field between Two Eagles

[Candidate source](https://www.britannica.com/biography/Constantine-I-Roman-emperor): Britannica, Constantine, chronology

Research candidate (not yet approved narration): Constantino y Licinio libran guerra en Cibalae; pactan reparto territorial en 317.

The battle is usually dated 316, though some chronologies place it in 314; the conflict was dynastic/political, not simply religious.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/06-finite-field-withdrawal-cibalae/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Zosimus narrates Constantine’s victory near Cibalae and Licinius’ subsequent withdrawal toward Sirmium. The exact year314/316 and battlefield footprint remain disputed or unverified; the local auxiliary convoy does not represent the emperor’s entire retreat.

ES: Zósimo narra la victoria de Constantino junto a Cibalae y la retirada posterior de Licinio hacia Sirmio. El año exacto314/316 y la huella del campo siguen discutidos o sin verificar; el convoy auxiliar local no representa toda la retirada del emperador.

Source consultation pending: No accessible primary/academic passage opened for Cibalae in this pass; dossier relies on Britannica.

Limit: Dating 314 vs 316 is disputed; Britannica URL not consulted. Do not present either year as settled here.

Status: unavailable

[Additional consulted passage](https://www.tertullian.org/fathers/zosimus02_book2.htm): Zosimus New History II, displayed Cibalis battle/retreat paragraphs (II.18–20 locator to compare)

Limit: Later hostile narrative; displayed passage does not settle314/316 or exact317 settlement date. No modern battlefield coordinate or high mountain inferred.

[Additional consulted passage](https://grad-vinkovci.hr/geoprometni-polozaj): Municipal geography/elevation paragraph

Limit: Modern regional control only, not ancient wetlands, road or battlefield survey.

[Additional consulted passage](https://grad-vinkovci.hr/povijest-grada): Municipal history, Roman Cibalae paragraph

Limit: Official municipal summary does not resolve scholarly314/316 dispute; unrelated later monastery chronology not adopted.

### 7. A Day beneath the Law

[Candidate source](https://www.fourthcentury.com/constantine-321-sunday-law/): Codex Theodosianus 2.8.1

Research candidate (not yet approved narration): Una ley imperial limita actividad judicial dominical y permite labor agrícola.

No fue cierre total del trabajo.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/07-court-record-logistics-rome-ostia/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: CJ3.12.2 preserves7March321 urban rest and the rural agricultural exception. CTh2.8.1 separately permits emancipation/manumission and their acts, published at Caralis3July321. Norms and later interpretation do not prove universal enforcement or mandatory conversion.

ES: CJ3.12.2 conserva descanso urbano y excepción agrícola rural del7de marzo de321. CTh2.8.1 permite por separado emancipación/manumisión y sus actas, publicado en Caralis el3de julio de321. Las normas y la interpretación posterior no prueban aplicación universal ni conversión obligatoria.

[Corrected primary passage](https://droitromain.univ-grenoble-alpes.fr/Corpus/CJ3.htm): Codex Justinianus 3.12.2 (3.12.3 in older numbering), Constantine to Helpidius. Later codification preserves a 321 constitution. City rest and rural agricultural exception differ from the June permission for manumission in CTh 2.8.1. No uniform compliance or mandated conversion follows from the text.

[Consulted source](https://www.thelatinlibrary.com/codtheod.html): Codex Theodosianus 2.8.1 (Constantine to Elpidius; Latin transcription, 3 July 321).

Limit: The cited law does not contain the agricultural-work exception; that appears in a different legal context. Replace or remove that claim. Website is a transcription rather than critical edition.

Status: disputed

[Additional consulted passage](https://droitromain.univ-grenoble-alpes.fr/Corpus/CJ3.htm): CJ3.12.2, Constantine to Helpidius, datedPP VNONMART321

Limit: Later codification/transcription; no321 Rome enactment venue or uniform compliance. Number3.12.3 in some older references must be matched by text.

[Additional consulted passage](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/CTh02.html): CTh2.8.1 including subscription and separately labelled Interpretatio

Limit: This is not the agricultural-exception text. Caralis is the displayed publication place; local Rome gameplay is fiction. Later interpretative text is separate, not an additional contemporary decree.

### 8. The Maritsa Crossing

[Candidate source](https://www.britannica.com/biography/Constantine-I-Roman-emperor): Eusebius VC II; resumen cronológico

Research candidate (not yet approved narration): Constantino derrota a Licinio en Adrianópolis y Chrysopolis; queda como único emperador.

La fuente panegírica de Eusebio requiere cautela.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/09-crossing-and-supply-adrianople/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Constantine defeated Licinius in the Adrianople/Hebrus region before the later Bithynian operations;3July324 is conventional chronology, not dated in the displayed Zosimus account.

ES: Constantino derrotó a Licinio en la región de Adriánopolis/Hebro antes de las operaciones bitinias posteriores; el3de julio de324 es cronología convencional, no fecha indicada en el relato mostrado de Zósimo.

[Consulted source](https://www.newadvent.org/fathers/25022.htm): No precise battle passage opened; Eusebius VC II checked generally, Britannica not consulted.

Limit: Date and military detail remain unverified in this audit; should retain as conventional only with a better source.

Status: unavailable

[Additional consulted passage](https://www.tertullian.org/fathers/zosimus02_book2.htm): New History II; printed47–48 Adrianople/Hebrus crossing and retreat

Limit: Later hostile account; not a precise calendar date, GPS crossing/battlefield, neutral casualty total or private dialogue.

[Additional consulted passage](https://roman-emperors.sites.luc.edu/licinius.htm): Michael DiMaio, Second Civil War and Death paragraphs

Limit: Modern scholarly reference updated1997, not a primary ancient date attestation; summary and interpretive dates retain review gate.

[Additional consulted passage](https://dergipark.org.tr/en/download/article-file/6126842): Yildirim2015; abstract and opening pp181–183; regional map figure1 onPDFpage2

Limit: Not full24-page archaeological analysis read; medieval/modern city plans elsewhere not adopted as324 footprint. Exact ford and ancient channels unverified.

### 9. Across the Bright Shore

[Candidate source](https://www.britannica.com/biography/Constantine-I-Roman-emperor): Eusebius VC II; resumen cronológico

Research candidate (not yet approved narration): Constantino derrota a Licinio en Adrianópolis y Chrysopolis; queda como único emperador.

La fuente panegírica de Eusebio requiere cautela.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/10-land-and-strait-logistics-chrysopolis/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The final324 military sequence includes the Asian-shore victory conventionally dated18September atChrysopolis and Licinius’ subsequent surrender. Zosimus’ northern crossing narrative does not survey this local supply route.

ES: La secuencia militar final de324 incluye la victoria asiática fechada convencionalmente el18de septiembre enCrisópolis y la rendición posterior deLicinio. El relato de cruce norteño deZósimo no prospecta esta ruta local de provisiones.

[Consulted source](https://www.newadvent.org/fathers/25022.htm): No precise battle passage opened; Eusebius VC II checked generally, Britannica not consulted.

Limit: Do not merge both battles as one event; precise conventional dates need source support.

Status: unavailable

[Additional consulted passage](https://www.tertullian.org/fathers/zosimus02_book2.htm): New History II; printed49–50 Asian shore and battle/surrender sequence

Limit: Later hostile account; not a precise calendar date, GPS crossing/battlefield, neutral casualty total or private dialogue.

[Additional consulted passage](https://roman-emperors.sites.luc.edu/licinius.htm): Michael DiMaio, Second Civil War and Death paragraphs

Limit: Modern scholarly reference updated1997, not a primary ancient date attestation; summary and interpretive dates retain review gate.

[Additional consulted passage](https://www.ancientportsantiques.com/wp-content/uploads/Documents/PLACES/Bosphorus-BlackSea/Chalcedon-Belke2021.pdf): Belke2021 chapter pp223–224 and227–228; map figure pp226

Limit: Only selected chapter passages, not full73-page offprint; multi-era coast and later Skutarion ruins not324 quay. Official Propylaeum access denied; mirrored scholarly PDF consulted.

### 10. Words over Alexandria

[Candidate source](https://www.newadvent.org/fathers/25021.htm): Eusebius, Life of Constantine II.64–73

Research candidate (not yet approved narration): Controversia entre Alejandro de Alejandría y Arrio se extiende por redes episcopales.

Relato de Eusebio presenta el conflicto como problema de unidad.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/08-disputed-correspondence-alexandria/15-odyssey-dossier.md) — independent approval pending

[Consulted source](https://www.newadvent.org/fathers/25022.htm): Eusebius VC II.61–64 checked for dispute background and imperial intervention.

Limit: Eusebius’ account is selective and pro-Constantinian; date range 324–325 and the phrase “networks” are editorial synthesis, not an exact dated event.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/25022.htm): VC II.61–73, especiallyII.67 andII.72 post-victory/Nicomedia framing andII.73 continued dispute

Limit: Richardson1890 translation revised onNewAdvent; noGreek critical apparatus or exactletterdate. Eusebius is panegyrical; imperial characterization of the dispute as minor remains attributed, never the agnostic narrator’s verdict.

### 11. Before the Lakeside Council

[Candidate source](https://onlinelibrary.wiley.com/doi/10.1111/erev.12782): Kinzig, “The Creed of Nicaea,” sección sobre sínodo

Research candidate (not yet approved narration): Sínodo regional de Antioquía suspende a obispos en antesala de Nicea.

Cronología reconstruida; evidencia transmitida por fuentes posteriores.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/11-council-record-escort-antioch/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: A transmitted synodal letter attributed to Antioch around324–325 reports refusing communion to three bishops and names a future meeting at Ancyra. Its exact date, authorship, textual history and order relative to imperial intervention remain disputed.

ES: Una carta sinodal transmitida y atribuida a Antioquía hacia324–325 refiere negar comunión a tres obispos y nombra una reunión futura en Ancira. Su fecha exacta, autoría, historia textual y orden respecto a la intervención imperial siguen discutidos.

[Consulted source](https://www.newadvent.org/fathers/26011.htm): Socrates HE I.25 checked only for post-Nicaea Antioch context; it does not establish the selected pre-Nicaea suspension claim. Wiley article not consulted.

Limit: Potential confusion with the Antioch synod after Nicaea; specialist article remains unconsulted.

Status: unavailable

[Additional consulted passage](https://www.fourthcentury.com/wp-content/uploads/2024/05/Dok-20-Urkunde-18-1.pdf): Urk18/Dok20, editorial note and §§1–15 including colophon

Limit: Greek is a reconstruction from Syriac, not a preserved original. English translator Aaron West. Header/colophon and Greek heading differ on recipient; no exact venue, attested escort or removal from episcopal office. January325 in editorial header is a reconstruction, not the letter’s date.

[Additional consulted passage](https://kath-akademie-bayern.de/en/mediathek-eintrag/das-schreiben-der-synode-von-antiochia-324-325-urk-18-ueberlieferungsgeschichtliche-einordnung-edition-uebersetzung-und-kommentar/): Matthias Simperl presentation, Scholarly disputes, transmission and324/25 revaluations sections

Limit: Presentation of an academic argument, not full critical monograph consultation; motives and attribution to Eustathius remain the author’s reconstruction.

[Additional consulted passage](https://theologicalstudies.net/wp-content/uploads/2025/09/The-Council-of-Nicaea-325_-Reassessing-the-Role-of-Eusebius-of-Caesarea.pdf): Samuel Fernandez2025, Ossius in Alexandria/Antioch, printed378–379 andnotes66–68

Limit: Selected pages only, not full25-page article. Reconstruction differs from Simperl; no exact meeting date or court/escort footprint. The modern scholarly date/order is not an ancient subscription.

### 12. Many Voices beside the Lake

[Candidate source](https://www.newadvent.org/fathers/3801.htm): Credo y cánones de Nicea

Research candidate (not yet approved narration): Concilio de Nicea acuerda un credo y cánones sobre doctrina y disciplina.

No creó las iglesias católica y ortodoxa modernas.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/02-nicaea/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The council at Nicaea in 325 issued a creed and disciplinary canons and reported a common Easter agreement. These are distinct matters; neither a biblical canon nor the creation of modern Catholic and Orthodox churches.

ES: El concilio de Nicea de 325 emitió un credo y cánones disciplinarios y comunicó un acuerdo sobre Pascua. Son asuntos distintos; no un canon bíblico ni la creación de las iglesias católica y ortodoxa modernas.

[Consulted source](https://www.newadvent.org/fathers/3801.htm): Nicaea page: canon 20; post-council letter paragraph on Easter (lines 93–95).

Limit: Canon 20 is not an Easter-calendar canon. The surviving letter is a post-council report; it does not supply a detailed computational rule or prove uniform compliance.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/3801.htm): Creed; canons 1–20, especially 4–7 and 20; synodal letter

Limit: Disciplinary canons are normative, not proof of universal practice. Canon 20 concerns standing prayer, not an Easter computation. Creed of 325 is not silently replaced with the later liturgical expansion. Letter reports agreement, not an algorithm or universal compliance.

[Additional consulted passage](https://www.newadvent.org/fathers/25023.htm): Eusebius VC III.6–23

Limit: Pro-imperial narrative; logistical details are attributed. III.7 prayer-house and III.10 palace hall do not locate excavated buildings. Reported unanimity is rhetoric, not proof that later controversy ceased; III.23 itself reports renewed Egyptian contention. No exact guest count or cost is derived from this text.

### 13. Stone above the Old City

[Candidate source](https://www.newadvent.org/fathers/25023.htm): Eusebius, Life of Constantine III.25–40

Research candidate (not yet approved narration): Constantino patrocina iglesias y obras en los lugares santos de Jerusalén.

La obra se inició en algún momento del periodo; no fechar automáticamente por viaje de Helena.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://www.newadvent.org/fathers/25023.htm): Eusebius VC III.25–40 checked for imperial church-building at Jerusalem.

Limit: Eusebius is a Christian panegyrist; source establishes patronage and his identification, not independent proof of the biblical site or the exact dating of each work.

Status: consulted

### 14. A City beneath a New Sky

[Candidate source](https://www.britannica.com/place/Istanbul/History): Chronicon Paschale, annal 330; overview

Research candidate (not yet approved narration): Constantinopla recibe dedicación ceremonial y juegos fundacionales.

Fecha tradicional, ceremonia sobre proceso urbano anterior.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Source consultation pending: Chronicon Paschale not directly consulted; Britannica URL not consulted.

Limit: 11 May is a conventional date but remains unverified in this audit; avoid implying all construction occurred on dedication day.

Status: unavailable

### 15. A Letter beyond the Frontier

[Candidate source](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.8–13

Research candidate (not yet approved narration): Constantino escribe a Shapur II sobre cristianos en el imperio persa, según Eusebio.

Eusebio presenta al emperador como protector universal; sesgo panegírico.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://www.newadvent.org/fathers/25024.htm): Eusebius VC IV.8–13 checked: embassy and Constantine’s letter to the Persian king.

Limit: Eusebius does not establish the dossier’s c.332–333 date in this passage; identify the recipient as Sapor/Shapur only as Eusebius names him. Panegyrical source, not Persian-side confirmation.

Status: consulted

### 16. The Council on the Shore

[Candidate source](https://www.newadvent.org/fathers/25023.htm): Eusebius, Life of Constantine IV.41–47; III.28

Research candidate (not yet approved narration): Sínodo de Tiro juzga a Atanasio; poco después se consagra el complejo de la Resurrección.

Narrativas de sínodo y consagración son interesadas.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Corrected primary passage](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.41–47. Book III URL in raw candidate does not contain this locator. Eusebius is a partisan biographer.

[Consulted source](https://www.newadvent.org/fathers/25024.htm): Eusebius VC IV.41–47 checked: Tyre proceedings and Jerusalem dedication (IV.47).

Limit: The source is hostile/panegyrical toward Athanasius; separate the Tyre council from Jerusalem dedication. Chronology is not precise enough to imply immediate sequence without qualification.

Status: consulted

### 17. The Empty Appointment

[Candidate source](https://www.newadvent.org/fathers/26023.htm): Sozomen, HE II.29

Research candidate (not yet approved narration): Arrio muere en Constantinopla antes de una readmisión prevista.

Relatos sobre circunstancias milagrosas son polémicos.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://www.newadvent.org/fathers/26022.htm): Sozomen HE II.30 (New Advent 26022), account of Arius’ death.

Limit: Sozomen presents the death as providential punishment and explicitly reports hearsay; date 336 is not established by this passage. The cited dossier URL 26023 is Book III and is wrong for II.29.

Status: disputed

### 18. The Court without Its Emperor

[Candidate source](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.61–64

Research candidate (not yet approved narration): Constantino recibe bautismo de Eusebio de Nicomedia y muere en Nicomedia.

Bautismo de Silvestre es leyenda posterior.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://www.newadvent.org/fathers/25024.htm): Eusebius VC IV.61–64 checked for baptism and death at Nicomedia.

Limit: The narrative is an imperial Christian encomium; day 22 May is not independently verified by the passage checked.

Status: consulted

### 19. Three Seals, One Inheritance

[Candidate source](https://www.newadvent.org/fathers/26012.htm): Socrates Scholasticus, Ecclesiastical History II.1 y 2.25; fuente narrativa de siglo V, no contemporánea.

Research candidate (not yet approved narration): Tras la muerte de Constantino, sus hijos toman el poder imperial; las disputas sucesorias y la distribución de territorios preceden nuevas intervenciones en asuntos eclesiásticos.

La sucesión estuvo marcada por violencia contra miembros de la familia imperial; evitar presentar la división territorial como una partición constitucional permanente ya fijada en 337.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://www.newadvent.org/fathers/26012.htm): Socrates HE II.1 / II.25 identified as relevant narrative; checked introductory framing and selected passage context.

Limit: Not a contemporary dispatch; exact territorial division and timing need passage-level audit before detailed map/campaign claims.

Status: consulted

### 20. The Council That Divided

[Candidate source](https://www.newadvent.org/fathers/3815.htm): Council of Sardica: introducción y cánones; síntesis contextual académica de Milton V. Anastos: https://www.myriobiblos.gr/texts/english/milton1_5.html

Research candidate (not yet approved narration): Obispos occidentales y orientales se reúnen en Sardica; el desacuerdo por Atanasio produce sesiones y decisiones separadas.

La fecha exacta se debate entre 342–344, con 343 habitual. Los cánones sobrevivieron en tradiciones griega y latina con diferencias interpretativas.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://www.newadvent.org/fathers/3815.htm): Sardica canons page: introduction and selected canons; Anastos link not opened.

Limit: Page’s own date discussion is inconsistent/uncertain (343/344; wider alternatives); avoid a precise date without resolving textual chronology.

Status: disputed

### 21. The Road Back to Alexandria

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Athanasius, Historia Acephala §§1–2; Socrates, Ecclesiastical History II, regreso y carta imperial: https://www.newadvent.org/fathers/26012.htm

Research candidate (not yet approved narration): Atanasio vuelve a Alejandría tras su exilio, respaldado por cartas de Constancio II y Constante.

La Historia Acephala conserva cronología alejandrina valiosa; sus lagunas y transmisión fragmentaria aconsejan mantener fecha como día calendárico convertido desde el calendario local.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://www.newadvent.org/fathers/2820.htm): Historia Acephala §I.2; Socrates HE II contextual account.

Limit: Athanasius’ chronicle is aligned with his side of the dispute; support from imperial letters is broadly reported, but the exact political motives should not be inferred.

Status: consulted

### 22. The Dispatch from Gaul

[Candidate source](https://www.newadvent.org/fathers/26012.htm): Socrates, Ecclesiastical History II.25–26; contexto secundario en CCEL, Socrates and Sozomen, Book IV.1: https://www.ccel.org/ccel/schaff/npnf202.iii.ix.i.html

Research candidate (not yet approved narration): Constante es asesinado en la Galia durante la usurpación de Magnencio; Constancio II queda como único emperador y el equilibrio que había favorecido a Atanasio desaparece.

Socrates vincula el cambio político con nuevos conflictos eclesiásticos, pero no reducir toda la guerra civil a una disputa teológica.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Later church histories report that Constans was killed in Gaul during the usurpation of Magnentius in 350. Constantius II still faced a rival; this Milan setting receives news from Gaul rather than depicting the killing.

ES: Las historias eclesiásticas posteriores relatan que Constante murió en la Galia durante la usurpación de Magnencio en 350. Constancio II aún tenía un rival; este escenario de Milán recibe noticias de la Galia y no representa la muerte.

[Consulted source](https://www.ccel.org/ccel/schaff/npnf202.iii.ix.i.html): Socrates/CCEL passage on Constans’ death in Gaul in 350 and Magnentius.

Limit: Candidate is wrong to say Constantius II became sole emperor in 350; Magnentius remained a rival until defeated in 353. Geographic focus Milan is reception of news, not death site.

Status: disputed

### 23. Seals at the Western Synod

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Athanasius, Historia Acephala (entrada de tropas, 6–9 Feb 356); su relato defensivo: Apologia de Fuga https://www.newadvent.org/fathers/2814.htm

Research candidate (not yet approved narration): Tras presión imperial en sínodos occidentales, Atanasio es perseguido; tropas entran en una iglesia de Alejandría durante la noche y él escapa.

La cronología de la Historia Acephala sitúa el ataque en febrero de 356. Atanasio escribe como parte enfrentada; sus cifras y caracterización de adversarios requieren cautela.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Sozomen describes a council at Milan at which bishops were pressed to condemn Athanasius and dissenting bishops were exiled.

ES: Sozomeno describe un concilio en Milán en el que se presionó a los obispos para condenar a Atanasio y se exilió a obispos disidentes.

[Consulted source](https://www.newadvent.org/fathers/2820.htm): Athanasius Historia Acephala and Apologia de Fuga checked for February 356 church raid/escape; no evidence for the Milan hearing in this source.

Limit: Episode has wrong local event/date alignment: Milan hearing and Alexandria raid are distinct episodes. Athanasius is a partisan witness; figures and adversary descriptions require caution.

Status: disputed

[Additional consulted passage](https://www.newadvent.org/fathers/26024.htm): Sozomen, Ecclesiastical HistoryIV.9, Milan council

Limit: Later partisan church history; its theological judgements are attributed to the author. Conventional355 date and exact local hearing logistics are not independent court records. This event is distinct from the Alexandria night raid in356.

### 24. The Night of the Open Doors

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Athanasius, Historia Acephala (entrada de tropas, 6–9 Feb 356); su relato defensivo: Apologia de Fuga https://www.newadvent.org/fathers/2814.htm

Research candidate (not yet approved narration): Tras presión imperial en sínodos occidentales, Atanasio es perseguido; tropas entran en una iglesia de Alejandría durante la noche y él escapa.

La cronología de la Historia Acephala sitúa el ataque en febrero de 356. Atanasio escribe como parte enfrentada; sus cifras y caracterización de adversarios requieren cautela.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Athanasius reports a nighttime military entry into a church in Alexandria and his escape in 356. This is his partisan testimony, not a neutral transcript or an episode at Milan.

ES: Atanasio relata una entrada militar nocturna en una iglesia de Alejandría y su huida en 356. Es su testimonio partidista, no una transcripción neutral ni un episodio ocurrido en Milán.

[Consulted source](https://www.newadvent.org/fathers/2814.htm): Athanasius Historia Acephala / Apologia de Fuga; exact raid account checked.

Limit: Potential duplicate with episode 23; source is partisan and the reported troop count is not independently verified. Keep only if the two episodes have distinct historical content.

Status: disputed

### 25. A Formula on the Adriatic Road

[Candidate source](https://www.newadvent.org/fathers/26012.htm): Socrates, Ecclesiastical History II.37–41; la cronología secundaria alojada por CCEL también registra 359: https://www.ccel.org/ccel/s/schaff/npnf202/cache/npnf202.pdf

Research candidate (not yet approved narration): Constancio convoca simultáneamente un concilio occidental en Rimini y uno oriental en Seleucia para buscar una fórmula doctrinal común; ambos producen controversias y no una unidad estable.

Socrates escribe en el siglo V y es pro-niceno. Los sínodos no fueron una única reunión ni una decisión idéntica; evitar etiquetar a todos los participantes con categorías posteriores simplificadas.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://www.newadvent.org/fathers/26012.htm): Socrates HE II.37 and II.39–40: Ariminum and Seleucia both met in 359, Seleucia divided into factions; the text places Seleucia meeting on 27 September.

Limit: Socrates is a fifth-century pro-Nicene narrator. The selected page supports that these were separate synods, not that they pursued an identical formula or produced a single outcome.

Status: consulted

### 26. The Temples Open Again

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/22*.html): Ammianus Marcellinus, Res Gestae XXII.2; fuente de un contemporáneo pagano que sirvió en la campaña persa.

Research candidate (not yet approved narration): Juliano entra en Constantinopla tras la muerte de Constancio II y asume el gobierno único; reabre templos y restablece sacrificios públicos.

Ammiano admira a Juliano. Las prácticas religiosas se reanudaron por decreto y patronazgo, pero no toda la población cambió de culto ni se revirtió de inmediato la infraestructura cristiana.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/22*.html): Ammianus XXII.2 §1 checked for Julian’s entry into Constantinople and sole rule.

Limit: This passage does not support reopening temples/restoring sacrifices; that needs a separate exact source. Ammianus is an admiring pagan narrator.

Status: disputed

### 27. The Return That Did Not Last

[Candidate source](https://romanletters.org/letters/julian_emperor/24/): Julian, Letter 24 to the Alexandrians (362), sobre el retorno de Atanasio; Ammianus, Res Gestae XXIII–XXV, campaña y muerte en 363: https://tertullian.org/fathers/ammianus_25_book25.htm

Research candidate (not yet approved narration): Juliano permite el regreso de obispos exiliados y luego vuelve a expulsar a Atanasio de Alejandría; su campaña contra Persia termina con su muerte en Mesopotamia.

Juliano presenta su conducta como aplicación de la ley; cartas imperiales son retóricas oficiales. Las circunstancias exactas de su herida mortal son inciertas.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://romanletters.org/letters/julian_emperor/24/): Julian Letter 24 checked for order that Athanasius leave Alexandria; Ammianus XXV checked for death during Persian campaign.

Limit: Julian’s letter is polemical; exact wound cause and killer are uncertain. The Persian campaign/death is not a local Alexandria event—present as reported news, not on-map action.

Status: consulted

### 28. The Weight of an Imperial Word

[Candidate source](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/Thessalonique.htm): Codex Theodosianus 16.1.2, Edictum de fide catholica; edición de texto latino y encabezamiento consultados.

Research candidate (not yet approved narration): Graciano, Valentiniano II y Teodosio publican en Tesalónica una constitución que prescribe la fe nicena para los pueblos bajo su gobierno y clasifica a otros grupos como herejes.

Es una norma legal dirigida a Constantinopla, no prueba de cumplimiento uniforme inmediato ni de la desaparición de otras religiones. Evitar llamarla, sin matices, conversión instantánea del imperio.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/Thessalonique.htm): CTh 16.1.2 Latin text and editorial heading checked.

Limit: The constitution is addressed to the people of Constantinople though issued at Thessalonica; it does not prove uniform enforcement, conversion, or universal application. Header date/location should be checked in a critical edition if exact day matters.

Status: consulted

### 29. Under the Same Eastern Sky

[Candidate source](https://www.papalencyclicals.net/councils/ecum02.htm): Credo y cánones del Concilio de Constantinopla I; la página señala el problema de la transmisión del credo y el estatus inicialmente limitado del concilio.

Research candidate (not yet approved narration): Un concilio en Constantinopla reafirma la fe nicena, trata controversias sobre el Espíritu y fija en canon 3 la precedencia honorífica del obispo de Constantinopla después de Roma.

El credo conocido como niceno-constantinopolitano se atestigua textualmente en Calcedonia (451); no atribuir sin reservas toda su forma conservada a actas contemporáneas de 381. El canon 3 trata rango, no una división moderna entre católicos y ortodoxos.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

[Consulted source](https://www.papalencyclicals.net/councils/ecum02.htm): Council of Constantinople I page, canon 3 and editorial transmission note.

Limit: Canon is about precedence/honor, not a modern Catholic/Orthodox split or unrestricted jurisdiction. Creed text transmission is separate; page is a translation/compilation.

Status: consulted

[Source-audit passage](https://www.papalencyclicals.net/councils/ecum02.htm): Constantinople I: canon 3; creed and canons, but status/transmission caveat

The source text supports a council traditionally dated 381 and canon 3 giving Constantinople honor after Rome because it is New Rome; creed transmission/history is separate from these canons.

Limit: Canon 3 does not establish papal/imperial jurisdiction or later East-West schism. Page is a compiled translation; it acknowledges transmission complexity.

Coverage: Opened council page and checked canon 3 and creed section; not manuscript apparatus.
