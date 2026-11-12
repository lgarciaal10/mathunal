import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 3 Funciones, trigonometría y geometría analítica"
TS=[-1+8*k/100 for k in range(101)]
graf={"tipo":"plano","x":[-3.5,9.5],"y":[-5.5,9],"a":0,"b":6,"inicio":3,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"{t:.4f}*{t:.4f}-6*{t:.4f}+5"] for t in TS],"c":2},
  {"t":"recta","p":["3","0"],"dir":["0","1"],"guion":True,"c":3,"guia":True},
  {"t":"recta","p":["0","-4"],"dir":["1","0"],"guion":True,"c":3,"guia":True},
  {"t":"segmento","a":["x","0"],"b":["x","x*x-6*x+5"],"c":1,"guia":True,"guion":True},
  {"t":"punto","p":["x","x*x-6*x+5"],"c":2}],
 "lecturas":[{"rotulo":"valor de x","formula":"x"},{"rotulo":"f(x)","formula":"x*x-6*x+5"}],
 "etiquetas":["Valor de x","Valor de la función f de x"],"etiquetaSlider":"Valor de x",
 "alt":"La parábola x al cuadrado menos 6x más 5, con vértice en 3, menos 4. Corta el eje en 1 y en 5, y es simétrica respecto a la recta vertical x igual a 3"}
