from itertools import combinations 

n, m = map(int, input().split())
nums = [i+1 for i in range(n)]

nxt = list(combinations(nums, m))

for a in nxt:
   print(*a)