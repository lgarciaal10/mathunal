/* MathUNAL, widget "¿Te sirvió?"
   Uso. Incluir este archivo al final de la lección y llamar MathunalFeedback.init({ leccion: 'calculo-derivada-3' }).
   Por defecto NO envía nada a ningún servidor. Guarda la respuesta en el navegador de la persona.
   Para enviar, definir antes window.MATHUNAL_FEEDBACK_URL con un endpoint propio que acepte POST con JSON.
   No recoge nombre, correo ni ningún dato personal. Solo un identificador aleatorio local para no contar dos veces. */
(function () {
  'use strict';
  var KEY = 'mathunal.fb.v1';
  function read() { try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { return {}; } }
  function write(o) { try { localStorage.setItem(KEY, JSON.stringify(o)); } catch (e) {} }
  function rid() { return 'a' + Math.random().toString(36).slice(2, 10) + Date.now().toString(36); }

  var MOTIVOS = [
    ['explicacion', 'No entendí la explicación'],
    ['ejercicios', 'Los ejercicios me quedaron difíciles'],
    ['ritmo', 'Fue muy rápido o muy lento'],
    ['fallo', 'Algo no funcionó'],
    ['otro', 'Otra razón']
  ];

  function el(tag, attrs, kids) {
    var n = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (k) {
      if (k === 'text') n.textContent = attrs[k]; else n.setAttribute(k, attrs[k]);
    });
    (kids || []).forEach(function (c) { n.appendChild(c); });
    return n;
  }

  function enviar(payload) {
    var s = read(); s.respuestas = s.respuestas || []; s.respuestas.push(payload); write(s);
    var url = window.MATHUNAL_FEEDBACK_URL;
    if (!url || typeof fetch !== 'function') return Promise.resolve(false);
    return fetch(url, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload), keepalive: true })
      .then(function (r) { return r.ok; }).catch(function () { return false; });
  }

  function init(opts) {
    opts = opts || {};
    var leccion = opts.leccion || (document.title || 'leccion');
    var estado = read();
    if (!estado.id) { estado.id = rid(); write(estado); }
    var host = opts.contenedor ? document.querySelector(opts.contenedor) : document.body;
    if (!host) return;

    var caja = el('section', { 'aria-labelledby': 'fb-t', 'class': 'mu-fb', 'style': 'max-width:640px;margin:32px auto;padding:20px;border:1px solid #d9d4cc;border-radius:12px;font-family:inherit' });
    var t = el('h2', { id: 'fb-t', text: '¿Te sirvió esta lección?', style: 'margin:0 0 12px;font-size:1.1rem' });
    var fila = el('div', { role: 'group', 'aria-label': 'Tu respuesta', style: 'display:flex;gap:8px;flex-wrap:wrap' });
    var msg = el('p', { 'aria-live': 'polite', style: 'margin:12px 0 0', text: '' });
    caja.appendChild(t); caja.appendChild(fila); caja.appendChild(msg);

    function boton(txt, fn) {
      var b = el('button', { type: 'button', text: txt, style: 'padding:10px 16px;border:1px solid #E8632A;background:#fff;color:#1a1a1a;border-radius:8px;font:inherit;cursor:pointer;min-height:44px' });
      b.addEventListener('click', fn); return b;
    }

    function gracias(txt) { fila.innerHTML = ''; msg.textContent = txt; }

    function pedirMotivo(valor) {
      fila.innerHTML = '';
      msg.textContent = 'Gracias. ¿Qué fue lo que más te costó?';
      MOTIVOS.forEach(function (m) {
        fila.appendChild(boton(m[1], function () {
          enviar({ id: estado.id, leccion: leccion, valor: valor, motivo: m[0], t: new Date().toISOString() });
          gracias('Gracias, lo vamos a revisar.');
        }));
      });
    }

    [['si', 'Sí, me sirvió'], ['medio', 'Más o menos'], ['no', 'No me sirvió']].forEach(function (o) {
      fila.appendChild(boton(o[1], function () {
        if (o[0] === 'si') {
          enviar({ id: estado.id, leccion: leccion, valor: 'si', t: new Date().toISOString() });
          gracias('Gracias por contarlo.');
        } else { pedirMotivo(o[0]); }
      }));
    });

    host.appendChild(caja);
  }

  window.MathunalFeedback = { init: init, _leer: read };
})();
