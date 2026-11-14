import os, math
os.environ['CURSO_FU']='Matemáticas Discretas'; os.environ['BANCO']='discretas'
from mklib import *
from fundlib import *
MOD="Módulo 2 Conjuntos, conteo y combinatoria"
WAYS=[1,2,3,4,5,6,5,4,3,2,1]
EL=[]
for i,w in enumerate(WAYS):
    s=i+2
    EL.append({"t":"poligono","puntos":[[str(s-0.5),"0"],[str(s+0.5),"0"],[str(s+0.5),str(w)],[str(s-0.5),str(w)]],"c":0})
    ind=lagr([1 if j==i else 0 for j in range(11)])
    EL.append({"t":"poligono","puntos":[[str(s-0.5),"0"],[str(s+0.5),"0"],[str(s+0.5),f"{w}*({ind})"],[str(s-0.5),f"{w}*({ind})"]],"c":3})
graf={"tipo":"plano","x":[0.5,14.5],"y":[-1.2,7.2],"a":0,"b":10,"inicio":5,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"suma s de los dos dados","formula":"x+2"},{"rotulo":"probabilidad de esa suma","formula":"("+lagr(WAYS)+")/36"}],
 "etiquetas":["Suma elegida entre 2 y 12","Casos favorables entre 36 casos posibles"],"etiquetaSlider":"Suma de los dados, de 2 a 12",
 "alt":"Barras con el número de formas de obtener cada suma al lanzar dos dados. La suma 2 tiene 1 forma, la suma 7 tiene 6 formas y la suma 12 tiene 1 forma. La suma elegida con el deslizador se resalta en verde"}
glos={"espacio":"El espacio muestral es el conjunto de todos los resultados posibles de un experimento.",
 "evento":"Un evento es un subconjunto del espacio muestral. Su probabilidad es el número de casos favorables entre el de casos posibles, si todos los resultados son igualmente probables.",
 "independientes":"Dos eventos son independientes si la probabilidad de que ocurran ambos es el producto de sus probabilidades.",
 "complementario":"El evento complementario de A es que A no ocurra. Su probabilidad es uno menos la de A."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Cada barra cuenta de cuántas formas se obtiene una suma al lanzar dos dados. Hay 36 resultados posibles."],
 [4,9,"La suma 2 tiene una sola forma, un uno y un uno. Su probabilidad es 1 sobre 36."],
 [9,15,"La suma 7 es la que tiene más formas, seis. Su probabilidad es 6 sobre 36, o sea 0.1667."],
 [15,19,"Después del 7, las barras bajan de forma simétrica."],
 [19,22,"La probabilidad de un evento es los casos favorables entre los casos posibles, cuando todos son igualmente probables."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[7,0],[9,5],[15,5],[16,9],[19,9],[22,9]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[9,15]}}
