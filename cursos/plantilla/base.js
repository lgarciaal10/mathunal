/* base común: tema, variantes y KaTeX */
(function(){
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  window.MU = { RM: RM };
  var root = document.documentElement, THEMES=['dark','black','gray','light'], NAMES={dark:'Azul',black:'Negro',gray:'Gris',light:'Claro'};
  function sysTheme(){ return (window.matchMedia && matchMedia('(prefers-color-scheme: light)').matches) ? 'light' : 'dark'; }
  function current(){ var t = root.getAttribute('data-theme'); return THEMES.indexOf(t)>=0 ? t : sysTheme(); }
  function paintThemes(){ var box=document.getElementById('theme'); if(!box) return; var cur=current();
    box.className='themes'; box.setAttribute('role','group'); box.setAttribute('aria-label','Tema de color');
    box.innerHTML=THEMES.map(function(t){ return '<button type="button" data-t="'+t+'" aria-pressed="'+(t===cur)+'" aria-label="Tema '+NAMES[t]+'"><i></i></button>'; }).join(''); }
  try { var saved = localStorage.getItem('mu-theme'); if(THEMES.indexOf(saved)>=0) root.setAttribute('data-theme', saved); } catch(e){}
  paintThemes();
  var tb = document.getElementById('theme');
  if(tb) tb.addEventListener('click', function(e){ var b=e.target.closest('button[data-t]'); if(!b) return; var n=b.getAttribute('data-t'); root.setAttribute('data-theme', n);
    try{ localStorage.setItem('mu-theme', n); }catch(e2){} paintThemes(); document.dispatchEvent(new CustomEvent('mu-theme')); });
  // variantes
  var tabs = [].slice.call(document.querySelectorAll('.tab')), vars = [].slice.call(document.querySelectorAll('.var'));
  function show(id){
    tabs.forEach(function(t){ t.setAttribute('aria-selected', t.getAttribute('data-v')===id ? 'true':'false'); });
    vars.forEach(function(v){ var on = v.id===id; v.classList.toggle('on', on); if(on){ v.dispatchEvent(new CustomEvent('mu-show')); } });
    try{ window.scrollTo(0,0); }catch(e){}
  }
  tabs.forEach(function(t){ t.addEventListener('click', function(){ show(t.getAttribute('data-v')); }); });
  window.MU.show = show;
  // KaTeX
  window.MU.math = function(scope){
    if(typeof katex==='undefined') return false;
    [].forEach.call((scope||document).querySelectorAll('[data-tex]:not([data-done])'), function(el){
      try{
        var tx=el.getAttribute('data-tex'), tps=tx.match(/\\text\{[^{}]*\}/g);
        if(tps && tps.join('').length>45){
          /* enunciado con mucha prosa, se parte en texto que baja de renglón y fórmulas en línea */
          el.textContent=''; el.className=(el.className?el.className+' ':'')+'mixto';
          tx.split(/(\\text\{[^{}]*\})/).forEach(function(pz){
            if(!pz.trim()) return;
            var m=pz.match(/^\\text\{([^{}]*)\}$/);
            if(m){ el.appendChild(document.createTextNode(m[1])); }
            else { var sp=document.createElement('span'); el.appendChild(sp); katex.render(pz,sp,{throwOnError:false}); }
          });
          el.setAttribute('data-done','1');
        } else { katex.render(tx, el, { throwOnError:false, displayMode: el.hasAttribute('data-block') }); el.setAttribute('data-done','1'); }
      }catch(e){}
    });
    return true;
  };
  function tryMath(n){ if(window.MU.math()) return; if(n>0) setTimeout(function(){ tryMath(n-1); }, 150); }
  window.addEventListener('load', function(){ tryMath(40); });
  window.MU.ready = function(fn){ if(document.readyState==='complete') fn(); else window.addEventListener('load', fn); };
  show(tabs.length ? tabs[0].getAttribute('data-v') : '');
})();
