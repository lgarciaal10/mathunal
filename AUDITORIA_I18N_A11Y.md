# Auditoría i18n + accesibilidad — MathUNAL

- **Fecha:** 2026-10-07 · **Rama:** `auditoria-i18n-a11y` · **Alcance:** solo lectura (este archivo es el único cambio).
- **Archivos revisados:** `index.html` (38 180 líneas, las 8 plantillas `tpl-*` + el HTML/JS persistente), `404.html`, `simulacros-lab.html`, `sw.js` (sin texto de UI). Las referencias `archivo:línea` son de `index.html` salvo que se indique otro archivo.
- **Severidad:** **alta** = bloquea o vacía una función para teclado/lector de pantalla, o deja contenido principal en el idioma equivocado/ilegible · **media** = degrada claramente la experiencia · **baja** = pulido/limpieza. **a verificar** = lo veo en el código pero no lo pude confirmar en ejecución.

## 0. Cómo se midió (y límites)

| Qué | Cómo |
|---|---|
| Diccionarios | Extraje `LANG_ES`/`LANG_EN` (líneas 34018–34301 y 34302–34590) y comparé claves, duplicados, referencias en código y valores. |
| Texto visible por idioma | Chromium headless (Playwright) sirviendo el repo en `127.0.0.1`. Recorrí 10 rutas × ES/EN (incluye `materia?s=…` ×3), más flujos interactivos en EN y ES: ajustes, menú «Más», modales (pánico, semana del parcial, cuenta), paleta Ctrl+K, FAQ, calculadoras, Sprint, diagnóstico completo, simulacro (con pago simulado de dev), 5 juegos, filtros de materia. En cada paso extraje texto visible y `aria-label`/`title`/`placeholder`/`alt`. |
| Calidad de la traducción automática | Evalué en el navegador `_examEN()` sobre las 542 preguntas de `window.EXAMS` y `_docEN()` sobre los 673 nombres de archivo de las 12 materias. |
| Contraste | axe-core (reglas WCAG 2 A/AA, 2.1, 2.2 AA + best-practice) en **4 temas × 9 rutas** y en 7 estados superpuestos (menús, modales, paleta), más cálculo de razones de contraste de los tokens de cada tema. |
| Teclado | Recorrido real con `Tab` (Azul: home 130 paradas, fórmulas 46, juegos, diagnóstico, simulacro y materia; Gris/Claro/Negro: home, fórmulas, diagnóstico y simulacro), con diferencia de píxeles entre «con foco» y «sin foco» por cada parada; inventario de elementos con `onclick` no semánticos. |
| Táctil | Viewport 390×844 con touch; todos los elementos interactivos visibles < 44 px. |

**Límites:** (1) corrí en `localhost`, así que el panel dev (`#mu-dev-tab`, `__SIM_LOCAL`) está activo; lo excluí de todos los conteos. (2) Los conteos son de estados por defecto + los flujos listados, no exhaustivos. (3) No usé lector de pantalla real; lo marcado «a verificar» necesita esa prueba. (4) Los scripts de medición viven fuera del repo (no se commitearon).

**Lo que ya está bien (para no tocarlo):** existe `:focus-visible` global (`14917`, `18989`); hay skip link; `<html lang>` se actualiza en `setLang` (34600); las 4 `<img>` tienen `alt`; axe **no** encontró `button-name`, `image-alt` ni `link-name` fallidos en los estados probados; hay una regla global de `prefers-reduced-motion` (18996) y `scroll-behavior` ya se respeta en una de las 13 llamadas JS (24547); los temas Azul y Claro están cerca de AA (43 y 46 nodos con fallo en 9 rutas; ver 2.1); la paridad de claves ES/EN es perfecta (442/442).

---

# 1. Traducciones (i18n)

## 1.1 (b) Claves ES ↔ EN (diccionarios)

Resultado base: **442 claves en ES y 442 en EN, 0 faltantes en cada lado.** No hay hueco ES/EN a nivel de clave; los problemas están en duplicados, claves muertas e inconsistencias de contenido.

| ID | Archivo:línea | Problema | Sev. | Arreglo sugerido |
|---|---|---|---|---|
| K-01 | `setLang` 34752–34754 y 34763–34766 vs 35000 y 35053; dict. ES 34058/34195 y 34064/34225, EN 34342/34479 y 34348/34509 | `comm-h` y `prom-h` están **definidas dos veces con valores distintos** (la última gana). El primer bloque de `setLang` (34753, 34765) hace `L['comm-h']+' <i>'+L['comm-hi']+'</i>'` esperando la versión corta («No estudies solo,»), recibe la larga que ya trae `<i>únete</i>` y pinta «…únete únete» hasta que el bloque posterior (35000, 35053) lo pisa. Funciona por accidente. | media | Dejar una sola definición por clave (la larga con HTML) y borrar el bloque viejo de 34752–34754 y 34763–34766 (el posterior ya lo cubre). Quitar `comm-label`/`comm-hi`/`prom-label`/`prom-hi` si no se usan en otro sitio. |
| K-02 | `foot-made` 34299/34583 vs HTML 21734 | `foot-made` es una clave huérfana **y** su texto difiere del HTML («Hecho a mano en Medellín ♥» vs «Hecho en Medellín ♥»). Nunca se aplica: el pie queda en español en EN (visto en ejecución). | media | `21734`: `<p class="foot-made">Hecho en Medellín …` y en `setLang`: `setHTML('.foot-made','foot-made')` (unificando el texto ES con el del diccionario). |
| K-03 | `comm-sub` 34059/34343 (usada en 34754) vs `comm-p` 34196/34480 (usada en 35000), y `hero-sub` 34026/34310 vs `mat-sub` 34032/34316 y `ruta-foot` 34273/34557 | Datos contradictorios entre claves: `comm-sub` dice «+2.400 estudiantes» y `comm-p` «+2.000» (solo se ve la segunda); `hero-sub` dice «6 materias del núcleo» mientras `mat-sub`/`ruta-foot` dicen «12». En EN `hero-sub` además agrega «of the School of Engineering» que no está en ES. | media | Decidir la cifra real y dejar una sola clave por dato; quitar `comm-sub`. En EN: «…for the **6 core math subjects**.» (sin «of the School of Engineering») o aclarar qué son las 6 vs 12. **a verificar** cuál cifra es la vigente. |
| K-04 | 34050–34056 = 34183–34189 (ES); 34334–34340 = 34467–34473 (EN) | Bloque `calc-*` duplicado idéntico (11 claves). | baja | Borrar uno de los dos bloques. |
| K-05 | ver lista abajo | **55 claves huérfanas** (no se referencian como literal en ningún lugar fuera de los diccionarios). | baja | Borrar o reconectar. Lista: `banco-label, banco-h, banco-hi, banco-sub, banco-mat, banco-all, banco-search, test-label, test-h, test-hi, cp-title-default, cm-l-parciales, cm-l-talleres, cm-l-quices, cm-l-simulacros, cm-l-solucionarios, cm-l-total, hero-ctx, calc-min, calc-p2, comm-tg-t/-d/-l, comm-dc-t/-d/-l, ap2-wa-i3, ap3-i3, smap-col1…4, smap-ver-todas, smap-popular, smap-sim, smap-form, smap-calc, smap-prom, smap-banco, smap-pack, smap-aportar, smap-hist, smap-prox, smap-faq, smap-wa, smap-tg, smap-dc, smap-top, smap-quick-sim/-banco/-form, foot-ig, foot-vertodas, mu-calc-pf-ph, foot-made`. (`cm-l-*` y `smap-*` pueden armarse con prefijo dinámico: **a verificar** antes de borrar.) |
| K-06 | 34149/34433 (`tl-title`), 21603, 24242–24243 | Formato numérico mezclado: ES usa «60,000» (coma inglesa) en `tl-title`; en EN siguen saliendo «$5.000» (21603, `.ap-amount`) y «$12.000» (24242, `sim-intro-prohint`) con punto de miles español. | baja | Un helper `fmtCOP(n)` con `n.toLocaleString(curLang==='en'?'en-US':'es-CO')`; en ES cambiar «60,000» por «60.000». |
| K-07 | 22342, 22345 | Los contadores animados formatean con `toLocaleString('es-CO')` siempre (hoy solo `data-n="1200"` ≥ 1000 → «1.200» también en EN). | baja (**a verificar** visualmente) | `toLocaleString(window.curLang==='en'?'en-US':'es-CO')`. |

