from collections import deque 

def solution(x, y, n):
    q = deque()
    q.append((x, 0))
    
    visited = [0] * (y+1)
    
    while q:
        curr, cnt = q.popleft()
        if curr == y:
            return cnt
        if curr * 2 <= y and visited[curr*2] != 1:
            q.append((curr * 2, cnt + 1))
            visited[curr*2] = 1 
        if curr + n <= y and visited[curr+n] != 1:
            q.append((curr + n , cnt + 1))
            visited[curr + n] = 1
        if curr * 3 <= y and visited[curr*3] != 1:
            q.append((curr * 3, cnt + 1))
            visited[curr * 3] = 1
    
    return -1
