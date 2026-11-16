#!/usr/bin/env python3
"""Cifra las paginas de los cursos para publicarlas en una ruta que solo abre quien tenga el codigo.

Uso:
  MU_CODIGO='el-codigo' python3 cifrar.py ORIGEN DESTINO

ORIGEN trae index.html, estudio.html, formulario.html, practica.html y las lecciones como
leccion-<nombre>.html (o ya dentro de l/<nombre>.html). DESTINO es la carpeta publicada.

Cada archivo se comprime con gzip y se cifra con AES-GCM de 256 bits. La clave sale del codigo
con PBKDF2 sobre SHA-256, con sal e iv propios de cada archivo. El codigo nunca se guarda aqui.
Sin el codigo el contenido no se puede leer, ni siquiera mirando el codigo fuente de la pagina.
"""
import base64, gzip, os, re, sys, secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ITER = 200_000

PLANTILLA = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow,noarchive">
<title>MathUNAL, acceso privado</title>
<style>
:root{color-scheme:light dark;--bg:#fbf7f1;--fg:#221c16;--mu:#6b5f54;--ac:#E8632A;--ln:#e3d9cc}
@media (prefers-color-scheme:dark){:root{--bg:#17130f;--fg:#f3ebe0;--mu:#b3a595;--ln:#3a3128}}
html,body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.5 system-ui,sans-serif}
main{min-height:100vh;display:grid;place-items:center;padding:24px}
form{width:100%;max-width:360px;display:grid;gap:12px}
h1{font-size:1.3rem;margin:0}p{margin:0;color:var(--mu)}
input{font:inherit;padding:12px 14px;border:1px solid var(--ln);border-radius:10px;background:transparent;color:inherit}
button{font:inherit;font-weight:600;padding:12px;border:0;border-radius:10px;background:var(--ac);color:#fff;cursor:pointer}
#e{color:#c0392b;min-height:1.4em}
</style></head><body>
<main><form id="f" hidden>
<h1>MathUNAL</h1><p>Esta parte todavia es privada. Escribe el codigo de acceso.</p>
<input id="p" type="password" autocomplete="current-password" aria-label="Codigo de acceso" required>
<button type="submit">Entrar</button><p id="e" role="alert"></p>
</form><p id="w">Abriendo...</p></main>
<script>
(function(){
var D=/*DATOS*/,K='mu-priv-codigo';
function b(x){var s=atob(x),u=new Uint8Array(s.length);for(var i=0;i<s.length;i++)u[i]=s.charCodeAt(i);return u;}
async function abrir(pw){
  var k0=await crypto.subtle.importKey('raw',new TextEncoder().encode(pw),'PBKDF2',false,['deriveKey']);
  var k=await crypto.subtle.deriveKey({name:'PBKDF2',salt:b(D.s),iterations:D.n,hash:'SHA-256'},k0,{name:'AES-GCM',length:256},false,['decrypt']);
  var pt=await crypto.subtle.decrypt({name:'AES-GCM',iv:b(D.i)},k,b(D.c));
  var st=new Blob([pt]).stream().pipeThrough(new DecompressionStream('gzip'));
  return await new Response(st).text();
}
async function probar(pw,guardar){
  var h=await abrir(pw);
  if(guardar){try{localStorage.setItem(K,pw);}catch(e){}}
  document.open();document.write(h);document.close();
}
var f=document.getElementById('f'),w=document.getElementById('w'),e=document.getElementById('e');
function pedir(msg){w.hidden=true;f.hidden=false;e.textContent=msg||'';document.getElementById('p').focus();}
f.addEventListener('submit',function(ev){ev.preventDefault();e.textContent='';
  probar(document.getElementById('p').value,true).catch(function(){pedir('Codigo incorrecto.');});});
if(!(window.crypto&&crypto.subtle&&window.DecompressionStream)){w.textContent='Este navegador no puede abrir la pagina privada. Usa una version reciente de Chrome, Edge, Firefox o Safari.';return;}
var g=null;try{g=localStorage.getItem(K);}catch(e2){}
if(g){probar(g,false).catch(function(){try{localStorage.removeItem(K);}catch(e3){}pedir('');});}else{pedir('');}
})();
</script></body></html>
"""


def cifrar(html_bytes, codigo):
    sal = secrets.token_bytes(16)
    iv = secrets.token_bytes(12)
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=sal, iterations=ITER)
    clave = kdf.derive(codigo.encode('utf-8'))
    comp = gzip.compress(html_bytes, 9, mtime=0)
    ct = AESGCM(clave).encrypt(iv, comp, None)
    b = lambda x: base64.b64encode(x).decode()
    datos = '{"s":"%s","i":"%s","c":"%s","n":%d}' % (b(sal), b(iv), b(ct), ITER)
    return PLANTILLA.replace('/*DATOS*/', datos)


def main():
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    origen, destino = sys.argv[1], sys.argv[2]
    codigo = os.environ.get('MU_CODIGO', '')
    if len(codigo) < 12:
        sys.exit('Falta MU_CODIGO, con al menos 12 caracteres.')
    os.makedirs(os.path.join(destino, 'l'), exist_ok=True)
    n = 0
    for nombre in sorted(os.listdir(origen)):
        if not nombre.endswith('.html') or nombre.endswith('.test.html'):
            continue
        ruta = os.path.join(origen, nombre)
        m = re.match(r'leccion-(.+)\.html$', nombre)
        if m:
            sal = os.path.join(destino, 'l', m.group(1) + '.html')
        else:
            sal = os.path.join(destino, nombre)
        with open(ruta, 'rb') as f:
            datos = f.read()
        with open(sal, 'w', encoding='utf-8') as f:
            f.write(cifrar(datos, codigo))
        n += 1
    print(n, 'archivos cifrados en', destino)


if __name__ == '__main__':
    main()
