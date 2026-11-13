import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 2 Demostración y conjuntos"
U=[1,2,3,4,5]; A={1,2,3}; B={2,3,4}
OPS=[A|B, A&B, A-B, A^B, set(U)-A]
W=1.2; H=1.1
def rect(xa,ya,xb,yb,c,txt=None):
    d={"t":"poligono","puntos":[[str(xa),str(ya)],[str(xb),str(ya)],[str(xb),str(yb)],[str(xa),str(yb)]],"c":c}
    if txt is not None: d["nombre"]=txt
    return d
EL=[]
for ri,(lab,S_) in enumerate([("n",None),("A",A),("B",B),("R",None)]):
    top=[4.4,3.3,2.2,1.1][ri]; bot=top-H
    if lab=="n": EL.append(rect(0,top,W,bot,0,""))
    else: EL.append(rect(0,top,W,bot,0,lab))
for j,n in enumerate(U):
    xa=W*(j+1); xb=xa+W
    EL.append(rect(xa,4.4,xb,3.3,0,str(n)))
    EL.append(rect(xa,3.3,xb,2.2,3 if n in A else 1,"V" if n in A else "F"))
    EL.append(rect(xa,2.2,xb,1.1,3 if n in B else 1,"V" if n in B else "F"))
    L=lagr([1 if n in o else 0 for o in OPS])
    EL.append({"t":"poligono","puntos":[[str(xa),"0"],[str(xb),"0"],[str(xb),f"1.1*({L})"],[str(xa),f"1.1*({L})"]],"c":3})
    EL.append({"t":"poligono","puntos":[[str(xa),f"1.1*({L})"],[str(xb),f"1.1*({L})"],[str(xb),"1.1"],[str(xa),"1.1"]],"c":1})
graf={"tipo":"plano","x":[-0.6,7.8],"y":[-0.1,4.5],"a":0,"b":4,"inicio":0,"entero":True,"sinejes":True,"elementos":EL,
 "lecturas":[{"rotulo":"operación (0 unión, 1 intersección, 2 diferencia, 3 simétrica, 4 complemento de A)","formula":"x"},{"rotulo":"elementos del resultado R","formula":lagr([len(o) for o in OPS])}],
 "etiquetas":["Número de la operación elegida","Cantidad de elementos del conjunto resultado"],"etiquetaSlider":"Operación, de 0 a 4",
 "alt":"Una tabla con el universo de 1 a 5. La fila A marca los elementos 1, 2 y 3 y la fila B marca 2, 3 y 4. La fila R muestra en verde los elementos del resultado de la operación elegida con el deslizador"}
glos={"union":"La unión reúne los elementos que están en A, en B o en ambos.",
 "interseccion":"La intersección reúne solo los elementos que están en A y en B a la vez.",
 "diferencia":"La diferencia A menos B tiene los elementos de A que no están en B.",
 "simetrica":"La diferencia simétrica reúne los elementos que están en uno de los conjuntos pero no en los dos.",
 "producto":"El producto cartesiano A por B es el conjunto de pares ordenados con el primer elemento en A y el segundo en B."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"El universo son los números del 1 al 5. La fila A marca el conjunto uno, dos y tres, y la fila B marca dos, tres y cuatro."],
 [4,9,"En la operación 0, la unión, el resultado tiene los elementos que están en A o en B, o sea, del 1 al 4."],
 [9,13,"La intersección, operación 1, deja solo los que están en los dos, que son el 2 y el 3."],
 [13,18,"La diferencia A menos B deja el 1, y la simétrica deja el 1 y el 4, los que están en un conjunto pero no en los dos."],
 [18,24,"El complemento de A, operación 4, son los elementos del universo que no están en A, es decir, el 4 y el 5."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[5,0],[6,0],[9,0],[10,1],[13,1],[14,2],[16,3],[17,3],[18,4],[24,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,24]}}
