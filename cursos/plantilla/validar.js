#!/usr/bin/env node
/* Validador de lecciones MathUNAL.
   Uso  node validar.js ../lecciones/calculo-limite-1.json [--katex ruta/katex.min.js]
   Revisa el esquema, que cada ecuación renderice con KaTeX, que los números de la gráfica
   y de la pregunta cuadren (con cálculo numérico) y que los textos cumplan las reglas de escritura.
   Sale con código 1 si encuentra errores. Las advertencias no detienen. */
const fs = require('fs');
const args = process.argv.slice(2);
if (!args[0]) { console.log('Uso  node validar.js leccion.json [--katex ruta/katex.min.js]'); process.exit(1); }
const kIdx = args.indexOf('--katex');
let katex;
try { katex = require(kIdx >= 0 ? require('path').resolve(args[kIdx + 1]) : 'katex'); }
catch (e) { console.error('No se pudo cargar KaTeX. Pasa la ruta con --katex'); process.exit(2); }
let L;
try { L = JSON.parse(fs.readFileSync(args[0], 'utf8')); } catch (e) { console.error('JSON inválido ' + e.message); process.exit(1); }

const errores = [], avisos = [];
const err = (m) => errores.push(m), aviso = (m) => avisos.push(m);
const falta = (o, k, tipo, ruta) => { if (o == null || o[k] === undefined) { err(`Falta ${ruta}${k}`); return false; } if (tipo && typeof o[k] !== tipo && !(tipo === 'array' && Array.isArray(o[k]))) { err(`${ruta}${k} debe ser ${tipo}`); return false; } return true; };

/* ---------- esquema ---------- */
if (L.esquema !== 1) err('esquema debe ser 1');
['id', 'curso', 'modulo', 'posicion', 'titulo'].forEach(k => falta(L, k, 'string', ''));
['minutos', 'ejercicios'].forEach(k => falta(L, k, 'number', ''));
['grafica', 'glosario', 'ver', 'leer', 'practicar', 'pregunta'].forEach(k => falta(L, k, 'object', ''));
if (!Array.isArray(L.resumen)) err('Falta resumen');
if (errores.length) { salir(); }

