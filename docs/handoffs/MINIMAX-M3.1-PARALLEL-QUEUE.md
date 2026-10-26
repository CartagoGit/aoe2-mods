# Cola de entregas para trabajo en paralelo

Decisión del propietario: el arquitecto sigue cerrando diseño mientras MiniMax materializa entregas ya preparadas. No se espera a terminar las nueve odiseas. Se usan propuestas, unidades, locks y revisiones del DelendAI conectado; este documento es un paquete de instrucciones, no una segunda cola o implementación de su runtime.

## Estado recuperado el 25 de octubre de 2026

| Entrega | Trabajo del arquitecto | Encargo de MiniMax y bloqueo real |
|---|---|---|
| f00001/S1, laboratorio de rutas | Especificación, inventario bilingüe y matriz redactados por gpt-6, integrados en06e688e y aprobados independientemente por gpt-6-luna; metadatos integrados en3c41b4f5. | El servidor confirma S1 done; no adjudicar a MiniMax el texto del arquitecto. |
| f00001/S2 | S1 y su corrección de briefing están integrados y revisados. | Luna materializó los dos bundles, 36 claves runtime y catálogos draft por locale; siete intenciones nativas quedan fuera. Producto `9d5e744b`, veredicto `137fdd73`; S2 `done`. |
| f00001/S3 | S2 revisado; se reservaron conjuntamente staging, campañas, IDs/glosario. | Promoción conjunta y exportación soportada hechas en producto `3d955598`; revisión independiente `9c1486af` integrada en `dc23f194`; S3 `done`. No afirmar pruebas de juego ni GAME VERIFIED. |
| f00001/S4 | Dossier de pruebas y kit privado entregados y revisados en producto `9eac67e5` / veredicto `9047d995`. | S4 done; pruebas reales del motor y capacidades ausentes siguen pendientes en s00001. Un gate estático no las acredita. |
| i00008 | Decisión del arquitecto y revisiones independientes integradas; S1 done (Luna 2/2, 34 casos prospectivos), S2 done (`6f06737`, `e08a5cb`) y S3 done (`c5533f7`, `3746e076`). | S3 conserva la rama legacy para registros sin `designProfile` y añade despacho opt-in. La integración preservó el corte previo de 63 filas; el informe regenerado tras insertar el dossier ID34 tiene 64 filas, 54 candidatos y 63 casos con presupuestos accesibles idénticos. No añade soporte nativo. |
| f00002 y f00003–f00011 | Preparar primer expediente individual aprobado, metadatos comunes y mapa/operaciones como diseño, con revisión independiente. | Ningún capítulo histórico está concedido por este documento. Consultar estado vivo y recibir paquete individual; lo demás sigue bloqueado. |

El primer lanzamiento real por OpenCode, configurado como `minimax/MiniMax-M3.1-Flash`, recibió HTTP429/código2056: Token Plan usage limit. La sesión `ses_e90709888ffegF4vCs3Axe1zWY` no produjo edición, commit, unidad DelendAI ni muestra de calidad de código. La consulta OAuth de mmx mostró 0 % de cuota semanal general y la consulta del 25 de octubre mantenía ese bloqueo. No confundir autenticación con cuota disponible ni atribuir esta incidencia a calidad de MiniMax. No comprar créditos ni arrancar una escalada automática por ese fallo. El propietario autorizó después delegar también la materialización a Luna: esa asignación explícita produjo S2, sin atribuir el resultado a MiniMax. El siguiente intento recuperará el estado real y tomará sólo la tarea designada entonces.

El [reparto por LLM](LLM-WORK-ALLOCATION.md) detalla los volúmenes restantes y las correcciones observadas en la primera implementación. El catálogo actualizado tiene 64 dossiers, 214 selecciones sin dossier, 2.645 pantallas y 398 secundarios. Constantinopla380 (ID 34, orden 33) aporta 51 pantallas y siete secundarios dentro de ese total; su diseño candidato no constituye aprobación histórica, mapa jugado ni ejecución nativa.

