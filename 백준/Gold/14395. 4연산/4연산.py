import sys 
input = sys.stdin.readline
from collections import deque 


def sol(start, target):
  q = deque()
  visited = set()

  q.append((start, ''))

  while q:
    cur, calc = q.popleft()
    #print(cur, calc)
    if cur == target:
      return calc
      
    if cur in visited:
      continue 
    visited.add(cur)

    # * 
    if cur*cur <= target:
      q.append((cur*cur, calc+'*'))
    # + 
    if cur+cur <= target:
      q.append((cur+cur, calc+'+'))
    # -
    q.append((cur-cur, calc+'-'))
    # /
    if cur != 0 and cur//cur <= target:
      q.append((cur//cur, calc+'/'))
    
  return -1

start, target = map(int, input().split(" "))

if start == target:
  print(0)
  exit()


print(sol(start, target))

