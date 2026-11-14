from mklib import *
MOD="Módulo 3 Aplicaciones, polares y series"
graf={"tipo":"polar","x":[-1.75,3.75],"y":[-1.5,1.5],"funcion":"1+cos(x)","primitiva":"3*x/4+sin(x)+sin(2*x)/8","a":0,"b":6.1,"rango":[0,6.2832],"franja":0.2,"limite":2,
 "etiquetas":["Área barrida","Radio"],"rotulos":["área","radio"],"etiquetaSlider":"Ángulo theta en radianes",
 "alt":"Cardioide de ecuación r igual a 1 más coseno de theta, con la región barrida por el radio sombreada desde theta igual a 0 hasta un ángulo que avanza"}
glos={"polares":"Las coordenadas polares dan un punto con su distancia r al origen y el ángulo theta que forma con el eje x.",
 "cardioide":"La cardioide es una curva con forma de corazón, de ecuación r igual a a por (1 más coseno de theta).",
 "sector":"Un sector es la región que barre un radio al girar un ángulo, como una rebanada de pizza."}
ver={"duracion":22.0,"capitulos":[
 [0,2.5,"Esta es la curva r igual a 1 más coseno de theta, una cardioide. Cada punto se da con un radio y un ángulo."],
 [2.5,5,"Se parte del ángulo 0, donde el radio mide 2."],
 [5,12,"Al girar el radio, la región que barre se va llenando. En theta igual a pi el radio es 0 y ya se barrió la mitad."],
 [12,17,"Con theta igual a pi el área barrida es 2.356 y el radio vale 0."],
 [17,22,"Al cerrar la vuelta, con theta igual a 2 pi, el área total es 3 pi sobre 2, o sea 4.7124."]],
 "canales":{"draw":[[0.3,0],[2.4,1]],"hole":[[2.5,0],[3.3,1]],"d":[[5,0.3],[12,3.1416],[17,3.1416],[19,6.2832],[22,6.2832]],"guide":[[12,0],[13,1]]},
 "intervalos":{"ok":[19,22]}}
