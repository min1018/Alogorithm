def solution(n):
    answer = [list(0 for _ in range(i+1)) for i in range(n)]
    
    x, y = 0, 0 
    cnt = 0 
    dir = 0  
    sta = sum(i for i in range(1, n+1))


    dx = [1, 0, -1]
    dy = [0, 1, -1]

    while True:
        cnt += 1
        if cnt > sta:
            break 
        
        answer[x][y] = cnt
        
        nx, ny = x + dx[dir], y + dy[dir]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= len(answer[nx]) or answer[nx][ny] != 0:
            dir = (dir + 1) % 3  
            nx, ny = x + dx[dir], y + dy[dir]  
            
        x, y = nx, ny

    result = []
    for sublist in answer:
        for item in sublist:
            result.append(item)
            
    return result
