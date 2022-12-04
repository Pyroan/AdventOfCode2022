f=lambda x:range(*map(int,x.split('-')))
g=lambda a,b:(a&b in[a,b])+(a^b!=a|b)*1000
c=sum(g(*[set(f(e))|{f(e).stop}for e in p.split(',')])for p in open('day4.txt'))
print(c%1000,c//1000)