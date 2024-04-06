from collections import Counter

def zeroPadd(new):
  maxLen = 0
  for i in range(len(new)):
    maxLen = max(maxLen, len(new[i]))
  for i, item in enumerate(new):
    new[i] = item+[0]*(maxLen - len(item))

def row():
  new = []
  for row in graph:
    counter = Counter(row)
    if 0 in counter:
      del counter[0]
    sorted_ = sorted(counter.items(), key = lambda x: (x[1], x[0]))
    ans = []
    for item, freq in sorted_:
      ans.append(item)
      ans.append(freq)
    new.append(ans)
  # 0채우기
  zeroPadd(new)
  return new

def col():
  new = []
  for c in range(len(graph[0])):
    column = [graph[r][c] for r in range(len(graph))]
    counter = Counter(column)
    if 0 in counter:
      del counter[0]
    sorted_ = sorted(counter.items(), key = lambda x: (x[1], x[0]))
    ans = []
    for item, freq in sorted_:
      ans.append(item)
      ans.append(freq)
    new.append(ans)
  # 0 채우기
  zeroPadd(new)
  real = [[0] * len(new) for _ in range(len(new[0]))]
  for i in range(len(new)):
    for k in range(len(new[0])):
      real[k][i]= new[i][k]
  return real


targetX, targetY, targetA = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(3)]

time = 0

while True:
  if len(graph) > targetX -1  and len(graph[0]) > targetY -1:
      if graph[targetX-1][targetY-1] == targetA:
        print(time)
        break
  if time == 100:
    print(-1)
    break
  time += 1
  if len(graph) >= len(graph[0]):
    graph = row()
  elif len(graph[0]) > len(graph):
    graph = col()


