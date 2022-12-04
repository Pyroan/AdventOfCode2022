import re
t,s=0,0
for p in open('day4.txt'):a,b,c,d=map(int,re.split(',|-',p));t+=b-c>=0<=d-a;s+=(a-c)*(b-d)<=0
print(s,t)