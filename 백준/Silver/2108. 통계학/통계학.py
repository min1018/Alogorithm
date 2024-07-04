from collections import Counter

n = int(input())
nums = [int(input()) for _ in range(n)]

nums.sort()
print(round(sum(nums)/n))
print(nums[n//2])

counter_sort = sorted(Counter(nums).items(), key = lambda x : (-x[1], x[0]))
if n == 1:
  print(nums[0])
else:
  if counter_sort[0][1] != counter_sort[1][1]:
    print(counter_sort[0][0])
  else:
    print(counter_sort[1][0])
print(nums[-1] - nums[0])
      