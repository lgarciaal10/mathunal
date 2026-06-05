# MathUNAL — App (PWA)

App de una sola página, instalable y con soporte offline.

## Archivos
- `index.html` — la app completa (SPA con router por hash)
- `manifest.json` — metadatos PWA (nombre, íconos, color)
- `sw.js` — service worker (caché offline de la app + KaTeX)
- `icon-*.png`, `favicon.png` — íconos
- `integraciones/` — código listo para conectar backend y pagos (requiere TUS cuentas)

## Cómo publicar (GitHub Pages, gratis)
1. Crea un repo y sube TODO el contenido de esta carpeta a la raíz.
2. Settings → Pages → Branch: `main` / root → Save.
3. Listo: `https://TU-USUARIO.github.io/TU-REPO/`
   - El service worker y el manifest necesitan HTTPS — GitHub Pages ya lo da.
   - Para que sea instalable, ábrela en Chrome/Edge → menú → "Instalar app".

## Funciona YA (sin configurar nada)
- ✅ Navegación entre Home / Simulacros / Materia / Formulario
- ✅ 7 simulacros con LaTeX, retroalimentación y explicaciones
- ✅ Guarda resultados y progreso (localStorage) — puedes reanudar exámenes
- ✅ Calculadora de notas, plan semanal del parcial
- ✅ Offline: una vez cargada, funciona sin internet
- ✅ Instalable como app en celular/escritorio

## Necesita TUS cuentas (ver `integraciones/`)
- **Supabase** (`supabase.js` + `schema.sql`): contador real de visitas y
  subida de material por estudiantes. Gratis. Setup ~10 min.
- **Wompi** (`wompi.js`): cobrar el Pack Premium (tarjeta, PSE, Nequi).
  Requiere cuenta de comercio + un webhook para confirmar pagos en producción.
- **Gate Premium** (`premium-gate.js`): desbloqueo por código. Funciona ya,
  útil para validar demanda antes de montar Wompi.

## Nota sobre seguridad del Premium
El gate por código y el desbloqueo en `localStorage` son para MVP. Para cobrar
de verdad y proteger contenido, el contenido premium debe servirse desde un
backend que verifique el pago (webhook de Wompi → marca al usuario como pago).
