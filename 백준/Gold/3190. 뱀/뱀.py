from collections import deque
# 사과 잇으면 머리에 더하고 그대로 
# 없으면 사과 앞에 하나 더하고 꽁지 빼고 

def turn(d, curr):
  if d == 'L':
   curr = (curr+3)%4
  elif d == 'D':
   curr = (curr+1)%4
  return curr
 # 북 동 남 서 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
graph = [[0]*n for _ in range(n)]

apple = int(input())
for _ in range(apple):
   x, y = map(int, input().split(" "))
   graph[x-1][y-1] = 1

o = int(input())
dir = deque()
for _ in range(o):
  num, d = input().split(" ")
  dir.append((num, d))
   # L -> 왼쪽, D -> 오른쪽 

snake = deque()
snake.append((0,0))
time = 1
ct, cd = dir.popleft()
x, y = 0, 0
curr = 1
while True:
  #print("time", time)
  # *초에 움직임
  if time == int(ct)+1:
    curr = turn(cd, curr)
    if dir:
      ct, cd = dir.popleft()
  nx = x + dx[curr]
  ny = y + dy[curr]
  if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in snake:
    if graph[nx][ny] == 1:
      # 사과가 있는 경우, 머리에 더하기
      graph[nx][ny] = 0
      x, y = nx, ny
      snake.append((nx, ny))
    else:
      # 사과가 없는 경우, 머리 더하고 꽁지 빼기 
      snake.append((nx, ny))
      x, y = nx, ny
      snake.popleft()
    #print("snake", snake)
  else: 
    print(time)
    break
  time += 1
  