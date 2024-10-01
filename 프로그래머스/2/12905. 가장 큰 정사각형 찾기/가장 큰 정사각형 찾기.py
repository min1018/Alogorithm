def solution(board):
    ans = 0

    for i in range(1, len(board)):
        for k in range(1, len(board[0])):
            if board[i][k] == 1:
                board[i][k] = min(board[i-1][k-1], board[i-1][k], board[i][k-1])+1

    for i in range(len(board)):
        ans = max(ans, max(board[i]))
    return ans**2