# Módulo 9 — Práctica: tu primer agente con Claude Code

> Bloque B · **Manos a la obra.** Vas a crear, tú mismo, un mini "vendedor" de IA en Python.
> No te asustes: Claude Code escribe el código **contigo** y te explica cada línea. Lo
> importante no es teclear rápido, es **entender** lo que construyes.

---

## 🎯 Objetivos

- Crear un agente sencillo con `create_agent`.
- Darle **2 herramientas** (buscar producto, crear pedido) y una **personalidad**.
- Ver al agente **decidir solo** cuándo usar cada herramienta.
- Perder el miedo al código leyéndolo con calma.

---

## 🧰 Requisitos

- **Python 3.10 o superior** instalado ([python.org/downloads](https://www.python.org/downloads/)).
- **Claude Code** abierto en esta carpeta (es tu copiloto en toda la práctica).
- *(Opcional, para ejecutarlo de verdad)* una **API key** de Anthropic u OpenAI.

> Hay **dos caminos**:
> - **Camino A (recomendado para empezar):** construyes el código y Claude Code te explica y
>   "simula" la ejecución razonando contigo. **No necesitas API key.** El aprendizaje está en
>   construir y entender.
> - **Camino B (bonus):** si tienes una API key, lo **ejecutas de verdad** y ves al agente
>   responder. Instrucciones abajo.

---

## 🪜 Pasos

### 1. Abre la práctica con Claude Code

Estando en esta carpeta con Claude Code abierto, pégale este prompt:

```
Vamos a hacer la práctica del Módulo 9. Quiero crear mi primer agente. Abre el archivo
agente.py de esta carpeta y guíame paso a paso para completar los TODO. Explícame cada línea
como si fuera nuevo en programación y no avances hasta que entienda. No completes todo de una:
hazlo conmigo, parte por parte.
```

### 2. Completa `agente.py` con su ayuda

El archivo [`agente.py`](agente.py) tiene comentarios y marcas `TODO` donde te toca completar
(con la ayuda de Claude). Vas a:

1. **Importar** `create_agent`.
2. Revisar las **dos herramientas** ya escritas (las manos del agente).
3. **Crear el agente** con sus 3 ingredientes: `model`, `tools`, `system_prompt`.
4. **Hablarle** al agente y mostrar su respuesta.

### 3. (Camino B) Ejecútalo de verdad

Si tienes API key, instala las dependencias y corre el archivo. Pídele a Claude Code que te
guíe, o sigue esto:

```bash
# 1. Crear entorno e instalar dependencias
pip install -r requirements.txt

# 2. Configurar tu API key (ejemplo con Anthropic)
#    Windows (PowerShell):
$env:ANTHROPIC_API_KEY = "tu-clave-aqui"
#    Mac/Linux:
export ANTHROPIC_API_KEY="tu-clave-aqui"

# 3. Ejecutar
python agente.py
```

Deberías ver al agente responder algo como: *"¡Claro! Tenemos Zapatillas Runner a $189.000..."*
y, si le das ciudad y cantidad, **crear el pedido solo**.

---

## 👀 Qué observar (lo importante)

- Tú **nunca** programaste "si el cliente dice zapatillas, busca en el catálogo". El agente
  **decidió** usar `buscar_producto` por su cuenta. Eso es un agente.
- Cambia el `system_prompt` (la personalidad) y vuelve a correr: verás que **cambia el tono**.
  Ese mismo poder es el que usas al configurar prompts en MergeOn.

---

## 🆘 Si algo falla (sin pánico)

Los errores son normales. Cópiale el error completo a Claude Code y pídele que te lo explique
y lo arregle contigo. Errores típicos:

- `ModuleNotFoundError` → faltó `pip install -r requirements.txt`.
- Error de API key → no configuraste la variable, o la clave es inválida.
- `python no se reconoce...` → Python no quedó en el PATH; reinstala marcando "Add to PATH".

---

## ✅ Solución de referencia

Intenta primero por tu cuenta con Claude. Si te trabas, así queda el archivo completo:

```python
from langchain.agents import create_agent

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

agente = create_agent(
    model="anthropic:claude-haiku-4-5",
    tools=[buscar_producto, crear_pedido],
    system_prompt=(
        "Eres un vendedor amable de una tienda colombiana. "
        "Usa 'tú', sé breve y cierra la venta pidiendo ciudad y cantidad."
    ),
)

if __name__ == "__main__":
    pregunta = "Hola, ¿tienes zapatillas? quiero 2 para Medellín"
    respuesta = agente.invoke({"messages": [{"role": "user", "content": pregunta}]})
    print(respuesta["messages"][-1].content)
```

---

## ✅ Checklist de dominio

- [ ] Entendí (no solo copié) qué hace cada parte de `agente.py`.
- [ ] Reconozco el cerebro, las manos y la personalidad en mi código.
- [ ] Vi (o razoné con Claude) cómo el agente decide solo usar una herramienta.
- [ ] Cambié el `system_prompt` y entendí cómo afecta la respuesta.
- [ ] Perdí un poco el miedo a leer código y errores.

---

⬅️ Anterior: [Módulo 8 — LangChain y `create_agent`](../08-langchain-create-agent/README.md)
➡️ Siguiente: [Módulo 10 — MCPs y APIs](../10-mcps-y-apis/README.md)
