# ADR 0003 — Autoría inicial en inglés

Decisión del propietario (2026-10-12), posterior al encargo original: títulos y contenido nuevos se conciben primero en inglés (`en`); el español de España (`es-ES`) tiene catálogo completo y revisión independiente. La documentación operativa puede permanecer en español.

Cada campaña declara `sourceLocale`, obligatorio en el contrato schemaVersion 1. No hay fallback implícito: el validador compara claves, placeholders y marcadores con ese catálogo, y CLI usa el mismo selector para propiedad de claves, IDs y audio sin locale explícito. Las campañas nuevas declaran `en`. El fixture existente se migra declarando `es-ES`: conserva sus textos, identidades e IDs. Los documentos de planificación contienen ambas versiones editoriales.

Es una ampliación requerida de schemaVersion 1 mientras no hay campañas publicadas. Una fuente anterior sin sourceLocale debe añadirlo explícitamente antes de cargar; no se adivina por orden del array. Los 17 destinos siguen siendo obligatorios para producción y requieren revisión. `en` es la clave registrada del motor, no `en-US`. El idioma fuente no otorga aprobación lingüística ni acredita compatibilidad del juego.

Títulos de presentación nuevos no cambian campaignId, internalName, publicId ni namespaces de progreso. La exportación nativa y el lock no dependen del idioma utilizado para concebir un título.
