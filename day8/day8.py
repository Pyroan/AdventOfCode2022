# Still tempted to refactor this to only care about local maxima but at the end of the day the data's just really noisy so
# I don't think it really makes a difference I just think it'd be really nice to do this in one sweep
with open('day8.txt') as f:
    field = [list(map(int, x[:-1])) for x in f.readlines()]
lookup = [[False]*len(field) for _ in field[0]]
for i in range(len(field)):
    biggest_bois = [-1]*4
    for j in range(len(field[i])):
        # left to right (aka visible from left)
        if field[i][j] > biggest_bois[0]:
            lookup[i][j] = True
            biggest_bois[0] = field[i][j]
        # right to left
        if field[i][-1-j] > biggest_bois[1]:
            lookup[i][-1-j] = True
            biggest_bois[1] = field[i][-1-j]
        # up to down
        if field[j][i] > biggest_bois[2]:
            lookup[j][i] = True
            biggest_bois[2] = field[j][i]
        # down to up
        if field[-1-j][i] > biggest_bois[3]:
            lookup[-1-j][i] = True
            biggest_bois[3] = field[-1-j][i]
print(sum(sum(l)for l in lookup))