## 1.2 (a) Texto que no pasa por i18n (se queda en un solo idioma)

T-01…T-10 se **reprodujeron en ejecución en modo EN** (el texto queda en español); T-11…T-16 son hallazgos de lectura del código/archivo. Ordenado por severidad.

| ID | Archivo:línea | Problema | Sev. | Arreglo sugerido |
|---|---|---|---|---|
| T-01 | 22278, 22287–22296, 22307, 22323 (`calc2/3/4`, `calcResult`) | La calculadora estrella «¿Cuánto necesito para pasar?»: todos los **mensajes de resultado** están en español fijo («Ya pasas sin importar lo que saques…», «Fácil. Lo tienes…», «Los pesos deben sumar 100%…»). Probado: en EN responde «Alcanzable. Estudia bien estos días.» | **alta** | Ver snippet **S1**. |
| T-02 | 22531, 22541–22545 (`calcProm`) | Calculadora de promedio: estado («Aprobado (SIA redondea a 3.4)», «Excelente · Honor roll»…) y las 4 filas de estadísticas («Total créditos», «Materias aprobadas», «Materias reprobadas», «Créditos × nota prom.») en español fijo. Probado en EN: «Aprobado (SIA redondea a 3.4)». | **alta** | Mismo patrón que S1 (`var L=window.curLang==='en'`). |
| T-03 | 23688–23691, 24553, 24564–24566, 24674 | Pantalla de pregunta del simulacro: contador «Pregunta 1 de 9», tipo («Selección múltiple con única respuesta»), botones «← Anterior / Marcar para revisar / Siguiente → / Confirmar respuesta» quedan en ES en EN (reproducido). | **alta** | Ver snippet **S2**. |
| T-04 | 24151, 24213, 24195/24360, 23650 | Selector de simulacros: títulos de tarjeta («Cálculo Diferencial · Quiz») sin traducir; intro: `6 opción múltiple` (24213 no usa `en?`, el 24367 sí); `CORTE 1 (30%)` (nombre de corte del examen) mezclado; cabecera «Sede **Medellin** · Escuela de **Matematicas**» sin tildes **en ambos idiomas** (typo ES, 23650). | media | Traducir `ex.titulo` con el mismo mapa `matEn` de `muApplyLang_simulacro` (23820); 24213 → `nmcq+(en?' multiple choice':' opción múltiple')`; corregir tildes en 23650 (y `Cod.` 24443 ya tiene rama EN). |
| T-05 | 20574 | Skip link «Saltar al contenido» nunca se traduce (`setLang` no lo toca). | media | `setLang`: `var sk=document.querySelector('.skip-link'); if(sk) sk.textContent=en?'Skip to content':'Saltar al contenido';` |
| T-06 | 20578–20580, 20707, 21909, 36351, 20590, 21307, 20679/23400/23477/25523/27786/28371/28517 | **Nombres accesibles** que quedan en español en EN: `#mu-scrollnav` («Navegación de la página»), `#mu-goup`/`#mu-godown` («Ir arriba», «Ir al fondo», también `title`), burger («Abrir menú»; `tmob()` además reescribe `'Cerrar menú'/'Abrir menú'` fijos, 21909), botón de cuenta («Cuenta», 36351), `#cmd-box` («Buscador rápido»), `#wm-fecha` («Fecha del parcial»), botón de ajustes («Ajustes» ×7 plantillas). | media | Centralizar en `setLang`: `document.querySelectorAll('[data-i18n-aria]')` con diccionario, o añadir esas claves a `LANG_*` y asignarlas: `document.getElementById('mu-goup').setAttribute('aria-label',L['a11y-up'])`. En `tmob()`: `en?'Close menu':'Cerrar menú'`. |
| T-07 | 21489, 21491, 21498, 21591–21598, 21739, 28355, 22472, 22478 | `alt`/`title`/`aria-label` de los QR («Código QR del grupo de WhatsApp…», «Ampliar el código QR», «Toca para ampliar», «…ampliado»), botón flotante de WhatsApp («Escríbenos por WhatsApp») y placeholder «Nombre de la materia» (22472) / `title="Eliminar"` (22478) sin traducir en EN. | media | Igual que T-06 (claves nuevas + asignación en `setLang`). |
| T-08 | 25935, 25939–25940, 25946, 25985, 26024, 26071, 26082, 26091, 26847, 27475, 26246–26253, 26477, 26664 | Juegos: hints/descripciones del Portal, títulos de resultado («¡Chocaste!», «¡Llegaste!», «¡Completado!», «¡Nivel superado!», «Elige la opción correcta.»), **toasts** («La bola se detuvo…», «¡No puede ir ahí!…», «¡Copiado! Pégalo en tu grupo») y el **texto de compartir** («…resuelto en N movimientos. ¿Me superas?») solo en ES. El propio comentario de 26113–26115 reconoce que está pendiente. | media | Extender `muApplyLang_juegos` (26117) con los `t(id, es, en)` que faltan y envolver `toast()`: `function toast(es,en){ … t.textContent=(window.curLang==='en'&&en)?en:es; }`. |
| T-09 | 21130, 21734, 23422, 23436–23438 (+31411/31416/31426), 37745, 37514/37643, 30152/30139, 28534/23580, 20596–20601, 21765, 21811, 23499 | Resto de textos visibles en ES con la web en EN: «Diagnóstico rápido (gratis)» (home), «Hecho en Medellín» (pie), «CÓDIGO» y «Materias relacionadas» (materia), cabecera de tabla «Sem.» y abreviatura «GRAL./REF.» (materia), «No se pudo cargar la gráfica (sin conexión o CDN bloqueado)» + «Reintentar» (fórmulas), `aria-label="Filtrar por materia"`, pie de la paleta Ctrl+K («cerrar / navegar / abrir»), «Modo Sprint» y su línea de atajos («Espacio revela · 1 la sabía · 2 repasar · Esc salir»), `title="Tiempo en esta pregunta"`. | media | Añadir claves y asignarlas en `setLang`/`muApplyLang_<página>` (el patrón `t(id,es,en)` de `muApplyLang_juegos` sirve tal cual). |
| T-10 | 24412, 31342, 31365 | Toasts en español fijo: «Modo Examen Real — las soluciones salen al entregar», «Semestre actualizado», «Enlace copiado». (Los demás `_muToast` sí usan `_t()`/`en?`.) | media | `_muToast(window.curLang==='en'?'Real Exam Mode — solutions appear when you submit':'…')`; igual los otros dos. |
| T-11 | 15913, 15915 (CSS) | `content:'Examen '` y `content:'Código curso '` son texto fijo en ES; el workaround 15919–15920 los vacía en EN (bien), pero hay que mantenerlo y un lector de pantalla los lee como parte del nombre. | baja | Mover el texto al JS que rellena `#sidex-tipo-badge`/`#sidex-code` y borrar los `::before`. |
| T-12 | 35245 | Con `mu-lang=en` guardado, la app arranca en ES y llama `setLang(saved)` a los 300 ms: parpadeo de español (y `<html lang="es">`, `<title>` en ES) antes del cambio. | baja (**a verificar** visualmente) | Aplicar `document.documentElement.lang` y marcar un `data-lang` en el script del `<head>` (junto a 35) y llamar `setLang` en `DOMContentLoaded` sin `setTimeout`. |
| T-13 | 38–60 (`<head>`) | `<title>`, `description`, Open Graph y Twitter solo en ES; `og:locale` solo `es_CO`; no hay `hreflang`/`og:locale:alternate` aunque el sitio es bilingüe. Al ser SPA con hash, los rastreadores solo ven ES. | baja | Añadir `<meta property="og:locale:alternate" content="en_US">`; si se quiere SEO en EN haría falta ruta/URL distinta (decisión de producto). |
| T-14 | `404.html` (todo) | 404 solo en español; ignora `mu-lang` y `mu-theme` (`<html data-theme="dark">` fijo, así que el `@media (prefers-color-scheme:light)` con `:root:not([data-theme="dark"])` nunca aplica). | baja | Leer `localStorage` (`mu-lang`, `mu-theme`) en un script de 5 líneas y traducir 3 textos; quitar `data-theme="dark"` fijo. |
| T-15 | `simulacros-lab.html` (todo) | Prototipo público (no enlazado desde `index.html` ni en `sitemap.xml`, pero servido por GitHub Pages y sin `noindex`): 1 112 líneas, sin i18n, sin roles/`aria`/`alt`, `outline:none` en `.numin`. | baja | Moverlo fuera del sitio publicado o añadir `<meta name="robots" content="noindex">`; no vale la pena invertir i18n/a11y ahí. |
| T-16 | 23787, 35584 | (Fuera de alcance, pero visible) la tarjeta de resultado muestra `mathunal.co` y el `.ics` del calendario escribe `— mathunal.co`; el dominio es `mathunal.com`. | baja | Cambiar a `mathunal.com`. |

