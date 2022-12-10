# HELL YEAH HELL YEAH TIME TO REDEEM MYSELF FOR THE INTCODE THING
X = 1
cycles = 0
siggy_wiggies = []
w, h = 40, 6
raster = 0
screen = ''
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
    global cycles, siggy_wiggies, raster, screen
    # raster doesn't need to be it's own var but this isn't golf
    cycles += 1
    raster = (cycles-1) % (w*h) % w
    screen += '#' if abs(raster-X) < 2 else '.'
    if cycles % 40 == 0:
        screen += '\n'


for n in ins:
    if n[0] == 'noop':
        tick()
    elif n[0] == 'addx':
        addx(int(n[1]))

print(screen)
