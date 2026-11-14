import os, math
os.environ['CURSO_FU']='Geometría Vectorial y Analítica'; os.environ['BANCO']='geovec'
from mklib import *
MOD="Módulo 2 Vectores en el espacio"
B=3.605551275
graf={"tipo":"plano","x":[-1.5,8.0],"y":[-1.5,8.5],"a":0,"b":8,"inicio":6,
 "elementos":[
  {"t":"poligono","puntos":[["0","0"],[str(B),"0"],[str(B),"x"]],"c":3},
  {"t":"segmento","a":["0","0"],"b":[str(B),"0"],"c":0,"nombre":"base","guia":True},
  {"t":"segmento","a":[str(B),"0"],"b":[str(B),"x"],"c":2,"guia":True,"guion":True},
  {"t":"vector","b":[str(B),"x"],"nombre":"u","c":1}],
 "lecturas":[{"rotulo":"norma de u, con u igual a (2, 3, z)","formula":"sqrt(13+x*x)"},{"rotulo":"cuadrado de la norma","formula":"13+x*x"}],
 "etiquetas":["Longitud del vector u en el espacio","Suma de los cuadrados de las tres componentes"],"etiquetaSlider":"Tercera componente z",
 "alt":"Un triángulo rectángulo con la diagonal de la base, que mide raíz de 13, y la altura z. La hipotenusa es el vector u igual a (2, 3, z), y su longitud es la raíz de 13 más z al cuadrado"}
glos={"componentes3":"Un vector de R³ tiene tres componentes, que miden cuánto avanza en cada eje.",
 "norma3":"La norma de un vector de R³ es la raíz de la suma de los cuadrados de sus tres componentes.",
 "punto3":"El producto punto en R³ es la suma de los tres productos de componentes. También vale la norma de u por la de v por el coseno del ángulo.",
 "ortogonales3":"Dos vectores de R³ son ortogonales si su producto punto es cero."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"El vector u tiene componentes 2, 3 y z. Primero se mide la diagonal de su base, que es la raíz de 13."],
 [4,10,"Después, la altura z y esa diagonal forman un triángulo rectángulo. Su hipotenusa es la norma de u."],
 [10,15,"Con z igual a 6, la norma es la raíz de 49, que es 7."],
 [15,19,"Con z igual a 0, el vector queda en el plano de la base y la norma es la raíz de 13."],
 [19,22,"La fórmula es la raíz de la suma de los tres cuadrados."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,2],[8,4],[10,6],[15,6],[17,0],[19,0],[22,0]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[19,22]}}
