# Módulo 5 — Tipos de Ads

> Bloque A · Los anuncios son la **gasolina** del negocio: traen a la gente al WhatsApp donde el
> agente de MergeOn la atiende. Aquí entiendes qué tipo de anuncio usar y por qué.

---

## 🎯 Objetivos

- Entender la estructura **Campaña → Conjunto de anuncios → Anuncio**.
- Conocer los **objetivos de campaña** y qué optimiza cada uno.
- Dominar los **Click-to-WhatsApp (CTWA)**, el anuncio clave del negocio.
- Saber qué objetivo elegir (y cuál **evitar**) para traer conversaciones.

---

## 💼 Por qué importa para tu trabajo

MergeOn brilla cuando **llegan conversaciones**. Esas conversaciones vienen, en gran parte, de
anuncios **Click-to-WhatsApp**. Si tu cliente corre el anuncio con el objetivo equivocado,
recibe clics que no conversan y dice "esto no sirve". Si lo corre bien, el agente cierra ventas.

Entender los anuncios te vuelve un socio **completo**: no solo montas el chat, ayudas a que
llegue tráfico de calidad.

---

## 📚 Conceptos

### 1. La estructura de 3 niveles

```
CAMPAÑA            → Aquí defines el OBJETIVO (qué quieres lograr)
  └─ CONJUNTO DE ANUNCIOS → Aquí defines PÚBLICO, PRESUPUESTO y UBICACIÓN
       └─ ANUNCIO          → Aquí va la pieza: imagen/video, texto y botón
```

Es como un árbol: una campaña puede tener varios conjuntos, y cada conjunto varios anuncios.

### 2. Objetivos de campaña

El **objetivo** es lo que le pides a Meta que optimice. Los principales:

| Objetivo | Para qué sirve |
|---|---|
| **Reconocimiento** | Que mucha gente vea tu marca |
| **Tráfico** | Llevar clics a un sitio/enlace |
| **Interacción** | Conseguir acciones, **incluyendo conversaciones** |
| **Clientes potenciales (Leads)** | Conseguir contactos interesados |
| **Ventas** | Conversiones/compras (necesita medición conectada) |

Meta usa inteligencia artificial para mostrarle tu anuncio a quien tenga **más probabilidad** de
hacer la acción del objetivo. Por eso **elegir mal el objetivo arruina la campaña**.

### 3. Click-to-WhatsApp (CTWA): el anuncio estrella

Es el anuncio que, al hacer clic, **abre un chat de WhatsApp** con el negocio (existen también
Click-to-Messenger y Click-to-Instagram). El usuario ve tu anuncio en Facebook o Instagram,
toca "Enviar mensaje" y **cae directo en el WhatsApp** donde trabaja el agente de MergeOn.

**Requisito:** la página de Facebook debe estar conectada al número de WhatsApp.

### 4. Qué objetivo elegir para CTWA (¡clave!)

- ✅ **Interacción (optimizado a conversaciones) o Mensajes:** lo mejor por defecto. Meta busca
  gente con más probabilidad de **iniciar un chat**.
- ✅ **Leads:** si quieres que Meta optimice por consultas de mayor calidad.
- ✅ **Ventas:** solo si tienes la **medición conectada** (CAPI — módulo 6) para reportar las
  compras. Ahí Meta busca gente con intención de compra.
- ❌ **Tráfico: EVÍTALO** para CTWA. Optimiza por *toques al enlace*, no por *conversaciones*.
  Recibes muchos clics… y pocas charlas reales.

### 5. El mensaje pre-rellenado (¡el puente con MergeOn!)

En un CTWA puedes configurar un **mensaje de bienvenida pre-rellenado**: el texto que ya aparece
escrito cuando el usuario abre el chat (ej: *"Hola, quiero info de los zapatos"*).

Esto es **oro** para MergeOn: como ese texto es **siempre el mismo**, se puede crear un **flow**
que lo detecte (con coincidencia exacta de texto) y **responda automático al instante**, sin
gastar IA. Es exactamente el caso de uso que ahorra tokens del que hablan los flows de MergeOn.

> Conexión: en MergeOn esto se arma con un flow `default_message` + `equal_text` con el texto
> exacto de la pauta. Lo verás a fondo en el módulo 11.

### 6. Formatos y presupuesto

- **Formatos:** imagen, video, carrusel. El video suele rendir muy bien para captar atención.
- **Presupuesto:** arranca con un presupuesto diario que le dé a Meta **datos suficientes en
  ~5-7 días** para aprender. No cambies todo cada día: dale tiempo de optimizar.

---

## 🔗 Documentación oficial

- **Crear anuncios que dirijan a WhatsApp (oficial)** — [facebook.com/business/help/447934475640650](https://www.facebook.com/business/help/447934475640650)
- **Centro de ayuda para empresas (anuncios)** — [facebook.com/business/help](https://www.facebook.com/business/help)
- **Administrador de anuncios** — [business.facebook.com](https://business.facebook.com)

## 🎓 Cursos / videos gratis

- **Cursos gratis de Meta Blueprint** (busca "anuncios", "objetivos", "Click to WhatsApp") — [facebookblueprint.com (cursos gratis)](https://www.facebookblueprint.com/student/page/512235-browse-free-courses-from-the-blueprint-catalog)
- **Certificaciones de Meta** (la de nivel asociado es gratis) — [facebook.com/business/learn/certification](https://www.facebook.com/business/learn/certification)

---

## ✍️ Práctica

1. Dibuja (en papel o texto) la estructura Campaña → Conjunto → Anuncio para una tienda de ropa
   que quiere conversaciones por WhatsApp. ¿Qué objetivo eliges y por qué?
2. Escribe un **mensaje pre-rellenado** para un anuncio de trampolines y explica cómo un flow de
   MergeOn lo aprovecharía.
3. Un cliente eligió objetivo **Tráfico** y se queja de que "llegan clics pero nadie compra".
   Explícale qué pasó y qué cambiar.

---

## 🤖 Prompt para Claude Code

```
Estudiemos el Módulo 5 (Tipos de Ads). Explícame la estructura de campañas y los objetivos con
una analogía. Luego enséñame por qué para Click-to-WhatsApp se elige Interacción/Mensajes y no
Tráfico. Termina mostrándome cómo el mensaje pre-rellenado conecta con un flow de MergeOn.
```

---

## ✅ Checklist de dominio

- [ ] Entiendo la estructura Campaña → Conjunto de anuncios → Anuncio.
- [ ] Sé qué optimiza cada objetivo de campaña.
- [ ] Puedo explicar qué es un CTWA y su requisito (página conectada al WhatsApp).
- [ ] Sé qué objetivo elegir para conversaciones y por qué se evita Tráfico.
- [ ] Entiendo el mensaje pre-rellenado y cómo un flow de MergeOn lo aprovecha.

---

⬅️ Anterior: [Módulo 4 — Políticas de WhatsApp](../04-politicas-whatsapp/README.md)
➡️ Siguiente: [Módulo 6 — CAPI y mensajes comerciales](../06-capi-mensajes-comerciales/README.md) ⭐
