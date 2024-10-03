def dfs(i, ans):
    global l, c
    
    if len(ans) == l:
        cnt = 0
        for m in mo:
            if m in ans:
                cnt += 1
        if cnt >= 1 and len(ans)-cnt >= 2:        
            result.append(ans)
            return 
            
    for k in range(i, c):
        dfs(k+1, ans+word[k])


l, c = map(int, input().split(" "))
word = list(input().split(" "))
mo = ['a', 'e', 'i', 'o', 'u']
visited = [0] * c
word.sort()

result = []
dfs(0, '')
for r in result:
    print(r)