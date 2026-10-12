# Preparación e incorporación de campañas

Cada slice se integra con `bun run validate` pasando sobre todas las campañas activas. Una carpeta incompleta en campaigns rompe loadProject; un texto nuevo sin ID rompe la validación. Por eso los slices preparatorios escriben en staging/campaigns/<id>, con la misma organización final, y el slice de materialización incorpora fuentes completas, IDs y glosario en una sola entrega.

## Borradores

El dossier fija identidad, orden de escenarios y claves semánticas. El slice de metadatos prepara campaign.json en staging; los siguientes añaden sus escenarios allí. Las rutas de assets declaran su destino final en campaigns; los bytes se guardan junto al borrador para copiarse durante la materialización.

`bun run staging:check <id> --partial` analiza metadatos y todos los escenarios declarados que existan mediante los contratos estrictos. Enumera los archivos pendientes. Es una comprobación de borrador parcial; no acredita referencias completas, IDs, bytes multimedia, exportación ni juego. JSON corrupto, esquema inválido, ruta insegura o escenario existente inválido falla incluso con --partial.

Cuando estén todos los escenarios, `bun run staging:check <id>` exige el bundle completo y valida historia, catálogos, narradores, objetivos, reservas y progreso final. El informe mantiene explícito su alcance de borrador. Completar los archivos no cambia su estado editorial ni autoriza publicar.

## Materialización

El slice final reclama staging/campaigns/<id>/**, campaigns/<id>/**, config/string-ids.lock.json y config/glossary.json; sus Files incluyen estos ámbitos. Serializar el registro global entre propuestas. Los dos mods del piloto técnico se incorporan juntos.

1. Comprobar el bundle con staging:check sin --partial y la ausencia de una campaña activa con ese ID. Si ya existe, revisar y actualizar sus archivos explícitamente; no sobrescribirla a ciegas.
2. Copiar el bundle completo al destino campaigns/<id>, incluidos escenarios, medios y plantillas acreditadas. Ajustar asset.path a su ubicación final, verificar hashes/licencias y conservar todas las claves e identidades previstas.
3. Ejecutar `bun run ids:allocate` ahora que loadProject puede cargar todas las fuentes. Actualizar glosario en el mismo slice. Revisar que ningún ID anterior cambie y que las claves nuevas tengan su namespace.
4. Ejecutar `bun run validate`, `bun run test:export` y `bun run campaign:build <id> --export` para cada mod incorporado. Corregir antes de commitear; no integrar un estado intermedio.
5. Eliminar el borrador promovido de staging dentro de esa entrega, conservar dossier y evidencia. Un único commit de materialización incluye fuentes completas, IDs, glosario y eliminación del borrador. Someterlo a revisión y publicación oficial.

Las aprobaciones de 17 catálogos, reparto, audio, imágenes y juego pertenecen al cierre de producción con release:check. Mantener draft donde proceda y reportar pendientes. No retrasar los IDs hasta un slice posterior a la incorporación ni bajar el gate de develop para aceptar contenido incompleto.
