def divisor(n):
    dic = {}
    i = 2
    while i <= n:
        if n % i == 0:
            n = n / i
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        else:
            i += 1    
    return dic

def solution(arr):
    answer = 1
    temp = []
    ans = {}
    for num in arr:
        temp.append(divisor(num))
    for k in temp:
        for key, val in k.items():
            if key in ans:
                if ans.get(key) < val:
                    ans[key] = val
            else:
                ans[key] = val
    for key, val in ans.items():
        answer = answer * (key ** val)
    return answer

# 2 / 2 3 / 2 2 2 / 2 7 -> 2 2 2 3 7
# 약수를 구해서 딕셔너리 혹은 카운터 