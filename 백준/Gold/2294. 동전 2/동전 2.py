n, total = map(int, input().split(" "))

coin = [int(input()) for _ in range(n)]

dp = [1000001] * (total+1)
dp[0] = 0

for i in coin:
    for j in range(1, total+1):
        if j-i >= 0:
            dp[j] = min(dp[j], dp[j-i] + 1)

if dp[total] == 1000001:
    print(-1)
else:
    print(dp[total])
