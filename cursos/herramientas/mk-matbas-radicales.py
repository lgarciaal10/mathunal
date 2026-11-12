import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 2 Ecuaciones, inecuaciones y sistemas"
TS=[-4+12*k/100 for k in range(101)]
graf={"tipo":"plano","x":[-4.5,8.5],"y":[-5.5,7],"a":-3,"b":7,"inicio":1,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"sqrt({t:.4f}+4)"] for t in TS],"c":2},
  {"t":"recta","p":["0","-2"],"dir":["1","1"],"c":3,"guia":True},
  {"t":"segmento","a":["x","sqrt(x+4)"],"b":["x","x-2"],"c":1,"guia":True},
  {"t":"punto","p":["x","sqrt(x+4)"],"c":2},
  {"t":"punto","p":["x","x-2"],"c":3,"guia":True}],
 "lecturas":[{"rotulo":"valor de x","formula":"x"},{"rotulo":"raíz menos recta","formula":"sqrt(x+4)-(x-2)"}],
 "etiquetas":["Valor de x","Distancia vertical entre la raíz y la recta"],"etiquetaSlider":"Valor de x",
 "alt":"La curva raíz de x más 4 y la recta x menos 2. La distancia vertical entre ellas vale cero solo en x igual a 5, la única solución real de la ecuación. En x igual a 0 la distancia vale 4, y esa es una solución falsa"}
