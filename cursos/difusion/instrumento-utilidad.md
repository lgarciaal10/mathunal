# Cómo saber si las lecciones sirven

Hoy las 158 lecciones están escritas y verificadas por dentro, pero ninguna persona real las ha usado. Eso es lo más importante que falta. Este documento propone una forma sencilla de averiguar si ayudan, sin prometer nada que no se pueda medir.

## Qué se quiere saber

1. Si la persona entendió algo que antes no entendía.
2. Dónde se atasca, tema por tema.
3. Si vuelve, que es la señal más honesta de utilidad.

## Primera fase, con cinco a ocho estudiantes

Antes de medir con números, conviene mirar a unas pocas personas usando la lección. Es lo que más rápido encuentra problemas.

Cómo hacerlo. Se le pide a cada estudiante que abra una lección de un tema que le toque en este momento, y que piense en voz alta mientras la usa. Quien observa no explica ni ayuda, solo anota dónde se detiene, dónde se confunde y dónde se aburre. Treinta minutos por persona alcanzan.

Qué anotar por persona.
- Qué modo usó, Ver, Leer o Practicar, y cuál dejó a la mitad.
- En qué ejercicio falló más de una vez.
- Qué palabra o símbolo no entendió.
- Si llegó al simulacro y qué le pareció.
- Qué haría distinto si fuera suya la lección.

Con cinco personas ya aparecen los problemas que se repiten. Si tres de cinco se atascan en el mismo punto, ese punto se arregla antes de seguir.

Esta fase no la puede hacer Claude, porque necesita personas reales. Lo que sí queda listo es la lista de preguntas de arriba.

## Segunda fase, con el widget de utilidad

El archivo `feedback.js` agrega al final de cada lección una pregunta, ¿te sirvió esta lección, con tres respuestas, sí, más o menos y no. Si la respuesta no es un sí, pide una razón entre cinco opciones, como no entendí la explicación o los ejercicios me quedaron difíciles. Eso es todo, tres toques como máximo.

Decisiones de diseño.
- No pide nombre, correo ni ningún dato personal.
- Guarda un identificador aleatorio solo en el navegador, para no contar dos veces a la misma persona.
- Por defecto no envía nada a ningún servidor. Las respuestas quedan en el navegador hasta que se configure un destino propio.
- Funciona sin conexión a servicios externos.

Cómo se activa. Se incluye el archivo en la lección, se llama `MathunalFeedback.init` con el nombre de la lección, y si se quiere recoger las respuestas se define antes `window.MATHUNAL_FEEDBACK_URL` con un endpoint que acepte POST con JSON. Cada respuesta llega como un objeto con identificador, lección, valor, motivo y hora.

Qué se probó. Se verificó en Chromium que los botones aparecen, que el flujo de no me sirvió pide la razón, que la respuesta queda guardada en el navegador y que se envía por POST a un servidor local de prueba. No se probó en Safari ni en celular físico, y no se conectó a ninguna base de datos real.

Importante. Esto solo funciona cuando las lecciones estén en el dominio propio. Dentro de las páginas publicadas como artefactos de claude.ai el navegador bloquea el envío a otros servidores, así que allí solo se guardaría local.

## Qué mirar en los números

Con unas cien respuestas ya se pueden mirar tres cosas.

1. El porcentaje de sí por lección. Una lección con muchos más no que el resto es la primera candidata a revisar.
2. El motivo más frecuente entre los que no dijeron sí. Si domina no entendí la explicación, el problema es de redacción. Si domina los ejercicios me quedaron difíciles, el problema es de dificultad o de pistas.
3. Cuántas personas vuelven a otra lección en la misma semana. Es la señal que menos se puede maquillar.

Una advertencia honesta. Cien respuestas son pocas para comparar lecciones entre sí con confianza. Sirven para encontrar casos muy malos, no para ordenar las buenas.

## Qué no se debe concluir

Un sí no demuestra que la persona aprendió. Mide que se sintió ayudada. Para saber si aprendió hace falta algo más, por ejemplo un par de preguntas cortas antes y después, o seguir cómo le va en el simulacro semanas después. Eso se puede diseñar cuando haya público.

Tampoco conviene presentar estos resultados como mejora de notas. Ninguna de estas mediciones lo puede probar.

## Siguiente paso concreto

El paso más barato y más informativo es la primera fase. Cinco estudiantes, una lección cada uno, treinta minutos. No requiere programar nada y encuentra más problemas que cualquier cantidad de revisiones internas.