/* ---------- fórmulas ---------- */
const FN = /\b(sin|cos|tan|exp|ln|sqrt|abs|pi)\b/g;
const compilar = (e, donde) => { if (!/^[0-9x+\-*\/().^\s]*$/.test(String(e).replace(FN, ''))) { err(`Fórmula no permitida en ${donde}`); return null; } try { const js = String(e).replace(/\^/g, '**').replace(/\bln\b/g, 'log').replace(/\bpi\b/g, 'PI').replace(/\b(sin|cos|tan|exp|log|sqrt|abs|PI)\b/g, 'Math.$1'); return new Function('x', 'return ' + js); } catch (x) { err(`Fórmula inválida en ${donde}`); return null; } };
const G = L.grafica, SEC = G.tipo === 'secante', TVM = G.tipo === 'tvm', A = (SEC || TVM) ? G.a : (G.hueco && G.hueco.x);
if (G.tipo && !['hueco', 'secante', 'tvm', 'newton', 'area', 'entre', 'asintota'].includes(G.tipo)) err(`Tipo de gráfica desconocido ${G.tipo}`);
if (SEC) {
  const f = compilar(G.funcion, 'grafica.funcion'), fd = compilar(G.derivada, 'grafica.derivada');
  if (f && fd) {
    if (Math.abs(fd(A) - G.limite) > 1e-9) err(`La derivada en x=${A} vale ${fd(A)} y el límite dice ${G.limite}`);
    let prev = Infinity;
    for (const h of [1, 0.5, 0.1, 0.01, 1e-3, 1e-4]) { const e = Math.abs((f(A + h) - f(A)) / h - G.limite); if (e > prev + 1e-12) err('Las pendientes de la secante no se acercan de forma decreciente'); prev = e; }
    if (prev > 1e-3) err('La pendiente de la secante con h=1e-4 no está cerca de la derivada');
    if (!(A > G.x[0] && A < G.x[1])) err('El punto queda fuera del rango x'); else if (!(f(A) > G.y[0] && f(A) < G.y[1])) err('El punto queda fuera del rango y');
    if (!(f(A + 1) >= G.y[0] && f(A + 1) <= G.y[1] && A + 1 <= G.x[1])) aviso('Con h=1 el segundo punto sale del rango de la gráfica');
  }
} else if (TVM) {
  const f = compilar(G.funcion, 'grafica.funcion'), fd = compilar(G.derivada, 'grafica.derivada');
  if (!(G.a < G.b)) err('En el teorema del valor medio a debe ser menor que b');
  if (f && fd && G.a < G.b) {
    const cuerda = (f(G.b) - f(G.a)) / (G.b - G.a);
    if (Math.abs(cuerda - G.limite) > 1e-9) err(`La pendiente de la cuerda vale ${cuerda} y limite dice ${G.limite}`);
    if (typeof G.c !== 'number' || !(G.c > G.a && G.c < G.b)) err('grafica.c debe estar entre a y b');
    else if (Math.abs(fd(G.c) - cuerda) > 1e-6) err(`La derivada en c=${G.c} vale ${fd(G.c)} y la cuerda ${cuerda}`);
    for (const x of [G.a, G.b]) if (!(f(x) > G.y[0] && f(x) < G.y[1])) err('Un extremo queda fuera del rango y');
    if (!(G.x[0] < G.a && G.b < G.x[1])) err('Los extremos deben quedar dentro del rango x');
  }
} else if (G.tipo === 'newton') {
  const f = compilar(G.funcion, 'grafica.funcion'), fd = compilar(G.derivada, 'grafica.derivada');
  if (f && fd) {
    let x = G.x0; const xs = [x];
    for (let i = 0; i < G.pasos; i++) { const d = fd(x); if (Math.abs(d) < 1e-12) { err(`La derivada vale 0 en la iteración ${i}`); break; } x = x - f(x) / d; xs.push(x); }
    if (Math.abs(xs[xs.length - 1] - G.raiz) > 1e-6) err(`Después de ${G.pasos} pasos Newton llega a ${xs[xs.length - 1]} y raiz dice ${G.raiz}`);
    if (Math.abs(f(G.raiz)) > 1e-6) err('f(raiz) no es 0');
    xs.forEach((q, i) => { if (!(q > G.x[0] && q < G.x[1])) aviso(`x${i}=${q} queda fuera del rango x`); if (!(f(q) > G.y[0] && f(q) < G.y[1])) aviso(`f(x${i}) queda fuera del rango y`); });
  }
} else if (G.tipo === 'area') {
  const f = compilar(G.funcion, 'grafica.funcion'), F = compilar(G.primitiva, 'grafica.primitiva');
  if (!(G.a < G.b)) err('En la gráfica de área a debe ser menor que b');
  if (f && F && G.a < G.b) {
    for (const x of [G.a + 0.1, (G.a + G.b) / 2, G.b - 0.1]) { const h = 1e-5, num = (F(x + h) - F(x - h)) / (2 * h); if (Math.abs(num - f(x)) > 1e-4) err(`La derivada de la primitiva en x=${x} da ${num} y f vale ${f(x)}`); }
    if (!(f(G.b) < G.y[1] && f(G.b) > G.y[0])) err('f(b) queda fuera del rango y');
    if (!(G.b < G.x[1])) err('b debe quedar dentro del rango x');
  }
} else if (G.tipo === 'entre') {
  const f = compilar(G.funcion, 'grafica.funcion'), g = compilar(G.inferior, 'grafica.inferior'), F = compilar(G.primitiva, 'grafica.primitiva');
  if (!(G.a < G.b)) err('En la gráfica entre curvas a debe ser menor que b');
  if (f && g && F && G.a < G.b) {
    if (Math.abs(f(G.a) - g(G.a)) > 1e-6) err(`Las curvas no se cortan en a=${G.a}, f vale ${f(G.a)} y la inferior vale ${g(G.a)}`);
    for (let i = 1; i < 20; i++) { const x = G.a + (G.b - G.a) * i / 20; if (!(f(x) >= g(x) - 1e-9)) err(`La función de arriba queda por debajo de la inferior en x=${x}`); }
    for (const x of [G.a + 0.1 * (G.b - G.a), (G.a + G.b) / 2, G.b - 0.1 * (G.b - G.a)]) { const h = 1e-5, num = (F(x + h) - F(x - h)) / (2 * h); if (Math.abs(num - (f(x) - g(x))) > 1e-4) err(`La derivada de la primitiva en x=${x} da ${num} y f menos la inferior vale ${f(x) - g(x)}`); }
    for (const x of [G.a, (G.a + G.b) / 2, G.b]) for (const v of [f(x), g(x)]) if (!(v > G.y[0] && v < G.y[1])) err(`La curva en x=${x} sale del rango y (${v})`);
    if (!(G.b < G.x[1])) err('b debe quedar dentro del rango x');
  }
} else if (G.tipo === 'asintota') {
  const f = compilar(G.funcion, 'grafica.funcion');
  if (!G.deslizador || !(G.deslizador.dmin > 0 && G.deslizador.dmax > G.deslizador.dmin)) err('Falta grafica.deslizador con ancla, dmin y dmax');
  if (f) (G.asintotas || []).forEach(a => {
    if (a.y != null) { const big = f(1e6); if (Math.abs(big - a.y) > 1e-3) err(`f(1e6) vale ${big} y la asíntota horizontal dice ${a.y}`); if (a.etiqueta && /[:;—–]/.test(a.etiqueta)) err('Signo no permitido en la etiqueta de la asíntota'); }
    else if (a.x != null) { if (Math.abs(f(a.x + 1e-6)) < 1e3 || Math.abs(f(a.x - 1e-6)) < 1e3) err(`La función no se dispara cerca de x=${a.x}`); }
    else err('Cada asíntota necesita x o y');
  });
} else {
const fc = compilar(G.curva, 'grafica.curva'), ff = compilar(G.funcion, 'grafica.funcion');
if (fc && ff) {
  for (const x of [A - 1, A - 0.37, A + 0.37, A + 1.5]) if (Math.abs(fc(x) - ff(x)) > 1e-9) err(`La curva y la función no coinciden en x=${x}`);
  { let ca = fc(A); if (!isFinite(ca)) ca = fc(A + 1e-9); if (Math.abs(ca - G.hueco.y) > 1e-6) err(`La curva en x=${A} vale ${ca} y el hueco dice ${G.hueco.y}`); }
  if (G.hueco.y !== G.limite) err(`El hueco (${G.hueco.y}) y el límite (${G.limite}) deberían coincidir en este tipo de gráfica`);
  let prev = Infinity;
  for (const d of [1, 1e-1, 1e-2, 1e-3, 1e-4]) {
    const e = Math.max(Math.abs(ff(A - d) - G.limite), Math.abs(ff(A + d) - G.limite));
    if (e > prev + 1e-12) err('Los valores no se acercan al límite de forma decreciente'); prev = e;
  }
  if (prev > 1e-3) err('f(a±1e-4) no está cerca del límite');
}
if (G.normal && SEC) { const fd0 = compilar(G.derivada, 'grafica.derivada'); if (fd0 && Math.abs(fd0(A)) < 1e-9) err('Con normal la derivada no puede valer 0 en el punto'); if (G.x && G.y && Math.abs((G.x[1]-G.x[0])/550 - (G.y[1]-G.y[0])/300) > 0.002) aviso('Para que la normal se vea perpendicular, los rangos x e y deben dar la misma escala (550 por 300 píxeles)'); }
if (G.zoom && !(typeof G.zoom.factor === 'number' && G.zoom.factor > 1 && G.zoom.factor <= 100000)) err('grafica.zoom.factor debe ser un número entre 1 y 100000');
if (G.rotulos && (!Array.isArray(G.rotulos) || G.rotulos.length !== 2 || G.rotulos.some(t => /[:;—–]/.test(t)))) err('grafica.rotulos debe tener dos textos sin signos no permitidos');
if (G.punto) { if (G.punto.x !== A) err('grafica.punto.x debe ser igual al x del hueco'); if (!(G.y && G.punto.y > G.y[0] && G.punto.y < G.y[1])) err('grafica.punto queda fuera del rango y'); if (G.punto.y === G.limite) aviso('grafica.punto ya vale el límite, la función sería continua'); [G.punto.etiqueta, G.punto.etiquetaFija].forEach(t => { if (t && /[:;—–]/.test(t)) err('Signo no permitido en la etiqueta del punto'); }); }
const rangos = G.x && G.y && G.x.length === 2 && G.y.length === 2;
if (!rangos) err('grafica.x y grafica.y deben tener dos números');
else if (!(A > G.x[0] && A < G.x[1] && G.hueco.y > G.y[0] && G.hueco.y < G.y[1])) err('El hueco queda fuera del rango de la gráfica');
}

