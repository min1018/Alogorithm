def solution(k, m, score):
    answer = 0
    score.sort()
    
    while len(score) >= m:
        case = 10
        for _ in range(m):
            s = score.pop()
            case = min(case, s)
        answer += case * m
            
    return answer