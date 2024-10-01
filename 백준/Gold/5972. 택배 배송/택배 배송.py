import sys
import heapq

def dijkstra(n):
    q = []
    heapq.heappush(q, (0, 1)) # cost, idx
    distance[1] = 0

    while q: 
        dist, curr = heapq.heappop(q)
        if dist > distance[curr]:
            continue
        for i, w in graph[curr]:
            cost = dist + w
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))
    return distance[n]
                


n, m = map(int, input().split(" "))
graph = [[] for _ in range(n+1)]
distance = [sys.maxsize] * (n+1)

for _ in range(m):
    a, b, cost = map(int, input().split(" "))
    graph[a].append((b, cost))
    graph[b].append((a, cost))

print(dijkstra(n))

# heapq [0]을 기준으로 소팅