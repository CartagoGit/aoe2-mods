# Producción de audio

VoiceProvider desacopla sintetizadores. RecordedVoiceProvider admite grabación humana; CommandVoiceProvider llama una herramienta local mediante argv, recibe AudioRequest JSON por stdin y exige WAV PCM por stdout. El proveedor debe declarar versión y licencia; el hash de grabación forma parte de su versión. No hay backend pagado ni voz generada masivamente.

produceAudio usa hash de texto, locale, voz, interpretación, rate, pronunciación e identidad/versión/licencia del proveedor. CommandVoiceProvider conserva el ID configurado e incorpora executable/argv en esa identidad; IDs duplicados y el ID reservado recorded fallan. Cambiar pesos/modelo requiere actualizar la versión. Las sustituciones humanas invalidan caché por contenido. inspectWav comprueba RIFF exacto, chunks completos con padding, un único formato PCM, canales, rate, byte rate, blockAlign y frames completos; subtitles produce SRT con duraciones reales.

El pipeline puede incorporar TTS local mediante un ejecutable que cumpla el puerto; un proveedor remoto requiere propuesta propia, presupuesto y autorización. La reproducibilidad de una síntesis depende del modelo/proveedor y seed, no solo de una caché. El manifiesto registra permiso, autor, coste, hash y aprobación.

Normalizar y convertir en producción con una herramienta fijada y registrar parámetros; WAV validado no acredita reproducción en todos los caminos AoE2. WEM/Wwise y rutas de voiceover requieren pruebas de motor. Los audios finales se distribuyen offline. Si el tamaño obliga a paquetes de voz separados, deben ser opcionales por idioma y conservar subtítulos completos en el mod principal.

`bun run audio:build ID --locale=es-ES` produce WAV normalizado a pico configurable, SRT y manifiesto de voz/hash/duración/licencia. Las grabaciones se vinculan mediante asset.lineId y asset.locale; no reutilizar el mismo audio español para los demás idiomas. Un proveedor local se declara en config/audio-providers.json y debe existir/licenciarse; la ausencia falla explícitamente. La normalización PCM peak implementada no se presenta como LUFS.
