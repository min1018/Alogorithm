from collections import deque 

def check(s):
    temp = []
    for c in s:
        if c == '(' or c == '[' or c == '{':
            temp.append(c)
        elif c == ')':
            if temp and temp[-1] == '(':
                del temp[-1]
            else:
                return 0
        elif c == ']':
            if temp and temp[-1] == '[':
                del temp[-1]
            else:
                return 0
        elif c == '}':
            if temp and temp[-1] == '{':
                del temp[-1]
            else:
                return 0
    if temp: return 0 # 예외
    return 1   
    
def solution(s):
    answer = 0
    s = list(s)
    for i in range(len(s)):
        s = deque(s)
        s.rotate()
        answer += check(s)
    return answer