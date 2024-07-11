from collections import deque
import sys
input = sys.stdin.readline

spread = deque()

def spring_summer():
  for i in range(n):
    for k in range(n):
      if tree[i][k]:
        length = len(tree[i][k])
        for t in range(length):
          nxt = tree[i][k][t]
          if graph[i][k] < nxt:
            for _ in range(length - t):
              nxt = tree[i][k].pop()
              dead[i][k] += (nxt//2)
            break
          else:
            graph[i][k] -= nxt
            tree[i][k][t] += 1
            # 여기서 죽는 식물들 다 추가해서 돌기 
            if tree[i][k][t] % 5 == 0:
              spread.append((i, k))
      graph[i][k] += (dead[i][k]+food[i][k])
      dead[i][k] = 0


def fall_winter():
  dx = [0, 0, -1, 1, 1, 1, -1, -1]
  dy = [-1, 1, 0, 0, 1, -1, 1, -1]
  while spread:
    x, y = spread.popleft()
    for h in range(8):
      nx = x + dx[h]
      ny = y + dy[h]
      if 0 <= nx < n and 0 <= ny < n:
        tree[nx][ny].appendleft(1)



n, m, k = map(int, input().split(" "))
graph = [[5] * n for _ in range(n)] # 양분 
food = [list(map(int, input().split(" "))) for _ in range(n)]
dead = [[0] * n for _ in range(n)] #죽은 나무 
tree = [[deque() for _ in range(n)] for _ in range(n)] # 나무 


for _ in range(m):
  x, y, age = map(int, input().split(" "))
  tree[x-1][y-1].append(age)

for _ in range(k):
  spring_summer()
  fall_winter()

ans = 0

for i in range(n):
  for k in range(n):
    if tree[i][k]:
      ans += len(tree[i][k])

print(ans)


# https://www.acmicpc.net/board/view/99700