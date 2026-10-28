# Compilar y publicar mods

campaign:build produce IR; --export produce el subconjunto binario soportado y un ZIP de fixture. release:check falla hasta que el contenido esté aprobado, las traducciones completas, los medios acreditados y las pruebas reales registradas. No subir el ZIP de fixture como campaña final.

El mod final debe contener resources/_common/campaign/NAME.aoe2campaign, NAME.json y NAME_layout.json obtenidos mediante plantillas nativas probadas, catálogos por idioma y medios en rutas verificadas. Los nombres coinciden y no se traducen. No modificar recursos privados de AoE2 ni suscripciones ajenas.

Antes de publicación: probar instalación limpia y actualización, continuidad sin predecesora, mismo progreso con cambio de idioma, prioridades y coexistencia 2/5/10 mods, tres dificultades, derechos, tamaño y accesibilidad. Guardar hash del ZIP y versión del juego junto al QA. Cambiar un artefacto invalida la evidencia vinculada a su hash.

La subida al portal o desde el juego requiere autorización del propietario. Guardar después el ID real del portal en el registro de publicación. Las campañas siguen siendo independientes; el mod de voz por idioma, si existe, es opcional. No crear automáticamente un repositorio remoto nuevo: este proyecto ya tiene origin.

## Candidato y aprobación

`bun run campaign:candidate ID` exige campaigns/ID/native/manifest.json y sus plantillas. Genera dist/ID-release.zip y build/ID/candidate-report.json con hash y huella de contenido. Se permite un candidato experimental para pruebas; no se aprueba su publicación automáticamente. Registrar los resultados del juego en compatibility/QA de la campaña, sin alterar el contenido del ZIP. Después ejecutar release:check. Si cambian textos, mapa, medios o plantillas, recompilar y comparar el ZIP: las evidencias deben corresponder a su hash nuevo. No renombrar el fixture como release.

El manifest nativo es un contrato de la fábrica, no un formato del juego: schemaVersion=1, source, license, restrictions, gameBuild, reviewer, status (experimental/game-verified), narrativeTemplate, layoutTemplate y values. Las dos plantillas conservan las envolturas nativas acreditadas, con tokens @cdf:string:<clave> y @cdf:value:<nombre>. Ningún recurso oficial protegido se redistribuye sin permiso. Para release las plantillas deben estar game-verified; aportar primero evidencia real, nunca cambiar la marca para ocultar un fallo.
