def solution(n):
    word = ["1", "2", "4"]
    ans = ""
    
    while n >0:
        n -= 1
        ans = word[n%3] + ans
        n //= 3
    
    return ans