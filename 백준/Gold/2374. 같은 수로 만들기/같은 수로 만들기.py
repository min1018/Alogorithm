import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10 ** 9)

n = int(input())
nums = [int(input()) for _ in range(n)]

result = 0

def sol(nums):
  global result 
  size = len(nums)
  if size == 1:
    return nums[0]
  if size == 0:
    return None

  maxVal = max(nums)
  idx = nums.index(maxVal)

  left_max = sol(nums[:idx])
  right_max = sol(nums[idx+1:])

  if left_max is not None:
    result += maxVal - left_max
  if right_max is not None:
    result += maxVal - right_max

  return maxVal

sol(nums)

print(result)