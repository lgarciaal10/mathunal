# Reel v4 con HyperFrames

Segunda versión del reel de fracciones algebraicas, con un lenguaje visual oscuro, ecuaciones grandes, subtítulos por palabra, entrada de marca, indicador de capítulos, música y efectos de sonido.

- `gen4.py` parte de la composición v3 y la restyle: fondo oscuro con brillos y puntos, cámara lenta, entrada de marca de 2.8 s, subtítulos sin burbuja y barra de capítulos.
- `mkaudio.py` mezcla la voz (edge-tts) con una base musical sintetizada, efectos en los cambios de escena y bajada automática de la música cuando hay voz. Necesita numpy y scipy.
- `sfx.json` tiempos de los efectos, que escribe `gen4.py`.

Las rutas apuntan a la carpeta de trabajo de la sesión. Render con `npx hyperframes@0.9.40 render --quality looks`.
La voz sigue siendo sintética (edge-tts). Una voz humana o de ElevenLabs sube mucho la percepción de calidad.

## v5
- `tts.py` sintetiza cada frase por separado (es-CO-SalomeNeural, -8 %) y se une con pausas medidas, luego cadena de voz con filtro de graves, presencia, compresión y eco corto.
- Escenas bajadas para centrar el contenido, cuadrícula de la gráfica atenuada y duración ajustada a la voz nueva (121 s).