/* ---------- pregunta ---------- */
const Q = L.pregunta;
if (!Array.isArray(Q.opciones) || Q.opciones.length < 2) err('pregunta.opciones necesita al menos 2');
else if (!(Number.isInteger(Q.correcta) && Q.correcta >= 0 && Q.correcta < Q.opciones.length)) err('pregunta.correcta fuera de rango');
if (Array.isArray(Q.opciones)) Q.opciones.forEach((o, i) => { if (/\\[a-zA-Z]/.test(String(o)) && !String(o).includes('$')) err(`pregunta.opciones[${i}] lleva TeX sin signos de dólar y se vería como código`); });
if (Q.verificacion) {
  const f = compilar(Q.verificacion.formula, 'pregunta.verificacion.formula');
  if (f) { const a = Q.verificacion.a, v1 = f(a - 1e-6), v2 = f(a + 1e-6);
    if (Math.abs(v1 - Q.verificacion.esperado) > 1e-4 || Math.abs(v2 - Q.verificacion.esperado) > 1e-4) err(`La verificación numérica da ${v1.toFixed(6)} y ${v2.toFixed(6)} y se esperaba ${Q.verificacion.esperado}`);
    const op = Number(String(Q.opciones[Q.correcta]).replace(',', '.'));
    if (!Number.isNaN(op) && Math.abs(op - Q.verificacion.esperado) > 1e-9) err(`La opción marcada correcta (${Q.opciones[Q.correcta]}) no es el valor esperado ${Q.verificacion.esperado}`);
  }
} else aviso('La pregunta no trae verificacion numérica');

