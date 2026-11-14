import os
os.environ['CURSO_FU']='Álgebra Lineal'
from mklib import *
MOD="Módulo 3 Ortogonalidad y valores propios"
graf={"tipo":"plano","x":[-3.5,9.33],"y":[-2,5],"a":-2,"b":4,"inicio":1,
 "elementos":[
  {"t":"vector","b":["2","1"],"nombre":"a1","c":0},
  {"t":"vector","b":["x","3"],"nombre":"a2","c":1},
  {"t":"segmento","a":["(2*x+3)/5*2","(2*x+3)/5"],"b":["x","3"],"guion":True,"c":3,"guia":True},
  {"t":"vector","b":["(x-6)/5","(12-2*x)/5"],"nombre":"q2","c":2}],
 "lecturas":[{"rotulo":"producto punto de a1 con q2","formula":"2*(x-6)/5+(12-2*x)/5"},{"rotulo":"longitud de q2","formula":"sqrt(((x-6)/5)^2+((12-2*x)/5)^2)"}],
 "etiquetas":["Producto punto de a1 con q2","Longitud de q2"],"etiquetaSlider":"Primera componente del vector a2",
 "alt":"Los vectores a1 igual a (2, 1) y a2 igual a (x, 3), la parte de a2 que va en la dirección de a1 y el vector q2, que es lo que sobra de a2 y siempre es perpendicular a a1"}
glos={"ortogonal":"Un conjunto de vectores es ortogonal si cada par de ellos tiene producto punto cero. Si además todos miden 1, es ortonormal.",
 "ortonormal":"Un conjunto ortonormal es un conjunto ortogonal cuyos vectores miden 1.",
 "proyeccion":"La proyección de a2 sobre a1 es la parte de a2 que va en la dirección de a1.",
 "qr":"La factorización QR escribe una matriz como Q por R, con Q de columnas ortonormales y R triangular."}
ver={"duracion":22.0,"capitulos":[
 [0,3,"Se tienen dos vectores, a1 igual a (2, 1) y a2 igual a (x, 3), que no son perpendiculares."],
 [3,6,"Gram-Schmidt quiere dos vectores perpendiculares que generen lo mismo. El primero se deja igual."],
 [6,12,"Del segundo se quita su proyección sobre a1. Lo que queda, q2, es perpendicular a a1."],
 [12,17,"Se puede mover a2 y q2 siempre queda perpendicular. El producto punto de a1 con q2 vale 0 siempre."],
 [17,22,"Con x igual a 1, a2 es (1, 3) y q2 es (menos 1, 2). Los dos vectores nuevos, a1 y q2, forman un ángulo recto."]],
 "canales":{"draw":[[0.3,0],[5.5,1]],"d":[[6,1],[9,3],[11,-1],[12,1],[22,1]],"guide":[[6,0],[7,1]]},
 "intervalos":{"ok":[17,22]}}
