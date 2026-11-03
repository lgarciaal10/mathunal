#!/usr/bin/env python3
"""Agrupa por tema las preguntas que saca extraer-banco.js (bank.json) y escribe mapa-temas.json.
Uso  python3 agregar-temas.py carpeta/con/bank.json"""
import json, collections, re, sys, os
B = sys.argv[1] if len(sys.argv) > 1 else '.'
d = json.load(open(os.path.join(B, 'bank.json'), encoding='utf8'))
MAT = {'calcdif': 'Cálculo Diferencial', 'calcint': 'Cálculo Integral', 'calcvec': 'Cálculo en Varias Variables'}
out = {'fuente': 'index.html subido por Luis (banco EXAMS y SIM_NEW)', 'aviso': 'Sale del banco de MathUNAL y no del programa oficial de la materia', 'materias': {}}
for m, nombre in MAT.items():
    ex = {}
    for r in d['rows']:
        if r['exam'].startswith(m + '_'):
            e = ex.setdefault(r['exam'], {'semestre': r['semestre'], 'n': 0}); e['n'] += 1
    tipo = lambda k: 'corte' if re.search(r'_c\d$', k) else 'parcial'
    parc = [k for k in ex if tipo(k) == 'parcial']
    temas = collections.OrderedDict()
    def t(n): return temas.setdefault(n, {'tema': n, 'parciales_n': 0, 'parciales_examenes': set(), 'simulacros_n': 0, 'cortes': collections.Counter(), 'freq': collections.Counter(), 'error': collections.Counter(), '_h': set()})
    for r in d['rows']:
        if not r['exam'].startswith(m + '_'): continue
        x = t(r['tema'])
        if tipo(r['exam']) == 'parcial': x['parciales_n'] += 1; x['parciales_examenes'].add(r['exam'])
        else:
            if r['h'] in x['_h']: continue
            x['_h'].add(r['h']); x['simulacros_n'] += 1
        c = r['corte']
        if c is None and re.search(r'_c(\d)$', r['exam']): c = int(re.search(r'_c(\d)$', r['exam']).group(1))
        if c is not None: x['cortes'][c] += 1
        x['freq'][r['freq']] += 1; x['error'][r['tipoError']] += 1
    for r in d['sim']:
        if r['materia'] != m: continue
        x = t(r['tema'])
        if r['h'] in x['_h']: continue
        x['_h'].add(r['h']); x['simulacros_n'] += 1
        if r['corte'] is not None: x['cortes'][r['corte']] += 1
        x['freq'][r['freq']] += 1; x['error'][r['tipoError']] += 1
    lst = []
    for v in temas.values():
        corte = v['cortes'].most_common(1)[0][0] if v['cortes'] else None
        lst.append({'tema': v['tema'], 'corte': corte, 'cortes': dict(sorted(v['cortes'].items())), 'parciales_n': v['parciales_n'], 'parciales_con_el_tema': len(v['parciales_examenes']), 'simulacros_n': v['simulacros_n'], 'total': v['parciales_n'] + v['simulacros_n'], 'freq': dict(v['freq']), 'error': dict(v['error'])})
    lst.sort(key=lambda a: (a['corte'] or 9, -a['total'], a['tema']))
    out['materias'][m] = {'nombre': nombre, 'examenes_parcial': [{'clave': k, 'semestre': ex[k]['semestre'], 'preguntas': ex[k]['n']} for k in parc], 'examenes_corte': [{'clave': k, 'semestre': ex[k]['semestre'], 'preguntas': ex[k]['n']} for k in ex if tipo(k) == 'corte'], 'n_parciales': len(parc), 'temas': lst}
json.dump(out, open(os.path.join(B, 'mapa-temas.json'), 'w', encoding='utf8'), ensure_ascii=False, indent=1)
print('listo')
