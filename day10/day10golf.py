X=1;c=g=0;s='';t=lambda n,s,g,c:n and t(n-1,s+'.#'[X-c%40in[-1,0,1]]+'\n'*(38<c%40),g+(c:=c+1)*X*(c%40==20),c)or(s,g,c)
for n in open('day10.txt'):m='a'in n;s,g,c=t(1+m,s,g,c);X+=m and int(n[5:])
print(f'{g}\n{s}')
