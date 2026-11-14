import os, math
os.environ['CURSO_FU']='Matemáticas Discretas'; os.environ['BANCO']='discretas'
from mklib import *
from fundlib import *
MOD="Módulo 3 Recurrencias, grafos y teoría de números"
FIB=[0,1,1,2,3,5,8,13,21,34,55]
RAT=[0]+[FIB[n+1]/FIB[n] for n in range(1,10)]+[0]
RAT=[0]+[round(FIB[n+1]/FIB[n],6) for n in range(1,10)]+[round(89/55,6)]
EL=[]
for n,f in enumerate(FIB):
    EL.append({"t":"poligono","puntos":[[str(n+0.1),"0"],[str(n+0.9),"0"],[str(n+0.9),str(f)],[str(n+0.1),str(f)]],"c":0})
    ind=lagr([1 if j==n else 0 for j in range(11)])
    EL.append({"t":"poligono","puntos":[[str(n+0.1),"0"],[str(n+0.9),"0"],[str(n+0.9),f"{f}*({ind})"],[str(n+0.1),f"{f}*({ind})"]],"c":3})
graf={"tipo":"plano","x":[-1.0,12.0],"y":[-7,62],"a":0,"b":10,"inicio":6,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"término F de n","formula":"("+lagr(FIB)+")"},{"rotulo":"razón entre F de n más 1 y F de n","formula":"("+lagr(RAT)+")"}],
 "etiquetas":["Término de Fibonacci elegido","Cociente entre un término y el anterior, que se acerca a 1.618"],"etiquetaSlider":"Posición n, de 0 a 10",
 "alt":"Barras con los términos de Fibonacci de F de 0 a F de 10, que valen 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 y 55. Cada barra es la suma de las dos anteriores. El término elegido se resalta en verde"}
glos={"recurrencia":"Una relación de recurrencia define cada término a partir de los anteriores, junto con unos valores iniciales.",
 "caracteristica":"La ecuación característica de una recurrencia lineal homogénea se obtiene reemplazando a de n por r elevado a n. Sus raíces dan las soluciones.",
 "fibonacci":"La sucesión de Fibonacci empieza con 1 y 1, y cada término es la suma de los dos anteriores.",
 "cerrada":"Una fórmula cerrada da el término n directamente, sin calcular los anteriores."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Cada barra es un término de Fibonacci. Cada uno es la suma de los dos anteriores."],
 [4,9,"Con n igual a 6, el término es 8, que es 5 más 3."],
 [9,15,"El cociente entre un término y el anterior se acerca a 1.618."],
 [15,19,"Ese número es la raíz positiva de la ecuación característica r al cuadrado menos r menos 1 igual a 0."],
 [19,22,"Resolver una recurrencia es hallar una fórmula cerrada para cada término."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[6,6],[9,6],[10,8],[15,10],[22,10]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[9,22]}}
