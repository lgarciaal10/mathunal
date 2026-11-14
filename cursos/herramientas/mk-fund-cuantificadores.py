import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 1 Lógica y argumentación"
W=1.2
EL=[]
for n in range(1,6):
    xa=(n-1)*W; xb=n*W
    EL.append({"t":"poligono","puntos":[[str(xa),"1.3"],[str(xb),"1.3"],[str(xb),"2.4"],[str(xa),"2.4"]],"c":0,"nombre":str(n)})
    vals=[1 if n>k else 0 for k in range(6)]
    L=lagr(vals)
    EL.append({"t":"poligono","puntos":[[str(xa),"0"],[str(xb),"0"],[str(xb),f"1.2*({L})"],[str(xa),f"1.2*({L})"]],"c":3})
    EL.append({"t":"poligono","puntos":[[str(xa),f"1.2*({L})"],[str(xb),f"1.2*({L})"],[str(xb),"1.2"],[str(xa),"1.2"]],"c":1})
TODO=lagr([1,0,0,0,0,0]); EXISTE=lagr([1,1,1,1,1,0])
graf={"tipo":"plano","x":[-0.3,6.3],"y":[-0.6,3.0],"a":0,"b":5,"inicio":0,"entero":True,"sinejes":True,"elementos":EL,
 "lecturas":[{"rotulo":"para todo x, x es mayor que k (1 si es cierto)","formula":TODO},{"rotulo":"existe un x mayor que k (1 si es cierto)","formula":EXISTE}],
 "etiquetas":["Valor de la afirmación para todo, 1 si es verdadera","Valor de la afirmación existe, 1 si es verdadera"],"etiquetaSlider":"Valor de k, de 0 a 5",
 "alt":"Cinco casillas numeradas del 1 al 5 que representan el universo. Cada casilla es verde si el número es mayor que k y roja si no lo es. Al subir k las casillas pasan de verdes a rojas, empezando por el 1"}
glos={"predicado":"Un predicado es una afirmación con una variable, como x es mayor que 3. No es verdadera ni falsa hasta que se da un valor a x o se cuantifica.",
 "universo":"El universo es el conjunto de valores que puede tomar la variable. Una afirmación con cuantificadores siempre se lee dentro de un universo.",
 "universal":"El cuantificador universal, para todo, se escribe con una A al revés. La afirmación es verdadera solo si se cumple para cada elemento del universo.",
 "existencial":"El cuantificador existencial, existe, se escribe con una E al revés. La afirmación es verdadera si se cumple para al menos un elemento."}
