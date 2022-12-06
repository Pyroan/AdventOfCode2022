N = 4
with open('day6.txt') as f:
    s = f.read()
for i in range(len(s)-N):
    if len(set(s[i:i+N])) == N:
        print(i+N)
        break
