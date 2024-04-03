import copy
from collections import deque

# N 0 S 1
# 시계 -> rotate(1), 반시계 -> rotate(-1)
# 같은 극 회전지 않음  
# 다른 극 반대 방향 

# 오른쪽 나 2번, 상대 6번 / 왼쪽 나 6번 상대 2번 

def move(num, direction, save):
  keep = copy.deepcopy(save)
  dir = direction
  for i in range(num-1, 3):
    # save[i] save[i+1]
    if save[i][2] == save[i+1][6]:
      break
    else:
      if dir == 1: # 시계
        keep[i+1].rotate(-1)
        dir = -1
      elif dir == -1: # 반시계 
        keep[i+1].rotate(1)
        dir = 1
  dir = direction
  for i in range(num-1, 0, -1):
    # save[i] 6 save[i-1] 2
    if save[i][6] == save[i-1][2]:
      break
    else:
      if dir == 1: 
        keep[i-1].rotate(-1)
        dir = -1
      elif dir == -1:
        keep[i-1].rotate(1)
        dir = 1
  if direction == 1:
    keep[num-1].rotate(1)
  else:
    keep[num-1].rotate(-1)
  return keep


save = []

for _ in range(4):
  temp = list(input())
  save.append(deque(temp))

trial = int(input())
for _ in range(trial):
  num, dir = map(int, input().split(" "))
  save = move(num, dir, save)

ans = 0
for i in range(4):
  if i == 0 and save[i][0] == '1':
    ans += 1
  elif i == 1 and save[i][0] == '1':
    ans += 2
  elif i == 2 and save[i][0] == '1':
    ans += 4 
  elif i == 3 and save[i][0] == '1':
    ans += 8

print(ans)