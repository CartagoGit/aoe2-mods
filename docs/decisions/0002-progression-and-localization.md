# ADR 0002 — Continuidad opcional e IDs permanentes

Estado: aceptado. Fuente canónica: es-ES. Fecha: 2026-10-12.

Toda campaña puede jugarse por separado. recommendedPrevious describe recomendaciones y recapitulaciones. CampaignVariable solo se usa en SequenceItems con una plantilla nativa verificada. La descripción pública conserva la recomendación estática aunque no pueda consultar progreso.

Los autores usan claves semánticas. Un lock global asigna IDs numéricos, ordena nuevas claves y nunca reutiliza tombstones. El rango 1900000001 en el fixture NO es oficialmente reservado; la release requiere comprobarlo contra recursos y mods objetivo. No traducir internalName, endingKey ni progressKey.

Cada mod exporta actualmente su catálogo. La convivencia de archivos con la misma ruta no se presume acumulativa: hay una prueba obligatoria con 2/5/10 mods y prioridades. Si el motor reemplaza los catálogos, seleccionar y acreditar una estrategia de catálogo común por versión antes de publicar, sin obligar a instalar campañas predecesoras.
