from collections import deque 

def bfs(x, y, land, visited):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    min_num, max_num = y, y
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0
    while q:
        cx, cy = q.popleft()
        min_num = min(min_num, cy)
        max_num = max(max_num, cy)
        count += 1
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < len(land) and 0 <= ny < len(land[0]):
                if visited[nx][ny] == 0 and land[nx][ny] == 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    
    return count, min_num, max_num
         

def solution(land):
    answer = 0
    visited = [[0] * len(land[0]) for _ in range(len(land))]
    total = [0 for _ in range(len(land[0]))]
    for i in range(len(land)):
        for k in range(len(land[0])):
            if visited[i][k] == 0 and land[i][k] == 1:
                count, min_y, max_y = bfs(i, k, land, visited)
                for h in range(min_y, max_y+1):
                    total[h] += count
    return max(total)

# bfs 로 순회해서 덩어리 구함 
# 열별로 최대 시추량은 어떻게 구하지? -> 보드에 저장할 때 (석유량, 몇번째 땅인지) -> 열별로 탐색후 set으로 반환 -> 석유량 총합 구하기 
