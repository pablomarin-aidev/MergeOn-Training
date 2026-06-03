"""
Mi primer agente de IA — Práctica del Módulo 9 (Academia MergeOn Seller).

Objetivo: crear un mini "vendedor" que pueda buscar un producto y crear un pedido.

Trabaja este archivo CON Claude Code: pídele que te guíe paso a paso y te explique cada línea.
Donde veas "TODO", ahí te toca completar (con su ayuda). No tienes que saber programar:
solo entender qué hace cada parte.
"""

# ----------------------------------------------------------------------------------
# Paso 1 — Importar la función que crea agentes.
# TODO (con Claude): importa create_agent desde langchain.agents
# Pista: from <libreria>.<modulo> import <funcion>
# ----------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------
# Paso 2 — LAS MANOS: dos herramientas (funciones normales de Python).
# Estas ya están escritas para que veas cómo se ve una herramienta:
#   - un nombre claro
#   - un docstring (el texto entre comillas) que explica qué hace; el agente lo lee
#     para decidir cuándo usarla.
# ----------------------------------------------------------------------------------

def buscar_producto(nombre: str) -> str:
    """Busca un producto en el catálogo y devuelve precio y stock."""
    catalogo = {
        "zapatillas": "Zapatillas Runner — $189.000 — 12 en stock",
        "gorra": "Gorra Classic — $49.000 — 3 en stock",
    }
    return catalogo.get(nombre.lower(), "No encontré ese producto.")


def crear_pedido(producto: str, cantidad: int, ciudad: str) -> str:
    """Registra un pedido y devuelve una confirmación."""
    return f"Pedido creado: {cantidad} x {producto}, envío a {ciudad}."


# ----------------------------------------------------------------------------------
# Paso 3 — Arma el agente con los 3 ingredientes: cerebro, manos y personalidad.
# TODO (con Claude): crea el agente llamando a create_agent(...).
#   - model:         el cerebro, ej. "anthropic:claude-haiku-4-5"
#   - tools:         la lista de herramientas [buscar_producto, crear_pedido]
#   - system_prompt: la personalidad (un texto con las reglas del vendedor)
# ----------------------------------------------------------------------------------
# agente = create_agent(
#     model="...",
#     tools=[...],
#     system_prompt="...",
# )


# ----------------------------------------------------------------------------------
# Paso 4 — Habla con tu agente y muestra su respuesta.
# TODO (con Claude): descomenta esto cuando el agente ya esté creado arriba.
# ----------------------------------------------------------------------------------
# if __name__ == "__main__":
#     pregunta = "Hola, ¿tienes zapatillas? quiero 2 para Medellín"
#     respuesta = agente.invoke({"messages": [{"role": "user", "content": pregunta}]})
#     print(respuesta["messages"][-1].content)
