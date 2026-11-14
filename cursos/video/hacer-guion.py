#!/usr/bin/env python3
"""Arma src/guiones/<id>.json a partir del audio y de las frases del guion.
Uso: python3 hacer-guion.py <id>
Las frases (una por parrafo del texto que se mando a la voz) y las escenas estan en GUIONES."""
import json, re, subprocess, sys
GUIONES = json.load(open('guiones-fuente.json'))
def tiempos(audio, frases):
    out = subprocess.run(f"ffmpeg -hide_banner -i public/{audio} -af silencedetect=noise=-38dB:d=0.28 -f null - 2>&1", shell=True, capture_output=True, text=True).stdout
    st = [float(x) for x in re.findall(r'silence_start: ([\d.]+)', out)]
    du = [float(x) for x in re.findall(r'silence_duration: ([\d.]+)', out)]
    sil = [(a, a + d) for a, d in zip(st, du)]
    dur = float(subprocess.run(f"ffprobe -v error -show_entries format=duration -of csv=p=0 public/{audio}", shell=True, capture_output=True, text=True).stdout)
    tot = sum(len(s) for s in frases); cum = 0; fr = [0.0]; usados = set()
    for s in frases[:-1]:
        cum += len(s); exp = dur * cum / tot
        c = min((x for x in sil if x not in usados), key=lambda x: abs((x[0] + x[1]) / 2 - exp)); usados.add(c); fr.append(c)
    res = []
    for i, s in enumerate(frases):
        a = 0.0 if i == 0 else fr[i][1]; b = fr[i + 1][0] if i < len(frases) - 1 else dur
        res.append({'t': s, 'a': round(a, 2), 'b': round(b, 2)})
    return res, dur
if __name__ == '__main__':
    k = sys.argv[1]; g = GUIONES[k]
    sent, dur = tiempos(g['audio'], g['frases'])
    json.dump({'audio': g['audio'], 'fin': round(dur + 0.9, 2), 'sent': sent, 'escenas': g['escenas']}, open(f'src/guiones/{k}.json', 'w'), ensure_ascii=False, indent=1)
    for i, s in enumerate(sent): print(i, s['a'], s['b'], s['t'][:60])
