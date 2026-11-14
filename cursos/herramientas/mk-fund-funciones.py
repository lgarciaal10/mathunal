import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 3 Relaciones y funciones"
R=lagr([0,0,0,1,2**0.5,3**0.5,2]); CC=lagr([0,0,0,1,2,3,4])
EL=[{"t":"trazo","puntos":[[str(t/4),str((t/4)**2)] for t in range(-12,13)],"c":0},
 {"t":"recta","p":["0","x-2"],"dir":["1","0"],"c":3,"guia":True},
 {"t":"punto","p":[R,CC],"c":2},
 {"t":"punto","p":["-("+R+")",CC],"c":2}]
graf={"tipo":"plano","x":[-4.4,4.4],"y":[-3.4,5.0],"a":0,"b":6,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"valor de c","formula":"x-2"},{"rotulo":"cantidad de x con f(x) igual a c","formula":lagr([0,0,1,2,2,2,2])}],
 "etiquetas":["Altura de la recta horizontal","Cuántas entradas tienen esa salida"],"etiquetaSlider":"Posición de la recta, de 0 a 6",
 "alt":"La parábola y igual a x al cuadrado y una recta horizontal y igual a c que se mueve con el deslizador. Con c negativo la recta no toca la curva. Con c igual a 0 la toca en un punto y con c positivo la toca en dos puntos"}
glos={"inyectiva":"Una función es inyectiva si entradas distintas dan salidas distintas. Si f de a es igual a f de b, entonces a es igual a b.",
 "sobreyectiva":"Una función es sobreyectiva si todo elemento del codominio es la salida de alguna entrada.",
 "biyectiva":"Una función es biyectiva si es inyectiva y sobreyectiva. Solo una función biyectiva tiene inversa.",
 "codominio":"El codominio es el conjunto en el que se declara que caen las salidas. No es lo mismo que la imagen, que son las salidas que realmente ocurren."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La curva es y igual a x al cuadrado y la recta horizontal es y igual a c. Cada punto de corte es una entrada que da la salida c."],
 [4,9,"Con c igual a menos 2 la recta no toca la curva. Ninguna entrada da menos 2, así que la función no es sobreyectiva."],
 [9,15,"Con c igual a 1 la recta corta en dos puntos, x igual a menos 1 y x igual a 1. Dos entradas distintas dan la misma salida, así que no es inyectiva."],
 [15,19,"Con c igual a 0 hay un solo punto, y con c igual a 4 vuelven a aparecer dos, el menos 2 y el 2."],
 [19,24,"Una función es inyectiva si ninguna recta horizontal corta la gráfica más de una vez, y sobreyectiva si toda recta horizontal la corta al menos una vez."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[9,3],[14,3],[15,2],[17,2],[18,6],[24,6]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[19,24]}}
