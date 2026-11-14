import os, math
os.environ['CURSO_FU']='Ecuaciones Diferenciales'; os.environ['BANCO']='edo'
from mklib import *
MOD="Módulo 1 EDO de primer orden"
XR=[-0.5,6.5]; YR=[-0.5,3.3]
EL=campo(lambda x,y:y*(2-y),XR,YR,14,8,0.14)
EL+=[{"t":"recta","p":["0","2"],"dir":["1","0"],"guion":True,"c":3,"guia":True},{"t":"recta","p":["0","0"],"dir":["1","0"],"guion":True,"c":1,"guia":True},
 trazo("2/(1+((2-x)/x)*exp(0-2*{x}))",0,6.4,64,2),{"t":"punto","p":["0","x"],"c":1}]
graf={"tipo":"plano","x":XR,"y":YR,"a":0.2,"b":3,"inicio":0.5,"elementos":EL,
 "lecturas":[{"rotulo":"y(0)","formula":"x"},{"rotulo":"y(3)","formula":"2/(1+((2-x)/x)*exp(-6))"}],
 "etiquetas":["Valor inicial","Valor en x igual a 3"],"etiquetaSlider":"Valor inicial y(0)",
 "alt":"El campo de pendientes de y prima igual a y por (2 menos y), con los equilibrios y igual a 0 e y igual a 2, y una solución que parte del valor inicial y se acerca a 2"}
