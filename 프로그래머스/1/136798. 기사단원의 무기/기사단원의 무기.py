def get(num):
    ans = 0
    for i in range(1, int(num **(1/2))+1):
        if (num % i == 0):
            ans += 2
            if i ** 2 == num:
                ans -= 1
    return ans 

def solution(number, limit, power):
    keep = []
    for i in range(1, number+1):
        keep.append(get(i))

    for i in range(len(keep)):
        if keep[i] > limit:
            keep[i] = power
    return sum(keep)

# 약수 
# 제한수치 -> 협약기관 공격력 
