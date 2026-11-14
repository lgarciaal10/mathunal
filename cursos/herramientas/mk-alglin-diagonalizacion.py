import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 3 Ortogonalidad y valores propios"
graf={"tipo":"plano","x":[-3.5,9.33],"y":[-2,5],"a":0,"b":2,"inicio":1,"entero":True,
 "elementos":[
  {"t":"recta","p":["0","0"],"dir":["1","1"],"guion":True,"nombre":"valor propio 3","c":1},
  {"t":"recta","p":["0","0"],"dir":["1","-1"],"guion":True,"nombre":"valor propio 1","c":3},
  {"t":"vector","b":["(exp(x*ln(3))+1)/2","(exp(x*ln(3))-1)/2"],"nombre":"A^n v","c":2},
  {"t":"segmento","a":["0","0"],"b":["exp(x*ln(3))/2","exp(x*ln(3))/2"],"nombre":"crece","c":1,"guia":True},
  {"t":"segmento","a":["exp(x*ln(3))/2","exp(x*ln(3))/2"],"b":["(exp(x*ln(3))+1)/2","(exp(x*ln(3))-1)/2"],"nombre":"queda igual","c":3,"guia":True}],
 "lecturas":[{"rotulo":"n","formula":"x"},{"rotulo":"peso en la dirección (1, 1)","formula":"exp(x*ln(3))/2"}],
 "etiquetas":["Número de aplicaciones","Peso en la dirección (1, 1)"],"etiquetaSlider":"Número n de aplicaciones de A",
 "alt":"El vector (1, 0) después de aplicarle n veces la matriz de filas (2, 1) y (1, 2). Su parte sobre la dirección (1, 1) se triplica en cada paso y su parte sobre (1, menos 1) no cambia"}
