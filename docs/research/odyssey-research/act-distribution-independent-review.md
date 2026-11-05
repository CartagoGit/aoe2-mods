# Revisión independiente acotada: coherencia de actos

23 de octubre de 2026 · d00002/S1 · revisora independiente: `gpt-6-luna`; implementador: `gpt-6`. Unidad review: `wip/gpt-6-luna/review/d00002-S1-g1/act-distribution-review`. Commits revisados: `3995bcdf14b725dcd79b0f5c79a65f8f608f6867` y actualización de fingerprint `c38c58c`.

## Alcance y resultado

Revisé la reconciliación de `actEpisodeTargets`, el validador compartido, las dos regresiones adversariales y la actualización del snapshot cívico. No encontré un defecto bloqueante en este componente acotado. Este informe registra evidencia técnica; no es un veredicto formal, aprobación ni cierre de S1.

`docs/design/odyssey-policy.json` ahora refleja los tamaños de los cinco `acts[].episodeIds` existentes. `tools/design/odyssey_catalog.helper.py` exige cinco enteros positivos (excluye booleanos), total igual al objetivo de campaña y coincidencia, en orden, con la pertenencia editorial actual. Las selecciones, su orden/identidad y contratos de motor no se alteran. Las pruebas nuevas detectan tanto un cambio de reparto que conserva la suma como forma/total inválidos.

`c38c58c` modifica en `civic-difficulty-mechanical-audit.json` únicamente la fecha de snapshot y el hash de la política; conserva las métricas registradas. El checkpoint atribuye la regeneración al helper existente y no presenta los candidatos mecánicos como aprobados.

## Límites que siguen abiertos

La validación es estructural: confirma coherencia entre cuotas y membresía ya escrita, pero no juzga si la división de actos, sus hitos, ritmo o curvas de presión resultan históricamente fundamentados o editorialmente convincentes. El plan de producción prohíbe rellenar periodos con guerras inventadas y exige justificar divisiones y cambios de arco; esa revisión humana sigue pendiente.

El checkpoint común también identifica como pendiente enlazar, selección por selección, la investigación delegada con el pasaje realmente consultado, el alcance de acceso y la decisión del arquitecto. Una anotación o URL no equivale a aceptación histórica. Esta revisión no comprueba hechos históricos, terrenos, licencias de cada recurso ni balance en AoE2.

Los generadores de dossiers y secundarios son una arquitectura existente con contratos y validaciones explícitas del contenido autoral; el cambio revisado no amplía esos contratos ni acredita que generen mapas nativos. La ausencia de dossiers de 215 selecciones no se usa aquí como fallo automático del componente común: redacción y aprobaciones de campaña corresponden a S2–S10. No hay aprobación ampliada de juego derivada de esta revisión.

## Comprobaciones ejecutadas

Las comprobaciones siguientes se ejecutaron sobre el mismo tip de implementación (`c38c58c`) mientras el informe estaba temporalmente en la unidad inicial mal clasificada como `implement`. El informe se trasladó intacto a la unidad oficial `review`; este ajuste de registro de unidad/atribución no cambió código ni datos, por lo que no se repitieron las pruebas.

- `python3 tools/design/test_design.py`: 68 pruebas, correctas; incluye las dos regresiones de distribución.
- `python3 tools/design/odyssey_render.script.py --check`: 9 campañas y 278 selecciones comprobadas; los dossiers ampliados siguen sin certificación.
- `bun run validate`: terminó con exit 0 en esta unidad: TypeScript/Biome, 142 pruebas Bun (2.069 expectativas), documentación/enlaces locales y validación de una campaña.

La validación no prueba terreno transitable ni comportamiento, dificultad o diversión dentro del juego. El gate completo reportado no modifica esos límites.
