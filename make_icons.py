from PIL import Image, ImageDraw
import numpy as np, math
def bez(a,b,c,n=24):
    return [((1-t)**2*a[0]+2*(1-t)*t*b[0]+t*t*c[0],(1-t)**2*a[1]+2*(1-t)*t*b[1]+t*t*c[1]) for t in [i/n for i in range(n+1)]]
def ell(cx,cy,rx,ry,rot=0,n=72):
    o=[]
    for i in range(n):
        a=2*math.pi*i/n;x=rx*math.cos(a);y=ry*math.sin(a)
        o.append((cx+x*math.cos(rot)-y*math.sin(rot),cy+x*math.sin(rot)+y*math.cos(rot)))
    return o
def icon(size):
    S=4;N=size*S;k=N/180
    yy,xx=np.mgrid[0:N,0:N]/N
    t=((xx+yy)/2)[...,None]
    bg=np.array([20,184,176])*(1-t)+np.array([11,53,102])*t
    g=(np.clip(1-np.sqrt((xx-100/180)**2+(yy-80/180)**2)/(100/180),0,1)*.3)[...,None]
    bg=bg*(1-g)+255*g
    im=Image.fromarray(bg.astype('uint8'),'RGB').convert('RGBA');dr=ImageDraw.Draw(im)
    P=lambda pts:[(x*k,y*k) for x,y in pts]
    def thick(p,q,col,w):
        dr.line(P([p,q]),fill=col,width=int(w*k))
        for pt in (p,q):
            x,y,r=pt[0]*k,pt[1]*k,w*k/2;dr.ellipse((x-r,y-r,x+r,y+r),fill=col)
    dr.polygon(P([(62,128),(22,158),(36,170),(76,146)]),fill='#232323')
    dr.line(P([(42,143),(56,158)]),fill='white',width=int(5*k))
    for i,d in enumerate([-160,-135,-110,-85,-60]):
        a=math.radians(d);L=36-abs(i-2)*3;b=(104,62)
        m=(b[0]+(L-10)*math.cos(a),b[1]+(L-10)*math.sin(a));tp=(b[0]+L*math.cos(a),b[1]+L*math.sin(a))
        thick(b,m,'#f0a35a',10);thick(m,tp,'#1d1d1d',10)
    mask=Image.new('L',(N,N),0);md=ImageDraw.Draw(mask)
    md.polygon(P(ell(88,114,42,34,-.35)),fill=255);md.polygon(P(ell(106,72,24,24)),fill=255)
    ys=np.clip((np.arange(N)/k-48)/102,0,1)[:,None,None]
    grad=np.array([249,211,163])*(1-ys)+np.array([223,132,52])*ys
    grad=np.broadcast_to(grad,(N,N,3)).astype('uint8')
    im.paste(Image.fromarray(grad,'RGB'),(0,0),mask)
    wm=Image.new('L',(N,N),0);ImageDraw.Draw(wm).polygon(P(ell(78,116,34,22,-.4)),fill=255)
    wl=Image.new('RGB',(N,N),'white');wd=ImageDraw.Draw(wl)
    c,s=math.cos(-.4),math.sin(-.4)
    for kk in range(-3,4):
        r=[(kk*12-3,-30),(kk*12+3,-30),(kk*12+3,30),(kk*12-3,30)]
        wd.polygon(P([(78+x*c-y*s,116+x*s+y*c) for x,y in r]),fill='#232323')
    im.paste(wl,(0,0),wm)
    dr=ImageDraw.Draw(im)
    dr.polygon(P(bez((126,64),(156,64),(170,96))+bez((170,96),(148,86),(126,80))),fill='#2b1d17')
    for (x,y,r,col) in [(112,68,3.6,'#111'),(113.2,66.8,1.2,'white')]:
        dr.ellipse(((x-r)*k,(y-r)*k,(x+r)*k,(y+r)*k),fill=col)
    sp=bez((148,24),(148,36),(160,36))+bez((160,36),(148,36),(148,48))+bez((148,48),(148,36),(136,36))+bez((136,36),(148,36),(148,24))
    dr.polygon(P(sp),fill='white')
    return im.convert('RGB').resize((size,size),Image.LANCZOS)
for n,s in [('apple-touch-icon.png',180),('icon-192.png',192),('icon-512.png',512)]:
    icon(s).save(n)
