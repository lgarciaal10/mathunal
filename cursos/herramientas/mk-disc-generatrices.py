import os, math
os.environ['CURSO_FU']='Matemáticas Discretas'; os.environ['BANCO']='discretas'
from mklib import *
from fundlib import *
MOD="Módulo 3 Recurrencias, grafos y teoría de números"
EL=[{"t":"trazo","puntos":[[str(round(-0.9+0.1*k,2)),f"exp(x*ln({round(1+(-0.9+0.1*k),2)}))"] for k in range(20)],"c":0},
    {"t":"recta","p":["1","0"],"dir":["0","1"],"c":3,"guion":True,"guia":True},
    {"t":"punto","p":["1","exp(x*ln(2))"],"c":2}]
graf={"tipo":"plano","x":[-1.4,2.2],"y":[-3,36],"a":0,"b":5,"inicio":2,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"coeficiente de t al cuadrado en (1 más t) a la n","formula":"x*(x-1)/2"},{"rotulo":"valor del polinomio en t igual a 1, la suma de los coeficientes","formula":"exp(x*ln(2))"}],
 "etiquetas":["Combinaciones C de n sobre 2","Dos elevado a n, el total de subconjuntos"],"etiquetaSlider":"Exponente n, de 0 a 5",
 "alt":"La curva del polinomio 1 más t elevado a la n, para t entre menos 0.9 y 1.0. Un punto marca el valor en t igual a 1, que es dos elevado a n. Al subir n la curva crece más rápido. Los coeficientes del polinomio son las combinaciones C de n sobre k"}
