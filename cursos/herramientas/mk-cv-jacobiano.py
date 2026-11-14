import os, math
os.environ['CURSO_FU']='Cálculo en Varias Variables'; os.environ['BANCO']='calcvec'
from mklib import *
MOD="Módulo 2 Integrales múltiples"
EL=[{"t":"poligono","puntos":[["0","0"],["x","0"],["x","x"],["0","x"]],"c":0,"nombre":"R"},
    {"t":"poligono","puntos":[["0","0"],["2*x","x"],["3*x","3*x"],["x","2*x"]],"c":1,"nombre":"S"}]
graf={"tipo":"plano","x":[-2.5,9.6],"y":[-0.6,6.6],"a":0.3,"b":2,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"área del cuadrado en u y v, de lado s","formula":"x*x"},{"rotulo":"área de su imagen en x y y, igual a 3 por el área anterior","formula":"3*x*x"}],
 "etiquetas":["El cuadrado de lado s en el plano u v","Su imagen en el plano x y, que es un paralelogramo con tres veces el área"],"etiquetaSlider":"Lado s, de 0.3 a 2",
 "alt":"Un cuadrado de lado s en el plano u v, y su imagen bajo la transformación x igual a 2u más v, y igual a u más 2v. La imagen es un paralelogramo con vértices 0, 0, 2s, s, 3s, 3s y s, 2s. El área de la imagen es el área del cuadrado por el jacobiano, que vale 3"}
