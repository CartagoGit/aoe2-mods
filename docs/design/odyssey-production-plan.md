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

A 15 de octubre de 2026, la selección contiene **278 episodios** y **305 slices de autoría**: 278 individuales y 27 de conformidad, metadatos y promoción. Hay **60 dossiers redactados**, **2.469 pantallas EN/es-ES** y **370 secundarios**; quedan **218 selecciones sin dossier** y no hay dossiers ampliados aprobados. El catálogo anterior conserva sus 39 identidades, 1.496 pantallas y claves de progreso.

| Odisea | Dossiers / selección | Órdenes con dossier | Pendiente del arquitecto |
|---|---:|---|---|
| Embers of the Covenant | 30 / 30 | 1–30 | Revisión histórica/editorial, relieve y huellas, capacidades nativas, jugabilidad y dificultad |
| The Eagle and the Cross | 30 / 34 | 1–28, 32, 34 | Dossiers de los órdenes 29–31 y 33; los mismos gates históricos, geográficos, nativos y de juego |
| Otras siete odiseas | 0 / 214 | Ninguno | Interpretación de fuentes recopiladas y diseño completo por episodio |

Las nueve biblias de narrador fijan biografía ficticia, cinco actos y acceso al conocimiento por episodio en [su fuente canónica](voices/odyssey-narrators.json). Los 34 recursos locales adicionales del [manifiesto](../research/odyssey-research/reference-manifest.json) tienen procedencia; ninguno acredita por sí solo una escena histórica ni arte de producción. La referencia Bernard Nolan continúa sin escenarios descargados o licencia de reutilización acreditada.

## Cobertura imperial y trabajo designado

La [enmienda](imperial-coverage-amendment.md) se integró oficialmente en `8a37f763d1b0e5b2bb1866131c45636bb5c1f283`. Su [revisión técnica independiente](../qa/campaign-design/imperial-coverage-migration-independent-review.md) verificó conservación de IDs/progreso/frontmatter, 278 selecciones y la corrección del bypass por etiqueta de scope. No aprueba los nuevos hechos históricos ni cierra d00002.

Los IDs nuevos 30/31/32/33/34 se presentan en los órdenes 28/29/30/31/33, slices S33/S34/S35/S36/S37. Los antiguos IDs 28/29 son ahora órdenes 32/34 y conservan S31/S32. Después de S30 se ejecuta S33→S34→S35→S36→S31→S37→S32; promoción S6 depende del último S32. El concilio381 sigue siendo el único final imperial. [Asignaciones](../handoffs/MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md) conserva la matriz de las nueve campañas.

*Beyond the Quiet River*, orden28, añade una red local ficticia en Alejandría365–366: seis voluntarios originales, cualquier mínimo simultáneo de cuatro en sus puestos asignados y un recadero distinto con salida causal. Tres lotes tienen reparto2/1; los pagos suman380F240W. Siete secundarios se pueden omitir. La presencia se comprueba al completar o2 y o3; no se congela a los primeros cuatro ni se exige residencia continua. El New River y la villa no se localizan. La crónica, los meses históricos y la carta/regreso permanecen separados del trabajo jugable. Su revisión independiente está pendiente.

Los siguientes dossiers son la sucesión alejandrina convencionalmente fechada373 (con sincronismo contradictorio en Sócrates), la derrota de Adrianópolis378, la reorganización de Sirmio379 (día de acceso sin resolver) y las transferencias urbanas de noviembre380. Sirmio tiene perfil regional y dos fotografías arqueológicas modernas: no identifican el lugar de proclamación ni la hidrología de379. Ninguna selección sustituye un dossier completo.

## Jugabilidad cívica y dificultad

La [auditoría mecánica](../research/odyssey-research/civic-difficulty-mechanical-audit.json) identifica 54 candidatos a riesgo entre 60 dossiers: no tienen hostiles/plazo estructurados y el stock accesible es igual en las tres dificultades. Es un filtro estático, no una prueba de falta de interés. Los otros seis tampoco tienen balance jugado aprobado. Se aplica el [contrato de aceptación cívica](civic-playability-acceptance.md): menos trabajadores o más minutos no bastan para aprobar dificultad. El arquitecto conserva los cambios de economía, distribución, objetivos y ritmo; MiniMax no resuelve esas decisiones.

## Capacidades y continuidad que siguen gobernando la entrega

- i00003/S1 implementa la referencia de fases, recibos, derivaciones financiadas y salidas causales; los observadores/materialización nativa y QA del motor siguen pendientes. Una conjunción final no autoriza fabricar antes de recoger y pagar.
- i00005/S1 está formalmente revisado e integrado en `d793ae4`, con corrección `983ef905`; S2/S3 siguen pendientes. Milán350 y la red alejandrina365 requieren presencia actual: una entrega pasada no prueba residencia. No reemplazarla por temporizador, flag arrived ni actor inmovilizado.
- Los manifiestos fluviales de las batallas324 y los riesgos ambientales de faith-origins15 siguen declarando capacidad pendiente. No usar llegada geométrica para fingir embarque, tránsito o desembarque.
- Cada final espera una elección válida antes de victoria, escribe solo su clave acumulativa y preserva las anteriores. Las sucesoras muestran título/ID y advertencia cronológica; recomendación de predecesora, recapitulación y comienzo independiente siguen obligatorios. Variables/menús/audio nativos y guardado/carga requieren evidencia propia.
- Las pruebas estáticas, round-trip y revisiones acotadas se documentan con su hash y alcance. Ninguna acredita terreno antiguo, navegación, voces auténticas, balance jugado o una campaña completa.

El [registro histórico](../qa/campaign-design/odyssey-design-progress-history.md) conserva los cortes anteriores y sus cautelas; sus números no son el estado actual. d00002/S1–S11 continúa abierto según DelendAI. El traspaso histórico a MiniMax sigue bloqueado hasta cerrar cada requisito que le corresponda.
