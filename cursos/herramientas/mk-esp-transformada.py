import os, math
os.environ['CURSO_FU']='Matemáticas Especiales'; os.environ['BANCO']='especiales'
from mklib import *
MOD="Módulo 2 Transformada de Fourier y EDP de evolución"
# gaussiana f(x)=exp(-a x^2) y su transformada sqrt(1/(2a)) exp(-w^2/(4a)), con a = slider
TS=[round(-4+0.1*k,1) for k in range(81)]
EL=[{"t":"trazo","puntos":[[str(t),f"exp(-x*{t*t:.4f})"] for t in TS],"c":0},
    {"t":"trazo","puntos":[[str(t),f"(1/sqrt(2*x))*exp(-{t*t:.4f}/(4*x))"] for t in TS],"c":1}]
graf={"tipo":"plano","x":[-5.5,5.5],"y":[-0.4,2.4],"a":0.1,"b":4,"inicio":1,"elementos":EL,
 "lecturas":[{"rotulo":"ancho de la gaussiana, la raíz de 1 entre a","formula":"1/sqrt(x)"},{"rotulo":"altura de la transformada en omega igual a 0","formula":"1/sqrt(2*x)"}],
 "etiquetas":["Mientras mayor es a, más angosta es la función en el tiempo","Y más baja y ancha es su transformada, en la frecuencia"],"etiquetaSlider":"Parámetro a, de 0.1 a 4",
 "alt":"La gaussiana e elevado a menos a x al cuadrado, en azul, y su transformada de Fourier, otra gaussiana, en marrón. Al aumentar a la gaussiana original se hace más angosta y su transformada se hace más ancha y baja. Una función no puede ser angosta en el tiempo y en la frecuencia a la vez"}
glos={"transformada":"La transformada de Fourier de f es la función f gorro de omega, que mide cuánto de la frecuencia omega hay en f. Sirve para funciones no periódicas.",
 "traslacion":"Trasladar la función por a multiplica la transformada por e elevado a menos i a omega. El módulo no cambia, solo la fase.",
 "convolucion":"La transformada de una convolución es proporcional al producto de las transformadas.",
 "incertidumbre":"Una función angosta en el tiempo tiene una transformada ancha en la frecuencia, y al revés. No pueden ser angostas las dos a la vez."}
ver={"duracion":24.0,"capitulos":[
 [0,4,"La curva azul es la gaussiana e elevado a menos a x al cuadrado, y la marrón es su transformada de Fourier."],
 [4,9,"La transformada de una gaussiana es otra gaussiana. Con a igual a 1 las dos tienen un ancho parecido."],
 [9,15,"Con a grande, la gaussiana es muy angosta y su transformada es ancha y baja."],
 [15,20,"Con a chico, la gaussiana es ancha y su transformada es angosta y alta."],
 [20,24,"Esta es la relación de incertidumbre. No se puede ser angosto en el tiempo y en la frecuencia a la vez."]],
 "canales":{"draw":[[0.3,0],[3.5,1]],"d":[[4,1],[8,1],[10,4],[14,4],[16,0.1],[19,0.1],[24,0.1]],"guide":[[4,0],[5,1]]},
 "intervalos":{"ok":[15,24]}}
