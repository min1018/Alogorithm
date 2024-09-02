def solution(arr1, arr2):
    answer = []
    A = len(arr1)
    B = len(arr2[0])
    C = len(arr2)
    
    for i in range(A):
        temp = []
        for k in range(B):
            num = 0
            for h in range(C):
                num += (arr1[i][h] * arr2[h][k])
            temp.append(num)
        answer.append(temp)
    
    #print(answer)
    return answer