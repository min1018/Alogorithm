import sys 
input = sys.stdin.readline 
from collections import deque 

a, b, c = map(int, input().split(" "))

visited = set()

def sol(a, b, c):
  q = deque()
  q.append((a, b, c))

  while q:
    a, b, c = q.popleft()

    if a == b == c :
      return True
    if (a,b,c) not in visited:
      
      visited.add((a, b, c))
      # a, b
      if a < b:
        q.append((a+a, b-a, c))
      if b < a:
        q.append((a-b, b+b, c))
      
      # a, c
      if a < c:
        q.append((a+a, b, c-a))
      if c < a:
        q.append((a-c, b, c+c))
      
      # b, c
      if b < c:
        q.append((a, b+b, c-b))
      if c < b:
        q.append((a, b-c, c+c))  

  return False 

if sol(a, b, c) :
  print(1)
else:
  print(0)