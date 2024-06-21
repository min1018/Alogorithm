from itertools import product

def solution(word):
    result = []
    for i in range(1,6):
        for w in product(['A', 'E', 'I', 'O', 'U'], repeat = i):
            result.append(''.join(list(w)))
            
    result.sort()
    return result.index(word) + 1