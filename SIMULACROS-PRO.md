# MathUNAL · Simulacros Pro

Documento de referencia de la feature de simulacros. Rama `simulacros-pro`,
**sin pushear ni desplegar** — activa solo al abrir `index.html` en local (`localhost`,
red privada o `file://`). En `mathunal.com` sigue apagada, con el teaser "Muy pronto".
El esquema de Supabase SÍ está aplicado en producción (tablas nuevas, no tocan lo existente).
Falta Wompi para poder cobrar de verdad.

---

## 1. Qué es

Un **entrenador para el parcial**, no un banco de preguntas con cronómetro.
El valor está en el loop completo:

```
haces el simulacro → sabes tu nota y en qué temas fallas
                   → ves la solución + "el truco" de cada pregunta
                   → entrenas solo tus errores (repaso espaciado)
                   → repites → mides tu evolución → llegas al parcial sabiendo si estás listo
```

Frase norte: **no vendemos preguntas, vendemos certeza antes del parcial.**

---

## 2. Gratis vs Pro

| GRATIS (todos) | PRO (pago, **por materia**) |
|---|---|
| Diagnóstico corto por materia/corte (8 preguntas) | Simulacros por corte ilimitados |
| **1 simulacro gratis por corte** con nota /5.0 + "Preparación X%" | Tabla **dominio por tema** completa + tipo de error + insight de confianza |
| El **resumen** (1 línea) de cada pregunta | Todas las soluciones paso a paso + **"el truco"** + gráficas interactivas |
| **1 tema flojo** como adelanto ("tu mayor fuga: X") | Pregunta gemela + entrenar errores + repaso espaciado |
| Modo Examen Real · reto por WhatsApp | Dashboard "Mi preparación" + predicción de nota calibrada |

**No hay solución de muestra en el gratis** — se ve el resumen y un candado. (Decisión:
"en el gratis no decir en qué falla"; el enganche es el resumen + el teaser del diagnóstico.)

El **2.º simulacro del mismo corte** dispara el paywall (**$12.000 COP**, un pago,
acceso todo el semestre, sin renovación automática). El Pro se compra **por materia**
(SKU por materia), no "todas".

---

## 3. Pantallas y flujo

### En el home
La sección **Simulacros** está justo después de "Hoy" (racha). Muestra:
- "¿Qué tan listo estás para el parcial?"
- Mi Progreso (si ya hiciste alguno)
- Grid de las **11 materias**: las 5 con modo Pro (Cálc. Diferencial, Cálc. Integral, Álgebra
  Lineal, EDO, CVV) = "Modo completo · por corte", marcadas **PRO** y primero; el resto =
  "N parciales de práctica"
- Botones: *Ir a Simulacros* · *Diagnóstico rápido (gratis)*
- Modo Pánico (parcial en <24h)

### En `#simulacro`
1. **Selector** — filtro por materia (11 pills), por tipo (parcial/quiz/taller). Arriba de todo:
   - Card **"Repasar mis errores (N)"** si hay preguntas pendientes de repaso espaciado
   - Los **Simulacros por Corte** de las 5 materias Pro (3 cada una)
   - Onboarding "¿Qué vas a presentar?" (materia · corte · **fecha del parcial**) — hoy calcdif
2. **Intro** — instrucciones + toggle **"Modo Examen Real"** (pantalla completa, sin ver soluciones hasta entregar)
3. **Examen** — cronómetro, navegador de preguntas, marcar, autoguardado, chips de **confianza** ("¿seguro / dudoso / adiviné?")
4. **Entrega** — resumen (respondidas / marcadas / en blanco)
5. **Resultados** — nota /5.0 · Panel de Éxito (tiempo por pregunta, etc.) · **Dominio por tema** ·
   **tipo de error dominante** · **insight de confianza** · qué estudiar · tarjeta para **retar por WhatsApp**
6. **Revisión pregunta por pregunta** — cada solución trae: concepto, desarrollo, resultado,
   error común, **cómo reconocerlo en el parcial**, **el truco**, y en las de razón de cambio /
   optimización / tangente / límite una **gráfica interactiva "compruébalo tú mismo"**.
   Si fallaste y hay gemela: *"¿ya lo entendiste? prueba una parecida"*.

### Dashboard "Mi preparación" (en el selector, tras hacer simulacros)
Por cada corte: **Preparación /100** (Conocimiento 60 % + Velocidad 20 % + Cobertura 20 %),
estado 🔴🟡🟢🔥, **tu punto ciego** (el tema que fallas siempre), badge **"LISTO PARA EL CORTE"**
(2 notas seguidas ≥ 4.0), **estimación de nota** (rango; "beta" hasta tener notas reales),
y "faltan N días para tu parcial" si pusiste la fecha.

