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

El corte histórico de Adrianópolis del17deoctubre pasó a62dossiers,2.553pantallas y384secundarios;216selecciones siguen sin dossier. Hay36recursos adicionales locales, sin nuevos binarios en esta ampliación. [Fuente histórica](imperial32-source-audit.json), [relieve y decisiones](adrianople378-relief-design.md), [muestras completas](adrianople378-relief-sampling.json) y [marco de control](imperial32-map-control-audit.json) corresponden al ID32/orden30. Se verificaron1414valores del DSM y sus índices contra el TIFF integrado, con4335aserciones de comprobación de datos; no son pruebas de motor. La etiqueta equivocada de identidad/puntos del informe preliminar deLuna se conserva como corrección de procedencia, no como autoría del usuario.

La [auditoría cívica actual](civic-difficulty-mechanical-audit.json) mantiene54candidatos estáticos y pasa a ocho con hostiles. El [corte previo de61](civic-difficulty-mechanical-audit-61-2026-10-17.json) conserva sus hashes y métricas reales. Todas las aprobaciones históricas/nativas/jugadas siguen pendientes.


### Controles de fuentes para los dos dossiers imperiales restantes

[Marco de Sirmio379](imperial33-source-audit.json): lectura directa seleccionada deSócrates,Sozomeno,Marcelino y síntesis deDavidWoods;16de enero en la traducción deSócrates frente aXIIIIkalendasFebruarias/19de enero enMarcelino. El comentario críticoKFHist no pudo recuperarse (418/403), por lo que sus fragmentos de búsqueda no se presentan como lectura completa. [Transferencias deConstantinopla380](imperial34-source-audit.json): llegada24/transferencia26de noviembre enSócrates, frente al mes de diciembre enMarcelino. Estos registros de fuentes no son por sí solos una reconstrucción urbana aprobada ni permiso de materialización. Sirmio tiene ahora dossier de diseño; Constantinopla380 todavía no. El recuento actual es63borradores.

### Reproducción de la auditoría mecánica

La auditoría actual se genera con `python3 tools/design/civic_difficulty_audit.script.py --write --author REAL_ID --date YYYY-MM-DD` y se comprueba ejecutando el mismo script sin argumentos. Lee las nueve campañas de la política y solamente sus dossiers `episodes[]`; conserva hashes y declara cobertura cero donde todavía no hay dossier. El [corte de62del17deoctubre](civic-difficulty-mechanical-audit-62-2026-10-17.json) conserva la recopilación de Luna y su seguimiento original. La nueva ejecución se atribuye al agente que realmente la ejecuta. La [aceptación de jugabilidad](../../design/civic-playability-acceptance.md) sigue pendiente; este informe no mide diversión ni acredita dificultad.

El gate de diseño rechaza hashes o métricas obsoletos de esta auditoría. Las cinco regresiones específicas forman parte de `tools/design/test_design.py`; notas narrativas, modo del reloj y objetos de límites nulos no cuentan como presión temporal.

Las recopilaciones de lectura de Luna del18deoctubre quedan en [Sirmium379](sirmium379-geography-collection.md) y [Gregorio/Constantinopla380–381](constantinople380-gregory-collection.md). La primera no sitúa una sala de accesión ni un muelle antiguo. La segunda distingue el discurso de despedida de381 de los relatos posteriores sobre380 y no autentica un diálogo imperial ni una parcela de iglesia. Son investigación atribuida y acotada para los dos dossiers todavía pendientes, sin aprobación histórica independiente.


### Sirmio379: The Burden of the Purple

El borrador del ID33, orden31/S36, añade41pantallas bilingües y siete secundarios. Hay63dossiers/278selecciones,2.594pantallas y391secundarios;215selecciones siguen sin dossier y todas las aprobaciones históricas/nativas/jugadas siguen pendientes. La [recopilación geométrica de Luna](sirmium33-frame-collection.json) acota el frame regional, el punto DARE y los recursos visuales ya existentes. No se añade un nuevo binario ni cambia el total de36referencias. La fuente cronológica conserva16de enero enSócrates frente a19en la lectura inclusiva deMarcelino; el juego usa379sin fijar día.

