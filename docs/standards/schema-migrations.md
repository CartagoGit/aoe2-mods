# Migraciones de contratos

El contrato actual es schemaVersion=1 y rechaza campos desconocidos. Las fuentes no se migran silenciosamente al abrir o compilar. Una versión nueva requiere ADR con motivo, comparación de contratos, programa explícito de migración, fixture de entrada de la versión previa y salida esperada, pruebas de idempotencia y backward compatibility.

La migración trabaja en la unidad aislada y se revisa antes de reemplazar fuentes. Conservar IDs, claves de progreso, nombres de motor y tombstones. Si una clave narrativa se divide, asignar IDs nuevos a las piezas sin reutilizar el antiguo. El lock y los artefactos publicados permiten comparar estabilidad.

No existe una migración v1→v2 porque no hay v2; implementar scripts vacíos simularía una capacidad inexistente. La propuesta de un cambio de esquema debe incluir su migración y pruebas como slices obligatorios.
