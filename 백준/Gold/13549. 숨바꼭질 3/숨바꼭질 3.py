from collections import deque 

n, k = map(int, input().split(" "))

def bfs(x, y):
    q = deque()
    q.append((x, 0))
    visited = [0] * 100001
    visited[x] = 1
    while q:
        num, cnt = q.popleft()
        if num == y:
            return cnt
        c3 = num * 2 
        if 0 <= c3 <= 100000 and visited[c3] == 0:
            q.appendleft((c3, cnt))
            visited[c3] = 1
        c1 = num - 1 
        if 0 <= c1 <= 100000 and visited[c1] == 0:
            q.append((c1, cnt+1))
            visited[c1] = 1
        c2 = num + 1
        if 0 <= c2 <= 100000 and visited[c2] == 0:
            q.append((c2, cnt+1))
            visited[c2] = 1 
        
    
    
print(bfs(n, k))