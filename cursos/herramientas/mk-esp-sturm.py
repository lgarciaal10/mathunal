import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 3 Ecuación de Laplace y variable compleja"
XS=[round(k*math.pi/60,5) for k in range(61)]
EL=[{"t":"trazo","puntos":[[str(xv),f"cos({xv}*x)"] for xv in XS],"c":3},
    {"t":"trazo","puntos":[[str(xv),f"sin({xv}*x)"] for xv in XS],"c":0}]
graf={"tipo":"plano","x":[-0.4,3.6],"y":[-1.4,1.4],"a":1,"b":5,"inicio":1,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"valor propio lambda, igual a n al cuadrado","formula":"x*x"},{"rotulo":"número de ceros dentro del intervalo, n menos 1","formula":"x-1"}],
 "etiquetas":["Con extremos fijos, la función propia es seno de n x","Cada modo tiene un cero más que el anterior, y el coseno en verde sería con extremos libres"],"etiquetaSlider":"Modo n, de 1 a 5",
 "alt":"Las funciones propias del problema menos X segunda igual a lambda X en el intervalo de 0 a pi. Con extremos fijos son seno de n x, en azul, y con extremos libres son coseno de n x, en verde. Con n mayor la función oscila más, y tiene n menos 1 ceros dentro del intervalo"}
