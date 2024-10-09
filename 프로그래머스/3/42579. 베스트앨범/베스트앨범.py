def solution(genres, plays):    
    dic = {}
    for i in range(len(plays)):
        if genres[i] in dic :
            dic[genres[i]].append([plays[i], i])
        else:
            dic[genres[i]] = [[plays[i], i]]
    
    order = []
    for i in dic.keys():
        dic[i].sort(key = lambda x : (-x[0], x[1]))
        tmp = 0
        for cnt, _ in dic[i]:
            tmp += cnt
        order.append([tmp, i])
    order.sort(key = lambda x : (-x[0]))       
    answer = []
    for cnt, genre in order:
        if len(dic[genre]) >= 2:
            answer.append(dic[genre][0][1])
            answer.append(dic[genre][1][1])
        else:
            answer.append(dic[genre][0][1])
    return answer