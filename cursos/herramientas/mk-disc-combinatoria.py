import os, math
os.environ['CURSO_FU']='Matemáticas Discretas'; os.environ['BANCO']='discretas'
from mklib import *
from fundlib import *
MOD="Módulo 2 Conjuntos, conteo y combinatoria"
EL=[]
for k in range(9):
    vals=[math.comb(n,k) for n in range(9)]
    L=lagr(vals)
    EL.append({"t":"poligono","puntos":[[str(k),"0"],[str(k+1),"0"],[str(k+1),L],[str(k),L]],"c":2 if k==2 else 3})
graf={"tipo":"plano","x":[-1.0,10.0],"y":[-9,78],"a":0,"b":8,"inicio":4,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"combinaciones C(n, 2), la barra roja","formula":"x*(x-1)/2"},{"rotulo":"suma de todas las barras, dos elevado a n","formula":"exp(x*ln(2))"}],
 "etiquetas":["Subconjuntos de 2 elementos de un conjunto de n","Total de subconjuntos del conjunto de n elementos"],"etiquetaSlider":"Número de elementos n, de 0 a 8",
 "alt":"Barras que muestran las combinaciones C de n sobre k para k de 0 a 8. Con n igual a 4 las alturas son 1, 4, 6, 4 y 1. La barra de k igual a 2 está en rojo, y la suma de todas las barras es dos elevado a n"}
glos={"factorial":"El factorial de n es el producto de los números de 1 a n. Cuenta las formas de ordenar n objetos distintos.",
 "permutacion":"Una permutación de k elementos tomados de n es una selección ordenada. Su número es n factorial dividido entre n menos k factorial.",
 "combinacion":"Una combinación de k elementos tomados de n es una selección sin orden. Su número es n factorial entre k factorial y n menos k factorial.",
 "pascal":"El triángulo de Pascal tiene en la fila n los números C de n sobre k. Cada número es la suma de los dos que tiene encima."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Cada barra es una cantidad de combinaciones. La barra k cuenta cuántos subconjuntos de tamaño k tiene un conjunto de n elementos."],
 [4,10,"Con n igual a 4 la fila es 1, 4, 6, 4, 1. Las barras son simétricas, porque escoger k es lo mismo que dejar fuera n menos k."],
 [10,16,"Con n igual a 6, la barra roja, la de k igual a 2, vale 15. Esa es la combinación 6 sobre 2."],
 [16,20,"Con n igual a 8, la barra central llega a 70, y la suma de todas las barras es 256."],
 [20,24,"La suma de la fila siempre es dos elevado a n, que es el total de subconjuntos."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[6,4],[9,4],[10,6],[15,6],[16,8],[22,8],[24,8]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[10,24]}}