S=[
 sec("La idea",None,P("Una {{gl:recurrencia|relación de recurrencia}} describe una sucesión diciendo cómo se obtiene cada término a partir de los anteriores. Con valores iniciales queda bien definida. La más famosa es la de {{gl:fibonacci|Fibonacci}}. Para las lineales se usa la {{gl:caracteristica|ecuación característica}}, que lleva a una fórmula {{gl:cerrada|cerrada}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira los términos de Fibonacci. Cada barra es la suma de las dos anteriores, y el cociente entre términos consecutivos se acerca a un número fijo."),EQ("F_{n}=F_{n-1}+F_{n-2},\\qquad F_{1}=F_{2}=1"),{"t":"grafica","animar":"dibujar","alt":"Las barras de Fibonacci"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Fibonacci empieza con 1, 1, 2, 3, 5. ¿Cuál es el término siguiente?","opciones":[6,7,8,9],"correcta":8,"bien":"Muy bien. Es 5 más 3, o sea 8. Más abajo se ve en la barra.","mal":"Es 8, porque es la suma de los dos anteriores, 5 más 3. Más abajo se ve en la barra."}),
 sec("Recorriendo los términos","Los términos",P("Mira los términos con n igual a 0, 6, 8 y 10."),{"t":"acercando","ds":[0,6,8,10],"alt":"Los términos de Fibonacci para cuatro valores de n"},P("El cociente entre términos consecutivos se estabiliza cerca de 1.618, la razón áurea.")),
 sec("Calcular términos","Calcular",P("Con la regla y los valores iniciales se calcula término por término."),
   PASOS([("a_{n}=3a_{n-1},\\ a_{0}=2\\ \\Rightarrow\\ a_{1}=6,\\ a_{2}=18,\\ a_{3}=54","Cada término es el triple del anterior."),
          ("a_{n}=2\\cdot3^{n}","La fórmula cerrada de esta recurrencia."),
          ("F_{1}=F_{2}=1,\\ F_{3}=2,\\ F_{4}=3,\\ F_{5}=5,\\ F_{6}=8","Los primeros términos de Fibonacci.")])),
 sec("La ecuación característica","Característica",P("Para recurrencias lineales de segundo orden se busca una solución de la forma r elevado a n."),
   PASOS([("a_{n}=a_{n-1}+2a_{n-2}\\ \\Rightarrow\\ r^{2}-r-2=0","Se reemplaza a de n por r elevado a n y se divide entre r elevado a n menos 2."),
          ("(r-2)(r+1)=0\\ \\Rightarrow\\ r=2\\ \\text{o}\\ r=-1","Las raíces."),
          ("a_{n}=A\\,2^{n}+B\\,(-1)^{n}","La solución general, con A y B según los valores iniciales."),
          ("a_{n}=5a_{n-1}-6a_{n-2}\\ \\Rightarrow\\ r^{2}=5r-6","Otro ejemplo, con raíces 2 y 3.")]),
   OJO("La ecuación característica pasa todos los términos al mismo lado con el signo cambiado. Un error de signo en ese paso da raíces equivocadas.")),
 eng("La altura de los rebotes","Una pelota se suelta desde 2 metros y en cada rebote alcanza el 80 por ciento de la altura anterior. La altura del rebote n cumple la recurrencia h de n igual a 0.8 por h de n menos 1. Su fórmula cerrada es 2 por 0.8 elevado a n.","h_{n}=0.8\\,h_{n-1},\\quad h_{n}=2\\cdot0.8^{n}",
   [("Altura inicial","2 m"),("Factor por rebote","0.8"),("Altura tras 5 rebotes","0.66 m")],"Después de 5 rebotes la altura es 2 por 0.8 elevado a 5, o sea 0.66 metros. Con la fórmula cerrada no hace falta calcular los 4 rebotes anteriores. La misma idea sirve para el saldo de una deuda con interés, o para la señal que se amortigua en un circuito."),
 completar("Se calcula el primer término de la recurrencia a de n igual a 3 por a de n menos 1, con a de 0 igual a 2.","a_{1}=3\\cdot2=[[hueco]]",
   [("6","seis"),("5","cinco"),("9","nueve")],0,
   ["","Cinco sería sumar, y la regla multiplica por 3.","Nueve sería el triple de 3, y el valor inicial es 2."],"Se multiplica el valor inicial por 3.","3 por 2 es 6."),
 error("Alguien halló la ecuación característica de a de n igual a a de n menos 1 más 2 por a de n menos 2 y se equivocó en un paso. Toca el paso que está mal.",
   [("a_{n}=a_{n-1}+2a_{n-2}","La recurrencia.","la regla de recurrencia"),
    ("r^{n}=r^{n-1}+2r^{n-2}","Se reemplaza a de n por r elevado a n.","se reemplaza por potencias de r"),
    ("r^{2}+r-2=0","Este paso es el que falla.","queda r al cuadrado más r menos 2")],2,
   "Al dividir entre r elevado a n menos 2 queda r al cuadrado igual a r más 2. Pasando todo al mismo lado queda r al cuadrado menos r menos 2 igual a 0. El signo de r cambia.",
   "r^{2}-r-2=0","Pasa todos los términos a un lado."),
 ordenar("Estos son los pasos para calcular a de 3 en la recurrencia a de n igual a 3 por a de n menos 1, con a de 0 igual a 2, pero están desordenados.",
   [("a_{0}=2","Se parte del valor inicial"),
    ("a_{1}=3\\cdot2=6","Se calcula a de 1"),
    ("a_{2}=3\\cdot6=18","Se calcula a de 2"),
    ("a_{3}=3\\cdot18=54","Se calcula a de 3")],[2,0,3,1],
   "Se parte del valor inicial y se aplica la regla una vez por cada término.","Se empieza con el valor inicial."),
]
S+=cierre("Mini simulacro de relaciones de recurrencia",[
 banco("di_c3_01","$a_1=6$, $a_2=18$, $a_3=54$."),
 banco("di_c3_05","Se pasa todo a un lado, $r^2-r-2=0$, con raíces $2$ y $-1$."),
 banco("di_c3_07","$1,1,2,3,5,8$.")])
prac=[
 {"titulo":"Fibonacci","grafica":{"draw":1},"bloques":[P("Los términos de la sucesión de Fibonacci."),EQ("F_{n}=F_{n-1}+F_{n-2}")]},
 {"titulo":"Recorre n","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 10. Abajo se leen el término y el cociente con el siguiente.")]},
 {"titulo":"El cociente","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":10,"bloques":[EQ("\\dfrac{89}{55}=1.6182"),P("Con n igual a 10, el cociente ya está muy cerca de 1.618.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":10},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Aplica la regla paso a paso desde el valor inicial."}]}]
preg={"tex":"\\text{Si}\\ a_{n}=2a_{n-1}+1\\ \\text{con}\\ a_{0}=1,\\ \\text{entonces}\\ a_{3}=","opciones":["$15$","$8$","$9$","$7$"],"correcta":0,
 "explicacion":"a de 1 es 2 por 1 más 1, o sea 3. a de 2 es 2 por 3 más 1, o sea 7. Y a de 3 es 2 por 7 más 1, o sea 15.",
 "verificacion":{"formula":"2*(2*(2*1+1)+1)+1+0*x","a":0,"esperado":15},
 "pistas":["Calcula a de 1 con la regla.","Son 3 y luego 7.","El siguiente es 2 por 7 más 1."],
 "errores":["","Ocho sería 2 elevado a 3, que no incluye el sumando 1 de cada paso.","Nueve sale de detenerse un paso antes y sumar mal.","Siete es a de 2, y se pide a de 3."]}
res=["Una recurrencia define cada término a partir de los anteriores, con valores iniciales.","La ecuación característica de a de n igual a a de n menos 1 más 2 por a de n menos 2 es r al cuadrado menos r menos 2.","Las raíces de la característica dan la fórmula cerrada, y en Fibonacci el cociente de términos se acerca a 1.618."]
write(lesson("di-m3-l1","Lección 1 de 4","Relaciones de recurrencia",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Discretas"),"disc-recurrencias.json")
