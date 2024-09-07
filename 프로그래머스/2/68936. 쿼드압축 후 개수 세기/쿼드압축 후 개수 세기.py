

def solution(arr):
    global length
    length = len(arr)
    global answer 
    answer = [0, 0]
    for i in range(length):
        for k in range(length):
            if arr[i][k] == 0:
                answer[0] += 1
            elif arr[i][k] == 1:
                answer[1] += 1
                
    def dfs(depth):
        global answer
        global length
        if depth == 1:
            return 
        
        for i in range(0, length, depth): # 시작점, 사각형 왼쪽 위 
            for j in range(0, length, depth):
                standard = arr[i][j] 
                if standard == -1:
                    continue
                flag = 1
                for k in range(i, i+depth):
                    for h in range(j, j+depth):
                        if standard != arr[k][h]:
                            flag = 0
                            break
                    if flag == 0:
                        break
                if flag == 1:
                    for k in range(i, i+depth):
                        for h in range(j, j+depth):
                            arr[k][h] = -1
                    if standard == 0:
                        answer[0] -= (int(depth ** 2) -1)
                    elif standard == 1:
                        answer[1] -= (int(depth ** 2) -1)
        dfs(depth//2)
                     
    dfs(length)
        
    return answer

# 맨처음 0, 1 개수 세고 -> 사각형 변 길이 구해서 n 이라면 
# 처음 개수 - (n**2-1)
# 이미 합쳐진 애들은 -1로 변경해두기 