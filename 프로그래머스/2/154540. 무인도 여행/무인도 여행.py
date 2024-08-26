from collections import deque 

def bfs(x, y, maps, visited):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append((x, y))
    
    stay = 0
    
    while q:
        cx, cy = q.popleft()
        stay += int(maps[cx][cy])
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != 'X' and visited[nx][ny] != 1:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
    return stay
                    
            
def solution(maps):
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    answer = []
        
    for i in range(len(maps)):
        for k in range(len(maps[0])):
            if maps[i][k] != 'X' and visited[i][k] == 0:
                visited[i][k] = 1
                days = bfs(i, k, maps, visited)
                answer.append(days)
                
    if len(answer) == 0:
        answer.append(-1)
    else: 
        answer.sort()
        
    return answer