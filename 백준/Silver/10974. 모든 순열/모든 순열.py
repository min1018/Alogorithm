from itertools import permutations 

n = int(input())
num = [i for i in range(1, n+1)]

nums = list(permutations(num, n))
for t in nums:
  print(*t)
