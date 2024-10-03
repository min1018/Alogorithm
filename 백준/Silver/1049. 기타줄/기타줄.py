import math

n, m = map(int, input().split(" "))

ans = 0
much = []
dozen, each = 1001, 1001
for _ in range(m):
    a, b = map(int, input().split(" "))
    dozen, each = min(a, dozen), min(b, each)

ans = min(n*each, math.ceil(n/6)*dozen, (n//6) * dozen+each*(n%6))
print(ans)
    
# 6줄 패키지, 1개 그이상 낱개 