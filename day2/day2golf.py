for n in[[4,1,7,8,5,2,3,9,6],[3,1,2,4,5,6,8,9,7]]:print(sum(n[3*ord(l[2])+ord(l[0])-329]for l in open('day2.txt')))