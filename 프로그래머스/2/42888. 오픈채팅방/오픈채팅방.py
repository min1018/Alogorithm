def solution(record):
    answer = []

    dic = {}
    for str in record:
        temp = str.split(" ")
        if temp[0] == 'Enter' or temp[0] == 'Change':
            dic[temp[1]] = temp[2]
        
    for str in record:
        temp = str.split(" ")
        if temp[0] == 'Enter':
            answer.append(dic.get(temp[1])+"님이 들어왔습니다.")
        elif temp[0] == 'Leave':
            answer.append(dic.get(temp[1])+"님이 나갔습니다.")         
    return answer

# userid 가 제공됨 -> 딕셔너리로 구분 