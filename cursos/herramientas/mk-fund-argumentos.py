import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 1 Lógica y argumentación"
FIL=[[1,1,1,1,1],[1,0,0,0,1],[0,1,1,1,0],[0,0,1,0,0]]
EL,WX,WY=tabla(["p","q","P1","P2","C"],FIL)
PREM=lagr([1,0,1,0]); CONC=lagr([1,1,0,0])
graf={"tipo":"plano","x":WX,"y":WY,"a":0,"b":3,"inicio":0,"entero":True,"sinejes":True,"elementos":EL,
 "lecturas":[{"rotulo":"las dos premisas son verdaderas (1 si es cierto)","formula":PREM},{"rotulo":"la conclusión es verdadera (1 si es cierto)","formula":CONC}],
 "etiquetas":["Valor de las dos premisas juntas, 1 si ambas son verdaderas","Valor de la conclusión, 1 si es verdadera"],"etiquetaSlider":"Fila de la tabla, de 0 a 3",
 "alt":"La tabla de verdad del argumento de p implica q y q, luego p. Hay columnas para p, q, la premisa P1, la premisa P2 y la conclusión C. En la fila en que p es falsa y q es verdadera las dos premisas son verdaderas y la conclusión es falsa, así que el argumento es inválido"}
glos={"premisa":"Una premisa es una proposición que se acepta como punto de partida en un argumento.",
 "conclusion":"La conclusión es la proposición que se quiere obtener a partir de las premisas.",
 "valido":"Un argumento es válido si en toda fila en que las premisas son verdaderas, la conclusión también lo es. La validez habla de la forma, no de si las premisas son ciertas.",
 "falacia":"Una falacia es un razonamiento que parece válido pero no lo es, porque existe una fila con premisas verdaderas y conclusión falsa."}
ver={"duracion":24.0,"capitulos":[
 [0,5,"Este argumento tiene dos premisas, P1 que dice p implica q, y P2 que dice q. La conclusión C es p. Veamos si es válido."],
 [5,10,"Recorre las filas. Un argumento es válido si, cada vez que las dos premisas son verdaderas, la conclusión también lo es."],
 [10,17,"En la fila 2, p es falsa y q es verdadera. Las dos premisas son verdaderas, pero la conclusión es falsa."],
 [17,21,"Esa sola fila es un contraejemplo. El argumento es inválido, y se llama afirmar el consecuente."],
 [21,24,"Para mostrar que un argumento es inválido basta un contraejemplo, y para mostrar que es válido hay que revisar todas las filas."]],
 "canales":{"draw":[[0.3,0],[4.5,1]],"d":[[5,0],[8,0],[9,1],[11,1],[12,2],[22,2],[23,3],[24,3]],"guide":[[5,0],[6,1]]},
 "intervalos":{"ok":[17,24]}}
