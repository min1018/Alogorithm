def solution(a, b, n):
    get = 0
    tmp = n
    while tmp > 0:
        tmp = int(n // a)*b
        left = n % a
        n = tmp + left
        get += tmp
    return get