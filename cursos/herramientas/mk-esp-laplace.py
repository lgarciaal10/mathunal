import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 3 Ecuación de Laplace y variable compleja"
XS=[round(k*math.pi/40,5) for k in range(41)]
SH="((exp(2*x)-exp(-2*x))/2/3.62686)"
EL=[{"t":"trazo","puntos":[[str(xv),f"{math.sin(2*xv):.6f}"] for xv in XS],"c":3},
    {"t":"trazo","puntos":[[str(xv),f"{math.sin(2*xv):.6f}*{SH}"] for xv in XS],"c":0}]
graf={"tipo":"plano","x":[-0.4,3.6],"y":[-1.5,1.5],"a":0,"b":1,"inicio":0.5,"elementos":EL,
 "lecturas":[{"rotulo":"factor seno hiperbólico de 2y entre seno hiperbólico de 2","formula":SH},{"rotulo":"altura y dentro del rectángulo","formula":"x"}],
 "etiquetas":["Este factor reduce la onda del borde de arriba","La altura y va de 0, la base, a 1, el borde de arriba"],"etiquetaSlider":"Altura y, de 0 a 1",
 "alt":"Una función armónica en un rectángulo, con valor seno de 2x en el borde de arriba y cero en los otros tres lados. La curva verde es el borde de arriba. La curva azul es la solución a la altura y, que es la misma onda multiplicada por un factor que crece de 0 a 1"}