S=[
 sec("La idea",None,P("Los conjuntos se combinan con operaciones. La {{gl:union|unión}} junta, la {{gl:interseccion|intersección}} deja lo común, la {{gl:diferencia|diferencia}} quita y la {{gl:simetrica|diferencia simétrica}} deja lo que no es común. El complemento toma lo que queda fuera del conjunto, dentro de un universo. Y el {{gl:producto|producto cartesiano}} arma pares ordenados.")),
 sec("Un ejemplo","Un ejemplo",P("Con el universo del 1 al 5, el conjunto A de 1, 2 y 3, y el conjunto B de 2, 3 y 4, mueve el deslizador para ver cada operación."),EQ("A=\\{1,2,3\\},\\qquad B=\\{2,3,4\\}"),{"t":"grafica","animar":"dibujar","alt":"La tabla con los conjuntos A, B y el resultado"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"El conjunto A tiene 3 elementos, B también tiene 3 y comparten 2. ¿Cuántos elementos tiene la unión de A y B?","opciones":[3,4,5,6],"correcta":4,"bien":"Muy bien. Son 4, porque los 2 compartidos se cuentan una sola vez. Más abajo se ve en la tabla.","mal":"Son 4. Si se suman 3 y 3 se obtiene 6, pero los 2 elementos compartidos se contaron dos veces, así que hay que restarlos."}),
 sec("Recorriendo las operaciones","Las operaciones",P("Mira el resultado de cada operación."),{"t":"acercando","ds":[0,1,2,3],"alt":"El resultado de la unión, la intersección, la diferencia y la diferencia simétrica"},P("La fila R se pinta de verde en los elementos del resultado.")),
 sec("Las operaciones","Resumen",P("Estas son las operaciones con los conjuntos del ejemplo."),
   PASOS([("A\\cup B=\\{1,2,3,4\\}","Unión. Está en A, en B o en ambos."),
          ("A\\cap B=\\{2,3\\}","Intersección. Está en A y en B."),
          ("A-B=\\{1\\}","Diferencia. Está en A y no está en B."),
          ("A\\,\\triangle\\,B=(A-B)\\cup(B-A)=\\{1,4\\}","Diferencia simétrica. Está en uno solo de los dos."),
          ("A^{c}=\\{4,5\\}","Complemento de A en el universo del 1 al 5."),
          ("\\{a,b\\}\\times\\{1,2,3\\}\\ \\text{tiene}\\ 2\\cdot3=6\\ \\text{pares}","Producto cartesiano. Se multiplican las cantidades.")]),
   OJO("La diferencia no es conmutativa, porque A menos B no es B menos A. Y en un producto cartesiano el orden importa, así que el par a, 1 no es el par 1, a.")),
 sec("Cómo se cuenta","Contar",P("Para contar una unión no basta sumar, porque los elementos comunes se contarían dos veces."),
   PASOS([("|A\\cup B|=|A|+|B|-|A\\cap B|","Inclusión y exclusión. Se resta lo que se contó doble."),
          ("|A|=3,\\ |B|=3,\\ |A\\cap B|=2","Los datos del ejemplo."),
          ("|A\\cup B|=3+3-2=4","Resultado.")]),
   OJO("La fórmula se usa cuando se conocen las cantidades y no los elementos. Si los conjuntos no comparten elementos, la intersección vale cero y basta sumar.")),
 eng("Las alarmas de una planta","En una planta, 30 sensores tienen alarma de temperatura, 25 tienen alarma de presión y 10 tienen las dos. Para saber cuántos sensores tienen al menos una alarma no se suman 30 y 25, porque los 10 que tienen ambas se contarían dos veces.","|A\\cup B|=|A|+|B|-|A\\cap B|",
   [("Con alarma de temperatura","30"),("Con alarma de presión","25"),("Con las dos","10")],"Los sensores con al menos una alarma son 30 más 25 menos 10, que da 45. Esa cuenta evita pedir mantenimiento para sensores que no existen. Contar con inclusión y exclusión es útil siempre que dos criterios se superponen, como permisos, fallas o clientes que cumplen dos condiciones."),
 completar("Se cuenta la unión de dos conjuntos. Falta lo que se resta.","|A\\cup B|=|A|+|B|-[[hueco]]",
   [("|A\\cap B|","los elementos comunes"),("|A-B|","los que están solo en A"),("|A\\times B|","los pares ordenados")],0,
   ["","Los que están solo en A se cuentan una vez, y no hay que restarlos.","Los pares ordenados son otro conjunto, y no se relacionan con lo que se contó doble."],"Se resta lo que se contó dos veces.","Los elementos comunes se contaron en A y en B, por eso se restan una vez."),
 error("Alguien calculó la diferencia simétrica de dos conjuntos y se equivocó en un paso. Toca el paso que está mal.",
   [("A=\\{1,2,3\\},\\ B=\\{3,4\\}","Los conjuntos.","los conjuntos son estos"),
    ("A\\,\\triangle\\,B=(A-B)\\cup(B-A)","La definición.","se usa la definición"),
    ("\\text{Entonces}\\ A\\,\\triangle\\,B=\\{1,2,3,4\\}","Este paso es el que falla.","queda toda la unión")],2,
   "El 3 está en los dos conjuntos, así que no entra en la diferencia simétrica. A menos B es 1 y 2, B menos A es 4, y la unión es 1, 2 y 4.",
   "A\\,\\triangle\\,B=\\{1,2,4\\}","Calcula A menos B y B menos A por separado."),
 ordenar("Estos son los pasos para contar la unión de dos conjuntos, pero están desordenados.",
   [("|A|=3,\\ |B|=3","Se cuentan los dos conjuntos"),
    ("|A\\cap B|=2","Se cuenta lo que comparten"),
    ("3+3-2","Se aplica la inclusión y exclusión"),
    ("|A\\cup B|=4","Se escribe el resultado")],[2,0,3,1],
   "Se cuentan los dos conjuntos, se cuenta lo común y se resta.","Se empieza contando cada conjunto."),
]
S+=cierre("Mini simulacro de operaciones con conjuntos",[
 banco("fu_c2_10","La intersección deja los elementos que están en los dos conjuntos."),
 banco("fu_c2_11","La diferencia simétrica deja lo que está en uno solo de los dos conjuntos."),
 banco("fu_c2_14","El producto cartesiano tiene 2 por 3, es decir, 6 pares.")])
