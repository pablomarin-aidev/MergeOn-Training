# Módulo 3 — Revisión de Apps (App Review)

> Bloque A · Por qué Meta revisa las "apps" antes de dejarlas usar permisos sensibles, y qué
> significa eso cuando conectas MergeOn con WhatsApp o Instagram.

---

## 🎯 Objetivos

- Entender qué es una **app de Meta** y por qué existe.
- Explicar qué es **App Review** y qué busca Meta.
- Diferenciar **acceso estándar** de **acceso avanzado**.
- Saber cómo se relaciona con la verificación de negocio (módulo 2).

---

## 💼 Por qué importa para revender

Cuando MergeOn se conecta al WhatsApp o Instagram de tu cliente, por detrás hay una **app de
Meta** pidiendo **permisos** (enviar mensajes, leer conversaciones, etc.). Meta no entrega esos
permisos gratis: **revisa** que se usen bien.

Entender esto te deja **manejar expectativas**: le explicas al cliente por qué hay un paso de
aprobación, por qué no es instantáneo, y por qué algunos permisos requieren más trámite.

---

## 📚 Conceptos

### 1. Qué es una "app" de Meta

No es una app de celular. Es un **proyecto técnico** dentro de *Meta for Developers* que sirve
de **puente** entre un software (como MergeOn) y los productos de Meta (WhatsApp, Instagram,
Messenger). Esa app es la que tiene las "llaves" (tokens) para actuar.

### 2. Permisos (scopes)

Una app pide **permisos** específicos según lo que necesita hacer. Por ejemplo:

- *enviar y recibir mensajes de WhatsApp*
- *gestionar mensajes de Instagram*
- *administrar anuncios*

Cada permiso **sensible** debe ser **aprobado** por Meta. No puedes simplemente "activarlo".

**Analogía:** la app es un empleado nuevo. Los permisos son las llaves de cada puerta de la
empresa. Meta es el jefe de seguridad: no le da la llave de la bodega a alguien sin revisar
para qué la quiere y cómo la va a usar.

### 3. Qué es App Review

Es el proceso en el que **Meta revisa tu app** antes de que la use el público. Meta literalmente
**prueba** que la app usa los permisos que pidió de la forma que dijo. Si pides "leer mensajes"
pero tu app hace otra cosa, te rechazan.

> Dato clave: si la app la va a usar **cualquier persona** que no tenga un rol dentro de la app
> o del negocio que la creó, **primero** debe pasar por App Review.

### 4. Acceso estándar vs. acceso avanzado

- **Acceso estándar (Standard):** limitado. Sirve para probar, normalmente solo con personas
  que tienen un rol en la app (tú, el equipo).
- **Acceso avanzado (Advanced):** lo que se necesita para usarlo con el público / clientes
  reales y a escala. Este suele requerir App Review **y** verificación de negocio.

### 5. Modo desarrollo vs. producción

Una app empieza en **modo desarrollo** (solo para pruebas internas) y pasa a **producción /
"Live"** cuando ya está lista y aprobada para usuarios reales.

### 6. Cómo se conecta con el módulo 2

App Review y verificación de negocio van de la mano: para acceso avanzado a APIs sensibles
(como WhatsApp a escala), Meta normalmente exige que el **negocio esté verificado**. Por eso en
un proyecto real haces primero la verificación (módulo 2) y en paralelo preparas la app.

> En MergeOn, gran parte de este trabajo de app ya está hecho del lado de la plataforma. Tu
> labor como revendedor es entender el **proceso** para acompañar al cliente y explicar tiempos
> y requisitos sin que te tome por sorpresa.

---

## 🔗 Documentación oficial

- **App Review (Meta for Developers)** — [developers.facebook.com/docs/resp-plat-initiatives/individual-processes/app-review](https://developers.facebook.com/docs/resp-plat-initiatives/individual-processes/app-review)
- **Verificación de negocio (relacionado)** — [developers.facebook.com/docs/development/release/business-verification](https://developers.facebook.com/docs/development/release/business-verification/)
- **Meta for Developers (portal)** — [developers.facebook.com](https://developers.facebook.com)

## 🎓 Cursos / videos gratis

- **Documentación de plataforma de WhatsApp Business** (incluye flujo de apps y permisos) — [developers.facebook.com/docs/whatsapp](https://developers.facebook.com/docs/whatsapp)
- **Cursos gratis de Meta Blueprint** — [facebookblueprint.com (cursos gratis)](https://www.facebookblueprint.com/student/page/512235-browse-free-courses-from-the-blueprint-catalog)

---

## ✍️ Práctica

1. Explica con tus palabras la diferencia entre una "app de Meta" y una app de celular.
2. Inventa 3 permisos que necesitaría una app de ventas por WhatsApp y di, para cada uno, por
   qué Meta querría revisarlo.
3. Un cliente te dice: *"¿por qué no puedo mandarle mensajes a todos mis contactos desde ya?"*
   Redacta una respuesta de 2-3 frases que use lo aprendido (permisos + App Review + acceso
   avanzado).

---

## 🤖 Prompt para Claude Code

```
Estudiemos el Módulo 3 (App Review). Explícame con la analogía del "empleado y las llaves" qué
son los permisos y por qué Meta los revisa. Luego hazme de cliente desconfiado que no entiende
por qué hay un trámite de aprobación, y corrige mis respuestas hasta que sepa explicarlo claro.
```

---

## ✅ Checklist de dominio

- [ ] Entiendo qué es una app de Meta y que es un puente técnico, no una app de celular.
- [ ] Puedo explicar qué son los permisos y dar ejemplos.
- [ ] Sé qué busca Meta en App Review y por qué.
- [ ] Distingo acceso estándar de acceso avanzado.
- [ ] Entiendo cómo App Review se relaciona con la verificación de negocio.

---

⬅️ Anterior: [Módulo 2 — Verificación de negocio](../02-verificacion-negocio/README.md)
➡️ Siguiente: [Módulo 4 — Políticas de WhatsApp](../04-politicas-whatsapp/README.md)
