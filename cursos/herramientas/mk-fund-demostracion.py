import os
os.environ['CURSO_FU']='Fundamentos de Matemáticas'; os.environ['BANCO']='fundamentos'
from mklib import *
from fundlib import *
MOD="Módulo 2 Demostración y conjuntos"
F="x*x+x+41"
EL=[{"t":"trazo","puntos":[[str(n),F.replace("x",str(n))] for n in range(0,41)],"c":0},
 {"t":"recta","p":["0","1681"],"dir":["1","0"],"guion":True,"c":3,"guia":True},
 {"t":"punto","p":["40","1681"],"c":1},
 {"t":"segmento","a":["x","0"],"b":["x",F],"c":1,"guia":True,"guion":True},
 {"t":"punto","p":["x",F],"c":2}]
graf={"tipo":"plano","x":[-4,44],"y":[-200,1900],"a":0,"b":40,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"n al cuadrado más n más 41","formula":F},{"rotulo":"ese valor dividido entre 41","formula":"("+F+")/41"}],
 "etiquetas":["Valor de la expresión para ese n","Cociente entre 41, es un entero cuando 41 divide al valor"],"etiquetaSlider":"Valor de n, de 0 a 40",
 "alt":"La curva de n al cuadrado más n más 41 para n de 0 a 40. Los valores son primos hasta n igual a 39. Con n igual a 40 el valor es 1681, que es 41 por 41, y no es primo"}
glos={"directa":"En una demostración directa se parte de las hipótesis y se llega a la conclusión con pasos lógicos.",
 "contrarrecproca":"La contrarrecíproca de p implica q es no q implica no p. Son equivalentes, así que probar una prueba la otra.",
 "contradiccion":"En una demostración por contradicción se supone que la conclusión es falsa y se llega a algo imposible.",
 "contraejemplo":"Un contraejemplo es un caso que cumple las hipótesis y no cumple la conclusión. Basta uno para refutar un para todo."}
ver={"duracion":24.0,"capitulos":[
 [0,5,"Se afirma que n al cuadrado más n más 41 es primo para todo entero n. Con n igual a 0 da 41, que es primo."],
 [5,11,"Sube n. Para 10, para 20, para 39, siempre da un número primo. Son cuarenta casos que cumplen la afirmación."],
 [11,17,"Pero con n igual a 40 el valor es 1681. Dividido entre 41 da 41, así que 1681 es 41 por 41 y no es primo."],
 [17,21,"Ese solo caso es un contraejemplo, y la afirmación para todo n es falsa."],
 [21,24,"Cuarenta casos buenos no prueban un para todo, pero un solo caso malo lo refuta."]],
 "canales":{"draw":[[0.3,0],[4.5,1]],"d":[[5,0],[6,0],[8,10],[9,10],[10,39],[11,39],[12,40],[24,40]],"guide":[[5,0],[6,1]]},
 "intervalos":{"ok":[17,24]}}
