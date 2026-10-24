# Expediente de revisión de la arquitectura común

24 de octubre de 2026 · implementador `gpt-6` · d00002/S1. Base integrada examinada: `990cfe133a80016db957cc4ca46d976984130154`. Este expediente presenta evidencia al revisor independiente; no registra un veredicto ni modifica el estado de DelendAI.

## Qué debe decidir la revisión

La lectura del servidor en esta fecha conserva S1 pendiente y dos criterios:

1. «Plan explícito de nueve odiseas por actos y curva de dificultad, criterio de hito documentado sin relleno y límites históricos/licencias.»
2. «Investigación delegada contrastada por arquitecto; generadores comunes y validación de contratos sin clonar lógica por escenario.»

Se solicita evaluar la arquitectura editorial e instrumental común contra esos dos criterios. Las aprobaciones por campaña de S2–S10 y la consolidación de S11 siguen separadas. No se presenta la cobertura de enlaces como respaldo completo de 278 hechos, ni se pide aprobar los 215 expedientes que todavía no existen. El revisor debe señalar cualquier carencia común que impida cumplir S1; este documento no restringe su juicio ni sustituye la revisión oficial posterior a la integración.

## Plan, extensión y decisiones de los actos

El [plan de producción](../../design/odyssey-production-plan.md), la [política](../../design/odyssey-policy.json) y las [selecciones](../../design/odyssey-selections.md) fijan nueve odiseas y cinco actos por odisea. Las [45 fichas editoriales](act-editorial-review.md), con [IDs y fingerprints](act-editorial-review.json), concretan entrada, inflexión estructural, salida, presión/recuperación y diferencia exigida respecto de episodios vecinos.

| Odisea | Selecciones | Reparto de los cinco actos | Fuente editorial |
|---|---:|---|---|
| Embers of the Covenant | 30 | 8 / 7 / 6 / 6 / 3 | [faith-origins](../../design/odysseys/faith-origins.json) |
| The Eagle and the Cross | 34 | 6 / 6 / 7 / 6 / 9 | [imperial-church](../../design/odysseys/imperial-church.json) |
| Keepers of the Unbroken Word | 30 | 5 / 7 / 5 / 7 / 6 | [jewish-tradition](../../design/odysseys/jewish-tradition.json) |
| The Keys of the Eternal City | 32 | 6 / 6 / 6 / 7 / 7 | [church-of-rome](../../design/odysseys/church-of-rome.json) |
| Beyond the Golden Gate | 32 | 8 / 9 / 5 / 3 / 7 | [new-rome](../../design/odysseys/new-rome.json) |
| Beneath the Desert Stars | 30 | 7 / 7 / 7 / 5 / 4 | [first-caliphs](../../design/odysseys/first-caliphs.json) |
| The Shattered Oath | 28 | 5 / 6 / 5 / 7 / 5 | [first-fitna](../../design/odysseys/first-fitna.json) |
| From Damascus to the Far Horizon | 32 | 3 / 9 / 7 / 8 / 5 | [umayyads](../../design/odysseys/umayyads.json) |
| The River Remembers | 30 | 5 / 5 / 6 / 7 / 7 | [house-of-ali](../../design/odysseys/house-of-ali.json) |

Un hito cambia lugar, agentes, problema o consecuencia; dividir tres recados de una misma situación no produce tres misiones justificadas. La política prohíbe inventar batallas para cubrir cuotas y limita la repetición del núcleo mecánico; las fichas convierten ese límite en indicaciones particulares. Por ejemplo, la transmisión en Corinto y Éfeso debe cambiar recursos e identidades; la sucesión administrativa difiere del auxilio bajo asedio; una noticia de muerte fuera del mapa no coloca al personaje en el campo de batalla. Estas decisiones dirigen los expedientes del arquitecto. No son una prueba automática de interés ni eximen de rediseñar un episodio que resulte repetitivo.

Las cuotas ya coinciden con la pertenencia real de los actos. Ocho bandas temporales se ajustaron a fechas o variantes ya seleccionadas, sin cambiar episodios ni elegir entre cronologías disputadas. La [revisión independiente editorial](act-editorial-independent-review.md), integrada en `e70ace6d`, no dejó hallazgos P1/P2 abiertos y conserva las 21 correcciones explícitas de paginación de First Fitna. Su alcance fue ese componente, no el slice entero.

## Curva de dificultad y ritmo

