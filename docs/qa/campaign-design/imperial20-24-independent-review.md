# Revisión independiente en solo lectura — imperial20–24

Revisor gpt-6.1-sol. Base de inspección: fuente WIP en unidad gpt-6-new-all;20–22 entregados previamente (coordinador identifica45a86261),23–24 borradores sin integración. No se ejecutó Git, no se abrió veredicto DelendAI ni se editaron fuentes/políticas. Extracción previa a correcciones del autor: /tmp/gpt61-imperial20-24-contract-extract.json.

## P1 — permanencia actual no se deduce del historial de llegada

21,o4 req4–6: las tres parejas de hogares tienen únicamente entity-state/state=arrived hacia sus hosts4/5/6. Texto dice que cada pareja mantiene su host.22,o3 req3–5: los legajos hacia stores2/3/4;req6: tres custodios hacia esos stores; todos state=arrived. Texto y checkpoint requieren legajos/custodios permanentes mientras los reportingclerks regresan a5.23,o4 solo exige departure y nueva llegada de los asistentes; no comprueba que la outgoinglist siga bajo custodia pese a afirmarlo el texto.

Arrival es un hecho persistente por diseño. /tmp/gpt61-imperial-stay-vs-arrival.ts demuestra que una llegada posterior a otra zona conserva hasArrival(original)=true. No prueba presencia actual. No hay requisito reversible de localización/custodia porID ni transferencia que inmovilice el objeto. Repetir arrived al final no lo añade.22 es bloqueo del contrato de preservación, no defecto nuevo del S1 aprobado.

Autor acepta:21/23 deben prometer recepción registrada sin residencia implícita;22 necesita presencia viva actual de3legajos+3custodios porID→zona al cierre, con observación reversible y capacidad expresamente PENDIENTE. No se puede emular con timer o fake primitive ni marcar implementado con QA estático. Fuente corregida todavía no verificada por este informe; conservar P1 abierto hasta revisar el delta. No alterar S1done para acomodar el diseño.

## P2 — separar consultas antiguas superadas de evidencia aplicable

sourcePassages23 conserva consulta antigua2820/HistoriaAcephala/ApologiadeFuga que explícitamente no respaldaMilan y aún afirma wronglocalalignment.24 conserva comentario Potentialduplicatewith23. Los hechos actuales separanMilan355/Alex356 correctamente. Mantener trazabilidad es útil, pero esas filas deben marcarse superseded/candidate-only y no confundirse con apoyo de hechos actuales. Las consultas nuevas correctas permanecen.

## Historia y narrador comprobados

20:343 es marco editorial cualificado, no año demostrado porSocratesII20. Pasaje consultado utiliza intervalo/consulado y separaPhilippopolis. Los dos patios deSardica son ficticios; no se transporta el concilio externo dentro del mapa ni se compra reconciliación. Fechas alternativas y venue pendientes visibles.

21:HistoriaAcephala se atribuye al fragmento anónimo, no aAthanasius comoautor por un título delhost. I.2 leído incluyePaophi24 y conversión editorial21Oct346 con corchetes/reparaciones. Seis hogares y hosts son ficción, no séquito/gatehistórico. Marcus c334 tiene unos12; voz dice recibió papeles y no estuvo enAlexandria.

22:350 no convierte aConstantius en único emperador sin rival;353 permanece posterior. Milan recibe noticia deGaul, no es lugar de muerte ni batalla atestiguada. Marcus16 comoordinaryapprentice dentro de itinerarioMilan350–356; no vozomnisciente. La facticidad externa no depende de guardar los legajos jugables.

23:SozomenIV9 consultado presenta asistencia, presión/exilio y juicios partidarios, no transcripción neutral ni roomcoords. Se evita deducir de lista de exiliados asistencia deHilary. Markauskaspp72–74 consultadas: distingue respuestas, Hilarynoasistió, contextoMilan y anécdotaLiberius separada;Rimini359 no se traslada a355. Las notas/copias jugables son ficción contemporánea y no libros futuros; no bishopscomoactors ocreedscore. Marcus21 limita su memoria a taller imaginado, no sala deconcilio.