glos={"radical":"Una ecuación con radicales tiene la incógnita dentro de una raíz. Se aísla la raíz y se eleva al cuadrado, y después hay que comprobar las soluciones.",
 "extrana":"Una solución extraña es la que aparece al resolver, pero no cumple la ecuación original. Pasa porque elevar al cuadrado también deja pasar los signos contrarios.",
 "valorabsoluto":"El valor absoluto de un número es su distancia al cero. La ecuación valor absoluto de A igual a B se divide en dos casos, A igual a B y A igual a menos B."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La curva es la raíz de x más 4 y la recta es x menos 2. Las soluciones de la ecuación son los puntos donde se cruzan."],
 [4,8,"El segmento vertical mide la distancia entre las dos. Cuando vale 0, la curva y la recta se tocan."],
 [8,14,"Mueve x. A la izquierda la raíz está por encima de la recta, y a la derecha queda por debajo."],
 [14,18,"Se cruzan en x igual a 5, donde las dos valen 3. Esa es la solución de la ecuación."],
 [18,22,"Al elevar al cuadrado también aparece x igual a 0. Ahí la raíz vale 2 y la recta vale menos 2, y no se cruzan. Es una solución falsa."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,-3],[12,7],[14,5],[17,5],[18,0],[22,0]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("En una ecuación con {{gl:radical|radicales}} se aísla la raíz y se eleva al cuadrado en los dos lados. Eso elimina la raíz, pero puede crear {{gl:extrana|soluciones extrañas}}, que no cumplen la ecuación original. Por eso siempre se comprueba. Con {{gl:valorabsoluto|valor absoluto}}, la ecuación se divide en dos casos.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la raíz y la recta. Las soluciones están donde se cruzan."),EQ("\\sqrt{x+4}=x-2"),{"t":"grafica","animar":"dibujar","alt":"La raíz y la recta"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Al elevar al cuadrado x menos 2 se obtiene x al cuadrado, menos 4x, más 4. Con x igual a 0, ¿cuánto vale x menos 2?","opciones":[2,-2,0,4],"correcta":-2,"bien":"Muy bien. Vale menos 2. Una raíz nunca da un valor negativo, así que x igual a 0 no sirve.","mal":"Vale menos 2, porque 0 menos 2 es menos 2. Una raíz nunca da un valor negativo, así que x igual a 0 no sirve."}),
 sec("Moviendo x","Moviendo x",P("Mira dónde se cruzan la raíz y la recta."),{"t":"acercando","ds":[5,0,-3,7],"alt":"La distancia entre la raíz y la recta en varios x"},P("Solo en x igual a 5 la distancia es 0. En x igual a 0 vale 4, así que esa solución es falsa.")),
 sec("Ecuaciones con radicales","Radicales",P("Se aísla la raíz, se eleva al cuadrado y se comprueba."),
   PASOS([("\\sqrt{x+4}=x-2\\ \\Rightarrow\\ x+4=(x-2)^{2}","Se eleva al cuadrado los dos lados."),
          ("x+4=x^{2}-4x+4\\ \\Rightarrow\\ x^{2}-5x=0\\ \\Rightarrow\\ x=0\\ \\text{o}\\ x=5","Se resuelve la ecuación cuadrática."),
          ("x=0:\\ \\sqrt{4}=2\\ne -2\\qquad x=5:\\ \\sqrt{9}=3=3","Se comprueba en la ecuación original. Solo sirve x igual a 5.")]),
   OJO("La comprobación no es opcional. Al elevar al cuadrado, menos 2 y 2 dan el mismo 4, y por eso aparece una solución que no sirve.")),
 sec("Valor absoluto","Valor absoluto",P("El valor absoluto de A igual a B, con B positivo, se divide en dos casos."),
   PASOS([("|2x-1|=5","La ecuación."),
          ("2x-1=5\\quad\\text{o}\\quad 2x-1=-5","Se separan los dos casos."),
          ("x=3\\quad\\text{o}\\quad x=-2","Se resuelve cada uno.")]),
   OJO("Si B es negativo, no hay solución, porque un valor absoluto nunca es negativo.")),
 eng("La profundidad de un pozo","Se deja caer una piedra en un pozo y se mide el tiempo hasta oír el golpe. Sin tener en cuenta el sonido, el tiempo de caída es una raíz, y la profundidad sale de una ecuación con radicales.","t=\\sqrt{\\dfrac{2h}{g}}",
   [("Tiempo","2.0 s"),("Gravedad","9.8 m/s²"),("Profundidad","19.6 m")],"Se aísla la raíz y se eleva al cuadrado, y queda 4 igual a 2h sobre 9.8. Entonces h vale 4 por 9.8 sobre 2, o sea 19.6 metros. Como la raíz no puede ser negativa, el tiempo debe ser positivo. En un pozo real, el sonido tarda en volver, y con 19.6 metros eso agrega casi 0.06 segundos."),
 completar("Se desarrolla el cuadrado al elevar los dos lados.","x+4=x^{2}-[[hueco]]x+4",
   [("4","cuatro"),("2","dos"),("5","cinco")],0,
   ["","El doble producto de x por 2 es 4x, no 2x.","Con 5 se estaría usando el término ya despejado, y no el doble producto."],"El cuadrado de x menos 2 es x al cuadrado menos 2 por x por 2, más 4.","2 por 2 es 4."),
 error("Alguien resolvió una ecuación con radicales y se equivocó en un paso. Toca el paso que está mal.",
   [("\\sqrt{x+4}=x-2\\ \\Rightarrow\\ x+4=(x-2)^{2}","Se eleva al cuadrado.","se eleva al cuadrado y queda x más 4 igual a x menos 2 al cuadrado"),
    ("x^{2}-5x=0\\ \\Rightarrow\\ x=0\\ \\text{o}\\ x=5","Se resuelve.","queda x al cuadrado menos 5x, con raíces 0 y 5"),
    ("\\text{Las soluciones son}\\ x=0\\ \\text{y}\\ x=5","Este paso es el que falla.","las soluciones son 0 y 5")],2,
   "Falta comprobar. Con x igual a 0, la raíz de 4 es 2 y el lado derecho es menos 2, así que no se cumple. Solo sirve x igual a 5.",
   "x=5","Reemplaza cada valor en la ecuación original."),
 ordenar("Estos son los pasos para resolver el valor absoluto de 2x menos 1 igual a 5, pero están desordenados.",
   [("|2x-1|=5","La ecuación"),
    ("2x-1=5\\ \\text{o}\\ 2x-1=-5","Se separan los dos casos"),
    ("2x=6\\ \\text{o}\\ 2x=-4","Se suma 1 en cada caso"),
    ("x=3\\ \\text{o}\\ x=-2","Se despeja x")],[2,0,3,1],
   "Se separan los dos casos, se suma 1 en cada uno y se despeja.","Se empieza con la ecuación original."),
]
S+=cierre("Mini simulacro de ecuaciones con radicales y valor absoluto",[
 banco("mb_c2_05","Se eleva al cuadrado y salen $x=0$ y $x=5$, pero al comprobar solo sirve $x=5$."),
 banco("mb_c2_06","Se separa en $2x-1=5$ y $2x-1=-5$, con soluciones $3$ y $-2$.")])
prac=[
 {"titulo":"Raíz y recta","grafica":{"draw":1,"guide":1},"bloques":[P("La raíz de x más 4 y la recta x menos 2."),EQ("\\sqrt{x+4}=x-2")]},
 {"titulo":"Cambia x","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se lee cuánto separa la raíz de la recta. La solución es donde vale 0.")]},
 {"titulo":"Una solución falsa","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0,"bloques":[EQ("x=0:\\ \\sqrt{4}=2\\ne-2"),P("Con x igual a 0 la distancia vale 4, así que esa solución es falsa.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Separa los dos casos del valor absoluto."}]}]
preg={"tex":"|x+1|=4\\ \\text{tiene como soluciones}","opciones":["$x=3$ y $x=-5$","$x=4$ y $x=-4$","$x=3$ y $x=5$","solo $x=3$"],"correcta":0,
 "explicacion":"Se separan los casos, x más 1 igual a 4, que da x igual a 3, y x más 1 igual a menos 4, que da x igual a menos 5.",
 "verificacion":{"formula":"abs(x+1)","a":3,"esperado":4},
 "pistas":["Separa en dos casos, positivo y negativo.","El primero es x más 1 igual a 4.","El segundo es x más 1 igual a menos 4."],
 "errores":["","Esas serían las soluciones de |x|=4. Aquí hay que restar 1 en cada caso.","Con x igual a 5 el valor absoluto de 6 es 6, no 4.","Falta el segundo caso, x más 1 igual a menos 4."]}
res=["En una ecuación con radicales se aísla la raíz, se eleva al cuadrado y se comprueba cada solución.","Elevar al cuadrado puede crear soluciones que no sirven.","El valor absoluto de A igual a B se divide en A igual a B y A igual a menos B."]
write(lesson("mb-m2-l5","Lección 5 de 5","Ecuaciones con radicales y valor absoluto",24,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=2,curso="Matemáticas Básicas"),"matbas-radicales.json")
