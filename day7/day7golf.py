w=[{"/":{}}]
for l in open('day7.txt').read().split('$ '):
 if(i:=-2)*len(t:=l.split()[1:])==i:x=t[0];w=w[:-(x=='..')]+w[:x=='/']or w+[w[-1][x]]
 while(i:=i+2)<len(t)>1:w[-1][t[i+1]]=t[i]!='dir'and int(t[i])or{}
def u(l,q,f=w[0]):
 z=f
 for i in'pop'in dir(f)and~(z:=0)and f or[]:l,s=u(l,q,f[i]);z+=s;l=(type(f[i])!=int)*(s*(l>s>=-4e7+d)if q else(1e5>s)*s+l)or l
 return l,z
s,d=u(0,0);print(s,u(d,1)[0]) 