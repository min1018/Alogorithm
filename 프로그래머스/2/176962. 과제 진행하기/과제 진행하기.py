

def solution(plans):
    # 시간 변환 
    for i in range(len(plans)):
        subject, time, take = plans[i]
        start = int(time.split(":")[0])*60 + int(time.split(":")[1])
        plans[i] = [subject, start, int(take)]
    plans.sort(key = lambda x : (x[1]))   
    
    stop = []
    answer = []
    for i in range(len(plans)):
        if i == len(plans)-1:
            answer.append(plans[i][0])
            break
            
        currsubject, currtime, currdur = plans[i]
        nxtsubject, nxttime, nxtdur = plans[i+1]
        
        if currtime + currdur <= nxttime:
            answer.append(currsubject) # 완료 
            
            lefttime = nxttime - (currtime + currdur)
            while lefttime != 0 and stop:
                tmpsubject, tmptime, tmpdur = stop.pop()
                if tmpdur <= lefttime: # 수행 끝내기 가능 
                    lefttime -= tmpdur
                    answer.append(tmpsubject)
                else: # 불가 다시 돌아가
                    tmpdur -= lefttime
                    lefttime = 0
                    stop.append([tmpsubject, tmptime, tmpdur])
        
        else:
            stop.append([currsubject, currtime, currdur - (nxttime-currtime)])
        
    while stop:
        sub, _, _ = stop.pop()
        answer.append(sub)
        
    return answer
# 새로운 과제 > 멈춘 과제, 진행중인 과제 