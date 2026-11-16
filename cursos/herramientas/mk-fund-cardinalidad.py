import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 3 Relaciones y funciones"
INY=[1,3,6,6,0]
EL=[{"t":"trazo","puntos":[[str(m/4),f"exp({m/4}*ln(3))"] for m in range(0,17)],"c":0},
 {"t":"trazo","puntos":[[str(m),str(v)] for m,v in enumerate(INY)],"c":1},
 {"t":"segmento","a":["x","0"],"b":["x","exp(x*ln(3))"],"c":1,"guia":True,"guion":True},
 {"t":"punto","p":["x","exp(x*ln(3))"],"c":2},
 {"t":"punto","p":["x",lagr(INY)],"c":3}]
graf={"tipo":"plano","x":[-0.6,4.6],"y":[-9,92],"a":0,"b":4,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"funciones de A en B, con B de 3 elementos","formula":"exp(x*ln(3))"},{"rotulo":"funciones inyectivas de A en B","formula":lagr(INY)}],
 "etiquetas":["Todas las funciones, tres elevado a m","Solo las inyectivas, que desaparecen cuando m pasa de 3"],"etiquetaSlider":"Elementos de A, m, de 0 a 4",
 "alt":"La curva de tres elevado a m, que cuenta las funciones de un conjunto de m elementos en uno de 3 elementos, y una línea más baja con las funciones inyectivas. Las inyectivas valen 1, 3, 6, 6 y luego 0 cuando m supera 3"}
