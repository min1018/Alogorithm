from collections import deque 
import sys 

nums = [False] * 2 + [True] * 99999
for i in range(2, int(100000 ** 0.5)+1):
    for k in range(i*2, 100001, i):
        nums[k] = False

while True:
    ans = 0
    n = input().rstrip()

    if n == '0':
        break
    for i in range(5, 0, -1):
        if len(n) > i and ans == 0:
            for k in range(0, len(n)-i):
                num = int(n[k:k+i])
                if nums[num]:
                    ans = max(num, ans)
        if ans != 0:
            break
    print(ans)
        
    
        