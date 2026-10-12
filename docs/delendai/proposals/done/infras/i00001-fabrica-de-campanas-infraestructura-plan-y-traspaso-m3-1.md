---
id: i00001
title: "Fabrica de campanas: infraestructura, plan y traspaso M3.1"
kind: infra
status: done
type: proposal
track: general
date: 2026-10-12
last-transition-id: 0b1a5610-b4e6-4f65-a4e6-fffcd5bbacaa
last-correlation-id: 0b1a5610-b4e6-4f65-a4e6-fffcd5bbacaa
last-transition-from: review
last-transition-at: 2026-10-12T11:57:19.896Z
shipped-in:
  - "69cf3e72ecdfb952d0cc7998790544cb73305068"
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
- **Status**: done
- **Files**: `package.json`, `bun.lock`, `tsconfig.json`, `biome.json`, `AGENTS.md`, `config`, `packages`, `tools`, `tests`, `campaigns`, `requirements.lock.txt`, `delendai.config.json`, `README.md`, `CONTRIBUTING.md`, `LICENSE`, `LICENSE-CONTENT.md`, `.editorconfig`, `.gitattributes`, `.gitignore`, `.github`, `.claude`, `.codex`, `docs`
- **Gate**: e2e
- acceptance:
  - "bun run validate: tipado/lint/tests/documentación/localización y fixtures; prueba Python round-trip real."
  - "Propuestas oficiales con slices, alcance/dependencias/aceptación/fuentes y límites; prompts de inicio y continuación."
  - "Separar BASE READY/EXPORT READY/GAME VERIFIED/PRODUCTION READY; registrar limitaciones y revisión independiente."
- review-state: done
- review-implementer: gpt-6
- review-reviewer: gpt-6.1-sol
- review-log: approved by gpt-6.1-sol — verified at 69cf3e72ecdf, validate exit 0, tests 41/41 — Revisión formal independiente por gpt-6.1-sol, distinto del implementador gpt-6. Código e4f5fc9 validado independientemente y documentación 6a4e0bf revisada; el árbol del hash oficialmente integrado 69cf3e72ecdfb952d0cc7998790544cb73305068 es idéntico a 6a4e0bf (git diff vacío). Incorporado origin/develop mediante merge en unidad review propia. Sin hallazgos bloqueantes. Bootstrap autorizado aplicado y work publish/gate oficial completados según certificación; no se falsea evidencia de AoE2,CI remota,traducciones ni medios. No hay campañas históricas completas implementadas.
- shipped-in: `69cf3e72ecdf`

## acceptance

- bun run validate: tipado/lint/tests/documentación/localización y fixtures; prueba Python round-trip real.
- Propuestas oficiales con slices, alcance/dependencias/aceptación/fuentes y límites; prompts de inicio y continuación.
- Separar BASE READY/EXPORT READY/GAME VERIFIED/PRODUCTION READY; registrar limitaciones y revisión independiente.
