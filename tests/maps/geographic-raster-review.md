# Revisión técnica independiente del raster geográfico

Revisión acotada de código para `i00003/S2`, candidato exacto `6d8bca8026076f3f583a4ce243b2e6838736b246` (incluye `8276456` y la corrección posterior). Revisor: `gpt-6-luna`. No es aprobación de S2 completo ni revisión histórica, de transporte nativo o de juego.

## Resultado

No encontré bloqueantes en el componente revisado. El helper conserva la proyección directa existente en `tools/design/geography.py`, y las pruebas verifican ida/vuelta en orientación norte-arriba, límites de centros y celdas, plano sintético y cobertura. El compilador requiere EPSG:4326, datum vertical y unidades métricas explícitos; acepta únicamente valores finitos o `null`; interpola bilinealmente en centros de muestra y falla ante nodata con peso, cobertura exterior o extrapolación. El ajuste de índices a enteros dentro de `1e-7` evita peso espurio por redondeo cerca de un centro exacto; el test nuevo conserva el valor válido aunque el vecino de peso cero sea nodata. El umbral equivale a una fracción minúscula de píxel y no es gap filling.

El control de finitud antes de serializar evita introducir un resultado no finito. El CLI comprueba el hash SHA-256 de los bytes de la fuente citada, restringe la fuente y el aviso de licencia al proyecto, y copia ese aviso al candidato. Es correcto que el CLI no afirme que verificó la extracción: `sourceSampleExtractionVerified` permanece `false`. La lógica y los tests son compatibles con Python 3.10; ejecuté la suite con `python3.10`.

## Verificación ejecutada

- `python3.10 tests/maps/test_geographic_raster.py`: 6 tests correctos.
- `bun test tests/maps/geographic-raster.test.ts`: 1 test, 2 expectativas correctas.
- `bun run validate`: `check`, 108 tests Bun / 426 expectativas, `docs:check` y `campaign:validate` correctos.
- Ejecuté el CLI con la cuadrícula DSM real a 400×400: cobertura completa; rango de salida 34.881202–38.48747 m; el artefacto indica `nativeTerrainWritten=false` y `gameVerified=false`.
- Leí independientemente la ventana TIFF original y comparé las 25 celdas con el fixture: 25/25 valores exactos; el hash del TIFF coincide. PixelIsPoint y el origen de centro/steps del fixture son coherentes con la georreferencia y el affine del registro de procesamiento.

## Límites y cuestiones pendientes

El hash identifica los bytes del archivo citado, pero no certifica extracción, georreferenciación, conversión vertical ni adecuación del remuestreo. El CLI exige que el aviso exista, pero no evalúa legalmente su contenido; la revisión solo comprobó que el candidato incluye el texto del aviso local y que la ruta está dentro del proyecto. La cobertura significa soporte de interpolación en todos los centros solicitados, no precisión ni exactitud del relieve. El DSM moderno puede incluir edificios y vegetación; el código lo deja explícito y no deduce suelo antiguo, agua, transitabilidad, rutas, puentes, edificios o terreno de AoE2. No lee GeoTIFF ni escribe elevación nativa. Las pruebas no ejecutan el juego ni implementan/verifican navegación o transporte; esas condiciones de S2 siguen pendientes.
