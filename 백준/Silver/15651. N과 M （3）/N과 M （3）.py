from itertools import product 

n, m = map(int, input().split(" "))
nums = [i for i in range(1, n+1)]
result = product(nums, repeat = m)
for x in result:
  print(*x)