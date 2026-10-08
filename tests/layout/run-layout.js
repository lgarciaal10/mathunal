#!/usr/bin/env node
/*
 * Análisis de maquetación de MathUNAL a 360 / 768 / 1280 px.
 * Recorre todas las rutas del router y detecta, con medición real en el navegador:
 *   - desborde horizontal (página o elementos fuera del viewport sin un contenedor que los recorte/desplace),
 *   - texto cortado por un contenedor con overflow:hidden,
 *   - elementos interactivos que se solapan entre sí (y botones flotantes que tapan a otros),
 *   - botones/controles muy pequeños (< 32 px) en pantallas ≤ 768 px.
 * Guarda una captura con los elementos problemáticos resaltados en rojo en tests/capturas/
 * y un resumen en tests/capturas/reporte.json y tests/capturas/REPORTE.md.
 *
 * Uso:  npm run layout            (siempre sale con 0; es un informe)
 *       npm run layout:estricto   (sale con 1 si hay problemas de severidad alta)
 *       MU_ROOT=/otra/carpeta npm run layout   (analiza otra copia del sitio)
 *       node tests/layout/run-layout.js --solo=home,formulas --ancho=360
 */
const { chromium } = require('@playwright/test');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const { load } = require('../helpers/routes');

const args = Object.fromEntries(process.argv.slice(2).filter(a => a.startsWith('--')).map(a => { const [k, v] = a.replace(/^--/, '').split('='); return [k, v === undefined ? true : v]; }));
const PORT = process.env.MU_PORT || '4174';
const HOST = 'mathunal.test';
const ROOT = path.resolve(process.env.MU_ROOT || path.join(__dirname, '..', '..'));
const OUT = process.env.MU_CAPTURAS || path.join(__dirname, '..', 'capturas');
const WIDTHS = (args.ancho ? String(args.ancho).split(',').map(Number) : [360, 768, 1280]);
const SOLO = args.solo ? String(args.solo).split(',') : null;
// ES a todos los anchos; EN solo en móvil (los textos en inglés son más largos y rompen primero)
const COMBOS = (w) => (w <= 400 ? ['es', 'en'] : ['es']);

