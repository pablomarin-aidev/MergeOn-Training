# Academia MergeOn Seller — Formación para Socios

Bienvenido. Este repositorio es un **curso completo** para que aprendas a implementar
**MergeOn Seller** con tus clientes y, sobre todo, para que **entiendas qué hay detrás**:
Meta, WhatsApp, anuncios, CAPI, agentes de IA, LangChain, MCP y APIs.

No es un curso para leer y ya. Trae un archivo `CLAUDE.md` que convierte a **Claude Code**
en tu **profesor particular**: te explica, te pone ejercicios, te corrige y no te deja
avanzar hasta que de verdad entiendes.

> **Objetivo:** que pases de "sé hacer clic en la interfaz de MergeOn" a
> "entiendo el negocio y la tecnología, y puedo montarle todo el sistema a un cliente
> y explicárselo con seguridad".

---

## ¿Para quién es esto?

Para **socios de MergeOn Seller**. No necesitas ser programador.
Solo necesitas ganas de aprender y seguir los pasos. Los módulos técnicos (8, 9 y 10)
están escritos para que cualquiera los entienda, y Claude Code hace el trabajo pesado contigo.

---

## ¿Cómo funciona? (la idea clave)

```
   Tú  ───►  abres esta carpeta con Claude Code  ───►  Claude lee CLAUDE.md
                                                              │
                                                              ▼
                          Claude se convierte en tu TUTOR y te guía módulo por módulo
```

Cada módulo (carpeta numerada dentro de `modulos/`) tiene un `README.md` con:

- **Objetivos** — qué vas a poder hacer al terminar.
- **Por qué importa para tu trabajo** — la conexión con tu día a día.
- **Conceptos** — la explicación clara, con analogías.
- **Documentación oficial** — los enlaces que de verdad valen (no blogs random).
- **Cursos / videos gratis** — para profundizar.
- **Práctica** — ejercicios concretos.
- **Prompt para Claude Code** — copia y pega para que el tutor te enseñe ese tema.
- **Checklist de dominio** — para saber si ya lo dominas.

---

## Ruta de aprendizaje

Sigue el orden. Cada módulo se apoya en el anterior.

### Bloque A — Meta para negocios (el terreno donde vives)
1. [Portafolio comercial en Meta](modulos/01-portafolio-comercial-meta/README.md) — qué es, para qué sirve, cómo crearlo.
2. [Verificación de negocio](modulos/02-verificacion-negocio/README.md) — qué es, para qué y cómo se hace.
3. [Revisión de Apps (App Review)](modulos/03-revision-apps/README.md) — por qué Meta revisa las apps y qué significa.
4. [Políticas de WhatsApp](modulos/04-politicas-whatsapp/README.md) — qué se puede y qué no (evita bloqueos).
5. [Tipos de Ads](modulos/05-tipos-de-ads/README.md) — incluyendo los Click-to-WhatsApp, que son la base del negocio.
6. [CAPI y mensajes comerciales](modulos/06-capi-mensajes-comerciales/README.md) — ⭐ el módulo estrella: cómo se mide y optimiza la pauta.

### Bloque B — IA y lo técnico detrás
7. [¿Qué es un agente de IA?](modulos/07-que-es-un-agente-ia/README.md) — la diferencia entre un chatbot y un agente.
8. [LangChain y `create_agent`](modulos/08-langchain-create-agent/README.md) — cómo se construye un agente por dentro.
9. [Práctica: tu primer agente con Claude Code](modulos/09-practica-primer-agente/README.md) — vas a crear uno tú mismo.
10. [MCPs y APIs](modulos/10-mcps-y-apis/README.md) — cómo se conectan las piezas del software moderno.

### Bloque C — Síntesis
11. [Qué hay detrás de MergeOn Seller](modulos/11-detras-de-mergeon-seller/README.md) — todo lo anterior, junto, en el producto que vendes.

📖 Apóyate en el [GLOSARIO](GLOSARIO.md) cada vez que veas una palabra que no entiendas.

---

## Requisitos

| Necesitas | Para qué | Cómo conseguirlo |
|---|---|---|
| Cuenta de Claude (Pro, Max, Team o Console) | Usar Claude Code como tutor | <a href="https://claude.ai" target="_blank" rel="noopener">claude.ai</a> |
| Claude Code instalado | Abrir este curso y estudiar | Ver instalación abajo |
| Python 3.10 o superior | Solo para los módulos 8 y 9 (práctica de código) | <a href="https://www.python.org/downloads/" target="_blank" rel="noopener">python.org/downloads</a> |

> El plan **gratis** de Claude.ai **no** incluye Claude Code. Necesitas un plan de pago.

---

## Instalación paso a paso

### 1. Instala Claude Code

Sigue la guía oficial: **<a href="https://code.claude.com/docs/en/setup" target="_blank" rel="noopener">code.claude.com/docs/en/setup</a>**

Resumen rápido:
- **Windows / Mac / Linux:** usa el instalador nativo (no requiere nada más).
- Alternativa con Node.js 18+: `npm install -g @anthropic-ai/claude-code`

### 2. Descarga este curso

**Opción A — Fácil (ZIP):**
Descarga el repositorio como `.zip` desde GitHub y descomprímelo en una carpeta que recuerdes
(por ejemplo `Documentos/Academia-MergeOn`).

**Opción B — Con Git:**
```bash
git clone <URL-del-repo>
cd academia-mergeon-seller
```

### 3. Abre el curso con Claude Code

1. Abre una terminal **dentro de la carpeta del curso**.
2. Escribe `claude` y presiona Enter.
3. La primera vez te pedirá iniciar sesión en el navegador. Hazlo.

### 4. Empieza a estudiar

Cuando Claude Code esté abierto, escríbele:

```
Hola, soy socio de MergeOn y quiero empezar el curso. Guíame desde el módulo 1.
```

El `CLAUDE.md` de esta carpeta ya le dice cómo enseñarte. **Él lleva el ritmo contigo.**

---

## Cómo estudiar cada módulo (método recomendado)

1. **Lee** el `README.md` del módulo por tu cuenta primero.
2. **Pídele a Claude** que te lo explique con tus palabras: *"Explícame el módulo 1 como si fuera nuevo en esto"*.
3. **Pregunta** todo lo que no entiendas. No hay preguntas tontas.
4. **Haz la práctica** del módulo.
5. **Usa el prompt** del final del módulo para que Claude te evalúe.
6. **Marca el checklist**. Si algo no lo puedes marcar, repasa antes de avanzar.

> Regla de oro: **no avances al siguiente módulo hasta cerrar el checklist del actual.**

---

## Preguntas frecuentes

**¿Tengo que saber programar?**
No. Solo los módulos 8 y 9 tocan código, y Claude Code lo escribe contigo, línea por línea.

**¿Cuánto dura el curso?**
A tu ritmo. Calcula entre 1 y 2 horas por módulo. No corras: el objetivo es entender.

**¿Esto reemplaza la documentación oficial de Meta?**
No. Te enseña los conceptos y te lleva de la mano a la documentación oficial, que siempre es
la fuente de verdad y la que más cambia. Por eso cada módulo enlaza a la fuente oficial.

**Las pantallas de Meta cambiaron y no coinciden con lo que dice el módulo.**
Es normal: Meta cambia su interfaz seguido. Los **conceptos** no cambian. Cuando un paso
exacto no coincida, sigue el enlace oficial del módulo y pídele ayuda a Claude.

---

*Academia creada para socios de MergeOn Seller · https://mergeon.dev*
