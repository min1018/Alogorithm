from collections import deque

def melt():
  cnt = 0
  visited = [[0] * m for _ in range(n)]
  q = deque()
  q.append((0, 0))
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
        if board[nx][ny] == 0:
          q.append((nx, ny))
        if board[nx][ny] == 1:
          board[nx][ny] = 0
          cnt += 1
        visited[nx][ny] = 1
      #print("cnt", cnt)
  return cnt 
  

n, m = map(int, input().split(" "))
board = [list(map(int, input().split(" "))) for _ in range(n)]

time = 0
remain = []
while True:
  left = melt()
  remain.append(left)
  if left == 0 :
    print(time)
    print(remain[-2])
    break
  time += 1