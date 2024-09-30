mx, my = 0, 0
shape = []
for _ in range(4):
    lx, ly, rx, ry = map(int, input().split(" "))
    shape.append((lx, ly, rx, ry))
    mx, my = max(mx, lx, rx), max(my, ly, ry)

board = [[0] * (my+1) for _ in range(mx+1)]

for lx, ly, rx, ry in shape:
    for i in range(lx, rx):
        for k in range(ly, ry):
            board[i][k] = 1

ans = 0
for i in range(mx):
    for k in range(my):
        if board[i][k] == 1:
            ans += 1

print(ans)