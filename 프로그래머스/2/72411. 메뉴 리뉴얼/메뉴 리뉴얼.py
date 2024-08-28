from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for n in course:
        poss = []
        for menu in orders:
            for m in combinations(menu, n):
                res = ''.join(sorted(m))
                poss.append(res)
        sorted_poss = Counter(poss).most_common()
        print("turn", sorted_poss)

        for menu, cnt in sorted_poss:
            if cnt > 1 and cnt == sorted_poss[0][1]:
                answer.append(menu)

    return sorted(answer)