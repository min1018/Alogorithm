import math 

def solution(n,a,b):
    answer = 0
    
    while True:
        na, nb = math.ceil(a/2), math.ceil(b/2)
        #print(na, nb)
        answer += 1
        if na == nb :
            return answer
        a, b = na, nb
