def solution(elements):
    length = len(elements)
    poss = set()

    for i in range(length):
        ssum = elements[i]
        poss.add(ssum)
        for k in range(i+1, i+length):
            ssum += elements[k%length]
            poss.add(ssum)
    return len(poss)