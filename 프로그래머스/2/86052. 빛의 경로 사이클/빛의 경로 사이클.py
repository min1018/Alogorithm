from collections import deque 

def solution(grid):
    answer = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # s 그대로, r +3%4, l +1%4
    ly = len(grid) 
    lx = len(grid[0])
    
    visited = [[[0] * 4 for _ in range(lx)] for _ in range(ly)]
    
    for y in range(ly):
        for x in range(lx):
            for d in range(4):
                if visited[y][x][d] == 1 :
                    continue
                count = 0
                ny, nx = y, x 
                while visited[ny][nx][d] == 0:
                    visited[ny][nx][d] = 1
                    count += 1 
                    if grid[ny][nx] == 'L':
                        d = (d + 1) % 4
                    elif grid[ny][nx] == 'R':
                        d = (d + 3) % 4
                    ny = (ny + dy[d]) % ly
                    nx = (nx + dx[d]) % lx
                answer.append(count)
                
    answer.sort()
    return answer
                     