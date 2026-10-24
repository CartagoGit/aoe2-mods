# Checkpoint de arquitectura común de las odiseas

23 de octubre de 2026 · d00002/S1 · arquitecto `gpt-6`; recopilación de cobertura `gpt-6-luna`. Este documento registra un componente y trabajo pendiente, no una aprobación o cierre del slice.

## Discrepancia corregida

El arquitecto contrastó los nueve `actEpisodeTargets` de la [política](../../design/odyssey-policy.json) con la pertenencia existente de cada acto en los JSON de campaña. Se conservan las selecciones y su cronología; se actualizan las siete cuotas iniciales obsoletas, sin cambios de identidad, orden, contrato de motor ni cadenas.

| Campaña | Cuota anterior | Distribución editorial conservada |
|---|---|---|
| faith-origins | 6/6/6/6/6 | 8/7/6/6/3 |
| jewish-tradition | 6/6/6/6/6 | 5/7/5/7/6 |
| new-rome | 6/6/6/7/7 | 8/9/5/3/7 |
| first-caliphs | 6/6/6/6/6 | 7/7/7/5/4 |
| first-fitna | 5/6/6/6/5 | 5/6/5/7/5 |
| umayyads | 6/6/7/7/6 | 3/9/7/8/5 |
| house-of-ali | 6/6/6/6/6 | 5/5/6/7/7 |

Los repartos imperiales 6/6/7/6/9 y romanos 6/6/6/7/7 ya coincidían. El validador común comprueba ahora forma, integridad positiva, total y pertenencia; las regresiones distinguen una suma equivocada de una redistribución equivocada que conserva el total. No se introducen cuotas uniformes para forzar acontecimientos inventados.

## Evidencia existente y límites de S1

El [plan](../../design/odyssey-production-plan.md) establece nueve arcos, cinco actos, ritmo, variedad, fuentes atribuidas y prohibición de relleno. Los generadores compartidos de dossiers y secundarios reciben decisiones explícitas del autor y validan sus contratos; no seleccionan historia ni producen mapas nativos. Las curvas de los actos son hipótesis de presión, logística y recuperación, con calibración pendiente. Su presencia no acredita una progresión divertida ni sustituye revisión editorial.

La investigación delegada conserva consultas, variantes y límites; la nueva [colección de episodios judíos 5–8](jewish-episodes-05-08-primary-collection.md) es un ejemplo de contraste acotado, sin aprobación. El índice cuenta anotaciones de consulta, no hechos verificados. Hay cobertura desigual: 30/30 faith, 34/34 imperial, 17/30 judía, 19/32 romana y 16/32 oriental y ninguna anotación enlazada en las cuatro odiseas islámicas. Existen recopilaciones separadas; antes de cerrar S1 deben relacionarse con las selecciones canónicas y conservar la decisión del arquitecto, el pasaje realmente leído, tipo de acceso y cautela. Un enlace presente no será automáticamente una aceptación histórica.

También permanece pendiente la revisión editorial de hitos y de las curvas de acto. No se implementa una prueba automática que pretenda medir interés narrativo o rigor histórico a partir de un texto. La auditoría humana deberá justificar divisiones, repeticiones y cambios de contexto, manteniendo las restricciones de las fuentes y de reutilización de medios.

Los 215 episodios sin dossier no se usan por sí solos para declarar fallida esta arquitectura común: su redacción y aprobación pertenecen a las campañas S2–S10. El estado general conserva 278 selecciones, 63 borradores ampliados y ninguna aprobación ampliada de juego. Nada de esta reconciliación desbloquea MiniMax histórico, i00007/S3, navegación o ejecución en AoE2.


## Comprobaciones del componente

`python3 tools/design/test_design.py` pasa 68 pruebas, incluidas las dos regresiones nuevas; `python3 tools/design/odyssey_render.script.py --check` conserva nueve campañas y 278 selecciones, sin regenerar dossiers. La primera validación completa detectó correctamente que la política nueva invalidaba el fingerprint de la auditoría cívica. Se regeneró mediante su comando existente, con autor y fecha reales; el diff cambia únicamente fecha y hash de la política. Sus 63 dossiers y 54 candidatos a riesgo permanecen iguales. Esa actualización no corrige ni aprueba esos riesgos.

La integración del componente requiere el gate completo y una revisión independiente acotada. No se solicita `approve` del slice S1 entero por corregir su distribución de actos; el contraste histórico y la revisión editorial descritos arriba siguen pendientes.


## Cruce de consultas — continuación del 23 de octubre

El [informe reproducible de consultas](source-consultation-crosswalk.md) comienza a cubrir la brecha de vínculo por selección. Añade 30 registros de la auditoría islámica existente mediante identidades semánticas y punteros exactos; las cifras anteriores de anotaciones dentro de los JSON de campaña no cambian. El registro lateral conserva las selecciones sin modificarlas y distingue la declaración archivada de la consulta nueva del arquitecto.

