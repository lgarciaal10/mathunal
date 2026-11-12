import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 1 Álgebra y expresiones"
TS=[-0.5+5.0*k/100 for k in range(101)]
graf={"tipo":"plano","x":[-0.5,4.5],"y":[-7.5,7.5],"a":0,"b":4,"inicio":0,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"{t:.4f}*{t:.4f}*{t:.4f}-6*{t:.4f}*{t:.4f}+11*{t:.4f}-6"] for t in TS],"c":2},
  {"t":"recta","p":["x","0"],"dir":["0","1"],"guion":True,"c":3,"guia":True},
  {"t":"punto","p":["x","x*x*x-6*x*x+11*x-6"],"c":1}],
 "lecturas":[{"rotulo":"valor de c","formula":"x"},{"rotulo":"residuo P(c)","formula":"x*x*x-6*x*x+11*x-6"}],
 "etiquetas":["Valor de c","Residuo al dividir entre x menos c"],"etiquetaSlider":"Valor de c",
 "alt":"La gráfica del polinomio x al cubo menos 6x al cuadrado más 11x menos 6, con un punto que se mueve. Cuando el punto cae sobre el eje, en 1, 2 y 3, el residuo es cero"}
glos={"residuo":"El teorema del residuo dice que el residuo de dividir un polinomio P de x entre x menos c es P de c.",
 "factor":"El teorema del factor dice que x menos c es un factor de P de x si y solo si P de c vale 0, es decir, c es una raíz.",
 "sintetica":"La división sintética es una forma corta de dividir un polinomio entre x menos c usando solo los coeficientes."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Esta es la gráfica del polinomio x al cubo, menos 6x al cuadrado, más 11x, menos 6."],
 [4,8,"Al dividir el polinomio entre x menos c, el residuo es el valor del polinomio en c. El punto marca ese valor."],
 [8,14,"Mueve c. Cuando el punto cae sobre el eje, el residuo es 0 y x menos c es un factor."],
 [14,18,"Pasa en c igual a 1, 2 y 3. Los tres factores dan el polinomio completo, x menos 1, por x menos 2, por x menos 3."],
 [18,22,"Con c igual a 4 el residuo es 6, así que x menos 4 no es un factor."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,1],[12,2],[13,3],[16,3],[17,4],[22,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Un polinomio se puede dividir entre otro, como los números. Dos teoremas ahorran mucho trabajo. El del {{gl:residuo|residuo}} dice cuánto sobra al dividir entre x menos c, sin hacer la división. El del {{gl:factor|factor}} dice cuándo la división es exacta, y eso sirve para factorizar y hallar ceros.")),
 sec("Un ejemplo","Un ejemplo",P("Mira este polinomio de grado 3 y un punto que se mueve sobre él."),EQ("P(x)=x^{3}-6x^{2}+11x-6"),{"t":"grafica","animar":"dibujar","alt":"La gráfica del polinomio"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Para el polinomio P de x igual a x al cuadrado menos 4, ¿cuánto vale P de 2?","opciones":[0,2,4,-4],"correcta":0,"bien":"Muy bien. Vale 0, porque 4 menos 4 es 0. Entonces x menos 2 es un factor.","mal":"Vale 0, porque 2 al cuadrado es 4 y 4 menos 4 es 0. Entonces x menos 2 es un factor."}),
 sec("Moviendo c","Moviendo c",P("Mira el valor del polinomio en distintos valores de c."),{"t":"acercando","ds":[1,2,3,4],"alt":"El valor del polinomio para varios c"},P("En c igual a 1, 2 y 3 el valor es 0. En c igual a 4 es 6, y ese es el residuo de dividir entre x menos 4.")),
 sec("Los dos teoremas","Teoremas",P("Estos son los teoremas, con el ejemplo."),
   PASOS([("P(x)=(x-c)\\,Q(x)+r\\ \\Rightarrow\\ r=P(c)","Teorema del residuo. Se reemplaza x por c y el término con x menos c desaparece."),
          ("P(c)=0\\ \\Leftrightarrow\\ (x-c)\\ \\text{es factor de}\\ P(x)","Teorema del factor. Si el residuo es 0, la división es exacta."),
          ("P(4)=64-96+44-6=6","El residuo de dividir el ejemplo entre x menos 4.")]),
   OJO("Para dividir entre x más 3 se usa c igual a menos 3. Hay que escribir el divisor como x menos c.")),
 sec("Factorizar con una raíz","Factorizar",P("Con una raíz conocida, se divide y queda un polinomio más pequeño."),
   PASOS([("P(1)=1-6+11-6=0\\ \\Rightarrow\\ (x-1)\\ \\text{es factor}","Se prueba con un divisor del término independiente."),
          ("x^{3}-6x^{2}+11x-6=(x-1)\\left(x^{2}-5x+6\\right)","La división da un cuadrático."),
          ("x^{2}-5x+6=(x-2)(x-3)","Se factoriza el cuadrático."),
          ("P(x)=(x-1)(x-2)(x-3)","Los ceros son 1, 2 y 3.")])),
 eng("La caja de una lámina","Se hace una caja sin tapa recortando cuadrados de lado x en las esquinas de una lámina de 30 por 20 centímetros. El volumen es un polinomio de grado 3 en x, y sus ceros dicen qué valores de x no tienen sentido.","V(x)=x\\,(30-2x)(20-2x)",
   [("Lámina","30 por 20 cm"),("Ceros de V","0, 10 y 15"),("Con x de 4 cm","1056 cm³")],"El volumen se anula en x igual a 0, a 10 y a 15. Solo los valores entre 0 y 10 sirven, porque con x igual a 10 la lámina se acaba por el lado corto. Con x igual a 4 centímetros, el volumen es 4 por 22 por 12, o sea 1056 centímetros cúbicos, cerca del máximo. Es un modelo geométrico simple, que no cuenta el espesor del material ni los dobleces."),
 completar("Se divide el polinomio entre x menos 1 y se completa el cociente.","x^{3}-6x^{2}+11x-6=(x-1)\\left(x^{2}-5x+[[hueco]]\\right)",
   [("6","seis"),("5","cinco"),("-6","menos seis")],0,
   ["","Con 5 el producto da un término de x que no coincide con 11x.","Con menos 6 el término constante daría 6 y no menos 6."],"Al multiplicar, el término constante es menos 1 por el término constante del cociente.","Menos 1 por 6 es menos 6, que es el término constante del polinomio."),
 error("Alguien calculó el residuo de dividir x al cubo, menos 3x al cuadrado, más 2x, más 4, entre x menos 3, y se equivocó en un paso. Toca el paso que está mal.",
   [("r=P(3)","El teorema del residuo.","el residuo es P de 3"),
    ("P(3)=27-9+6+4","Este paso es el que falla.","P de 3 es 27 menos 9 más 6 más 4"),
    ("r=28","El resultado.","el residuo es 28")],1,
   "El término de 3x al cuadrado en x igual a 3 vale 3 por 9, o sea 27, y no 9. El valor correcto es 27 menos 27 más 6 más 4, que es 10.",
   "P(3)=27-27+6+4=10","Fíjate en el segundo término."),
 ordenar("Estos son los pasos para factorizar x al cubo, menos 6x al cuadrado, más 11x, menos 6, pero están desordenados.",
   [("P(1)=0","Se prueba una raíz"),
    ("(x-1)\\ \\text{es factor}","Por el teorema del factor"),
    ("P(x)=(x-1)\\left(x^{2}-5x+6\\right)","Se divide"),
    ("P(x)=(x-1)(x-2)(x-3)","Se factoriza el cuadrático")],[2,0,3,1],
   "Se halla una raíz, se divide y se factoriza lo que queda.","Se empieza probando una raíz."),
]
S+=cierre("Mini simulacro de polinomios",[
 banco("mb_c1_14","Por el teorema del residuo, se calcula $P(2)=8-8+2-5=-3$."),
 banco("mb_c1_15","Se calcula $P(1)=1-6+11-6=0$, así que $x=1$ es una raíz."),
 banco("mb_c1_16","Se factoriza $x^2-x-6=(x-3)(x+2)$, y los ceros son $3$ y $-2$.")])
prac=[
 {"titulo":"El polinomio","grafica":{"draw":1,"guide":1},"bloques":[P("Un polinomio de grado 3 con un punto que se mueve."),EQ("P(x)=x^{3}-6x^{2}+11x-6")]},
 {"titulo":"Cambia c","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee el residuo, que es el valor del polinomio en c.")]},
 {"titulo":"Una raíz","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("P(3)=0"),P("En c igual a 3 el residuo es 0, así que x menos 3 es un factor.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Reemplaza x por c y calcula."}]}]
preg={"tex":"\\text{El residuo de dividir}\\ x^{3}+2x-4\\ \\text{entre}\\ x-1\\ \\text{es}","opciones":["$-1$","$-7$","$1$","$-4$"],"correcta":0,
 "explicacion":"Por el teorema del residuo, el residuo es P de 1. Queda 1 más 2 menos 4, que es menos 1.",
 "verificacion":{"formula":"x*x*x+2*x-4","a":1,"esperado":-1},
 "pistas":["El divisor es x menos 1, así que c vale 1.","El residuo es P de 1.","Calcula 1 al cubo, más 2 por 1, menos 4."],
 "errores":["","Ese es P de menos 1. El divisor x menos 1 corresponde a c igual a 1, no a menos 1.","Ese resultado sale de olvidar el menos 4 o de sumarlo con el signo contrario.","Ese es solo el término independiente. Hay que reemplazar también el resto de términos."]}
res=["El residuo de dividir P entre x menos c es P de c.","Si P de c vale 0, entonces x menos c es un factor.","Con una raíz conocida se divide y se factoriza lo que queda."]
write(lesson("mb-m1-l2","Lección 2 de 4","Polinomios y división",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=6,curso="Matemáticas Básicas"),"matbas-polinomios.json")
