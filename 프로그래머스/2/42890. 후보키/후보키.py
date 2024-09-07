from itertools import combinations 

def solution(relation):
    answer = 0
    col = len(relation[0])
    com = []
    for i in range(1, col+1):
        com.extend(combinations(range(col), i))
    #print(com)
       
    unique = []
    for i in com:
        temp = []
        for item in relation:
            inner_list = []
            for key in i:
                inner_list.append(item[key])
            temp.append(tuple(inner_list))
        print(temp)
        if len(set(temp)) == len(relation):
            flag = True
            for x in unique:
                if set(x).issubset(set(i)):
                    flag = False
                    break
            if flag: unique.append(i)
                
    return len(unique)