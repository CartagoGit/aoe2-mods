# Investigación delegada para odiseas

Estos JSON son recopilaciones de Luna solicitadas por el arquitecto y verificadas sintácticamente. No son el registro final de hechos aprobados. Cada fila conserva fecha, evento, lugar, URL, localizador y cautela; sources declara el alcance consultado. Abstract, vista previa, traducción antigua y texto completo no son equivalentes.

- [Tradiciones cristianas y judías](christian-jewish.json).
- [Primer islam, fitna y dinastía](islamic.json).
- [Plan editorial que decide el alcance](../../design/odyssey-production-plan.md).

Durante la auditoría se corrigieron el traslado de los restos de Crisóstomo a438, la carta de Gelasio494, el nombramiento de al-Hajjaj694 y la muerte de al-Walid715; se retiraron hechos fuera del arco asignado y se incluyó Hasan661 en la continuidad. Siguen pendientes la comprobación de cada candidato, el complemento de los periodos ampliados y su selección jugable. Las fechas lunares, la localización exacta de campos de batalla y los relatos polémicos mantienen sus cautelas.

El contenido publicado por una comunidad de fe describe también su propia memoria. No se transforma una tradición atribuida en una afirmación neutral, ni un relato de persecución provincial en una política uniforme. Las decisiones del arquitecto deben citar el pasaje que respalda el hecho y distinguirlo del contexto de una página general.

## Selección y auditorías posteriores

El arquitecto ha seleccionado [278 episodios](../../design/odyssey-selections.md), con identidades estables, títulos EN/es, cinco actos por campaña y operaciones principales diferentes. La selección no acredita expedientes completos ni mapas jugables. Los candidatos originales se conservan para trazabilidad; una corrección en `historicalSelection.selectedClaim`, `auditedSourcePassages` o `researchAudit` prevalece sobre la fila original.

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

Los [25 dossiers ampliados](../../wiki/faith-origins/14-odyssey-arc.md) son órdenes 1–25; Jerusalén 70 conserva su desenlace histórico fijo y atribuye las fuentes sin fusionarlas. Las fuentes añadidas de Marcos 1, Mateo 1, Lucas 3:23–38 y Didaché 11–13 conservan fecha de consulta y límites en cada selección. No se descargan traducciones modernas para reutilizarlas como guion ni se colocan autógrafos canónicos en las actividades ficticias.

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

- [Fuentes orientales iniciales1–14](new-rome-first-source-audit.json) y [tardías15–32](new-rome-late-source-audit.json): investigación delegada con polémicas, cronologías disputadas y accesos parciales; no modificaciones automáticas de la selección.
- [Tres nuevas referencias fotográficas](faith-late-images-audit.json): Lyon y Cartago, licencias CC explícitas, hashes comprobados y fotografías conservadas en `images/`. Son estados arqueológicos modernos, con restauraciones y visitantes; no vistas de los siglos II–III ni pruebas de un martirio.

Los órdenes23–25 retienen consultas precisas de EusebioIV26, la carta de Lyon/Vienne enV1 e IreneoIII3. Se preservan la fragmentariedad, la voz de parte y los desenlaces de muerte; los trabajos locales son ficción.

## Recopilación romana y transporte de324

Las auditorías de [Roma1–10](church-of-rome-first-ten-source-audit.json), [11–20](church-of-rome-middle-source-audit.json) y [21–32](church-of-rome-final-source-audit.json), y de [Nueva Roma1–10](new-rome-first-ten-source-audit.json), [11–20](new-rome-middle-source-audit.json) y [21–32](new-rome-final-source-audit.json), conservan candidateUrl/consulta real, fechas discutidas y architectApproval:false. No son instrucciones aprobadas. La [auditoría de Antioquía previa a Nicea](antioch-pre-nicaea-source-audit.json) distingue traducción/retroversión, destinatario discutido, exclusión de comunión y variantes cronológicas; la lectura y decisión del arquitecto siguen pendientes.

Los nuevos controles locales son hidrografía moderna Natural Earth10m y offprint íntegro de Belke2021 con CC BY-SA4.0, créditos y SHA-256. Hay24 recursos adicionales realmente presentes. El [contrato de viajes](manifest-water-journeys.md) describe arquitectura futura; no acredita embarque nativo ni terreno histórico. Los tres candidatos fotográficos de324 que fallaron por HTTP429 siguen fuera del manifiesto de descargas.

