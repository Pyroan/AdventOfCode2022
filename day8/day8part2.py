with open('day8.txt') as f:
    field = [list(map(int, x[:-1])) for x in f.readlines()]
lookup = [[False]*len(field) for _ in field[0]]
prettiest_tree = -1
for i in range(1, len(field)-1):
    for j in range(1, len(field[i])-1):
        t = field[i][j]
        scenic_score = 1
        done = [False]*4
        n = 1
        while False in done:
            # right
            if not done[0] and (i+n >= len(field)-1 or field[i+n][j] >= t):
                scenic_score *= n
                # print(f'\tLeft: {n}')
                done[0] = True
            # left
            if not done[1] and (i-n < 1 or field[i-n][j] >= t):
                scenic_score *= n
                # print(f'\tRight: {n}')
                done[1] = True
            # up
            if not done[2] and (j+n >= len(field[0])-1 or field[i][j+n] >= t):
                scenic_score *= n
                # print(f'\tUp: {n}')
                done[2] = True
            # down
            if not done[3] and (j-n < 1 or field[i][j-n] >= t):
                scenic_score *= n
                # print(f'\tDown: {n}')
                done[3] = True
            n += 1
        # print(f"{i},{j} ({t}): {scenic_score}")
        if scenic_score > prettiest_tree:
            prettiest_tree = scenic_score
print(prettiest_tree)
