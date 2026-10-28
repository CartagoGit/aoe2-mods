# Capacidades verificadas y pruebas pendientes

Consulta: 2026-10-12. La conversación adjunta es un brief, no evidencia técnica. Se verificaron documentación oficial, API/código de dependencias y exportaciones locales. No se ejecutó AoE2.

| Característica | Evidencia primaria | Estado | Límite / prueba / decisión |
|---|---|---|---|
| Escenario 1.59 | [AoE2ScenarioParser](https://github.com/KSneijders/AoE2ScenarioParser), soporte1.36–1.59 | Confirmado en biblioteca y round-trip | Parser0.9.6 fijado; motor pendiente |
| Contenedor .aoe2campaign | [rge_campaign](https://github.com/withmorten/rge_campaign), revisión3c40203b650de9888ca82fae1276ea67bf3d3d93 | Round-trip confirmado | Empaquetar/extraer propios; no redistribuir herramienta sin licencia |
| Store/Load/Delete Key | [Update128442](https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-128442/) | Documentado | Solo campaña; Store Key serializado; guardar/cargar y replay necesitan juego |
| CampaignVariable | [Update141935](https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-141935/) | Documentado | Condition de SequenceItems; no control de permisos; plantilla nativa pendiente |
| UnlockScenarios | [Update107882](https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-107882/) | Documentado | true permite todos los escenarios; no árbol condicional entre campañas |
| XS archivos/dificultad | [Referencia oficial XS](https://www.forgottenempires.net/age-of-empires-ii-definitive-edition/xs-scripting-in-age-of-empires-ii-definitive-edition) | Documentado; XS generado validado por xs-check | xsdat por perfil/tamaño limitado no necesario para arquitectura final; xsGetDifficulty exacto evita ambigüedad de umbral |
| Objetivos/variables/disparadores | [API del parser](https://ksneijders.github.io/AoE2ScenarioParser/) | Serializados y reabiertos | Comparaciones, timers, destroy, terminal, rutas/eventos/reservas; comportamiento motor pendiente |
| IA PER integrada | API player.set_custom_ai del parser | Serializada en variante de exportación | Texto propio; economía/estrategia debe diseñarse y probarse; None para reserva simple |
| Dificultad | Dataset DifficultyLevel del parser + referencia XS | Enums confirmados / motor experimental | Perfiles internos easy>=3,standard=2,hard<=1; recursos y órdenes por XS; UI y balance requieren juego |
| 17 idiomas | [Steam](https://store.steampowered.com/app/813780/), API appdetails813780 | Lista confirmada | en/fr/it/de/ja/ko/pt-BR/ru/zh-Hans/es-LATAM/zh-Hant/tr/vi/es-ES/pl/hi/ms; carpetas candidatas pendientes |
| IDs semánticos | Contrato propio + campos string_id del parser | Compilador numérico probado | No presumir soporte de letras en todos los campos. Rango del fixture no reservado; requiere escaneo |
| Strings del mod | [Guía de autores UGC](https://ugc.aoe2.rocks/mods/) | Documentado | resources/LOCALE/strings/key-value/key-value-modded-strings-utf8.txt; coexistencia/prioridad pendiente |
| Slides/layout | [Guía de autores JSON](https://steamcommunity.com/sharedfiles/filedetails/?id=2363743236) y Update141935 | Documentado parcialmente | No envolver JSON imaginado; importar plantilla nativa completa, tokens y probar en motor |
| WAV y subtítulos | Validación RIFF/PCM/SRT local | Pipeline confirmado | PCM16/24, duración, peak normalization; rutas/WEM/voiceover motor pendientes |
| PNG/medios | Cabecera/manifest/hash local | Validación estática | Resoluciones del manifiesto; permisos y formatos efectivos del motor pendientes |
| Return of Rome | Modo separado; sin fixtures propios ejecutados | Pendiente | Rechazado por adaptador hasta prueba específica; no mezclar civilizaciones/datos sin acreditación |
| Producción multiplataforma | pathlib/argv/Bun y CI matrix | Linux ejecutado; Win/mac CI configurada | No afirmar CI remota ejecutada ni juego nativo universal |

## DelendAI

Servidor0.1.0; CLI local0.1.1; checkout de referencia9bbb94ffde31e5162688d35ddb33ba0648c3a958 en la lectura inicial. [Repositorio](https://github.com/CartagoGit/DelendAI). Se leyó CROSS-PROJECT-SETUP y AGENT-BOOTSTRAP y se usó adopción, catálogo y creación oficial. El runtime actual manda sobre listas antiguas.

## Experimentos de aceptación

Nuevas partidas, A, B, ambas, reinicio, guardado/carga, ausencia de predecesora, idiomas, prioridades2/5/10, XS dificultad, simultaneidad terminal, slides/audio, actualización y RoR. Cada resultado registra versión, plataforma, ZIP/hash, pasos, evidencia y revisor. Un bug antiguo o una nota de parche no acredita solución en nuestro contenido.

No se validaron servicios de pago de voz/imágenes ni especificaciones de sus planes. Los contratos permiten sustituir proveedor sin necesidad de recomendar ni contratar uno ahora.

El XS incluido por la wheel no es nativo macOS. Ver [portabilidad y requisito COF_XS_CHECK_BIN](../guides/development.md); CI valida contratos en tres SO y el round-trip nativo en Linux/Windows. La acreditación macOS está asignada a s00001-S5.
