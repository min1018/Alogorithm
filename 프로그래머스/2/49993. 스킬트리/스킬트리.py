def solution(skill, skill_trees):
    answer = len(skill_trees)
    for code in skill_trees:
        idx = 0 
        flag = 0
        for word in code:
            if word in skill:
                check = skill.find(word) - idx 
                if check == 0:
                    flag = 1
                    continue
                elif check == 1 and flag != 0:
                    idx += 1
                else:
                    answer -= 1
                    break
                
            
    return answer