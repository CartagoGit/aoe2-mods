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
