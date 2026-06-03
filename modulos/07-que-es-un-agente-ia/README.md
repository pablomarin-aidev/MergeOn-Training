# Módulo 7 — ¿Qué es un agente de IA?

> Bloque B · Aquí empieza la parte "de adentro". MergeOn es, en el fondo, un **agente de IA que
> vende**. Si entiendes qué es un agente, entiendes el corazón del producto.

---

## 🎯 Objetivos

- Saber qué es un **LLM** y por qué solo no basta.
- Diferenciar un **chatbot** de un **agente de IA**.
- Entender qué son las **herramientas (tools)** y el **bucle** de un agente.
- Distinguir **flujos (workflows)** de **agentes**, y ver dónde está cada uno en MergeOn.

---

## 💼 Por qué importa para tu trabajo

Cuando un cliente te pregunta *"¿esto es un bot?"*, la respuesta correcta no es "sí". Es:
*"es un **agente de IA**, que es mucho más: decide, busca, arma pedidos y atiende como un
vendedor real"*. Entender la diferencia te deja **vender mejor** y **configurar mejor**.

---

## 📚 Conceptos

### 1. El LLM: un cerebro que solo habla

Un **LLM** (modelo de lenguaje grande, como Claude o GPT) es buenísimo entendiendo y generando
texto. Pero por sí solo **no puede hacer nada en el mundo**: no consulta tu catálogo, no crea
pedidos, no sabe el stock. Es un cerebro sin manos.

### 2. Chatbot vs. Agente

| | Chatbot tradicional | Agente de IA |
|---|---|---|
| Cómo responde | Respuestas fijas / árbol de opciones | Decide en el momento |
| Flexibilidad | Rígido ("escribe 1, 2 o 3") | Conversa natural y se adapta |
| Puede actuar | No, o muy limitado | Sí: **usa herramientas** |
| Si preguntas algo raro | Se pierde | Razona y responde |

**Analogía:** un chatbot es una **máquina dispensadora** (botones fijos: si aprietas A, sale A).
Un agente es un **buen vendedor**: lo saludas como quieras, te entiende, busca lo que pides,
arma tu pedido y resuelve imprevistos.

### 3. Qué es un agente (definición seria)

Según Anthropic, un **agente** es un sistema donde el LLM **dirige por sí mismo** sus pasos y
**decide qué herramientas usar** para lograr un objetivo. Planea, decide, usa herramientas,
pregunta si le falta información y reconoce cuándo terminó — **sin un guion fijo**.

### 4. Las herramientas (tools): las manos del agente

Una **herramienta** es una acción concreta que el agente puede ejecutar. En una tienda:

- `buscar_producto` — consultar el catálogo
- `crear_pedido` — registrar una venta
- `consultar_envio` — ver costos de envío

El LLM (cerebro) **decide cuándo** usar cada herramienta (manos). Esa combinación = agente.

> Dato MergeOn: el agente que atiende a los compradores tiene **16 herramientas** (buscar
> productos, crear pedidos, escalar a un humano, cambiar el estado del lead, etc.).

### 5. El bucle del agente

Un agente trabaja en un ciclo, como un humano resolviendo algo:

```
   piensa  →  elige una herramienta  →  observa el resultado
      ▲                                        │
      └────────────────────────────────────────┘
            (repite hasta tener la respuesta)
                          │
                          ▼
                  responde al cliente
```

### 6. Flujos (workflows) vs. agentes

No todo necesita un agente. Anthropic distingue:

- **Flujo (workflow):** pasos **predefinidos** en código. Predecible y barato. Ideal cuando la
  respuesta es siempre la misma.
- **Agente:** el LLM **decide** sobre la marcha. Flexible. Ideal cuando hace falta razonar.

**En MergeOn conviven los dos:**
- Los **flows** (los que viste en la skill de flows) son **workflows**: rápidos, sin gastar IA,
  para respuestas predecibles (responder a una pauta, confirmar una venta).
- El **bot vendedor** es un **agente**: razona y cierra ventas cuando la charla lo amerita.

Saber cuándo usar cada uno es clave para montar un sistema eficiente (y barato) a tu cliente.

---

## 🔗 Documentación oficial

- **Building Effective Agents — Anthropic** (la referencia base) — <a href="https://www.anthropic.com/engineering/building-effective-agents" target="_blank" rel="noopener">anthropic.com/engineering/building-effective-agents</a>
- **Building Effective AI Agents (recursos)** — <a href="https://resources.anthropic.com/building-effective-ai-agents" target="_blank" rel="noopener">resources.anthropic.com/building-effective-ai-agents</a>

## 🎓 Cursos / videos gratis

- **AI Agents in LangGraph — DeepLearning.AI** (gratis, con el fundador de LangChain) — <a href="https://www.deeplearning.ai/courses/ai-agents-in-langgraph" target="_blank" rel="noopener">deeplearning.ai/courses/ai-agents-in-langgraph</a>
- **Functions, Tools and Agents with LangChain — DeepLearning.AI** — <a href="https://www.deeplearning.ai/courses/functions-tools-agents-langchain" target="_blank" rel="noopener">deeplearning.ai/courses/functions-tools-agents-langchain</a>

---

## ✍️ Práctica

1. Explica con la analogía de la máquina dispensadora vs. el vendedor la diferencia entre
   chatbot y agente.
2. Para una tienda de electrodomésticos, inventa **3 herramientas** que su agente necesitaría.
3. Da **2 ejemplos** de tareas en una tienda que conviene hacer con **flow** (no con agente) y
   explica por qué.

---

## 🤖 Prompt para Claude Code

```
Estudiemos el Módulo 7 (Qué es un agente de IA). Explícame la diferencia entre un LLM, un
chatbot y un agente con analogías. Luego pregúntame cuándo usar un flow y cuándo un agente en
MergeOn, con ejemplos de una tienda real. Corrígeme hasta que lo explique con seguridad.
```

---

## ✅ Checklist de dominio

- [ ] Sé qué es un LLM y por qué "solo no basta".
- [ ] Puedo explicar la diferencia entre chatbot y agente.
- [ ] Entiendo qué son las herramientas y el bucle del agente.
- [ ] Distingo flujo (workflow) de agente y sé dónde está cada uno en MergeOn.
- [ ] Puedo decirle a un cliente qué es MergeOn sin reducirlo a "un bot".

---

⬅️ Anterior: [Módulo 6 — CAPI](../06-capi-mensajes-comerciales/README.md)
➡️ Siguiente: [Módulo 8 — LangChain y `create_agent`](../08-langchain-create-agent/README.md)
