board = [list(map(int, input().split(" "))) for _ in range(5)]

call = []
for _ in range(5):
    call.append(list(map(int, input().split(" "))))

def check(board):
    cnt = 0
    for i in range(5):
        if len(set(board[i])) == 1 and board[i][0] == -1:
            cnt += 1
    for i in range(5):
        flag = 0
        for k in range(5):
            if board[k][i] != -1:
                flag = 1
                break
        if flag == 0:
            cnt += 1
            
    flag = 0
    for i in range(5):
        if board[i][i] != -1:
            flag = 1
            break
    if flag == 0:
        cnt += 1
    
    flag = 0
    for i in range(5):
        if board[i][4-i] != -1:
            flag = 1
            break
    if flag == 0:
        cnt += 1

    return cnt 
    
time = 0
for nums in call:
    for num in nums:
        time += 1
        for i in range(5):
            for k in range(5):
                if board[i][k] == num:
                    board[i][k] = -1
        if time >= 12:
            if check(board) >= 3:
                print(time)
                exit()