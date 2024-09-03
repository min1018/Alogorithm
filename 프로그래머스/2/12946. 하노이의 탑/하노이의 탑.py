def solution(n):
    answer = []
    
    def hanoi(start, target, mid, n):
        if n == 1:
            answer.append([start, target])
        else:
            hanoi(start, mid, target, n-1)
            hanoi(start, target, mid, 1)
            hanoi(mid, target, start, n-1)
    hanoi(1, 3, 2, n)
    return answer

# 출발 중간 도착 몇개의 원판 