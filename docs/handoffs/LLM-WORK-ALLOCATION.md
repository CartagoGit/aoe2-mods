# Reparto de trabajo y volumen pendiente

Corte operativo: 5 de noviembre de 2026. La [nota CURRENT-STATE](CURRENT-STATE.md) es la fuente compacta de contadores, dependencias y próximos paquetes; las secciones fechadas de este archivo conservan su valor histórico. El arquitecto decide historia, geografía, economía y diseño; Luna y MiniMax materializan paquetes cerrados sin solaparse. Recuperar del DelendAI conectado el estado, los claims y las unidades antes de asignar trabajo.

## Volumen de diseño histórico

| Odisea | Episodios seleccionados | Dossiers completos de diseño en borrador | Dossiers todavía por redactar |
|---|---:|---:|---:|
| Embers of the Covenant |30|30|0|
| The Eagle and the Cross |34|34|0|
| Keepers of the Unbroken Word |30|1|29|
| The Keys of the Eternal City |32|0|32|
| Beyond the Golden Gate |32|0|32|
| Beneath the Desert Stars |30|0|30|
| The Shattered Oath |28|0|28|
| From Damascus to the Far Horizon |32|0|32|
| The River Remembers |30|0|30|
| **Total** |**278**|**65**|**213**|

Los 65 borradores contienen 2.689 pantallas EN/es-ES, 405 secundarios y 216 objetivos principales. Siguen necesitando revisión histórica/editorial, geografía y calibración según cada slice; no equivalen a campañas aprobadas ni a escenarios jugados. Yavneh (dossier 65) es una inserción mecánica revisada dentro de un solo episodio; la revisión no cierra d00002/S4 ni aprueba historia, terreno, soporte nativo o juego. Hay cero campañas completas y cero campañas históricas plenamente verificadas en el motor.

El catálogo combina 26 perfiles base y 19 suplementales (45 identidades únicas), con 40 identidades geográficas ausentes que afectan a 58 selecciones. El manifiesto registra 50 recursos. Las referencias DSM modernas, incluidas las de Jerusalén, no reconstruyen terreno antiguo ni acreditan mapas jugables.

## Reparto por modelo

| Modelo/rol | Trabajo que conserva o recibe | Condición para darlo por terminado |
|---|---|---|
| gpt-6, arquitecto | Cerrar la arquitectura y las herramientas faltantes; decidir historia/geografía, revisar borradores y diseñar el siguiente episodio de la primera campaña. Preparar paquetes con contratos, datos y bloqueos explícitos. | Cada paquete puede ejecutarse con las operaciones existentes o registra el requisito ausente. Revisión independiente y aprobación formal separadas. |
| gpt-6-luna, recopilación/materialización | Investigación acotada y trabajo mecánico con archivos exclusivos. i00013/S1 está aceptada; S2 ya tiene una unidad Luna en corrección por un hallazgo de overflow. No abrir otra implementación paralela. | Claim propio, diff acotado, evidencia reproducible y revisión de otro modelo. No decide arquitectura, historia, mapas ni balances para desbloquearse. |
| MiniMax M3.1, materialización | Recibir un paquete cerrado de episodio nativo tras la decisión de mapa de root; luego, avanzar progresivamente por la primera campaña. No se autoriza completar los 213 dossiers en masa ni trabajar nueve campañas a la vez. | Cumplir el slice oficial y documentar límites; no inventar fuentes, historia, economía, terreno o capacidades. Un solo implementador por conjunto de archivos. |
| Revisor independiente | Un modelo distinto del implementador revisa el diff, criterios, casos negativos y evidencia del commit exacto. | Veredicto formal y gate DelendAI del producto exacto; el informe por sí solo no cierra un slice. |

Estos son volúmenes de trabajo, no horas/costes medidos. El reparto no concede a MiniMax todo el backlog ni obliga a esperar al cierre de las nueve odiseas. Una implementación nativa todavía sin contrato/template/evidencia vuelve al arquitecto; no se oculta como tarea mecánica.

## Primera implementación delegada y aprendizaje observado

