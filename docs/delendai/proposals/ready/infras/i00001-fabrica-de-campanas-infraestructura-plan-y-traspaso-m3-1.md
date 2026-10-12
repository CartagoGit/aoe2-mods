---
id: i00001
title: "Fabrica de campanas: infraestructura, plan y traspaso M3.1"
kind: infra
status: ready
type: proposal
track: general
date: 2026-10-12
---

# i00001 — Fabrica de campanas: infraestructura, plan y traspaso M3.1

## goal

Implementar el sistema de producción descrito en el encargo: contratos versionados; compiladores y CLI Bun/TypeScript/Python; localización semántica; historia y QA; medios; exportación real con fixtures; documentación y propuestas de contenido para MiniMax M3.1. Plan secuencial: investigar/adoptar; cerrar arquitectura; construir y probar; auditar; entregar backlog y prompts. No generar campañas históricas completas.

## why

Repositorio sin infraestructura. La conversación final exige mods independientes, continuidad opcional, narradores general y por campaña, documentación española y producción multiplataforma. Reutilizar bibliotecas del ecosistema y no inventar formatos del motor.

## non-goals

- Publicar mods o modificar ejecutable/perfil del juego.
- Construir gestor externo Angular/Tauri descartado en la conversación.
- Afirmar GAME VERIFIED sin ejecutar AoE2.

## slices

- global_gate: e2e

### S1 — Bootstrap, investigación, arquitectura e implementación verificable
- **Status**: pending
- **Files**: `package.json`, `bun.lock`, `tsconfig.json`, `biome.json`, `AGENTS.md`, `config/**`, `packages/**`, `tools/**`, `tests/**`, `campaigns/**`, `assets/**`, `requirements*.txt`, `delendai.config.json`, `README.md`, `CONTRIBUTING.md`, `LICENSE*`, `.editorconfig`, `.gitattributes`, `.gitignore`, `.github/**`, `.claude/**`, `.codex/**`, `.delendai/project-profile.json`, `docs/**`
- **Gate**: e2e
- acceptance:
  - "bun run validate: tipado/lint/tests/documentación/localización y fixtures; prueba Python round-trip real."
  - "Propuestas oficiales con slices, alcance/dependencias/aceptación/fuentes y límites; prompts de inicio y continuación."
  - "Separar BASE READY/EXPORT READY/GAME VERIFIED/PRODUCTION READY; registrar limitaciones y revisión independiente."

## acceptance

- bun run validate: tipado/lint/tests/documentación/localización y fixtures; prueba Python round-trip real.
- Propuestas oficiales con slices, alcance/dependencias/aceptación/fuentes y límites; prompts de inicio y continuación.
- Separar BASE READY/EXPORT READY/GAME VERIFIED/PRODUCTION READY; registrar limitaciones y revisión independiente.
