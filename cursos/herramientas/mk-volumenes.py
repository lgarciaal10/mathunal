from mklib import *
MOD="Módulo 3 Aplicaciones, polares y series"
graf={"tipo":"area","x":[0,4.5],"y":[0,14],"funcion":"pi*x","primitiva":"pi*x*x/2","a":0,"b":3.8,"franja":0.12,"limite":6.28,
 "etiquetas":["Volumen acumulado","Área del disco"],"rotulos":["volumen","área del disco"],"etiquetaSlider":"Posición de x",
 "alt":"Recta pi por x, que es el área de cada disco, con el área bajo ella sombreada, que es el volumen acumulado del sólido"}
glos={"revolucion":"Un sólido de revolución es el que se forma al girar una región plana alrededor de una recta, llamada eje de giro.",
 "disco":"Un disco es una rebanada delgada del sólido, con forma de cilindro muy bajito. Su volumen es el área de su cara por su grosor.",
 "arandela":"Una arandela es un disco con un hueco circular en el centro, como la rondana de un tornillo.",
 "capa":"Una capa es un cascarón cilíndrico delgado, como un tubo de pared muy fina, que se usa cuando el giro es alrededor del eje y."}
ver={"duracion":22.0,"capitulos":[
 [0,2.5,"Se gira la región bajo la raíz de x, entre 0 y 4, alrededor del eje x. Se forma un sólido."],
 [2.5,5,"Se parte el sólido en discos delgados. Cada disco tiene radio igual a la raíz de x."],
 [5,11,"Esta gráfica muestra el área de la cara de cada disco, que es pi por x. El volumen es el área bajo ella."],
 [11,16,"Con x igual a 2 el disco tiene área 6.28 y el volumen acumulado es 6.28."],
 [16,22,"Con x igual a 4 el volumen acumulado es 25.13, que es 8 pi."]],
 "canales":{"draw":[[0.3,0],[2.4,1]],"hole":[[2.5,0],[3.3,1]],"d":[[5,0.3],[11,2],[15,2],[16,4],[22,4]],"guide":[[11,0],[12,1]]},
 "intervalos":{"ok":[16,22]}}
