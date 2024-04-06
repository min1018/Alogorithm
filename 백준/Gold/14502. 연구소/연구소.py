from collections import deque
import copy

ans = 0

def possible(cnt):
  if cnt == 3:
    bfs()
    return 
  #벽 3개를 골라야함 
  for i in range(n):
    for k in range(m):
      if board[i][k] == 0:
        board[i][k] = 1
        possible(cnt + 1)
        board[i][k] = 0
  
def bfs():
  global ans 
  graph = copy.deepcopy(board)
  q = deque()
  for i in range(n):
    for k in range(m):
      if graph[i][k] == 2:
        q.append((i, k))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1 , 1]
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
        q.append((nx, ny))
        graph[nx][ny] = 2
  res = 0
  for i in range(n):
    res += graph[i].count(0)

  ans = max(ans, res)


n, m = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(n)]

possible(0)
print(ans)

