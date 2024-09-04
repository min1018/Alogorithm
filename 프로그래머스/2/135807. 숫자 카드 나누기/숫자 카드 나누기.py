import math

def solution(arrayA, arrayB):
    answer = 0
    a, b = arrayA[0], arrayB[0]
    for i in range(len(arrayA)):
        a = math.gcd(a, arrayA[i])
        b = math.gcd(b, arrayB[i])
        
    f1 = 1
    f2 = 1
    for i in range(len(arrayA)):
        if arrayA[i] % b == 0:
            f1 = 0
        if arrayB[i] % a == 0:
            f2 = 0
    if f1 == 0 and f2 == 0:
        return 0
    else:
        return max(a, b)

# 공약수를 구해야함 
# 각자 팀의 공약수끼리 다시 공약수이면 안됨 