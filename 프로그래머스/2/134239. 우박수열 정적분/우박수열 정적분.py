def getnum(k):
    ans = []
    while k != 1:
        ans.append(k)
        if k % 2 == 0:
            k /= 2
        elif k % 2 == 1:
            k = k * 3 + 1
    ans.append(k)
    return ans

def solution(k, ranges):
    answer = []
    nums = getnum(k)
    
    for start, end in ranges:
        total = 0
        if start >= end + len(nums):
            answer.append(-1)
            continue
        temp = nums[start: len(nums)+end]
        for i in range(len(temp) - 1):
            total += (temp[i]+temp[i+1])/2
        answer.append(total)
    
    return answer

# a b b c c d d e e f * 1/2 *1