Luna materializó f00001/S2: los dos bundles del laboratorio ficticio, 17 catálogos draft por bundle y 36 claves runtime en total, dejando fuera 7 intenciones condicionales documentales. Producto integrado en `9d5e744b`; [revisión independiente](../qa/route-pilot/s2-source-bundle-independent-review.md). El veredicto gpt-6 de `d29b751` se integró mediante el gate oficial en `137fdd73`; el servidor confirmó S2 done, implementer gpt-6-luna y reviewer gpt-6, aceptación3/3. Recuperar siempre ese estado antes de reclamar S3. La [enmienda de briefing](../wiki/route-pilot/17-briefing-binding-amendment.md) y su revisión están integradas en `c77052b2`.

1. **Omisión de especificación:** el inventario original no asignaba la intro de escenario obligatoria de T01. El arquitecto cerró la reutilización de la clave factual con ID de línea propio; no pidió al implementador inventar texto o alterar esquema. Las próximas revisiones de inventario comprueban todas las superficies obligatorias.
2. **Duración de lectura:** la implementación inicial daba 5 segundos también al resumen largo. Se corrigió con la estimación existente de 130 palabras/minuto sobre el máximo EN/es-ES, antes de integrar. Las próximas tareas reciben esa regla explícita, con tiempos estimados y pruebas nativas pendientes.
3. **Traducción acotada:** el lote se dividió en 8 locales y 7 locales entre agentes. Se comprobaron exactamente las 36 claves por locale y los textos EN/es-ES; el estado sigue draft. Ningún check sustituye revisión lingüística ni aprueba voces.
4. **Proveniencia:** snapshots automáticos de DelendAI conservaron archivos con autoría Git heredada. El implementador registró los hashes y su autoría real; no reescribió historia ni cambió configuración Git global/local.

La revisión independiente ejecutó ambos checks completos de staging y validate: 142 pruebas Bun, 2.069 aserciones, documentación/enlaces y campaña activa válidos. Se verificaron por separado las 14 duraciones, geometría/terminal del fixture y 36 claves. No se midió rendimiento de MiniMax: su lanzamiento real devolvió HTTP429/2056 sin ejecutar herramientas y la consulta MMX del 25 de octubre seguía indicando 0 % semanal general. No se compraron créditos. La asignación a Luna responde a la autorización posterior del propietario, no a una escalada automática oculta.

## Gates que siguen fuera de la mera autoría

Las capacidades nativas pendientes, plantillas reales, exportación soportada, carga en AoE2, rutas/huellas, guardado, progreso, presentación y calibración requieren sus evidencias propias. Pueden necesitar un tester con el juego disponible. La aprobación de textos en 17 idiomas y medios/voz conserva su revisión específica. No distribuir mods ni lanzar generación pagada masiva por completar un dossier o un piloto.

Para el trabajo concreto, seguir la [cola de paquetes](MINIMAX-M3.1-PARALLEL-QUEUE.md), la [especificación del piloto](../wiki/route-pilot/02-implementation-specification.md) y las propuestas actuales. i00008/S1 está `done` (revisión Luna 2/2; metadatos integrados en `137fdd73`), S2 está `done` (producto `6f06737`, veredicto `e08a5cb`) y S3 está `done` (producto `c5533f7`, revisión formal `3746e076`). S3 añadió la rama opt-in al auditor y preservó entonces la salida previa; tras insertar el nuevo dossier y regenerar, el informe actual tiene 64 filas y 54 candidatos, con 63 filas que muestran presupuesto accesible idéntico. No añade soporte nativo. `readiness_timing_audit` sigue cubriendo solo su plan legacy, no los perfiles v3.


## Medición por interacción y pruebas tempranas

El [primer corte reconstruido](../qa/campaign-design/interaction-progress-checkpoints.md) fija la comparación c5533f7→d6acfed: +1 dossier integrado, +51 pantallas, +7 secundarios y +2 recursos locales; quedaron64/214/2645/398/49. Es un intervalo reconstruido, sin timestamps de mensajes ni consumo por modelo; no es una media ni una predicción. Los siguientes cortes deben usar snapshots integrados comparables, distinguir los mismos contadores y disponer de al menos tres intervalos antes de publicar una media móvil. No sumar mensajes de herramientas, compacciones ni trabajo WIP. La cuota restante no está medida.

