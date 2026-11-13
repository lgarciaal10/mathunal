import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 1 Cálculo diferencial en varias variables"
XS=[round(0.25*i,3) for i in range(41)]
EL=[{"t":"trazo","puntos":[[str(xv),f"{xv*(10-xv):.4f}"] for xv in XS],"c":3},
    {"t":"punto","p":["x","x*(10-x)"],"c":0},
    {"t":"segmento","a":["x","0"],"b":["x","x*(10-x)"],"c":1}]
graf={"tipo":"plano","x":[-1,11],"y":[-3,28],"a":0.5,"b":9.5,"inicio":2,"elementos":EL,
 "lecturas":[{"rotulo":"posición x sobre la restricción x más y igual a 10","formula":"x"},{"rotulo":"valor de f igual a x por y sobre la restricción","formula":"x*(10-x)"}],
 "etiquetas":["Se recorre la recta x más y igual a 10, y y vale 10 menos x","El producto xy sobre la restricción, con su máximo en el centro"],"etiquetaSlider":"Posición x, de 0.5 a 9.5",
 "alt":"Se recorre la restricción x más y igual a 10 y se mide f igual a x por y. Sobre la restricción, f vale x por 10 menos x, una parábola que abre hacia abajo. Su máximo, 25, ocurre en x igual a 5, donde los gradientes de f y de la restricción son paralelos"}
