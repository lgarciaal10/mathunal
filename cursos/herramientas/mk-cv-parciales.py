import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 1 Cálculo diferencial en varias variables"
XS=[round(-2.6+0.13*i,3) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(xv),f"{xv}*{xv}*x+x*x*x"] for xv in XS],"c":0},
    {"t":"recta","p":["1","x+x*x*x"],"dir":["1","2*x"],"c":1},
    {"t":"punto","p":["1","x+x*x*x"],"c":1}]
graf={"tipo":"plano","x":[-2.6,2.6],"y":[-2,34],"a":0,"b":2.5,"inicio":2,"elementos":EL,
 "lecturas":[{"rotulo":"pendiente en x igual a 1, f sub x igual a 2 x y","formula":"2*x"},{"rotulo":"altura del punto, f de 1 y","formula":"x+x*x*x"}],
 "etiquetas":["La pendiente de la tangente es la derivada parcial respecto a x","La altura del punto cuando x vale 1 y y vale la posición del deslizador"],"etiquetaSlider":"Valor fijo de y, de 0 a 2.5",
 "alt":"Se corta la superficie z igual a x al cuadrado por y más y al cubo con un plano y constante. El corte es una parábola, y la recta tangente en x igual a 1 tiene pendiente igual a la derivada parcial respecto a x, que es 2 por y. Al subir y, la parábola se cierra y la pendiente crece"}
