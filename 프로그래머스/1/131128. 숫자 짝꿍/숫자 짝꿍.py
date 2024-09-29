from collections import Counter

def solution(X, Y):
    xcnt = Counter(X)
    ycnt = Counter(Y)
    
    tmp = []
    for xnum in xcnt:
        if xnum in ycnt:
            tmp.extend([xnum] * min(xcnt[xnum], ycnt[xnum]))
    
    tmp.sort(reverse=True)
    
    if len(tmp) == 0:
        answer = '-1'
    elif tmp[0] == '0':
        answer = '0'
    else:
        answer = ''.join(tmp)
    
    return answer