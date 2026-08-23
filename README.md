# MathUNAL — App (PWA)

App de una sola página, instalable y con soporte offline. Sin framework, sin build step: `index.html` es HTML+CSS+JS inline (SPA con router por hash y `<template>`).

## Archivos
- `index.html` — la app completa (routing por hash, templates lazy-loaded, i18n manual ES/EN)
- `manifest.json` — metadatos PWA (nombre, íconos, color)
- `sw.js` — service worker (caché offline de la app + KaTeX). **Sube el número de `CACHE` en cada release** o los usuarios seguirán viendo la versión vieja cacheada.
- `icon-*.png`, `favicon.png` — íconos
- `*-parciales/` — material digitalizado (PDFs) organizado por materia
- `supabase/` — config local de la CLI de Supabase (no se despliega, solo referencia para el proyecto vinculado)

## Producción
Publicado en **https://mathunal.com** vía GitHub Pages (repo `lgarciaal10/mathunal`, branch `main`, dominio propio con `CNAME`, HTTPS activo). Cualquier push a `main` se despliega automáticamente.

## Backend (Supabase — ya integrado, no requiere setup)
El frontend habla directo con la REST API de Supabase usando la key `anon` (pública por diseño, protegida por RLS):
- **`materiales`** — catálogo de PDFs (complementa al objeto `MATS` hardcodeado en `index.html`).
- **`explicaciones`** — explicaciones de IA pre-generadas por pregunta de examen. Solo lectura pública.
- **`aportes`** — material que suben los usuarios (moderado: solo visible tras `estado='aprobado'`).
- **`stats`**, **`premium_usuarios`**, **`parciales_reportados`** — contador de visitas, gate de acceso premium, reportes de fecha de parcial.
- Bucket `Materiales` — público de solo lectura, sin políticas de escritura desde el navegador.

Todas las escrituras sensibles (aprobar aportes, activar premium) pasan por Edge Functions con `service_role`, nunca directo desde el navegador.

## Pagos (Wompi)
El desbloqueo de soluciones (modal "Unlock solutions") usa el widget real de Wompi con key de **producción** (`pub_prod_...`) — tarjeta, PSE, Nequi. El "Pack Salva-Semestre" de la sección de aportes usa un flujo distinto: WhatsApp con pago manual. Son dos productos/rutas de compra separadas, no un fallback.

## Funciona YA
- ✅ Navegación entre Home / Simulacros / Materia / Formulario / Banco de Exámenes / Juegos / Diagnóstico
- ✅ Simulacros con LaTeX, retroalimentación y explicaciones (locales o vía Supabase)
- ✅ Guarda resultados y progreso (localStorage) — puedes reanudar exámenes
- ✅ Calculadora de notas, promedio ponderado, plan semanal del parcial
- ✅ Offline: una vez cargada, funciona sin internet
- ✅ Instalable como app en celular/escritorio
- ✅ Español/Inglés, tres temas (oscuro/gris/claro)

## Nota sobre seguridad del Premium
El desbloqueo actual verifica el correo contra `premium_usuarios` en Supabase (RLS cerrado, sin políticas de acceso público — solo se consulta vía función server-side). El pago en sí sigue siendo manual por WhatsApp.
