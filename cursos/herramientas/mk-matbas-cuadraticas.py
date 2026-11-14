import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 2 Ecuaciones, inecuaciones y sistemas"
TS=[-1+7.5*k/100 for k in range(101)]
graf={"tipo":"plano","x":[-1,6.5],"y":[-7,8.5],"a":0,"b":8,"inicio":6,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"{t:.4f}*{t:.4f}-5*{t:.4f}+x"] for t in TS],"c":2},
  {"t":"recta","p":["0","0"],"dir":["1","0"],"guion":True,"c":3,"guia":True},
  {"t":"punto","p":["0","x"],"c":1}],
 "lecturas":[{"rotulo":"término q","formula":"x"},{"rotulo":"discriminante 25-4q","formula":"25-4*x"}],
 "etiquetas":["Valor de q","Discriminante de x al cuadrado menos 5x más q"],"etiquetaSlider":"Valor de q",
 "alt":"La parábola x al cuadrado menos 5x más q. Con q igual a 6 corta el eje en 2 y 3. Con q igual a 6.25 solo lo toca, y con q mayor no lo corta, porque el discriminante es negativo"}
glos={"discriminante":"El discriminante de a x al cuadrado más b x más c es b al cuadrado menos 4 a c. Si es positivo hay dos soluciones reales, si es cero hay una doble y si es negativo no hay reales.",
 "formulageneral":"La fórmula general da las soluciones de a x al cuadrado más b x más c igual a 0 como menos b más o menos la raíz del discriminante, todo sobre 2a.",
 "raices":"Las raíces de una ecuación son los valores de x que la hacen cierta. En la gráfica de la función son los cortes con el eje x."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Esta es la parábola x al cuadrado, menos 5x, más q. Las soluciones de la ecuación igual a 0 son los puntos donde corta el eje horizontal."],
 [4,8,"Con q igual a 6 corta en 2 y en 3. La ecuación se factoriza como x menos 2 por x menos 3."],
 [8,14,"Al bajar q la parábola baja y los cortes se separan. Al subir q se acercan."],
 [14,18,"Con q igual a 6.25 el discriminante vale 0. La parábola solo toca el eje, en 2.5, y hay una solución doble."],
 [18,22,"Con q igual a 8 el discriminante es negativo. La parábola no toca el eje y no hay soluciones reales."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,6],[8,6],[11,3],[14,6.25],[17,6.25],[18,8],[22,8]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Una ecuación lineal se resuelve despejando x. Una ecuación cuadrática puede tener dos soluciones, una o ninguna, y se resuelve factorizando o con la {{gl:formulageneral|fórmula general}}. El {{gl:discriminante|discriminante}} dice cuántas soluciones reales hay antes de calcularlas.")),
 sec("Un ejemplo","Un ejemplo",P("Mira cómo cambia la parábola, y con ella las soluciones, al cambiar el término q."),EQ("x^{2}-5x+q=0"),{"t":"grafica","animar":"dibujar","alt":"La parábola"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Para x al cuadrado menos 5x más 6, el discriminante es b al cuadrado menos 4ac. Con b igual a menos 5, a igual a 1 y c igual a 6, ¿cuánto vale?","opciones":[1,25,-1,49],"correcta":1,"bien":"Muy bien. Vale 1, porque 25 menos 24 es 1. Es positivo, así que hay dos soluciones.","mal":"Vale 1, porque 25 menos 24 es 1. Es positivo, así que hay dos soluciones."}),
 sec("Cambiando q","Cambiando q",P("Mira cuántas veces corta la parábola al eje según el valor de q."),{"t":"acercando","ds":[6,3,6.25,8],"alt":"La parábola para varios valores de q"},P("Con q menor que 6.25 hay dos cortes, con q igual a 6.25 hay uno, y con q mayor no hay ninguno. Justo cuando el discriminante cambia de signo.")),
 sec("Ecuaciones lineales","Lineales",P("En una ecuación lineal se despeja x. Si hay fracciones, se multiplica por el denominador común."),
   PASOS([("\\dfrac{x}{2}-\\dfrac{x-1}{3}=1","La ecuación."),
          ("3x-2(x-1)=6","Se multiplica todo por 6."),
          ("x+2=6\\ \\Rightarrow\\ x=4","Se reducen términos y se despeja.")]),
   OJO("Al multiplicar por un denominador hay que multiplicar cada término, incluido el que está del otro lado del igual.")),
 sec("Ecuaciones cuadráticas","Cuadráticas",P("Se factoriza, si se puede. Si no, se usa la fórmula general."),
   PASOS([("x^{2}-5x+6=0\\ \\Rightarrow\\ (x-2)(x-3)=0\\ \\Rightarrow\\ x=2,\\ 3","Si un producto es 0, algún factor es 0."),
          ("x=\\dfrac{-b\\pm\\sqrt{b^{2}-4ac}}{2a}","La fórmula general."),
          ("2x^{2}-3x-2=0\\ \\Rightarrow\\ x=\\dfrac{3\\pm\\sqrt{9+16}}{4}=\\dfrac{3\\pm 5}{4}","Con a igual a 2, b igual a menos 3 y c igual a menos 2."),
          ("x=2\\ \\text{o}\\ x=-\\tfrac{1}{2}","Las dos soluciones.")]),
   OJO("La suma de las raíces es menos b sobre a, y el producto es c sobre a. En x al cuadrado menos 7x más 10, la suma es 7 y el producto es 10.")),
 eng("El lanzamiento de una pelota","La altura de una pelota lanzada hacia arriba es una función cuadrática del tiempo. El momento en que llega al suelo es la solución positiva de una ecuación cuadrática.","h(t)=1.5+12t-4.9t^{2}=0",
   [("Altura inicial","1.5 m"),("Velocidad inicial","12 m/s"),("Llega al suelo","a los 2.57 s")],"El discriminante es 144 más 29.4, o sea 173.4, y su raíz es 13.17. Las soluciones son 12 más o menos 13.17, sobre 9.8, o sea 2.57 y menos 0.12. La negativa no sirve, porque es antes del lanzamiento. La pelota llega al suelo a los 2.57 segundos. Es un modelo sin resistencia del aire."),
 completar("Se factoriza la ecuación x al cuadrado menos 5x más 6 igual a 0.","(x-2)(x-[[hueco]])=0",
   [("3","tres"),("-3","menos tres"),("6","seis")],0,
   ["","Con x más 3 el producto no daría menos 5x. Los dos números deben sumar 5 y multiplicar 6.","Con 6 el producto de los números daría 12 y no 6."],"Los dos números suman 5 y multiplican 6.","2 y 3 suman 5 y multiplican 6."),
 error("Alguien resolvió una ecuación con la fórmula general y se equivocó en un paso. Toca el paso que está mal.",
   [("2x^{2}-3x-2=0\\ \\Rightarrow\\ a=2,\\ b=-3,\\ c=-2","Se identifican los coeficientes.","a es 2, b es menos 3 y c es menos 2"),
    ("b^{2}-4ac=9-4(2)(-2)=9-16=-7","Este paso es el que falla.","el discriminante es 9 menos 16, igual a menos 7"),
    ("\\text{No hay soluciones reales}","La conclusión.","no hay soluciones reales")],1,
   "Menos 4 por 2 por menos 2 es más 16, porque dos negativos se multiplican y dan positivo. El discriminante es 9 más 16, o sea 25, y hay dos soluciones reales.",
   "b^{2}-4ac=9+16=25","Cuidado con el signo de menos 4ac cuando c es negativo."),
 ordenar("Estos son los pasos para resolver x sobre 3, más x más 1 sobre 2, igual a 2, pero están desordenados.",
   [("\\dfrac{x}{3}+\\dfrac{x+1}{2}=2","La ecuación"),
    ("2x+3(x+1)=12","Se multiplica por 6"),
    ("5x+3=12","Se reducen términos"),
    ("x=\\dfrac{9}{5}","Se despeja x")],[2,0,3,1],
   "Se multiplica por el denominador común, se reducen los términos y se despeja.","Se empieza con la ecuación original."),
]
S+=cierre("Mini simulacro de ecuaciones lineales y cuadráticas",[
 banco("mb_c2_02","El discriminante es $9+16=25$, y las soluciones son $\\dfrac{3\\pm5}{4}$."),
 banco("mb_c2_03","La suma de las raíces de $x^2-7x+10=0$ es $-b/a=7$."),
 banco("mb_r19_10","Se pasa a la forma $3z^2+12z+7=0$, y el discriminante es $144-84=60$.")])
prac=[
 {"titulo":"La parábola","grafica":{"draw":1,"guide":1},"bloques":[P("La parábola de x al cuadrado menos 5x más q."),EQ("y=x^{2}-5x+q")]},
 {"titulo":"Cambia q","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee el discriminante. Cuando es negativo, la parábola no toca el eje.")]},
 {"titulo":"Sin soluciones","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":8,"bloques":[EQ("q=8\\ \\Rightarrow\\ 25-32=-7<0"),P("Con q igual a 8 no hay soluciones reales.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":8},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Busca dos números que sumen y multipliquen lo que pide la ecuación."}]}]
preg={"tex":"x^{2}-x-12=0\\ \\text{tiene como soluciones}","opciones":["$x=4$ y $x=-3$","$x=-4$ y $x=3$","$x=6$ y $x=-2$","$x=12$ y $x=-1$"],"correcta":0,
 "explicacion":"Se factoriza buscando dos números que multipliquen menos 12 y sumen menos 1, que son menos 4 y 3. Los factores son x menos 4 y x más 3, y las soluciones son 4 y menos 3.",
 "verificacion":{"formula":"x*x-x-12","a":4,"esperado":0},
 "pistas":["Factoriza buscando dos números que multipliquen menos 12.","Esos números deben sumar menos 1.","Son 3 y menos 4, y las soluciones tienen el signo contrario."],
 "errores":["","Esos tienen los signos al revés. Los factores serían x más 4 y x menos 3, y el término del medio saldría más x.","Esas soluciones suman 4, pero la suma de las soluciones debe ser 1, que es menos el coeficiente de x.","Esas soluciones suman 11, pero la suma de las soluciones debe ser 1."]}
res=["Una ecuación lineal se resuelve despejando x, y con fracciones se multiplica por el denominador común.","Una cuadrática se resuelve factorizando o con la fórmula general.","El discriminante dice si hay dos soluciones reales, una doble, o ninguna."]
write(lesson("mb-m2-l2","Lección 2 de 5","Ecuaciones lineales y cuadráticas",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Básicas"),"matbas-cuadraticas.json")
