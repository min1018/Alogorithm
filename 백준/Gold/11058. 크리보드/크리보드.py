import sys 

input = sys.stdin.readline 

n = int(input())
dp = [i for i in range(0, n+1)] #6번째까지는 무관

for i in range(7, n+1):
  dp[i] = max(dp[i-3] * 2, dp[i-4] * 3, dp[i-5] * 4) 

print(dp[n])