// Todo el análisis corre dentro de la página.
function analizar({ vw, vh }) {
  const out = { overflowPagina: null, desbordes: [], cortados: [], solapes: [], flotantes: [], pequenos: [] };
  const sig = (el) => {
    let s = el.tagName.toLowerCase();
    if (el.id) s += '#' + el.id;
    else if (typeof el.className === 'string' && el.className.trim()) s += '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.');
    return s;
  };
  const vis = (el) => {
    const cs = getComputedStyle(el);
    if (cs.display === 'none' || cs.visibility === 'hidden' || +cs.opacity === 0) return false;
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  };
  const txt = (el) => (el.innerText || el.value || el.getAttribute('aria-label') || '').trim().replace(/\s+/g, ' ').slice(0, 50);
  const mark = (el, tipo) => { el.setAttribute('data-mu-prob', tipo); };
  const all = Array.from(document.querySelectorAll('body *')).filter((el) => !['SCRIPT', 'STYLE', 'TEMPLATE', 'NOSCRIPT', 'LINK', 'META'].includes(el.tagName) && !(el.closest('svg') && el.tagName.toLowerCase() !== 'svg') && vis(el));

  const docW = Math.max(document.documentElement.scrollWidth, document.body.scrollWidth);
  if (docW > vw + 1) out.overflowPagina = docW;

  const clipAnc = (el) => {   // ancestro que recorta en horizontal
    for (let a = el.parentElement; a && a !== document.documentElement; a = a.parentElement) {
      const cs = getComputedStyle(a);
      if (a === document.body) return null;
      if (cs.overflowX !== 'visible') return a;
    }
    return null;
  };
  const OFFCANVAS = '#mob,#mob-backdrop,.mu-sr,.skip-link';

  // 1) desborde horizontal
  const flagged = new Set();
  for (const el of all) {
    if (el.closest(OFFCANVAS)) continue;
    const r = el.getBoundingClientRect();
    if (r.right <= vw + 1 && r.left >= -1) continue;
    const cs = getComputedStyle(el);
    if (cs.position === 'fixed' && (cs.transform !== 'none')) continue;
    // ¿lo contiene un ancestro que recorta/desplaza y que SÍ cabe en el viewport?
    let ok = false;
    for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) {
      const acs = getComputedStyle(a);
      if (acs.overflowX !== 'visible') { const ar = a.getBoundingClientRect(); if (ar.right <= vw + 1 && ar.left >= -1) { ok = true; break; } }
    }
    if (ok) continue;
    if (el.getAttribute('aria-hidden') === 'true' && cs.pointerEvents === 'none') continue; // decorativo
    flagged.add(el);
  }
  for (const el of flagged) {
    if (el.parentElement && flagged.has(el.parentElement)) continue;      // solo el ancestro más alto
    const r = el.getBoundingClientRect();
    out.desbordes.push({ el: sig(el), texto: txt(el), derecha: Math.round(r.right), izquierda: Math.round(r.left), ancho: Math.round(r.width) });
    mark(el, 'desborde');
  }

  // 2) texto cortado: elemento con texto que sobresale de un ancestro con overflow hidden/clip
  for (const el of all) {
    if (el.closest(OFFCANVAS) || el.closest('[aria-hidden="true"]') || el.closest('.hero-bg,.marquee-track,.nav-aurora,.noise-overlay,.mu-rail-sym')) continue;
    const own = Array.from(el.childNodes).some((n) => n.nodeType === 3 && n.nodeValue.trim().length >= 3);
    if (!own) continue;
    const cs = getComputedStyle(el);
    if (cs.display === 'inline') continue;
    // (a) el propio elemento recorta su texto
    if ((cs.overflowX === 'hidden' || cs.overflowX === 'clip') && el.scrollWidth > el.clientWidth + 2 && cs.textOverflow !== 'ellipsis' && el.clientWidth > 0) {
      out.cortados.push({ el: sig(el), texto: txt(el), detalle: `scrollWidth ${el.scrollWidth} > clientWidth ${el.clientWidth}` }); mark(el, 'cortado'); continue;
    }
    // (b) un ancestro con overflow hidden lo recorta
    for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) {
      const acs = getComputedStyle(a);
      if (acs.overflowX === 'hidden' || acs.overflowX === 'clip') {
        const ar = a.getBoundingClientRect(), r = el.getBoundingClientRect();
        if (r.right > ar.right + 2 || r.left < ar.left - 2) { out.cortados.push({ el: sig(el), texto: txt(el), detalle: `sobresale de ${sig(a)}` }); mark(el, 'cortado'); }
        break;
      }
    }
  }

  // 3) solapes entre controles interactivos
  const inter = all.filter((el) => el.matches('a[href],button,input:not([type=hidden]),select,textarea,[role=button],summary') && !el.closest(OFFCANVAS));
  const fixedI = inter.filter((el) => getComputedStyle(el).position === 'fixed' || el.closest('[style*="position:fixed"],nav,#mu-scrollnav,.fab-wa'));
  const rect = (el) => el.getBoundingClientRect();
  const inter2 = (a, b) => { const w = Math.min(a.right, b.right) - Math.max(a.left, b.left), h = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top); return w > 0 && h > 0 ? w * h : 0; };
  const flow = inter.filter((el) => !fixedI.includes(el));
  const seen = new Set();
  for (let i = 0; i < flow.length; i++) {
    for (let j = i + 1; j < flow.length; j++) {
      const A = flow[i], B = flow[j];
      if (A.contains(B) || B.contains(A)) continue;
      if (A.closest('label') && A.closest('label') === B.closest('label')) continue;
      const ra = rect(A), rb = rect(B), ov = inter2(ra, rb);
      if (!ov) continue;
      const min = Math.min(ra.width * ra.height, rb.width * rb.height);
      if (ov / min > 0.35) {
        const k = sig(A) + '|' + sig(B); if (seen.has(k)) continue; seen.add(k);
        out.solapes.push({ a: sig(A), ta: txt(A), b: sig(B), tb: txt(B), porcentaje: Math.round((ov / min) * 100) });
        mark(A, 'solape'); mark(B, 'solape');
      }
    }
  }
  // 3b) flotantes (position:fixed) sobre otros controles, en la posición actual del scroll
  for (const F of inter.filter((el) => getComputedStyle(el).position === 'fixed' && !el.closest('nav'))) {
    const rf = rect(F);
    for (const O of flow) {
      const ro = rect(O); if (ro.bottom < 0 || ro.top > vh) continue;
      const ov = inter2(rf, ro); if (!ov) continue;
      if (ov / Math.min(rf.width * rf.height, ro.width * ro.height) > 0.2) { out.flotantes.push({ flotante: sig(F), tapa: sig(O), texto: txt(O) }); mark(F, 'solape'); mark(O, 'solape'); }
    }
  }

  // 4) controles muy pequeños (< 32 px) — solo se listan en pantallas ≤ 768
  if (vw <= 768) {
    for (const el of inter) {
      if (el.tagName === 'A' && getComputedStyle(el).display === 'inline') continue;     // enlaces en línea de un párrafo
      if (el.type === 'range' || el.type === 'checkbox' || el.type === 'radio') continue;
      const r = rect(el);
      if (Math.min(r.width, r.height) < 32) { out.pequenos.push({ el: sig(el), texto: txt(el), tamano: `${Math.round(r.width)}x${Math.round(r.height)}` }); mark(el, 'pequeno'); }
    }
  }
  return out;
}

