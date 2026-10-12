# Auditoría de infraestructura

Fecha: 2026-10-12. Agente implementador: GPT-6. Esta auditoría interna revisa la fábrica; no reemplaza la revisión independiente exigida por DelendAI.

## Alcance construido

Contratos estrictos versionados, carga con rutas contenidas, catálogos/IDs/glosario, validadores de historia/gameplay, compiladores IR, adapter Python y contenedor externo fijados, medios con hashes/licencias, voces offline intercambiables y caché, normalización PCM/subtítulos, CLI, JSON Schema, CI Linux/Windows/macOS, guides/wiki, dossier imperial-church y cinco propuestas oficiales iniciales con slices. El fixture es técnico y no constituye una campaña histórica.

## Hallazgos corregidos

Base del WIP incorporada desde develop tras la corrección del usuario. Se corrigieron escapes de strings, campos nativos según la API del parser, sintaxis XS y permiso ejecutable de xs-check en la wheel Unix; se mantuvo su comprobación activa. Se añadieron referencias cerradas, reserva acumulada de eventos, terminal común/rutas, control de symlinks, validación real de glosario, cache corrupta regenerable, audio por línea/idioma y recursos con destino nativo.

La auditoría detectó que faltaba un candidato publicable diferenciado del ZIP fixture: campaign:candidate genera ZIP con plantillas acreditadas y reporte de hash/vigencia; release:check exige esa evidencia y rechaza contenido obsoleto. Se añadieron los seis paneles de mensajes localizados y nombres de unidades/facciones por string_id, comprobados al reabrir. Se unificó la compilación de condiciones de objetivos y eventos; llegada a áreas, saldo de recursos, diplomacia y tributos permiten misiones de negociación/economía sin formatos nuevos. Se exige saldo suficiente y costes agregados para tributos finitos. Los terrenos/elevaciones, tecnologías y spawns se validan contra el catálogo real y se comprueba persistencia del terreno al reabrir el escenario.

## Evidencia reproducible

La última validación supera 33 tests, 74 expectativas y cero fallos. La exportación supera tres round-trips de escenarios/contenedores, incluyendo las variantes; Return of Rome se rechaza. Los comandos, hashes y límites están en verification.json. bun run validate incluye tipado, Biome, pruebas y comprobación de docs/campañas. test:export produce el fixture principal más variantes de rutas/oleada finita/PER/terreno, reabre escenarios y extrae contenedores propios. Return of Rome y release prematura deben fallar explícitamente. Los reportes privados regenerables están en build/; ZIPs en dist/ y no se versionan.

No se ha ejecutado AoE2 en este entorno ni los runners remotos de los tres SO. No se ha llamado a proveedores pagados, generado doblaje histórico, publicado mods ni acreditado 17 traducciones. No prometer determinismo de bytes del parser; el ZIP fija orden y fecha de entradas, pero depende de esos bytes.

## Estado por nivel

EXPORT READY para el subconjunto binario del fixture cuando supera test:export. BASE READY queda pendiente de revisión independiente y de integración oficial. GAME VERIFIED y PRODUCTION READY no alcanzados. La propuesta de compatibilidad y las propuestas de contenido contienen los pendientes externos; una ausencia de evidencia no equivale a un resultado positivo.

## Bloqueos y siguiente responsable

El perfil exige gate en el HEAD de develop; la declaración en el candidato no satisface el bootstrap. Se comprobará el estado real y la publicación oficial; un rechazo se registrará aquí y se preservará la ref de la unidad. El implementador no hace commits/push manuales de develop ni autoaprueba. El propietario/runtime debe resolver un bootstrap legítimo y un revisor distinto debe revisar el commit.

s00001 requiere AoE2 para progresión entre mods, guardados, coexistencia de textos/17 carpetas/rango, templates slideshow/layout/voz, dificultad y RoR. f00001/f00002/f00003 desarrollan contenido posteriormente; ver NEXT-PROPOSALS. Toda mecánica futura fuera del DSL actual exige una ampliación de infraestructura revisada, antes de su misión.

La trazabilidad completa se encuentra en [requirements-traceability](../production/requirements-traceability.md). Las decisiones y fuentes se encuentran en [capabilities](../research/aoe2-capabilities.md); los prompts están en [START](../handoffs/MINIMAX-M3.1-START.md).

El XS incluido por la wheel no es nativo macOS. Ver [portabilidad y requisito COF_XS_CHECK_BIN](../guides/development.md); CI valida contratos en tres SO y el round-trip nativo en Linux/Windows. La acreditación macOS está asignada a s00001-S5.

## Resultado de integración y recuperación

La publicación oficial fue rechazada: develop (283173341452cd4943470280e0334fa020b76eac) no declara validationMatrix.scopes ni un script validate. El runtime no certifica una política que solo aparece en el candidato. No se modificó develop para eludir esta condición. La entrega se presentó oficialmente a revisión: i00001/S1 está in_review, implementer=gpt-6, sin reviewer ni aprobación. Commit de código sometido: ae2171aed68ad1bcede6238e428265a286dc6a88. Los commits siguientes solo registran revisión/rechazo y recuperación.

Resolución legítima del bootstrap: el propietario/runtime debe incorporar el gate en el HEAD de develop. El bloque concreto ya está en delendai.config.json del candidato: validationMatrix.scopes.project contiene bun install --frozen-lockfile y bun run validate. Una vez declarado, recuperar la ref conservada mediante el workflow oficial, reconciliar develop sin reescribir historia, resolver revisión independiente y volver a publicar. No hacer push/merge manual de develop desde un agente. Las pruebas de exportación se exigen además en la propuesta de infraestructura y CI compatible.

En una unidad aislada se hace commit con Git en esa unidad. work checkpoint opera sobre el checkout compartido cuando se invoca desde el servidor; no debe utilizarse para capturar una unidad distinta. Se detectó que ese checkpoint recogía solo dos archivos compartidos; se conservó todo el contenido con un commit completo en el WIP y se verificó la base y ausencia de cambios pendientes antes de entregar. Las propuestas mantienen los estados emitidos por sus herramientas oficiales.

Mientras el bootstrap y revisión falten, no iniciar el traspaso productivo a M3.1. START contiene el prompt completo para cuando la base quede revisada/integrada. La retirada conservadora de la unidad, si procede, preserva el tip en una ref retired y un dossier local de revisión; no significa aprobación ni abandono de los requisitos pendientes.
