import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 3 Relaciones y funciones"
W=1.3; H=0.9
REL=[lambda i,j:i<=j, lambda i,j:(i==j) or {i,j}=={1,2}, lambda i,j:i!=j, lambda i,j:(i,j)==(1,2)]
def rect(xa,ya,xb,yb,c,txt=None):
    d={"t":"poligono","puntos":[[str(xa),str(ya)],[str(xb),str(ya)],[str(xb),str(yb)],[str(xa),str(yb)]],"c":c}
    if txt is not None: d["nombre"]=txt
    return d
EL=[rect(0,3.6,W,2.7,0,"x/y")]
for j in range(1,4):
    EL.append(rect(round(j*W,3),3.6,round((j+1)*W,3),2.7,0,str(j)))
for i in range(1,4):
    top=round(3.6-i*H,3); bot=round(top-H,3)
    EL.append(rect(0,top,W,bot,0,str(i)))
    for j in range(1,4):
        xa=round(j*W,3); xb=round((j+1)*W,3)
        L=lagr([1 if r(i,j) else 0 for r in REL])
        EL.append({"t":"poligono","puntos":[[str(xa),str(bot)],[str(xb),str(bot)],[str(xb),f"{bot}+{H}*({L})"],[str(xa),f"{bot}+{H}*({L})"]],"c":3})
        EL.append({"t":"poligono","puntos":[[str(xa),f"{bot}+{H}*({L})"],[str(xb),f"{bot}+{H}*({L})"],[str(xb),str(top)],[str(xa),str(top)]],"c":1})
refl=[1,1,0,0]; sim=[0,1,1,0]
graf={"tipo":"plano","x":[-1.25,6.45],"y":[-0.3,3.9],"a":0,"b":3,"inicio":0,"entero":True,"sinejes":True,"elementos":EL,
 "lecturas":[{"rotulo":"la relación es reflexiva (1 si es cierto)","formula":lagr(refl)},{"rotulo":"la relación es simétrica (1 si es cierto)","formula":lagr(sim)}],
 "etiquetas":["Reflexiva, 1 si la diagonal está llena","Simétrica, 1 si la tabla es igual al reflejarla sobre la diagonal"],"etiquetaSlider":"Relación, de 0 a 3",
 "alt":"Una tabla de 3 por 3 para el conjunto 1, 2, 3. Una casilla verde en la fila x y la columna y significa que x se relaciona con y. Con el deslizador cambia la relación entre menor o igual, equivalencia, distinto y un solo par"}
glos={"relacion":"Una relación en A es un conjunto de pares ordenados de A. Si el par x, y está en R se escribe x R y.",
 "reflexiva":"Una relación es reflexiva si todo elemento se relaciona consigo mismo. En la tabla, la diagonal está llena.",
 "simetrica":"Una relación es simétrica si cada vez que x se relaciona con y, también y se relaciona con x. La tabla es igual a su reflejo sobre la diagonal.",
 "transitiva":"Una relación es transitiva si x R y y y R z implican x R z.",
 "antisimetrica":"Una relación es antisimétrica si x R y y y R x solo pueden ocurrir cuando x es igual a y."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La tabla muestra una relación en el conjunto 1, 2, 3. Una casilla verde en la fila x y la columna y significa que x se relaciona con y."],
 [4,9,"Con la relación menor o igual, la diagonal está llena y por eso es reflexiva. Pero el par 1, 2 está y el 2, 1 no, así que no es simétrica."],
 [9,14,"Con la equivalencia, la diagonal está llena y la tabla es simétrica respecto de la diagonal."],
 [14,19,"La relación distinto tiene la diagonal vacía, así que no es reflexiva, pero sí es simétrica."],
 [19,24,"Reflexiva pide la diagonal llena. Simétrica pide que la tabla sea igual al reflejarla sobre la diagonal."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[8,0],[9,1],[13,1],[14,2],[18,2],[19,0],[24,0]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[19,24]}}
