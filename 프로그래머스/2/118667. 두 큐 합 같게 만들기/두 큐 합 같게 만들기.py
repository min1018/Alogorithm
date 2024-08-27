from collections import deque 

def bfs(q1, q2):
    sum1, sum2 = sum(q1), sum(q2)
    q1 = deque(q1)
    q2 = deque(q2)
    cnt = 0
    #visited = [0] * (sum1+sum2+1)
    while q1 and q2 and cnt <= 300000:
        if sum1 == sum2 :
            return cnt 
        elif sum1 < sum2:
            num = q2.popleft()
            sum2 -= num
            sum1 += num
            q1.append(num)
            #visited[sum1] = 1
        elif sum1 > sum2:
            num = q1.popleft()
            sum1 -= num
            sum2 += num
            q2.append(num)
            #visited[sum1] = 1
        cnt += 1    
    return -1 


def solution(queue1, queue2):
    return bfs(queue1, queue2)

# 큐의 형태를 유지하며 이동하되 최소 이동 회수를 찾아야함 