ver={"duracion":23.0,"capitulos":[
 [0,4,"El universo son los números del 1 al 5 y la afirmación es x mayor que k. Una casilla verde cumple la afirmación y una roja no."],
 [4,9,"Con k igual a 0, las cinco casillas son verdes. Para todo x se cumple, y por supuesto también existe uno que cumple."],
 [9,15,"Sube k a 1. La casilla del 1 se vuelve roja. Para todo deja de ser verdad, pero existe sigue siéndolo."],
 [15,19,"Con k igual a 4 queda una sola casilla verde, y con k igual a 5 ninguna. Existe solo se vuelve falso cuando todas son rojas."],
 [19,23,"Basta una casilla roja para romper un para todo, y basta una verde para que un existe sea verdadero."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[9,0],[10,1],[15,1],[16,4],[18,5],[19,5],[23,5]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[19,23]}}
S=[
 sec("La idea",None,P("Una afirmación como x es mayor que 3 no es verdadera ni falsa, porque depende de x. Se llama {{gl:predicado|predicado}}. Para convertirla en una proposición se le pone un cuantificador, que dice sobre cuántos elementos del {{gl:universo|universo}} se afirma. El {{gl:universal|universal}} dice para todos y el {{gl:existencial|existencial}} dice para al menos uno.")),
 sec("Un ejemplo","Un ejemplo",P("Mira las cinco casillas del universo. Cada una es verde si el número cumple la afirmación y roja si no."),EQ("\\forall x\\in\\{1,\\dots,5\\}\\ (x>k)\\qquad\\exists x\\in\\{1,\\dots,5\\}\\ (x>k)"),{"t":"grafica","animar":"dibujar","alt":"Las cinco casillas del universo"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Se afirma que para todo x del universo se cumple una propiedad. ¿Cuántos casos que no la cumplan bastan para que esa afirmación sea falsa?","opciones":[1,2,3,5],"correcta":1,"bien":"Muy bien. Un solo caso que falle es suficiente. Eso se ve más abajo con las casillas.","mal":"Basta con uno. Si un solo elemento falla, ya no se cumple para todos. Eso se ve más abajo con las casillas."}),
 sec("Recorriendo los valores de k","Valores de k",P("Mira las casillas y las dos lecturas cuando k vale 0, 1, 4 y 5."),{"t":"acercando","ds":[0,1,4,5],"alt":"Las casillas para cuatro valores de k"},P("Con k igual a 0 todo es verdad. Con k igual a 1 deja de cumplirse para todo, pero existe sigue valiendo. Solo con k igual a 5 desaparece también el existe.")),
 sec("Cómo se niegan","Negación",P("Negar una afirmación cuantificada cambia el cuantificador y niega el predicado."),
   PASOS([("\\neg\\forall x\\,P(x)\\ \\equiv\\ \\exists x\\,\\neg P(x)","No es cierto que todos cumplan, o sea, alguno no cumple."),
          ("\\neg\\exists x\\,P(x)\\ \\equiv\\ \\forall x\\,\\neg P(x)","No es cierto que alguno cumpla, o sea, todos fallan."),
          ("\\neg\\forall x\\,\\big(P(x)\\rightarrow Q(x)\\big)\\equiv\\exists x\\,\\big(P(x)\\wedge\\neg Q(x)\\big)","Se combinan las dos reglas, la del cuantificador y la del condicional.")]),
   OJO("La negación de todos aprobaron no es ninguno aprobó. Es alguno no aprobó. Para romper un para todo basta un caso.")),
 sec("El orden importa","El orden",P("Cuando hay dos cuantificadores, el orden cambia el significado."),
   PASOS([("\\forall x\\,\\exists y\\ (y>x)","Para cada número hay otro mayor. Es verdadera en los enteros."),
          ("\\exists y\\,\\forall x\\ (y>x)","Hay un número mayor que todos. Es falsa en los enteros."),
          ("\\exists x\\,\\forall y\\ \\neg(x<y)\\ \\text{equivale a}\\ \\neg\\forall x\\,\\exists y\\ (x<y)","Para negar varios cuantificadores se cambia cada uno y se niega el predicado al final.")]),
   OJO("Los cuantificadores de distinto tipo no se pueden intercambiar. Para cada x existe un y no dice lo mismo que existe un y que sirve para todo x.")),
 eng("El control de calidad de un lote","Un lote de cinco piezas se aprueba solo si todas están dentro de tolerancia. Esa regla es un para todo. Se rechaza si existe al menos una pieza fuera de tolerancia, que es su negación.","\\text{aprobado}=\\forall i\\,P(i)",
   [("Piezas del lote","5"),("Piezas fuera de tolerancia que bastan para rechazar","1"),("Piezas que hay que medir para aprobar","las 5")],"Aprobar exige medir las cinco piezas, y rechazar puede ocurrir con la primera que falle. Por eso en control de calidad se diseña la inspección para encontrar un contraejemplo, y no para sumar casos buenos. Treinta piezas buenas no prueban un para todo, pero una mala basta para negarlo."),
 completar("Se niega un para todo. Falta el cuantificador del resultado.","\\neg\\forall x\\,P(x)\\ \\equiv\\ [[hueco]]\\,x\\ \\neg P(x)",
   [("\\exists","existe"),("\\forall","para todo"),("\\neg\\exists","no existe")],0,
   ["","Con para todo se mantiene el cuantificador. La negación debe cambiarlo.","Con no existe el resultado dice que ninguno falla, y es lo contrario de lo que se quiere."],"Negar un para todo es decir que alguno falla.","La negación de para todo es existe uno que no cumple."),
 error("Alguien negó la afirmación de que todos los lotes pasaron la prueba y se equivocó en un paso. Toca el paso que está mal.",
   [("\\forall x\\,P(x)","Todos pasaron.","todos los lotes pasaron"),
    ("\\neg\\forall x\\,P(x)","Se niega la afirmación.","se niega"),
    ("\\text{Entonces}\\ \\forall x\\,\\neg P(x)","Este paso es el que falla.","queda que todos fallaron")],2,
   "Negar un para todo no da otro para todo. Que ninguno pase es mucho más fuerte que decir que no todos pasaron. La negación correcta dice que existe al menos uno que no pasó.",
   "\\neg\\forall x\\,P(x)\\equiv\\exists x\\,\\neg P(x)","Pregúntate si hace falta que fallen todos para romper un para todo."),
 ordenar("Estos son los pasos para negar la afirmación para todo x existe y con x menor que y, pero están desordenados.",
   [("\\neg\\forall x\\,\\exists y\\ (x<y)","Se escribe la negación"),
    ("\\exists x\\,\\neg\\exists y\\ (x<y)","Se pasa la negación al primer cuantificador"),
    ("\\exists x\\,\\forall y\\ \\neg(x<y)","Se pasa la negación al segundo"),
    ("\\exists x\\,\\forall y\\ (x\\ge y)","Se niega el predicado")],[2,0,3,1],
   "Cada cuantificador se cambia de afuera hacia adentro, y al final se niega el predicado.","Se empieza escribiendo la negación completa."),
]
S+=cierre("Mini simulacro de cuantificadores y predicados",[
 banco("fu_c1_10","Al negar un para todo, aparece un existe y se niega el predicado."),
 banco("fu_c1_13","La negación de existe es para todo con el predicado negado, es decir, ninguno."),
 banco("fu_c1_14","Ningún x cumple R significa que para todo x se cumple no R.")])
prac=[
 {"titulo":"El universo","grafica":{"draw":1,"guide":1},"bloques":[P("Las cinco casillas del universo, verdes si cumplen x mayor que k."),EQ("x>k")]},
 {"titulo":"Recorre k","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 5. Abajo se leen los valores de para todo y de existe.")]},
 {"titulo":"Una casilla roja","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("k=1\\ \\Rightarrow\\ \\forall\\ \\text{falso},\\ \\exists\\ \\text{verdadero}"),P("Con k igual a 1 hay una casilla roja. Eso rompe el para todo, pero no el existe.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Recuerda qué cambia al negar un cuantificador."}]}]
preg={"tex":"\\text{La negación de}\\ \\exists x\\,P(x)\\ \\text{es}","opciones":["$\\forall x\\,\\neg P(x)$","$\\exists x\\,\\neg P(x)$","$\\neg\\forall x\\,P(x)$","$\\forall x\\,P(x)$"],"correcta":0,
 "explicacion":"Negar existe da para todo con el predicado negado. Decir que no existe ninguno que cumpla es lo mismo que decir que todos fallan.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Hay que cambiar el cuantificador.","También se niega el predicado.","Queda para todo x, no P de x."],
 "errores":["","Esa dice que alguno falla, y no es la negación. Cambia el predicado pero deja el cuantificador.","Esa es la negación de para todo, no la de existe.","Esa afirma que todos cumplen, y es otra afirmación distinta."]}
res=["Un predicado se vuelve proposición con un cuantificador, para todo o existe, dentro de un universo.","Para romper un para todo basta un caso que falle, y para probar un existe basta un caso que cumpla.","Al negar se cambia el cuantificador y se niega el predicado. El orden de cuantificadores distintos no se puede intercambiar."]
write(lesson("fu-m1-l2","Lección 2 de 3","Cuantificadores y predicados",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-cuantificadores.json")
