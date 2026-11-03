#!/usr/bin/env python3
"""Construye una lección de un solo archivo HTML a partir de su JSON.

Uso
  python3 construir.py ../lecciones/calculo-limite-1.json salida.html
  python3 construir.py leccion.json salida.html --katex-inline katex-inline.css --doctype

Sin opciones el HTML enlaza KaTeX 0.16.9 desde jsdelivr (para el sitio). Con --katex-inline
incrusta ese CSS con sus fuentes (para un artifact o para abrir el archivo sin internet).
Con --doctype agrega <!doctype html> y la cabecera, para abrirlo directamente en el navegador.
"""
import sys, json, os, re
AQUI = os.path.dirname(os.path.abspath(__file__))
def leer(n): return open(os.path.join(AQUI, n), encoding="utf8").read()
def main():
    a = sys.argv[1:]
    if len(a) < 2: print(__doc__); sys.exit(1)
    datos, salida = a[0], a[1]
    inline = a[a.index("--katex-inline") + 1] if "--katex-inline" in a else None
    json.loads(open(datos, encoding="utf8").read())   # falla si el JSON no es válido
    cuerpo = leer("motor.body.html").replace("/*LECCION_JSON*/", open(datos, encoding="utf8").read().replace("</", "<\\/"))
    titulo = json.loads(open(datos, encoding="utf8").read())["titulo"]
    if inline:
        kx = "<style>" + open(inline, encoding="utf8").read() + "</style>"
    else:
        kx = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css" crossorigin="anonymous">'
    html = (f"<title>{titulo}</title>\n"
        '<meta name="claude:viewport-fit-sides" content="cover">\n'
        '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
        '<link href="https://fonts.googleapis.com/css2?family=Literata:ital,wght@0,400;0,600;0,700;0,900&family=Space+Grotesk:wght@300;400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">\n'
        f"{kx}\n<style>\n{leer('base.css')}\n{leer('motor.css')}\n</style>\n{leer('icons.svg')}\n{cuerpo}\n"
        '<script src="https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js" defer></script>\n'
        f"<script>\n{leer('base.js')}\n</script>\n<script>\n{leer('motor.js')}\n</script>\n")
    if "--doctype" in a:
        html = '<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover"></head><body style="margin:0">' + html + "</body></html>"
    open(salida, "w", encoding="utf8").write(html)
    print(salida, len(html), "bytes")
main()
