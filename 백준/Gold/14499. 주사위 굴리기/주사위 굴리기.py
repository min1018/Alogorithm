# 위 1 오른쪽 3
# 처음에는 주사위 모든 면에 0
# 윗 면의 수 출력 
# 동 서 북 남 
# 1 2 3 4 

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def roll(dir):
  a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
  # 동 서 북 남 
  # 1 2 3 4 
  if dir == 1: 
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c
  elif dir == 2: 
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d
  elif dir == 3: 
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b
  elif dir == 4: 
    dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e
  
f, w, x, y, o = map(int, input().split(" "))

graph = [list(map(int, input().split(" "))) for i in range(f)]
move = list(map(int, input().split(" ")))

nx, ny = x, y
for i in move:
  nx += dx[i-1]
  ny += dy[i-1]
  if 0 <= nx < f and 0 <= ny < w:
    roll(i)
    if graph[nx][ny] == 0:
      graph[nx][ny] = dice[-1]
    else:
      dice[-1] = graph[nx][ny]
      graph[nx][ny] = 0
  else:
    nx -= dx[i-1]
    ny -= dy[i-1]
    continue
    
  print(dice[0])
