from collections import defaultdict

def solution(n, lost, reserve):
    keep = []
    new_lost=list(lost)
    for l in new_lost:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)

    r = defaultdict(int)
    
    for tmp in reserve:
        r[tmp] += 1
    
    sad = len(lost)
    lost.sort()
    for l in lost:
        if r[l-1] > 0:
            sad -= 1
            r[l-1] -= 1
        elif r[l+1] > 0:
            sad -= 1
            r[l+1] -= 1
            
    return n-sad