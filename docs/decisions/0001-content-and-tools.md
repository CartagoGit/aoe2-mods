# ADR 0001 — Contenido declarativo y herramientas locales

Estado: aceptado para la infraestructura. Fecha: 2026-10-12.

Se elige JSON en lugar de YAML/TypeScript para contenido: permite JSON Schema, herramientas de edición y traductores sin ejecución de código ni ambigüedad de tipos YAML. Las campañas referencian escenarios mediante scenarioFiles y el loader los compone antes de validar.

Bun y TypeScript estricto implementan orquestación, contratos y políticas; Python usa AoE2ScenarioParser 0.9.6 con soporte declarado 1.59. rge_campaign se fija a una revisión con hashes, se ejecuta fuera del repo y no se redistribuye por ausencia de licencia en esa revisión. No se copia implementación interna de DelendAI.

Consecuencia: se requiere instalar toolchain de producción, pero el jugador solo recibe un mod. Los fallos de compatibilidad bloquean la exportación correspondiente. Los binarios no se declaran deterministas si contienen metadatos del parser.
