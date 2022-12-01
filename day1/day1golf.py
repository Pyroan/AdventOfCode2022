s=sorted(sum(map(int,s.split()))for s in open('day1.txt').read().split('\n\n'))[-3:]
print(s[2],sum(s))
