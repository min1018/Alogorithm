from heapq import heappop, heappush

def solution(n, k, enemy):
    answer, enimies = 0, 0
    heap = []
    
    for e in enemy:
        heappush(heap, -e)
        enimies += e
        if enimies > n:
            if k == 0: # 무적권 다씀 
                break
            enimies += heappop(heap)
            k -= 1
        answer += 1        
    return answer


# 하나하나 해보는게 맞긴한데, 적의 수가 누가 봐도 작은 데서는 무적권을 쓸 필요가 없음 
# 이때까지 중 가장 많은 값 혹은 가장 적은 값에 대한 접근이 필요 