## 1.3 (c) Mezclas de idioma

Medido en ejecución sobre el contenido real.

| ID | Archivo:línea | Problema | Sev. | Arreglo sugerido |
|---|---|---|---|---|
| M-01 | `_EXAM_EN` 31580–31985, `_examEN` 31964 (usado p. ej. en 24608) | El enunciado de los exámenes en EN se «traduce» con una lista de 991 pares de reemplazo de palabras/frases. Cobertura insuficiente = **español-inglés mezclado**. Medido en las 542 preguntas: de **456 enunciados con texto, 210 (46 %) salen mezclados**, 245 limpios (muchos solo LaTeX), 1 sin cambio; resúmenes: 95/389 mezclados; opciones: 36/161; pasos: 26/183. Ejemplos reales: «Al realizar the operación … and simplificar, gives:», «El area of material for construirla (base + 4 lados, sin tapa) is minima cuando:», «In a curso, 30 estudiantes ven Cálculo, 25 ven Álgebra and 12 ven ambas. How many ven to the menos a of the dos?» Se ve también en el Diagnóstico gratis y en el simulacro. | **alta** | Dos pasos: (1) **ya**: que `_examEN` devuelva el original cuando quede español residual — ver **S3** (mejor un enunciado 100 % español, con aviso, que mezcla ilegible); (2) a medio plazo: campos `textoEn`/`opcionesEn`/`resumenEn` por pregunta (ya existen `body_en` en las soluciones Pro: `sim-solutions-en.dev.js`) y usar el diccionario solo como relleno. |
| M-02 | `_dictApply` 31987, `_docEN` 31988, `_DOC_EN` 37564–37640 | Los **nombres de archivo** se traducen con `split/join` **sin límites de palabra** y con reglas genéricas (`' de '→' of '`, `' y '→' and '`). Medido con un criterio conservador: **al menos 49 de 673 nombres salen mezclados** y hay un bug de subcadena: `['Potencia','Power']` rompe «Potenciación» → «**Powerción**». Ejemplos: «Class notes — 01. Teoría Intuitiva **of** Conjuntos», «Quiz 17 — Área **and** Perímetro **of** Figuras Planas…», «Worksheet 01 [Clases 1 **and** 2]», «Formula sheet **of** Integrals Múltiples **and** Calculus **en** Varias Variables». | **alta** | **S4**: motor con límites de palabra y la misma regla de retroceso que S3 (si queda español residual, mostrar el nombre original). Quitar las reglas `' de '/' y '/' e '` genéricas. Revisar `['Tema ','Version ']` (37625): «Tema 5» (tema = *topic*) no es «Version 5» (**a verificar** qué usan los archivos reales). |
| M-03 | 24195/24360 (`intro-sem`), 24443, `sim-teaser-price` 34119/34403 y `au-p0-i3`, `calc-*` | «Corte» entra en EN como préstamo en unos sitios («the 3 cortes», «by corte», «CORTE 1 (30%)», «Mock exam · Corte 1») y como «periods»/«Exam N»/«Exam period» en otros. Un estudiante que lee en inglés ve 3 términos para lo mismo. | media | Glosario único (ver D-07): p. ej. «exam period (corte)» la primera vez y «period» después; en datos de examen traducir `semestre` con regex `CORTE (\d)`→`PERIOD $1`. |
| M-04 | 31988–31990, `cm-l-*` 34390, `cat-tab2`, `wm-corte-l` | «Parcial» → «Midterm» (`_TYPE1_EN`, `_DOC_EN`), «Exams» (`cm-l-parciales`), «Solved Exams» (`cat-tab2`) y «Exam period»: cuatro traducciones de la misma palabra en una misma pantalla. | baja | Elegir «Midterms» para «Parcial N» y «Exams» solo para el genérico; propagar. |

## 1.4 (d) Traducciones incorrectas o poco naturales

(Claves de `LANG_EN`; línea = definición EN.)

