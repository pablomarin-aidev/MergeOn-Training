# Módulo 6 — CAPI y mensajes comerciales ⭐

> Bloque A · **El módulo más importante del bloque.** CAPI es lo que hace que la pauta deje de
> ser "a ver qué pasa" y se vuelva una máquina que aprende a traer **compradores**, no solo
> curiosos. Tómate tu tiempo aquí.

---

## 🎯 Objetivos

- Entender **el problema de medición** que CAPI resuelve.
- Explicar qué es **CAPI (Conversions API)** y en qué se diferencia del pixel.
- Entender **CAPI para mensajería**: cómo conecta lo que pasa *dentro* del WhatsApp con la pauta.
- Conocer los **límites técnicos** clave (1 evento por clic, 7 días).
- Saber cómo MergeOn usa CAPI y por qué es un **argumento de venta** enorme.

---

## 💼 Por qué importa para tu trabajo

Este es, probablemente, **el mayor diferenciador** que puedes ofrecerle a un cliente.

Sin CAPI, Meta solo sabe que "se inició una conversación". No sabe si esa persona **compró**.
Entonces optimiza la pauta para traer gente que *chatea*… aunque no compre.

Con CAPI, Meta sabe **quién compró de verdad**. Entonces aprende a buscar **más compradores
parecidos**. El resultado: mejor ROAS, leads más baratos, y un reporte real de cuánto vende la
pauta. Cuando le explicas esto a un cliente, entiende por qué tu solución vale más.

---

## 📚 Conceptos

### 1. El problema: Meta es "ciega" dentro del chat

Imagina un anuncio que lleva a WhatsApp. Meta **ve el clic**, pero **no ve** lo que pasa después
dentro de la conversación: no sabe si la persona preguntó precio, si compró, si se arrepintió.

Antes, la medición vivía en la **web** con el **pixel** (un código en la página que registra
"vio producto", "compró"). Pero hoy ese rastreo por navegador es **poco confiable**: bloqueadores
de anuncios, reglas de privacidad de los celulares, cookies que se borran… y peor aún, **en una
venta por WhatsApp no hay página web**: la venta ocurre en el chat.

**Resultado:** Meta optimiza a ciegas. Trae gente que abre chats, pero no necesariamente gente
que paga.

### 2. Qué es CAPI (Conversions API)

CAPI es una forma de **enviarle los eventos a Meta desde tu servidor** (no desde el navegador
del usuario). Es una conexión **directa y confiable** entre tus datos —web, app, CRM, tienda y,
ahora, **tus conversaciones de WhatsApp**— y Meta.

| | Pixel | CAPI |
|---|---|---|
| Dónde corre | En el **navegador** del usuario | En el **servidor** del negocio |
| Confiabilidad | Frágil (bloqueadores, privacidad) | Alta y estable |
| Sirve para chats de WhatsApp | No | **Sí** |

> No compiten: muchas tiendas web usan pixel **y** CAPI juntos. Pero para ventas por mensajería,
> **CAPI es la única forma** de cerrarle el círculo a Meta.

**Analogía:** es como un pescador. El pixel le avisa "alguien mordió el anzuelo". CAPI le avisa
"este pez **se pescó y se vendió**". Con esa segunda señal, el pescador aprende **en qué parte
del lago** están los peces que de verdad se venden, y tira la red ahí.

### 3. CAPI para mensajería (Business Messaging)

Esta es la versión que nos importa. Meta abrió CAPI para conectar datos de **WhatsApp,
Messenger** (y pronto Instagram) y así potenciar los anuncios **Click-to-Message**.

¿Qué logra?

- En el **Administrador de anuncios** aparecen columnas como **Meta Leads** (clientes
  potenciales) y **Meta Purchases** (compras) que reflejan lo que pasó **dentro del WhatsApp**.
- Puedes ver **ROAS** (retorno) y **CPL** (costo por lead) **reales**, no solo "conversaciones
  iniciadas".