### Repaso espaciado
Lo que fallas vuelve a los **1, 2, 4, 9, 18 días** (cajas de Leitner). Aciertas → sube de caja;
fallas → vuelve a caja 1. Sin reloj.

---

## 4. Cobertura de contenido

**5 materias con modo Pro completo** (taxonomía por corte/tema, 3 simulacros por
corte, "el truco" + "cómo reconocerlo" + solución en cada pregunta, diagnóstico
por tema). Total: **206 filas en `sim_solutions`**.

| Materia | Código | Filas | Preguntas | Gráficas interactivas |
|---|---|---|---|---|
| **Cálculo Diferencial** | 1000004 | 49 | 29 reales + 20 nuevas | 6 (escalera, cono, globo, caja, tangente, límite) |
| **Cálculo Integral** | 1000005 | 40 | 22 + 18 | — |
| **Álgebra Lineal** | 1000006 | 39 | 24 + 15 | — |
| **Ecuaciones Diferenciales** | 1000008 | 37 | 22 + 15 | — |
| **Cálculo en Varias Variables** (CVV) | 1000007 | 41 | 26 + 15 | — |
| Otras 6 materias | — | — | los parciales reales sirven como simulacro con cronómetro, **sin** enriquecimiento Pro | — |

`PRO_COURSES = ['1000004','1000005','1000006','1000008','1000007']`. Siguiente:
Geometría Vectorial, Matemáticas Discretas, etc. (misma pasada). Gráficas
interactivas para calcint/alglin/edo/cvv: pendiente.

---

## 5. Arquitectura

### Archivos
- **`index.html`** — todo el código (single-file). Inline en el `<head>`: el bloque **FLACO**
  (SIM_TAX + SIM_META lite + SIM_NEW lite — solo lo renderizable + el `resumen`) y `sim-lab.js`.
- **`sim-pro-schema.sql`** — esquema de Supabase. **APLICADO** en producción (`goxhxrdchfyphkenixng`).
- **`sim-solutions.dev.js`** — espejo local de la tabla `sim_solutions` (GITIGNORED, solo
  localhost). El contenido Pro real (pasos, "el truco", soluciones de abiertas) **ya no está
  en `index.html`**: vive en `sim_solutions` con RLS. En local se lee de este espejo para QA
  sin entitlement; se regenera con `scratchpad/build-dev-sol.js` + `build-calcint.js`.

### El motor (ya existía)
`tpl-simulacro` en `index.html`: pantallas `screen-sel → screen-intro → screen-q → screen-results`,
cronómetro, tipos mcq/numérica/abierta, autoevaluación con crédito parcial, Panel de Éxito,
revisión, tutoría con IA (Supabase `explicaciones` + endpoint + fallback local), diagnóstico (`#diag-*`).

### La capa Pro (esta rama)
- **`SIM_TAX`** — taxonomía: cortes + temas (calcdif, calcint)
- **`SIM_META`** (inline, lite) — `c/t/f/e/gem/cx` por pregunta existente. El `ab`/`rc` ("el truco",
  "cómo reconocerlo") **salió del inline** → `sim_solutions`
- **`SIM_NEW`** (inline, lite) — preguntas nuevas: solo `texto/opciones/correcta/tipo/resumen`.
  Los `pasos`/`ab`/`rc` → `sim_solutions`
- **`__simFetchSol()`** — GET autenticado a `/rest/v1/sim_solutions` (sin filtro de course; la RLS
  devuelve solo lo comprado); `__simMergeSol()` fusiona sobre los objetos-pregunta
- **`SIM_POOL`** / **`__simBuildCorte(slug, corte)`** — pool por materia + simulacro curado por corte
- **`__simLab`** — 6 widgets SVG interactivos (solo calcdif por ahora)
- **Hooks** (`__simExplHook`, `__simResultHook`, `__simQHook`, ...): "el truco", dominio por tema,
  confianza, candados del gratis, sin reescribir el motor
- **`__simSRS`** / **`__simRenderPrep`** — repaso espaciado + dashboard
- **`__simPro`** — `isPro(course)` (entitlement por materia, `mu-sim-pro-srv-<course>`) ·
  `anyPro()` para las vistas globales · `syncFromServer()` consulta `sim_has_pro` por cada materia
