# God so tempted to find a way to call it $X
X = 1
cycles = 0
siggy_wiggies = []
with open('day10.txt') as f:
    ins = [*map(str.split, f.readlines())]


def addx(y):
    global X
    xtime = 2  # ticks until we're going to execute for real
    while xtime:
        tick()
        xtime -= 1
    X += y


def tick():
    global cycles, siggy_wiggies
    cycles += 1
    if (cycles-20) % 40 == 0:
        siggy_wiggies += [cycles*X]


for n in ins:
    if n[0] == 'noop':
        tick()
    elif n[0] == 'addx':
        addx(int(n[1]))

print(sum(siggy_wiggies))
