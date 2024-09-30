n = int(input())

dp = [1, 1, 1]
for _ in range(n-1):
    nxt = [0] * 3
    nxt[0] = (dp[0] + dp[1] + dp[2]) % 9901
    nxt[1] = (dp[0] + dp[2]) % 9901
    nxt[2] = (dp[0] + dp[1]) % 9901 
    dp = nxt
print(sum(dp)%9901)