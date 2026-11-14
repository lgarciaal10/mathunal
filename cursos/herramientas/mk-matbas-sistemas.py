import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 2 Ecuaciones, inecuaciones y sistemas"
graf={"tipo":"plano","x":[-3,11.7],"y":[-1,7],"a":-3,"b":5,"inicio":1,
 "elementos":[{"t":"recta","p":["0","5"],"dir":["1","-1"],"c":2},
  {"t":"recta","p":["0","0-x"],"dir":["1","1"],"c":3,"guia":True},
  {"t":"punto","p":["(5+x)/2","(5-x)/2"],"c":1,"guia":True}],
 "lecturas":[{"rotulo":"x de la solución","formula":"(5+x)/2"},{"rotulo":"y de la solución","formula":"(5-x)/2"}],
 "etiquetas":["Coordenada x del cruce","Coordenada y del cruce"],"etiquetaSlider":"Valor de k en x menos y igual a k",
 "alt":"Las rectas x más y igual a 5 y x menos y igual a k. Su punto de cruce es la solución del sistema. Con k igual a 1 el cruce es el punto 3, 2"}
glos={"sistema":"Un sistema de ecuaciones es un conjunto de ecuaciones que deben cumplirse a la vez. Su solución son los valores de las incógnitas que cumplen todas.",
 "sustitucion":"El método de sustitución despeja una incógnita de una ecuación y la reemplaza en la otra.",
 "eliminacion":"El método de eliminación suma o resta las ecuaciones, multiplicadas por un número si hace falta, para que una incógnita desaparezca."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Dos rectas, x más y igual a 5, y x menos y igual a k. La solución del sistema es el punto donde se cruzan."],
 [4,8,"La recta de la suma es fija. La otra se mueve al cambiar k, y el cruce se mueve con ella."],
 [8,14,"Mueve k. Abajo aparecen las coordenadas del cruce, la x y la y."],
 [14,18,"Con k igual a 1 el cruce es el punto 3, 2. Es la solución de x más y igual a 5 y x menos y igual a 1."],
 [18,22,"Con k igual a 5 el cruce es 5, 0. Al sumar las dos ecuaciones, x vale 5 más k, sobre 2."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[11,-3],[13,5],[14,1],[17,1],[18,5],[22,5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Un {{gl:sistema|sistema de ecuaciones}} lineal con dos incógnitas es un par de rectas. Si se cruzan, hay una sola solución, el punto de cruce. Si son paralelas, no hay solución, y si son la misma recta, hay infinitas. Se resuelve por {{gl:sustitucion|sustitución}} o por {{gl:eliminacion|eliminación}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira dos rectas y el punto donde se cruzan."),EQ("\\begin{cases}x+y=5\\\\ x-y=k\\end{cases}"),{"t":"grafica","animar":"dibujar","alt":"Las dos rectas"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Al sumar x más y igual a 5 con x menos y igual a 1, la y desaparece y queda 2x igual a 6. ¿Cuánto vale x?","opciones":[2,3,5,6],"correcta":3,"bien":"Muy bien. Vale 3. Entonces y vale 2.","mal":"Vale 3, porque 6 entre 2 es 3. Entonces y vale 2."}),
 sec("Moviendo k","Moviendo k",P("Mira cómo se mueve el cruce al cambiar k."),{"t":"acercando","ds":[1,-3,5,3],"alt":"El cruce para varios valores de k"},P("La recta x más y igual a 5 no cambia. Cuando k cambia, la otra recta se desplaza y el cruce se mueve sobre la primera.")),
 sec("Sustitución","Sustitución",P("Se despeja una incógnita y se reemplaza en la otra ecuación."),
   PASOS([("2x+y=7,\\quad x=y-1","El sistema."),
          ("2(y-1)+y=7\\ \\Rightarrow\\ 3y=9\\ \\Rightarrow\\ y=3","Se reemplaza x en la primera ecuación."),
          ("x=y-1=2","Se vuelve a la segunda para hallar x.")]),
   OJO("Al reemplazar una expresión con una suma, hay que ponerla entre paréntesis. 2 por y menos 1 es 2y menos 2, no 2y menos 1.")),
 sec("Eliminación","Eliminación",P("Se suman o se restan las ecuaciones para que una incógnita se cancele."),
   PASOS([("x+y=5,\\quad x-y=1","El sistema."),
          ("2x=6\\ \\Rightarrow\\ x=3","Al sumar, la y desaparece."),
          ("y=5-3=2","Se reemplaza en una ecuación para hallar y.")]),
   OJO("Si ninguna incógnita se cancela, se multiplica una ecuación, o las dos, por un número. Las rectas paralelas dan una contradicción, como 0 igual a 3, y no tienen solución.")),
 eng("Una mezcla de aleaciones","Para hacer 100 kilogramos de una aleación con 45 por ciento de cobre se mezclan otras dos, una con 30 por ciento y otra con 60. Las cantidades salen de un sistema de dos ecuaciones.","\\begin{cases}x+y=100\\\\ 0.3x+0.6y=45\\end{cases}",
   [("Aleación A","30 por ciento de cobre"),("Aleación B","60 por ciento de cobre"),("Resultado","50 kg de cada una")],"La primera ecuación suma los kilogramos y la segunda suma el cobre. Al reemplazar x por 100 menos y, queda 30 más 0.3y igual a 45, y y vale 50. Entonces x también vale 50. El resultado es lógico, porque 45 está justo a mitad de camino entre 30 y 60. Supone que el cobre se mezcla sin pérdidas."),
 completar("Se suman las ecuaciones x más y igual a 5 y x menos y igual a 1.","2x=[[hueco]]",
   [("6","seis"),("4","cuatro"),("1","uno")],0,
   ["","Eso sería restarlas y no sumarlas. Al restar desaparece la x.","Con 1 solo se usó la segunda ecuación. Al sumar se suman también los lados derechos, 5 más 1."],"Al sumar se suman los dos lados derechos.","5 más 1 es 6."),
 error("Alguien resolvió un sistema por sustitución y se equivocó en un paso. Toca el paso que está mal.",
   [("3x+y=9,\\quad y=2x-1\\ \\Rightarrow\\ 3x+(2x-1)=9","Se reemplaza y.","se reemplaza y por 2x menos 1"),
    ("3x+2x+1=9","Este paso es el que falla.","se quita el paréntesis y queda 3x más 2x más 1"),
    ("5x=8\\ \\Rightarrow\\ x=1.6","El resultado.","queda 5x igual a 8")],1,
   "Al quitar el paréntesis, el signo menos se mantiene, porque el paréntesis tiene un signo más delante. Queda 3x más 2x menos 1 igual a 9, o sea 5x igual a 10, y x vale 2.",
   "3x+2x-1=9\\ \\Rightarrow\\ x=2","Fíjate en el signo del 1 al quitar el paréntesis."),
 ordenar("Estos son los pasos para resolver x más y igual a 5, y x menos y igual a 1, por eliminación, pero están desordenados.",
   [("x+y=5,\\ x-y=1","El sistema"),
    ("2x=6","Se suman las ecuaciones"),
    ("x=3","Se despeja x"),
    ("y=5-3=2","Se halla y")],[2,0,3,1],
   "Se suman las ecuaciones, se despeja una incógnita y se reemplaza para hallar la otra.","Se empieza con el sistema."),
]
_hamb=banco("mb_r19_02","Las cuatro hamburguesas y las dos malteadas dan $4x+2y=90$, y las malteadas cuestan $2y=x+2.5$.")
_hamb["texto"]=_hamb["texto"].replace("\\$90","90 dólares").replace("\\$2,5","2,5 dólares")
_hamb["opciones"]=[o.replace(", \\\\ "," y ") for o in _hamb["opciones"]]
S+=cierre("Mini simulacro de sistemas de ecuaciones",[
 banco("mb_c2_15","Al sumar las ecuaciones queda $2x=6$, así que $x=3$ y $y=2$."),
 banco("mb_c2_16","Se reemplaza $x=y-1$ en la primera ecuación y queda $3y-2=7$."),
 _hamb])
prac=[
 {"titulo":"Las rectas","grafica":{"draw":1,"guide":1},"bloques":[P("Dos rectas, que se cruzan en la solución."),EQ("x+y=5,\\quad x-y=k")]},
 {"titulo":"Cambia k","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen las coordenadas del cruce.")]},
 {"titulo":"Un caso","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5,"bloques":[EQ("k=5\\ \\Rightarrow\\ (x,y)=(5,0)"),P("Con k igual a 5 el cruce está sobre el eje horizontal.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Suma o resta las ecuaciones para eliminar una incógnita."}]}]
preg={"tex":"\\begin{cases}x+y=7\\\\ 2x-y=2\\end{cases}\\ \\text{tiene como solución}","opciones":["$(3,4)$","$(4,3)$","$(2,5)$","$(5,2)$"],"correcta":0,
 "explicacion":"Al sumar las ecuaciones, la y se cancela y queda 3x igual a 9, o sea x igual a 3. Entonces y vale 7 menos 3, o sea 4.",
 "verificacion":{"formula":"2*x-4","a":3,"esperado":2},
 "pistas":["Suma las dos ecuaciones.","Queda 3x igual a 9.","Reemplaza x en la primera ecuación."],
 "errores":["","El orden está al revés. Ese par cumple la primera ecuación, pero con 2x menos y da 5 y no 2.","Ese par suma 7, pero con 2x menos y da menos 1 y no 2.","Ese par suma 7, pero con 2x menos y da 8 y no 2."]}
res=["La solución de un sistema es el punto de cruce de las rectas.","Por sustitución se despeja una incógnita y se reemplaza. Por eliminación se suman o restan las ecuaciones.","Las rectas paralelas no tienen solución, y la misma recta tiene infinitas."]
write(lesson("mb-m2-l4","Lección 4 de 5","Sistemas de ecuaciones",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=3,curso="Matemáticas Básicas"),"matbas-sistemas.json")
