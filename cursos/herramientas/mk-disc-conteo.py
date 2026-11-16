import os, math
os.environ['CURSO_FU']='Matemáticas Discretas'; os.environ['BANCO']='discretas'
from mklib import *
from fundlib import *
MOD="Módulo 2 Conjuntos, conteo y combinatoria"
EL=[]
for j in range(5):
    vals=[(N+4-j)//5 for N in range(12)]
    L=lagr(vals)
    EL.append({"t":"poligono","puntos":[[str(j+0.1),"0"],[str(j+0.9),"0"],[str(j+0.9),"1"],[str(j+0.1),"1"]],"c":0})
    EL.append({"t":"poligono","puntos":[[str(j+0.1),"0"],[str(j+0.9),"0"],[str(j+0.9),L],[str(j+0.1),L]],"c":3})
mx=[-(-N//5) for N in range(12)]
graf={"tipo":"plano","x":[-0.6,5.6],"y":[-0.7,3.4],"a":0,"b":11,"inicio":6,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"objetos repartidos en las 5 cajas","formula":"x"},{"rotulo":"mínimo posible del máximo en una caja","formula":lagr(mx)}],
 "etiquetas":["Cantidad total de objetos","Alguna caja tiene al menos esta cantidad"],"etiquetaSlider":"Objetos, de 0 a 11",
 "alt":"Cinco cajas, cada una con una altura que indica sus objetos. Se reparten de a uno, en orden. Con 5 objetos cada caja tiene uno, y con 6 objetos alguna caja tiene al menos 2"}
glos={"suma":"La regla de la suma dice que si una tarea se puede hacer de a formas o de b formas, sin que se superpongan, hay a más b formas en total.",
 "producto":"La regla del producto dice que si una tarea tiene pasos con a, b y c opciones, hay a por b por c formas de hacerla.",
 "palomar":"El principio del palomar dice que si se colocan n más 1 objetos en n cajas, alguna caja tiene al menos 2 objetos.",
 "cadena":"Una cadena binaria de longitud n es una lista de n ceros y unos. Hay 2 elevado a n."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Hay 5 cajas y se reparten objetos de a uno, en orden."],
 [4,9,"Con 5 objetos, cada caja puede tener uno. Es posible que ninguna tenga dos."],
 [9,14,"Con 6 objetos, alguna caja debe tener al menos 2. Eso es el principio del palomar."],
 [14,19,"Con 11 objetos, alguna caja tiene al menos 3."],
 [19,22,"Con n más 1 objetos en n cajas, siempre hay una caja con al menos 2."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[7,5],[9,5],[10,6],[14,6],[15,11],[19,11],[22,11]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[9,22]}}
S=[
 sec("La idea",None,P("Contar sin listar se basa en pocas reglas. La {{gl:suma|regla de la suma}} junta casos que no se superponen, y la {{gl:producto|regla del producto}} multiplica las opciones de cada paso. Con ellas se cuentan las {{gl:cadena|cadenas binarias}} y las funciones entre conjuntos. Y el {{gl:palomar|principio del palomar}} afirma que, con más objetos que cajas, alguna caja se repite.")),
 sec("Un ejemplo","Un ejemplo",P("Se reparten objetos de a uno en 5 cajas. Mueve la cantidad de objetos y mira cuándo una caja tiene que tener dos."),EQ("n+1\\ \\text{objetos en}\\ n\\ \\text{cajas}\\ \\Rightarrow\\ \\text{alguna caja tiene}\\ \\ge2"),{"t":"grafica","animar":"dibujar","alt":"Cinco cajas con objetos"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Hay 5 cajas y se reparten 6 objetos. ¿Cuál es el menor número de objetos que tiene la caja más llena?","opciones":[1,2,3,6],"correcta":2,"bien":"Muy bien. Es 2, porque no caben 6 objetos en 5 cajas con uno cada una. Más abajo se ve.","mal":"Es 2. Con 5 objetos se llenaría una por caja, pero el sexto obliga a que alguna tenga dos. Más abajo se ve."}),
 sec("Recorriendo los objetos","Los objetos",P("Mira las cajas con 0, 5, 6 y 11 objetos."),{"t":"acercando","ds":[0,5,6,11],"alt":"Las cajas con cuatro cantidades de objetos"},P("Con 6 objetos aparece la primera caja con 2. Con 11 aparece una con 3.")),
 sec("Las reglas de conteo","Reglas",P("Con dos reglas se cuentan muchas situaciones."),
   PASOS([("a+b","Regla de la suma. Si se escoge una opción o la otra, se suman."),
          ("a\\cdot b\\cdot c","Regla del producto. Si se hacen pasos seguidos, se multiplican."),
          ("2^{5}=32","Cadenas binarias de longitud 5, con 2 opciones por posición."),
          ("4^{3}=64","Funciones de un conjunto de 3 elementos en uno de 4. Cada elemento elige entre 4.")]),
   OJO("Se suma cuando hay que escoger entre alternativas, y se multiplica cuando se hacen pasos seguidos. Confundirlas es el error más común al contar.")),
 sec("El principio del palomar","Palomar",P("Es sencillo, pero demuestra cosas que no parecen obvias."),
   PASOS([("n+1\\ \\text{objetos en}\\ n\\ \\text{cajas}\\ \\Rightarrow\\ \\text{alguna caja tiene}\\ \\ge2","La forma básica."),
          ("m\\ \\text{objetos en}\\ n\\ \\text{cajas}\\ \\Rightarrow\\ \\text{alguna caja tiene}\\ \\ge\\lceil m/n\\rceil","La forma general."),
          ("30\\ \\text{personas, 12 meses}\\ \\Rightarrow\\ \\ge\\lceil 30/12\\rceil=3","Siempre hay un mes con al menos 3 cumpleaños.")]),
   OJO("El principio afirma que existe una caja con al menos esa cantidad, pero no dice cuál es. Sirve para probar que algo existe, y no para encontrarlo.")),
 eng("Los códigos de 8 bits","Un código de 8 bits es una cadena binaria de longitud 8, así que hay dos elevado a 8 códigos distintos. Si hay más mensajes que códigos, el principio del palomar obliga a que dos mensajes distintos compartan código.","2^{8}=256",
   [("Bits","8"),("Códigos posibles","256"),("Con 257 mensajes","dos comparten código")],"Es la razón por la que ninguna función hash puede ser inyectiva sobre un conjunto más grande que su salida. En sistemas reales las colisiones son inevitables, y lo que se diseña es la forma de manejarlas. Esta cuenta, de dos elevado a n, es la misma de los subconjuntos y de las cadenas binarias."),
 completar("Se cuentan las cadenas binarias de longitud 4. Falta el resultado.","2\\cdot2\\cdot2\\cdot2=[[hueco]]",
   [("16","dieciséis"),("8","ocho"),("4","cuatro")],0,
   ["","Ocho sale de multiplicar solo tres de las cuatro posiciones.","Cuatro es la longitud, y no la cantidad de cadenas."],"Se multiplican las opciones de las cuatro posiciones.","2 por 2 por 2 por 2 es 16."),
 error("Alguien contó las funciones de un conjunto de 3 elementos a uno de 4 y se equivocó en un paso. Toca el paso que está mal.",
   [("|A|=3,\\quad |B|=4","Los datos.","los tamaños son 3 y 4"),
    ("\\text{Cada elemento de}\\ A\\ \\text{elige una imagen en}\\ B","La idea de la cuenta.","cada elemento de A elige"),
    ("\\#=3^{4}=81","Este paso es el que falla.","son 3 elevado a 4")],2,
   "Cada uno de los 3 elementos del dominio tiene 4 opciones, así que el total es 4 por 4 por 4, o sea 4 al cubo, que es 64. La base es el tamaño del codominio.",
   "\\#=4^{3}=64","Fíjate en cuántas opciones tiene cada elemento."),
 ordenar("Estos son los pasos para contar las cadenas binarias de longitud 5, pero están desordenados.",
   [("5\\ \\text{posiciones}","Se cuentan las posiciones"),
    ("2\\ \\text{opciones en cada una}","Se cuentan las opciones de cada posición"),
    ("2\\cdot2\\cdot2\\cdot2\\cdot2","Se multiplican"),
    ("32","Se calcula")],[2,0,3,1],
   "Se cuentan las posiciones, las opciones de cada una, y se multiplica.","Se empieza contando las posiciones."),
]
S+=cierre("Mini simulacro de principios de conteo",[
 banco("di_c2_04","Hay 2 opciones en cada una de las 5 posiciones, o sea $2^5=32$."),
 banco("di_c2_10","Cada uno de los 3 elementos elige entre 4 imágenes, o sea $4^3=64$."),
 banco("di_c2_11","Con más objetos que cajas, alguna caja contiene al menos 2.")])
prac=[
 {"titulo":"Las cajas","grafica":{"draw":1},"bloques":[P("Cinco cajas y objetos repartidos de a uno."),EQ("\\lceil m/5\\rceil")]},
 {"titulo":"Reparte objetos","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 11. Abajo se leen la cantidad de objetos y el mínimo posible de la caja más llena.")]},
 {"titulo":"Con 6 objetos","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":6,"bloques":[EQ("\\lceil 6/5\\rceil=2"),P("Con 6 objetos, alguna caja tiene al menos 2.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":6},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Divide los objetos entre las cajas y redondea hacia arriba."}]}]
preg={"tex":"\\text{En una clase de 30 estudiantes, ¿cuántos cumplen años en el mismo mes, como mínimo?}","opciones":["$3$","$2$","$1$","$12$"],"correcta":0,
 "explicacion":"Hay 12 meses y 30 estudiantes. El principio del palomar da al menos el redondeo hacia arriba de 30 entre 12, o sea 3 estudiantes, en algún mes.",
 "verificacion":{"formula":"3+0*x","a":0,"esperado":3},
 "pistas":["Hay 12 cajas, los meses.","Divide 30 entre 12.","Redondea hacia arriba, y queda 3."],
 "errores":["","Dos es el redondeo hacia abajo, y el principio pide hacia arriba.","Uno es lo que se obtiene con 12 estudiantes, y aquí hay 30.","Doce es el número de meses, y no la cantidad de estudiantes."]}
res=["La regla de la suma junta alternativas y la del producto multiplica pasos seguidos.","Hay 2 elevado a n cadenas binarias de longitud n, y B elevado a A funciones de A en B.","Con m objetos en n cajas, alguna caja tiene al menos m entre n, redondeado hacia arriba."]
write(lesson("di-m2-l4","Lección 4 de 4","Principios de conteo",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Discretas"),"disc-conteo.json")
