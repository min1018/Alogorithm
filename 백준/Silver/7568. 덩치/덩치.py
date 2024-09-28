n = int(input())

case = [list(map(int, input().split(" "))) for _ in range(n)]

ans = []
for i in range(n):
    sw, sh = case[i][0], case[i][1]
    rank = 1
    for k in range(n):
        cw, ch = case[k][0], case[k][1]
        if sw < cw and sh < ch:
            rank += 1
    ans.append(rank)
    
print(*ans)
        