24:ApologiadeFuga24–25 yHistoriaAcephalaIV5/V6 consultados separan el ataque nocturnoMechir13/14 de transferencias posteriores/George357. Másde5000 sigue cantidad atribuida al defensor, no ejército certificado ni exigencia delmotor. Civiles ordinarios ficticios, ningún obispocontrolable ni rescate histórico. Marcus22 sigueenMilan recibiendo noticia posterior al ataque, no testigo presencialAlexandrino.

## Contratos y viabilidad estática

Todos los cincoaudit_dossier actuales devuelvenerrors=[]; esto NO cubre elP1 de presencia.60 desigualdades5×3×4 de stock sin premios cubren principal+reserva protegida+presupuesto reemplazo+todos los costes opcionales. Pagos/allocations finitos y sumas conservadas. Fundedderivation usa inputs propios recogidos y recibo exacto del pago del mismo objetivo opredecesor; no segundo débito. Departures22/23 consultan sus reportingclerks/assistants, no custodios o notas, y nuevas llegadas guardadas por arrivalAfterDeparture. No se encontró ciclo en esta lectura.

20 tiene8secundarios,21tiene7,22tiene6,23/24tienen7:35en total, todos dentro6–8, con actores/beneficios separados y tres carteras combinables. Su pérdida opcional no crea derrota principal. Solvencia no demuestra navegación ni disfrute.

24: pool original8 y mínimo6; final toma cualquier6supervivientes delpool entero, sin ledger deprimerosseis ni ordereddeparture deall8. Dos bajas no fuerzan un imposible, tercera viola supervivencia. Note original independiente. Cuatro guards fijos enjunction y roster inicial único16/22/28 por dificultad comprobados;20friendly, productionfalse/mobilizationsvacías. Área controlada/passable deo2hasta o3 requerida; pérdida tras latch causa derrota anunciada. No se acredita combate real con ese roster. Huellas/leashes/terreno/lineasagua y churchTheonasroute son planificación pendiente, no mapas antiguos nativos certificados.

## Lecturas propias y límites

- SocratesHEII20, NewAdvent https://www.newadvent.org/fathers/26012.htm : capítulo pertinente leído; no libro entero.
- HistoriaAcephalaI.2,IV.5,V.6, NewAdvent https://www.newadvent.org/fathers/2820.htm : pasajes pertinentes leídos, no testigo/autoría deducida del rótulohost.
- AthanasiusApologiadeFuga24–25, NewAdvent https://www.newadvent.org/fathers/2814.htm : ataque/retirada/polemica leídos; no todaobra.
- SozomenHEIV9, NewAdvent https://www.newadvent.org/fathers/26024.htm : asistencia/exilios y lenguaje delautor contrastados; no todaobra.
- MelissaMarkauskas2015: /tmp/markauskas2015.pdf, SOLO páginas físicas72–74/selección impresa72–74 extraídas también a /tmp/gpt61-markauskas-72-74.txt y leídas. No lectura de tesis completa, nuevasfiguras oproducción deassets.
- EutropiusX9: lectura independiente anterior propia de esta sesión sostiene distinguir muerte350 de sucesos340/350 y noMilan; no se afirma nueva consultaX10–12.

No consultados aquí:fuentesarqueológicasMuseoMilano/CEAlex/Sofia ni canones completos/Anastos/otrasmonografías. Datos queaportan son auditorías delautor con límites, no approvalpropio. No raster/DEM/nativeplaythrough ejecutado. Gate independiente adicional bun run validate enWIP:89/89Bun,301expect pasan, pero docs:check falla1. Su suitePython ejecuta50tests y uno falla: test_odyssey_status_rejects_false_approval_and_stale_artifact_coverage, error imperial-church: official proposal document missing. No validación global pasada atribuida. La auditoría focalizada y60desigualdades fueron propias, sin atribuir gates delautor como propios.