| ID | Clave · línea EN | Actual (EN) | Problema | Sev. | Mejor |
|---|---|---|---|---|---|
| D-01 | `nmd-cal-s` · 34416 | «Cuts and key dates of the term» | «Cortes» ≠ *cuts*; «semestre» ≠ *term* aquí. Error de significado. | media | «Exam periods and key dates this semester» |
| D-02 | `ht-p` · 34407 | «…outlasted two **research stays**…» | ES dice «pasantías» (= internships). Cambia el significado. | media | «It outlasted two internships, a city move and a graduation.» |
| D-03 | `hero-sub` 34310, `cat-tab1` 34313 | «Workshops» | «Talleres» en la UNAL son guías de ejercicios; *workshop* es un evento. Además el mismo sitio usa «Worksheets» en 5 sitios. | media | «Worksheets» (o «Problem sets») en todos. |
| D-04 | `au-tab1` 34521, `au-p1-*`, `pm-tip` 34427, `pk-i2-s`, `pk-cmp-4`, `pk-desc` | «Monitor», «Monitor's tip», «Monitor's notes» | «Monitor» es colombianismo (auxiliar docente); en inglés es la pantalla. | media | «TA (monitor)» la primera vez; después «TA» / «TA's tip» / «TA notes». |
| D-05 | `nav-simulacros` 34305, `hero-btn2` 34311 | «Practice», «▶ Start Practice» | «Simulacros» se llama «Mock exams» en `cm-l-simulacros`, `sim-label`, `smap-*`. «Practice» en el menú principal no dice qué es. | media | «Mock exams» / «▶ Start a mock exam». |
| D-06 | `cp-con-3-d` 34378 vs `sim-teaser-pill` 34403 | «Automated SIDEX-format mock exams are **coming soon**» vs «6 questions · no sign-up · **available now**» | Contradicción de contenido en ambos idiomas (34094 «llega pronto» vs 34119 «ya disponible»). | media | Actualizar `cp-con-3-d` a presente. |
| D-07 | `calc-tab1…3` 34334, `calc-hdr-corte`, `calc-corte1…4`, `calc-need2…4` | «periods», «1st period», «You need on the 2nd period» | Gramática (*on the 2nd period* → *in*), y terminología distinta al resto (M-03). | baja | «You need on the 2nd exam period» / «grading period» + glosario. |
| D-08 | `nav-promedio` 34306 | «GPA» | «Promedio» ponderado ≠ GPA en el sentido en que lo entiende un estadounidense; el título de la página dice «Weighted average». | baja | «Average» (nav) / «Weighted average» (título). |
| D-09 | `sim-f-edo` 34320 | «ODE» | Jerga; los otros filtros sí se escriben («Differential Calc.»). | baja | «Diff. Eq.» |
| D-10 | `ht-h` 34406 | «From **borrowing** past exams at the copy shop to this» | ES: «rebuscar» (hunting around), no «pedir prestados». | baja | «From digging up past exams at the copy shop to this» |
| D-11 | `sp-hint` 34581 | «Tap when you're ready» | En escritorio es «Pulsa» (Space); «Tap» solo vale en móvil. | baja | «Press when you're ready» |
| D-12 | `hf-cta-note` / `sim-teaser-pill` / `faq-a1` | «No signup» / «no sign-up» | Dos grafías. | baja | «sign-up» (sustantivo) en todos. |
| D-13 | `prom-foot` 34517 | «PAES cap: 3.5» | Sigla sin glosa. | baja | «PAES (special admission) cap: 3.5» |
| D-14 | `hs-l2` 34582 vs `hero-sub` 34310 | «Solutions» vs «answer keys» | Dos nombres para el solucionario. | baja | «Solutions» o «Answer keys», uno. |

---

# 2. Accesibilidad

## 2.1 Contraste (WCAG 1.4.3 / 1.4.11) por tema

**Matriz de tokens** (razón mínima del token como texto sobre `--bg`/`--bg2`/`--card`/`--card2`; AA = 4,5 texto normal; ✗ = falla en al menos una superficie).

| Token | Azul (`dark`) | Negro | Gris | Claro |
|---|---|---|---|---|
| `--t1` | 13,7 | 16,9 | 6,7 ✓ | 16,5 |
| `--t2` | 6,6 | 6,6 | **3,4 ✗** (card2) / 4,0 (card) | 7,7 |
| `--t3` | 4,65 | **3,6 ✗** | **2,9 ✗** | 5,7 |
| `--acc` como texto | 4,47 ✗ (card2) | 5,5 | **2,1 ✗** | 5,6 |
| `--red` / `--bad` | ✓ | ✓ | **2,6 / 2,5 ✗** | `--red` 4,2 ✗ |
| `--grn`, `--ok`, `--yel`, `--warn` | ✓ | ✓ | **3,1–4,2 ✗** | 4,3–4,5 ✗ (bg2/card2) |
| `--gold` como texto | ✓ (8,1+) | ✓ | 3,8 ✗ | **1,6–1,9 ✗** |
| blanco sobre `--acc` (botones) | **3,36 ✗** | **3,36 ✗** | **3,36 ✗** | 6,5 ✓ |

**Resultado axe (9 rutas, estado por defecto, sin contar `#mu-dev-tab`):** nodos con contraste insuficiente → **Azul 43 · Negro 162 · Gris 600 · Claro 46**. Además ~330 nodos por tema «incompletos» (axe no puede decidir: contenido por `::before`/`::after`, glifos fuera de BMP, degradados) → **a verificar**, sobre todo los links del nav (`pseudoContent`).

| ID | Archivo:línea | Problema | Sev. | Arreglo sugerido |
|---|---|---|---|---|
| C-01 | 15350 `.btn-a`, 16272 `.btn-start`, 16117 `.qbtn.primary`, 17251 `.sim-pmode-b.on`, 25577 `.gc-btn`, `404.html` `a.btn`, botones inline `background:var(--acc);color:#fff` | **Botón principal: blanco sobre `#E8632A` = 3,36:1** en Azul, Negro y Gris (texto de 13–16 px negrita → exige 4,5). Es el CTA de casi todas las pantallas (Comenzar, Confirmar respuesta, Jugar, Explorar materias…). En Claro pasa porque `--acc` es `#A63A08`. Además, en `.gc-btn` con fondo verde (`jg-3-btn`, `jg-4-btn`) el blanco da 2,3:1. | **alta** | **S5**: `--acc-btn:#C2410C` (blanco = 5,18:1) para fondos de botón, o texto `#1A0B03` sobre `--acc` (5,72:1). Verde: texto `#052E16` sobre `#22C55E` (6,54:1). |
| C-02 | 14845–14861 (tema gris) | **El tema Gris falla AA de forma estructural**: 600 nodos. Sobre `--card`/`--card2` los textos secundarios (`--t2` `#B4B4C2`, 4,0/3,4), terciarios (`--t3`, 3,4/2,9), el naranja de marca como texto (2,4/2,1), verdes/rojos de estado (2,5–3,6) quedan por debajo. Ejemplos medidos: `.mu-fc-meta` (4,00), `.mc-arrow` «Ver material →» (2,43), `.cp-tag` (3,24), chips de materia en simulacro (3,31). No se arregla subiendo un token: las superficies son demasiado claras para esos acentos. | **alta** | **S6**: oscurecer superficies a `bg #292930 · bg2 #2F2F36 · card #35353D · card2 #3C3C44` (con eso `t1` 10,5 · `t2` 5,3 · `t3` 4,55 · `acc2` 4,9 · `grn` 5,9 · `yel` 6,6, probado) y ajustar `--red:#FB8192`, `--bad:#F98585`. Texto naranja → token nuevo `--acc-text`. |
| C-03 | 14863–14884 (tema negro) | `--t3:#6E6E6E` = 4,12:1 sobre `#000` y 3,6–3,8 sobre cards. 162 nodos (`.sidex-inst`, `.timer-label`, `.q-num-label`, `.sim-conf-lbl`, `.au-stat-l`, `.mc-tag-item`, `.mu-kpi-lbl`, `th`, pie de página…). | **alta** | `--t3:#7E7E7E` (4,54–5,17 en las 4 superficies, probado). |
| C-04 | 17258 `.sim-pw-tag`, 17268 `.sim-pw-price b`; otros `color:var(--gold)`: 15542, 15548, 19461, 19480, 19501 | Tema Claro: `--gold` (`#F0B429`) **como texto** sobre blanco/crema: `.sim-pw-tag` **1,86:1** (9,9 px) y el **precio del paywall `.sim-pw-price b` 1,73:1** (medido con axe). No hay override de `--gold` para claro. | **alta** | `html[data-theme="light"]{--gold-text:#8A5A00}` (5,5–5,9:1) y usar `color:var(--gold-text)` en esos selectores (el fondo/borde sigue con `--gold`). |
| C-05 | 20571 `#mu-version-badge` (`opacity:.7`, `var(--t2)`) | «MathUNAL v2 · © 2026»: 3,83 (claro), 3,45 (gris), 3,99 (negro). Texto informativo fijo en todas las pantallas de escritorio. | media | Quitar `opacity:.7` y usar `--t2`; o `aria-hidden="true"` si es decorativo (hoy también cae fuera de landmarks). |
| C-06 | 16897–16899, 18929 `.cp-j-step` (+ `opacity` en dark), `cp-j-title/desc` | Pasos «inactivos» del ciclo del parcial atenuados por `opacity`: texto a 1,5–3,7:1 en azul/negro/claro (título 2,3–3,7; descripción 1,5–2,5). Son contenido clicable, no controles deshabilitados. | media | Atenuar con color (`var(--t3)` sobre `--card`) en vez de `opacity`, manteniendo ≥ 4,5. **a verificar** si el diseño quiere que el paso inactivo sea «de fondo». |
| C-07 | CSS de `.sim-card-tipo` (inline `color:#E05D1A`), `data-col="#…"` en `.sim-prev-ico`, panic (`#ef4444`), `.cp-col-hd`, `.btn-panic` | Colores **hard-coded** que no respetan el tema: `#E05D1A` sobre blanco 3,65; `#ef4444` 3,76 (`.panic-l h4/p`); `.btn-panic` 4,29 en claro. | media | `color:var(--acc)`; rojo → `var(--bad)`; los `data-col` oscuros (`#1E3A8A`, `#BE123C`) sobre card oscura (1,5–2,6) → `color-mix(in srgb,var(--t1) 85%,transparent)` o usar la variante clara en dark. |
| C-08 | 17056 `.sim-free-teaser b`, 17097 `.sl-out b`, 17139 `.sim-prep-pred b` | `color:var(--acc2)` (`#FF7A3D` en claro = 2,4–2,6:1). axe no los vio en los estados probados. | media (**a verificar**) | `var(--acc)` en claro: `html[data-theme="light"] .sim-free-teaser b,…{color:var(--acc)}`. |
| C-09 | `.mc-sym` (símbolo grande de cada tarjeta de materia), `.diag-mat-sym`, `.smt-leaf-badge` | Dark: `.mc-sym` `#1F2D4A` sobre card = 1,21:1 (ornamental, 5 nodos); `.diag-mat-sym`/«Popular» `#E8632A` sobre `--card2` = 4,46:1 (0,04 de fallo). | baja | Ornamentales → `aria-hidden="true"` (WCAG los exime si son decoración pura); los de 4,46 → `var(--acc2)`. |
| C-10 | `#mu-dev-tab` | (solo dev) 2,3:1. | — | Fuera de producción; ignorar. |

