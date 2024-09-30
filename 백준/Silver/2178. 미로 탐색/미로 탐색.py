from collections import deque 

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited=[[0]* m for _ in range(n)]
    visited[x][y] = 1

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and board[nx][ny] == '1':
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                
    print(visited)
    

n, m = map(int, input().split(" "))
board = [list(input()) for _ in range(n)]

print(bfs(0,0))