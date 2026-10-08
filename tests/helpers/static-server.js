// Servidor estático mínimo (sin dependencias) para servir el repo en las pruebas.
// MU_ROOT = carpeta a servir (por defecto la raíz del repo); MU_PORT = puerto (por defecto 4173).
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(process.env.MU_ROOT || path.join(__dirname, '..', '..'));
const PORT = Number(process.env.MU_PORT || 4173);
const TYPES = {
  '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8', '.json': 'application/json',
  '.css': 'text/css; charset=utf-8', '.png': 'image/png', '.jpg': 'image/jpeg', '.svg': 'image/svg+xml',
  '.pdf': 'application/pdf', '.xml': 'application/xml', '.txt': 'text/plain; charset=utf-8', '.ico': 'image/x-icon',
};

http.createServer((req, res) => {
  let p = decodeURIComponent(req.url.split('?')[0]);
  if (p.endsWith('/')) p += 'index.html';
  const file = path.normalize(path.join(ROOT, p));
  if (!file.startsWith(ROOT)) { res.writeHead(403); return res.end(); }
  fs.stat(file, (err, st) => {
    if (err || !st.isFile()) {
      // como GitHub Pages: 404.html si existe
      const nf = path.join(ROOT, '404.html');
      res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
      return fs.existsSync(nf) ? fs.createReadStream(nf).pipe(res) : res.end('404');
    }
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream', 'Cache-Control': 'no-store' });
    fs.createReadStream(file).pipe(res);
  });
}).listen(PORT, '127.0.0.1', () => console.log(`Sirviendo ${ROOT} en http://127.0.0.1:${PORT}`));