S=[
 sec("La idea",None,P("Demostrar es mostrar que una afirmación vale siempre, con argumentos que no admiten excepciones. Hay cuatro caminos principales. La {{gl:directa|demostración directa}} parte de las hipótesis. La {{gl:contrarrecproca|contrarrecíproca}} prueba no q implica no p. La {{gl:contradiccion|contradicción}} supone lo contrario y llega a un absurdo. Y un {{gl:contraejemplo|contraejemplo}} refuta una afirmación con un solo caso.")),
 sec("Un ejemplo","Un ejemplo",P("Esta expresión da números primos para muchos valores de n. Mira qué pasa al recorrerlos."),EQ("n^{2}+n+41\\ \\text{es primo para todo entero}\\ n\\ge0"),{"t":"grafica","animar":"dibujar","alt":"La curva de la expresión para n entre 0 y 40"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Una afirmación para todo n se cumple en los 40 primeros casos. ¿Cuántos casos que fallen se necesitan para refutarla?","opciones":[1,2,40,41],"correcta":1,"bien":"Muy bien. Basta uno. Más abajo se ve el caso que la rompe.","mal":"Basta uno. Un solo caso que falle refuta un para todo, sin importar cuántos casos buenos haya. Más abajo se ve el caso que la rompe."}),
 sec("Recorriendo los valores de n","Valores de n",P("Mira el valor de la expresión para n igual a 0, 10, 39 y 40."),{"t":"acercando","ds":[0,10,39,40],"alt":"La expresión para cuatro valores de n"},P("Hasta n igual a 39 todos los valores son primos. Con n igual a 40 da 1681, que es 41 por 41.")),
 sec("Los cuatro métodos","Métodos",P("Cada método se elige según la forma de la afirmación."),
   PASOS([("a\\mid b,\\ a\\mid c\\ \\Rightarrow\\ b=ak,\\ c=am\\ \\Rightarrow\\ b+c=a(k+m)","Directa. Se parte de lo que se sabe y se llega a que a divide a b más c."),
          ("n^{2}\\ \\text{impar}\\Rightarrow n\\ \\text{impar}\\ \\equiv\\ n\\ \\text{par}\\Rightarrow n^{2}\\ \\text{par}","Contrarrecíproca. Es más fácil, porque n igual a 2k da n al cuadrado igual a 2 por 2k al cuadrado."),
          ("\\sqrt2=\\dfrac pq\\ \\Rightarrow\\ p^{2}=2q^{2}\\ \\Rightarrow\\ p\\ \\text{y}\\ q\\ \\text{pares}","Contradicción. Se supone que la raíz de 2 es racional y reducida, y se llega a que p y q son pares."),
          ("\\exists n\\ \\neg P(n)","Contraejemplo. Un solo caso que falle refuta un para todo.")]),
   OJO("Probar con ejemplos no demuestra un para todo. Sirve para intuir, pero la demostración necesita un argumento que cubra todos los casos.")),
 sec("Cuándo usar cada uno","Cuándo usarlos",P("La forma de la afirmación orienta la elección."),
   PASOS([("p\\Rightarrow q\\ \\text{con una cuenta directa}","Se usa la demostración directa."),
          ("p\\Rightarrow q\\ \\text{cuando}\\ \\neg q\\ \\text{da más información}","Se usa la contrarrecíproca."),
          ("\\text{la conclusión niega algo, como irracional o infinito}","Se usa la contradicción."),
          ("\\forall x\\ P(x)\\ \\text{que parece falsa}","Se busca un contraejemplo.")]),
   OJO("Un condicional con hipótesis imposible es verdadero por vacuidad. Por ejemplo, si n es par e impar a la vez, entonces n al cuadrado es igual a menos 1. La hipótesis nunca se cumple, así que la afirmación es verdadera sin comprobar nada más.")),
 eng("Probar un programa con casos de prueba","Un ingeniero de software prueba una función con 40 casos y todos pasan. Eso no demuestra que la función sea correcta para todas las entradas. Basta un caso límite que falle para refutarla, igual que n igual a 40 refuta la expresión de este módulo.","40^{2}+40+41=41^{2}",
   [("Casos que pasan","40"),("Casos que fallan y bastan para refutar","1"),("Primer caso que falla","n = 40")],"Por eso en ingeniería se prueban los valores límite y los casos raros, y para las partes críticas se pasa de probar casos a demostrar. Un conjunto de casos buenos da confianza, pero solo una demostración cubre todas las entradas, y un contraejemplo basta para tirar abajo una afirmación general."),
 completar("Se prueba por contrarrecíproca que si n al cuadrado es impar, entonces n es impar. Falta la hipótesis de la contrarrecíproca.","n\\ \\text{es}\\ [[hueco]]\\ \\Rightarrow\\ n^{2}\\ \\text{es par}",
   [("\\text{par}","par"),("\\text{impar}","impar"),("\\text{primo}","primo")],0,
   ["","La contrarrecíproca niega la conclusión, y la conclusión original era que n es impar. Su negación es par.","Primo no es lo contrario de impar, así que no corresponde."],"Se niega la conclusión original, que era n impar.","La contrarrecíproca parte de n par y llega a n al cuadrado par."),
 error("Alguien probó por contradicción que la raíz de 2 es irracional y se equivocó en un paso. Toca el primer paso donde aparece el error.",
   [("\\sqrt2=\\dfrac pq\\ \\text{reducida}","Se supone lo contrario.","se supone que es racional"),
    ("p^{2}=2q^{2}","Se eleva al cuadrado.","p al cuadrado es el doble de q al cuadrado"),
    ("\\text{Entonces}\\ p\\ \\text{es impar}","Este paso es el que falla.","queda p impar")],2,
   "De p al cuadrado igual a 2 q al cuadrado, p al cuadrado es par, y un cuadrado par solo viene de un número par. Entonces p es par. Con p igual a 2r queda q al cuadrado igual a 2r al cuadrado, y q también es par, lo que contradice que la fracción esté reducida.",
   "p^{2}=2q^{2}\\Rightarrow p^{2}\\ \\text{par}\\Rightarrow p\\ \\text{par}","Un cuadrado par solo viene de un número par."),
 ordenar("Estos son los pasos de una demostración por contradicción, pero están desordenados.",
   [("\\neg C","Se supone lo contrario de la conclusión"),
    ("\\text{se razona con las hipótesis}","Se deducen consecuencias"),
    ("\\bot","Se llega a una contradicción"),
    ("C","Se concluye que lo supuesto era falso y vale la conclusión")],[2,0,3,1],
   "Se supone lo contrario, se razona, se llega a algo imposible y se concluye.","Se empieza negando la conclusión."),
]
S+=cierre("Mini simulacro de métodos de demostración",[
 banco("fu_c2_01","La contrarrecíproca es una cuenta de una línea, que n par da n al cuadrado par."),
 banco("fu_c2_02","Negar un para todo requiere un solo caso que falle."),
 banco("fu_c2_03","Se niega la conclusión, o sea, se supone que la raíz de 2 es racional y reducida.")])
prac=[
 {"titulo":"La afirmación","grafica":{"draw":1,"guide":1},"bloques":[P("La expresión n al cuadrado más n más 41 para n de 0 a 40."),EQ("n^{2}+n+41")]},
 {"titulo":"Recorre n","grafica":{"draw":1,"guide":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 40. Abajo se lee el valor de la expresión y su cociente entre 41.")]},
 {"titulo":"El contraejemplo","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":40,"bloques":[EQ("40^{2}+40+41=41^{2}=1681"),P("Con n igual a 40 el valor es 41 por 41, y no es primo.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":40},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Recuerda cuántos casos que fallen bastan para refutar un para todo."}]}]
preg={"tex":"\\text{Para refutar}\\ \\forall n\\ (n^{2}+n+41\\ \\text{es primo})\\ \\text{basta}","opciones":["el caso $n=40$, que da $41^{2}$","probarlo para $n=0,1,2$","una demostración por inducción","negar la afirmación sin dar un caso"],"correcta":0,
 "explicacion":"Un solo caso que falle refuta un para todo. Con n igual a 40 el valor es 1681, que es 41 por 41 y no es primo. Que se cumpla en 40 casos no demuestra nada.",
 "verificacion":{"formula":"1-(1-0)*1+0*x","a":0,"esperado":0},
 "pistas":["Se necesita un caso que falle.","Prueba con n igual a 40.","Da 41 por 41."],
 "errores":["","Esos casos cumplen la afirmación, y no la refutan.","La inducción sirve para probar, y esta afirmación es falsa.","Hace falta mostrar un caso concreto, y no solo negarla."]}
res=["Las demostraciones pueden ser directas, por contrarrecíproca, por contradicción o con un contraejemplo.","Un solo contraejemplo refuta un para todo, y muchos casos buenos no lo prueban.","La forma de la afirmación orienta qué método usar."]
write(lesson("fu-m2-l1","Lección 1 de 4","Métodos de demostración",30,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Fundamentos de Matemáticas"),"fund-demostracion.json")
