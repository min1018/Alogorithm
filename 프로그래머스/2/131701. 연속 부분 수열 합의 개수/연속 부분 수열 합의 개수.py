def solution(elements):
    poss = set()
    n = len(elements)
    elements += elements
    print(elements)
    for i in range(n):
        for k in range(n):
            poss.add(sum(elements[k: k+i]))
    return len(poss)
        