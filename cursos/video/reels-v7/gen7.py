import json,re,sys,os,subprocess,asyncio,ssl,shutil
sys.path.insert(0,'/tmp/ref/v7')
from specs7 import SPECS,OUTRO
sid=sys.argv[1];spec=[s for s in SPECS if s['id']==sid][0]
D='/tmp/ref/v7/'+sid;os.makedirs(D,exist_ok=True)
FR=[f[0] for f in spec['fr']]+OUTRO
n_math=len(spec['fr'])
# ---- voz
import edge_tts,edge_tts.communicate as C
C._SSL_CTX=ssl.create_default_context(cafile='/root/.ccr/ca-bundle.crt')
async def tts():
    res=[]
    for i,t in enumerate(FR):
        com=edge_tts.Communicate(t,'es-CO-GonzaloNeural',rate='-6%',pitch='-2Hz',boundary='WordBoundary')
        b=bytearray();ws=[]
        async for ch in com.stream():
            if ch['type']=='audio':b+=ch['data']
            elif ch['type']=='WordBoundary':ws.append((ch['text'],ch['offset']/1e7,(ch['offset']+ch['duration'])/1e7))
        open(f'{D}/s{i}.mp3','wb').write(b);res.append(ws)
    return res
if not os.path.exists(D+'/wb.json'):
    raw=asyncio.run(tts());wb=[];t=0.0;lst=[]
    for i,ws in enumerate(raw):
        d=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f'{D}/s{i}.mp3']))
        nw=len(FR[i].split())
        if len(ws)!=nw: print('AVISO palabras',i,len(ws),nw)
        for (w,a,b) in ws: wb.append([w,round(t+a,3),round(t+b,3)])
        lst.append(f"file 's{i}.mp3'");t+=d
        if i<len(raw)-1:
            subprocess.run(['ffmpeg','-v','error','-y','-f','lavfi','-i','anullsrc=r=24000:cl=mono','-t','0.55','-q:a','9',f'{D}/g{i}.mp3'],check=True);lst.append(f"file 'g{i}.mp3'");t+=.55
    open(D+'/list.txt','w').write('\n'.join(lst));json.dump(wb,open(D+'/wb.json','w'))
    subprocess.run(f'ffmpeg -v error -y -f concat -safe 0 -i {D}/list.txt -ar 44100 -ac 1 {D}/raw.wav && ffmpeg -v error -y -i {D}/raw.wav -af "highpass=f=75,equalizer=f=220:t=q:w=1:g=1.5,equalizer=f=3200:t=q:w=1.2:g=2.5,acompressor=threshold=-20dB:ratio=3:attack=8:release=120:makeup=4,aecho=0.8:0.5:35|70:0.12|0.07,loudnorm=I=-16:TP=-1.5" {D}/voz.mp3',shell=True,check=True)
    VD=float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',D+'/voz.mp3']));json.dump({'vd':VD},open(D+'/vd.json','w'))
VD=json.load(open(D+'/vd.json'))['vd']
# ---- medidas
states=[f[1] for f in spec['fr'] if f[1]]
json.dump({'r':{'fs':170,'states':states}},open(D+'/scenes.json','w'))
if not os.path.exists(D+'/measured.json'):
    subprocess.run(f'cd /tmp/ref/v7 && FMT=9x16 SCENES={D}/scenes.json OUT={D}/measured.json node measure7.js',shell=True,check=True)
DATA=open(D+'/measured.json').read()
# ---- tiempos
WB=json.load(open(D+'/wb.json'));OFF=2.8;words=[];SENT=[];i=0
for si,f in enumerate(FR):
    n=len(f.split());ws=WB[i:i+n];i+=n;SENT.append((ws[0][1]+OFF,ws[-1][2]+OFF))
    for k,w in enumerate(ws):words.append((si,k,f.split()[k],w[1]+OFF,w[2]+OFF))
