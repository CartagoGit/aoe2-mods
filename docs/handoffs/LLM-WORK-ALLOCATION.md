# Reparto de trabajo y volumen pendiente

Corte: 25 de octubre de 2026. Instrucción del propietario: el arquitecto decide y revisa; delega recopilación y materialización a Luna o MiniMax según disponibilidad. Se trabaja en paralelo por paquetes cerrados. Este documento describe responsabilidades y evidencia, no implementa una cola: recuperar siempre el estado del DelendAI conectado y sus claims/unidades.

## Volumen de diseño histórico

| Odisea | Episodios seleccionados | Dossiers completos de diseño en borrador | Dossiers todavía por redactar |
|---|---:|---:|---:|
| Embers of the Covenant |30|30|0|
| The Eagle and the Cross |34|34|0|
| Keepers of the Unbroken Word |30|0|30|
| The Keys of the Eternal City |32|0|32|
| Beyond the Golden Gate |32|0|32|
| Beneath the Desert Stars |30|0|30|
| The Shattered Oath |28|0|28|
| From Damascus to the Far Horizon |32|0|32|
| The River Remembers |30|0|30|
| **Total** |**278**|**64**|**214**|

Los 64 borradores contienen 2.645 pantallas EN/es-ES y 398 secundarios. Siguen necesitando revisión histórica/editorial, terreno y calibración. No equivalen a paquetes aprobados para autoría ni a escenarios jugados. Constantinopla380 (ID 34, orden 33) forma parte de esos totales; su plan de mundo y perfil de referencia son materiales auxiliares, no mapas jugados. Hay cero aprobaciones ampliadas de juego.

El informe mecánico cívico actual tiene 64 filas y 54 candidatos estáticos; en una métrica distinta, 63 filas muestran el mismo presupuesto accesible entre dificultades. Requieren decisiones sobre dificultad/ritmo, pero no son fallos de motor demostrados. La nota de cobertura geográfica conserva 22 identidades pendientes para 25 selecciones. Los cuatro recortes DSM del Hiyaz y las dos referencias DSM modernas de Jerusalén aportan datos modernos, no perfiles antiguos ni mapas jugables. El manifiesto registra 49 recursos locales y `geography.json` 26 perfiles canónicos.

## Reparto por modelo

| Modelo/rol | Trabajo que conserva o recibe | Condición para darlo por terminado |
|---|---|---|
| gpt-6, arquitecto | Completar 214 dossiers, revisar los 64 borradores, resolver los 54 candidatos estáticos señalados por el informe cívico actual y las 22 identidades de cobertura, cerrar historia, geografía, narración, pantallas, objetivos, dificultad y continuidad. Diseñar cualquier capacidad realmente ausente y supervisar los diffs delegados. | Paquete individual completo, operaciones disponibles en el contrato, evidencia atribuida y revisión independiente del alcance aprobado. Nunca aprobar su propia implementación. |
| gpt-6-luna, recopilación/materialización | Consultas acotadas con localizadores, inventarios, hashes, comparación de datos, borradores lingüísticos y código/fuentes cuando las decisiones estén cerradas. Puede implementar paquetes inicialmente previstos para MiniMax por autorización expresa del propietario. | Artefactos concretos, claims propios, checks pertinentes, límites registrados y revisión por un modelo distinto. No sustituye investigación por snippets ni decide arquitectura/historia para desbloquearse. |
| MiniMax M3.1, materialización | Recibir el próximo slice mecánico que el arquitecto asigne al recuperar cuota, después pilotos y los 278 episodios de 9 campañas de forma gradual. Comparte el pool de trabajo mecánico con Luna: un slice tiene un solo implementador activo. | Cumplir el paquete y aceptación oficiales, corregir hallazgos y pasar gate/revisión. Ninguna nueva decisión de mapa, economía, historia o contrato por su cuenta. |
| Revisor independiente | gpt-6 para entregas Luna/MiniMax; Luna para entregas gpt-6; GPT-6.1 cuando esté disponible y corresponda a una revisión asignada. Comprobar independencia real, diff, casos negativos y evidencia del commit exacto. | Veredicto formal correspondiente al slice y alcance, integrado por DelendAI. La existencia de un informe no cierra sola un slice. |

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