S=[
 sec("La idea",None,P("Si se gira una región plana alrededor de una recta, se forma un {{gl:revolucion|sólido de revolución}}. Su volumen se calcula partiéndolo en rebanadas delgadas, calculando el volumen de cada una y sumando. Esa suma es una integral.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la región bajo la raíz de x, entre x igual a 0 y x igual a 4, que gira alrededor del eje x."),EQ("V=\\pi\\int_{0}^{4}\\left(\\sqrt{x}\\right)^{2}dx"),P("La gráfica de esta lección muestra el área de la cara de cada {{gl:disco|disco}}. El volumen es el área bajo esa curva."),{"t":"grafica","animar":"dibujar","alt":"Recta que se dibuja y marca el punto de partida en x igual a 0"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con x igual a 2, el radio del disco es la raíz de 2 y su cara tiene área pi por el radio al cuadrado. ¿Cuánto vale esa área, más o menos?","opciones":[3.14,6.28,9.42,12.57],"correcta":6.28,"bien":"Muy bien. Es pi por 2, o sea 6.28. Más abajo se ve cómo se acumula el volumen.","mal":"Es pi por 2, o sea 6.28, porque el radio al cuadrado es 2. Más abajo se ve cómo se acumula el volumen."}),
 sec("El volumen que se acumula","El volumen",P("Mira cómo crece el volumen y qué área tiene el disco en cada x."),{"t":"acercando","ds":[1,2,3,4],"alt":"El área bajo la recta que va creciendo y representa el volumen acumulado del sólido"},P("Con x igual a 4 el volumen acumulado es <b>25.13</b>. Ese es el valor de la integral.")),
 sec("Método de los discos","Discos",P("Cada disco tiene radio igual al valor de la función, así que su cara tiene área pi por el radio al cuadrado. El volumen es la suma de esas áreas."),
   EQ("V=\\pi\\int_{a}^{b}\\left[f(x)\\right]^{2}dx"),
   PASOS([("V=\\pi\\int_{0}^{4}\\left(\\sqrt{x}\\right)^{2}dx=\\pi\\int_{0}^{4}x\\,dx","El radio es la raíz de x. Al elevarlo al cuadrado queda x."),
          ("=\\pi\\left[\\dfrac{x^{2}}{2}\\right]_{0}^{4}=\\pi\\cdot 8=8\\pi\\approx 25.13","Se integra y se evalúa. Es el mismo valor que mostraba la gráfica.")]),
   OJO("El radio se eleva al cuadrado antes de integrar, y el pi sale de la integral.")),
 sec("Método de las arandelas","Arandelas",P("Si la región queda entre dos curvas, el sólido tiene un hueco y cada rebanada es una {{gl:arandela|arandela}}. Su área es la de la cara grande menos la del hueco."),
   EQ("V=\\pi\\int_{a}^{b}\\left(R^{2}-r^{2}\\right)dx"),
   PASOS([("y=\\sqrt{x}\\ \\text{y}\\ y=\\dfrac{x}{2}\\ \\Rightarrow\\ x=0\\ \\text{o}\\ x=4","Se hallan los cortes. Arriba va la raíz de x, que es el radio exterior R, y abajo va x sobre 2, que es el interior r."),
          ("V=\\pi\\int_{0}^{4}\\left(x-\\dfrac{x^{2}}{4}\\right)dx","Se elevan los dos radios al cuadrado y se restan."),
          ("=\\pi\\left(8-\\dfrac{16}{3}\\right)=\\dfrac{8\\pi}{3}\\approx 8.38","Se integra y se evalúa.")]),
   OJO("Se restan los cuadrados de los radios, no se eleva al cuadrado la resta. Es decir, R cuadrado menos r cuadrado, y no R menos r todo al cuadrado.")),
 sec("Método de las capas","Capas",P("Cuando el giro es alrededor del eje y, a veces conviene partir el sólido en {{gl:capa|capas}} cilíndricas. Cada una tiene radio x, altura f de x y grosor dx."),
   EQ("V=2\\pi\\int_{a}^{b}x\\,f(x)\\,dx"),
   PASOS([("f(x)=3x-x^{2},\\quad 0\\le x\\le 3,\\quad \\text{giro alrededor del eje}\\ y","La región queda sobre el eje x y gira alrededor del eje y."),
          ("V=2\\pi\\int_{0}^{3}x\\left(3x-x^{2}\\right)dx=2\\pi\\int_{0}^{3}\\left(3x^{2}-x^{3}\\right)dx","Se multiplica por el radio x."),
          ("=2\\pi\\left[x^{3}-\\dfrac{x^{4}}{4}\\right]_{0}^{3}=2\\pi\\cdot\\dfrac{27}{4}=\\dfrac{27\\pi}{2}\\approx 42.41","Se integra y se evalúa.")])),
 sec("Cuál método usar","Cuál usar",P("Se elige el que dé la integral más fácil."),
   PASOS([("\\text{Giro alrededor del eje }x\\ \\Rightarrow\\ \\text{discos o arandelas con}\\ dx","Las rebanadas son perpendiculares al eje de giro."),
          ("\\text{Giro alrededor del eje }y\\ \\Rightarrow\\ \\text{capas con}\\ dx,\\ \\text{o discos con}\\ dy","Las capas evitan tener que despejar x en términos de y.")])),
 eng("Una pieza torneada","Un eje cónico se fabrica en un torno. Su perfil gira alrededor de su propio eje, así que su volumen es un sólido de revolución. Con él se calcula el peso del material que se necesita.","r(x)=1+\\dfrac{x}{2}\\ \\text{cm},\\quad 0\\le x\\le 4",
   [("Largo de la pieza","4 cm"),("Radio","de 1 cm a 3 cm"),("Densidad del acero","7.85 g/cm³")],"Por discos, el volumen es pi por la integral de (1 + x/2) al cuadrado entre 0 y 4, o sea 52 pi sobre 3, unos 54.5 centímetros cúbicos. Con la densidad del acero, la pieza pesa unos 427 gramos. Es un modelo simplificado, porque no incluye chaflanes ni agujeros."),
 completar("Se aplica el método de los discos a la región bajo la raíz de x. Falta lo que se integra.","V=\\pi\\int_{0}^{4}[[hueco]]\\,dx",
   [("x","x"),("\\sqrt{x}","raíz de x"),("x^{2}","x al cuadrado")],0,
   ["","Falta elevar el radio al cuadrado. El radio es la raíz de x y su cuadrado es x.","El cuadrado de la raíz de x es x y no x al cuadrado. Elevar dos veces es de más."],"Eleva el radio al cuadrado.","El radio es la raíz de x. Su cuadrado es x, y por eso se integra x."),
 error("Alguien calculó el volumen de la arandela y se equivocó en un paso. Toca el paso que está mal.",
   [("R=\\sqrt{x},\\quad r=\\dfrac{x}{2},\\quad 0\\le x\\le 4","Se identifican los dos radios y el intervalo.","R es raíz de x, r es x sobre 2, de 0 a 4"),
    ("V=\\pi\\int_{0}^{4}\\left(\\sqrt{x}-\\dfrac{x}{2}\\right)^{2}dx","Este paso es el que falla.","V es pi por la integral de 0 a 4 de raíz de x menos x sobre 2, todo al cuadrado"),
    ("=\\pi\\int_{0}^{4}\\left(x-\\sqrt{x}\\,x+\\dfrac{x^{2}}{4}\\right)dx","La cuenta sigue con lo que viene del paso anterior.","Se desarrolla el cuadrado"),
    ("\\text{El resultado no corresponde al volumen del sólido}","El resultado depende del paso que falló.","El resultado no corresponde al volumen del sólido")],1,
   "El área de una arandela es pi por R al cuadrado menos pi por r al cuadrado, y no pi por la resta de los radios al cuadrado. Hay que elevar cada radio por separado y luego restar.",
   "V=\\pi\\int_{0}^{4}\\left(\\left(\\sqrt{x}\\right)^{2}-\\left(\\dfrac{x}{2}\\right)^{2}\\right)dx=\\pi\\int_{0}^{4}\\left(x-\\dfrac{x^{2}}{4}\\right)dx","Piensa cuál es el área de una arandela. ¿Es el área de la cara grande menos la del hueco?"),
 ordenar("Estos son los pasos para el volumen con capas de la región bajo 3x menos x al cuadrado, pero están desordenados.",
   [("V=2\\pi\\int_{0}^{3}x\\,f(x)\\,dx","El volumen es 2 pi por la integral de x por f de x"),
    ("=2\\pi\\int_{0}^{3}x\\left(3x-x^{2}\\right)dx","Se reemplaza f de x"),
    ("=2\\pi\\left[x^{3}-\\dfrac{x^{4}}{4}\\right]_{0}^{3}","Se integra"),
    ("=\\dfrac{27\\pi}{2}","Se evalúa y queda 27 pi sobre 2")],[2,0,3,1],
   "Se escribe la fórmula, se reemplaza la función, se integra y se evalúa.","Primero va la fórmula general."),
]
S+=cierre("Mini simulacro de volúmenes de revolución",[
 mcq("El volumen del sólido al rotar la región bajo $y=x$, sobre $[0,1]$, alrededor del eje $x$ (discos) es:",["$\\dfrac{\\pi}{3}$","$\\dfrac{\\pi}{2}$","$\\pi$","$\\dfrac{2\\pi}{3}$"],0,"Discos. $V=\\pi\\int_0^1 [R(x)]^2\\,dx=\\pi\\int_0^1 x^2\\,dx=\\frac{\\pi}{3}$."),
 num("El volumen del sólido al rotar $y=x^{2}$, $0\\le x\\le 1$, alrededor del eje $x$ es (decimal, 4 cifras):","0.6283",0.005,"Discos. $V=\\pi\\int_0^1 x^4\\,dx=\\frac{\\pi}{5}\\approx 0.6283$."),
 mcq("El método de CAPAS (cascarones cilíndricos) para rotar una región alrededor del eje $y$ usa:",["$V = 2\\pi\\displaystyle\\int_a^b x\\,f(x)\\,dx$","$V = \\pi\\displaystyle\\int_a^b f(x)^{2}\\,dx$","$V = \\displaystyle\\int_a^b f(x)\\,dx$","$V = 2\\pi\\displaystyle\\int_a^b f(x)\\,dx$"],0,"Cada capa tiene radio $x$, altura $f(x)$ y grosor $dx$, así que su volumen es $2\\pi x\\,f(x)\\,dx$.")])
prac=[
 {"titulo":"El área del disco","grafica":{"draw":1},"bloques":[P("Esta curva es el área de la cara de cada disco."),EQ("A(x)=\\pi x")]},
 {"titulo":"El punto de partida","grafica":{"draw":1,"hole":1},"bloques":[P("El volumen se empieza a acumular desde x igual a 0.")]},
 {"titulo":"Mueve x","grafica":{"draw":1,"hole":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La zona sombreada es el volumen acumulado y abajo se ve el área del disco en x.")]},
 {"titulo":"El disco","grafica":{"draw":1,"hole":1,"guide":1},"laboratorio":True,"d":2,"bloques":[P("La franja amarilla es un disco delgado. Con x igual a 2 su cara mide 6.28 y el volumen acumulado es 6.28.")]},
 {"titulo":"El volumen","grafica":{"draw":1,"hole":1,"guide":1,"ok":True},"laboratorio":True,"d":3.7,"bloques":[EQ("V=\\pi\\int_{0}^{4}x\\,dx=8\\pi\\approx 25.13"),P("Con x igual a 3.7 el volumen ya es 21.5. En x igual a 4 llega a 25.13, que es 8 pi.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"hole":1,"guide":1,"ok":True,"d":3.7},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Eleva el radio al cuadrado y no olvides el pi."}]}]
preg={"tex":"\\text{Giro de}\\ y=x^{3},\\ 0\\le x\\le 1,\\ \\text{alrededor del eje}\\ x","opciones":["$\\dfrac{\\pi}{7}$","$\\dfrac{\\pi}{4}$","$\\dfrac{2\\pi}{7}$","$\\dfrac{1}{7}$"],"correcta":0,
 "explicacion":"Por discos, el radio es x al cubo y su cuadrado es x a la sexta. El volumen es pi por la integral de x a la sexta entre 0 y 1, que es pi por 1 sobre 7.",
 "verificacion":{"formula":"pi*(1)^7/7+0*x","a":0,"esperado":0.4487989505},
 "pistas":["Se gira alrededor del eje x, así que se usan discos.","El radio es x al cubo. Elévalo al cuadrado.","Integra x a la sexta entre 0 y 1 y multiplica por pi."],
 "errores":["","Es la integral de x al cubo por pi. Falta elevar el radio al cuadrado.","Se usó el 2 pi de las capas. Con discos solo va pi.","Falta el pi. El volumen es pi por la integral."]}
res=["Con discos, el volumen es pi por la integral del radio al cuadrado.","Con arandelas, se restan los cuadrados de los radios, R cuadrado menos r cuadrado.","Con capas alrededor del eje y, el volumen es 2 pi por la integral de x por f de x."]
write(lesson("calcint-m3-l1","Lección 1 de 5","Volúmenes de revolución",28,graf,glos,ver,S,prac,preg,res,modulo=MOD),"calcint-volumenes.json")
