import json,subprocess,numpy as np
from scipy.signal import butter,lfilter
from scipy.io import wavfile
sr=44100
import sys
cfg=json.load(open(sys.argv[1])); OFF=cfg['off']; FIN=cfg['fin']
subprocess.run(['ffmpeg','-v','error','-y','-i',sys.argv[2],'-ar',str(sr),'-ac','1',sys.argv[3]+'/voz.wav'],check=True)
_,v=wavfile.read(sys.argv[3]+'/voz.wav'); v=v.astype(np.float32)/32768
N=int(FIN*sr); out_v=np.zeros(N,np.float32); o=int(OFF*sr); out_v[o:o+len(v)]=v[:N-o]
t=np.arange(N)/sr
def lp(x,f,order=2): b,a=butter(order,f/(sr/2)); return lfilter(b,a,x)
def bp(x,f1,f2): b,a=butter(2,[f1/(sr/2),f2/(sr/2)],btype='band'); return lfilter(b,a,x)
rng=np.random.default_rng(7)
# musica: pad lento + pulso suave
chords=[[57,60,64],[53,57,60],[48,52,55],[55,59,62]]  # Am F C G
hz=lambda m:440*2**((m-69)/12)
music=np.zeros(N,np.float32)
CL=7.0
for k in range(int(FIN/CL)+1):
    a=int(k*CL*sr); b=min(N,int((k+1)*CL*sr))
    if a>=N: break
    tt=np.arange(b-a)/sr
    env=np.minimum(1,tt/1.6)*np.minimum(1,(CL-tt)/1.8).clip(0)
    ch=chords[k%4]
    seg=np.zeros(b-a,np.float32)
    for m in ch:
        for d in (-0.15,0.15):
            f=hz(m)*(1+d/100)
            seg+=np.sin(2*np.pi*f*tt)*0.5+np.sin(2*np.pi*2*f*tt)*0.12
    seg+=np.sin(2*np.pi*hz(ch[0]-24)*tt)*0.7
    music[a:b]+=seg*env*0.05
# arpegio suave
step=0.5
for i in range(int(FIN/step)):
    ti=i*step; k=int(ti//CL); ch=chords[k%4]
    m=ch[i%3]+12*(1+(i//3)%2)
    a=int(ti*sr); L=int(0.9*sr)
    if a+L>=N: break
    tt=np.arange(L)/sr
    music[a:a+L]+=np.sin(2*np.pi*hz(m)*tt)*np.exp(-tt*5)*0.035
music=lp(music,3200)
# ducking por envolvente de voz
env=np.abs(out_v); env=lp(env,6)*8; env=np.clip(env,0,1)
duck=1-0.6*env
music=music*duck.astype(np.float32)
# fade musica entrada/salida
music*=np.minimum(1,t/2.0)*np.minimum(1,(FIN-t)/2.5).clip(0)
sf=np.zeros(N,np.float32)
def add(x,tm,g=1.0):
    a=int(tm*sr)
    if a<0 or a>=N: return
    x=x[:N-a]; sf[a:a+len(x)]+=x*g
def whoosh(d=0.7):
    n=int(d*sr); x=rng.standard_normal(n).astype(np.float32); tt=np.arange(n)/sr
    x=bp(x,400,3500); x*=np.sin(np.pi*np.clip(tt/d,0,1))**2
    return x*0.35
def pop(f=700):
    n=int(0.18*sr); tt=np.arange(n)/sr
    return (np.sin(2*np.pi*(f+500*np.exp(-tt*30))*tt)*np.exp(-tt*28)*0.5).astype(np.float32)
def ding(f=1175):
    n=int(0.9*sr); tt=np.arange(n)/sr
    return ((np.sin(2*np.pi*f*tt)+0.4*np.sin(2*np.pi*2*f*tt))*np.exp(-tt*5)*0.3).astype(np.float32)
def buzz():
    n=int(0.35*sr); tt=np.arange(n)/sr
    x=np.sign(np.sin(2*np.pi*110*tt))*np.exp(-tt*6)*0.18
    return lp(x.astype(np.float32),900)
def chime():
    out=np.zeros(int(1.6*sr),np.float32)
    for i,m in enumerate([72,76,79,84]):
        n=int(1.1*sr); tt=np.arange(n)/sr; a=int(i*0.11*sr)
        out[a:a+n]+=(np.sin(2*np.pi*hz(m)*tt)*np.exp(-tt*3.5)*0.25).astype(np.float32)
    return out
for b in cfg['bounds'][1:-1]: add(whoosh(),b-0.45)
add(whoosh(0.9),0.3,0.8); add(whoosh(0.7),OFF-0.55,0.6)
for t0 in cfg['chips']: add(pop(),t0)
for t0 in cfg['check']: add(ding(),t0)
for t0 in cfg['bad']: add(buzz(),t0)
for t0 in cfg['res']+cfg['cta']+cfg['big']: add(chime(),t0)
for t0 in cfg['hole']: add(pop(520),t0)

def boom():
    n=int(1.6*sr);tt=np.arange(n)/sr
    x=np.sin(2*np.pi*(55*np.exp(-tt*2.2)+30)*tt)*np.exp(-tt*2.6)*0.9
    nz=lp(rng.standard_normal(n).astype(np.float32),1800)*np.exp(-tt*5)*0.5
    return (x+nz).astype(np.float32)
def riser(d=1.0):
    n=int(d*sr);tt=np.arange(n)/sr;f=300+1800*(tt/d)**2
    x=np.sin(2*np.pi*np.cumsum(f)/sr)*(tt/d)**2*0.18
    nz=bp(rng.standard_normal(n).astype(np.float32),800,5000)*(tt/d)**3*0.25
    return (x+nz).astype(np.float32)
for t0 in cfg.get('go',[]): add(whoosh(0.8),t0-0.1,0.7)
for t0 in cfg.get('boom',[]): add(boom(),t0)
for t0 in cfg.get('riser',[]): add(riser(1.0),t0)
mix=out_v*1.0+music+sf*0.9
mix=mix/np.max(np.abs(mix))*0.92
wavfile.write(sys.argv[3]+'/mix.wav',sr,(mix*32767).astype(np.int16))
subprocess.run(['ffmpeg','-v','error','-y','-i',sys.argv[3]+'/mix.wav','-b:a','192k',sys.argv[3]+'/mix.mp3'],check=True)
print('ok',FIN)