Los órdenes15–16 imperiales tienen auditorías precisas separadas. La carta persa no tiene fecha o dirección de despacho Nicomedia acreditadas; se retiene el candidato previo como procedencia. Tiro distingue VC41–42 de Jerusalén43–47, y la carta jerosolimitana en Atanasio84. Marriner2007 esPNAS104(22), noQSR; su figura6 se inspeccionó en una copia temporal y no representa335 ni se redistribuye. La auditoría mecánica de15–16 pertenece al arquitecto, no constituye aprobación independiente.


La auditoría de17–19 corrige tres datos de recopilación: Muehlberger2015 es autora del artículo de Arrio (noBond); JanDrijvers firma la reseña deAmerise (noPohlsander); elEpitome es anónimo, distinto deAurelioVíctor. Para el PDF deBurgess efectivamente descargado, páginas físicas11–12/índices10–11 corresponden a impresas14–15. EusebioIV61–66 no identifica oficiante ni fecha numeral22mayo; Jerónimo posterior identificaEusebioNic. El artículo deBurgess y fuentes tardías exigen no contar relatos dependientes como múltiples testimonios independientes. Mapas17–19 tienen auditoría geométrica del arquitecto; no aprobación independiente, reconstrucción antigua ni QA de motor.


Rímini359: [consulta del arquitecto](imperial25-source-audit.json) distingue los relatos de Sulpicio Severo y Sócrates, el prefecto Taurus, la cronología de Liberio y la separación respecto a Seleucia. El [registro visual](rimini359-visual-reference-candidates.json) y el manifiesto conservan dos fotografías originales modernas de monumentos, con licencia, crédito y hash. Los PDF municipales permanecen como consultas temporales: no se incorporan sus imágenes sin licencia. C1.1.1 muestra cambios de los siglosXIX–XX, no fases romanas. Las imágenes actuales no certifican359, la sede conciliar ni una orilla navegable.


## Estado de investigación al 17 de octubre de 2026

La selección vigente tiene278episodios y61dossiers redactados, con2.511pantallas EN/es-ES y377secundarios;217selecciones no tienen dossier. Las secciones anteriores conservan cortes históricos de recopilación, no recuentos actuales de producción. Hay36recursos adicionales realmente locales, todavía sin aprobación de producción.

- [Alejandría365–366](imperial30-source-audit.json) y [límites geográficos](alexandria365-geography-audit.json): New River/villa sin localizar; la [revisión técnica](../../qa/campaign-design/imperial30-independent-review.md) no equivale a aprobación histórica o nativa.
- [Sucesión alejandrina373](imperial31-source-audit.json): sincronismo deSócrates371distinto del marco convencional373; intervención, prisión, huida y posesión separadas. La escena de hogares y presión local es ficción declarada.
- [Adrianópolis378 y DSM](adrianople378-geography-and-dem-candidates.json): hora octava, no radio de ocho millas; se corrigió también la transcripción latina del recolector a `octava tandem hora`. Posición anterior a quince millas tampoco localiza la batalla.
- [Procesamiento del relieve moderno](edirne-modern-dsm-processing.json), [licencia y avisos](geography/edirne-modern-dsm-license.md) y [vista local](images/edirne-modern-dsm-regional-preview.png): recorte lossless de4.1MB más vista de1.2MB. No es terreno desnudo, hidrología antigua ni mapa de batalla certificado.
- [Auditoría mecánica actual](civic-difficulty-mechanical-audit.json) y [snapshot previo de60](civic-difficulty-mechanical-audit-2026-10-15.json):54candidatos de riesgo y siete con hostiles; no medidas de diversión ni balance.


### Adrianópolis378: ampliación del mismo17de octubre

El corte actual pasa a62dossiers,2.553pantallas y384secundarios;216selecciones siguen sin dossier. Hay36recursos adicionales locales, sin nuevos binarios en esta ampliación. [Fuente histórica](imperial32-source-audit.json), [relieve y decisiones](adrianople378-relief-design.md), [muestras completas](adrianople378-relief-sampling.json) y [marco de control](imperial32-map-control-audit.json) corresponden al ID32/orden30. Se verificaron1414valores del DSM y sus índices contra el TIFF integrado, con4335aserciones de comprobación de datos; no son pruebas de motor. La etiqueta equivocada de identidad/puntos del informe preliminar deLuna se conserva como corrección de procedencia, no como autoría del usuario.

La [auditoría cívica actual](civic-difficulty-mechanical-audit.json) mantiene54candidatos estáticos y pasa a ocho con hostiles. El [corte previo de61](civic-difficulty-mechanical-audit-61-2026-10-17.json) conserva sus hashes y métricas reales. Todas las aprobaciones históricas/nativas/jugadas siguen pendientes.