FIN=round(VD+OFF+3.6,2)
A=lambda s:SENT[s][0];f2=lambda x:round(x,2)
W,Hh=1080,1920;CX=540;CY=880;SY=1264
KFS=min(170,int(980/(0.56*max(len(x) for x in spec['titulo'].split('|')))))
js=[];J=js.append
sidx=[k for k,fr in enumerate(spec['fr']) if fr[1]]  # frases con estado
first=sidx[0];ostart=n_math  # primera frase de cierre
J(f"var OFF={OFF};")
J(f"tl.fromTo('#kk0',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.6,immediateRender:false}},{f2(OFF+.1)});tl.to('#kk0',{{opacity:0,duration:.3}},{f2(A(first)-.2)});kinetic('k0',{f2(OFF+.2)},{f2(A(first)-.35)},0,0,{KFS});")
J(f"var S=new Seq('r',{CX},{CY});S.show({f2(A(first)+.15)});")
gos=[];fx=[];notes=[]
for j,k in enumerate(sidx):
    if j>0:
        T=A(k)+.05;J(f"S.go({j},{f2(T)});");gos.append(T)
    nt=spec['fr'][k][2]
    if nt:
        T=A(k)+.9;nxt=A(k+1)-.2
        J(f"note({f2(T)},{CX},{SY},{json.dumps(nt)},'#6FB1FF',0,{f2(nxt)});");notes.append(T)
    if spec['fr'][k][3]=='ring':
        T=A(k)+1.4;J(f"ring({f2(T)},{CX},{CY},'#FFB48A',7);burst({f2(T)},{CX},{CY},30,['#FF8A4C','#FFD166','#fff','#6FB1FF'],300);");fx.append(T)