El [paquete i00008/S2](FULFILLMENT-DOSSIER-S2-PACKET.md) describe el proyector/reutilización económica. El [paquete S3](FULFILLMENT-DOSSIER-S3-PACKET.md) delimita el despacho del auditor: sin discriminador se conserva la rama legacy; solo `designProfile=alternative-fulfillment-v3` usa la rama nueva; un discriminador desconocido o vistas incompletas/drifted fallan con diagnóstico, no con valores por defecto. La aceptación S3 no autoriza contenido histórico, herramienta de tiempo v3 ni exportación nativa.

## Gates según el trabajo concreto

1. **Diseño individual aprobado para fuentes.** El arquitecto entrega dossier completo de ese episodio, narrador/voz situada, pasajes consultados y cautelas, plano geográfico y limitaciones, objetivos principales/secundarios, economías/variantes, estados/persistencia, inventario de pantallas y continuidad exacta. Una revisión independiente identifica el commit aprobado y el alcance de esa aprobación. Un borrador o una selección no basta. La revisión como diseño no se presenta como prueba de mapa nativo o calibración jugada.
2. **Contrato disponible.** Todos los datos se representan en esquemas y referencias reutilizables existentes y revisados. Si la forma no existe, vuelve al arquitecto con reproducción; no editar packages/tools ni introducir campos para que parezca posible. Una referencia v2/v3 no habilita su exportación nativa. La autoría fuente puede avanzar conservando esa dependencia de exportación explícita.
3. **Fuentes en staging.** Tras metadatos comunes S2, cada slice de episodio depende de S2 y de su propio paquete aprobado, sin esperar materializar todos los episodios anteriores. La cronología del jugador sigue el manifiesto aprobado, no el orden de trabajo del agente. Cada episodio reclama además su campaign.json: localización y referencias de medios/fuentes se almacenan allí. Añade sólo el contenido aprobado del episodio; no modifica el manifiesto completo, la identidad ni el arco. El lock central serializa esas escrituras dentro de cada campaña, sin exigir materializar otros episodios antes. No fingir fragmentos de catálogos que el loader no soporta. Se usa staging:check --partial sólo donde el slice lo permite; una campaña incompleta permanece fuera de campaigns. Un slice terminado no convierte el bundle parcial en exportable.
4. **Promoción de campaña completa.** El slice final depende explícitamente de todos los slices individuales, no sólo del último cronológico. Exige todos los dossiers y fuentes revisados, pilotos y capacidades nativas usadas, plantillas reales, QA de motor por hash, traducciones/medios con estados honestos, staging completo y gates de exportación. IDs/glosario se materializan conjuntamente y bajo una sola propiedad. No bajar estos requisitos por autorizar fuentes tempranas.

Los títulos, IDs, orden de presentación, desenlaces, strings de progreso, esquemas y presupuestos no cambian con esta planificación. Las propuestas históricas conservan su bloqueo hasta que el servidor permita una transición y sus requisitos reales estén acreditados. El cambio de dependencias no aprueba 278 episodios. En el estado recuperado, d00002/S2–S11 siguen pendientes; S11 consolida el traspaso de los materiales ya producidos, sin declarar aprobación de contenido, historia ni juego. La integración parcial de documentación o dossiers no cierra S11 completo, que sigue dependiendo de la finalización de S2–S10.

## Contenido obligatorio del paquete individual

El arquitecto asigna una sola entrega inicial y proporciona estos datos concretos antes de que MiniMax reclame archivos:

| Dato | Contenido verificable |
|---|---|
| Unidad | proposalId/sliceId reales, aceptación viva, base develop e identidad real del proveedor; sin sesión prestada. |
| Fuente aprobada | Commit integrado y revisión independiente con alcance; rutas del dossier, datos y documentos generadores que lo sustentan. |
| Archivos | Lista exacta de Files y del claim; señalar registros globales que ese slice no posee. |
| Materialización | Esquema/perfil y referencias existentes; entradas→JSON/medios/QA esperados, posiciones, recursos, condiciones y traducciones cerrados. |
| Decisiones | Narradores, hechos frente a ficción, alternativas, recetas/IDs/umbrales, prioridades terminales, continuidad y siguiente episodio/campaña ya elegidos. |
| Texto | Fuente EN y es-ES íntegros, claves semánticas, pantallas/condiciones, estados lingüísticos; señalar cada intención que no admite el contrato actual. |
| Evidencia | Comandos exactos que aplican al slice, resultados esperados, qué requiere motor/plantilla/proveedor y debe seguir pendiente. |
| Escalación | Ante contradicción: reproducción mínima, campo/operación ausente, decisión que debe tomar el arquitecto; conservar el resto del trabajo autorizado. |
| Entrega | Ref, checkout, sesión propia, claim, commit, diff, logs reales, limitaciones, próxima tarea designada. Sin aprobación propia. |

Para el laboratorio, usar [especificación](../wiki/route-pilot/02-implementation-specification.md), [matriz](../wiki/route-pilot/03-acceptance-matrix.md) e [inventario](../wiki/route-pilot/15-text-inventory.json), cuando estén integrados y revisados. No copiar la versión preliminar de pantallas generadas por encima de la decisión cerrada. Las 36 claves de S2 y las 7 intenciones nativas pendientes están separadas por `sourceDisposition`; no añadir las7a un catálogo de ejecución ni enlazarlas con eventos falsos para eludir el validador.

Las líneas obligatorias deben tener un binding explícito, incluido el intro de escenario. Repetir una clave existente no crea una clave nueva y cada línea conserva su ID propio. Para duraciones estimadas de fuente se usa la regla existente `max(2, ceil(max(palabras EN, palabras es-ES) / 130 * 60))`; la medida nativa sigue pendiente. Son correcciones derivadas de defectos observados, no nuevos requisitos inventados para cada tarea.

## Ciclo de supervisión

El primer encargo es pequeño para observar el resultado real. MiniMax abre su propia unidad oficial, reclama sólo sus Files, materializa y ejecuta sus checks. El arquitecto revisa el diff contra el paquete, reutilización/naming, geografía y economía sin desviaciones, referencias/catálogos/medios y veracidad de la evidencia. La revisión formal la registra un modelo independiente del implementador conforme al runtime. Se corrigen defectos en la misma unidad, se vuelve a comprobar lo afectado y se publica sólo mediante DelendAI y su gate.

Cada devolución incluye archivo/campo, reproducción, resultado observado, resultado requerido y comprobación que cerrará el hallazgo. Las indicaciones de próximas tareas incorporan reglas extra sólo a partir de defectos observados. Registrar tiempos/coste/iteraciones únicamente si el proveedor aporta medidas reales; no inferir eficiencia o calidad por el nombre del modelo. El fallo de cuota inicial no aporta una muestra de implementación.

Mientras MiniMax trabaja, el arquitecto avanza otra entrega sin tocar su claim: fuentes históricas y geográficas, planos, narradores, secundarios, solvencia, dificultad y revisión de su última salida. Por defecto una sola unidad de implementación de MiniMax a la vez; tareas de recopilación o revisión independientes pueden seguir en paralelo con agentes autorizados. Las mutaciones de IDs/glosario siguen serializadas. Si una operación bloquea el encargo, se devuelve esa decisión al arquitecto; no se encadena por iniciativa propia otro episodio sin paquete aprobado.


## Corte de coordinación — 26 de octubre de 2026

El propietario solicita pruebas privadas de escenarios/campañas mientras continúa el diseño. f00001/S4 prepara los dos ZIP fixture y escenarios exportados de diagnóstico con hashes/ficha; su aprobación formal y cualquier resultado real se consultan por separado. Las observaciones pueden avanzar en carga, caminos, rutas A/B normales, guardia, guardado e idiomas. La ausencia de plantillas/UI, lector de progreso, recap adaptativo o harness same-tick bloquea esos casos concretos, sin falsear el resultado ni detener toda la investigación histórica. Nunca usar un diagnóstico de editor para acreditar carga de la campaña o persistencia entre campañas.

