/* Generadores de práctica de MathUNAL.
   Cada plantilla recibe un generador aleatorio con semilla y devuelve un ejercicio con
   enunciado, cuatro opciones (una correcta y tres con un error típico explicado), pista,
   solución paso a paso y un objeto chk con los datos para verificar la respuesta de forma
   independiente (ver verificar.py). Funciona en el navegador y en Node. */
(function (root) {
  'use strict';
  var T = String.raw;

  /* ---------- azar con semilla ---------- */
  function RNG(seed) {
    var s = seed >>> 0;
    function rnd() { s += 0x6D2B79F5; var t = s; t = Math.imul(t ^ t >>> 15, t | 1); t ^= t + Math.imul(t ^ t >>> 7, t | 61); return ((t ^ t >>> 14) >>> 0) / 4294967296; }
    return {
      rnd: rnd,
      ri: function (a, b) { return a + Math.floor(rnd() * (b - a + 1)); },
      pick: function (a) { return a[Math.floor(rnd() * a.length)]; },
      sign: function () { return rnd() < 0.5 ? -1 : 1; },
      shuffle: function (a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(rnd() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }
    };
  }

  /* ---------- fracciones ---------- */
  function gcd(a, b) { a = Math.abs(a); b = Math.abs(b); while (b) { var t = a % b; a = b; b = t; } return a || 1; }
  function F(n, d) { d = d === undefined ? 1 : d; if (d < 0) { n = -n; d = -d; } var g = gcd(n, d); return { n: n / g, d: d / g }; }
  function fadd(a, b) { return F(a.n * b.d + b.n * a.d, a.d * b.d); }
  function fmul(a, b) { return F(a.n * b.n, a.d * b.d); }
  function fdiv(a, b) { return F(a.n * b.d, a.d * b.n); }
  function fsub(a, b) { return fadd(a, F(-b.n, b.d)); }
  function ftex(f) { if (f.d === 1) return String(f.n); return (f.n < 0 ? '-' : '') + T`\dfrac{${Math.abs(f.n)}}{${f.d}}`; }
  function fval(f) { return f.d === 1 ? String(f.n) : f.n + '/' + f.d; }
  function fopt(f, e) { return { tex: ftex(f), v: fval(f), e: e }; }

  /* ---------- polinomios y sumas de términos ---------- */
  function xp(p) { return p === 0 ? { t: '', s: '1' } : p === 1 ? { t: 'x', s: 'x' } : { t: 'x^{' + p + '}', s: 'x**' + p }; }
  function sum(items) {
    var tex = '', sym = '';
    var first = true;
    items.forEach(function (it) {
      if (it.c === 0) return;
      var a = Math.abs(it.c), sg = it.c < 0 ? '-' : '+';
      var coef = (a === 1 && it.t !== '') ? '' : String(a);
      var piece = coef + it.t;
      if (first) { tex += (it.c < 0 ? '-' : '') + piece; first = false; }
      else tex += ' ' + sg + ' ' + piece;
      sym += '+(' + it.c + ')*' + it.s;
    });
    if (first) { tex = '0'; sym = '0'; }
    return { tex: tex, v: sym.replace(/^\+/, '') };
  }
  function it(c, p) { var q = xp(p); return { c: c, t: q.t, s: q.s }; }
  function vec(a) { return T`\left(${a.join(',\\ ')}\right)`; }
  function pmat(M) { return T`\begin{pmatrix}` + M.map(function (r) { return r.join(' & '); }).join(T` \\ `) + T`\end{pmatrix}`; }

  /* ---------- armado de opciones ---------- */
  function armar(r, correcta, malas) {
    var vistos = {}; vistos[JSON.stringify(correcta.v)] = 1; vistos[correcta.tex] = 1;
    var ops = [{ tex: correcta.tex, v: correcta.v, ok: true }];
    for (var i = 0; i < malas.length && ops.length < 4; i++) {
      var m = malas[i], k = JSON.stringify(m.v);
      if (vistos[k] || vistos[m.tex]) continue;
      vistos[k] = 1; vistos[m.tex] = 1;
      ops.push({ tex: m.tex, v: m.v, ok: false, e: m.e });
    }
    if (ops.length < 4) return null;
    return r.shuffle(ops);
  }

  /* ---------- plantillas ---------- */
  var PL = [];
  function def(o) { PL.push(o); }

  /* 1. Derivada de un producto */
  def({
    id: 'deriv-producto', tema: 'Derivada de un producto', curso: 'Cálculo Diferencial', lec: ['calculo-derivada-2'],
    gen: function (r) {
      var a = r.ri(2, 9), m = r.ri(2, 5), gk = r.pick(['sen', 'cos', 'exp']);
      var G = {
        sen: { t: T`\operatorname{sen}x`, s: 'sin(x)', dc: 1, dt: T`\cos x`, ds: 'cos(x)' },
        cos: { t: T`\cos x`, s: 'cos(x)', dc: -1, dt: T`\operatorname{sen}x`, ds: 'sin(x)' },
        exp: { t: T`e^{x}`, s: 'exp(x)', dc: 1, dt: T`e^{x}`, ds: 'exp(x)' }
      }[gk];
      var x1 = xp(m - 1), xm = xp(m);
      function termino(c, q, g, gs) { return { c: c, t: q.t + g, s: q.s + '*' + gs }; }
      var t1 = termino(a * m, x1, G.t, G.s), t2 = termino(a * G.dc, xm, G.dt, G.ds);
      var ok = sum([t1, t2]);
      var f = sum([{ c: a, t: xm.t + G.t, s: xm.s + '*' + G.s }]);
      var w1 = sum([termino(a * m * G.dc, x1, G.dt, G.ds)]);
      var w2 = sum([t1]);
      var w3 = sum([t1, { c: -t2.c, t: t2.t, s: t2.s }]);
      var w4 = sum([t2]);
      var ops = armar(r, ok, [
        { tex: w1.tex, v: w1.v, e: 'Derivó cada factor y multiplicó las derivadas. La derivada de un producto no es el producto de las derivadas.' },
        { tex: w2.tex, v: w2.v, e: 'Solo derivó el primer factor. Falta el término con la derivada del segundo factor.' },
        { tex: w3.tex, v: w3.v, e: 'Restó los dos términos. La regla del producto los suma, con cada signo propio.' },
        { tex: w4.tex, v: w4.v, e: 'Solo derivó el segundo factor. Falta el término con la derivada del primero.' }]);
      if (!ops) return null;
      return {
        enun: 'Deriva la función.', tex: 'f(x)=' + f.tex, ops: ops,
        pista: 'La regla del producto dice derivada del primero por el segundo, más el primero por la derivada del segundo.',
        pasos: [
          { tex: T`u=${xm.t === '' ? '' : a + xm.t},\quad v=${G.t}`, why: 'Se separan los dos factores.' },
          { tex: T`u'=${sum([it(a * m, m - 1)]).tex},\quad v'=${G.dc < 0 ? '-' : ''}${G.dt.replace(/^-/, '')}`, why: 'Se deriva cada factor por separado.' },
          { tex: T`f'(x)=u'v+uv'=${ok.tex}`, why: 'Se suman los dos términos de la regla del producto.' }],
        chk: { k: 'deriv', f: a + '*x**' + m + '*' + G.s }
      };
    }
  });

  /* 2. Regla de la cadena */
  def({
    id: 'deriv-cadena', tema: 'Regla de la cadena', curso: 'Cálculo Diferencial', lec: ['calculo-derivada-3'],
    gen: function (r) {
      var a = r.ri(1, 4), b = r.sign() * r.ri(1, 5), n = r.ri(3, 5);
      var inner = sum([it(a, 2), it(b, 0)]);
      function pot(k) { return k === 1 ? '(' + inner.tex + ')' : '(' + inner.tex + ')^{' + k + '}'; }
      var innerS = '(' + inner.v + ')';
      var ok = { tex: sum([it(2 * a * n, 1)]).tex + pot(n - 1), v: (2 * a * n) + '*x*' + innerS + '**' + (n - 1) };
      var w1 = { tex: n + pot(n - 1), v: n + '*' + innerS + '**' + (n - 1), e: 'Aplicó la regla de la potencia pero no multiplicó por la derivada de lo de adentro.' };
      var w2 = { tex: sum([it(2 * a * n, 1)]).tex + pot(n), v: (2 * a * n) + '*x*' + innerS + '**' + n, e: 'Multiplicó por la derivada de lo de adentro pero no bajó el exponente en uno.' };
      var w3 = { tex: sum([it(2 * a, 1)]).tex + pot(n - 1), v: (2 * a) + '*x*' + innerS + '**' + (n - 1), e: 'Olvidó el factor n que baja del exponente.' };
      var w4 = { tex: n + sum([it(2 * a, 1)]).tex + pot(n), v: (2 * a * n) + '*x*' + innerS + '**' + n, e: 'Dejó el exponente igual en vez de bajarlo.' };
      var w5 = { tex: n + pot(n - 1) + sum([it(2 * a, 1)]).tex.replace(/^/, '+'), v: n + '*' + innerS + '**' + (n - 1) + '+' + (2 * a) + '*x', e: 'Sumó las derivadas en lugar de multiplicarlas.' };
      var ops = armar(r, ok, [w1, w2, w3, w5, w4]);
      if (!ops) return null;
      return {
        enun: 'Deriva la función.', tex: 'f(x)=' + pot(n), ops: ops,
        pista: 'Deriva la potencia de afuera y multiplica por la derivada de lo de adentro.',
        pasos: [
          { tex: T`u=${inner.tex},\quad f=u^{${n}}`, why: 'Se identifica la función de adentro.' },
          { tex: T`\dfrac{df}{du}=${n}u^{${n - 1}},\quad \dfrac{du}{dx}=${sum([it(2 * a, 1)]).tex}`, why: 'Se deriva cada capa.' },
          { tex: T`f'(x)=${ok.tex}`, why: 'Se multiplican las dos derivadas.' }],
        chk: { k: 'deriv', f: innerS + '**' + n }
      };
    }
  });

  /* 3. Límite por factorización */
  def({
    id: 'limite-factor', tema: 'Límite por factorización', curso: 'Cálculo Diferencial', lec: ['calculo-limite-2'],
    gen: function (r) {
      var rr = r.pick([-4, -3, -2, -1, 1, 2, 3, 4, 5]), s = r.pick([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]);
      if (s === -rr) return null;
      var num = sum([it(1, 2), it(s - rr, 1), it(-rr * s, 0)]);
      var den = sum([it(1, 1), it(-rr, 0)]);
      var ans = rr + s;
      var ops = armar(r, { tex: String(ans), v: String(ans) }, [
        { tex: '0', v: '0', e: 'Al sustituir queda cero sobre cero, y eso no es el valor del límite. Hay que factorizar y cancelar.' },
        { tex: String(rr - s), v: String(rr - s), e: 'Cancelaron bien pero restaron en lugar de sumar los dos números del otro factor.' },
        { tex: String(s), v: String(s), e: 'Tomó solo el segundo número del factor que queda. Hay que evaluarlo completo en x igual a ' + rr + '.' },
        { tex: T`\text{no existe}`, v: 'zoo', e: 'Cero sobre cero es una indeterminación, y se resuelve cancelando el factor común.' },
        { tex: String(rr * s), v: String(rr * s), e: 'Multiplicó en lugar de sumar al evaluar el factor que queda.' }]);
      if (!ops) return null;
      return {
        enun: 'Calcula el límite.', tex: T`\lim_{x\to ${rr}}\dfrac{${num.tex}}{${den.tex}}`, ops: ops,
        pista: 'El numerador se anula en x igual a ' + rr + '. Factoriza y cancela.',
        pasos: [
          { tex: T`\dfrac{${num.tex}}{${den.tex}}=\dfrac{(x-${rr < 0 ? '(' + rr + ')' : rr})(x${s < 0 ? s : '+' + s})}{x-${rr < 0 ? '(' + rr + ')' : rr}}`, why: 'El numerador tiene como factor la misma resta del denominador.' },
          { tex: T`=x${s < 0 ? s : '+' + s}`, why: 'Se cancela el factor común, válido porque x es distinto de ' + rr + ' en el límite.' },
          { tex: T`\lim=${rr}${s < 0 ? s : '+' + s}=${ans}`, why: 'Ahora se sustituye.' }],
        chk: { k: 'limit', f: '(' + num.v + ')/(' + den.v + ')', x0: rr }
      };
    }
  });

  /* 4. Un paso del método de Newton */
  def({
    id: 'newton-paso', tema: 'Un paso del método de Newton', curso: 'Métodos Numéricos', lec: ['mn-newton', 'calculo-newton'],
    gen: function (r) {
      var c = r.pick([2, 3, 5, 6, 7, 8, 10, 11, 12, 13]), x0 = r.pick([2, 3, 4, 5, 6]);
      var X = F(x0), C = F(c);
      var fx = fsub(fmul(X, X), C), dfx = fmul(F(2), X);
      var ok = fsub(X, fdiv(fx, dfx));
      var ops = armar(r, fopt(ok), [
        fopt(fadd(X, fdiv(fx, dfx)), 'Sumó el cociente en lugar de restarlo. La fórmula es x menos f sobre f prima.'),
        fopt(fsub(X, fx), 'Restó solo f de x cero. Falta dividir entre la derivada.'),
        fopt(fsub(X, fdiv(dfx, fx)), 'Invirtió el cociente. Es f sobre f prima, no f prima sobre f.'),
        fopt(fsub(X, fdiv(fx, F(1))), 'Dividió entre uno en lugar de la derivada.')]);
      if (!ops) return null;
      return {
        enun: 'Con x cero igual a ' + x0 + ', calcula x uno con un paso del método de Newton.', tex: 'f(x)=x^{2}-' + c, ops: ops,
        pista: 'La fórmula es x uno igual a x cero menos f de x cero sobre f prima de x cero.',
        pasos: [
          { tex: T`f(${x0})=${ftex(fx)},\quad f'(x)=2x\ \Rightarrow\ f'(${x0})=${ftex(dfx)}`, why: 'Se evalúan la función y su derivada.' },
          { tex: T`x_{1}=${x0}-\dfrac{${ftex(fx)}}{${ftex(dfx)}}=${ftex(ok)}`, why: 'Se aplica la fórmula.' }],
        chk: { k: 'newton', f: 'x**2-' + c, x0: x0 }
      };
    }
  });

  /* 5. Integral por sustitución */
  def({
    id: 'integral-sust', tema: 'Integral por sustitución', curso: 'Cálculo Integral', lec: ['calcint-sustitucion'],
    gen: function (r) {
      var a = r.ri(1, 4), c = r.sign() * r.ri(1, 6), n = r.ri(2, 5);
      var u = sum([it(a, 2), it(c, 0)]);
      var us = '(' + u.v + ')';
      var integrando = sum([it(2 * a, 1)]).tex + '(' + u.tex + ')^{' + n + '}';
      var ok = { tex: T`\dfrac{(${u.tex})^{${n + 1}}}{${n + 1}}+C`, v: us + '**' + (n + 1) + '/' + (n + 1) };
      var ops = armar(r, ok, [
        { tex: T`(${u.tex})^{${n + 1}}+C`, v: us + '**' + (n + 1), e: 'Subió el exponente pero no dividió entre el nuevo exponente.' },
        { tex: T`\dfrac{(${u.tex})^{${n}}}{${n}}+C`, v: us + '**' + n + '/' + n, e: 'No subió el exponente. Al integrar una potencia el exponente aumenta en uno.' },
        { tex: T`\dfrac{(${u.tex})^{${n + 1}}}{${2 * a * (n + 1)}}+C`, v: us + '**' + (n + 1) + '/' + (2 * a * (n + 1)), e: 'Dividió también entre la derivada de u, pero ese factor ya estaba en el integrando y se usa para formar du.' },
        { tex: T`${n + 1}(${u.tex})^{${n + 1}}+C`, v: (n + 1) + '*' + us + '**' + (n + 1), e: 'Multiplicó por el exponente. Al integrar se divide, no se multiplica.' }]);
      if (!ops) return null;
      return {
        enun: 'Calcula la integral indefinida.', tex: T`\int ${integrando}\,dx`, ops: ops,
        pista: 'Llama u a ' + u.tex + '. Mira si su derivada aparece en el integrando.',
        pasos: [
          { tex: T`u=${u.tex},\quad du=${sum([it(2 * a, 1)]).tex}\,dx`, why: 'La derivada de lo de adentro es justo el otro factor.' },
          { tex: T`\int u^{${n}}\,du=\dfrac{u^{${n + 1}}}{${n + 1}}+C`, why: 'La integral queda como una potencia sencilla.' },
          { tex: T`=${ok.tex}`, why: 'Se regresa a x.' }],
        chk: { k: 'antider', f: sum([it(2 * a, 1)]).v + '*' + us + '**' + n }
      };
    }
  });

  /* 6. Integral por partes (exponencial, seno y coseno) */
  def({
    id: 'integral-partes', tema: 'Integral por partes', curso: 'Cálculo Integral', lec: ['calcint-partes'],
    gen: function (r) {
      var fam = r.pick(['exp', 'cos', 'sen']);
      var k = fam === 'exp' ? r.pick([2, 3, 4, 5, -1, -2, -3]) : r.ri(1, 6), kk = k * k;
      var kt = k === 1 ? '' : String(k);
      if (fam === 'exp') {
        var ex = T`e^{${kt}x}`, exs = 'exp(' + k + '*x)';
        var kx = sum([it(k, 1), it(-1, 0)]).tex, kxm = sum([it(k, 1), it(1, 0)]).tex;
        var ok = { tex: T`\dfrac{(${kx})${ex}}{${kk}}+C`, v: '(' + k + '*x-1)*' + exs + '/' + kk };
        var ops = armar(r, ok, [
          { tex: T`\dfrac{(${kxm})${ex}}{${kk}}+C`, v: '(' + k + '*x+1)*' + exs + '/' + kk, e: 'Se equivocó de signo en el segundo término. Al restar la integral de v por du aparece un menos.' },
          { tex: T`\dfrac{x${ex}}{${k}}+C`, v: 'x*' + exs + '/' + k, e: 'Se quedó en el primer término. Falta restar la integral de v por du.' },
          { tex: T`\dfrac{(${kx})${ex}}{${k}}+C`, v: '(' + k + '*x-1)*' + exs + '/' + k, e: 'El denominador del segundo término debe ser k al cuadrado, porque la exponencial se integra dos veces.' },
          { tex: T`\dfrac{x^{2}}{2}${ex}+C`, v: 'x**2/2*' + exs, e: 'Integró x pero dejó la exponencial sin integrar.' }]);
        if (!ops) return null;
        return {
          enun: 'Calcula la integral indefinida.', tex: T`\int x\,${ex}\,dx`, ops: ops,
          pista: 'Elige u igual a x, porque al derivarla se simplifica, y dv igual a la exponencial.',
          pasos: [
            { tex: T`u=x,\ dv=${ex}dx\ \Rightarrow\ du=dx,\ v=\dfrac{${ex}}{${k}}`, why: 'Se elige u de modo que la nueva integral sea más sencilla.' },
            { tex: T`\int u\,dv=uv-\int v\,du=\dfrac{x${ex}}{${k}}-\dfrac{1}{${k}}\int ${ex}dx`, why: 'Se aplica integración por partes.' },
            { tex: T`=${ok.tex}`, why: 'Se integra la exponencial y se agrupa.' }],
          chk: { k: 'antider', f: 'x*' + exs }
        };
      }
      var s = fam === 'cos' ? 'cos' : 'sin', tc = fam === 'cos' ? T`\cos` : T`\operatorname{sen}`;
      var og = fam === 'cos' ? 'sin' : 'cos', tog = fam === 'cos' ? T`\operatorname{sen}` : T`\cos`;
      var arg = '(' + k + '*x)', targ = T`(${kt}x)`;
      var sg = fam === 'cos' ? 1 : -1;
      function exprTex(sx, c1, tx, c2, ty, d1, d2) {
        var p1 = (c1 < 0 ? '-' : '') + T`\dfrac{x${tx}${targ}}{${d1}}`;
        var p2 = (c2 < 0 ? '-' : '+') + T`\dfrac{${ty}${targ}}{${d2}}`;
        return p1 + ' ' + p2 + '+C';
      }
      function exprSym(c1, a1, c2, a2, d1, d2) { return '(' + c1 + ')*x*' + a1 + arg + '/' + d1 + '+(' + c2 + ')*' + a2 + arg + '/' + d2; }
      var c1 = fam === 'cos' ? 1 : -1;
      var main = fam === 'cos' ? { t1: tog, a1: 'sin', t2: tc, a2: 'cos' } : { t1: tog, a1: 'cos', t2: tc, a2: 'sin' };
      var okx = { tex: exprTex(0, c1, main.t1, 1, main.t2, k, kk), v: exprSym(c1, main.a1, 1, main.a2, k, kk) };
      var ops2 = armar(r, okx, [
        { tex: exprTex(0, c1, main.t1, -1, main.t2, k, kk), v: exprSym(c1, main.a1, -1, main.a2, k, kk), e: 'Se equivocó de signo en el segundo término. Revisa el signo al integrar la función trigonométrica.' },
        { tex: exprTex(0, c1, main.t1, 1, main.t2, k, k), v: exprSym(c1, main.a1, 1, main.a2, k, k), e: 'El denominador del segundo término debe ser k al cuadrado, porque se integra dos veces.' },
        { tex: exprTex(0, -c1, main.t1, 1, main.t2, k, kk), v: exprSym(-c1, main.a1, 1, main.a2, k, kk), e: 'Se equivocó de signo en el primer término. Revisa el signo de la integral de la función trigonométrica.' },
        { tex: T`\dfrac{x^{2}}{2}${tc}${targ}+C`, v: 'x**2/2*' + s + arg, e: 'Integró x pero dejó la función trigonométrica sin integrar.' }]);
      if (!ops2) return null;
      return {
        enun: 'Calcula la integral indefinida.', tex: T`\int x\,${tc}${targ}\,dx`, ops: ops2,
        pista: 'Elige u igual a x y dv igual a la función trigonométrica. Hay que integrar por partes dos veces la parte trigonométrica.',
        pasos: [
          { tex: T`u=x,\ dv=${tc}${targ}dx\ \Rightarrow\ du=dx,\ v=${sg < 0 ? '-' : ''}\dfrac{${tog}${targ}}{${k}}`, why: 'Se elige u de modo que la nueva integral sea más sencilla.' },
          { tex: T`\int u\,dv=uv-\int v\,du`, why: 'Se aplica integración por partes.' },
          { tex: T`=${okx.tex}`, why: 'Se integra lo que queda y se agrupa.' }],
        chk: { k: 'antider', f: 'x*' + s + arg }
      };
    }
  });

  /* 7. Integral definida de un polinomio */
  def({
    id: 'integral-def', tema: 'Integral definida de un polinomio', curso: 'Cálculo Integral', lec: ['calcint-tfc', 'calculo-tfc'],
    gen: function (r) {
      var a = r.ri(1, 6), b = r.ri(1, 6), p = r.ri(1, 4);
      var ok = fadd(F(a * p * p * p, 3), F(b * p * p, 2));
      var ops = armar(r, fopt(ok), [
        fopt(fadd(F(a * p * p * p, 3), F(b * p * p, 1)), 'No dividió el segundo término entre 2 al integrar bx.'),
        fopt(F(2 * a * p + b), 'Derivó en lugar de integrar.'),
        fopt(fadd(F(a * p * p * p, 1), F(b * p * p, 2)), 'No dividió el primer término entre 3 al integrar ax cuadrado.'),
        fopt(fadd(F(a * p * p, 2), F(b * p, 1)), 'Bajó el exponente en lugar de subirlo. Al integrar el exponente aumenta.')]);
      if (!ops) return null;
      var integ = sum([it(a, 2), it(b, 1)]);
      return {
        enun: 'Calcula la integral definida.', tex: T`\int_{0}^{${p}}\left(${integ.tex}\right)dx`, ops: ops,
        pista: 'Encuentra una antiderivada y evalúala en los dos extremos.',
        pasos: [
          { tex: T`F(x)=\dfrac{${a}}{3}x^{3}+\dfrac{${b}}{2}x^{2}`, why: 'Cada potencia sube en uno y se divide entre el nuevo exponente.' },
          { tex: T`F(${p})-F(0)=${ftex(ok)}`, why: 'Se evalúa en los extremos y se resta.' }],
        chk: { k: 'defint', f: integ.v, lo: 0, hi: p }
      };
    }
  });

  /* 8. Determinante 3 por 3 */
  def({
    id: 'det-3', tema: 'Determinante de una matriz 3 por 3', curso: 'Álgebra Lineal', lec: ['alglin-det'],
    gen: function (r) {
      var M = []; for (var i = 0; i < 3; i++) { M.push([]); for (var j = 0; j < 3; j++) M[i].push(r.ri(-3, 4)); }
      var a = M[0][0], b = M[0][1], c = M[0][2];
      var m11 = M[1][1] * M[2][2] - M[1][2] * M[2][1];
      var m12 = M[1][0] * M[2][2] - M[1][2] * M[2][0];
      var m13 = M[1][0] * M[2][1] - M[1][1] * M[2][0];
      var det = a * m11 - b * m12 + c * m13;
      var ops = armar(r, { tex: String(det), v: det }, [
        { tex: String(a * m11 + b * m12 + c * m13), v: a * m11 + b * m12 + c * m13, e: 'No alternó los signos del desarrollo por cofactores. Los signos son más, menos, más.' },
        { tex: String(a * M[1][1] * M[2][2]), v: a * M[1][1] * M[2][2], e: 'Multiplicó solo la diagonal principal. Eso no es el determinante en una matriz 3 por 3.' },
        { tex: String(-det), v: -det, e: 'El signo final está invertido. Revisa el signo de cada cofactor.' },
        { tex: String(a * m11 - b * m12 - c * m13), v: a * m11 - b * m12 - c * m13, e: 'El último cofactor lleva signo más, no menos.' },
        { tex: String(det + 2), v: det + 2, e: 'Hay un error de cuenta en alguno de los menores de 2 por 2.' }]);
      if (!ops) return null;
      return {
        enun: 'Calcula el determinante.', tex: T`\det\,${pmat(M)}`, ops: ops,
        pista: 'Desarrolla por la primera fila con los signos más, menos, más.',
        pasos: [
          { tex: T`\det=${a}\cdot(${m11})-(${b})\cdot(${m12})+(${c})\cdot(${m13})`, why: 'Cada elemento de la primera fila multiplica el determinante de su menor.' },
          { tex: T`\det=${det}`, why: 'Se hacen las cuentas.' }],
        chk: { k: 'det', M: M }
      };
    }
  });

  /* 9. Valores propios 2 por 2 */
  def({
    id: 'eig-2', tema: 'Valores propios de una matriz 2 por 2', curso: 'Álgebra Lineal', lec: ['alglin-propios'],
    gen: function (r) {
      var l1 = r.ri(-2, 5), l2 = r.ri(-2, 5);
      if (l1 >= l2) return null;
      var tr = l1 + l2, dt = l1 * l2, p = r.ri(1, 4), s = tr - p;
      var qr = p * s - dt, q = qr === 0 ? 0 : 1, rr = qr === 0 ? r.ri(0, 3) : qr;
      var M = [[p, q], [rr, s]];
      function par(x, y) { return { tex: x + T`\ \text{y}\ ` + y, v: [x, y].sort(function (u, w) { return u - w; }) }; }
      var ops = armar(r, par(l1, l2), [
        Object.assign(par(-l1, -l2), { e: 'Cambió el signo de los valores. Se resuelve el determinante de A menos lambda por la identidad igual a cero.' }),
        Object.assign(par(p, s), { e: 'Tomó los elementos de la diagonal como valores propios. Eso solo es cierto en una matriz triangular.' }),
        Object.assign(par(tr, dt), { e: 'Confundió la suma y el producto de los valores propios con los valores propios mismos.' }),
        Object.assign(par(l1 + 1, l2 + 1), { e: 'Hay un error en la ecuación característica. Revisa la traza y el determinante.' })]);
      if (!ops) return null;
      return {
        enun: 'Halla los valores propios de la matriz.', tex: 'A=' + pmat(M), ops: ops,
        pista: 'La ecuación es lambda al cuadrado menos la traza por lambda más el determinante, igual a cero.',
        pasos: [
          { tex: T`\operatorname{tr}A=${tr},\quad \det A=${dt}`, why: 'Se calculan la traza y el determinante.' },
          { tex: T`\lambda^{2}${-tr < 0 ? '-' + tr : '+' + (-tr)}\lambda${dt < 0 ? dt : '+' + dt}=0`, why: 'Esa es la ecuación característica.' },
          { tex: T`(\lambda-${l1 < 0 ? '(' + l1 + ')' : l1})(\lambda-${l2 < 0 ? '(' + l2 + ')' : l2})=0`, why: 'Se factoriza.' }],
        chk: { k: 'eig', M: M }
      };
    }
  });

  /* 10. Sistema 2 por 2 */
  def({
    id: 'sistema-2', tema: 'Sistema de dos ecuaciones lineales', curso: 'Álgebra Lineal', lec: ['alglin-sistemas', 'matbas-sistemas'],
    gen: function (r) {
      var x = r.pick([-3, -2, -1, 1, 2, 3, 4]), y = r.pick([-3, -2, -1, 1, 2, 3, 4]);
      if (Math.abs(x) === Math.abs(y)) return null;
      var a = r.ri(1, 4), b = r.sign() * r.ri(1, 4), c = r.sign() * r.ri(1, 4), d = r.sign() * r.ri(1, 4);
      if (a * d - b * c === 0) return null;
      var e = a * x + b * y, f = c * x + d * y;
      function par(u, w) { return { tex: T`x=${u},\ y=${w}`, v: [u, w] }; }
      var ops = armar(r, par(x, y), [
        Object.assign(par(y, x), { e: 'Intercambió los valores de x y de y al leer el resultado.' }),
        Object.assign(par(x, -y), { e: 'Hay un error de signo al despejar y. Sustituye en las dos ecuaciones para comprobar.' }),
        Object.assign(par(-x, y), { e: 'Hay un error de signo al despejar x. Sustituye en las dos ecuaciones para comprobar.' }),
        Object.assign(par(x + 1, y), { e: 'Cumple una ecuación pero no la otra. La solución debe cumplir las dos.' })]);
      if (!ops) return null;
      var eq1 = sum([{ c: a, t: 'x', s: 'x' }, { c: b, t: 'y', s: 'y' }]).tex;
      var eq2 = sum([{ c: c, t: 'x', s: 'x' }, { c: d, t: 'y', s: 'y' }]).tex;
      var D = a * d - b * c;
      return {
        enun: 'Resuelve el sistema.', tex: T`\begin{cases}${eq1}=${e}\\ ${eq2}=${f}\end{cases}`, ops: ops,
        pista: 'Puedes eliminar una variable multiplicando las ecuaciones por números adecuados, o usar la regla de Cramer.',
        pasos: [
          { tex: T`D=${a}\cdot${d < 0 ? '(' + d + ')' : d}-(${b})(${c})=${D}`, why: 'El determinante de los coeficientes es distinto de cero.' },
          { tex: T`x=\dfrac{${e}\cdot${d < 0 ? '(' + d + ')' : d}-(${b})(${f})}{${D}}=${x},\quad y=\dfrac{${a}\cdot${f < 0 ? '(' + f + ')' : f}-${e}\cdot(${c})}{${D}}=${y}`, why: 'Se aplica la regla de Cramer.' }],
        chk: { k: 'linsys', A: [[a, b], [c, d]], b: [e, f] }
      };
    }
  });

  /* 11. EDO y' = k y con condición inicial */
  def({
    id: 'edo-exp', tema: 'Ecuación y prima igual a k por y', curso: 'Ecuaciones Diferenciales', lec: ['edo-separables'],
    gen: function (r) {
      var k = r.pick([2, 3, 4, 5, 6, -2, -3, -4, -5]), y0 = r.ri(2, 9);
      function e(kk) { return 'exp(' + kk + '*t)'; }
      function et(kk) { return T`e^{${kk === 1 ? '' : kk}t}`; }
      var ok = { tex: y0 + et(k), v: y0 + '*' + e(k) };
      var ops = armar(r, ok, [
        { tex: et(k), v: e(k), e: 'Olvidó la condición inicial. La constante de integración vale ' + y0 + ', no 1.' },
        { tex: y0 + T`e^{t/${k}}`, v: y0 + '*exp(t/' + k + ')', e: 'Puso la constante dividiendo en el exponente. Al integrar queda k por t.' },
        { tex: (k * y0) + et(k), v: (k * y0) + '*' + e(k), e: 'Multiplicó la constante por k. Eso es y prima, no y.' },
        { tex: y0 + et(-k), v: y0 + '*' + e(-k), e: 'El signo del exponente está cambiado.' }]);
      if (!ops) return null;
      return {
        enun: 'Halla la solución del problema con valor inicial.', tex: T`y'=${k}y,\qquad y(0)=${y0}`, ops: ops,
        pista: 'Separa las variables y integra los dos lados.',
        pasos: [
          { tex: T`\dfrac{dy}{y}=${k}\,dt\ \Rightarrow\ \ln|y|=${k}t+C`, why: 'Se separan las variables y se integra.' },
          { tex: T`y=Ae^{${k}t},\quad y(0)=A=${y0}`, why: 'La condición inicial fija la constante.' },
          { tex: T`y(t)=${ok.tex}`, why: 'Esa es la solución.' }],
        chk: { k: 'edo', rhs: k + '*y', y0: y0 }
      };
    }
  });

  /* 12. EDO lineal, valor de equilibrio */
  def({
    id: 'edo-equil', tema: 'A dónde tiende la solución', curso: 'Ecuaciones Diferenciales', lec: ['edo-lineal', 'edo-autonomas'],
    gen: function (r) {
      var a = r.ri(2, 5), b = r.ri(2, 12), y0 = r.ri(0, 6);
      var ok = F(b, a);
      var ops = armar(r, fopt(ok), [
        fopt(F(-b, a), 'Hay un error de signo. Al anular la derivada queda a por y igual a b.'),
        fopt(F(a, b), 'Invirtió el cociente. El equilibrio es b sobre a.'),
        fopt(F(b), 'Tomó b como equilibrio sin dividir entre el coeficiente de y.'),
        fopt(F(y0), 'Tomó el valor inicial. La solución tiende al equilibrio, no se queda en el valor inicial.')]);
      if (!ops) return null;
      return {
        enun: 'Halla el valor al que tiende y cuando t crece.', tex: T`y'+${a}y=${b},\qquad y(0)=${y0}`, ops: ops,
        pista: 'El equilibrio es donde la derivada vale cero. El coeficiente de y es positivo, así que la solución se acerca a él.',
        pasos: [
          { tex: T`y'=0\ \Rightarrow\ ${a}y=${b}`, why: 'En el equilibrio la derivada se anula.' },
          { tex: T`y=${ftex(ok)}`, why: 'Se despeja y. Como a es positivo, el equilibrio atrae.' }],
        chk: { k: 'edolim', a: a, b: b, y0: y0 }
      };
    }
  });

  /* 13. Cuadrado de un binomio */
  def({
    id: 'binomio', tema: 'Cuadrado de un binomio', curso: 'Matemáticas Básicas', lec: ['matbas-notables'],
    gen: function (r) {
      var a = r.ri(1, 6), b = r.sign() * r.ri(1, 9);
      var inner = sum([it(a, 1), it(b, 0)]).tex;
      var ok = sum([it(a * a, 2), it(2 * a * b, 1), it(b * b, 0)]);
      var w1 = sum([it(a * a, 2), it(b * b, 0)]);
      var w2 = sum([it(a * a, 2), it(a * b, 1), it(b * b, 0)]);
      var w3 = sum([it(a * a, 2), it(2 * a * b, 1), it(-b * b, 0)]);
      var w4 = sum([it(a, 2), it(2 * a * b, 1), it(b * b, 0)]);
      var ops = armar(r, ok, [
        { tex: w1.tex, v: w1.v, e: 'Olvidó el doble producto. El cuadrado de una suma no es la suma de los cuadrados.' },
        { tex: w2.tex, v: w2.v, e: 'Tomó el producto de los dos términos una vez y no dos veces.' },
        { tex: w3.tex, v: w3.v, e: 'El último término siempre es positivo, porque es el cuadrado del segundo término.' },
        { tex: w4.tex, v: w4.v, e: 'No elevó al cuadrado el coeficiente del primer término.' }]);
      if (!ops) return null;
      return {
        enun: 'Desarrolla la expresión.', tex: '(' + inner + ')^{2}', ops: ops,
        pista: 'El cuadrado de un binomio es el cuadrado del primero, más el doble producto, más el cuadrado del segundo.',
        pasos: [
          { tex: T`(${inner})^{2}=(${inner})(${inner})`, why: 'Cuadrado quiere decir multiplicar por sí mismo.' },
          { tex: T`=${ok.tex}`, why: 'Se reparte y se juntan los dos términos del medio.' }],
        chk: { k: 'expand', f: '(' + sum([it(a, 1), it(b, 0)]).v + ')**2' }
      };
    }
  });

  /* 14. Raíces de un cuadrático factorizable */
  def({
    id: 'raices', tema: 'Raíces de un polinomio cuadrático', curso: 'Matemáticas Básicas', lec: ['matbas-cuadraticas'],
    gen: function (r) {
      var p = r.pick([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]), q = r.pick([-6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6]);
      if (p >= q || p + q === 0) return null;
      var B = -(p + q), C = p * q;
      function par(u, w) { var s = [u, w].sort(function (x, y) { return x - y; }); return { tex: s[0] + T`\ \text{y}\ ` + s[1], v: s }; }
      var ops = armar(r, par(p, q), [
        Object.assign(par(-p, -q), { e: 'Cambió el signo de las raíces. Si el factor es x menos p, la raíz es p.' }),
        Object.assign(par(B, C), { e: 'Tomó los coeficientes como raíces. Las raíces son los números cuya suma es menos B y cuyo producto es C.' }),
        Object.assign(par(p, -q), { e: 'Solo una raíz tiene el signo correcto. Comprueba sustituyendo.' }),
        Object.assign(par(p + 1, q), { e: 'Una de las dos no anula el polinomio. Comprueba sustituyendo.' })]);
      if (!ops) return null;
      var poly = sum([it(1, 2), it(B, 1), it(C, 0)]);
      return {
        enun: 'Halla las raíces.', tex: poly.tex + '=0', ops: ops,
        pista: 'Busca dos números cuyo producto sea ' + C + ' y cuya suma sea ' + (-B) + '.',
        pasos: [
          { tex: T`x^{2}${B < 0 ? B + 'x' : '+' + B + 'x'}${C < 0 ? C : '+' + C}=(x${-p < 0 ? -p : '+' + (-p)})(x${-q < 0 ? -q : '+' + (-q)})`, why: 'Se factoriza buscando dos números con esa suma y ese producto.' },
          { tex: T`x=${p},\quad x=${q}`, why: 'Cada factor igualado a cero da una raíz.' }],
        chk: { k: 'roots', f: poly.v }
      };
    }
  });

  /* 15. Vectores perpendiculares */
  def({
    id: 'perpend', tema: 'Vectores perpendiculares', curso: 'Geometría Vectorial', lec: ['geovec-punto', 'geovec-r3'],
    gen: function (r) {
      var a = r.ri(-3, 4), b = r.ri(1, 4), d = r.ri(-3, 4), c = r.pick([1, 2, 3, -1, -2]), k = r.pick([-3, -2, -1, 1, 2, 3]);
      var num = -c * k - a * d;
      if (num % b !== 0) return null;
      var e = num / b;
      var dot = a * d + b * e;
      var ops = armar(r, { tex: String(k), v: k }, [
        { tex: String(-k), v: -k, e: 'Hay un error de signo al despejar k de la ecuación.' },
        { tex: String(dot), v: dot, e: 'Calculó el producto punto de los dos primeros componentes pero no lo igualó con el término que falta.' },
        { tex: String(dot / c === Math.floor(dot / c) ? dot / c : dot + 1), v: dot / c === Math.floor(dot / c) ? dot / c : dot + 1, e: 'Dividió sin el signo menos. El producto punto debe ser cero, así que k vale menos esa cantidad entre c.' },
        { tex: String(k + 1), v: k + 1, e: 'Revisa la cuenta del producto punto. Debe dar exactamente cero.' }]);
      if (!ops) return null;
      return {
        enun: 'Halla el valor de k para que los vectores sean perpendiculares.', tex: T`\mathbf{u}=${vec([a, b, c])},\qquad \mathbf{v}=${vec([d, e, 'k'])}`, ops: ops,
        pista: 'Dos vectores son perpendiculares cuando su producto punto vale cero.',
        pasos: [
          { tex: T`\mathbf{u}\cdot\mathbf{v}=${a}\cdot${d < 0 ? '(' + d + ')' : d}+${b}\cdot${e < 0 ? '(' + e + ')' : e}+${c}k=${dot}+${c}k`, why: 'Se multiplican los componentes y se suman.' },
          { tex: T`${dot}+${c}k=0\ \Rightarrow\ k=${k}`, why: 'Se iguala a cero y se despeja.' }],
        chk: { k: 'perp', u: [a, b, c], v: [d, e] }
      };
    }
  });

  /* 16. Producto vectorial */
  def({
    id: 'cruz', tema: 'Producto vectorial', curso: 'Geometría Vectorial', lec: ['geovec-cruz'],
    gen: function (r) {
      var u = [r.ri(-3, 4), r.ri(-3, 4), r.ri(-3, 4)], v = [r.ri(-3, 4), r.ri(-3, 4), r.ri(-3, 4)];
      var w = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]];
      var w2 = [w[0], -w[1], w[2]];
      var w3 = w.map(function (z) { return -z; });
      var w4 = [u[1] * v[2] + u[2] * v[1], u[2] * v[0] + u[0] * v[2], u[0] * v[1] + u[1] * v[0]];
      var w5 = [u[0] * v[0], u[1] * v[1], u[2] * v[2]];
      function o(z, e) { return { tex: vec(z), v: z, e: e }; }
      var ops = armar(r, { tex: vec(w), v: w }, [
        o(w2, 'Olvidó que el componente del medio lleva signo menos en el desarrollo por cofactores.'),
        o(w3, 'Calculó v cruz u. El producto vectorial cambia de signo al invertir el orden.'),
        o(w4, 'Sumó en lugar de restar los dos productos de cada componente.'),
        o(w5, 'Multiplicó componente a componente. Eso no es el producto vectorial.')]);
      if (!ops) return null;
      return {
        enun: 'Calcula el producto vectorial.', tex: T`\mathbf{u}\times\mathbf{v}\ \text{con}\ \mathbf{u}=${vec(u)},\ \mathbf{v}=${vec(v)}`, ops: ops,
        pista: 'Usa el determinante simbólico con i, j, k y cuida el signo del componente del medio.',
        pasos: [
          { tex: T`\mathbf{u}\times\mathbf{v}=\begin{vmatrix}\mathbf{i}&\mathbf{j}&\mathbf{k}\\ ${u.join('&')}\\ ${v.join('&')}\end{vmatrix}`, why: 'Se arma el determinante.' },
          { tex: T`=${vec(w)}`, why: 'Se desarrolla por la primera fila con signos más, menos, más.' }],
        chk: { k: 'cross', u: u, v: v }
      };
    }
  });

  /* 17. Combinaciones */
  def({
    id: 'comb', tema: 'Combinaciones', curso: 'Matemáticas Discretas', lec: ['disc-combinatoria', 'disc-conteo'],
    gen: function (r) {
      var n = r.ri(6, 20), k = r.ri(2, 5);
      function C(a, b) { var x = 1; for (var i = 1; i <= b; i++) x = x * (a - b + i) / i; return Math.round(x); }
      function P(a, b) { var x = 1; for (var i = 0; i < b; i++) x *= (a - i); return x; }
      var ok = C(n, k);
      var ops = armar(r, { tex: String(ok), v: ok }, [
        { tex: String(P(n, k)), v: P(n, k), e: 'Contó los grupos como si el orden importara. En un comité el orden no importa, y hay que dividir entre k factorial.' },
        { tex: String(Math.pow(n, k)), v: Math.pow(n, k), e: 'Permitió repetir personas. Aquí cada persona se escoge una sola vez.' },
        { tex: String(C(n - 1, k)), v: C(n - 1, k), e: 'Usó n menos uno en lugar de n. Hay n personas para escoger.' },
        { tex: String(n * k), v: n * k, e: 'Multiplicó n por k. Los grupos no se cuentan así.' }]);
      if (!ops) return null;
      return {
        enun: '¿De cuántas formas se pueden escoger ' + k + ' personas de un grupo de ' + n + ' para formar un comité? El orden no importa.', tex: '', ops: ops,
        pista: 'Cuando el orden no importa, se cuentan las ordenaciones y se divide entre las formas de ordenar lo escogido.',
        pasos: [
          { tex: T`\binom{${n}}{${k}}=\dfrac{${n}!}{${k}!\,${n - k}!}`, why: 'Es el número combinatorio.' },
          { tex: T`=${ok}`, why: 'Se simplifica.' }],
        chk: { k: 'comb', n: n, kk: k }
      };
    }
  });

  /* 18. Gradiente en un punto */
  def({
    id: 'gradiente', tema: 'Gradiente en un punto', curso: 'Cálculo en Varias Variables', lec: ['cv-gradiente', 'cv-parciales'],
    gen: function (r) {
      var a = r.ri(1, 4), b = r.ri(1, 4), p = r.ri(-2, 3), q = r.ri(-2, 3);
      if (p === q || p === 0 || q === 0) return null;
      function gx(x, y) { return 2 * a * x * y + b * y * y; }
      function gy(x, y) { return a * x * x + 2 * b * x * y; }
      var g = [gx(p, q), gy(p, q)];
      function o(z, e) { return { tex: vec(z), v: z, e: e }; }
      var ops = armar(r, { tex: vec(g), v: g }, [
        o([g[1], g[0]], 'Intercambió las dos componentes. La primera es la derivada respecto de x.'),
        o([2 * a * p * q, a * p * p], 'Al derivar respecto de una variable olvidó el término del otro sumando.'),
        o([gx(q, p), gy(q, p)], 'Evaluó en el punto con las coordenadas cambiadas.'),
        o([gx(p, q), -gy(p, q)], 'Cambió el signo de la segunda componente sin motivo.')]);
      if (!ops) return null;
      var f = sum([{ c: a, t: 'x^{2}y', s: 'x**2*y' }, { c: b, t: 'xy^{2}', s: 'x*y**2' }]);
      return {
        enun: 'Calcula el gradiente en el punto (' + p + ', ' + q + ').', tex: 'f(x,y)=' + f.tex, ops: ops,
        pista: 'El gradiente tiene las dos derivadas parciales como componentes. Deriva primero y evalúa después.',
        pasos: [
          { tex: T`f_{x}=${sum([{ c: 2 * a, t: 'xy', s: 'x*y' }, { c: b, t: 'y^{2}', s: 'y**2' }]).tex},\quad f_{y}=${sum([{ c: a, t: 'x^{2}', s: 'x**2' }, { c: 2 * b, t: 'xy', s: 'x*y' }]).tex}`, why: 'Se deriva respecto de cada variable.' },
          { tex: T`\nabla f(${p},${q})=${vec(g)}`, why: 'Se evalúa en el punto.' }],
        chk: { k: 'grad', f: f.v, pt: [p, q] }
      };
    }
  });

  /* 19. Integral doble sobre un rectángulo */
  def({
    id: 'integral-doble', tema: 'Integral doble sobre un rectángulo', curso: 'Cálculo en Varias Variables', lec: ['cv-dobles'],
    gen: function (r) {
      var a = r.ri(1, 5), b = r.ri(1, 5), p = r.ri(1, 4), q = r.ri(1, 4);
      var ok = fadd(F(a * p * p * q, 2), F(b * p * q * q, 2));
      var ops = armar(r, fopt(ok), [
        fopt(fadd(F(a * p * q * q, 2), F(b * p * p * q, 2)), 'Intercambió los límites de las dos variables. x va de 0 a ' + p + ' y y va de 0 a ' + q + '.'),
        fopt(fadd(F(a * p * p * q, 1), F(b * p * q * q, 1)), 'No dividió entre 2 al integrar cada término.'),
        fopt(fadd(F(a * p * p, 2), F(b * q * q, 2)), 'Olvidó multiplicar por la longitud del otro lado en cada término.'),
        fopt(fadd(F(a * p * p * q, 2), F(b * p * q * q, 1)), 'No dividió entre 2 en el segundo término.')]);
      if (!ops) return null;
      return {
        enun: 'Calcula la integral doble.', tex: T`\int_{0}^{${p}}\int_{0}^{${q}}\left(${a}x+${b}y\right)dy\,dx`, ops: ops,
        pista: 'Integra primero respecto de y tratando x como constante, y luego respecto de x.',
        pasos: [
          { tex: T`\int_{0}^{${q}}(${a}x+${b}y)\,dy=${a * q}x+\dfrac{${b * q * q}}{2}`, why: 'Se integra respecto de y.' },
          { tex: T`\int_{0}^{${p}}\left(${a * q}x+\dfrac{${b * q * q}}{2}\right)dx=${ftex(ok)}`, why: 'Se integra respecto de x.' }],
        chk: { k: 'dint', f: a + '*x+' + b + '*y', p: p, q: q }
      };
    }
  });

  /* 20. Bisección, cuántos pasos */
  def({
    id: 'biseccion', tema: 'Cuántos pasos de bisección', curso: 'Métodos Numéricos', lec: ['mn-biseccion'],
    gen: function (r) {
      var L = r.pick([1, 2, 3, 4, 5, 6, 8, 10, 12, 20]), tolE = r.pick([1, 2, 3, 4, 5]);
      var tol = Math.pow(10, -tolE);
      var n = 0; while (L / Math.pow(2, n) >= tol * (1 - 1e-12)) n++;
      var ops = armar(r, { tex: String(n), v: n }, [
        { tex: String(n - 1), v: n - 1, e: 'Se quedó un paso corto. Con ese número el intervalo todavía no es menor que la tolerancia.' },
        { tex: String(n + 2), v: n + 2, e: 'Se pasó. Con menos pasos ya se cumple la tolerancia.' },
        { tex: String(Math.round(L / tol)), v: Math.round(L / tol), e: 'Dividió la longitud entre la tolerancia. Cada paso reduce el intervalo a la mitad, así que se necesita un logaritmo en base 2.' },
        { tex: String(n + 4), v: n + 4, e: 'Es más de lo necesario. Cada paso divide la longitud entre 2.' }]);
      if (!ops) return null;
      return {
        enun: 'Una raíz está en un intervalo de longitud ' + L + '. ¿Cuántas bisecciones bastan para que el intervalo final mida menos de 10 a la menos ' + tolE + '?', tex: '', ops: ops,
        pista: 'Después de n pasos la longitud es la inicial dividida entre 2 a la n.',
        pasos: [
          { tex: T`\dfrac{${L}}{2^{n}}<10^{-${tolE}}\ \Rightarrow\ 2^{n}>${L}\cdot10^{${tolE}}`, why: 'Se plantea la condición.' },
          { tex: T`n>\log_{2}(${L * Math.pow(10, tolE)})\approx${(Math.log(L * Math.pow(10, tolE)) / Math.log(2)).toFixed(2)}\ \Rightarrow\ n=${n}`, why: 'Se toma el entero siguiente.' }],
        chk: { k: 'biseccion', L: L, e: tolE }
      };
    }
  });

  /* 21. Potencia de un número complejo */
  def({
    id: 'complejo-cuad', tema: 'Cuadrado de un número complejo', curso: 'Matemáticas Especiales', lec: ['esp-complejos'],
    gen: function (r) {
      var a = r.ri(1, 6), b = r.sign() * r.ri(1, 6);
      function c(re, im) { return { tex: sumC(re, im), v: re + '+(' + im + ')*I' }; }
      function sumC(re, im) { var s = re === 0 ? '' : String(re); if (im !== 0) { var ai = Math.abs(im); s += (s === '' ? (im < 0 ? '-' : '') : (im < 0 ? '-' : '+')) + (ai === 1 ? '' : ai) + 'i'; } return s || '0'; }
      var ok = c(a * a - b * b, 2 * a * b);
      var ops = armar(r, ok, [
        Object.assign(c(a * a + b * b, 0), { e: 'Olvidó que i al cuadrado vale menos uno y que aparece el término cruzado.' }),
        Object.assign(c(a * a + b * b, 2 * a * b), { e: 'Tomó i al cuadrado como más uno. Vale menos uno.' }),
        Object.assign(c(a * a - b * b, a * b), { e: 'Olvidó el factor 2 del doble producto en la parte imaginaria.' }),
        Object.assign(c(a * a, b * b), { e: 'Elevó cada parte por separado. El cuadrado de una suma incluye el doble producto.' })]);
      if (!ops) return null;
      return {
        enun: 'Calcula el cuadrado del número complejo.', tex: '(' + sumC(a, b) + ')^{2}', ops: ops,
        pista: 'Desarrolla el cuadrado del binomio y recuerda que i al cuadrado vale menos uno.',
        pasos: [
          { tex: T`(${sumC(a, b)})^{2}=${a * a}+${2 * a * b < 0 ? '(' + 2 * a * b + ')' : 2 * a * b}i+${b * b}i^{2}`, why: 'Se desarrolla el cuadrado del binomio.' },
          { tex: T`=${ok.tex}`, why: 'Con i al cuadrado igual a menos uno.' }],
        chk: { k: 'expand', f: '(' + a + '+(' + b + ')*I)**2' }
      };
    }
  });

  /* 22. Inclusión y exclusión */
  def({
    id: 'inclusion', tema: 'Unión de dos conjuntos', curso: 'Fundamentos de Matemáticas', lec: ['fund-conjuntos', 'disc-inclusion'],
    gen: function (r) {
      var A = r.ri(20, 60), B = r.ri(20, 60), I = r.ri(3, 15);
      var ok = A + B - I;
      var ops = armar(r, { tex: String(ok), v: ok }, [
        { tex: String(A + B), v: A + B, e: 'Sumó los dos conjuntos y contó dos veces los elementos que están en ambos.' },
        { tex: String(A + B + I), v: A + B + I, e: 'Sumó la intersección en lugar de restarla.' },
        { tex: String(A + B - 2 * I), v: A + B - 2 * I, e: 'Restó la intersección dos veces. Basta restarla una vez.' },
        { tex: String(Math.max(A, B)), v: Math.max(A, B), e: 'Tomó solo el conjunto más grande, y se pierden los elementos que solo están en el otro.' }]);
      if (!ops) return null;
      return {
        enun: 'En un grupo, ' + A + ' personas estudian cálculo, ' + B + ' estudian álgebra y ' + I + ' estudian las dos. ¿Cuántas personas estudian al menos una de las dos materias?', tex: '', ops: ops,
        pista: 'Las personas que estudian las dos materias quedan contadas dos veces al sumar.',
        pasos: [{ tex: T`|A\cup B|=|A|+|B|-|A\cap B|`, why: 'Es el principio de inclusión y exclusión para dos conjuntos.' },
          { tex: T`=${A}+${B}-${I}=${ok}`, why: 'Se sustituyen los datos.' }],
        chk: { k: 'incl', A: A, B: B, I: I }
      };
    }
  });

  /* ---------- API ---------- */
  function crear(idx, seed) {
    var t = PL[idx];
    for (var intento = 0; intento < 40; intento++) {
      var r = RNG(seed * 7919 + intento * 104729 + idx);
      var p = t.gen(r);
      if (p) { p.plantilla = t.id; p.tema = t.tema; p.curso = t.curso; p.lec = t.lec; p.seed = seed; return p; }
    }
    throw new Error('No se pudo generar ' + t.id + ' con semilla ' + seed);
  }
  root.MUPractica = {
    plantillas: PL.map(function (t) { return { id: t.id, tema: t.tema, curso: t.curso, lec: t.lec }; }),
    crear: crear,
    porId: function (id, seed) { for (var i = 0; i < PL.length; i++) if (PL[i].id === id) return crear(i, seed); throw new Error('plantilla ' + id); }
  };
  if (typeof module !== 'undefined') module.exports = root.MUPractica;
})(typeof window !== 'undefined' ? window : globalThis);
