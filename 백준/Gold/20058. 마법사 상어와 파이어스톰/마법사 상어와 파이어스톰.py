from collections import deque 

def rotate(n, num):
  new = [[0 for _ in range(2 ** n)] for _ in range(2**n)]
  
  for i in range(0, 2 ** n, 2 ** num):
    for k in range(0, 2 ** n, 2 ** num):
      for a in range(2**num):
        for b in range(2**num):
          new[i+b][k+2**num-1-a] = board[i+a][k+b]

  return new 

def melt(n):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  new = [[0 for _ in range(2 ** n)] for _ in range(2**n)]
  for i in range(2**n):
    for k in range(2**n):
      if board[i][k] > 0:
        cnt = 0
        for h in range(4):
          nx, ny = i + dx[h], k + dy[h]
          if 0 <= nx < 2**n  and 0 <= ny < 2**n:  
           if board[nx][ny] > 0:
              cnt += 1
        if cnt < 3:
          new[i][k] = board[i][k] -1
        else:
          new[i][k] = board[i][k]
      else:
        new[i][k] = 0

  return new

def bfs(n, x, y, visited):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  cnt, ice = 1, board[x][y]
  q = deque()
  q.append((x, y))
  visited[x][y] = 1
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx, ny = x + dx[i], y + dy[i]
      if 0 <= nx < 2**n and 0 <= ny < 2**n:
        if board[nx][ny] > 0 and visited[nx][ny] == 0:
          cnt += 1
          ice += board[nx][ny]
          visited[nx][ny] = 1
          q.append((nx, ny))
  return cnt, ice, visited



n, count = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(2**n)]
visited = [[0] * (2**n) for _ in range(2**n)]

order = list(map(int, input().split(" ")))

for o in order:
  board = rotate(n, o)
  board = melt(n)

total = 0
icesize = 0
for i in range(2**n):
  for k in range(2**n):
    if board[i][k] > 0 and visited[i][k] == 0:
      cnt, ice, visited = bfs(n, i, k, visited)
      total += ice
      if cnt > icesize:
        icesize = cnt

print(total)
print(icesize)