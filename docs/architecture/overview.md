# Arquitectura

```mermaid
flowchart LR
  A[Campañas JSON y fuentes históricas] --> B[Contratos Zod]
  B --> C[Validadores]
  C --> D[Compiladores TypeScript]
  D --> E[IR y catálogos de textos]
  E --> F[Adaptador Python]
  F --> G[AoE2ScenarioParser]
  G --> H[rge_campaign externo]
  H --> I[Mod independiente]
  J[Voces y recursos licenciados] --> C
  I --> K[Pruebas reales en AoE2]
  K --> L[Gate de release]
```

## Responsabilidades

| Directorio | Propiedad |
|---|---|
| packages/core | Diagnósticos, hashes, escritura atómica y rutas contenidas |
| packages/schemas | Contratos estrictos versionados |
| packages/localization | Claves, placeholders, marcadores, lock y exportación UTF-8 |
| packages/historical-validation | Fuentes, afirmaciones y trazabilidad narrativa |
| packages/gameplay-validation | Referencias, objetivos, economía finita, grafo y conectividad |
| packages/scenario-compiler | IR de escenarios con IDs de textos y variables |
| packages/campaign-compiler | Integridad de campaña, narradores y composición de IR |
| packages/audio | Puerto VoiceProvider, grabaciones, comando local, WAV, cache y SRT |
| packages/assets | Hashes, procedencia, licencias y resolución PNG |
| packages/aoe2-adapter | Ejecución del puente y vinculación de plantillas nativas |
| tools/cli | Carga del proyecto, comandos y políticas de release |
| tools/python | Instalación aislada, escenarios, contenedor y ZIP |
| campaigns | Especificaciones editables; una carpeta por campaña |
| docs/wiki | Evidencia histórica y diseño por campaña |

La entrada y el IR son formatos propios, identificados como tales. Nunca se presentan como JSON reconocido por AoE2. El adaptador falla ante capacidades no implementadas. Las plantillas nativas deben proceder de archivos reales y conservar su estructura, con tokens @cdf para claves y valores.

Los módulos son unidades de responsabilidad, no microservicios ni paquetes npm publicados. Las dependencias fluyen de compiladores a validadores y contratos; los validadores no invocan el juego. Los proveedores multimedia no forman parte del mod que juega el usuario.

El build no modifica campañas ni el lock. La asignación de IDs es un comando explícito revisable. Los artefactos incluyen hash de la fuente, locales utilizados y límites de exportación. La publicación externa de mods es un paso humano separado de la integración Git.
