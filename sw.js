/* MathUNAL Service Worker — offline-first para app shell, network-first para CDN
   NOTA: actualmente NO se registra desde index.html (se quitó el 2026-07-27).
   Si se vuelve a activar, subir el número de CACHE en cada release. */
const CACHE = 'mathunal-v201';
const SHELL = [
  './',
  './index.html',
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './favicon.png',
  './qr-wa-grupo.png'
];
const CDN = [
  'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css',
  'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js',
  'https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js'
];

self.addEventListener('install', function(e){
  e.waitUntil(
    caches.open(CACHE).then(function(c){
      // Cachea el shell local; intenta el CDN sin bloquear la instalación si falla
      return c.addAll(SHELL).then(function(){
        return Promise.allSettled(CDN.map(function(u){
          return fetch(u, {mode:'cors'}).then(function(r){ if(r.ok) return c.put(u, r); });
        }));
      });
    }).then(function(){ return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function(e){
  e.waitUntil(
    caches.keys().then(function(keys){
      return Promise.all(keys.filter(function(k){return k!==CACHE;}).map(function(k){return caches.delete(k);}));
    }).then(function(){ return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function(e){
  var req = e.request;
  if (req.method !== 'GET') return;
  // Para el HTML: network-first (evita servir una versión vieja de la app).
  var isDoc = req.mode === 'navigate' ||
              (req.headers.get('accept') || '').indexOf('text/html') !== -1;
  if (isDoc) {
    e.respondWith(
      fetch(req).then(function(res){
        if (res && res.status === 200) {
          var copy = res.clone();
          caches.open(CACHE).then(function(c){ try{ c.put(req, copy); }catch(_){} });
        }
        return res;
      }).catch(function(){ return caches.match(req).then(function(c){ return c || caches.match('./index.html'); }); })
    );
    return;
  }
  // Resto de assets: stale-while-revalidate.
  e.respondWith(
    caches.match(req).then(function(cached){
      var net = fetch(req).then(function(res){
        if (res && res.status === 200 && req.url.startsWith('http')) {
          var copy = res.clone();
          caches.open(CACHE).then(function(c){ try{ c.put(req, copy); }catch(_){} });
        }
        return res;
      }).catch(function(){ return cached; });
      return cached || net;
    })
  );
});
