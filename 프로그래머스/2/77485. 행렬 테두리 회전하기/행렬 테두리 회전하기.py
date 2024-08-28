answer = []

def rotate(board, a, b, c, d):
    global answer 
    
    curr = board[a][b]
    temp = 0
    cx, cy = a, b
    save = []
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    
    while True:
        cx, cy = cx + dx[dir], cy + dy[dir]   
        if not a <= cx <= c or not b <= cy <= d:
            cx, cy = cx - dx[dir], cy - dy[dir]
            if dir == 3:
                break
            dir += 1
            continue
        next = board[cx][cy]
        board[cx][cy] = curr
        curr = next
        save.append(curr)
         
    answer.append(min(save))
    
    return board 
        
            
            

def solution(rows, columns, queries):
    board = [[0] * columns for _ in range(rows)]
    cnt = 1
    for i in range(rows):
        for k in range(columns):
            board[i][k] = cnt 
            cnt += 1
            
    for q in queries:
        a, b, c, d = q[0]-1, q[1] - 1, q[2] - 1, q[3] - 1
        rotate(board, a, b, c, d)
            
    return answer