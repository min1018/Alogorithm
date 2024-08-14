import sys
input = sys.stdin.readline
from collections import deque 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt(current):
  nxt = [[0] * m for _ in range(n)]
  for i in range(n):
    for k in range(m):
      if current[i][k] != 0:
        cnt = 0
        for h in range(4):
          nx = i + dx[h]
          ny = k + dy[h]
          if 0 <= nx < n and 0 <= ny < m and current[nx][ny] == 0:
            cnt += 1
        if current[i][k] - cnt < 0:
          nxt[i][k] = 0
        else:
          nxt[i][k] = current[i][k] - cnt

  return nxt 

def bfs(current, x, y, visited):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    visited[x][y] = 1
    for h in range(4):
      nx = x + dx[h]
      ny = y + dy[h]
      if 0 <= nx < n and 0 <= ny < m and current[nx][ny] != 0 and visited[nx][ny] == 0:
        q.append((nx, ny))
        visited[nx][ny] = 1
  return visited
  
  
def many(graph):
  visited = [[0] * m for _ in range(n)]
  cnt = 0
  flag = 0
  for i in range(n):
    for k in range(m):
      if graph[i][k] != 0 and visited[i][k] == 0:
        # print("visited")
        # print(visited)
        visited = bfs(graph, i, k, visited)
        cnt += 1
        flag = 1
  return cnt, flag
        

n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

year = 0
while True:
  count, flag = many(graph)
  if count > 1:
    print(year)
    break
  if flag == 0:
    print(0)
    break
  graph = melt(graph)
  # print("year", year)
  # print(graph)
  year += 1