Sin blanketapproval histórico/geográfico/native/fun, sin cambio de estado de propuesta. P1 requiere corrección delcontrato antes de entregar23–24 como cierre de esta revisión conjunta.

Consulta adicional propia: introducción editorialRobertson/NPNF aHistoriaAcephala https://ccel.org/ccel/schaff/npnf204/npnf204.xxv.ii.i.html, párrafos sobre annalist bajoTheophilus, transmisión latina imperfecta y reconstrucciones/conversiones. Es crítica editorial antigua, no consenso actual. Ayuda a distinguir fragmento anónimo delautorAthanasius sugerido por elhost. No libro completo consultado.

## P2 adicional — integridad de la ruta oficial f00003 enWIP

El gate independiente no está verde: docs:check/test_design encuentra que el documento de propuesta imperial indicado en assignments no existe. Conservar el rename/trace y alinear ruta real según flujo oficial antes de publicar. No modificar archivos root por el revisor. Posible cambio concurrente/normalización automática mientras se elaboran los borradores; no se deduce una falla histórica de este resultado. El error reproducible exacto se comunicó alautor.

## Reevaluación del delta local — 2026-10-14

P1 atendido en DISEÑO, sin acreditar implementación. Inspección propia de episodes y episodeBlueprints actuales:21/o4 ahora solo exige tres notas y explica en EN/es que la recepción de los hogares no exige permanecer;23/o4 explica recepción separada de la lista, sin comprobar ubicación actual.22/o3 req3–6 identifica exactamente tres legajos originales y tres custodios originales, cada uno con destino asignado; current-alive-position, reevaluateBeforeTerminal=true, deliveryLedgerSubstitute=false e implementationStatus=unimplemented. presencePlan vincula las cuatro cláusulas y exige estado actual antes del cierre; requiredCapabilities declara referencia y nativo pendientes. Es metadata de diseño para futura fábrica, no un perfil ejecutable ya implementado.

Leí la propuesta i00005: S1 contrato/referencia y observación reversible/snapshots; S2 observadores nativos con prerequisito adicional explícito i00003/S3; S3 promoción/QA. Esto registra el requisito que faltaba sin alterar aprobación S1 previa. No apruebo la propuesta ni afirmo que estos slices estén implementados. El comportamiento real de22 sigue bloqueado hasta implementación y revisión de esa capacidad, exportación nativa y QA.

P2 de provenance atendido: las entradas antiguas23/24 figuran superseded-candidate-only con limitaciones de procedencia, tanto en dossier como en selección. P2 de ruta atendido: restaurada la ruta canónica referenciada por assignments; docs:check pasa ahora. No volví a consultar fuentes históricas en esta reevaluación: las lecturas propias documentadas arriba siguen siendo la base histórica, con sus límites.

Validación propia del WIP corregido: bun run validate exit0,89/89 pruebas Bun,301 expectativas, documentación/enlaces y campaign:validate correctos. Log /tmp/gpt61-imperial20-24-delta-validate.log. Auditoría focal de los cinco dossiers20–24: audit_dossier devuelve cero errores para cada uno. Mutación propia de22 req3 a entity-state/arrived conserva presencePlan y se rechaza con “current presence replaced with delivery history”. Inspeccioné los nuevos adversariales que también rechazan falsa implementación, capacidad ausente, destinos ausentes, duplicación de IDs y sustitución por ledger.

Este cierre es acotado a los hallazgos de diseño y metadata descritos. No constituye aprobación global histórica, geográfica, nativa, de diversión, balance ni d00002;23–24 siguen borradores locales.

Suite adversarial Python ejecutada independientemente:52/52 tests,exit0 (incluye las dos regresiones nuevas de presencia). Log /tmp/gpt61-imperial20-24-delta-python.log.
