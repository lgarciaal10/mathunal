# MathUNAL · Simulacros Pro

Documento de referencia de la feature de simulacros. Rama `simulacros-pro`,
**sin desplegar** — activa solo al abrir `index.html` en local (`localhost`,
red privada o `file://`). En `mathunal.com` sigue apagada, con el teaser "Muy pronto".

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

| GRATIS (todos) | PRO (pago) |
|---|---|
| Diagnóstico corto por materia/corte (8 preguntas) | Todos los simulacros por corte, cuantos quieras |
| **1 simulacro gratis por corte** con nota + dominio por tema | Todas las soluciones paso a paso + "el truco" + gráficas interactivas |
| Qué temas fallaste, qué tipo de error (concepto / álgebra / signo / procedimiento) | Entrenar solo tus errores + pregunta gemela |
| Reto por WhatsApp (adquisición) | Repaso espaciado (Leitner) de lo que fallas |
| | Dashboard "Mi preparación" + predicción de nota |

El **2.º simulacro del mismo corte** dispara el paywall (**$12.000**, un pago, acceso todo el semestre, sin renovación automática).

---

## 3. Pantallas y flujo

### En el home
La sección **Simulacros** está justo después de "Hoy" (racha). Muestra:
- "¿Qué tan listo estás para el parcial?"
- Mi Progreso (si ya hiciste alguno)
- Grid de las **11 materias**: Cálculo Diferencial = "Modo completo · por corte" (PRO);
  el resto = "N parciales de práctica"
- Botones: *Ir a Simulacros* · *Diagnóstico rápido (gratis)*
- Modo Pánico (parcial en <24h)

### En `#simulacro`
1. **Selector** — filtro por materia (11 pills), por tipo (parcial/quiz/taller). Arriba de todo:
   - Card **"Repasar mis errores (N)"** si hay preguntas pendientes de repaso espaciado
   - Los **3 Simulacros por Corte** de Cálculo Diferencial
   - Onboarding "¿Qué vas a presentar?" (materia · corte · **fecha del parcial**)
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

| Materia | Estado |
|---|---|
| **Cálculo Diferencial** | Modo completo: 49 preguntas etiquetadas por corte/tema, 3 simulacros por corte, soluciones con "el truco", 6 gráficas interactivas, diagnóstico por tema |
| Otras 10 materias | Los parciales reales (30 exámenes en total) funcionan como simulacros con cronómetro y solución, pero **sin** el enriquecimiento Pro (corte, "el truco", gráficas) |

La enriquecida se hace **materia por materia**. Cálculo Diferencial es el piloto —
cuando convierta, se replica.

---

## 5. Arquitectura

### Archivos
- **`index.html`** — todo el código (single-file). Los datos de simulacros (`sim-calcdif.js` +
  `sim-lab.js`) están **inline** en `<script>` dentro del `<head>`.
- **`sim-pro-schema.sql`** — el esquema de Supabase para el Pro real. **NO aplicado.**

### El motor (ya existía)
`tpl-simulacro` en `index.html`: pantallas `screen-sel → screen-intro → screen-q → screen-results`,
cronómetro, tipos mcq/numérica/abierta, autoevaluación con crédito parcial, Panel de Éxito,
revisión, tutoría con IA (Supabase `explicaciones` + endpoint + fallback local), diagnóstico (`#diag-*`).

### La capa Pro (esta rama)
- **`SIM_TAX`** — taxonomía: cortes + temas de cada materia
- **`SIM_META`** — metadata sobre las 29 preguntas existentes (corte, tema, frecuencia, tipoError, "el truco", cómo reconocerlo)
- **`SIM_SOL`** — solución + rúbrica para las 4 abiertas que no tenían
- **`SIM_NEW`** — 20 preguntas nuevas
- **`SIM_POOL`** — pool plano por materia (existentes enriquecidas + nuevas)
- **`__simBuildCorte(slug, corte)`** — arma un simulacro curado por corte
- **`__simLab`** — 6 widgets SVG interactivos (escalera, cono, globo, caja, tangente, límite)
- **Hooks** en el motor (`__simExplHook`, `__simResultHook`, `__simQHook`, ...): agregan "el truco",
  dominio por tema, confianza, etc. sin reescribir el motor
- **`__simSRS`** — repaso espaciado (localStorage `mu-sim-srs`)
- **`__simRenderPrep`** — dashboard "Mi preparación"
- **`__simPro`** — gate: `isPro()` mira Supabase si hay sesión, si no el mock local

### Interruptores
| Flag | Qué controla |
|---|---|
| `window.__SIM_LOCAL` | true en localhost / red privada / file:// |
| `SIMULACROS_HABILITADOS` | = `!!__SIM_LOCAL` (para soltar en prod: cambiar a `true`) |
| `window.__SIMPRO_DEV` | = `__SIM_LOCAL` o `?simpro=1` — activa toda la capa Pro en dev |
| `localStorage['mu-sim-pro']` | mock de "es Pro" para probar en local |

---

## 6. Modelo de datos (localStorage hoy, Supabase después)

| Clave | Contenido |
|---|---|
| `mu-results` | historial de simulacros (nota, desglose por tema, corte, tiempo) |
| `mu-sim-srs` | cajas de repaso espaciado por pregunta |
| `mu-sim-corte` / `mu-sim-fecha` | onboarding |
| `mu-sim-notas-reales` | notas reales post-parcial (calibración de la predicción) |
| `mu-sim-pro` / `mu-sim-pro-srv` / `mu-sim-lic` | flag Pro (mock / servidor) + licencia para marca de agua |

`sim-pro-schema.sql` traduce esto a Supabase: `sim_entitlements` (RLS: cada quien ve solo lo suyo),
`sim_purchases`, `sim_solutions` (el contenido Pro, servido solo a quien pagó — **anti-piratería**),
`sim_real_grades` + vista de calibración.

---

## 7. Cómo probar

```bash
python -m http.server 8791
```

Abre `http://localhost:8791/` (sin parámetros). Todo está activo.
Si no ves los cambios: agrega `?nc=1` a la URL (el navegador cachea localhost).

---

## 8. Pendiente para producción

1. Cambiar `SIMULACROS_HABILITADOS` a `true`
2. Reescribir el copy inventado "2.4 vs 3.8" del Pack
3. **Pro real:** aplicar `sim-pro-schema.sql` + migrar las soluciones a `sim_solutions` +
   conectar Wompi + decidir si el Pro requiere cuenta con correo (ver §9)
4. Enriquecer la 2.ª materia (Cálculo Integral es la de más impacto)
5. Piloto con 20–30 estudiantes, medir el embudo demo → compra → 2.º simulacro

---

## 9. Decisión pendiente: ¿el Pro requiere cuenta con correo?

- **Sin cuenta** (solo navegador): cero fricción, pero se pierde al borrar caché, no pasa entre
  dispositivos, y **es imposible frenar que alguien comparta el acceso** (paga uno, lo usan 10).
- **Con cuenta** (correo + código, ya existe en el sitio): el Pro queda atado a la persona,
  funciona entre dispositivos y se puede limitar el abuso. El diagnóstico y el simulacro gratis
  **no piden nada** — la cuenta solo aparece al pagar.

Recomendación: **con cuenta** (el login por código que ya está), correo abierto (no solo `@unal.edu.co`)
para no cerrar la puerta. Es el único camino que hace que el Pro no sea trivial de piratear.
