from itertools import product 
def solution(users, emoticons):
    answer = [0, 0]
    
    discount = list(product([10, 20, 30, 40], repeat = len(emoticons)))
    
    for d in discount:
        pay = [0] * len(users)
        for i in range(len(users)):
            for k in range(len(emoticons)):
                if d[k] >= users[i][0]: #기준보다 더 할인 -> 구매 
                    pay[i] += (emoticons[k]) * (100-d[k])/100
        
        # 플러스 여부 
        join = 0
        for i in range(len(users)):
            if pay[i] >= users[i][1]:
                pay[i] = 0
                join += 1
        
        if join > answer[0]:
            answer[0] = join
            answer[1] = sum(pay)
        if join == answer[0]:
            answer[1] = max(sum(pay), answer[1])
                    
    return answer


# 구매 비용합 일정 가격 이상 -> 플러스 가입
# 경우의수 -> 이모티콘수 ** 4