import os, math
os.environ['CURSO_FU']='Matemáticas Discretas'; os.environ['BANCO']='discretas'
from mklib import *
MOD="Módulo 2 Conjuntos, conteo y combinatoria"
EL=[{"t":"poligono","puntos":[["0","1.6"],["20","1.6"],["20","2.6"],["0","2.6"]],"c":0},
 {"t":"poligono","puntos":[["20-x","0.4"],["35-x","0.4"],["35-x","1.4"],["20-x","1.4"]],"c":1},
 {"t":"poligono","puntos":["20-x,0.4".split(","),["20","0.4"],["20","2.6"],["20-x","2.6"]],"c":2},
 {"t":"poligono","puntos":[["0","-1.4"],["35-x","-1.4"],["35-x","-0.4"],["0","-0.4"]],"c":3}]
# el resaltado de la interseccion cubre de 20-x a 20, entre las alturas 0.4 y 2.6
EL[2]["puntos"]=[["20-x","0.4"],["20","0.4"],["20","2.6"],["20-x","2.6"]]
graf={"tipo":"plano","x":[-4.0,39.0],"y":[-2.6,3.8],"a":0,"b":15,"inicio":5,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"elementos en común, la intersección","formula":"x"},{"rotulo":"elementos de la unión, 20 más 15 menos la intersección","formula":"35-x"}],
 "etiquetas":["Cuántos elementos están en A y en B","Tamaño de la unión, que es la barra de abajo"],"etiquetaSlider":"Elementos en común, de 0 a 15",
 "alt":"Tres barras. La de arriba es el conjunto A con 20 elementos y la del medio es el conjunto B con 15. La parte donde se superponen está resaltada. La barra de abajo es la unión y mide 35 menos los elementos en común"}
glos={"union":"La unión reúne los elementos de A, de B o de ambos. Cada elemento se cuenta una sola vez.",
 "inclusion":"El principio de inclusión y exclusión dice que para contar una unión se suman los tamaños y se restan las intersecciones, para no contar dos veces los elementos comunes.",
 "diferencia":"La diferencia A menos B reúne los elementos de A que no están en B. Es lo mismo que A intersección el complemento de B.",
 "potencia":"El conjunto potencia de A tiene todos los subconjuntos de A. Si A tiene n elementos, el conjunto potencia tiene dos elevado a n."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"El conjunto A tiene 20 elementos y B tiene 15. La barra de abajo es la unión de los dos."],
 [4,10,"Con 5 elementos en común, la unión tiene 20 más 15 menos 5, o sea 30."],
 [10,15,"Si los conjuntos no comparten nada, la unión tiene 35 elementos."],
 [15,19,"Si comparten los 15, B queda dentro de A y la unión es solo A, con 20 elementos."],
 [19,22,"La fórmula resta lo común, porque se contó dos veces."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,5],[9,5],[10,0],[14,0],[15,15],[19,15],[22,15]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,22]}}
