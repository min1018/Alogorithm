import math 

def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        temp = int(math.sqrt(d ** 2 - i**2)) // k + 1
        answer += temp
    return answer
