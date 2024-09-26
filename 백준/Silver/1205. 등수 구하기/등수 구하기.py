curr, new, maxLen = map(int, input().split(" "))
if curr == 0:
    print(1)
    exit()
    
scores = list(map(int, input().split(" ")))


if curr >= maxLen:
    if scores[-1] >= new:
        print(-1)
        exit()

scores.append(new)
scores.sort(reverse=True)

ans = 0
for i in range(len(scores)):
    ans += 1
    if new == scores[i]:
        print(ans)
        break