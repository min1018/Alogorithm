import math 
from itertools import permutations

def solution(numbers):
    poss = []
    for i in range(1, len(numbers)+1):
        poss += list(permutations(numbers, i))
    answer = []
    for nxt in poss:
        num = int(('').join(nxt))
        if isPrime(num):
            answer.append(num)
    return len(set(answer))

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True