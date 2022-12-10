def f(R,i):
 R[i in'RL']+=i in'UR'or-1;k=x=y=2
 while k<L and'2'in f'{(x:=R[k]-R[k-2]),(y:=R[k+1]-R[k-1])}':R[k]-=(0<x)-(0>x);R[k+1]-=(0<y)-(0>y);k+=2
for L in 4,20:R=[0]*L;print(len({f'{f(R,i[0])or R[-2:]}'for i in open('day9.txt')for _ in range(int(i[2:]))}))