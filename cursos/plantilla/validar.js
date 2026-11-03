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
const compilar = (e, donde) => { if (!/^[0-9x+\-*\/().^\s]+$/.test(e)) { err(`Fórmula no permitida en ${donde}`); return null; } try { return new Function('x', 'return ' + e.replace(/\^/g, '**')); } catch (x) { err(`Fórmula inválida en ${donde}`); return null; } };
const G = L.grafica, A = G.hueco && G.hueco.x;
const fc = compilar(G.curva, 'grafica.curva'), ff = compilar(G.funcion, 'grafica.funcion');
if (fc && ff) {
  for (const x of [A - 1, A - 0.37, A + 0.37, A + 1.5]) if (Math.abs(fc(x) - ff(x)) > 1e-9) err(`La curva y la función no coinciden en x=${x}`);
  if (Math.abs(fc(A) - G.hueco.y) > 1e-9) err(`La curva en x=${A} vale ${fc(A)} y el hueco dice ${G.hueco.y}`);
  if (G.hueco.y !== G.limite) err(`El hueco (${G.hueco.y}) y el límite (${G.limite}) deberían coincidir en este tipo de gráfica`);
  let prev = Infinity;
  for (const d of [1, 1e-1, 1e-2, 1e-3, 1e-4]) {
    const e = Math.max(Math.abs(ff(A - d) - G.limite), Math.abs(ff(A + d) - G.limite));
    if (e > prev + 1e-12) err('Los valores no se acercan al límite de forma decreciente'); prev = e;
  }
  if (prev > 1e-3) err('f(a±1e-4) no está cerca del límite');
}
const rangos = G.x && G.y && G.x.length === 2 && G.y.length === 2;
if (!rangos) err('grafica.x y grafica.y deben tener dos números');
else if (!(A > G.x[0] && A < G.x[1] && G.hueco.y > G.y[0] && G.hueco.y < G.y[1])) err('El hueco queda fuera del rango de la gráfica');

/* ---------- pregunta ---------- */
const Q = L.pregunta;
if (!Array.isArray(Q.opciones) || Q.opciones.length < 2) err('pregunta.opciones necesita al menos 2');
else if (!(Number.isInteger(Q.correcta) && Q.correcta >= 0 && Q.correcta < Q.opciones.length)) err('pregunta.correcta fuera de rango');
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
const TIPOS = ['p', 'nota', 'eq', 'pregunta', 'resumen', 'grafica', 'acercando', 'piensa', 'pasos', 'ojo'];
const tex = [], textos = [];
const glosa = new Set(Object.keys(L.glosario));
function bloque(b, donde) {
  if (!TIPOS.includes(b.t)) { err(`Bloque desconocido ${b.t} en ${donde}`); return; }
  if (b.html) { textos.push([donde, b.html]); for (const m of b.html.matchAll(/\{\{gl:([a-z0-9_]+)\|/g)) if (!glosa.has(m[1])) err(`Término ${m[1]} no está en el glosario (${donde})`); }
  if (b.t === 'eq') tex.push([donde, b.tex]);
  if (b.t === 'pasos') b.items.forEach((s, i) => { tex.push([`${donde} paso ${i + 1}`, s.tex]); textos.push([`${donde} paso ${i + 1}`, s.porque]); });
  if (b.t === 'piensa') { textos.push([donde, b.pregunta + ' ' + b.bien + ' ' + b.mal]); if (!b.opciones.includes(b.correcta)) err(`La opción correcta de piensa no está en sus opciones (${donde})`); if (b.correcta !== G.limite) aviso(`piensa.correcta (${b.correcta}) no coincide con el límite de la gráfica (${G.limite}) en ${donde}`); }
  if (b.alt) textos.push([donde + ' alt', b.alt]);
}
(L.leer.secciones || []).forEach((s, i) => { textos.push([`leer ${i + 1} título`, s.titulo]); (s.bloques || []).forEach(b => bloque(b, `leer ${i + 1}`)); });
(L.practicar.pasos || []).forEach((s, i) => { textos.push([`practicar ${i + 1} título`, s.titulo]); (s.bloques || []).forEach(b => bloque(b, `practicar ${i + 1}`)); if (!s.grafica) err(`practicar ${i + 1} sin estado de gráfica`); });
tex.push(['pregunta', Q.tex]);
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
