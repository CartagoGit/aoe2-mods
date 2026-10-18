# Revisión técnica independiente de padding y visibilidad de criterios

Revisión acotada del candidato `d60694a` (incluye `fb879a9` y `d60694a`) sobre `d71a61d06f118c980b0f91a6a348b13cb16d992b`. Revisor: `gpt-6-luna`. No es aprobación formal de `d00002/all`, ni certificación histórica, de navegación o de juego.

## Resultado

No encontré bloqueantes en los cambios revisados. `clipped_tile_segments` mantiene el bbox original como proyección y recibe un `clip_bbox` opcional para seleccionar el viewport. El renderer obtiene ese viewport del `geographic_frame` común (`bounds_at(0, size - 1)`) y lo aplica a las capas geográficas y al control de agua; no recalcula hubs, corredores, dossiers ni mapa. El modo legado conserva el redondeo por defecto de seis decimales, y el modo de viewport explícito pide intersecciones sin redondeo prematuro. La prueba exacta comprueba ambos modos; la prueba de padding cubre una línea contenida solo en el margen y otra que atraviesa el borde completo.

Revisé y rendericé antes/después de Corinto y Tesalónica. En ambos resultados, las líneas antes cortadas siguen visibles por el margen hasta el borde del marco; los hubs y rutas permanecen en la misma ubicación. `python3.10 tools/design/episode_dossiers.script.py --check` reproduce correctamente los SVG comprometidos: 47 archivos. No cambió ningún JSON, lock de cadenas ni mapa de la línea base fuera del directorio `odyssey`; los archivos fuente de campaña y sus blueprints no aparecen en el diff.

El segundo commit elimina exclusivamente dos líneas en blanco que interrumpían el bloque indentado `acceptance` de la propuesta. El diff no cambia metadatos, estados, dependencias ni texto de criterio. La llamada al parser real instalado `parseProposalSlicePlan` sobre el archivo candidato devuelve cuatro criterios para S3 y tres para S4, incluidos reloj relativo y control de entradas antes del briefing. La API viva de DelendAI todavía devuelve 3/2; esto es el estado prepublicación esperado y la confirmación de servidor después de integrar sigue pendiente.

## Verificación ejecutada

- `python3.10 tools/design/test_design.py`: 66 tests correctos.
- `python3.10 tools/design/episode_dossiers.script.py --check`: 63 dossiers verificados, sin aprobación histórica/nativa afirmada.
- `bun run validate`: check, 108 tests Bun / 426 expectativas, documentación y validación de campaña correctos.
- Revisión visual antes/después de los SVG de Corinto y Tesalónica; `git diff --check` limpio.
- Parser real instalado: aceptación S3/S4 local 4/3; API online consultada antes de publicación: 3/2.

Estos cambios aumentan la visibilidad de controles esquemáticos/modernos y los criterios pendientes; no certifican cobertura de datos, costa antigua, navegación ni operación nativa. El perfil y la navegación histórica siguen sujetos a revisión y confirmación del runtime.
