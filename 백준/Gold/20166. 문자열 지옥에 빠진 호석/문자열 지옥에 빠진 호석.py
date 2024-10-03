from sys import setrecursionlimit, stdin
setrecursionlimit(10 ** 6)
input = stdin.readline
# 8방향, 재방문 가능 

n, m, k = map(int, input().split(" "))

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [0, -1, 1, -1, 1, -1, 0, 1]

board = [list(input().rstrip()) for _ in range(n)]
keep = set()
ans = {}
for _ in range(k):
    word = input().rstrip()
    keep.add(word)
    ans[word] = 0

def solve(x, y, cnt, word):
    if cnt > 5:
        return 
    if word in keep:
        ans[word] += 1
    for i in range(8):
        nx, ny = (x+dx[i]+n)%n, (y+m+dy[i])%m
        solve(nx, ny, cnt+1, word+board[nx][ny])


for i in range(n):
    for k in range(m):
        start = ''
        solve(i, k, 1, start + board[i][k])


for k in keep:
    print(ans[k])