- Puedes crear **conversiones personalizadas** (ej: "completó el chatbot", "llegó a etapa X del
  CRM").

### 4. Cómo funciona, a grandes rasgos

```
1. El usuario hace clic en el anuncio Click-to-WhatsApp
        │   (Meta le pega una "etiqueta de clic" a esa conversación: el ctwa_clid)
        ▼
2. Conversa en WhatsApp. El agente de MergeOn lo atiende.
        ▼
3. Ocurre algo valioso: deja sus datos (Lead) o compra (Purchase).
        ▼
4. El SERVIDOR (MergeOn) le envía ese evento a Meta vía CAPI,
   con la etiqueta del clic para que Meta sepa de QUÉ anuncio vino.
        ▼
5. Meta atribuye la venta a ese anuncio y APRENDE a buscar más compradores.
```

### 5. Límites técnicos que debes conocer

Para anuncios Click-to-WhatsApp, CAPI tiene reglas estrictas:

- **Solo 1 evento CAPI por cada clic de anuncio.** No puedes reportar 5 cosas del mismo clic.
- **El evento debe enviarse dentro de los 7 días** posteriores al clic. Pasados 7 días, Meta
  **no lo procesa**.

Esto explica por qué los sistemas serios envían el evento **correcto** y **a tiempo** (por
ejemplo, la compra), no cualquier cosa.

### 6. Tipos de evento típicos

- **Lead** — la persona mostró interés / dejó datos.
- **Purchase** — la persona compró (con su monto).
- **Conversiones personalizadas** — etapas propias del negocio (CRM, chatbot completado, etc.).

### 7. Cómo lo hace MergeOn

MergeOn envía estos eventos **del lado del servidor** por ti. Cuando una venta nace de un lead
que vino de un anuncio, MergeOn puede mandarle a Meta el evento **Purchase** con el monto,
atándolo al anuncio que lo originó. La plataforma incluye herramientas para **previsualizar** el
evento, **ver el estado** del envío y **revisar** los eventos enviados de cada orden.

> Para ti como socio: no tienes que programar nada de esto. Tu trabajo es **entenderlo**
> para configurarlo bien y para **venderlo** como la ventaja que es. Lo conectaremos todo en el
> módulo 11.

---

## 🔗 Documentación oficial

- **Conversions API para Business Messaging (oficial)** — <a href="https://developers.facebook.com/docs/marketing-api/conversions-api/business-messaging/" target="_blank" rel="noopener">developers.facebook.com/docs/marketing-api/conversions-api/business-messaging</a>
- **Conversions API (general)** — <a href="https://developers.facebook.com/docs/marketing-api/conversions-api/" target="_blank" rel="noopener">developers.facebook.com/docs/marketing-api/conversions-api</a>
- **WhatsApp + Conversions API (blog oficial WhatsApp Business)** — <a href="https://whatsappbusiness.com/blog/conversions-api-messaging/" target="_blank" rel="noopener">whatsappbusiness.com/blog/conversions-api-messaging</a>

## 🎓 Cursos / videos gratis

- **Cursos gratis de Meta Blueprint** (busca "medición", "Conversions API", "eventos") — <a href="https://www.facebookblueprint.com/student/page/512235-browse-free-courses-from-the-blueprint-catalog" target="_blank" rel="noopener">facebookblueprint.com (cursos gratis)</a>
- **Centro de ayuda para empresas (medición)** — <a href="https://www.facebook.com/business/help" target="_blank" rel="noopener">facebook.com/business/help</a>

---

## ✍️ Práctica

1. Explica, **sin tecnicismos**, por qué Meta "no ve" lo que pasa dentro de un chat de WhatsApp
   y qué problema causa eso en la pauta.
2. Con la analogía del pescador, cuéntale a un cliente imaginario por qué activar CAPI hará que
   sus anuncios mejoren con el tiempo.
3. Dibuja el flujo de 5 pasos (clic → conversación → venta → evento → optimización) con tus
   propias palabras.
4. Un cliente envía la compra a Meta **10 días después** del clic. ¿Qué pasa y por qué?

---

## 🤖 Prompt para Claude Code

```
Estudiemos el Módulo 6 (CAPI), que es el más importante. Ve despacio. Primero hazme entender el
problema de medición (por qué el pixel no basta y por qué Meta es ciega en el chat). Luego
explícame CAPI con la analogía del pescador. Después pregúntame el flujo de 5 pasos hasta que lo
diga bien. Termina explicándome los límites (1 evento por clic, 7 días) y cómo lo usa MergeOn.
No me dejes avanzar si no logro explicarte CAPI con mis palabras.
```

---

## ✅ Checklist de dominio

- [ ] Entiendo por qué el rastreo por navegador/pixel no basta para ventas por WhatsApp.
- [ ] Puedo explicar qué es CAPI y la diferencia con el pixel.
- [ ] Entiendo qué logra CAPI para mensajería (Meta Leads, Meta Purchases, ROAS real).
- [ ] Puedo describir el flujo de 5 pasos (clic → venta → evento → optimización).
- [ ] Conozco los límites: 1 evento por clic y ventana de 7 días.
- [ ] Sé cómo MergeOn usa CAPI y por qué es un argumento de venta.

---

⬅️ Anterior: [Módulo 5 — Tipos de Ads](../05-tipos-de-ads/README.md)
➡️ Siguiente: [Módulo 7 — ¿Qué es un agente de IA?](../07-que-es-un-agente-ia/README.md)
