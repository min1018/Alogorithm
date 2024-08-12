n = int(input())

nums = [int(input()) for _ in range(n)]
limit = max(nums)

dp = [(0, 0, 0)] * 10001
dp[1] = (1, 0, 0)
dp[2] = (1, 1, 0)
dp[3] = (2, 0, 1)

for i in range(4, limit + 1):
  dp[i] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2], dp[i-2][1] + dp[i-2][2], dp[i-3][2])

for num in nums:
  print(dp[num][0]+dp[num][1]+dp[num][2])