# Auditoría de seguridad y rendimiento — MathUNAL

Base auditada: `main` @ `05d74f2` (`index.html` 38.322 líneas / 2,27 MB, `sw.js` v208).
Solo lectura: este archivo es lo único que cambia el PR.

**Leyenda de estado**
- **Confirmado**: visto en el código y/o reproducido con una medición (se indica cuál).
- **A verificar**: el código cliente muestra el patrón, pero la explotabilidad o el impacto dependen de algo que no está en el repo (código de las Edge Functions, políticas RLS reales, configuración de Supabase) o que no medí.

**Qué NO se pudo ver (límites de esta auditoría)**
- Las Edge Functions (`reportar-parcial`, `sim-wompi-sign`, `sim-wompi-verify`) y las políticas RLS reales de Supabase no están en el repo (solo `sim-pro-schema.sql`, que cubre las tablas `sim_*`). No hice peticiones contra producción. Al final hay SQL para verificar las políticas en 2 minutos.
- Las mediciones de rendimiento son de laboratorio: Chromium headless, sitio servido localmente sin compresión, recursos externos bloqueados (excepto donde se indica que se simuló latencia). Sirven para comparar y detectar patrones, no son datos de usuarios reales.

---

## Resumen ejecutivo

1. **Lo más serio de seguridad**: el banner de "Semana del Parcial" pinta con `innerHTML` el nombre de materia que viene de la tabla `parciales_reportados`, que **cualquier visitante** puede alimentar vía `reportar-parcial` (SEG-01). Si esa función no valida el campo, es XSS almacenado para todos los visitantes. El cliente no se defiende.
2. **Lo más serio de rendimiento**: `checkout.wompi.co/widget.js` está como `<script>` síncrono en el `<head>` (PERF-01). Medido: si Wompi tarda N segundos, la home aparece N segundos después, 1 a 1. Google Fonts y KaTeX tienen el mismo problema (PERF-02).
3. **Lo bueno** (verificado, ver sección "Revisado sin hallazgo"): no hay secretos privados en el código ni en el historial para los patrones buscados; los parámetros de URL están acotados por listas blancas; los toasts usan `textContent`; el SRI de KaTeX coincide con los archivos reales; el cobro firma e integra la verificación en servidor.
4. El service worker cachea respuestas autenticadas de Supabase (incluidas las soluciones Pro) y no las borra al cerrar sesión (SEG-02).
5. Hay 4 arreglos de ≤15 min con buen retorno (sección final).

---

# PARTE 1 — SEGURIDAD

## SEG-01 · XSS almacenado potencial por `parciales_reportados.materia_nombre`

| | |
|---|---|
| **Archivo:línea** | Origen del dato: `index.html:22844-22848` (el cliente envía `materia_nombre` a `/functions/v1/reportar-parcial`, sin autenticación). Lectura: `index.html:22711-22716` (`mat:f.materia_nombre`). Sinks: `index.html:22793` (`msg.innerHTML = prox.mat+…`) y `index.html:22890-22891` (`t.innerHTML = … prox.mat …`). |
| **Descripción** | El nombre de materia viaja del cliente al servidor, se guarda y luego se vuelve a leer para **todos** los visitantes, donde se concatena sin escapar dentro de `innerHTML`. El formulario solo ofrece el `<select>` de `SUBJECTS`, pero nada impide llamar a la función directamente con otro valor (`curl`). |
| **Severidad** | **Alta (potencial)**. Baja a media-baja si la Edge Function ya valida contra una lista blanca. |
| **Estado** | Sink y falta de escape en el cliente: **Confirmado**. Que la función acepte texto libre: **A verificar** (no tengo su código). |
| **Impacto real** | Se activa para cualquier visitante mientras exista una fila con `fecha_parcial` dentro de los próximos 14 días (`MU_DIAS_AVISO`, línea 22705); el atacante elige la fecha. `PEDIR_FECHA_HABILITADO=false` solo apaga el estado vacío del banner, **no** este camino. Con JS arbitrario en `mathunal.com` se pueden leer `localStorage['mu-auth']` (access + refresh token de Supabase, línea 35646) y suplantar sesiones, incluidas las de usuarios Pro. Es un ataque de un solo POST anónimo. |
| **Arreglo propuesto** | Dos capas (hacer ambas). **Cliente**: no usar el nombre que viene del servidor; resolverlo localmente por código y escapar lo demás. ```js function muEsc(s){return String(s==null?'':s).replace(/[&<>"']/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c];});}``` y en `__loadParciales` (22716): `mat: muEsc((SUBJECTS.find(function(s){return s.code===f.materia_code;})\|\|{}).nameEs \|\| f.materia_nombre)` (confirmar que la columna `materia_code` existe; el POST la envía). Además `confirmaciones`: `Number(f.confirmaciones)\|\|0`. **Servidor** (`reportar-parcial`): ignorar `materia_nombre` del cliente y derivarlo de `materia_code` contra una lista fija; validar `fecha_parcial` con regex `^\d{4}-\d{2}-\d{2}$`; limitar tasa por IP. |

## SEG-02 · El service worker cachea respuestas autenticadas/Pro de Supabase y no las limpia al cerrar sesión

