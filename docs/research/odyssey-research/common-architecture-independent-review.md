# Arquitectura común de odiseas: revisión independiente integral

24 de octubre de 2026 · revisor `gpt-6.1-sol` · d00002/S1.

Unidad oficial `wip/gpt-6.1-sol/review/d00002-S1-g5/common-architecture-independent-review`, sesión propia servida `89db9473`. Base integrada `990cfe133a80016db957cc4ca46d976984130154`; candidato inicial `2b42d766d4fb2297918908dbdbc1e46b66857fe2`. Sólo este informe está editado por el revisor. Se recuperaron overview, catálogo y criterios vivos; S1 seguía pendiente y la cola no contenía una entrega formal para dictamen.

**Conformidad técnica integral con los dos criterios comunes de S1; sin hallazgos P1/P2 abiertos.** Los dos P2 encontrados se corrigieron y comprobaron independientemente. No es todavía una aprobación formal ni una entrega por cuenta del implementador. La corrección examinada es `1290bdf58148da7a246be29eb328d8905c3e5067`; su diff agrega un helper y adapta cinco módulos/pruebas, sin cambiar datos canónicos, fuentes, IDs, fechas, contratos de campaña ni adaptador. El candidato final `f71c43496f8260428353705d9205198aec092a0d` añade únicamente once líneas al expediente de aceptación para registrar las correcciones y los resultados del implementador; leí ese diff y es coherente con la evidencia.

## Criterios completos de S1

1. «Plan explícito de nueve odiseas por actos y curva de dificultad, criterio de hito documentado sin relleno y límites históricos/licencias.»
2. «Investigación delegada contrastada por arquitecto; generadores comunes y validación de contratos sin clonar lógica por escenario.»

La revisión abarca ambos criterios y el cuerpo integrado que los sustenta, además del diff del expediente actual. No se limita al resumen del implementador ni a las anteriores revisiones parciales.

## Plan y límites editoriales

Contrasté [plan](../../design/odyssey-production-plan.md), [política](../../design/odyssey-policy.json), [selecciones](../../design/odyssey-selections.md), nueve archivos canónicos y [fichas de acto](act-editorial-review.json). Recomputé nueve campañas, 45 actos, 278 selecciones y los nueve repartos exactos de cuotas. Los nueve hashes de campaña de las fichas coinciden con sus bytes; los 135 IDs de entrada, inflexión y salida existen en el acto correspondiente. Las 45 fichas contienen intención, presión/recuperación y una diferencia particular exigida respecto de las misiones vecinas.

La escala militar compartida de cinco actos y los márgenes de logística/recuperación son hipótesis iniciales explícitas, no nueve curvas medidas. Las fichas concretan preparación, crisis, descanso, transmisión o retirada; una inflexión no obliga a inventar combate. La regla de hito exige cambio de lugar, agentes, problema o consecuencia y prohíbe dividir recados para cubrir cuotas. Las cuotas, identidad previa, asociación de actos y repetición mecánica tienen comprobaciones comunes; la calidad particular y la diversión requieren juicio y partidas posteriores.

El [contrato cívico](../../design/civic-playability-acceptance.md) exige decisiones y recuperación observables. Sus 54 candidatos a riesgo estático entre 63 borradores no se presentan como prueba de aburrimiento ni de nivelación. El plan conserva desenlaces documentados, personas ficticias situadas, narración común de hechos y límites de conocimiento. La continuidad recomienda otras campañas sin bloquear acceso, borrar claves acumulativas o lanzar automáticamente un mod.

El manifiesto de investigación y [créditos](CREDITS.md) separan 37 recursos adicionales de las 14 referencias anteriores y mantienen su aprobación de producción pendiente. Licencia de una descripción no licencia todas sus imágenes; fotografías modernas, restauraciones y capas actuales no representan automáticamente la antigüedad. La referencia al mod 550831 conserva acceso público parcial y ausencia de licencia de reutilización establecida. No se inspeccionó ni volvió a consultar ese mod durante esta revisión.

El primer criterio común queda cubierto con estos límites. Aprobar una arquitectura de dificultad no aprueba los presupuestos ni mapas particulares.

## Contraste y reutilización

Revisé la cadena de recopilaciones delegadas, contrastes del arquitecto, proyecciones fechadas y [cruce de procedencia](source-consultation-crosswalk.md). Sus 278 vínculos conservan identidad, punteros, localizadores, hashes y 118 alternativas; 121 comprobaciones de acceso/alcance, 117 con algún pasaje, cuatro sólo fallidas y 48 consultas reutilizadas no equivalen a 278 afirmaciones históricas aprobadas. Los 157 vínculos archivados sin contraste nuevo no implican que nunca se consultaran. Permanecen atribución desconocida donde corresponde, lecturas parciales, fallos de acceso y correcciones explícitas, incluidas las 21 páginas de First Fitna.

Las propias lecturas acotadas de fuentes y recomputaciones de los componentes anteriores constan en [contraste de first-caliphs](first-caliphs-source-contrast-independent-review.md), [actos](act-editorial-independent-review.md) y [vínculo completo](research-linkage-independent-review.md). Aquí revisé su integración y límites; no atribuyo nuevas lecturas completas de libros, textos árabes, manuscritos o los 278 hechos. Las discrepancias documentadas —Hormozan, fases de Alejandría, volúmenes de al-Tabari, Bukhara, cronologías de 749 y norma de 429 frente a escena de 425— demuestran contraste efectivo y seguimiento, sin convertir las fuentes insuficientes en respaldo.

