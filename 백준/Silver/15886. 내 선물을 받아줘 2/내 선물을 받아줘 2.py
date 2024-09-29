n = int(input())

road = list(input().rstrip())
visited = [0] * n 

ans = 0
for i in range(n-1):
    if road[i] == 'W' and road[i+1] == 'E':
        ans += 1
print(ans+1)