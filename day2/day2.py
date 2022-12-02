# Doing this a silly obfuscated way for no reason I guess.
m = [4, 1, 7, 8, 5, 2, 3, 9, 6]
s = 0
with open('day2.txt') as f:
    for l in f:
        s += m[3*(ord(l[2])-88)+ord(l[0])-65]
print(s)


'''
For some reason, instead of just calculating the result,
I'm hard coding the results as a lookup table.
I don't know what possessed me to do this.
0 1 2
r p s

them | you | result
-----+-----+---------
0    | 0   | D  (+4)
     | 1   | W  (+8)
     | 2   | L  (+3)
1    | 0   | L  (+1)
     | 1   | D  (+5)
     | 2   | W  (+9)
2    | 0   | W  (+7)
     | 1   | L  (+2)
     | 2   | D  (+6)
Huh interesting how every digit from 0-9 is represented


or, if you prefer a matrix....
 | A  B  C
-+---------
X| 4  1  7
Y| 8  5  2
Z| 3  9  6
this is like, *so* close to being a magic square...
As in the only thing that fails is the first and last row
'''
