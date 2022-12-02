# This works just like the first one but the matrix is '''inverted'''
'''
0 1 2
A B C
r p s
X Y Z
L D W

them | you   | result
-----+-------+---------
0    | X 2   | L  (+3)
     | Y 0   | D  (+4)
     | Z 1   | W  (+8)
1    | X 0   | L  (+1)
     | Y 1   | D  (+5)
     | Z 2   | W  (+9)
2    | X 1   | L  (+2)
     | Y 2   | D  (+6)
     | Z 0   | W  (+7)

 | A  B  C
-+---------
X| 3  1  2
Y| 4  5  6
Z| 8  9  7
Huh fancy that it sure looks like this is the
Same matrix as before but with the outer columns
shifted.
'''
m = [3, 1, 2, 4, 5, 6, 8, 9, 7]
s = 0
with open('day2.txt') as f:
    for l in f:
        s += m[3*(ord(l[2])-88)+ord(l[0])-65]
print(s)
