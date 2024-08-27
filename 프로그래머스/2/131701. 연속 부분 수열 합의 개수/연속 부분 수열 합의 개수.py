from collections import deque
def solution(elements):
    answer = set()
    q = deque(elements)
    for i in range(len(q)):
        sum = 0
        for e in q:
            sum += e
            if not sum in answer: ## 조건문추가
            	answer.add(sum)   
        q.append(q.popleft())

    return len(answer)