import os, math
os.environ['CURSO_FU']='Matemáticas Discretas'; os.environ['BANCO']='discretas'
from mklib import *
from fundlib import *
MOD="Módulo 3 Recurrencias, grafos y teoría de números"
A=[48,18,12,6]; B=[18,12,6,0]
LA=lagr(A); LB=lagr(B)
EL=[{"t":"poligono","puntos":[["0","1.6"],[LA,"1.6"],[LA,"2.6"],["0","2.6"]],"c":0},
    {"t":"poligono","puntos":[["0","0.2"],[LB,"0.2"],[LB,"1.2"],["0","1.2"]],"c":3}]
graf={"tipo":"plano","x":[-4.0,52.0],"y":[-1.0,3.6],"a":0,"b":3,"inicio":0,"entero":True,"elementos":EL,
 "lecturas":[{"rotulo":"a, el número mayor, la barra de arriba","formula":"("+LA+")"},{"rotulo":"b, el menor, la barra de abajo","formula":"("+LB+")"}],
 "etiquetas":["En cada paso, a pasa a ser el b anterior","En cada paso, b pasa a ser el residuo de dividir a entre b. Cuando vale 0, a es el máximo común divisor"],"etiquetaSlider":"Paso del algoritmo, de 0 a 3",
 "alt":"Dos barras que muestran los números del algoritmo de Euclides para 48 y 18. En el paso 0 miden 48 y 18, luego 18 y 12, luego 12 y 6, y en el paso 3 miden 6 y 0. Cuando la barra de abajo desaparece, la de arriba es el máximo común divisor, 6"}
glos={"modulo":"a mod n es el residuo de dividir a entre n. Por ejemplo, 17 mod 5 es 2.",
 "congruencia":"Dos enteros son congruentes módulo n si dejan el mismo residuo al dividir entre n, o sea, si n divide a su diferencia.",
 "mcd":"El máximo común divisor de a y b es el mayor entero que divide a los dos.",
 "euclides":"El algoritmo de Euclides halla el máximo común divisor con divisiones sucesivas. Se reemplaza el par a, b por el par b, a mod b hasta que el segundo valga 0."}
ver={"duracion":22.0,"capitulos":[
 [0,4,"Para hallar el máximo común divisor de 48 y 18, se divide el mayor entre el menor y se queda con el residuo."],
 [4,9,"48 entre 18 deja residuo 12. Ahora los números son 18 y 12."],
 [9,14,"18 entre 12 deja residuo 6. Ahora son 12 y 6."],
 [14,19,"12 entre 6 deja residuo 0. Cuando el residuo es 0, el máximo común divisor es el último divisor, o sea 6."],
 [19,22,"El algoritmo funciona porque el máximo común divisor de a y b es el mismo que el de b y el residuo."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,0],[6,0],[8,1],[11,2],[15,3],[22,3]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[14,22]}}
