from collections import deque
import copy

def move(temp, num):
  if num == 0: # 상
    for k in range(n):
      pointer = 0
      for i in range(1, n):
        if temp[i][k] :
          tmp = temp[i][k]
          temp[i][k] = 0
          if temp[pointer][k] == 0:
            temp[pointer][k] = tmp
          elif temp[pointer][k] == tmp:
            temp[pointer][k] *= 2
            pointer += 1
          else:
            pointer+= 1
            temp[pointer][k] = tmp
  elif num == 1: #하
    for k in range(n):
      pointer = n-1
      for i in range(n-2, -1, -1):
        if temp[i][k] :
          tmp = temp[i][k]
          temp[i][k] = 0
          if temp[pointer][k] == 0:
            temp[pointer][k] = tmp
          elif temp[pointer][k] == tmp:
            temp[pointer][k] *= 2
            pointer -= 1
          else:
            pointer -= 1
            temp[pointer][k] = tmp
  elif num == 2: #좌
    for i in range(n):
      pointer = 0
      for k in range(1, n):
        if temp[i][k]:
          tmp = temp[i][k]
          temp[i][k] = 0
          if temp[i][pointer] == 0:
            temp[i][pointer] = tmp
          elif temp[i][pointer] == tmp:
            temp[i][pointer] *= 2
            pointer += 1
          else:
            pointer += 1
            temp[i][pointer] = tmp
  elif num == 3: #우
    for i in range(n):
      pointer = n-1
      for k in range(n-2, -1, -1):
        if temp[i][k]:
          tmp = temp[i][k]
          temp[i][k] = 0
          if temp[i][pointer] == 0:
            temp[i][pointer] = tmp
          elif temp[i][pointer] == tmp:
            temp[i][pointer] *= 2
            pointer -= 1
          else:
            pointer -= 1
            temp[i][pointer] = tmp
  return temp



def dfs(temp, depth):
  global ans
  if depth == 5:
    for i in range(n):
      ans = max(ans, max(temp[i]))
    return
  for i in range(4):
    temp_ = move(copy.deepcopy(temp), i)
    dfs(temp_, depth+1)
    
  

n = int(input())
temp = [list(map(int, input().split(" "))) for _ in range(n)]
ans = 0

dfs(temp, 0)
print(ans)


# 이문제도 결국 dfs를 사용해 모든 경우의 수를 탐방해야하는 그 맥락 