# Desarrollo y comandos

Bun 1.4.2; Python >=3.10; paquetes Python fijados con hashes en requirements.lock.txt. `python tools/python/setup.py` crea .venv, instala paquetes y compila rge_campaign externo con fuentes fijadas/hash. En Windows: MinGW con gcc disponible o RGE_CAMPAIGN_BIN. COF_PYTHON sirve para un intérprete aislado alternativo. No incluir rutas personales en archivos versionados.

| Comando | Resultado y fallos |
|---|---|
| bun run validate | Tipado, lint, tests, docs y campañas; cualquier error devuelve código distinto de cero |
| bun run check | TypeScript estricto y Biome |
| bun run test | Tests sin el juego |
| bun run build | IR para todas las campañas; no promete archivos jugables |
| bun run campaign:build ID | IR y catálogos en build/ID |
| bun run campaign:build ID --export | Perfil binario real, round-trip y ZIP etiquetado fixture |
| bun run campaign:build ID --export --templates | Exporta usando manifest nativo acreditado; falla si no existe |
| bun run campaign:candidate ID | ZIP candidato y reporte de hash/vigencia; exige plantillas reales |
| bun run audio:build ID --locale=es-ES | Voz/grabaciones locales, PCM normalizado y SRT; falla sin proveedor |
| bun run test:export | Exportación real del fixture técnico; requiere Python y rge |
| bun run schema:export | JSON Schema generado desde los mismos contratos |
| bun run ids:allocate | Añade IDs; no sustituye IDs existentes; revisar diff |
| bun run campaigns:list | Catálogo registrado |
| bun run campaign:validate [ID] | Integridad del proyecto y campaña seleccionada |
| bun run staging:check ID [--partial] | Esquemas de borrador; enumera pendientes, exige bundle completo sin --partial; ver staging.md |
| bun run docs:check | Documentos obligatorios y enlaces locales |
| bun run i18n:check [ID] | Claves, variables, marcadores y codificación |
| bun run assets:check [ID] | Existencia, hash, PNG y metadatos |
| bun run audio:check [ID] | Audio PCM WAV válido |
| bun run release:check [ID] | Rechaza datos no aprobados o evidencias de juego pendientes |

Los builds limpian exclusivamente su propia carpeta mod para evitar recursos obsoletos. sourceFile verifica enlaces simbólicos y rutas contenidas. No importes ZIP o campañas binarios de origen desconocido en rge_campaign: su uso está limitado a contenedores propios recién generados. Nunca introducir credenciales en contenido ni usar shell para una voz.

## Portabilidad del validador XS

La wheel fijada contiene xs-check ELF Linux y xs-check.exe Windows, sin binario Mach-O. La validación de contratos/CLI se ejecuta en los tres SO en CI; el round-trip con XS se configura para Linux/Windows. macOS necesita COF_XS_CHECK_BIN compatible 0.1.2–0.2.30 y la exportación falla explícitamente sin él. No se desactiva xs-check ni se aprueba syntax inválida: raise_on_error está activado. La compilación/acreditación macOS se registra en s00001-S5 antes de anunciar soporte nativo probado. No se ha ejecutado CI remota ni ese binario macOS aquí.