S=[
 sec("La idea",None,P("Trabajar con vectores {{gl:ortogonal|ortogonales}} es mucho más fácil, porque no se estorban entre sí. El proceso de Gram-Schmidt convierte cualquier lista de vectores independientes en otra ortogonal que genera lo mismo, quitando de cada vector lo que ya está en los anteriores.")),
 sec("Un ejemplo","Un ejemplo",P("Se parte de a1 igual a (2, 1) y a2 igual a (x, 3). Se deja a1 igual y a a2 se le quita su {{gl:proyeccion|proyección}} sobre a1."),EQ("q_{1}=a_{1},\\qquad q_{2}=a_{2}-\\dfrac{a_{2}\\cdot q_{1}}{q_{1}\\cdot q_{1}}\\,q_{1}"),{"t":"grafica","animar":"dibujar","alt":"Los vectores a1 y a2"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Con x igual a 1, a2 es (1, 3) y a1 es (2, 1). ¿Cuánto vale el producto punto de a2 con a1?","opciones":[3,4,5,6],"correcta":5,"bien":"Muy bien. Vale 5, y es el número que mide cuánto de a2 va en la dirección de a1. Más abajo se ve.","mal":"Vale 5, porque 1 por 2 más 3 por 1 es 5. Más abajo se ve cómo se usa."}),
 sec("Quitar la proyección","Quitar",P("Mira cómo se construye q2 a partir de a2."),{"t":"acercando","ds":[-1,1,2,3],"alt":"El vector q2 para varios valores de x"},P("Sin importar a2, el vector q2 que queda es perpendicular a a1. Su producto punto con a1 vale <b>0</b>.")),
 sec("Gram-Schmidt paso a paso","Paso a paso",PASOS([("a_{1}=(1,1),\\quad a_{2}=(3,1)","Son dos vectores independientes que no son perpendiculares."),
          ("q_{1}=a_{1}=(1,1)","El primero se queda igual."),
          ("\\dfrac{a_{2}\\cdot q_{1}}{q_{1}\\cdot q_{1}}=\\dfrac{4}{2}=2","Es el coeficiente de la proyección."),
          ("q_{2}=a_{2}-2q_{1}=(1,-1)","Se resta la proyección."),
          ("q_{1}\\cdot q_{2}=1-1=0","Ahora son perpendiculares.")]),
   OJO("Con más de dos vectores, a cada uno se le restan las proyecciones sobre todos los anteriores, no solo sobre uno.")),
 sec("Normalizar","Normalizar",P("Para que los vectores sean {{gl:ortonormal|ortonormales}}, se divide cada uno entre su longitud."),
   PASOS([("e_{1}=\\dfrac{(1,1)}{\\sqrt{2}},\\quad e_{2}=\\dfrac{(1,-1)}{\\sqrt{2}}","Ahora miden 1."),
          ("Q=\\dfrac{1}{\\sqrt{2}}"+M(1,1,1,-1),"Las columnas de Q son ortonormales."),
          ("Q^{T}Q=I\\ \\Rightarrow\\ Q^{-1}=Q^{T}","Una matriz cuadrada con columnas ortonormales se invierte trasponiéndola. Si no es cuadrada, solo se cumple Q transpuesta por Q igual a I.")]),
   P("La factorización {{gl:qr|QR}} que sale de este proceso se usa mucho en cálculo numérico.")),
 sec("Matrices ortogonales","Ortogonales",P("Una matriz Q es ortogonal si sus columnas son ortonormales, y eso equivale a Q traspuesta por Q igual a la identidad."),
   PASOS([("R="+M(0,-1,1,0)+",\\quad R^{T}R="+M(1,0,0,1),"El giro de 90 grados es ortogonal."),
          ("\\|Q\\mathbf{x}\\|=\\|\\mathbf{x}\\|","Las matrices ortogonales conservan las longitudes y los ángulos.")])),
 eng("Ajustar una recta a unos datos","Cuando se miden datos con ruido, como una fuerza contra un alargamiento, no hay una recta que pase por todos los puntos. El mejor ajuste es la proyección del vector de las mediciones sobre el de los alargamientos, y el error que queda es perpendicular a ese vector.","\\hat{a}=\\dfrac{\\mathbf{x}\\cdot\\mathbf{y}}{\\mathbf{x}\\cdot\\mathbf{x}}",
   [("Alargamientos","1, 2 y 3 mm"),("Fuerzas","2, 3 y 5 N"),("Pendiente ajustada","1.64 N/mm")],"El producto punto de x con y es 1 por 2 más 2 por 3 más 3 por 5, o sea 23, y el de x consigo mismo es 14. La pendiente es 23 sobre 14, o sea unos 1.64 newtons por milímetro. El vector de errores queda perpendicular al de alargamientos. Es un modelo simplificado, porque supone una relación lineal que pasa por el origen."),
 completar("Se calcula q2 para a1 igual a (2, 1) y a2 igual a (1, 3). La proyección de a2 sobre a1 es 5 sobre 5 por (2, 1), o sea (2, 1). Falta la primera componente de q2.","q_{2}=(1,3)-(2,1)=([[hueco]],\\ 2)",
   [("-1","menos uno"),("3","tres"),("1","uno")],0,
   ["","Se sumó en vez de restar. 1 menos 2 es menos 1.","Esa es la primera componente de a2, sin quitar nada. Hay que restar 2."],"Resta 2 de la primera componente de a2.","1 menos 2 es menos 1. Y 3 menos 1 es 2, así que q2 es (menos 1, 2)."),
 error("Alguien aplicó Gram-Schmidt y se equivocó en un paso. Toca el primer paso donde aparece el error.",
   [("a_{1}=(1,1),\\quad a_{2}=(3,1)","Son los vectores de partida.","a1 es 1, 1 y a2 es 3, 1"),
    ("q_{2}=a_{2}-a_{1}=(2,0)","Este paso es el que falla.","q2 es a2 menos a1, o sea 2, 0"),
    ("\\text{Entonces}\\ q_{2}\\ \\text{es perpendicular a}\\ a_{1}","Depende del paso anterior.","Entonces q2 es perpendicular a a1")],1,
   "Falta el coeficiente de la proyección. Hay que restar a2 punto a1 sobre a1 punto a1 veces a1, o sea 2 veces a1. Con la resta directa el producto punto de q2 con a1 es 2, no 0.",
   "q_{2}=a_{2}-2a_{1}=(1,-1),\\quad q_{2}\\cdot a_{1}=0","Calcula el producto punto del vector q2 con a1."),
 ordenar("Estos son los pasos de Gram-Schmidt para a1 igual a (1, 1) y a2 igual a (3, 1), pero están desordenados.",
   [("q_{1}=a_{1}=(1,1)","El primer vector se deja igual"),
    ("\\dfrac{a_{2}\\cdot q_{1}}{q_{1}\\cdot q_{1}}=\\dfrac{4}{2}=2","Se calcula el coeficiente de la proyección"),
    ("q_{2}=a_{2}-2q_{1}=(1,-1)","Se resta la proyección"),
    ("q_{1}\\cdot q_{2}=0","Se comprueba que son perpendiculares")],[2,0,3,1],
   "Se deja el primero, se calcula el coeficiente, se resta la proyección y se comprueba.","Se empieza dejando el primer vector igual."),
]
S+=cierre("Mini simulacro de ortogonalidad",[
 banco("al_c3_05","El producto punto es $1-1+0=0$, así que son ortogonales."),
 banco("al_c3_07","La proyección es $\\frac{(3,0)\\cdot(1,1)}{(1,1)\\cdot(1,1)}(1,1)=\\frac{3}{2}(1,1)$."),
 banco("al_c3_08","Es la definición de matriz ortogonal.")])
prac=[
 {"titulo":"Dos vectores","grafica":{"draw":1},"bloques":[P("Se parte de dos vectores que no son perpendiculares."),EQ("a_{1}=(2,1),\\qquad a_{2}=(x,3)")]},
 {"titulo":"Mueve a2","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. El vector a2 cambia. Abajo se ven el producto punto de a1 con q2 y la longitud de q2.")]},
 {"titulo":"Quitar la proyección","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[P("El segmento punteado es la proyección de a2 sobre a1. Lo que queda, q2, es perpendicular a a1 sin importar dónde esté a2, y su producto punto con a1 siempre es 0.")]},
 {"titulo":"El resultado","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":1,"bloques":[EQ("q_{2}=(1,3)-(2,1)=(-1,2)"),P("Con x igual a 1, q2 es (menos 1, 2). Los vectores a1 y q2 forman un ángulo recto.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":1},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Calcula el coeficiente de la proyección y réstala."}]}]
preg={"tex":"q_{2}\\ \\text{con}\\ a_{1}=(1,2),\\ a_{2}=(4,1)","encabezado":"Con a1 igual a (1, 2) y a2 igual a (4, 1), ¿cuánto vale la segunda componente de q2?","opciones":["$-1.4$","$1.4$","$-2.4$","$2.8$"],"correcta":0,
 "explicacion":"El producto punto de a2 con a1 es 6 y el de a1 consigo mismo es 5. El coeficiente es 6 sobre 5. Entonces q2 es (4, 1) menos 6 sobre 5 por (1, 2), o sea (2.8, menos 1.4). Su segunda componente es menos 1.4.",
 "verificacion":{"formula":"1-6/5*2+0*x","a":0,"esperado":-1.4},
 "pistas":["Calcula el producto punto de a2 con a1 y el de a1 consigo mismo.","Son 6 y 5. El coeficiente de la proyección es 6 sobre 5.","Resta 6 sobre 5 por la segunda componente de a1 a la segunda de a2."],
 "errores":["","Es el valor absoluto. Falta el signo, porque 1 menos 12 sobre 5 es negativo.","Revisa la cuenta. 6 sobre 5 por 2 es 2.4, y 1 menos 2.4 es menos 1.4.","Esa es la primera componente de q2, 2.8. Se pide la segunda."]}
res=["Gram-Schmidt convierte vectores independientes en ortogonales, restando a cada uno su proyección sobre los anteriores.","Dividiendo entre la longitud se obtienen vectores ortonormales, con los que se arma una matriz ortogonal.","Una matriz ortogonal cumple Q traspuesta por Q igual a la identidad, y conserva longitudes y ángulos."]
write(lesson("alglin-m3-l3","Lección 3 de 4","Gram-Schmidt y ortogonalidad",26,graf,glos,ver,S,prac,preg,res,modulo=MOD,curso="Álgebra Lineal"),"alglin-gramschmidt.json")
