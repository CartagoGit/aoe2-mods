# Revisión técnica independiente: Sirmium 379 (dossier 33)

Fecha: 2026-10-18. Revisor: `gpt-6-luna`. Candidato revisado: `b3fc89594bead5313b100d2b35b6a922ea80115d`, incluidos los commits `469de30` y `b3fc895`, sobre `65bafb11e3445eb7a2edaa9764fb1ff0c44ecef6`.

## Alcance y resultado

La revisión cubre la proyección del dossier a los predicados tipados de referencia, el vencimiento del plazo en el modelo, la regresión del audit cívico existente y una comprobación aritmética del frame final frente al bbox padre y la línea moderna Sava disponible. No certifica la geografía histórica de 379, terreno transitable, geometría nativa, navegación, balance ni experiencia de juego. No aprueba el slice de implementación completo.

No encontré bloqueantes en este alcance acotado.

## Evidencia ejecutada

- `bun run validate` pasó en la unidad de revisión: `bun run check`, 107 pruebas con 424 expectativas, `docs:check` y validación de una campaña.
- Adapté `/tmp/imperial33-reference-fixture.ts` para importar exclusivamente desde esta unidad y alimentar el episodio `33-accession-and-reassembly-sirmium` extraído del JSON candidato. Bun informó 0 pruebas registradas y 5.162 llamadas a `expect`; el fixture terminó con `allPassed: true`, 2.520 asignaciones de staging y 28 subconjuntos finales. Incluye pago/recibos, llegadas tempranas no suficientes, combinaciones de asignación, ambas APIs terminales, muerte, falta de presencia actual, avisos y expiración en easy/standard/hard, además de guardar y reutilizar estados serializados. Es una proyección del modelo tipado, no ejecución nativa ni prueba de juego.
- Comparé `episodes[]` del audit cívico actual con el audit en `65bafb11`: los 62 registros anteriores son idénticos y ninguno falta. El nuevo registro eleva el total a 63, principales a 214, secundarios a 391 y pantallas a 2.594; añade un único plazo estructurado. Los 54 candidatos de riesgo estático y los 8 dossiers con hostiles finitos no cambian. Los 63 conservan presupuestos accesibles iguales por dificultad.
- Recalculé el SHA-256 del GeoJSON local `ne_10m_rivers_lake_centerlines.geojson`: coincide con `bb854a900ecbd3b408df46d5e16e3e0f974ba55993f9d8b5c26e855273c0905a`. Una comprobación de intersección segmento-rectángulo sobre sus segmentos con nombre `Sava` confirma cero cruces con `[19.6, 44.971, 19.632, 44.992]` y con `[19.59808, 44.9688245557402, 19.63392, 44.994175444259795]`. La caja expandida queda dentro de `[19.575, 44.948, 19.65, 44.996]`; esa línea sí cruza el bbox padre. Esto verifica solo la aritmética respecto al recurso moderno y sus coordenadas, no la exactitud hidrográfica ni el suelo antiguo.
- `git diff --check 65bafb11..b3fc895` no informó errores de whitespace.

## Límites pendientes

El artefacto de control geográfico declara expresamente que su frame y la ausencia de cruce con la línea moderna no prueban terreno seco, ribera antigua o marisma en 379. Tampoco se localizaron con esta revisión palacio, puerta, puerto, calle concreta ni sede de la proclamación. El plazo está marcado como no implementado nativamente; la presencia de un modelo de referencia y textos de dossier no demuestra soporte del motor. Las métricas de staging, capacidades de unidades, recorridos y economía siguen siendo diseño, no balance validado.
