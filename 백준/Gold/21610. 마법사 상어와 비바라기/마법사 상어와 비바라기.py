n, o = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

cloud = [(n-1, 0), (n-1,1), (n-2,0), (n-2, 1)]

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

def cloudMoveRain(dir, speed):
  for x, y in cloud:
    nx = (x + dx[dir-1]*speed)%n
    ny = (y + dy[dir-1]*speed)%n
    graph[nx][ny] += 1
    visited[nx][ny] = 1

  
def waterCopy():
  mx = [-1, -1, 1, 1]
  my = [-1, 1, -1, 1]
  for x in range(n):
    for y in range(n):
      if visited[x][y] == 1:
        for i in range(4):
          nx = x + mx[i]
          ny = y + my[i]
          if 0<= nx <n and 0<= ny < n and graph[nx][ny] > 0:
            graph[x][y] += 1
  

def decreaseWater():
  for x in range(n):
    for y in range(n):
      if graph[x][y] >= 2 and visited[x][y] != 1:
        graph[x][y] -= 2
        cloud.append((x,y))

for k in range(o):
  dir, speed = map(int, input().split(" "))
  visited = [[0] * n for _ in range(n)]
  cloudMoveRain(dir, speed)
  cloud = [] # 구름 삭제
  waterCopy()
  decreaseWater()

print(sum(map(sum, graph)))
