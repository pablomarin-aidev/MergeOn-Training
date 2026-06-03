# Glosario

Diccionario de bolsillo del curso. Cuando veas una palabra que no entiendas, búscala aquí.
Si aún no queda claro, pídele a Claude: *"Explícame [término] del glosario con un ejemplo"*.

---

## Meta y WhatsApp

**Meta** — La empresa dueña de Facebook, Instagram y WhatsApp.

**Portafolio comercial (Business Portfolio)** — El "maletín" donde un negocio guarda y
organiza todos sus activos digitales en Meta (páginas, cuentas de Instagram, números de
WhatsApp, cuentas publicitarias, apps). Antes se llamaba **Business Manager**.

**Meta Business Suite** — La herramienta para gestionar el día a día (mensajes, publicaciones,
anuncios) de tu negocio en Facebook e Instagram desde un solo lugar.

**Activo (asset)** — Cada pieza que vive en tu portafolio: una página, una cuenta publicitaria,
un número de WhatsApp, un pixel, etc.

**WABA (WhatsApp Business Account)** — La cuenta de WhatsApp Business *de plataforma* (API),
distinta de la app de WhatsApp Business del celular. Es la que usan los sistemas como MergeOn.

**Verificación de negocio (Business Verification)** — Proceso en que Meta confirma que tu
empresa es real y legal, pidiéndote documentos. Desbloquea funciones avanzadas.

**App / Aplicación de Meta** — Un proyecto técnico dentro de Meta for Developers que conecta
tu software (como MergeOn) con WhatsApp, Instagram o Messenger.

**App Review (Revisión de Apps)** — Proceso en que Meta revisa que tu app use sus permisos de
forma correcta antes de dejar que la use el público.

**Permiso (permission / scope)** — Autorización específica que una app pide para hacer algo
(por ejemplo, "leer mensajes de WhatsApp"). Cada permiso sensible pasa por App Review.

**Token (de acceso)** — Una "llave" digital que la app usa para identificarse ante Meta y
poder actuar (enviar mensajes, leer datos). Es secreta.

**Opt-in** — El permiso explícito que da una persona para recibir mensajes de WhatsApp de un
negocio. Sin opt-in, no se debe enviar.

**Plantilla / Template** — Mensaje de WhatsApp pre-aprobado por Meta que se puede enviar fuera
de la ventana de 24 horas.

**Ventana de 24 horas** — Periodo tras el último mensaje del cliente en el que el negocio puede
responder con mensajes libres. Pasadas 24h, solo se puede contactar con plantillas aprobadas.

---

## Anuncios y medición

**Ad / Anuncio** — La pieza publicitaria que se muestra al usuario.

**Campaña** — La estructura que agrupa tus anuncios y define el **objetivo** (mensajes, ventas,
leads, etc.).

**Objetivo de campaña** — Lo que le pides a Meta que optimice (conseguir conversaciones, ventas,
clics...). Elegir el objetivo correcto es clave.

**CTWA (Click-to-WhatsApp Ads)** — Anuncios que, al hacer clic, abren un chat de WhatsApp con
el negocio. Son la base del negocio de MergeOn.

**Pixel** — Pieza de código en una página web que registra lo que hacen los visitantes (ver
producto, comprar). Sirve para medir y optimizar anuncios.

**Evento (de conversión)** — Una acción valiosa que se reporta a Meta: un lead, una compra, etc.

**CAPI (Conversions API)** — Forma de enviar esos eventos a Meta **desde el servidor** (no desde
el navegador), de manera más confiable. Para mensajería conecta lo que pasa *dentro del chat de
WhatsApp* con la pauta. (Módulo 6.)

**ROAS (Return on Ad Spend)** — Retorno de la inversión publicitaria: cuántos pesos vendes por
cada peso que gastas en pauta.

**CPL (Cost per Lead)** — Cuánto te cuesta conseguir un contacto interesado (lead).

**Lead** — Un contacto interesado que aún no ha comprado.

---

## IA y tecnología

**IA / Inteligencia Artificial** — Software capaz de tareas que antes requerían a un humano.

**LLM (Large Language Model)** — Modelo de lenguaje grande (como Claude o GPT). El "cerebro"
que entiende y genera texto. No "sabe" hacer cosas por sí solo: necesita herramientas.

**Chatbot** — Programa que responde mensajes siguiendo reglas o respuestas fijas.

**Agente de IA** — Un paso más allá del chatbot: un LLM que **decide solo** qué pasos dar y qué
**herramientas** usar para cumplir un objetivo. (Módulo 7.)

**Herramienta / Tool** — Una acción concreta que un agente puede ejecutar: buscar un producto,
crear un pedido, consultar stock. El LLM elige cuándo usarla.

**Prompt** — Las instrucciones que le das a un LLM o agente para que se comporte de cierta forma.

**LangChain** — Librería de Python para construir aplicaciones con LLMs y agentes. (Módulo 8.)

**`create_agent`** — Función de LangChain que crea un agente listo para usar, dándole un modelo
y una lista de herramientas. (Módulo 8.)

**LangGraph** — Motor sobre el que corren los agentes de LangChain; permite flujos más complejos.
Es lo que usa el bot de MergeOn por dentro.

**API** — "Enchufe" estándar para que dos programas se hablen entre sí. (Módulo 10.)

**Endpoint** — Una dirección específica de una API que hace una cosa (por ejemplo,
"crear pedido" o "listar productos").

**MCP (Model Context Protocol)** — Estándar abierto (creado por Anthropic) para conectar
agentes de IA con herramientas y datos externos, sin código a medida para cada integración.
"El USB-C de la IA". (Módulo 10.)

**Webhook** — Aviso automático que un sistema le manda a otro cuando pasa algo (por ejemplo,
"llegó un mensaje nuevo"). Es como un timbre que suena solo.

**JSON** — Formato de texto para intercambiar datos entre programas. Lo verás en APIs y MCP.
