n = int(input())
nums = list(map(int, input().split(" ")))

ans = 0
start, end = 0, 0
temp = set()

while start < n and end < n:
    if nums[end] not in temp:
        temp.add(nums[end])
        end += 1
        ans += end-start
    else:
        while nums[end] in temp:
            temp.remove(nums[start])
            start += 1
print(ans)