S=[
 sec("La idea",None,P("Una {{gl:relacion|relación}} dice qué elementos de un conjunto están conectados entre sí. Se estudian cuatro propiedades. La {{gl:reflexiva|reflexiva}} conecta cada elemento consigo mismo, la {{gl:simetrica|simétrica}} conecta en los dos sentidos, la {{gl:antisimetrica|antisimétrica}} no permite conexiones de ida y vuelta entre distintos, y la {{gl:transitiva|transitiva}} permite encadenar. Con ellas se distinguen las equivalencias y los órdenes.")),
 sec("Un ejemplo","Un ejemplo",P("La tabla muestra cuatro relaciones en el conjunto 1, 2, 3. Una casilla verde significa que la fila se relaciona con la columna."),EQ("x\\,R\\,y\\ \\iff\\ (x,y)\\in R"),{"t":"grafica","animar":"dibujar","alt":"La tabla de la relación"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Una relación en el conjunto 1, 2, 3 es reflexiva. ¿Cuántos pares tiene como mínimo?","opciones":[1,2,3,6],"correcta":3,"bien":"Muy bien. Son 3, los de la diagonal, el 1, 1, el 2, 2 y el 3, 3. Más abajo se ve en la tabla.","mal":"Son 3, los pares de la diagonal, el 1, 1, el 2, 2 y el 3, 3. Más abajo se ve en la tabla."}),
 sec("Recorriendo las relaciones","Las relaciones",P("Mira las cuatro relaciones y sus lecturas."),{"t":"acercando","ds":[0,1,2,3],"alt":"Las cuatro relaciones"},P("La equivalencia es la única que es reflexiva y simétrica a la vez.")),
 sec("Las cuatro propiedades","Propiedades",P("Cada propiedad se lee en la tabla o se prueba con elementos."),
   PASOS([("\\forall x\\ \\ x\\,R\\,x","Reflexiva. Toda la diagonal está llena."),
          ("x\\,R\\,y\\ \\Rightarrow\\ y\\,R\\,x","Simétrica. La tabla es igual a su reflejo."),
          ("x\\,R\\,y\\ \\wedge\\ y\\,R\\,x\\ \\Rightarrow\\ x=y","Antisimétrica. No hay ida y vuelta entre elementos distintos."),
          ("x\\,R\\,y\\ \\wedge\\ y\\,R\\,z\\ \\Rightarrow\\ x\\,R\\,z","Transitiva. Si hay un camino de dos pasos, también hay uno directo.")]),
   OJO("Simétrica y antisimétrica no son opuestas. La igualdad es las dos cosas, y una relación con el par 1, 2 y el par 2, 1 no es ninguna de las dos si se agrega algo más.")),
 sec("Equivalencias y órdenes","Tipos",P("Con las propiedades se arman dos tipos de relaciones muy importantes."),
   PASOS([("\\text{reflexiva}+\\text{simétrica}+\\text{transitiva}","Relación de equivalencia, como tener el mismo residuo."),
          ("\\text{reflexiva}+\\text{antisimétrica}+\\text{transitiva}","Orden parcial, como menor o igual o como divide a."),
          ("x\\ \\text{divide a}\\ y\\ \\text{en}\\ \\mathbb{Z}^{+}","Es reflexiva y transitiva, pero no simétrica, porque 2 divide a 4 y 4 no divide a 2.")]),
   OJO("La relación x R y si el producto x por y es mayor o igual que cero no es transitiva. Con 1, 0 y menos 1, el 0 rompe la cadena.")),
 eng("Las dependencias de un proyecto","En un proyecto se dice que la tarea A precede a la B si A debe terminar antes de que empiece B. Si A precede a B y B precede a C, entonces A precede a C, que es la transitividad. Y no puede ocurrir que A preceda a B y B preceda a A, que es la antisimetría.","a\\prec b,\\ b\\prec c\\ \\Rightarrow\\ a\\prec c",
   [("Tareas","A, B y C"),("Dependencias directas","A antes de B, B antes de C"),("Dependencia que se deduce","A antes de C")],"Si las dependencias formaran un ciclo, A precedería a B y B precedería a A, y el proyecto no podría terminar, porque ninguna tarea podría empezar primero. Verificar que la relación es antisimétrica y transitiva, o sea un orden parcial, sirve para detectar ciclos y para calcular una secuencia posible de trabajo."),
 completar("Se prueba que la relación x divide a y es reflexiva. Falta lo que debe cumplirse.","\\text{Reflexiva exige que}\\ [[hueco]]\\ \\text{para todo}\\ x",
   [("x\\mid x","x divide a x"),("x\\mid y","x divide a y"),("y\\mid x","y divide a x")],0,
   ["","Eso habla de dos elementos distintos, y la reflexividad solo compara cada elemento consigo mismo.","Eso también habla de dos elementos, y no de un elemento con él mismo."],"Reflexiva compara cada elemento consigo mismo.","Todo número se divide a sí mismo, así que x divide a x y la relación es reflexiva."),
 error("Alguien dijo que la relación x R y si x por y es mayor o igual que cero es transitiva y se equivocó en un paso. Toca el paso que está mal.",
   [("x=1,\\ y=0,\\ z=-1","Se eligen valores.","se eligen tres números"),
    ("1\\cdot0\\ge0\\ \\text{y}\\ 0\\cdot(-1)\\ge0","Se cumplen x R y y y R z.","las dos primeras relaciones valen"),
    ("\\text{Entonces}\\ 1\\cdot(-1)\\ge0\\ \\text{y}\\ x\\,R\\,z","Este paso es el que falla.","también x R z")],2,
   "El producto de 1 por menos 1 es menos 1, que no es mayor o igual que cero. Entonces x no se relaciona con z, y la relación no es transitiva.",
   "1\\cdot(-1)=-1<0","Calcula el producto de x por z."),
 ordenar("Estos son los pasos para probar que x divide a y es transitiva, pero están desordenados.",
   [("x\\mid y\\ \\text{y}\\ y\\mid z","Se parte de las dos divisibilidades"),
    ("y=xa,\\ \\ z=yb","Se escriben con múltiplos"),
    ("z=x(ab)","Se sustituye y"),
    ("x\\mid z","Por tanto la relación es transitiva")],[2,0,3,1],
   "Se escriben las dos divisibilidades, se sustituye y se ve que x divide a z.","Se empieza con las hipótesis."),
]
S+=cierre("Mini simulacro de relaciones y sus propiedades",[
 banco("fu_c3_03","Reflexiva exige la diagonal completa, o sea, todos los pares de un elemento consigo mismo."),
 banco("fu_c3_04","Divide a es reflexiva y transitiva, pero no simétrica."),
 banco("fu_c3_05","El cero rompe la transitividad de la relación del producto.")])
prac=[
 {"titulo":"La tabla","grafica":{"draw":1,"guide":1},"bloques":[P("Una tabla de 3 por 3 para el conjunto 1, 2, 3."),EQ("x\\,R\\,y")]},
 {"titulo":"Recorre las relaciones","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 3. Abajo se lee si la relación es reflexiva y si es simétrica.")]},
 {"titulo":"La equivalencia","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("\\text{reflexiva}=1,\\ \\text{simétrica}=1"),P("Con la relación 1, la diagonal está llena y la tabla es igual a su reflejo.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Revisa una por una las propiedades en la relación menor que."}]}]
preg={"tex":"\\text{La relación}\\ x<y\\ \\text{en}\\ \\mathbb{R}\\ \\text{es}","opciones":["transitiva, pero no reflexiva ni simétrica","reflexiva y transitiva","de equivalencia","simétrica y transitiva"],"correcta":0,
 "explicacion":"Menor que no es reflexiva, porque x no es menor que x. No es simétrica, porque si x es menor que y entonces y no es menor que x. Sí es transitiva, porque x menor que y y y menor que z dan x menor que z.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Revisa si x es menor que x.","Revisa si se puede invertir el orden.","Solo se cumple la transitividad."],
 "errores":["","No es reflexiva, porque x no es menor que x.","No es de equivalencia, porque no es reflexiva ni simétrica.","No es simétrica, porque si x es menor que y entonces y no es menor que x."]}
res=["Una relación puede ser reflexiva, simétrica, antisimétrica y transitiva, y se lee en la tabla.","Reflexiva más simétrica más transitiva es una equivalencia, y reflexiva más antisimétrica más transitiva es un orden parcial.","Para refutar una propiedad basta un contraejemplo, y para probarla hay que cubrir todos los casos."]
write(lesson("fu-m3-l3","Lección 3 de 5","Relaciones y sus propiedades",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-relaciones.json")