async function main() {
  const { routes } = load(ROOT);
  const lista = routes.filter((r) => !SOLO || SOLO.includes(r.name) || SOLO.includes(r.page));
  const server = spawn(process.execPath, [path.join(__dirname, '..', 'helpers', 'static-server.js')], { env: { ...process.env, MU_PORT: PORT, MU_ROOT: ROOT }, stdio: 'ignore' });
  await new Promise((r) => setTimeout(r, 800));
  const browser = await chromium.launch({ args: ['--no-sandbox', `--host-resolver-rules=MAP ${HOST} 127.0.0.1`], ...(process.env.PW_CHROMIUM ? { executablePath: process.env.PW_CHROMIUM } : {}) });
  fs.mkdirSync(OUT, { recursive: true });
  for (const f of fs.readdirSync(OUT)) if (/\.(png|json|md)$/.test(f)) fs.unlinkSync(path.join(OUT, f));
  const informe = [];
  try {
    for (const w of WIDTHS) {
      const movil = w <= 820;
      for (const lang of COMBOS(w)) {
        const ctx = await browser.newContext({ viewport: { width: w, height: movil ? 800 : 800 }, isMobile: movil, hasTouch: movil, deviceScaleFactor: 1, ignoreHTTPSErrors: true });
        await ctx.addInitScript((l) => { try { localStorage.setItem('mu-lang', l); localStorage.setItem('mu-theme', 'dark'); } catch (e) {} }, lang);
        await ctx.route((u) => new URL(u).host !== `${HOST}:${PORT}`, (route) => route.abort());
        for (const r of lista) {
          const page = await ctx.newPage();
          try {
            await page.goto(`http://${HOST}:${PORT}/index.html#${r.hash}`, { waitUntil: 'domcontentloaded' });
            await page.waitForFunction((p) => window.__muCurrentPage === p && document.querySelector('#mu-app nav'), r.page, { timeout: 15000 });
            await page.waitForTimeout(1500);
            await page.addStyleTag({ content: '*{scroll-behavior:auto !important}' });
            await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise((s) => setTimeout(s, 30)); } window.scrollTo(0, 0); });
            await page.waitForTimeout(500);
            const res = await page.evaluate(analizar, { vw: w, vh: 800 });
            const graves = (res.overflowPagina ? 1 : 0) + res.desbordes.length;
            const medios = res.cortados.length + res.solapes.length + res.flotantes.length;
            const item = { ruta: r.name, ancho: w, idioma: lang, ...res, graves, medios, captura: null };
            if (graves || medios) {
              const first = await page.$('[data-mu-prob="desborde"], [data-mu-prob="cortado"], [data-mu-prob="solape"]');
              await page.addStyleTag({ content: '[data-mu-prob]{outline:2px solid #ff2d2d !important;outline-offset:-2px}' });
              if (first) await first.evaluate((e) => e.scrollIntoView({ block: 'center', inline: 'nearest' }));
              await page.waitForTimeout(200);
              const nombre = `${r.name}_${w}_${lang}.png`;
              await page.screenshot({ path: path.join(OUT, nombre) });
              item.captura = `tests/capturas/${nombre}`;
            }
            informe.push(item);
            process.stdout.write(`${graves ? '✘' : medios ? '!' : '✓'} ${lang} ${String(w).padStart(4)} ${r.name.padEnd(18)} graves:${graves} medios:${medios} pequeños:${res.pequenos.length}\n`);
          } catch (e) {
            informe.push({ ruta: r.name, ancho: w, idioma: lang, error: String(e).slice(0, 200), graves: 1, medios: 0 });
            process.stdout.write(`✘ ${lang} ${w} ${r.name} ERROR ${String(e).slice(0, 100)}\n`);
          }
          await page.close();
        }
        await ctx.close();
      }
    }
  } finally { await browser.close(); server.kill(); }

  fs.writeFileSync(path.join(OUT, 'reporte.json'), JSON.stringify(informe, null, 1));
  const L = ['# Reporte de maquetación', '', `Anchos: ${WIDTHS.join(', ')} · ${informe.length} combinaciones ruta×ancho×idioma`, '',
    '| Ruta | Ancho | Idioma | Desbordes | Cortados | Solapes | Pequeños (<32px) | Captura |', '|---|---|---|---|---|---|---|---|'];
  for (const i of informe) L.push(`| ${i.ruta} | ${i.ancho} | ${i.idioma} | ${i.error ? 'ERROR' : (i.overflowPagina ? 'página ' + i.overflowPagina + 'px + ' : '') + i.desbordes.length} | ${i.cortados ? i.cortados.length : '-'} | ${i.solapes ? i.solapes.length + i.flotantes.length : '-'} | ${i.pequenos ? i.pequenos.length : '-'} | ${i.captura || ''} |`);
  fs.writeFileSync(path.join(OUT, 'REPORTE.md'), L.join('\n') + '\n');
  const g = informe.reduce((s, i) => s + (i.graves || 0), 0), m = informe.reduce((s, i) => s + (i.medios || 0), 0);
  console.log(`\nResumen: ${g} problemas graves, ${m} medios. Detalle en ${path.relative(process.cwd(), OUT)}/`);
  if (args.estricto && g) process.exit(1);
}
main().catch((e) => { console.error(e); process.exit(2); });