La preparación local es ficción explícita: tres remesas con destinos distintos, tres parejas simultáneas elegidas de ocho originales y un plazo visible de20/16/12minutos de juego. Después se libera la reunión y la salida causal es una fase sin plazo. Total principal360de alimento260de madera. El filtro mecánico registra ahora un deadline estructurado y ocho dossiers con hostiles; mantiene54candidatos estáticos, sin que ninguno de esos conteos pruebe dificultad real. Controles nativos del inicio, recursos, footprints y calibración quedan en sus gates de infraestructura.


### Corte actual del 18 de octubre: 63 dossiers y 37 referencias

Se mantienen 278 selecciones, 63 dossiers, 2.594 pantallas y 391 secundarios; 215 episodios siguen sin dossier completo. El [estudio de asignación de Constantinopla](../../design/episode-plans/imperial-church/34-care-allocation.study.md) añade un prototipo contable, no el dossier 64: nueve combinaciones, asequibilidad sin secundarios 9/7/3, siete slots opcionales y prefijos de pago/recompensa comprobados. La nueva propuesta i00007 registra la capacidad faltante; ni elección/reserva, terreno ni reto jugado están implementados.

La [referencia DSM moderna de Constantinopla](constantinople-modern-dsm-processing.json) y sus [avisos](geography/constantinople-modern-dsm-license.md) añaden el recurso local número 37 del manifiesto. Luna recopiló un único tile; el arquitecto extendió el recorte una fila y una columna con muestras originales para cubrir el bbox solicitado. Son 60.060 muestras float32 (286×210), comprobadas exactamente contra el original con Rasterio y otra lectura Pillow/numpy. Las GeoKeys decodificadas, escala y tiepoint Point coinciden; los offsets internos de las GeoKeys pueden cambiar al recodificar. Los límites de centros y de celdas quedan separados. No hay nueva dependencia del proyecto, costa antigua, edificio/iglesia380 ni terreno jugable acreditado.

Este corte del 18 de octubre registraba 37 recursos en el manifiesto. El primer corte del 24 de octubre, tras incorporar dos registros de la costa OSM moderna, registró 39 recursos; la ampliación posterior del Hiyaz se recoge al final. Ninguno tiene aprobación de producción.

La [recopilación de apertura judía](jewish-opening-primary-collection.json), atribuida a gpt-6-luna, reúne consultas acotadas para los episodios 1–4. Separa Josefo, tradiciones rabínicas redactadas después, comentarios modernos y datos arqueológicos; registra accesos parciales, edición no identificada y la ausencia de una parcela/fecha segura para una escuela o debate. El arquitecto recibió la colección sin adoptar automáticamente sus conclusiones como aprobación histórica: cada afirmación deberá contrastarse al escribir el dossier. No cambia las selecciones ni crea una academia excavada, ruta de huida o «concilio de Jamnia».


## Consulta acotada de episodios judíos 5–8

La [colección contrastada del 23 de octubre](jewish-episodes-05-08-primary-collection.md), con [matriz de fuentes](jewish-episodes-05-08-primary-collection.json), conserva las selecciones de Roma–Ostia96, Lodc.100–135, Cirene115–117 y Alejandría115–117. Separa reforma fiscal de abolición, registra atribuciones rabínicas alternativas y distingue los relatos retrospectivos de Dión/Eusebio de la geografía todavía pendiente. No añade dossiers, imágenes, hechos aprobados ni evidencia de juego.


## Trazabilidad por identidad de episodio

