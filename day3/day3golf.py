def f(x):a,b,c,*_=map(set,x);d,*_=a&b&c;return[ord(d)]
l,s,t=open('day3.txt').read().split(),[],[]
for i in range(300):k=len(l[i])//2;s+=f([l[i][:k],l[i][k:]]*2);t+=i%3*[38]or f(l[i:i+3])
for m in s,t:print(sum(x-38-58*(x>96)for x in m))