Cada acto declara `difficultyCurve` para easy, standard y hard. Se comparte una escala inicial estimada de cinco actos, aplicada a la base que el arquitecto debe fijar por episodio. En hard, el multiplicador militar progresa de 0,90 a 1,10; easy amplía la ventana logística a 1,70 y la recuperación a 1,50 respecto de la base. Los valores enteros particulares del episodio prevalecen sobre el redondeo de la curva. El multiplicador militar sólo se usa cuando existe oposición declarada; nunca crea enemigos en un acontecimiento pacífico.

La escala compartida no pretende distinguir por sí sola las nueve experiencias. La dirección concreta está en `pressureAndRecovery` de cada ficha: preparación antes de extracción, alivio tras una crisis, cambio de logística a testimonio, o retirada cuyo éxito local conserva la derrota histórica. Una inflexión puede ser una pérdida o cambio de información; no tiene que ser el combate más difícil. La dificultad cambia presión, ventanas y margen de recuperación, sin alterar el desenlace histórico.

El [contrato de jugabilidad cívica](../../design/civic-playability-acceptance.md) exige decisiones y presión observables: menos trabajadores o más minutos no bastan. La [auditoría estática](civic-difficulty-mechanical-audit.json) conserva 54 candidatos a riesgo entre 63 borradores, sin declararlos divertidos ni fallidos por ese filtro. Las curvas siguen `pending cohort calibration`. S2–S10 deben convertirlas en presupuestos, distancias, secuencias y recuperación particulares y contrastarlas en mapas; s00001 aporta la evidencia del motor. Aprobar una arquitectura de curva no aprueba nivelación.

## Historia, narradores, continuidad y derechos

La [biblia de nueve narradores](../../design/voices/odyssey-narrators.json) conserva biografía ficticia, carácter, evolución y base de conocimiento por episodio. La voz común presenta contexto sobrio y atribuye las creencias; luego cede la palabra a la persona de campaña. Un archivo heredado no se vuelve recuerdo presencial y una narración partidista no altera el resumen factual. La ampliación de Marcus distingue los documentos anteriores a su nacimiento de la experiencia adulta.

El plan y el helper común de continuidad conservan campañas independientes: recomendación de predecesora, recapitulación, solapamiento cronológico explícito y elecciones acumulativas al final real. La indicación de continuación no bloquea una descarga ni lanza automáticamente otro mod. Las pantallas particulares y su materialización pertenecen a los expedientes y a las capacidades nativas.

La referencia del propietario al mod 550831 mantiene nombre y número como información suya: se obtuvo la página pública, pero el servicio de detalle devolvió 401 y no se inspeccionaron sus escenarios. No hay licencia de reutilización establecida. El [manifiesto de recursos](reference-manifest.json) y los [créditos](CREDITS.md) conservan los 37 recursos adicionales locales y sus usos de investigación; las 14 referencias anteriores permanecen separadas. Ni una ficha leída ni una imagen disponible conceden derechos de distribución. Las fotografías arqueológicas y DSM modernos no representan automáticamente el paisaje antiguo. No se ha distribuido un mod ni ejecutado generación pagada masiva.

## Investigación delegada y contraste del arquitecto

El [cruce reproducible](source-consultation-crosswalk.md) enlaza los 278 IDs a registros exactos, con punteros, localizadores, URL y hashes. Se conservan las recopilaciones originales y 118 referencias alternativas. La regla para elegir un registro principal resuelve identidad y procedencia; no puntúa verdad histórica. Las proyecciones incluyen 27 snapshots directos comprobados y cinco archivos principales de registros.

Hay 121 comprobaciones propias de acceso/alcance, 117 con algún pasaje y cuatro sólo fallidas. Se reutilizan 48 consultas acotadas. Otros 157 enlaces mantienen declaraciones archivadas sin comprobación nueva en el cruce; sus consultas anteriores y límites siguen visibles. No se afirma que estos números equivalgan a fuentes completas, hechos respaldados, lecturas distintas o aprobaciones. Son evidencia de qué contrastó cada agente y de qué sigue abierto.

Los [contrastes de first-caliphs](first-caliphs-source-contrast-checkpoint.md), [familia de Ali](ali-family-architect-source-contrast.md), [omeyas](umayyad-architect-source-contrast.md) y [final judío](jewish-finale-source-check.md) documentan límites y discrepancias: identificación del volumen de al-Tabari, paginación, fases de Bukhara, cronologías competidoras, interpretación de moneda, ausencia de pasaje recuperado o norma de 429 que no puede estar en una escena de 425. Se conserva el acceso fallido a Aqaba, Harra y Sijpesteijn. No se completan huecos inventando hechos, autenticidad de cartas, testimonios independientes ni voces antiguas.