El propietario pidió probar la base en paralelo. La entrega f00001/S4 prepara un kit privado de los fixtures route-pilot/route-successor, con hashes, escenarios de diagnóstico separados, instrucciones y ficha de observación. Recuperar su producto y revisión actuales; el kit no demuestra que la UI o el juego hayan cargado. Primero probar carga, rutas A/B normales, derrota del guardia, guardado y EN/es. La sucesora tiene resumen estático: lector de progreso/recap adaptativo, arbitraje same-tick sin harness, plantillas/audio y calibración histórica conservan sus gates. No esperar los214 dossiers para registrar estos primeros fallos reales.

Dos decisiones mecánicas adicionales ya tienen paquetes cerrados: i00009/S1 recompensas opcionales authored/zero y i00010/S1 conjuntos de supervivientes originales (ambas con aprobación independiente; i00010 veredicto f4a2599). S2 de i00010 espera i00009/S2 aceptado e integrado porque comparten factory/runner; no trabajar los mismos archivos simultáneamente. La [incidencia de sesión vacía](../qa/campaign-design/delendai-unit-session-recovery-incident.md) documenta el rechazo inicial de i00009/S2 y limpieza oficial; comprobar la entrada nueva del trabajador antes de afirmar que está implementando. Ninguna decisión documental crea otro dossier o acredita un mapa nativo.

MiniMax fue consultado el26 de octubre mediante la skill mmx-cli: el endpoint devolvió100 % restante general (contadores absolutos generales0, por lo que no se infiere un cupo de tokens). Un lanzamiento real OpenCode1.19.3 con minimax/MiniMax-M3.1-Flash completó un inventario read-only, sin cambios. Encontró el campo loss obligatorio del contrato público y la ausencia de un archivo TypeScript en el Files del paquete de pruebas; el arquitecto los aclaró. La ejecución tuvo59 steps y105 tool calls: no es todavía una muestra de implementación y las futuras tareas deben recibir rutas concretas y evitar búsquedas recursivas amplias. La habilidad de razonar o eficiencia no se deduce del nombre del modelo. i00009/S2 ya está aceptado e integrado(0cf4d064/9f4be255); i00010/S2 sólo empieza con el packet actualizado integrado.


## Reanudación con resultados de MiniMax

El corte 188c2f9→dbee40d ya contiene una implementación real MiniMax: i00010/S2 (d86c5613, aprobación Luna afa036fc), más la revisión independiente de i00009/S3 (7cbac2b). Las tres propuestas i00008/i00009/i00010 están cerradas. No tratar como pendientes ni como tres nuevas campañas esos cierres. El diagnóstico parcial de Luna está integrado en a7f8dcd; root exportó después un escenario real de 400 × 400 y decodificó 160000 casillas y 36 marcadores, con validate 158/2138 y export 3 variantes / 2 round-trips. Aún no hay observación de juego.

El diseño parcial de Jerusalén quedó integrado en 4a0bdab: 20 entradas bilingües, 45 superficies prospectivas, sin nuevo dossier completo. En el corte dbee40d, el volumen era 64/214/2645/398/49, con 54 señales cívicas y 22 identidades geográficas pendientes para 25 selecciones. La recopilación posterior descrita al final eleva solo las referencias a 50. Los 278 episodios mecánicos se reparten entre Luna/MiniMax cuando cada paquete esté cerrado; no son 278 para cada modelo. La media de interacciones no se calcula con dos intervalos que contienen tipos de trabajo distintos. Ver el segundo corte en el registro.

Luna devolvió límite de cuota en un intento anterior, pero el 26 de octubre retomó y completó una inspección acotada de los cinco primeros dossiers de faith-origins. No se infiere cuota restante de ese éxito. MiniMax también completó revisiones acotadas; ambos pueden recibir paquetes explícitos sin solapar archivos. El [paquete de presencia](MINIMAX-M3.1-PRESENCE.md) resuelve el documento ausente, pero sigue bloqueado por capacidades nativas; no es permiso para producir historia.


