import sys
input = sys.stdin.readline 

n, start, maxvol = map(int, input().split(" "))
volume = list(map(int, input().split(" ")))

poss = []
poss.append(start)

def nxt_volume(i, poss):
  tmp = set()
  for num in poss:
    if num + volume[i] <= maxvol:
      tmp.add(num + volume[i])
    if num - volume[i] >= 0:
      tmp.add(num - volume[i])
  return list(tmp)
  

for i in range(n):
  poss = nxt_volume(i, poss)

if not poss:
  print(-1)
else:
  print(max(poss))