La [revisión independiente del vínculo](research-linkage-independent-review.md), incluida en `990cfe13`, resolvió los 275 candidatos no islámicos y sus hashes y no dejó hallazgos P1/P2 abiertos. Tampoco aprobó S1 entero. El contraste de afirmaciones restantes, su decisión editorial por episodio y la revisión histórica de los expedientes siguen a cargo del arquitecto y revisor en S2–S10; MiniMax no recibe esa responsabilidad.

## Reutilización y comprobaciones

| Responsabilidad | Implementación compartida | Límite |
|---|---|---|
| Identidad y selección | [odyssey_catalog.helper.py](../../../tools/design/odyssey_catalog.helper.py), [odyssey_render.script.py](../../../tools/design/odyssey_render.script.py) | No seleccionan historia a partir de una cuota |
| Dossier y wiki derivados | [episode_dossier.factory.py](../../../tools/design/episode_dossier.factory.py), [episode_dossiers.script.py](../../../tools/design/episode_dossiers.script.py) | Requieren decisiones explícitas del autor; no producen mapas nativos |
| Predicados, identidad, recepción, pagos y causalidad | [episode_dossier.validator.py](../../../tools/design/episode_dossier.validator.py) | Contrato de diseño; las capacidades nativas tienen propuesta propia |
| Secundarios, costes, reservas y recompensas | [secondary.py](../../../tools/design/secondary.py), [optional_design.script.py](../../../tools/design/optional_design.script.py) | Seis a ocho tareas particulares, cuatro mecánicas y tres planes; éxito principal solvente al ignorarlas |
| Entrada y final | [odyssey_continuity.helper.py](../../../tools/design/odyssey_continuity.helper.py) | Identidad estable y recomendación no bloqueante; no acredita menú o variables en AoE2 |
| Narradores y asignaciones | [odyssey_narrators.validator.py](../../../tools/design/odyssey_narrators.validator.py), [odyssey_assignments.validator.py](../../../tools/design/odyssey_assignments.validator.py) | Valida vínculos y contratos; no mide calidad literaria |
| Procedencia de investigación | [research_crosswalk.validator.py](../../../tools/design/research_crosswalk.validator.py), [research_crosswalk.script.py](../../../tools/design/research_crosswalk.script.py) | Ruta confinada, bytes y snapshots directos declarados; no aprobación histórica ni recorrido recursivo de dependencias |
| Presión y análisis finito | [civic_difficulty_audit.script.py](../../../tools/design/civic_difficulty_audit.script.py), [finite_allocation.helper.py](../../../tools/design/finite_allocation.helper.py) | Aritmética y observaciones artificiales, sin afirmar juego probado |

Los autores aportan hechos, grupos, destinatarios, costes, fases y texto EN/es-ES; los helpers construyen identidades, ledgers, reservas y representación de forma común. No se clona un motor de misión por escenario. Los módulos TypeScript siguen responsabilidad/tipo, importación concreta y ausencia de barrels conforme a la norma del proyecto. El material de investigación no reimplementa DelendAI.

En el componente integrado `990cfe13`, `bun run validate` pasó por el gate oficial contra `e70ace6d`: instalación congelada y validación completa. En su candidato, el implementador pasó 142 pruebas de código/2.069 aserciones y 82 de diseño; GPT-6.1 repitió la validación y las 13 regresiones focalizadas de procedencia. Las regresiones rechazan snapshots cambiados detrás de una proyección actualizada, rutas/duplicados inválidos y symlinks externos aun con hash coincidente. Los informes de cada componente conservan comandos, versiones revisadas y resultados. No se modificó el adaptador ni se atribuyen nuevas pruebas de exportación o motor.

## Frontera de la entrega

El catálogo conserva 63 borradores ampliados, 2.594 pantallas bilingües, 391 secundarios y 215 selecciones sin dossier. No hay aprobación ampliada histórica/geográfica/jugada. El próximo expediente imperial es Constantinopla 380, orden 33, todavía con brief y estudio de alternativas, sin dossier completo.

Una eventual aprobación formal de S1 sólo satisfaría esa dependencia de planificación. No aprueba automáticamente S2–S10/S11, i00003 nativo, i00007/S3 ni s00001; tampoco permite a MiniMax diseñar o materializar episodios históricos bloqueados. Su primera tarea designada sigue siendo f00001/S1 al recuperar el estado vivo del servidor. El arquitecto continuará los expedientes y la geografía y resolverá los hallazgos de la revisión independiente.