S=[
 sec("La idea",None,P("Un vector del espacio tiene tres {{gl:componentes3|componentes}}. Todo lo del plano se extiende con una componente más. La {{gl:norma3|norma}} es la raíz de la suma de tres cuadrados, el {{gl:punto3|producto punto}} suma tres productos, y dos vectores son {{gl:ortogonales3|ortogonales}} si ese producto es cero.")),
 sec("Un ejemplo","Un ejemplo",P("Mira el vector u de componentes 2, 3 y z. Su norma se arma con dos triángulos rectángulos, uno en la base y otro vertical."),EQ("\\|\\mathbf{u}\\|=\\sqrt{2^{2}+3^{2}+z^{2}}=\\sqrt{13+z^{2}}"),{"t":"grafica","animar":"dibujar","alt":"El triángulo de la norma de u"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La diagonal de la base mide la raíz de 13 y la altura es 6. ¿Cuánto vale 13 más 6 al cuadrado?","opciones":[19,36,49,169],"correcta":49,"bien":"Muy bien. Es 13 más 36, o sea 49, y su raíz es 7. Más abajo se ve.","mal":"Es 13 más 36, o sea 49, y su raíz es 7. Más abajo se ve."}),
 sec("Cambiando z","Cambiando z",P("Mira la norma de u para z igual a 0, 2, 4 y 6."),{"t":"acercando","ds":[0,2,4,6],"alt":"El vector u para cuatro valores de z"},P("Con z igual a 6 el vector es (2, 3, 6) y su norma es exactamente 7.")),
 sec("Producto punto y norma","Producto punto",P("Se hacen las mismas cuentas del plano, con una componente más."),
   PASOS([("(1,2,3)\\cdot(4,5,6)=4+10+18=32","Se multiplica componente por componente y se suma."),
          ("\\|(2,3,6)\\|=\\sqrt{4+9+36}=7","La norma, con tres cuadrados."),
          ("(1,0,0)\\cdot(0,1,0)=0","Los vectores de la base son ortogonales entre sí."),
          ("\\cos\\theta=\\dfrac{\\mathbf{u}\\cdot\\mathbf{v}}{\\|\\mathbf{u}\\|\\,\\|\\mathbf{v}\\|}","El ángulo entre dos vectores del espacio.")])),
 sec("Ortogonalidad y ángulos","Ángulos",P("El producto punto detecta los ángulos rectos y mide los demás."),
   PASOS([("(1,2,3)\\cdot(2,-1,0)=2-2+0=0","Son ortogonales."),
          ("(1,1,0)\\cdot(0,1,1)=1","El producto punto es 1."),
          ("\\cos\\theta=\\dfrac{1}{\\sqrt{2}\\,\\sqrt{2}}=\\dfrac12\\ \\Rightarrow\\ \\theta=60^{\\circ}","El ángulo entre las dos diagonales de caras vecinas de un cubo.")]),
   OJO("En el espacio, dos vectores perpendiculares a un tercero no son paralelos entre sí. Hay infinitos vectores perpendiculares a uno dado, y forman un plano.")),
 eng("El ángulo entre dos barras","Dos barras salen de un mismo nodo de una armadura espacial, con vectores (2, 3, 6) y (6, 2, 3) metros. Para diseñar la unión se necesita el ángulo entre ellas, que se obtiene con el producto punto.","\\cos\\theta=\\dfrac{36}{7\\cdot7}=\\dfrac{36}{49}",
   [("Barra 1","(2, 3, 6) m"),("Barra 2","(6, 2, 3) m"),("Ángulo entre ellas","42.7 grados")],"Las dos barras miden 7 metros, el producto punto es 36 y el coseno es 36 sobre 49, o sea 0.735. El ángulo es 42.7 grados. Con ese valor se diseña la placa de unión. Es un cálculo geométrico y no incluye las cargas, que dependen del material y de la estructura."),
 completar("Se calcula el producto punto de (1, 2, 2) y (3, 0, 4). Falta el resultado.","1\\cdot3+2\\cdot0+2\\cdot4=[[hueco]]",
   [("11","once"),("9","nueve"),("24","veinticuatro")],0,
   ["","Nueve sale de olvidar el último producto, 2 por 4.","Veinticuatro es el producto de todas las componentes, y no la suma de los productos."],"Se suman los tres productos.","3 más 0 más 8 es 11."),
 error("Alguien calculó la norma de un vector y se equivocó en un paso. Toca el paso que está mal.",
   [("\\mathbf{u}=(2,3,6)","El vector.","el vector es 2, 3, 6"),
    ("\\|\\mathbf{u}\\|=\\sqrt{2+3+6}=\\sqrt{11}","Este paso es el que falla.","la norma es raíz de 11"),
    ("\\text{La norma vale}\\ 3.32","Depende del paso anterior.","la norma vale 3.32")],1,
   "En la norma se elevan al cuadrado las componentes antes de sumar. La suma correcta es 4 más 9 más 36, o sea 49, y la norma es 7.",
   "\\|\\mathbf{u}\\|=\\sqrt{4+9+36}=7","Recuerda elevar cada componente al cuadrado."),
 ordenar("Estos son los pasos para hallar el ángulo entre (1, 1, 0) y (0, 1, 1), pero están desordenados.",
   [("\\mathbf{u}\\cdot\\mathbf{v}=0+1+0=1","Se calcula el producto punto"),
    ("\\|\\mathbf{u}\\|=\\|\\mathbf{v}\\|=\\sqrt{2}","Se calculan las normas"),
    ("\\cos\\theta=\\dfrac{1}{2}","Se arma el coseno"),
    ("\\theta=60^{\\circ}","Se despeja el ángulo")],[2,0,3,1],
   "Se calcula el producto punto, las normas, el coseno y finalmente el ángulo.","Se empieza con el producto punto."),
]
S+=cierre("Mini simulacro de vectores en R³ y producto punto",[
 banco("gv_c2_03","El producto punto es $2-2+0=0$, así que son ortogonales."),
 banco("gv_c2_07","$\\sqrt{4+9+36}=7$."),
 banco("gv_c2_08","El coseno del ángulo es el producto punto entre el producto de las normas.")])
prac=[
 {"titulo":"El vector","grafica":{"draw":1},"bloques":[P("El vector u de componentes 2, 3 y z."),EQ("\\|\\mathbf{u}\\|=\\sqrt{13+z^{2}}")]},
 {"titulo":"Cambia z","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen la norma de u y el cuadrado de la norma.")]},
 {"titulo":"Norma 7","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":6,"bloques":[EQ("\\|(2,3,6)\\|=\\sqrt{49}=7"),P("Con z igual a 6 la norma vale exactamente 7.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":6},"bloques":[{"t":"pregunta"},{"t":"nota","html":"El coseno es el producto punto entre el producto de las normas."}]}]
preg={"tex":"\\text{El ángulo entre}\\ (1,1,0)\\ \\text{y}\\ (0,1,1)\\ \\text{es}","opciones":["$60^{\\circ}$","$45^{\\circ}$","$90^{\\circ}$","$30^{\\circ}$"],"correcta":0,
 "explicacion":"El producto punto es 1 y las dos normas son raíz de 2, así que el coseno es 1 entre 2. El ángulo cuyo coseno es un medio mide 60 grados.",
 "verificacion":{"formula":"(0+1+0)/(sqrt(2)*sqrt(2))+0*x","a":0,"esperado":0.5},
 "pistas":["Calcula el producto punto y las normas.","El coseno sale 1 entre 2.","El ángulo es 60 grados."],
 "errores":["","El coseno de 45 grados es raíz de 2 entre 2, y aquí el coseno es 1 entre 2.","Noventa grados sería un producto punto igual a cero, y aquí vale 1.","El coseno de 30 grados es raíz de 3 entre 2, y aquí el coseno es 1 entre 2."]}
res=["En el espacio, la norma es la raíz de la suma de tres cuadrados y el producto punto suma tres productos.","Dos vectores son ortogonales si su producto punto es cero.","El ángulo entre dos vectores sale del coseno, que es el producto punto entre el producto de las normas."]
write(lesson("gv-m2-l3","Lección 3 de 4","Vectores en R³ y producto punto",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Geometría Vectorial y Analítica"),"geovec-r3.json")