S=[
 sec("La idea",None,P("Un argumento tiene {{gl:premisa|premisas}} y una {{gl:conclusion|conclusión}}. Es {{gl:valido|válido}} si, siempre que las premisas son verdaderas, la conclusión también lo es. Si existe una sola fila donde las premisas son verdaderas y la conclusión falsa, el razonamiento es una {{gl:falacia|falacia}}. Validez y verdad son cosas distintas, porque un argumento válido puede partir de premisas falsas.")),
 sec("Un ejemplo","Un ejemplo",P("Esta tabla revisa el argumento de que si p implica q, y q es verdadera, entonces p. P1 es p implica q, P2 es q y C es la conclusión p."),EQ("p\\rightarrow q,\\ \\ q\\ \\ \\therefore\\ \\ p"),{"t":"grafica","animar":"dibujar","alt":"La tabla del argumento"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Para probar que un argumento es inválido hay que encontrar una fila con premisas verdaderas y conclusión falsa. ¿Cuántas filas así se necesitan?","opciones":[1,2,3,4],"correcta":1,"bien":"Muy bien. Una sola fila basta. Más abajo se ve en la tabla.","mal":"Basta una. Un solo contraejemplo ya rompe la validez. Más abajo se ve en la tabla."}),
 sec("Recorriendo las filas","Las filas",P("Mira las dos lecturas en cada fila."),{"t":"acercando","ds":[0,1,2,3],"alt":"Las cuatro filas de la tabla"},P("En la fila 2 las premisas valen 1 y la conclusión vale 0. Ese es el contraejemplo.")),
 sec("Las formas válidas","Formas válidas",P("Estas cuatro formas son válidas, y vale la pena reconocerlas de memoria."),
   PASOS([("p\\rightarrow q,\\ \\ p\\ \\ \\therefore\\ \\ q","Modus ponens. Si se cumple la condición, se cumple la consecuencia."),
          ("p\\rightarrow q,\\ \\ \\neg q\\ \\ \\therefore\\ \\ \\neg p","Modus tollens. Si la consecuencia falla, la condición no pudo cumplirse."),
          ("p\\rightarrow q,\\ \\ q\\rightarrow r\\ \\ \\therefore\\ \\ p\\rightarrow r","Silogismo hipotético. Los condicionales se encadenan."),
          ("p\\vee q,\\ \\ \\neg p\\ \\ \\therefore\\ \\ q","Silogismo disyuntivo. Si una de dos opciones falla, se cumple la otra.")]),
   OJO("Afirmar el consecuente, de p implica q y q concluir p, y negar el antecedente, de p implica q y no p concluir no q, parecen válidos pero no lo son.")),
 sec("Cómo se prueba una falacia","Contraejemplos",P("Para mostrar que un argumento es inválido basta dar valores que hagan verdaderas las premisas y falsa la conclusión."),
   PASOS([("p\\rightarrow q,\\ \\ \\neg p\\ \\ \\therefore\\ \\ \\neg q","Se quiere ver si negar el antecedente permite negar el consecuente."),
          ("p=F,\\ \\ q=V","Se elige este caso."),
          ("p\\rightarrow q=V,\\ \\ \\neg p=V,\\ \\ \\neg q=F","Las premisas valen V y la conclusión vale F, así que es una falacia.")]),
   OJO("Que un argumento sea válido no significa que su conclusión sea cierta. Si una premisa es falsa, la conclusión puede ser falsa aunque el argumento sea válido.")),
 eng("Diagnóstico de una falla","Un técnico razona así. Si el fusible se quemó, el motor no arranca. El motor no arranca, luego el fusible se quemó. Ese razonamiento afirma el consecuente. El motor puede no arrancar por una batería descargada o por un contacto suelto.","p\\rightarrow q,\\ \\ q\\ \\ \\not\\therefore\\ \\ p",
   [("Premisas","2"),("Causas posibles de que no arranque","varias"),("Conclusión que sí es válida","si arranca, el fusible está bien")],"El razonamiento válido es el contrarrecíproco. Si el motor arranca, el fusible no se quemó. Un diagnóstico sensato usa modus tollens para descartar causas, y no afirma el consecuente para señalar una sola. Cada causa descartada acota el problema, pero un síntoma por sí solo no prueba qué falló."),
 completar("Se usa modus tollens. Falta la conclusión.","p\\rightarrow q,\\ \\ \\neg q\\ \\ \\therefore\\ \\ [[hueco]]",
   [("\\neg p","no p"),("p","p"),("q","q")],0,
   ["","Concluir p no es válido. Con la premisa de que q es falsa, lo válido es concluir no p.","La segunda premisa ya dice que q es falsa, así que no se puede concluir q."],"Si la consecuencia falla, la condición no pudo cumplirse.","De p implica q y no q se concluye no p."),
 error("Alguien razonó con dos premisas y se equivocó en un paso. Toca el paso que está mal.",
   [("p\\rightarrow q","Primera premisa.","si llueve, la calle se moja"),
    ("q","Segunda premisa.","la calle está mojada"),
    ("\\text{Entonces}\\ p\\ \\text{por modus ponens}","Este paso es el que falla.","entonces llovió")],2,
   "Modus ponens necesita la condición p como premisa. Aquí se tiene la consecuencia q, y concluir p es afirmar el consecuente. q pudo ser verdadera por otra razón distinta de p.",
   "p\\rightarrow q,\\ \\ q\\ \\ \\not\\therefore\\ \\ p","Pregúntate si la calle solo se moja cuando llueve."),
 ordenar("Estos son los pasos para concluir r a partir de p, de p implica q y de q implica r, pero están desordenados.",
   [("p","Se parte de la premisa p"),
    ("q","Con p implica q y modus ponens se obtiene q"),
    ("q\\rightarrow r","Se toma la premisa q implica r"),
    ("r","Con q, q implica r y modus ponens se obtiene r")],[2,0,3,1],
   "Se aplica modus ponens dos veces, y la conclusión de la primera es la premisa de la segunda.","Se empieza con la premisa que no es un condicional."),
]
S+=cierre("Mini simulacro de formas de argumento e inferencia",[
 banco("fu_c1_08","Es modus tollens. Si q es falsa y p implica q, entonces p es falsa."),
 banco("fu_c1_16","De p implica q y no q se concluye no p."),
 banco("fu_c1_18","Es el silogismo disyuntivo. Si una opción falla, se cumple la otra.")])
prac=[
 {"titulo":"El argumento","grafica":{"draw":1,"guide":1},"bloques":[P("La tabla del argumento de p implica q y q, luego p."),EQ("p\\rightarrow q,\\ q\\ \\therefore\\ p")]},
 {"titulo":"Recorre las filas","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 3. Abajo se leen las premisas juntas y la conclusión.")]},
 {"titulo":"El contraejemplo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("p=F,\\ q=V\\ \\Rightarrow\\ P1=P2=V,\\ C=F"),P("En la fila 2 las premisas valen 1 y la conclusión vale 0.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Busca cuál de los razonamientos afirma el consecuente."}]}]
preg={"tex":"\\text{Cuál de estos razonamientos es inválido}","opciones":["De $p\\rightarrow q$ y $q$ se concluye $p$","De $p\\rightarrow q$ y $p$ se concluye $q$","De $p\\rightarrow q$ y $\\neg q$ se concluye $\\neg p$","De $p\\rightarrow q$ y $q\\rightarrow r$ se concluye $p\\rightarrow r$"],"correcta":0,
 "explicacion":"Concluir p a partir de p implica q y de q es afirmar el consecuente. Falla en la fila p falsa y q verdadera. Los otros tres son modus ponens, modus tollens y silogismo hipotético, que son válidos.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Busca el que concluye algo a partir de la consecuencia.","Una de las opciones usa q para obtener p.","Es la primera."],
 "errores":["","Esa es modus ponens y es válida.","Esa es modus tollens y es válida.","Esa es el silogismo hipotético y es válida."]}
res=["Un argumento es válido si en toda fila con premisas verdaderas la conclusión es verdadera.","Las formas válidas básicas son modus ponens, modus tollens, silogismo hipotético y silogismo disyuntivo.","Afirmar el consecuente y negar el antecedente son falacias, y se prueban con un contraejemplo."]
write(lesson("fu-m1-l3","Lección 3 de 3","Formas de argumento e inferencia",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-argumentos.json")