| | |
|---|---|
| **Archivo:línea** | `sw.js:58-66` (todo `…supabase.co/rest/v1/` se guarda en Cache Storage con `c.put`); `index.html:33662` (`GET /rest/v1/sim_solutions`), `35781` (`progreso`), `36229` (`mu_reminders`); `index.html:36396` (`signOut` no borra cachés; no hay ningún `caches.` en `index.html`). |
| **Descripción** | La clave de caché es solo la URL, no el usuario ni el `Authorization`. Los GET autenticados (soluciones Pro, progreso, recordatorios) quedan guardados en Cache Storage hasta que cambie la versión del SW, y se sirven si falla la red. |
| **Severidad** | **Media**. |
| **Estado** | **Confirmado** por lectura de `sw.js` y búsqueda de `caches.` en `index.html` (0 resultados). No ejecuté el escenario de dos usuarios en un navegador. |
| **Impacto real** | (a) En un equipo compartido (sala de cómputo de la universidad, caso realista), tras cerrar sesión el contenido de pago y el progreso del usuario anterior siguen leíbles en DevTools y se sirven offline a quien use después ese navegador. (b) Si se revoca un entitlement (reembolso), el navegador del usuario conserva las soluciones. (c) Efecto secundario de rendimiento/almacenamiento: `muPresenciaContar` pide cada 25 s una URL distinta (`last_seen=gte.<fecha>`, línea 34006) y cada una se guarda como entrada nueva: unas 144 entradas por hora de pestaña abierta en la home, sin límite hasta el próximo bump de versión. |
| **Arreglo propuesto** | En `sw.js`, cachear solo lo público que se beneficia de estar offline y dejar el resto en red: ```js if (req.url.indexOf('.supabase.co/rest/v1/') !== -1) { if (!/\/rest\/v1\/materiales\?/.test(req.url)) return; /* red directa, sin caché */ …resto igual… }``` y en `signOut` (`index.html:36396`): `if(window.caches) caches.keys().then(function(k){k.forEach(function(n){caches.delete(n);});});`. Subir `CACHE` en `sw.js`. (Nota: esto toca `sw.js`; en esta tarea no lo modifiqué.) |

## SEG-03 · HTML crudo proveniente de la base de datos (materiales, explicaciones, `_mathHtml`)

| | |
|---|---|
| **Archivo:línea** | Ingesta: `index.html:20495-20500` (`name`, `size`, `sem`, `url`, `tipo` desde `materiales`). Sinks: `index.html:37788-37822` (`expFileCard`: `f.name`, `f.size`, `f.sem`, `f.type` concatenados en HTML y `url` dentro de `onclick="window.open('…')"` con solo `'` escapado), `index.html:37298-37303` (`<a href="'+m.url+'"`). Explicaciones: `index.html:32692-32700` + `32375` (`var esc=function(s){return String(s)}` — **no escapa nada**, el nombre engaña) + `32387+`. `_mathHtml` (`31594-31606`) deja pasar tal cual `<svg…>…</svg>` e `<img …>`. |
| **Descripción** | Contenido que se renderiza como HTML sin sanitizar por diseño (los textos llevan LaTeX/SVG). En `expFileCard` la URL va en un atributo `"…"`; un `"` en `url` rompe el atributo y permite inyectar un handler (`" onmouseover="…`). `_mathHtml` conserva `<img onerror=…>` y `<svg onload=…>`. |
| **Severidad** | **Baja-media**: la barrera es el acceso de escritura a `materiales`/`explicaciones`, que debería ser solo del dueño. |
| **Estado** | Falta de escape: **Confirmado**. Quién puede escribir esas tablas: **A verificar** (SQL al final). |
| **Impacto real** | Si las políticas RLS son correctas, solo explota alguien con la clave de servicio o acceso al panel de Supabase (en cuyo caso ya tiene problemas mayores). Es una amplificación: un compromiso de la BD o un error futuro de RLS se convierte en XSS contra todos los visitantes. |
| **Arreglo propuesto** | En `expFileCard`/`fileLink` pasar `name/size/sem/type` por `muEsc` (definida en SEG-01) y validar la URL: `/^https:\/\/goxhxrdchfyphkenixng\.supabase\.co\/storage\//.test(url)`; reemplazar el `onclick` en línea por `data-url` + un solo listener delegado. Para `_mathHtml`, filtrar atributos `on*` y `javascript:` de lo que conserva (o usar DOMPurify con lista blanca de `svg`). Renombrar `esc` en 32375 o hacerlo escapar realmente donde el contenido no lleve HTML. |

## SEG-04 · No hay Content-Security-Policy ni cabeceras de seguridad

| | |
|---|---|
| **Archivo:línea** | `index.html` (`<head>`, sin ninguna `<meta http-equiv>`); el sitio se sirve desde GitHub Pages (`CNAME`, `.nojekyll`), que **no permite cabeceras personalizadas**. |
| **Descripción** | Sin CSP, cualquier XSS (p. ej. SEG-01/03) puede cargar scripts de cualquier origen y exfiltrar a cualquier host. Sin `X-Frame-Options`/`frame-ancestors`, el sitio se puede enmarcar (clickjacking del botón de pago). |
| **Severidad** | **Media** (defensa en profundidad; no hay una vulnerabilidad explotable por sí misma). |
| **Estado** | **Confirmado** (ausencia). |
| **Impacto real** | Limitado por una realidad del código: hay 270 `onclick=` en línea en `index.html` más los que genera JS, scripts en línea por todos lados y un `new Function` (SEG-09), así que la CSP necesita `'unsafe-inline'` y `'unsafe-eval'`. Con eso **no frena XSS inyectado**; lo que sí aporta es limitar a dónde se puede enviar datos (`connect-src`), bloquear `<object>`, `<base>` y formularios hacia fuera. |
| **Arreglo propuesto** | Meta CSP inicial (hay que probarla en una copia: la lista de dominios de GA/Clarity/Wompi es **a verificar** con la consola del navegador antes de publicar; `<meta>` no admite `report-only` ni `frame-ancestors`): ```html <meta http-equiv="Content-Security-Policy" content="default-src 'self'; script-src 'self' 'unsafe-inline' 'unsafe-eval' https://cdn.jsdelivr.net https://cdnjs.cloudflare.com https://unpkg.com https://cdn.plot.ly https://www.googletagmanager.com https://plausible.io https://www.clarity.ms https://scripts.clarity.ms https://checkout.wompi.co; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com https://cdn.jsdelivr.net; font-src https://fonts.gstatic.com https://cdn.jsdelivr.net; img-src 'self' data: https:; connect-src 'self' https://goxhxrdchfyphkenixng.supabase.co https://*.google-analytics.com https://*.analytics.google.com https://www.googletagmanager.com https://plausible.io https://*.clarity.ms https://c.bing.com https://*.wompi.co; frame-src https://*.wompi.co; object-src 'none'; base-uri 'self'; form-action 'self'"> ``` Para cabeceras reales (y `frame-ancestors`) habría que poner Cloudflare (u otro proxy) delante de GitHub Pages. A largo plazo, mover los `onclick` a listeners permitiría quitar `'unsafe-inline'` de `script-src`. |