glos={"laplace":"La ecuación de Laplace, u sub x x más u sub y y igual a cero, describe un estado de equilibrio, sin variación en el tiempo.",
 "dirichlet":"La condición de Dirichlet da el valor de la función sobre la frontera. La de Neumann da la derivada normal.",
 "armonica":"Una función armónica cumple la ecuación de Laplace. Alcanza sus valores máximo y mínimo en la frontera.",
 "mediovalor":"La propiedad del valor medio dice que el valor de una armónica en el centro de un círculo es el promedio de sus valores sobre el círculo."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"En un rectángulo, la función vale seno de 2x en el borde de arriba, y cero en los otros tres lados."],
 [4,10,"Se separan las variables. En x queda seno de 2x, y en y queda un seno hiperbólico."],
 [10,16,"A la altura 0.5, la onda se reduce al 32 por ciento del borde de arriba."],
 [16,20,"En la base vale cero, y en el borde de arriba vale seno de 2x completo."],
 [20,24,"Una armónica no tiene máximos adentro, y su valor en el centro es el promedio de la frontera."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,0.5],[16,0.5],[18,1],[24,1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("La ecuación de {{gl:laplace|Laplace}} describe el equilibrio, como la temperatura que ya no cambia. Su solución depende solo de la frontera. Las condiciones de {{gl:dirichlet|Dirichlet}} dan el valor en el borde. Las soluciones son {{gl:armonica|armónicas}}, y cumplen la propiedad del {{gl:mediovalor|valor medio}}.")),
 sec("Un ejemplo","Un ejemplo",P("El rectángulo tiene valor seno de 2x en el borde de arriba, y cero en los otros tres lados. Mueve la altura y mira cómo decae la onda."),EQ("u(x,y)=\\dfrac{\\operatorname{senh}2y}{\\operatorname{senh}2}\\operatorname{sen}2x"),{"t":"grafica","animar":"dibujar","alt":"La solución de Laplace a distintas alturas"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Una función armónica en una región cerrada alcanza su máximo, ¿dónde?","opciones":["En la frontera","En el centro","En un punto cualquiera","No tiene máximo"],"correcta":"En la frontera","bien":"Muy bien. Es el principio del máximo para funciones armónicas.","mal":"Alcanza su máximo y su mínimo en la frontera. Es el principio del máximo."}),
 sec("Por alturas","Alturas",P("Mira la solución en las alturas 0.2, 0.5, 0.8 y 1."),{"t":"acercando","ds":[0.2,0.5,0.8,1],"alt":"La solución a cuatro alturas"},P("A la altura 0.5 la onda vale 32 por ciento de la del borde de arriba, y a 0.8 vale 66 por ciento.")),
 sec("Separación de variables","Separación",P("Se busca u como producto, y se usa la condición cero en los lados."),
   PASOS([("u(x,y)=X(x)\\,Y(y)\\ \\Rightarrow\\ \\dfrac{X''}{X}=-\\dfrac{Y''}{Y}=-\\lambda","Se separan las variables."),
          ("X(0)=X(\\pi)=0\\ \\Rightarrow\\ X=\\operatorname{sen}nx,\\ \\lambda=n^{2}","Los lados verticales fijan X."),
          ("Y''=n^{2}Y,\\ Y(0)=0\\ \\Rightarrow\\ Y=\\operatorname{senh}ny","La base en cero deja el seno hiperbólico."),
          ("u(x,1)=\\operatorname{sen}2x\\ \\Rightarrow\\ u=\\dfrac{\\operatorname{senh}2y}{\\operatorname{senh}2}\\operatorname{sen}2x","Se ajusta el borde de arriba.")]),
   OJO("En Laplace, a diferencia de la onda, en y no hay oscilación sino crecimiento exponencial. Por eso aparece el seno hiperbólico y no el seno.")),
 sec("El valor medio","Valor medio",P("En un disco, la solución es un desarrollo en r y theta, y se cumple una propiedad fuerte."),
   PASOS([("u(r,\\theta)=a_{0}+\\displaystyle\\sum r^{n}(a_{n}\\cos n\\theta+b_{n}\\operatorname{sen}n\\theta)","Solución en un disco, acotada en el centro."),
          ("u(1,\\theta)=3+2\\cos\\theta\\ \\Rightarrow\\ u=3+2r\\cos\\theta","Se lee de la frontera."),
          ("u(0,0)=3","El centro vale el promedio de la frontera."),
          ("u(0,0)=\\dfrac{1}{2\\pi}\\displaystyle\\int_{0}^{2\\pi}u(1,\\theta)\\,d\\theta=3","Propiedad del valor medio.")]),
   OJO("En el disco, la solución debe ser acotada en el origen, y por eso solo aparecen potencias positivas de r. Si no, hay una singularidad en el centro.")),
 eng("La temperatura en una placa","Una placa metálica cuadrada tiene tres lados a 0 grados y el cuarto con un perfil de temperatura que sube y baja. Una vez que se estabiliza, la temperatura interior cumple la ecuación de Laplace.","u(x,y)=\\dfrac{\\operatorname{senh}ny}{\\operatorname{senh}n}\\operatorname{sen}nx",
   [("Lados a cero","tres"),("Borde calentado","seno de n x"),("Decaimiento hacia adentro","rápido para n grande")],"Los detalles finos del borde, que son de frecuencia alta, se atenúan rápido al entrar en la placa. Por eso las placas muestran una temperatura suave adentro aunque el borde sea irregular. En el diseño, se usa para ubicar sensores."),
 completar("Una función armónica en un disco, con valor medio en el centro, cumple que el centro vale el [[hueco]] de la frontera.","u(0,0)=[[hueco]]\\ \\text{de la frontera}",
   [("\\text{promedio}","promedio"),("\\text{maximo}","máximo"),("\\text{minimo}","mínimo")],0,
   ["","El máximo está en la frontera, y no es el valor en el centro.","El mínimo está en la frontera, y no es el valor en el centro."],"Es la propiedad del valor medio.","El centro vale el promedio."),
 error("Alguien resolvió la parte de y en Laplace con la base en cero y se equivocó. Toca el paso que está mal.",
   [("Y''=4Y","La ecuación para n igual a 2.","la ecuación"),
    ("Y=\\operatorname{sen}2y","Este paso es el que falla.","seno"),
    ("Y(0)=0\\ \\checkmark","Se cumple la condición.","la condición")],1,
   "Con Y segunda igual a 4Y, la solución usa exponenciales, y no senos. La que vale cero en 0 es el seno hiperbólico de 2y.",
   "Y=\\operatorname{senh}2y","Con y segunda igual a más 4Y, hay crecimiento exponencial."),
 ordenar("Estos son los pasos para resolver Laplace en un rectángulo, pero están desordenados.",
   [("u=X(x)\\,Y(y)","Se separan las variables"),
    ("X=\\operatorname{sen}nx","Los lados verticales fijan X"),
    ("Y=\\operatorname{senh}ny","La base fija Y"),
    ("u(x,1)=\\operatorname{sen}2x","Se ajusta el borde de arriba")],[2,0,3,1],
   "Primero se separa, luego se fija X, después Y y por último se ajusta el borde.","Se empieza separando las variables."),
]
S+=cierre("Mini simulacro de la ecuación de Laplace",[
 banco("es_c3_01","Las soluciones de Laplace se llaman armónicas."),
 banco("es_c3_02","La condición de Dirichlet."),
 banco("es_c3_03","La solución en el rectángulo."),
 banco("es_c3_06","La propiedad del valor medio.")])
prac=[
 {"titulo":"El rectángulo","grafica":{"draw":1},"bloques":[P("El borde de arriba vale seno de 2x, y los otros tres lados valen cero."),EQ("u_{xx}+u_{yy}=0")]},
 {"titulo":"Sube la altura","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el factor de decaimiento y la altura.")]},
 {"titulo":"El borde","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("\\dfrac{\\operatorname{senh}2}{\\operatorname{senh}2}=1"),P("En el borde de arriba el factor vale 1, y la solución coincide con el dato.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El centro vale el promedio de la frontera."}]}]
preg={"tex":"u\\ \\text{armonica en el disco unidad},\\ u(1,\\theta)=5+4\\cos\\theta.\\ u(0,0)\\ \\text{vale}","opciones":["$5$","$9$","$1$","$4$"],"correcta":0,
 "explicacion":"El valor en el centro es el promedio de la frontera. El promedio de coseno de theta es cero, y queda 5.",
 "verificacion":{"formula":"5+0*x","a":0,"esperado":5},
 "pistas":["Usa la propiedad del valor medio.","Promedia 5 más 4 coseno de theta.","El promedio del coseno en una vuelta es cero."],
 "errores":["","El 9 es el máximo en la frontera, y no el valor en el centro.","El 1 es el mínimo en la frontera, y no el valor en el centro.","El 4 es el coeficiente del coseno, y no el promedio."]}
res=["Las soluciones de la ecuación de Laplace se llaman armónicas, y describen estados de equilibrio.","La separación de variables en un rectángulo da senos en una dirección y senos hiperbólicos en la otra.","El valor de una armónica en el centro de un círculo es el promedio de la frontera."]
write(lesson("es-m3-l4","Lección 4 de 5","Ecuación de Laplace y problemas de frontera",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-laplace.json")