S=[
 sec("La idea",None,P("Un experimento tiene un {{gl:espacio|espacio muestral}}, que reúne todos sus resultados. Un {{gl:evento|evento}} es un conjunto de resultados, y si todos son igualmente probables, su probabilidad es los casos favorables entre los casos posibles. Con eventos {{gl:independientes|independientes}} las probabilidades se multiplican, y el evento {{gl:complementario|complementario}} se calcula restando de uno.")),
 sec("Un ejemplo","Un ejemplo",P("Al lanzar dos dados hay 36 resultados igualmente probables. Mira de cuántas formas sale cada suma."),EQ("P(A)=\\dfrac{\\text{casos favorables}}{\\text{casos posibles}}"),{"t":"grafica","animar":"dibujar","alt":"Las barras de las formas de cada suma"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Al lanzar dos dados, la suma 7 sale con 1 y 6, 2 y 5, 3 y 4, 4 y 3, 5 y 2, y 6 y 1. ¿Cuántas formas hay?","opciones":[3,4,6,12],"correcta":6,"bien":"Muy bien. Son 6, de un total de 36 resultados. Más abajo se ve la barra.","mal":"Son 6, una por cada pareja de la lista. Hay 36 resultados en total. Más abajo se ve la barra."}),
 sec("Recorriendo las sumas","Las sumas",P("Mira la probabilidad de las sumas 2, 7, 10 y 12."),{"t":"acercando","ds":[0,5,8,10],"alt":"Las sumas 2, 7, 10 y 12"},P("La suma 7 es la más probable, con 6 sobre 36. Las sumas 2 y 12 son las menos probables, con 1 sobre 36.")),
 sec("Probabilidad básica","Probabilidad",P("Para eventos igualmente probables se cuenta."),
   PASOS([("P(A)=\\dfrac{|A|}{|\\Omega|}","Casos favorables entre casos posibles."),
          ("P(\\text{cara})=\\dfrac12=0.5","Una moneda justa."),
          ("P(\\text{dos caras})=\\dfrac12\\cdot\\dfrac12=\\dfrac14","Dos lanzamientos independientes."),
          ("P(\\text{suma 7})=\\dfrac{6}{36}=0.1667","Dos dados.")]),
   OJO("Los 11 valores posibles de la suma no son igualmente probables. Los casos igualmente probables son los 36 pares de resultados de los dos dados.")),
 sec("Reglas","Reglas",P("Algunas reglas permiten calcular sin listar los casos."),
   PASOS([("P(A^{c})=1-P(A)","El complemento."),
          ("P(A\\cup B)=P(A)+P(B)-P(A\\cap B)","La unión, como en la inclusión y exclusión."),
          ("P(A\\cap B)=P(A)\\,P(B)\\ \\text{si son independientes}","El producto de independientes.")]),
   OJO("Que dos eventos no se influyan es una suposición que hay que justificar. No basta con que parezca razonable.")),
 eng("La confiabilidad de un sistema","Dos componentes funcionan cada uno con probabilidad 0.9, y fallan de forma independiente. En serie, el sistema funciona solo si funcionan los dos. En paralelo, funciona si al menos uno funciona.","P_{\\text{serie}}=0.9^{2}=0.81,\\qquad P_{\\text{paralelo}}=1-0.1^{2}=0.99",
   [("Cada componente","0.9"),("En serie","0.81"),("En paralelo","0.99")],"Poner componentes en paralelo sube la confiabilidad del sistema, porque solo falla si fallan los dos. Poner componentes en serie la baja. La cuenta usa dos ideas de esta lección, que son la multiplicación de eventos independientes y el complemento. Supone que las fallas no se contagian, lo que no siempre es cierto."),
 completar("Se calcula la probabilidad de obtener dos caras en dos lanzamientos independientes. Falta el segundo factor.","P(\\text{dos caras})=\\dfrac12\\cdot[[hueco]]",
   [("\\dfrac12","un medio"),("1","uno"),("2","dos")],0,
   ["","Uno sería la probabilidad de un evento seguro, y la segunda cara no es segura.","Una probabilidad no puede ser dos. Siempre está entre 0 y 1."],"El segundo lanzamiento también tiene probabilidad un medio.","Un medio por un medio da un cuarto."),
 error("Alguien calculó la probabilidad de que la suma de dos dados sea 7 y se equivocó en un paso. Toca el paso que está mal.",
   [("36\\ \\text{resultados posibles}","El total de pares de resultados.","hay 36 pares"),
    ("6\\ \\text{casos con suma 7}","Los casos favorables.","hay 6 casos favorables"),
    ("P=\\dfrac{6}{11}","Este paso es el que falla.","hay 11 sumas posibles, así que es 6 sobre 11")],2,
   "Las 11 sumas posibles no son igualmente probables, y por eso no se pueden usar como casos posibles. Los casos igualmente probables son los 36 pares, y la probabilidad es 6 sobre 36, o sea 0.1667.",
   "P=\\dfrac{6}{36}=0.1667","Revisa cuáles resultados son igualmente probables."),
 ordenar("Estos son los pasos para calcular la probabilidad de dos caras en dos lanzamientos, pero están desordenados.",
   [("\\Omega=\\{CC,CS,SC,SS\\}","Se escribe el espacio muestral"),
    ("\\text{casos favorables}=1","Se cuenta el caso CC"),
    ("P=\\dfrac14","Se divide"),
    ("P=0.25","Se escribe en decimal")],[2,0,3,1],
   "Se escribe el espacio muestral, se cuentan los casos favorables y se divide.","Se empieza con todos los resultados."),
]
S+=cierre("Mini simulacro de probabilidad discreta",[
 banco("di_c2_05","Hay un caso favorable, CC, entre 4 casos posibles."),
 banco("di_c2_17","Una moneda justa tiene dos resultados igualmente probables."),
 banco("di_c2_18","$\\dfrac{6}{36}=0.1667$.")])
prac=[
 {"titulo":"Las sumas","grafica":{"draw":1},"bloques":[P("Las formas de obtener cada suma con dos dados."),EQ("P(s)=\\dfrac{\\text{formas}}{36}")]},
 {"titulo":"Recorre las sumas","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la suma elegida y su probabilidad.")]},
 {"titulo":"La suma 7","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5,"bloques":[EQ("P(7)=\\dfrac{6}{36}=0.1667"),P("La suma 7 es la más probable, con 6 formas.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Cuenta las parejas de dados que suman 5."}]}]
preg={"tex":"\\text{Al lanzar dos dados, la probabilidad de que la suma sea 5 es}","opciones":["$\\tfrac19$","$\\tfrac16$","$\\tfrac14$","$\\tfrac1{12}$"],"correcta":0,
 "explicacion":"La suma 5 sale con 1 y 4, 2 y 3, 3 y 2, y 4 y 1, o sea 4 formas. La probabilidad es 4 sobre 36, que se simplifica a 1 sobre 9.",
 "verificacion":{"formula":"4/36+0*x","a":0,"esperado":0.1111},
 "pistas":["Lista las parejas que suman 5.","Son 4.","Son 4 de 36 casos, o sea 1 sobre 9."],
 "errores":["","Un sexto es la probabilidad de la suma 7, que tiene 6 formas.","Un cuarto sería 9 formas, y la suma 5 solo tiene 4.","Un doceavo sería 3 formas, y la suma 5 tiene 4."]}
res=["La probabilidad de un evento es los casos favorables entre los casos posibles, cuando todos son igualmente probables.","El complemento se calcula como uno menos la probabilidad, y los eventos independientes se multiplican.","Al lanzar dos dados la suma 7 es la más probable, con 6 sobre 36."]
write(lesson("di-m2-l3","Lección 3 de 4","Probabilidad discreta",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Discretas"),"disc-probabilidad.json")
