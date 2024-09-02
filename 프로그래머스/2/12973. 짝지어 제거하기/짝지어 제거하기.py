def solution(s):
    stack = []
    
    for word in s:
        if stack:
            if stack[-1] == word:
                stack.pop()
            else:
                stack.append(word)
        else:
            stack.append(word)
    
    if stack:
        return 0
    else:
        return 1