## SEG-05 · Scripts cargados dinámicamente sin SRI (three.js y Plotly)

| | |
|---|---|
| **Archivo:línea** | `index.html:20455` (`three@r128` desde cdnjs), `index.html:20544-20548` (Plotly 2.30.0 con 3 CDN de respaldo: jsdelivr, unpkg, plot.ly). |
| **Descripción** | KaTeX sí lleva `integrity` (líneas 79-81) y lo verifiqué; estos dos no. Un CDN comprometido ejecutaría código con acceso a la sesión. |
| **Severidad** | **Baja-media** (supply chain; requiere compromiso del CDN). |
| **Estado** | **Confirmado**. |
| **Impacto real** | Se cargan solo bajo demanda (fórmulas/juegos). Riesgo bajo pero el arreglo es barato. |
| **Arreglo propuesto** | Añadir `s.integrity='sha384-…'; s.crossOrigin='anonymous';` Hashes calculados hoy: three r128 (cdnjs) `sha384-CI3ELBVUz9XQO+97x6nwMDPosPR5XvsxW2ua7N1Xeygeh1IxtgqtCkGfQY9WWdHu`; Plotly desde jsdelivr (1.012.076 bytes) `sha384-rbHKh6NJkNLS4VPfOqaIegL2/G63qKM7B6AHM75XvvQ7oX/ZbkDYxqHQr3Cb0ANL`; Plotly desde cdn.plot.ly (1.010.573 bytes) `sha384-498vpZWJ4s46d993ZfLEhJ0nKiBSBR/nuPJY4cRVCM9BdGpfZPRFGGqM5YNqv7sD`. **Ojo**: los archivos de jsdelivr y plot.ly **no son idénticos** (distinto tamaño), así que cada URL del arreglo `cdns` necesita su propio hash (cambiar el arreglo a objetos `{src, integrity}`). unpkg no pude verificarlo desde este entorno (respuesta de 59 bytes del proxy): calcular su hash antes de usarlo o quitarlo de la lista. |

## SEG-06 · El paywall del simulacro por corte es 100 % del lado del cliente

| | |
|---|---|
| **Archivo:línea** | `index.html:33857` (`?freeplay=1` hace `return true` en `__simProGate`; el comentario dice "solo pruebas locales" pero corre en producción), `24271`; flags en `localStorage`: `mu-sim-pro`, `mu-sim-pro-srv-*` (`33553-33567`), `mu-premium` (`35290`); panel dev activable con `localStorage['mu-dev']='1'` (`38126`). |
| **Descripción** | Cualquiera puede abrir un simulacro de corte sin pagar con `?freeplay=1` o editando `localStorage`. |
| **Severidad** | **Baja** (modelo de negocio, no fuga de datos). |
| **Estado** | **Confirmado**. |
| **Impacto real** | Importante matizar: lo que está protegido de verdad es el contenido de valor. Las **soluciones, pasos y rúbricas** viven en `sim_solutions` con RLS por `sim_has_pro` (`sim-pro-schema.sql:84-86`, `index.html:33662`), y el cobro firma e integra la verificación en servidor. Lo que `freeplay` salta es el acceso a los enunciados, que de todos modos viajan en el JS del banco "flaco". El código ya lo documenta como "hint de UI" (`22641-22648`). Dicho esto, si el plan de monetización depende de que el enunciado completo sea de pago, hoy no lo es. |
| **Arreglo propuesto** | Decisión de producto. Mínimo: cambiar el chequeo de `freeplay` a `window.__SIM_LOCAL` para que deje de existir en producción (1 línea en 33857 y 24271). Si se quiere proteger el enunciado, habría que moverlo también a Supabase con RLS. |

## SEG-07 · Tokens de sesión de Supabase en `localStorage`

| | |
|---|---|
| **Archivo:línea** | `index.html:35646-35648` (`SKEY='mu-auth'`, `store()` guarda `access_token` + `refresh_token`). |
| **Descripción** | Es el patrón estándar de una SPA sin backend propio, pero cualquier XSS los lee. |
| **Severidad** | **Baja / informativa**. |
| **Estado** | **Confirmado** (comportamiento). |
| **Impacto real** | Es lo que convierte SEG-01/SEG-03 en toma de cuenta en vez de solo "defacement". No hay un arreglo barato sin servidor (cookies `HttpOnly` requieren un backend). Mitigación real: cerrar SEG-01/03 y SEG-04. |
| **Arreglo propuesto** | Ninguno propio; priorizar SEG-01/03. Opcional: acortar la vida del refresh token en la configuración de Auth de Supabase. |

## SEG-08 · `window.open(...,'_blank')` y enlaces `target="_blank"` sin `noopener`

