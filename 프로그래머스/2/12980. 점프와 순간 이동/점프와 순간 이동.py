def solution(n):
    ans = 0
    while n > 0:
        if n % 2 == 0:
            n = n //2
        else:
            n -= 1
            ans += 1
    return ans


# 가능한 경우의 수는 n-1 에서 n 혹은 n/2 에서 n

