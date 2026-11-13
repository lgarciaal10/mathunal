import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 2 Demostración y conjuntos"
EL=[{"t":"trazo","puntos":[[str(n/4),f"exp({n/4}*ln(2))"] for n in range(0,25)],"c":0},
 {"t":"segmento","a":["x","0"],"b":["x","exp(x*ln(2))"],"c":1,"guia":True,"guion":True},
 {"t":"punto","p":["x","exp(x*ln(2))"],"c":2}]
graf={"tipo":"plano","x":[-1,7],"y":[-8,72],"a":0,"b":6,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"subconjuntos de un conjunto con n elementos","formula":"exp(x*ln(2))"},{"rotulo":"subconjuntos con exactamente 2 elementos","formula":"x*(x-1)/2"}],
 "etiquetas":["Tamaño del conjunto potencia, dos elevado a n","Cantidad de subconjuntos de 2 elementos, n por n menos 1 entre 2"],"etiquetaSlider":"Número de elementos n, de 0 a 6",
 "alt":"La curva de dos elevado a n para n de 0 a 6. Cada elemento nuevo duplica la cantidad de subconjuntos. Con 6 elementos hay 64 subconjuntos"}
glos={"subconjunto":"A es subconjunto de B si todo elemento de A está en B. El conjunto vacío y el propio conjunto son siempre subconjuntos.",
 "potencia":"El conjunto potencia de A es el conjunto formado por todos los subconjuntos de A. Si A tiene n elementos, el conjunto potencia tiene dos elevado a n.",
 "complemento":"El complemento de A son los elementos del universo que no están en A.",
 "demorgan":"Las leyes de De Morgan dicen que el complemento de una unión es la intersección de los complementos, y el complemento de una intersección es la unión de los complementos."}