| | |
|---|---|
| **Archivo:línea** | `window.open`: `33110`, `37180`, `37192`, `37194`, `37815`, `30714`. `<a target="_blank">` sin `rel`: `20864`, `21452`, `21614`, `21742`, `21743`, `21749`, `21750`, `21770`, `37303`. |
| **Descripción** | `window.open` sin la característica `noopener` deja a la página abierta con `window.opener`. Los `<a target=_blank>` ya reciben `noopener` implícito en navegadores modernos (Chrome ≥ 88, Firefox ≥ 79, Safari ≥ 12.1). |
| **Severidad** | **Baja**. |
| **Estado** | **Confirmado** (ausencia); impacto bajo. |
| **Impacto real** | Los destinos son `wa.me`, redes propias y PDFs en Supabase Storage (control del dueño). No hay vector práctico hoy; solo higiene. |
| **Arreglo propuesto** | `window.open(url,'_blank','noopener,noreferrer')` y `rel="noopener noreferrer"` en los 9 enlaces. Búsqueda y reemplazo mecánico. |

## SEG-09 · `new Function` sobre expresiones de figuras

| | |
|---|---|
| **Archivo:línea** | `index.html:32070`. |
| **Descripción** | Compila expresiones del campo de curvas de las figuras (`with(Math){return (expr)}`). El comentario dice "contenido propio, no entrada de usuario". |
| **Severidad** | **Baja**. |
| **Estado** | **A verificar**: confirmar que `fig` solo viene del banco empaquetado en el JS y nunca de Supabase (`sim_solutions`/`explicaciones`). Si viniera de la BD, pasaría a ser de la misma clase que SEG-03 pero con ejecución directa. |
| **Impacto real** | Obliga a `'unsafe-eval'` en la CSP (SEG-04). |
| **Arreglo propuesto** | Si el origen es solo local, dejarlo y documentarlo. Si algún día viene del servidor, reemplazar por un mini-parser de expresiones. |

## SEG-10 · `supabase/.temp/*` versionado

| | |
|---|---|
| **Archivo:línea** | `supabase/.temp/` (9 archivos, `git ls-files supabase`). Incluye `project-ref`, `linked-project.json` (nombre y `organization_id`) y `pooler-url` (`postgresql://postgres.<ref>@aws-1-us-east-1.pooler.supabase.com:5432/postgres`). |
| **Descripción** | Es el directorio temporal de la CLI de Supabase; no debería estar en git. |
| **Severidad** | **Baja**. |
| **Estado** | **Confirmado**. |
| **Impacto real** | No hay contraseñas (revisé el contenido). El `project-ref` ya es público por la URL de la API. Revela el ID de organización, la región y el host del pooler, que facilitan ataques de reconocimiento. |
| **Arreglo propuesto** | `git rm -r --cached supabase/.temp` y añadir `supabase/.temp/` a `.gitignore`. |

## SEG-11 · Tabla de presencia: escritura anónima y número suplantable

| | |
|---|---|
| **Archivo:línea** | `index.html:33994-34000` (POST anónimo a `presencia_online` con `session_id` elegido por el cliente), `34006` (conteo), `34024` (intervalo de 25 s). |
| **Descripción** | El "N personas navegando ahora" de la home sale de filas que cualquiera puede crear. |
| **Severidad** | **Baja**. |
| **Estado** | **A verificar** (políticas RLS/limpieza de la tabla). |
| **Impacto real** | Se puede inflar el contador (un POST por sesión falsa) o llenar la tabla. Es una afirmación pública del sitio ("real, no inventado", comentario en 33978), así que conviene que sea difícil de falsear. |
| **Arreglo propuesto** | Política `INSERT` con límite (p. ej. una función RPC que haga el upsert y limite por IP), job de purga de filas con `last_seen` viejo, y filtrar el conteo a sesiones con más de un latido. |

## SEG-12 · Terceros con acceso total a la página

| | |
|---|---|
| **Archivo:línea** | `index.html:6` (GA4), `14` (Plausible), `17-25` (Microsoft Clarity), `20596` (Wompi), `75` (Google Fonts). |
| **Descripción** | Estos scripts corren con los mismos permisos que el código propio y no admiten SRI (son dinámicos). Clarity graba la sesión (clics, scroll, DOM). |
| **Severidad** | **Informativa / baja**. |
| **Estado** | **Confirmado** (presencia). La política de privacidad ya los menciona (`index.html:28381-28389`). |
| **Impacto real** | Clarity puede registrar contenido de pantallas con sesión iniciada (correo, progreso). **A verificar** en el panel de Clarity que el enmascarado esté en modo estricto o que se ocultan los elementos con datos de cuenta (`data-clarity-mask="True"`). |
| **Arreglo propuesto** | Revisar el modo de enmascarado en Clarity; limitar con `connect-src` (SEG-04). |

## SEG-13 · Clave pública de Supabase duplicada en 5 lugares

| | |
|---|---|
| **Archivo:línea** | `index.html:20478`, `22709`, `25215`, `32743`, `35645` (y la URL del proyecto en 370 apariciones, la mayoría en el catálogo de PDFs). |
| **Descripción** | La clave `sb_publishable_…` es la pública equivalente a la `anon` (normal en el cliente, **no es un secreto**). El problema es mantenimiento: el comentario de `20473-20477` dice que rotarla es costoso, y hoy habría que cambiarla en cinco sitios. |
| **Severidad** | **Informativa**. |
| **Estado** | **Confirmado**. |
| **Impacto real** | Sin impacto de seguridad. Riesgo de olvidar uno al rotar. |
| **Arreglo propuesto** | Una sola constante `window.MU_SB_ANON` definida arriba y reutilizada. |

---

## Revisado sin hallazgo (confirmado)