S=[
 sec("La idea",None,P("La {{gl:transformada|transformada de Fourier}} es la versión de la serie de Fourier para funciones que no son periódicas. Convierte una función del tiempo en una función de la frecuencia. Tiene propiedades muy útiles. La {{gl:traslacion|traslación}} se vuelve una fase, la derivada se vuelve una multiplicación, y la {{gl:convolucion|convolución}} se vuelve un producto. Y siempre hay una relación de {{gl:incertidumbre|incertidumbre}} entre el ancho en el tiempo y en la frecuencia.")),
 sec("Un ejemplo","Un ejemplo",P("La gaussiana es su propia forma en la frecuencia. Mira cómo cambia el ancho de las dos curvas al mover a."),EQ("\\mathcal{F}\\{e^{-ax^{2}}\\}(\\omega)=\\dfrac{1}{\\sqrt{2a}}\\,e^{-\\omega^{2}/4a}"),{"t":"grafica","animar":"dibujar","alt":"La gaussiana y su transformada"}),
 sec("Piensa antes de ver","Piensa",{"t":"piensa","pregunta":"Si una función se comprime en el tiempo, ¿su transformada se ensancha o se angosta en la frecuencia?","opciones":["Se ensancha","Se angosta"],"correcta":"Se ensancha","bien":"Muy bien. Comprimir en el tiempo ensancha la frecuencia. Más abajo se ve con la gaussiana.","mal":"Se ensancha. Una señal corta contiene muchas frecuencias, y una señal larga contiene pocas. Más abajo se ve con la gaussiana."}),
 sec("Variando a","El parámetro",P("Mira las dos gaussianas con a igual a 0.1, 1 y 4."),{"t":"acercando","ds":[0.1,1,4],"alt":"Las gaussianas con tres valores de a"},P("Con a igual a 4 la gaussiana es angosta y su transformada es ancha y baja. Con a igual a 0.1 es al revés.")),
 sec("Propiedades","Propiedades",P("Las propiedades permiten calcular transformadas sin integrar de nuevo."),
   PASOS([("\\mathcal{F}\\{f(x-a)\\}=e^{-ia\\omega}\\,\\hat{f}(\\omega)","Traslación. Solo cambia la fase."),
          ("\\mathcal{F}\\{f'(x)\\}=i\\omega\\,\\hat{f}(\\omega)","Derivada. Se multiplica por i omega."),
          ("\\mathcal{F}\\{f(ax)\\}=\\dfrac{1}{|a|}\\,\\hat{f}\\!\\left(\\dfrac{\\omega}{a}\\right)","Escalamiento. Comprimir en x ensancha en omega."),
          ("\\mathcal{F}\\{f*g\\}\\propto\\hat{f}(\\omega)\\,\\hat{g}(\\omega)","Convolución. Se vuelve un producto.")]),
   OJO("Hay varias convenciones para la transformada, con constantes distintas. Las propiedades son las mismas, pero las constantes cambian, y hay que revisar cuál usa cada libro.")),
 sec("Ejemplos clásicos","Ejemplos",P("Algunas transformadas conviene conocerlas."),
   PASOS([("e^{-|x|}\\ \\to\\ \\sqrt{\\tfrac{2}{\\pi}}\\dfrac{1}{1+\\omega^{2}}","La exponencial de dos lados da una lorentziana."),
          ("h(x)=f(x-2)\\ \\Rightarrow\\ \\hat{h}=e^{-2i\\omega}\\sqrt{\\tfrac{2}{\\pi}}\\dfrac{1}{1+\\omega^{2}}","Con la propiedad de traslación."),
          ("\\text{pulso}\\ [-a,a]\\ \\to\\ \\sqrt{2/\\pi}\\,\\dfrac{\\operatorname{sen}(a\\omega)}{\\omega}","El pulso rectangular da una función sinc."),
          ("e^{-ax^{2}}\\ \\to\\ \\text{gaussiana}","La gaussiana se transforma en otra gaussiana.")])),
 eng("El ancho de banda de un pulso","Un pulso rectangular muy corto sirve para excitar un circuito y probar muchas frecuencias a la vez, porque su transformada es ancha. Un pulso largo prueba pocas frecuencias, con más precisión. Ese es el compromiso de la incertidumbre.","\\Delta t\\cdot\\Delta\\omega\\gtrsim\\text{constante}",
   [("Pulso corto","banda ancha"),("Pulso largo","banda angosta"),("Compromiso","no se tienen los dos")],"En un radar o en un sistema de comunicaciones, el ancho del pulso decide la resolución en distancia y en frecuencia. Si se quiere medir una distancia con precisión se usa un pulso corto, pero entonces la frecuencia queda poco definida. Es la misma limitación que aparece en mecánica cuántica con posición y momento."),
 completar("Se aplica la propiedad de traslación de la transformada de Fourier. Falta el factor.","\\mathcal{F}\\{f(x-a)\\}=[[hueco]]\\,\\hat{f}(\\omega)",
   [("e^{-ia\\omega}","una fase"),("i\\omega","multiplicar por i omega"),("\\dfrac{1}{|a|}","un factor de escala")],0,
   ["","Multiplicar por i omega es la propiedad de la derivada, y no la de la traslación.","El factor de escala aparece cuando se comprime la función, y no cuando se traslada."],"La traslación solo cambia la fase.","El factor es una exponencial compleja que no cambia el módulo."),
 error("Alguien aplicó una propiedad de la transformada de Fourier y se equivocó en un paso. Toca el paso que está mal.",
   [("f(x)=e^{-|x|},\\quad h(x)=f(x-2)","La función y su traslación.","h es f trasladada 2"),
    ("\\hat{h}(\\omega)=\\hat{f}(\\omega-2)","Este paso es el que falla.","la transformada se traslada en omega"),
    ("\\text{Es la lorentziana trasladada}","Depende del paso anterior.","es la misma lorentziana trasladada")],1,
   "Trasladar en x no traslada la transformada, sino que la multiplica por una fase, e elevado a menos 2 i omega. El módulo de la transformada no cambia.",
   "\\hat{h}(\\omega)=e^{-2i\\omega}\\hat{f}(\\omega)","Recuerda qué cambia con la traslación."),
 ordenar("Estos son los pasos para obtener la transformada de la derivada de f, pero están desordenados.",
   [("\\hat{f'}(\\omega)=\\displaystyle\\int f'(x)e^{-i\\omega x}dx","Se escribe la definición"),
    ("=\\Big[f\\,e^{-i\\omega x}\\Big]+i\\omega\\displaystyle\\int f\\,e^{-i\\omega x}dx","Se integra por partes"),
    ("\\Big[f\\,e^{-i\\omega x}\\Big]=0","Los términos en los extremos se anulan"),
    ("\\hat{f'}(\\omega)=i\\omega\\,\\hat{f}(\\omega)","Se obtiene el resultado")],[2,0,3,1],
   "Se escribe la definición, se integra por partes y los términos del borde se anulan.","Se empieza con la definición."),
]
S+=cierre("Mini simulacro de la transformada de Fourier y propiedades",[
 banco("es_c2_05","La traslación multiplica por una fase, $e^{-ia\\omega}$."),
 banco("es_c2_06","La derivada se vuelve la multiplicación por $i\\omega$."),
 banco("es_c2_08","La transformada de una gaussiana es otra gaussiana.")])