Inspeccioné los módulos comunes de selección/render, fábrica de dossiers, predicados, secundarios, continuidad, narradores, asignaciones, referencias, cruce, presión cívica y análisis finito. Los autores aportan hechos, decisiones, identidades de grupos, destinatarios, costes y texto; una fábrica construye contratos y representaciones. Los helpers de continuidad y secundarios se reutilizan; el renderer deriva wiki y planos. No hay un motor clonado por escenario ni generación nativa encubierta. Los validadores no sustituyen a DelendAI ni emiten aprobaciones históricas.

Las regresiones comunes cubren identidad previa, cuotas, variedad, conocimiento del narrador, traducción/pantallas, causalidad de recogida/pago/derivación, familias exactas, receptores, continuidad, reservas, procedencia, rutas y capacidades pendientes. El gate de documentación ejecuta `render.py --check`, `verify.py` y `test_design.py`, además de enlaces locales. Encontré dos huecos numéricos que impedían dar por cerrado el segundo criterio antes de su corrección.

## Hallazgos reproducidos

**P2-1: umbrales vacíos o no enteros.** En una copia temporal de `faith-origins`, episodio `01-administrative-records-caesarea`, cambié sólo `objectivePlan[0].predicate.requirements[0].requiredCount` a `0`, `-1`, `true` y `0.5`. `audit_dossier` devolvió `[]` en los cuatro casos. La recogida obligatoria podía quedar vacía o usar fracciones/booleanos. El primer secundario `entity-arrival` del mismo episodio admitía los mismos valores. El validador legado `check_objectives`, `01-roads-of-antioch/main-entities`, también admitía `true` y `0.5`. Se requiere un entero positivo sin coerción booleana antes de comparar tamaños, incluyendo presencia, área, ledgers y supervivencia.

**P2-2: asignación de recursos inválida con suma conservada.** En `11-distributed-preservation-ephesus`, el pago principal de 80 de madera admitía asignaciones de `-1/81`, `true/79` y `0.5/79.5` a sus dos receptores; `audit_dossier` devolvía `[]` aunque la suma coincidiera. Añadir una clave `unknown=999` a `amounts` y una asignación también se ignoraba. La conservación de la suma no valida débitos individuales. Se requieren vectores de recursos canónicos, cantidades enteras no negativas y rechazo de claves desconocidas antes de la aritmética, compartiendo la regla ya existente en el análisis finito.

Estas reproducciones usaron copias en memoria; no se alteraron implementación, datos canónicos ni pruebas por el revisor. El implementador recibió ambos hallazgos antes del informe final.

**Cierre de ambos P2 en `1290bdf`.** Leí el helper puro `design_numbers.helper.py`, las llamadas desde dossiers, contratos legados y secundarios, la reutilización del validador de recursos por `finite_allocation.helper.py` y las ocho nuevas regresiones. Los umbrales requieren `type(value) is int` y valor positivo antes de comparaciones dependientes; incluyen tipos de presencia/área/transporte, contadores opcionales, distribución, ledger y supervivencia. Los vectores rechazan tipos/coerciones, cantidades negativas y claves ajenas a los cuatro recursos, incluyendo asignaciones, recibos, mínimos de stock, totales compuestos, recompensas y presupuestos. La extracción conserva la regla del análisis finito, sin copia divergente ni dependencia circular.

Repetí independientemente todos mis casos originales: cada umbral principal/opcional de `0`, `-1`, `true` y `0.5`, los dos umbrales legados, las tres asignaciones de suma conservada y la clave desconocida son rechazados. También comprobé rechazo de `false`, `1.0`, infinito, NaN, `null`, texto y negativos en recursos. El entero positivo mínimo `1`, los vectores vacíos y la cantidad explícita cero siguen admitidos donde corresponden. No quedan hallazgos P1/P2 abiertos. El segundo criterio común queda cubierto tras estas correcciones.

## Verificación propia y alcance del dictamen

`bun run validate` sobre `2b42d76` terminó con salida 0: 142 pruebas Bun, 2069 aserciones, suite Bun de 30,45 s, tipado/lint, render/validación/regresiones de diseño, documentación/enlaces y una campaña válidos. Registro temporal: `/tmp/common-architecture-independent-validate.log`. El éxito inicial no detectaba los dos huecos adversariales anteriores.

El gate propio final `bun run validate` sobre `1290bdf`, con el borrador de este informe presente, terminó con salida 0: 142/142 pruebas Bun, 2069 aserciones, suite Bun de 29,40 s, tipado/lint, render/validación y las 90 regresiones actuales de diseño, documentación/enlaces y una campaña válidos. Registro temporal: `/tmp/common-architecture-independent-validate-final.log`. Después sólo se integró el diff Markdown de `f71c434` y se finalizó este informe; sus enlaces locales se comprobaron sin repetir pruebas pesadas ante cambios exclusivamente de prosa. La publicación oficial deberá validar el merge exacto que integre ambos documentos.

S1 sólo establece la arquitectura editorial e instrumental común. Los 63 dossiers, 2594 pantallas y 391 secundarios siguen borradores; las 215 selecciones sin dossier corresponden a S2–S10. No se imponen 157 lecturas nuevas para cambiar un contador ni se confunde trazabilidad con respaldo. La historia y geografía particulares, presupuestos, arte, derechos de distribución, huellas, navegación, cohortes, juego y materialización nativa mantienen sus puertas propias. No hubo cambio del adaptador ni nuevas pruebas de exportación; no se afirma evidencia de juego.

Un dictamen formal sobre S1 requerirá integración oficial de la corrección y este informe, entrega del implementador y evidencia exacta ligada al hash integrado. No corresponde cerrar S2–S11, i00003, i00007/S3, s00001 ni autorizar producción histórica por MiniMax desde este informe.
