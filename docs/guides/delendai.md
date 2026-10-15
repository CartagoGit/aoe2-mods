# DelendAI y recuperación de contexto

Este repositorio se ha adoptado mediante el servidor conectado. La configuración y agentes generados son wiring; no copias del runtime. Usar overview, catálogo/búsqueda de capacidades y detalle de esquema servido por el runtime. No conservar listas de herramientas estáticas ni asumir IDs de propuestas entre sesiones.

Abrir una unidad oficial basada en develop, reclamar archivos, validar, entregar a revisión independiente y publicar mediante el workflow declarado. Guardar checkpoints y estado con las herramientas actuales. Una propuesta sin ID se crea dentro de una unidad de creación oficial; nunca redactar frontmatter o mover carpetas por cuenta propia.

En la versión instalada, la revisión técnica puede comprobar el WIP, pero approve exige que evidence.commitHash ya pertenezca a develop. Secuencia acreditada: validación y revisión técnica → work publish con gate declarado en HEAD de develop → unidad review propia de otro modelo real → aprobación formal del hash integrado → publicación del veredicto/cierre según runtime. No usar el SHA de develop para acreditar otro commit ni inventar sufijos de agente. La identidad es el ID literal del modelo declarado por el host; review es el kind de unidad.

Files se comprueba mediante rutas literales, incluidos directorios; no se expanden comodines. Declarar los ámbitos reales de cada slice y mantenerlos disponibles hasta el cierre global. Los locks son una capacidad distinta y pueden aceptar patrones. Las transiciones siguen el DFA servido: in-progress pasa por review antes de done; no forzar ni editar estados a mano.

Si una sesión se interrumpe: leer AGENTS y handoffs; consultar Git, unidad y locks; localizar el slice propio, su commit y gate; reconciliar develop sin reescribir trabajo compartido; continuar únicamente el alcance concedido. No repetir una operación con rechazo permanente sin resolver la causa.

El perfil actual exige un gate declarado en el HEAD de develop antes de aceptar merges. Declararlo solo dentro del candidato no satisface esa política. Si el repositorio de arranque no lo tiene, la integración queda bloqueada hasta bootstrap legítimo por el propietario; no omitirlo ni hacer push manual de develop.

Cuando se trabaja en el worktree que imprime work enter, hacer git add/commit únicamente dentro de él, con identidad real y alcance revisado. work checkpoint desde el MCP sin checkout captura el checkout compartido; no usarlo como sustituto de commit en otra unidad. La recuperación del trabajo retirado y su ref se consulta al runtime; nunca confundir el dossier local de revisión con una unidad editable.
