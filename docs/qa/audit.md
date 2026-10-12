# Auditoría de infraestructura

Fecha: 2026-10-12. Implementador GPT-6; revisor formal independiente GPT-6.1 (identidad de host gpt-6.1-sol). BASE READY alcanzado: código integrado, gate certificado, revisión formal publicada e i00001 cerrada oficialmente. f00001 está ready; su S1 es la primera tarea designada para MiniMax M3.1.

## Alcance construido

Contratos estrictos versionados, carga con rutas contenidas, catálogos/IDs/glosario, validadores de historia/gameplay, compiladores IR, adapter Python y contenedor externo fijados, medios con hashes/licencias, voces offline intercambiables/caché, normalización PCM/subtítulos, CLI, JSON Schema, CI Linux/Windows/macOS, guías/wiki, dossier imperial-church y cinco propuestas oficiales con 20 slices. El fixture es técnico; no se han implementado campañas históricas completas.

## Verificación

41 tests,124 expectativas y cero fallos. Tres round-trips reales de escenarios y contenedores, incluido rutas/oleada finita/PER/terreno; Return of Rome y release prematura se rechazan. Se reabren escenarios y se extraen exclusivamente contenedores propios. Los hashes y comandos están en verification.json. Se ejecutó además la validación propia de DelendAI, con resultado declarado/pasado y evidencia journalled para el cierre.

El gate oficial ejecutó instalación frozen y bun run validate sobre el merge, primero para fuente y después para veredicto. Los reportes regenerables viven en build y dist; el ZIP fixture no se publica como mod de producción. No prometer determinismo de bytes del parser: el ZIP fija orden/fecha de entradas, pero depende de sus bytes.

No se ha ejecutado AoE2 ni CI remota. Hay dos catálogos draft de muestra, cero catálogos aprobados y cero recursos/doblajes de producción. No se ha llamado a proveedores pagados ni publicado mods.

## Revisión y correcciones

La primera instancia independiente identificó ocho fallos y confirmó sus correcciones. GPT-6.1 revisó código, documentación, handoffs y los 20 slices, ejecutó 41/41 tests y tres round-trips, sin hallazgos bloqueantes. Ver [informe independiente](independent-review.md).

Caché de voces separada por ID/configuración/version/licencia; huella de candidato vinculada a motor/locks/generadores TS/Python; destinos portables y sin colisiones locales/globales; WAV con chunks/frames/alineación íntegros; progreso final obligatorio; IDs únicos de eventos/reservas/QA/evidencias; política de 17 locales y carpetas únicas; staging y materialización conjunta con IDs/glosario. Los slices mantienen validación global pasando.

También se ajustaron Files a rutas literales, porque el runtime comprueba existencia sin expandir comodines. Los snapshots staging se conservan hasta cerrar toda la propuesta. Esto permite cerrar las fases preparatorias sin referencias perdidas; no cambia arquitectura ni crea contenido histórico.

## Integración y cierre reales

El WIP incorporó develop tras la corrección del usuario y conservó su trabajo. El gate inicial faltaba en HEAD de develop, por lo que DelendAI rechazó publicar. El propietario autorizó explícitamente una excepción limitada: commit4139908a3941897103ddff8ded27f5d4f6d2b3ef añade solo validationMatrix.scopes.project con frozen install y validate. Ningún otro código se integró manualmente.

DelendAI integró la infraestructura con gate pasado en 69cf3e72ecdfb952d0cc7998790544cb73305068. El runtime exige aprobar lo ya integrado: GPT-6.1 registró approve sobre ese hash; commit de veredicto6d17864eabde271ee5255dd9d2a618478a3bbdf1, integrado mediante su publicación oficial en 5ae5d2c47902ebb63617ccaf0ddab066443030f2, también con gate pasado. i00001/S1 está done, implementer=gpt-6,reviewer=gpt-6.1-sol. La propuesta recorrió in-progress→review→done según el DFA; no se editó su estado a mano.

## Estados y siguientes responsables

BASE READY alcanzado. EXPORT READY acreditado para el subconjunto binario del fixture. GAME VERIFIED y PRODUCTION READY pendientes; esa distinción se aplica también al traspaso.

f00001/S1: MiniMax completa dossier/matriz del piloto técnico; S2 prepara dos bundles, S3 materializa fuentes/IDs/glosario juntos y S4 registra QA. s00001 requiere tester con AoE2 para progreso entre mods, guardados, 17 carpetas/coexistencia/rango, templates slideshow/layout/audio, dificultad/terminal e instalación. f00002 y f00003 conservan sus dependencias y permanecen blocked. No transferir esas decisiones de infraestructura al autor de contenido.

La wheel XS fijada no contiene binario macOS: [COF_XS_CHECK_BIN y alcance de CI](../guides/development.md). No se desactiva la comprobación; s00001-S5 acredita soporte nativo macOS. Toda mecánica fuera del DSL exige ampliación revisada antes de su misión.

Ver [trazabilidad](../production/requirements-traceability.md), [capacidades](../research/aoe2-capabilities.md), [START](../handoffs/MINIMAX-M3.1-START.md) y [staging](../guides/staging.md). La fuente actual de estados es DelendAI; recuperar sus propuestas/unidades/locks antes de comenzar. Una copia local de revisión no sustituye un worktree oficial.
