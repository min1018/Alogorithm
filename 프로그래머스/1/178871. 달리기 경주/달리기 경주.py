def solution(players, callings):
    dic = {}
    cnt = 0
    answer = []
    for p in players:
        dic[p] = cnt
        cnt += 1
     
    for c in callings:
        idx = dic[c]
        dic[c] -= 1
        dic[players[idx-1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]
    
    return players