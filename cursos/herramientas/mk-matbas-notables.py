import os, math
os.environ['CURSO_FU']='Matemáticas Básicas'; os.environ['BANCO']='matbas'
from mklib import *
MOD="Módulo 1 Álgebra y expresiones"
TS=[-3.5+7.0*k/100 for k in range(101)]
graf={"tipo":"plano","x":[-3.5,3.5],"y":[-2.5,19],"a":0.5,"b":2.5,"inicio":1,
 "elementos":[{"t":"trazo","puntos":[[f"{t:.4f}",f"{t:.4f}*{t:.4f}+2*x*{t:.4f}"] for t in TS],"c":3,"guia":True},
  {"t":"trazo","puntos":[[f"{t:.4f}",f"({t:.4f}+x)*({t:.4f}+x)"] for t in TS],"c":2},
  {"t":"recta","p":["1","0"],"dir":["0","1"],"guion":True,"c":3},
  {"t":"punto","p":["1","(1+x)*(1+x)"],"c":1},
  {"t":"punto","p":["1","1+2*x"],"c":3,"guia":True}],
 "lecturas":[{"rotulo":"valor de h","formula":"x"},{"rotulo":"lo que falta, h al cuadrado","formula":"x*x"}],
 "etiquetas":["Valor de h","Distancia entre las curvas, h al cuadrado"],"etiquetaSlider":"Valor de h",
 "alt":"Las curvas x más h, al cuadrado, y x al cuadrado más 2h x. La distancia vertical entre las dos es siempre h al cuadrado, el término que falta"}
glos={"notable":"Un producto notable es un producto de polinomios que se puede escribir directo, sin multiplicar término a término, como el cuadrado de una suma.",
 "factorizar":"Factorizar es escribir una expresión como un producto de expresiones más simples. Es el camino contrario a los productos notables.",
 "trinomio":"Un trinomio cuadrado perfecto es una expresión de tres términos que es el cuadrado de un binomio, como x al cuadrado más 6x más 9."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"La curva grande es x más h, al cuadrado. La curva de apoyo es solo x al cuadrado más 2h por x."],
 [4,8,"Entre las dos hay una distancia fija. Se ve en x igual a 1, entre los dos puntos."],
 [8,14,"Al subir h, esa distancia crece. Es h al cuadrado, el término que falta. Por eso x más h, al cuadrado, no es x al cuadrado más h al cuadrado."],
 [14,18,"Con h igual a 2, la distancia es 4. Mira la lectura de abajo."],
 [18,22,"Con h igual a 1.5 la distancia es 2.25. El error más común es olvidar el término del medio, el doble producto."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[11,2.5],[13,2],[17,2],[18,1.5],[22,1.5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[18,22]}}
