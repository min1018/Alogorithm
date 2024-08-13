import sys
input = sys.stdin.readline

n, m = map(int, input().split(" "))

graph = [list(input().strip()) for _ in range(n)]

# visited 배열을 매번 새로 만들 필요 없음 한번 방문한 곳에서 사이클 안되면 어차피 안됨 


ans = False

def dfs(x, y, cnt, sx, sy):
  global ans
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < m:
      if graph[x][y] == graph[nx][ny]: # 색이 같아야함 
        if cnt >= 4 and nx == sx and ny == sy: # 사이클 발견, 길이 4이상 
          print("Yes")
          exit()
        if visited[nx][ny] == 0:
          visited[nx][ny] = 1
          dfs(nx, ny, cnt+1, sx, sy)
          visited[nx][ny] = 0
      

visited = [[0] * m for _ in range(n)]

for i in range(n):
  for k in range(m):
    visited[i][k] = 1
    dfs(i, k, 1, i, k)
    visited[i][k] = 0

print("No")