| Tema | Resultado |
|---|---|
| **Secretos en el código** | No hay `service_role`, claves privadas, `prv_*`, `sk_*`, JWT ni bloques `BEGIN … KEY` en el árbol ni en el historial de git (103 commits; patrones buscados: `sk_live`, `prv_prod_/prv_test_`, JWT `eyJhbGciOi…`, `-----BEGIN`). La única clave en cliente es la publishable de Supabase (SEG-13). El comentario de `20475` menciona `service_role` solo como texto. Los archivos `sim-solutions*.dev.js` están en `.gitignore` y no están versionados. **Límite**: la búsqueda cubre esos patrones, no garantiza que no haya otros formatos. |
| **Parámetros de URL** | `s` (materia) se resuelve con `SUBJECTS.find(...)` (`37148`, `37261`, `37538`); `exam` solo es válido si existe en `EXAMS` (`25534`); `reto` se decodifica y se usa solo como claves de búsqueda en bancos locales y `corte` numérico (`33084-33099`). `id=` de Wompi (`33871`) solo se envía a la verificación en servidor. Ninguno llega a `innerHTML` sin pasar por una lista blanca. |
| **Toasts** | `_muToast` usa `textContent` (`24007-24013`), así que los mensajes de error del servidor (`35662`, `35670`) no inyectan HTML. |
| **SRI de KaTeX** | Recalculé los tres hashes sha384 contra los archivos reales de jsdelivr (`katex.min.css`, `katex.min.js`, `auto-render.min.js`): **coinciden**. |
| **Sinks peligrosos** | 0 usos de `eval(`, `document.write`, `postMessage`, `<iframe>`, `srcdoc`, `document.cookie`, `importScripts`. |
| **Cobro (Wompi)** | La referencia, el monto, la moneda y la firma de integridad vienen del servidor (`sim-wompi-sign`, `33798-33813`); la activación del Pro se confirma con `sim-wompi-verify` (`33693`) y el webhook. El cliente no decide el precio. El texto "$12.000" de `24273` es solo informativo. |
| **Contenido Pro** | Las soluciones salen de `sim_solutions` con RLS `sim_has_pro` (`sim-pro-schema.sql:84-86`); los `mu-premium`/`mu-sim-pro*` de `localStorage` solo cambian la UI (comentarios `22641-22648`). Los comentarios indican que las URL premium reales ya no viajan en el fetch público; **A verificar** en BD que `materiales` no devuelva filas `tier='premium'` con `url` a un bucket público. |
| **Robots/sitemap/Search Console** | `robots.txt`, `sitemap.xml`, `google90a1…html` sin contenido sensible. |

---

# PARTE 2 — RENDIMIENTO

Tamaños de `index.html` (calculados sobre el archivo): total **2.271 KB**; **577 KB con gzip -9** (GitHub Pages sirve gzip); 8 bloques `<style>` = 398 KB; 30 scripts en línea = 1.697 KB; 8 `<template>` = 670 KB. Cinco imágenes PNG en la raíz suman 1,1 MB, pero solo dos se piden al cargar la home (PERF-04).

## PERF-01 · `widget.js` de Wompi bloquea el arranque de toda la app

| | |
|---|---|
| **Archivo:línea** | `index.html:20596` (`<script src="https://checkout.wompi.co/widget.js" data-render="false"></script>`, sin `async`/`defer`, dentro del `<head>`). |
| **Descripción** | Script síncrono de tercero antes del código principal de la aplicación. Los scripts en línea que siguen (casi todo el JS de la app) no ejecutan hasta que Wompi responde o falla. |
| **Severidad** | **Alta**. |
| **Estado** | **Confirmado con medición**: con Playwright retrasé solo la respuesta de ese host y medí cuándo se renderiza la home (`__muCurrentPage==='home'`): sin retraso **282 ms**; con 3 s de latencia, **3.201 ms**; con 8 s, **8.149 ms**. Es lineal: el sitio tarda exactamente lo que tarde Wompi. |
| **Impacto real** | Es un punto único de falla en el camino crítico para una función (pago) que usa una fracción de los visitantes y solo en un modal. Una red universitaria lenta, un bloqueo parcial o una caída de Wompi dejan la página en blanco. (Si el host está bloqueado del todo, falla rápido y el efecto es menor; el peor caso es la conexión que se cuelga.) El comentario de la línea dice "sandbox" pero la URL es la de producción. |
| **Arreglo propuesto** | Cargarlo bajo demanda al abrir el checkout, que ya comprueba `window.WidgetCheckout` (`33801`): ```js function muLoadWompi(cb){ if(window.WidgetCheckout) return cb(); var s=document.createElement('script'); s.src='https://checkout.wompi.co/widget.js'; s.async=true; s.setAttribute('data-render','false'); s.onload=cb; s.onerror=function(){ /* toast "pago no disponible" */ }; document.head.appendChild(s); }``` y llamar `muLoadWompi(function(){ new window.WidgetCheckout(...) })` en `33801-33815`. Alternativa mínima de 1 línea: agregar `async` a la etiqueta (el chequeo `!window.WidgetCheckout` ya cubre el caso de que aún no haya cargado). |

## PERF-02 · Google Fonts y KaTeX bloquean el primer render y el arranque