glos={"generatriz":"La función generatriz de una sucesión es la serie cuyos coeficientes son los términos de la sucesión.",
 "binomio":"El binomio de Newton dice que el coeficiente de t elevado a k en 1 más t elevado a n es C de n sobre k.",
 "producto":"El producto de funciones generatrices cuenta las formas de combinar elecciones independientes.",
 "geometrica":"La serie geométrica 1 más x más x al cuadrado y siguientes tiene suma 1 sobre 1 menos x, para x pequeño."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La curva es 1 más t elevado a n, la función generatriz de las combinaciones."],
 [4,9,"Los coeficientes del polinomio son los números C de n sobre k. Con n igual a 2, el polinomio es 1 más 2t más t al cuadrado."],
 [9,14,"En t igual a 1 el polinomio vale 2 elevado a n, porque es la suma de todos los coeficientes."],
 [14,19,"Con n igual a 5, el coeficiente de t al cuadrado es 10, que es C de 5 sobre 2."],
 [19,22,"Una función generatriz guarda una sucesión entera como los coeficientes de una serie."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[6,2],[9,2],[11,4],[14,4],[15,5],[22,5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[14,22]}}
S=[
 sec("La idea",None,P("Una {{gl:generatriz|función generatriz}} guarda una sucesión como los coeficientes de una serie, y así las operaciones con series cuentan cosas. El {{gl:binomio|binomio}} 1 más t elevado a n genera las combinaciones. El {{gl:producto|producto}} de funciones generatrices cuenta combinaciones de elecciones. Y la serie {{gl:geometrica|geométrica}} genera la sucesión de unos.")),
 sec("Un ejemplo","Un ejemplo",P("El polinomio 1 más t elevado a n reúne las combinaciones C de n sobre k como coeficientes. Mueve n y observa la curva y su valor en t igual a 1."),EQ("(1+t)^{n}=\\displaystyle\\sum_{k=0}^{n}\\dbinom{n}{k}t^{k}"),{"t":"grafica","animar":"dibujar","alt":"La curva del polinomio"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El polinomio 1 más t, elevado a 2, es 1 más 2t más t al cuadrado. ¿Cuánto suman sus coeficientes?","opciones":[2,3,4,5],"correcta":4,"bien":"Muy bien. Suman 1 más 2 más 1, o sea 4, que es 2 al cuadrado. Más abajo se ve el punto.","mal":"Suman 4, porque 1 más 2 más 1 es 4, que es 2 al cuadrado. Más abajo se ve el punto."}),
 sec("Cambiando el exponente","El exponente",P("Mira el polinomio con n igual a 1, 2, 4 y 5."),{"t":"acercando","ds":[1,2,4,5],"alt":"El polinomio para cuatro valores de n"},P("La suma de los coeficientes es siempre 2 elevado a n. Es el valor del polinomio en t igual a 1.")),
 sec("Series y sucesiones","Series",P("La misma idea sirve para otras sucesiones."),
   PASOS([("\\dfrac{1}{1-t}=1+t+t^{2}+t^{3}+\\cdots","La sucesión 1, 1, 1, y siguientes."),
          ("(1+t)^{2}=1+2t+t^{2}","Los coeficientes son 1, 2 y 1."),
          ("\\dfrac{1}{1-2t}=1+2t+4t^{2}+8t^{3}+\\cdots","La sucesión de las potencias de 2."),
          ("\\dfrac{1}{1-t-t^{2}}=1+t+2t^{2}+3t^{3}+5t^{4}+\\cdots","La función generatriz de Fibonacci.")]),
   OJO("En una serie infinita, t se trata como un símbolo formal y no se evalúa en un número cualquiera. Lo que importa son los coeficientes. En un polinomio como uno más t, elevado a la n, sí se puede evaluar, y t igual a 1 da la suma de los coeficientes.")),
 sec("Contar con productos","Productos",P("El producto de funciones generatrices cuenta combinaciones de elecciones independientes."),
   PASOS([("(1+t)(1+t)=1+2t+t^{2}","Dos elecciones de tomar o no tomar un objeto."),
          ("\\dfrac{1}{(1-t)(1-t^{2})(1-t^{5})}","Monedas de 1, 2 y 5, con cualquier cantidad de cada una."),
          ("[t^{10}]\\ \\text{vale}\\ 10","Hay 10 formas de reunir 10 con esas monedas.")]),
   OJO("Cada factor representa un tipo de elección. El coeficiente de t elevado a n en el producto cuenta las formas de que el total sea n.")),
 eng("Armar una longitud con espaciadores","Se quiere armar una pila de 10 milímetros con espaciadores de 1, 2 y 5 milímetros, usando cuantos se quiera de cada tipo. Cada tipo aporta un factor a la función generatriz, y el coeficiente de t elevado a 10 cuenta las formas.","\\dfrac{1}{(1-t)(1-t^{2})(1-t^{5})}",
   [("Espaciadores","1, 2 y 5 mm"),("Altura total","10 mm"),("Formas de armarla","10")],"Hay 6 formas sin usar espaciadores de 5, 3 usando uno, y 1 usando dos, para un total de 10. Con la función generatriz se obtiene el mismo resultado sin listar casos, y se puede cambiar la altura para ver cuántas formas hay. Es un conteo de combinaciones, y no dice cuál de ellas conviene en la práctica."),
 completar("Se desarrolla 1 más t, elevado a 2. Falta el coeficiente del medio.","(1+t)^{2}=1+[[hueco]]\\,t+t^{2}",
   [("2","dos"),("1","uno"),("3","tres")],0,
   ["","Uno sería el coeficiente de (1 más t) a la 1, y aquí el exponente es 2.","Tres no sale, porque los coeficientes son 1, 2 y 1."],"El coeficiente del medio es C de 2 sobre 1.","C de 2 sobre 1 es 2."),
 error("Alguien halló el coeficiente de t al cuadrado en 1 más t, elevado a 4, y se equivocó en un paso. Toca el paso que está mal.",
   [("(1+t)^{4}=\\displaystyle\\sum_{k}\\dbinom{4}{k}t^{k}","El binomio.","el desarrollo con combinaciones"),
    ("[t^{2}]=\\dbinom{4}{2}","El coeficiente de t al cuadrado.","hay que calcular C de 4 sobre 2"),
    ("\\dbinom{4}{2}=4","Este paso es el que falla.","C de 4 sobre 2 vale 4")],2,
   "C de 4 sobre 2 es 4 por 3 entre 2, o sea 6. El valor 4 es C de 4 sobre 1.",
   "\\dbinom{4}{2}=6","Calcula 4 por 3 y divide entre 2."),
 ordenar("Estos son los pasos para desarrollar 1 más t, elevado a 2, pero están desordenados.",
   [("(1+t)^{2}=(1+t)(1+t)","Se escribe como un producto"),
    ("=1+t+t+t^{2}","Se multiplica término a término"),
    ("=1+2t+t^{2}","Se juntan los términos iguales"),
    ("\\text{coeficientes}\\ 1,\\ 2,\\ 1","Se leen los coeficientes")],[2,0,3,1],
   "Se escribe el producto, se multiplica, se juntan términos y se leen los coeficientes.","Se empieza escribiendo el producto."),
]
S+=cierre("Mini simulacro de funciones generatrices",[
 pnum("El coeficiente de $t^{2}$ en $(1+t)^{6}$ es:","15",0.001,"Es $\\binom{6}{2}=15$."),
 pnum("La suma de los coeficientes de $(1+t)^{4}$ es:","16",0.001,"Es el valor en $t=1$, o sea $2^{4}=16$."),
 pmcq("La función generatriz de la sucesión $1,1,1,1,\\ldots$ es:",["$\\dfrac{1}{1-t}$","$1+t$","$\\dfrac{1}{1+t}$","$(1-t)^{2}$"],0,"La serie geométrica $1+t+t^{2}+\\cdots$ suma $\\dfrac{1}{1-t}$.")])
prac=[
 {"titulo":"El polinomio","grafica":{"draw":1},"bloques":[P("La curva de 1 más t elevado a n."),EQ("(1+t)^{n}")]},
 {"titulo":"Cambia n","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 5. Abajo se leen el coeficiente de t al cuadrado y la suma de los coeficientes.")]},
 {"titulo":"Con n igual a 5","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5,"bloques":[EQ("\\dbinom{5}{2}=10,\\qquad 2^{5}=32"),P("Con n igual a 5, el coeficiente de t al cuadrado es 10 y los coeficientes suman 32.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El coeficiente de t elevado a k en 1 más t elevado a n es C de n sobre k."}]}]
preg={"tex":"\\text{El coeficiente de}\\ t^{3}\\ \\text{en}\\ (1+t)^{5}\\ \\text{es}","opciones":["$10$","$5$","$15$","$20$"],"correcta":0,
 "explicacion":"El coeficiente es la combinación C de 5 sobre 3, que es 5 por 4 por 3 entre 3 por 2 por 1, o sea 10.",
 "verificacion":{"formula":"5*4*3/(3*2*1)+0*x","a":0,"esperado":10},
 "pistas":["El coeficiente es una combinación.","Es C de 5 sobre 3.","Calcula 5 por 4 por 3 entre 6."],
 "errores":["","Cinco es C de 5 sobre 1, el coeficiente de t.","Quince es C de 6 sobre 2, y no 5 sobre 3.","Veinte es P de 5 y 2, que no es una combinación."]}
res=["Una función generatriz guarda una sucesión como los coeficientes de una serie.","El coeficiente de t elevado a k en 1 más t elevado a n es C de n sobre k, y la suma de los coeficientes es 2 elevado a n.","El producto de funciones generatrices cuenta combinaciones de elecciones independientes."]
write(lesson("di-m3-l4","Lección 4 de 4","Funciones generatrices",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Discretas"),"disc-generatrices.json")
