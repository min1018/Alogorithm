from itertools import combinations

n = int(input())
graph = [list(map(int, input().split(" "))) for _ in range(n)]

power = []
link = []
start = []
for i in combinations(range(n), n//2):
  team = 0
  for j in combinations(i, 2):
    team += graph[j[0]][j[1]] + graph[j[1]][j[0]]
  power.append(team)
link = power[len(power)//2:]
start = power[:len(power)//2]
result = float('inf')
for i in range(len(link)):
  result = min(result, abs(link[len(link)-1-i] - start[i]))
print(result)