S=[
 sec("La idea",None,P("Para contar los elementos de una {{gl:union|unión}} no basta sumar los tamaños, porque los elementos comunes se contarían dos veces. El principio de {{gl:inclusion|inclusión y exclusión}} corrige eso restando la intersección. También se cuentan las {{gl:diferencia|diferencias}} y el {{gl:potencia|conjunto potencia}}.")),
 sec("Un ejemplo","Un ejemplo",P("Se tienen un conjunto A de 20 elementos y un conjunto B de 15. Mueve la cantidad de elementos en común y mira la barra de la unión."),EQ("|A\\cup B|=|A|+|B|-|A\\cap B|"),{"t":"grafica","animar":"dibujar","alt":"Las barras de A, B y la unión"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Si A tiene 20 elementos, B tiene 15 y comparten 5, ¿cuántos elementos tiene la unión?","opciones":[25,30,35,40],"correcta":30,"bien":"Muy bien. Son 20 más 15 menos 5, o sea 30. Más abajo se ve en la barra.","mal":"Son 30. Sumar 20 y 15 da 35, pero los 5 comunes se contaron dos veces, así que se restan. Más abajo se ve en la barra."}),
 sec("Cambiando la intersección","La intersección",P("Mira la unión con 0, 5, 10 y 15 elementos en común."),{"t":"acercando","ds":[0,5,10,15],"alt":"La unión con cuatro valores de la intersección"},P("Cuanto más comparten, más pequeña es la unión. Con 15 en común, la unión es A.")),
 sec("Inclusión y exclusión","Fórmulas",P("La fórmula se extiende a tres conjuntos, alternando signos."),
   PASOS([("|A\\cup B|=|A|+|B|-|A\\cap B|","Dos conjuntos."),
          ("|A|=5,\\ |B|=7,\\ |A\\cap B|=2\\ \\Rightarrow\\ |A\\cup B|=10","Con los números del banco."),
          ("|A\\cup B\\cup C|=|A|+|B|+|C|-|A\\cap B|-|A\\cap C|-|B\\cap C|+|A\\cap B\\cap C|","Tres conjuntos."),
          ("|A^{c}|=|U|-|A|","El complemento se cuenta restando del universo.")])),
 sec("Diferencias y conjunto potencia","Más conteo",P("Otras cuentas de conjuntos que aparecen a menudo."),
   PASOS([("A\\setminus B=A\\cap B^{c}","La diferencia es lo que está en A y no está en B."),
          ("|A\\setminus B|=|A|-|A\\cap B|","Se cuenta quitando lo común."),
          ("|\\mathcal{P}(A)|=2^{|A|},\\quad |A|=4\\ \\Rightarrow\\ 16","El conjunto potencia tiene dos elevado a la cantidad de elementos.")]),
   OJO("En la fórmula de tres conjuntos, el último término se suma. Los signos alternan, y por eso la intersección triple vuelve a entrar con signo positivo.")),
 eng("Piezas con defectos de dos tipos","En un lote de 200 piezas, 20 tienen defecto de superficie y 15 tienen defecto dimensional. Se encontró que 5 piezas tienen los dos defectos. Para saber cuántas piezas deben revisarse no se suman 20 y 15.","|A\\cup B|=20+15-5=30",
   [("Con defecto de superficie","20"),("Con defecto dimensional","15"),("Con ambos defectos","5")],"Las piezas con al menos un defecto son 30, y las 170 restantes están libres de defectos. Si se hubieran sumado 20 y 15, se habrían descartado 35 piezas, y 5 de ellas se habrían contado dos veces. Con inclusión y exclusión se evita descartar de más, y se estima el costo real del control de calidad."),
 completar("Se completa la fórmula de inclusión y exclusión para tres conjuntos. Falta el último término.","|A\\cup B\\cup C|=\\ldots-|B\\cap C|+[[hueco]]",
   [("|A\\cap B\\cap C|","la intersección triple"),("|A\\cup B\\cup C|","la unión triple"),("0","cero")],0,
   ["","La unión es lo que se está calculando, y no entra en el lado derecho.","El término no vale cero en general, porque hay elementos que están en los tres conjuntos."],"La intersección triple vuelve a entrar con signo positivo.","Al restar las intersecciones de a pares se quitó de más lo que está en los tres, y se vuelve a sumar."),
 error("Alguien calculó la unión de dos conjuntos y se equivocó en un paso. Toca el paso que está mal.",
   [("|A|=5,\\ |B|=7,\\ |A\\cap B|=2","Los datos.","los tamaños son 5, 7 y 2"),
    ("|A\\cup B|=5+7+2","Este paso es el que falla.","se suman los tres"),
    ("|A\\cup B|=14","Resultado.","la unión tiene 14")],1,
   "Los 2 elementos comunes ya están dentro de los 5 y los 7, así que se restan para no contarlos dos veces. La cuenta correcta es 5 más 7 menos 2, o sea 10.",
   "|A\\cup B|=5+7-2=10","Recuerda qué se hace con la intersección."),
 ordenar("Estos son los pasos para probar que A menos B es igual a A intersección el complemento de B, pero están desordenados.",
   [("x\\in A\\setminus B","Se toma x en la diferencia"),
    ("x\\in A\\ \\wedge\\ x\\notin B","Por definición de diferencia"),
    ("x\\in A\\ \\wedge\\ x\\in B^{c}","No estar en B es estar en el complemento"),
    ("x\\in A\\cap B^{c}","Es la intersección")],[2,0,3,1],
   "Se parte de la definición de la diferencia y se reescribe cada condición con el complemento.","Se empieza tomando un elemento."),
]
S+=cierre("Mini simulacro de teoría de conjuntos e inclusión-exclusión",[
 banco("di_c2_01","$20+15-5=30$."),
 banco("di_c2_07","El conjunto potencia de un conjunto de 4 elementos tiene $2^4=16$ subconjuntos."),
 banco("di_c2_08","$A\\setminus B$ son los elementos de $A$ que no están en $B$, es decir, $A\\cap B^{c}$.")])
prac=[
 {"titulo":"Dos conjuntos","grafica":{"draw":1},"bloques":[P("A con 20 elementos y B con 15, y la barra de la unión."),EQ("|A\\cup B|=35-|A\\cap B|")]},
 {"titulo":"Mueve la intersección","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 15. Abajo se leen los elementos en común y el tamaño de la unión.")]},
 {"titulo":"Con 5 en común","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":5,"bloques":[EQ("20+15-5=30"),P("Con 5 elementos en común, la unión tiene 30.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Cuenta primero a cuántos estudian al menos un idioma."}]}]
preg={"tex":"\\text{Hay 40 estudiantes. 25 estudian inglés, 18 francés y 6 ambos. ¿Cuántos no estudian ninguno?}","opciones":["$3$","$9$","$12$","$15$"],"correcta":0,
 "explicacion":"Los que estudian al menos un idioma son 25 más 18 menos 6, o sea 37. Los que no estudian ninguno son 40 menos 37, o sea 3.",
 "verificacion":{"formula":"40-(25+18-6)+0*x","a":0,"esperado":3},
 "pistas":["Primero cuenta la unión de los dos grupos.","Son 25 más 18 menos 6, o sea 37.","Resta 37 de 40."],
 "errores":["","Nueve sale de restar solo 31, que es 25 más 6 sin considerar el francés.","Doce sale de olvidar el término que se resta.","Quince es 40 menos 25, que no usa los datos del francés."]}
res=["La unión de dos conjuntos tiene |A| más |B| menos |A intersección B| elementos.","Con tres conjuntos los signos alternan, y la intersección triple se suma.","A menos B es A intersección el complemento de B, y el conjunto potencia de n elementos tiene dos elevado a n."]
write(lesson("di-m2-l2","Lección 2 de 4","Teoría de conjuntos e inclusión-exclusión",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Discretas"),"disc-inclusion.json")