prac=[
 {"titulo":"Los conjuntos","grafica":{"draw":1,"guide":1},"bloques":[P("El universo del 1 al 5, con A de 1, 2 y 3, y B de 2, 3 y 4."),EQ("A=\\{1,2,3\\},\\ B=\\{2,3,4\\}")]},
 {"titulo":"Recorre las operaciones","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 4. Abajo se lee la operación elegida y cuántos elementos tiene el resultado.")]},
 {"titulo":"La intersección","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("A\\cap B=\\{2,3\\}"),P("Con la operación 1, la fila R tiene verdes solo el 2 y el 3.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"A menos B deja lo que está en A y no está en B."}]}]
preg={"tex":"\\text{Si}\\ A=\\{1,2,3\\}\\ \\text{y}\\ B=\\{2,3,4\\},\\ \\text{entonces}\\ A-B\\ \\text{es}","opciones":["$\\{1\\}$","$\\{4\\}$","$\\{2,3\\}$","$\\{1,4\\}$"],"correcta":0,
 "explicacion":"A menos B son los elementos de A que no están en B. El 2 y el 3 sí están en B, así que solo queda el 1.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Mira los elementos de A.","Quita los que están en B.","Queda el 1."],
 "errores":["","El 4 está en B y no en A, así que sería B menos A.","Esa es la intersección, los elementos comunes.","Esa es la diferencia simétrica, que une las dos diferencias."]}
res=["La unión junta, la intersección deja lo común, la diferencia quita y la simétrica deja lo que no es común.","Para contar una unión se usa |A| más |B| menos |A intersección B|.","El producto cartesiano tiene tantos pares como el producto de las cantidades, y el orden de cada par importa."]
write(lesson("fu-m2-l4","Lección 4 de 4","Operaciones con conjuntos",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-operaciones.json")
