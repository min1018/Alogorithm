n, x = map(int, input().split(" "))
visitor = list(map(int, input().split(" ")));


ans = 1
temp = sum(visitor[0:0+x])
maxV = temp

for i in range(1, n-x+1):
    temp = temp - visitor[i-1] + visitor[i+x-1]
    if (maxV < temp):
        maxV = temp
        ans = 1
    elif maxV == temp:
        ans += 1

if maxV == 0:
    print("SAD")
else:
    print(maxV)
    print(ans)