S=[
 sec("La idea",None,P("La aritmética {{gl:modulo|modular}} trabaja con residuos. Dos enteros son {{gl:congruencia|congruentes}} módulo n si dejan el mismo residuo. Para hallar el {{gl:mcd|máximo común divisor}} de dos números se usa el algoritmo de {{gl:euclides|Euclides}}, que reemplaza el par a, b por b y el residuo de a entre b, hasta llegar a cero.")),
 sec("Un ejemplo","Un ejemplo",P("Mira el algoritmo de Euclides con 48 y 18. Mueve el paso y observa cómo se achican los números."),EQ("\\operatorname{mcd}(a,b)=\\operatorname{mcd}(b,\\ a\\bmod b)"),{"t":"grafica","animar":"dibujar","alt":"Las barras del algoritmo de Euclides"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Al dividir 48 entre 18, el cociente es 2 y sobran 12. ¿Cuánto vale el residuo?","opciones":[6,12,18,30],"correcta":12,"bien":"Muy bien. Es 48 menos 2 por 18, o sea 12. Más abajo se ve en el paso 1.","mal":"Es 12, porque 2 por 18 es 36 y 48 menos 36 es 12. Más abajo se ve en el paso 1."}),
 sec("Los pasos del algoritmo","Los pasos",P("Mira los cuatro pasos del algoritmo."),{"t":"acercando","ds":[0,1,2,3],"alt":"Los cuatro pasos del algoritmo"},P("En el último paso la barra de abajo desaparece, y la de arriba es el máximo común divisor.")),
 sec("Residuos y congruencias","Residuos",P("El residuo es el protagonista de toda la lección."),
   PASOS([("17\\bmod5=2","17 dividido entre 5 da cociente 3 y residuo 2."),
          ("a\\equiv b\\pmod n\\ \\Leftrightarrow\\ n\\mid a-b","Congruencia módulo n."),
          ("(a+b)\\bmod n=((a\\bmod n)+(b\\bmod n))\\bmod n","Sumar y reducir se puede hacer en cualquier orden."),
          ("(7\\cdot9)\\bmod5=(2\\cdot4)\\bmod5=3","Lo mismo vale para el producto.")]),
   OJO("El residuo siempre está entre 0 y n menos 1. En módulo 5 los únicos residuos posibles son 0, 1, 2, 3 y 4.")),
 sec("El algoritmo de Euclides","Euclides",P("Se hacen divisiones sucesivas hasta que el residuo es cero."),
   PASOS([("48=2\\cdot18+12","Se divide 48 entre 18."),
          ("18=1\\cdot12+6","Se divide 18 entre 12."),
          ("12=2\\cdot6+0","Se divide 12 entre 6, con residuo cero."),
          ("\\operatorname{mcd}(48,18)=6","El último divisor, que es 6, es el máximo común divisor.")]),
   OJO("Con el máximo común divisor se calcula el mínimo común múltiplo, porque mcm de a y b es a por b entre su máximo común divisor.")),
 eng("Los dientes de dos engranajes","Dos engranajes tienen 48 y 18 dientes. Un diente del primero toca siempre al mismo diente del segundo cada cierto número de dientes. Ese número es el mínimo común múltiplo, que se obtiene con el máximo común divisor.","\\operatorname{mcm}(48,18)=\\dfrac{48\\cdot18}{6}=144",
   [("Dientes","48 y 18"),("Máximo común divisor","6"),("Se repite el mismo contacto cada","144 dientes")],"Cada 144 dientes el primer engranaje da 3 vueltas y el segundo da 8, y el contacto vuelve a empezar. Si el máximo común divisor es 1, el desgaste se reparte en todos los dientes, y por eso a veces se eligen números de dientes que no tengan factores comunes."),
 completar("Se hace la primera división del algoritmo de Euclides con 48 y 18. Falta el residuo.","48=2\\cdot18+[[hueco]]",
   [("12","doce"),("6","seis"),("30","treinta")],0,
   ["","Seis es el máximo común divisor, y no el residuo de este primer paso.","Treinta es 48 menos 18, y falta restar otra vez 18 para llegar al residuo."],"El residuo es 48 menos 2 por 18.","48 menos 36 es 12."),
 error("Alguien hizo el primer paso del algoritmo de Euclides con 48 y 18 y se equivocó. Toca el paso que está mal.",
   [("\\operatorname{mcd}(48,18)","Se busca el máximo común divisor.","se busca el mcd"),
    ("\\text{residuo}=48-2\\cdot18=6","Este paso es el que falla.","el residuo es 6"),
    ("\\operatorname{mcd}(18,6)=6","Se sigue con el nuevo par.","queda el par 18 y 6")],1,
   "2 por 18 es 36, y 48 menos 36 es 12, y no 6. El par siguiente es 18 y 12. Aunque al final el resultado coincide, el paso intermedio está mal.",
   "48-2\\cdot18=12","Calcula 2 por 18 y réstalo de 48."),
 ordenar("Estos son los pasos del algoritmo de Euclides con 48 y 18, pero están desordenados.",
   [("48=2\\cdot18+12","Se divide 48 entre 18"),
    ("18=1\\cdot12+6","Se divide 18 entre 12"),
    ("12=2\\cdot6+0","Se divide 12 entre 6"),
    ("\\operatorname{mcd}=6","Se toma el último divisor")],[2,0,3,1],
   "Se divide cada vez el divisor anterior entre el residuo, hasta que el residuo es cero.","Se empieza dividiendo el mayor entre el menor."),
]
S+=cierre("Mini simulacro de aritmética modular y Euclides",[
 banco("di_c3_03","17 dividido entre 5 da cociente 3 y residuo 2."),
 pnum("El máximo común divisor de $60$ y $45$ es:","15",0.001,"$60=1\\cdot45+15$ y $45=3\\cdot15+0$, así que el mcd es $15$."),
 pnum("$(7\\cdot9)\\bmod5$ es:","3",0.001,"$63$ dividido entre $5$ da cociente $12$ y residuo $3$.")])
prac=[
 {"titulo":"Dos números","grafica":{"draw":1},"bloques":[P("El par 48 y 18 al comienzo del algoritmo."),EQ("(a,b)=(48,18)")]},
 {"titulo":"Avanza el algoritmo","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador de 0 a 3. Abajo se leen los números a y b en cada paso.")]},
 {"titulo":"El final","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":3,"bloques":[EQ("(a,b)=(6,0)\\ \\Rightarrow\\ \\operatorname{mcd}=6"),P("Cuando b es 0, el máximo común divisor es a.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":3},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Divide el mayor entre el menor y sigue con el residuo."}]}]
preg={"tex":"\\operatorname{mcd}(84,36)=","opciones":["$12$","$6$","$36$","$4$"],"correcta":0,
 "explicacion":"84 es 2 por 36 más 12. Luego 36 es 3 por 12 más 0. El último divisor es 12, que es el máximo común divisor.",
 "verificacion":{"formula":"12+0*x","a":0,"esperado":12},
 "pistas":["Divide 84 entre 36.","El residuo es 12. Ahora divide 36 entre 12.","El residuo es 0, así que el mcd es 12."],
 "errores":["","Seis divide a los dos, pero no es el mayor. Doce también los divide.","Treinta y seis no divide a 84.","Cuatro divide a los dos, pero hay un divisor común más grande."]}
res=["a mod n es el residuo de dividir a entre n, y siempre está entre 0 y n menos 1.","Dos enteros son congruentes módulo n si n divide a su diferencia.","El algoritmo de Euclides reemplaza a, b por b, a mod b hasta llegar a 0, y el último divisor es el máximo común divisor."]
write(lesson("di-m3-l3","Lección 3 de 4","Aritmética modular y Euclides",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Discretas"),"disc-modular.json")
