n = int(input())
temp = list(map(int, input().split(" ")))
temp.sort()

ans = 0
for i in range(n):
    start, end = 0, n-1
    while start < end:
        curr = temp[start] + temp[end]
        if temp[i] == curr:
            if i == start or i == end:
                if start == i:
                   start += 1
                elif end == i:
                    end -= 1
            else:
                ans += 1
                break
        elif curr > temp[i]:
            end -= 1
        elif curr < temp[i]:
            start += 1
            
print(ans)

# 5
# -1 0 1 2 3
# 