def solution(numbers):
    answer = []

    for num in numbers:
        binnum = list('0' + bin(num)[2:])
        idx = ''.join(binnum).rfind('0')
        binnum[idx] = '1'
        
        if num % 2 == 1:
            binnum[idx+1] = '0'
        
        answer.append(int(''.join(binnum), 2))
    
    return answer
# 원래 수에서 제일 왼쪽의 1 건들고 젤 오른쪽의 0 건들기 
# -> 현재수보다 큰 수임을 보장 가능하지 않음 
# 1씩 늘려가면서 
# ^ 연산 -> 이진수변환 -> count("1")