def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key = len)
    
    for nums in s:
        #print(nums)
        numss = nums.split(",")
        for n in numss:
            if int(n) not in answer:
                answer.append(int(n))
    
    return answer

# 길이 순으로 소팅해서 없는 값만 가지고 오기 