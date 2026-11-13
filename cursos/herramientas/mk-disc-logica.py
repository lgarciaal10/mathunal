import os, math
os.environ['CURSO_FU']='Matemáticas Discretas'; os.environ['BANCO']='discretas'
from mklib import *
from fundlib import *
MOD="Módulo 1 Lógica y demostración"
FIL=[[1,1,1,1],[1,0,0,0],[0,1,1,1],[0,0,1,1]]
EL,WX,WY=tabla(["p","q","p→q","¬p∨q"],FIL)
IMP=lagr([1,0,1,1])
graf={"tipo":"plano","x":WX,"y":WY,"a":0,"b":3,"inicio":0,"entero":True,"sinejes":True,"elementos":EL,
 "lecturas":[{"rotulo":"p implica q en esta fila","formula":IMP},{"rotulo":"no p o q en esta fila","formula":IMP}],
 "etiquetas":["Valor de p implica q, 1 si es verdadera","Valor de no p o q, 1 si es verdadera"],"etiquetaSlider":"Fila de la tabla, de 0 a 3",
 "alt":"La tabla de verdad de p implica q y de no p o q. Las dos columnas son idénticas, falsas solo en la fila en que p es verdadera y q es falsa. Un cuadro resalta la fila elegida"}
glos={"proposicion":"Una proposición es una afirmación que es verdadera o falsa, pero no las dos. Se representa con letras como p y q.",
 "conectivo":"Un conectivo une proposiciones. Los principales son y, o, no, implica y si y solo si.",
 "equivalencia":"Dos proposiciones son lógicamente equivalentes si tienen el mismo valor de verdad en todas las filas de la tabla.",
 "tautologia":"Una tautología es una proposición que es verdadera en todas las filas. Una contradicción es falsa en todas."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Una proposición es verdadera o falsa. Con dos proposiciones, p y q, hay cuatro casos posibles, que son las cuatro filas de la tabla."],
 [4,8,"La columna de p implica q es falsa en una sola fila, cuando p es verdadera y q es falsa. En las demás es verdadera."],
 [8,14,"Mueve el cuadro para recorrer las filas. La última columna, no p o q, da exactamente los mismos valores. Por eso las dos proposiciones son equivalentes."],
 [14,18,"En la fila 1, p es verdadera y q es falsa. Las dos columnas valen falso."],
 [18,22,"Con cuatro proposiciones habría 16 filas, porque cada proposición nueva duplica el número de filas."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[10,3],[13,0],[14,1],[22,1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("La lógica estudia cuándo un razonamiento es correcto. Su material son las {{gl:proposicion|proposiciones}}, que se combinan con {{gl:conectivo|conectivos}}. Para decidir si dos expresiones dicen lo mismo, se usan tablas de verdad, y si coinciden en todas las filas son {{gl:equivalencia|equivalentes}}.")),
 sec("Un ejemplo","Un ejemplo",P("Mira la tabla de verdad del condicional y de su forma con o y no."),EQ("p\\rightarrow q\\ \\equiv\\ \\neg p\\vee q"),{"t":"grafica","animar":"dibujar","alt":"La tabla de verdad"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con una proposición hay dos filas, con dos hay cuatro. Cada proposición nueva duplica las filas. ¿Cuántas filas tiene la tabla con tres proposiciones?","opciones":[3,6,8,9],"correcta":8,"bien":"Muy bien. Son 8, que es 2 al cubo. Más abajo se ve la tabla con dos.","mal":"Son 8, porque 4 por 2 es 8, o sea 2 al cubo. Más abajo se ve la tabla con dos."}),
 sec("Recorriendo la tabla","Las filas",P("Mira el valor de las dos columnas en cada fila."),{"t":"acercando","ds":[0,1,2,3],"alt":"Las cuatro filas de la tabla"},P("Las dos columnas coinciden en las cuatro filas. Eso es lo que significa ser lógicamente equivalentes.")),
 sec("Los conectivos","Conectivos",P("Estos son los conectivos, con las ideas más importantes de cada uno."),
   PASOS([("p\\wedge q\\ \\text{es verdadera solo si}\\ p\\ \\text{y}\\ q\\ \\text{lo son}","La conjunción, o sea y."),
          ("p\\vee q\\ \\text{es falsa solo si}\\ p\\ \\text{y}\\ q\\ \\text{son falsas}","La disyunción, o sea o. Es inclusiva."),
          ("p\\rightarrow q\\ \\text{es falsa solo si}\\ p\\ \\text{es V y}\\ q\\ \\text{es F}","El condicional. Una promesa solo se rompe si se cumple la condición y no la consecuencia."),
          ("p\\leftrightarrow q\\ \\text{es verdadera si}\\ p\\ \\text{y}\\ q\\ \\text{valen lo mismo}","El bicondicional.")]),
   OJO("Si p es falsa, p implica q es verdadera sin importar q. Es la parte del condicional que más cuesta aceptar.")),
 sec("Equivalencias útiles","Equivalencias",P("Estas equivalencias permiten reescribir y negar proposiciones."),
   PASOS([("p\\rightarrow q\\ \\equiv\\ \\neg p\\vee q","El condicional como disyunción."),
          ("\\neg(p\\wedge q)\\equiv\\neg p\\vee\\neg q,\\qquad \\neg(p\\vee q)\\equiv\\neg p\\wedge\\neg q","Las leyes de De Morgan."),
          ("\\neg(p\\rightarrow q)\\equiv p\\wedge\\neg q","La negación del condicional. Es la única forma de romper una promesa."),
          ("p\\rightarrow q\\ \\equiv\\ \\neg q\\rightarrow\\neg p","El contrarrecíproco. Tiene el mismo valor que el original, a diferencia del recíproco.")]),
   OJO("El recíproco, q implica p, no es equivalente al original. Se parecen, pero tienen tablas distintas.")),
 eng("El mando a dos manos de una prensa","Una prensa industrial solo debe bajar cuando el operario tiene las dos manos en los botones, y así no puede tenerlas bajo el pistón. Esa regla es una conjunción, y la lógica permite comprobarla fila por fila.","\\text{baja}=A\\wedge B",
   [("Botones","A y B"),("Combinaciones","4 filas"),("Filas que bajan","solo 1")],"La prensa baja únicamente en la fila en que A y B son verdaderos. En las otras tres, la salida es falsa. Si por error se programa A o B, la prensa bajaría con una sola mano y la regla de seguridad quedaría rota. Por eso en ingeniería se verifica una regla lógica con su tabla completa, no solo con los casos que parecen razonables."),
 completar("Se aplica la ley de De Morgan a la negación de una conjunción.","\\neg(p\\wedge q)\\equiv\\neg p\\ [[hueco]]\\ \\neg q",
   [("\\vee","o"),("\\wedge","y"),("\\rightarrow","implica")],0,
   ["","Con y no se cambia el conectivo. En De Morgan la negación convierte la conjunción en disyunción.","Con implica se cambia el tipo de proposición. El resultado de De Morgan es una disyunción."],"La negación intercambia y con o.","La negación de p y q es no p o no q."),
 error("Alguien negó un condicional y se equivocó en un paso. Toca el paso que está mal.",
   [("p\\rightarrow q\\equiv\\neg p\\vee q","El condicional como disyunción.","p implica q es no p o q"),
    ("\\neg(\\neg p\\vee q)\\equiv p\\wedge\\neg q","Se aplica De Morgan.","por De Morgan queda p y no q"),
    ("\\text{Entonces}\\ \\neg(p\\rightarrow q)\\equiv\\neg p\\wedge q","Este paso es el que falla.","queda no p y q")],2,
   "El resultado del paso anterior ya era la respuesta, p y no q. Escribir no p y q cambia las dos proposiciones, y no es lo que salió de De Morgan.",
   "\\neg(p\\rightarrow q)\\equiv p\\wedge\\neg q","Compara con el resultado del paso anterior."),
 ordenar("Estos son los pasos para probar que un condicional equivale a su contrarrecíproco, pero están desordenados.",
   [("p\\rightarrow q\\equiv\\neg p\\vee q","Se escribe como disyunción"),
    ("\\neg p\\vee q\\equiv q\\vee\\neg p","Se conmuta"),
    ("q\\vee\\neg p\\equiv\\neg(\\neg q)\\vee\\neg p","Se usa la doble negación"),
    ("\\neg(\\neg q)\\vee\\neg p\\equiv\\neg q\\rightarrow\\neg p","Se vuelve al condicional")],[2,0,3,1],
   "Se escribe el condicional como disyunción, se reordena y se vuelve a escribir como condicional.","Se empieza reescribiendo el condicional."),
]
S+=cierre("Mini simulacro de lógica proposicional",[
 banco("di_c1_08","Por De Morgan, la negación de una conjunción es la disyunción de las negaciones."),
 banco("di_c1_05","$p\\wedge\\neg p$ nunca es verdadera, porque $p$ y $\\neg p$ no pueden serlo a la vez. Es una contradicción."),
 banco("di_c1_09","Cada variable duplica las filas, así que con $3$ hay $2^3=8$.")])
prac=[
 {"titulo":"La tabla","grafica":{"draw":1,"guide":1},"bloques":[P("La tabla de verdad de p implica q y de no p o q."),EQ("p\\rightarrow q\\equiv\\neg p\\vee q")]},
 {"titulo":"Recorre las filas","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 3. Abajo se leen los valores de las dos columnas, que son siempre iguales.")]},
 {"titulo":"La fila que rompe","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("p=V,\\ q=F\\ \\Rightarrow\\ p\\rightarrow q=F"),P("En la fila 1 las dos columnas valen 0, es decir, falso.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Recuerda qué se cambia en el contrarrecíproco."}]}]
preg={"tex":"\\text{El contrarrecíproco de}\\ p\\rightarrow q\\ \\text{es}","opciones":["$\\neg q\\rightarrow\\neg p$","$q\\rightarrow p$","$\\neg p\\rightarrow\\neg q$","$p\\wedge\\neg q$"],"correcta":0,
 "explicacion":"El contrarrecíproco niega las dos proposiciones y las intercambia, y tiene el mismo valor de verdad que el original. El recíproco es q implica p, y el inverso es no p implica no q, y ninguno de los dos es equivalente.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Hay que negar las dos proposiciones.","Y después intercambiarlas.","Se obtiene no q implica no p."],
 "errores":["","Ese es el recíproco. No es equivalente al original, porque tiene la tabla distinta.","Ese es el inverso. Se niegan las dos proposiciones, pero falta intercambiarlas.","Esa es la negación del condicional, y no su contrarrecíproco."]}
res=["Un condicional es falso solo cuando la condición es verdadera y la consecuencia es falsa.","Dos proposiciones son equivalentes si coinciden en todas las filas de la tabla, como p implica q y no p o q.","La negación de un condicional es p y no q, y su contrarrecíproco es no q implica no p."]
write(lesson("di-m1-l1","Lección 1 de 4","Lógica proposicional",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Discretas"),"disc-logica.json")
