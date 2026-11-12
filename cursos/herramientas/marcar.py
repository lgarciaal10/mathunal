import json,sys
tema,arch=sys.argv[1],sys.argv[2]
p='/home/user/mathunal/cursos/datos/estructuras/calcint.json'
d=json.load(open(p));ok=False
for m in d['modulos']:
    for l in m['lecciones']:
        if l['tema']==tema: l['estado']='borrador para revisión'; l['leccion']='lecciones/'+arch; ok=True
assert ok,tema
json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