Orden de paquetes de proyección: i00009/S1 aprobado → i00009/S2 materialización y revisión → i00009/S3 guía/evidencia; i00010/S1 aprobado en veredicto f4a2599 → S2 sólo después de i00009/S2 integrado y revisado. Ambos cambios reutilizan contratos existentes; ningún trabajador modifica identidad, esquema público o estadísticas para resolver Jerusalén. La [incidencia operativa](../qa/campaign-design/delendai-unit-session-recovery-incident.md) conserva rechazos y limpieza de la unidad vacía. La asignación viva sigue siendo exclusivamente DelendAI, no esta tabla.

El [registro por interacción](../qa/campaign-design/interaction-progress-checkpoints.md) mantiene cortes y deltas verificables. La primera comparación suma1 dossier/51 pantallas/7 secundarios/2 recursos; no permite estimar horas, cuota o interacciones restantes. Los64 dossiers siguen siendo borradores y los278 episodios forman un pool compartido entre implementadores, no una asignación duplicada para cada modelo.

f00001/S4 quedó aceptado2/2 (producto 9eac67e5, veredicto 9047d995) como dossier de pruebas, con motor pendiente. i00009/S2 quedó aceptado3/3 en0cf4d064/9f4be255. La próxima implementación que puede designarse es i00010/S2 tras integrar su aclaración de Files/puente artificial; i00009/S3 queda como tarea documental separada. Windows/Steam/español es la plataforma de prueba declarada por el propietario; la build y todas las observaciones siguen pendientes.


## Reanudación verificada

Desde 188c2f9 hasta dbee40d se integraron la implementación pooled y su revisión (d86c5613/afa036fc), la guía de recompensas y su revisión (34f87ce/7cbac2b), el diagnóstico grande parcial (a7f8dcd), y las decisiones parciales de Jerusalén (4a0bdab). i00008/i00009/i00010 están done globalmente. Los contadores históricos no cambian: 64 dossiers, 214 pendientes, 2645 pantallas, 398 secundarios, 49 referencias; juego verificado 0.

El siguiente paquete documental disponible es [presencia](MINIMAX-M3.1-PRESENCE.md), todavía bloqueado para ejecución. El diagnóstico 400 sí tiene una ruta existente de exportación reutilizable y root ya produjo un primer kit privado; el estado de publicación de sus nuevos recibos se recupera de DelendAI. No anunciar un nuevo escenario histórico por ello.

Cada trabajador usa exclusivamente su propia identidad, sesión y unidad oficial. No actuar dentro de una unidad ajena ni publicar usando `--agent` de otro modelo para rescatar trabajo durante una interrupción. Consultar el servidor y conservar el trabajo; las limpiezas permitidas del runtime no convierten el contenido parcial en aceptación completa. Antes de publicar, preservar kit y logs fuera de una worktree que el runtime puede retirar.

## Estado posterior de la misma reanudación

El paquete naval de i00003/S2 fue asignado a Luna y su producto `223740c7` se integró oficialmente en `8f6687f3`, con revisión técnica acotada root y gate. La unidad entregada se retiró conservando el producto; no es un encargo todavía activo ni aceptación de todo S2. El kit de 400 incluye barco, pasajero y franja artificial; la carga y el comportamiento de juego siguen pendientes.

La investigación y seis textos fuente bilingües de Yavneh se integraron en `7361d603` como diseño previo al dossier; no desbloquean propuestas de autoría histórica. El manifiesto está en 50 referencias locales, los dossiers en 64 y los pendientes en 214. Consultar el servidor para la próxima asignación concreta. El paquete de presencia sigue bloqueado y el arquitecto continúa decisiones históricas, geográficas y económicas sin pedir a MiniMax que las invente.
