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


def pwd(): print(json.dumps(wd, indent=2))  # for debugging


# weird bug where root isn't root even though the data is correct?
wd = [filesystem["/"]]

# _ is the total size of the first parameter, l is the size of everything that fits the condition.
d, _ = filtered_du(filesystem, lambda x, _: x)
unused = 70_000_000 - d
must_free = 30_000_000 - unused

_, s = filtered_du(filesystem, lambda size, minimum: size if size >=
                   must_free and size < minimum else minimum, d)
print(s)
