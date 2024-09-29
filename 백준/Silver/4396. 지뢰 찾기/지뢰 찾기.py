n = int(input())

board = [list(input().rstrip()) for _ in range(n)]
visited = [list(input().rstrip()) for _ in range(n)]
ans = [['.']*n for _ in range(n)]

dx = [-1, -1, -1,  0, 0, 1, 1, 1]
dy = [-1, 1, 0, -1, 1, -1, 0, 1]

flag = 0
for i in range(n):
    for k in range(n):
        if visited[i][k] == 'x':
            if board[i][k] == '*':
                flag = 1
            cnt = 0
            for h in range(8):
                nx, ny = i+dx[h], k+dy[h]
                if 0 <= nx < n and 0 <= ny < n:
                    if board[nx][ny] == '*':
                        cnt += 1
            ans[i][k] = cnt
            
if flag == 1:
    for i in range(n):
        for k in range(n):
            if board[i][k] == '*':
                ans[i][k] = '*'

for tmp in ans:
    for i in tmp:
        print(i, end = '')
    print()