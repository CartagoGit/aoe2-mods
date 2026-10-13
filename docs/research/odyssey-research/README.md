# Investigación delegada para odiseas

Estos JSON son recopilaciones de Luna solicitadas por el arquitecto y verificadas sintácticamente. No son el registro final de hechos aprobados. Cada fila conserva fecha, evento, lugar, URL, localizador y cautela; sources declara el alcance consultado. Abstract, vista previa, traducción antigua y texto completo no son equivalentes.

- [Tradiciones cristianas y judías](christian-jewish.json).
- [Primer islam, fitna y dinastía](islamic.json).
- [Plan editorial que decide el alcance](../../design/odyssey-production-plan.md).

Durante la auditoría se corrigieron el traslado de los restos de Crisóstomo a438, la carta de Gelasio494, el nombramiento de al-Hajjaj694 y la muerte de al-Walid715; se retiraron hechos fuera del arco asignado y se incluyó Hasan661 en la continuidad. Siguen pendientes la comprobación de cada candidato, el complemento de los periodos ampliados y su selección jugable. Las fechas lunares, la localización exacta de campos de batalla y los relatos polémicos mantienen sus cautelas.

El contenido publicado por una comunidad de fe describe también su propia memoria. No se transforma una tradición atribuida en una afirmación neutral, ni un relato de persecución provincial en una política uniforme. Las decisiones del arquitecto deben citar el pasaje que respalda el hecho y distinguirlo del contexto de una página general.

## Selección y auditorías posteriores

El arquitecto ha seleccionado [273 episodios](../../design/odyssey-selections.md), con identidades estables, títulos EN/es, cinco actos por campaña y operaciones principales diferentes. La selección no acredita expedientes completos ni mapas jugables. Los candidatos originales se conservan para trazabilidad; una corrección en `historicalSelection.selectedClaim`, `auditedSourcePassages` o `researchAudit` prevalece sobre la fila original.

- [Auditoría occidental y oriental](western-source-audit.json): cada registro distingue pasaje comprobado de `pending_source_check`, incluye URL corregida, afirmación respaldada y alcance leído.
- [Auditoría independiente de la fitna](fitna-editorial-audit.md): geografía imprecisa, cronología, consolidaciones y ficciones civiles permitidas.
- [Geografía candidata](geography-candidates.json): los enlaces que son búsquedas OSM todavía requieren comprobación; no son pruebas de coordenadas antiguas.
- [Referencias descargadas](reference-manifest.json): incluye bytes y SHA-256 del conjunto moderno de lugares poblados Natural Earth, de dominio público. [Datos locales](geography/ne_10m_populated_places.geojson). Un punto urbano moderno no representa el campamento, la muralla o la demografía de la ciudad antigua. Esta descarga es material de investigación y no está aprobada para distribuirse en un mod.

La pérdida de Egipto en 658 se distingue de las incursiones en el Hiyaz de 660. La primera promesa tradicional de Aqaba se fecha en 621 y la segunda en 622. La actividad de Akiva no se traslada a 150–180. La carta de Cipriano a Successus documenta el rescripto de Valeriano; la ejecución de Cipriano exige el testimonio separado de Pontius. Estas correcciones no convierten en certeza las diferencias de calendario o los relatos partidistas.

## Nuevas consultas y expedientes del primer acto

- [Veintinueve fichas de auditoría de imperial-church](imperial-source-audit-v2.json): se distinguen Milán en 355 y Alejandría en 356; el alcance parcial y las consultas pendientes permanecen explícitos.
- [Diez localizaciones orientales adicionales](geography-additional-audit.json): fichas con evidencias de cauces, núcleos antiguos y límites de coordenadas; la aprobación geográfica permanece pendiente.
- [Treinta consultas de fuentes de faith-origins](faith-source-audit-v2.json): URL y pasaje consultado, afirmación EN/es y límites; consulta no equivale a aprobación editorial.
- [Auditoría de localizaciones adicionales](geography-source-audit-v2.json): distingue textos completos, abstracts y comprobaciones pendientes.
- [Geografía de episodios](episode-geography.json): añade Cesarea con punto de gazetteer, bbox regional y cautelas de costa y fases monumentales.
- [Seis referencias visuales](faith-open-images.json), descargadas en `images/`, con [créditos](CREDITS.md), licencias y hashes en el manifiesto. Pilato es un molde moderno en Milán; Sardis incluye reconstrucción y fases posteriores. Ninguna imagen está aprobada como escena antigua o arte de distribución.

