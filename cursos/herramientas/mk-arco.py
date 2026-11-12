from mklib import *
MOD="Módulo 3 Aplicaciones, polares y series"
graf={"tipo":"area","x":[0,2.5],"y":[0,3],"funcion":"sqrt(1+x*x)","primitiva":"(x*sqrt(1+x*x)+ln(x+sqrt(1+x*x)))/2","a":0,"b":2.3,"franja":0.08,"limite":1,
 "etiquetas":["Longitud acumulada","Elemento de longitud"],"rotulos":["longitud","elemento"],"etiquetaSlider":"Posición de x",
 "alt":"Curva de la raíz de 1 más x al cuadrado con el área bajo ella sombreada, que es la longitud de arco acumulada de la parábola y igual a x al cuadrado sobre 2"}
glos={"arco":"La longitud de arco es la longitud de una curva medida a lo largo de ella, como si se estirara un hilo sobre la curva.",
 "ds":"El elemento de longitud ds es un pedacito diminuto de la curva, casi recto, cuya longitud sale de un triángulo con catetos dx y dy.",
 "superficie":"El área de una superficie de revolución es el área de la cáscara que se forma al girar una curva alrededor de un eje."}
ver={"duracion":22.0,"capitulos":[
 [0,2.5,"Se quiere la longitud de la parábola y igual a x al cuadrado sobre 2, entre x igual a 0 y x igual a 2. Esta gráfica muestra cuánta curva hay por cada unidad de x."],
 [2.5,5,"La altura vale 1 en x igual a 0, donde la curva es horizontal."],
 [5,11,"Al avanzar x, la curva se inclina y hay más longitud por cada paso en x. El área acumulada es la longitud recorrida."],
 [11,16,"Con x igual a 1 la longitud acumulada es 1.1478 y la altura es 1.41."],
 [16,22,"Con x igual a 2 la longitud es 2.9579, un poco más que la distancia recta entre los extremos."]],
 "canales":{"draw":[[0.3,0],[2.4,1]],"hole":[[2.5,0],[3.3,1]],"d":[[5,0.2],[11,1],[15,1],[16,2],[22,2]],"guide":[[11,0],[12,1]]},
 "intervalos":{"ok":[16,22]}}
