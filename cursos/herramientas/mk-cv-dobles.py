import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 2 Integrales múltiples"
EL=[{"t":"poligono","puntos":[["0","0"],["1","0"],["1","1"]],"c":2,"nombre":"D"},
    {"t":"segmento","a":["x","0"],"b":["x","x"],"c":0},
    {"t":"segmento","a":["x","x"],"b":["1","x"],"c":1},
    {"t":"punto","p":["x","x"],"c":3}]
graf={"tipo":"plano","x":[-0.8,2.2],"y":[-0.4,1.4],"a":0,"b":1,"inicio":0.4,"elementos":EL,
 "lecturas":[{"rotulo":"longitud del corte vertical, y va de 0 a x","formula":"x"},{"rotulo":"longitud del corte horizontal, x va de y a 1","formula":"1-x"}],
 "etiquetas":["Con el orden dy dx se corta con rectas verticales","Con el orden dx dy se corta con rectas horizontales"],"etiquetaSlider":"Posición del corte, de 0 a 1",
 "alt":"La región triangular D, con vértices en 0, 0, en 1, 0 y en 1, 1. El corte vertical en x va desde y igual a 0 hasta y igual a x. El corte horizontal en y va desde x igual a y hasta x igual a 1. Se recorre la misma región con los dos órdenes de integración"}