Actualización de recopilación: el manifiesto pasa de 49 a 50 recursos por el preview documentado del plano de Jerusalén 1865; no es terreno 70 ni nuevo dossier/geografía. Se mantienen 64/214/2645/398 y cero aprobación de juego. Los cortes d6acfed/dbee40d y las entregas previas que mencionan 49 siguen fechados; no se reescriben sus métricas.


El tercer corte documental dbee40d→6839db57 mantiene 64 dossiers / 214 pendientes / 2645 pantallas / 398 secundarios y suma una referencia (50). Incluye el diagnóstico real de 400 × 400 corregido/revisado, el packet de presencia bloqueado y el apoyo cartográfico de 1865. Son entregas concretas del arquitecto y revisiones de MiniMax; no otra campaña terminada ni una muestra adicional de implementación histórica. El [registro](../qa/campaign-design/interaction-progress-checkpoints.md) conserva las diferencias y por qué aún no hay media de interacciones comparable.

La [inspección económica de los cinco primeros episodios](../qa/campaign-design/faith-origins-first-five-economy-review.md) concreta cinco de las 54 señales existentes: todos sus pagos principales caben aritméticamente en el stock inicial declarado en las tres dificultades. No se han corregido todavía esos cinco dossiers ni acreditado cuentas nativas. El [packet de observación naval](TRANSPORT-MAP-DIAGNOSTIC-PACKET.md) cierra la siguiente tarea técnica parcial de i00003/S2; conserva pendientes sus observaciones de juego y la aceptación completa del slice.

## Cierre ampliado de la misma interacción

Luna implementó el paquete naval en `223740c7`, integrado por gate en `8f6687f3`. Root comprobó independientemente el binario, 9.600 celdas de franja, 36 marcadores, cuatro unidades, el vínculo exacto del guardia y TIMER 1800, además de hashes y catálogos. Las correcciones de revisión evitaron inferir el vínculo nativo desde el JSON y aceptar la condición en un disparador distinto. Es otra entrega mecánica acotada supervisada, sin aprobación completa de i00003/S2 ni de un escenario histórico.

En ese corte, root integró `7361d603`: Yavneh interior frente a su puerto, cautelas de fuentes y seis pares de texto fuente de narración, entrada y continuidad, revisados en alcance por Luna. Aún no era el dossier 65. El corte ampliado conservaba 64 dossiers, 214 pendientes, 2.645 pantallas, 398 secundarios y 50 referencias. El kit naval privado de 400 permitía observar la base mientras continuaba el diseño; juego verificado seguía falso. Ninguna nueva campaña histórica quedó completamente diseñada o aprobada para materialización por ese cierre.

Siguiente trabajo del arquitecto: cerrar controles, huellas, rosters finitos y perfiles de Jerusalén 70; convertir Yavneh en un dossier individual completo, resolver los cinco casos económicos concretos y continuar los 214 dossiers pendientes. Los cinco casos de revisión pertenecen a los 64 existentes y no restan de los 214 nuevos. Los trabajadores reciben el próximo paquete cuando esas decisiones estén cerradas; el de presencia permanece bloqueado por infraestructura nativa. No se deja una asignación ficticia activa por tener un documento.


## Corte vigente: primer episodio nativo entregado

El prototipo de Cesarea ya tiene seis variantes privadas, tres objetivos principales y seis secundarios, con [guía](PRIVATE-CAESAREA-OPENING.md) y [hashes](../qa/campaign-design/caesarea-private-opening-build.json). El producto de código `c55c3bd` quedó integrado en `e443aaaa`; su revisión independiente acotada se documentó en `6e1245e4`. MiniMax terminó la extracción reutilizable de la base nativa; Luna terminó los helpers espaciales y transaccionales, y las correcciones de fuente/binding; el arquitecto terminó su integración y empaquetado. El subconjunto privado no aprueba los slices amplios ni habilita el exportador público compuesto. Se mantienen 0 misiones históricas con prueba completa en el juego.

