def win(board, word):
    for i in range(3): # 세로
        if board[i][0] == board[i][1] == board[i][2] == word:
            return 1
        
    for i in range(3): # 가로
        if board[0][i] == board[1][i] == board[2][i] == word:
            return 1
        
    #대각선 
    if board[0][0] == board[1][1] == board[2][2] == word:
        return 1
    
    if board[2][0] == board[1][1] == board[0][2] == word:
        return 1
    
    return -1 

def solution(board):
    Ocount = 0
    Xcount = 0
    for i in range(3):
        for k in range(3):
            if board[i][k] == 'O':
                Ocount += 1
            elif board[i][k] == 'X':
                Xcount += 1
                
    if (Ocount + Xcount) % 2 == 0: # O부터 함 보장 
        if Ocount != Xcount :
            return 0
    if (Ocount + Xcount) % 2 == 1: # O부터 함 보장  
        if Ocount != Xcount + 1 :
            return 0
    
    Owin = win(board, 'O')
    Xwin = win(board, 'X')
    if Owin == 1 and Xwin == 1:
        return 0
    if Owin == 1 and Ocount != Xcount+1:
        return 0
    if Xwin == 1 and Xcount != Ocount:
        return 0
    
    return 1

# 1. O 부터 시작 => 총 홀수개라면 동그라미가 더 많은지 확인하면 됨 / 짝수개라면 그냥 개수가 같으면 됨 
# 2. 한명이 승리되어 게임이 종료 됨 -> 더 생기면 안됨 / 검사하기 위해서는 대각선, 직선으로 확인
#    => 

