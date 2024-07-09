def solution(n):
    answer = [0, 3, 11]
    if int(n/2) < 3:
        return answer[int(n/2)]
    
    for i in range(3, int(n/2)+1):
        answer.append((3*answer[i-1] + sum(answer[:i-1]) * 2 + 2) % 1000000007)
    return answer[int(n/2)]
    
