# Only difference here is L12
count = 0
with open('day4.txt') as f:
    l = f.read().split()
    for p in l:
        p = p.split(',')
        for i, e in enumerate(p):
            e = e.split('-')
            minimum, maximum = map(int, e)
            p[i] = set(range(minimum, maximum+1))
        a, b = p
        if a & b:
            count += 1
print(count)
