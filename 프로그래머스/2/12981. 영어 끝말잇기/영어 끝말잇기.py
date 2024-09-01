def solution(n, words):
    answer = []
    turn = 1
    before = words[0]
    
    for i in range(1, len(words)):
        if i % n == 0:
            turn += 1
        if before[-1] == words[i][0] and len(words[i]) > 1 and len(set(words[:i+1])) == i+1:
            before = words[i]
            continue
        answer.append(i%n+1)
        answer.append(turn)
        break
    
    if not answer:
        answer.append(0)
        answer.append(0)
    return answer