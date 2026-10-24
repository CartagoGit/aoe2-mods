# Vínculo de investigación de las 278 selecciones

24 de octubre de 2026 · `gpt-6` · componente d00002/S1, pendiente de revisión independiente e integración. No aprueba S1 entero.

## Resultado y reutilización

El [cruce existente](source-consultation-crosswalk.md) enlaza las nueve campañas y 278 IDs semánticos. Se conservan sus 30 registros anteriores de first-caliphs íntegros. Las proyecciones añaden 58 registros de las recopilaciones de la familia de Ali, 32 omeyas, 157 auditorías cristianas/judías previas y un nuevo registro del final judío. No se cambia una selección, fuente canónica, fecha, contrato, objetivo, narrador, rango de cadenas, geografía o identidad para obtener cobertura. Las proyecciones son instantáneas de declaraciones, no nuevos hechos históricos.

Luna recopiló las 32 selecciones omeyas en su unidad oficial separada. El arquitecto incorporó su commit `6a304f24b18ec2144467eb14b28d708751549ce8`. Otro trabajo de Luna, de solo lectura y sin unidad, localizó 275 candidatos de identidad exacta para 157 selecciones de las cinco campañas no islámicas. Root comprobó cada identidad, URL, localizador y SHA contra sus bytes originales. Se conservaron 118 alternativas y 22 snapshots de origen. El primer inventario omitía alias explícitos como `consultedUrl` y confundía punteros de raíz; esas omisiones se corrigieron antes de producir el archivo incorporado. El puntero JSON raíz es vacío, no `/`, y los punteros de campos anidados no llevan una barra adicional. Ningún archivo de investigación original fue reescrito.

La elección del registro principal prefiere `consultedUrl` explícito; después una URL canónica exacta entre candidatos de la misma identidad; después conserva el candidato del inventario. Es una regla de enlace, no un ranking de validez. Las referencias alternativas permanecen. Una autoría o fecha no declarada sigue siendo desconocida; `consulted: false`, un locator o la etiqueta genérica de consulta no se convierten en lectura completa. Las fechas y lugares de diseño se copian únicamente como contexto canónico, marcado como tal.

Las proyecciones usan el contrato ya existente del cruce. Para evitar que un hash nuevo de proyección oculte cambios de sus entradas, `checked_archive` comparte las comprobaciones previas de ruta/bytes y el validador aplica las mismas a cada snapshot directo declarado. No se emula DelendAI ni se crea un sistema de aprobación. La revisión de exactitud semántica de la proyección permanece responsabilidad del autor/revisor; un hash no decide si una afirmación histórica es verdadera.

## Lecturas nuevas, cautelas y huecos

Hay 121 comprobaciones de acceso/alcance: 117 con algún pasaje y cuatro sólo fallidas. Otras 157 declaraciones archivadas no reciben lectura nueva del arquitecto en el cruce. Se reutilizan 48 consultas acotadas; no equivalen a 121 fuentes distintas ni a 117 episodios respaldados por completo. Los pasajes pueden ser parciales, irrelevantes para un detalle o contradictorios. La revisión histórica de campaña permanece separada.

Los [20 contrastes omeyas](umayyad-architect-source-contrast.md) no afirman lectura de libros completos, crónicas árabes, inscripciones o todo el aparato crítico. Se conservan los fallos de Birzeit y Sijpesteijn. El volumen XVIII de al-Tabari no abarca los años 81–82; XXIII es una pista de catálogo y no el pasaje leído de Dayr al-Jamajim. La cronología recuperada no expone el locator 685 seleccionado; sus resúmenes 693/696 no justifican sustituir silenciosamente 694 ni las fases de la moneda. El inicio público del año 65 en XX no es la reunión de Jabiya. La mezquita de Bukhara sí tiene un párrafo recuperado después por root en la página 3 del PDF; eso no verifica asistencia forzada ni el plano original. Kufa conserva relatos de octubre/noviembre 749 distintos, y Marv distingue propaganda de captura.

El [final judío](jewish-finale-source-check.md) registra la ausencia inicial de auditoría propia y la consulta limitada posterior. UNESCO da contexto patrimonial; no fecha la desaparición del patriarcado ni el cierre del Talmud en 425. La cláusula fiscal de 429 es retrospectiva, no un documento disponible en una escena de 425. No se traslada la vida de Judá el Príncipe al final del arco. Se conserva el límite editorial y la necesidad de investigación/dossier.

Las [correcciones de paginación de First Fitna](ali-family-architect-source-contrast.md#pagination-correction-after-independent-review) siguen explícitas y no alteran los bytes de Luna. El intento fallido del volumen XVII no se atribuye como lectura nueva de root. No se descarga un libro moderno ni se concede una licencia de imágenes por leer una ficha.

## Comprobación y siguiente trabajo

Las tres regresiones nuevas exigen detectar cambios de una entrada aun con el hash de la proyección actualizado, rechazan snapshots malformados/duplicados/rutas fuera de investigación y un symlink externo con bytes coincidentes. Las 13 pruebas focalizadas pasan. Los resultados completos y la revisión independiente se registrarán antes de integrar el candidato. No hay cambios del adaptador ni nuevas pruebas de exportación o motor atribuidas a este componente.

La cobertura de vínculos no cierra los juicios históricos/editoriales de S1 ni los dossiers S2–S10. El catálogo conserva 63 borradores, 215 selecciones sin dossier, 2.594 pantallas y 391 secundarios. La dificultad, el relieve/huellas históricos, las capacidades nativas y las pruebas en AoE2 siguen sus gates. MiniMax histórico continúa bloqueado; su primera tarea designada sigue siendo f00001/S1 al recuperar el estado vivo.


Comprobación del candidato `0bbcb24`: `bun run validate` exit0 (142 pruebas, 2.069 aserciones; suite Bun24,62s; tipado/lint, documentos/enlaces y campaña técnica válidos). Las 82 pruebas de diseño pasaron en29,115s y las 13 focalizadas en0,178s. La comprobación adicional conserva íntegros los 30 bindings/18consultas originales y los nueve JSON canónicos byte a byte frente a `e70ace6d`; todos los fingerprints de snapshots coinciden. Los ajustes posteriores de presentación Markdown requieren el gate final de publicación y revisión independiente; no alteran datos o lecturas.
