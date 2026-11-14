import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
from fundlib import *
MOD="Módulo 1 Errores y ecuaciones no lineales"
A=[1,1,1.25,1.375,1.375,1.40625]; Bv=[2,1.5,1.5,1.5,1.4375,1.4375]
M=[(a+b)/2 for a,b in zip(A,Bv)]
LA=lagr(A); LB=lagr(Bv); LM=lagr(M)
EL=[{"t":"trazo","puntos":[[str(round(0.8+0.05*k,2)),str(round((0.8+0.05*k)**2-2,4))] for k in range(0,31)],"c":0},
 {"t":"segmento","a":[LA,"0"],"b":[LA,f"({LA})*({LA})-2"],"c":1,"guia":True,"guion":True},
 {"t":"segmento","a":[LB,"0"],"b":[LB,f"({LB})*({LB})-2"],"c":1,"guia":True,"guion":True},
 {"t":"punto","p":[LM,"0"],"c":2},
 {"t":"punto","p":[LA,"0"],"c":3},{"t":"punto","p":[LB,"0"],"c":3}]
graf={"tipo":"plano","x":[0.5,2.5],"y":[-1.9,3.0],"a":0,"b":5,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"punto medio p del intervalo","formula":"("+LM+")"},{"rotulo":"ancho b menos a del intervalo","formula":"("+LB+")-("+LA+")"}],
 "etiquetas":["Punto medio de a y b, la nueva aproximación de la raíz","El ancho se reduce a la mitad en cada iteración"],"etiquetaSlider":"Iteración, de 0 a 5",
 "alt":"La curva y igual a x al cuadrado menos 2 entre 0.8 y 2.3. Dos segmentos verticales marcan los extremos a y b del intervalo, y un punto en el eje marca el punto medio. En cada iteración el intervalo se queda con la mitad donde la función cambia de signo, y se acerca a la raíz de 2, que vale 1.4142"}
