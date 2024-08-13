import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split(" ")))

dp = [[0] * n for _ in range(n)]
for i in range(n):
  dp[i][i] = 1

for i in range(n-1):
  if nums[i] == nums[i+1]:
    dp[i][i+1] = 1

for i in range(n-2):
  for start in range(n-2-i):
    end = start + 2 + i
    if nums[start] == nums[end] and dp[start+1][end-1] == 1:
      dp[start][end] = 1
    

q = int(sys.stdin.readline())
for _ in range(q):
  start, end = map(int, sys.stdin.readline().split(" "))
  print(dp[start-1][end-1])