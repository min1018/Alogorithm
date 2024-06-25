from collections import deque 

def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0: 
            q = deque()
            q.append(i)
            while q:
                curr = q.popleft()
                visited[curr] = 1
                for k in range(n):
                    if computers[curr][k] == 1 and curr != k and visited[k] != 1:
                        q.append(k)
                        visited[k] = 1
            answer += 1
    return answer