glos={"autonoma":"Una EDO es autónoma si la función de la derecha no depende de la variable independiente. Describe un proceso cuyas reglas no cambian con el tiempo.",
 "equilibrio":"Un punto de equilibrio es un valor de y donde la derivada es cero, así que si la solución empieza ahí, se queda ahí para siempre.",
 "estable":"Un equilibrio es estable si las soluciones cercanas se acercan a él, e inestable si se alejan."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La ecuación y prima igual a y por (2 menos y) no depende de x, solo de y. Es autónoma."],
 [4,9,"Se anula en y igual a 0 y en y igual a 2. Son los equilibrios. Ahí las soluciones son rectas horizontales."],
 [9,15,"Entre 0 y 2 la pendiente es positiva, y la solución sube hacia 2. Arriba de 2 la pendiente es negativa y la solución baja hacia 2."],
 [15,19,"Por eso 2 es un equilibrio estable, y 0 es inestable, porque las soluciones se alejan de él."],
 [19,22,"Con y de 0 igual a 0.5, la solución vale casi 2 en x igual a 3."]],
 "canales":{"draw":[[0.3,0],[4,1]],"d":[[4,0.5],[9,1.5],[12,2.8],[15,0.3],[19,0.5],[22,0.5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[19,22]}}
S=[
 sec("La idea",None,P("En una ecuación {{gl:autonoma|autónoma}}, y prima igual a f de y, el comportamiento se puede entender sin resolverla. Basta ver dónde f vale 0, que son los puntos de {{gl:equilibrio|equilibrio}}, y qué signo tiene f entre ellos. Con eso se sabe hacia dónde van las soluciones y si cada equilibrio es {{gl:estable|estable}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira esta ecuación logística, un modelo de crecimiento con límite."),EQ("y'=y\\,(2-y)"),{"t":"grafica","animar":"dibujar","alt":"El campo de pendientes y los dos equilibrios"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En y igual a 1 la pendiente es y por (2 menos y). ¿Cuánto vale?","opciones":[0,1,2,3],"correcta":1,"bien":"Muy bien. Vale 1, así que la solución sube. Más abajo se ve.","mal":"Vale 1, porque 1 por (2 menos 1) es 1. La solución sube ahí. Más abajo se ve."}),
 sec("Hacia el equilibrio","Hacia el equilibrio",P("Mira cómo se mueve la solución con valores iniciales distintos."),{"t":"acercando","ds":[0.3,0.5,1.5,2.8],"alt":"La solución para varios valores iniciales"},P("Todas las soluciones que parten entre 0 y 3 se acercan a 2.")),
 sec("Los equilibrios","Equilibrios",P("Los equilibrios salen de resolver f de y igual a 0."),
   PASOS([("y(2-y)=0\\ \\Rightarrow\\ y=0\\ \\text{o}\\ y=2","Son los dos equilibrios."),
          ("y'=y-2\\ \\Rightarrow\\ y=2","Con f igual a y menos 2 solo hay un equilibrio, el 2.")])),
 sec("La estabilidad","Estabilidad",P("Se mira el signo de f a cada lado de cada equilibrio."),
   PASOS([("0<y<2:\\ f>0\\ \\Rightarrow\\ y\\ \\text{sube}","Entre los equilibrios la solución sube."),
          ("y>2:\\ f<0\\ \\Rightarrow\\ y\\ \\text{baja}","Arriba de 2 la solución baja hacia 2."),
          ("y=2\\ \\text{estable (sumidero)},\\quad y=0\\ \\text{inestable (fuente)}","Un equilibrio es estable si las soluciones llegan a él desde los dos lados.")]),
   OJO("Si f cambia de signo de más a menos al subir y, el equilibrio es estable. Si cambia de menos a más, es inestable.")),
 sec("Con la derivada","Con la derivada",P("Otra forma es mirar la derivada de f."),
   PASOS([("f'(y)=2-2y","Se deriva f."),
          ("f'(2)=-2<0\\ \\Rightarrow\\ \\text{estable}","Una derivada negativa en el equilibrio dice que es estable."),
          ("f'(0)=2>0\\ \\Rightarrow\\ \\text{inestable}","Una derivada positiva dice que es inestable.")])),
 eng("La velocidad terminal","Un cuerpo que cae en el aire acelera con la gravedad, pero el aire se opone con una fuerza que crece con el cuadrado de la velocidad. La ecuación es autónoma, y su equilibrio estable es la velocidad terminal, la que alcanza cuando las fuerzas se igualan.","v'=g-k\\,v^{2}",
   [("Gravedad","9.81 m/s²"),("Constante k","0.0098 1/m"),("Velocidad terminal","31.6 m/s")],"El equilibrio sale de g menos k v cuadrado igual a 0, o sea v igual a la raíz de g sobre k, unos 31.6 metros por segundo. Como f cambia de positiva a negativa, el equilibrio es estable. Cualquier velocidad inicial positiva se acerca a él. Es un modelo simplificado, porque supone una resistencia proporcional al cuadrado."),
 completar("Se halla el equilibrio de y prima igual a y menos 2, que resulta inestable. Falta el valor.","y'=y-2=0\\ \\Rightarrow\\ y=[[hueco]]",
   [("2","dos"),("-2","menos dos"),("0","cero")],0,
   ["","El signo está al revés. y menos 2 igual a 0 da y igual a 2.","Con y igual a 0, y menos 2 vale menos 2, no 0."],"Despeja y de y menos 2 igual a 0.","Sumando 2 a los dos lados, y es igual a 2. Es un equilibrio inestable, porque f crece con y."),
 error("Alguien clasificó un equilibrio y se equivocó en un paso. Toca el paso que está mal.",
   [("y'=y(1-y)\\ \\Rightarrow\\ y=0,\\ y=1","Los equilibrios son 0 y 1.","y prima es y por (1 menos y), con equilibrios 0 y 1"),
    ("\\text{Entre 0 y 1}\\ f>0\\ \\Rightarrow\\ y\\ \\text{sube hacia 1}","La solución sube entre los equilibrios.","Entre 0 y 1 f es positiva, así que y sube hacia 1"),
    ("\\text{Por tanto 1 es inestable}","Este paso es el que falla.","Por tanto 1 es inestable")],2,
   "Las soluciones cercanas se acercan a 1 desde abajo y desde arriba, porque f es positiva antes de 1 y negativa después. Eso es un equilibrio estable, un sumidero. Con la derivada, f prima de 1 es menos 1, negativa.",
   "f'(1)=1-2=-1<0\\ \\Rightarrow\\ y=1\\ \\text{es estable}","Mira hacia dónde van las soluciones cercanas a 1."),
 ordenar("Estos son los pasos para estudiar y prima igual a y por (3 menos y), pero están desordenados.",
   [("y(3-y)=0\\ \\Rightarrow\\ y=0,\\ y=3","Se hallan los equilibrios"),
    ("f'(y)=3-2y","Se deriva f"),
    ("f'(3)=-3<0\\ \\Rightarrow\\ \\text{estable},\\ f'(0)=3>0\\ \\Rightarrow\\ \\text{inestable}","Se evalúa en cada equilibrio"),
    ("y\\to 3\\ \\text{si}\\ y(0)>0","Se concluye hacia dónde van las soluciones")],[2,0,3,1],
   "Se hallan los equilibrios, se deriva f, se evalúa en cada uno y se concluye.","Primero van los equilibrios."),
]
S+=cierre("",None)
prac=[
 {"titulo":"El campo","grafica":{"draw":1,"guide":1},"bloques":[P("Las rectas punteadas son los equilibrios."),EQ("y'=y(2-y)")]},
 {"titulo":"Cambia y(0)","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La solución se acerca a 2 sin importar el valor inicial, mientras sea positivo. Abajo se ven y(0) y y(3).")]},
 {"titulo":"Estable","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.5,"bloques":[EQ("f'(2)=-2<0\\ \\Rightarrow\\ \\text{estable}"),P("Cerca de 2 las soluciones se acercan. Cerca de 0 se alejan, así que 0 es inestable.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Halla los equilibrios y mira el signo de f a cada lado."}]}]
preg={"tex":"y'=y(1-y)","encabezado":"Para la ecuación logística y prima igual a y por (1 menos y), el equilibrio y igual a 1 es:","opciones":["asintóticamente estable (sumidero)","inestable (fuente)","semiestable","no es un equilibrio"],"correcta":0,
 "explicacion":"Cerca de 1 la pendiente es positiva por debajo y negativa por arriba. Las soluciones se acercan a 1 desde los dos lados. Con la derivada, f prima de 1 es 1 menos 2, o sea menos 1, negativa.",
 "pistas":["Mira el signo de f a la izquierda y a la derecha de 1.","A la izquierda es positiva y a la derecha negativa.","La derivada de f en 1 vale menos 1."],
 "errores":["","Una fuente haría que las soluciones se alejen, y aquí se acercan.","Semiestable sería si f no cambiara de signo en el equilibrio, y aquí sí cambia.","y prima vale 0 en 1 porque f de 1 es 0, así que sí es un equilibrio."]}
res=["En una ecuación autónoma los equilibrios salen de f de y igual a 0.","El signo de f a cada lado dice hacia dónde van las soluciones, y la derivada de f en el equilibrio dice si es estable.","Un equilibrio estable atrae a las soluciones cercanas, y uno inestable las aleja."]
write(lesson("edo-m1-l5","Lección 5 de 6","Autónomas y estabilidad",24,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Ecuaciones Diferenciales",ejercicios=4),"edo-autonomas.json")
