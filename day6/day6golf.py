s=open('day6.txt').read()
for N in 4,14:i=-1;print([N-len({*s[(i:=i+1):i+N]})for _ in s].index(0)+N)