def solution(park, routes):
    answer = []
    dx = [-1, 1, 0, 0] # N S W E 
    dy = [0, 0, -1, 1]
    x, y = 0, 0

    for i in range(len(park)):
        for k in range(len(park[0])):
            if park[i][k] == 'S':
                x, y = i, k
    
    for move in routes:
        dir, dis = move.split(" ")
        if dir == 'N' :
            d = 0
        if dir == 'S' :
            d = 1 
        if dir == 'W' :
            d = 2 
        if dir == 'E' :
            d = 3
        sx, sy = x, y
        for i in range(int(dis)):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < len(park) and 0 <= ny < len(park[0]) and park[nx][ny] != 'X':
                x, y = nx, ny
            else:
                x, y = sx, sy
                break
        
    answer = [x, y]       
    return answer