# Videos de MathUNAL con Remotion

Un video es una página React que se renderiza cuadro por cuadro. Así las animaciones usan las mismas cifras y el mismo diseño que las lecciones.

## Qué hay
- `src/Cadena.tsx` es el video de 25 segundos de la regla de la cadena, con cinco escenas y subtítulos.
- `src/Root.tsx` registra dos formatos del mismo video, vertical de 1080 por 1920 para redes y horizontal de 1920 por 1080.
- `remotion.config.ts` apunta al navegador instalado en el entorno. Si se trabaja en otra máquina, hay que cambiar esa ruta o quitar la línea para que Remotion descargue el suyo.

## Cómo se usa
1. `npm install`
2. Ver un cuadro suelto con `npx remotion still cadena-vertical salida.png --frame=262`
3. Renderizar el video con `npx remotion render cadena-vertical salida.mp4 --codec=h264 --crf=20`

## Para hacer otro video
Copiar `Cadena.tsx`, cambiar los textos de `CAPS`, la función de la gráfica y las ecuaciones de las escenas. Las cifras deben salir de la lección, y conviene comprobarlas a mano antes de renderizar.

## Lo que falta
Los videos salen sin voz. La voz depende de resolver la cuota de ElevenLabs y de decidir si se clona la voz de Lucho. Tampoco llevan música, porque no hay una pista con licencia clara.