glos={"diagonalizable":"Una matriz es diagonalizable si se puede escribir como P por D por P inversa, con D diagonal. Es lo mismo que tener tantos vectores propios independientes como su tamaño.",
 "diagonal":"Una matriz diagonal tiene ceros fuera de su diagonal principal. Sus potencias se calculan elevando cada número de la diagonal.",
 "propio":"Un vector propio de A es uno que A solo estira. El factor de estiramiento es su valor propio."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"La matriz A, de filas (2, 1) y (1, 2), tiene dos direcciones propias, con valores propios 3 y 1."],
 [3,6,"Se parte del vector (1, 0) y se le aplica A varias veces."],
 [6,12,"El vector se separa en dos partes, una sobre cada dirección propia. La parte de valor propio 3 se triplica en cada paso."],
 [12,17,"La parte de valor propio 1 no cambia. Por eso es fácil saber qué pasa después de n pasos."],
 [17,22,"Con n igual a 2 se obtiene (5, 4). La diagonalización da ese resultado sin multiplicar matrices."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,0],[8,1],[10,2],[12,0],[14,1],[16,2],[22,2]],"guide":[[6,0],[7,1]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("Elevar una matriz a una potencia grande es muy laborioso, pero se vuelve fácil si la matriz es {{gl:diagonalizable|diagonalizable}}. Entonces se cambia de base a la de sus vectores propios, donde la matriz es {{gl:diagonal|diagonal}} y las potencias son triviales, y se regresa. Sirve para estudiar procesos que se repiten en el tiempo.")),
 sec("Un ejemplo","Un ejemplo",P("Mira lo que pasa al aplicarle a un vector la matriz A varias veces."),EQ("A="+M(2,1,1,2)+",\\qquad A^{n}\\begin{pmatrix}1\\\\0\\end{pmatrix}=?"),{"t":"grafica","animar":"dibujar","alt":"El vector y sus imágenes sucesivas"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con n igual a 1, A por (1, 0) es la primera columna de A, o sea (2, 1). ¿Cuánto vale su primera componente?","opciones":[1,2,3,4],"correcta":2,"bien":"Muy bien. Vale 2. Más abajo se ve cómo sigue creciendo.","mal":"Vale 2, que es la primera entrada de la primera columna. Más abajo se ve cómo sigue creciendo."}),
 sec("Aplicar A varias veces","Varias veces",P("Mira cómo cambia el vector cuando se aplica A una, dos y más veces. Solo tienen sentido los valores enteros de n."),{"t":"acercando","ds":[0,1,2],"alt":"El vector después de cero, una y dos aplicaciones de A"},P("La parte sobre la dirección (1, 1) se triplica en cada paso. La parte sobre la dirección (1, menos 1) no cambia.")),
 sec("Diagonalizar","Diagonalizar",P("Se escribe A como P por D por P inversa, con las columnas de P siendo los vectores propios y D teniendo los valores propios en la diagonal."),
   PASOS([("\\lambda=3,\\ \\mathbf{v}=(1,1);\\qquad \\lambda=1,\\ \\mathbf{v}=(1,-1)","Son los valores y vectores propios de A."),
          ("P="+M(1,1,1,-1)+",\\quad D="+M(3,0,0,1),"Las columnas de P son los vectores propios y D lleva los valores propios en el mismo orden."),
          ("A=PDP^{-1}=\\dfrac{1}{2}"+M(3,1,3,-1)+M(1,1,1,-1)+"="+M(2,1,1,2),"Se comprueba multiplicando.")])),
 sec("Potencias","Potencias",P("Lo bueno de la forma diagonal es que sus potencias son fáciles."),
   EQ("A^{n}=PD^{n}P^{-1},\\qquad D^{n}=\\begin{pmatrix}3^{n}&0\\\\0&1^{n}\\end{pmatrix}"),
   PASOS([("A^{n}=\\dfrac{1}{2}"+M("3^{n}+1","3^{n}-1","3^{n}-1","3^{n}+1"),"Se multiplica P por D a la n por P inversa."),
          ("A^{2}=\\dfrac{1}{2}"+M(10,8,8,10)+"="+M(5,4,4,5),"Con n igual a 2."),
          ("A^{2}\\begin{pmatrix}1\\\\0\\end{pmatrix}=\\begin{pmatrix}5\\\\4\\end{pmatrix}","Es el vector que mostraba la gráfica.")])),
 sec("Cuándo se puede","Condiciones",P("No todas las matrices son diagonalizables."),
   PASOS([("A\\ (n\\times n)\\ \\text{diagonalizable}\\iff A\\ \\text{tiene}\\ n\\ \\text{vectores propios independientes}","Esa es la condición exacta."),
          ("n\\ \\text{valores propios distintos}\\ \\Rightarrow\\ \\text{diagonalizable}","Es una condición suficiente."),
          ("B="+M(2,1,0,2)+"\\ \\text{no es diagonalizable}","Solo tiene el valor propio 2, repetido, y un solo vector propio independiente, el (1, 0).")])),
 eng("El intercambio de calor entre dos placas","Dos placas se enfrían y calientan entre sí en intervalos de tiempo. En cada paso, cada placa conserva el 80 por ciento de su temperatura y recibe el 20 por ciento de la otra. La temperatura después de muchos pasos sale de las potencias de la matriz.","T_{n+1}=A\\,T_{n},\\quad A="+M(0.8,0.2,0.2,0.8),
   [("Temperaturas iniciales","100 y 20 °C"),("Valores propios","1 y 0.6"),("Después de 5 pasos","63.1 y 56.9 °C")],"Los valores propios son 1, con vector propio (1, 1), y 0.6, con vector propio (1, menos 1). La temperatura inicial se escribe como 60 por (1, 1) más 40 por (1, menos 1). Después de n pasos queda 60 por (1, 1) más 40 por 0.6 a la n por (1, menos 1). Con n igual a 5 salen 63.1 y 56.9 grados, y al final ambas placas llegan a 60. Es un modelo simplificado, porque no incluye pérdidas al ambiente."),
 completar("Se calcula D a la n para D igual a la matriz diagonal con 3 y 1. Falta el segundo elemento de la diagonal.","D^{n}=\\begin{pmatrix}3^{n}&0\\\\0&[[hueco]]\\end{pmatrix}",
   [("1","uno"),("n","n"),("3","tres")],0,
   ["","1 elevado a cualquier potencia es 1, no n. Cada número de la diagonal se eleva a la n.","Ese es el otro valor propio. El segundo elemento es 1, y 1 a la n es 1."],"Eleva el 1 a la n.","Cada elemento de la diagonal se eleva a la n, y 1 a la n es 1."),
 error("Alguien analizó si una matriz es diagonalizable y se equivocó en un paso. Toca el paso que está mal.",
   [("B="+M(2,1,0,2),"Es la matriz.","B tiene filas 2, 1 y 0, 2"),
    ("\\text{Sus valores propios son 2 y 2, así que }B=PDP^{-1}\\text{ con }D=2I","Este paso es el que falla."  ,"Sus valores propios son 2 y 2, así que B es P por D por P inversa con D igual a 2 veces la identidad"),
    ("\\text{Por tanto B es diagonalizable}","Depende del paso anterior.","Por tanto B es diagonalizable")],1,
   "Si D fuera 2I, entonces P D P inversa sería 2I, y B no lo es. Solo hay un vector propio independiente, el (1, 0), porque la nulidad de B menos 2I es 1. Faltan vectores propios, así que B no es diagonalizable.",
   "\\operatorname{rango}(B-2I)=1\\ \\Rightarrow\\ \\text{un solo vector propio independiente}","Si D fuera 2I, ¿a qué sería igual P D P inversa?"),
 ordenar("Estos son los pasos para calcular las potencias de A igual a la matriz de filas (2, 1) y (1, 2), pero están desordenados.",
   [("A=PDP^{-1}","Se diagonaliza A"),
    ("A^{n}=PD^{n}P^{-1}","Las potencias de A son las de D, entre P y P inversa"),
    ("D^{n}=\\operatorname{diag}(3^{n},1)","Se elevan los elementos de la diagonal"),
    ("A^{n}=\\dfrac{1}{2}"+M("3^{n}+1","3^{n}-1","3^{n}-1","3^{n}+1"),"Se multiplica y queda la fórmula")],[2,0,3,1],
   "Se diagonaliza, se eleva D a la n, se multiplica por P a la izquierda y por P inversa a la derecha.","Se empieza diagonalizando."),
]
S+=cierre("",None)
prac=[
 {"titulo":"Aplica A varias veces","grafica":{"draw":1},"bloques":[P("Se parte del vector (1, 0) y se le aplica la matriz n veces."),EQ("A="+M(2,1,1,2))]},
 {"titulo":"Cambia n","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Solo importan los valores enteros de n, 0, 1 y 2. Abajo se ven n y el peso del vector en la dirección (1, 1).")]},
 {"titulo":"Las dos partes","grafica":{"draw":1,"guide":1},"laboratorio":True,"d":2,"bloques":[P("El vector se separa en una parte sobre (1, 1), que crece, y otra sobre (1, menos 1), que queda igual. Con n igual a 2 el peso en (1, 1) es 4.5.")]},
 {"titulo":"La fórmula","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":2,"bloques":[EQ("A^{2}\\begin{pmatrix}1\\\\0\\end{pmatrix}=\\begin{pmatrix}5\\\\4\\end{pmatrix}"),P("La diagonalización lo da sin multiplicar la matriz por sí misma.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":2},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Una matriz es diagonalizable si tiene tantos vectores propios independientes como su tamaño."}]}]
preg={"tex":"\\text{matriz no diagonalizable}","encabezado":"¿Cuál de estas matrices NO es diagonalizable?","opciones":["$"+M(1,1,0,1)+"$","$"+M(2,0,0,3)+"$","$"+M(1,2,2,1)+"$","$"+M(0,1,1,0)+"$"],"correcta":0,
 "explicacion":"La primera tiene el valor propio 1 repetido y solo un vector propio independiente, el (1, 0), así que no se puede diagonalizar. La segunda ya es diagonal. La tercera y la cuarta son simétricas, con dos valores propios distintos, así que se diagonalizan.",
 "pistas":["Busca una matriz con un valor propio repetido.","La primera matriz tiene el valor propio 1 dos veces.","Mira cuántos vectores propios independientes tiene. Necesita 2."],
 "errores":["","Ya es diagonal. Una matriz diagonal es diagonalizable, con P igual a la identidad.","Es simétrica, con valores propios 3 y menos 1, distintos, así que se diagonaliza.","Es simétrica, con valores propios 1 y menos 1, distintos, así que se diagonaliza."]}
res=["Una matriz es diagonalizable si es P D P inversa, con las columnas de P siendo vectores propios.","Sus potencias son A a la n igual a P D a la n P inversa, y D a la n se calcula elevando su diagonal.","Si hay n valores propios distintos, es diagonalizable. Si faltan vectores propios independientes, no."]
write(lesson("alglin-m3-l2","Lección 2 de 4","Diagonalización",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal",ejercicios=4),"alglin-diagonalizacion.json")