| | |
|---|---|
| **Archivo:línea** | `index.html:75` (CSS de Google Fonts, bloqueante de render), `79` (`katex.min.css`, bloqueante), `80-81` (`katex.min.js` y `auto-render` con `defer`). |
| **Descripción** | Dos hojas de estilo externas bloquean el pintado; los scripts `defer` retrasan `DOMContentLoaded`, que es cuando arranca la app. KaTeX solo se usa en Simulacros, Fórmulas y Diagnóstico, pero se carga en cada página. |
| **Severidad** | **Media-alta** (misma clase de riesgo que PERF-01, con latencia más probable porque son más archivos). |
| **Estado** | **Confirmado con medición** (retrasando 6 s cada recurso): Google Fonts CSS → app lista y FCP a los **6.190 / 6.140 ms**; `katex.min.css` → **6.159 / 6.096 ms**; `katex.min.js` (defer) → FCP 180 ms pero app lista a los **6.098 ms**; GA y Clarity (async) → sin efecto (222 y 283 ms). |
| **Impacto real** | Cada recurso externo lento en la ruta crítica se convierte en pantalla vacía. GA/Clarity/Plausible están bien (async). |
| **Arreglo propuesto** | Fuentes: ```html <link rel="stylesheet" href="…fonts.googleapis…" media="print" onload="this.media='all'"> <noscript><link rel="stylesheet" href="…"></noscript>``` (ya tiene `display=swap`). KaTeX: cargar CSS y JS solo cuando la ruta lo necesita (el código ya soporta KaTeX tardío con `__onKatexReady`, líneas 80 y 30962). Cuidado: `auto-render` necesita que `katex` exista antes, así que no basta con `async`; hay que encadenar (cargar `katex.min.js`, en `onload` cargar `auto-render`). Mantener `integrity`. |

## PERF-03 · Todo se descarga y parsea de entrada (monolito de 2,3 MB)

| | |
|---|---|
| **Archivo:línea** | Script de materia `index.html:31428-37915` (723 KB), segundo bloque grande `32757` (389 KB), banco de simulacros `85-13782` (337 KB), `35306+` (213 KB); `<template>` de formulas (174 KB), juegos (130 KB), simulacro (111 KB), diagnóstico (33 KB) dentro del mismo HTML. |
| **Descripción** | El HTML inicial incluye el JS y las plantillas de todas las páginas, los diccionarios EN (`_EXAM_EN` ~42 KB, `LANG_ES/EN` ~53 KB), el catálogo `MATS` (~71 KB) y el banco completo de simulacros. |
| **Severidad** | **Media**. |
| **Estado** | **Confirmado**. Mediciones de laboratorio en la home con 4× de ralentización de CPU (móvil modesto): 6 tareas largas, una de **1.087 ms**; unos 4,5 s de CPU muestreada, de los cuales ~2,9 s son "program" (parseo/compilación/layout nativo) frente a ~0,9 s de JS propio. Sin ralentización, DCL = 738 ms (escritorio), 256 ms (móvil emulado). La home deja **~13.400 nodos de DOM** (~10.000 tras estabilizar). |
| **Impacto real** | En un teléfono de gama baja, el primer arranque es lento aunque la red sea buena; cada visita con caché caducada (GitHub Pages usa `max-age=600`) vuelve a bajar 577 KB comprimidos. |
| **Arreglo propuesto** | Por orden de retorno/esfuerzo: (1) Extraer a archivos `.js` separados lo que no necesita la home, cargados al entrar en la ruta: el banco de simulacros (337 KB) y los `<template>` de formulas/juegos/simulacro/diagnóstico (~450 KB, ahorro estimado ~110 KB comprimidos). (2) Archivos externos permiten caché del navegador independiente del HTML. (3) Diccionarios EN solo si `lang==='en'`. Es refactor de riesgo medio; hacerlo con la suite de rutas Playwright de la rama `pruebas-y-movil` como red de seguridad. |

## PERF-04 · Dos imágenes ocultas se descargan siempre (287 KB)

| | |
|---|---|
| **Archivo:línea** | `index.html:21529` (`qr-wa-grupo.png`, 18 KB) y `21629` (`qr-breb-v3.png`, 269 KB), ambas dentro de overlays de "ampliar" (`display:none`) y **sin** `loading="lazy"`. Sus gemelas visibles (21520, 21625) sí lo tienen. |
| **Descripción** | La versión visible es lazy, pero la copia del overlay no, así que se baja desde la carga de la home aunque nadie abra el zoom. |
| **Severidad** | **Media-baja**. |
| **Estado** | **Confirmado**: en Playwright, tras cargar la home, las dos imágenes lazy tenían `complete:false` y las dos del overlay `complete:true` (naturalWidth 480 y 413). El log de red de la home muestra solo esas dos peticiones locales además del HTML. |
| **Impacto real** | 287 KB (más que todo el HTML comprimido de otras páginas) en cada primera visita, en móvil con datos. |
| **Arreglo propuesto** | Añadir `loading="lazy"` a las dos etiquetas (2 líneas). Opcional: `qr-breb-v3.png` mide 413×622 y se muestra a 240×362; un QR de 2 colores comprime muy por debajo de 269 KB (convertir a PNG indexado o WebP; **a verificar** el ahorro real, no tengo herramienta de imagen en este entorno). |

## PERF-05 · CSS: gran parte no se aplica en ninguna ruta probada

| | |
|---|---|
| **Archivo:línea** | 3 hojas en `index.html` (380.640 caracteres de reglas en total). |
| **Descripción** | Recorrido de 10 rutas × 4 temas × 2 idiomas × 2 anchos (360 y 1280) con el seguimiento de uso de reglas de Chrome: se usó el **32 %** (~123 KB); ~251 KB nunca coincidieron con ningún elemento. Por otro lado, 611 de las 1.813 clases definidas en CSS (**34 %**) no aparecen en ningún otro punto del archivo (ni en HTML ni en cadenas de JS). Ejemplos de prefijos completos: `bkl-*` (≈40 clases), `aport-*`, `arc-hud*`. |
| **Severidad** | **Baja-media**. |
| **Estado** | **A verificar**. Mi recorrido no activa hover/focus, modales, juegos, pantallas intermedias del simulacro, panel dev, ni reglas generadas con concatenación de cadenas (`'bkl-'+x`). Sirve como mapa de candidatos, no como lista para borrar. |
| **Impacto real** | Peso y tiempo de parseo/cálculo de estilos en cada carga; también hace más difícil mantener el CSS. |
| **Arreglo propuesto** | Revisar los prefijos con más clases sin uso (`bkl-`, `aport-`, `arc-hud`) y borrarlos con la suite de rutas y capturas como verificación; luego repetir la medición. |

