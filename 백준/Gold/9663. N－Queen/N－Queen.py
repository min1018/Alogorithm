# 열 같으면 안됨, 행 같으면 안됨 
# 대각선이면 안됨 현재 퀸으로부터 x좌표 = y좌표 

def promising(x):
  for i in range(x):
    if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
      return False
  return True
    

def dfs(cnt):
  global ans 
  if cnt == n:
    ans += 1
    return 
  for i in range(n):
    row[cnt] = i
    if promising(cnt): #백
      dfs(cnt + 1)

n = int(input())
row = [0] * n
ans = 0
dfs(0)
print(ans)