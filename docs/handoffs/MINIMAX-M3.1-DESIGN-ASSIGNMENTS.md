# Asignaciones y gates de MiniMax M3.1

El alcance vigente son nueve odiseas y273episodios. Cada episodio tiene un slice mecánico explícito en su propuesta oficial. Las propuestas permanecen bloqueadas: el arquitecto debe cerrar todos los dossiers, capacidades, geografía y nivelación antes de entregar autoría. Las veinticinco fichas ampliadas de faith-origins son borradores en revisión, no escenarios nativos.

Lee [plan](../design/odyssey-production-plan.md), [selecciones](../design/odyssey-selections.md), [asignaciones estructuradas](../design/assignments.json), [arquitectura](../architecture/overview.md) y el traspaso. Recupera estados vivos de DelendAI antes de elegir cualquier slice.

| Campaña / título inglés | Propuesta oficial | Episodios | Slices |
|---|---|---:|---|
| faith-origins / Embers of the Covenant | [f00004](../delendai/proposals/blocked/f00004-autoria-designada-embers-of-the-covenant.md) | 30 | S1 conformidad; S2 metadatos; 30 slices individuales; S7 promoción |
| imperial-church / The Eagle and the Cross | [f00003](../delendai/proposals/blocked/f00003-campana-futura-iglesia-imperial-312-337.md) | 29 | S1 conformidad; S2 metadatos; 29 slices individuales; S6 promoción |
| jewish-tradition / Keepers of the Unbroken Word | [f00005](../delendai/proposals/blocked/f00005-autoria-designada-keepers-of-the-unbroken-word.md) | 30 | S1 conformidad; S2 metadatos; 30 slices individuales; S7 promoción |
| church-of-rome / The Keys of the Eternal City | [f00006](../delendai/proposals/blocked/f00006-autoria-designada-the-keys-of-the-eternal-city.md) | 32 | S1 conformidad; S2 metadatos; 32 slices individuales; S7 promoción |
| new-rome / Beyond the Golden Gate | [f00007](../delendai/proposals/blocked/f00007-autoria-designada-beyond-the-golden-gate.md) | 32 | S1 conformidad; S2 metadatos; 32 slices individuales; S8 promoción |
| first-caliphs / Beneath the Desert Stars | [f00008](../delendai/proposals/blocked/f00008-autoria-designada-beneath-the-desert-stars.md) | 30 | S1 conformidad; S2 metadatos; 30 slices individuales; S8 promoción |
| first-fitna / The Shattered Oath | [f00009](../delendai/proposals/blocked/f00009-autoria-designada-the-shattered-oath.md) | 28 | S1 conformidad; S2 metadatos; 28 slices individuales; S8 promoción |
| umayyads / From Damascus to the Far Horizon | [f00010](../delendai/proposals/blocked/f00010-autoria-designada-from-damascus-to-the-far-horizon.md) | 32 | S1 conformidad; S2 metadatos; 32 slices individuales; S8 promoción |
| house-of-ali / The River Remembers | [f00011](../delendai/proposals/blocked/f00011-autoria-designada-the-river-remembers.md) | 30 | S1 conformidad; S2 metadatos; 30 slices individuales; S7 promoción |

Los IDs de los39escenarios y sus slices anteriores permanecen reservados. Por eso un número S mayor puede preceder a S3: se ejecuta `DependsOn` y `order`, nunca el orden numérico del nombre. Cada propuesta enumera cinco actos, fecha, lugar, operación e identidad de cada episodio. La promoción espera al final ampliado efectivo, no al antiguo final de la base.

Pilotos: f00001 laboratorio T01/T02; f00002 Milvio. i00003 pertenece al arquitecto: fases/transacciones, geografía/transporte, reserva nativa y voz/progreso. s00001 corresponde al arquitecto/tester con motor. d00002/S2–S10 cierran los dossiers de cada odisea y S11 consolida el traspaso. Estas tareas no se transfieren a MiniMax.

## Matriz de actos y trabajos

### Embers of the Covenant

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6, 7, 8 | S8, S9, S10, S11, S12, S3, S13, S14 |
| act-2 | 9, 10, 11, 12, 13, 14, 15 | S15, S16, S17, S18, S19, S20, S21 |
| act-3 | 16, 17, 18, 19, 20, 21 | S22, S4, S23, S24, S25, S5 |
| act-4 | 22, 23, 24, 25, 26, 27 | S26, S27, S28, S29, S30, S31 |
| act-5 | 28, 29, 30 | S32, S33, S6 |

### The Eagle and the Cross

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6 | S3, S7, S8, S9, S10, S11 |
| act-2 | 7, 8, 9, 10, 11, 12 | S12, S13, S14, S15, S16, S4 |
| act-3 | 13, 14, 15, 16, 17, 18, 19 | S17, S5, S18, S19, S20, S21, S22 |
| act-4 | 20, 21, 22, 23, 24, 25 | S23, S24, S25, S26, S27, S28 |
| act-5 | 26, 27, 28, 29 | S29, S30, S31, S32 |

