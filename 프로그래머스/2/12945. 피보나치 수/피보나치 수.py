def recur(nums, n):
    for i in range(2, n+1):
        nums.append((nums[i-1] + nums[i-2])%1234567)
    return nums[-1]

def solution(n):
    nums = []
    nums.append(0)
    nums.append(1)
    answer = recur(nums, n)
    
    return answer