Los [ocho primeros expedientes](../../wiki/faith-origins/14-odyssey-arc.md) tienen autoría explícita del arquitecto y una generación compartida de contratos. Conservan la evidencia candidata y la afirmación corregida; las actividades jugables ficticias no se convierten en hechos por tener coordenadas.

## Second-act sources and archaeological controls

[Seven episode/source consultations and three places](faith-act2-source-geography-audit.json) retain partial access and provenance disputes. The authorial claim in1Cor16:8 is checked separately from exact composition date. The seven new dossiers distinguish fictional working notes from canonical originals. [Five downloaded ASCSA datasets](corinth-gis-audit.json) add archaeological and relief research controls with checksums and [credits](CREDITS.md); mixed dates and the contour raster’s undeclared CRS prevent automatic use as first-century footprints.

[Auditoría de los30episodios de first-caliphs](first-caliphs-source-audit-v2.json) conserva las consultas pendientes, relatos tardíos y alternativas de calendario. Sus propuestas de corrección aún necesitan decisión editorial y no modifican automáticamente la cronología seleccionada.


## Consultas del tercer acto y corpus judío

Los [22 dossiers ampliados](../../wiki/faith-origins/14-odyssey-arc.md) son órdenes 1–22; Jerusalén 70 conserva su desenlace histórico fijo y atribuye las fuentes sin fusionarlas. Las fuentes añadidas de Marcos 1, Mateo 1, Lucas 3:23–38 y Didaché 11–13 conservan fecha de consulta y límites en cada selección. No se descargan traducciones modernas para reutilizarlas como guion ni se colocan autógrafos canónicos en las actividades ficticias.

- [Finale de Milán 303–313](faith-finale-source-audit.json): distingue reunión/acuerdo en Milán, publicación del rescripto en Nicomedia y una orden genérica de restitución; no prueba una restitución local concreta.
- [Auditoría judía inicial, episodios 1–6](jewish-first-act-source-audit.json): tradiciones sobre Yavneh, Akiva y reforma fiscal; no un concilio único ni abolición acreditada del fiscus.
- [Auditoría judía intermedia, episodios 7–17](jewish-middle-source-audit.json): rebeliones, archivos de cuevas, ciudadanía, Dura y círculos amoraicos, con accesos parciales explícitos.
- [Auditoría judía tardía, episodios 18–30](jewish-late-source-audit.json): arqueología, compilaciones y disposiciones legales; promulgación no implica cumplimiento y c.425 sigue siendo un límite editorial.

Estas recopilaciones son investigación delegada, pendiente de interpretación del arquitecto y revisión independiente. No fijan objetivos, poblaciones, mapas o mecánicas ni aprueban una campaña.

- [Primer acto de Roma, seis consultas](rome-first-act-source-audit.json): distingue viaje de Atanasio, cronología disputada de Sardica, exilio de Liberio, fuente candidata incorrecta de Rimini, relato de violencia de Amiano y penitencia en Ambrosio. La corrección de selecciones y aprobación siguen pendientes de interpretación del arquitecto.

- [Fuentes romanas intermedias, episodios7–18](rome-middle-source-audit.json): cronologías de asedios y reinos, negociación frente a paz consumada, viajes y fuentes parciales.
- [Fuentes romanas tardías, episodios19–32](rome-late-source-audit.json): iconos, alianzas, llaves, coronación y diferencias entre testimonio y reconstrucción.
- [Geografía romana aún sin perfil](rome-missing-geography-audit.json): Chersonesos táurico, Saint-Denis y Paderborn, con controles institucionales y sin equivaler direcciones actuales a huellas antiguas.

Las consultas añadidas por el arquitecto para los episodios20–22 distinguen Primera de Clemente1/44–48, las dos cartas completas de Plinio10.96–97 y Justino65–67. La preparación de un envío no acredita recepción ni reconciliación; el recibo local de Bitinia no es respuesta imperial; las prácticas descritas por Justino no acreditan todas las comunidades.
