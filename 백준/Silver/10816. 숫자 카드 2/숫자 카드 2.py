from collections import Counter 

n = int(input())
nums = list(map(int, input().split(" ")))
m = int(input())
get = list(map(int, input().split(" ")))

counter = Counter(nums)

for i in get:
  print(counter[i], end = " ")