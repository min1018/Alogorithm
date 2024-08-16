import sys 
input = sys.stdin.readline 
from collections import deque

def bfs():
  q = deque()
  q.append((0, 0, 0)) # x y move used or not 

  visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  visited[0][0][0] = 1 # x y z -> z = 0 벽 안 뚫음 / z = 1 벽 뚫음 
  
  while q:
    x, y, w = q.popleft()
    
    if x == n-1 and y == m-1:
      print(visited[x][y][w])
      return
      
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m:
        if graph[nx][ny] == 0 and visited[nx][ny][w] == 0: # 벽이 아닌 경우
          visited[nx][ny][w] = visited[x][y][w] + 1
          q.append((nx, ny, w))
        if graph[nx][ny] == 1 and w == 0: # 벽이고 깬적 없음 
          visited[nx][ny][w+1] = visited[x][y][w] + 1
          q.append((nx, ny, 1))
  

  print(-1)
  
    
  

n, m = map(int, input().split(" "))
graph = [list(map(int, input().strip())) for _ in range(n)]

bfs()

