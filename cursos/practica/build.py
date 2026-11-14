"""Arma practica.html a partir de tpl.html, gen.js y los enlaces de las lecciones."""
import json,sys
S='/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/'
tpl=open('tpl.html',encoding='utf-8').read()
gen=open('gen.js',encoding='utf-8').read()
css=open(S+'kx/katex-inline.css',encoding='utf-8').read()
ids=json.load(open(S+'stem2id.json'))
lecs={k:'https://claude.ai/artifact/'+v for k,v in ids.items()}
out=tpl.replace('/*KATEXCSS*/',css).replace('/*GEN*/',gen).replace('/*LECS*/',json.dumps(lecs))
open('practica.html','w',encoding='utf-8').write(out)
open('practica.test.html','w',encoding='utf-8').write('<!doctype html><meta charset="utf-8">'+out)
print(len(out))
