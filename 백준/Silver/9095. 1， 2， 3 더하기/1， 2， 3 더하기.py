def dfs(curr, target):
  global cnt 
  if curr == target:
    cnt += 1 
    return 
  if curr > target:
    return 
  for i in range(1, 4):
    dfs(curr+i, target)

n = int(input())
nums = [int(input()) for _ in range(n)]
for target in nums:
  cnt = 0
  dfs(1, target)
  dfs(2, target)
  dfs(3, target)
  print(cnt)