def solution(dirs):
    dir = {'U':(-1, 0), 'D':(1, 0), 'R':(0, 1), 'L':(0, -1)}
    
    answer = set()
    x, y = 0, 0
    
    for d in dirs:
        dx, dy = dir[d]
        nx, ny = x + dx, y + dy
        
        if abs(nx) <= 5 and abs(ny) <= 5:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x, y = nx, ny
    
    return len(answer) // 2


# 처음 걸어본 '길' 점이 아닌 길 