glos={"lagrange":"El método de los multiplicadores de Lagrange halla extremos de f sujetos a una restricción g igual a c, resolviendo gradiente de f igual a lambda por gradiente de g.",
 "restriccion":"Una restricción es una condición que deben cumplir las variables, como x más y igual a 10.",
 "multiplicador":"El multiplicador lambda es el factor que relaciona los dos gradientes, y mide cuánto cambia el óptimo al mover la restricción.",
 "paralelos":"En el óptimo restringido, el gradiente de f es paralelo al gradiente de la restricción, porque la curva de nivel de f es tangente a la restricción."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Se quiere el mayor valor de x por y, con la restricción de que x más y vale 10."],
 [4,10,"Sobre la restricción, y vale 10 menos x, y el producto queda x por 10 menos x."],
 [10,16,"Con x igual a 2, el producto vale 16. Con x igual a 8 también vale 16, así que el máximo está en medio."],
 [16,20,"Con x igual a 5 el producto vale 25, y es el máximo. Aquí los gradientes son paralelos."],
 [20,24,"El método de Lagrange halla ese punto sin despejar, con gradiente de f igual a lambda por gradiente de g."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,2],[8,2],[10,2],[13,2],[16,5],[18,5],[24,5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Cuando se optimiza una función con una {{gl:restriccion|restricción}}, no basta con que el gradiente sea cero. El método de {{gl:lagrange|Lagrange}} pide que el gradiente de f sea {{gl:paralelos|paralelo}} al de la restricción, con un {{gl:multiplicador|multiplicador}} lambda. Se resuelve junto con la restricción.")),
 sec("Un ejemplo","Un ejemplo",P("Se quiere el máximo de x por y con x más y igual a 10. Mueve x sobre la restricción y mira el valor."),EQ("f=xy,\\quad g=x+y=10,\\qquad \\nabla f=\\lambda\\nabla g"),{"t":"grafica","animar":"dibujar","alt":"El producto xy sobre la restricción"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con x más y igual a 10 y x igual a 2, ¿cuánto vale y?","opciones":[8,2,10,12],"correcta":8,"bien":"Muy bien. y es 10 menos 2, o sea 8, y el producto es 16.","mal":"y es 10 menos x, o sea 8. El producto es 2 por 8, que da 16."}),
 sec("Recorrer la restricción","Recorrido",P("Mira el producto con x igual a 2, 3.5, 5 y 8."),{"t":"acercando","ds":[2,3.5,5,8],"alt":"El producto en cuatro puntos de la restricción"},P("El valor sube hasta x igual a 5 y luego baja, así que el máximo es 25.")),
 sec("El método","Método",P("Se igualan los gradientes y se agrega la restricción."),
   PASOS([("\\nabla f=(y,\\,x),\\quad \\nabla g=(1,\\,1)","Los gradientes."),
          ("y=\\lambda,\\quad x=\\lambda","Se igualan componente por componente."),
          ("x=y,\\quad x+y=10\\ \\Rightarrow\\ x=y=5","Se usa la restricción."),
          ("f(5,5)=25,\\quad \\lambda=5","El valor máximo y el multiplicador.")]),
   OJO("El método da los puntos candidatos, pero no dice si son máximos o mínimos. Se compara el valor de f en los candidatos, o se analiza con otro criterio.")),
 sec("Otro ejemplo","Mínimo",P("Se minimiza la distancia al cuadrado al origen sobre una recta."),
   PASOS([("f=x^{2}+y^{2},\\quad g=x+y=4","Se minimiza sobre la recta."),
          ("\\nabla f=(2x,2y)=\\lambda(1,1)\\ \\Rightarrow\\ x=y","Los gradientes paralelos."),
          ("x+y=4\\ \\Rightarrow\\ x=y=2","Con la restricción."),
          ("f(2,2)=8","El valor mínimo.")]),
   OJO("En este caso hay un mínimo y no hay máximo, porque lejos del origen la función crece sin límite. Revisa siempre qué tipo de extremo es.")),
 eng("El cercado de área máxima","Un ganadero tiene 20 metros de malla para encerrar un corral rectangular. Quiere el área mayor, y el perímetro es la restricción.","A=xy,\\quad 2x+2y=20",
   [("Perímetro","20 m"),("Lados óptimos","5 m por 5 m"),("Área máxima","25 m²")],"El óptimo es un cuadrado, como sale del método de Lagrange. Con una pared ya construida se plantea otra restricción, y cambia la forma óptima."),
 completar("Para optimizar f con la restricción g igual a c, se resuelve el gradiente de f igual a lambda por [[hueco]].","\\nabla f=\\lambda\\,[[hueco]]",
   [("\\nabla g","el gradiente de g"),("g","la función g"),("c","la constante c")],0,
   ["","Un gradiente es un vector, y g es un número.","La constante c no es un vector."],"Los dos lados deben ser vectores.","Es el gradiente de g."),
 error("Alguien resolvió el máximo de x por y con x más y igual a 10 y se equivocó. Toca el paso que está mal.",
   [("\\nabla f=(y,x)=\\lambda(1,1)","Condición de Lagrange.","condición"),
    ("x=\\lambda,\\ y=\\lambda\\ \\Rightarrow\\ x=y=\\lambda=10","Este paso es el que falla.","usa lambda igual a 10"),
    ("f=100","Resultado.","100")],1,
   "Falta usar la restricción x más y igual a 10. Con x igual a y, x más y es 2x, así que x es 5. Entonces el máximo es 25.",
   "x=y,\\ x+y=10\\ \\Rightarrow\\ x=y=5","Usa la restricción para hallar x."),
 ordenar("Estos son los pasos del método de Lagrange, pero están desordenados.",
   [("\\nabla f=\\lambda\\nabla g","Se plantea la condición"),
    ("g=c","Se agrega la restricción"),
    ("(x,y,\\lambda)","Se resuelve el sistema"),
    ("f\\ \\text{en cada candidato}","Se comparan los valores")],[2,0,3,1],
   "Se plantea la condición, se agrega la restricción, se resuelve y se comparan los valores.","Se empieza con la condición de los gradientes."),
]
S+=cierre("Mini simulacro de multiplicadores de Lagrange",[
 banco("cv_c1_05","El máximo de x por y con x más y igual a 10."),
 banco("cv_c1_17","La condición de Lagrange."),
 pnum("El valor mínimo de $x^{2}+y^{2}$ sujeto a $x+y=4$ es:","8",0.01,"El mínimo ocurre en x igual a y igual a 2, y vale 4 más 4, o sea 8.")])
prac=[
 {"titulo":"La restricción","grafica":{"draw":1},"bloques":[P("Se optimiza f sobre la restricción."),EQ("f=xy,\\quad x+y=10")]},
 {"titulo":"Recorre la recta","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la posición x y el valor de f.")]},
 {"titulo":"El máximo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5,"bloques":[EQ("f(5,5)=25"),P("En x igual a 5, el producto es máximo, y vale 25.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Los gradientes son paralelos en el óptimo."}]}]
preg={"tex":"\\max\\ xy\\ \\text{con}\\ x+y=10\\ \\text{vale}","opciones":["$25$","$10$","$50$","$100$"],"correcta":0,
 "explicacion":"Con Lagrange, x es igual a y, y la restricción da x igual a y igual a 5. El producto es 25.",
 "verificacion":{"formula":"5*5+0*x","a":0,"esperado":25},
 "pistas":["Iguala los gradientes de f y de g.","Eso da x igual a y.","Usa la restricción para hallar x."],
 "errores":["","El 10 es la suma, y no el producto.","El 50 duplica el producto correcto.","El 100 es el cuadrado de la suma."]}
res=["El método de Lagrange resuelve gradiente de f igual a lambda por gradiente de g, junto con la restricción.","En el óptimo restringido, los gradientes son paralelos.","Se comparan los valores de f en los candidatos."]
write(lesson("cv-m1-l7","Lección 7 de 7","Multiplicadores de Lagrange",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-lagrange.json")
