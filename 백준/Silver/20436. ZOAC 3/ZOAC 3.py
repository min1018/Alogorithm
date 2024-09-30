def get(word):
    for i in range(3):
        if i == 0:
            n = 10
        elif i == 1:
            n = 9
        elif i == 2:
            n == 7
        for k in range(n):
            if board[i][k] == word:
                return (i, k)

board = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']

l, r = input().split(" ")

lx, ly = get(l)
rx, ry = get(r)
mo = 'yuiophjklbnm'

search = list(input().rstrip())
cnt = 0

for w in search:
    cx, cy = get(w)
    lc = abs(lx-cx)+abs(ly-cy)
    rc = abs(rx-cx)+abs(ry-cy)
    if w in mo:
        rx, ry = cx, cy 
        cnt += rc+1
    else:
        lx, ly = cx, cy
        cnt += lc+1

print(cnt)