glos={"vertice":"El vértice de una parábola es su punto más alto o más bajo. Está en x igual a menos b sobre 2a, y ahí está el valor máximo o mínimo de la función cuadrática.",
 "pendiente":"La pendiente de una recta mide cuánto sube y por cada unidad que avanza x. Con dos puntos se calcula como la diferencia de las y sobre la diferencia de las x.",
 "completarcuadrado":"Completar el cuadrado es reescribir una expresión cuadrática como un binomio al cuadrado más una constante, y deja ver el vértice."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Esta es la parábola x al cuadrado, menos 6x, más 5. Es una función cuadrática."],
 [4,8,"El punto más bajo es el vértice. La recta vertical punteada es el eje de simetría, en x igual a 3."],
 [8,14,"Mueve x. A los dos lados del eje los valores se repiten, porque la parábola es simétrica."],
 [14,18,"En x igual a 1 y en x igual a 5 la función vale 0. Son los ceros, las soluciones de x al cuadrado menos 6x más 5 igual a 0."],
 [18,22,"En el vértice, x igual a 3, la función vale menos 4. Es el valor mínimo."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,3],[8,3],[11,0],[13,6],[14,1],[16,5],[17,3],[22,3]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Las funciones más sencillas son la lineal, cuya gráfica es una recta, y la cuadrática, cuya gráfica es una parábola. De la recta importa su {{gl:pendiente|pendiente}}. De la parábola importan sus ceros y su {{gl:vertice|vértice}}, que es donde está el máximo o el mínimo.")),
 sec("Un ejemplo","Un ejemplo",P("Mira una parábola y sus puntos importantes."),EQ("f(x)=x^{2}-6x+5=(x-3)^{2}-4"),{"t":"grafica","animar":"dibujar","alt":"La parábola"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Para x al cuadrado menos 6x más 5, el vértice está en x igual a menos b sobre 2a. Con b igual a menos 6 y a igual a 1, ¿cuánto vale?","opciones":[-3,3,6,-6],"correcta":3,"bien":"Muy bien. Vale 3. Allí está el valor mínimo.","mal":"Vale 3, porque menos menos 6 sobre 2 es 3. Allí está el valor mínimo."}),
 sec("Moviendo el punto","Moviendo x",P("Mira el valor de la función en varios puntos."),{"t":"acercando","ds":[3,0,1,5],"alt":"El valor de la función en varios puntos"},P("En x igual a 1 y 5 vale 0, y en el vértice, x igual a 3, vale menos 4. Los puntos a la misma distancia de 3 tienen el mismo valor.")),
 sec("La función lineal","Lineal",P("Una recta queda determinada por su pendiente y un punto."),
   PASOS([("m=\\dfrac{y_{2}-y_{1}}{x_{2}-x_{1}}","La pendiente con dos puntos."),
          ("y=mx+b","La forma con pendiente y corte con el eje y."),
          ("2x-4y=8\\ \\Rightarrow\\ y=\\tfrac{1}{2}x-2\\ \\Rightarrow\\ m=0.5","Se despeja y para leer la pendiente.")]),
   OJO("Una pendiente positiva sube hacia la derecha y una negativa baja. Con pendiente 0 la recta es horizontal.")),
 sec("La función cuadrática","Cuadrática",P("Con completar el cuadrado se ve el vértice, y con la factorización se ven los ceros."),
   PASOS([("x^{2}-6x+5=(x-3)^{2}-9+5=(x-3)^{2}-4","Se completa el cuadrado. El vértice es 3, menos 4."),
          ("x^{2}-6x+5=(x-1)(x-5)","La factorización da los ceros 1 y 5."),
          ("x^{2}+2x+5=(x+1)^{2}+4\\ \\Rightarrow\\ \\text{mínimo}\\ 4","Otro ejemplo, con mínimo 4 en x igual a menos 1.")]),
   OJO("Si el coeficiente de x al cuadrado es positivo, la parábola abre hacia arriba y tiene un mínimo. Si es negativo, abre hacia abajo y tiene un máximo.")),
 eng("El corral de área máxima","Se tienen 40 metros de cerca para encerrar un corral rectangular. Si un lado mide x, el otro mide 20 menos x, y el área es una función cuadrática de x.","A(x)=x\\,(20-x)=-x^{2}+20x",
   [("Cerca","40 m"),("Lado óptimo","10 m"),("Área máxima","100 m²")],"El coeficiente de x al cuadrado es negativo, así que la parábola abre hacia abajo y tiene un máximo. El vértice está en x igual a 10, y ahí el área es 100 metros cuadrados. Es el cuadrado de lado 10. Esto supone que se usa toda la cerca y que el terreno es plano."),
 completar("Se completa el cuadrado de x al cuadrado menos 6x más 5.","x^{2}-6x+5=(x-[[hueco]])^{2}-4",
   [("3","tres"),("6","seis"),("-3","menos tres")],0,
   ["","El número dentro del paréntesis es la mitad del coeficiente de x, y no el coeficiente completo.","Con x más 3 el término del medio saldría con signo positivo."],"Es la mitad de 6.","La mitad de 6 es 3."),
 error("Alguien halló el vértice de x al cuadrado menos 6x más 5 y se equivocó en un paso. Toca el paso que está mal.",
   [("x_{v}=-\\dfrac{b}{2a}","La fórmula del vértice.","la fórmula del vértice"),
    ("x_{v}=-\\dfrac{-6}{2}=-3","Este paso es el que falla.","menos menos 6 sobre 2 es menos 3"),
    ("f(-3)=9+18+5=32","El valor.","f de menos 3 es 32")],1,
   "Menos por menos da más. Menos menos 6 es 6, y 6 sobre 2 es 3. El vértice está en x igual a 3.",
   "x_{v}=-\\dfrac{-6}{2}=3","Cuidado con los signos al reemplazar b."),
 ordenar("Estos son los pasos para hallar el mínimo de x al cuadrado más 2x más 5, pero están desordenados.",
   [("x^{2}+2x+5","La función"),
    ("(x+1)^{2}-1+5","Se completa el cuadrado"),
    ("(x+1)^{2}+4","Se suman las constantes"),
    ("\\text{mínimo}\\ 4\\ \\text{en}\\ x=-1","El resultado")],[2,0,3,1],
   "Se completa el cuadrado, se suman las constantes y se lee el vértice.","Se empieza con la función."),
]
S+=cierre("Mini simulacro de función lineal y cuadrática",[
 banco("mb_c3_06","Se completa el cuadrado, $x^2-6x+5=(x-3)^2-4$, y el vértice es $(3,-4)$."),
 banco("mb_c3_07","Se despeja $y=\\tfrac{1}{2}x-2$, así que la pendiente es $0.5$."),
 banco("mb_c3_09","Se completa el cuadrado, $(x+1)^2+4$, y el mínimo es $4$.")])
prac=[
 {"titulo":"La parábola","grafica":{"draw":1,"guide":1},"bloques":[P("Una parábola con su eje de simetría y su vértice."),EQ("f(x)=x^{2}-6x+5")]},
 {"titulo":"Mueve x","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee el valor de la función.")]},
 {"titulo":"El vértice","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("f(3)=-4"),P("En x igual a 3 la función alcanza su mínimo.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Resta las y y resta las x en el mismo orden."}]}]
preg={"tex":"\\text{La pendiente de la recta por}\\ (1,2)\\ \\text{y}\\ (3,8)\\ \\text{es}","opciones":["$3$","$\\tfrac{1}{3}$","$6$","$5$"],"correcta":0,
 "explicacion":"La pendiente es la diferencia de las y sobre la diferencia de las x. Es 8 menos 2, sobre 3 menos 1, o sea 6 sobre 2, que es 3.",
 "verificacion":{"formula":"(8-2)/(3-1)+0*x","a":0,"esperado":3},
 "pistas":["La pendiente es la variación de y sobre la variación de x.","Resta 8 menos 2 arriba y 3 menos 1 abajo.","Queda 6 sobre 2."],
 "errores":["","Esa es la pendiente al revés, con la variación de x arriba.","Ese es solo el cambio de y. Falta dividir entre el cambio de x.","Ese valor sale de sumar en vez de restar. La pendiente usa diferencias."]}
res=["La pendiente es la diferencia de las y sobre la diferencia de las x.","El vértice de una parábola está en x igual a menos b sobre 2a, y ahí está el máximo o el mínimo.","Completar el cuadrado muestra el vértice, y factorizar muestra los ceros."]
write(lesson("mb-m3-l3","Lección 3 de 4","Función lineal y cuadrática",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=6,curso="Matemáticas Básicas"),"matbas-linealcuad.json")
