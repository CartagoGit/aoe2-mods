# Asignación cerrada del catálogo a MiniMax M3.1

Lee [catálogo](../design/README.md), [contrato de producción](../design/production-contract.md), [assignments.json](../design/assignments.json), [arquitectura](../architecture/overview.md) y los cinco documentos originales de traspaso. Recupera los estados actuales de DelendAI antes de elegir slice. La documentación fija qué crear; no cambia estados oficiales ni demuestra que esté GAME VERIFIED.

| Campaña / título inglés | Propuesta | Escenarios | Secuencia de slices |
|---|---|---:|---|
| faith-origins / Embers of the Covenant | f00004 | 4 | S1 conformidad; S2 metadatos; S3–S6 misiones; S7 promoción/IDs/QA |
| imperial-church / The Eagle and the Cross | f00003 | 3 | S1 conformidad; S2 metadatos; S3–S5 misiones; S6 promoción/IDs/QA |
| jewish-tradition / Keepers of the Unbroken Word | f00005 | 4 | S1 conformidad; S2 metadatos; S3–S6 misiones; S7 promoción/IDs/QA |
| church-of-rome / The Keys of the Eternal City | f00006 | 4 | S1 conformidad; S2 metadatos; S3–S6 misiones; S7 promoción/IDs/QA |
| new-rome / Beyond the Golden Gate | f00007 | 5 | S1 conformidad; S2 metadatos; S3–S7 misiones; S8 promoción/IDs/QA |
| first-caliphs / Beneath the Desert Stars | f00008 | 5 | S1 conformidad; S2 metadatos; S3–S7 misiones; S8 promoción/IDs/QA |
| first-fitna / The Shattered Oath | f00009 | 5 | S1 conformidad; S2 metadatos; S3–S7 misiones; S8 promoción/IDs/QA |
| umayyads / From Damascus to the Far Horizon | f00010 | 5 | S1 conformidad; S2 metadatos; S3–S7 misiones; S8 promoción/IDs/QA |
| house-of-ali / The River Remembers | f00011 | 4 | S1 conformidad; S2 metadatos; S3–S6 misiones; S7 promoción/IDs/QA |

Pilotos: f00001 laboratorio T01/T02 con brief cerrado; f00002 Milvio reutiliza el diseño C01, sin otra arquitectura ni versión histórica. i00003 pertenece al arquitecto: fases/transacciones, geografía/transporte, reserva nativa y layouts/voz/progreso. s00001 pertenece al arquitecto/tester con motor. No asignar estas decisiones a MiniMax ni saltar bloqueos.

## Prompt de ejecución por slice

```text
Trabaja solo en <proposalId>/<sliceId> designado por DelendAI, bajo tu identidad real MiniMax M3.1. Base develop y unidad aislada oficial; confirma ancestro, reclama exclusivamente Files. Lee AGENTS.md y recupera gate/review policy del servidor.

Tu fuente editorial es docs/design/catalog.json + geography.json y docs/wiki/<campaignId>/12-production-blueprint.md, 13-narrator-bible.md, scenarios/<scenarioId>.md. No cambies la trama, el narrador, los resultados históricos, los mapas regionales, las rutas, los umbrales o los presupuestos por tu cuenta. No conviertas estimaciones en mediciones. Si una instrucción resulta incompatible con el motor, registra reproducción y devuelve la decisión al arquitecto; conserva trabajo independiente autorizado.

Materializa en staging con sourceLocale=en, todas las claves EN/es-ES, general factual antes de persona subjetiva, eventos ficticios declarados, mapas300–400 orientados geográficamente, roster finito y recuperación. IDs de unidades/terrenos/tecnologías vienen del catálogo fijado; los números de cadenas se asignan con ids:allocate solo en el slice de promoción que posee el lock/glosario. Cumple literalmente los predicados compuestos y estados; no uses un timer para fingir escolta, entrega, acuerdo o batalla.

Usa las capacidades reutilizables acreditadas; no toques packages/tools fuera de propuesta explícita. Si i00003/s00001 o los pilotos siguen pendientes, no desbloquees autoría nativa por suposición. Los17idiomas y medios mantienen estados reales; referencias descargadas no son arte de release aprobado. Sin generación pagada masiva ni publicación del mod.

Ejecuta staging:check --partial cuando la propuesta lo permita; completo sin --partial antes de promoción. Materializa campaña+IDs/glosario conjuntamente, bun run validate verde, export/candidate cuando aplique; adjunta hash, build y QA real en los slices que lo requieren. Solicita revisor distinto, corrige hallazgos, integra exclusivamente por work publish, aprobación formal según el runtime y nunca autoapruebes. Continúa únicamente con el siguiente slice oficialmente implementable.
```

El arquitecto mantiene los generadores/verificador del diseño. MiniMax no edita los dossiers generados; los cambios aprobados se realizan en catálogo/perfiles y se regeneran. Cada misión enlaza todos sus objetivos, pantallas, fuentes y coordenadas, evitando que el agente invente trabajo para rellenar una carpeta.
