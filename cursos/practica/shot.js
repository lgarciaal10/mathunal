const fs=require('fs');const {chromium}=require('playwright');const KJS=fs.readFileSync('/tmp/claude-0/-home-user-mathunal/9faafdd8-c612-508f-bc32-bfaf0ebbc107/scratchpad/kx/katex.min.js','utf8');
(async()=>{const b=await chromium.launch();
for(const [n,vp] of [['d',{width:1100,height:820}],['m',{width:390,height:800}]]){
const p=await (await b.newContext({viewport:vp})).newPage();
await p.route('**/*',r=>{const u=r.request().url();if(/katex\.min\.js/.test(u))return r.fulfill({contentType:'text/javascript',body:KJS});if(/fonts\.g/.test(u))return r.fulfill({contentType:'text/css',body:''});return r.continue()});
await p.goto('file://'+process.cwd()+'/practica.test.html');await p.waitForSelector('.card');
await p.screenshot({path:'/tmp/ref/pr-'+n+'-lista.png'});
await p.evaluate(()=>abrir(MUPractica.plantillas.find(x=>x.id==='eig-2'),false));await p.waitForSelector('.op');
const m=await p.evaluate(()=>ej.ops.findIndex(o=>!o.ok));await p.locator('.op').nth(m).click();
await p.screenshot({path:'/tmp/ref/pr-'+n+'-mal.png',fullPage:true});
const k=await p.evaluate(()=>ej.ops.findIndex(o=>o.ok));await p.locator('.op').nth(k).click();await p.waitForTimeout(200);
await p.screenshot({path:'/tmp/ref/pr-'+n+'-bien.png',fullPage:true});}
await b.close();})();
