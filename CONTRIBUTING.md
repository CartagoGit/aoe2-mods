# Contribución

Usa las instrucciones de AGENTS.md y una propuesta oficial de DelendAI. Cada entrega declara alcance, dependencias, archivos, criterios y pruebas. Código TypeScript estricto; contratos Zod; Python solo para interoperabilidad. Reutiliza funciones de core, validadores y compiladores antes de añadir nuevas capas.

Commits convencionales: feat, fix, docs, test, infra o refactor con alcance semántico. No incluir `.venv`, cachés, builds, secretos ni recursos cuyo permiso no esté documentado. No modificar archivos generados para corregir sus fuentes.

La revisión cubre contrato, efecto sobre campañas existentes, fuentes históricas, licencias, idioma, bugs y evidencia. Cambios de esquema requieren ADR y migración explícita; preservar claves retiradas en el lock. La propuesta solo se cierra según el estado oficial de revisión de DelendAI.

Código bajo MIT; documentación original bajo CC-BY-4.0. Los recursos tienen licencias individuales en su manifiesto. Las dependencias conservan sus propias licencias; rge_campaign es una herramienta externa cuyo código/binario no se redistribuye con este repositorio.
