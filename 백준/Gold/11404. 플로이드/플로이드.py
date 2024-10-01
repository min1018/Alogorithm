import sys

n = int(input())
m = int(input())

def FloydWarshall():
    for k in range(n):
        for i in range(n):
            for h in range(n):
                if board[i][h] > board[i][k] + board[k][h]:
                    board[i][h] = board[i][k] + board[k][h]
    for i in range(n):
         for k in range(n):
             if board[i][k] == sys.maxsize or i == k:
                    board[i][k] = 0
    return






board = [[sys.maxsize] * (n) for _ in range(n)]
for i in range(n):
    board[i][i] = 0

for _ in range(m):
    a, b, cost = map(int, input().split(" "))
    board[a-1][b-1] = min(cost, board[a-1][b-1])


FloydWarshall()
for i in board:
    print(*i)
