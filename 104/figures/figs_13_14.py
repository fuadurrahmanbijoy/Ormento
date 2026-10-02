#!/usr/bin/env python3
# Figures for Ch XIII-XIV. Run: python3 figs_13_14.py  (writes 4 svg files beside it)
F="font-family=\"'Libre Caslon Text',Georgia,serif\" font-size=\"11\" fill=\"#1a1612\""
def fig(name,xm,ym,xt,yt,body,xl,yl='Price (Tk)'):
    X=lambda q:50+q/xm*340; Y=lambda p:250-p/ym*225
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 420 295" fill="none" stroke="#1a1612" stroke-width="1.2" stroke-linecap="round">',
    '<defs><pattern id="h" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0v5" stroke-width=".6"/></pattern>'
    '<pattern id="c" width="5" height="5" patternUnits="userSpaceOnUse"><path d="M0 0v5M0 0h5" stroke-width=".4"/></pattern>'
    '<pattern id="d" width="3" height="3" patternUnits="userSpaceOnUse" patternTransform="rotate(-45)"><path d="M0 0v3" stroke-width="1"/></pattern></defs>',
    f'<path d="M{X(0)} {Y(ym)-4}V{Y(0)}H{X(xm)+6}"/>']
    for v in xt: o.append(f'<path d="M{X(v)} {Y(0)}v4" stroke-width=".8"/><text x="{X(v)}" y="{Y(0)+15}" text-anchor="middle" stroke="none" {F}>{v}</text>')
    for v in yt: o.append(f'<path d="M{X(0)} {Y(v)}h-4" stroke-width=".8"/><text x="{X(0)-7}" y="{Y(v)+4}" text-anchor="end" stroke="none" {F}>{v}</text>')
    o.append(f'<text x="{X(xm)}" y="{Y(0)+30}" text-anchor="end" stroke="none" {F} font-style="italic">{xl}</text>')
    o.append(f'<text x="8" y="14" stroke="none" {F} font-style="italic">{yl}</text>')
    o+=body(X,Y); o.append('</svg>'); open(name,'w').write('\n'.join(o))
def L(X,Y,pts,w=1.6,dash=None):
    d='M'+' L'.join(f'{X(a):.1f} {Y(b):.1f}' for a,b in pts)
    return f'<path d="{d}" stroke-width="{w}"'+(f' stroke-dasharray="{dash}"' if dash else '')+'/>'
def T(X,Y,q,p,s,a='start',dx=0,dy=0,i=False):
    return f'<text x="{X(q)+dx:.1f}" y="{Y(p)+dy:.1f}" text-anchor="{a}" stroke="none" {F}'+(' font-style="italic"' if i else '')+f'>{s}</text>'
def dot(X,Y,q,p): return f'<circle cx="{X(q):.1f}" cy="{Y(p):.1f}" r="3" fill="#1a1612"/>'
def poly(X,Y,pts,fill): return '<path d="M'+' L'.join(f'{X(a):.1f} {Y(b):.1f}' for a,b in pts)+f'Z" fill="url(#{fill})" stroke-width=".8"/>'

def mono(X,Y):
    o=[L(X,Y,[(0,18),(300,8)]),L(X,Y,[(0,18),(270,0)]),L(X,Y,[(0,6),(300,16)]),
       L(X,Y,[(120,0),(120,14)],.8,'4 3'),L(X,Y,[(0,14),(120,14)],.8,'4 3'),L(X,Y,[(180,0),(180,12)],.8,'2 3'),L(X,Y,[(0,12),(180,12)],.8,'2 3'),
       dot(X,Y,120,14),dot(X,Y,120,10),dot(X,Y,180,12),
       T(X,Y,296,8,'D',dy=-6),T(X,Y,262,3.5,'MR',dx=4),T(X,Y,296,16,'MC',dy=-6),
       T(X,Y,124,14.4,'A',dy=-3),T(X,Y,124,10,'B',dx=2,dy=14),T(X,Y,184,12.2,'C',dy=-4),
       T(X,Y,-8,14,'14',a='end',dx=-3,dy=4),T(X,Y,-8,10,'10',a='end',dx=-3,dy=4)]
    return o
