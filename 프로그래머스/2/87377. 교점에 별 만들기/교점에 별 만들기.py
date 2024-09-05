from itertools import combinations 

def solution(line):
    dots = []
    answer = []
    min_x, min_y, max_x, max_y = int(1e15), int(1e15), int(-1e15), int(-1e15)
    

    temp = list(combinations(line, 2))
    for i in range(len(temp)):
        a, b, e = temp[i][0][0], temp[i][0][1], temp[i][0][2]
        c, d, f = temp[i][1][0], temp[i][1][1], temp[i][1][2]
        if a*d - b*c != 0:
            y = (b*f-e*d)/(a*d-b*c)
            x = (e*c-a*f)/(a*d-b*c)
            if x == int(x) and y == int(y):
                if x < min_x: min_x = int(x)
                if y < min_y: min_y = int(y)
                if x > max_x: max_x = int(x)
                if y > max_y: max_y = int(y)
                dots.append((int(x),int(y)))       

                
    xlen = max_x-min_x+1
    ylen = max_y-min_y+1
    result = [['.' for _ in range(ylen)] for _ in range(xlen)]
    # 왼쪽 위, 왼쪽 -> min_y 위 -> max_x
    for x, y in dots:
        result[max_x - x][y-min_y] = '*'
    for i in result:
        answer.append(''.join(i))
    return answer

# 조합 -> 교점 공식 적용 
# minx, miny 구해서 x-minx, y-miny 가 새로운 좌표 