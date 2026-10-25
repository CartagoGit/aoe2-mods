# Reparto de trabajo y volumen pendiente

Corte: 25 de octubre de 2026. Instrucción del propietario: el arquitecto decide y revisa; delega recopilación y materialización a Luna o MiniMax según disponibilidad. Se trabaja en paralelo por paquetes cerrados. Este documento describe responsabilidades y evidencia, no implementa una cola: recuperar siempre el estado del DelendAI conectado y sus claims/unidades.

## Volumen de diseño histórico

| Odisea | Episodios seleccionados | Dossiers completos de diseño en borrador | Dossiers todavía por redactar |
|---|---:|---:|---:|
| Embers of the Covenant |30|30|0|
| The Eagle and the Cross |34|33|1|
| Keepers of the Unbroken Word |30|0|30|
| The Keys of the Eternal City |32|0|32|
| Beyond the Golden Gate |32|0|32|
| Beneath the Desert Stars |30|0|30|
| The Shattered Oath |28|0|28|
| From Damascus to the Far Horizon |32|0|32|
| The River Remembers |30|0|30|
| **Total** |**278**|**63**|**215**|

Los 63 borradores contienen 2.594 pantallas EN/es-ES y 391 secundarios. Siguen necesitando revisión histórica/editorial, terreno y calibración. No equivalen a 63 paquetes aprobados para autoría ni a escenarios jugados. El plan auxiliar de Constantinopla380 y su perfil candidato no incrementan esos totales. Hay cero aprobaciones ampliadas de juego.

Quedan 54 casos señalados por la auditoría cívica que requieren decisiones sobre dificultad/ritmo; no son 54 fallos de motor demostrados. Faltan 22 identidades geográficas en el registro para 25 selecciones. Los cuatro recortes DSM del Hiyaz aportan evidencia de relieve moderno, pero no incorporan esos cuatro perfiles ni certifican el paisaje antiguo. El manifiesto conserva 47 recursos locales, con 26 perfiles canónicos; no se suman imágenes como si fueran mapas jugables.

## Reparto por modelo

| Modelo/rol | Trabajo que conserva o recibe | Condición para darlo por terminado |
|---|---|---|
| gpt-6, arquitecto | Completar 215 dossiers, revisar 63 borradores, resolver 54 casos cívicos y 22 perfiles, cerrar historia, geografía, narración, pantallas, objetivos, dificultad y continuidad. Diseñar cualquier capacidad realmente ausente y supervisar los diffs delegados. | Paquete individual completo, operaciones disponibles en el contrato, evidencia atribuida y revisión independiente del alcance aprobado. Nunca aprobar su propia implementación. |
| gpt-6-luna, recopilación/materialización | Consultas acotadas con localizadores, inventarios, hashes, comparación de datos, borradores lingüísticos y código/fuentes cuando las decisiones estén cerradas. Puede implementar paquetes inicialmente previstos para MiniMax por autorización expresa del propietario. | Artefactos concretos, claims propios, checks pertinentes, límites registrados y revisión por un modelo distinto. No sustituye investigación por snippets ni decide arquitectura/historia para desbloquearse. |
| MiniMax M3.1, materialización | Recibir el próximo slice mecánico que el arquitecto asigne al recuperar cuota, después pilotos y los 278 episodios de 9 campañas de forma gradual. Comparte el pool de trabajo mecánico con Luna: un slice tiene un solo implementador activo. | Cumplir el paquete y aceptación oficiales, corregir hallazgos y pasar gate/revisión. Ninguna nueva decisión de mapa, economía, historia o contrato por su cuenta. |
| Revisor independiente | gpt-6 para entregas Luna/MiniMax; Luna para entregas gpt-6; GPT-6.1 cuando esté disponible y corresponda a una revisión asignada. Comprobar independencia real, diff, casos negativos y evidencia del commit exacto. | Veredicto formal correspondiente al slice y alcance, integrado por DelendAI. La existencia de un informe no cierra sola un slice. |

Estos son volúmenes de trabajo, no horas/costes medidos. El reparto no concede a MiniMax todo el backlog ni obliga a esperar al cierre de las nueve odiseas. Una implementación nativa todavía sin contrato/template/evidencia vuelve al arquitecto; no se oculta como tarea mecánica.

## Primera implementación delegada y aprendizaje observado

Luna materializó f00001/S2: los dos bundles del laboratorio ficticio, 17 catálogos draft por bundle y 36 claves runtime en total, dejando fuera 7 intenciones condicionales documentales. Producto integrado en `9d5e744b`; [revisión independiente](../qa/route-pilot/s2-source-bundle-independent-review.md). El veredicto gpt-6 se registró en `d29b751`; consultar el estado integrado antes de reclamar S3. La [enmienda de briefing](../wiki/route-pilot/17-briefing-binding-amendment.md) y su revisión están integradas en `c77052b2`.

1. **Omisión de especificación:** el inventario original no asignaba la intro de escenario obligatoria de T01. El arquitecto cerró la reutilización de la clave factual con ID de línea propio; no pidió al implementador inventar texto o alterar esquema. Las próximas revisiones de inventario comprueban todas las superficies obligatorias.
2. **Duración de lectura:** la implementación inicial daba 5 segundos también al resumen largo. Se corrigió con la estimación existente de 130 palabras/minuto sobre el máximo EN/es-ES, antes de integrar. Las próximas tareas reciben esa regla explícita, con tiempos estimados y pruebas nativas pendientes.
3. **Traducción acotada:** el lote se dividió en 8 locales y 7 locales entre agentes. Se comprobaron exactamente las 36 claves por locale y los textos EN/es-ES; el estado sigue draft. Ningún check sustituye revisión lingüística ni aprueba voces.
4. **Proveniencia:** snapshots automáticos de DelendAI conservaron archivos con autoría Git heredada. El implementador registró los hashes y su autoría real; no reescribió historia ni cambió configuración Git global/local.

La revisión independiente ejecutó ambos checks completos de staging y validate: 142 pruebas Bun, 2.069 aserciones, documentación/enlaces y campaña activa válidos. Se verificaron por separado las 14 duraciones, geometría/terminal del fixture y 36 claves. No se midió rendimiento de MiniMax: su lanzamiento real devolvió HTTP429/2056 sin ejecutar herramientas y la consulta MMX del 25 de octubre seguía indicando 0 % semanal general. No se compraron créditos. La asignación a Luna responde a la autorización posterior del propietario, no a una escalada automática oculta.

## Gates que siguen fuera de la mera autoría

Las capacidades nativas pendientes, plantillas reales, exportación soportada, carga en AoE2, rutas/huellas, guardado, progreso, presentación y calibración requieren sus evidencias propias. Pueden necesitar un tester con el juego disponible. La aprobación de textos en 17 idiomas y medios/voz conserva su revisión específica. No distribuir mods ni lanzar generación pagada masiva por completar un dossier o un piloto.

Para el próximo trabajo concreto, seguir la [cola de paquetes](MINIMAX-M3.1-PARALLEL-QUEUE.md), la [especificación del piloto](../wiki/route-pilot/02-implementation-specification.md) y las propuestas actuales. La planificación de i00008 y sus 34 casos son instrucciones de implementación pendientes, no un mapper ya construido ni el dossier 64.
