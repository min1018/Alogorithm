import sys 
input = sys.stdin.readline

caught = 0
# # 사이즈
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def catch(x):
  for i in range(f):
    if graph[i][x]:
      size, _, _ = graph[i][x][0]
      graph[i][x] = []
      return size

# # 상 하 우 좌
# # 1 2 3 4 
def decideDir(dir, x, y, speed):
  nx, ny = 0, 0
  while speed > 0:
    nx = x + dx[dir-1]
    ny = y + dy[dir-1]
    if 0 <= nx < f and 0 <= ny < w:
      x, y = nx, ny
      speed -= 1
      continue
    else:
      if dir in [1,3]:
        dir += 1
      elif dir in [2,4]:
        dir -= 1
  return (dir, nx, ny)



def sharkMove():
  for i in range(f):
    for k in range(w):
      if graph[i][k]:
        size, speed, dir = graph[i][k][0]
        nx = i + dx[dir-1]*speed
        ny = k + dy[dir-1]*speed
        if 0 <= nx < f and 0 <= ny < w:
          move[nx][ny].append((size, speed, dir))
        else: # 방향 전환
          nxt, nx, ny = decideDir(dir, i, k, speed)
          move[nx][ny].append((size, speed, nxt))
          
# 방향 전환이 두세번 일어나는 경우는?

def sharkEat():
  for i in range(f):
    for k in range(w):
      if len(move[i][k]) > 1:
        move[i][k].sort(key = lambda x : -x[0])
        move[i][k] = [move[i][k][0]]
  

f, w, shark = map(int, input().split(" "))
graph = [[[] for _ in range(w)] for _ in range(f)]

if shark == 0:
  print(0)
  exit(0)
  
for _ in range(shark):
  x, y, speed, dir, size = map(int, input().split(" "))
  graph[x-1][y-1].append((size, speed, dir))


for i in range(w):
  move = [[[] for _ in range(w)] for _ in range(f)]
  t = catch(i)
  # print(i, "try ")
  # print("fish catch", graph)
  sharkMove()
  sharkEat()
  graph = move
  # print("shark eat and move", graph)
  if t :
    caught += t
  
  

print(caught)

# # # 8 X 3 5 4 2

# 그래프 속의 형식 유지 [[(튜플)]] 형식으로 둔거 까먹지 말고 다시 저장할 때도 그 양식에 맞춰서