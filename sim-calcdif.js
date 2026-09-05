/* ═══════════════════════════════════════════════════════════════════════════
   MathUNAL · Simulacros Pro — Banco enriquecido de CÁLCULO DIFERENCIAL
   ---------------------------------------------------------------------------
   TANDA 1 (rama simulacros-pro, sin desplegar). Este archivo:
     1. SIM_TAX   — taxonomía: cortes + temas de la materia
     2. SIM_META  — overlay posicional sobre las 29 preguntas ya en EXAMS
                    (agrega corte/tema/freq/tipoError/antibobo/reconocer)
     3. SIM_SOL   — solución + rúbrica para las 4 abiertas que no tenían
     4. SIM_NEW   — preguntas nuevas para cubrir bien cada corte
   El motor (Tanda 2) fusiona esto en window.EXAMS y arma "Simulacro por Corte".
   Nota: strings con backtick porque el contenido lleva apóstrofes (f', L'Hôpital).
   ═══════════════════════════════════════════════════════════════════════════ */
(function(){
"use strict";

/* ── 1. Taxonomía ─────────────────────────────────────────────────────────── */
var SIM_TAX = {
  calcdif: {
    materia: `Cálculo Diferencial`, codigo: `1000004`, slug: `calcdif`,
    cortes: {
      1: { nombre: `Funciones, límites y continuidad`, pct: 30,
           temas: [`Límites algebraicos`,`Límites indeterminados`,`Límites notables`,
                   `Límites al infinito`,`Continuidad`,`Asíntotas`] },
      2: { nombre: `La derivada y sus reglas`, pct: 30,
           temas: [`Definición de derivada`,`Reglas de derivación`,`Regla de la cadena`,
                   `Derivación implícita`,`Derivación logarítmica`,`Derivadas de orden superior`,
                   `Recta tangente y normal`,`Aproximación lineal`,`Razón de cambio`,
                   `Movimiento rectilíneo`] },
      3: { nombre: `Aplicaciones de la derivada`, pct: 40,
           temas: [`Regla de L'Hôpital`,`Valores extremos`,`Optimización`,
                   `Teorema del valor medio`,`Análisis de gráficas`,`Monotonía y concavidad`,
                   `Método de Newton`,`Teorema fundamental del cálculo`] }
    }
  }
};

/* ── 2. Overlay de metadata sobre las 29 preguntas existentes ─────────────────
   Índice = posición en EXAMS[examKey].preguntas. Campos:
     c   corte (1|2|3)
     t   tema
     f   frecuencia en parciales reales: 'alta'|'media'|'baja'
     e   tipoError dominante: conceptual|algebra|signo|procedimiento|formula|interpretacion
     ab  Antibobo (regla corta y memorable)
     rc  cómo reconocer el ejercicio en el parcial
     gem examKey_idx de una pregunta gemela (opcional)
     cx  id de widget "compruébalo" (opcional)                                   */
var SIM_META = {
 calcdif: {
  calcdif_p1: [
   {c:1,t:`Continuidad`,f:`alta`,e:`algebra`,
    ab:`Continua en $a$ = el límite existe Y vale $f(a)$. Factoriza y cancela el $(x-a)$ que causa el $0/0$.`,
    rc:`Función a trozos + "para que sea continua" → calcula el límite y ponlo igual al valor puntual.`},
   {c:1,t:`Límites notables`,f:`media`,e:`conceptual`,
    ab:`$(1+x)^{1/x}\\to e$. Si además aparece un $-e$ y un $/x$, es una derivada disfrazada (o Taylor de primer orden).`,
    rc:`$(1+x)^{1/x}$ o $(1+a/x)^{x}$ cerca de $0$ o $\\infty$ → piensa en $e$.`},
   {c:2,t:`Regla de la cadena`,f:`alta`,e:`procedimiento`,gem:`calcdif_quiz3_1`,
    ab:`AFUERA · DEJA · ADENTRO. La derivada interna de $3/x$ es $-3/x^2$; al multiplicar por el $x^2$ del producto queda $-3$.`,
    rc:`Aparece una $f$ genérica con algo adentro → cadena; y si hay un $x^2$ multiplicando → también producto.`},
   {c:3,t:`Valores extremos`,f:`alta`,e:`procedimiento`,
    ab:`Punto crítico = donde $f'=0$ O donde $f'$ no existe. La potencia fraccionaria casi siempre esconde un crítico del segundo tipo.`,
    rc:`Potencia fraccionaria, raíz o valor absoluto → revisa dónde $f'$ NO existe, no solo dónde vale 0.`},
   {c:2,t:`Reglas de derivación`,f:`baja`,e:`procedimiento`,
    ab:`Deriva TODO el lado izquierdo (producto + cadena), y solo entonces sustituye el $x$ y los datos $f(1)$, etc.`,
    rc:`Te dan una identidad con $f$ y piden $f'$ en un punto → deriva la identidad completa y sustituye.`},
   {c:2,t:`Movimiento rectilíneo`,f:`media`,e:`signo`,
    ab:`Sentido = signo de $v(t)=s'(t)$. "Sentido negativo" = va hacia atrás, NO que está frenando.`,
    rc:`"Sentido / dirección" del movimiento = signo de $v$. "Frena o acelera" = signo de $a\\cdot v$.`},
   {c:1,t:`Asíntotas`,f:`alta`,e:`conceptual`,
    ab:`Verticales: denominador $=0$ y numerador $\\neq0$. Horizontal: límite en $\\pm\\infty$; cuenta UNA sola aunque salga igual por ambos lados.`,
    rc:`Racional: grados iguales → AH en el cociente de coeficientes líderes; raíces del denominador → AV.`},
   {c:2,t:`Definición de derivada`,f:`alta`,e:`algebra`,
    ab:`En el cociente incremental con raíces: racionaliza por el conjugado. La NORMAL tiene pendiente $-1/f'(a)$.`,
    rc:`"Usando la definición" = límite del cociente incremental, obligatorio (no reglas de derivación).`},
   {c:2,t:`Reglas de derivación`,f:`baja`,e:`formula`,
    ab:`Regla de la potencia: baja el exponente, réstale 1. Luego evalúa.`,
    rc:`Polinomio y piden $f'(a)$ → deriva término a término y sustituye.`}
  ],
  calcdif_p2: [
   {c:3,t:`Teorema fundamental del cálculo`,f:`baja`,e:`signo`,
    ab:`$\\dfrac{d}{dx}\\displaystyle\\int_{a(x)}^{b(x)}\\! g\\,dt = g(b)\\,b' - g(a)\\,a'$. El límite de ABAJO entra restando.`,
    rc:`Derivada de una integral cuyos límites dependen de $x$ → TFC + regla de la cadena en cada límite.`},
   {c:2,t:`Derivación implícita`,f:`alta`,e:`procedimiento`,
    ab:`Cada término con $y$ suelta un $y'$ pegado. Deriva todo, agrupa los $y'$ a un lado, despeja.`,
    rc:`Ecuación que enreda $x$ e $y$ y no puedes despejar $y$ → implícita.`},
   {c:3,t:`Optimización`,f:`alta`,e:`procedimiento`,cx:`caja`,gem:`calcdif_p3_5`,
    ab:`Función OBJETIVO (lo que optimizas) + RESTRICCIÓN (el dato fijo). Sustituye para dejar una variable, deriva, iguala a 0.`,
    rc:`"Minimice el material / maximice el volumen" con un dato fijo → optimización con restricción.`},
   {c:2,t:`Regla de la cadena`,f:`baja`,e:`formula`,
    ab:`$(\\arctan u)' = \\dfrac{u'}{1+u^2}$. Con $u=\\sinh x$: $1+\\sinh^2 x = \\cosh^2 x$.`,
    rc:`Trig inversa compuesta con hiperbólica → cadena + identidad $\\cosh^2 x - \\sinh^2 x = 1$.`},
   {c:3,t:`Método de Newton`,f:`baja`,e:`formula`,
    ab:`$x_1 = x_0 - \\dfrac{f(x_0)}{f'(x_0)}$. Nada más. Evalúa con cuidado y no busques la raíz exacta.`,
    rc:`"Método de Newton" / "primera iteración" → aplica la fórmula UNA vez.`},
   {c:2,t:`Razón de cambio`,f:`alta`,e:`procedimiento`,cx:`escalera`,
    ab:`Dibuja el triángulo. Pitágoras relaciona los lados; deriva respecto de $t$. El ángulo va con $\\cos\\theta = x/L$.`,
    rc:`Escalera / sombra / triángulo que cambia de forma → Pitágoras + $d/dt$.`},
   {c:2,t:`Recta tangente y normal`,f:`media`,e:`formula`,
    ab:`Pendiente de la tangente $= f'(a)$. $(\\ln x)' = 1/x$.`,
    rc:`"Pendiente de la recta tangente en $x=a$" → deriva y evalúa en $a$.`}
  ],
  calcdif_quiz3: [
   {c:2,t:`Derivación implícita`,f:`alta`,e:`algebra`,
    ab:`Deriva, mete el punto $(1,2)$ lo antes posible para trabajar con números, y despeja $y'$.`,
    rc:`Ecuación implícita + "en el punto $(a,b)$" → deriva y sustituye el punto de una.`},
   {c:2,t:`Derivación logarítmica`,f:`alta`,e:`procedimiento`,gem:`calcdif_p1_2`,
    ab:`Variable en la BASE y en el EXPONENTE → $\\ln$ a ambos lados PRIMERO. Nunca derives $x^{\\sin x}$ directo.`,
    rc:`$x^{g(x)}$ (base y exponente con $x$) → derivación logarítmica, siempre.`},
   {c:2,t:`Regla de la cadena`,f:`baja`,e:`conceptual`,
    ab:`Antes de derivar el monstruo: ¿se simplifica? $\\dfrac{2x}{1-x^2} = \\tan(2\\arctan x)$, así que $f(x)=2\\arctan x$.`,
    rc:`Argumento de $\\arctan$ con forma $\\dfrac{2u}{1-u^2}$ → es $2\\arctan u$. Simplifica y ahórrate el trabajo.`},
   {c:3,t:`Análisis de gráficas`,f:`alta`,e:`procedimiento`,
    ab:`Críticos: $f'=0$. Criterio 2ª: $f''(c)>0$ mínimo, $<0$ máximo. Concavidad: signo de $f''$.`,
    rc:`"Clasifique los críticos / intervalos de concavidad" → $f'$ para críticos, $f''$ para clasificar y concavidad.`}
  ],
  calcdif_p3: [
   {c:3,t:`Regla de L'Hôpital`,f:`alta`,e:`procedimiento`,
    ab:`L'Hôpital SOLO si es $0/0$ o $\\infty/\\infty$. Verifica la forma ANTES y DESPUÉS de cada derivada.`,
    rc:`Cociente que al sustituir da $0/0$ o $\\infty/\\infty$ → L'Hôpital (o Taylor si se repite).`},
   {c:3,t:`Regla de L'Hôpital`,f:`media`,e:`conceptual`,
    ab:`La exponencial le gana a cualquier polinomio: $x^n/e^x \\to 0$.`,
    rc:`Polinomio sobre exponencial cuando $x\\to\\infty$ → tiende a 0 (la exponencial manda).`},
   {c:2,t:`Razón de cambio`,f:`alta`,e:`procedimiento`,cx:`globo`,
    ab:`Fórmula → deriva respecto de $t$ → sustituye AL FINAL. $\\dfrac{dV}{dt}=4\\pi r^2\\dfrac{dr}{dt}$.`,
    rc:`Te dan una razón (cm/s) y piden otra (cm³/s) en un instante → razón de cambio.`},
   {c:2,t:`Aproximación lineal`,f:`media`,e:`algebra`,
    ab:`$L(x)=f(a)+f'(a)(x-a)$. $a$ es el número "bonito" más cercano; $x-a$ es chiquito.`,
    rc:`Aproximar $\\sqrt{\\ }$, $\\ln$, trig de un número cercano a uno fácil → linealización.`},
   {c:3,t:`Valores extremos`,f:`alta`,e:`procedimiento`,
    ab:`Máx/mín absoluto en $[a,b]$: evalúa $f$ en los críticos internos Y en $a$ y $b$. Compara valores; el mayor gana.`,
    rc:`"Máximo/mínimo absoluto en intervalo cerrado" → críticos + extremos del intervalo, compara.`},
   {c:3,t:`Optimización`,f:`alta`,e:`procedimiento`,gem:`calcdif_p2_2`,
    ab:`Objetivo + restricción. Deja una variable, deriva, iguala a 0, verifica que sea mínimo (2ª derivada o signo de $S'$).`,
    rc:`"Lado / dimensión que minimiza..." con volumen o área fija → optimización.`},
   {c:3,t:`Teorema del valor medio`,f:`media`,e:`formula`,
    ab:`$f'(c)=\\dfrac{f(b)-f(a)}{b-a}$. Despeja $c$ y descarta los que caen fuera de $(a,b)$.`,
    rc:`"Valor $c$ que garantiza el TVM / Rolle" → iguala $f'(c)$ a la pendiente de la secante.`},
   {c:2,t:`Movimiento rectilíneo`,f:`alta`,e:`signo`,
    ab:`Sentido = signo de $v=s'$. Distancia $\\neq$ desplazamiento: parte en los $t$ donde $v=0$ y suma valores absolutos.`,
    rc:`Partícula con $s(t)$: sentido → $v$; frena/acelera → $a\\cdot v$; distancia total → parte en los ceros de $v$.`},
   {c:2,t:`Reglas de derivación`,f:`baja`,e:`formula`,
    ab:`Regla de la potencia y evalúa. $f'(x)=3x^2-4$.`,
    rc:`Polinomio, piden $f'(a)$.`}
  ]
 }
};

/* ── 3. Solución + rúbrica para las 4 abiertas ────────────────────────────────
   key = examKey + '_' + idx. rubrica: [criterio, "obtenido / total"].          */
var SIM_SOL = {
 calcdif: {
  calcdif_p1_7: {
   concepto:`Derivada por definición (límite del cociente incremental) y recta normal.`,
   quePregunta:`Probar $f'(x)=\\tfrac{3\\sqrt{x}}{2}$ SIN reglas, solo con el límite, y luego la recta normal en $x=4$.`,
   solucion:[
    `$f(x)=x\\sqrt{x}=x^{3/2}$. Por definición: $f'(x)=\\displaystyle\\lim_{h\\to0}\\dfrac{(x+h)^{3/2}-x^{3/2}}{h}$.`,
    `Multiplico y divido por el conjugado $(x+h)^{3/2}+x^{3/2}$:`,
    `$f'(x)=\\displaystyle\\lim_{h\\to0}\\dfrac{(x+h)^3-x^3}{h\\left[(x+h)^{3/2}+x^{3/2}\\right]}$.`,
    `Numerador: $(x+h)^3-x^3 = h(3x^2+3xh+h^2)$.`,
    `$f'(x)=\\displaystyle\\lim_{h\\to0}\\dfrac{3x^2+3xh+h^2}{(x+h)^{3/2}+x^{3/2}} = \\dfrac{3x^2}{2x^{3/2}} = \\dfrac{3\\sqrt{x}}{2}$. $\\blacksquare$`,
    `Recta normal en $x=4$: $f(4)=8$, $f'(4)=3$. Pendiente normal $=-\\tfrac13$.`,
    `$y-8 = -\\tfrac13(x-4)\\ \\Rightarrow\\ y = -\\tfrac13 x + \\tfrac{28}{3}$.`
   ],
   resultado:`$f'(x)=\\dfrac{3\\sqrt{x}}{2}$; recta normal $y = -\\dfrac{1}{3}x + \\dfrac{28}{3}$.`,
   errorComun:`Usar la regla de la potencia (la pregunta EXIGE la definición) o poner la pendiente de la normal $=f'(4)$ en vez de $-1/f'(4)$.`,
   antibobo:`"Por definición" = límite, sí o sí. Normal = perpendicular = pendiente $-1/f'(a)$.`,
   reconocer:`"Demuestre usando la definición" → cociente incremental. "Recta normal" → $-1/f'(a)$.`,
   rubrica:[[`Planteo del límite (definición)`,`0 / 0.20`],[`Racionalización / manejo algebraico`,`0 / 0.30`],
            [`Límite y resultado de $f'(x)$`,`0 / 0.20`],[`Pendiente normal $-1/f'(4)$`,`0 / 0.15`],
            [`Ecuación de la recta`,`0 / 0.15`],[`Total`,`0 / 1.00`]]
  },
  calcdif_p2_5: {
   concepto:`Razón de cambio: escalera (Pitágoras) + razón angular.`,
   quePregunta:`(a) rapidez de descenso del extremo superior; (b) rapidez de cambio del ángulo con el suelo, cuando la base está a 6 m.`,
   solucion:[
    `Sea $x$ la distancia base–pared, $y$ la altura del tope. $x^2+y^2=100$. Dato: $\\tfrac{dx}{dt}=0.5$.`,
    `En $x=6$: $y=\\sqrt{100-36}=8$.`,
    `(a) $2x\\tfrac{dx}{dt}+2y\\tfrac{dy}{dt}=0 \\Rightarrow \\tfrac{dy}{dt}=-\\dfrac{x}{y}\\tfrac{dx}{dt}=-\\dfrac{6}{8}(0.5)=-0.375$ m/s (baja a $0.375$ m/s).`,
    `(b) $\\cos\\theta = \\dfrac{x}{10}$. Derivo: $-\\sin\\theta\\,\\tfrac{d\\theta}{dt} = \\dfrac{1}{10}\\tfrac{dx}{dt}$.`,
    `$\\sin\\theta = \\dfrac{y}{10}=0.8$. Entonces $\\tfrac{d\\theta}{dt} = -\\dfrac{0.5}{10(0.8)} = -0.0625$ rad/s.`
   ],
   resultado:`(a) $\\dfrac{dy}{dt}=-0.375$ m/s. (b) $\\dfrac{d\\theta}{dt}=-0.0625$ rad/s (el ángulo disminuye).`,
   errorComun:`Sustituir $x=6$ ANTES de derivar (pierdes la relación), o no hallar $y$ con Pitágoras.`,
   antibobo:`Dibuja el triángulo, escribe la relación, deriva respecto de $t$, y SOLO al final metes los números.`,
   reconocer:`Escalera que resbala → $x^2+y^2=L^2$. Piden ángulo → relación trig con un lado.`,
   rubrica:[[`Planteo (Pitágoras + datos)`,`0 / 0.20`],[`Derivar y despejar $dy/dt$ (a)`,`0 / 0.30`],
            [`Relación trig del ángulo (b)`,`0 / 0.20`],[`Derivar y despejar $d\\theta/dt$`,`0 / 0.20`],
            [`Interpretación (signos, unidades)`,`0 / 0.10`],[`Total`,`0 / 1.00`]]
  },
  calcdif_quiz3_3: {
   concepto:`Puntos críticos, criterio de la segunda derivada, concavidad.`,
   quePregunta:`(a) críticos de $f(x)=x^3-3x^2+2$; (b) clasificarlos con $f''$; (c) intervalos de concavidad.`,
   solucion:[
    `(a) $f'(x)=3x^2-6x=3x(x-2)=0 \\Rightarrow x=0,\\ x=2$.`,
    `(b) $f''(x)=6x-6$. $f''(0)=-6<0 \\Rightarrow$ máximo local en $x=0$ ($f(0)=2$). $f''(2)=6>0 \\Rightarrow$ mínimo local en $x=2$ ($f(2)=-2$).`,
    `(c) $f''(x)=0 \\Rightarrow x=1$. $f''<0$ en $(-\\infty,1)$: cóncava hacia abajo. $f''>0$ en $(1,\\infty)$: cóncava hacia arriba. Inflexión en $(1,0)$.`
   ],
   resultado:`Máx local $(0,2)$; mín local $(2,-2)$; cóncava abajo en $(-\\infty,1)$, arriba en $(1,\\infty)$; inflexión $(1,0)$.`,
   errorComun:`Confundir el criterio: $f''>0$ es MÍNIMO (cara feliz), $f''<0$ es MÁXIMO.`,
   antibobo:`$f''>0$ = sonrisa = mínimo. $f''<0$ = ceño = máximo. Concavidad = signo de $f''$.`,
   reconocer:`"Clasifique los críticos" → $f'$ para hallarlos, $f''$ evaluada en cada uno para el tipo.`,
   rubrica:[[`Puntos críticos ($f'=0$)`,`0 / 0.25`],[`Segunda derivada y clasificación`,`0 / 0.35`],
            [`Concavidad + inflexión`,`0 / 0.30`],[`Valores de $f$ en los críticos`,`0 / 0.10`],[`Total`,`0 / 1.00`]]
  },
  calcdif_p3_7: {
   concepto:`Movimiento rectilíneo: velocidad, aceleración, distancia total.`,
   quePregunta:`$s(t)=2t^3-9t^2+12t-4$. (a) intervalos de sentido $\\pm$; (b) aceleración cuando $v=0$; (c) distancia total en $[0,3]$.`,
   solucion:[
    `$v(t)=s'(t)=6t^2-18t+12=6(t-1)(t-2)$. $v=0$ en $t=1,\\ t=2$.`,
    `(a) $v>0$ en $[0,1)$ y $(2,3]$ (sentido positivo); $v<0$ en $(1,2)$ (sentido negativo).`,
    `(b) $a(t)=s''(t)=12t-18$. $a(1)=-6$, $a(2)=6$.`,
    `(c) Posiciones: $s(0)=-4$, $s(1)=1$, $s(2)=0$, $s(3)=5$.`,
    `Distancia $=|1-(-4)| + |0-1| + |5-0| = 5+1+5 = 11$.`
   ],
   resultado:`(a) $+$ en $[0,1)\\cup(2,3]$, $-$ en $(1,2)$. (b) $a=-6$ en $t=1$, $a=6$ en $t=2$. (c) distancia total $=11$.`,
   errorComun:`Calcular $|s(3)-s(0)|=9$ como "distancia" — eso es el desplazamiento. La distancia parte en los $t$ donde $v=0$.`,
   antibobo:`Distancia total: encuentra dónde $v=0$, evalúa $s$ en esos puntos y en los extremos, suma los saltos en valor absoluto.`,
   reconocer:`"Distancia total recorrida" (no "desplazamiento") → siempre parte en los ceros de la velocidad.`,
   rubrica:[[`Velocidad y sus ceros`,`0 / 0.20`],[`Intervalos de sentido`,`0 / 0.20`],
            [`Aceleración en $v=0$`,`0 / 0.20`],[`Distancia total (parte en $v=0$)`,`0 / 0.30`],
            [`Unidades / interpretación`,`0 / 0.10`],[`Total`,`0 / 1.00`]]
  }
 }
};

/* ── 4. Preguntas nuevas por corte ─────────────────────────────────────────── */
var SIM_NEW = {
 calcdif: [
  /* ---------- CORTE 1 ---------- */
  {id:`cd_c1_01`,c:1,t:`Límites indeterminados`,f:`alta`,e:`algebra`,tipo:`mcq`,dif:1,tEsp:75,
   texto:`Calcule $\\displaystyle\\lim_{x\\to0}\\dfrac{\\sqrt{x+4}-2}{x}$.`,
   opciones:[`$\\dfrac{1}{4}$`,`$0$`,`$\\dfrac{1}{2}$`,`No existe`],correcta:0,
   resumen:`Forma $0/0$: se racionaliza multiplicando por el conjugado.`,
   pasos:[`Multiplico por $\\dfrac{\\sqrt{x+4}+2}{\\sqrt{x+4}+2}$:`,
     `$\\dfrac{(x+4)-4}{x(\\sqrt{x+4}+2)} = \\dfrac{x}{x(\\sqrt{x+4}+2)} = \\dfrac{1}{\\sqrt{x+4}+2}$.`,
     `$\\displaystyle\\lim_{x\\to0}\\dfrac{1}{\\sqrt{x+4}+2} = \\dfrac{1}{4}$.`],
   ab:`Raíz menos número sobre algo que tiende a 0 → racionaliza por el conjugado, se cancela el factor problemático.`,
   rc:`Raíz menos constante en el numerador y $0/0$ → conjugado.`},

  {id:`cd_c1_02`,c:1,t:`Límites al infinito`,f:`alta`,e:`algebra`,tipo:`mcq`,dif:2,tEsp:90,
   texto:`Calcule $\\displaystyle\\lim_{x\\to\\infty}\\left(\\sqrt{x^2+3x}-x\\right)$.`,
   opciones:[`$\\dfrac{3}{2}$`,`$0$`,`$3$`,`$\\infty$`],correcta:0,
   resumen:`Forma $\\infty-\\infty$: se racionaliza y se divide por $x$.`,
   pasos:[`$\\left(\\sqrt{x^2+3x}-x\\right)\\dfrac{\\sqrt{x^2+3x}+x}{\\sqrt{x^2+3x}+x} = \\dfrac{3x}{\\sqrt{x^2+3x}+x}$.`,
     `Divido arriba y abajo por $x$ (con $x>0$, $\\sqrt{x^2}=x$): $\\dfrac{3}{\\sqrt{1+3/x}+1}$.`,
     `$\\displaystyle\\lim_{x\\to\\infty} \\dfrac{3}{\\sqrt{1}+1} = \\dfrac{3}{2}$.`],
   ab:`$\\sqrt{\\ }-x$ en $\\infty$ → conjugado, luego saca $x$ de la raíz ($\\sqrt{x^2}=|x|=x$ para $x\\to+\\infty$).`,
   rc:`Diferencia de una raíz y un polinomio en $\\infty$ ($\\infty-\\infty$) → racionaliza.`},

  {id:`cd_c1_03`,c:1,t:`Límites notables`,f:`alta`,e:`formula`,tipo:`mcq`,dif:1,tEsp:60,
   texto:`Calcule $\\displaystyle\\lim_{x\\to0}\\dfrac{\\operatorname{sen}(3x)}{\\tan(5x)}$.`,
   opciones:[`$\\dfrac{3}{5}$`,`$1$`,`$\\dfrac{5}{3}$`,`$0$`],correcta:0,
   resumen:`Se usan $\\dfrac{\\operatorname{sen} u}{u}\\to1$ y $\\dfrac{\\tan u}{u}\\to1$.`,
   pasos:[`$\\dfrac{\\operatorname{sen}(3x)}{\\tan(5x)} = \\dfrac{\\operatorname{sen}(3x)}{3x}\\cdot\\dfrac{5x}{\\tan(5x)}\\cdot\\dfrac{3x}{5x}$.`,
     `Los dos primeros factores $\\to 1$; el tercero es $\\dfrac{3}{5}$.`,
     `Límite $= \\dfrac{3}{5}$.`],
   ab:`$\\dfrac{\\operatorname{sen}(ax)}{\\operatorname{sen}(bx)}\\to\\dfrac{a}{b}$ (con $\\tan$ igual). Arma los cocientes "$\\operatorname{sen} u/u$".`,
   rc:`Cociente de senos/tangentes de múltiplos de $x$ cuando $x\\to0$ → cociente de los coeficientes.`},

  {id:`cd_c1_04`,c:1,t:`Continuidad`,f:`media`,e:`procedimiento`,tipo:`mcq`,dif:2,tEsp:90,
   texto:`Sea $f(x)=\\begin{cases} ax+3 & x\\le 1\\\\ x^2+b & 1<x<3\\\\ bx+1 & x\\ge 3\\end{cases}$. Si $f$ es continua en todo $\\mathbb{R}$, entonces $a+b$ es:`,
   opciones:[`$6$`,`$2$`,`$-2$`,`$4$`],correcta:0,
   resumen:`Se igualan los límites laterales en $x=1$ y $x=3$.`,
   pasos:[`En $x=1$: $a(1)+3 = 1+b \\Rightarrow a - b = -2$.`,
     `En $x=3$: $9+b = 3b+1 \\Rightarrow 8 = 2b \\Rightarrow b = 4$.`,
     `$a = b - 2 = 2$. Entonces $a+b = 6$.`],
   ab:`Continuidad en cada frontera de la definición a trozos = un límite lateral igual al otro. Una ecuación por frontera.`,
   rc:`Función a trozos + "continua en todo $\\mathbb{R}$" → una ecuación por cada punto de empalme.`},

  {id:`cd_c1_05`,c:1,t:`Límites indeterminados`,f:`media`,e:`interpretacion`,tipo:`mcq`,dif:1,tEsp:50,
   texto:`El valor de $\\displaystyle\\lim_{x\\to2}\\dfrac{|x-2|}{x-2}$ es:`,
   opciones:[`No existe`,`$1$`,`$-1$`,`$0$`],correcta:0,
   resumen:`Los límites laterales dan $+1$ y $-1$: no coinciden.`,
   pasos:[`Para $x>2$: $|x-2|=x-2$, cociente $=1$. Límite por derecha $=1$.`,
     `Para $x<2$: $|x-2|=-(x-2)$, cociente $=-1$. Límite por izquierda $=-1$.`,
     `$1\\neq-1 \\Rightarrow$ el límite no existe.`],
   ab:`Valor absoluto dividido por su argumento = función signo. En la raíz del argumento, los laterales chocan.`,
   rc:`$|g(x)|/g(x)$ cerca de una raíz de $g$ → revisa los dos lados por separado.`},

  {id:`cd_c1_06`,c:1,t:`Límites notables`,f:`media`,e:`formula`,tipo:`numerica`,dif:2,tEsp:70,
   texto:`Calcule $\\displaystyle\\lim_{x\\to0}\\dfrac{1-\\cos x}{x^2}$. (Responde en decimal.)`,
   respuesta:`0.5`,unidad:``,tolNum:0.001,puntaje:15,
   resumen:`Multiplicar por $\\dfrac{1+\\cos x}{1+\\cos x}$ y usar $\\operatorname{sen}^2 x = 1-\\cos^2 x$.`,
   pasos:[`$\\dfrac{1-\\cos x}{x^2}\\cdot\\dfrac{1+\\cos x}{1+\\cos x} = \\dfrac{\\operatorname{sen}^2 x}{x^2(1+\\cos x)}$.`,
     `$= \\left(\\dfrac{\\operatorname{sen} x}{x}\\right)^2\\cdot\\dfrac{1}{1+\\cos x} \\to 1\\cdot\\dfrac{1}{2} = \\dfrac{1}{2}$.`],
   ab:`$\\dfrac{1-\\cos x}{x^2}\\to\\dfrac12$. Sale con el conjugado $1+\\cos x$ y $\\operatorname{sen}^2=1-\\cos^2$.`,
   rc:`$1-\\cos x$ sobre $x^2$ → conjugado; sobre $x$ → tiende a 0.`},

  /* ---------- CORTE 2 ---------- */
  {id:`cd_c2_01`,c:2,t:`Regla de la cadena`,f:`alta`,e:`procedimiento`,tipo:`mcq`,dif:3,tEsp:90,gem:`calcdif_p1_2`,
   texto:`Si $y=\\sqrt{\\tan(3x)}$, entonces $\\dfrac{dy}{dx}=$`,
   opciones:[`$\\dfrac{3\\sec^2(3x)}{2\\sqrt{\\tan(3x)}}$`,`$\\dfrac{\\sec^2(3x)}{2\\sqrt{\\tan(3x)}}$`,
             `$\\dfrac{3\\sec^2(3x)}{\\sqrt{\\tan(3x)}}$`,`$\\dfrac{1}{2\\sqrt{\\tan(3x)}}$`],correcta:0,
   resumen:`Cadena de tres capas: raíz, tangente y $3x$.`,
   pasos:[`$y=[\\tan(3x)]^{1/2}$. Capa 1: $\\dfrac12[\\tan(3x)]^{-1/2}\\cdot\\dfrac{d}{dx}\\tan(3x)$.`,
     `Capa 2: $\\dfrac{d}{dx}\\tan(3x) = 3\\sec^2(3x)$.`,
     `$\\dfrac{dy}{dx} = \\dfrac{1}{2\\sqrt{\\tan(3x)}}\\cdot 3\\sec^2(3x) = \\dfrac{3\\sec^2(3x)}{2\\sqrt{\\tan(3x)}}$.`],
   ab:`Cuenta las capas: raíz, $\\tan$, $3x$ = tres derivadas encadenadas, todas multiplicadas. El $3$ del $3x$ es el que más se olvida.`,
   rc:`Raíz de una trig de un múltiplo de $x$ → tres capas.`},

  {id:`cd_c2_02`,c:2,t:`Derivación implícita`,f:`media`,e:`procedimiento`,tipo:`mcq`,dif:3,tEsp:95,
   texto:`Si $x^2+y^2=25$, entonces $\\dfrac{d^2y}{dx^2}$ en el punto $(3,4)$ es:`,
   opciones:[`$-\\dfrac{25}{64}$`,`$-\\dfrac{3}{4}$`,`$\\dfrac{25}{64}$`,`$-\\dfrac{7}{16}$`],correcta:0,
   resumen:`Se deriva $y'=-x/y$ con la regla del cociente y se sustituye el punto.`,
   pasos:[`Primera: $2x+2yy'=0 \\Rightarrow y'=-\\dfrac{x}{y}$. En $(3,4)$: $y'=-\\dfrac34$.`,
     `Segunda (cociente): $y'' = -\\dfrac{y - x y'}{y^2} = -\\dfrac{y - x\\left(-\\tfrac{x}{y}\\right)}{y^2} = -\\dfrac{y^2+x^2}{y^3}$.`,
     `Como $x^2+y^2=25$: $y'' = -\\dfrac{25}{y^3}$.`,
     `En $(3,4)$: $y'' = -\\dfrac{25}{64}$.`],
   ab:`$y''$ implícita: deriva $y'$ con la regla del cociente, y donde aparezca $y'$ mete su expresión ($-x/y$).`,
   rc:`"Segunda derivada implícita" → deriva $y'$ otra vez; usa la ecuación original para simplificar al final.`},

  {id:`cd_c2_03`,c:2,t:`Razón de cambio`,f:`alta`,e:`procedimiento`,tipo:`numerica`,dif:2,tEsp:100,cx:`cono`,
   texto:`Un tanque cónico (vértice abajo, radio 3 m, altura 6 m) se llena a $2\\ \\text{m}^3/\\text{min}$. ¿A qué rapidez (m/min) sube el nivel cuando $h=4$ m? Responde en la forma $\\tfrac{1}{a\\pi}$ escribiendo solo $a$.`,
   respuesta:`2`,unidad:`(es decir $\\tfrac{1}{2\\pi}$ m/min)`,tolNum:0.001,puntaje:20,
   resumen:`Semejanza $r=h/2$ para dejar $V$ en función de $h$, luego derivar.`,
   pasos:[`Semejanza: $\\dfrac{r}{h}=\\dfrac{3}{6}\\Rightarrow r=\\dfrac{h}{2}$.`,
     `$V=\\dfrac13\\pi r^2 h = \\dfrac{\\pi h^3}{12}$.`,
     `$\\dfrac{dV}{dt}=\\dfrac{\\pi h^2}{4}\\dfrac{dh}{dt}$. Con $h=4$: $2 = 4\\pi\\dfrac{dh}{dt}$.`,
     `$\\dfrac{dh}{dt}=\\dfrac{1}{2\\pi}\\approx0.159$ m/min.`],
   ab:`Cono que se llena → el radio depende del nivel. Usa semejanza para dejar $V(h)$ ANTES de derivar.`,
   rc:`Recipiente que "se abre" hacia arriba (cono, pirámide) → semejanza de triángulos primero.`},

  {id:`cd_c2_04`,c:2,t:`Recta tangente y normal`,f:`media`,e:`algebra`,tipo:`mcq`,dif:2,tEsp:80,
   texto:`La recta tangente a la curva $x^3+y^3=9$ en el punto $(1,2)$ es:`,
   opciones:[`$y = -\\dfrac{1}{4}x + \\dfrac{9}{4}$`,`$y = -\\dfrac{1}{4}x + 2$`,`$y = 4x-2$`,`$y = -4x+6$`],correcta:0,
   resumen:`Derivación implícita para la pendiente, luego punto–pendiente.`,
   pasos:[`$3x^2+3y^2y'=0 \\Rightarrow y' = -\\dfrac{x^2}{y^2}$.`,
     `En $(1,2)$: $y' = -\\dfrac{1}{4}$.`,
     `$y-2 = -\\dfrac14(x-1) \\Rightarrow y = -\\dfrac14 x + \\dfrac94$.`],
   ab:`Curva implícita: pendiente por implícita, luego $y-y_0 = m(x-x_0)$. No olvides el punto.`,
   rc:`"Recta tangente a la curva $F(x,y)=c$ en $(a,b)$" → implícita para $m$, punto–pendiente.`},

  /* ---------- CORTE 3 ---------- */
  {id:`cd_c3_01`,c:3,t:`Regla de L'Hôpital`,f:`alta`,e:`procedimiento`,tipo:`mcq`,dif:2,tEsp:80,
   texto:`Calcule $\\displaystyle\\lim_{x\\to0^+} x\\ln x$.`,
   opciones:[`$0$`,`$-\\infty$`,`$1$`,`No existe`],correcta:0,
   resumen:`Forma $0\\cdot(-\\infty)$: se reescribe como cociente para aplicar L'Hôpital.`,
   pasos:[`$x\\ln x = \\dfrac{\\ln x}{1/x}$, forma $\\dfrac{-\\infty}{\\infty}$.`,
     `L'Hôpital: $\\dfrac{1/x}{-1/x^2} = -x$.`,
     `$\\displaystyle\\lim_{x\\to0^+}(-x) = 0$.`],
   ab:`$0\\cdot\\infty$: pasa uno de los factores al denominador como su recíproco para volverlo $0/0$ o $\\infty/\\infty$.`,
   rc:`Producto donde un factor $\\to0$ y el otro $\\to\\pm\\infty$ → reescribe como cociente.`},

  {id:`cd_c3_02`,c:3,t:`Regla de L'Hôpital`,f:`media`,e:`procedimiento`,tipo:`mcq`,dif:3,tEsp:100,
   texto:`Calcule $\\displaystyle\\lim_{x\\to0}(1+2x)^{1/x}$.`,
   opciones:[`$e^2$`,`$e$`,`$1$`,`$2$`],correcta:0,
   resumen:`Forma $1^\\infty$: tomar $\\ln$, resolver, y exponenciar.`,
   pasos:[`Sea $L$ el límite. $\\ln L = \\displaystyle\\lim_{x\\to0}\\dfrac{\\ln(1+2x)}{x}$, forma $0/0$.`,
     `L'Hôpital: $\\dfrac{2/(1+2x)}{1} \\to 2$.`,
     `$\\ln L = 2 \\Rightarrow L = e^2$.`],
   ab:`$1^\\infty$ (o $0^0$, $\\infty^0$): $\\ln$ a ambos lados, resuelve el límite del exponente, y al final $e^{(\\text{resultado})}$.`,
   rc:`Base $\\to1$ y exponente $\\to\\infty$ → toma logaritmo.`},

  {id:`cd_c3_03`,c:3,t:`Optimización`,f:`alta`,e:`procedimiento`,tipo:`mcq`,dif:3,tEsp:110,
   texto:`El punto de la parábola $y=x^2$ más cercano al punto $(0,3)$ tiene abscisa:`,
   opciones:[`$\\pm\\sqrt{\\dfrac{5}{2}}$`,`$0$`,`$\\pm\\dfrac{3}{2}$`,`$\\pm\\sqrt{3}$`],correcta:0,
   resumen:`Minimizar la distancia al cuadrado $D(x)=x^2+(x^2-3)^2$.`,
   pasos:[`$D(x)=x^2+(x^2-3)^2$ (misma $x$ que minimiza la distancia).`,
     `$D'(x) = 2x + 2(x^2-3)(2x) = 2x(2x^2-5)$.`,
     `$D'(x)=0 \\Rightarrow x=0$ (da $D=9$) o $x^2=\\dfrac52$ (da $D$ menor).`,
     `Abscisa $= \\pm\\sqrt{\\dfrac{5}{2}}$.`],
   ab:`"Punto más cercano" → minimiza la distancia AL CUADRADO (te ahorra la raíz, mismo mínimo).`,
   rc:`"Punto de la curva más cercano a $P$" → $D^2$ = suma de cuadrados de las diferencias, deriva.`},

  {id:`cd_c3_04`,c:3,t:`Análisis de gráficas`,f:`media`,e:`conceptual`,tipo:`mcq`,dif:2,tEsp:70,
   texto:`¿Cuántos puntos de inflexión tiene $f(x)=x^4-6x^2+5$?`,
   opciones:[`$2$`,`$1$`,`$0$`,`$3$`],correcta:0,
   resumen:`Contar los cambios de signo de $f''$.`,
   pasos:[`$f'(x)=4x^3-12x$; $f''(x)=12(x^2-1)$.`,
     `$f''=0$ en $x=\\pm1$. $f''>0$ para $|x|>1$, $f''<0$ para $|x|<1$.`,
     `Cambio de concavidad en $x=-1$ y en $x=1$: $2$ puntos de inflexión.`],
   ab:`Inflexión = $f''$ CAMBIA de signo. No basta $f''=0$ ($x^4$ tiene $f''(0)=0$ y no hay inflexión).`,
   rc:`"Cuántos puntos de inflexión" → raíces de $f''$ donde además cambia de signo.`},

  {id:`cd_c3_05`,c:3,t:`Teorema del valor medio`,f:`media`,e:`formula`,tipo:`numerica`,dif:2,tEsp:70,
   texto:`Para $f(x)=\\sqrt{x}$ en $[0,4]$, el valor $c\\in(0,4)$ del Teorema del Valor Medio es:`,
   respuesta:`1`,unidad:``,tolNum:0.001,puntaje:15,
   resumen:`$f'(c) = \\dfrac{f(4)-f(0)}{4-0}$.`,
   pasos:[`Pendiente secante: $\\dfrac{\\sqrt4-\\sqrt0}{4} = \\dfrac{1}{2}$.`,
     `$f'(x) = \\dfrac{1}{2\\sqrt x}$. Igualo: $\\dfrac{1}{2\\sqrt c} = \\dfrac12 \\Rightarrow \\sqrt c = 1 \\Rightarrow c = 1$.`],
   ab:`TVM: $f'(c)$ = pendiente de la recta que une los extremos. Despeja $c$, verifica que caiga dentro.`,
   rc:`"Valor $c$ del TVM" → $f'(c) = $ pendiente secante entre los extremos.`}
 ]
};

/* ── export ──────────────────────────────────────────────────────────────── */
window.SIM_TAX = SIM_TAX;
window.SIM_META = SIM_META;
window.SIM_SOL = SIM_SOL;
window.SIM_NEW = SIM_NEW;
})();
