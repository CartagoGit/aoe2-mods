# Cola de entregas para trabajo en paralelo

Decisión del propietario: el arquitecto sigue cerrando diseño mientras MiniMax materializa entregas ya preparadas. No se espera a terminar las nueve odiseas. Se usan propuestas, unidades, locks y revisiones del DelendAI conectado; este documento es un paquete de instrucciones, no una segunda cola o implementación de su runtime.

## Estado recuperado el24de octubre de2026

| Entrega | Trabajo del arquitecto | Encargo de MiniMax y bloqueo real |
|---|---|---|
| f00001/S1, laboratorio de rutas | Especificación, inventario bilingüe y matriz redactados por gpt-6, integrados en06e688e y aprobados independientemente por gpt-6-luna; metadatos integrados en3c41b4f5. | El servidor confirma S1 done; no adjudicar a MiniMax el texto del arquitecto. |
| f00001/S2 | S1 ya aprobado cierra mapas, identidades, objetivos, textos y límites nativos. | Primera materialización designada: ambos bundles en staging,36claves representables en17catálogos draft;7intenciones condicionales sólo documentales. S1 está satisfecho; falta cuota del proveedor para el trabajador designado. |
| f00001/S3 | Revisar ambos bundles y sus medios; reservar propiedad global de IDs/glosario. | Promoción conjunta únicamente tras S2, validación/export del perfil realmente soportado; no afirmar recap adaptativo implementado. |
| f00001/S4 | Arquitecto/tester verifica el motor y las capacidades ausentes. | Registrar evidencia real del artefacto; no completar por una suite estática verde. |
| f00002 y f00003–f00011 | Preparar primer expediente individual aprobado, metadatos comunes y mapa/operaciones como diseño, con revisión independiente. | Ningún capítulo histórico está concedido por este documento. Consultar estado vivo y recibir paquete individual; lo demás sigue bloqueado. |

El primer lanzamiento real por OpenCode, configurado como `minimax/MiniMax-M3.1-Flash`, recibió HTTP429/código2056: Token Plan usage limit. La sesión `ses_e90709888ffegF4vCs3Axe1zWY` no produjo edición, commit, unidad DelendAI ni muestra de calidad de código. La consulta OAuth de mmx mostró0% de cuota semanal general. No confundir autenticación con cuota disponible ni atribuir esta incidencia a calidad de MiniMax. No comprar créditos, cambiar de modelo ni arrancar una escalada automática por ese fallo. El siguiente intento recuperará el estado real y tomará sólo la tarea designada entonces.

## Gates según el trabajo concreto

1. **Diseño individual aprobado para fuentes.** El arquitecto entrega dossier completo de ese episodio, narrador/voz situada, pasajes consultados y cautelas, plano geográfico y limitaciones, objetivos principales/secundarios, economías/variantes, estados/persistencia, inventario de pantallas y continuidad exacta. Una revisión independiente identifica el commit aprobado y el alcance de esa aprobación. Un borrador o una selección no basta. La revisión como diseño no se presenta como prueba de mapa nativo o calibración jugada.
2. **Contrato disponible.** Todos los datos se representan en esquemas y referencias reutilizables existentes y revisados. Si la forma no existe, vuelve al arquitecto con reproducción; no editar packages/tools ni introducir campos para que parezca posible. Una referencia v2/v3 no habilita su exportación nativa. La autoría fuente puede avanzar conservando esa dependencia de exportación explícita.
3. **Fuentes en staging.** Tras metadatos comunes S2, cada slice de episodio depende de S2 y de su propio paquete aprobado, sin esperar materializar todos los episodios anteriores. La cronología del jugador sigue el manifiesto aprobado, no el orden de trabajo del agente. Cada episodio reclama además su campaign.json: localización y referencias de medios/fuentes se almacenan allí. Añade sólo el contenido aprobado del episodio; no modifica el manifiesto completo, la identidad ni el arco. El lock central serializa esas escrituras dentro de cada campaña, sin exigir materializar otros episodios antes. No fingir fragmentos de catálogos que el loader no soporta. Se usa staging:check --partial sólo donde el slice lo permite; una campaña incompleta permanece fuera de campaigns. Un slice terminado no convierte el bundle parcial en exportable.
4. **Promoción de campaña completa.** El slice final depende explícitamente de todos los slices individuales, no sólo del último cronológico. Exige todos los dossiers y fuentes revisados, pilotos y capacidades nativas usadas, plantillas reales, QA de motor por hash, traducciones/medios con estados honestos, staging completo y gates de exportación. IDs/glosario se materializan conjuntamente y bajo una sola propiedad. No bajar estos requisitos por autorizar fuentes tempranas.

Los títulos, IDs, orden de presentación, desenlaces, strings de progreso, esquemas y presupuestos no cambian con esta planificación. Las nueve propuestas conservan su estado blocked hasta que el servidor permita una transición y sus requisitos reales estén acreditados. El cambio de dependencias documenta una posibilidad de trabajo, no aprueba278episodios ni marca done ningún slice de d00002. S11 completo sigue dependiendo de los expedientes S2–S10.

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

Para el laboratorio, usar [especificación](../wiki/route-pilot/02-implementation-specification.md), [matriz](../wiki/route-pilot/03-acceptance-matrix.md) e [inventario](../wiki/route-pilot/15-text-inventory.json), cuando estén integrados y revisados. No copiar la versión preliminar de pantallas generadas por encima de la decisión cerrada. Las36claves de S2 y las7intenciones nativas pendientes están separadas por `sourceDisposition`; no añadir las7a un catálogo de ejecución ni enlazarlas con eventos falsos para eludir el validador.

## Ciclo de supervisión

El primer encargo es pequeño para observar el resultado real. MiniMax abre su propia unidad oficial, reclama sólo sus Files, materializa y ejecuta sus checks. El arquitecto revisa el diff contra el paquete, reutilización/naming, geografía y economía sin desviaciones, referencias/catálogos/medios y veracidad de la evidencia. La revisión formal la registra un modelo independiente del implementador conforme al runtime. Se corrigen defectos en la misma unidad, se vuelve a comprobar lo afectado y se publica sólo mediante DelendAI y su gate.

Cada devolución incluye archivo/campo, reproducción, resultado observado, resultado requerido y comprobación que cerrará el hallazgo. Las indicaciones de próximas tareas incorporan reglas extra sólo a partir de defectos observados. Registrar tiempos/coste/iteraciones únicamente si el proveedor aporta medidas reales; no inferir eficiencia o calidad por el nombre del modelo. El fallo de cuota inicial no aporta una muestra de implementación.

Mientras MiniMax trabaja, el arquitecto avanza otra entrega sin tocar su claim: fuentes históricas y geográficas, planos, narradores, secundarios, solvencia, dificultad y revisión de su última salida. Por defecto una sola unidad de implementación de MiniMax a la vez; tareas de recopilación o revisión independientes pueden seguir en paralelo con agentes autorizados. Las mutaciones de IDs/glosario siguen serializadas. Si una operación bloquea el encargo, se devuelve esa decisión al arquitecto; no se encadena por iniciativa propia otro episodio sin paquete aprobado.