glos={"parcial":"La derivada parcial respecto a x se calcula derivando respecto a x y tratando a y como una constante.",
 "corte":"Un corte es la curva que resulta de fijar una variable. Con y fija, la superficie se convierte en una curva en x.",
 "clairaut":"El teorema de Clairaut dice que las derivadas parciales mixtas son iguales cuando son continuas.",
 "mixta":"Una derivada parcial mixta es la que se obtiene derivando primero respecto a una variable y luego respecto a la otra."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La función es x al cuadrado por y más y al cubo. Se fija el valor de y y queda una curva en x."],
 [4,10,"La derivada parcial respecto a x es la pendiente de esa curva, y vale 2 por x por y."],
 [10,16,"Con y igual a 0.5 la parábola es ancha, y la pendiente en x igual a 1 es 1."],
 [16,20,"Con y igual a 2 la parábola se cierra, y la pendiente es 4. Es el valor de f sub x en 1 y 2."],
 [20,24,"Para la derivada respecto a y se fija x y se deriva respecto a y, y en 1 y 2 da 13."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.2],[8,0.2],[10,0.5],[13,0.5],[16,2],[18,2],[24,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("La {{gl:parcial|derivada parcial}} mide cómo cambia la función al mover una sola variable, con las demás fijas. Geométricamente es la pendiente de un {{gl:corte|corte}} de la superficie. Las derivadas parciales de segundo orden incluyen las {{gl:mixta|mixtas}}, que por el teorema de {{gl:clairaut|Clairaut}} son iguales cuando son continuas.")),
 sec("Un ejemplo","Un ejemplo",P("La función es x al cuadrado por y más y al cubo. Mueve el valor fijo de y y mira la pendiente en x igual a 1."),EQ("f(x,y)=x^{2}y+y^{3},\\qquad f_{x}=2xy,\\qquad f_{y}=x^{2}+3y^{2}"),{"t":"grafica","animar":"dibujar","alt":"El corte de la superficie con y fija y su tangente"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Al derivar x al cuadrado por y respecto a x, ¿qué papel tiene y?","opciones":["Es una constante","Se deriva también","Desaparece","Se iguala a x"],"correcta":"Es una constante","bien":"Muy bien. Se deriva solo respecto a x, y y se trata como un número fijo.","mal":"Al derivar respecto a x, la variable y se trata como una constante, igual que un número."}),
 sec("Varios cortes","Cortes",P("Mira el corte con y igual a 0.2, 0.5, 1.2 y 2."),{"t":"acercando","ds":[0.2,0.5,1.2,2],"alt":"El corte con cuatro valores de y"},P("Con y igual a 2, la pendiente de la tangente en x igual a 1 es 4.")),
 sec("Calcular derivadas parciales","Cálculo",P("Se deriva respecto a una variable y la otra se trata como constante."),
   PASOS([("f(x,y)=x^{2}y+y^{3}","La función."),
          ("f_{x}=2xy+0=2xy","Respecto a x, y es constante y y al cubo desaparece."),
          ("f_{y}=x^{2}+3y^{2}","Respecto a y, x es constante."),
          ("f_{x}(1,2)=4,\\quad f_{y}(1,2)=1+12=13","Evaluadas en el punto 1 y 2.")]),
   OJO("En f sub x, el término y al cubo desaparece porque no depende de x. Pero en f sub y, el término x al cuadrado por y deja x al cuadrado.")),
 sec("Derivadas mixtas","Mixtas",P("Se derivan dos veces, y el orden no importa si las derivadas son continuas."),
   PASOS([("f=x^{2}y^{3}","La función."),
          ("f_{x}=2xy^{3}\\ \\Rightarrow\\ f_{xy}=6xy^{2}","Primero x y luego y."),
          ("f_{y}=3x^{2}y^{2}\\ \\Rightarrow\\ f_{yx}=6xy^{2}","Primero y y luego x."),
          ("f_{xy}=f_{yx}","Coinciden, como dice Clairaut.")]),
   OJO("La igualdad de las mixtas pide continuidad en un entorno del punto. Hay funciones extrañas donde no se cumple, pero no suelen aparecer en los cursos.")),
 eng("La ley de los gases ideales","La presión de un gas depende del volumen y la temperatura según P igual a n R T entre V. Las derivadas parciales dicen cómo cambia la presión al mover solo una variable.","P=\\dfrac{nRT}{V},\\quad P_{T}=\\dfrac{nR}{V},\\quad P_{V}=-\\dfrac{nRT}{V^{2}}",
   [("Respecto a la temperatura","P sube con T"),("Respecto al volumen","P baja con V"),("Unidad","presión entre kelvin")],"Con las derivadas parciales se estima cuánto cambia la presión cuando solo se calienta, o solo se comprime. En un tanque real se combinan los dos cambios con la diferencial total."),
 completar("Para f igual a x al cuadrado por y al cubo, la derivada parcial respecto a y es [[hueco]].","f_{y}=[[hueco]]",
   [("3x^{2}y^{2}","3 x al cuadrado y al cuadrado"),("2xy^{3}","2 x y al cubo"),("x^{2}y^{3}","la misma función")],0,
   ["","Esa es la derivada respecto a x, y no respecto a y.","Si la derivada fuera la misma función, no habría derivado nada."],"Se trata x como constante y se deriva y al cubo.","Queda 3 x al cuadrado por y al cuadrado."),
 error("Alguien calculó f sub x de x al cuadrado por y más y al cubo, y se equivocó. Toca el paso que está mal.",
   [("f=x^{2}y+y^{3}","La función.","la función"),
    ("f_{x}=2xy+3y^{2}","Este paso es el que falla.","deriva también y al cubo"),
    ("f_{x}(1,2)=4+12=16","Resultado.","16")],1,
   "Al derivar respecto a x, y al cubo es una constante y su derivada es cero. Entonces f sub x es 2xy, y en el punto 1 y 2 vale 4.",
   "f_{x}=2xy\\ \\Rightarrow\\ f_{x}(1,2)=4","Los términos sin x tienen derivada cero."),
 ordenar("Estos son los pasos para calcular una derivada mixta, pero están desordenados.",
   [("f=x^{2}y^{3}","Se parte de la función"),
    ("f_{x}=2xy^{3}","Se deriva respecto a x"),
    ("f_{xy}=6xy^{2}","Se deriva respecto a y"),
    ("f_{xy}(1,1)=6","Se evalúa")],[2,0,3,1],
   "Primero la función, luego x, luego y y al final se evalúa.","Se empieza con la función."),
]
S+=cierre("Mini simulacro de derivadas parciales",[
 banco("cv_c1_01","Se deriva respecto a y, con x como constante."),
 banco("cv_c1_06","f sub x de 1 y 2 es 2 por 1 por 2."),
 banco("cv_c1_07","f sub y de 1 y 2 es 1 más 3 por 4."),
 banco("cv_c1_08","La igualdad de las mixtas pide continuidad.")])
prac=[
 {"titulo":"La función","grafica":{"draw":1},"bloques":[P("Se fija y y se mira el corte en x."),EQ("f(x,y)=x^{2}y+y^{3}")]},
 {"titulo":"Cambia y","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la pendiente de la tangente en x igual a 1 y la altura del punto.")]},
 {"titulo":"El punto 1 y 2","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("f_{x}(1,2)=4,\\quad f(1,2)=10"),P("Con y igual a 2, la pendiente es 4 y la altura es 10.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Al derivar respecto a x, y es constante."}]}]
preg={"tex":"f(x,y)=3x^{2}+xy.\\ f_{x}(1,2)\\ \\text{es}","opciones":["$8$","$6$","$2$","$3$"],"correcta":0,
 "explicacion":"f sub x es 6x más y, y en el punto 1 y 2 vale 6 más 2, o sea 8.",
 "verificacion":{"formula":"6*1+2+0*x","a":0,"esperado":8},
 "pistas":["Deriva respecto a x, con y constante.","La derivada de 3 x al cuadrado es 6x.","La derivada de x por y es y."],
 "errores":["","El 6 olvida la derivada de x por y, que es y.","El 2 es solo el valor de y.","El 3 es un coeficiente, pero no la derivada."]}
res=["La derivada parcial respecto a x se calcula con las demás variables constantes, y es la pendiente de un corte.","Las derivadas mixtas coinciden cuando son continuas, por el teorema de Clairaut.","Se evalúa en el punto pedido al final."]
write(lesson("cv-m1-l2","Lección 2 de 7","Derivadas parciales",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-parciales.json")
