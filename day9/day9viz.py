# sorry windows users it was too annoying
from time import sleep
import curses
from curses import wrapper
ROPE_LENGTH = 10

FPS = 30
DBUG = 0

rope = [[0, 0]for _ in range(ROPE_LENGTH)]
s = set()


def draw(stdscr, cam):
    for b in range(cam['height']-1, -1, -1):
        for a in range(cam['width']-1):
            x, y = cam['x']+a-cam['width']//2, cam['y']+b-cam['height']//2
            stdscr.attrset(curses.color_pair(1))
            # World's lasiest randomly generated background:
            dirt = " "*20+".,'`"
            c = dirt[hash(f'{0xa0c2022}{x}{y}') % len(dirt)]
            if [x, y] == [0, 0]:
                stdscr.attrset(curses.color_pair(5))
                c = 's'
            if [x, y] == rope[0]:
                stdscr.attrset(curses.color_pair(2))
                c = 'H'
            if f'{x},{y}' in s:
                stdscr.attrset(curses.color_pair(3))
                c = '#'
            if [x, y] in rope[1:]:
                stdscr.attrset(curses.color_pair(4))
                c = str('01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'[
                        rope.index([x, y])])
            stdscr.addch(b, a, c)
    stdscr.refresh()


def manhattan(a, b):
    ax, ay = a
    bx, by = b
    return max(abs(ax-bx), abs(ay-by))


def signum(a):
    return a > 0 and 1 or a < 0 and -1 or 0


def diag_direction(a, b):
    ax, ay = a
    bx, by = b
    x = signum(bx-ax)
    y = signum(by-ay)
    return x, y


def main(stdscr):
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_BLACK, -1)
    curses.init_pair(2, curses.COLOR_YELLOW, -1)
    curses.init_pair(3, curses.COLOR_CYAN, -1)
    curses.init_pair(4, curses.COLOR_WHITE, -1)
    curses.init_pair(5, curses.COLOR_RED, -1)
    curses.curs_set(0)
    h, w = stdscr.getmaxyx()
    cam = {'x': 0, 'y': 0, 'width': w, 'height': h}
    with open('day9.txt') as f:
        instructions = [tuple(x.split())for x in f]
    for i, d in instructions:
        d = int(d)
        for _ in range(d):
            if i == 'U':
                rope[0][1] += 1
            elif i == 'D':
                rope[0][1] -= 1
            elif i == 'L':
                rope[0][0] -= 1
            elif i == 'R':
                rope[0][0] += 1
            if rope[0][0] < cam['x']-w//2:
                cam['x'] -= 1
            if rope[0][0] > cam['x']+w//2:
                cam['x'] += 1
            if rope[0][1] < cam['y']-h//2:
                cam['y'] -= 1
            if rope[0][1] > cam['y']+h//2:
                cam['y'] += 1
            for k in range(1, ROPE_LENGTH):
                if manhattan(rope[k], rope[k-1]) > 1:
                    x, y = diag_direction(rope[k], rope[k-1])
                    rope[k][0] += x
                    rope[k][1] += y

            s.add(f'{rope[ROPE_LENGTH-1][0]},{rope[ROPE_LENGTH-1][1]}')
        draw(stdscr, cam)
        sleep(1/FPS)
    input()


wrapper(main)