### Keepers of the Unbroken Word

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5 | S3, S8, S9, S10, S11 |
| act-2 | 6, 7, 8, 9, 10, 11, 12 | S12, S13, S14, S15, S16, S17, S18 |
| act-3 | 13, 14, 15, 16, 17 | S4, S19, S20, S5, S21 |
| act-4 | 18, 19, 20, 21, 22, 23, 24 | S22, S23, S24, S25, S26, S27, S28 |
| act-5 | 25, 26, 27, 28, 29, 30 | S29, S30, S31, S32, S33, S6 |

### The Keys of the Eternal City

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6 | S8, S9, S10, S11, S12, S13 |
| act-2 | 7, 8, 9, 10, 11, 12 | S3, S14, S15, S16, S17, S18 |
| act-3 | 13, 14, 15, 16, 17, 18 | S19, S20, S21, S22, S4, S23 |
| act-4 | 19, 20, 21, 22, 23, 24, 25 | S24, S25, S26, S27, S28, S29, S30 |
| act-5 | 26, 27, 28, 29, 30, 31, 32 | S31, S5, S32, S33, S34, S35, S6 |

### Beyond the Golden Gate

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6, 7, 8 | S9, S10, S11, S12, S13, S14, S15, S16 |
| act-2 | 9, 10, 11, 12, 13, 14, 15, 16, 17 | S3, S17, S18, S19, S4, S20, S21, S5, S22 |
| act-3 | 18, 19, 20, 21, 22 | S23, S24, S25, S26, S6 |
| act-4 | 23, 24, 25 | S27, S28, S7 |
| act-5 | 26, 27, 28, 29, 30, 31, 32 | S29, S30, S31, S32, S33, S34, S35 |

### Beneath the Desert Stars

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5, 6, 7 | S9, S10, S11, S12, S13, S14, S3 |
| act-2 | 8, 9, 10, 11, 12, 13, 14 | S15, S16, S17, S18, S19, S20, S21 |
| act-3 | 15, 16, 17, 18, 19, 20, 21 | S22, S4, S23, S24, S5, S6, S25 |
| act-4 | 22, 23, 24, 25, 26 | S26, S27, S7, S28, S29 |
| act-5 | 27, 28, 29, 30 | S30, S31, S32, S33 |

### The Shattered Oath

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5 | S3, S9, S10, S11, S12 |
| act-2 | 6, 7, 8, 9, 10, 11 | S13, S14, S4, S15, S16, S17 |
| act-3 | 12, 13, 14, 15, 16 | S18, S5, S19, S20, S21 |
| act-4 | 17, 18, 19, 20, 21, 22, 23 | S22, S23, S24, S6, S25, S26, S27 |
| act-5 | 24, 25, 26, 27, 28 | S28, S29, S30, S31, S7 |

### From Damascus to the Far Horizon

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3 | S3, S9, S10 |
| act-2 | 4, 5, 6, 7, 8, 9, 10, 11, 12 | S11, S12, S13, S14, S4, S15, S16, S17, S5 |
| act-3 | 13, 14, 15, 16, 17, 18, 19 | S18, S19, S20, S21, S22, S23, S24 |
| act-4 | 20, 21, 22, 23, 24, 25, 26, 27 | S6, S25, S26, S27, S28, S29, S30, S31 |
| act-5 | 28, 29, 30, 31, 32 | S32, S33, S34, S7, S35 |

### The River Remembers

| Acto | Episodios | Slices cronológicos |
|---|---|---|
| act-1 | 1, 2, 3, 4, 5 | S8, S9, S10, S3, S11 |
| act-2 | 6, 7, 8, 9, 10 | S4, S12, S13, S14, S15 |
| act-3 | 11, 12, 13, 14, 15, 16 | S16, S17, S5, S18, S19, S20 |
| act-4 | 17, 18, 19, 20, 21, 22, 23 | S21, S22, S23, S24, S25, S26, S27 |
| act-5 | 24, 25, 26, 27, 28, 29, 30 | S28, S29, S30, S31, S32, S33, S6 |

## Prompt de ejecución por slice