| Rol | Volumen pendiente en este corte | Trabajo que puede avanzar en paralelo |
|---|---|---|
| Arquitecto | 214 nuevos dossiers; revisión/corrección de los 64; cierre de geografía, dificultad, continuidad y capacidades nativas que falten. La calibración de la apertura y el diseño físico/semántico de Jerusalén siguen abiertos. | Decisiones del episodio siguiente, fuentes, rutas y contratos mientras se prueba la apertura y los trabajadores ejecutan paquetes cerrados. |
| MiniMax M3.1 | Materialización gradual de los 278 episodios, compartida con Luna. Hay 1 prototipo privado, 0 campañas históricas completas y 0 episodios con prueba completa del motor. Esos 278 no se suman a los 214 de diseño. | Inventario mecánico de riesgos de los 64 borradores, conforme al paquete cerrado asignado; después, implementación del siguiente componente decidido. |
| Luna | Recopilación y materialización del mismo pool, sin cuota separada prometida ni número adicional de escenarios. | Ya terminó el inventario de Jerusalén y la consulta arqueológica; inspecciona ahora las semánticas concretas del ledger de familias. Recibe nuevas fuentes o código solo con alcance explícito. |
| GPT-6.1 / revisión independiente | Revisión de cada producto de root asignado, y veredictos formales cuando se cumpla todo el criterio del slice. | Revisión del kit, hashes y guía sin bloquear el diseño del siguiente episodio. No equivale a ejecutar AoE2. |

El backlog geográfico y las banderas cívicas siguen siendo candidatos de revisión, no una cuenta de fallos de juego. No hay velocidad comparable de producción histórica por interacción; los intervalos de infraestructura no permiten calcular cuántas conversaciones o tokens faltan. Se conserva evidencia por producto y se actualizan los contadores solo al integrar.

Lección operativa incorporada: una generación superior del mismo slice sustituye las unidades anteriores incluso entre agentes. Los trabajos paralelos del mismo slice usan la generación vigente y Files disjuntos; se consulta al runtime antes de abrirlos. Las entregas anteriores de MiniMax y Luna se conservaron y transfirieron oficialmente; no se cambia identidad para publicarlas ni se usa develop manualmente.


La corrección mecánica del episodio02 ya está integrada (`53f5275` → `1a286985`): mismo grupo original, requisito adicional de supervivencia con tipos existentes, recepción occidental de visitantes y descripción geográfica corregida. El diseño independiente (`74a59de`) incluye 21 casos prospectivos y una comparación de 648 muestras del DSM moderno; ninguna ruta está aprobada ni hay un segundo escenario nativo. El cierre nativo deberá comprobar las identidades vivas y registrar objetivo/desenlace en una misma operación.

El [paquete de reutilización del runtime civil](SHARED-CIVILIAN-NATIVE-RUNTIME-PACKET.md) asigna a Luna una extracción de tres archivos, con comparación estricta contra la misión privada existente. MiniMax mantiene el inventario de riesgos de los 64 borradores en su unidad: los resultados son WIP hasta corregir los hallazgos y verificar todas las referencias. No se suman sus candidatos a los 54 de la auditoría cívica ni se presentan como fallos de juego.


El inventario de MiniMax ya está integrado en `9ef440c5`, con [revisión independiente](../qa/campaign-design/catalogue-design-risk-independent-review.md) y 20 comprobaciones enfocadas conformes. En ese corte dejó de ser una asignación activa: cualquier corrección de contenido requería un paquete propio cerrado por el arquitecto. La prioridad entonces era el binding geográfico y el compilador de hogares del episodio02, usando el runtime civil ya extraído; no se delegaba la selección de una ruta antigua ni la calibración como si estuvieran resueltas. El corte vigente está resumido en [CURRENT-STATE](CURRENT-STATE.md).


## Corte operativo: controlador de hogares y distribución física

El controlador privado de hogares de MiniMax está integrado: producto `111d4967`, merge oficial `5bdd1fa3`. Root y GPT-6.1 cerraron los hallazgos del alcance acotado; pasaron26 pruebas enfocadas, validate158/2.138 y export3 variantes/2 roundtrips. El [registro de revisión](../qa/campaign-design/native-household-controller-review.md) distingue compilación nativa, harness con consultas simuladas y juego todavía pendiente. No existe un segundo escenario histórico entregado ni aprobación completa de i00003/S3.

