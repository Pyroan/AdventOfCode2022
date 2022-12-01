with open('day1.txt') as f:
    print(
        sum(
            sorted(
                sum(
                    map(int, s.split())
                ) for s in f.read().split('\n\n'))[-3:]
        )
    )
