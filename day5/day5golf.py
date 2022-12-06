l=open('day5.txt').readlines();u=l.index('\n')
for y in[-1,1]:
 a=(len(l[0])//4+1)*[[]]
 for i in range(1,len(a)):a[i]=[x for w in l[:u-1]if(x:=w[i*4-3])!=' ']
 for z in l[u+1:]:n,h,t=map(int,z.split()[1::2]);a[t]=a[h][:n][::y]+a[t];a[h]=a[h][n:]
 print(''.join(s[0]for s in a[1:]))