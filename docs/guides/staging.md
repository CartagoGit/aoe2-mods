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
5. Conservar el borrador promovido como snapshot congelado hasta el cierre oficial de toda la propuesta, indicando el commit de materialización en staging/campaigns/<id>/PROMOTED.md. Las ediciones siguientes se hacen exclusivamente en campaigns; el snapshot conserva la evidencia de los slices preparatorios. Un único commit de materialización incluye fuentes completas, IDs, glosario y ese recibo. Su limpieza posterior requiere una tarea de mantenimiento tras cerrar la propuesta; no eliminar antes rutas que DelendAI comprueba al cerrar.

En Files de las propuestas se declaran rutas literales existentes al terminar su trabajo (por ejemplo campaigns/<id> o staging/campaigns/<id>/scenarios/01-<slug>). El runtime instalado no expande comodines en la comprobación de completitud. Los locks pueden usar patrones según su esquema propio; no trasladar automáticamente ese formato a Files.

Las aprobaciones de 17 catálogos, reparto, audio, imágenes y juego pertenecen al cierre de producción con release:check. Mantener draft donde proceda y reportar pendientes. No retrasar los IDs hasta un slice posterior a la incorporación ni bajar el gate de develop para aceptar contenido incompleto.
