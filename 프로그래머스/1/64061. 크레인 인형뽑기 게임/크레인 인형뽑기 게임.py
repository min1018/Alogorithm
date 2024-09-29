def solution(board, moves):
    stack = []
    answer = 0
    for i in moves:
        for k in range(len(board)):
            if board[k][i-1] != 0:
                if stack and stack[-1] == board[k][i-1]:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(board[k][i-1])
                board[k][i-1] = 0
                break
    return answer

# stack[-1] == curr -> stack.pop()