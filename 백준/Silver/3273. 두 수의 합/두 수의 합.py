n = int(input())
nums = list(map(int, input().split(" ")))
target = int(input())

nums.sort()
left, right = 0, n-1
answer = 0
while left < right:
    curr = nums[left] + nums[right]
    if curr < target:
        left += 1
    elif curr > target:
        right -= 1
    elif curr == target:
        left += 1
        answer += 1
print(answer)