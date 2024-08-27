def solution(data, col, row_begin, row_end):
    data.sort(key = lambda x : (x[col-1], -x[0]))
    answer = 0
    for i in range(row_begin, row_end+1):
        temp = 0
        for num in data[i-1]:
            temp += (num % i)
        answer ^= temp
        
    return answer