answer = 0

def dfs(depth, i, total, numbers, target):
    if depth == len(numbers):
        if total == target:
            global answer
            answer += 1
        return 
    dfs(depth+1, i+1, total + numbers[i+1], numbers, target)
    dfs(depth+1, i+1, total - numbers[i+1], numbers, target)
    
def solution(numbers, target):
    global answer
    dfs(1, 0, numbers[0], numbers, target)
    dfs(1, 0, -numbers[0], numbers, target)
    
    return answer