glos={"jacobiano":"El jacobiano de una transformación es el determinante de sus derivadas parciales, y mide cuánto se estira el área.",
 "cambio":"Un cambio de variable reemplaza x y y por funciones de u y v, para convertir una región o una función complicada en una sencilla.",
 "absoluto":"En la integral se usa el valor absoluto del jacobiano, porque el área no puede ser negativa.",
 "polar":"El jacobiano de las polares es r, y por eso el elemento de área es r dr d theta."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"Un cuadrado de lado s en el plano u v se transforma con x igual a 2u más v y y igual a u más 2v."],
 [4,10,"La imagen es un paralelogramo. Su área no es la del cuadrado, sino tres veces más."],
 [10,16,"Con s igual a 1 el cuadrado tiene área 1 y el paralelogramo tiene área 3."],
 [16,20,"Con s igual a 2 el cuadrado tiene área 4 y la imagen tiene área 12. La razón siempre es 3."],
 [20,24,"Ese 3 es el valor absoluto del jacobiano, el determinante de la matriz de derivadas."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0.5],[8,0.5],[10,1],[13,1],[16,2],[18,2],[24,2]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Un {{gl:cambio|cambio de variable}} transforma una región difícil en una sencilla. El área se estira o se encoge, y el {{gl:jacobiano|jacobiano}} dice por cuánto. En la integral se usa su {{gl:absoluto|valor absoluto}}. Las polares son un caso especial, con jacobiano igual a r, que explica el {{gl:polar|factor r}}.")),
 sec("Un ejemplo","Un ejemplo",P("La transformación es x igual a 2u más v y y igual a u más 2v. Cambia el lado y mira cómo cambia el área."),EQ("J=\\begin{vmatrix}x_{u}&x_{v}\\\\y_{u}&y_{v}\\end{vmatrix}=\\begin{vmatrix}2&1\\\\1&2\\end{vmatrix}=3"),{"t":"grafica","animar":"dibujar","alt":"El cuadrado y su imagen, con tres veces el área"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Un cuadrado de lado 1 se transforma con jacobiano 3. ¿Cuál es el área de la imagen?","opciones":[3,1,9,1.5],"correcta":3,"bien":"Muy bien. El área se multiplica por el valor absoluto del jacobiano.","mal":"El área se multiplica por 3, y da 3."}),
 sec("Distintos tamaños","Tamaños",P("Mira el área con s igual a 0.5, 1, 1.5 y 2."),{"t":"acercando","ds":[0.5,1,1.5,2],"alt":"El cuadrado y su imagen con cuatro lados"},P("La imagen siempre mide 3 veces el área del cuadrado.")),
 sec("Calcular el jacobiano","Jacobiano",P("Es el determinante de las derivadas de x y de y respecto a u y a v."),
   PASOS([("x=2u+v,\\quad y=u+2v","La transformación."),
          ("J=\\dfrac{\\partial(x,y)}{\\partial(u,v)}=x_{u}y_{v}-x_{v}y_{u}","La definición."),
          ("J=2\\cdot2-1\\cdot1=3","El valor."),
          ("\\displaystyle\\iint_{R}f\\,dx\\,dy=\\iint_{S}f\\,|J|\\,du\\,dv","La fórmula de cambio de variable.")]),
   OJO("El jacobiano que se usa es el de x y y respecto a u y v, el de la transformación que va de u v a x y. Si se calcula el inverso, queda uno entre J.")),
 sec("Las polares","Polares",P("El jacobiano de las polares explica el factor r."),
   PASOS([("x=r\\cos\\theta,\\quad y=r\\operatorname{sen}\\theta","Las polares."),
          ("J=\\begin{vmatrix}\\cos\\theta&-r\\operatorname{sen}\\theta\\\\\\operatorname{sen}\\theta&r\\cos\\theta\\end{vmatrix}","El determinante."),
          ("J=r\\cos^{2}\\theta+r\\operatorname{sen}^{2}\\theta=r","Con la identidad pitagórica."),
          ("dA=r\\,dr\\,d\\theta","El elemento de área.")]),
   OJO("Para x igual a u más v y y igual a u menos v el jacobiano es menos 2, y se usa su valor absoluto, 2.")),
 eng("El cambio de variable en un mapa","Una zona rectangular de un mapa se transforma a otro sistema de coordenadas lineal. El área real de la zona se calcula con el jacobiano de la transformación.","A_{real}=|J|\\,A_{mapa}",
   [("Jacobiano","3"),("Área en el mapa","10 unidades"),("Área real","30 unidades")],"Con transformaciones no lineales el jacobiano cambia de un punto a otro. Entonces se integra su valor, en lugar de multiplicar por una constante."),
 completar("En un cambio de variable, el área se multiplica por el valor absoluto del [[hueco]].","dx\\,dy=[[hueco]]\\,du\\,dv",
   [("|J|","el valor absoluto del jacobiano"),("J^{-1}","el inverso del jacobiano"),("1","uno")],0,
   ["","El inverso del jacobiano sirve para ir en sentido contrario.","Con uno el área se conservaría. Aquí el determinante da otro valor, y se calcula con la fórmula."],"Es el determinante de las derivadas.","Es el jacobiano."),
 error("Alguien calculó el jacobiano de x igual a 2u más v y y igual a u más 2v, y se equivocó. Toca el paso que está mal.",
   [("x_{u}=2,\\ x_{v}=1,\\ y_{u}=1,\\ y_{v}=2","Derivadas.","derivadas"),
    ("J=2\\cdot1-1\\cdot2=0","Este paso es el que falla.","usa los productos cruzados"),
    ("J=0","Resultado.","cero")],1,
   "El determinante es x sub u por y sub v menos x sub v por y sub u, o sea 2 por 2 menos 1 por 1, que da 3.",
   "J=2\\cdot2-1\\cdot1=3","Multiplica la diagonal principal y resta el producto de la otra."),
 ordenar("Estos son los pasos para hacer un cambio de variable, pero están desordenados.",
   [("x=x(u,v),\\ y=y(u,v)","Se define el cambio"),
    ("J=x_{u}y_{v}-x_{v}y_{u}","Se calcula el jacobiano"),
    ("S","Se transforma la región"),
    ("\\displaystyle\\iint_{S}f\\,|J|\\,du\\,dv","Se escribe la integral")],[2,0,3,1],
   "Primero el cambio, luego el jacobiano, después la región y por último la integral.","Se empieza definiendo el cambio."),
]
S+=cierre("Mini simulacro de cambio de variable",[
 banco("cv_c2_14","El factor del cambio de variable."),
 pnum("El jacobiano de $x=2u+v,\\ y=u+2v$ es:","3",0.01,"Es 2 por 2 menos 1 por 1, o sea 3."),
 pnum("El valor absoluto del jacobiano de $x=u+v,\\ y=u-v$ es:","2",0.01,"El determinante es 1 por menos 1 menos 1 por 1, que da menos 2, y su valor absoluto es 2.")])
prac=[
 {"titulo":"El cuadrado","grafica":{"draw":1},"bloques":[P("Se transforma un cuadrado de lado s."),EQ("x=2u+v,\\quad y=u+2v")]},
 {"titulo":"Cambia el lado","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el área del cuadrado y la de su imagen.")]},
 {"titulo":"Con lado 2","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("4\\cdot3=12"),P("Con s igual a 2 el área de la imagen es 12.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El área se multiplica por el valor absoluto del jacobiano."}]}]
preg={"tex":"x=2u+v,\\ y=u+2v.\\ \\text{El jacobiano vale}","opciones":["$3$","$5$","$1$","$4$"],"correcta":0,
 "explicacion":"El determinante es 2 por 2 menos 1 por 1, o sea 3.",
 "verificacion":{"formula":"2*2-1*1+0*x","a":0,"esperado":3},
 "pistas":["Es un determinante de 2 por 2.","Las entradas son las derivadas parciales.","Diagonal principal menos la otra."],
 "errores":["","El 5 sale de sumar 2 por 2 y 1 por 1 en lugar de restarlos.","El 1 es el valor de la diagonal secundaria.","El 4 es el producto de la diagonal sin restar."]}
res=["El jacobiano es el determinante de las derivadas parciales, y mide el factor de estiramiento del área.","En la integral se usa su valor absoluto.","Las polares tienen jacobiano r."]
write(lesson("cv-m2-l3","Lección 3 de 6","Cambio de variable y jacobiano",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Cálculo en Varias Variables"),"cv-jacobiano.json")
