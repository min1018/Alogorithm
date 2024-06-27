from collections import deque 

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def like(friend):
  currMax = -1 
  visited = [[0] * n for _ in range(n)]
  poss = []
  for i in range(n):
    for k in range(n):
      if visited[i][k] == 0 and board[i][k] == 0:
        visited[i][k] = 1
        cnt = 0
        for h in range(4):
          nx = i + dx[h]
          ny = k + dy[h]
          if 0 <= nx <n and 0 <= ny < n:
            if board[nx][ny] in friend:
              cnt += 1
        if currMax < cnt:
          currMax = cnt
          poss = []
          poss.append((i, k))
        elif currMax == cnt:
          poss.append((i, k))
        
  return poss 

def blank(poss):
  result = []
  for x, y in poss:
    cnt = 0
    for h in range(4):
      nx = x + dx[h]
      ny = y + dy[h]
      if 0 <= nx <n and 0 <= ny < n:
        if board[nx][ny] == 0:
          cnt += 1
    result.append((x, y, cnt))
  return result 
          

n = int(input())
board = [[0] * n for _ in range(n)]
student = [[] for _ in range(n**2+1)]
for i in range(n**2):
  stu, l1, l2, l3, l4 = map(int, input().split(" "))
  friend = [l1, l2, l3, l4]
  student[stu] = friend
  ans = []
  ans = like(friend)
  #print("after like", ans)
  ans = blank(ans)
  #print("after blank", ans)
  ans.sort(key= lambda x : (-x[2], x[0], x[1]))
  x, y, cnt = ans[0]
  board[x][y] = stu

  #print("after", i+1, board)

score = 0
for x in range(n):
  for y in range(n):
    cnt = 0
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx <n and 0 <= ny < n:
        if board[nx][ny] in student[board[x][y]]:
          cnt += 1
    if cnt == 0:
      continue
    else:
      score += 10 ** (cnt - 1)

print(score)
  