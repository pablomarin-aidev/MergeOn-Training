# Módulo 8 — LangChain y `create_agent`

> Bloque B · Cómo se construye un agente **por dentro**, en código. No tienes que volverte
> programador: la meta es **entender** las piezas para que MergeOn deje de ser una caja negra.

---

## 🎯 Objetivos

- Saber qué es **LangChain** y su relación con **LangGraph**.
- Entender la función **`create_agent`** y sus **3 ingredientes**.
- Leer un ejemplo de código de un agente y reconocer cada parte.
- Conectar esto con cómo está hecho el agente de MergeOn.

---

## 💼 Por qué importa para tu trabajo

Cuando entiendes que un agente son básicamente **3 cosas** (cerebro + manos + instrucciones),
el producto deja de ser magia. Entiendes por qué el **prompt** (las instrucciones que tú
configuras) es tan importante, y por qué agregar o quitar **herramientas** cambia lo que el
agente puede hacer. Eso te vuelve un socio que **sabe de qué habla**.

---

## 📚 Conceptos

### 1. LangChain y LangGraph

- **LangChain** es una librería de **Python** para construir aplicaciones con LLMs y agentes.
  Te da piezas listas para no programar todo desde cero.
- **LangGraph** es el **motor** sobre el que corren los agentes de LangChain. Permite flujos
  robustos y con memoria. **El bot de MergeOn corre sobre LangGraph.**

### 2. `create_agent`: el atajo para crear un agente

`create_agent` es una función de LangChain que te crea un agente **listo para usar**. Por
dentro arma el famoso bucle "piensa → usa herramienta → observa → responde" (patrón **ReAct**)
sobre LangGraph. Tú solo le das los ingredientes.

### 3. Los 3 ingredientes de un agente

```python
from langchain.agents import create_agent

agente = create_agent(
    model="...",              # 1) EL CEREBRO  (qué LLM piensa)
    tools=[...],              # 2) LAS MANOS   (qué puede hacer)
    system_prompt="..."       # 3) LA PERSONALIDAD (cómo se comporta)
)
```

| Ingrediente | Qué es | En MergeOn |
|---|---|---|
| **model** | El LLM que razona | Un modelo de Azure OpenAI |
| **tools** | Lista de herramientas | Las 16 herramientas del bot |
| **system_prompt** | Las reglas e identidad | **El prompt de ventas que TÚ configuras** |

> 💡 Por eso la skill de **creación de prompts** es tan importante: el `system_prompt` es la
> "personalidad y reglas" del agente. Cambiar ese texto cambia cómo vende.

### 4. Un ejemplo completo (para leer, no para memorizar)

```python
from langchain.agents import create_agent

# --- 2) LAS MANOS: dos herramientas simples ---
def buscar_producto(nombre: str) -> str:
    """Busca un producto en el catálogo y devuelve precio y stock."""
    catalogo = {
        "zapatillas": "Zapatillas Runner — $189.000 — 12 en stock",
        "gorra": "Gorra Classic — $49.000 — 3 en stock",
    }
    return catalogo.get(nombre.lower(), "No encontré ese producto.")

def crear_pedido(producto: str, cantidad: int, ciudad: str) -> str:
    """Registra un pedido y devuelve la confirmación."""
    return f"Pedido creado: {cantidad} x {producto}, envío a {ciudad}."

# --- 1) EL CEREBRO + 3) LA PERSONALIDAD ---
agente = create_agent(
    model="anthropic:claude-haiku-4-5",  # o el proveedor que tengas
    tools=[buscar_producto, crear_pedido],
    system_prompt=(
        "Eres un vendedor amable de una tienda colombiana. "
        "Usa 'tú', sé breve y cierra la venta pidiendo ciudad y cantidad."
    ),
)

# --- Ejecutar ---
respuesta = agente.invoke(
    {"messages": [{"role": "user", "content": "Hola, ¿tienes zapatillas?"}]}
)
print(respuesta["messages"][-1].content)
```

Fíjate: el agente **decide solo** llamar a `buscar_producto` cuando preguntas por zapatillas.
Nadie programó "si dice zapatillas, busca": el LLM lo decide. Eso es un agente.

### 5. Parámetros extra (solo para que te suenen)

`create_agent` también acepta cosas como `response_format` (forzar un formato de respuesta) o
`middleware` (insertar lógica en medio del bucle). No los necesitas para empezar; solo debes
saber que existen y dan poder.

---

## 🔗 Documentación oficial

- **Agentes en LangChain (guía)** — <a href="https://docs.langchain.com/oss/python/langchain/agents" target="_blank" rel="noopener">docs.langchain.com/oss/python/langchain/agents</a>
- **Referencia de `create_agent`** — <a href="https://reference.langchain.com/python/langchain/agents/factory/create_agent" target="_blank" rel="noopener">reference.langchain.com/python/langchain/agents/factory/create_agent</a>

## 🎓 Cursos / videos gratis

- **Functions, Tools and Agents with LangChain — DeepLearning.AI** — <a href="https://www.deeplearning.ai/courses/functions-tools-agents-langchain" target="_blank" rel="noopener">deeplearning.ai/courses/functions-tools-agents-langchain</a>
- **AI Agents in LangGraph — DeepLearning.AI** — <a href="https://www.deeplearning.ai/courses/ai-agents-in-langgraph" target="_blank" rel="noopener">deeplearning.ai/courses/ai-agents-in-langgraph</a>

---

## ✍️ Práctica

1. En el ejemplo de código, señala **cuál línea** es el cerebro, cuál las manos y cuál la
   personalidad.
2. Si quisieras que el agente también pudiera **consultar el estado de un envío**, ¿qué
   ingrediente cambiarías y cómo?
3. Explica por qué cambiar el `system_prompt` cambia la forma de vender, conectándolo con la
   skill de creación de prompts.

> En el siguiente módulo vas a **escribir y correr** este agente tú mismo con ayuda de Claude
> Code. Este módulo es para entender las piezas; el próximo, para construirlas.

---

## 🤖 Prompt para Claude Code

```
Estudiemos el Módulo 8 (LangChain y create_agent). Explícame los 3 ingredientes de un agente con
el ejemplo de código del módulo, línea por línea. Luego hazme preguntas: tápame partes del código
y pídeme que diga cuál es el cerebro, las manos y la personalidad. Conéctalo con cómo está hecho
el bot de MergeOn.
```

---

## ✅ Checklist de dominio

- [ ] Sé qué es LangChain y qué es LangGraph (y que MergeOn corre sobre LangGraph).
- [ ] Puedo nombrar los 3 ingredientes de `create_agent`.
- [ ] Leo el ejemplo de código y reconozco cada parte.
- [ ] Entiendo por qué el `system_prompt` define cómo vende el agente.
- [ ] Puedo explicar que el agente decide solo cuándo usar una herramienta.

---

⬅️ Anterior: [Módulo 7 — ¿Qué es un agente de IA?](../07-que-es-un-agente-ia/README.md)
➡️ Siguiente: [Módulo 9 — Práctica: tu primer agente](../09-practica-primer-agente/README.md)