S=[
 sec("La idea",None,P("La {{gl:arco|longitud de arco}} es lo que mediría un hilo puesto sobre una curva. Se calcula partiendo la curva en pedacitos casi rectos y sumando sus longitudes. Esa suma es una integral. Con una idea parecida se calcula el área de una {{gl:superficie|superficie de revolución}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la parábola y igual a x al cuadrado sobre 2, entre x igual a 0 y x igual a 2. Se quiere medir su longitud."),EQ("L=\\int_{0}^{2}\\sqrt{1+\\left(y'\\right)^{2}}\\,dx"),P("La gráfica de esta lección no muestra la parábola sino su elemento de longitud, la cantidad de curva por cada paso en x. El área bajo ella es la longitud."),{"t":"grafica","animar":"dibujar","alt":"Curva que se dibuja y marca el punto de partida en x igual a 0"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En x igual a 0 la parábola es horizontal, con pendiente 0. ¿Cuánto vale entonces la raíz de 1 más la pendiente al cuadrado?","opciones":[0,0.5,1,2],"correcta":1,"bien":"Muy bien. Vale 1, porque no hay inclinación y un paso en x es un paso a lo largo de la curva.","mal":"Vale 1. Sin inclinación, un paso en x es un paso a lo largo de la curva."}),
 sec("La longitud que se acumula","La longitud",P("Mira cómo se llena el área y qué valen la longitud y el elemento de longitud en cada x."),{"t":"acercando","ds":[0.5,1,1.5,2],"alt":"El área bajo la curva que va creciendo y representa la longitud de arco acumulada"},P("Con x igual a 2 la longitud acumulada es <b>2.9579</b>. La distancia en línea recta entre los extremos de la parábola es 2.83, así que la curva es un poco más larga, como debe ser.")),
 sec("De dónde sale la fórmula","La fórmula",P("Un pedacito de curva es casi recto, y su longitud sale del teorema de Pitágoras con catetos dx y dy. Como dy es y prima por dx, queda la fórmula."),
   EQ("ds=\\sqrt{dx^{2}+dy^{2}}=\\sqrt{1+\\left(y'\\right)^{2}}\\,dx"),
   EQ("L=\\int_{a}^{b}\\sqrt{1+\\left(y'\\right)^{2}}\\,dx"),
   OJO("La derivada se eleva al cuadrado y luego se suma 1, antes de sacar la raíz. Esa raíz suele complicar la integral, y por eso se eligen ejemplos donde el contenido sale como un cuadrado perfecto.")),
 sec("Aplicarla","Aplicarla",PASOS([("y=\\dfrac{x^{2}}{2}\\ \\Rightarrow\\ y'=x","Se deriva la función."),
          ("L=\\int_{0}^{2}\\sqrt{1+x^{2}}\\,dx","Se reemplaza en la fórmula."),
          ("=\\left[\\dfrac{x\\sqrt{1+x^{2}}+\\ln\\left(x+\\sqrt{1+x^{2}}\\right)}{2}\\right]_{0}^{2}","Esta primitiva sale con sustitución trigonométrica, con x igual a tangente de theta."),
          ("=\\sqrt{5}+\\dfrac{\\ln\\left(2+\\sqrt{5}\\right)}{2}\\approx 2.9579","Se evalúa. Es el mismo valor que mostraba el área de la gráfica.")])),
 sec("Un caso que sale fácil","Caso fácil",P("Cuando la derivada deja una expresión lineal bajo la raíz, la integral se hace con una sustitución sencilla."),
   PASOS([("y=x^{3/2},\\quad y'=\\dfrac{3}{2}\\sqrt{x},\\quad 1+\\left(y'\\right)^{2}=1+\\dfrac{9x}{4}","Se deriva y se arma la expresión bajo la raíz."),
          ("L=\\int_{0}^{1}\\sqrt{1+\\dfrac{9x}{4}}\\,dx=\\dfrac{8}{27}\\left[\\left(1+\\dfrac{9x}{4}\\right)^{3/2}\\right]_{0}^{1}","Con u igual a 1 más 9x sobre 4, du es 9 sobre 4 dx."),
          ("=\\dfrac{8}{27}\\left(\\left(\\dfrac{13}{4}\\right)^{3/2}-1\\right)\\approx 1.4397","Se evalúa.")])),
 sec("Área de una superficie de revolución","Superficie",P("Si la curva se gira alrededor del eje x, cada pedacito de curva barre una banda con radio f de x y ancho ds. Su área es 2 pi por el radio por el ancho."),
   EQ("S=2\\pi\\int_{a}^{b}f(x)\\sqrt{1+\\left(f'(x)\\right)^{2}}\\,dx"),
   PASOS([("f(x)=x,\\quad 0\\le x\\le 2,\\quad f'(x)=1","Girar esta recta alrededor del eje x forma un cono."),
          ("S=2\\pi\\int_{0}^{2}x\\sqrt{1+1}\\,dx=2\\sqrt{2}\\,\\pi\\left[\\dfrac{x^{2}}{2}\\right]_{0}^{2}","Se reemplaza en la fórmula."),
          ("=4\\sqrt{2}\\,\\pi\\approx 17.77","Es el área lateral del cono. Se comprueba con la fórmula de geometría, pi por radio por generatriz, que da pi por 2 por 2 raíz de 2.")])),
 eng("La longitud de un cable entre dos postes","Un cable entre dos postes cuelga formando una curva parecida a una parábola. Para pedir la cantidad de cable hay que conocer su longitud real, que es mayor que la distancia entre los postes.","y=0.01\\,x^{2},\\quad -20\\le x\\le 20",
   [("Distancia entre postes","40 m"),("Flecha del cable","4 m"),("Cable necesario","unos 41.0 m")],"Se usa la simetría, 2 por la integral de 0 a 20 de la raíz de 1 más (0.02x) al cuadrado. Resulta unos 41.0 metros, cerca de un metro más que la distancia entre los postes. Es un modelo simplificado, porque un cable real forma una catenaria y no una parábola exacta."),
 completar("Se halla la longitud de la parábola y igual a x al cuadrado. Falta lo que va bajo la raíz.","L=\\int\\sqrt{1+[[hueco]]}\\,dx",
   [("(2x)^{2}","dos x, todo al cuadrado"),("2x","dos x"),("x^{2}","x al cuadrado")],0,
   ["","Falta elevar la derivada al cuadrado. Bajo la raíz va 1 más la derivada al cuadrado.","Esa es la función y no su derivada. Bajo la raíz va la derivada al cuadrado, y la derivada de x al cuadrado es 2x."],"Primero deriva y, y luego elévala al cuadrado.","La derivada de x al cuadrado es 2x, y bajo la raíz va su cuadrado, o sea 4x al cuadrado."),
 error("Alguien planteó la longitud de la parábola y igual a x al cuadrado sobre 2 y se equivocó en un paso. Toca el paso que está mal.",
   [("y=\\dfrac{x^{2}}{2}\\ \\Rightarrow\\ y'=x","La derivada está bien.","y es x al cuadrado sobre 2 y y prima es x"),
    ("L=\\int_{0}^{2}\\sqrt{1+x}\\,dx","Este paso es el que falla.","L es la integral de 0 a 2 de raíz de 1 más x"),
    ("=\\dfrac{2}{3}\\left[(1+x)^{3/2}\\right]_{0}^{2}=\\dfrac{2}{3}\\left(3\\sqrt{3}-1\\right)","La cuenta está bien con lo que viene del paso anterior.","Es dos tercios de la potencia tres medios evaluada de 0 a 2")],1,
   "Bajo la raíz va 1 más la derivada al cuadrado, y aquí la derivada es x, así que hay que poner x al cuadrado.",
   "L=\\int_{0}^{2}\\sqrt{1+x^{2}}\\,dx","Revisa si la derivada se elevó al cuadrado."),
 ordenar("Estos son los pasos para el área lateral del cono que sale de girar y igual a x entre 0 y 2, pero están desordenados.",
   [("f(x)=x,\\quad f'(x)=1","La función es x y su derivada es 1"),
    ("S=2\\pi\\int_{0}^{2}x\\sqrt{1+1^{2}}\\,dx","El área es 2 pi por la integral de x por raíz de 1 más 1"),
    ("=2\\sqrt{2}\\,\\pi\\int_{0}^{2}x\\,dx","Se saca la raíz de 2, que es constante"),
    ("=4\\sqrt{2}\\,\\pi","Se evalúa y queda 4 raíz de 2 pi")],[2,0,3,1],
   "Se deriva, se arma la fórmula, se saca la constante y se integra.","Primero se deriva la función."),
]
S+=cierre("",None)
prac=[
 {"titulo":"El elemento de longitud","grafica":{"draw":1},"bloques":[P("Esta curva es la cantidad de arco por cada paso en x."),EQ("\\sqrt{1+x^{2}}")]},
 {"titulo":"El punto de partida","grafica":{"draw":1,"hole":1},"bloques":[P("La longitud se empieza a medir en x igual a 0.")]},
 {"titulo":"Mueve x","grafica":{"draw":1,"hole":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El área sombreada es la longitud acumulada y abajo se ve el elemento de longitud en x.")]},
 {"titulo":"Más inclinación","grafica":{"draw":1,"hole":1,"guide":1},"laboratorio":True,"d":1.5,"bloques":[P("Con x igual a 1.5 la parábola está bastante inclinada. Cada paso en x equivale a 1.8 de curva y la longitud acumulada es 1.95.")]},
 {"titulo":"El resultado","grafica":{"draw":1,"hole":1,"guide":1,"ok":True},"laboratorio":True,"d":2.2,"bloques":[EQ("L=\\int_{0}^{2}\\sqrt{1+x^{2}}\\,dx\\approx 2.9579"),P("Con x igual a 2.2 la longitud ya pasa de 3.4. La longitud pedida llega hasta x igual a 2, donde vale 2.9579.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"hole":1,"guide":1,"ok":True,"d":2.2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Deriva, eleva al cuadrado, suma 1 y mira si sale un cuadrado perfecto."}]}]
preg={"tex":"y=\\dfrac{1}{3}\\left(x^{2}+2\\right)^{3/2},\\quad 0\\le x\\le 3,\\quad L=?","opciones":["$12$","$9$","$18$","$6$"],"correcta":0,
 "explicacion":"La derivada es x por la raíz de x al cuadrado más 2. Al elevarla al cuadrado y sumar 1 queda x a la cuarta más 2x al cuadrado más 1, que es (x al cuadrado más 1) al cuadrado. La raíz es x al cuadrado más 1 y la integral entre 0 y 3 vale 9 más 3, o sea 12.",
 "verificacion":{"formula":"(3^3/3+3)-(0)+0*x","a":0,"esperado":12},
 "pistas":["Deriva y. La derivada de un tercio por (x al cuadrado más 2) a la tres medios es x por la raíz de x al cuadrado más 2.","Eleva la derivada al cuadrado y suma 1. Queda un cuadrado perfecto.","La raíz da x al cuadrado más 1. Integra entre 0 y 3."],
 "errores":["","Se olvidó el 1 de x al cuadrado más 1. La integral es x al cubo sobre 3 más x, que da 9 más 3.","Revisa la cuenta. La integral es x al cubo sobre 3 más x entre 0 y 3, que da 12.","Revisa la cuenta. La integral es x al cubo sobre 3 más x entre 0 y 3, que da 12."]}
res=["La longitud de arco es la integral de la raíz de 1 más la derivada al cuadrado.","Se eligen casos donde lo de adentro de la raíz es un cuadrado perfecto o una expresión lineal.","El área de la superficie de revolución es 2 pi por la integral de f por la raíz de 1 más f prima al cuadrado."]
write(lesson("calcint-m3-l3","Lección 3 de 5","Longitud de arco y superficies",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=4),"calcint-arco.json")