glos={"cardinalidad":"La cardinalidad de un conjunto es su tamaño. Dos conjuntos tienen la misma cardinalidad si existe una biyección entre ellos.",
 "numerable":"Un conjunto es numerable si se puede poner en lista, es decir, si hay una biyección con los naturales. Los enteros y los racionales son numerables.",
 "principio":"El principio de multiplicación dice que si una tarea se hace en pasos independientes con a, b, c opciones, hay a por b por c formas de hacerla.",
 "permutacion":"Una permutación de n elementos es una forma de ordenarlos. Hay n factorial."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"El conjunto A tiene m elementos y B tiene 3. La curva alta cuenta las funciones de A en B, que son 3 elevado a m."],
 [4,9,"Con m igual a 1 hay 3 funciones. Con m igual a 2, cada uno de los dos elementos tiene 3 opciones, y son 9."],
 [9,14,"Las funciones inyectivas son menos. Con m igual a 2 son 3 por 2, o sea 6."],
 [14,19,"Con m igual a 3 hay 6 inyectivas, que son las biyecciones. Con m igual a 4 ya no hay ninguna, porque no caben 4 elementos en 3 sin repetir."],
 [19,24,"Contar funciones se reduce a contar las opciones de cada elemento y multiplicarlas."]],
 "canales":{"draw":[[0.3,0],[4.5,1]],"d":[[4,0],[5,1],[8,1],[9,2],[13,2],[14,3],[16,3],[17,4],[19,4],[24,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[19,24]}}
S=[
 sec("La idea",None,P("Contar es decidir cuántos elementos tiene un conjunto. La {{gl:cardinalidad|cardinalidad}} dice que dos conjuntos tienen el mismo tamaño si se pueden emparejar uno a uno, o sea, si hay una biyección. Para los conjuntos infinitos esto da sorpresas, porque hay conjuntos {{gl:numerable|numerables}}. Para los finitos se usa el {{gl:principio|principio de multiplicación}} para contar funciones.")),
 sec("Un ejemplo","Un ejemplo",P("Se cuentan las funciones de un conjunto A de m elementos en uno de 3 elementos. Mira qué pasa con todas las funciones y con las inyectivas."),EQ("\\#\\{f:A\\to B\\}=|B|^{|A|}=3^{m}"),{"t":"grafica","animar":"dibujar","alt":"La curva de 3 elevado a m y las funciones inyectivas"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Un conjunto A tiene 2 elementos y B tiene 3. Cada elemento de A elige una imagen en B. ¿Cuántas funciones hay?","opciones":[5,6,8,9],"correcta":9,"bien":"Muy bien. Son 3 opciones para cada uno de los 2 elementos, o sea 3 por 3. Más abajo se ve la curva completa.","mal":"Son 9, porque cada uno de los 2 elementos tiene 3 opciones, y 3 por 3 es 9. Más abajo se ve la curva completa."}),
 sec("Recorriendo los valores de m","Valores de m",P("Mira el total de funciones y las inyectivas con m igual a 1, 2, 3 y 4."),{"t":"acercando","ds":[1,2,3,4],"alt":"Funciones totales e inyectivas para cuatro valores de m"},P("Con m igual a 3 las inyectivas son 6, y con m igual a 4 desaparecen.")),
 sec("Cómo se cuentan","Cómo se cuentan",P("Cada elemento del dominio elige su imagen, y las opciones se multiplican."),
   PASOS([("|B|^{|A|}","Todas las funciones. Cada elemento de A tiene |B| opciones."),
          ("|B|\\cdot(|B|-1)\\cdots(|B|-|A|+1)","Las inyectivas. Cada elección no puede repetir las anteriores."),
          ("n!","Las biyecciones entre dos conjuntos de n elementos."),
          ("f\\ \\text{biyectiva}\\Rightarrow|A|=|B|","Una biyección empareja uno a uno, así que los tamaños coinciden.")]),
   OJO("Las funciones se cuentan por lo que elige cada elemento del dominio, y no por lo que recibe cada elemento del codominio. Con 2 elementos y 3 imágenes son 3 al cuadrado, y no 2 al cubo.")),
 sec("Conjuntos infinitos","Infinitos",P("Dos conjuntos infinitos pueden tener la misma cardinalidad aunque uno contenga al otro."),
   PASOS([("0,\\ 1,\\ -1,\\ 2,\\ -2,\\ 3,\\ -3,\\ \\ldots","Los enteros se pueden poner en lista alternando los signos."),
          ("|\\mathbb{N}|=|\\mathbb{Z}|","Hay una biyección, así que son numerables los dos."),
          ("|\\mathbb{N}|<|\\mathbb{R}|","Los reales son más. No se pueden poner en lista, como mostró Cantor.")]),
   OJO("Con los conjuntos infinitos, ser subconjunto propio no significa tener menos elementos. Los naturales están contenidos en los enteros y tienen la misma cardinalidad.")),
 eng("Los códigos de acceso","Un código de 4 dígitos puede formarse con repetición o sin repetición. Con repetición, cada una de las 4 posiciones tiene 10 opciones. Sin repetir dígitos, cada posición tiene una opción menos que la anterior.","10^{4}\\quad\\text{y}\\quad 10\\cdot9\\cdot8\\cdot7",
   [("Con repetición","10 000 códigos"),("Sin repetir","5040 códigos"),("Códigos que se pierden","casi la mitad")],"Si un sistema exige no repetir dígitos, el espacio de códigos baja de 10 000 a 5040, y quien intente adivinar tiene cerca de la mitad de las opciones que había. Contar las funciones del dominio al codominio, con repetición o inyectivas, permite estimar de qué tamaño es un espacio de búsqueda."),
 completar("Se cuentan las funciones de un conjunto A de 2 elementos en un conjunto B de 3 elementos.","\\#\\text{funciones}=[[hueco]]",
   [("3^{2}","tres elevado a dos"),("2^{3}","dos elevado a tres"),("2\\cdot3","dos por tres")],0,
   ["","Dos al cubo sería lo que sale si B tuviera 2 elementos y A tuviera 3. Aquí cada elemento de A elige entre 3.","Dos por tres contaría pares ordenados, pero las funciones se cuentan con una elección por elemento del dominio."],"Cada elemento de A elige una imagen entre las de B.","Los 2 elementos de A tienen 3 opciones cada uno, así que son 3 por 3."),
 error("Alguien contó las funciones inyectivas del conjunto 1, 2 al conjunto a, b, c y se equivocó en un paso. Toca el paso que está mal.",
   [("f(1)\\ \\text{tiene 3 opciones}","Se elige la imagen del 1.","tres opciones para el 1"),
    ("f(2)\\ \\text{tiene 3 opciones}","Este paso es el que falla.","tres opciones para el 2"),
    ("\\text{Total}\\ 3\\cdot3=9","Se multiplican.","en total 9")],1,
   "Si f es inyectiva, f de 2 no puede repetir el valor de f de 1, así que quedan 2 opciones. El total es 3 por 2, que da 6.",
   "3\\cdot2=6","Piensa qué no puede elegir f de 2."),
 ordenar("Estos son los pasos para probar que los naturales y los enteros tienen la misma cardinalidad, pero están desordenados.",
   [("0,\\ 1,\\ -1,\\ 2,\\ -2,\\ \\ldots","Se enumeran los enteros alternando signos"),
    ("f(0)=0,\\ f(1)=1,\\ f(2)=-1,\\ \\ldots","Se define la asignación de los naturales a esa lista"),
    ("f\\ \\text{es inyectiva y sobreyectiva}","Se ve que es una biyección"),
    ("|\\mathbb{N}|=|\\mathbb{Z}|","Se concluye que tienen la misma cardinalidad")],[2,0,3,1],
   "Se enumeran los enteros, se define la biyección y se concluye.","Se empieza armando la lista."),
]
S+=cierre("Mini simulacro de cardinalidad y conteo",[
 banco("fu_c3_13","Una biyección empareja uno a uno, así que los dos conjuntos tienen el mismo tamaño."),
 banco("fu_c3_19","Cada uno de los 2 elementos tiene 3 imágenes posibles, así que son 3 al cuadrado."),
 banco("fu_c3_20","Hay 3 opciones para la imagen del 1 y 2 para la del 2.")])
prac=[
 {"titulo":"Las funciones","grafica":{"draw":1,"guide":1},"bloques":[P("Las funciones de un conjunto de m elementos en uno de 3 elementos."),EQ("3^{m}")]},
 {"titulo":"Recorre m","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 4. Abajo se lee el total de funciones y cuántas son inyectivas.")]},
 {"titulo":"Con m igual a 3","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("3^{3}=27,\\qquad 3\\cdot2\\cdot1=6"),P("Con m igual a 3 hay 27 funciones y 6 son inyectivas, que además son biyectivas.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Cada elemento del dominio elige su imagen, y en las inyectivas no se repiten."}]}]
preg={"tex":"\\text{Funciones inyectivas de}\\ \\{1,2,3\\}\\ \\text{a}\\ \\{a,b,c,d\\}","opciones":["$24$","$64$","$12$","$81$"],"correcta":0,
 "explicacion":"El 1 tiene 4 opciones, el 2 tiene 3 porque no puede repetir y el 3 tiene 2, así que son 4 por 3 por 2, que da 24.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Cada elemento elige sin repetir.","El primero tiene 4 opciones.","Son 4 por 3 por 2."],
 "errores":["","Esas son 4 por 4 por 4, que cuentan todas las funciones y no solo las inyectivas.","Eso son 4 por 3, que se olvida del tercer elemento.","Eso es 3 elevado a 4, que invierte el papel del dominio y el codominio."]}
res=["Dos conjuntos tienen la misma cardinalidad si hay una biyección entre ellos.","Las funciones de A en B son |B| elevado a |A|, y las inyectivas se cuentan sin repetir imágenes.","Los naturales y los enteros son numerables y tienen la misma cardinalidad, aunque los naturales estén contenidos en los enteros."]
write(lesson("fu-m3-l4","Lección 4 de 5","Cardinalidad y conteo",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-cardinalidad.json")
