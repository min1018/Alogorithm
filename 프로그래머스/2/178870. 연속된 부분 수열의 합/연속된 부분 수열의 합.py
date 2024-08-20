def solution(sequence, k):
    l = r = 0
    answer = [0, len(sequence)]
    curr = sequence[0]
    
    while True:
        if curr < k:
            r += 1
            if r == len(sequence):
                break
            curr += sequence[r]
        else: 
            if curr == k:
                if r-l < answer[1] - answer[0]:
                    answer = [l, r]
            curr -= sequence[l]
            l += 1
            
    return answer
