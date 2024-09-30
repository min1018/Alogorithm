n = int(input())
m = int(input())
seat = []
must = [int(input()) for _ in range(m)]
last = 0
for i in must:
    if i - last != 1 and i - last > 0:
        seat.append(i-last-1)
    last = i
seat.append(n-last)
limit = max(seat)

dp = [1] * (n+2)
dp[1] = 1
dp[2] = 2
for i in range(3, limit+1):
    dp[i] = dp[i-1] + dp[i-2]

ans = 1
for i in seat:
    ans *= dp[i]
print(ans)