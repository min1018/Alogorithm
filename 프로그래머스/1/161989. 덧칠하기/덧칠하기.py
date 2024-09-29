def solution(n, m, section):
    answer = 0
    visited = [1] * (n+1)
    # 안 칠해진 애들 표기 
    for i in section:
        visited[i] = 0
    for curr in section:
        if visited[curr] == 0:
            for k in range(curr, curr+m):
                if k <= n and visited[k] == 0:
                    visited[k] = 1
            answer += 1
        
    return answer

# section + m 