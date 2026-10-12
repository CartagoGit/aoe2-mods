---
id: s00001
title: "Acreditar compatibilidad nativa y pruebas de motor"
kind: spike
status: ready
type: proposal
track: campaign-factory
date: 2026-10-12
---

# s00001 — Acreditar compatibilidad nativa y pruebas de motor

## goal

Completar la evidencia necesaria antes de producción sin inventar formatos. Responsable: arquitecto y probador con AoE2; MiniMax no debe modificar infraestructura por iniciativa propia. Leer docs/research/aoe2-capabilities.md, docs/guides/publishing.md y el perfil de exportación. Registrar build, OS, hash, pasos, resultados y capturas. Conservar diferencias entre soporte documentado, exportación y GAME VERIFIED.

## why

La infraestructura funciona fuera del juego, pero no hay una instalación AoE2 ejecutada en este entorno. Estas evidencias habilitan la producción; no se sustituyen por tests del parser.

## non-goals

- Desbloqueo obligatorio o gestor externo.
- Generar historia completa o marcar pruebas pendientes como aprobadas.

## slices

- global_gate: e2e

### S1 — Progreso acumulativo y campaña ausente
- **Status**: pending
- **Files**: `tests/compatibility/progression.json`, `docs/qa/game-progression.md`
- **Gate**: e2e
- acceptance:
  - "Dos rutas con claves distintas, replay A/B en ambos órdenes, guardar/cargar antes de ganar y después de elegir."
  - "Campaña sucesora sin predecesora instalada: siempre jugable, aviso y recapitulación; con clave correcta desaparece recomendación."
  - "Registrar también ausencia de clave y cambio de idioma sin renombrar nombres del motor."

### S2 — Idiomas y colisiones entre mods
- **Status**: pending
- **Files**: `tests/compatibility/localization.json`, `docs/qa/game-localization.md`, `config/languages.json`
- **Gate**: e2e
- acceptance:
  - "Obtener códigos exactos de 17 carpetas de una instalación con build registrado."
  - "Probar 2,5,10 mods y prioridades invertidas, todos los alfabetos, cambios de idioma y actualización."
  - "Resolver colisión de archivos de cadenas mediante estrategia acreditada; revisar ADR antes de alterar compilador."

### S3 — Plantillas narrativas, layout y audio
- **Status**: pending
- **Files**: `campaigns/technical-pilot/native/**`, `tests/compatibility/media.json`, `docs/qa/game-media.md`
- **Gate**: e2e
- acceptance:
  - "Conservar plantilla nativa completa con fuente/build/licencia y tokens documentados; generar NAME.json y NAME_layout.json con --templates."
  - "Narrador general y particular antes/después de misión, subtítulo e imagen; audio WAV/WEM en rutas comprobadas."
  - "CampaignVariable en SequenceItems; ninguna condición cambia accesibilidad."

### S4 — XS, dificultad y simultaneidad
- **Status**: pending
- **Files**: `tests/compatibility/difficulty.json`, `docs/qa/game-difficulty.md`, `config/engine.json`
- **Gate**: e2e
- acceptance:
  - "Verificar xsGetDifficulty con UI de campaña y editor, perfiles easy>=3/standard=2/hard<=1 sin presentar nombres internos como oficiales."
  - "Medir recursos, retrasos de reacción, hints y estados terminales simultáneos; confirmar XS integrado pasa xs-check."
  - "Comprobar rango de IDs contra juego/mods; registrar evidencia antes de stringRangeStatus=verified."

### S5 — Instalación y Return of Rome
- **Status**: pending
- **Files**: `tests/compatibility/distribution.json`, `tests/compatibility/return-of-rome.json`, `docs/qa/game-distribution.md`
- **Gate**: e2e
- acceptance:
  - "Instalar ZIP propio como mod local limpio, reiniciar, actualizar sin perder progreso; no tocar suscripciones ajenas."
  - "Return of Rome permanece experimental: comprobar datos/civilizaciones, archivo y posible consulta de claves entre modos antes de ampliar adaptador."
  - "Toda incompatibilidad crea propuesta específica asignada al arquitecto, con reproducibilidad; no improvisar dentro de contenido."

## acceptance

- Dos rutas con claves distintas, replay A/B en ambos órdenes, guardar/cargar antes de ganar y después de elegir.
- Campaña sucesora sin predecesora instalada: siempre jugable, aviso y recapitulación; con clave correcta desaparece recomendación.
- Registrar también ausencia de clave y cambio de idioma sin renombrar nombres del motor.
- Obtener códigos exactos de 17 carpetas de una instalación con build registrado.
- Probar 2,5,10 mods y prioridades invertidas, todos los alfabetos, cambios de idioma y actualización.
- Resolver colisión de archivos de cadenas mediante estrategia acreditada; revisar ADR antes de alterar compilador.
- Conservar plantilla nativa completa con fuente/build/licencia y tokens documentados; generar NAME.json y NAME_layout.json con --templates.
- Narrador general y particular antes/después de misión, subtítulo e imagen; audio WAV/WEM en rutas comprobadas.
- CampaignVariable en SequenceItems; ninguna condición cambia accesibilidad.
- Verificar xsGetDifficulty con UI de campaña y editor, perfiles easy>=3/standard=2/hard<=1 sin presentar nombres internos como oficiales.
- Medir recursos, retrasos de reacción, hints y estados terminales simultáneos; confirmar XS integrado pasa xs-check.
- Comprobar rango de IDs contra juego/mods; registrar evidencia antes de stringRangeStatus=verified.
- Instalar ZIP propio como mod local limpio, reiniciar, actualizar sin perder progreso; no tocar suscripciones ajenas.
- Return of Rome permanece experimental: comprobar datos/civilizaciones, archivo y posible consulta de claves entre modos antes de ampliar adaptador.
- Toda incompatibilidad crea propuesta específica asignada al arquitecto, con reproducibilidad; no improvisar dentro de contenido.
