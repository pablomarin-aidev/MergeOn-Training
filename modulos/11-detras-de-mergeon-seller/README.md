# Módulo 11 — Qué hay detrás de MergeOn Seller

> Bloque C · El cierre. Aquí **se junta todo lo que aprendiste**. Vas a ver el viaje completo,
> de principio a fin, y a entender cómo cada módulo es una pieza de la misma máquina.

---

## 🎯 Objetivos

- Ver el **recorrido completo**: del anuncio a la venta optimizada.
- Ubicar **cada módulo** dentro de ese recorrido.
- Entender **qué hace MergeOn** en cada paso y **cuál es tu rol** como socio.
- Poder explicarle a un cliente, de punta a punta, **por qué tu solución funciona**.

---

## 🗺️ El viaje completo de una venta

```
   [ANUNCIO Click-to-WhatsApp]              ← Módulo 5 (tipos de ads)
            │  el cliente hace clic
            ▼
   [Llega a WhatsApp con mensaje pre-rellenado]
            │
            ▼
   [FLOW lo detecta y responde al instante]  ← Módulo 7 (flow = workflow), sin gastar IA
            │  (texto exacto de la pauta → respuesta automática)
            ▼
   [El AGENTE de IA toma la conversación]    ← Módulos 7 y 8 (agente, create_agent, LangGraph)
            │  usa sus HERRAMIENTAS:
            │     • buscar_producto   ─┐
            │     • crear_pedido       ├─ por debajo llaman a la API ← Módulo 10
            │     • escalar a humano  ─┘
            ▼
   [Se crea la venta]
            │
            ▼
   [MergeOn envía el evento a Meta vía CAPI] ← Módulo 6 (CAPI) ⭐
            │  "esta persona COMPRÓ, y vino de tal anuncio"
            ▼
   [Meta aprende y trae más compradores]     ← el ciclo se retroalimenta y mejora
```

Y todo esto vive sobre una base que montaste al inicio:

```
   PORTAFOLIO COMERCIAL  ← Módulo 1   (el maletín con todos los activos)
   VERIFICACIÓN          ← Módulo 2   (Meta confirma que el negocio es real)
   APP REVIEW + permisos ← Módulo 3   (la app aprobada para conectar WhatsApp)
   POLÍTICAS DE WHATSAPP ← Módulo 4   (jugar limpio para no quemar el número)
```

Y tú lo administras todo **conversando con Claude** gracias al **MCP** ← Módulo 10.

---

## 🧩 Dónde entra cada módulo

| Módulo | Pieza de la máquina |
|---|---|
| 1 · Portafolio comercial | La base donde viven todos los activos del cliente |
| 2 · Verificación | Lo que desbloquea las funciones serias |
| 3 · App Review | El permiso de Meta para que la app conecte WhatsApp |
| 4 · Políticas WhatsApp | Las reglas para no perder el número |
| 5 · Tipos de Ads | El motor que trae conversaciones (CTWA) |
| 6 · CAPI ⭐ | El cierre del círculo: Meta aprende quién compra |
| 7 · Qué es un agente | El concepto detrás del bot vendedor |
| 8 · LangChain / create_agent | Cómo está construido ese agente por dentro |
| 9 · Práctica | Tú mismo creaste uno y le perdiste el miedo |
| 10 · MCPs y APIs | Cómo se conectan las piezas y cómo lo manejas desde Claude |

---

## 🧠 Las dos capas de MergeOn

Todo lo que aprendiste se resume en **dos capas que trabajan juntas**:

1. **Capa Meta (módulos 1–6):** el terreno. Portafolio, verificación, app, políticas, anuncios
   y medición (CAPI). Es **dónde** y **cómo** llega y se mide el cliente.
2. **Capa IA (módulos 7–10):** el cerebro. El agente que atiende y vende, sus herramientas, y
   el MCP con el que tú lo gobiernas. Es **quién** atiende y **cómo lo controlas**.

MergeOn vale porque **une las dos**: trae al cliente bien (Meta), lo atiende como un vendedor
real (agente) y le enseña a Meta quién compra (CAPI) para traer más ventas. Pocas soluciones
cierran ese círculo completo.

---

## 🛠️ Tu rol como socio, fase por fase

- **Montaje:** creas/ordenas el portafolio, acompañas la verificación, configuras el WhatsApp.
- **Tráfico:** asesoras al cliente para que corra CTWA con el objetivo correcto.
- **Conversación:** configuras **flows** (para lo predecible) y el **prompt** del agente (para
  vender). Aquí brillan las skills que ya tienes.
- **Medición:** activas y explicas **CAPI** — tu mayor diferenciador.
- **Operación:** administras todo desde Claude vía el MCP, y le enseñas al cliente a leer sus
  resultados.

---

## ✍️ Práctica final (integradora)

1. Explícale a un cliente imaginario, en menos de un minuto, **todo el viaje** de una venta en
   MergeOn (del anuncio a la optimización). Grábate o escríbelo.
2. Toma un negocio real (de los que vas a atender) y di, para cada uno de los 11 módulos, **qué
   harías** en ese paso para ese negocio.
3. Identifica **tu mayor argumento de venta** y explica por qué (pista: revisa el módulo 6).

---

## 🤖 Prompt para Claude Code

```
Estudiemos el Módulo 11 (Qué hay detrás de MergeOn Seller). Tómame examen final: pídeme que te
explique el viaje completo de una venta, del anuncio a CAPI, y que ubique cada módulo en ese
viaje. Hazme de cliente que pregunta "¿por qué esto es mejor que un bot normal?" y evalúa mi
respuesta. Dime honestamente si ya estoy listo para implementarlo o qué módulo debo repasar.
```

---

## 🎓 Checklist de graduación

- [ ] Puedo explicar el viaje completo de una venta (anuncio → flow → agente → venta → CAPI).
- [ ] Ubico cada uno de los 11 módulos dentro de ese viaje.
- [ ] Entiendo las dos capas (Meta + IA) y por qué juntas hacen valioso a MergeOn.
- [ ] Sé cuál es mi mayor argumento de venta y por qué.
- [ ] Me siento listo para montarle el sistema a un cliente y explicárselo con seguridad.

---

## 🚀 Próximos pasos

Ya tienes la teoría y la práctica. Ahora:
- Repasa los módulos donde el checklist quedó flojo.
- Usa las **skills de MergeOn** (crear flows, crear prompts) sobre un caso real con Claude.
- Móntale el sistema a tu primer cliente, paso por paso, usando este curso como mapa.

**¡Felicitaciones! Terminaste la Academia MergeOn Seller. 🎉**

---

⬅️ Anterior: [Módulo 10 — MCPs y APIs](../10-mcps-y-apis/README.md)
🏠 Volver al [inicio del curso](../../README.md)
