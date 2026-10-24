# The Eagle and the Cross / El águila y la cruz

`imperial-church` · CDF-C01 · 34 selected episodes · source locale `en`

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
    "targetEpisodeCount": 34,
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
    "sourceAuditStatus": "34 selections with bounded source consultations; one complete dossier and all independent historical approvals pending",
    "coreMechanicPolicy": "at least four mission-core families in each odyssey; no more than two consecutive identical core families without authored reason; side-objective variety does not excuse identical main missions",
    "narratorMigration": {
      "proposedLifespan": "c.334–403",
      "replaces": "c.290–350",
      "reason": "extend arc to381 without an implausibly long-lived omniscient clerk",
      "knowledge": "312–337 inherited documents; early childhood never adult eyewitness; later dated visits explicitly recorded episode by episode",
      "status": "authored decision; baseline catalogue/voice bible migration occurs with expanded campaign dossier"
    },
    "selectedEpisodeCount": 34,
    "selectionNotes": [
      "Helena death328–330andCrispus/Fausta326remain cautious background, not invented detective missions at uncertain locations.",
      "Paschal decisions are integrated withNicea; capital expansion is integrated with330.",
      "Adrianople/Chrysopolis andMilan/Alexandria are separate local episodes because they involve different places and operations.",
      "Sole rule is not asserted in350: Magnentius survives until353.",
      "Rome/eastern successors open337 and disclose the return in chronology after the381finale."
    ],
    "authoredDossierCount": 33
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
| 15 / 15-long-distance-dispatch-nicomedia | A Letter beyond the Frontier / Una carta más allá de la frontera | Undated letter within 324–337 CE; retrospective local interlude after 330 | nicomedia | long-distance-dispatch |
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

Historical year band: [342, 359]. Sardica, exilios y fórmulas rivales; Marcus crece entre papeles familiares y empieza a trabajar.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 20 / 20-separate-reception-logistics-sardica | The Council That Divided / El concilio que se dividió | 343 CE as an editorial frame; 342/344 alternatives and source chronology qualified | sardica | separate-reception-logistics |
| 21 / 21-returning-households-escort-alexandria | The Road Back to Alexandria / El camino de vuelta a Alejandría | 21 October 346 CE | alexandria | returning-households-escort |
| 22 / 22-civilian-record-preservation-milan | The Dispatch from Gaul / El despacho desde la Galia | 350 CE; reception of news, killing site not asserted; Constantius not yet sole emperor | milan | civilian-record-preservation |
| 23 / 23-bounded-political-pressure-milan | The Seal and the Exile / El sello y el destierro | 355 CE; Milan hearing focus | milan | bounded-political-pressure |
| 24 / 24-night-civilian-withdrawal-alexandria | The Night of the Open Doors / La noche de las puertas abiertas | 356 CE; night of Mechir13/14 in the anonymous chronicle, civil conversion qualified | alexandria | night-civilian-withdrawal |
| 25 / 25-delegate-and-draft-network-rimini | The Winter of Divided Voices / El invierno de las voces divididas | 359 CE; Western council, Seleucia off-map comparison | rimini | delegate-and-draft-network |

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

Historical year band: [361, 381]. Reversiones de política, sucesión, derrota y recomposición antes de la ley de380, los cambios de acceso urbano y la coda conciliar de381. Prescripción y aceptación siguen siendo distintas.

| Order / semantic ID | English / Español | Date | Local geography | Main operation |
|---|---|---|---|---|
| 26 / 26-plural-civic-logistics-constantinople | Altars of a New Reign / Los altares de un nuevo reinado | December 361–early 362 CE; policy sequence, no fixed local reopening day | constantinople | plural-civic-logistics |
| 27 / 27-return-and-departure-records-alexandria | The Return That Did Not Last / El regreso que no duró | 362–363 CE; exile policies focus, Persian campaign reported off-map | alexandria | return-and-departure-records |
| 28 / 30-policy-reversal-alexandria | Beyond the Quiet River / Más allá del río silencioso | 365–366 CE; source calendar and consular formulas qualified | alexandria | policy-reversal-and-discreet-support |
| 29 / 31-contested-succession-alexandria | The Empty Chair / La silla vacía | 373 CE conventional; Socrates’ consular synchronism conflicts | alexandria | contested-succession-and-local-continuity |
| 30 / 32-defeat-and-withdrawal-adrianople | Where the Eagles Fell / Donde cayeron las águilas | 378 CE; conventional Roman-calendar August 9, not a verified Gregorian conversion | adrianople378 | finite-post-defeat-withdrawal |
| 31 / 33-accession-and-reassembly-sirmium | The Burden of the Purple / El peso de la púrpura | 379 CE; exact accession day requires chronology comparison | sirmium | post-crisis-reassembly-and-accession |
| 32 / 28-law-and-local-reception-thessalonica | The Weight of an Imperial Word / El peso de una palabra imperial | 27 February 380 CE | thessalonica | law-and-local-reception |
| 33 / 34-church-transfer-constantinople | The Doors of New Rome / Las puertas de Nueva Roma | November380 CE; arrival and church transfer are distinct source dates | constantinople | changed-urban-access-and-local-care |
| 34 / 29-council-and-final-perspective-constantinople | Under the Same Eastern Sky / Bajo el mismo cielo oriental | 381 CE | constantinople | council-and-final-perspective |

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

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/13-finite-works-logistics-jerusalem/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Eusebius reports Constantine’s patronage, work orders and requests for labor and materials at Jerusalem. The precise commencement year is not stated; the 326–330 preparation window is editorial. Site identification remains attributed and later building phases stay separate.

ES: Eusebio refiere patrocinio de Constantino, órdenes de obra y peticiones de trabajadores y materiales en Jerusalén. No indica el año exacto de inicio; el marco de preparación 326–330 es editorial. La identificación del lugar permanece atribuida y las fases de obras posteriores se mantienen separadas.

[Consulted source](https://www.newadvent.org/fathers/25023.htm): Eusebius VC III.25–40 checked for imperial church-building at Jerusalem.

Limit: Eusebius is a Christian panegyrist; source establishes patronage and his identification, not independent proof of the biblical site or the exact dating of each work.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/25023.htm): VC III.25–40, especially letter III.30–32

Limit: Panegyric attributes patronage and requests for workers/materials. Exact commencement year, construction log and quantities absent. Site identification and cult motives remain attributed; no Helena or Cross discovery in this span.

