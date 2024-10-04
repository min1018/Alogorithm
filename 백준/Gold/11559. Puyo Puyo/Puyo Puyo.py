from collections import deque 

def popPuyo(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append((x, y))
    visited[x][y] = 1 
    color = board[x][y]
    keep = []
    keep.append((x, y))

    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == 0 and board[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = 1
                keep.append((nx, ny))
    return keep
                
def delete(keep):
    for x, y in keep:
        board[x][y] = '.'

    
def fall():
    for col in range(6):
        empty = 11 
        for row in range(11, -1, -1):
            if board[row][col] != '.':  
                board[empty][col], board[row][col] = board[row][col], board[empty][col]
                empty -= 1 


board = [list(input().rstrip()) for _ in range(12)]

cnt = 0
while True:
    fall()
    flag = 0
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for k in range(6):
            if visited[i][k] == 0 and board[i][k] != '.':
                keep = popPuyo(i, k)
                if len(keep) >=4:
                    delete(keep)
                    flag = 1
    if flag == 0:
        break
    cnt += 1
    


print(cnt)