glos={"doble":"Una integral doble suma los valores de una función sobre una región del plano, y con f igual a 1 da el área de la región.",
 "iterada":"Una integral iterada calcula la integral doble integrando primero respecto a una variable y luego respecto a la otra.",
 "fubini":"El teorema de Fubini dice que en una región razonable el orden de integración no cambia el resultado.",
 "region":"El primer paso de cualquier integral doble es dibujar la región, para saber los límites de cada variable."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La región es un triángulo con vértices en 0, 0, en 1, 0 y en 1, 1, donde y va de 0 hasta x."],
 [4,10,"Con el orden dy dx se corta con rectas verticales. En cada x, y va de 0 a x."],
 [10,16,"Con x igual a 0.4 el corte vertical mide 0.4. El mismo triángulo se puede cortar con rectas horizontales."],
 [16,20,"Con las horizontales, en cada y, x va desde y hasta 1. Con y igual a 0.4 el corte mide 0.6."],
 [20,24,"Los dos órdenes recorren la misma región, y por eso dan el mismo resultado."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.15],[8,0.15],[10,0.4],[16,0.4],[18,0.8],[24,0.8]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Una {{gl:doble|integral doble}} se calcula como una {{gl:iterada|integral iterada}}, integrando primero respecto a una variable. Todo parte de dibujar la {{gl:region|región}}. Con el teorema de {{gl:fubini|Fubini}} se puede cambiar el orden, y a veces uno de los dos órdenes es mucho más fácil.")),
 sec("Un ejemplo","Un ejemplo",P("La región es el triángulo bajo la recta y igual a x. Mueve el corte y mira los dos órdenes."),EQ("\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{x}f\\,dy\\,dx=\\int_{0}^{1}\\!\\int_{y}^{1}f\\,dx\\,dy"),{"t":"grafica","animar":"dibujar","alt":"El triángulo con sus cortes verticales y horizontales"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Si el corte vertical en x va de y igual a 0 a y igual a x, ¿cuánto mide con x igual a 0.4?","opciones":[0.4,0.6,1,0],"correcta":0.4,"bien":"Muy bien. Mide x, o sea 0.4.","mal":"Mide x menos 0, o sea 0.4."}),
 sec("Los dos cortes","Cortes",P("Mira los cortes con la posición en 0.15, 0.4, 0.6 y 0.8."),{"t":"acercando","ds":[0.15,0.4,0.6,0.8],"alt":"Los dos cortes en cuatro posiciones"},P("El corte vertical crece con x, y el horizontal disminuye con y.")),
 sec("Una integral sobre un rectángulo","Rectángulo",P("En un rectángulo los límites son constantes, y el orden no cambia nada."),
   PASOS([("\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{2}xy\\,dy\\,dx","El ejemplo."),
          ("\\displaystyle\\int_{0}^{2}xy\\,dy=x\\cdot\\dfrac{y^{2}}{2}\\Big|_{0}^{2}=2x","Se integra respecto a y, con x constante."),
          ("\\displaystyle\\int_{0}^{1}2x\\,dx=x^{2}\\Big|_{0}^{1}=1","Luego respecto a x."),
          ("\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{1}(x+y)\\,dx\\,dy=\\dfrac{1}{2}+\\dfrac{1}{2}=1","Otro ejemplo, que también da 1.")]),
   OJO("Se integra primero la integral de adentro, con la otra variable como constante. El resultado de la primera integración es una función de la variable que queda.")),
 sec("Cambiar el orden","Cambio",P("Se dibuja la región y se lee con el otro orden."),
   PASOS([("0\\le y\\le x\\le1","La región del triángulo."),
          ("\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{x}f\\,dy\\,dx","Orden original."),
          ("0\\le y\\le1,\\quad y\\le x\\le1","Con rectas horizontales."),
          ("\\displaystyle\\int_{0}^{1}\\!\\int_{y}^{1}f\\,dx\\,dy","Orden invertido.")]),
   OJO("Al cambiar el orden, los límites de afuera son constantes y los de adentro son funciones de la variable de afuera. Si queda al revés, hay un error en la región.")),
 eng("La carga total de una placa","Una placa triangular tiene una densidad de carga que crece con el producto x por y. La carga total se calcula con una integral doble sobre el triángulo.","Q=\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{x}xy\\,dy\\,dx=\\dfrac{1}{8}",
   [("Región","triángulo con vértices 0, 0, 1, 0 y 1, 1"),("Densidad","x por y"),("Carga total","un octavo")],"Elegir el orden que haga más fácil la integral es parte del trabajo. En este caso los dos funcionan, pero en otros uno de los órdenes obliga a partir la región en pedazos."),
 completar("Al invertir el orden de la integral de 0 a 1 de la integral de 0 a x, los nuevos límites de x son de y a [[hueco]].","\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{x}f\\,dy\\,dx=\\int_{0}^{1}\\!\\int_{y}^{[[hueco]]}f\\,dx\\,dy",
   [("1","uno"),("0","cero"),("y","y")],0,
   ["","El límite de x no puede terminar en 0, porque entonces la región sería vacía.","El límite superior no puede ser igual al inferior."],"En la región, x llega hasta el borde derecho, que es x igual a 1.","El límite superior es 1."),
 error("Alguien cambió el orden de la integral de 0 a 1 de la integral de 0 a x, y se equivocó. Toca el paso que está mal.",
   [("0\\le y\\le x\\le1","Región.","región"),
    ("\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{y}f\\,dx\\,dy","Este paso es el que falla.","x de 0 a y"),
    ("\\text{el resultado cambia}","Conclusión.","cambia")],1,
   "Con rectas horizontales, x va de y hasta 1, y no de 0 a y. Los límites de adentro deben seguir la región.",
   "\\displaystyle\\int_{0}^{1}\\!\\int_{y}^{1}f\\,dx\\,dy","Mira dónde está x en cada fila horizontal."),
 ordenar("Estos son los pasos para cambiar el orden de integración, pero están desordenados.",
   [("0\\le y\\le x\\le1","Se dibuja la región"),
    ("0\\le y\\le1","Se fijan los límites de afuera"),
    ("y\\le x\\le1","Se escriben los límites de adentro"),
    ("\\displaystyle\\int_{0}^{1}\\!\\int_{y}^{1}f\\,dx\\,dy","Se escribe la integral")],[2,0,3,1],
   "Primero la región, luego los límites de afuera, después los de adentro y por último la integral.","Se empieza dibujando la región."),
]
S+=cierre("Mini simulacro de integrales dobles",[
 banco("cv_c2_01","El valor de la integral de x y sobre el rectángulo."),
 banco("cv_c2_03","El orden invertido de la integral con x de y a 1."),
 banco("cv_c2_07","La integral de x más y sobre el cuadrado unidad."),
 banco("cv_c2_08","El orden invertido con y de 0 a x.")])
prac=[
 {"titulo":"La región","grafica":{"draw":1},"bloques":[P("La región es el triángulo bajo la recta y igual a x."),EQ("0\\le y\\le x\\le1")]},
 {"titulo":"Mueve el corte","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen las longitudes del corte vertical y del horizontal.")]},
 {"titulo":"Un corte en 0.4","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.4,"bloques":[EQ("x=0.4:\\ 0.4,\\qquad y=0.4:\\ 0.6"),P("El corte vertical mide 0.4, y el horizontal mide 0.6.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.4},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Dibuja siempre la región primero."}]}]
preg={"tex":"\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{x}f\\,dy\\,dx\\ \\text{es igual a}","opciones":["$\\displaystyle\\int_{0}^{1}\\!\\int_{y}^{1}f\\,dx\\,dy$","$\\displaystyle\\int_{0}^{1}\\!\\int_{0}^{y}f\\,dx\\,dy$","$\\displaystyle\\int_{0}^{x}\\!\\int_{0}^{1}f\\,dx\\,dy$","$\\displaystyle\\int_{0}^{1}\\!\\int_{x}^{1}f\\,dy\\,dx$"],"correcta":0,
 "explicacion":"La región es y entre 0 y 1, con x desde y hasta 1. Esa es la integral con el orden invertido.",
 "verificacion":{"formula":"1-0.4+0*x","a":0,"esperado":0.6},
 "pistas":["Dibuja el triángulo.","Corta con rectas horizontales.","En cada y, x va de y a 1."],
 "errores":["","En esa x iría de 0 a y, que es otra región, la del lado izquierdo.","Los límites de afuera no pueden depender de otra variable.","Es el orden original con límites cambiados, y no es la misma región."]}
res=["Se dibuja la región para leer los límites de cada variable.","Al cambiar el orden, los límites de afuera son constantes.","El resultado no cambia si la región es la misma."]
write(lesson("cv-m2-l1","Lección 1 de 6","Integrales dobles y cambio de orden",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-dobles.json")
