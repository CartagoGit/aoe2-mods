# Revisión técnica independiente del cruce de consultas

23 de octubre de 2026 · componente de d00002/S1 · revisor `gpt-6.1-sol` · implementador `gpt-6`.

Esta revisión cubre exclusivamente el registro de consultas, su validador, generador, regresiones e integración documental. No solicita ni registra `approve` de d00002/S1 completo. El contraste histórico restante, los hitos y curvas editoriales, los dossiers y los gates de autoría conservan sus estados oficiales pendientes.

El candidato revisado es `100f8f017e138f21299171f20a256c8ecd7efd66`, sobre `9642c1d9a82aeefd0ec6d2680a61299482c9f096`. La unidad oficial del revisor es `wip/gpt-6.1-sol/review/d00002-S1-g1/source-crosswalk-component-review`, sesión `94626b5b`. Se consultaron overview, capacidades vigentes, instrucciones, traspasos y propuesta. El revisor reclamó y editó únicamente este informe; incorporó los candidatos a su propia unidad y no modificó implementación, pruebas, selecciones ni auditorías originales.

## Integridad comprobada

El [registro](source-consultation-crosswalk.json) fija los bytes de la auditoría archivada mediante SHA-256 y enlaza registros por ámbito de campaña declarado, ID semántico y JSON Pointer exacto. El hash de selección incluye campaña, ID, fecha, geografía y selección histórica completa; no depende del ordinal de presentación. Se inspeccionaron el parser de punteros, el confinamiento de rutas/symlinks, campos y versiones estrictos, unicidad, fuentes y consultas utilizadas, fechas, URLs HTTPS atribuidas y distinción entre acceso legible, metadatos e inaccesibilidad.

Las consultas nuevas no heredan una lectura completa del autor archivado. Los resúmenes, extractos y pasajes mantienen su alcance explícito. Un contador de texto accesible no demuestra relevancia, respaldo histórico ni aceptación. El comando de regeneración escribe únicamente el [informe reproducible](source-consultation-crosswalk.md); `verify.py` valida el cruce y rechaza resultados desactualizados dentro del gate documental existente.

El diff de producto frente a la base contiene nueve archivos de investigación y herramientas comunes. Permanecen intactos los JSON canónicos bajo `docs/design`, campañas, contratos, IDs, adaptadores y el archivo `first-caliphs-source-audit-v2.json`. El campo antiguo `sourceFile` de ese archivo no se usa para resolver rutas actuales. Las discordancias de URL, localizador, fecha y geografía se muestran sin corregir silenciosamente el canon.

## Riesgo reproducido y cerrado

En el candidato inicial se aceptaba trasladar un vínculo a otra campaña que declaraba el mismo ID de episodio, si se recalculaba el hash de selección: el registro de fuentes no delimitaba sus campañas. Este riesgo fue señalado por el implementador y reproducido independientemente con el fixture compartido entre `test-campaign` y `unlinked-campaign`.

El candidato final exige `campaignIds` no vacío, único y limitado al catálogo canónico, y comprueba ese ámbito en cada vínculo. Se repitió la reproducción con hash recalculado: devuelve `Binding campaign is outside the archived source scope` y ningún informe. La regresión automatizada incluye ese caso y ámbitos vacíos, duplicados, desconocidos o mal tipados. No quedan hallazgos técnicos abiertos del componente.

## Consultas bibliográficas propias y límites

La comprobación del revisor se distingue de las seis consultas que el registro atribuye a GPT-6:

- [Brockopp, extracto del editor](https://assets.cambridge.org/97805217/13726/excerpt/9780521713726_excerpt.pdf): se inspeccionaron los pasajes de las páginas impresas 4, 6–7. Son un contexto moderno de la tradición, los primeros adherentes, emigración/boicot e Hégira; no una lectura íntegra del libro ni un cotejo de testimonios tempranos.
- [Berkey, ficha y resumen del editor](https://www.cambridge.org/highereducation/books/the-formation-of-islam/0C58C7DC69FC4FFE20933C00B54D839F/the-origins-of-the-muslim-community/86DD5D5461286D6EA3B6EB4B9A120B5E): la búsqueda indexada de la página oficial expuso autor, capítulo, páginas 61–69 y resumen. Confirma la corrección bibliográfica Jonathan P. Berkey frente a Hawting. Los intentos de apertura directa agotaron tiempo; no se leyó el capítulo completo.
- [Poonawala, vida de Ali](https://www.iranicaonline.org/articles/ali-b-abi-taleb/ali-b-abi-taleb-i-life/): tras fallos de apertura directa, la búsqueda indexada oficial expuso metadatos y el párrafo de las expediciones. Se comprobaron la reputación legendaria y las atribuciones a relatos anteriores; ese párrafo no fecha Badr en 624. No se consultaron las obras medievales citadas ni se acredita lectura del artículo entero.
- [Morony, Khandaq, PDF del editor](https://www.iranicaonline.org/articles/khandaq/?generate_pdf=1): se localizó en la segunda página el párrafo final del cuerpo sobre Medina, abril de 627 y la cita visible a Balʿami I, páginas 202–7. La atribución del consejo a Salman está cualificada. Se comunicó al implementador el pasaje recuperado; el registro final conserva su intento parcial anterior y añade su consulta posterior. No se leyó Balʿami ni se verificaron calendario, dimensiones, tropas o terreno.
- [Repositorio del registro de Aqaba](https://escholarship.org/uc/item/87q494b4): los intentos propios devolvieron HTTP 429. No se leyó una tesis ni se comprobó su identidad bibliográfica; esto no convierte en lectura el intento fallido registrado por el implementador.

Estas observaciones corroboran localizadores o límites concretos, no la veracidad global de las afirmaciones de los escenarios. La consulta posterior de Khandaq resuelve un problema de recuperación, no una aprobación histórica completa. La fecha divergente de Yamama y las demás afirmaciones pendientes conservan su revisión específica.

## Pruebas y alcance del dictamen

Las diez pruebas focalizadas del candidato final pasan. La ejecución independiente anterior de diseño pasó 78 pruebas; el nuevo guard se inspeccionó y su regresión se repitió directamente. Doce mutaciones adicionales propias rechazaron versiones booleanas, aprobación desconocida, campañas/selecciones duplicadas, punteros inválidos, URLs sin atribución o HTTP, fecha imposible, consultas duplicadas, tipo de acceso inválido y hallazgos indebidamente atribuidos a metadatos. Una modificación explícita de la auditoría con hash actualizado produjo las cuatro discordancias esperadas sin alterar selecciones canónicas.

La validación completa independiente final sobre el candidato pasó con salida 0: `bun run validate`, 142/142 pruebas, 2069 aserciones, documentación/enlaces válidos y una campaña comprobada. Incluyó este informe; la sustitución posterior de este párrafo registra únicamente el resultado, sin cambiar enlaces ni código. Dos intentos propios anteriores fallaron exclusivamente por el timeout de 30 segundos de la prueba existente de 95 portfolios (31,991 s en la ejecución concurrente inicial y 30,172 s en el primer intento final serial), con 141 pruebas aprobadas y las 2069 aserciones completadas. El último reintento serial terminó con 142 aprobadas y 0 fallos, 30,30 s para toda la suite Bun. Se conservaron los fallos; no se modificaron timeouts, configuración ni alcance S2. La validación verde del implementador es evidencia separada, no se presentó como ejecución del revisor. No se ejecutó `test:export`: este componente no afecta al adaptador.

El informe final cuenta nueve campañas y 278 selecciones, con 30 vínculos de `first-caliphs`, nueve comprobaciones de episodio, siete con algún texto accesible, dos con acceso fallido y 21 vínculos sin comprobación nueva del arquitecto. Son seis consultas reutilizadas: no nueve lecturas independientes ni siete episodios aprobados. Las otras campañas sin vínculos aquí pueden tener anotaciones y auditorías anteriores en otros archivos.

El componente es técnicamente conforme con los límites descritos; el dictamen se limita a la trazabilidad. No registra revisión formal de S1, no aprueba hechos, fechas, mapas, mecánicas, traducciones, balance o exportación nativa, y no autoriza MiniMax ni distribución de mods. La integración y el retiro de la unidad del revisor se realizarán mediante las operaciones oficiales de DelendAI, conservando los commits y el informe.
