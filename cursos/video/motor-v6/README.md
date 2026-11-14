# Motor de transformación de ecuaciones (v6)

Reel de fracciones con cámara, símbolos que viajan en arco, anotaciones dibujadas y choque de factores. Se genera en cuatro formatos, 9x16, 16x9, 3x4 y 4x3.

1. `scenes6.py` define los estados LaTeX de cada escena.
2. `measure6.js` mide en un navegador real la posición de cada símbolo de KaTeX para cada estado y formato.
3. `gen6b.py` arma la composición de HyperFrames con `engine6.js` (el motor) y `style6t.css`. Usa la variable `FMT`.
4. `mkaudio6.py` mezcla voz, música y efectos.

El motor empareja los símbolos de un estado al siguiente con la subsecuencia común más larga, y acepta una lista de pares para forzar el emparejamiento. Las rutas apuntan a la carpeta de trabajo de la sesión.