prac=[
 {"titulo":"Dos gaussianas","grafica":{"draw":1},"bloques":[P("La gaussiana y su transformada de Fourier."),EQ("e^{-ax^{2}}\\ \\leftrightarrow\\ \\dfrac{1}{\\sqrt{2a}}e^{-\\omega^{2}/4a}")]},
 {"titulo":"Cambia a","grafica":{"draw":1},"laboratorio":True,"bloques":[P("Mueve el deslizador. Abajo se leen el ancho de la gaussiana y la altura de su transformada.")]},
 {"titulo":"Una gaussiana angosta","grafica":{"draw":1,"guide":1,"ok":True},"laboratorio":True,"d":4,"bloques":[EQ("a=4\\ \\Rightarrow\\ \\text{ancho}=0.5,\\ \\text{altura}=0.35"),P("Con a igual a 4, la función es angosta y su transformada es ancha y baja.")]},
 {"titulo":"Revisa tu respuesta","grafica":{"draw":1,"guide":1,"ok":True,"d":4},"bloques":[{"t":"pregunta"},{"t":"nota","html":"Recuerda qué se multiplica en cada propiedad."}]}]
preg={"tex":"\\mathcal{F}\\{f'(x)\\}(\\omega)\\ \\text{es}","opciones":["$i\\omega\\,\\hat{f}(\\omega)$","$\\dfrac{\\hat{f}(\\omega)}{i\\omega}$","$\\omega^{2}\\hat{f}(\\omega)$","$\\hat{f}(\\omega-1)$"],"correcta":0,
 "explicacion":"Al integrar por partes, los términos del borde se anulan y queda i omega por la transformada de f. Por eso derivar en x equivale a multiplicar por i omega en la frecuencia.",
 "verificacion":{"formula":"1+0*x","a":0,"esperado":1},
 "pistas":["Integra por partes.","Los términos de borde se anulan.","Queda i omega por la transformada."],
 "errores":["","Dividir entre i omega corresponde a integrar, y no a derivar.","Omega al cuadrado aparece con la segunda derivada, y con signo menos.","Trasladar en la frecuencia corresponde a multiplicar por una exponencial en x."]}
res=["La transformada de Fourier representa funciones no periódicas con frecuencias continuas.","La traslación multiplica por una fase, la derivada por i omega, y la convolución se vuelve un producto.","Una función angosta en x tiene una transformada ancha, y no se puede tener angosto en los dos lados."]
write(lesson("es-m2-l1","Lección 1 de 5","Transformada de Fourier y propiedades",28,graf,glos,ver,S,prac,preg,res,modulo=MOD,ejercicios=8,curso="Matemáticas Especiales"),"esp-transformada.json")
