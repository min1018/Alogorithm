from itertools import combinations

n, m = map(int, input().split(" "))

graph = []
house = []
chicken = []
for i in range(n):
  graph.append(list(map(int, input().split(" "))))
  for k in range(n):
    if graph[i][k] == 1:
      house.append((i,k))
    elif graph[i][k] == 2:
      chicken.append((i,k))

result = 999999999
for case in list(combinations(chicken, m)):
  ans = 0
  for x, y in house:
    temp = 99999999
    for a, b in case:
      temp = min(temp, abs(a-x) + abs(b-y))
    ans += temp
  result = min(ans, result)

print(result)