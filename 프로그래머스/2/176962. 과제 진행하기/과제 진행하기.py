
def solution(plans):
    answer = []
    for i in range(len(plans)):
        work = plans[i]
        cur_time = int(work[1].split(":")[0]) * 60 + int(work[1].split(":")[1])
        plans[i] = [work[0], cur_time, int(work[2])]
    plans.sort(key = lambda x: x[1])  
    
    left = []
    
    for i in range(len(plans)):
        if i == len(plans) - 1:
            left.append(plans[i])
            break
        name, time, duration = plans[i]
        nxtname, nxttime, nxtduration = plans[i+1]
        
        if time + duration <= nxttime:
            answer.append(name)
            lefttime = nxttime - (time+duration)
            
            while lefttime != 0 and left:
                tempname, temptime, tempduration = left.pop()
                if lefttime >= tempduration:
                    answer.append(tempname)
                    lefttime = lefttime - tempduration
                else:
                    left.append([tempname, temptime, tempduration - lefttime])
                    lefttime = 0
                
        else:
            left.append([name, time, duration - (nxttime-time)])
    
    while left:
        name, time, duration = left.pop()
        answer.append(name)
    return answer