## 2.2 Nombre, rol y estado (botones, formularios, ARIA)

| ID | Archivo:línea | Problema | Sev. | Arreglo sugerido |
|---|---|---|---|---|
| N-01 | 24606 | `.q-opt` (opciones de respuesta) lleva `role="button" aria-label="Opción A"`: el `aria-label` **sustituye al contenido**, así que un lector de pantalla anuncia solo «Opción A», no la opción (que es una fórmula). Además es ES fijo y los botones no comunican «seleccionada». | **alta** | **S7**: `role="radiogroup" aria-labelledby="q-text"` en `#q-options`, cada opción `role="radio" aria-checked="false"` **sin** `aria-label`; el nombre sale del contenido (`.q-opt-circle` + texto). Para la fórmula KaTeX usar el MathML que ya genera (`.katex-mathml`) como nombre. |
| N-02 | 21621–21642 (HTML), 31235 (`toggleFaq`) | FAQ: `<div class="faq-q" onclick>`: no entra en el orden de tabulación, sin rol ni `aria-expanded`. Con teclado/lector las 4 preguntas son inaccesibles. | **alta** | **S8**. |
| N-03 | 27998, 28049 | Diagnóstico gratuito: `div.momento-card` ×3 y `div.diag-mat-card` ×11 con `onclick`: **no se puede completar con teclado**. | **alta** | `<button type="button" class="diag-mat-card" aria-pressed="false">` y en `_diagPickMateria/_diagPickMomento` `aria-pressed` ↔ `.sel`. |
| N-04 | 30534 | Formulario: 58 `div.item onclick="sel(i)"` (toda la lista de fórmulas) sin foco ni rol; y `#vf-items` (28538) es una región con scroll sin foco (axe `scrollable-region-focusable`). | **alta** | `<button class="item" aria-current="true">` (o `role="option"` en un `listbox` con flechas) y `tabindex="0"` + `role="region" aria-label` en `#vf-items` si queda como contenedor. |
| N-05 | 37673 | Materia: 56 filas `div.mu-fc onclick="window.open(…)"` (cada PDF) no son enlaces: no se pueden abrir con teclado ni abrir en pestaña nueva con el menú contextual. | **alta** | Renderizar `<a class="mu-fc" href="URL" target="_blank" rel="noopener">…</a>` (ya se hace así en `.mu-ruta-file`, 37161). |
| N-06 | 20627 | `<div role="menu">` con hijos `<a>` sin `role="menuitem"`: axe `aria-required-children` **crítico**. El patrón real es *disclosure* (botón + lista de enlaces). | **alta** | Quitar `role="menu"` (y `aria-haspopup="true"` del botón, 20626). |
| N-07 | 36351 (`aria-label="Cuenta"`), 36329/36341 (texto visible) | El botón de cuenta tiene `aria-label="Cuenta"` pero su texto visible es «Guardar progreso» / «Mi cuenta». **WCAG 2.5.3 (Label in Name)** — usuarios de reconocimiento de voz dicen «Guardar progreso» y no funciona; axe `label-content-name-mismatch` serious en 8/9 rutas. También ES fijo en EN. | **alta** | Quitar el `aria-label` del `innerHTML` de 36351 (el texto basta) o asignar el mismo texto en `paintOne()`. |
| N-08 | 30458 (`#speed-sel`), 23538 (`#sim-onb-fecha`) | `<select id="speed-sel">` sin nombre accesible y `<input type="date" id="sim-onb-fecha">` sin etiqueta (axe **critical**). | **alta** | `aria-label="Velocidad de animación"` / `aria-label="Fecha de tu parcial"` (con claves ES/EN). |
| N-09 | 22478 | Botón de borrar fila: `title="Eliminar" aria-label="Cerrar"` — el nombre accesible es «Cerrar» (no cierra nada: elimina una materia). | media | `aria-label="Eliminar materia"`. |
| N-10 | 36096, 23710 | `role="dialog" aria-modal="true"` **sin nombre** (axe `aria-dialog-name` serious) en el modal de cuenta y el paywall; en el de cuenta las `<label class="mu-auth-lb">` (36110, 36117) no están asociadas al `<input>` (sin `for`/`id`). | media | `aria-labelledby` apuntando al título; `<label for="mu-auth-em">`. Devolver el foco al botón que abrió el modal al cerrar. |
| N-11 | todo el archivo | **0** usos de `aria-pressed`, `aria-selected`, `aria-current`, `role="tab"`. Los estados «activo» (idioma `#btn-es/#btn-en`, temas `#th-*`, `.au-tab`, `.calc-tab`, `.cat-tab`, `.sim-filter`, `.mu-exp-fbtn`, `.cpill`) existen solo como clase CSS `.on`. | media | Alternar `aria-pressed` donde se toggle `.on` (botones de filtro/tema/idioma) o `role="tablist/tab"` + `aria-selected` donde sean pestañas (`.au-tab`, `.calc-tab`). |
| N-12 | 20584, 26100, 23974–23980, 31346 | Los 3 sistemas de toast (`#toast-container`, `#toast`, `#mu-toast`) no son regiones vivas: ningún lector anuncia «Enlace copiado», «Marca quitada», etc. (WCAG 4.1.3). | media | `role="status" aria-live="polite"` en los contenedores (crear el contenedor una sola vez, vacío, y luego rellenarlo). |
| N-13 | 20605 | `<main id="mu-app" role="main" aria-live="polite">`: cada navegación reemplaza todo el `innerHTML` (incluido el `<nav>` y el pie) dentro de una región viva → riesgo de que se lea la página entera en cada cambio. Además `role="main"` es redundante. | media (**a verificar** con lector) | Quitar `aria-live`; anunciar el cambio con una región viva aparte (`#mu-route-announcer`, `role="status"`) y mover el foco al `<h1>` (ver F-05). |
| N-14 | 20578 | `<div id="mu-scrollnav" aria-label=…>` sin rol: `aria-label` no está soportado en un `div` genérico (axe `aria-prohibited-attr`). | baja | `role="group"`. |
| N-15 | materia (tpl-materia, 23386–23466 + JS) | La página de materia no tiene `<h1>` (axe `page-has-heading-one`, 2 rutas). | baja | `<h1>` con el nombre de la materia (hoy es un `div`). |
| N-16 | 20738, 25876, 25934, 25973, 26012 | `<canvas>` sin nombre ni `aria-hidden`: el del héroe (20738) es decorativo; los 4 de juegos son contenido visual sin alternativa. | baja | Héroe: `aria-hidden="true"`; juegos: `role="img" aria-label="Juego Rebota: …"` y avisar en la tarjeta que no hay modo accesible. |

