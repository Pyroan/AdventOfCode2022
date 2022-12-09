# I typically don't refactor the original solutions much, but
# day9part2.py can solve this one just as well with a parameter change.
h, t = [0, 0], [0, 0]
s = set()
dbug = False


def dump():
    st = ''
    for y in range(5, -1, -1):
        for x in range(6):
            if [x, y] == h:
                st += 'H'
            elif [x, y] == t:
                st += 'T'
            elif f'{x},{y}' in s:
                st += '#'
            else:
                st += '.'
        st += '\n'
    print(st)


def manhattan(a, b):
    ax, ay = a
    bx, by = b
    return max(abs(ax-bx), abs(ay-by))


with open('day9.txt') as f:
    instructions = [tuple(x.split())for x in f]
for i, l in instructions:
    l = int(l)
    for _ in range(l):
        oldh = h[:]
        if dbug:
            dump()
            input()
        if i == 'U':
            h[1] += 1
        elif i == 'D':
            h[1] -= 1
        elif i == 'L':
            h[0] -= 1
        elif i == 'R':
            h[0] += 1
        if manhattan(h, t) > 1:
            t = oldh

        s.add(f'{t[0]},{t[1]}')
print(len(s))
