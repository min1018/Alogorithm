n, total = map(int, input().split(" "))

road = [i for i in range(total+1)]
discount = [list(map(int, input().split(" "))) for _ in range(n)]
discount.sort()

for start, end, weight in discount:
    if end <= total:
        road[end] = min(road[end], road[start] + weight)
        for i in range(end+1, total+1):
            road[i] = min(road[i], road[i-1]+1)

print(road[total])
