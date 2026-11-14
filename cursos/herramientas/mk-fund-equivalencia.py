import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 3 Relaciones y funciones"
W=1.4; H=1.1
def rect(xa,ya,xb,yb,c,txt=None):
    d={"t":"poligono","puntos":[[str(xa),str(ya)],[str(xb),str(ya)],[str(xb),str(yb)],[str(xa),str(yb)]],"c":c}
    if txt is not None: d["nombre"]=txt
    return d
EL=[]
for col in range(5):
    EL.append(rect(round(col*W,3),4.4,round((col+1)*W,3),3.3,0,"r"+str(col)))
for row in range(3):
    for col in range(5):
        n=5*row+col; top=round(3.3-row*H,3); bot=round(top-H,3)
        EL.append(rect(round(col*W,3),top,round((col+1)*W,3),bot,0,str(n)))
for row in range(3):
    for col in range(5):
        top=round(3.3-row*H,3); bot=round(top-H,3)
        ind=lagr([1 if r==col else 0 for r in range(5)])
        # resaltado de la clase elegida, translucido, se contrae a una linea cuando no esta elegida
        yb=f"{top}-{H}*({ind})"
        xa=round(col*W,3); xb=round((col+1)*W,3)
        EL.append({"t":"poligono","puntos":[[str(xa),str(top)],[str(xb),str(top)],[str(xb),yb],[str(xa),yb]],"c":3})
graf={"tipo":"plano","x":[-0.6,7.6],"y":[-0.15,4.5],"a":0,"b":4,"inicio":0,"entero":True,"sinejes":True,"elementos":EL,
 "lecturas":[{"rotulo":"residuo r de la clase elegida","formula":"x"},{"rotulo":"suma de los elementos de la clase entre 0 y 14","formula":"3*x+15"}],
 "etiquetas":["Residuo al dividir entre 5 de todos los elementos de la clase","Suma de los tres números de la columna elegida"],"etiquetaSlider":"Clase r, de 0 a 4",
 "alt":"Los enteros del 0 al 14 en tres filas de cinco. Cada columna reúne los números con el mismo residuo al dividir entre 5. El deslizador resalta una columna, que es una clase de equivalencia"}
glos={"equivalencia":"Una relación de equivalencia es reflexiva, simétrica y transitiva. Agrupa los elementos que se consideran iguales para un propósito.",
 "clase":"La clase de equivalencia de a reúne todos los elementos relacionados con a. Se escribe entre corchetes.",
 "particion":"Una partición de A es una familia de subconjuntos no vacíos, disjuntos, que cubren A.",
 "congruencia":"Dos enteros son congruentes módulo n si su diferencia es múltiplo de n. Es una relación de equivalencia."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Los enteros del 0 al 14 están en filas de 5. Cada columna reúne los números con el mismo residuo al dividir entre 5."],
 [4,9,"La columna 0 tiene el 0, el 5 y el 10. Están relacionados porque su diferencia es un múltiplo de 5."],
 [9,14,"Cambia de columna. Cada una es una clase de equivalencia. Los números de una columna se relacionan entre sí y con ninguno de otra columna."],
 [14,19,"Hay cinco columnas, o sea, cinco clases. Y cada entero está en una sola."],
 [19,24,"Eso es una partición del conjunto. Toda relación de equivalencia parte el conjunto en clases, y toda partición define una relación de equivalencia."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[5,0],[6,0],[9,1],[11,2],[13,3],[15,4],[19,4],[24,4]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[19,24]}}
