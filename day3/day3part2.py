s = []
with open('day3.txt') as f:
    l = f.read().split()
    for i in range(0, len(l), 3):
        a, b, c = map(set, l[i:i+3])
        d, *_ = a & b & c
        s += [ord(d)]
print(sum(x-96 if x > 96 else x-38 for x in s))
