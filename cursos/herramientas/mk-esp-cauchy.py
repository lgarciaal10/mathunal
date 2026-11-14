import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 3 Ecuación de Laplace y variable compleja"
SEMI=[[f"{2.71828*math.cos(k*math.pi/30):.4f}",f"{2.71828*math.sin(k*math.pi/30):.4f}"] for k in range(31)]
EL=[{"t":"trazo","puntos":SEMI,"c":3},
    {"t":"segmento","a":["0","0"],"b":["3.7*cos(x)","3.7*sin(x)"],"c":0},
    {"t":"punto","p":["2.71828*cos(x)","2.71828*sin(x)"],"c":1}]
graf={"tipo":"plano","x":[-4,4],"y":[-0.5,4],"a":0.05,"b":3.1,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"ángulo del rayo, igual a Im z, en radianes","formula":"x"},{"rotulo":"parte imaginaria de w en Re z igual a 1","formula":"2.71828*sin(x)"}],
 "etiquetas":["El rayo, imagen de una recta horizontal, con ángulo igual a la altura","El punto sobre el semicírculo de radio e, imagen de Re z igual a 1"],"etiquetaSlider":"Altura Im z, de 0 a pi",
 "alt":"La aplicación w igual a e elevado a z lleva cada recta horizontal Im z igual a s a un rayo que sale del origen con ángulo s. Al variar s de 0 a pi, los rayos barren el semiplano superior. La recta vertical Re z igual a 1 se convierte en un semicírculo de radio e"}