[Additional consulted passage](https://hadashot.iaa.org.il/Report_Detail_Eng.aspx?id=26542): Stasolla preliminary report published 1 September 2024, 2022 excavation; pre-Christian and early-Christian phases

Limit: Small sampled areas, preliminary interpretation; fourth-century remains include later decades and cannot be flattened into a 326–330 complex. No independent verification of sacred identification.

[Additional consulted passage](https://www.custodia.org/wp-content/uploads/2024/11/Comunicato.pdf): Sapienza preliminary November2024 report, Italian pp.1–3 and English pp.4–6

Limit: Preliminary phases include end-fourth-century Rotunda work. Cult structure interpretation differs from an earlier reconstruction; its footprint/identity and exact phase require separate review. Figures/translation not copied into production.

[Additional consulted passage](https://www.custodia.org/en/news/excavations-at-the-holy-sepulcher-the-first-volume-of-the-hagia-polis-project-at-sapienza-university/): 19 September2026 volume presentation announcement

Limit: Publication existence and project status only; no detailed plans or new dating inferred from unread book. Explicit image/text reuse restrictions remain respected.

### 14. A City beneath a New Sky

[Candidate source](https://www.britannica.com/place/Istanbul/History): Chronicon Paschale, annal 330; overview

Research candidate (not yet approved narration): Constantinopla recibe dedicación ceremonial y juegos fundacionales.

Fecha tradicional, ceremonia sobre proceso urbano anterior.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/03-new-capital/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The later Chronicon Paschale reports Constantinople’s naming and public festival in 330, conventionally dated 11 May. Urban works preceded and outlasted the ceremony. Eusebius presents Christian patronage and symbols through imperial praise; this is not evidence of a uniformly Christian population.

ES: El posterior Chronicon Paschale refiere el nombramiento y la fiesta pública de Constantinopla en 330, fechados convencionalmente el 11 de mayo. Las obras urbanas precedieron y continuaron después de la ceremonia. Eusebio presenta patrocinio y símbolos cristianos mediante elogio imperial; no demuestra una población uniformemente cristiana.

Source consultation pending: Chronicon Paschale not directly consulted; Britannica URL not consulted.

Limit: 11 May is a conventional date but remains unverified in this audit; avoid implying all construction occurred on dedication day.

Status: unavailable

[Additional consulted passage](https://catholiclibrary.org/library/view?chunk.id=00000267&docId=/Fathers-Synchronized-EN/Chronicon_Paschale__Chronicon_paschale.en.html): Annal 330, printed equivalent pp.529–530; displayed lines 378–386

Limit: Seventh-century chronicle, not eyewitness record. Five days before May Ides conventionally gives 11 May. Adjacent annal chronology and magistrate titles are not accepted wholesale. Its later bread-dole entry is not a 330 entitlement. Ceremony reports do not certify exact buildings or total construction completion.

[Additional consulted passage](https://www.newadvent.org/fathers/25023.htm): VC III.48–49 and III.54

Limit: Pro-imperial Christian panegyric; asserted suppression of cult practices does not certify universal enforcement or a single-faith population. Does not date all monuments to the dedication.

[Additional consulted passage](https://www.ime.gr/chronos/projects/justinian/en/journey/j1a.html): Topography introduction, paragraphs on Constantinian expansion and later walls

Limit: Broad position and multi-period account; fifth/sixth-century statistics and later Mese monuments are not 330 inventories. No exact Constantinian wall survey.

[Additional consulted passage](https://jfa.arch.metu.edu.tr/uploads/docs/sayilar/sayi-33-1/121-145.pdf): Pelin Yoncaci Arslan 2016, selected printed pp.121–125

Limit: Modern reconstruction from mixed literary/archaeological evidence, disputed exact geometry and statue symbolism; no image reuse license established. Later column repairs are not 330 fabric.

### 15. A Letter beyond the Frontier

[Candidate source](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.8–13

Research candidate (not yet approved narration): Constantino escribe a Shapur II sobre cristianos en el imperio persa, según Eusebio.

Eusebio presenta al emperador como protector universal; sesgo panegírico.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/15-long-distance-dispatch-nicomedia/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Eusebius transmits an imperial letter about Christians under the Persian king. Its date, circumstances and independent attestation remain debated; a 324–337 interval is a modern scholarly frame, with an earlier date argued more likely. Neither actual Persian receipt/effect nor a Nicomedia dispatch site is certified here.

ES: Eusebio transmite una carta imperial sobre cristianos bajo el rey persa. Su fecha, circunstancias y testimonio independiente siguen discutidos; el intervalo 324–337 es un marco académico moderno, con una fecha temprana defendida como más probable. Aquí no se acredita recepción o efecto real en Persia ni un lugar de despacho en Nicomedia.

[Consulted source](https://www.newadvent.org/fathers/25024.htm): Eusebius VC IV.8–13 checked: embassy and Constantine’s letter to the Persian king.

Limit: Eusebius does not establish the dossier’s c.332–333 date in this passage; identify the recipient as Sapor/Shapur only as Eusebius names him. Panegyrical source, not Persian-side confirmation.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/25024.htm): VC IV.8–13

Limit: Imperial panegyric transmits a letter; no precise date, writing city, historical carrier itinerary, Persian response or causal persecution proof. Literal wording is not used as an authentic player quotation.

[Additional consulted passage](https://sites.duke.edu/clas/files/2016/10/smith_constantine.pdf): Kyle Smith2016, selected printed pp.28–32; PDF zero-based pages49–53

Limit: Modern argument considers likely authenticity/early date while retaining debate. Independent confirmation of another Constantinian document is not confirmation of this particular letter. Interpretations of reception and effects remain hypotheses, not game triggers.

[Additional consulted passage](https://www.classics.ox.ac.uk/node/4988256): Oxford ARCON institutional project introduction and status

Limit: Identifies Nicomedia/Izmit and current archaeological mapping work, not an imperial dispatch site or precise fourth-century city plan.

### 16. The Council on the Shore

[Candidate source](https://www.newadvent.org/fathers/25023.htm): Eusebius, Life of Constantine IV.41–47; III.28

Research candidate (not yet approved narration): Sínodo de Tiro juzga a Atanasio; poco después se consagra el complejo de la Resurrección.

Narrativas de sínodo y consagración son interesadas.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/16-witness-record-comparison-tyre/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: A council met at Tyre in 335 under imperial direction. Eusebius praises the imperial demand for settlement; Athanasius later contests the proceedings and transmits protests. These are interested accounts, not a neutral transcript. The Jerusalem dedication is a separate event and city. No particular council building or waterfront venue is established here.

ES: En 335 se reunió un concilio en Tiro por dirección imperial. Eusebio elogia la exigencia imperial de arreglo; Atanasio impugna después los procedimientos y transmite protestas. Son relatos interesados, no una transcripción neutral. La dedicación de Jerusalén es otro acontecimiento y otra ciudad. Aquí no se acredita un edificio conciliar concreto ni una sede junto al agua.

[Corrected primary passage](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.41–47. Book III URL in raw candidate does not contain this locator. Eusebius is a partisan biographer.

[Consulted source](https://www.newadvent.org/fathers/25024.htm): Eusebius VC IV.41–47 checked: Tyre proceedings and Jerusalem dedication (IV.47).

Limit: The source is hostile/panegyrical toward Athanasius; separate the Tyre council from Jerusalem dedication. Chronology is not precise enough to imply immediate sequence without qualification.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/25024.htm): VC IV.40–47; Tyre41–42, Jerusalem43–47

Limit: Panegyric, imperial compulsion and settlement rhetoric are source-attributed; no neutral verdict, excavated venue or exact interval to Jerusalem. Marianus reception and Eusebius orations belong to Jerusalem, not Tyre.

[Additional consulted passage](https://www.ewtn.com/catholicism/library/apology-against-the-arians-11607): Athanasius Apologia contra Arianos §§71–84

Limit: Retrospective advocate and embedded documents; accusations of coercion, falsification and motive are allegations, not an adjudicated game truth. Modern comparative criticism is never a physical335 book.

[Additional consulted passage](https://www.ancientportsantiques.com/wp-content/uploads/Documents/PLACES/Levant/Tyr/Tyr-Marriner2007.pdf): Marriner, Morhange and Meulé2007, PNAS104(22):9218–9223, DOI10.1073/pnas.0611325104; selected introduction, subsidence discussion, conclusion and fig.6

Limit: Fig.6 contrasts332BCE and2000CE, not335CE. Sedimentation and late-Roman subsidence preclude transplanting either shore. No council-venue evidence; ©NAS2007, no explicit free-reuse license identified.

[Additional consulted passage](https://whc.unesco.org/en/list/299/): Tyre property description and modern point metadata

Limit: Headland and mainland archaeological areas identify broad context only. Page text hasCCBYSAIGO3 terms; map/individual-image rights require separate proof. Modern site point is not a council address.

### 17. The Empty Appointment

[Candidate source](https://www.newadvent.org/fathers/26023.htm): Sozomen, HE II.29

Research candidate (not yet approved narration): Arrio muere en Constantinopla antes de una readmisión prevista.

Relatos sobre circunstancias milagrosas son polémicos.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/17-rumour-and-source-investigation-constantinople/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Later church historians place Arius’s death at Constantinople before an anticipated readmission.336 is one defended modern chronology, not a date numbered by SozomenII 29–30. Bodily circumstances, exact site, causes and providential explanations are uncertain or polemical. This fictional local rumour exercise certifies no cause and stages no death.

ES: Historiadores eclesiásticos posteriores sitúan la muerte de Arrio en Constantinopla antes de una readmisión prevista.336 es una cronología moderna defendida, no una fecha numerada por SozomenoII 29–30. Las circunstancias corporales, lugar exacto, causas y explicaciones providenciales son inciertos o polémicos. Este ejercicio local ficticio de rumores no acredita causa ni escenifica una muerte.

[Consulted source](https://www.newadvent.org/fathers/26022.htm): Sozomen HE II.30 (New Advent 26022), account of Arius’ death.

Limit: Sozomen presents the death as providential punishment and explicitly reports hearsay; date 336 is not established by this passage. The cited dossier URL 26023 is Book III and is wrong for II.29.

Status: disputed

[Additional consulted passage](https://www.newadvent.org/fathers/26022.htm): SozomenHEII29–30

Limit: Fifth-century providential author; reports competing explanations and embeds Athanasius account. Not contemporary neutral medical/venue evidence, no numbered336 date. Candidate26023 is wrong book.

[Additional consulted passage](https://academic.oup.com/past/issue/227/1): Publisher issue metadata; EllenMuehlberger2015, Past&Present227(1):3–29, DOI10.1093/pastj/gtu042

Limit: Initial delegated author SarahBond was wrong and is corrected. Paper examines legendary/rumour development and later represented space; does not establish actual336 latrine coordinates or death cause. No figure/PDF copied.

[Additional consulted passage](https://academic.oup.com/jts/article-abstract/60/1/109/1684824): TimothyBarnes2009, TheExileandRecallsofArius, abstract, DOI10.1093/jts/flp003

Limit: Argues335 recall/336 death against earlier dating. Supports a defended chronology rather than unquestioned precise date or graphic narrative.

### 18. The Court without Its Emperor

[Candidate source](https://www.newadvent.org/fathers/25024.htm): Eusebius, Life of Constantine IV.61–64

Research candidate (not yet approved narration): Constantino recibe bautismo de Eusebio de Nicomedia y muere en Nicomedia.

Bautismo de Silvestre es leyenda posterior.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/18-administrative-transition-nicomedia/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Eusebius reports Constantine’s final illness, baptism in Nicomedia’s suburbs, Pentecost death and transfer of his body to Constantinople.22May 337 is a conventional calendrical date, not a numeral in VCIV 64. Eusebius names no baptizer; Jerome later names Eusebius of Nicomedia with a polemical gloss. Exact villa/site and motive remain unverified here.

ES: Eusebio refiere enfermedad final de Constantino, bautismo en los alrededores de Nicomedia, muerte en Pentecostés y traslado de su cuerpo a Constantinopla.22mayo 337 es una fecha calendárica convencional, no un número enVCIV 64. Eusebio no nombra oficiante; Jerónimo nombra después a Eusebio de Nicomedia con comentario polémico. Villa o lugar exactos y motivo siguen sin acreditarse aquí.

[Consulted source](https://www.newadvent.org/fathers/25024.htm): Eusebius VC IV.61–64 checked for baptism and death at Nicomedia.

Limit: The narrative is an imperial Christian encomium; day 22 May is not independently verified by the passage checked.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/25024.htm): VCIV61–66

Limit: Christian imperial encomium; reconstructed speeches not stenography. Nicomedia suburbs and Pentecost named, no exact22May numeral, officiating bishop name or Achyron villa in this span. Body transfer to Constantinople off-map, itinerary not supplied.

[Additional consulted passage](https://www.tertullian.org/fathers/jerome_chronicle_03_part2.htm): Chronicle annal337 baptism note and nearby death notice

Limit: Late-fourth-century chronicle names EusebiusNic and appends doctrinal blame. Nearby death notice lies in a confusing year-column sequence and readsAncyra nearNicomedia; no corrected precise villa coordinate is inferred. Not eyewitness diary.

[Additional consulted passage](https://bmcr.brynmawr.edu/2006/2006.04.03/): JanDrijvers2006 review of MarilenaAmerise2005, selected source survey

Limit: Corrects initial delegated authorHansPohlsander. Review prints377 in illness sentence, a typo excluded from chronology; its22May337 date is conventional. Achyron probable, not recovered game building. No deliberate omission motive treated as established.

### 19. Three Seals, One Inheritance

[Candidate source](https://www.newadvent.org/fathers/26012.htm): Socrates Scholasticus, Ecclesiastical History II.1 y 2.25; fuente narrativa de siglo V, no contemporánea.

Research candidate (not yet approved narration): Tras la muerte de Constantino, sus hijos toman el poder imperial; las disputas sucesorias y la distribución de territorios preceden nuevas intervenciones en asuntos eclesiásticos.

La sucesión estuvo marcada por violencia contra miembros de la familia imperial; evitar presentar la división territorial como una partición constitucional permanente ya fijada en 337.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/19-competing-dispatches-constantinople/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: After Constantine’s death, sources report succession arrangements and Dalmatius’s killing by soldiers. Eutropius says Constantius permitted rather than ordered it; later accounts and modern criticism contest responsibility. Some surviving accounts share a lost-source tradition. Constantinople here is court context, not a proven massacre address. Local household defense is disclosed fiction, not rescuing named historical victims.

ES: Tras la muerte de Constantino, las fuentes refieren arreglos sucesorios y muerte de Dalmacio a manos de soldados. Eutropio dice que Constancio permitió más que ordenó el hecho; relatos posteriores y crítica moderna discuten responsabilidad. Algunos relatos conservados comparten una tradición de fuente perdida. Constantinopla aquí es contexto de corte, no dirección acreditada de la matanza. La defensa local de hogares es ficción declarada, no rescate de víctimas históricas nombradas.

[Consulted source](https://www.newadvent.org/fathers/26012.htm): Socrates HE II.1 / II.25 identified as relevant narrative; checked introductory framing and selected passage context.

Limit: Not a contemporary dispatch; exact territorial division and timing need passage-level audit before detailed map/campaign claims.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/26012.htm): SocratesHEII2 andII25

Limit: Fifth-century Nicene historian; court doctrinal motives attributed. II25 retrospectively describes Dalmatius killed by troops without Constantius ordering/forbidding; later340/350 events are not337 gameplay. II2 eastern will-share does not prove instantaneous permanent partition.

[Additional consulted passage](https://dcc.dickinson.edu/eutropius/10-9): EutropiusBreviarium10.9.1;10.9.2 laterAquileia distinct

Limit: Compressed politically framed source; permitted rather than ordered wording does not independently prove complete command/motive. Aquileia340 and Constans350 deaths remain outside337.

[Additional consulted passage](https://www.gottwein.de/Lat/AurVict/vict_epit41.php): AnonymousEpitomedeCaesaribus41.15–20 Latin

Limit: Anonymous later epitome, not AureliusVictor proper despite page branding. Regional-share list includesDalmatius/Hannibalianus and compresses events; no permanent instantaneous three-only constitutional partition or killing address inferred.

[Additional consulted passage](https://constantinethegreatcoins.com/articles/Burgess_THE_SUMMER_OF_BLOOD_The_Great_Massacre_of_337_and_the_Promotion_of_the_Sons_of_Constantine.pdf): BurgessDOP62(2008), selected printed14–15: physicalPDF11–12, zero-based10–11; note45/source dependence

Limit: Corrects delegated claimzero-index10=printed15: actualzero10=printed14. Reconstructs lostKaisergeschichte dependence, official versions and alternative accusations. Modern scholarly inference attributed, no automatic motive/adjudication. No explicit figure/free-reuse license checked; no copied projectPDF.

### 20. The Council That Divided

[Candidate source](https://www.newadvent.org/fathers/3815.htm): Council of Sardica: introducción y cánones; síntesis contextual académica de Milton V. Anastos: https://www.myriobiblos.gr/texts/english/milton1_5.html

Research candidate (not yet approved narration): Obispos occidentales y orientales se reúnen en Sardica; el desacuerdo por Atanasio produce sesiones y decisiones separadas.

La fecha exacta se debate entre 342–344, con 343 habitual. Los cánones sobrevivieron en tradiciones griega y latina con diferencias interpretativas.

Knowledge: inherited family papers, not direct adult memory. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/20-separate-reception-logistics-sardica/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Socrates describes western and eastern bishops coming to Sardica, refusing a common conference over participation of Athanasius and Paul, then an eastern withdrawal to a separate council at Philippopolis. His 347 chronology is not adopted here;343 is a qualified editorial frame. Local reception courts are fiction, not two actual synods in the same city or a certified basilica venue.

ES: Sócrates describe la llegada a Sárdica de obispos occidentales y orientales, rechazo de conferencia común por participación de Atanasio y Pablo y posterior retirada oriental a un concilio separado en Filipópolis. Aquí no se adopta su cronología de 347;343 es un marco editorial cualificado. Los patios locales de recepción son ficticios, no dos sínodos reales en la misma ciudad ni sede basilical acreditada.

[Consulted source](https://www.newadvent.org/fathers/3815.htm): Sardica canons page: introduction and selected canons; Anastos link not opened.

Limit: Page’s own date discussion is inconsistent/uncertain (343/344; wider alternatives); avoid a precise date without resolving textual chronology.

Status: disputed

[Additional consulted passage](https://www.newadvent.org/fathers/26012.htm): SocratesHEII20

Limit: Fifth-century Nicene narrative; doctrinal labels/numbers/motive are attributed. Gives347, not selected343. Eastern separate council isPhilippopolis, not local eastern court inSardica. No exact venue or joint reconciliation.

[Additional consulted passage](https://www.newadvent.org/fathers/3815.htm): Old editorial chronology introduction and Greek/Latin canons3–5

Limit: Historical nineteenth-century editorial discussion and variant transmissions, not settled current consensus.343/344 discussion internally inconsistent wording; no proof of precise starting day. Canonical appeals are prescriptions, not every-case enforcement or a universal papacy game score.

[Additional consulted passage](https://sofiahistorymuseum.bg/en/chain-offices/serdica-ancient-cultural-and-communicative-complex): Institutional site description and phase/venue qualifications

Limit: Visible structures mixII–III/IV–VI and later phases. Protogenes basilica as council venue is explicitlypresumably, not a certified address. Leontius residence lateVI cannot be343. Current conservation/exhibition not ancient state.

[Additional consulted passage](https://www.sofiahistorymuseum.bg/en/chain-offices/west-gate-of-serdica-archeological-park): West gate and fortification phase overview

Limit: EarliestII wall/III–IV reconstruction distinct from pentagonal gate tower aftermidV and addedV–VI belt. No copying current walls into343 or historical public-gate dimensions from undated image.

### 21. The Road Back to Alexandria

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Anonymous Historia Acephala I.1–2, transmitted among Athanasian material; Socrates HE II.23, selected return letters

Research candidate (not yet approved narration): Atanasio vuelve a Alejandría tras su exilio, respaldado por cartas de Constancio II y Constante.

La Historia Acephala conserva cronología alejandrina valiosa; sus lagunas y transmisión fragmentaria aconsejan mantener fecha como día calendárico convertido desde el calendario local.

Knowledge: received family accounts; Marcus about12, no adult clerk recollection or placement in Alexandria. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/21-returning-households-escort-alexandria/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: An anonymous Alexandrian chronicle places Athanasius’ return after time in Rome and Italy on Paophi 24, rendered as 21 October 346 in the consulted edition. Socrates transmits letters concerning his recall. Six local returning households and their reception courts are disclosed fiction; no historical entourage, population count or route of the bishop is reconstructed.

ES: Una crónica alejandrina anónima sitúa el regreso de Atanasio tras su estancia en Roma e Italia en Paofi 24, convertido en 21 de octubre de 346 por la edición consultada. Sócrates transmite cartas relativas a su retorno. Los seis hogares locales que regresan y sus patios de acogida son ficción declarada; no se reconstruyen séquito histórico, cifras de población ni ruta del obispo.

[Consulted source](https://www.newadvent.org/fathers/2820.htm): Historia Acephala §I.2; Socrates HE II contextual account.

Limit: Anonymous annalistic fragment about Athanasius, not his own autobiographical chronicle. The old edition supplies calendar conversion and bracketed repairs. Transmitted return letters do not certify private motives, ordinary household identities or exact local receiving addresses.

Status: consulted

[Additional consulted passage](https://www.newadvent.org/fathers/2820.htm): Anonymous Historia Acephala I.1–2

Limit: Paophi24 and old edition conversion; bracketed emendations visible. Not a list of ordinary household migrants, precise entrance gate or historical receiving courtyard.

[Additional consulted passage](https://ccel.org/ccel/schaff/npnf204/npnf204.xxv.ii.i.html): Archibald Robertson, old NPNF editorial introduction to Historia Acephala

Limit: Anonymous annalist under Theophilus, imperfect Latin transmission and internal chronology repairs; editor argues chronological value. His reconstruction is attributed, not a modern consensus or independent author identification from a web heading.

[Additional consulted passage](https://www.newadvent.org/fathers/26012.htm): Socrates HE II.23, introduction, three imperial letters and opening of Julius letter

Limit: Later Nicene historical narrative transmitting letters. No private royal motives, independent authentication of every letter or exact reception district. No claim to have read the full chapter.

[Additional consulted passage](https://www.cealex.org/evenement/cartalex-is-online/): CEAlex CartAlex institutional announcement

Limit: 1866 reconstruction,1993 archaeological plan and1933–1948 cadastre are distinct layers, not a346 shoreline or dated household parcel. No map reuse license established, no institutional figure copied.

### 22. The Dispatch from Gaul

[Candidate source](https://www.newadvent.org/fathers/26012.htm): Socrates, Ecclesiastical History II.25–26; contexto secundario en CCEL, Socrates and Sozomen, Book IV.1: https://www.ccel.org/ccel/schaff/npnf202.iii.ix.i.html

Research candidate (not yet approved narration): Constante es asesinado en la Galia durante la usurpación de Magnencio; Constancio II queda como único emperador y el equilibrio que había favorecido a Atanasio desaparece.

Socrates vincula el cambio político con nuevos conflictos eclesiásticos, pero no reducir toda la guerra civil a una disputa teológica.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/22-civilian-record-preservation-milan/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Later church histories report that Constans was killed in Gaul during the usurpation of Magnentius in 350. Constantius II still faced a rival; this Milan setting receives news from Gaul rather than depicting the killing.

ES: Las historias eclesiásticas posteriores relatan que Constante murió en la Galia durante la usurpación de Magnencio en 350. Constancio II aún tenía un rival; este escenario de Milán recibe noticias de la Galia y no representa la muerte.

[Consulted source](https://www.ccel.org/ccel/schaff/npnf202.iii.ix.i.html): Socrates/CCEL passage on Constans’ death in Gaul in 350 and Magnentius.

Limit: Candidate is wrong to say Constantius II became sole emperor in 350; Magnentius remained a rival until defeated in 353. Geographic focus Milan is reception of news, not death site.

Status: disputed

[Additional consulted passage](https://www.newadvent.org/fathers/26012.htm): Socrates HE II.25

Limit: Later Nicene ecclesiastical account; war is not reduced to theology, private motives are attributed. Milan is fictional reception, not the killing site. Constantius faces a western rival in350.

[Additional consulted passage](https://www.thelatinlibrary.com/eutropius/eutropius10.shtml): Eutropius Breviarium X.9–12

Limit: Constans killing near the Spanish frontier/Helena is not a Milan killing. Do not pull Magnentius final defeat into350. Exact killing site and event-specific Milan parcel not certified.

[Additional consulted passage](https://www.museoarcheologicomilano.it/it/pagine-virtual-tour/la-torre-poligonale-e-le-mura): Municipal museum description of Maximian wall phases

Limit: LateIII/earlyIV wall rebuilding and eastern extension provide broad urban context. Later medieval names/decorations are not350. Textual descriptions do not identify a storage court or prove absence of ancient small waterways.

[Additional consulted passage](https://www.museoarcheologicomilano.it/web/museo-archeologico-milano/scopri-il-museo/le-torri-romane-e-il-monastero-maggiore/la-torre-del-circo): Municipal museum circus and tower phase description

Limit: LateIII/earlyIV circus is distinct from itsVIII–IXbell-tower adaptation and later events. No350 dispatch reception venue, route widths, exact ancient drainage or figure reuse right established.

### 23. The Seal and the Exile

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Sozomen HE IV.9, Milan council passage, distinguished from later Alexandria account; Markauskas2015 printed72–73

Research candidate (not yet approved narration): Tras presión imperial en sínodos occidentales, Atanasio es perseguido; tropas entran en una iglesia de Alejandría durante la noche y él escapa.

La cronología de la Historia Acephala sitúa el ataque en febrero de 356. Atanasio escribe como parte enfrentada; sus cifras y caracterización de adversarios requieren cautela.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/23-bounded-political-pressure-milan/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Sozomen describes a council at Milan at which bishops were pressed to condemn Athanasius and dissenting bishops were exiled.

ES: Sozomeno describe un concilio en Milán en el que se presionó a los obispos para condenar a Atanasio y se exilió a obispos disidentes.

[Consulted source](https://www.newadvent.org/fathers/2820.htm): Athanasius Historia Acephala and Apologia de Fuga checked for February 356 church raid/escape; no evidence for the Milan hearing in this source.

Limit: Historical collection record retained as provenance, superseded for current selection. Episode has wrong local event/date alignment: Milan hearing and Alexandria raid are distinct episodes. Athanasius is a partisan witness; figures and adversary descriptions require caution.

Status: superseded-candidate-only

[Additional consulted passage](https://www.newadvent.org/fathers/26024.htm): Sozomen, Ecclesiastical HistoryIV.9, Milan council

Limit: Later partisan church history; its theological judgements are attributed to the author. Conventional355 date and exact local hearing logistics are not independent court records. This event is distinct from the Alexandria night raid in356.

[Additional consulted passage](https://www.newadvent.org/fathers/26024.htm): Sozomen HE IV.9, council paragraph and immediate outcome

Limit: Later pro-Nicene narration; fear/fraud/motives and providential judgment are authorial. No reliable exact attendance, synod room or private transcript. Avoid importing his inconsistent bishop/place label or assembled exile list as attendance proof.

[Additional consulted passage](https://pure.manchester.ac.uk/ws/portalfiles/portal/54577636/FULL_TEXT.PDF): Melissa Markauskas2015, From Privilege to Proscription, selected printed72–74; physical PDF72–74, zero71–73

Limit: Milan355, differentiated responses and Hilary nonattendance; synod and separate Liberius legal anecdote distinct. Rimini359 belongs to next episode. Secondary argument, no venue plan. Copyright retained by author, temporary research PDF not copied into project assets.

### 24. The Night of the Open Doors

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Anonymous Historia Acephala IV.5, with later transfer V.6 distinguished; Athanasius Apologia de Fuga24–25

Research candidate (not yet approved narration): Tras presión imperial en sínodos occidentales, Atanasio es perseguido; tropas entran en una iglesia de Alejandría durante la noche y él escapa.

La cronología de la Historia Acephala sitúa el ataque en febrero de 356. Atanasio escribe como parte enfrentada; sus cifras y caracterización de adversarios requieren cautela.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/24-night-civilian-withdrawal-alexandria/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Athanasius describes a nighttime military assault and his escape from an Alexandrian church. The anonymous Historia Acephala IV.5 identifies Theonas and the night of Mechir13/14; exact civil conversion and building footprint are qualified. Later church transfer and George’s357 arrival are separate. Eight playable civilians, their road junction and finite combat roster are explicit local fiction, not a verified assault headcount or control of the bishop’s fate.

ES: Atanasio describe un asalto militar nocturno y su huida de una iglesia alejandrina. La Historia Acephala anónima IV.5 identifica Theonas y la noche de Mequir13/14; se cualifican conversión civil exacta y huella del edificio. El traslado posterior de iglesias y la llegada de Jorge en357 son hechos separados. Los ocho civiles jugables, su cruce de caminos y plantilla finita de combate son ficción local explícita, no cifras acreditadas del asalto ni control del destino del obispo.

[Consulted source](https://www.newadvent.org/fathers/2814.htm): Athanasius Historia Acephala / Apologia de Fuga; exact raid account checked.

Limit: Historical collection record retained as provenance, superseded for current selection. Potential duplicate with episode 23; source is partisan and the reported troop count is not independently verified. Keep only if the two episodes have distinct historical content.

Status: superseded-candidate-only

[Additional consulted passage](https://www.newadvent.org/fathers/2814.htm): Athanasius Apologia de Fuga24–25; §6 read only to distinguish later sequence

Limit: Apologetic self-defense and providential framing are attributed. More-than5000 is source assertion, not independently verified or native population requirement. No verbatim dialogue or theological damage modifier.

[Additional consulted passage](https://www.newadvent.org/fathers/2820.htm): Anonymous Historia Acephala IV.5 and V.6

Limit: Fragment/old edition conversions, no certified civil-calendar conversion or excavated356church parcel. June356church transfer/George357 differ from initialFebruary night.

[Additional consulted passage](https://www.cealex.org/evenement/cartalex-is-online/): CEAlex CartAlex layer dates and institutional GIS announcement

Limit: Multi-date controls do not certify Theonas address,356streets/coastline or reuse license. No institutional map copied.

### 25. The Winter of Divided Voices

[Candidate source](https://www.newadvent.org/fathers/26012.htm): Sulpicius Severus Chronica II.41–44; Socrates HE II.37 with chronology cautions; Markauskas2015 printed73–74

Research candidate (not yet approved narration): Constancio convoca simultáneamente un concilio occidental en Rimini y uno oriental en Seleucia para buscar una fórmula doctrinal común; ambos producen controversias y no una unidad estable.

Socrates escribe en el siglo V y es pro-niceno. Los sínodos no fueron una única reunión ni una decisión idéntica; evitar etiquetar a todos los participantes con categorías posteriores simplificadas.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/25-delegate-and-draft-network-rimini/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: In 359 the western council met at Ariminum, separately from Seleucia. Later pro-Nicene accounts describe rival drafts, delegations, pressure and an eventual disputed settlement. Exact meeting places and a neutral transcript remain unverified.

ES: En 359 el concilio occidental se reunió en Arímino, separado de Seleucia. Relatos posteriores favorables a Nicea describen borradores rivales, delegaciones, presión y un acuerdo final disputado. La sede exacta y una transcripción neutral siguen sin verificar.

[Consulted source](https://www.newadvent.org/fathers/26012.htm): Socrates HE II.37 and II.39–40: Ariminum and Seleucia both met in 359, Seleucia divided into factions; the text places Seleucia meeting on 27 September.

Limit: Socrates is a fifth-century pro-Nicene narrator. The selected page supports that these were separate synods, not that they pursued an identical formula or produced a single outcome.

Status: consulted

[Additional consulted passage](https://www.thelatinlibrary.com/sulpiciusseveruschron2.html): Chronica II.41–44; II.42 distinguishes Seleucia

Limit: Later pro-Nicene account: numbers, age contrasts, alleged fraud and motives remain source claims. Winter/seven-month language attributed, not a real-time survival countdown. Church/empty hall not securely located; Taurus prefect distinct from magistri officialibus. No authentic council draft, signature or bishop role spawned.

[Additional consulted passage](https://www.newadvent.org/fathers/26012.htm): HE II.37, complete chapter selected directly

Limit: Fifth-century pro-Nicene history and embedded documents, Greek transmission of Latin drafts. Do not infer neutral verbatim transcript, motives, modern faction taxonomy or exact council room. Embedded Liberius exile sequence is chronologically unsafe; do not move his355exile into359. Nice in Thrace is not Nicaea in Bithynia.

[Additional consulted passage](https://pure.manchester.ac.uk/ws/portalfiles/portal/54577636/FULL_TEXT.PDF): Markauskas2015, selected printed73–74; PDFphysical73–74

Limit: Praetorian prefect Taurus, fiscal council arrangements and legal context. No ancient building footprint, creed truth verdict or universal acceptance practice. CopyrightedPDF temporary only.

[Additional consulted passage](https://www.comune.rimini.it/sites/default/files/2021-07/c.rel_.archeo_0_0.pdf): Municipal archaeological report selected PDF46–48, printed47–49; VIII.2 and beginningVIII.3

Limit: Multiphase roads/walls/monuments, uncertain harbor/public buildings and later contraction. Broad urban periods do not certify359 footprint or council venue; later Christian archaeological traces do not disprove fourth-century literary church reports. Report/platemaps not imported as licensed assets.

[Additional consulted passage](https://www.comune.rimini.it/sites/default/files/2021-07/c_1_1_1.pdf): C1.1.1, Analisi evolutiva del centro storico, legend and one-page actualpixels

Limit: Despite generic title this is modern urban transformation, not Roman/359phaseplan. Used only to flag later rebuilding and modern footprint risk. Copyright unresolved, temp only.

### 26. Altars of a New Reign

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/22*.html): Ammianus Res Gestae XXII.2.1–5 and XXII.5.1–4

Research candidate (not yet approved narration): Juliano entra en Constantinopla tras la muerte de Constancio II y asume el gobierno único; reabre templos y restablece sacrificios públicos.

Ammiano admira a Juliano. Las prácticas religiosas se reanudaron por decreto y patronazgo, pero no toda la población cambió de culto ni se revirtió de inmediato la infraestructura cristiana.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/26-plural-civic-logistics-constantinople/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Ammianus describes Julian entering Constantinople after Constantius’ death and later ordering temples opened and sacrifice restored. His explanation of the emperor’s motives is authorial interpretation; the decree does not establish uniform implementation or belief.

ES: Amiano describe la entrada de Juliano en Constantinopla tras la muerte de Constancio y su posterior orden de abrir templos y restablecer sacrificios. Su explicación de los motivos imperiales es interpretación del autor; el decreto no demuestra aplicación ni creencia uniformes.

[Consulted source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/22*.html): Ammianus XXII.2 §1 checked for Julian’s entry into Constantinople and sole rule.

Limit: This passage does not support reopening temples/restoring sacrifices; that needs a separate exact source. Ammianus is an admiring pagan narrator.

Status: disputed

[Additional consulted passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/22*.html): XXII.2.1–5 and XXII.5.1–4; especially2.4 and5.2

Limit: Later fourth-century narrator and former officer, not a neutral stenographer of the palace. Entry11December in this edition; use broad working frame for subsequent policy. Reopening/sacrifice orders do not quantify each local temple, acceptance or practice. Christian discord and imperial calculation in5.4 remain attributed interpretation; no recycled hostile generalization or authentic dialogue.

### 27. The Return That Did Not Last

[Candidate source](https://www.tertullian.org/fathers/julian_apostate_letters_1_trans.htm): Julian Letter24 in Wright1923 translation; anonymous HistoriaAcephalaVII9–11/VIII12–13; AmmianusXXV.3.1–23 for off-map report

Research candidate (not yet approved narration): Juliano permite el regreso de obispos exiliados y luego vuelve a expulsar a Atanasio de Alejandría; su campaña contra Persia termina con su muerte en Mesopotamia.

Juliano presenta su conducta como aplicación de la ley; cartas imperiales son retóricas oficiales. Las circunstancias exactas de su herida mortal son inciertas.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/27-return-and-departure-records-alexandria/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Athanasius returned to Alexandria in 362 and later left after Julian ordered his departure. Julian’s own letter and the anonymous chronicle frame the return differently. Julian died during his Persian expedition in 363; that distant event and its later announcement at Alexandria remain distinct.

ES: Atanasio regresó a Alejandría en 362 y más tarde partió después de que Juliano ordenara su salida. La carta de Juliano y la crónica anónima presentan el regreso de forma diferente. Juliano murió durante su expedición persa en 363; ese hecho distante y su posterior anuncio en Alejandría siguen separados.

[Consulted source](https://romanletters.org/letters/julian_emperor/24/): Julian Letter 24 checked for order that Athanasius leave Alexandria; Ammianus XXV checked for death during Persian campaign.

Limit: Julian’s letter is polemical; exact wound cause and killer are uncertain. The Persian campaign/death is not a local Alexandria event—present as reported news, not on-map action.

Status: superseded-candidate-only

[Additional consulted passage](https://www.tertullian.org/fathers/julian_apostate_letters_1_trans.htm): W.C.Wright1923 translation, Letter24, both shortparagraphs and notes; selected no wholecorpus claim

Limit: Official imperial polemic, not independent proof of lawfulness or public sentiment. Date362/Constantinople and February21return date appear in editorialheading/footnote, not text ofletter. Modernizedmirror inserts explanations; neither its catalogdate nor insertedprivatecharacterization is adopted as an ancient statement. No manuscript inspected or Greek apparatus collated.

[Additional consulted passage](https://www.newadvent.org/fathers/2820.htm): Anonymous HistoriaAcephalaVII9–11 andVIII12–13, selectedparagraphs

Limit: Sourcecalendar/translation has date/formula issues: returnMechir27, staythroughPaophi26, departurepublicationPaophi27; broad362frame retained without certifying exact civilcalendarconversion. Deathannouncement inAlexandria in363 differs from deathatPersianfront. Chronicle says prefectorderedreturntoChurch whileJulianlaterclaimsreturnpermissiononlytohomecountries: preserve interested institutionalaccounts, do not silently harmonize or adjudicate legality. Claimedextraordinary/providentialevents not objective facts.

[Additional consulted passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/25*.html): AmmianusXXV.3.1–23, especially3.6–9/3.23

Limit: Ammianusservedonthecampaign but selectedpassage doesnotestablish hisphysicalwitnessofthewound/tentdialogue. Lastspeech, portents,virtue,polemicalorprovidentialinterpretation remain authorial. No namedkiller, divinetarget,playableemperorrescue,preciseunverifiedbattletileor localAlexandriabattle. AllPersiangeography off-map.

### 28. Beyond the Quiet River

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Anonymous Historia Acephala X.15–XI.16

Research candidate (not yet approved narration): The anonymous chronicle reports a new order, local resistance, Athanasius’ concealed departure and later recall.

Do not certify a New River villa coordinate, derive a Gregorian date from an editorial parenthesis, make a historical bishop playable or treat the official fine as player religious currency.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/30-policy-reversal-alexandria/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: An anonymous Alexandrian chronicle reports a renewed expulsion order in 365, a dispute over whether it applied to Athanasius, his concealed withdrawal and an imperial letter followed by his return in 366. Its account does not locate the villa or provide a neutral legal judgment.

ES: Una crónica alejandrina anónima refiere una nueva orden de expulsión en 365, una disputa sobre si afectaba a Atanasio, su retirada oculta y una carta imperial seguida de su regreso en 366. Su relato no localiza la villa ni ofrece un juicio jurídico neutral.

[Consulted source](https://www.newadvent.org/fathers/2820.htm): Anonymous Historia Acephala X.15–XI.16

Limit: Do not certify a New River villa coordinate, derive a Gregorian date from an editorial parenthesis, make a historical bishop playable or treat the official fine as player religious currency.

Status: consulted as bounded source collection; full dossier pending

[Additional consulted passage](https://www.newadvent.org/fathers/2820.htm): Historia Acephala X.15–XI.16, XII.17 chronological control

Limit: Athanasius-favorable anonymous account, not his autobiography. The New River, villa and church apartment are unlocated. Imperial letter, local announcement and return are distinct. Source calendar and later editorial civil dates remain qualified.

[Additional consulted passage](https://www.cambridge.org/core/journals/antiquity/article/streets-and-houses-of-roman-alexandria-revisited/71B9F539334D3FCA6A222D43FF0219D2): Majcherek2021, abstract and excavation discussion through street-grid paragraph; early Roman phase cautions

Limit: Local excavation does not certify a complete365 city grid, the New River, a villa or a channel crossing. Early Roman houses are not assumed unchanged in the later fourth century.

[Additional consulted passage](https://egymonuments.gov.eg/archaeological-sites/kom-el-dikka/): Official institutional description of Roman/Byzantine residential and civic remains

Limit: Modern archaeological visitor site, not a365 snapshot. Lecture halls, baths, odeon and mosaic phases need individual dating before scenery selection.

### 29. The Empty Chair

[Candidate source](https://www.newadvent.org/fathers/2820.htm): Historia Acephala XII.17 and XIII.19; Socrates HE IV.20–22, with chronology conflict

Research candidate (not yet approved narration): Athanasius’ death and the contested succession changed Alexandrian church leadership. The adopted 373 frame is not obtained by silently correcting Socrates’ conflicting synchronism.

Socrates IV.20 names the second consulate of Gratian and Probus, identified as371 by the old translator’s note. Preserve this against the373chronology from other evidence; allegations remain attributed and exact civil-day conversion unverified.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/31-contested-succession-alexandria/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Athanasius’ death, conventionally dated 373, was followed by Peter’s succession and a struggle over Alexandrian church possession. Later Nicene historians report imperial intervention, Peter’s imprisonment and flight, and Lucius’ installation. Socrates’ own consular synchronism points to 371 in the translation’s note; it is preserved rather than silently repaired.

ES: A la muerte de Atanasio, fechada convencionalmente en 373, siguieron la sucesión de Pedro y una disputa por la posesión de las iglesias alejandrinas. Historiadores nicenos posteriores refieren intervención imperial, prisión y huida de Pedro e instalación de Lucio. El sincronismo consular de Sócrates apunta a 371 según la nota de traducción; se conserva sin corregirlo en silencio.

[Consulted source](https://www.newadvent.org/fathers/2820.htm): Historia Acephala XII.17 and XIII.19; Socrates HE IV.20–22, with chronology conflict

Limit: Socrates IV.20 names the second consulate of Gratian and Probus, identified as371 by the old translator’s note. Preserve this against the373chronology from other evidence; allegations remain attributed and exact civil-day conversion unverified.

Status: consulted as bounded source collection; full dossier pending

[Additional consulted passage](https://www.newadvent.org/fathers/2820.htm): Historia Acephala XII.17 and XIII.19

Limit: Anonymous favorable chronicle, not Athanasius’ autobiography. Its consular/calendar formula and editorial May3conversion are not a verified Gregorian day. No exact succession room, funeral route or urban battle plan.

[Additional consulted passage](https://www.newadvent.org/fathers/26014.htm): Socrates HE IV.20–22, with IV.1 as prior-claimant context

Limit: Later Nicene historian, not an eyewitness assertion. Providential causation, hostile labels and ethnic stereotypes remain the author’s framing. Peter’s letters cited by Socrates were not independently read. No two modern translations count as two independent ancient witnesses.

[Additional consulted passage](https://www.ccel.org/ccel/schaff/npnf202.ii.vii.xx.html): Socrates IV.20 and NPNF editorial footnote616

Limit: This is an editor’s comparison, not a fresh reading of Jerome or a correction to Socrates’ words. Do not claim his consular phrase converts to373.

[Additional consulted passage](https://www.newadvent.org/fathers/26026.htm): Sozomen HE VI.19

Limit: Not demonstrated independent eyewitness corroboration of Socrates. Descriptions of cruelty and generalization about parties stay attributed; no playable massacre, torture sequence or game-unit count is derived. VI.20desert/island material is outside this local episode.

[Additional consulted passage](https://athanasius.phil.uni-erlangen.de/athanasius-life-and-works.html): Uta Heil, introduction and selected1.12–1.13paragraphs, especially death endpoint

Limit: Its displayed death day differs from the older translation’s parenthesis; retain year373only. Modern synthesis is not a new ancient witness or geographic survey. Unread editions, Jerome, Peter’s letters and manuscript apparatus remain pending.

### 30. Where the Eagles Fell

[Candidate source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/31%2A.html): Ammianus XXXI.11–13, especially12.10 and13.12–17

Research candidate (not yet approved narration): Ammianus describes a Roman defeat near Hadrianopolis and preserves competing accounts of Valens’ death. Local survivor gameplay must not reverse that outcome.

No exact battlefield or wagon-circle coordinate, emperor rescue, verified fatal-wound witness, religious cause or unlimited enemy production follows from the passage.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/32-defeat-and-withdrawal-adrianople/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The Roman army was defeated near Hadrianopolis in 378 and Valens died. Ammianus preserves conflicting death accounts and describes scattered survivors. Their local escape does not reverse the defeat, and survival did not guarantee admission to the city.

ES: El ejército romano fue derrotado cerca de Adrianópolis en 378 y Valente murió. Amiano conserva versiones distintas de su muerte y describe supervivientes dispersos. Su fuga local no invierte la derrota, y sobrevivir no garantizaba entrar en la ciudad.

[Consulted source](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/31%2A.html): Ammianus XXXI.11–13, especially12.10 and13.12–17

Limit: No exact battlefield or wagon-circle coordinate, emperor rescue, verified fatal-wound witness, religious cause or unlimited enemy production follows from the passage.

Status: consulted as bounded source collection; full dossier pending

[Additional consulted passage](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Ammian/31%2A.html): Ammianus31.12.3/10–17,31.13.1–19;31.15.1–4as aftermath control

Limit: Retrospective literary military narrative. Motives, ethnic stereotypes and broad casualty ratios belong to the author’s account, not measured tactical data or a license to portray religious guilt. No exact modern battlefield, circle, cottage, formation or universal route.

[Additional consulted passage](https://penelope.uchicago.edu/Thayer/L/Roman/Texts/Ammian/31%2A.html): 31.12.3/10–11

Limit: The eighth hour is not an eight-mile radius; the earlier fifteen-mile position is not the final battle coordinate. Exact local-time/Gregorian conversion not performed.

[Additional consulted passage](https://sourcebooks.web.fordham.edu/source/378adrianople.asp): Short Yonge1862selection, march clause

Limit: A translation discrepancy, not a measured route. Do not infer an author’s dependence on Yonge from the same number alone.

### 31. The Burden of the Purple

[Candidate source](https://www.newadvent.org/fathers/26015.htm): Socrates HE V.2–3

Research candidate (not yet approved narration): Socrates reports Theodosius’ elevation at Sirmium and a still-divided religious landscape after Valens. The appointment is fixed narrated history.

Socrates NPNF V.2 gives16January, whereas Marcellinus379.1 givesXIIIIkalendasFebruarias, conventionally19January; the selected modern synthesis adopts19January. Preserve these transmitted distinctions without a manuscript collation or silently corrected quotation. Use year379only pending chronology review. Accession is fixed history, not bought by player payments; the religious survey is not simultaneous uniform implementation. No exact proclamation room or ancient landmask is certified.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/33-accession-and-reassembly-sirmium/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: Socrates reports Theodosius’ elevation at Sirmium and a still-divided religious landscape after Valens. The appointment is fixed narrated history.

ES: Sócrates refiere la elevación de Teodosio en Sirmio y un panorama religioso todavía dividido tras Valente. El nombramiento es historia fija narrada.

[Consulted source](https://www.newadvent.org/fathers/26015.htm): Socrates HE V.2–3

Limit: The translated V.2 gives January16 and a consular formula. Do not silently replace its day from a different chronology or infer simultaneous implementation of every recall and policy; no Sirmium map is certified yet.

Status: consulted as bounded source collection; full dossier pending

[Additional consulted passage](https://www.newadvent.org/fathers/26015.htm): Socrates HE V.2–3; V.6–7 as later-event control

Limit: Later Nicene author. Universal praise, confession labels and motives are attributed, not an objective competence rating or an independently proved private council. Later episcopal outcomes in a survey paragraph are not all instantaneous379changes. V.6arrival24November and V.7transfer26November are separate from accession.

[Additional consulted passage](https://www.newadvent.org/fathers/26027.htm): Sozomen HE VII.1–2; VII.4–5 as scope control

Limit: Nicene retrospective framing, no exact accession day in this selected passage and no established independence from Socrates. Law, recall, local reception and later possession of churches cannot be compressed into one playable coronation. Do not turn its generalizations into a complete geographical census.

[Additional consulted passage](https://www.thelatinlibrary.com/marcellinus1.html): Marcellinus Comes Chronicon, preface and379.1–2;380entry as chronology control

Limit: Sixth-century chronicle with favorable Catholic/Theodosian evaluation; not a379eyewitness. Army victories in379.2 lack local tactical detail and are not a reason to invent a Sirmium battle. Its380December church-restoration month differs from Socrates’November report; preserve the distinction for episode34. Italica origin in the entry is not an approved birthplace scene.

[Additional consulted passage](https://www.roman-emperors.sites.luc.edu/theo1.htm): David Woods, TheodosiusI, selected Origin and Early Career and initial Foreign Policy paragraphs; author/date/footer checked

Limit: Specific reconstructive arguments about retirement, the father’s death, motives, military seniority or exact transfer dates are the author’s arguments, not imported as established facts. A modern summary is not another ancient witness or a surveyed379map.

[Additional consulted passage](https://ai.ac.rs/en/7729/): Institute of Archaeology, Sirmium project, selected site/urban areas/communication/palatial remains paragraphs

Limit: No exact379proclamation room, urban dry-ground mask, intact street footprint or seasonal inundation. Modern site images are archaeological context, not accession documentation.

### 32. The Weight of an Imperial Word

[Candidate source](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/Thessalonique.htm): Codex Theodosianus 16.1.2, Edictum de fide catholica; edición de texto latino y encabezamiento consultados.

Research candidate (not yet approved narration): Graciano, Valentiniano II y Teodosio publican en Tesalónica una constitución que prescribe la fe nicena para los pueblos bajo su gobierno y clasifica a otros grupos como herejes.

Es una norma legal dirigida a Constantinopla, no prueba de cumplimiento uniforme inmediato ni de la desaparición de otras religiones. Evitar llamarla, sin matices, conversión instantánea del imperio.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/28-law-and-local-reception-thessalonica/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: A constitution issued at Thessalonica on 27 February 380 bears the names of Gratian, Valentinian and Theodosius and addresses the people of Constantinople. It prescribes a religious norm; the text does not measure its reception or enforcement.

ES: Una constitución emitida en Tesalónica el 27 de febrero de 380 lleva los nombres de Graciano, Valentiniano y Teodosio y se dirige al pueblo de Constantinopla. Prescribe una norma religiosa; el texto no mide su recepción ni cumplimiento.

[Consulted source](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/Thessalonique.htm): CTh 16.1.2 Latin text and editorial heading checked.

Limit: The constitution is addressed to the people of Constantinople though issued at Thessalonica; it does not prove uniform enforcement, conversion, or universal application. Header date/location should be checked in a critical edition if exact day matters.

Status: consulted

[Additional consulted passage](https://droitromain.univ-grenoble-alpes.fr/Constitutiones/Thessalonique.htm): CTh XVI.1.2: complete short Latin constitution, heading and subscription

Limit: The compilation transmits a norm. No individual local receipt, dispatch route, exact room, universal conversion or uniform enforcement is established.

[Additional consulted passage](https://thessaloniki.gr/wp-content/uploads/2019/11/Thessaloniki-Monuments-Map-ENG-Web.pdf): Municipality 2013: physical PDF page 5 (printed 4–5), page 12 (printed 18–19), copyright back cover

Limit: Not a georeferenced 380 plan, dated coast or DEM. Exact place of law issue remains unknown. Copyrighted PDF consulted temporarily, not redistributed.

### 33. The Doors of New Rome

[Candidate source](https://www.newadvent.org/fathers/26015.htm): Socrates HE V.6–7

Research candidate (not yet approved narration): Socrates separately narrates Theodosius’ arrival and church-possession changes at Constantinople. His theological framing is attributed; it is not automatic implementation of the February law.

Socrates V.6 reports arrival24November and V.7 church possession26November380 as separate events; Marcellinus380 instead places church restoration inDecember. Preserve the discrepancy, not a harmonized exact calendar. Sozomen’s later enlarged Anastasia building and attributed miracles do not certify the380venue or terrain. Gregory’s later resignation and381council must remain distinct fromNovember380. No exact church footprint, universal compliance or playable forced conversion follows.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: selection and mechanic authored; full world/objective/balance/screen/map dossier pending

Architect-corrected claim EN: Socrates separately narrates Theodosius’ arrival and church-possession changes at Constantinople. His theological framing is attributed; it is not automatic implementation of the February law.

ES: Sócrates narra por separado la llegada de Teodosio y los cambios de posesión de iglesias en Constantinopla. Su interpretación teológica queda atribuida; no es cumplimiento automático de la ley de febrero.

[Consulted source](https://www.newadvent.org/fathers/26015.htm): Socrates HE V.6–7

Limit: Keep November24arrival and November26transfer as separately reported dates; no universal compliance, modern denominational schism, certified church parcel or playable forced conversion.

Status: consulted as bounded source collection; full dossier pending

[Additional consulted passage](https://www.newadvent.org/fathers/26015.htm): Socrates HE V.6–8, especiallyV.6arrival andV.7transfer

Limit: Retrospective Nicene framing. The narrator’s peace/orthodoxy judgments and reported speeches are not an objective moral verdict or independently authenticated verbatim dialogue. V.7also places a resignation of Gregory in its narrative sequence; do not automatically date every episcopal action toNovember380without comparing chronology and381council evidence.

[Additional consulted passage](https://www.newadvent.org/fathers/26027.htm): Sozomen HE VII.4–5, withVII.7–8as council context

Limit: No independent eyewitness proof or complete urban transfer register. Miracles and the etymology of Anastasia are attributed beliefs/traditions, not geographic proof or mandatory gameplay powers. Later magnificent church fabric cannot be pasted onto380. Law, arrival and physical possession are not one single instant.

[Additional consulted passage](https://www.thelatinlibrary.com/marcellinus1.html): Marcellinus Comes Chronicon380entry, labelled MommsenChronicaMinoraII1894

Limit: That month differs from Socrates’Novemberreport. Do not relabel it November, claim all chronicles agree, or assign the exact same dated transfer from modern harmonization alone. Its favorable confessional language remains attributed.

### 34. Under the Same Eastern Sky

[Candidate source](https://www.papalencyclicals.net/councils/ecum02.htm): Credo y cánones del Concilio de Constantinopla I; la página señala el problema de la transmisión del credo y el estatus inicialmente limitado del concilio.

Research candidate (not yet approved narration): Un concilio en Constantinopla reafirma la fe nicena, trata controversias sobre el Espíritu y fija en canon 3 la precedencia honorífica del obispo de Constantinopla después de Roma.

El credo conocido como niceno-constantinopolitano se atestigua textualmente en Calcedonia (451); no atribuir sin reservas toda su forma conservada a actas contemporáneas de 381. El canon 3 trata rango, no una división moderna entre católicos y ortodoxos.

Knowledge: fictional dated clerk experience with local placement specified in the complete dossier; external affairs remain reports. one local map; distant events use explicitly attributed dispatches; imperial motive never asserted from silence

Dossier status: authored full draft; independent source/geometry/native/balance gates pending

[Authored episode dossier](episodes/29-council-and-final-perspective-constantinople/15-odyssey-dossier.md) — independent approval pending

Architect-corrected claim EN: The council at Constantinople in 381 reaffirmed Nicene faith. Its transmitted canons distinguish diocesan administration from Constantinople’s honorary rank after Rome. Later transmission of the creed and later synodal letters are separate evidence; this is not the modern Catholic–Orthodox division.

ES: El concilio de Constantinopla de 381 reafirmó la fe nicena. Sus cánones transmitidos distinguen la administración diocesana del rango honorífico de Constantinopla tras Roma. La transmisión posterior del credo y las cartas sinodales posteriores son testimonios distintos; no es la división moderna entre católicos y ortodoxos.

[Consulted source](https://www.papalencyclicals.net/councils/ecum02.htm): Council of Constantinople I page, canon 3 and editorial transmission note.

Limit: Canon is about precedence/honor, not a modern Catholic/Orthodox split or unrestricted jurisdiction. Creed text transmission is separate; page is a translation/compilation.

Status: consulted

[Additional consulted passage](https://www.ccel.org/ccel/schaff/npnf214.ix.viii.iv.html): Percival/NPNF XIV, CanonIII body and selected editorial notes

Limit: Modern transcription of old translation, not Greek manuscript. The body states honor after Rome because New Rome; later commentators disagree about wider interpretation. No immediate schism or complete jurisdiction follows.

[Additional consulted passage](https://www.ccel.org/ccel/schaff/npnf214.ix.viii.iii.html): CanonII body

Limit: Normative text, not observed compliance or a modern national church map. Greek apparatus and complete later reception not examined.

[Additional consulted passage](https://www.newadvent.org/fathers/3808.htm): Canon1, synodal letter to Theodosius; comparison of short-page numbering

Limit: Incomplete/misnumbered web rendering is rejected for canonIII numbering. Do not transplant its subsequent numbers into authored content.

[Additional consulted passage](https://www.papalencyclicals.net/councils/ecum02.htm): Tanner editorial introduction: transmission/382 letter/later canons; canonIII cross-check

Limit: Editorial transmission note only; no modern translation copied. No original council minutes, complete manuscript tradition or later reception independently verified.

[Source-audit passage](https://www.papalencyclicals.net/councils/ecum02.htm): Constantinople I: canon 3; creed and canons, but status/transmission caveat

The source text supports a council traditionally dated 381 and canon 3 giving Constantinople honor after Rome because it is New Rome; creed transmission/history is separate from these canons.

Limit: Canon 3 does not establish papal/imperial jurisdiction or later East-West schism. Page is a compiled translation; it acknowledges transmission complexity.

Coverage: Opened council page and checked canon 3 and creed section; not manuscript apparatus.
