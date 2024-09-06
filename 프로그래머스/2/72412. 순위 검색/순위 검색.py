from itertools import combinations 
from bisect import bisect_left 

def solution(info, query):
    answer = []
    dic = {}
    for i in info:
        i = i.split(' ')
        for j in range(5):
            combi = list(combinations(i, j))
            for com in combi:
                str_val = ''.join(list(com))
                if str_val in dic:
                    dic[str_val].append(int(i[4]))
                else:
                    dic[str_val] = [int(i[4])]
    for key in dic:
        dic[key].sort()
    
    for q in query:
        q = q.split(" and ")
        val = q[3].split(" ")
        q[3] = val[0]
        
        str_val = []
        for i in q:
            if i != '-':
                str_val.append(i)
        str_val = ''.join(str_val)
        
        if str_val in dic:
            result = dic[str_val]
            answer.append(len(result) - bisect_left(result, int(val[1])))
        else:
            answer.append(0)

    return answer 