J(f"S.hide({f2(A(ostart)-.35)});")
J(f"kinetic('k8',{f2(A(ostart)+.1)},{f2(FIN)});note({f2(A(ostart+1)-.1)},{CX},{SY},'Practica con preguntas reales de parciales','#FFFFFF',0);")
J(f"var ct=document.getElementById('cta');tl.fromTo(ct,{{opacity:0,scale:.3}},{{opacity:1,scale:1,duration:.7,ease:'elastic.out(1,.5)',immediateRender:false}},{f2(A(ostart+1)+1.4)});ring({f2(A(ostart+1)+1.4)},{CX},1400,'#FF8A4C',8);burst({f2(A(ostart+1)+1.4)},{CX},1400,44,['#FF8A4C','#FFD166','#3DDC84','#6FB1FF','#fff'],420);flash({f2(A(ostart+1)+1.4)},'#fff',.35);")
# hud
marks=[0,first,ostart-1,ostart];labels=['Pregunta','Paso a paso','Resultado','Cierre']
J("var HL=document.getElementById('hudl');")
for p,(m,lab) in enumerate(zip([0,first,max(first+1,(first+ostart)//2),ostart],['La pregunta','Paso a paso','Resultado','Cierre'])):
    t=OFF if m==0 else A(m)
    J(f"tl.to('#pl{p}',{{backgroundColor:'#FF8A4C',duration:.4}},{f2(t)});tl.call(function(){{HL.textContent={json.dumps(lab)}}},null,{f2(t)});")
# subtitulos
chunks=[]
for si,fr in enumerate(FR):
    ws=[w for w in words if w[0]==si];cur=[]
    for w in ws:
        cur.append(w)
        if (len(cur)>=4 and re.search(r'[.,]$',w[2])) or len(cur)>=6:chunks.append(cur);cur=[]
    if cur:
        if chunks and len(cur)<=2 and chunks[-1][0][0]==si:chunks[-1]+=cur
        else:chunks.append(cur)
caps='';wid=0
for ci,ch in enumerate(chunks):
    a=ch[0][3];nxt=chunks[ci+1][0][3] if ci+1<len(chunks) else FIN
    bb=nxt if nxt-ch[-1][4]<.9 else ch[-1][4]+.3;spans=''
    for w in ch:
        spans+=f'<span class="w" id="w{wid}">{w[2]}</span> '
        J(f'tl.to("#w{wid}",{{backgroundColor:"#FF8A4C",color:"#0A0F1F",scale:1.06,duration:.1}},{f2(w[3])});tl.to("#w{wid}",{{backgroundColor:"rgba(255,138,76,0)",color:"#F4F6FF",scale:1,duration:.2}},{f2(w[4])});');wid+=1
    caps+=f'<div id="cap{ci}" class="clip capc" data-start="{f2(a)}" data-duration="{f2(bb-a)}" data-track-index="{3+ci%2}"><div class="cap">{spans}</div></div>'
PT=''.join(f'<div class="pt2" style="left:{(i*173)%1000}px;top:{(i*311)%1800+60}px;font-size:{40+(i%4)*18}px;opacity:{.05+(i%3)*.03}" id="pt{i}">{["+","−","×","÷","=","x²","√","π","∫","Σ"][i%10]}</div>' for i in range(26))
for i in range(26):J(f'tl.to("#pt{i}",{{y:{-80-(i%5)*50},x:{(i%7-3)*26},rotation:{(i%5-2)*14},duration:{FIN},ease:"none"}},0);')
J(f'tl.fromTo("#bar",{{scaleX:0}},{{scaleX:1,duration:{FIN},ease:"none"}},0);tl.fromTo("#cam",{{scale:1}},{{scale:1.035,duration:{FIN},ease:"none"}},0);')
J(f'tl.fromTo("#lg",{{opacity:0,scale:.82,letterSpacing:"26px"}},{{opacity:1,scale:1,letterSpacing:"2px",duration:1.0,ease:"power3.out",immediateRender:false}},.25);tl.to("#lgl",{{width:520,duration:.8,ease:"power2.inOut"}},.75);tl.fromTo("#lgs",{{opacity:0,y:14}},{{opacity:1,y:0,duration:.7,immediateRender:false}},1.05);tl.to("#intro",{{opacity:0,duration:.6,ease:"power1.in"}},{f2(OFF-.55)});tl.set("#intro",{{display:"none"}},{f2(OFF+.1)});')
css=open('/tmp/ref/v7/style6t.css').read()
for k,v in {'%W%':W,'%H%':Hh,'%CX%':CX,'%CY%':CY,'%KKT%':200,'%ULL%':150,'%ULT%':905,'%CTL%':290,'%CTT%':1340,'%CAL%':60,'%CAT%':1500,'%CAW%':960,'%CAH%':320,'%CAW2%':920,'%CAF%':70}.items():css=css.replace(k,str(v))
engine=open('/tmp/ref/v7/engine6.js').read()
HD=D+'/hf'
if not os.path.exists(HD):
    shutil.copytree('/tmp/ref/v6/hf',HD,ignore=shutil.ignore_patterns('.hyperframes','index.html'))
title=spec['titulo']
html=f'''<!doctype html>
<html lang="es"><head><meta charset="UTF-8"/><meta name="viewport" content="width={W}, height={Hh}"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<link rel="stylesheet" href="assets/katex.css"/>
<style>{css}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{FIN}" data-width="{W}" data-height="{Hh}">
<audio id="voz" src="assets/mix.mp3" data-start="0" data-duration="{FIN}" data-track-index="0"></audio>
<div id="bg"></div><div id="dots"></div><div class="blob" id="b1"></div><div class="blob" id="b2"></div><div class="blob" id="b3"></div>{PT}
<div id="cam"><div id="world"><div id="ann">
<div class="kin" id="k0" data-t="{title}" style="top:560px"></div>
<div class="kin" id="k8" data-t="Lo hiciste|muy bien" style="top:600px"></div><div id="cta">mathunal.com</div>
</div></div></div>
<div class="kk" id="kk0">{spec['curso']}</div>
<div class="brand">MATH<b>UNAL</b></div><div id="hud">{''.join(f'<div class="pill" id="pl{i}"></div>' for i in range(4))}</div><div id="hudl">{spec['curso']}</div>
{caps}
<div id="flash"></div><div id="bar"></div><div id="vig"></div><div id="grain"></div>
<div id="intro"><div id="lg">MATH<b>UNAL</b></div><div id="lgl"></div><div id="lgs">{spec['curso']}</div></div>
<script>window.__timelines=window.__timelines||{{}};
var DATA={DATA};
{engine.replace('CX=540,CY=840','CX=540,CY=880')}
{chr(10).join(js)}
window.__timelines["main"]=tl;tl.seek(0);</script></div></body></html>'''
open(HD+'/index.html','w').write(html)
sf={'off':OFF,'fin':FIN,'bounds':[A(first)-.3,A(ostart)-.3],'go':[g-.1 for g in gos],'chips':notes,'check':[],'bad':[],'boom':[],'res':fx,'cta':[A(ostart+1)+1.4],'hole':[],'big':[],'riser':[f-.9 for f in fx]}
json.dump(sf,open(D+'/sfx.json','w'))
subprocess.run(f'cd /tmp/ref/v7 && python3 mkaudio7.py {D}/sfx.json {D}/voz.mp3 {D}',shell=True,check=True)
shutil.copy(D+'/mix.mp3',HD+'/assets/mix.mp3')
print('listo',sid,FIN)
