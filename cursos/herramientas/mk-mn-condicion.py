import os, math
os.environ['CURSO_FU']='Métodos Numéricos'; os.environ['BANCO']='metnum'
from mklib import *
from fundlib import *
MOD="Módulo 2 Sistemas lineales e interpolación"
N=48
EL=[{"t":"trazo","puntos":[[f"{math.cos(2*math.pi*k/N):.5f}",f"{math.sin(2*math.pi*k/N):.5f}"] for k in range(N+1)],"c":0},
    {"t":"trazo","puntos":[[f"{2*math.cos(2*math.pi*k/N):.5f}",f"x*{math.sin(2*math.pi*k/N):.5f}"] for k in range(N+1)],"c":1},
    {"t":"punto","p":["2","0"],"c":3},{"t":"punto","p":["0","x"],"c":2}]
graf={"tipo":"plano","x":[-4.6,4.6],"y":[-2.5,2.5],"a":0.01,"b":2,"inicio":1,
 "elementos":EL,
 "lecturas":[{"rotulo":"semieje menor s de la elipse, el segundo valor de la diagonal de A","formula":"x"},{"rotulo":"número de condición, 2 entre s","formula":"2/x"}],
 "etiquetas":["Valor s en la matriz diagonal con 2 y s","Cociente entre el semieje mayor y el menor, igual al número de condición"],"etiquetaSlider":"Valor s, de 0.01 a 2",
 "alt":"La circunferencia unidad en azul, y en marrón la imagen de la circunferencia con la matriz diagonal de valores 2 y s. Es una elipse con semieje horizontal 2 y semieje vertical s. Al achicar s la elipse se aplasta, y el número de condición, 2 entre s, crece"}
glos={"norma":"Una norma mide el tamaño de un vector o de una matriz. La euclidiana de un vector es la raíz de la suma de los cuadrados de sus componentes.",
 "infinito":"La norma infinito de una matriz es la mayor suma de valores absolutos de los elementos de una fila.",
 "condicion":"El número de condición de una matriz es la norma de A por la norma de su inversa. Mide cuánto se amplifican los errores al resolver Ax igual a b.",
 "malcond":"Un sistema mal condicionado tiene un número de condición grande, y pequeñas perturbaciones en los datos producen grandes cambios en la solución."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La circunferencia unidad, en azul, se transforma con la matriz diagonal de 2 y s. El resultado es una elipse con semiejes 2 y s."],
 [4,10,"Cuando s vale 1, la elipse es casi redonda y el número de condición es 2."],
 [10,16,"Al achicar s, la elipse se aplasta. Con s igual a 0.1, el número de condición es 20."],
 [16,21,"Con s igual a 0.01 es 200. La matriz casi no distingue ciertas direcciones."],
 [21,24,"Un número de condición grande indica un sistema mal condicionado."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[11,0.1],[16,0.1],[17,0.01],[24,0.01]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[16,24]}}
