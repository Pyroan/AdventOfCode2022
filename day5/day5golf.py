l=[x[:-1]for x in open('day5.txt')]
u=l.index('')
c,p=l[:u-1],l[u+1:]
for y in[-1,1]:
 a=(len(c[0])+8)//4*['']
 for w in c:
  i=1
  for v in w[1::4]:a[i]+=v*(v!=' ');i+=1
 for z in p:n,h,t=map(int,z.split()[1::2]);a[t]=a[h][:n][::y]+a[t];a[h]=a[h][n:]
 print(*[s[0]for s in a[1:]],sep='')
