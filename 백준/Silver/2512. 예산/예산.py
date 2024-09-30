n = int(input())

bill = list(map(int, input().split(" ")))
total = int(input())

start = 1
end = max(bill)
ans = 0
while start <= end:
    mid = (start+end)//2
    case = 0
    for i in range(n):
        case += min(bill[i], mid)
    if case <= total:
        start = mid+1
        ans = mid
    else:
        end = mid-1


print(ans)