El [cruce de consultas](source-consultation-crosswalk.md) se genera desde un [registro interno](source-consultation-crosswalk.json) y complementa las anotaciones dentro de las selecciones. El primer lote enlaza los 30 registros de `first-caliphs-source-audit-v2.json` por campaña declarada, ID semántico y puntero JSON exactos. No se enlazan por el número de presentación, coincidencias vagas de título o una URL general. Sus bytes y la selección significativa llevan hashes: si cambian, hay que revisar el vínculo antes de regenerar el informe.

Se conservan las declaraciones originales de acceso sin atribuirlas al arquitecto. Tras el segundo lote, el registro identifica 18 consultas acotadas propias de GPT-6 reutilizadas entre los 30 episodios: 28 con algún pasaje accesible y dos con acceso fallido. Un pasaje accesible puede no respaldar la afirmación buscada; no es una puntuación de aceptación. Todos los vínculos de esta campaña tienen una comprobación de acceso y alcance; esto no resuelve sus afirmaciones históricas. La lectura parcial no equivale a leer el libro o artículo completo; no se aprueban hechos, dossiers, mapas ni juego. Las fuentes ausentes de este registro pueden tener investigación anterior en otros archivos.

La consulta del editor corrige la atribución a Hawting de *The Formation of Islam*: la ficha nombra a Jonathan P. Berkey. Las diferencias de URL, localizador y fecha entre auditoría y selección se muestran; no se copia automáticamente una versión sobre otra. La fecha de Yamama diverge entre el registro archivado y la selección, por lo que conserva su revisión específica pendiente. El antiguo campo `sourceFile` de la auditoría contiene una ruta de trabajo obsoleta; el cruce no la usa ni la presenta como procedencia actual.

El registro es una fuente de investigación interna; no cambia el esquema de campañas, el perfil del motor ni los IDs. Su validador comprueba identidad, punteros, alcance declarado y conservación de procedencia; no puede demostrar que una persona leyó un texto ni medir su veracidad. `verify.py` lo ejecuta siempre y rechaza informes desactualizados. No sustituye las propuestas, revisiones o decisiones del servidor DelendAI.

```sh
python3 tools/design/research_crosswalk.script.py --write
python3 tools/design/research_crosswalk.script.py
python3 tools/design/test_research_crosswalk.py
```

El primer comando regenera únicamente el informe de investigación; los otros comprueban sin escribir campañas. El gate documental ejecuta también las regresiones mediante `test_design.py`. S1 mantiene pendientes el resto del cruce y la revisión editorial de hitos/curvas; MiniMax sigue las asignaciones y bloqueos vigentes.

El [contraste del segundo lote](first-caliphs-source-contrast-checkpoint.md) documenta contradicciones de la cronología, atribuciones y paginación, distingue fases de Alejandría y conserva pendientes las dos consultas de Aqaba. Las fuentes se leen con crítica incluso cuando son enciclopedias académicas; ni las generalizaciones confesionales ni las cifras transmitidas se convierten automáticamente en narrativa objetiva o mecánicas.


## Dirección de los 45 actos y consultas de la familia de Ali — 24 de octubre

Las [fichas editoriales de los 45 actos](act-editorial-review.md), con [registro de decisiones](act-editorial-review.json), fijan entrada, inflexión, salida, presión/recuperación y una exigencia de diferenciación para cada acto de las nueve campañas. Son dirección del arquitecto fechada, pendiente de revisión independiente; no dossiers completos ni curvas medidas. Ocho bandas anuales de acto se ajustan al marco de sus episodios ya seleccionados, incluidas alternativas inciertas. Se conservan fechas de episodio, IDs, orden, contratos, voces y continuidad.

- [First Fitna: 28 selecciones](first-fitna-source-collection.md), recopilación de Luna con pasajes y alcance de lectura por ID canónico.
- [House of Ali: 30 selecciones](house-of-ali-source-collection.md), recopilación de Luna; el intento inaccesible del volumen XVII permanece sin lectura.
- [Siete contrastes acotados del arquitecto](ali-family-architect-source-contrast.md), separados de la declaración del recopilador: cronologías, arbitrajes, retirada, cautivos, memoria religiosa y límites de diálogo. Conservan hashes de ambas recopilaciones.

