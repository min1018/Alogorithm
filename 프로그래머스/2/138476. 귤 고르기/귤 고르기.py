from collections import Counter 

def solution(k, tangerine):
    counter = list(Counter(tangerine).items())
    counter.sort(key = lambda x : -x[1])
    answer = 0
    
    while k > 0:
        k -= counter[answer][1]
        answer += 1
        
    return answer

# 서로 다른 종류의 수가 최소이게끔 