glos={"cr":"Las ecuaciones de Cauchy-Riemann, u sub x igual a v sub y y u sub y igual a menos v sub x, son la condición para que una función compleja sea derivable.",
 "armonica":"Una función es armónica si cumple la ecuación de Laplace, u sub x x más u sub y y igual a cero.",
 "mapeo":"Un mapeo es la transformación del plano que hace una función compleja, y se estudia por la imagen de rectas y curvas.",
 "conforme":"Un mapeo conforme, dado por una función analítica con derivada no nula, conserva los ángulos entre curvas."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se escribe f de z como u más i v, y la derivabilidad compleja exige las ecuaciones de Cauchy-Riemann."],
 [4,10,"Con la función e a la z, una recta horizontal se convierte en un rayo desde el origen, con ángulo igual a la altura."],
 [10,16,"Con la altura en pi medios, el rayo apunta hacia arriba, y la imagen del punto es i por e."],
 [16,20,"Al llegar la altura a pi, el rayo es el eje real negativo, y la franja completa cubre el semiplano superior."],
 [20,24,"La parte real y la imaginaria de una función analítica son armónicas, y por eso están ligadas."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.3],[8,0.3],[10,1.57],[13,1.57],[16,3.1],[18,3.1],[24,3.1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Si f de z es u más i v, la derivada compleja existe solo si se cumplen las ecuaciones de {{gl:cr|Cauchy-Riemann}}, u sub x igual a v sub y y u sub y igual a menos v sub x. Entonces u y v son {{gl:armonica|armónicas}}. Una función analítica define un {{gl:mapeo|mapeo}} del plano que es {{gl:conforme|conforme}}, y conserva los ángulos.")),
 sec("Un ejemplo","Un ejemplo",P("La función e a la z transforma rectas horizontales en rayos. Cambia la altura y mira el rayo girar."),EQ("w=e^{z}=e^{x}\\cos y+i\\,e^{x}\\operatorname{sen}y"),{"t":"grafica","animar":"dibujar","alt":"El rayo imagen de una recta horizontal bajo e a la z"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con u igual a e elevado a x por coseno de y, ¿cuánto vale u sub x?","opciones":["e elevado a x por coseno de y","menos e elevado a x por seno de y","e elevado a x por seno de y","cero"],"correcta":"e elevado a x por coseno de y","bien":"Muy bien. Derivar respecto a x deja la misma expresión, porque e elevado a x no cambia.","mal":"Al derivar respecto a x, e elevado a x no cambia y el coseno de y es una constante. Queda e elevado a x por coseno de y."}),
 sec("Rectas y rayos","Rayos",P("Mira el rayo con alturas 0.3, 1.57, 2.5 y 3.1."),{"t":"acercando","ds":[0.3,1.57,2.5,3.1],"alt":"El rayo imagen con cuatro alturas"},P("Con la altura en 1.57 el rayo apunta hacia arriba, y con 3.1 es casi el eje real negativo.")),
 sec("Cauchy-Riemann","Ecuaciones",P("Se comprueba con la función e a la z, que debe ser analítica."),
   PASOS([("u=e^{x}\\cos y,\\quad v=e^{x}\\operatorname{sen}y","Las partes real e imaginaria."),
          ("u_{x}=e^{x}\\cos y=v_{y}","Primera ecuación."),
          ("u_{y}=-e^{x}\\operatorname{sen}y=-v_{x}","Segunda ecuación."),
          ("u_{xx}+u_{yy}=e^{x}\\cos y-e^{x}\\cos y=0","Entonces u es armónica.")]),
   OJO("Las ecuaciones de Cauchy-Riemann son necesarias. Para que sea analítica, además las derivadas parciales deben ser continuas.")),
 sec("Un contraejemplo","Contraejemplo",P("La conjugada de z no es analítica, y las ecuaciones lo detectan."),
   PASOS([("f(z)=\\bar{z}=x-iy\\ \\Rightarrow\\ u=x,\\ v=-y","Partes real e imaginaria."),
          ("u_{x}=1,\\quad v_{y}=-1","Las dos derivadas son distintas."),
          ("u_{x}\\ne v_{y}","No se cumple Cauchy-Riemann."),
          ("f\\ \\text{no es analitica en ningun punto}","La conjugada no es derivable.")]),
   OJO("Con f igual a z al cuadrado, u es x al cuadrado menos y al cuadrado y v es 2xy. Entonces u sub x es 2x y v sub y es 2x, y las ecuaciones sí se cumplen.")),
 eng("Flujo alrededor de un cilindro","En un fluido ideal que pasa por un cilindro, el potencial complejo es una función analítica. Su parte real es el potencial de velocidades y su parte imaginaria es la función de corriente. Ambas son armónicas.","\\Omega(z)=U\\left(z+\\dfrac{R^{2}}{z}\\right)",
   [("Velocidad lejos","U"),("Radio del cilindro","R"),("Sobre el cilindro","la corriente es constante")],"La analiticidad enlaza potencial y corriente por Cauchy-Riemann, y por eso se conoce uno al conocer el otro. Es un modelo ideal, sin viscosidad, y sirve como primera aproximación."),
 completar("Las ecuaciones de Cauchy-Riemann dicen que u sub x es igual a [[hueco]].","u_{x}=[[hueco]]",
   [("v_{y}","v sub y"),("v_{x}","v sub x"),("-v_{y}","menos v sub y")],0,
   ["","Con v sub x se confunde con la segunda ecuación, que lleva un signo menos.","Con menos v sub y el signo no es correcto."],"La primera ecuación iguala u sub x con v sub y.","Es v sub y."),
 error("Alguien revisó si f de z igual a la conjugada de z cumple Cauchy-Riemann, y se equivocó. Toca el paso que está mal.",
   [("u=x,\\quad v=-y","Partes real e imaginaria.","partes"),
    ("u_{x}=1,\\quad v_{y}=1","Este paso es el que falla.","v sub y igual a 1"),
    ("u_{x}=v_{y}\\ \\Rightarrow\\ \\text{analitica}","Conclusión.","analitica")],1,
   "v es menos y, así que v sub y es menos 1. Como u sub x es 1, no se cumple la igualdad, y la conjugada no es analítica.",
   "v_{y}=-1","Deriva v igual a menos y respecto a y."),
 ordenar("Estos son los pasos para verificar Cauchy-Riemann con z al cuadrado, pero están desordenados.",
   [("z^{2}=(x^{2}-y^{2})+i(2xy)","Se separan las partes"),
    ("u_{x}=2x,\\quad v_{y}=2x","Primera ecuación"),
    ("u_{y}=-2y,\\quad v_{x}=2y","Segunda ecuación"),
    ("u_{x}=v_{y},\\quad u_{y}=-v_{x}","Se cumplen las dos")],[2,0,3,1],
   "Primero se separan las partes, luego se calculan las derivadas y por último se comprueba.","Se empieza separando u y v."),
]
S+=cierre("Mini simulacro de Cauchy-Riemann",[
 banco("es_c3_17","Las ecuaciones de Cauchy-Riemann."),
 banco("es_c3_18","La conjugada no es analítica."),
 banco("es_c3_19","Las partes de una analítica son armónicas."),
 banco("es_c3_20","La franja se transforma con e a la z.")])
prac=[
 {"titulo":"La función","grafica":{"draw":1},"bloques":[P("Se estudia la imagen de rectas horizontales."),EQ("w=e^{z},\\quad z=x+iy")]},
 {"titulo":"Cambia la altura","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El rayo imagen gira con la altura, y abajo se leen el ángulo y la parte imaginaria de w.")]},
 {"titulo":"Arriba","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1.57,"bloques":[EQ("e^{1+i\\pi/2}=i\\,e"),P("Con la altura en pi medios, el rayo apunta hacia arriba.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1.57},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El ángulo del rayo es la altura Im z."}]}]
preg={"tex":"f(z)=z^{2},\\ u=x^{2}-y^{2},\\ v=2xy.\\ \\text{Entonces }v_{x}\\text{ es}","opciones":["$2y$","$2x$","$-2y$","$0$"],"correcta":0,
 "explicacion":"v es 2xy, y al derivar respecto a x queda 2y. Con u sub y igual a menos 2y, se cumple que u sub y es menos v sub x.",
 "verificacion":{"formula":"2*1+0*x","a":0,"esperado":2},
 "pistas":["v es 2xy.","Deriva respecto a x, con y constante.","Queda 2y."],
 "errores":["","Con 2x se derivó respecto a y.","Con menos 2y es u sub y, y no v sub x.","Con 0 se tomó y como cero."]}
res=["Las ecuaciones de Cauchy-Riemann son u sub x igual a v sub y y u sub y igual a menos v sub x.","Las partes real e imaginaria de una función analítica son armónicas.","La función e a la z convierte una franja de altura pi en el semiplano superior."]
write(lesson("es-m3-l2","Lección 2 de 5","Ecuaciones de Cauchy-Riemann y mapeos",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-cauchy.json")
