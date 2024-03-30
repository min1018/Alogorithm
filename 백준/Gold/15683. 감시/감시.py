# 1 -> 한쪽 방향 ㅎ
# 2 -> 양 방향 
# 3 -> 90도 차이
# 4 -> 붙어서 세 방향 
# 5 -> 모든 방향 
# 6 -> 벽 
# 감시 카메라 방향 조절헤서 사각 지대의 최소 개수 

# 조합처럼 다 따져서해야하나 독독한 접근을 해야하나 
# 그 순간 최대가 과연 진찌 최대일까?

# 각 경우 별로 1, 2, 3, 4, 5 번으로 배열을 두고 
# 각각의 경우에 대해 감시할 수 있는 영역을 세어서
# 소팅한 후 최적의 경우만 반영 
# -> 포문을 너무 많이 돌지 않아? -> 안해보고 최적인지 어케 알지? 
#-> dfs 를 사용한 노가다

import copy

# 동 남 북 서 
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

# 1번 - 1, 2, 3, 4
# 2번 - 14, 23
# 3번 - 12, 24, 34, 14
# 4번 - 123, 234, 124, 134
cctvDir = [
  [],
  [[0], [1], [2], [3]],
  [[0, 3], [1, 2]],
  [[0, 1], [1, 3], [2, 3], [0, 2]],
  [[0, 1, 2], [1, 2, 3], [0, 1, 3], [0, 2, 3]],
  [[0, 1, 2, 3]]
]

def dfs(graph, depth):
  global ans 
  if depth == len(cctv):
    cnt = 0 
    for i in range(f):
      cnt += graph[i].count(0)
    ans = min(ans, cnt)
    return 
  temp = copy.deepcopy(graph)
  x, y, type = cctv[depth]
  for cdir in cctvDir[type]:
    watch(x, y, cdir, temp)
    dfs(temp, depth + 1)
    temp = copy.deepcopy(graph)


def watch(x, y, dir, temp): 
  for d in dir:
    nx = x
    ny = y 
    while True:
      nx += dx[d]
      ny += dy[d]
      if 0 <= nx < f and 0<= ny < w:
        if temp[nx][ny] == 6 :
          break
        elif temp[nx][ny] == 0:
         temp[nx][ny] = -1
      else:
         break
          
  
ans = int(1e9)
f, w = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(f)]

cctv = []
for i in range(f):
  for k in range(w):
    if 1 <= graph[i][k] <= 5:
      cctv.append((i, k, graph[i][k]))
      

dfs(graph, 0)
print(ans)


