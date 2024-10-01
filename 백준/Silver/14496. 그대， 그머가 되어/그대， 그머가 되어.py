import sys
import heapq

def dijkstra(start, target ):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + 1
            if cost < distance[i] :
                distance[i] = cost
                heapq.heappush(q, (cost, i))
            if i == target:
                return cost
    return -1

start, target = map(int, input().split(" "))
if start == target:
    print(0)
    exit()
word, sets = map(int, input().split(" "))

graph = [[] for _ in range(word+1)]
distance = [sys.maxsize] * (word+1)

for _ in range(sets):
    a, b= map(int, input().split(" "))
    graph[a].append(b)
    graph[b].append(a)
print(dijkstra(start, target))