S=[
 sec("La idea",None,P("Una {{gl:equivalencia|relación de equivalencia}} es una forma de decir que dos elementos son lo mismo para cierto propósito. Debe ser reflexiva, simétrica y transitiva. Cada elemento queda en su {{gl:clase|clase de equivalencia}}, que reúne a todos los que se relacionan con él, y las clases forman una {{gl:particion|partición}} del conjunto. Un ejemplo es la {{gl:congruencia|congruencia}} módulo n.")),
 sec("Un ejemplo","Un ejemplo",P("Dos enteros se relacionan si su diferencia es múltiplo de 5. Mira cómo se agrupan los números del 0 al 14."),EQ("x\\,R\\,y\\ \\iff\\ 5\\mid x-y"),{"t":"grafica","animar":"dibujar","alt":"Los enteros del 0 al 14 agrupados por residuo"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Al dividir un entero entre 5 queda un residuo. ¿Cuántos residuos distintos son posibles?","opciones":[3,4,5,6],"correcta":5,"bien":"Muy bien. Son 5, del 0 al 4. Más abajo se ve cada residuo como una columna.","mal":"Son 5, los residuos 0, 1, 2, 3 y 4. Más abajo se ve cada residuo como una columna."}),
 sec("Recorriendo las clases","Las clases",P("Mira la columna resaltada para las clases 0, 1, 2 y 4."),{"t":"acercando","ds":[0,1,2,4],"alt":"Cuatro clases resaltadas"},P("Cada columna es una clase. Los números de la misma columna tienen el mismo residuo.")),
 sec("Las tres propiedades","Propiedades",P("Para comprobar que una relación es de equivalencia se verifican tres propiedades. Se muestran con la relación x menos y es par."),
   PASOS([("x-x=0\\ \\text{es par}","Reflexiva. Todo elemento se relaciona consigo mismo."),
          ("x-y\\ \\text{par}\\Rightarrow y-x=-(x-y)\\ \\text{par}","Simétrica. Si a se relaciona con b, entonces b se relaciona con a."),
          ("x-y\\ \\text{y}\\ y-z\\ \\text{pares}\\Rightarrow x-z=(x-y)+(y-z)\\ \\text{par}","Transitiva. Si a se relaciona con b y b con c, entonces a con c.")]),
   OJO("Las tres propiedades son independientes. La relación menor o igual es reflexiva y transitiva, pero no es simétrica, así que no es de equivalencia.")),
 sec("Clases y particiones","Particiones",P("Las clases de una relación de equivalencia nunca se mezclan ni se cruzan."),
   PASOS([("[a]=\\{x:\\ x\\,R\\,a\\}","La clase de a reúne a todos sus relacionados."),
          ("[a]=[b]\\ \\text{o}\\ [a]\\cap[b]=\\emptyset","Dos clases son iguales o no tienen nada en común."),
          ("\\mathbb{Z}/5\\mathbb{Z}=\\{[0],[1],[2],[3],[4]\\}","Hay cinco clases de enteros módulo 5.")]),
   OJO("Cada elemento de una clase puede representarla. La clase de 2 módulo 5 es la misma que la clase de 7 o la de menos 3.")),
 eng("Las casillas de una tabla hash","Una tabla hash con 5 casillas guarda cada clave k en la casilla que resulta de k módulo 5. Las claves 7, 12 y 17 caen todas en la casilla 2, porque tienen el mismo residuo. Las claves que comparten casilla forman una clase de equivalencia.","k\\equiv j\\pmod{5}",
   [("Casillas","5"),("Claves 7, 12 y 17","casilla 2"),("Claves por casilla si hay 15","3")],"Si las claves se reparten bien, cada clase tiene más o menos el mismo número de elementos, y buscar una clave es rápido. Cuando muchas claves caen en la misma clase hay colisiones. Entender las clases de equivalencia permite diseñar funciones hash que repartan mejor los datos."),
 completar("Se prueba que x R y si x menos y es par es simétrica. Falta el paso.","x-y\\ \\text{par}\\ \\Rightarrow\\ y-x=[[hueco]]\\ \\text{es par}",
   [("-(x-y)","el opuesto de x menos y"),("x-y","la misma diferencia"),("2(x-y)","el doble")],0,
   ["","La diferencia y menos x no es igual a x menos y, sino a su opuesto.","El doble no es lo que se obtiene al invertir el orden."],"Invertir el orden cambia el signo.","y menos x es el opuesto de x menos y, y el opuesto de un número par también es par."),
 error("Alguien dijo que la relación x menor o igual que y es de equivalencia y se equivocó en un paso. Toca el paso que está mal.",
   [("x\\le x","Reflexiva. Se cumple.","es reflexiva"),
    ("x\\le y\\Rightarrow y\\le x","Simétrica. Este paso es el que falla.","es simétrica"),
    ("\\text{Entonces es de equivalencia}","Conclusión.","es de equivalencia")],1,
   "Si x menor o igual que y, no siempre y es menor o igual que x. Con 1 y 2 se cumple uno menor o igual que 2, pero no 2 menor o igual que 1. Falla la simetría.",
   "1\\le2\\ \\text{pero}\\ 2\\not\\le1","Prueba con dos números distintos."),
 ordenar("Estos son los pasos para probar la transitividad de la congruencia módulo 5, pero están desordenados.",
   [("5\\mid x-y\\ \\text{y}\\ 5\\mid y-z","Se parte de dos diferencias múltiplos de 5"),
    ("x-y=5a,\\ \\ y-z=5b","Se escriben como múltiplos"),
    ("x-z=5(a+b)","Se suman las dos igualdades"),
    ("5\\mid x-z","Por tanto x y z se relacionan")],[2,0,3,1],
   "Se escriben las dos diferencias como múltiplos de 5 y se suman.","Se empieza con lo que se sabe."),
]
S+=cierre("Mini simulacro de relaciones de equivalencia",[
 banco("fu_c3_02","Es reflexiva, simétrica y transitiva."),
 banco("fu_c3_06","Hay un residuo por cada clase, y los residuos módulo 5 son 5."),
 banco("fu_c3_07","La clase de 2 módulo 4 reúne los números de la forma 4k más 2.")])
prac=[
 {"titulo":"Los números","grafica":{"draw":1,"guide":1},"bloques":[P("Los enteros del 0 al 14 en filas de 5."),EQ("x\\,R\\,y\\iff 5\\mid x-y")]},
 {"titulo":"Recorre las clases","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 4. Se resalta la columna de cada clase.")]},
 {"titulo":"La clase del 2","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("[2]=\\{\\ldots,-3,2,7,12,\\ldots\\}"),P("La columna 2 tiene el 2, el 7 y el 12.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Los elementos de una clase se obtienen sumando múltiplos del módulo."}]}]
preg={"tex":"\\text{Una clase de equivalencia módulo}\\ 3\\ \\text{es}","opciones":["$\\{\\ldots,-4,-1,2,5,8,\\ldots\\}$","$\\{0,1,2\\}$","$\\{2,3,4,5\\}$","$\\{1,3,5,7,\\ldots\\}$"],"correcta":0,
 "explicacion":"Una clase módulo 3 reúne a todos los enteros con el mismo residuo, que se obtienen sumando o restando múltiplos de 3. El conjunto de 2, 5, 8 y demás es la clase del 2, y los otros no son clases.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Los elementos de una clase se obtienen sumando 3.","Busca un conjunto infinito en los dos sentidos.","Es el primero."],
 "errores":["","Ese conjunto tiene los tres residuos distintos, o sea, una clase de cada una.","Ese conjunto no cumple que la diferencia entre elementos sea múltiplo de 3.","Ese conjunto es el de los impares, que es una clase del módulo 2."]}
res=["Una relación de equivalencia es reflexiva, simétrica y transitiva.","Sus clases son disjuntas y cubren el conjunto, o sea, forman una partición.","La congruencia módulo n tiene n clases, una por cada residuo posible."]
write(lesson("fu-m3-l2","Lección 2 de 5","Relaciones de equivalencia",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-equivalencia.json")
