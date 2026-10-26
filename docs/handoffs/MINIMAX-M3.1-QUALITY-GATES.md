# Gates y evidencia de entrega

| Nivel | Evidencia | Qué permite |
|---|---|---|
| BASE READY | Tipado/lint/tests/docs/contratos, revisión independiente e integración resueltas | Autoría de contenido acotado |
| EXPORT READY | Escenario reabierto, efectos/terreno persistidos y contenedor propio extraído sin pérdida | Probar el perfil binario exportado |
| GAME VERIFIED | Versión/plataforma/hash y pasos con resultados reales del motor | Marcar solo la capacidad y artefacto probados |
| PRODUCTION READY | release:check, 17 traducciones/voces, derechos, editorial/QA y revisiones | Solicitar publicación del mod concreto |

## Antes de entregar un slice

```sh
bun install --frozen-lockfile
bun run validate
bun run schema:export
bun run i18n:check
bun run assets:check
bun run audio:check
```

Para cambios en escenarios: preparar Python/C según README; ejecutar bun run test:export y bun run campaign:build <id> --export. Los tests negativos deben seguir rechazando rutas peligrosas, claves/objetivos rotos, reservas infinitas y releases prematuras. Un comando exitoso sobre un catálogo sin audios no demuestra una campaña doblada.

Para entrega completa: bun run audio:build <id> --locale=<locale> solo con proveedor/grabaciones configurados; acreditar plantillas y rutas de medios; bun run campaign:candidate <id>; probar ese ZIP en AoE2; registrar su hash y revisión; finalmente bun run release:check <id>. No generar candidato con plantillas imaginadas. No renombrar el ZIP fixture para superar el gate. El reporte del candidato comprueba que textos/gameplay/medios/plantillas actuales corresponden al ZIP.

## Pruebas en el juego

Instalación limpia/actualización, intro/slideshow/audio, locales completos y cambio de idioma, 2/5/10 mods y prioridades, perfil sin campaña predecesora, rutas A/B/ambas por replay, guardar/cargar antes/después del final, derrota y victoria simultáneas, tres dificultades y estrategias alternativas. En misiones históricas añadir personaje esencial, objetivo destruido temprano, bloqueo de puente, agotamiento y estancamiento de IA. Registra resultados fallidos además de los positivos.

La evidencia contiene gameBuild, plataforma, artifactSha256, responsable, pasos y observaciones. No inventes nombres de revisores ni marcas approved/passed. La revisión lingüística/histórica exige personas o agentes competentes y lectura de fuentes; el validador solo comprueba trazabilidad y consistencia. La revisión DelendAI es independiente del implementador.

Si cambia el ZIP, la evidencia vinculada al hash anterior deja de acreditar el candidato. Un cambio solo de revisión/QA puede conservar el ZIP, pero debe compararse el hash y la vigencia del reporte. El cierre oficial de propuesta se realiza en DelendAI, no editando encabezados.

## Ampliación de diseño vigente

El encargo vigente usa inglés como fuente inicial y nueve odiseas con 278 episodios seleccionados; los 39 contratos del catálogo previo conservan su identidad. La planificación específica está en [catálogo](../design/README.md), [contrato](../design/production-contract.md) y [asignaciones porcampaña](MINIMAX-M3.1-DESIGN-ASSIGNMENTS.md). Esos dossiers sustituyen los briefs provisionales en decisiones editoriales; conservan IDs existentes y los gates de pilotos/capacidades/motor. MiniMax verifica y materializa, no diseña historia, narradores, mapas ni nuevas economías. Recuperar estados oficiales antes de elegir slice.


## Estudios del arquitecto

Cuando se modifique el diseño, ejecutar además `python3 tools/design/test_design.py` y sus generadores/verificadores. El estudio económico candidato de Constantinopla se comprueba con `python3 tools/design/finite_allocation_audit.script.py` y `python3 tools/design/test_finite_allocation_audit.py`; son cuatro pruebas separadas del gate Bun, no pruebas nativas ni aprobación de jugabilidad. El fingerprint incluye el plan y los importes compartidos resueltos, no toda la semántica del módulo de secundarios. MiniMax no implementa i00007 ni decide sus recetas por pasar estas comprobaciones.


## Referencia de alternativas y gate nativo pendiente

El 23 de octubre de 2026, i00007/S1–S2 están aprobados; S2 se integró en `4ac57b8f` y la aprobación formal independiente en `66468212`. La [arquitectura](../architecture/overview.md) explica el perfil optativo v3, su núcleo v2 intacto y los límites. Consultar el veredicto vivo mediante `proposal_review action=status`; los informes fechados anteriores a la publicación no sustituyen ese registro.

La validación de S2 ejecutó 142 pruebas y 2069 aserciones, incluidas 34 de referencia de alternativas, y el gate documental/de campaña. La comprobación de exportación ejecutó 3 variantes y 2 round-trips del fixture soportado anterior, con `unsupportedModeRejected=true` y `gameVerified=false`. Se probó además el rechazo explícito de v3 en renderer y Python. No presentar esos resultados como exportación nativa de alternativas o como 95 partidas jugadas.

En una unidad aislada sin `.venv` propia puede usarse el `COF_PYTHON` documentado y `RGE_CAMPAIGN_BIN` apuntando a las herramientas fijadas del checkout compartido; no guardar rutas personales. Si faltan, seguir README y conservar el error real, nunca declarar el gate pasado por usar otro perfil. Repetir los comandos sobre el candidato propio cuando corresponda.

MiniMax comienza únicamente por el slice designado f00001/S1 si su estado vivo lo permite. i00007/S3, i00003 nativo/plantillas/entrada y s00001 requieren su evidencia antes de promover el perfil compuesto. Los 63 borradores y 215 selecciones sin dossier y bloqueos históricos permanecen vigentes; esta revisión de referencia no es aprobación de historia, mapa, idioma o nivelación.
