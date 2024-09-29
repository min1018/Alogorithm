import sys

n, target = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

left, right = 0, 0
answer = sys.maxsize
curr = nums[0]
while left<= right:
    if curr < target:
        right += 1
        if right >= n:
            break
        curr += nums[right]
    elif curr >= target:
        curr -= nums[left]
        answer = min(answer, right-left+1)
        left += 1
 
if answer == sys.maxsize:
    print(0)
else:
    print(answer)
        