def solution(s):
    result = []
    
    if len(s) == 1:
        return 1 
    
    for i in range(1, len(s) + 1):
        keep = ''
        cnt = 1
        tmp = s[:i]
        
        for k in range(i, len(s)+i, i):
            if tmp == s[k:k+i]:
                cnt += 1
            else:
                if cnt != 1:
                    keep = keep + str(cnt) + tmp        
                else:
                    keep = keep + tmp
                tmp = s[k: k+i]
                cnt = 1
        result.append(len(keep))
                    
        

    return min(result)