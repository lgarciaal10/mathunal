const fs=require('fs');const S='/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/';
const {chromium}=require('playwright');
const AXE=fs.readFileSync(S+'pw/node_modules/axe-core/axe.min.js','utf8');
const KJS=fs.readFileSync(S+'kx/katex.min.js','utf8');
(async()=>{const b=await chromium.launch();const out={};
for(const [nom,vp] of [['d',{width:1280,height:900}],['m',{width:390,height:800}]]){
 const ctx=await b.newContext({viewport:vp});const p=await ctx.newPage();const errs=[];
 p.on('pageerror',e=>errs.push(String(e)));p.on('console',m=>{if(m.type()==='error'&&!/fonts\.g|ERR_|net::/.test(m.text()))errs.push(m.text())});
 await p.route('**/katex.min.js',r=>r.fulfill({contentType:'text/javascript',body:KJS}));
 await p.route('**/fonts.googleapis.com/**',r=>r.fulfill({contentType:'text/css',body:''}));
 await p.goto('file://'+process.cwd()+'/practica.test.html');await p.waitForSelector('.card');
 const o={};o.cards=await p.locator('.card').count();
 o.desbL=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 await p.locator('.card button').first().click();await p.waitForSelector('.op');
 o.ops=await p.locator('.op').count();
 // fallar a proposito: buscar una opcion incorrecta via datos
 const idxMal=await p.evaluate(()=>ej.ops.findIndex(o=>!o.ok));const idxOk=await p.evaluate(()=>ej.ops.findIndex(o=>o.ok));
 await p.locator('.op').nth(idxMal).click();o.fbMal=(await p.locator('.fb.mal').first().innerText()).slice(0,80);
 o.sigOculto=await p.locator('button:has-text("Otro ejercicio")').isHidden();
 await p.locator('.op').nth(idxOk).click();await p.waitForSelector('.fb.bien');o.errConservado=await p.locator('.fb.mal').count();
 o.pasos=await p.locator('.st > div').count();o.sigVisible=await p.locator('button:has-text("Otro ejercicio")').isVisible();
 o.stats=await p.locator('.stats').innerText();
 o.katexOk=await p.locator('.op .katex').count();
 o.desbE=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);
 const ax=await p.evaluate(async(src)=>{eval(src);const r=await axe.run(document,{runOnly:{type:'tag',values:['wcag2a','wcag2aa','wcag21aa','best-practice']},rules:{region:{enabled:false}}});return r.violations.map(v=>v.id+':'+v.nodes.length)},AXE);
 o.axe=ax;
 await p.locator('button:has-text("Otro ejercicio")').click();await p.waitForSelector('.op');o.otro=await p.evaluate(()=>ej.seed);
 await p.locator('button:has-text("Volver")').click();
 o.guardado=await p.evaluate(()=>localStorage.getItem('mu-practica-v1'));
 await p.locator('button:has-text("Práctica mezclada")').click();await p.waitForSelector('.op');o.mezclado=await p.evaluate(()=>pl.id);
 // recorrer los 22 temas, 1 ejercicio cada uno, sin errores
 await p.locator('button:has-text("Volver")').click();
 const n=await p.locator('.card button').count();let ok=0;
 for(let i=0;i<n;i++){await p.locator('.card button').nth(i).click();await p.waitForSelector('.op');
   const k=await p.evaluate(()=>ej.ops.findIndex(o=>o.ok));await p.locator('.op').nth(k).click();await p.waitForSelector('.fb.bien');
   const sinKatexErr=await p.evaluate(()=>!document.querySelector('.katex-error'));if(sinKatexErr)ok++;else errs.push('katex-error en '+pl.id);
   const des=await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth);if(des)errs.push('desborde en '+pl.id);
   await p.locator('button:has-text("Volver")').click();}
 o.temasOk=ok+'/'+n;o.errs=errs;out[nom]=o;await ctx.close();}
console.log(JSON.stringify(out,null,1));await b.close();})();