S=[
 sec("La idea",None,P("Los {{gl:notable|productos notables}} son atajos para multiplicar, y la {{gl:factorizar|factorización}} es usarlos al revés. Saber factorizar sirve para simplificar fracciones, resolver ecuaciones y hallar ceros. Casi todo se reduce a reconocer unos pocos patrones.")),
 sec("Un ejemplo","Un ejemplo",P("Mira el cuadrado de una suma. Falta algo si solo se elevan los términos al cuadrado."),EQ("(x+h)^{2}=x^{2}+2hx+h^{2}"),{"t":"grafica","animar":"dibujar","alt":"Las dos curvas"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"En x más 3, al cuadrado, el término del medio es 2 por x por 3. ¿Cuánto vale ese coeficiente de x?","opciones":[3,6,9,12],"correcta":6,"bien":"Muy bien. Es 6x. Más abajo se ve qué pasa si se olvida ese término.","mal":"Es 6, porque 2 por 3 es 6. Más abajo se ve qué pasa si se olvida ese término."}),
 sec("Lo que falta","Lo que falta",P("Mira cómo cambia la distancia entre las curvas al cambiar h."),{"t":"acercando","ds":[1,2,2.5,1.5],"alt":"La distancia para varios h"},P("La distancia entre las curvas es h al cuadrado. Es justo el término que se pierde si se olvida el doble producto, o si se dice que el cuadrado de una suma es la suma de los cuadrados.")),
 sec("Los productos notables","Productos",P("Estos son los patrones que más se usan."),
   PASOS([("(a+b)^{2}=a^{2}+2ab+b^{2},\\qquad (a-b)^{2}=a^{2}-2ab+b^{2}","El cuadrado de una suma o de una resta."),
          ("(a+b)(a-b)=a^{2}-b^{2}","La diferencia de cuadrados."),
          ("a^{3}-b^{3}=(a-b)\\left(a^{2}+ab+b^{2}\\right)","La diferencia de cubos."),
          ("(2x-3)^{2}=4x^{2}-12x+9","Un ejemplo, con a igual a 2x y b igual a 3.")])),
 sec("Factorizar","Factorizar",P("Para factorizar se prueban estos pasos, en este orden."),
   PASOS([("3x^{2}-12=3\\left(x^{2}-4\\right)=3(x-2)(x+2)","Primero el factor común, y después la diferencia de cuadrados."),
          ("x^{2}-9x+20=(x-4)(x-5)","Se buscan dos números que sumen menos 9 y multipliquen 20."),
          ("6x^{2}+x-2=(2x-1)(3x+2)","Con coeficiente distinto de 1 se prueban los factores de 6 y de menos 2.")]),
   OJO("Siempre se puede comprobar multiplicando. Si al multiplicar los factores no sale la expresión original, la factorización está mal.")),
 eng("Una placa que se dilata","Una placa cuadrada de acero se calienta y su lado crece un poco. El área nueva es el cuadrado de una suma, y el término h al cuadrado resulta tan pequeño que en la práctica se desprecia.","A=(L+\\Delta L)^{2}=L^{2}+2L\\,\\Delta L+\\Delta L^{2}",
   [("Lado","1 m"),("Aumento de lado","0.6 mm"),("Aumento de área","unos 12 cm²")],"Con 50 grados de aumento y un coeficiente de 12 millonésimas por grado, el lado crece 0.6 milímetros. El aumento de área es 2 por L por el aumento, o sea 12 centímetros cuadrados, más el término del cuadrado, que es 0.0036 centímetros cuadrados y pesa menos del 0.03 por ciento. Por eso en ingeniería se usa 2 L por el aumento. Es una aproximación válida para cambios pequeños."),
 completar("Se desarrolla el cuadrado de una resta.","(2x-3)^{2}=4x^{2}-12x+[[hueco]]",
   [("9","nueve"),("-9","menos nueve"),("6","seis")],0,
   ["","Al elevar menos 3 al cuadrado el signo se pierde, y queda positivo.","El 6 sería 2 por 3, que ya aparece en el término del medio, y no el cuadrado de 3."],"El último término es el cuadrado de 3.","Tres al cuadrado es 9, y es positivo."),
 error("Alguien factorizó x al cuadrado, menos 7x, más 12, y se equivocó en un paso. Toca el paso que está mal.",
   [("\\text{Dos números que suman}\\ -7\\ \\text{y multiplican}\\ 12","Lo que se busca.","se buscan dos números que sumen menos 7 y multipliquen 12"),
    ("\\text{Son}\\ -3\\ \\text{y}\\ -4","Los dos números.","son menos 3 y menos 4"),
    ("x^{2}-7x+12=(x-3)(x+4)","Este paso es el que falla.","queda x menos 3 por x más 4")],2,
   "Los números son menos 3 y menos 4, así que los factores son x menos 3 y x menos 4. Con x más 4 el término del medio sería x, no menos 7x.",
   "x^{2}-7x+12=(x-3)(x-4)","Compara los signos de los factores con los de los números."),
 ordenar("Estos son los pasos para factorizar 3x al cuadrado menos 12, pero están desordenados.",
   [("3x^{2}-12","La expresión original"),
    ("3\\left(x^{2}-4\\right)","Se saca factor común 3"),
    ("3\\left(x^{2}-2^{2}\\right)","Se reconoce una diferencia de cuadrados"),
    ("3(x-2)(x+2)","Se factoriza")],[2,0,3,1],
   "Se saca el factor común, se reconoce la diferencia de cuadrados y se factoriza.","Se empieza con la expresión original."),
]
S+=cierre("Mini simulacro de productos notables y factorización",[
 banco("mb_c1_06","El cuadrado de una resta da $a^2-2ab+b^2$, con $a=2x$ y $b=3$."),
 banco("mb_c1_07","Se buscan dos números que sumen $-9$ y multipliquen $20$, que son $-4$ y $-5$."),
 banco("mb_c1_10","Se prueban los factores de $6$ y de $-2$ hasta que el término del medio sea $x$.")])
prac=[
 {"titulo":"Las curvas","grafica":{"draw":1,"guide":1},"bloques":[P("El cuadrado de una suma y su aproximación sin el último término."),EQ("(x+h)^{2}\\ \\text{y}\\ x^{2}+2hx")]},
 {"titulo":"Cambia h","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. La distancia entre las curvas es h al cuadrado.")]},
 {"titulo":"Un valor","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1.5,"bloques":[EQ("h=1.5\\ \\Rightarrow\\ h^{2}=2.25"),P("Esa es la distancia entre las dos curvas.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Usa la fórmula de la diferencia de cubos."}]}]
preg={"tex":"x^{3}-27\\ \\text{se factoriza como}","opciones":["$(x-3)\\left(x^{2}+3x+9\\right)$","$(x-3)^{3}$","$(x-3)\\left(x^{2}-3x+9\\right)$","$(x-3)\\left(x^{2}+9\\right)$"],"correcta":0,
 "explicacion":"Es una diferencia de cubos, con a igual a x y b igual a 3. La fórmula es a menos b por a cuadrado, más ab, más b cuadrado. Queda x menos 3 por x cuadrado, más 3x, más 9.",
 "verificacion":{"formula":"(x-3)*(x*x+3*x+9)-(x*x*x-27)","a":2,"esperado":0},
 "pistas":["Es una diferencia de cubos, porque 27 es 3 al cubo.","La fórmula es a menos b por a cuadrado más ab más b cuadrado.","Todos los signos del segundo factor son positivos."],
 "errores":["","Al desarrollar x menos 3 al cubo salen cuatro términos con signos alternados, no x al cubo menos 27.","En la diferencia de cubos el término del medio del segundo factor es positivo. Con menos 3x sería una suma de cubos.","Al multiplicar eso no aparece el término de x al cuadrado que se cancela. Falta el término del medio."]}
res=["Los productos notables dan el desarrollo directo, como el cuadrado de una suma, la diferencia de cuadrados y la diferencia de cubos.","El cuadrado de una suma tiene el doble producto, y no es la suma de los cuadrados.","Para factorizar se saca factor común, se busca un producto notable y se prueba con dos números que sumen y multipliquen lo debido."]
write(lesson("mb-m1-l3","Lección 3 de 4","Productos notables y factorización",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=6,curso="Matemáticas Básicas"),"matbas-notables.json")
