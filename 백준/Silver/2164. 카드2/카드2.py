from collections import deque 

cnt = int(input())
q = deque([i for i in range(1, cnt+1)])

while len(q) != 1:
    q.popleft()
    tmp = q.popleft()
    q.append(tmp)
    
print(q.popleft())