import math

def solution(n, k):
    nums = [i for i in range(1, n+1)]
    answer = []
    
    while nums :
        a = (k-1) // math.factorial(n-1)
        answer.append(nums.pop(a))
        
        k = k % math.factorial(n-1)
        n -= 1
        
    return answer