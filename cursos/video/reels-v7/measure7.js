const FMT=process.env.FMT||'9x16';const DIM={'9x16':[1080,1920],'16x9':[1920,1080],'3x4':[1080,1440],'4x3':[1440,1080]}[FMT];const MAXW=Math.floor(DIM[0]*0.8)*(DIM[0]>DIM[1]?0.72:1);const CAP=Math.floor(DIM[1]*(DIM[0]>DIM[1]?0.15:(DIM[1]>1500?0.0885:0.1)));
const {chromium}=require('/opt/node-tools/node_modules/playwright');const fs=require('fs');
(async()=>{const S=JSON.parse(fs.readFileSync(process.env.SCENES||'scenes.json','utf8'));
const b=await chromium.launch({args:['--no-sandbox']});const p=await b.newPage({viewport:{width:1200,height:900}});
await p.goto('file:///tmp/ref/v6/hf/assets/measure.html');await p.waitForTimeout(500);
const out=await p.evaluate(async([S,MAXW,CAP])=>{
 function measure(latex,fs,host){host.style.fontSize=fs+'px';host.innerHTML='';katex.render(latex,host,{throwOnError:false,output:'html',trust:true});
  const root=host.querySelector('.katex-html'),rr=root.getBoundingClientRect(),gl=[],br=[];
  root.querySelectorAll('*').forEach(e=>{
   if(e.classList.contains('frac-line')){const r=e.getBoundingClientRect(),cs=getComputedStyle(e);br.push({x:r.left-rr.left,y:r.top-rr.top,w:r.width,h:Math.max(2,parseFloat(cs.borderBottomWidth)||r.height)});return}
   if(e.children.length===0){const t=(e.textContent||'').replace(/[​\s]/g,'');if(!t)return;const r=e.getBoundingClientRect(),cs=getComputedStyle(e);
    gl.push({k:t,text:e.textContent,x:r.left-rr.left,y:r.top-rr.top,w:r.width,h:r.height,fs:parseFloat(cs.fontSize),color:cs.color,ff:cs.fontFamily,fst:cs.fontStyle,fw:cs.fontWeight})}});
  return {gl,br,w:rr.width,h:rr.height}}
 const host=document.getElementById('h');await document.fonts.ready;
 const res={};
 for(const id in S){let fs=S[id].fs;let G=S[id].states.map(s=>measure(s,fs,host));
  const mw=Math.max(...G.map(g=>g.w));if(true){fs=Math.min(CAP,Math.floor(fs*MAXW/mw));G=S[id].states.map(s=>measure(s,fs,host))}
  res[id]={fs,states:G}}
 return res},[S,MAXW,CAP]);
fs.writeFileSync(process.env.OUT||('measured_'+FMT+'.json'),JSON.stringify(out));console.log(Object.keys(out).map(k=>k+':'+out[k].fs+' '+out[k].states.map(s=>Math.round(s.w)+'x'+Math.round(s.h)).join(',')).join('\n'));
await b.close()})();
