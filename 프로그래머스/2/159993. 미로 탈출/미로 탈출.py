from collections import deque 

def bfs(maps, sx, sy, tx, ty):
    q = deque()
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    q.append((sx, sy, 0))
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while q:
        x, y, cnt = q.popleft()
        if x == tx and y == ty:
            return cnt 
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == 0 and maps[nx][ny] != 'X':
                q.append((nx, ny, cnt+ 1))
                visited[nx][ny] = 1
    return -1
                
                
    
    
    
def solution(maps):
    for i in range(len(maps)):
        for k in range(len(maps[0])):
            if maps[i][k] == 'S':
                sx, sy = i, k
            elif maps[i][k] == 'L':
                lx, ly = i, k
            elif maps[i][k] == 'E':
                ex, ey = i, k
                
    p1 = bfs(maps, sx, sy, lx, ly)
    p2 = bfs(maps, lx, ly, ex, ey)
    if p1 != -1 and p2 != -1:
        return p1+p2
    else:
        return -1



# 갔던 길을 또방문하는 최단 거리의 경우는 레버를 찾기 이전과 찾고 난 후 사이에만 존재할 수 있음 
# 두가지 과정으로 나누어 접근 