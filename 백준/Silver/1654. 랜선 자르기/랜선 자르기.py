n, m = map(int, input().split(" "))
keep = [int(input()) for _ in range(n)]

start = 1
end = max(keep)

while start <= end:
    mid = (start+end)//2
    case = 0
    for i in range(n):
        case += keep[i]//mid
    if case < m:
        end = mid-1
    else:
        start = mid+1


print(end)