**Imágenes (alt):** 4 `<img>` en `index.html` (21489, 21498, 21594, 21598), las 4 con `alt` (solo falta traducirlos: T-07). 0 `<img>` en `404.html` y `simulacros-lab.html`. Las figuras SVG de preguntas llevan `role="img" aria-label` (en español fijo, por la misma razón que M-01).

## 2.3 Orden de tabulación y foco

| ID | Archivo:línea | Problema | Sev. | Arreglo sugerido |
|---|---|---|---|---|
| F-01 | 15190–15201 (`#mob`), 20723 | El menú móvil cerrado está **desplazado con `transform:translateX(100%)` pero sigue en el orden de tabulación**: `Tab` pasa por sus 9 enlaces (fuera de pantalla, x=1302) justo después de «Ajustes», en escritorio y en móvil (medido: 9 paradas invisibles; en móvil el primer enlace queda en x=412 > 390). | **alta** | **S9**: `#mob{visibility:hidden;transition:transform .32s…,visibility 0s .32s} #mob.open{visibility:visible;transition-delay:0s}` (y `inert` mientras esté cerrado). |
| F-02 | 16806–16817, 20578–20580 | `#mu-scrollnav` (`opacity:0; pointer-events:none` hasta hacer scroll) mantiene sus 2 botones en el orden de tabulación: **2 paradas invisibles** justo tras el skip link (foco desaparece). | **alta** | `#mu-scrollnav:not(.show){visibility:hidden}` o `inert`; mostrarlo también con `:focus-within`. |
| F-03 | 20574, 20605 | **El skip link no salta nada**: su destino `#mu-app` es el `<main>`, que **contiene el `<nav>`** (cada plantilla empieza con `<nav>`), y no es enfocable. Medido: tras `Enter` el foco sigue en el skip link y el siguiente `Tab` va a `#mu-goup`. (WCAG 2.4.1). | **alta** | Marcar el contenido: `<div id="mu-content" tabindex="-1">` justo después del `<nav>` en cada plantilla (o mover el `<nav>` fuera de `#mu-app`) y apuntar el skip link allí; en `_loadPage` (≈30780) hacer `document.getElementById('mu-content').focus({preventScroll:true})` tras inyectar. |
| F-04 | 17811, 17910, 19247–19250 | **Foco invisible** en `#vf-mat` (filtro de materia del Formulario) y `#speed-sel` (velocidad de animación): `outline:none` con mayor especificidad que `:focus-visible`, y el único indicador es `box-shadow:0 0 0 3px rgba(232,99,42,.12)` (12 % alfa ≈ 1,1:1). La regla `.vf-shell #vf-mat:focus{border-color:var(--acc)}` tampoco llega a aplicarse (borde sin cambio en el cómputo). Verificado con captura: con y sin foco son idénticas. 4 temas. | **alta** | Borrar `outline:none` de 17811 y 17910; añadir `.vf-shell select:focus-visible{outline:2px solid var(--acc);outline-offset:2px}`. |
| F-05 | 30780–30800 (`_loadPage`) | Al navegar con teclado (p. ej. `Enter` en «Fórmulas»), la plantilla se reinyecta y `document.activeElement` pasa a `<body>`: el usuario pierde su posición y no se anuncia la página nueva (medido). | media | Tras inyectar: `app.querySelector('h1,[tabindex="-1"]')?.focus({preventScroll:true})` y actualizar un `role="status"` con el título (`document.title` ya cambia). |
| F-06 | 14917 (`:focus-visible`), tema gris | El anillo de foco (`2px solid var(--acc)`) en el tema Gris tiene 2,1–3,2:1 contra las superficies → < 3:1 (1.4.11) sobre `--card`/`--card2`. | media | Se arregla solo con S6 (superficies más oscuras → 3,25–4,3:1) o usando `outline-color:var(--acc-text)` en gris. |
| F-07 | 15287 (`#cmd-input`), 15574, 16420, 17394, 17723, 17801, 18398, 19069 | Campos de búsqueda con `outline:none` dentro de contenedores; la mayoría tiene `:focus-within` (15573, 17392, 17722, 17800, 19068) pero `#cmd-input`, `.search-inp` (16420) y `.mu-search-input` (18398) **no**. | baja (**a verificar**) | `#cmd-input-wrap:focus-within`, `.search-inp:focus-visible`, etc. (o dejar el outline global). |
| F-08 | todo el archivo | `tabindex` positivo: **ninguno** (bien). `inert`: ninguno (relacionado con F-01/F-02). Recorrido home en Azul: logo → nav → Más → Cuenta → Ajustes → [9 invisibles de `#mob`] → contenido; sin saltos hacia atrás. | — | — |

## 2.4 Objetivos táctiles (< 44 px, móvil 390×844)

Medidos como caja del elemento (WCAG 2.5.8 exige ≥ 24 px; 2.5.5 AAA y las guías de plataforma, 44 px). **Todos los de abajo están < 44 px;** los marcados † están además < 24 px.

