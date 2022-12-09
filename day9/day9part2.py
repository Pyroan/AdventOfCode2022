# Set this to 2 to solve part 1
ROPE_LENGTH = 10

# 0: No debugging
# 1: Visualize (poorly) a hard-coded-sized-and-positioned chart of the rope
# 2: Do the above, then wait for user input (aka frame by frame)
DBUG = 0

rope = [[0, 0]for _ in range(ROPE_LENGTH)]
s = set()


def dump():
    st = ''
    for b in range(20, -1, -1):
        for a in range(26):
            x, y = a-11, b-5
            c = '.'
            if [x, y] == rope[0]:
                c = 'H'
            if f'{x},{y}' in s:
                c = '#'
            if [x, y] in rope[1:]:
                c = str(rope.index([x, y]))

            st += c
        st += '\n'
    print(st)
    print(rope)


def manhattan(a, b):
    """return the largest delta of either axis for a and b.
    not actually manhattan, sorry.
    whats the word for manhattan when its octodirectional
    is it called like manhattan-8 or smth i can't remember"""
    ax, ay = a
    bx, by = b
    return max(abs(ax-bx), abs(ay-by))


def signum(a):
    return a > 0 and 1 or a < 0 and -1 or 0


def diag_direction(a, b):
    """Return a vector describing the movement of b to bring it
    one 'ring' closer to a
    """
    ax, ay = a
    bx, by = b
    x = signum(bx-ax)
    y = signum(by-ay)
    return x, y


with open('day9.txt') as f:
    instructions = [tuple(x.split())for x in f]
for i, d in instructions:
    d = int(d)
    if DBUG > 0:
        dump()
    if DBUG == 2:
        input()
    for _ in range(d):

        if i == 'U':
            rope[0][1] += 1
        elif i == 'D':
            rope[0][1] -= 1
        elif i == 'L':
            rope[0][0] -= 1
        elif i == 'R':
            rope[0][0] += 1
        for k in range(1, ROPE_LENGTH):
            if manhattan(rope[k], rope[k-1]) > 1:
                x, y = diag_direction(rope[k], rope[k-1])
                rope[k][0] += x
                rope[k][1] += y

        s.add(f'{rope[ROPE_LENGTH-1]},{rope[ROPE_LENGTH-1]}')
print(len(s))
