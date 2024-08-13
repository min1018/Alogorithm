import sys
input = sys.stdin.readline 

n = int(input())
nums = [int(input()) for _ in range(n)]

limit = max(nums)
dp = [0] * 5001
dp[0] = 1

for i in range(2, 5001, 2):
  for k in range(2, i+1, 2):
    dp[i] += dp[k-2] * dp[i-k]
  dp[i] = dp[i] % 1000000007

for num in nums:
  print(dp[num])