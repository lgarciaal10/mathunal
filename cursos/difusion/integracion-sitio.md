# Notas para llevar los cursos al sitio real

Estas notas no cambian nada del sitio. Son el mapa de lo que hay que decidir y hacer cuando quieras mover las 158 lecciones a mathunal.com. Cada decisión que depende de ti está marcada con la etiqueta Decide Lucho.

## Qué se sabe del sitio hoy

El sitio es estático. Tiene `CNAME`, `404.html`, `sitemap.xml`, `robots.txt`, un service worker en `sw.js` y una carpeta `supabase`. El service worker dice en su propio encabezado que el HTML siempre se pide a la red y que los archivos estáticos usan stale-while-revalidate. Eso encaja bien con lecciones que son una sola página HTML.

Cada lección ya es un archivo HTML autónomo, con el motor, los estilos y KaTeX en línea. No necesita servidor para funcionar.

## Por qué vale la pena moverlas

La razón principal es el progreso. Hoy las lecciones viven en direcciones distintas dentro de claude.ai, y el navegador guarda los datos por dominio. Por eso el cuaderno de errores, la lectura de seguridad al responder y el avance de cada persona no se pueden compartir entre lecciones. Bajo un solo dominio sí. Es la ganancia más grande y no cuesta nada de diseño.

La segunda razón es el control. Con las lecciones en tu dominio decides la dirección, el formato de los enlaces y qué se indexa en buscadores.

## Pasos propuestos, en orden

1. Elegir la ruta. Una opción simple es `mathunal.com/cursos/` para el hub y `mathunal.com/cursos/<materia>/<tema>.html` para cada lección. Decide Lucho.
2. Copiar los 158 HTML construidos a esa ruta. Salen de `cursos/plantilla/construir.py`, uno por lección.
3. Cambiar los enlaces del hub, del Estudio y del Formulario. Hoy usan direcciones de claude.ai que viven en los diccionarios de `hub/build-hub.py` y `estudio/build-estudio.py`. Hay que reemplazarlos por rutas relativas y reconstruir las tres páginas.
4. Subir el número de `CACHE` en `sw.js`, como pide su propio comentario, para que nadie quede con una versión vieja.
5. Agregar las URL nuevas a `sitemap.xml` si quieres que se indexen. Decide Lucho.
6. Probar en un celular real y en Safari antes de publicar, que es lo que todavía no está probado.

## Lo que hay que revisar antes de publicar

El motor de las lecciones usa KaTeX incluido en cada archivo, así que no depende de una red externa. Aun así hay que comprobar cómo se comporta con la política de contenido del dominio real, si tiene una.

El motor guarda datos en `localStorage` bajo las claves `mu-errores` y `mu-confianza`. Eso no choca con nada conocido del sitio, pero conviene revisar que `index.html` y las páginas de simulacros no usen esas mismas claves.

La carpeta `supabase` y el archivo `sim-pro-schema.sql` indican que el sitio ya guarda datos de simulacros. Las lecciones no hablan con Supabase. Si quieres medir uso real, el widget de `feedback.js` está pensado para eso, y se explica en `instrumento-utilidad.md`.

## Cosas que dejo sin tocar a propósito

El PR 12, el de lo legal, sigue sin fusionar. Si mueves los cursos antes de eso, conviene que el aviso legal y la política de datos queden publicados primero, porque el widget de utilidad y el cuaderno de errores sí guardan datos en el navegador de la persona.

La limpieza de SQL en Supabase y la dirección de pago de Wompi también quedan como estaban. No hay nada en los cursos que dependa de ellas.

## Estado honesto

Nada de esto se probó en el dominio real, porque no se ha publicado nada ahí. Lo que sí está probado es que las lecciones se abren y funcionan como archivos sueltos en Chromium, en escritorio y en ancho de celular emulado. No se probó en Safari, en Firefox ni en un teléfono físico.
