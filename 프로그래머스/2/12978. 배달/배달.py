from collections import deque

def dijkstra(dist, adj):
    q = deque()
    q.append([1, 0])
    
    while q:
        node, cost = q.popleft()
        for n, c in adj[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c 
                q.append([n, cost+c])
                
                
def solution(N, road, K):
    dist = [K+1] * (N+1)
    dist[1] = 0
    adj = [[] for _ in range(N+1)]
    for i, k, w in road:
        adj[i].append([k, w])
        adj[k].append([i, w])
    dijkstra(dist, adj)
    #print(dist)
    return len([i for i in dist if i <= K])