## PERF-06 · Fuga de nodos y listeners al visitar `#formulas`

| | |
|---|---|
| **Archivo:línea** | Pantalla `tpl-formulas` (`index.html`, template ~174 KB; la causa exacta no está identificada). |
| **Descripción** | Navegando home → fórmulas → home 10 veces con GC forzado, el recuento de nodos de DOM sube linealmente: 10.009 → 14.245 (5 visitas) → 18.475 (10 visitas) ≈ **+850 nodos y ≈ +87 listeners por visita**, sin bajar tras GC. Las demás rutas (`#juegos`, `#diagnostico`, `#acerca`, `#materia`, `#simulacro`, `#privacidad`) se estabilizan; `acerca` sube ~330 nodos y se recupera al visitar otra (se limpia tarde, no es fuga continua). |
| **Severidad** | **Baja-media**. |
| **Estado** | **Confirmado con medición** (contadores `Nodes`/`JSEventListeners` de CDP tras `HeapProfiler.collectGarbage` ×2). La causa raíz es **a verificar**. |
| **Impacto real** | Crece el uso de memoria en sesiones largas navegando entre fórmulas y otras páginas; el JS heap medido casi no se mueve (3,3 MB), así que el efecto en memoria es moderado (decenas de MB tras cientos de visitas), no un cierre del navegador. |
| **Arreglo propuesto** | Buscar en el script de Fórmulas listeners en `document`/`window` o referencias globales a nodos de la página que no se limpian al salir (`addEventListener` sin `removeEventListener`, arreglos globales que acumulan elementos). Reproducir con el bucle de visitas para confirmar la corrección. Los intervalos y observadores están bien: solo quedan vivos los 2 `setInterval` esperados (presencia en home, recordatorios) y se cancelan al cambiar de ruta. |

## PERF-07 · Animaciones infinitas de `box-shadow` mantienen la home ocupada en reposo

| | |
|---|---|
| **Archivo:línea** | `@keyframes muCalPulse` (`index.html:19802`, usada en 19828 y 19848) y `muDatoGlow` (`19787`) animan `box-shadow`; `tdot` (`15274`) anima `opacity`; el resto son `transform` (`logoFloat` 19224, `mfloat` 15264, `muSymFloat` 19786, `simSweep` 19414). |
| **Descripción** | `box-shadow` no se compone en la GPU: cada fotograma repinta. En la home hay 13 animaciones infinitas activas a la vez. |
| **Severidad** | **Media-baja**. |
| **Estado** | **Confirmado con medición**: página en reposo 5 s (sin interacción) → **0,464 s de tarea de hilo principal y 176 recálculos de estilo en la home**, frente a 0,007–0,099 s en `#formulas`, `#simulacro` y `#juegos`. Medido en escritorio rápido; en móvil modesto pesa proporcionalmente más. |
| **Impacto real** | Consumo de CPU/batería constante mientras la home está abierta (≈9 % del hilo principal en la máquina de prueba). |
| **Arreglo propuesto** | Sustituir el pulso de `box-shadow` por un pseudo-elemento cuyo `opacity`/`transform` se anime (compositor), pausar las animaciones con `animation-play-state` cuando la pestaña no es visible o el elemento sale de pantalla (IntersectionObserver), y respetar `prefers-reduced-motion` en estas animaciones (la rama de accesibilidad ya lo propone). |

## PERF-08 · Patrones de layout/reflow menores (no medidos individualmente)

| | |
|---|---|
| **Archivo:línea** | Handler de scroll `index.html:30943-30962` (lee `scrollHeight`/`clientHeight` tras alternar clases en cada evento); `@keyframes sim-lock-shine` (`17081`) anima `left`; 150 usos de `transition: all`; 41 de `backdrop-filter`; solo 2 `will-change`. |
| **Descripción** | Escribir clases y luego leer geometría en cada scroll fuerza recálculo de layout; animar `left` repinta en vez de componer; `transition: all` anima propiedades no previstas. |
| **Severidad** | **Baja**. |
| **Estado** | **A verificar**: en reposo medí 0 layouts; **no** medí el scroll real ni el costo de `backdrop-filter` en móvil. |
| **Impacto real** | Probable jank leve al hacer scroll en móviles de gama baja con muchos elementos con `backdrop-filter`. |
| **Arreglo propuesto** | En el handler de scroll, medir una vez (en `resize`/carga) y no en cada evento, o usar un `IntersectionObserver` sobre un centinela para `show` del botón de subir; reemplazar `left` por `transform: translateX` en `sim-lock-shine`; revisar en un dispositivo real con el perfil de rendimiento de Chrome antes de tocar los `backdrop-filter`. |

## PERF-09 · Desplazamiento de layout (CLS) intermitente en la carga de la home

| | |
|---|---|
| **Archivo:línea** | Elementos `.lg-blob` (blobs decorativos del fondo). |
| **Descripción** | En el arranque se registra un desplazamiento de layout atribuido a `lg-blob lg-blob-center` (y `-tr`, `-tl`, `math-float` en escritorio) alrededor de los 650-700 ms. |
| **Severidad** | **Baja**. |
| **Estado** | **A verificar**: es intermitente (CLS 0,111 en móvil, 0,137 en escritorio, 0,000 en la corrida con CPU 4× más lenta); el umbral "bueno" es ≤ 0,1. Son medidas de laboratorio sin fuentes ni terceros reales. |
| **Impacto real** | Posible salto visual al abrir la home; poco efecto probable en Core Web Vitals reales si los blobs son `position:absolute` decorativos, pero conviene confirmarlo con datos de campo (Search Console / CrUX). |
| **Arreglo propuesto** | Fijar tamaño/posición de los blobs desde el CSS inicial (sin que dependan de la inyección del template) o aplicarles `contain: layout`. |