El primer lote registró nueve comprobaciones acotadas: siete con algún texto accesible y dos cuyo repositorio solo mostró una barrera de JavaScript. Se conserva el intento parcial de Khandaq que no recuperó el pasaje de Medina. Una consulta posterior del PDF del editor sí localizó ese párrafo: resuelve el acceso a esa referencia atribuida, sin cotejar fuentes medievales ni aprobar cronología, terreno o interpretación. En ese lote, otros 21 registros enlazados todavía no tenían lectura nueva del arquitecto. Se corrige una atribución bibliográfica y se muestran las discordancias del archivo original; no se afirma resolver por ello las fechas, la geografía ni las condiciones de ninguno de los 30 escenarios. Los nombres y rangos de campaña permanecen intactos.

S1 continúa pendiente. La validez del cruce es integridad de investigación, no aprobación histórica: faltan extenderlo al resto de selecciones y contrastar sus afirmaciones, además del juicio editorial de hitos y curvas. Ningún contador de enlaces levanta gates de autoría, motor o nivelación.

### Segundo lote de contraste de fuentes

El [checkpoint de contraste](first-caliphs-source-contrast-checkpoint.md) amplía el registro a 30 comprobaciones de acceso/alcance para first-caliphs, con 18 consultas reutilizadas, 28 episodios con algún pasaje legible y dos intentos de Aqaba sin texto. Se preservan los intentos anteriores, las auditorías originales y las selecciones canónicas. Los nuevos contrastes identifican la contradicción sobre Hormozan, una página equivocada de Kaegi, cronologías competidoras y fases distintas en la recopilación sobre Alejandría. No son 30 aprobaciones históricas ni mapas listos. Los 248 episodios de las otras ocho campañas siguen sin vínculo en este registro lateral, aunque sus anotaciones anteriores permanezcan disponibles; el resto de S1, la revisión editorial y los gates de juego siguen pendientes.


## Dirección editorial por acto y nuevas recopilaciones — 24 de octubre

El arquitecto redactó [45 fichas particulares](act-editorial-review.md), una por acto, con referencias semánticas de entrada, inflexión y cierre. Incluyen consecuencias y recuperación, distinguen problemas de episodios vecinos y asignan al arquitecto las decisiones pendientes; no delegan su resolución a MiniMax. El [registro JSON](act-editorial-review.json) fija la revisión contra hashes de las nueve fuentes. Es un componente editorial fechado, pendiente de revisión independiente; no una aprobación formal de S1, una nueva investigación histórica integral ni un contrato jugable por episodio.

Ocho bandas `historicalYearBand` de cinco campañas se ajustan a fechas ya presentes en sus selecciones, conservando incertidumbres: Kent hasta 597, Chipre desde 649, los solapamientos de tres actos de First Fitna y dos de House of Ali, y el marco 342–359 del acto imperial que contiene Sárdica. El último no selecciona un año exacto del concilio entre alternativas transmitidas. El diff canónico se limita a esos ocho campos de metadatos. No cambia ningún episodio, pertenencia de acto, ID, orden, fecha de episodio, narrador, objetivo, contrato, cadena ni continuidad. Las cinco cabeceras wiki afectadas se regeneran mediante la herramienta existente. La auditoría cívica actualiza fecha y cinco fingerprints de campaña, manteniendo íntegros sus resultados y 54 candidatos de riesgo.

Luna aporta dos recopilaciones con referencias exactas a las [28 selecciones de First Fitna](first-fitna-source-collection.md) y las [30 de House of Ali](house-of-ali-source-collection.md). La primera procede de su unidad oficial separada; la segunda es investigación de solo lectura incorporada por el arquitecto tras rechazarse una entrada simultánea con la misma identidad real. No se presenta esa segunda recopilación como trabajo de una unidad que no existió. Los [siete contrastes propios del arquitecto](ali-family-architect-source-contrast.md) distinguen quién leyó qué y preservan el intento fallido del volumen XVII. No se han leído íntegramente las obras citadas ni cotejado el árabe.

El cruce normalizado sigue enlazando únicamente las 30 selecciones de first-caliphs; las otras 248 no se añaden a su contador por tener recopilaciones separadas. Estas nuevas fuentes no resuelven automáticamente fechas, localizaciones, motivaciones privadas o voces auténticas. La revisión histórica por selección y la consolidación editorial de S1 siguen abiertas. Los dossiers y sus gates geográficos, nativos y de juego permanecen en S2–S10: 63 borradores, 215 selecciones sin dossier y ninguna aprobación ampliada de juego.

La revisión independiente de este componente detectó 21 localizadores de First Fitna con páginas inconsistentes. El arquitecto comprobó las transiciones del PDF oficial y conserva [la corrección explícita](ali-family-architect-source-contrast.md#pagination-correction-after-independent-review), junto al localizador archivado: no se reescriben los bytes ni la declaración original de Luna.

Comprobaciones de esta continuación: 79 pruebas de diseño correctas (32,888 s); `odyssey_render.script.py --check` conserva nueve campañas y 278 selecciones. La comprobación acotada confirma 45 anclajes exactos, nueve fingerprints de campaña, ocho únicos campos de metadatos modificados, 28 + 30 vínculos canónicos, dos hashes de recopilación y resultados cívicos idénticos. `bun run validate` pasa completo: 142 pruebas, 2.069 aserciones (31,39 s), tipado/lint, documentación y validación de la campaña técnica. No se toca el adaptador y no se atribuye a esta entrega una nueva prueba de exportación o motor. Las correcciones posteriores de redacción y localizador requieren la comprobación documental y el gate de publicación sobre el candidato final.