- **`_t(es,en)` / `window.__simT`** — i18n del chrome del entrenador (candados, dashboard, paywall…).
  El **contenido** de las soluciones sigue en español (igual que todo el banco)

### Interruptores
| Flag | Qué controla |
|---|---|
| `window.__SIM_LOCAL` | true en localhost / red privada / file:// |
| `SIMULACROS_HABILITADOS` | = `!!__SIM_LOCAL` (para soltar en prod: cambiar a `true`) |
| `window.__SIMPRO_DEV` | = `__SIM_LOCAL` o `?simpro=1` — activa toda la capa Pro en dev |
| `localStorage['mu-sim-pro']` | mock de "es Pro" para probar en local (`window.__simPro.unlock()`) |
| `sim-solutions.dev.js` | espejo de `sim_solutions`, se carga solo si `__SIM_LOCAL` (en prod da 404) |

---

## 6. Modelo de datos (localStorage hoy, Supabase después)

| Clave | Contenido |
|---|---|
| `mu-results` | historial de simulacros (nota, desglose por tema, corte, tiempo) |
| `mu-sim-srs` | cajas de repaso espaciado por pregunta |
| `mu-sim-corte` / `mu-sim-fecha` | onboarding |
| `mu-sim-notas-reales` | notas reales post-parcial (calibración de la predicción) |
| `mu-sim-pro` | mock de dev ("es Pro en todo") |
| `mu-sim-pro-srv-<course>` | último resultado real de `sim_has_pro` por materia |
| `mu-sim-lic` | licencia corta para la marca de agua de las soluciones |

**Supabase (aplicado):** `sim_entitlements` (RLS: cada quien ve solo lo suyo, `unique(user,product,period)`),
`sim_purchases`, `sim_solutions` (**el contenido Pro**, `src` PK + `course_id` + `body` jsonb, RLS
`using sim_has_pro(course_id)` — **anti-piratería**), `sim_real_grades`, función
`sim_has_pro(p_course)` (SECURITY DEFINER, revocada de anon), vista `sim_calib_agg`.
Hoy `sim_solutions` tiene **206 filas** (calcdif 49 · calcint 40 · alglin 39 · edo 37 · cvv 41).

**Para darle Pro a alguien:** insertar fila en `sim_entitlements` con su `user_id`
(de `auth.users`, tras login OTP), `product_id`, `course_id`, `valid_until`.

---

## 7. Cómo probar

```bash
python -m http.server 8791
```

Abre `http://localhost:8791/` (sin parámetros). Todo está activo.
Si no ves los cambios: agrega `?nc=1` a la URL (el navegador cachea localhost).

**Para verlo como Pro en local:** `window.__simPro.unlock()` en la consola (o el botón "Pagar"
del paywall, que en local desbloquea directo). Trae las soluciones del espejo `sim-solutions.dev.js`.
El `unlock()` NO usa un entitlement real: para probar el camino completo con Supabase hay que
loguearse por OTP y meter una fila en `sim_entitlements`.

---

## 8. Pendiente para producción

1. **Conectar Wompi** — hoy el botón "Pagar" del paywall es un mock (`__simPro.unlock()`).
   Falta: merchant keys de Luis + webhook/edge-function que, al confirmarse el pago, escriba
   `sim_entitlements` + `sim_purchases`.
2. Cambiar `SIMULACROS_HABILITADOS` a `true` cuando se quiera soltar la capa gratis.
3. Gráficas interactivas "compruébalo tú mismo" para calcint / alglin / edo / cvv
   (hoy solo Cálculo Diferencial tiene las 6).
4. Traducción EN del **contenido** de las soluciones (hoy solo el chrome está en inglés).
5. Más materias con modo Pro (Geometría Vectorial, Matemáticas Discretas, …) — misma pasada.
6. Micro-simulacros de 10 min, ranking opcional, más badges (aplazados).
7. Piloto con 20–30 estudiantes, medir el embudo demo → compra → 2.º simulacro.

---

## 9. Decisión tomada: el Pro requiere cuenta

Login por **correo + código** (el que ya existe en el sitio), **por materia**. El diagnóstico y
el simulacro gratis **no piden nada** — la cuenta solo aparece al pagar (`__muAuthUI.open('pro')`).
Se acepta **cualquier correo**, pero el copy **recomienda el `@unal.edu.co`** ("más fácil de
recuperar y es el que reconocemos"). Es lo que hace que el Pro no sea trivial de piratear:
queda atado a la persona, funciona entre dispositivos, y la marca de agua lleva la licencia.