fig('fig_monopoly.svg',300,20,[0,60,120,180,240,300],[0,4,8,12,16,20],mono,'Quantity of buns a day')
def welf(X,Y):
    return [poly(X,Y,[(0,18),(0,14),(120,14)],'h'),poly(X,Y,[(0,14),(120,14),(120,10),(0,6)],'c'),poly(X,Y,[(120,14),(120,10),(180,12)],'d'),
      L(X,Y,[(0,18),(200,18-200/30)]),L(X,Y,[(0,6),(200,6+200/30)]),L(X,Y,[(120,0),(120,14)],.8,'4 3'),L(X,Y,[(180,0),(180,12)],.8,'2 3'),
      T(X,Y,128,18.2,'Consumers’ surplus 240',dy=0),f'<path d="M{X(128)-3} {Y(18.2)-3} L{X(45)} {Y(15)}" stroke-width=".6"/>',
      T(X,Y,32,10.2,'Producers’ surplus 720',dx=-20,dy=0),T(X,Y,128,5.2,'Deadweight loss 120',dx=0),f'<path d="M{X(150)} {Y(5.2)-12} L{X(138)} {Y(11.8)}" stroke-width=".6"/>',
      T(X,Y,196,11.3,'D',dy=14),T(X,Y,196,12.7,'MC',dy=-6)]
fig('fig_welfare.svg',200,20,[0,40,80,120,160,200],[0,4,8,12,16,20],welf,'Quantity of buns a day')
def mc(X,Y):
    ac=[(q,60/q+8+q/20) for q in range(8,71,2)]
    return [L(X,Y,[(0,14),(70,7)]),L(X,Y,[(0,14),(70,0)]),L(X,Y,[(0,8),(70,15)]),L(X,Y,ac),
      L(X,Y,[(20,0),(20,12)],.8,'4 3'),L(X,Y,[(0,12),(20,12)],.8,'4 3'),L(X,Y,[(34.64,0),(34.64,11.46)],.8,'2 3'),
      dot(X,Y,20,12),dot(X,Y,20,10),dot(X,Y,34.64,11.46),
      T(X,Y,22,12.3,'T',dy=-2),T(X,Y,22,9.6,'E',dy=10),T(X,Y,66,7.2,'D',dy=-6),T(X,Y,60,2.2,'MR',dx=0),T(X,Y,66,15.2,'MC',dy=-6),T(X,Y,10,15.6,'AC',dx=6),
      L(X,Y,[(20,1.5),(34.64,1.5)],.8),L(X,Y,[(20,1.1),(20,1.9)],.8),L(X,Y,[(34.64,1.1),(34.64,1.9)],.8),T(X,Y,27.3,2.0,'excess capacity',a='middle',dy=-6,i=True)]
fig('fig_mcomp.svg',70,16,[0,10,20,30,40,50,60,70],[0,4,8,12,16],mc,'Quantity of milk buns a day')
def kink(X,Y):
    return [L(X,Y,[(0,20),(40,16),(100,4)],2),L(X,Y,[(0,20),(40,12)]),L(X,Y,[(40,12),(40,8)],1,'3 3'),L(X,Y,[(40,8),(60,0)]),
      L(X,Y,[(0,6),(100,16)]),L(X,Y,[(0,7.5),(100,17.5)],1.2,'5 3'),L(X,Y,[(40,0),(40,16)],.6,'2 3'),dot(X,Y,40,16),
      T(X,Y,43,16.4,'kink',dy=-2,i=True),T(X,Y,96,5,'D',dy=-6),T(X,Y,50,6.4,'MR',dx=4),T(X,Y,98,16.5,'MC',dy=-6),T(X,Y,70,15.2,'higher MC',a='end',dy=-4,i=True)]
fig('fig_kink.svg',100,24,[0,20,40,60,80,100],[0,4,8,12,16,20,24],kink,'Quantity of milk buns a day')
