import sys

input = sys.stdin.readline

n, w = map(int, input().split(" "))
dp = [[0] * (w+1) for _ in range(n+1)]

bag = [[0,0]]
for _ in range(n):
  bag.append(list(map(int, input().split(" "))))

for i in range(1, n+1):
  for k in range(1, w+1):
    wei = bag[i][0]
    v = bag[i][1]
    if k < wei: # 담을 수 없음 
      dp[i][k] = dp[i-1][k]
    else: # 담을 수 있음 
      dp[i][k] = max(dp[i-1][k], dp[i-1][k-wei]+v)

print(dp[n][w])