
n = int(input())

for _ in range(n):
    stack = []
    word = list(input().rstrip())
    flag = 0
    for w in word:
        if w == ')':
            if stack and stack[-1]== '(':
                stack.pop()
            else:
                print("NO")
                flag = 1
                break
        else:
            stack.append("(")
    if flag == 0:
        if len(stack) > 0:
            print("NO")
        else:
            print("YES")
            