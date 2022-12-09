F=[];L=0;p=-1
for x in open('day8.txt'):F+=list(map(int, x[:-1]));L+=1
k=[0]*L*L
for i in(l:=range(L)):
 z=[-1]*4
 for j in l:
  a=L-1-j;e=i*L+j,i*L+a,j*L+i,a*L+i;q=-1;c=1
  for v in e:
   n=0;b=(q:=q+1)&1or-1
   while n:=n+1:
    if[i,j][q>1]*b<=n+(1-L)*(~q&1)or F[i*L-L*n*b*(q<2)+j-n*b*(q>1)]>=F[e[0]]:c*=n;n=-1  
   if F[v]>z[q]:k[v]=1;z[q]=F[v]
  p=max(c,p)
print(sum(k),p)