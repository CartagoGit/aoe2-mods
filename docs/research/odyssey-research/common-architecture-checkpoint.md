# Checkpoint de arquitectura común de las odiseas

23 de octubre de 2026 · d00002/S1 · arquitecto `gpt-6`; recopilación de cobertura `gpt-6-luna`. Este documento registra un componente y trabajo pendiente, no una aprobación o cierre del slice.

## Discrepancia corregida

El arquitecto contrastó los nueve `actEpisodeTargets` de la [política](../../design/odyssey-policy.json) con la pertenencia existente de cada acto en los JSON de campaña. Se conservan las selecciones y su cronología; se actualizan las siete cuotas iniciales obsoletas, sin cambios de identidad, orden, contrato de motor ni cadenas.

| Campaña | Cuota anterior | Distribución editorial conservada |
|---|---|---|
| faith-origins | 6/6/6/6/6 | 8/7/6/6/3 |
| jewish-tradition | 6/6/6/6/6 | 5/7/5/7/6 |
| new-rome | 6/6/6/7/7 | 8/9/5/3/7 |
| first-caliphs | 6/6/6/6/6 | 7/7/7/5/4 |
| first-fitna | 5/6/6/6/5 | 5/6/5/7/5 |
| umayyads | 6/6/7/7/6 | 3/9/7/8/5 |
| house-of-ali | 6/6/6/6/6 | 5/5/6/7/7 |

Los repartos imperiales 6/6/7/6/9 y romanos 6/6/6/7/7 ya coincidían. El validador común comprueba ahora forma, integridad positiva, total y pertenencia; las regresiones distinguen una suma equivocada de una redistribución equivocada que conserva el total. No se introducen cuotas uniformes para forzar acontecimientos inventados.

## Evidencia existente y límites de S1

El [plan](../../design/odyssey-production-plan.md) establece nueve arcos, cinco actos, ritmo, variedad, fuentes atribuidas y prohibición de relleno. Los generadores compartidos de dossiers y secundarios reciben decisiones explícitas del autor y validan sus contratos; no seleccionan historia ni producen mapas nativos. Las curvas de los actos son hipótesis de presión, logística y recuperación, con calibración pendiente. Su presencia no acredita una progresión divertida ni sustituye revisión editorial.

La investigación delegada conserva consultas, variantes y límites; la nueva [colección de episodios judíos 5–8](jewish-episodes-05-08-primary-collection.md) es un ejemplo de contraste acotado, sin aprobación. El índice cuenta anotaciones de consulta, no hechos verificados. Hay cobertura desigual: 30/30 faith, 34/34 imperial, 17/30 judía, 19/32 romana y 16/32 oriental y ninguna anotación enlazada en las cuatro odiseas islámicas. Existen recopilaciones separadas; antes de cerrar S1 deben relacionarse con las selecciones canónicas y conservar la decisión del arquitecto, el pasaje realmente leído, tipo de acceso y cautela. Un enlace presente no será automáticamente una aceptación histórica.

También permanece pendiente la revisión editorial de hitos y de las curvas de acto. No se implementa una prueba automática que pretenda medir interés narrativo o rigor histórico a partir de un texto. La auditoría humana deberá justificar divisiones, repeticiones y cambios de contexto, manteniendo las restricciones de las fuentes y de reutilización de medios.

Los 215 episodios sin dossier no se usan por sí solos para declarar fallida esta arquitectura común: su redacción y aprobación pertenecen a las campañas S2–S10. El estado general conserva 278 selecciones, 63 borradores ampliados y ninguna aprobación ampliada de juego. Nada de esta reconciliación desbloquea MiniMax histórico, i00007/S3, navegación o ejecución en AoE2.
