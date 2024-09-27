n = int(input())
count = int(input())
where = list(map(int, input().split(" ")))

ans = where[0]
for i in range(len(where)-1):
    temp = (where[i+1]-where[i])
    if temp % 2 == 1:
        temp += 1
    ans = max(ans, temp//2)
ans = max(ans, n-where[-1])
print(ans)