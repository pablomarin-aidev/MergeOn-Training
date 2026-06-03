# Módulo 10 — MCPs y APIs

> Bloque B · Cómo se hablan los programas entre sí (API) y cómo un agente de IA usa
> herramientas externas de forma estándar (MCP). Esto explica por qué tú puedes **manejar
> MergeOn desde Claude** con solo chatear.

---

## 🎯 Objetivos

- Entender qué es una **API** y qué es un **endpoint**.
- Entender qué es un **MCP** y por qué le llaman "el USB-C de la IA".
- Distinguir **API** de **MCP** (cuándo es cada uno).
- Conectar esto con cómo tú administras MergeOn desde Claude.

---

## 💼 Por qué importa para tu trabajo

MergeOn tiene un **MCP**: por eso puedes pedirle a Claude *"créame un flow de bienvenida"* o
*"muéstrame las ventas de la semana"* y **funciona**. Entender el MCP te convierte en un socio
con un **superpoder**: administras la plataforma conversando, sin pelear con menús.

---

## 📚 Conceptos

### 1. Qué es una API

Una **API** es un "enchufe" estándar para que **dos programas se hablen**. Define qué le puedes
pedir a un sistema y cómo te responde.

**Analogía del restaurante:**
- Tú (una app) eres el cliente.
- El **menú** son las cosas que puedes pedir → cada plato es un **endpoint**.
- El **mesero** lleva tu pedido a la cocina y te trae el plato → eso es la API.
- La **cocina** (el servidor) prepara, pero tú no entras: solo pides por el menú.

Así, una app no necesita saber *cómo* funciona MergeOn por dentro; solo "pide del menú".

### 2. Endpoints, petición y respuesta

- **Endpoint:** una dirección que hace **una cosa**. Ej: "crear pedido", "listar productos".
- **Petición (request):** lo que pides, a veces con datos (ej: el producto y la cantidad).
- **Respuesta (response):** lo que el sistema te devuelve, normalmente en **JSON** (un formato
  de texto ordenado que los programas entienden).
- **Llave (API key):** muchas APIs piden una clave secreta para saber quién pide y dar permiso.

> MergeOn tiene su propia **API** (el backend). La interfaz que usan tus clientes y muchas
> integraciones (Shopify, Meta, Google) hablan con ella por endpoints.

### 3. Qué es un MCP

**MCP (Model Context Protocol)** es un **estándar abierto creado por Anthropic** para conectar
**agentes de IA** (como Claude) con **herramientas y datos externos** — sin tener que programar
una integración a medida para cada caso.

> Frase oficial: MCP es **"como un puerto USB-C para aplicaciones de IA"**. Así como el USB-C
> conecta cualquier dispositivo con un solo estándar, MCP conecta la IA con cualquier
> herramienta o dato con un solo estándar.

Un MCP ofrece tres tipos de cosas:
- **Tools (herramientas):** acciones que la IA puede ejecutar (ej: crear un flow).
- **Resources (recursos):** datos de solo lectura (ej: la lista de productos).
- **Prompts:** plantillas reutilizables.

### 4. API vs MCP (la diferencia clave)

| | API | MCP |
|---|---|---|
| ¿Para quién? | Para que **programas** se hablen | Para que **agentes de IA** usen herramientas |
| Estándar | Cada API es distinta | **Un solo estándar** para todas |
| Quién la consume | Otra app, programada a mano | Un cliente de IA (Claude) sin código a medida |

**No compiten.** Por debajo, un MCP normalmente **usa la API** del sistema. El MCP es la "capa"
que le presenta esas acciones a la IA de forma estándar y conversacional.

### 5. Cómo se junta en MergeOn

- MergeOn tiene una **API** (su backend) que hace todo: productos, pedidos, flows, CRM…
- MergeOn también tiene un **MCP** que expone esas acciones a Claude como **herramientas**.
- Por eso tú, desde Claude, puedes decir *"crea un flow que responda a la pauta X"* y Claude usa
  una herramienta del MCP (`flows_create`) que, por debajo, llama a la API de MergeOn.

Las **skills** que ya tienes instaladas (crear flows, crear prompts) funcionan justo sobre ese
MCP. Ahora entiendes **por qué** funcionan.

---

## 🔗 Documentación oficial

- **Qué es el Model Context Protocol (intro oficial)** — [modelcontextprotocol.io/docs/getting-started/intro](https://modelcontextprotocol.io/docs/getting-started/intro)
- **Especificación y docs de MCP (GitHub)** — [github.com/modelcontextprotocol/modelcontextprotocol](https://github.com/modelcontextprotocol/modelcontextprotocol)
- **Documentación de Claude Code** (donde se configuran MCPs) — [code.claude.com/docs](https://code.claude.com/docs/en/setup)

## 🎓 Cursos / videos gratis

- **Sitio oficial de MCP** (guías y ejemplos) — [modelcontextprotocol.io](https://modelcontextprotocol.io)
- **Building Effective AI Agents — Anthropic** (contexto de tools/agentes) — [anthropic.com/engineering/building-effective-agents](https://www.anthropic.com/engineering/building-effective-agents)

---

## ✍️ Práctica

1. Explica una API con la analogía del restaurante (cliente, menú, mesero, cocina) con tus
   palabras.
2. Di qué es un endpoint y da 3 ejemplos que tendría la API de una tienda.
3. Explica, en 2 frases, por qué puedes administrar MergeOn desde Claude (menciona MCP y que por
   debajo usa la API).

---

## 🤖 Prompt para Claude Code

```
Estudiemos el Módulo 10 (MCPs y APIs). Explícame qué es una API con la analogía del restaurante
y qué es un MCP con la analogía del USB-C. Luego pregúntame la diferencia entre los dos hasta que
la diga bien. Termina explicándome por qué yo puedo crear flows en MergeOn solo hablando contigo.
```

---

## ✅ Checklist de dominio

- [ ] Puedo explicar qué es una API con la analogía del restaurante.
- [ ] Sé qué es un endpoint y doy ejemplos.
- [ ] Puedo explicar qué es un MCP y la analogía del USB-C.
- [ ] Entiendo la diferencia entre API y MCP y que el MCP usa la API por debajo.
- [ ] Sé por qué puedo administrar MergeOn desde Claude.

---

⬅️ Anterior: [Módulo 9 — Práctica: tu primer agente](../09-practica-primer-agente/README.md)
➡️ Siguiente: [Módulo 11 — Qué hay detrás de MergeOn Seller](../11-detras-de-mergeon-seller/README.md)
