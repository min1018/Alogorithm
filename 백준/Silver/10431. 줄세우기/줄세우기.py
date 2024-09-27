n = int(input())

for _ in range(n):
  kids = list(map(int, input().split(" ")))
  total = 0
  for i in range(1, len(kids) - 1):
    for k in range(i+1, len(kids)):
      if kids[i] > kids[k]:
        kids[i], kids[k] = kids[k], kids[i]
        total += 1

  print(kids[0], total)