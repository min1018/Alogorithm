dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def fireballMove():
  next = [list([] for _ in range(n)) for _ in range(n)]
  for i in range(n):
    for k in range(n):
      if len(graph[i][k]) > 0:
        for ball in graph[i][k]:
          size, speed, dir = ball[0], ball[1], ball[2]
          nx = (i + dx[dir] * speed) % n 
          ny = (k + dy[dir] * speed) % n
          while nx < 0:
            nx += n
          while ny < 0:
            ny += n
          next[nx][ny].append([size, speed, dir])
  return next

def fireballAdd():
  for i in range(n):
    for k in range(n):
      if len(graph[i][k]) > 1:
        totalSize = 0
        totalSpeed = 0
        decideDir = 0
        for ball in graph[i][k]:
          totalSize += ball[0]
          totalSpeed += ball[1]
          if ball[2] % 2 == 0:
            decideDir += 1
        totalSize //= 5
        totalSpeed //= len(graph[i][k])
        if totalSize == 0:
          graph[i][k] = []
          continue
        if decideDir == len(graph[i][k]) or decideDir == 0: # 방향 짝수 
          graph[i][k] = []
          graph[i][k].append([totalSize, totalSpeed, 0])
          graph[i][k].append([totalSize, totalSpeed, 2])
          graph[i][k].append([totalSize, totalSpeed, 4])
          graph[i][k].append([totalSize, totalSpeed, 6])
        else:
          graph[i][k] = []
          graph[i][k].append([totalSize, totalSpeed, 1])
          graph[i][k].append([totalSize, totalSpeed, 3])
          graph[i][k].append([totalSize, totalSpeed, 5])
          graph[i][k].append([totalSize, totalSpeed, 7])
  return graph
      

n, ball, order = map(int, input().split(" "))
graph = [list([] for _ in range(n)) for _ in range(n)]

for _ in range(ball):
  x, y, size, speed, dir = map(int, input().split(" "))
  graph[x-1][y-1].append([size, speed, dir])


for _ in range(order):
  graph = fireballMove()
  fireballAdd()
ans = 0
for i in range(n):
  for k in range(n):
    if len(graph[i][k]) > 0:
      for h in graph[i][k]:
        ans += h[0]
print(ans)