S=[
 sec("La idea",None,P("Una {{gl:norma|norma}} da el tamaño de un vector o de una matriz. Con ellas se define el {{gl:condicion|número de condición}}, que mide cuánto se amplifican los errores al resolver un sistema. Un sistema con número de condición grande está {{gl:malcond|mal condicionado}}, y su solución cambia mucho con datos casi iguales. La norma {{gl:infinito|infinito}} de una matriz es la mayor suma de valores absolutos por fila.")),
 sec("Un ejemplo","Un ejemplo",P("La matriz diagonal con 2 y s transforma la circunferencia unidad en una elipse. Mueve s y mira cómo se aplasta."),EQ("\\kappa(A)=\\|A\\|\\,\\|A^{-1}\\|=\\dfrac{2}{s}"),{"t":"grafica","animar":"dibujar","alt":"La elipse que forma la matriz"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"La matriz diagonal con 2 y 0.01 estira 2 veces en una dirección y 0.01 veces en la otra. ¿Cuánto vale la razón entre el mayor estiramiento y el menor?","opciones":[2,20,100,200],"correcta":200,"bien":"Muy bien. Es 2 entre 0.01, o sea 200, y es el número de condición. Más abajo se ve la elipse aplastada.","mal":"Es 200, porque 2 entre 0.01 da 200. Ese es el número de condición. Más abajo se ve la elipse aplastada."}),
 sec("Aplastando la elipse","La elipse",P("Mira la elipse con s igual a 2, 1, 0.1 y 0.01."),{"t":"acercando","ds":[2,1,0.1,0.01],"alt":"La elipse con cuatro valores de s"},P("Con s igual a 2 la elipse es una circunferencia y el número de condición es 1. Con 0.01 queda casi un segmento.")),
 sec("Normas","Normas",P("Hay normas de vectores y normas de matrices."),
   PASOS([("\\|(3,-4)\\|_{2}=\\sqrt{9+16}=5","La norma euclidiana de un vector."),
          ("\\|A\\|_{\\infty}=\\max_{i}\\sum_{j}|a_{ij}|","La norma infinito, la mayor suma por filas."),
          ("A=\\begin{pmatrix}2&0\\\\0&0.01\\end{pmatrix}:\\ \\|A\\|_{\\infty}=2","Para la matriz del ejemplo."),
          ("\\|A^{-1}\\|_{\\infty}=100","La inversa es la diagonal de 0.5 y 100.")])),
 sec("El número de condición","Condición",P("El número de condición combina la norma de la matriz con la de su inversa."),
   PASOS([("\\kappa_{\\infty}(A)=\\|A\\|_{\\infty}\\,\\|A^{-1}\\|_{\\infty}=2\\cdot100=200","El número de condición del ejemplo."),
          ("\\dfrac{\\|\\delta x\\|}{\\|x\\|}\\le\\kappa(A)\\,\\dfrac{\\|\\delta b\\|}{\\|b\\|}","El error relativo en la solución, como máximo kappa veces el del dato."),
          ("\\kappa(A)\\ \\text{grande}\\ \\Rightarrow\\ \\text{mal condicionado}","Los errores pequeños en los datos pueden dar errores grandes en la solución.")]),
   OJO("El número de condición no depende del método, sino del problema. Un buen algoritmo no arregla un sistema mal condicionado. Solo mejores datos o una reformulación lo hacen.")),
 eng("Un sistema que amplifica el error","Se calibra un sensor con un sistema lineal cuyo número de condición es 200. Los datos tienen un error de 0.1 por ciento. En el peor caso, la solución, que son los coeficientes de calibración, puede tener un error de 200 veces eso.","\\dfrac{\\|\\delta x\\|}{\\|x\\|}\\le200\\cdot0.1\\%=20\\%",
   [("Número de condición","200"),("Error en los datos","0.1 %"),("Error posible en la solución","hasta 20 %")],"Un error de 20 por ciento en la calibración sería inaceptable. Es una cota de peor caso, y el error real puede ser menor, pero es una advertencia. Para reducirlo se escogen mejores puntos de calibración, se escala el problema o se usan más datos con mínimos cuadrados."),
 completar("Se calcula la norma infinito de la inversa de la matriz diagonal con 2 y 0.01. Falta el valor.","\\|A^{-1}\\|_{\\infty}=\\dfrac{1}{0.01}=[[hueco]]",
   [("100","cien"),("0.01","un centésimo"),("2","dos")],0,
   ["","Cero coma cero uno es el elemento de A. La inversa tiene el recíproco.","Dos es la norma de A, y la inversa tiene el recíproco de 0.01."],"La inversa de una diagonal invierte cada elemento.","1 entre 0.01 es 100."),
 error("Alguien calculó el número de condición de la matriz diagonal con 2 y 0.01 y se equivocó en un paso. Toca el paso que está mal.",
   [("\\|A\\|_{\\infty}=2","La norma de A.","la norma de A es 2"),
    ("\\|A^{-1}\\|_{\\infty}=100","La norma de la inversa.","la norma de la inversa es 100"),
    ("\\kappa=\\dfrac{2}{100}=0.02","Este paso es el que falla.","el número de condición es el cociente")],2,
   "El número de condición es el producto de las dos normas, y no el cociente. El valor es 2 por 100, o sea 200.",
   "\\kappa=2\\cdot100=200","Recuerda la definición del número de condición."),
 ordenar("Estos son los pasos para calcular el número de condición de la matriz diagonal con 2 y 0.01, pero están desordenados.",
   [("A=\\operatorname{diag}(2,\\ 0.01)","Se parte de la matriz"),
    ("\\|A\\|_{\\infty}=2","Se calcula la norma de A"),
    ("\\|A^{-1}\\|_{\\infty}=100","Se calcula la norma de la inversa"),
    ("\\kappa=2\\cdot100=200","Se multiplican")],[2,0,3,1],
   "Se calcula la norma de A, la de su inversa y se multiplican.","Se empieza con la matriz."),
]
S+=cierre("Mini simulacro de normas y número de condición",[
 banco("mn_c2_10","La norma infinito es la mayor suma de valores absolutos por fila, que aquí es 2."),
 banco("mn_c2_11","$\\kappa_{\\infty}=2\\cdot100=200$."),
 banco("mn_c2_12","Un número de condición grande indica un sistema mal condicionado.")])
prac=[
 {"titulo":"La elipse","grafica":{"draw":1},"bloques":[P("La imagen de la circunferencia unidad con la matriz diagonal."),EQ("A=\\operatorname{diag}(2,\\ s)")]},
 {"titulo":"Cambia s","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen s y el número de condición.")]},
 {"titulo":"Mal condicionado","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":0.01,"bloques":[EQ("\\kappa=\\dfrac{2}{0.01}=200"),P("Con s igual a 0.01 el número de condición es 200.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":0.01},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Suma los valores absolutos de cada fila y toma la mayor."}]}]
preg={"tex":"\\|A\\|_{\\infty}\\ \\text{de}\\ A=\\begin{pmatrix}1&-2\\\\3&4\\end{pmatrix}","opciones":["$7$","$3$","$10$","$5$"],"correcta":0,
 "explicacion":"La suma de los valores absolutos de la primera fila es 1 más 2, o sea 3. La de la segunda fila es 3 más 4, o sea 7. La norma infinito es la mayor de las dos, o sea 7.",
 "verificacion":{"formula":"7+0*x","a":0,"esperado":7},
 "pistas":["Suma los valores absolutos de cada fila.","Son 3 y 7.","Se toma la mayor."],
 "errores":["","Tres es la suma de la primera fila, pero la segunda es mayor.","Diez es la suma de todos los valores absolutos, y no la mayor por fila.","Cinco no corresponde a ninguna suma de fila."]}
res=["La norma infinito de una matriz es la mayor suma de valores absolutos por fila.","El número de condición es la norma de A por la norma de su inversa, y mide la amplificación de los errores.","Un número de condición grande indica un sistema mal condicionado, y ningún método lo corrige."]
write(lesson("mn-m2-l3","Lección 3 de 4","Normas y número de condición",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Métodos Numéricos"),"mn-condicion.json")
