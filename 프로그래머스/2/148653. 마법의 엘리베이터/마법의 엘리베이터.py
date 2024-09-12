def solution(storey):
    sta = 10
    answer = 0
    while storey:
        storey, temp = divmod(storey, sta)
        #print(sta, storey, temp)
        if temp > 5:
            answer += (10-temp)
            storey += 1
        elif temp == 5:
            if storey % 10 >= 5:
                answer += (10-temp)
                storey += 1
            else:
                answer+=temp
        else:
            answer += temp
        

    return answer

# 0층 아래로는 움직이지 않음 
# 돌을 최소한으로 아껴서 이동 