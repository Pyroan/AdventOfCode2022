# I know, I KNOW!
# This is massively out of character for me!
# Function declarations? Meaningful variable names? DOCSTRINGS?????
# "What's gotten into her?", you say.
#
# And that's because you weren't here for Intcode.

import json

filesystem = {"/": {}}  # grinning like an idiot at having to do this
# lmao. storing as a stack of references because why pretend
wd = [filesystem["/"]]


def _touch(name, size=0, wd=wd):
    """Return the file/directory at `<wd>/name`, creating it if it doesn't exist

    (so kind of like a combo of `$ touch` and `$ mkdir -p`)
    """
    if name not in wd[-1]:
        if size != 0:
            # `name` is a file
            wd[-1][name] = size
        else:
            # `name` is a dir
            wd[-1][name] = {}
    return wd[-1][name]


def _du(f):
    """Return total size of contents in `d`, including subdirectories"""
    if type(f) == dict:
        return sum(_du(file) for _, file in f.items())
    else:
        return f


def cd(d, wd=wd):
    if d == '..':
        wd.pop()
    elif d == '/':
        wd = filesystem['/']
    else:
        # The problem statement doesn't guarantee
        # that you'll only access dirs you already know about...
        # However if we do access a dir we know it exists because
        # we're reverse-engineering the filesystem
        wd.append(_touch(d))


def ls(data):
    """In this case, actually means 'make sure everything in data exists in `wd`'"""
    for i in range(0, len(data)-1, 2):
        size = int(data[i]) if data[i] != 'dir' else 0
        name = data[i+1]
        _touch(name, size)


def filtered_du(f, cond, l=0):
    """Uh. Sort of like a recursive reduce? Return the total size of `f`, and the result of `cond` recurisvely applied across every dir in `f`"""
    size = 0
    if type(f) == dict:
        for _, v in f.items():
            s, l = filtered_du(v, cond, l)
            if type(v) == dict:
                l = cond(s, l)
            size += s
    else:
        size = f
    return size, l


#######################################################
# We now return to your regularly scheduled spaghetti #
#######################################################
with open('day7.txt') as f:
    tty_output = f.read().split('$ ')[1:]

# LET'S DO THIS
# sickos.jpg
# (sets up filesystem)
mode = 0  # 0 for commands, 1 for output
for l in tty_output:
    t = l.split()
    if t[0] == 'cd':
        cd(t[1])
    elif t[0] == 'ls':
        ls(t[1:])


def smol_beans(f, l=0):
    size = 0
    # (get a list of all the smallest directories' sizes)
    # (subdirectories will be included more than once! on purpose for some reason!)
    if type(f) == dict:
        for k, v in f.items():
            s, l = smol_beans(v, l)
            if s <= 100000 and type(v) == dict:
                l += s
            size += s
            # print(f"{k}: {size}")
    else:
        size = f
    return size, l


# _ is the total size of the first parameter, s is the cumulative result second.
_, s = filtered_du(filesystem, lambda size, total: total +
                   size if size < 100000 else total)
print(s)