/* ---------- ver ---------- */
const V = L.ver;
if (!Array.isArray(V.capitulos) || !V.capitulos.length) err('ver.capitulos vacío');
else {
  let t = 0;
  V.capitulos.forEach((c, i) => { if (c[0] !== t) err(`Capítulo ${i + 1} empieza en ${c[0]} y debía empezar en ${t}`); if (!(c[1] > c[0])) err(`Capítulo ${i + 1} termina antes de empezar`); t = c[1]; });
  if (Math.abs(t - V.duracion) > 0.02) err(`Los capítulos terminan en ${t} y la duración dice ${V.duracion}`);
}
for (const [n, kf] of Object.entries(V.canales || {})) for (let i = 1; i < kf.length; i++) if (!(kf[i][0] > kf[i - 1][0])) err(`El canal ${n} no está en orden de tiempo`);

/* ---------- bloques ---------- */
const TIPOS = ['p', 'nota', 'eq', 'pregunta', 'resumen', 'grafica', 'acercando', 'piensa', 'pasos', 'ojo', 'completar', 'error', 'ordenar', 'simulacro', 'ingenieria', 'repaso'];
const tex = [], textos = [];
const glosa = new Set(Object.keys(L.glosario));
function bloque(b, donde) {
  if (!TIPOS.includes(b.t)) { err(`Bloque desconocido ${b.t} en ${donde}`); return; }
  if (b.html) { textos.push([donde, b.html]); for (const m of b.html.matchAll(/\{\{gl:([a-z0-9_]+)\|/g)) if (!glosa.has(m[1])) err(`Término ${m[1]} no está en el glosario (${donde})`); }
  if (b.t === 'eq') tex.push([donde, b.tex]);
  if (b.t === 'pasos') b.items.forEach((s, i) => { tex.push([`${donde} paso ${i + 1}`, s.tex]); textos.push([`${donde} paso ${i + 1}`, s.porque]); });
  if (b.t === 'piensa') { textos.push([donde, b.pregunta + ' ' + b.bien + ' ' + b.mal]); if (!b.opciones.includes(b.correcta)) err(`La opción correcta de piensa no está en sus opciones (${donde})`); if (b.correcta !== G.limite) aviso(`piensa.correcta (${b.correcta}) no coincide con el límite de la gráfica (${G.limite}) en ${donde}`); }
  if (b.alt) textos.push([donde + ' alt', b.alt]);
  const perm = (m, n) => Array.isArray(m) && m.length === n && new Set(m).size === n && m.every(k => Number.isInteger(k) && k >= 0 && k < n);
  if (b.t === 'completar') {
    if (typeof b.tex !== 'string' || !b.tex.includes('[[hueco]]')) err(`El bloque completar de ${donde} necesita tex con [[hueco]]`);
    else { tex.push([donde + ' completar', b.tex.replace('[[hueco]]', '\\boxed{?}')]); (b.opciones || []).forEach((o, i) => { tex.push([`${donde} completar opción ${i + 1}`, o.tex]); if (!o.txt) aviso(`Falta txt (texto para lector de pantalla) en la opción ${i + 1} de completar en ${donde}`); }); }
    if (!Array.isArray(b.opciones) || b.opciones.length < 2) err(`completar de ${donde} necesita al menos 2 opciones`);
    else if (!(Number.isInteger(b.correcta) && b.correcta >= 0 && b.correcta < b.opciones.length)) err(`completar de ${donde} tiene correcta fuera de rango`);
    else if (b.errores && b.errores.length !== b.opciones.length) err(`completar de ${donde} tiene errores con otra longitud que opciones`);
    [b.enunciado, b.porque, b.pista].concat(b.errores || []).forEach(t => { if (t) textos.push([donde + ' completar', t]); });
  }
  if (b.t === 'error') {
    if (!Array.isArray(b.pasos) || b.pasos.length < 3) err(`error de ${donde} necesita al menos 3 pasos`);
    else { b.pasos.forEach((s, i) => { tex.push([`${donde} error paso ${i + 1}`, s.tex]); if (!s.txt) aviso(`Falta txt (texto para lector de pantalla) en el paso ${i + 1} de error en ${donde}`); if (s.porque) textos.push([`${donde} error paso ${i + 1}`, s.porque]); }); if (!(Number.isInteger(b.mal) && b.mal >= 0 && b.mal < b.pasos.length)) err(`error de ${donde} tiene mal fuera de rango`); }
    tex.push([donde + ' error corrección', b.correccion]);
    [b.enunciado, b.explicacion, b.pista].forEach(t => { if (t) textos.push([donde + ' error', t]); });
  }
  if (b.t === 'ordenar') {
    if (!Array.isArray(b.pasos) || b.pasos.length < 3) err(`ordenar de ${donde} necesita al menos 3 pasos`);
    else { if (!Array.isArray(b.txt) || b.txt.length !== b.pasos.length) aviso(`Falta txt (un texto por paso para lector de pantalla) en ordenar de ${donde}`); b.pasos.forEach((s, i) => tex.push([`${donde} ordenar paso ${i + 1}`, s])); if (!perm(b.mezcla, b.pasos.length)) err(`mezcla de ${donde} debe ser una permutación de 0 a ${b.pasos.length - 1}`); else if (b.mezcla.every((k, i) => k === i)) err(`mezcla de ${donde} no puede dejar los pasos ya en orden`); }
    [b.enunciado, b.porque, b.pista].forEach(t => { if (t) textos.push([donde + ' ordenar', t]); });
  }
  if (b.t === 'simulacro') {
    if (!Array.isArray(b.preguntas) || b.preguntas.length < 2) err(`simulacro de ${donde} necesita al menos 2 preguntas`);
    else b.preguntas.forEach((q, i) => {
      const w = `${donde} simulacro ${i + 1}`;
      if (!q.fuente) err(`${w} necesita fuente`);
      [q.texto, q.resumen].concat(q.opciones || []).forEach(t => { if (typeof t === 'string') t.split('$').forEach((seg, k) => { if (k % 2 === 1) tex.push([w, seg]); }); });
      if (q.tipo === 'numerica') { if (Number.isNaN(parseFloat(q.respuesta))) err(`${w} numérica sin respuesta numérica`); }
      else if (!(Array.isArray(q.opciones) && q.opciones.length >= 2 && Number.isInteger(q.correcta) && q.correcta >= 0 && q.correcta < q.opciones.length)) err(`${w} tiene opciones o correcta inválidas`);
    });
  }
  if (b.t === 'ingenieria') {
    if (!b.html) err(`ingenieria de ${donde} necesita html`);
    if (b.tex) tex.push([donde + ' ingenieria', b.tex]);
    [b.titulo, b.html, b.cierre].forEach(t => { if (t) textos.push([donde + ' ingenieria', t]); });
    (b.datos || []).forEach(d => { textos.push([donde + ' ingenieria dato', d.k]); });
  }
}
(L.leer.secciones || []).forEach((s, i) => { textos.push([`leer ${i + 1} título`, s.titulo]); (s.bloques || []).forEach(b => bloque(b, `leer ${i + 1}`)); });
(L.practicar.pasos || []).forEach((s, i) => { textos.push([`practicar ${i + 1} título`, s.titulo]); (s.bloques || []).forEach(b => bloque(b, `practicar ${i + 1}`)); if (!s.grafica) err(`practicar ${i + 1} sin estado de gráfica`); });
tex.push(['pregunta', Q.tex]);
if (Q.errores) { if (!Array.isArray(Q.errores) || Q.errores.length !== Q.opciones.length) err('pregunta.errores debe tener un texto por opción'); else { Q.errores.forEach((t, i) => { if (i === Q.correcta) { if (t) aviso('pregunta.errores de la opción correcta debería ir vacío'); } else if (!t) aviso(`Falta explicar el error de la opción ${i + 1}`); else textos.push([`pregunta error ${i + 1}`, t]); }); } }
if (Q.pistas) { if (!Array.isArray(Q.pistas) || Q.pistas.length < 1 || Q.pistas.length > 4) err('pregunta.pistas debe tener entre 1 y 4 pistas'); else Q.pistas.forEach((t, i) => textos.push([`pregunta pista ${i + 1}`, t])); }
(V.capitulos || []).forEach((c, i) => textos.push([`ver ${i + 1}`, c[2]]));
(L.resumen || []).forEach((s, i) => textos.push([`resumen ${i + 1}`, s]));
Object.entries(L.glosario).forEach(([k, v]) => textos.push([`glosario ${k}`, v]));
textos.push(['pregunta explicación', Q.explicacion]); Q.opciones.forEach((o, i) => textos.push([`opción ${i + 1}`, String(o)]));
[['titulo', L.titulo], ['modulo', L.modulo], ['posicion', L.posicion]].forEach(x => textos.push(x));

/* ---------- KaTeX ---------- */
for (const [donde, t] of tex) { try { katex.renderToString(t, { throwOnError: true, trust: false }); } catch (e) { err(`KaTeX falla en ${donde} ${e.message.slice(0, 90)}`); } }

/* ---------- reglas de escritura (sin dos puntos, punto y coma ni guiones largos) ---------- */
for (const [donde, t] of textos) {
  const limpio = String(t).replace(/<[^>]+>/g, '').replace(/\{\{gl:[a-z0-9_]+\|([^}]+)\}\}/g, '$1');
  const m = limpio.match(/.{0,20}[:;—–].{0,20}/);
  if (m) err(`Signo no permitido en ${donde} cerca de "${m[0]}"`);
  if (/\b(garantiza(do|mos)?|aprobar[aá]s|seguro que pasas)\b/i.test(limpio) && !/no garantiza/i.test(limpio)) err(`Promesa de resultado en ${donde}`);
}

function salir() {
  console.log(`Lección ${L.id || args[0]}`);
  console.log(`Ecuaciones revisadas ${tex.length}  Textos revisados ${textos.length}`);
  avisos.forEach(a => console.log('AVISO ' + a));
  errores.forEach(e => console.log('ERROR ' + e));
  console.log(errores.length ? `Falló con ${errores.length} error(es)` : 'Todo en orden');
  process.exit(errores.length ? 1 : 0);
}
salir();
