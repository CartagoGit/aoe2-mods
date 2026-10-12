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
