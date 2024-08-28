def solution(cards):
    visited = [0 for _ in range(len(cards))]
    group = []
    
    for i in range(len(cards)):
        cnt = 0
        while visited[i] == 0:
            visited[i] = 1
            i = cards[i] - 1
            cnt += 1
        group.append(cnt)
            
    group.sort(reverse = True)
    return group[0] * group[1]

# 그룹이 몇갠지 파악 -> 그룹 속 카드 많은 두개 택 
# 싸이클 여부 