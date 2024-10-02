def solution(s):
    keep = s.split(" ")
    ans = []
    for k in range(len(keep)):
        word = list(keep[k])
        tmp = ''
        for i in range(0, len(word)):
            if i % 2 == 0:
                tmp += word[i].upper()
            else:
                tmp+= word[i].lower()
        ans.append(tmp)
    
    answer = " ".join(ans)
    return answer