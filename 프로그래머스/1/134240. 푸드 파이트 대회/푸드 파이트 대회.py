def solution(food):
    answer = '0'
    cnt = len(food) -1
    
    for i in range(len(food)-1, 0, -1):
        if food[i] % 2 == 1:
            food[i] = (food[i] -1)
        answer = str(cnt) * (food[i]//2) + answer + str(cnt) * (food[i]//2)
        cnt -= 1
    return answer

# 종류, 양 같아야 
# 칼로리 낮은 음식 먼저 