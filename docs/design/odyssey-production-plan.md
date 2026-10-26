# Plan de producción de las odiseas históricas

La nueva solicitud amplía el catálogo aprobado en d00001. Los 39 escenarios y 1.496 pantallas de aquella entrega son una base de contratos validada, no la entrega final de este alcance. d00002 se ocupa del diseño largo; MiniMax continúa bloqueado para la autoría nativa hasta que se cierren el diseño, las capacidades necesarias y los pilotos.

La referencia aportada por el propietario es [mod 550831](https://www.ageofempires.com/mods/details/550831), identificado por él como Bernard Nolan, con 29 escenarios. El portal público pudo descargarse, pero su servicio de detalles devolvió HTTP401 y no se han obtenido ni inspeccionado los escenarios. El número y el nombre se conservan como información del propietario, no como un hallazgo comprobado. No se copia texto, mapas, imágenes ni scripts de terceros por considerar que un mod descargable tiene licencia de reutilización.

## Propuesta completa de alcance

| Campaña | Objetivo de episodios | Periodo del arco | Actos y puntos de inflexión |
|---|---:|---|---|
| Embers of the Covenant | 30 | c.27–313 | Orígenes y testimonios / redes mediterráneas / diversidad y transmisión / crisis locales / persecución y cambio jurídico |
| The Eagle and the Cross | 34 | 312–381 | Puente Milvio y pactos / reunificación imperial / Nicea y nueva capital / muerte y sucesión / controversias y Constantinopla381 |
| Keepers of the Unbroken Word | 30 | 70–c.425 | Destrucción y reorganización / diáspora y revueltas / Mishnah / ciudades y academias / transmisión tardía y patriarcado |
| The Keys of the Eternal City | 32 | 337–800 | Roma y otras sedes / ciudad entre autoridades / guerras y reconstrucción / Gregorio y redes / francos y coronación800 |
| Beyond the Golden Gate | 32 | 337–843 | Capital y concilios / corte y crisis urbanas / guerra y abastecimiento / asedios e imágenes / disputas y restauración843 |
| Beneath the Desert Stars | 30 | c.610–656 | Primeras comunidades / Medina y pactos / sucesión y Arabia / expansión y acuerdos / administración y crisis656 |
| The Shattered Oath | 28 | 656–661 | Crisis y elección / Basra / Siffin / arbitraje y escisión / Hasan y transferencia661 |
| From Damascus to the Far Horizon | 32 | 661–750 | Consolidación y sucesión / Segunda Fitna / reformas y ciudades / fronteras / revolución y Zab |
| The River Remembers | 30 | 656–680 | Hogares y autoridad / conflicto y arbitraje / Ali y Hasan / mensajes y camino de Husayn / Karbala y memoria |

Total editorial vigente: 278 episodios; el objetivo inicial era 273. Las cifras guían la selección; no autorizan convertir un año vacío en una batalla inventada. Un proceso documentado puede desarrollarse en más de una misión cuando cambian lugar, agentes, problema o consecuencia. Dividir los tres objetivos de una misma misión en tres mapas repetidos no satisface este criterio. Cada excepción o ajuste de extensión se justifica con evidencia y arco.

El arco imperial se amplía hasta381 para incluir controversias, recepciones, exilios y transformaciones que no concluyeron en325. Las ramas romana y oriental comienzan antes de381 y sus entradas explican esa revisión cronológica desde otra perspectiva. Los antecedentes cristianos e islámicos se cuentan distinguiendo testimonios, creencias de las comunidades y hechos contrastados. La voz común no afirma milagros o revelaciones como hechos verificables, ni niega creencias mediante sarcasmo.

## Orden de ejecución y propietarios

S1 cierra esta arquitectura editorial, consolida y audita la investigación, y prepara funciones compartidas para construir y validar dossiers. S2–S10 cierran una odisea cada uno: cronología, actos, cada episodio, narrador, geografía, objetivos, tres dificultades, pantallas y QA. S11 consolida catálogo/wiki/propuestas/handoff y registra la revisión independiente.

Luna recopila fuentes, transcribe cronologías estructuradas y verifica formatos. Sus archivos son candidatos: el arquitecto verifica fechas, alcance, contradicciones y lo que realmente respalda cada pasaje antes de aprobar un hecho. No se asignan a Luna arquitectura, selección final, equilibrio, causalidad histórica ni interpretación del motor. Los informes completos y sus límites se guardan en [investigación](../research/odyssey-research/README.md).

El arquitecto mantiene los contratos y decide cada escenario; MiniMax materializa exclusivamente el slice indicado, sin ampliar periodos, inventar guerras, sustituir condiciones o diseñar una geografía distinta. i00003 acredita capacidades reutilizables; s00001 recoge pruebas reales del motor. Una capacidad no disponible no se presenta como implementada por describirla en un dossier.

## Contrato de cada episodio

Cada episodio tiene identidad estable y orden explícito; evento con rango temporal y grado de certeza; pasaje consultado, autor y sesgo; desenlace documentado; dramatización jugable acotada; lugar y extensión geográfica reales; protagonista jugable ficticio cuando conviene evitar falsificar la conducta de una persona histórica; y fases con predicados de mundo compuestos.

Se conservan los IDs de las 39 misiones existentes aunque cambie su posición. Las nuevas tienen IDs semánticos, independientes del número visible en el menú. No se renumeran cadenas ni se invalidan claves de progreso para acomodar un cambio editorial. Las últimas misiones y elecciones de ruta deben seguir siendo las que escriben las claves de cierre; una antigua misión final que pase al medio ya no puede cerrar anticipadamente el arco.

Los objetivos declaran objetos, custodios, familias, recibos, cantidades, zonas, precondiciones, recuperación y prioridades. Se preservan IDs entre fases; copia y copista son entidades distintas. Un recurso se descuenta y recibe una sola vez. El abastecimiento emparejado y la retirada usan el ledger de los mismos receptores. Todos los requisitos secundarios son tipados, nunca una frase que MiniMax deba interpretar. La falta de soporte nativo bloquea la compilación y abre un requisito de infraestructura.

Cada episodio incluye pantallas EN/es: título, contexto objetivo, cesión explícita al narrador particular, introducción personal, objetivos, instrucciones, reconocimiento, ayuda, eventos, victoria factual y personal, derrota y recuperación. Una reacción opcional conserva la personalidad de la campaña y no sustituye el relato histórico. Las páginas históricas amplían contexto y fuentes; no obligan a leer una monografía durante una batalla.

## Un narrador por odisea

Se conserva una persona por campaña, con temperamento, profesión, familia, experiencias, limitaciones y evolución a través de cinco actos. La voz común abre y cierra los hechos con sobriedad; después da paso a esa persona. Ni la voz común ni la persona se convierten en árbitro de cuál religión o bando tiene razón.

La ampliación de The Eagle and the Cross requiere revisar a Marcus: propuesta c.334–403, escribiente imperial criado entre documentos y testimonios familiares. Milvio, los primeros pactos y Nicea son archivos anteriores a su nacimiento; los últimos episodios pueden pertenecer a su experiencia adulta. Ninguna frase antigua de testigo312 se conserva por accidente. Las fechas, edad y base de conocimiento se verifican por episodio.

La biografía no es un permiso para narrar acontecimientos futuros: toda fecha fuera de la vida requiere que ese hecho se cuente por la voz común, o que el personaje de la campaña se sitúe en una época posterior y vuelva a comprobarse todo el arco. Los recuerdos infantiles y los cantos heredados se identifican de forma distinta a una observación adulta.

## Geografía, variedad y ritmo

Los mapas normales siguen siendo300–400 tiles por lado. Cada episodio usa controles reales y distingue costa moderna, reconstrucción antigua y localización incierta. Se amplía el atlas cuando cambia la zona; no se convierte un mapa de Fustat en Alejandría ni Siffin en todo el Éufrates. El campo exacto de una batalla discutida se marca como reconstrucción regional.

La actividad combina núcleo, hinterland, reconocimiento y desvíos útiles. Los depósitos opcionales proceden del banco finito y no son indispensables para pagar las tareas principales. Los sectores verdes de los planos son ámbitos de diseño, no nuevos yacimientos históricos. La implantación definitiva requiere relieve/hidrología, footprint y navegación certificados.

Cada acto tiene entrada legible, expansión de herramientas, reto central, consecuencia y descanso relativo. La variedad se registra: convoy, extracción, defensa, control de paso, negociación, reparación, circuito urbano, archivos, transporte o batalla acotada. Dos misiones consecutivas no repiten sin justificación el mismo problema, fases, composición enemiga y resolución. El reto deriva del entorno histórico y de decisiones tácticas, no de fabricar una guerra para una carta doctrinal.

Las cifras se fijan por misión y dificultad: stocks, extracción, pagos, reemplazo, recuperación, reservas enemigas, avisos, rutas, duración prevista y presión. La curva de una odisea larga exige que un final de acto sea intenso sin hacer todas las misiones finales o excesivamente largas. Los asedios obligatorios resuelven reservas declaradas; las misiones de retirada pueden terminar dejando reservas no movilizadas. La velocidad y los daños nativos no cambian con la dificultad.

La calibración se hace con partidas y cohortes, conservando las pruebas adversariales del contrato anterior. Documentar278 presupuestos no acredita278 mapas transitables o campañas divertidas. Las tasas objetivo, duraciones y límites de rendimiento siguen siendo hipótesis hasta registrar resultados reales.

## Integración y traspaso

Se reutilizan los generadores y validadores de tools/design. Los datos editoriales se separan por campaña para que cambios y revisión no requieran mantener manualmente cientos de dossiers. El catálogo y la wiki se regeneran de esos datos; la salida conserva las referencias al episodio, fuente y versión.

Cada campaña recibe su propuesta oficial revisada con slices por acto y episodios identificados; incluye dependencias, Files, gate, aceptación, resultados esperados, pruebas de guardado/reentrada, rutas, localización y arte. Un slice no permite completar una campaña distinta ni decidir nuevos objetivos. La entrega a MiniMax exige índices coherentes, todos los contratos cerrados y bloqueos reales resueltos; este plan no desbloquea automáticamente la producción.

## Ampliación de arquitectura y secundarios solicitada el 12 de octubre

El naming TypeScript sigue `{responsabilidad}.{tipo}.ts`: tipos reales como `schema`, `loader`, `validator`, `compiler`, `adapter`, `pipeline`, `helper` y `script`. No se crean barrels ni `index.ts`. Una carpeta agrupa una responsabilidad del dominio, no un contenedor universal `shared/utils`. La migración del código existente pertenece a i00004; los contratos y generadores de diseño de este documento no alteran ese refactor. MiniMax debe importar el archivo concreto y respetar el grafo documentado.

Cada escenario histórico exige entre seis y ocho objetivos secundarios explícitos, al menos cuatro mecánicas y tres formas de jugar. La base de39misiones recibe234objetivos particulares como primer paso. Esto no da por terminados los episodios adicionales de las odiseas. Sus recetas editoriales están en `docs/design/odysseys/<campaña>.json`; la generación compartida de IDs, predicados, costes, estados y pantallas está en `tools/design/secondary.py` y `optional_design.script.py`. El autor decide tarea y contexto; el generador no adivina condiciones a partir de una frase.

Las tareas son actividades locales ficticias declaradas, contextualizadas en los hechos documentados: auxilio de dos hogares con dos entregas individuales, dos copias independientes, restauración de un almacén, una remesa comercial, guía de camino, dos grupos voluntarios de evacuados, reconocimiento y observación. Cada tarea determina sus entidades finitas, origen, receptores, cantidades, pago, ventaja y estado final. No se puede usar una familia de un objetivo secundario para sustituir un ID protegido del objetivo principal. Los dos receptores o miradores tienen radios separados incluso cuando dos hubs comparten centro.

Las ventajas son suministros finitos descontados de las antiguas reservas opcionales, información de aproximaciones, pista histórica respaldada por las fuentes del escenario o señalización de un corredor ya existente. No se cambian hechos históricos, fuerza enemiga, hidrología ni velocidad para premiar un secundario. Reparar un almacén consume una transacción de50W que incluye la restauración; no se añade por detrás otro coste del motor. La remesa comercial requiere llegada real del comerciante y pago único de50G, después entrega150F50W. Su gasto usa el margen discrecional, nunca la reserva protegida de recuperación.

La victoria principal debe ser solvente si el jugador ignora todos los secundarios. También se comprueba el extremo contrario: completar todas las tareas debe caber en el superávit de cada dificultad. `secondaryBudget` separa fondos reservados, costes máximos y stock accesible sin recompensas; los antiguos depósitos genéricos dejan de acumular ventajas. Cada recompensa exige la operación atómica verificar predicados/stock → debitar reserva → acreditar stock jugable → guardar flag de recompensa → guardar finalización. Pago, visitas, IDs entregados, stock y estados fallidos persisten al guardar/cargar. No completar por reloj, visibilidad inicial o aparición ya situada en la zona de recepción.

Estados: available, completed, failed-optional, closed-at-terminal. Una entidad opcional perdida cierra solo esa tarea y explica el motivo; la partida principal continúa. Los secundarios están disponibles desde el comienzo, no llevan cronómetro oculto y se cierran al ganar/perder sin retrasar la campaña. Una llegada repetida, un doble aviso o una carga de partida no repite pagos ni recursos. La certificación nativa de estas operaciones pertenece a i00003 y s00001; la documentación no afirma que ya funcionen en AoE2.

Las tres estrategias declaran los secundarios que aprovechan y su coste de oportunidad: preparación de suministros, movimiento informado, cuidado civil y memoria. Son opciones combinables, sin puntuación religiosa ni ruta única óptima impuesta por el guion. Cada misión requiere partidas piloto saltando todos los secundarios y completándolos por cada dificultad, además de visitas tempranas, bajas opcionales, guardado antes/después del pago y final principal mientras una tarea sigue abierta. La geometría y los presupuestos estáticos detectan errores de contrato; su aceptación práctica depende del mapa y de partidas reales.

## Estado actual y puertas pendientes

A 18 de octubre de 2026, la selección contenía **278 episodios** y **305 slices de autoría**: 278 individuales y 27 de conformidad, metadatos y promoción. En ese corte había **63 dossiers redactados**, **2.594 pantallas EN/es-ES** y **391 secundarios**; quedaban **215 selecciones sin dossier**. Este es un registro histórico; la actualización vigente aparece más abajo. El catálogo anterior conserva sus 39 identidades, 1.496 pantallas y claves de progreso.

| Odisea | Dossiers / selección | Órdenes con dossier | Pendiente del arquitecto |
|---|---:|---|---|
| Embers of the Covenant | 30 / 30 | 1–30 | Revisión histórica/editorial, relieve y huellas, capacidades nativas, jugabilidad y dificultad |
| The Eagle and the Cross | 34 / 34 | 1–34 | Revisión histórica/editorial, geografía, capacidades nativas, jugabilidad y dificultad |
| Otras siete odiseas | 0 / 214 | Ninguno | Interpretación de fuentes recopiladas y diseño completo por episodio |

La tabla refleja el estado actual: **64 dossiers**, **2.645 pantallas EN/es-ES**, **398 secundarios** y **214 selecciones sin dossier**. No implica aprobación ampliada.

Las nueve biblias de narrador fijan biografía ficticia, cinco actos y acceso al conocimiento por episodio en [su fuente canónica](voices/odyssey-narrators.json). Los 49 recursos locales adicionales del [manifiesto](../research/odyssey-research/reference-manifest.json) tienen procedencia; ninguno acredita por sí solo una escena histórica ni arte de producción. Las dos referencias DSM de Jerusalén son superficie moderna para investigación regional, no terreno de 70 CE. La referencia Bernard Nolan continúa sin escenarios descargados o licencia de reutilización acreditada.

## Cobertura imperial y trabajo designado

La [enmienda](imperial-coverage-amendment.md) se integró oficialmente en `8a37f763d1b0e5b2bb1866131c45636bb5c1f283`. Su [revisión técnica independiente](../qa/campaign-design/imperial-coverage-migration-independent-review.md) verificó conservación de IDs/progreso/frontmatter, 278 selecciones y la corrección del bypass por etiqueta de scope. No aprueba los nuevos hechos históricos ni cierra d00002.

Los IDs nuevos 30/31/32/33/34 se presentan en los órdenes 28/29/30/31/33, slices S33/S34/S35/S36/S37. Los antiguos IDs 28/29 son ahora órdenes 32/34 y conservan S31/S32. Después de S30 se ejecuta S33→S34→S35→S36→S31→S37→S32; promoción S6 depende del último S32. El concilio381 sigue siendo el único final imperial. [Asignaciones](../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md) conserva la matriz de las nueve campañas.

*Beyond the Quiet River*, orden28, añade una red local ficticia en Alejandría365–366: seis voluntarios originales, cualquier mínimo simultáneo de cuatro en sus puestos asignados y un recadero distinto con salida causal. Tres lotes tienen reparto2/1; los pagos suman380F240W. Siete secundarios se pueden omitir. La presencia se comprueba al completar o2 y o3; no se congela a los primeros cuatro ni se exige residencia continua. El New River y la villa no se localizan. La crónica, los meses históricos y la carta/regreso permanecen separados del trabajo jugable. Su [revisión técnica independiente](../qa/campaign-design/imperial30-independent-review.md) no detecta P1/P2 en e90ae5f; historia, terreno y juego siguen pendientes.

*The Empty Chair*, orden29/S34, añade dos grupos distintos de cuatro hogares originales: hacen falta tres de cada uno en receptores diferentes, con presencia actual al final. No vale juntar seis supervivientes si un grupo queda en dos. Dos lotes y pagos460F220W tienen destinos propios. Catorce escoltas y8/14/20hostiles son ficción táctica finita; no se exige matar, rescatar aPedro ni recapturar iglesias. La [revisión técnica independiente](../qa/campaign-design/imperial31-independent-review.md) de2be5b7e no detecta P1/P2; historia, terreno, motor y jugabilidad siguen pendientes.

*Where the Eagles Fell*, orden30/S35, añade una retirada regional ficticia tras la derrota de378. Cualquier grupo de4sobre6rezagados a pie debe coincidir al oeste con2sobre4exploradores montados en el centro; después ambos mínimos deben estar presentes en la acogida suroccidental. No se fija a los primeros integrantes ni se mantiene el puesto central tras o2. Pago final180F80W, catorce tropas de apoyo y8/14/22hostiles finitos. Siete secundarios y tres planes combinables. El [expediente del relieve](../research/odyssey-research/adrianople378-relief-design.md) compara rutas y conserva los límites de la fuente y del DSM moderno. La [primera revisión independiente](../qa/campaign-design/imperial32-independent-review.md) detectó P1: la presencia anterior se reexigía al terminal e impedía la retirada. i00006/S1 añade el checkpoint explícito, integrado y [aprobado formalmente](../qa/campaign-design/checkpoint-presence-independent-review.md) en4248102. Este dossier opta ahora por checkpoint en o2 y conserva presencia actual final en o3; la [reevaluación independiente](../qa/campaign-design/imperial32-independent-review-round2.md) cierra el P1 del modelo con90combinaciones/499aserciones y ambas APIs de victoria. S2/S3, terreno histórico, IA acotada y juego siguen pendientes.

*The Burden of the Purple*, orden 31/S36, prepara tres puestos con tres remesas distintas y parejas elegidas de un mismo grupo de ocho originales. Requiere seis personas distintas repartidas2/2/2 y cada remesa en su puesto en una única observación de checkpoint. El plazo visible es ficción logística:20/16/12minutos, aviso a3; después termina y la salida causal queda sin plazo. El final reúne seis originales y las tres remesas presentes en el despacho nororiental. Total360F260W, siete secundarios y tres enfoques combinables. Nombramiento imperial, controversias y fechas transmitidas quedan separados del trabajo local. La [auditoría de marco](../research/odyssey-research/imperial33-map-control-audit.json) comprueba también el cuadrado completo, sin acreditar terreno antiguo ni navegación. Revisión técnica final y calibración pendientes.

El dossier de las transferencias urbanas de noviembre380 ya está redactado como ID 34, orden 33. Conserva perfil de referencia y 51 pantallas en orden combinado; sus coordenadas, fuentes modernas y suplemento UI son auxiliares y no establecen mapa jugado ni ubicación arqueológica. Sirmio379 tiene borrador completo de diseño (día de acceso sin resolver). Su perfil regional y fotografías arqueológicas modernas no identifican el lugar de proclamación ni la hidrología de379.

## Jugabilidad cívica y dificultad

La [auditoría mecánica actual](../research/odyssey-research/civic-difficulty-mechanical-audit.json) tiene 64 filas y 54 candidatos estáticos de riesgo; por separado, 63 dossiers tienen el mismo stock accesible entre dificultades. Son contadores distintos. El filtro identifica registros sin hostiles/plazo estructurados, pero no prueba falta de interés ni balance jugado. Se aplica el [contrato de aceptación cívica](civic-playability-acceptance.md): menos trabajadores o más minutos no bastan para aprobar dificultad. El arquitecto conserva los cambios de economía, distribución, objetivos y ritmo; MiniMax no resuelve esas decisiones.

## Capacidades y continuidad que siguen gobernando la entrega

- i00003/S1 implementa la referencia de fases, recibos, derivaciones financiadas y salidas causales; los observadores/materialización nativa y QA del motor siguen pendientes. Una conjunción final no autoriza fabricar antes de recoger y pagar.
- i00005/S1 está formalmente revisado e integrado en `d793ae4`, con corrección `983ef905`; S2/S3 siguen pendientes. Milán350 y la red alejandrina365 requieren presencia actual: una entrega pasada no prueba residencia. No reemplazarla por temporizador, flag arrived ni actor inmovilizado.
- Los manifiestos fluviales de las batallas324 y los riesgos ambientales de faith-origins15 siguen declarando capacidad pendiente. No usar llegada geométrica para fingir embarque, tránsito o desembarque.
- Cada final espera una elección válida antes de victoria, escribe solo su clave acumulativa y preserva las anteriores. Las sucesoras muestran título/ID y advertencia cronológica; recomendación de predecesora, recapitulación y comienzo independiente siguen obligatorios. Variables/menús/audio nativos y guardado/carga requieren evidencia propia.
- Las pruebas estáticas, round-trip y revisiones acotadas se documentan con su hash y alcance. Ninguna acredita terreno antiguo, navegación, voces auténticas, balance jugado o una campaña completa.

El [registro histórico](../qa/campaign-design/odyssey-design-progress-history.md) conserva los cortes anteriores y sus cautelas; sus números no son el estado actual. d00002/S1 está `done`; S2–S11 siguen pendientes según DelendAI. El traspaso histórico a MiniMax sigue bloqueado hasta cerrar cada requisito que le corresponda.


El dossier de Sirmio (ID 33, orden 31) y su revisión técnica se integraron oficialmente mediante DelendAI en 559fbc22. El [análisis condicional de preparación](../qa/campaign-design/imperial33-readiness-timing-analysis.md) documenta sensibilidad del plazo difícil a recorridos y velocidades todavía hipotéticos; no acredita un mapa jugable ni nivelación. La [hoja del episodio de Constantinopla](episode-plans/imperial-church/34-church-transfer-constantinople.architect-brief.md) acompaña al dossier ID 34, orden 33. El paquete de referencia está redactado, sin aprobación histórica o nativa ni prueba de juego. El catálogo cuenta 64 borradores y 214 selecciones sin dossier.


## Coherencia de actos — 23 de octubre de 2026

La auditoría común encontró siete repartos `actEpisodeTargets` que todavía conservaban cuotas iniciales y divergían de las selecciones cronológicas ya escritas. La política adopta ahora los tamaños de `acts[].episodeIds`, en su orden existente: no se mueve, crea, elimina ni renumera ningún episodio para satisfacer una cuota. El validador compartido exige cinco enteros positivos, suma igual al total de campaña y coincidencia con esa distribución; comprueba también una divergencia que conserva la suma. Esto no aprueba los hitos, las fuentes ni la dificultad de ningún acto.

S1 sigue abierto. Falta completar el vínculo por selección entre las consultas delegadas y la decisión histórica del arquitecto, además de la revisión independiente y consolidación editorial de hitos y curvas; las fuentes con acceso fallido o parcial no se convierten en hechos aprobados. Los expedientes completos y sus aprobaciones históricas, geográficas y de juego pertenecen a S2–S10. Ver [checkpoint de arquitectura común](../research/odyssey-research/common-architecture-checkpoint.md).


## Dirección de cada acto — 24 de octubre de 2026

Las [45 fichas editoriales](../research/odyssey-research/act-editorial-review.md) concretan para cada acto su entrada, inflexión, salida, presión/recuperación y diferencia respecto de problemas vecinos. El arquitecto conserva las decisiones pendientes por episodio. Ocho bandas temporales de acto se ajustan al marco de selecciones existentes, sin modificar sus fechas, incertidumbres, identidades, orden, contratos ni continuidad. Las bandas son marcos editoriales, no una nueva datación ni un reloj de juego. Las fichas requieren revisión independiente y aplicación detallada; no certifican nivelación ni completan S1.

Las nuevas recopilaciones de [First Fitna](../research/odyssey-research/first-fitna-source-collection.md) y [House of Ali](../research/odyssey-research/house-of-ali-source-collection.md) vinculan 28 y 30 selecciones a consultas declaradas de Luna. Los [contrastes del arquitecto](../research/odyssey-research/ali-family-architect-source-contrast.md) separan las lecturas propias, sus discrepancias y accesos fallidos. No son 58 aprobaciones ni amplían por sí solos el cruce normalizado, que conserva 30 selecciones de first-caliphs. Las fuentes, los dossiers completos y los gates pendientes conservan su alcance individual.


## Candidato a revisión común — 24 de octubre de 2026

Las 45 fichas editoriales y la trazabilidad de las 278 selecciones están integradas en `e70ace6d` y `990cfe13`, con sus revisiones independientes de componente y gates completos. El [expediente de aceptación S1](../research/odyssey-research/common-architecture-acceptance.md) reúne ambos criterios para revisión integral. Los estados pendientes y las cifras parciales de las secciones anteriores describen su fecha de redacción; el cruce actual ya enlaza 278 selecciones, sin convertirlas en hechos aprobados. Al redactarse ese corte, S1 todavía no tenía veredicto formal. S2–S10 conservan los expedientes y revisiones por campaña; S11 conserva consolidación y traspaso. Siguen existiendo 63 borradores, 215 selecciones sin dossier y ninguna aprobación ampliada de juego.

## Corte histórico de d00002 — 24 de octubre de 2026

d00002/S1 está `done` con aprobación formal de GPT-6.1 integrada en `b9cff83e76b3eaee75cef789b5ace09a1c6b417b` (producto `924ebde2`). La revisión cubrió los dos criterios completos y confirmó la corrección de dos familias P2 numéricas, documentadas en [aceptación](../research/odyssey-research/common-architecture-acceptance.md) y [revisión independiente](../research/odyssey-research/common-architecture-independent-review.md). Evidencia registrada: 142 pruebas Bun, 2.069 aserciones y 90 pruebas de diseño; sin acreditación de juego ni aprobación ampliada. S2–S11 siguen `pending`; permanecen 63 dossiers, 215 selecciones sin dossier, 2.594 pantallas, 391 secundarios y cero aprobaciones ampliadas. MiniMax continúa bloqueado para autoría histórica. f00001/S1, especificado por el arquitecto, está `done` tras aprobación formal e integración (`06e688e`, metadatos `3c41b4f5`); su siguiente slice mecánico es f00001/S2, pendiente por cuota del proveedor.

## Corte histórico de Constantinopla y cola — 24 de octubre de 2026

El [plan de mundo auxiliar de The Doors of New Rome](episode-plans/imperial-church/34-constantinople-world-plan.md) especifica 45 pantallas fuente y siete secundarios; el [suplemento UI](episode-plans/imperial-church/34-profile-ui-supplement.json) agrega seis para un total dossier de 51 pantallas y siete secundarios en ID 34, orden 33. La [revisión independiente del plan](../research/odyssey-research/constantinople380-world-plan-luna-review.md) comprobó consistencia estática; no acredita mapa antiguo, ejecución nativa, dificultad jugada o aprobación histórica. El episodio forma parte de los totales vigentes 64/2.645/398. El [manifiesto](../research/odyssey-research/reference-manifest.json) contiene 49 recursos.

La especificación de f00001/S1 y su [matriz de aceptación](../wiki/route-pilot/03-acceptance-matrix.md) fueron aprobadas formalmente e integradas; en este corte f00001/S2 seguía pendiente por cuota. El intento de iniciar MiniMax M3.1 Flash por OpenCode fue rechazado antes de trabajo por HTTP429/2056 (Token Plan); la cuota semanal general de MMX OAuth informó 0 % y la sesión no produjo ediciones. La secuencia puede avanzar por slices aceptados sin esperar a las nueve campañas, pero mantiene los gates específicos y no desbloquea propuestas automáticamente.

## Estado operativo sincronizado — 25 de octubre de 2026

Consulta el [reparto de trabajo](../handoffs/LLM-WORK-ALLOCATION.md) y la [cola de paquetes](../handoffs/MINIMAX-M3.1-PARALLEL-QUEUE.md) para las asignaciones vigentes.

El estado recuperado de DelendAI registra d00002/S1 `done` y S2–S11 `pending`. El estado editorial suma 278 selecciones, 64 dossiers, 214 selecciones sin dossier, 2.645 pantallas y 398 secundarios. La auditoría mecánica actual tiene 64 filas y 54 candidatos estáticos; en un contador distinto, 63 dossiers tienen presupuestos accesibles iguales entre dificultades. Ninguna cifra demuestra defectos o balance jugado. Hay 26 perfiles geográficos y 49 recursos de investigación; los ocho recursos modernos del Hiyaz y dos DSM de Jerusalén no resuelven la nota de cobertura de 22 identidades faltantes que afectan a 25 selecciones.

f00001/S2 fue implementado mecánicamente por `gpt-6-luna`, revisado por GPT-6 e integrado en `9d5e744b`. El veredicto formal integrado en `137fdd73` registra S2 `done` con revisión GPT-6, 3/3. El propietario asignó explícitamente a Luna este trabajo mecánico; no hubo compra de créditos ni generación pagada de medios. La integración no acredita ejecución nativa ni verificación en AoE2.

i00008/S1 está `done` tras revisión independiente de Luna (2/2); su matriz contiene 34 casos prospectivos. S2 está `done` con producto `6f06737` y veredicto `e08a5cb`; S3 está `done` con producto `c5533f7` y revisión integrada `3746e076`. La integración de S3 preservó entonces el corte existente de 63 filas y el despacho opt-in; tras la posterior inserción de dossier y regeneración, el informe actual contiene 64 filas y 54 candidatos. El mapper nativo sigue sin implementarse. Estas aceptaciones no acreditan herramienta de tiempos v3 ni desbloquean la autoría histórica.
