n = int(input())
liquid = list(map(int, input().split(" ")))
liquid.sort()

start, end = 0, n-1
keep = liquid[start]+liquid[end]
ks, ke = start, end
while start < end:
    tmp = liquid[start] + liquid[end]
    if abs(tmp) < abs(keep):
        keep = tmp
        ks, ke = start, end
        if keep == 0:
            break
    if tmp < 0:
        start += 1
    else:
        end -= 1
print(liquid[ks], liquid[ke])