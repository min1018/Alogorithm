# L<= < R 국경선 오픈 
# 전체 다 더함 한덩이 전체 인구수/연합을 이루는 칸의 수 

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
  q = deque()
  q.append((x,y))
  save = [(x,y)]
  total = graph[x][y]
  while q:
    x, y = q.popleft()
    visited[x][y] = 1
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < n:
        val = abs(graph[nx][ny] - graph[x][y])
        if L <= val <= R and visited[nx][ny] == 0:
          visited[nx][ny] = 1
          q.append((nx, ny))
          total += graph[nx][ny]
          save.append((nx, ny))

  if len(save) == 1:
    return 1
  total = total // len(save)
  for x, y in save:
    graph[x][y] = total
  return 0



n, L, R = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

ans = 0
flag = 0
while True:
  flag = 1
  visited = [[0] * n for _ in range(n)]
  for i in range(n):
    for k in range(n):
      if visited[i][k] == 0:
        temp = bfs(i, k)
        if temp == 0: # 한덩이라도 바뀌었으면 
          flag = 0
  if flag == 1:
    break
  ans += 1


print(ans)