# Reel v3 con HyperFrames

Reel de fracciones algebraicas con estilo cuaderno, ritmo lento y voz pausada.

- `frases.txt` guion, una frase por línea.
- `wb.json` tiempos por palabra de la voz (edge-tts, es-CO-SalomeNeural, rate -6%).
- `kx-in.json` y `kx.js` expresiones LaTeX prerenderizadas con KaTeX.
- `gen3.py` arma `index.html` de un proyecto HyperFrames (GSAP, escenas con barrido, mascota que habla, burbuja de subtítulos).

Las rutas dentro de `gen3.py` apuntan a la carpeta de trabajo de la sesión y hay que ajustarlas. Render con `npx hyperframes@0.9.40 render --quality looks`.
