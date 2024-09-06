def check(place):
    curr = []
    for i in range(5):
        for k in range(5):
            if place[i][k] == 'P':
                curr.append((i, k))
    
    for x, y in curr:
        for x2, y2 in curr:
            dist = abs(x-x2) + abs(y-y2)
            if dist == 0 or dist > 2:
                continue
            if dist == 1:
                return 0
            elif x == x2 and place[x][int((y+y2)//2)] != 'X':
                return 0
            elif y == y2 and place[int((x+x2)//2)][y] != 'X':
                return 0
            elif y != y2 and x != x2:
                if place[x][y2] != 'X' or place[x2][y] != 'X':
                    return 0
    return 1
                    
    
    
    
def solution(places):
    answer = []
    for place in places:
        answer.append(check(place))
    return answer