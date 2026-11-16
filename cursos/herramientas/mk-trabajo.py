from mklib import *
MOD="Módulo 3 Aplicaciones, polares y series"
graf={"tipo":"area","x":[0,0.6],"y":[0,28],"funcion":"40*x","primitiva":"20*x*x","a":0,"b":0.55,"franja":0.02,"limite":20,
 "etiquetas":["Trabajo acumulado","Fuerza"],"rotulos":["trabajo (J)","fuerza (N)"],"etiquetaSlider":"Estiramiento x en metros",
 "alt":"Recta de fuerza 40 por x de un resorte con el área bajo ella sombreada, que es el trabajo acumulado al estirarlo"}
glos={"trabajo":"El trabajo es la energía que una fuerza le transfiere a un cuerpo al moverlo. Se mide en julios, que son newtons por metro.",
 "hooke":"La ley de Hooke dice que la fuerza de un resorte es proporcional a su estiramiento, F igual a k por x.",
 "promedio":"El valor promedio de una función es el valor constante que daría la misma área en el mismo intervalo."}
ver={"duracion":22.0,"capitulos":[
 [0,2.5,"Esta es la fuerza de un resorte que se estira. Crece en línea recta con la distancia, F igual a 40 por x."],
 [2.5,5,"El trabajo es el área bajo esta gráfica, a partir de x igual a 0."],
 [5,11,"Al estirar el resorte, el área se va llenando y el trabajo acumulado crece."],
 [11,16,"Con x igual a 0.5 metros la fuerza es 20 newtons y el trabajo acumulado es 5 julios."],
 [16,22,"La integral de la fuerza da el mismo valor, 5 julios."]],
 "canales":{"draw":[[0.3,0],[2.4,1]],"hole":[[2.5,0],[3.3,1]],"d":[[5,0.05],[11,0.3],[15,0.5],[22,0.5]],"guide":[[11,0],[12,1]]},
 "intervalos":{"ok":[16,22]}}
