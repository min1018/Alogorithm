def solution(plans):
    answer = []
    for i in range(len(plans)):
        work = plans[i]
        cur_time = int(work[1].split(":")[0]) * 60 + int(work[1].split(":")[1])
        plans[i] = [work[0], cur_time, int(work[2])]
    plans.sort(key = lambda x: x[1])    
    print(plans)
    return answer