from itertools import combinations 
import sys 

n = int(input())
nums = [i for i in range(n)]
taste = [list(map(int, input().split(" "))) for _ in range(n)]

keep = []
for i in range(1, n+1):
    keep += list(combinations(nums, i))

ans = sys.maxsize
for k in keep:
    sour = 1
    bitter = 0
    for idx in k:
        sour *= taste[idx][0]
        bitter += taste[idx][1] 
    ans = min(ans, abs(sour-bitter))
        
print(ans)
