with open('day5.txt') as f:
    crates, instructions = [x.split('\n')for x in f.read().split('\n\n')]
# Transpose the stacks...
stacks = [[]]*len(crates[0][1::4])
for row in crates[:-1]:
    r = row[1::4]
    for i, v in enumerate(r):
        if v != ' ':
            stacks[i] = [v]+stacks[i]
# Move Things Around
# don't forget the stacks are 1-indexed in the input!
for c in instructions[:-1]:
    c = c.split()
    n, source, dest = map(int, c[1::2])

    stacks[dest-1] += reversed(stacks[source-1][-n:])
    stacks[source-1] = stacks[source-1][:-n]

# Get the "top" of each statck
print(''.join([s[-1]for s in stacks]))
