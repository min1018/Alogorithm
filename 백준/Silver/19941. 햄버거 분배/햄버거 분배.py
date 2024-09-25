n, k = map(int, input().split(" "))
line = list(input().rstrip())

ans = 0
for i in range(len(line)):
    if line[i] == 'P':
        for h in range(i-k, i+k+1):
            if 0<= h < len(line) and line[h] == 'H':
                ans += 1
                line[h] = 'yum'
                break
print(ans)
                