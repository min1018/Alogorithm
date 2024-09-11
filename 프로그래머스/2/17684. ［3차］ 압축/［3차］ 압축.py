def solution(msg):
    dic = {}
    answer = []
    # 현재위치 + 1 -> 있으면 출력 / 없으면 추가, 본인 출력 
    for i in range(26):
        dic[chr(65+i)] = i+1
    
    curr, plus = 0, 0
    while True:
        plus += 1
        if plus == len(msg):
            answer.append(dic[msg[curr:plus]])
            break
        
        if msg[curr: plus+1] not in dic:
            dic[msg[curr:plus+1]] = len(dic) + 1
            answer.append(dic[msg[curr:plus]])
            curr = plus
        
    return answer