| ID | Archivo:línea (CSS) | Elementos / tamaño medido | Sev. | Arreglo sugerido |
|---|---|---|---|---|
| H-01 | 18521–18525 `.mu-exp-fbtn/.mu-exp-sbtn` | Filtros y orden en materia: 55–98 × **23–24** px † | media | `min-height:44px` en móvil o `padding:.7rem 1rem`. |
| H-02 | 17875 `.tb-btn`, 17902 `.vbtn`, `#anim-btn`, 17897 `.param-slider` | Barra de gráfica del Formulario: **30×23 †**, 57–89×25–26 †, slider **59×16 †**, `input.param-num` 56×31 | media | Zona táctil 44 px (padding o pseudo-elemento ampliado). |
| H-03 | 17184 `.sim-mat-pick-skip` | «Ver todas» 62×**21** † | media | `padding:.8rem 1rem`. |
| H-04 | 16818 `#mu-scrollnav button` | Botones ir arriba/abajo **22×36** † | media | Ancho ≥ 44. |
| H-05 | 36221 `.mu-acct-btn`, 15148 `.settings-btn`, 15175 `.burger` | Cuenta 36×**28**, Ajustes 34×34, menú 38×38 (cabecera, en todas las páginas) | media | `min-width/height:44px` en `@media(pointer:coarse)`. |
| H-06 | 17291 `.sim-onb-chip`, 18659 `.sim-tipo-pill`, 18666 `.sim-view-tog` | Chips de simulacro: 127–287 × **27–29** | baja | `min-height:44px` en `pointer:coarse`. |
| H-07 | 16617 `.smt-leaf`, `.smap-quick-btn` | Mapa del sitio: 268×**29**, 117–149×37 | baja | idem |
| H-08 | 18775 `.au-tab`, `#cpb-*` (18919), `.cp-j-switch`, `#mu-rc-mat-sel`, inputs de la calculadora (`.calc-inp`, `.prom-inp`) | 34–36 px de alto | baja | idem |
| H-09 | 16347 `.mat-nav-back`, `.logo`, `.mu-rel-chip` 18350, `.dbtn-s` 17921, `.gc-btn` 25577 | 80×35, 155×34, 147–193×35, 124–142×33, 116×35 | baja | idem |
| H-10 | 16755 `.fab-wa`, `.prom-del` 16954, `.prom-inp` 16951 | 40×40, 40×40, inputs 36 px | baja | 44 px. |
| H-11 | (enlaces dentro de texto) | «Privacidad» 96×19 y similares en el pie | baja | Los enlaces en línea quedan exentos de 2.5.8; aun así, `padding-block:.5rem`. |

No hay desbordamiento horizontal real a 390 px (`body{overflow-x:hidden}`; los `scrollWidth` altos que vi en una ruta son de elementos `fixed`, **a verificar**).

## 2.5 `prefers-reduced-motion` (WCAG 2.3.3 / 2.2.2)

Bien: regla global en 18996–18998 (`animation-duration:.01ms`, `iteration-count:1`, `transition-duration:.01ms`) + ~15 reglas específicas. **No cubre:**

| ID | Archivo:línea | Problema | Sev. | Arreglo sugerido |
|---|---|---|---|---|
| R-01 | 14758, 14777, 19127 (`html`/`*{scroll-behavior:smooth}`) y 13 llamadas JS (20579, 20580, 21823, 22944, 23129, 24548, 30478, 30718, 30743, 30869, 32584, 33901, 33917) | El scroll suave se aplica siempre: la regla global **no** pone `scroll-behavior:auto`, y solo 1 de las 13 llamadas JS (24548, que lee `matchMedia` en 24547) lo respeta. Incluye el scroll animado de cada cambio de ruta/ancla y el de foco por teclado. | media | **S10**. |
| R-02 | 22330–22349 (`runCounters`), 37775–37800 (esfera 2D del héroe), 37883 (visor 3D), 30232–30332 (animación de fórmulas), 26811 / 27003 (juegos) | Animaciones dirigidas por `requestAnimationFrame` (contadores que cuentan hacia arriba, esfera wireframe que rota sin parar detrás del héroe, visor 3D): el CSS de reduced-motion no las alcanza. El héroe se mueve indefinidamente (2.2.2: > 5 s sin control de pausa). Los juegos son movimiento esencial (exentos). | media | `var RM=matchMedia('(prefers-reduced-motion: reduce)'); if(RM.matches){ el.textContent=target… ; return; }` en contadores; pintar un solo frame de la esfera; autoplay del visor 3D en pausa. |
| R-03 | 18996 (`*{…}`), 18438 `.mu-si-cur::after`, 28402 `.ab-dot::after` (infinite), 16528 `.pack-v2-card::after` | `*` **no selecciona pseudo-elementos**; las animaciones infinitas sobre `::before/::after` solo se frenan si tienen regla propia (varias sí: 15355, 17082, 19450…). Sin regla: `muPulse` (18438) y `abPulse` (28402). | baja (**a verificar** cuáles se ven) | `*,*::before,*::after{…}` en la regla global. |
| R-04 | 404.html `a.btn:hover{transform}` | Transición menor sin `reduce`. | baja | Opcional. |

## 2.6 Snippets de arreglo

**S1 — mensajes de calculadora (T-01)**
```js
function _t(es,en){ return window.curLang==='en' ? en : es; }
// 22278 / 22307 / 22323:
m.textContent=_t('Los pesos deben sumar 100%. Suma actual: '+suma+'%.',
                 'Weights must add up to 100%. Current sum: '+suma+'%.');
// 22287:
m.textContent=_t('Ingresa los datos para calcular','Enter the data to calculate');
// calcResult 22289–22296:
needed<=0 → _t('Ya pasas sin importar lo que saques. Relájate (un poco).','You pass no matter what you score. Relax (a little).')
needed>5  → _t('Necesitarías '+n+' en una escala que llega a 5.0 — con estas notas no da matemáticamente. Piensa en cancelar la materia o hablar con tu director de carrera.',
               'You\'d need '+n+' on a scale that tops out at 5.0 — with these grades the math doesn\'t work. Consider withdrawing or talking to your program director.')
<=2.5     → _t('Fácil. Lo tienes. No seas confiado igual.','Easy. You\'ve got this. Don\'t get overconfident, though.')
<=3.5     → _t('Alcanzable. Estudia bien estos días.','Doable. Study well these days.')
<=4.5     → _t('Va a ser difícil, pero no imposible. Enfócate.','It\'ll be tough, but not impossible. Stay focused.')
else      → _t('Necesitas casi perfecto. Activa el Modo Pánico.','You need a near-perfect score. Switch on Panic Mode.')
```
Además, si el usuario cambia de idioma con un resultado ya calculado, el mensaje queda en el idioma anterior hasta que vuelva a teclear: llamar `calc2()/calc3()/calc4()` al final del bloque `/* CALCULADORA */` de `setLang` (la función correspondiente a la pestaña activa).

**S2 — pantalla de pregunta del simulacro (T-03)**
```js
// 24553
ctr.textContent=(en?'Question ':'Pregunta ')+(idx+1)+(en?' of ':' de ')+nq;
// 24564
lbl.textContent=q.tipo==='mcq'?(en?'Multiple choice, single answer':'Selección múltiple con única respuesta')
              :q.tipo==='numerica'?(en?'Numeric answer':'Respuesta numérica'):(en?'Open-ended question':'Pregunta de desarrollo');
// botones 23688–23691 y 24674 → asignar en muApplyLang_simulacro (23817):
T('#btn-prev','← Anterior','← Previous'); T('#btn-next','Siguiente →','Next →');
T('#btn-flag','Marcar para revisar','Flag for review'); T('#btn-check','Confirmar respuesta','Check answer');
```
(`var en=(window.curLang==='en')` al inicio de la función de 24553.)

**S3 — que `_examEN` no produzca mezclas (M-01)**
```js
var _ES_LEFT=/(^|[^A-Za-zÀ-ÿ])(el|la|los|las|de|del|que|para|con|una|un|por|se|en|y|o|cuando|valor|función|ecuación|sea|dada|entonces)(?![A-Za-zÀ-ÿ])|[áéíóúñ¿¡]/i;
function _plain(s){ return s.replace(/\$\$[\s\S]*?\$\$|\$[^$]*\$|<[^>]+>/g,' '); }
function _examEN(s){
  if(window.curLang!=='en') return s;
  var orig=String(s==null?'':s), out=/* …lógica actual… */;
  return _ES_LEFT.test(_plain(out)) ? orig : out;   // si quedó español, mostrar el original completo
}
```
(Con esto 210 enunciados pasan de mezcla a español completo; mostrar un aviso «Enunciado en español (idioma original del parcial)» y envolver en `<span lang="es">` para lectores.)

