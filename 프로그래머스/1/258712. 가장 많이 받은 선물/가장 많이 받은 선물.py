def solution(friends, gifts):
    answer = 0
    dic = {}
    for i in range(len(friends)):
        dic[friends[i]] = i
        
    n = len(friends)
    rate = {}
    
    board = [[0] * (n) for _ in range(n)]
    for i in gifts:
        s, t = i.split(" ")
        board[dic[s]][dic[t]] += 1
        if dic[s] in rate:
            rate[dic[s]] += 1
        else:
            rate[dic[s]] = 1
        if dic[t] in rate:
            rate[dic[t]] -= 1
        else:
            rate[dic[t]] = -1
            
    gift = [0] * (n)
    for i in range(n):
        for k in range(i+1, n):
            if board[i][k] > board[k][i]: # i가 더 많이 줌 
                gift[i] += 1
            elif board[i][k] < board[k][i]: # k가 더 많이 줌 
                gift[k] += 1
            else: #선물 지수 비교 
                if i in rate and k in rate and rate[i] > rate[k]:
                    gift[i] += 1
                elif i in rate and k in rate and rate[k] > rate[i]:
                    gift[k] += 1
                elif i in rate and k not in rate and rate[i] > 0:
                    gift[i] += 1
                elif k in rate and i not in rate and rate[k] > 0:
                    gift[k] += 1
                
        
    return max(gift)

# 선물 더 -> 다음 달 
# 기록X, 준거 == 받은거 -> 선물 지수 큰 => 선물 지수 작은 