## PERF-10 · Service worker: recarga automática y ciclo de vida

| | |
|---|---|
| **Archivo:línea** | `sw.js:20,28` (`skipWaiting` + `clients.claim`), `index.html:36457-36460` (`controllerchange` → `location.reload()`). |
| **Descripción** | Al desplegar una versión nueva, las pestañas abiertas se recargan solas. |
| **Severidad** | **Baja**. |
| **Estado** | **A verificar**: no comprobé si un simulacro en curso conserva su estado tras recargar (existen claves `mu-prog-*` en `localStorage`, lo que sugiere que sí). |
| **Impacto real** | Posible pérdida de contexto a mitad de un examen la primera vez que se despliega con la pestaña abierta. |
| **Arreglo propuesto** | Evitar el reload automático si hay un simulacro en curso, o mostrar un aviso "hay una versión nueva, recargar" en lugar de recargar a la fuerza. |

## PERF-11 · Imágenes y fuentes: observaciones menores

- `og-image.png` (194 KB), `icon-512.png` (164 KB) e `icon-maskable.png` (145 KB) solo las piden rastreadores y la instalación PWA, no la carga normal. Aceptables.
- Fuentes: 5 familias en una sola petición (Literata ×6 pesos/estilos, Space Grotesk ×5, IBM Plex Mono ×3, Source Serif 4 ×5, EB Garamond ×2). `Source Serif 4` aparece en 4 `font-family` y `EB Garamond` en 9, frente a 331 de IBM Plex Mono y 160 de Literata. **A verificar** si esas dos familias se justifican; quitarlas acorta el CSS de fuentes y reduce descargas.
- Código muerto en JS: casi nada. Solo 25 de 545 funciones aparecen una única vez en todo el archivo y varias son stubs (`renderMats`, `renderFormTab`, etc., líneas 37154-37160). No es donde está el peso; el peso es el volumen de datos y código eagerly cargado (PERF-03).

---

# Los 5 arreglos de mejor relación esfuerzo/beneficio

| # | Arreglo | Esfuerzo | Beneficio |
|---|---|---|---|
| 1 | **SEG-01**: escapar/derivar `materia_nombre` en el banner (3 líneas en `22716`) y validar `materia_code`/`fecha` en `reportar-parcial` | ~15 min | Cierra el único camino de XSS almacenado anónimo con robo de sesiones |
| 2 | **PERF-01 + PERF-02 (parte fuentes)**: `async` o carga a demanda del `widget.js` de Wompi y fuentes de Google no bloqueantes | ~15 min | La home deja de depender de la latencia de dos terceros; medido: de "N segundos de espera" a ~0 |
| 3 | **PERF-04**: `loading="lazy"` en las 2 imágenes de los overlays (`21529`, `21629`) | 2 min | −287 KB en cada primera visita |
| 4 | **SEG-02**: el SW solo cachea `…/rest/v1/materiales`, y `signOut` borra las cachés (+ subir versión de `CACHE`) | ~20 min | Elimina fuga de contenido Pro/progreso en equipos compartidos y el crecimiento infinito de entradas |
| 5 | **SEG-05 + SEG-04**: SRI en three/Plotly (hashes listos arriba) y meta CSP inicial probada en copia | ~45 min | Cierra la cadena de suministro dinámica y limita a dónde puede exfiltrar un script inyectado |

Siguientes en la lista: SEG-03 (escape en `expFileCard`), PERF-06 (fuga en fórmulas), SEG-08/10 (higiene), PERF-03 (dividir el monolito, el de mayor retorno a largo plazo y mayor esfuerzo).

---

# Anexos

## A. SQL para verificar los puntos "A verificar" de Supabase

```sql
-- Políticas RLS por tabla: ¿quién puede INSERT/UPDATE/DELETE?
select tablename, policyname, cmd, roles, qual, with_check
from pg_policies where schemaname = 'public'
order by tablename, cmd;

-- Tablas públicas sin RLS activado
select relname from pg_class c join pg_namespace n on n.oid = c.relnamespace
where n.nspname = 'public' and c.relkind = 'r' and not c.relrowsecurity;

-- ¿Filas premium con url expuesta a anon?
select tier, count(*), count(url) from public.materiales group by tier;
```
Tablas a mirar con prioridad: `materiales`, `explicaciones`, `parciales_reportados`, `presencia_online` (que `anon` no tenga `UPDATE/DELETE` ni `INSERT` libre donde no debe), y el bucket `Materiales` de Storage (que `anon` no pueda escribir).

## B. Método de las mediciones

- Servidor estático local y Chromium con `--host-resolver-rules` para servir `mathunal.test` desde 127.0.0.1 (así el sitio no entra en modo "local/dev"); peticiones externas bloqueadas salvo las que se retrasaron a propósito.
- Contadores de CDP (`Performance.getMetrics`, `Profiler`, `CSS.startRuleUsageTracking`), `PerformanceObserver` para tareas largas y layout shift, `Emulation.setCPUThrottlingRate` ×4 para el perfil móvil.
- Fuga de nodos: bucle de visitas ida y vuelta con `HeapProfiler.collectGarbage` antes de cada lectura.
- Los números absolutos dependen de esta máquina y deben tomarse como relativos. Los scripts de medición no se incluyen en este PR (es un único archivo); si los quieres versionados, se pueden añadir a `tests/` en la rama `pruebas-y-movil`.