S=[
 sec("La idea",None,P("En {{gl:polares|coordenadas polares}} un punto se da con su distancia r al origen y el ángulo theta. Muchas curvas simétricas, como círculos y espirales, tienen ecuaciones muy simples así. Para medir el área de una región, en vez de franjas verticales se usan {{gl:sector|sectores}} que gira el radio.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la curva r igual a 1 más coseno de theta, una {{gl:cardioide|cardioide}}. Se quiere el área que encierra."),EQ("A=\\dfrac{1}{2}\\int_{0}^{2\\pi}r^{2}\\,d\\theta"),{"t":"grafica","animar":"dibujar","alt":"Curva que se dibuja y marca el punto de partida en theta igual a 0"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Cuando theta vale 0, ¿cuánto mide el radio? Es 1 más el coseno de 0.","opciones":[0,1,2,3],"correcta":2,"bien":"Muy bien. El coseno de 0 es 1, así que el radio mide 2. Más abajo se ve cómo barre el radio.","mal":"Mide 2, porque el coseno de 0 es 1. Más abajo se ve cómo barre el radio."}),
 sec("El área que se barre","El área",P("Mira cómo gira el radio y qué valen el área barrida y el radio en cada ángulo."),{"t":"acercando","ds":[1.5,3.1416,4.5,6.2832],"alt":"La región que barre el radio de la cardioide mientras el ángulo avanza hasta una vuelta completa"},P("Con theta igual a 2 pi el radio vuelve a medir 2 y el área barrida es <b>4.7124</b>. Ese es el valor de la integral.")),
 sec("Pasar entre sistemas","Convertir",P("Las dos formas de dar un punto se relacionan con un triángulo rectángulo."),
   PASOS([("x=r\\cos\\theta,\\qquad y=r\\operatorname{sen}\\theta","De polares a cartesianas."),
          ("r^{2}=x^{2}+y^{2},\\qquad \\tan\\theta=\\dfrac{y}{x}","De cartesianas a polares."),
          ("r=2\\ \\text{y}\\ \\theta=\\dfrac{\\pi}{3}\\ \\Rightarrow\\ \\left(1,\\ \\sqrt{3}\\right)","Con el ejemplo del punto con radio 2 y ángulo de 60 grados.")])),
 sec("La fórmula del área","La fórmula",P("Un sector delgado con ángulo d theta es casi un triángulo con base r d theta y altura r, así que su área es un medio de r cuadrado d theta."),
   EQ("A=\\dfrac{1}{2}\\int_{\\alpha}^{\\beta}r(\\theta)^{2}\\,d\\theta"),
   PASOS([("A=\\dfrac{1}{2}\\int_{0}^{2\\pi}(1+\\cos\\theta)^{2}\\,d\\theta=\\dfrac{1}{2}\\int_{0}^{2\\pi}\\left(1+2\\cos\\theta+\\cos^{2}\\theta\\right)d\\theta","Se desarrolla el cuadrado."),
          ("=\\dfrac{1}{2}\\left[\\dfrac{3\\theta}{2}+2\\operatorname{sen}\\theta+\\dfrac{\\operatorname{sen}2\\theta}{4}\\right]_{0}^{2\\pi}","Se usa la identidad del coseno al cuadrado para integrar."),
          ("=\\dfrac{3\\pi}{2}\\approx 4.7124","Es el mismo valor que mostraba el área barrida de la gráfica.")]),
   OJO("La fórmula lleva un medio y el radio va al cuadrado. Olvidar el un medio es el error más común.")),
 sec("Qué rango de ángulos usar","Rango",P("Hay curvas que se trazan completas con menos de una vuelta. Si se integra de más, se cuenta el área dos veces."),
   PASOS([("r=3\\cos\\theta\\ \\text{traza el círculo completo para}\\ 0\\le\\theta\\le\\pi","Para theta entre pi y 2 pi la curva vuelve a pasar por los mismos puntos."),
          ("A=\\dfrac{1}{2}\\int_{0}^{\\pi}9\\cos^{2}\\theta\\,d\\theta=\\dfrac{9\\pi}{4}","Es el área del círculo de radio 1.5, que es pi por 1.5 al cuadrado.")])),
 eng("El perfil de una leva","Una leva excéntrica tiene un perfil cuyo radio cambia con el ángulo. Es natural describirla en polares. Para conocer su volumen y su peso se necesita el área de su perfil, que es una integral del radio al cuadrado.","r(\\theta)=20+5\\cos\\theta\\ \\text{mm}",
   [("Radio base","20 mm"),("Excentricidad","5 mm"),("Espesor de la leva","10 mm")],"El área del perfil es un medio de la integral de r al cuadrado entre 0 y 2 pi, o sea 412.5 pi milímetros cuadrados, unos 1296 mm². Con 10 mm de espesor, el volumen es de unos 12.96 centímetros cúbicos. Es un modelo simplificado, porque no incluye el agujero del eje ni los chaflanes."),
 completar("Se pasa el punto con r igual a 2 y theta igual a pi sobre 3 a coordenadas cartesianas. Falta x.","x=r\\cos\\theta=2\\cos\\dfrac{\\pi}{3}=[[hueco]]",
   [("1","uno"),("\\sqrt{3}","raíz de tres"),("2","dos")],0,
   ["","Esa es la coordenada y, que usa seno. Para x se usa coseno, y el coseno de pi sobre 3 vale un medio.","Ese es el radio. Hay que multiplicarlo por el coseno de pi sobre 3, que vale un medio."],"El coseno de pi sobre 3 vale un medio.","El coseno de pi sobre 3, o sea de 60 grados, vale un medio. Por 2 queda 1."),
 error("Alguien calculó el área de la cardioide y se equivocó en un paso. Toca el paso que está mal.",
   [("r=1+\\cos\\theta,\\quad 0\\le\\theta\\le 2\\pi","Se identifica la curva y el rango del ángulo.","r es 1 más coseno de theta, con theta de 0 a 2 pi"),
    ("A=\\int_{0}^{2\\pi}(1+\\cos\\theta)^{2}\\,d\\theta","Este paso es el que falla.","A es la integral de 0 a 2 pi de 1 más coseno de theta, al cuadrado"),
    ("=\\left[\\dfrac{3\\theta}{2}+2\\operatorname{sen}\\theta+\\dfrac{\\operatorname{sen}2\\theta}{4}\\right]_{0}^{2\\pi}=3\\pi","La cuenta sigue bien con lo que viene del paso anterior.","Se integra y queda 3 pi")],1,
   "Falta el un medio de la fórmula del área en polares. El área de un sector es un medio de r cuadrado d theta. Sin él sale 3 pi, el doble del área real.",
   "A=\\dfrac{1}{2}\\int_{0}^{2\\pi}(1+\\cos\\theta)^{2}\\,d\\theta=\\dfrac{3\\pi}{2}","Compara con la fórmula del área de un sector."),
 ordenar("Estos son los pasos para el área del círculo r igual a 3 coseno de theta, pero están desordenados.",
   [("r=3\\cos\\theta\\ \\text{traza el círculo para}\\ 0\\le\\theta\\le\\pi","La curva se traza completa entre 0 y pi"),
    ("A=\\dfrac{1}{2}\\int_{0}^{\\pi}(3\\cos\\theta)^{2}\\,d\\theta","El área es un medio de la integral de r al cuadrado"),
    ("=\\dfrac{9}{2}\\int_{0}^{\\pi}\\cos^{2}\\theta\\,d\\theta","Se saca la constante"),
    ("=\\dfrac{9}{2}\\cdot\\dfrac{\\pi}{2}=\\dfrac{9\\pi}{4}","Se integra y queda 9 pi sobre 4")],[2,0,3,1],
   "Se identifica el rango, se plantea la fórmula del área, se saca la constante y se integra.","Primero se decide el rango de theta."),
]
S+=cierre("",None)
prac=[
 {"titulo":"La curva","grafica":{"draw":1},"bloques":[P("Esta es la curva en polares."),EQ("r=1+\\cos\\theta")]},
 {"titulo":"El punto de partida","grafica":{"draw":1,"hole":1},"bloques":[P("El área se empieza a barrer desde theta igual a 0, donde el radio mide 2.")]},
 {"titulo":"Mueve theta","grafica":{"draw":1,"hole":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El radio gira, la región que barre se llena y abajo se ven el área y el radio en ese ángulo.")]},
 {"titulo":"Un sector","grafica":{"draw":1,"hole":1,"guide":1},"laboratorio":True,"d":3.1416,"bloques":[P("La zona amarilla es un sector delgado, casi un triángulo de base r por d theta. En theta igual a pi el radio es 0 y el área barrida es 2.356, la mitad de 4.712.")]},
 {"titulo":"El resultado","grafica":{"draw":1,"hole":1,"guide":1,"ok":True},"laboratorio":True,"d":5.9,"bloques":[EQ("A=\\dfrac{1}{2}\\int_{0}^{2\\pi}(1+\\cos\\theta)^{2}\\,d\\theta=\\dfrac{3\\pi}{2}"),P("Con theta igual a 5.9 el área barrida ya es 4.7. Con la vuelta completa llega a 4.7124, que es 3 pi sobre 2.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"hole":1,"guide":1,"ok":True,"d":5.9},"bloques":[{"t":"pregunta"},{"t":"nota","html":"No olvides el un medio, y fíjate en el rango de theta."}]}]
preg={"tex":"\\text{Área de}\\ r=2+\\cos\\theta,\\ 0\\le\\theta\\le 2\\pi","opciones":["$\\dfrac{9\\pi}{2}$","$9\\pi$","$4\\pi$","$5\\pi$"],"correcta":0,
 "explicacion":"El área es un medio de la integral de (2 más coseno de theta) al cuadrado. Al desarrollar queda 4 más 4 coseno de theta más coseno al cuadrado de theta. Entre 0 y 2 pi, el 4 da 8 pi, el coseno da 0 y el coseno al cuadrado da pi. La suma es 9 pi y con el un medio queda 9 pi sobre 2.",
 "verificacion":{"formula":"0.5*(4*2*pi+4*sin(2*pi)+2*pi/2+sin(4*pi)/4)+0*x","a":0,"esperado":14.1371669412},
 "pistas":["Usa la fórmula del área en polares, un medio de la integral de r al cuadrado.","Desarrolla (2 más coseno de theta) al cuadrado.","La integral del 4 da 8 pi, la del coseno da 0 y la del coseno al cuadrado da pi."],
 "errores":["","Falta el un medio de la fórmula. Sin él sale el doble del área.","Eso es solo el área del círculo de radio 2. Falta el efecto de sumar el coseno al radio.","Revisa la cuenta. La suma de las integrales es 9 pi, y el un medio la deja en 9 pi sobre 2."]}
res=["En polares, x es r coseno de theta y y es r seno de theta, y r al cuadrado es x al cuadrado más y al cuadrado.","El área es un medio de la integral de r al cuadrado en theta.","Hay que usar el rango de theta que traza la curva una sola vez para no contar el área dos veces."]
write(lesson("calcint-m3-l4","Lección 4 de 5","Coordenadas polares",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=4),"calcint-polares.json")