```text
Trabaja solo en <proposalId>/<sliceId> designado por DelendAI, bajo tu identidad real MiniMax M3.1. Base develop y unidad aislada oficial; confirma ancestro, reclama exclusivamente Files. Lee AGENTS.md y recupera gate/review policy del servidor.

Tu fuente editorial aprobada es docs/design/odysseys/<campaignId>.json y el expediente docs/wiki/<campaignId>/episodes/<scenarioId>/15-odyssey-dossier.md, junto a la geografía y biblia del narrador consolidadas por d00002. El catálogo base de39misiones conserva evidencia, no sustituye el dossier ampliado. No cambies la trama, el narrador, los resultados históricos, los mapas regionales, las rutas, los umbrales o los presupuestos por tu cuenta. No conviertas estimaciones en mediciones. Si una instrucción resulta incompatible con el motor, registra reproducción y devuelve la decisión al arquitecto; conserva trabajo independiente autorizado.

Materializa en staging con sourceLocale=en, todas las claves EN/es-ES, general factual antes de persona subjetiva, eventos ficticios declarados, mapas300–400 orientados geográficamente, roster finito y recuperación. IDs de unidades/terrenos/tecnologías vienen del catálogo fijado; los números de cadenas se asignan con ids:allocate solo en el slice de promoción que posee el lock/glosario. Cumple literalmente los predicados compuestos y estados; no uses un timer para fingir escolta, entrega, acuerdo o batalla.

Usa las capacidades reutilizables acreditadas; no toques packages/tools fuera de propuesta explícita. Si i00003/s00001 o los pilotos siguen pendientes, no desbloquees autoría nativa por suposición. Los17idiomas y medios mantienen estados reales; referencias descargadas no son arte de release aprobado. Sin generación pagada masiva ni publicación del mod.

Ejecuta staging:check --partial cuando la propuesta lo permita; completo sin --partial antes de promoción. Materializa campaña+IDs/glosario conjuntamente, bun run validate verde, export/candidate cuando aplique; adjunta hash, build y QA real en los slices que lo requieren. Solicita revisor distinto, corrige hallazgos, integra exclusivamente por work publish, aprobación formal según el runtime y nunca autoapruebes. Continúa únicamente con el siguiente slice oficialmente implementable.
```

El arquitecto mantiene los generadores/verificador del diseño. MiniMax no edita los dossiers generados; los cambios aprobados se realizan en catálogo/perfiles y se regeneran. Cada misión enlaza todos sus objetivos, pantallas, fuentes y coordenadas, evitando que el agente invente trabajo para rellenar una carpeta.

## Ampliación en curso y naming obligatorio

`d00002` prepara odiseas extensas: esta matriz asigna273slices de episodio, pero no cierra sus decisiones ni autoriza ejecución. Recupera sus estados reales antes de empezar. Ninguna capacidad faltante pasa a MiniMax por omisión. La base dispone de seis objetivos secundarios por misión, con predicados/financiación/estado/QA y tres estrategias en el catálogo y [plan](../design/odyssey-production-plan.md). Materializa todos esos contratos sin sustituirlos por timers, suministros infinitos ni eliminación de tareas difíciles. Respeta el naming i00004: responsabilidad.tipo.ts, importaciones directas, sin index/barrels y carpetas por dominio.

La [selección de las nueve odiseas](../design/odyssey-selections.md) contiene los273episodios y enlaza los nuevos documentos `14-odyssey-arc.md`. Cada entrada fija identidad, orden, acto, título EN/es, fecha, localización y operación principal. Es una selección editorial con auditorías de fuentes todavía en curso: no son273expedientes completos. No la uses para rellenar pantallas, nivelación o coordenadas con decisiones tuyas. Los episodios adicionales solo se asignarán tras los expedientes completos de d00002 y las capacidades acreditadas de i00003.

## Expedientes ampliados en revisión

Veinticinco episodios de faith-origins (órdenes 1–25) tienen expediente legible en `docs/wiki/faith-origins/episodes/<id>/15-odyssey-dossier.md` y fuente editable en `docs/design/odysseys/faith-origins.json`. Los generadores comparten identidad, transacciones, financiación, subtítulos y QA; los hechos, voz personal y decisiones de cada misión son autoría explícita del arquitecto. Hay 987 pantallas y 150 secundarios en los borradores ampliados. Los expedientes no están aprobados y sus planos SVG muestran controles geográficos, no terreno navegable. No produzcas binarios a partir de estos borradores.


## Voces de las odiseas ampliadas

La autoridad de diseño de voz ampliada es [odyssey-narrators.json](../design/voices/odyssey-narrators.json), con nueve fichas legibles en ese directorio y un plan de acceso al conocimiento para cada uno de los 273 episodios. La voz objetiva resume hechos y límites documentales antes de dar paso a la persona ficticia de campaña. No conviertas biografías inventadas en fuentes antiguas ni atribuyas acceso a concilios, revelaciones o motivos privados. Cada dossier debe precisar la colocación local; una edad compatible no demuestra presencia.

Marcus mantiene `imperial-clerk`, pero en la odisea ampliada su vida es c.334–403, frente al arco legado c.290–350. No copies recuerdos de 312 a los nuevos textos. La migración debe aprobarse antes de promoción nativa. Las biblias ampliadas siguen pendientes de revisión editorial y no autorizan nuevas campañas ni generación pagada de audio.