glos={"biseccion":"El método de bisección parte de un intervalo donde la función cambia de signo, calcula el punto medio y se queda con la mitad donde sigue el cambio de signo.",
 "bolzano":"El teorema del valor intermedio dice que si f es continua en a, b y f de a y f de b tienen signos opuestos, hay una raíz en el intervalo.",
 "tolerancia":"La tolerancia es el error máximo que se acepta. La iteración se detiene cuando la cota de error es menor que ella.",
 "cota":"La cota de error de la bisección después de n pasos es b menos a, dividido entre 2 elevado a n."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La función es x al cuadrado menos 2, y su raíz es raíz de 2, cerca de 1.4142. Se parte del intervalo de 1 a 2, donde cambia de signo."],
 [4,9,"El punto medio es 1.5. Como f de 1.5 es positiva, la raíz queda entre 1 y 1.5."],
 [9,14,"En la siguiente iteración el intervalo mide 0.5, y el punto medio es 1.25. Ahora f es negativa, y la raíz queda entre 1.25 y 1.5."],
 [14,20,"Cada iteración reduce el ancho a la mitad. Después de 5 iteraciones el intervalo mide 0.03125."],
 [20,24,"Así se acota el error sin conocer la raíz, porque el error es menor que el ancho del intervalo."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[5,0],[6,1],[9,1],[10,2],[14,2],[15,3],[17,4],[19,5],[24,5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[14,24]}}
S=[
 sec("La idea",None,P("Resolver f de x igual a 0 sin fórmula es lo que hace un método numérico. El método de {{gl:biseccion|bisección}} usa el teorema del {{gl:bolzano|valor intermedio}}. Si f cambia de signo en un intervalo, hay una raíz adentro. Se parte el intervalo por la mitad y se conserva la mitad donde el signo cambia, y así se acorrala la raíz. Su {{gl:cota|cota de error}} se conoce de antemano, y se compara con la {{gl:tolerancia|tolerancia}}.")),
 sec("Un ejemplo","Un ejemplo",P("Se busca la raíz de x al cuadrado menos 2 entre 1 y 2. Avanza las iteraciones y mira cómo se estrecha el intervalo."),EQ("p=\\dfrac{a+b}{2},\\qquad f(a)\\,f(b)<0"),{"t":"grafica","animar":"dibujar","alt":"La curva y los extremos del intervalo"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En el intervalo de 1 a 2, f de 1 vale menos 1 y f de 2 vale 2. ¿Cuánto vale el producto de f de 1 por f de 2?","opciones":[-2,-1,1,2],"correcta":-2,"bien":"Muy bien. Es menos 2, un producto negativo, que indica un cambio de signo. Más abajo se ve el método.","mal":"Es menos 2, porque menos 1 por 2 da menos 2. Un producto negativo indica cambio de signo, y hay una raíz adentro. Más abajo se ve el método."}),
 sec("Las iteraciones","Las iteraciones",P("Mira el intervalo en las iteraciones 0, 1, 2 y 5."),{"t":"acercando","ds":[0,1,2,5],"alt":"El intervalo en cuatro iteraciones"},P("El ancho es 1, 0.5, 0.25 y 0.03125. Se reduce a la mitad en cada paso.")),
 sec("El algoritmo","El algoritmo",P("Cada iteración repite los mismos pasos."),
   PASOS([("f(a)\\,f(b)<0","Se comprueba que hay cambio de signo en el intervalo."),
          ("p=\\dfrac{a+b}{2}","Se calcula el punto medio."),
          ("f(1)=-1,\\ f(2)=2,\\ p_{1}=1.5,\\ f(1.5)=0.25>0\\ \\Rightarrow\\ [1,\\,1.5]","Con el ejemplo, la raíz queda en la primera mitad."),
          ("\\left|p_{n}-p\\right|\\le\\dfrac{b-a}{2^{n}}","La cota de error después de n iteraciones.")]),
   OJO("Si f no cambia de signo, bisección no se puede aplicar, aunque haya raíz. Pasa con las raíces dobles, como la de x al cuadrado, donde la función toca el eje sin cruzarlo.")),
 sec("Cuántas iteraciones","Cuántas",P("La cota permite saber de antemano cuántas iteraciones hacen falta."),
   PASOS([("\\dfrac{1-0}{2^{n}}<0.01","Se parte de un intervalo de ancho 1 y se pide un error menor que 0.01."),
          ("2^{n}>100\\ \\Rightarrow\\ n>\\log_{2}100\\approx6.64","Se despeja n."),
          ("n=7","Siempre se redondea hacia arriba, porque n es un entero.")]),
   OJO("La bisección es lenta pero segura. Gana una cifra binaria en cada paso, que son unas 3.3 iteraciones por cada cifra decimal.")),
 eng("Una raíz que viene de una medición","Hay casos en que f no tiene fórmula y se obtiene midiendo, como la fuerza de un actuador a distintas posiciones. Se busca la posición donde la fuerza se anula. Bisección solo necesita evaluar f, sin derivadas.","n=7\\ \\Rightarrow\\ \\text{error}<\\dfrac{1}{2^{7}}\\approx0.008",
   [("Intervalo inicial","[1, 2]"),("Evaluaciones de f tras 7 pasos","9"),("Error máximo","menor que 0.01")],"Con 2 evaluaciones iniciales y una por cada iteración, hacen falta 9 mediciones para tener un error menor que 0.01. Es poco, y además se sabe de antemano. Por eso bisección es la primera opción cuando la función es costosa de evaluar y no hay derivada. Si f tiene ruido de medición, hay que revisar que el cambio de signo no sea ruido."),
 completar("Se calcula cuántas iteraciones de bisección hacen falta para un error menor que 0.01 desde un intervalo de ancho 1.","2^{n}>100\\ \\Rightarrow\\ n=[[hueco]]",
   [("7","siete"),("6","seis"),("10","diez")],0,
   ["","Con 6 iteraciones, 2 elevado a 6 es 64, que no supera 100. Hay que redondear hacia arriba.","Diez cumple, pero no es el menor n que sirve."],"Busca el menor n con 2 elevado a n mayor que 100.","2 elevado a 7 es 128, que supera 100. Con 6 se queda en 64."),
 error("Alguien hizo una iteración de bisección y se equivocó en un paso. Toca el paso que está mal.",
   [("f(1)=-1<0,\\quad f(2)=2>0","Hay cambio de signo.","el cambio de signo se cumple"),
    ("p_{1}=1.5,\\quad f(1.5)=0.25>0","El punto medio.","el punto medio es 1.5"),
    ("\\text{La raíz queda en}\\ [1.5,\\ 2]","Este paso es el que falla.","la raíz queda en la mitad derecha")],2,
   "f de 1 es negativa y f de 1.5 es positiva, así que el cambio de signo está en el intervalo de 1 a 1.5. En la mitad de 1.5 a 2 los dos extremos son positivos.",
   "[1,\\ 1.5]","Compara los signos de los dos extremos de cada mitad."),
 ordenar("Estos son los pasos de una iteración de bisección, pero están desordenados.",
   [("f(a)\\,f(b)<0","Se comprueba el cambio de signo"),
    ("p=\\dfrac{a+b}{2}","Se calcula el punto medio"),
    ("\\text{se evalúa}\\ f(p)","Se evalúa la función en el punto medio"),
    ("\\text{se conserva la mitad con cambio de signo}","Se escoge la nueva mitad")],[2,0,3,1],
   "Se comprueba el cambio de signo, se parte por la mitad, se evalúa y se conserva la mitad donde cambia el signo.","Se empieza comprobando el cambio de signo."),
]
S+=cierre("Mini simulacro de bisección y regla falsa",[
 banco("mn_c1_06","La bisección necesita que $f$ cambie de signo, o sea, $f(a)\\,f(b)<0$."),
 banco("mn_c1_08","Como $f(1)<0$ y $f(1.5)>0$, el cambio de signo está en la primera mitad."),
 banco("mn_c1_09","$\\dfrac{1}{2^{n}}<0.01\\Rightarrow n=7$.")])
prac=[
 {"titulo":"El intervalo","grafica":{"draw":1},"bloques":[P("La curva de x al cuadrado menos 2 y el intervalo inicial de 1 a 2."),EQ("f(x)=x^{2}-2")]},
 {"titulo":"Itera","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 5. Abajo se leen el punto medio y el ancho del intervalo.")]},
 {"titulo":"Iteración 5","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5,"bloques":[EQ("[1.40625,\\ 1.4375]\\ \\ni\\ \\sqrt{2}"),P("Con la iteración 5, el intervalo mide 0.03125 y contiene a la raíz de 2.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Usa la cota de error y busca el menor n que sirve."}]}]
preg={"tex":"\\text{Iteraciones de bisección en}\\ [0,2]\\ \\text{para un error menor que}\\ 0.01","opciones":["$8$","$7$","$6$","$10$"],"correcta":0,
 "explicacion":"La cota es 2 entre 2 elevado a n, y debe ser menor que 0.01. Eso da 2 elevado a n mayor que 200. Como 2 elevado a 7 es 128 y 2 elevado a 8 es 256, el menor n es 8.",
 "verificacion":{"formula":"8+0*x","a":0,"esperado":8},
 "pistas":["La cota es el ancho entre 2 elevado a n.","Hay que resolver 2 entre 2 elevado a n menor que 0.01.","2 elevado a n debe superar 200, y el primero que lo hace es 2 elevado a 8."],
 "errores":["","Con 7 iteraciones, 2 elevado a 7 es 128, que no supera 200.","Con 6 iteraciones, 2 elevado a 6 es 64, mucho menos de 200.","Con 10 se cumple, pero 8 ya alcanza."]}
res=["La bisección parte un intervalo con cambio de signo por la mitad y conserva la mitad donde el signo cambia.","La cota de error es b menos a entre 2 elevado a n, y se conoce de antemano.","Es lenta pero segura, y solo necesita evaluar f."]
write(lesson("mn-m1-l1","Lección 1 de 4","Bisección y regla falsa",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-biseccion.json")
