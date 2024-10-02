def solution(k, score):
    answer = []
    win = []
    
    for s in score:
        win.append(s)
        if len(win) > k:
            win.remove(min(win))
        answer.append(min(win))
        
            
    
    return answer