En la entrega editorial integrada en `e70ace6d`, estos archivos todavía no ampliaban el cruce normalizado, que enlazaba 30 selecciones de first-caliphs. La continuación de vínculo completo se documenta abajo. Las 58 selecciones de esas recopilaciones no son 58 hechos aprobados. Los 63 borradores, 215 selecciones sin dossier y 54 candidatos estáticos a riesgo cívico no cambian.

La revisión independiente de este componente detectó 21 localizadores de First Fitna con páginas inconsistentes. El arquitecto comprobó las transiciones del PDF oficial y conserva [la corrección explícita](ali-family-architect-source-contrast.md#pagination-correction-after-independent-review), junto al localizador archivado: no se reescriben los bytes ni la declaración original de Luna.


## Vínculo completo de investigación — continuación del 24 de octubre

El [cruce reproducible](source-consultation-crosswalk.md) enlaza ahora las **278 selecciones**, conservando el validador y las identidades canónicas. Las proyecciones fechadas de [First Fitna y House of Ali](ali-family-source-records.json), [Umayyads](umayyad-source-records.json) y [las cinco campañas cristianas/judía](non-islamic-source-records.json) conservan declaraciones, punteros y hashes de origen; no son consultas nuevas. Las 118 referencias alternativas de la última permanecen accesibles. El validador comprueba también los bytes de los `upstreamSnapshots` declarados, con las mismas restricciones de ruta de las fuentes principales.

La nueva [recopilación omeya de Luna](umayyad-source-collection.md) cubre 32 IDs exactos. Sus [20 contrastes acotados del arquitecto](umayyad-architect-source-contrast.md) distinguen pasajes, metadatos y dos intentos sin texto. El [final judío](jewish-finale-source-check.md), ausente del inventario anterior, obtiene un vínculo nuevo con una cautela explícita: UNESCO no acredita un final exacto en 425 y la norma fiscal de 429 es contexto retrospectivo. No se altera el canon para resolver una insuficiencia de las fuentes.

El cruce registra **121 comprobaciones de alcance/acceso**, de las que 117 incluyen algún pasaje y cuatro sólo acceso fallido; **157 declaraciones archivadas siguen sin comprobación nueva** en ese registro. Estos contadores no miden respaldo, aceptación histórica o lectura completa. Las consultas reutilizadas pueden ser parciales, contradecir un detalle o no exponer el pasaje seleccionado. El [checkpoint](research-linkage-checkpoint.md) conserva el alcance, los problemas encontrados y las pruebas. S1 y los dossiers conservan sus revisiones pendientes; no hay nuevo permiso para autoría histórica de MiniMax.


## Consolidación de la arquitectura común — 24 de octubre

Los componentes editoriales y de vínculo se integraron con gate oficial en `e70ace6d` y `990cfe13`, con revisiones independientes acotadas sin hallazgos P1/P2 abiertos. El [expediente de aceptación común](common-architecture-acceptance.md) reúne evidencia para evaluar los dos criterios completos de S1. No es un veredicto: DelendAI conserva S1 pendiente a la fecha de redacción. Las cifras actuales del cruce son 278 vínculos, 121 comprobaciones de acceso/alcance, 117 con algún pasaje, cuatro sólo fallidas y 157 declaraciones archivadas sin comprobación nueva; no son aceptaciones históricas. Las secciones anteriores son cortes fechados y mantienen su alcance original.

## Estado formal actual de S1 — 24 de octubre de 2026

DelendAI registra d00002/S1 `done` y aprobación formal de GPT-6.1, integrada en `b9cff83e76b3eaee75cef789b5ace09a1c6b417b` (producto `924ebde2`). Los dos criterios comunes se cumplieron; las dos familias P2 numéricas corregidas y la evidencia de 142 pruebas Bun, 2.069 aserciones y 90 pruebas de diseño están descritas en [aceptación](common-architecture-acceptance.md) y [revisión independiente](common-architecture-independent-review.md). Esto no aprueba contenido ampliado ni juego. S2–S11 siguen `pending`; se mantienen 63 dossiers, 215 selecciones sin dossier, 2.594 pantallas, 391 objetivos secundarios y cero aprobaciones ampliadas. MiniMax continúa bloqueado para autoría histórica; la especificación f00001/S1, aprobada por `gpt-6-luna` e integrada (`06e688e`, metadatos `3c41b4f5`), precede al primer slice mecánico f00001/S2, pendiente por cuota, sujeto al estado vivo de DelendAI. Los informes fechados anteriores conservan lo que constaba al redactarse.

## Plan parcial de Constantinopla — 24 de octubre de 2026

El [plan auxiliar de mundo](../../design/episode-plans/imperial-church/34-constantinople-world-plan.md) describe 45 pantallas EN/es-ES y siete secundarios; la [revisión independiente](constantinople380-world-plan-luna-review.md) limita el resultado a comprobaciones estáticas. No forma el dossier 64 y queda fuera de los totales de 63 dossiers, 2.594 pantallas y 391 secundarios. El [manifiesto actual](reference-manifest.json) contiene 47 recursos: los 37 del corte fechado del 18 de octubre preceden a los dos registros OSM y a los ocho derivados de relieve del Hiyaz añadidos después. Ninguna referencia adquiere aprobación de producción por estar listada.

## Cola mecánica del piloto de rutas — 24 de octubre de 2026

La [especificación f00001/S1](../../wiki/route-pilot/02-implementation-specification.md) y la [matriz de aceptación](../../wiki/route-pilot/03-acceptance-matrix.md), preparadas por el arquitecto, están formalmente aprobadas e integradas (`06e688e`, metadatos `3c41b4f5`). f00001/S2 es el siguiente trabajo mecánico y sigue pendiente por cuota. El lanzamiento OpenCode MiniMax M3.1 Flash fue rechazado antes de ejecutar herramientas (HTTP429/2056, Token Plan); la consulta OAuth MMX registró 0 % de cuota semanal general y no hubo ediciones. La cola se gestiona por slice aceptado y no requiere esperar a terminar las nueve campañas; los bloqueos oficiales de cada propuesta continúan vigentes hasta su cambio formal.


### Hiyaz: cuatro marcos de investigación, sin promoción de perfiles

El [contraste del arquitecto](desert-sites-architect-geography-contrast.md) distingue Badr, Uhud, Hudaybiyya y Mina-Aqaba mediante cinco marcadores institucionales modernos, conservando sus límites y las discrepancias cronológicas de las fichas divulgativas. No confunde Mina con Aqaba en Jordania ni adopta el centro de Medina/La Meca como coordenada de cada acontecimiento.

Los [recortes DSM y su trazabilidad](hijaz-modern-dsm-processing.json) añaden cuatro TIFF y cuatro vistas científicas con [licencia y avisos](geography/hijaz-modern-dsm-license.md). Son685.830muestras float32 sin interpolación ni modificación de alturas; dos decodificadores contrastaron cada recorte con su ventana original y se verificó la cobertura de todo el marco acolchado, incluidas sus celdas exteriores. Los originales completos de tres tiles quedan como descargas temporales identificadas por URL/bytes/hash; el proyecto conserva los recortes exactos, no una copia supuesta de esos originales.

El total pasa de39a47recursos adicionales, manteniendo intactos los39registros anteriores. Los cuatro marcos siguen fuera del registro geográfico: no reducen todavía las22identidades de selección sin perfil, no completan dossiers y no acreditan caminos, agua histórica, edificios, suelo antiguo, dificultad o juego. Continúan63dossiers,215selecciones sin dossier,2.594pantallas y391secundarios; las vistas nuevas no se cuentan como pantallas de campaña.
