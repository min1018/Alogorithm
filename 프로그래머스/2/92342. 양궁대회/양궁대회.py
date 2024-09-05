def solution(n, info):
    global max_gap, answer
    answer = [-1]
    score = [0] * 11
    max_gap = 0
    
    def get_winner(score):
        ryan = 0
        peach = 0
        #for i in range(11):
        for i in range(len(info)):
            if info[i] > 0 or score[i] > 0:
                if info[i] >= score[i]:
                    peach += (10-i)
                else:
                    ryan += (10-i)
        return (ryan > peach, abs(ryan - peach))
    
    def dfs(depth, left):
        global max_gap, answer
        if depth == 11 or left == 0:
            win, gap = get_winner(score)
            if win:
                if left >= 0:
                    score[10] = left
                if gap > max_gap:
                    answer = score.copy()
                    max_gap = gap
                elif gap == max_gap:
                    t1 = 0
                    t2 = 0
                    #for i in range(11):
                    for i in range(len(score)):
                        if answer[i] != 0:
                            t1 = i
                        if score[i] != 0:
                            t2 = i
                    if t1 < t2:
                        answer = score.copy()
            return 
        
        if left > info[depth]:
            score[depth] = info[depth]+1
            dfs(depth+1, left-info[depth]-1)
            score[depth] = 0
        dfs(depth+1, left)
    
        
    dfs(0, n)       
    return answer


            