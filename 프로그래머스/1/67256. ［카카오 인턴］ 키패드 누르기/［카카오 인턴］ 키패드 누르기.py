def solution(numbers, hand):
    lx, ly = 3, 0
    rx, ry = 3, 2
    dic = {}
    num = 1
    ans = ''
    for i in range(3):
        for k in range(3):
            dic[num] = [i, k]
            num += 1
    dic[0] = [3, 1]
    
    for n in numbers:
        if n % 3 == 2 or n == 0:
            dl = abs(dic[n][0] - lx) + abs(dic[n][1] - ly)
            dr = abs(dic[n][0] - rx) + abs(dic[n][1] - ry)
            if dl < dr :
                lx, ly = dic[n][0], dic[n][1]
                ans += 'L'
            elif dr < dl:
                rx, ry = dic[n][0], dic[n][1]
                ans += 'R'
            else:
                if hand == "right":
                    rx, ry = dic[n][0], dic[n][1]
                    ans += 'R'
                else:
                    lx, ly = dic[n][0], dic[n][1]
                    ans += 'L'
            
        elif n % 3 == 1:
            lx, ly = dic[n][0], dic[n][1]
            ans += 'L'
            
        elif n % 3 == 0:
            rx, ry = dic[n][0], dic[n][1]
            ans += 'R'
    
    
    return ans