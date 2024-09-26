from collections import deque 

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    visited = [[-1] * m for _ in range(n)]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] ==-1 and board[nx][ny] != 0 and board[nx][ny] != 2:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
    return visited
       

n, m = map(int, input().split(" "))
# 0 X 1 O 2 target 
board = [list(map(int, input().split(" "))) for _ in range(n)]

for x in range(n):
    for y in range(m):
        if board[x][y] == 2:
            tx, ty = x, y


answer= bfs(tx, ty)  
answer[tx][ty] = 0   
for i in range(n):
    for k in range(m):
        if board[i][k] == 0:
            answer[i][k] = 0
    print(*answer[i])
            