ver={"duracion":24.0,"capitulos":[
 [0,5,"El conjunto potencia de A reúne todos sus subconjuntos. La curva muestra cuántos son, según el número de elementos n."],
 [5,10,"Con 0 elementos hay un solo subconjunto, el vacío. Con 1 elemento hay 2, y con 2 elementos hay 4."],
 [10,16,"Cada elemento nuevo duplica la cantidad, porque puede estar o no estar en cada subconjunto. Con 6 elementos son 64."],
 [16,20,"La segunda lectura cuenta los subconjuntos de exactamente 2 elementos. Con 4 elementos son 6."],
 [20,24,"El conjunto potencia crece muy rápido. Por eso con pocos elementos ya hay muchísimos subconjuntos."]],
 "canales":{"draw":[[0.3,0],[4.5,1]],"d":[[5,0],[6,0],[7,1],[8,2],[10,2],[12,4],[14,6],[16,6],[17,4],[20,4],[24,4]],"guide":[[5,0],[6,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Un {{gl:subconjunto|subconjunto}} de A usa algunos de los elementos de A, o ninguno, o todos. El {{gl:potencia|conjunto potencia}} reúne todos esos subconjuntos. Para armar uno, cada elemento tiene dos opciones, estar o no estar, así que con n elementos hay 2 por 2, n veces, es decir, dos elevado a n subconjuntos.")),
 sec("Un ejemplo","Un ejemplo",P("Mira cómo crece la cantidad de subconjuntos cuando el conjunto tiene más elementos."),EQ("\\left|\\mathcal{P}(A)\\right|=2^{\\,|A|}"),{"t":"grafica","animar":"dibujar","alt":"La curva de dos elevado a n"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Un conjunto tiene 3 elementos. Para armar un subconjunto, cada elemento puede estar o no estar. ¿Cuántos subconjuntos hay?","opciones":[3,6,8,9],"correcta":8,"bien":"Muy bien. Son 2 por 2 por 2, que es 8. Más abajo se ve la curva completa.","mal":"Son 8, porque cada uno de los 3 elementos tiene 2 opciones, y 2 por 2 por 2 es 8. Más abajo se ve la curva completa."}),
 sec("Recorriendo los valores de n","Valores de n",P("Mira cuántos subconjuntos hay con 0, 2, 4 y 6 elementos."),{"t":"acercando","ds":[0,2,4,6],"alt":"La cantidad de subconjuntos para cuatro valores de n"},P("Con 0 elementos hay uno, el vacío. Cada elemento nuevo duplica la cantidad.")),
 sec("Los subconjuntos de tres elementos","Un caso",P("Para A con tres elementos se pueden escribir los 8 subconjuntos, y es la mejor forma de ver el patrón."),
   PASOS([("A=\\{a,b,c\\}","Un conjunto de 3 elementos."),
          ("\\emptyset","El subconjunto sin elementos, que siempre aparece."),
          ("\\{a\\},\\ \\{b\\},\\ \\{c\\}","Los de un elemento, que son 3."),
          ("\\{a,b\\},\\ \\{a,c\\},\\ \\{b,c\\}","Los de dos elementos, que son 3."),
          ("\\{a,b,c\\}","El propio conjunto, que también cuenta.")]),
   OJO("El conjunto vacío y el propio conjunto siempre son subconjuntos. Y a es un elemento de A, mientras que el conjunto con solo a es un subconjunto de A. No son lo mismo.")),
 sec("Álgebra de conjuntos","Álgebra",P("Las operaciones entre conjuntos siguen leyes que se usan para simplificar."),
   PASOS([("(A\\cup B)^{c}=A^{c}\\cap B^{c}","Primera ley de De Morgan."),
          ("(A\\cap B)^{c}=A^{c}\\cup B^{c}","Segunda ley de De Morgan."),
          ("A-(B\\cup C)=(A-B)\\cap(A-C)","Una diferencia con una unión se reparte como una intersección."),
          ("A\\subseteq B\\ \\Leftrightarrow\\ A\\cap B=A","Contenerse equivale a que la intersección deje a A completo.")]),
   OJO("Para probar que dos conjuntos son iguales se prueban las dos contenciones, o se razona elemento por elemento con equivalencias.")),
 eng("Las configuraciones de un sistema","Un equipo tiene 10 interruptores que pueden estar encendidos o apagados. Cada configuración es un subconjunto de los interruptores, el de los que están encendidos. Por eso hay dos elevado a 10 configuraciones posibles.","2^{n}",
   [("Interruptores","10"),("Configuraciones","1024"),("Con 20 interruptores","más de un millón")],"Probar todas las configuraciones es posible con 10 interruptores, pero con 20 ya son más de un millón y con 30 son más de mil millones. Por eso en ingeniería no se prueba todo, sino que se escoge un conjunto representativo de pruebas. Entender el crecimiento de dos elevado a n permite decidir cuándo una prueba exhaustiva sigue siendo realista."),
 completar("Se cuenta el conjunto potencia de un conjunto A.","\\left|\\mathcal{P}(A)\\right|=[[hueco]]",
   [("2^{|A|}","dos elevado a la cantidad de elementos"),("2|A|","el doble de la cantidad"),("|A|^{2}","el cuadrado de la cantidad")],0,
   ["","El doble sería lo que pasa si se agregan dos opciones, pero cada elemento nuevo duplica la cantidad total.","El cuadrado crece más despacio que la duplicación a medida que aumenta n."],"Cada elemento nuevo duplica la cantidad.","Cada elemento tiene dos opciones, así que se multiplica por 2 tantas veces como elementos haya."),
 error("Alguien escribió el conjunto potencia de A con dos elementos y se equivocó en un paso. Toca el paso que está mal.",
   [("A=\\{a,b\\}","Un conjunto de 2 elementos.","A tiene dos elementos"),
    ("\\mathcal{P}(A)=\\{\\{a\\},\\{b\\},\\{a,b\\}\\}","Se escriben los subconjuntos. Este paso es el que falla.","se escriben los subconjuntos"),
    ("\\text{Entonces}\\ |\\mathcal{P}(A)|=3","Se cuentan.","hay 3 subconjuntos")],1,
   "Falta el conjunto vacío, que siempre es subconjunto. Con el vacío son 4, que es 2 al cuadrado.",
   "\\mathcal{P}(A)=\\{\\emptyset,\\{a\\},\\{b\\},\\{a,b\\}\\}","Cuenta cuántos debería haber con dos elevado a 2."),
 ordenar("Estos son los pasos para probar que el complemento de la unión es la intersección de los complementos, pero están desordenados.",
   [("x\\in(A\\cup B)^{c}","Se toma un elemento x del complemento de la unión"),
    ("x\\notin A\\cup B","Eso significa que no está en la unión"),
    ("x\\notin A\\ \\wedge\\ x\\notin B","No está en A ni en B"),
    ("x\\in A^{c}\\cap B^{c}","Está en los dos complementos")],[2,0,3,1],
   "Se pasa de estar en el complemento a no estar en la unión, luego a no estar en ninguno y finalmente a la intersección.","Se empieza tomando un elemento."),
]
S+=cierre("Mini simulacro de álgebra de conjuntos y conjunto potencia",[
 banco("fu_c2_15","Por De Morgan, el complemento de la unión es la intersección de los complementos."),
 banco("fu_c2_16","El conjunto potencia de un conjunto con 5 elementos tiene 2 elevado a 5."),
 banco("fu_c2_18","Se cuentan los subconjuntos de 2 elementos entre 4, que son 4 sobre 2 igual a 6.")])
prac=[
 {"titulo":"El conjunto potencia","grafica":{"draw":1,"guide":1},"bloques":[P("La cantidad de subconjuntos de un conjunto con n elementos."),EQ("2^{n}")]},
 {"titulo":"Recorre n","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 6. Abajo se lee el tamaño del conjunto potencia y los subconjuntos de 2 elementos.")]},
 {"titulo":"Con 4 elementos","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":4,"bloques":[EQ("2^{4}=16,\\qquad \\dbinom{4}{2}=6"),P("Con 4 elementos hay 16 subconjuntos, y 6 de ellos tienen exactamente 2 elementos.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":4},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Cada elemento puede estar o no estar en el subconjunto."}]}]
preg={"tex":"\\text{Si}\\ |A|=4,\\ \\text{el conjunto potencia de}\\ A\\ \\text{tiene}","opciones":["$16$ elementos","$8$ elementos","$4$ elementos","$24$ elementos"],"correcta":0,
 "explicacion":"Cada uno de los 4 elementos puede estar o no estar en un subconjunto, así que hay 2 por 2 por 2 por 2, que es 16 subconjuntos. Se incluyen el vacío y el propio conjunto.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Cada elemento tiene dos opciones.","Se multiplica 2 cuatro veces.","Son 16."],
 "errores":["","Ocho es lo que sale con 3 elementos, pero aquí son 4.","Cuatro es el número de elementos, y no la cantidad de subconjuntos.","Veinticuatro sale de multiplicar 1 por 2 por 3 por 4, pero eso no cuenta subconjuntos."]}
res=["El conjunto potencia reúne todos los subconjuntos, incluidos el vacío y el propio conjunto.","Con n elementos hay dos elevado a n subconjuntos, porque cada elemento puede estar o no estar.","Las leyes de De Morgan convierten el complemento de una unión en una intersección, y el de una intersección en una unión."]
write(lesson("fu-m2-l2","Lección 2 de 4","Álgebra de conjuntos y conjunto potencia",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-conjuntos.json")