S=[
 sec("La idea",None,P("Contar de cuántas formas se puede escoger o acomodar un grupo es el corazón de la combinatoria. Si el orden importa, se usan {{gl:permutacion|permutaciones}}. Si no importa, se usan {{gl:combinacion|combinaciones}}. Ambas se calculan con el {{gl:factorial|factorial}}, y las combinaciones forman el {{gl:pascal|triángulo de Pascal}}.")),
 sec("Un ejemplo","Un ejemplo",P("Cada barra muestra cuántos subconjuntos de cada tamaño tiene un conjunto de n elementos. La barra roja es la de tamaño 2."),EQ("\\dbinom{n}{k}=\\dfrac{n!}{k!\\,(n-k)!}"),{"t":"grafica","animar":"dibujar","alt":"Las barras de las combinaciones"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"De un grupo de 4 personas se escogen 2 para un comité, sin importar el orden. Si el orden importara habría 4 por 3, o sea 12 formas. ¿Cuántos comités hay si no importa el orden?","opciones":[4,6,8,12],"correcta":6,"bien":"Muy bien. Cada comité se contó 2 veces, así que son 12 entre 2, o sea 6. Más abajo se ve la barra.","mal":"Son 6. En las 12 formas ordenadas cada comité aparece 2 veces, una por cada orden, así que se divide entre 2. Más abajo se ve la barra."}),
 sec("Recorriendo la fila","La fila",P("Mira las barras para n igual a 0, 4, 6 y 8."),{"t":"acercando","ds":[0,4,6,8],"alt":"Las barras para cuatro valores de n"},P("Con n igual a 6, la barra roja vale 15. Y en todos los casos la suma de las barras es dos elevado a n.")),
 sec("Permutaciones y combinaciones","Fórmulas",P("Se parte del factorial y se ajusta según importe o no el orden."),
   PASOS([("n!=n(n-1)\\cdots 2\\cdot1,\\quad 5!=120","Las formas de ordenar n objetos distintos."),
          ("P(n,k)=\\dfrac{n!}{(n-k)!},\\quad P(5,2)=\\dfrac{120}{6}=20","Selecciones ordenadas de k entre n."),
          ("\\dbinom{n}{k}=\\dfrac{P(n,k)}{k!},\\quad \\dbinom{5}{2}=\\dfrac{20}{2}=10","Se divide entre las k factorial formas de ordenar lo escogido."),
          ("\\dbinom{n}{k}=\\dbinom{n}{n-k}","Escoger k es lo mismo que dejar fuera n menos k.")])),
 sec("Triángulo de Pascal","Pascal",P("Los números C de n sobre k se pueden obtener sumando."),
   PASOS([("\\dbinom{n}{k}=\\dbinom{n-1}{k-1}+\\dbinom{n-1}{k}","Cada número es la suma de los dos de arriba."),
          ("1,\\ 4,\\ 6,\\ 4,\\ 1","La fila de n igual a 4."),
          ("\\dbinom{6}{2}=15,\\quad \\dbinom{6}{3}=20","Con n igual a 6, el valor central es 20."),
          ("\\displaystyle\\sum_{k=0}^{n}\\dbinom{n}{k}=2^{n}","La suma de cada fila es dos elevado a n.")]),
   OJO("Antes de usar una fórmula hay que decidir si el orden importa. Un comité de 3 personas es una combinación, pero una directiva con presidente, secretario y tesorero es una permutación.")),
 eng("Elegir sensores para calibrar","En una planta hay 6 sensores y se necesita escoger 2 para calibrarlos hoy. No importa cuál se calibre primero, así que es una combinación. En cambio, ordenar 4 tareas de mantenimiento en una secuencia sí importa el orden, y es una permutación.","\\dbinom{6}{2}=15,\\qquad 4!=24",
   [("Sensores a escoger","2 de 6"),("Formas de escoger","15"),("Secuencias de 4 tareas","24")],"Para planear pruebas, saber cuántas combinaciones hay indica el tamaño de la búsqueda. Con 6 sensores hay 15 parejas, pero con 20 sensores ya son 190. Y si el orden importa, la cantidad crece mucho más rápido, porque 10 tareas se pueden ordenar de más de 3 millones de formas."),
 completar("Se calcula una combinación a partir de una permutación. Falta el factorial por el que se divide.","\\dbinom{5}{2}=\\dfrac{P(5,2)}{[[hueco]]}",
   [("2!","dos factorial"),("5!","cinco factorial"),("3!","tres factorial")],0,
   ["","Cinco factorial es el total de formas de ordenar los 5 elementos, y aquí solo se ordenan los 2 escogidos.","Tres factorial correspondería a ordenar 3 elementos, y se escogen 2."],"Se divide entre las formas de ordenar lo escogido.","Con 2 elementos escogidos hay 2 factorial órdenes, que es 2."),
 error("Alguien calculó 6 sobre 2 y se equivocó en un paso. Toca el paso que está mal.",
   [("\\dbinom{6}{2}=\\dfrac{6!}{2!\\,4!}","La fórmula.","la fórmula de la combinación"),
    ("=\\dfrac{6\\cdot5\\cdot4!}{2\\cdot4!}","Se desarrolla 6 factorial.","se desarrolla y se simplifica 4 factorial"),
    ("=6\\cdot5=30","Este paso es el que falla.","queda 30")],2,
   "Después de simplificar el 4 factorial queda 6 por 5 sobre 2, y falta dividir entre 2. El resultado es 30 entre 2, o sea 15.",
   "=\\dfrac{6\\cdot5}{2}=15","Mira qué pasó con el 2 del denominador."),
 ordenar("Estos son los pasos para calcular P(5, 2), pero están desordenados.",
   [("P(5,2)=\\dfrac{5!}{(5-2)!}","Se escribe la fórmula"),
    ("5!=120,\\quad 3!=6","Se calculan los factoriales"),
    ("\\dfrac{120}{6}","Se arma el cociente"),
    ("20","Se calcula")],[2,0,3,1],
   "Se escribe la fórmula, se calculan los factoriales, se arma el cociente y se calcula.","Se empieza con la fórmula."),
]
S+=cierre("Mini simulacro de permutaciones y combinaciones",[
 banco("di_c2_03","$\\dfrac{6\\cdot5}{2}=15$."),
 banco("di_c2_12","$\\dfrac{5!}{3!}=20$."),
 banco("di_c2_15","La simetría de las combinaciones es $\\binom{n}{k}=\\binom{n}{n-k}$.")])
prac=[
 {"titulo":"Las barras","grafica":{"draw":1},"bloques":[P("Las combinaciones de n elementos tomados de a k, para cada k."),EQ("\\dbinom{n}{k}")]},
 {"titulo":"Recorre n","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 8. Abajo se leen la combinación C de n sobre 2 y la suma de la fila.")]},
 {"titulo":"Con n igual a 6","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":6,"bloques":[EQ("\\dbinom{6}{2}=15,\\qquad 2^{6}=64"),P("Con n igual a 6, la barra roja vale 15 y las barras suman 64.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":6},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Un comité no tiene orden, así que se usan combinaciones."}]}]
preg={"tex":"\\text{Comités de 3 personas que se forman con 5 personas}","opciones":["$10$","$60$","$20$","$15$"],"correcta":0,
 "explicacion":"En un comité no importa el orden, así que se usa la combinación 5 sobre 3, que es 5 por 4 por 3 entre 3 por 2 por 1, o sea 10. El valor 60 sería si el orden importara.",
 "verificacion":{"formula":"5*4*3/(3*2*1)+0*x","a":0,"esperado":10},
 "pistas":["Un comité no tiene orden.","Se usa la combinación 5 sobre 3.","Es 5 por 4 por 3 entre 6."],
 "errores":["","Sesenta es 5 por 4 por 3, que cuenta cada comité varias veces, una por cada orden.","Veinte es P de 5 y 2, y no corresponde a escoger 3 de 5 sin orden.","Quince es 6 sobre 2, y no 5 sobre 3."]}
res=["Si el orden importa se usan permutaciones, y si no importa se usan combinaciones.","P(n, k) es n factorial entre n menos k factorial, y C(n, k) es P(n, k) entre k factorial.","La suma de una fila del triángulo de Pascal es dos elevado a n, y C(n, k) es igual a C(n, n menos k)."]
write(lesson("di-m2-l1","Lección 1 de 4","Permutaciones y combinaciones",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Discretas"),"disc-combinatoria.json")
