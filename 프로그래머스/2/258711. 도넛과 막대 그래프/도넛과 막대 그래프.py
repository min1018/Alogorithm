def solution(edges):

    dic = {} # [들어옴, 나감]
    for start, end in edges:
        if start in dic:
            dic[start][1] += 1
        else: 
            dic[start] = [0, 1]
        if end in dic: 
            dic[end][0] += 1
        else:
            dic[end] = [1, 0]
    new, donut, stick, eight = 0, 0, 0, 0 

    for key, val in dic.items():
        if val[0] >= 2 and val[1] == 2:
            eight += 1
        elif val[0] >= 1 and val[1] == 0:
            stick += 1
        elif val[0] == 0 and val[1] >= 2:
            new = key 
            donut = val[1]
    # print(new, donut, stick, eight) 
    answer = [new, donut - eight - stick, stick, eight]
        
    return answer

# 막대 그래프 -> 나가는거 0, 들어오는거 1 
# 8자 그래프 -> 나가는거 2, 들어오는거 2 
# 정점 -> 1 
# 도넛 -> 정점에서 뻗어나가는 간선 수 - 8자 - 막대 