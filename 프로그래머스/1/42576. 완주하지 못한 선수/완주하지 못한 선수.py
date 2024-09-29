from collections import Counter

def solution(participant, completion):
    countp = Counter(participant)
    countc = Counter(completion)
    
    # print(dir(Counter([])))
    
    return list((countp-countc).keys())[0]

  
