import sys

def dfs(depth, ans, calc):
    global n, minVal, maxVal
    if depth == n:
        minVal = min(ans, minVal)
        maxVal = max(ans, maxVal)
        return 

    for i in range(4):
        if cnt[i] > 0:
            cnt[i] -= 1
            if i == 0:
                dfs(depth+1, ans+nums[depth], cnt)
            elif i == 1:
                dfs(depth+1, ans-nums[depth], cnt)
            elif i == 2:
                dfs(depth+1, ans*nums[depth], cnt)
            elif i == 3:
                dfs(depth+1, int(ans/nums[depth]), cnt)
            cnt[i] += 1

n = int(input())
minVal, maxVal = sys.maxsize, -sys.maxsize

nums = list(map(int, input().split(" ")))
cnt = list(map(int, input().split(" ")))


dfs(1, nums[0], cnt)
print(maxVal)
print(minVal)

