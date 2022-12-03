s = []
with open('day3.txt') as f:
    for l in f:
        a = set(l[:len(l)//2])
        b = set(l[len(l)//2:])
        # Not sure how I never learned about the unpacking operator but here we are
        # Incidentally you can golf a.intersection(b)` with `a-(a-b)`
        c, *_ = a & b
        s += [ord(c)]
print(sum(x-96 if x > 96 else x-38 for x in s))