Luna terminó la extracción de validación común (`cc92a7c` → `8e73c75`), conservando firma/XS de la apertura:143 triggers/87 variables. Su unidad ya está retirada. MiniMax terminó el [paquete cerrado de extracción de firma](MINIMAX-NATIVE-SIGNATURE-EXTRACTION-PACKET.md): producto5afacb1 integrado en f2418477. Root verificó AST y fuente exactos,34 pruebas enfocadas y gates completos; la [revisión](../qa/campaign-design/native-signature-extraction-review.md) conserva las incidencias de entorno y la corrección de checkpoint. No se le delega decidir historia, rutas antiguas o balance. La generación5 anterior está integrada y retirada.

La distribución física propuesta del episodio02 separa17 cuerpos y10 círculos y conserva23 casos prospectivos. La comprobación final de GPT-6.1 ya confirmó el contador corregido y el resto de su alcance. La nueva referencia DSM cubre el marco completo con495.187 muestras sin remuestreo; también fue comprobada independientemente, con georreferencia, bytes, hash y derechos. Son datos modernos y un diseño físico propuesto: ninguna ruta antigua está aprobada y no hay terreno nativo histórico construido. El [registro de diseño](../qa/campaign-design/jerusalem-household-design-review.md) documenta las limitaciones.

Luna y GPT-6.1 retomaron y completaron estos trabajos tras los límites de cuota anteriores. Aquellos rechazos quedan como antecedentes; no se presentan como bloqueos actuales ni permiten inferir una cuota futura. La unidad cartográfica vacía de Luna se retiró sin producto.

El diseño financiero y la inserción canónica de Yavneh se resumen en [CURRENT-STATE](CURRENT-STATE.md) y en el [informe de inserción](../qa/campaign-design/yavneh-canonical-draft-insertion-report.md). La revisión independiente del 5 de noviembre cubre esa transformación y su preservación, no la aprobación histórica ni el cierre amplio de d00002/S4. Las decisiones y la geografía siguen limitadas por los estados indicados allí.

| Rol | Pendiente verificable | Frente que puede avanzar |
|---|---|---|
| Arquitecto gpt-6 |Cerrar arquitectura/herramientas y decisiones de historia/geografía del episodio siguiente; revisar los borradores y autoría. |Paquetes cerrados y decisiones atribuibles; comenzar por el avance privado gradual de Embers of the Covenant. |
| MiniMax M3.1 |Implementar solo el siguiente paquete mecánico nativo tras decisión cartográfica de root; avanzar por campaña de forma progresiva. |Un slice oficial, sin inventar historia, presupuesto o terreno ni duplicar tareas de Luna. |
| Luna |i00013/S1 está aceptada; una unidad Luna ya corrige i00013/S2 tras el hallazgo de overflow. No duplicar la implementación. |Claim propio y revisión de otro modelo; el código WIP no hace disponible la operación en develop. |
| GPT-6.1 / revisor independiente |Revisar productos distintos al propio y registrar veredictos formales en los slices asignados. |Diff y evidencia del commit exacto; la revisión no acredita juego. |

El corte vigente es 278 selecciones/9 odiseas, 65 dossiers/213 sin dossier, 2.689 pantallas, 405 secundarios, 216 principales, 50 recursos y 45 perfiles geográficos únicos. Hay una apertura privada con seis variantes, cero campañas completas y cero campañas históricas plenamente verificadas en el motor. No se ha medido una tasa comparable de producción por interacción; véase [CURRENT-STATE](CURRENT-STATE.md) y el [registro de cortes](../qa/campaign-design/interaction-progress-checkpoints.md).


En el corte de `b4bdc4ee`, la proyección de costes authored de Luna ya había pasado por la fábrica real y el gate: se conserva el valor por defecto al omitir el campo; reparación/comercio/hospitalidad expresan costes en referencia. Hubo cuatro pruebas nuevas y 126 de diseño, más validate 158/2.138. No añadió hospitalidad nativa ni alternativas v3 nativas. El [candidato de Yavneh](../design/episode-plans/jewish-tradition/02-yavneh-world-plan.md) se integró en `b6dff66a` como preparación parcial; después se promovió a dossier 65 mediante `d771747`. Los requisitos que describen el helper anterior son diagnóstico histórico; el estado actual y los gates abiertos están en [CURRENT-STATE](CURRENT-STATE.md).
