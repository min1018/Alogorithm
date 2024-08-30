from collections import Counter 

def solution(want, number, discount):
    dic = {}
    answer = 0
    for i in range(len(want)):
        dic[want[i]] = number[i]
    
    for i in range(len(discount) - 9):
        if dic == Counter(discount[i:i+10]):
            answer += 1
    
    return answer

# 매일 하나 할인, 하나씩 구매 