S=[
 sec("La idea",None,P("Una función asigna a cada entrada una sola salida. Se pregunta de dos maneras si la asignación es buena. Es {{gl:inyectiva|inyectiva}} si nunca dos entradas distintas comparten salida, y es {{gl:sobreyectiva|sobreyectiva}} si todo elemento del {{gl:codominio|codominio}} se alcanza. Cuando se cumplen las dos es {{gl:biyectiva|biyectiva}}, y solo entonces se puede invertir.")),
 sec("Un ejemplo","Un ejemplo",P("La función f de x igual a x al cuadrado, de los reales en los reales. Mueve la recta horizontal y mira cuántas entradas tienen cada salida."),EQ("f:\\mathbb{R}\\to\\mathbb{R},\\qquad f(x)=x^{2}"),{"t":"grafica","animar":"dibujar","alt":"La parábola con una recta horizontal"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En la función x al cuadrado, ¿cuántas entradas distintas tienen salida 9?","opciones":[0,1,2,3],"correcta":2,"bien":"Muy bien. Son 3 y menos 3. Más abajo se ve esto con la recta horizontal.","mal":"Son 2, el 3 y el menos 3, porque los dos al cuadrado dan 9. Más abajo se ve esto con la recta horizontal."}),
 sec("Recorriendo la recta","La recta",P("Mira la recta horizontal con c igual a menos 2, 1, 0 y 4."),{"t":"acercando","ds":[0,3,2,6],"alt":"La recta horizontal en cuatro alturas"},P("Con c negativo no hay cortes. Con c positivo hay dos. Solo con c igual a 0 hay uno.")),
 sec("Cómo se prueba","Cómo se prueba",P("Cada propiedad se prueba de una manera propia."),
   PASOS([("f(a)=f(b)\\ \\Rightarrow\\ a=b","Inyectiva. Se supone que dan la misma salida y se llega a que las entradas son iguales."),
          ("\\forall y\\in B\\ \\exists x\\in A:\\ f(x)=y","Sobreyectiva. Se toma una salida cualquiera y se encuentra una entrada que la produce."),
          ("f(x)=2x+1:\\ 2a+1=2b+1\\Rightarrow a=b","Ejemplo. La función lineal con pendiente distinta de cero es inyectiva."),
          ("y=2x+1\\Rightarrow x=\\dfrac{y-1}{2}","Y es sobreyectiva, porque para cada y se despeja una entrada.")]),
   OJO("El codominio importa. La función x al cuadrado no es sobreyectiva de R en R, pero sí lo es de R en los reales no negativos.")),
 sec("Composición","Composición",P("Cuando se encadenan dos funciones, las propiedades se heredan."),
   PASOS([("f\\ \\text{y}\\ g\\ \\text{inyectivas}\\ \\Rightarrow\\ g\\circ f\\ \\text{inyectiva}","Si g de f de a1 es g de f de a2, la inyectividad de g da f de a1 igual a f de a2, y la de f da a1 igual a a2."),
          ("f\\ \\text{y}\\ g\\ \\text{sobreyectivas}\\ \\Rightarrow\\ g\\circ f\\ \\text{sobreyectiva}","Dado c, hay un b con g de b igual a c, y un a con f de a igual a b."),
          ("f\\ \\text{y}\\ g\\ \\text{biyectivas}\\ \\Rightarrow\\ g\\circ f\\ \\text{biyectiva}","Y su inversa es f inversa compuesta con g inversa.")]),
   OJO("La inversa de una composición invierte el orden. Para deshacer primero g y luego f, se aplica g inversa y después f inversa.")),
 eng("Un sensor que no se puede invertir","Un sensor entrega el voltaje V igual a T menos 20, al cuadrado, para una temperatura T entre 10 y 30 grados. Las temperaturas 15 y 25 dan el mismo voltaje, así que a partir del voltaje no se puede saber cuál fue la temperatura. La función no es inyectiva.","V=(T-20)^{2}",
   [("Temperatura 15 grados","V igual a 25"),("Temperatura 25 grados","V igual a 25"),("Solución","restringir el dominio a T mayor o igual que 20")],"Para poder calibrar el sensor se necesita una función inyectiva, que se logra restringiendo el dominio, es decir el intervalo de temperaturas, a una sola rama de la parábola. Ahí la función pasa a ser biyectiva sobre su imagen y se puede despejar T a partir de V. Esta es la razón por la que los sensores se diseñan con respuesta monótona."),
 completar("Se prueba que una función es inyectiva. Falta la conclusión.","f(a)=f(b)\\ \\Rightarrow\\ [[hueco]]",
   [("a=b","las entradas son iguales"),("a\\ne b","las entradas son distintas"),("f(a)=0","la salida es cero")],0,
   ["","Si las salidas son iguales y las entradas fueran distintas, la función no sería inyectiva.","Que la salida sea cero no es lo que se quiere probar."],"Salidas iguales deben venir de entradas iguales.","Una función inyectiva no repite salidas, así que f de a igual a f de b obliga a que a sea igual a b."),
 error("Alguien dijo que x al cuadrado es sobreyectiva de R en R y se equivocó en un paso. Toca el paso que está mal.",
   [("f(2)=4","El 4 tiene una entrada que lo produce.","el 4 sí se alcanza"),
    ("f(-3)=9","El 9 también.","el 9 sí se alcanza"),
    ("\\text{Entonces}\\ f\\ \\text{es sobreyectiva}","Este paso es el que falla.","se concluye que es sobreyectiva")],2,
   "Para ser sobreyectiva debe alcanzarse todo número real, y no solo algunos. El número menos 1 no es el cuadrado de ningún real, así que la función no es sobreyectiva.",
   "\\nexists\\,x\\in\\mathbb{R}:\\ x^{2}=-1","Busca un valor del codominio que no se alcance."),
 ordenar("Estos son los pasos para probar que f de x igual a 2x más 1 es inyectiva, pero están desordenados.",
   [("f(a)=f(b)","Se supone la misma salida"),
    ("2a+1=2b+1","Se escribe con la fórmula"),
    ("2a=2b","Se resta 1 a los dos lados"),
    ("a=b","Se divide entre 2, y la función es inyectiva")],[2,0,3,1],
   "Se parte de salidas iguales y se despeja hasta que las entradas son iguales.","Se empieza suponiendo que las salidas son iguales."),
]
S+=cierre("Mini simulacro de funciones inyectivas, sobreyectivas y biyectivas",[
 banco("fu_c3_09","Una función lineal con pendiente distinta de cero es inyectiva y sobreyectiva."),
 banco("fu_c3_10","La función x al cuadrado repite salidas y no alcanza los negativos."),
 banco("fu_c3_11","Doblar enteros es inyectivo, pero no alcanza los números impares.")])
prac=[
 {"titulo":"La función","grafica":{"draw":1,"guide":1},"bloques":[P("La parábola con una recta horizontal que se mueve."),EQ("f(x)=x^{2}")]},
 {"titulo":"Mueve la recta","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 6. Abajo se lee la altura de la recta y cuántas entradas tienen esa salida.")]},
 {"titulo":"Dos entradas, una salida","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("f(-1)=f(1)=1"),P("Con c igual a 1 la recta corta en dos puntos. Por eso la función no es inyectiva.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Una composición de inyectivas conserva la inyectividad."}]}]
preg={"tex":"\\text{Si}\\ f\\ \\text{y}\\ g\\ \\text{son inyectivas, entonces}\\ g\\circ f\\ \\text{es}","opciones":["inyectiva","sobreyectiva pero no inyectiva","ni inyectiva ni sobreyectiva","necesariamente biyectiva"],"correcta":0,
 "explicacion":"Si g de f de a1 es igual a g de f de a2, la inyectividad de g da f de a1 igual a f de a2, y la de f da a1 igual a a2. Pero no se puede asegurar que sea sobreyectiva, así que tampoco biyectiva.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Pide que no se repitan salidas.","Aplica la inyectividad dos veces.","Es inyectiva."],
 "errores":["","No ocurre siempre. La composición de inyectivas es inyectiva, así que no puede ser no inyectiva.","La composición de inyectivas conserva la inyectividad, así que no puede ser ninguna de las dos negaciones.","Para ser biyectiva faltaría la sobreyectividad, y eso no se puede asegurar."]}
res=["Inyectiva significa que ninguna salida se repite, y sobreyectiva que todo el codominio se alcanza.","La prueba de inyectividad parte de f de a igual a f de b, y la de sobreyectividad parte de una salida cualquiera.","Una composición de inyectivas es inyectiva, una de sobreyectivas es sobreyectiva, y una de biyectivas es biyectiva."]
write(lesson("fu-m3-l1","Lección 1 de 5","Funciones inyectivas, sobreyectivas y biyectivas",30,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-funciones.json")
