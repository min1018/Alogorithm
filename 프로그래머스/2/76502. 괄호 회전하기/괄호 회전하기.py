from collections import deque 

def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        s.rotate(-1)
        if check(s) == 1:
            answer += 1

    return answer

def check(s):
    left = ['(', '[', '{']
    keep = deque()
    
    for i in s:
        if i in left:
            keep.append(i)
        else:
            if keep:
                val = keep.pop()
                if i == ')' and val != '(':
                    return 0
                elif i == '}' and val != '{':
                    return 0
                elif i == ']' and val != '[':
                    return 
            else:
                return 0
    if len(keep) != 0:
        return 0
    return 1
                    