f=lambda a,b:{*range(a,b+1)}
g=lambda a,b:(a&b in[a,b])+(a^b<a|b)*1000
c=sum(g(*[f(*map(int,e.split('-')))for e in p.split(',')])for p in open('day4.txt'))
print(c%1000,c//1000)