# Revisión técnica independiente de la auditoría de extensión geográfica

Revisión acotada de `tools/map/geographic_extent_audit.script.py` en candidato exacto `c8fbc3f` sobre `baeb603001cf89cfbcc44003c4f26b59524a2130`. Revisor: `gpt-6-luna`. Este informe no aprueba terreno histórico, S2 completo ni jugabilidad.

## Resultado

No encontré bloqueantes en el audit. Reutiliza el catálogo/validador de odiseas y el helper de frame existente; comprueba por separado bbox solicitado, centros de muestra acolchados y envolvente de celdas completa. La envolvente de medio píxel se informa aparte, así que el resultado no confunde la cobertura de centros usada por la interpolación con la de celdas requerida para futuras huellas. El informe exige que cada campaña de la política aparezca, exige una lista de dossiers incluso si está vacía, rechaza perfiles geográficos faltantes y registra huellas semánticas de política, geografías, perfiles y campañas. Sus límites impiden leer una contención aritmética como fuente DEM completa, costa antigua, transitabilidad o aprobación de juego.

La salida predeterminada es JSON en stdout. La opción `--output` rechaza destinos dentro del proyecto salvo `build/`; permite salidas temporales externas. Probé que se rechaza `tests/maps/should-not-be-written.json` y no se crea. La suite también verifica el caso de escritura externa temporal usada por el CLI real.

## Verificación ejecutada

- `python3.10 tests/maps/test_geographic_raster.py`: 9 tests correctos, incluidos los tres casos nuevos.
- `python3.10 tools/map/geographic_extent_audit.script.py`: auditoría real correcta y JSON íntegro en `/tmp`.
- Comprobé de forma independiente las sumas y consistencia por registro: 63 dossiers, 278 selecciones, 26 preguntas de cobertura, cero casos causados solo por las celdas exteriores; los totales agregados coinciden con la suma de registros.
- Las nueve campañas están presentes: dos contienen dossiers; las siete restantes conservan cero dossiers, no se omiten.
- `bun run validate`: check, 108 tests Bun / 426 expectativas, documentación y validación de campaña correctos.

La salida muestra que las 26 preguntas exceden la referencia ya en los centros acolchados. Esto describe extensión de origen/cobertura para revisión: no demuestra que esos mapas sean errores históricos. No cambió ningún bbox, dossier, actor, perfil de fuente o contrato, y el audit no afirma transitabilidad. La aceptación pendiente de S2 todavía requiere extracción y controles de terreno/huellas/transporte/navegación y evaluación nativa; esta revisión no los certifica.
