from collections import defaultdict

n, k = map(int, input().split(" "))
nums = list(map(int, input().split(" ")))

start, end = 0, 0

count = defaultdict(int)

answer = 0
while end < n:
    if count[nums[end]] >= k:
        count[nums[start]] -= 1
        start += 1
    else:
        count[nums[end]] += 1
        end += 1
        answer = max(answer, end-start)
print(answer)