from collections import deque 

def bfs(i, k):
  q = deque()
  q.append((i, k))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  sheep = 0
  wolf = 0
  while q:
    x, y = q.popleft()
    visited[x][y] = 1
    if graph[x][y] == 'o':
      sheep += 1
    elif graph[x][y] == 'v':
      wolf += 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if visited[nx][ny] == 0 and graph[nx][ny] != '#':
          q.append((nx, ny))
          visited[nx][ny] = 1
  if sheep > wolf :
    wolf = 0
  else :
    sheep = 0

  return sheep, wolf

ts, tw = 0, 0
n, m = map(int, input().split(" "))
graph = [list(input()) for i in range(n)]
visited = [[0] * m for i in range(n)]
for i in range(n):
  for k in range(m) :
    if visited[i][k] == 0 and graph[i][k] != '#':
      sheeps, wolves = bfs(i, k)
      ts += sheeps
      tw += wolves

print(ts, tw)