S=[
 sec("La idea",None,P("Cuando una fuerza constante mueve un cuerpo, el {{gl:trabajo|trabajo}} es la fuerza por la distancia. Pero muchas fuerzas cambian a lo largo del movimiento. Entonces el trabajo es el área bajo la gráfica de la fuerza, o sea una integral. Con la misma idea se calcula el valor promedio de una función.")),
 sec("Un ejemplo","Un ejemplo",P("Un resorte se estira desde su posición natural hasta 0.5 metros. Según la {{gl:hooke|ley de Hooke}}, la fuerza crece con el estiramiento, y esta tiene constante de 40 newtons por metro."),EQ("W=\\int_{0}^{0.5}40\\,x\\,dx"),{"t":"grafica","animar":"dibujar","alt":"Recta de fuerza que se dibuja y marca el punto de partida en x igual a 0"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Cuando el resorte está estirado 0.5 metros, ¿cuánta fuerza hace? Es 40 por 0.5.","opciones":[10,20,40,80],"correcta":20,"bien":"Muy bien. Hace 20 newtons. Más abajo se ve el trabajo acumulado hasta ahí.","mal":"Hace 20 newtons, que es 40 por 0.5. Más abajo se ve el trabajo acumulado hasta ahí."}),
 sec("El trabajo que se acumula","El trabajo",P("Mira cómo se llena el área y qué valen el trabajo y la fuerza en cada estiramiento."),{"t":"acercando","ds":[0.1,0.2,0.4,0.5],"alt":"El área bajo la recta de fuerza que va creciendo mientras el resorte se estira"},P("Con 0.5 metros de estiramiento el trabajo acumulado es <b>5 julios</b>. Ese es el valor de la integral.")),
 sec("Trabajo con fuerza variable","Fuerza variable",EQ("W=\\int_{a}^{b}F(x)\\,dx"),
   PASOS([("W=\\int_{0}^{0.5}40\\,x\\,dx","Se integra la fuerza sobre la distancia recorrida."),
          ("=\\Bigl[20\\,x^{2}\\Bigr]_{0}^{0.5}=20\\cdot 0.25=5\\ \\text{J}","Se evalúa la primitiva. Es el mismo valor que mostraba el área de la gráfica."),
          ("W=\\int_{0.5}^{1}40\\,x\\,dx=20\\left(1-0.25\\right)=15\\ \\text{J}","Estirarlo de 0.5 a 1 metro cuesta el triple de trabajo, porque la fuerza ya es mayor.")]),
   OJO("El trabajo se mide en julios, que son newtons por metro. Revisa que la distancia esté en metros y la fuerza en newtons.")),
 sec("Dividir en rebanadas","Rebanadas",P("Cuando lo que se mueve es un cuerpo extendido, como un cable, cada rebanada recorre una distancia distinta. Se calcula el trabajo de una rebanada y se suman."),
   PASOS([("\\text{Cable de 20 m con 5 kg/m, que se sube desde abajo}","Cada metro de cable pesa 5 kilogramos por 9.81, o sea 49.05 newtons."),
          ("dW=\\underbrace{49.05\\,dy}_{\\text{peso}}\\cdot\\underbrace{y}_{\\text{distancia}}","Una rebanada a profundidad y pesa 49.05 dy y se sube una distancia y."),
          ("W=\\int_{0}^{20}49.05\\,y\\,dy=49.05\\cdot\\dfrac{400}{2}=9810\\ \\text{J}","Se suma todo con una integral.")])),
 sec("Valor promedio","Valor promedio",P("El {{gl:promedio|valor promedio}} de una función en un intervalo es la integral dividida entre la longitud del intervalo."),
   EQ("f_{\\text{prom}}=\\dfrac{1}{b-a}\\int_{a}^{b}f(x)\\,dx"),
   PASOS([("f_{\\text{prom}}=\\dfrac{1}{0.5}\\int_{0}^{0.5}40\\,x\\,dx=\\dfrac{5}{0.5}=10\\ \\text{N}","La fuerza promedio del resorte en ese estiramiento es 10 newtons."),
          ("40\\,c=10\\ \\Rightarrow\\ c=0.25","Hay un punto donde la fuerza vale justo el promedio. Eso es el teorema del valor medio para integrales."),
          ("T(t)=20+5\\operatorname{sen}\\dfrac{\\pi t}{12},\\quad 0\\le t\\le 12\\ \\Rightarrow\\ T_{\\text{prom}}\\approx 23.2\\ ^{\\circ}\\text{C}","Con la temperatura de la mañana a la noche, el promedio sale de la integral entre 12.")])),
 eng("Vaciar un tanque con una bomba","Para vaciar un tanque cilíndrico lleno de agua por la parte de arriba, la bomba sube cada capa de agua una distancia distinta. Las capas del fondo suben más que las de arriba. El trabajo total es una integral.","dW=\\rho\\,g\\,\\pi r^{2}\\,dy\\cdot y",
   [("Radio del tanque","1 m"),("Altura del tanque","3 m"),("Densidad del agua","1000 kg/m³")],"Con y medido desde la superficie, el trabajo es la integral de 1000 por 9.81 por pi por y entre 0 y 3, que vale 1000 por 9.81 por pi por 4.5, o sea unos 139 000 julios. Es un modelo simplificado, porque no incluye las pérdidas en la bomba ni en las tuberías."),
 completar("Se calcula el trabajo de una fuerza de 3x newtons desde x igual a 0 hasta x igual a 2 metros.","W=\\int_{0}^{2}3x\\,dx=\\left[\\dfrac{3x^{2}}{2}\\right]_{0}^{2}=[[hueco]]",
   [("6","seis"),("12","doce"),("3","tres")],0,
   ["","Falta dividir entre 2 al integrar. La primitiva es 3x al cuadrado sobre 2, que en 2 vale 6.","Revisa la cuenta. En x igual a 2 la primitiva vale 3 por 4 sobre 2, o sea 6."],"Evalúa 3 por 2 al cuadrado sobre 2.","En x igual a 2, 3 por 4 sobre 2 es 6. En 0 vale 0. El trabajo es 6 julios."),
 error("Alguien calculó el valor promedio de x entre 0 y 4 y se equivocó en un paso. Toca el paso que está mal.",
   [("f(x)=x\\quad \\text{en}\\quad [0,4]","Es la función y el intervalo.","La función es x en el intervalo de 0 a 4"),
    ("\\int_{0}^{4}x\\,dx=8","La integral está bien calculada.","La integral de x entre 0 y 4 es 8"),
    ("f_{\\text{prom}}=8","Este paso es el que falla.","El valor promedio es 8")],2,
   "Falta dividir entre la longitud del intervalo. El valor promedio es la integral dividida entre b menos a. Aquí es 8 entre 4.",
   "f_{\\text{prom}}=\\dfrac{1}{4-0}\\int_{0}^{4}x\\,dx=\\dfrac{8}{4}=2","Si x va de 0 a 4, ¿el promedio puede ser mayor que 4?"),
 ordenar("Estos son los pasos para el trabajo de comprimir un resorte de 0.1 a 0.3 metros, pero están desordenados.",
   [("F(x)=40\\,x","La fuerza es 40 por x"),
    ("W=\\int_{0.1}^{0.3}40\\,x\\,dx","El trabajo es la integral de la fuerza entre 0.1 y 0.3"),
    ("=\\Bigl[20\\,x^{2}\\Bigr]_{0.1}^{0.3}","Se integra"),
    ("=1.8-0.2=1.6\\ \\text{J}","Se evalúa y queda 1.6 julios")],[2,0,3,1],
   "Se escribe la fuerza, se plantea la integral entre los dos estiramientos, se integra y se evalúa.","Se empieza con la fuerza."),
]
S+=cierre("",None)
prac=[
 {"titulo":"La fuerza","grafica":{"draw":1},"bloques":[P("Esta es la fuerza de un resorte que se estira."),EQ("F(x)=40\\,x")]},
 {"titulo":"El punto de partida","grafica":{"draw":1,"hole":1},"bloques":[P("El trabajo se empieza a acumular desde x igual a 0, con el resorte sin estirar.")]},
 {"titulo":"Mueve x","grafica":{"draw":1,"hole":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El área sombreada es el trabajo acumulado y abajo se ve la fuerza en x.")]},
 {"titulo":"La fuerza","grafica":{"draw":1,"hole":1,"guide":1},"laboratorio":True,"d":0.3,"bloques":[P("La franja amarilla es un pedacito de trabajo, fuerza por distancia. Con 0.3 metros la fuerza es 12 newtons y el trabajo acumulado es 1.8 julios.")]},
 {"titulo":"El resultado","grafica":{"draw":1,"hole":1,"guide":1,"ok":True},"laboratorio":True,"d":0.5,"bloques":[EQ("W=\\int_{0}^{0.5}40\\,x\\,dx=5\\ \\text{J}"),P("Con 0.5 metros el trabajo es 5 julios. La fuerza promedio en ese tramo es 10 newtons, justo la mitad de la fuerza final.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"hole":1,"guide":1,"ok":True,"d":0.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Integra y, si es un promedio, divide entre la longitud del intervalo."}]}]
preg={"tex":"\\text{Valor promedio de}\\ f(x)=x^{2}\\ \\text{en}\\ [0,3]","opciones":["$3$","$9$","$\\dfrac{9}{2}$","$1$"],"correcta":0,
 "explicacion":"La integral de x al cuadrado entre 0 y 3 es 27 sobre 3, o sea 9. El valor promedio es la integral entre la longitud del intervalo, 9 entre 3, que es 3.",
 "verificacion":{"formula":"(3^3/3-0)/3+0*x","a":0,"esperado":3},
 "pistas":["El valor promedio es la integral dividida entre b menos a.","La integral de x al cuadrado entre 0 y 3 vale 9.","Divide ese 9 entre la longitud del intervalo, que es 3."],
 "errores":["","Es la integral sin dividir. El valor promedio se obtiene dividiendo entre la longitud del intervalo.","Se promediaron los valores en los extremos, 0 y 9. Eso solo funciona para funciones lineales.","Revisa la cuenta. La integral es x al cubo sobre 3, que vale 9, y luego se divide entre 3."]}
res=["El trabajo de una fuerza variable es la integral de la fuerza sobre la distancia, y se mide en julios.","Para un cuerpo extendido, se calcula el trabajo de una rebanada y se suma con una integral.","El valor promedio de f en un intervalo es la integral dividida entre b menos a."]
write(lesson("calcint-m3-l2","Lección 2 de 5","Trabajo y valor promedio",24,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=4),"calcint-trabajo.json")