glos={"sl":"Un problema de Sturm-Liouville busca los valores propios lambda para los que hay soluciones no nulas de una ecuación con condiciones de frontera.",
 "propios":"Los valores propios son los lambda admisibles, y las funciones propias son las soluciones correspondientes.",
 "clasificacion":"Una EDP de segundo orden con coeficientes A, B y C es elíptica, parabólica o hiperbólica según el signo de B al cuadrado menos 4 A C.",
 "neumann":"La condición de Neumann fija la derivada de la función en el extremo, y la de Dirichlet fija el valor."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Al separar variables siempre aparece el mismo problema, menos X segunda igual a lambda X, con condiciones en los extremos."],
 [4,10,"Con extremos fijos, las funciones propias son seno de n x, y los valores propios son n al cuadrado."],
 [10,16,"Con n igual a 3, hay dos ceros dentro del intervalo, y lambda vale 9."],
 [16,20,"Con extremos libres, que es Neumann, las funciones propias son coseno de n x, y n también puede ser 0."],
 [20,24,"Los modos son ortogonales, y por eso se pueden combinar para ajustar cualquier dato inicial."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,2],[13,3],[16,3],[18,4],[24,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Al resolver una EDP por separación de variables aparece un problema de {{gl:sl|Sturm-Liouville}}. Sus {{gl:propios|valores y funciones propias}} dependen de las condiciones de frontera, de {{gl:neumann|Dirichlet o Neumann}}. Por otra parte, el tipo de la EDP, que se lee con la {{gl:clasificacion|clasificación}}, indica qué método usar, y puede ser elíptica, parabólica o hiperbólica.")),
 sec("Un ejemplo","Un ejemplo",P("El problema es menos X segunda igual a lambda X en el intervalo de 0 a pi. Cambia n y mira cuántos ceros tiene la función propia."),EQ("-X''=\\lambda X,\\quad X(0)=X(\\pi)=0\\ \\Rightarrow\\ X_{n}=\\operatorname{sen}nx,\\ \\lambda_{n}=n^{2}"),{"t":"grafica","animar":"dibujar","alt":"Las funciones propias de un problema de Sturm-Liouville"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Para el problema con X en 0 y en pi iguales a cero, el valor propio del modo 3 es n al cuadrado. ¿Cuánto vale?","opciones":[9,3,6,27],"correcta":9,"bien":"Muy bien. Tres al cuadrado es 9.","mal":"El valor propio es n al cuadrado. Con n igual a 3 vale 9."}),
 sec("Los modos","Modos",P("Mira las funciones propias con n igual a 1, 2, 3 y 4."),{"t":"acercando","ds":[1,2,3,4],"alt":"Las funciones propias con cuatro valores de n"},P("Cada modo tiene un cero más dentro del intervalo.")),
 sec("Condiciones de frontera","Fronteras",P("El tipo de condición cambia los valores propios."),
   PASOS([("X(0)=X(\\pi)=0\\ \\Rightarrow\\ X_{n}=\\operatorname{sen}nx,\\ \\lambda_{n}=n^{2},\\ n\\ge1","Dirichlet, con valores fijos en los extremos."),
          ("X'(0)=X'(\\pi)=0\\ \\Rightarrow\\ X_{n}=\\cos nx,\\ \\lambda_{n}=n^{2},\\ n\\ge0","Neumann, con derivadas nulas, e incluye la constante."),
          ("\\displaystyle\\int_{0}^{\\pi}X_{m}X_{n}\\,dx=0\\quad(m\\ne n)","Las funciones propias son ortogonales."),
          ("\\lambda_{3}=3^{2}=9","Un valor concreto.")]),
   OJO("Con Neumann, lambda igual a 0 es un valor propio, con función propia constante. Con Dirichlet, lambda igual a 0 solo da la función nula, y por eso no cuenta.")),
 sec("Clasificar una EDP","Clasificación",P("El signo de B al cuadrado menos 4AC dice el tipo."),
   PASOS([("Au_{xx}+Bu_{xy}+Cu_{yy}+\\cdots=0","La forma general."),
          ("B^{2}-4AC<0\\ \\to\\ \\text{eliptica}","Como Laplace."),
          ("B^{2}-4AC=0\\ \\to\\ \\text{parabolica}","Como calor."),
          ("B^{2}-4AC>0\\ \\to\\ \\text{hiperbolica}","Como onda.")]),
   OJO("Los términos de primer orden y los de orden cero no cambian el tipo. Solo cuentan los coeficientes de las segundas derivadas A, B y C.")),
 eng("Las tres EDP clásicas","Cada EDP clásica tiene un tipo y una conducta. Calor es parabólica y disipa, onda es hiperbólica y propaga, Laplace es elíptica y describe el equilibrio.","\\text{calor, onda, Laplace}\\ \\leftrightarrow\\ \\text{parabolica, hiperbolica, eliptica}",
   [("Calor","u sub t igual a u sub x x"),("Onda","u sub t t igual a u sub x x"),("Laplace","u sub x x más u sub y y igual a 0")],"Conocer el tipo ayuda a escoger el método numérico. Las parabólicas se resuelven avanzando en el tiempo, las hiperbólicas siguen las características y las elípticas exigen resolver todo el dominio a la vez."),
 completar("Una EDP con B al cuadrado menos 4AC igual a cero es de tipo [[hueco]].","B^{2}-4AC=0\\ \\Rightarrow\\ [[hueco]]",
   [("\\text{parabolica}","parabólica"),("\\text{eliptica}","elíptica"),("\\text{hiperbolica}","hiperbólica")],0,
   ["","Con elíptica el discriminante sería negativo.","Con hiperbólica el discriminante sería positivo."],"El caso cero es el parabólico.","Es parabólica."),
 error("Alguien clasificó la EDP u sub x x más 2 u sub x y más u sub y y más u sub x igual a 0 y se equivocó. Toca el paso que está mal.",
   [("A=1,\\ B=2,\\ C=1","Se leen los coeficientes.","coeficientes"),
    ("B^{2}-4AC=4-4+1=1>0","Este paso es el que falla.","se suma el término de primer orden"),
    ("\\text{hiperbolica}","Conclusión.","hiperbólica")],1,
   "El término de primer orden no entra en el discriminante. B al cuadrado menos 4AC es 4 menos 4, o sea 0, y la EDP es parabólica.",
   "B^{2}-4AC=4-4=0","Solo usa A, B y C."),
 ordenar("Estos son los pasos para hallar los valores propios de menos X segunda igual a lambda X con extremos fijos, pero están desordenados.",
   [("-X''=\\lambda X","Se parte de la ecuación"),
    ("X=\\operatorname{sen}(kx)","Con X en cero a la izquierda queda seno"),
    ("\\operatorname{sen}(k\\pi)=0\\ \\Rightarrow\\ k=n","El extremo derecho fija k"),
    ("\\lambda_{n}=n^{2}","Se lee el valor propio")],[2,0,3,1],
   "Se parte de la ecuación, se elige seno, se usa el extremo derecho y se lee lambda.","Se empieza con la ecuación."),
]
S+=cierre("Mini simulacro de Sturm-Liouville",[
 banco("es_c3_07","La clasificación por B al cuadrado menos 4AC."),
 banco("es_c3_08","El tipo de una EDP concreta."),
 banco("es_c3_09","El tipo de las tres EDP clásicas."),
 banco("es_c3_11","El tercer valor propio."),
 banco("es_c3_12","Los valores propios con Neumann.")])
prac=[
 {"titulo":"El problema","grafica":{"draw":1},"bloques":[P("Se buscan los lambda con solución no nula."),EQ("-X''=\\lambda X,\\quad X(0)=X(\\pi)=0")]},
 {"titulo":"Cambia el modo","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Solo importan los valores enteros de n. Abajo se leen lambda y el número de ceros.")]},
 {"titulo":"El modo tres","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("\\lambda_{3}=9"),P("Con n igual a 3 hay dos ceros dentro del intervalo.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El tipo depende solo de A, B y C."}]}]
preg={"tex":"u_{xx}-u_{yy}=0\\ \\text{es de tipo}","opciones":["hiperbólico","elíptico","parabólico","no clasificable"],"correcta":0,
 "explicacion":"Aquí A vale 1, B vale 0 y C vale menos 1. El discriminante B al cuadrado menos 4AC es 4, que es positivo, y la EDP es hiperbólica.",
 "verificacion":{"formula":"0-4*1*(-1)+0*x","a":0,"esperado":4},
 "pistas":["Lee A, B y C.","Calcula B al cuadrado menos 4AC.","Es positivo."],
 "errores":["","Elíptico sería con discriminante negativo.","Parabólico sería con discriminante cero.","Siempre se puede clasificar con A, B y C."]}
res=["Los problemas de Sturm-Liouville dan valores propios y funciones propias ortogonales, según las condiciones de frontera.","Con extremos fijos en 0 y pi, el valor propio del modo n es n al cuadrado.","El tipo de una EDP depende del signo de B al cuadrado menos 4AC."]
write(lesson("es-m3-l5","Lección 5 de 5","Sturm-Liouville y clasificación de EDP",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-sturm.json")
