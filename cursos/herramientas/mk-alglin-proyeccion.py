import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 2 Espacios vectoriales y transformaciones"
graf={"tipo":"plano","x":[-3.5,9.33],"y":[-2,5],"a":-2,"b":4,"inicio":1,
 "elementos":[
  {"t":"vector","b":["2","1"],"nombre":"u","c":0},
  {"t":"vector","b":["x","3"],"nombre":"v","c":1},
  {"t":"vector","b":["(2*x+3)/5*2","(2*x+3)/5"],"nombre":"proyección","c":2},
  {"t":"segmento","a":["(2*x+3)/5*2","(2*x+3)/5"],"b":["x","3"],"guion":True,"nombre":"perpendicular","c":3,"guia":True}],
 "lecturas":[{"rotulo":"producto punto","formula":"2*x+3"},{"rotulo":"longitud de la proyección","formula":"abs(2*x+3)/sqrt(5)"}],
 "etiquetas":["Producto punto de v con u","Longitud de la proyección"],"etiquetaSlider":"Primera componente del vector v",
 "alt":"El vector u igual a (2, 1), el vector v igual a (x, 3) y la proyección de v sobre u, con un segmento punteado perpendicular a u que une la punta de la proyección con la de v"}
glos={"punto":"El producto punto de dos vectores es la suma de los productos de sus componentes. Mide cuánto apuntan en la misma dirección.",
 "norma":"La norma de un vector es su longitud. Se calcula como la raíz de la suma de los cuadrados de sus componentes.",
 "ortogonales":"Dos vectores son ortogonales si forman un ángulo recto, o sea si su producto punto es cero.",
 "proyeccion":"La proyección de v sobre u es la parte de v que va en la dirección de u. Es la sombra de v sobre la recta de u."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"Estos son dos vectores, u igual a (2, 1) y v igual a (x, 3)."],
 [3,6,"La proyección de v sobre u es la sombra de v sobre la recta de u."],
 [6,12,"Al mover v, la sombra se desliza sobre u. El segmento punteado, que une v con su sombra, siempre es perpendicular a u."],
 [12,17,"Con x igual a 1, el producto punto de v con u vale 5 y la proyección es el mismo u."],
 [17,22,"Con x igual a menos 1.5, v y u son perpendiculares y la proyección es cero."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,1],[9,3],[11,2],[12,1],[16,1],[17,-1.5],[22,-1.5]],"guide":[[3,0],[4,1]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("El producto punto es una operación que convierte dos vectores en un número. Ese número mide cuánto apuntan en la misma dirección y permite calcular longitudes, ángulos y proyecciones. Con él se descompone un vector en una parte que va a lo largo de otro y una parte perpendicular.")),
 sec("Un ejemplo","Un ejemplo",P("Mira los vectores u igual a (2, 1) y v igual a (x, 3), y la sombra de v sobre u."),EQ("\\operatorname{proy}_{u}v=\\dfrac{v\\cdot u}{u\\cdot u}\\,u"),{"t":"grafica","animar":"dibujar","alt":"Los vectores u y v"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con x igual a 1, v es (1, 3). Su producto punto con u igual a (2, 1) es 1 por 2 más 3 por 1. ¿Cuánto vale?","opciones":[3,4,5,6],"correcta":5,"bien":"Muy bien. Vale 5. Más abajo se ve la proyección que sale de ahí.","mal":"Vale 5, porque 2 más 3 es 5. Más abajo se ve la proyección que sale de ahí."}),
 sec("La sombra","La sombra",P("Mira cómo se mueve la proyección cuando cambia v."),{"t":"acercando","ds":[-1.5,0,1,3],"alt":"La proyección de v sobre u para varios valores de x"},P("Con x igual a <b>menos 1.5</b>, el producto punto es 0 y la proyección desaparece. Eso pasa cuando los vectores son perpendiculares.")),
 sec("Producto punto, norma y ángulo","Producto punto",P("Se multiplican las componentes que están en la misma posición y se suman."),
   PASOS([("(2,-1,3)\\cdot(1,4,0)=2-4+0=-2","Se multiplican componente por componente y se suma."),
          ("\\|(2,3,6)\\|=\\sqrt{4+9+36}=7","La norma es la raíz del producto punto del vector consigo mismo."),
          ("\\cos\\theta=\\dfrac{u\\cdot v}{\\|u\\|\\,\\|v\\|}","El producto punto también da el ángulo entre dos vectores."),
          ("u=(1,0),\\ v=(1,1)\\ \\Rightarrow\\ \\cos\\theta=\\dfrac{1}{\\sqrt{2}}\\ \\Rightarrow\\ \\theta=45^{\\circ}","Es el ángulo entre un vector del eje y la diagonal.")])),
 sec("Ortogonalidad","Ortogonalidad",P("Dos vectores distintos de cero son {{gl:ortogonales|ortogonales}} si y solo si su {{gl:punto|producto punto}} es cero."),
   PASOS([("(1,2)\\cdot(4,-2)=4-4=0","Son ortogonales."),
          ("(1,2)\\cdot(2,1)=4\\ne 0","No son ortogonales, aunque tengan la misma longitud.")]),
   OJO("Tener la misma norma no hace ortogonales a dos vectores. Lo que decide es el producto punto.")),
 sec("La proyección","La proyección",P("La {{gl:proyeccion|proyección}} de v sobre u es el múltiplo de u que queda más cerca de v. Lo que sobra, v menos la proyección, es perpendicular a u."),
   PASOS([("v=(1,3),\\ u=(2,1):\\quad v\\cdot u=5,\\quad u\\cdot u=5","Se calculan los dos productos punto."),
          ("\\operatorname{proy}_{u}v=\\dfrac{5}{5}(2,1)=(2,1)","Se aplica la fórmula."),
          ("v-\\operatorname{proy}_{u}v=(-1,2),\\quad (-1,2)\\cdot(2,1)=0","La parte que sobra es perpendicular a u.")])),
 eng("El trabajo de una fuerza inclinada","Cuando una fuerza empuja un cuerpo en una dirección distinta de su desplazamiento, solo trabaja la parte de la fuerza que va a lo largo del desplazamiento. Esa parte es la proyección, y el trabajo es el producto punto de la fuerza con el desplazamiento.","W=\\mathbf{F}\\cdot\\mathbf{d}=(30,40)\\cdot(5,0)",
   [("Fuerza","(30, 40) N"),("Desplazamiento","(5, 0) m"),("Trabajo","150 J")],"El producto punto da 30 por 5 más 40 por 0, o sea 150 julios. La componente vertical de 40 newtons no hace trabajo, porque el desplazamiento es horizontal. Es un modelo simplificado, porque supone una fuerza constante."),
 completar("Se proyecta v igual a (1, 3) sobre u igual a (2, 1). Falta el producto punto de u consigo mismo.","u\\cdot u=2^{2}+1^{2}=[[hueco]]",
   [("5","cinco"),("3","tres"),("25","veinticinco")],0,
   ["","Eso es 2 más 1. El producto punto suma los cuadrados de las componentes, o sea 4 más 1.","Eso es el cuadrado de 5. Hay que sumar 2 al cuadrado y 1 al cuadrado, que da 5."],"Suma los cuadrados de las componentes.","2 al cuadrado es 4 y 1 al cuadrado es 1. La suma es 5."),
 error("Alguien decidió si dos vectores son ortogonales y se equivocó en un paso. Toca el primer paso donde aparece el error.",
   [("u=(1,2),\\quad v=(2,1)","Son los dos vectores.","u es 1, 2 y v es 2, 1"),
    ("\\|u\\|=\\|v\\|=\\sqrt{5}\\ \\Rightarrow\\ \\text{son ortogonales}","Este paso es el que falla.","Las normas son iguales a raíz de 5, así que son ortogonales"),
    ("\\text{Los vectores forman un ángulo recto}","Depende del paso anterior.","Los vectores forman un ángulo recto")],1,
   "Que las normas sean iguales no decide. Se mira el producto punto, que aquí es 1 por 2 más 2 por 1, o sea 4, y no es cero. Los vectores no son ortogonales.",
   "u\\cdot v=2+2=4\\ne 0","Calcula el producto punto de los dos vectores."),
 ordenar("Estos son los pasos para proyectar v igual a (1, 3) sobre u igual a (2, 1), pero están desordenados.",
   [("v\\cdot u=1\\cdot 2+3\\cdot 1=5","El producto punto de v con u"),
    ("u\\cdot u=2^{2}+1^{2}=5","El producto punto de u consigo mismo"),
    ("\\operatorname{proy}_{u}v=\\dfrac{5}{5}(2,1)","Se arma el cociente por u"),
    ("=(2,1)","Es la proyección")],[2,0,3,1],
   "Se calculan los dos productos punto, se arma el cociente y se multiplica por u.","Se empieza con el producto punto de v con u."),
]
S+=cierre("Mini simulacro de producto punto y proyección",[
 banco("al_c3_03","La proyección sobre el eje $x$ conserva la primera componente, y su norma es $3$."),
 banco("al_c2_16","$1\\cdot2+2\\cdot0+2\\cdot1=4$."),
 banco("al_c2_17","$\\sqrt{3^2+4^2}=5$.")])
prac=[
 {"titulo":"Dos vectores","grafica":{"draw":1},"bloques":[P("Estos son dos vectores y la sombra de v sobre u."),EQ("u=(2,1),\\qquad v=(x,3)")]},
 {"titulo":"Mueve v","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El vector v cambia, la proyección se desliza sobre u y abajo se ven el producto punto y la longitud de la proyección.")]},
 {"titulo":"El perpendicular","grafica":{"draw":1,"guide":1},"laboratorio":True,"d":1,"bloques":[P("El segmento punteado une la punta de v con la de su proyección y es perpendicular a u. Con x igual a 1 la proyección es el mismo u.")]},
 {"titulo":"Ortogonales","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":-1.5,"bloques":[EQ("v\\cdot u=2x+3=0\\ \\Rightarrow\\ x=-\\tfrac{3}{2}"),P("Con x igual a menos 1.5 el producto punto es 0, los vectores son perpendiculares y no hay proyección.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":-1.5},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Calcula los dos productos punto y arma el cociente."}]}]
preg={"tex":"\\text{Segunda componente de}\\ \\operatorname{proy}_{u}v,\\ v=(5,1),\\ u=(2,1)","opciones":["$2.2$","$4.4$","$1.1$","$5.5$"],"correcta":0,
 "explicacion":"El producto punto de v con u es 5 por 2 más 1 por 1, o sea 11, y el de u consigo mismo es 5. La proyección es 11 sobre 5 por (2, 1), o sea (4.4, 2.2). Su segunda componente es 2.2.",
 "verificacion":{"formula":"11/5*1+0*x","a":0,"esperado":2.2},
 "pistas":["Calcula el producto punto de v con u y el de u consigo mismo.","Son 11 y 5. La proyección es 11 sobre 5 por u.","Multiplica 11 sobre 5 por la segunda componente de u, que es 1."],
 "errores":["","Ese es el valor de la primera componente de la proyección. Se pide la segunda.","Se dividió el producto punto entre 10 y no entre 5. El de u consigo mismo es 5.","Se dividió 11 entre 2 en vez de entre 5. Hay que dividir entre el producto punto de u consigo mismo."]}
res=["El producto punto mide cuánto apuntan dos vectores en la misma dirección. Da longitudes y ángulos.","Dos vectores son ortogonales si su producto punto es cero.","La proyección de v sobre u es el producto punto de v con u, dividido entre el de u consigo mismo, por u."]
write(lesson("alglin-m2-l3","Lección 3 de 4","Producto punto y proyección",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-proyeccion.json")
