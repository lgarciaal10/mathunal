PREREQ={
'matbas-exponentes':[],'matbas-notables':['matbas-exponentes'],'matbas-polinomios':['matbas-notables'],'matbas-fracciones':['matbas-notables','matbas-polinomios'],'matbas-explog':['matbas-exponentes'],'matbas-cuadraticas':['matbas-notables'],'matbas-inecuaciones':['matbas-cuadraticas'],'matbas-sistemas':['matbas-cuadraticas'],'matbas-radicales':['matbas-cuadraticas','matbas-exponentes'],'matbas-trigonometria':['matbas-cuadraticas'],'matbas-funciones':['matbas-cuadraticas'],'matbas-linealcuad':['matbas-cuadraticas'],'matbas-geoanalitica':['matbas-linealcuad'],
'calculo-limite-1':['matbas-funciones'],'calculo-limite-2':['calculo-limite-1'],'calculo-limite-3':['calculo-limite-2'],'calculo-limite-4':['calculo-limite-3'],
'calculo-infinito':['calculo-limite-3'],'calculo-asintotas':['calculo-infinito'],
'calculo-derivada-1':['calculo-limite-1','calculo-limite-4'],'calculo-derivada-2':['calculo-derivada-1'],'calculo-derivada-3':['calculo-derivada-2'],
'calculo-derivada-4':['calculo-derivada-3'],'calculo-derivada-5':['calculo-derivada-3'],'calculo-derivada-6':['calculo-derivada-5'],
'calculo-derivada-7':['calculo-derivada-2'],'calculo-derivada-8':['calculo-derivada-7'],'calculo-derivada-9':['calculo-derivada-3'],'calculo-derivada-10':['calculo-derivada-4'],
'calculo-valor-medio':['calculo-derivada-2','calculo-limite-4'],'calculo-derivada-11':['calculo-valor-medio'],'calculo-derivada-12':['calculo-derivada-11'],
'calculo-derivada-13':['calculo-derivada-12'],'calculo-derivada-14':['calculo-derivada-11'],'calculo-lhopital':['calculo-derivada-3','calculo-limite-3'],
'calculo-newton':['calculo-derivada-7'],'calculo-tfc':['calculo-valor-medio'],
'calcint-tfc':['calculo-tfc','calculo-derivada-2'],'calcint-sustitucion':['calcint-tfc','calculo-derivada-3'],'calcint-partes':['calcint-sustitucion','calculo-derivada-2'],
'calcint-entre':['calcint-tfc'],'calcint-trig':['calcint-sustitucion','matbas-trigonometria'],'calcint-sentri':['calcint-trig'],'calcint-fparc':['calcint-sustitucion'],
'calcint-impropias':['calcint-tfc','calculo-infinito'],'calcint-volumenes':['calcint-entre'],'calcint-trabajo':['calcint-tfc'],
'calcint-arco':['calcint-sentri','calcint-volumenes'],'calcint-polares':['calcint-trig','calcint-entre'],'calcint-series':['calculo-infinito','calcint-impropias'],
'alglin-matrices':[],'alglin-sistemas':['alglin-matrices'],'alglin-gauss':['alglin-sistemas'],'alglin-det':['alglin-matrices','alglin-gauss'],
'alglin-indep':['alglin-gauss'],'alglin-fundamentales':['alglin-indep'],'alglin-proyeccion':['alglin-indep'],'alglin-transformaciones':['alglin-matrices','alglin-det'],
'alglin-propios':['alglin-det','alglin-transformaciones'],'alglin-diagonalizacion':['alglin-propios','alglin-indep'],'alglin-gramschmidt':['alglin-proyeccion'],
'alglin-simetricas':['alglin-diagonalizacion','alglin-gramschmidt'],
'edo-separables':['calcint-sustitucion'],'edo-lineal':['edo-separables','calcint-sustitucion'],'edo-homogenea':['edo-lineal','calculo-derivada-3'],'edo-indeterminados':['edo-homogenea'],'edo-wronskiano':['edo-homogenea'],'edo-cauchy':['edo-homogenea'],'edo-inversa':['edo-laplace'],'edo-sistemas':['alglin-propios','edo-homogenea'],'edo-escalon':['edo-inversa'],'edo-series':['edo-homogenea','calcint-series'],'edo-existencia':['edo-separables'],'edo-exactas':['edo-separables','calculo-derivada-3'],'edo-autonomas':['edo-separables'],'edo-bernoulli':['edo-lineal','edo-separables'],'edo-laplace':['calcint-impropias','edo-lineal'],
}
PREREQ.update({
# Fundamentos
'fund-logica':[],'fund-cuantificadores':['fund-logica'],'fund-argumentos':['fund-logica'],'fund-demostracion':['fund-argumentos','fund-cuantificadores'],'fund-induccion':['fund-demostracion'],
'fund-conjuntos':['fund-logica'],'fund-operaciones':['fund-conjuntos'],'fund-relaciones':['fund-conjuntos'],'fund-equivalencia':['fund-relaciones'],'fund-funciones':['fund-relaciones'],'fund-imagen':['fund-funciones'],'fund-cardinalidad':['fund-funciones'],
# Geometría vectorial
'geovec-punto':['matbas-geoanalitica'],'geovec-vectores':['geovec-punto'],'geovec-rectas':['geovec-vectores'],'geovec-lineal':['geovec-vectores'],'geovec-area':['geovec-vectores'],'geovec-conicas':['geovec-rectas','matbas-cuadraticas'],
'geovec-r3':['geovec-vectores'],'geovec-cruz':['geovec-r3','alglin-det'],'geovec-triple':['geovec-cruz'],'geovec-planos':['geovec-cruz'],'geovec-distancias':['geovec-planos','geovec-rectas'],'geovec-espacio':['geovec-planos'],
# Discretas
'disc-logica':['fund-logica'],'disc-cuantificadores':['disc-logica'],'disc-demostracion':['disc-cuantificadores'],'disc-induccion':['disc-demostracion'],
'disc-conteo':[],'disc-combinatoria':['disc-conteo'],'disc-inclusion':['disc-conteo','fund-operaciones'],'disc-probabilidad':['disc-combinatoria'],'disc-recurrencias':['disc-induccion'],'disc-generatrices':['disc-recurrencias','disc-combinatoria'],'disc-modular':['disc-demostracion'],'disc-grafos':['disc-conteo'],
# Métodos numéricos
'mn-errores':['calculo-derivada-3'],'mn-biseccion':['mn-errores','calculo-limite-4'],'mn-puntofijo':['mn-biseccion'],'mn-newton':['mn-puntofijo','calculo-derivada-3'],'mn-gauss':['alglin-gauss','mn-errores'],'mn-condicion':['mn-gauss'],'mn-iterativos':['mn-gauss'],
'mn-interpolacion':['mn-errores','matbas-polinomios'],'mn-splines':['mn-interpolacion'],'mn-minimos':['mn-gauss','alglin-proyeccion'],'mn-integracion':['calcint-tfc','mn-interpolacion'],'mn-edo':['mn-integracion','edo-separables'],
# Matemáticas especiales
'esp-ortogonalidad':['calcint-trig','calculo-derivada-3'],'esp-coeficientes':['esp-ortogonalidad'],'esp-gibbs':['esp-coeficientes'],'esp-parseval':['esp-coeficientes'],'esp-senoscosenos':['esp-coeficientes'],
'esp-transformada':['esp-coeficientes','calcint-impropias'],'esp-calor':['esp-coeficientes','edo-homogenea'],'esp-integral':['esp-transformada'],'esp-onda':['esp-calor'],'esp-dalembert':['esp-onda'],
'esp-complejos':['matbas-trigonometria'],'esp-cauchy':['esp-complejos','cv-parciales'],'esp-residuos':['esp-cauchy','cv-lineas'],'esp-laplace':['esp-calor','cv-rotdiv'],'esp-sturm':['esp-laplace','esp-onda'],
# Cálculo en varias variables
'cv-limites':['calculo-limite-3','geovec-r3'],'cv-parciales':['cv-limites','calculo-derivada-3'],'cv-tangente':['cv-parciales','geovec-planos'],'cv-cadena':['cv-parciales','calculo-derivada-5'],'cv-gradiente':['cv-parciales','geovec-vectores'],'cv-hessiano':['cv-gradiente','alglin-simetricas'],'cv-lagrange':['cv-gradiente','cv-hessiano'],
'cv-dobles':['calcint-tfc','geovec-area'],'cv-polares':['cv-dobles','calcint-polares'],'cv-jacobiano':['cv-polares','alglin-det'],'cv-triples':['cv-dobles','geovec-triple'],'cv-cilesf':['cv-triples','cv-polares'],'cv-aplic':['cv-dobles'],
'cv-lineas':['cv-gradiente','calcint-arco'],'cv-rotdiv':['cv-gradiente','geovec-cruz'],'cv-green':['cv-lineas','cv-dobles'],'cv-flujo':['cv-rotdiv','cv-dobles'],'cv-stokes':['cv-green','cv-flujo','cv-cilesf'],
})
