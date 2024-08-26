def solution(picks, minerals):
    if len(minerals) > sum(picks) * 5 :
        minerals = minerals[:sum(picks)*5]
        
    check = [[0, 0, 0] for _ in range(len(minerals)//5 + 1)]
    for m in range(len(minerals)):
        if minerals[m] == 'diamond':
            check[m//5][0] += 1
        elif minerals[m] == 'iron':
            check[m//5][1] += 1
        elif minerals[m] == 'stone':
            check[m//5][2] += 1
    check.sort(key = lambda x: (x[0], x[1], x[2]), reverse = True)

    answer = 0
    for i in check:
        dia, iron, stone = i
        for k in range(len(picks)):
            if picks[k] > 0 and k == 0:
                picks[k] -= 1
                answer += dia + iron + stone
                break
            elif picks[k] > 0 and k == 1:
                picks[k] -= 1
                answer += dia * 5 + iron + stone 
                break
            elif picks[k] > 0 and k == 2:
                picks[k] -= 1
                answer += dia * 25 + iron * 5 + stone 
                break
                
    return answer

# 다이아 철 돌 - 피로도 
# 5개씩 캐기 가능 
# 좋은 곡괭이 바로바로 쓸 수 있으면 쓰는게
