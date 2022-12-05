l=open('day5.txt').readlines()
u=l.index('\n')
for y in[-1,1]:
 a=(len(l[0])//4+1)*[[]]
 for i in range(len(a)-1):a[i+1]=[x for w in l[:u-1]if(x:=w[1+i*4])!=' ']
 for z in l[u+1:]:n,h,t=map(int,z.split()[1::2]);a[t]=a[h][:n][::y]+a[t];a[h]=a[h][n:]
 print(''.join(s[0]for s in a[1:]))