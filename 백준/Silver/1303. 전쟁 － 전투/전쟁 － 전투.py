from collections import deque 

pw = 0 
pb = 0 

def bfs(cx, cy):
  cnt = 1
  q = deque()
  q.append((cx, cy))
  visited[cx][cy] = 1 
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1 ,1]
  while q: 
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m :
        if board[x][y] == board[nx][ny] and visited[nx][ny] == 0 :
          q.append((nx, ny))
          visited[nx][ny] = 1
          cnt += 1
  return cnt
          
# 가로, 세로    
m, n = map(int, input().split(" "))
board = [list(input()) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

for i in range(n):
  for k in range(m):
    if visited[i][k] == 0:
      if board[i][k] == 'W':
        num = bfs(i, k)
        pw += (num ** 2)

      else : 
        num = bfs(i, k)
        pb += (num ** 2)


print(pw, pb)