**S4 — `_dictApply` con límites de palabra (M-02)**
```js
var _DRE={};
function _dictApply(s,d){
  var orig=String(s==null?'':s), out=orig;
  for(var i=0;i<d.length;i++){
    var k=d[i][0];
    var re=_DRE[k]||(_DRE[k]=new RegExp('(^|[^A-Za-zÀ-ÿ])'+k.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')+'(?![A-Za-zÀ-ÿ])','g'));
    out=out.replace(re,function(m,p){ return p+d[i][1]; });
  }
  return _ES_LEFT.test(out) ? orig : out;   // misma red de seguridad que S3: si quedó español, mostrar el nombre original
}
```
(`_ES_LEFT` es el regex de S3; definirlo una vez arriba de `_EXAM_EN`. Borrar además las reglas genéricas `' de '`, `' y '`, `' e '`, `' de la '`, `' del '` de la lista `_DOC_EN` (línea 37639): son las que generan «Teoría **of** números». Las reglas con espacio final, como `'Semana '`, siguen funcionando con este motor porque el espacio hace de límite.)

**S5 — botones con contraste suficiente (C-01)**
```css
:root{ --acc-btn:#C2410C; }                       /* blanco sobre #C2410C = 5,18:1 */
html[data-theme="light"]{ --acc-btn:var(--acc); } /* #A63A08 ya da 6,5:1 */
.btn-a,.btn-start,.qbtn.primary,.sim-pmode-b.on,#sim-pw-pay{ background:var(--acc-btn); color:#fff; }
.gc-btn{ background:var(--gc,var(--acc-btn)); }          /* respeta el color por juego (--gc) */
.gc-btn[style*="var(--grn)"]{ color:#052E16; }          /* verde de estado: texto oscuro (6,5:1) */
```

**S6 — tema Gris (C-02)** (todas las combinaciones medidas ≥ 4,5:1)
```css
html[data-theme="gray"]{
  --bg:#292930; --bg2:#2F2F36; --card:#35353D; --card2:#3C3C44;
  --red:#FB8192; --bad:#F98585;           /* t1 10,5 · t2 5,3 · t3 4,55 · acc2 4,9 · grn 5,9 · yel 6,6 · ok 4,8 */
}
:root{ --acc-text:#FF9A6B; }                 /* texto naranja ≥ 5,25:1 en gris; ≥ 7,2 en azul y negro */
html[data-theme="light"]{ --acc-text:var(--acc); }
.cp-tag,.mc-arrow,.sidex-sub,.intro-badge,.smt-leaf-badge,.cp-j-action{ color:var(--acc-text); }
```
Negro (C-03): `html[data-theme="black"]{ --t3:#7E7E7E; }`.

**S7 — opciones del simulacro (N-01)**
```html
<div id="q-options" role="radiogroup" aria-labelledby="q-text">…</div>
<div class="q-opt" role="radio" aria-checked="false" tabindex="0"> <!-- sin aria-label -->
```
(En el handler de selección: `aria-checked` ↔ `.selected`, y roving `tabindex` con ←/→ si se quiere el patrón completo.)

**S8 — FAQ accesible (N-02)**
```html
<h3><button class="faq-q" aria-expanded="false" aria-controls="faq-a1">¿El material es gratuito? <span class="faq-ico" aria-hidden="true">+</span></button></h3>
<div class="faq-a" id="faq-a1" role="region" hidden>…</div>
```
```js
function toggleFaq(btn){ var item=btn.closest('.faq-item'), open=!item.classList.contains('open');
  document.querySelectorAll('.faq-item.open').forEach(function(e){ e.classList.remove('open'); e.querySelector('.faq-q').setAttribute('aria-expanded','false'); });
  if(open){ item.classList.add('open'); btn.setAttribute('aria-expanded','true'); } }
```
(`.faq-q{background:none;border:0;width:100%;text-align:left;font:inherit;color:inherit}`; `hidden` se quita/pone con la clase `.open` o se mantiene el CSS actual de `.faq-item.open .faq-a`.)

**S9 — menú móvil cerrado fuera del orden de tabulación (F-01)**
```css
#mob{ visibility:hidden; transition:transform .32s cubic-bezier(.22,1,.36,1), visibility 0s linear .32s; }
#mob.open{ visibility:visible; transition-delay:0s; }
#mu-scrollnav:not(.show){ visibility:hidden; }
```

**S10 — reduced motion (R-01…R-03)**
```css
@media (prefers-reduced-motion:reduce),(update:slow){
  html,*{ scroll-behavior:auto !important; }
  *,*::before,*::after{ animation-duration:.01ms !important; animation-iteration-count:1 !important; transition-duration:.01ms !important; }
}
```
```js
window.muSmooth=function(){ return matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth'; };
// y en las 13 llamadas: behavior: window.muSmooth()
```

---

# 3. Resumen — lo más urgente (≤ 10 líneas)

1. **Simulacro y Diagnóstico en inglés no son legibles:** 46 % de los enunciados (210/456) salen en spanglish (`_examEN`, 31964) y 49 nombres de archivo también, incluido «Powerción» (M-01, M-02). Cortar el reemplazo parcial con S3/S4 y, a medio plazo, traducir por pregunta.
2. **Calculadoras de la home en EN responden en español** (T-01, T-02) y la pantalla de pregunta del simulacro está medio en ES (T-03).
3. **Teclado/lector de pantalla:** FAQ, Diagnóstico, lista de Fórmulas y filas de PDF en Materia son `div` con `onclick` (N-02…N-05); opciones del simulacro nombradas solo «Opción A» (N-01).
4. **Orden de tabulación:** 11 paradas invisibles (menú móvil `#mob` y `#mu-scrollnav`, F-01/F-02), skip link que no salta nada (F-03), foco perdido al cambiar de ruta (F-05), foco invisible en `#vf-mat`/`#speed-sel` (F-04).
5. **Contraste:** el botón principal (`#fff` sobre `#E8632A`) da 3,36:1 en 3 de los 4 temas (C-01); el tema Gris falla en 600 nodos (C-02) y Negro en 162 por `--t3` (C-03); el precio del paywall en tema Claro es 1,7:1 (C-04).
6. **Nombres accesibles que mienten:** botón de cuenta (`aria-label="Cuenta"` vs «Guardar progreso», N-07), borrar fila llamado «Cerrar» (N-09), `select`/`date` sin etiqueta (N-08), `role="menu"` mal usado (N-06).
7. **Táctil:** filtros de Materia (23–24 px), barra de gráfica del Formulario (hasta 16 px) y cabecera (Cuenta 28 px) por debajo de 44 px (H-01…H-05).
8. **Movimiento:** scroll suave siempre activo y animaciones JS (contadores, esfera del héroe) ignoran `prefers-reduced-motion` (R-01, R-02).
9. **Por dónde empezar (≈ 1 día):** S5 + S6 (CSS de contraste), S9 (CSS foco), S8/N-03/N-05 (cambiar `div` por `button`/`a`), S3/S4 (retroceso a ES) y un helper `_t(es,en)` para T-01/T-02/T-03/T-10.
10. Limpieza menor: 13 claves duplicadas y 55 huérfanas en `LANG_*`, `mathunal.co` en 2 sitios, `simulacros-lab.html` público sin i18n/a11y.
