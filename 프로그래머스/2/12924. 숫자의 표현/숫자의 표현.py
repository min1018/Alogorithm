def solution(n):
    answer = 0
    for i in range(1, n+1):
        total = 0
        for k in range(i, n+1):
            total += k
            if total == n:
                answer += 1
            elif total > n:
                break 
    return answer
    
# 연속하는 k(홀수)개 : kn -> 약수 개수 - 1 
# 연속하는 k(짝수)개 : k(2n - 1) -> 홀수와의 곱으로 표현되면 됨 -> 약수 중 홀수의 개수 