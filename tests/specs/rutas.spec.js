// Recorre TODAS las rutas del router × 2 idiomas × 4 temas y comprueba que cada página:
//  - renderiza (el <main id="mu-app"> se llena y el router reporta la página correcta),
//  - respeta el idioma (<html lang>) y el tema (data-theme) pedidos,
//  - no lanza excepciones JS ni escribe errores en la consola,
//  - no tiene recursos locales rotos (HTTP >= 400, peticiones fallidas o <img> que no cargan).
// Las peticiones a dominios externos (analítica, fuentes, KaTeX, Supabase, Wompi…) se cortan para que la
// prueba sea determinista y offline; sus errores de red se ignoran (ver IGNORAR_EXTERNOS).
const { test, expect } = require('@playwright/test');
const { load, LANGS, THEMES } = require('../helpers/routes');

const { routes } = load();
const HOST = new URL(process.env.MU_BASE || `http://mathunal.test:${process.env.MU_PORT || '4173'}`).host;
const esLocal = (url) => { try { return new URL(url).host === HOST; } catch (e) { return false; } };

for (const lang of LANGS) {
  for (const theme of THEMES) {
    test.describe(`${lang} · ${theme}`, () => {
      for (const r of routes) {
        test(`${r.name}`, async ({ page }) => {
          const consola = [], excepciones = [], rotos = [];
          await page.addInitScript(([l, t]) => {
            try { localStorage.setItem('mu-lang', l); localStorage.setItem('mu-theme', t); } catch (e) {}
          }, [lang, theme]);
          // Corta todo lo que no sea el sitio local (determinista, sin red).
          await page.route((u) => !esLocal(u.toString()), (route) => route.abort());
          page.on('pageerror', (e) => excepciones.push(e.message));
          page.on('console', (m) => {
            if (m.type() !== 'error') return;
            const loc = m.location() && m.location().url;
            if (loc && !esLocal(loc)) return;                    // IGNORAR_EXTERNOS: fallo de red de un recurso externo cortado
            if (/Failed to load resource/.test(m.text()) && !loc) return;
            consola.push(m.text().slice(0, 200));
          });
          page.on('response', (resp) => { if (esLocal(resp.url()) && resp.status() >= 400) rotos.push(`${resp.status()} ${resp.url()}`); });
          page.on('requestfailed', (req) => { if (esLocal(req.url())) rotos.push(`FALLÓ ${req.url()}`); });

          await page.goto(`/index.html#${r.hash}`, { waitUntil: 'domcontentloaded' });
          await page.waitForFunction((p) => window.__muCurrentPage === p && document.querySelector('#mu-app nav'), r.page, { timeout: 15000 });
          await page.waitForTimeout(1200);                          // deja correr setLang/render diferido
          // baja y sube para disparar contenido perezoso (loading="lazy", .fi)
          await page.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 800) { window.scrollTo(0, y); await new Promise((s) => setTimeout(s, 40)); } window.scrollTo(0, 0); });
          await page.waitForTimeout(400);

          const estado = await page.evaluate(() => ({
            texto: (document.getElementById('mu-app') || {}).innerText || '',
            pagina: window.__muCurrentPage,
            lang: document.documentElement.lang,
            tema: document.documentElement.getAttribute('data-theme'),
            titulo: document.title,
            imgs: Array.from(document.images).filter((i) => i.complete && i.naturalWidth === 0 && i.src && !/^data:/.test(i.src) && i.currentSrc).map((i) => i.currentSrc),
          }));

          expect.soft(estado.pagina, 'ruta activa').toBe(r.page);
          expect.soft(estado.texto.trim().length, 'contenido renderizado').toBeGreaterThan(150);
          expect.soft(estado.lang, 'idioma de <html>').toBe(lang);
          expect.soft(estado.tema, 'tema').toBe(theme);
          expect.soft(estado.titulo.length, 'título de la pestaña').toBeGreaterThan(5);
          const imgsLocales = estado.imgs.filter(esLocal);
          expect.soft(imgsLocales, 'imágenes locales rotas').toEqual([]);
          expect.soft(rotos, 'recursos locales rotos').toEqual([]);
          expect.soft(excepciones, 'excepciones JS').toEqual([]);
          expect.soft(consola, 'errores de consola').toEqual([]);
        });
      }
    });
  }
}

// 404.html (la sirve GitHub Pages para rutas inexistentes)
test('404.html renderiza', async ({ page }) => {
  const excepciones = [];
  await page.route((u) => !esLocal(u.toString()), (route) => route.abort());
  page.on('pageerror', (e) => excepciones.push(e.message));
  const resp = await page.goto('/ruta-que-no-existe');
  expect(resp.status()).toBe(404);
  await expect(page.locator('h1')).toBeVisible();
  expect(excepciones).toEqual([]);
});
