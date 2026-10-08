# Pruebas automáticas de MathUNAL

Solo para desarrollo: el sitio en producción **no usa nada de esto** (Playwright es una `devDependency`).

## Requisitos
- Node 18+ y un Chromium que Playwright pueda usar.
- `npm install` en la raíz del repo (instala `@playwright/test`).
- Si no tienes los navegadores de Playwright: `npx playwright install chromium`.
  En entornos donde ya hay un Chromium instalado, apunta a él con `PW_CHROMIUM=/ruta/a/chrome`.

## Pruebas de rutas — `npm test`
Sirve el repo en local (`tests/helpers/static-server.js`, sin dependencias) y recorre **todas las rutas del router**
(se leen de `index.html`: `KNOWN` + los códigos de `SUBJECTS`, 19 rutas) × **ES/EN** × **4 temas** (152 pruebas + 404.html).
Cada una verifica que la página:
- renderiza (contenido en `#mu-app` y el router reporta la página correcta),
- respeta el idioma (`<html lang>`) y el tema (`data-theme`),
- no lanza excepciones JS ni escribe errores en la consola,
- no tiene recursos locales rotos (HTTP ≥ 400, peticiones fallidas, `<img>` que no cargan).

```bash
npm test                 # todo (≈ 2 min con 4 workers)
npm run test:rapido      # solo tema "dark" (ES y EN)
npx playwright test --grep "en · light.*formulas"   # una combinación
MU_WORKERS=2 npm test    # menos paralelismo
MU_ROOT=/ruta/a/otra/copia npm test   # probar otra copia/rama del sitio
```

Notas:
- El host de prueba es `mathunal.test` (resuelto a 127.0.0.1) para que el sitio **no** active su modo local
  (`__SIM_LOCAL`, panel dev, `*.dev.js`) y se comporte como en producción.
- Las peticiones a dominios externos (Google Analytics, Plausible, fuentes, KaTeX, Supabase, Wompi…) se cortan:
  la prueba es offline y determinista, y sus errores de red se ignoran. **Esto significa que no se prueba el
  contenido que depende de esos servicios** (fórmulas renderizadas con KaTeX, datos de Supabase, pagos).
- Para comprobar que la prueba detecta fallos: añade un `<img src="no-existe.png">` o un `throw` a una copia del
  sitio y corre con `MU_ROOT=` apuntando a ella.

## Análisis de maquetación — `npm run layout`
Visita cada ruta a **360, 768 y 1280 px** (ES; y EN también a 360 px) y mide, dentro del navegador:
- **Desbordes horizontales** (la página o un elemento sale del viewport sin un contenedor que lo recorte o desplace),
- **texto cortado** por un contenedor con `overflow:hidden`,
- **solapes** entre controles interactivos (y botones flotantes que tapan a otros),
- **controles muy pequeños** (< 32 px) en pantallas ≤ 768 px.

Guarda en `tests/capturas/`: una captura por cada ruta/ancho con problemas (los elementos problemáticos
resaltados en rojo), `reporte.json` y `REPORTE.md`. Siempre sale con código 0 (es un informe);
`npm run layout:estricto` sale con 1 si hay problemas graves (desbordes). Opciones:
`node tests/layout/run-layout.js --solo=home,formulas --ancho=360`.

Los resultados son heurísticos: un "solape" o "texto cortado" puede ser intencional. Revísalos con la captura.
