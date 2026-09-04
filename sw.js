/* MathUNAL Service Worker
   - HTML: SIEMPRE de la red; solo se usa el caché si no hay conexión.
   - No se precachea el HTML (evita que una respuesta parcial de GitHub Pages
     durante un deploy quede congelada como "versión offline").
   - Resto de assets (iconos, CDN): stale-while-revalidate.
   Subir el número de CACHE en cada release. */
const CACHE = 'mathunal-v202';
const STATIC = [
  './manifest.json',
  './icon-192.png',
  './icon-512.png',
  './favicon.png',
  './qr-wa-grupo.png'
];

self.addEventListener('install', function(e){
  e.waitUntil(
    caches.open(CACHE)
      .then(function(c){ return Promise.allSettled(STATIC.map(function(u){ return c.add(u); })); })
      .then(function(){ return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function(e){
  e.waitUntil(
    caches.keys()
      .then(function(keys){ return Promise.all(keys.filter(function(k){ return k!==CACHE; }).map(function(k){ return caches.delete(k); })); })
      .then(function(){ return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function(e){
  var req = e.request;
  if (req.method !== 'GET') return;

  var isDoc = req.mode === 'navigate' ||
              (req.headers.get('accept') || '').indexOf('text/html') !== -1;

  if (isDoc) {
    // Network-first, sin fallback a HTML viejo salvo que NO haya red.
    e.respondWith(
      fetch(req).then(function(res){
        if (res && res.status === 200) {
          var copy = res.clone();
          caches.open(CACHE).then(function(c){ try{ c.put(req, copy); }catch(_){} });
        }
        return res;
      }).catch(function(){
        return caches.match(req).then(function(hit){ return hit || caches.match('./'); });
      })
    );
    return;
  }

  // Assets: responde del caché si está, y refresca en segundo plano.
  e.respondWith(
    caches.match(req).then(function(cached){
      var net = fetch(req).then(function(res){
        if (res && res.status === 200 && req.url.indexOf('http') === 0) {
          var copy = res.clone();
          caches.open(CACHE).then(function(c){ try{ c.put(req, copy); }catch(_){} });
        }
        return res;
      }).catch(function(){ return cached; });
      return cached || net;
    })
  );
});
