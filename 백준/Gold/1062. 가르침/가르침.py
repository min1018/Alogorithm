n, k = map(int, input().split(" "))

if k < 5:
  print(0)
  exit()
elif k == 26:
  print(n)
  exit()

answer= 0 
words = [list(input()) for _ in range(n)]

learn = [0] * 26

for word in ['a', 'c', 'i', 'n', 't']:
  learn[ord(word) - ord('a')] = 1

def dfs(idx, cnt):
  global answer 
  if cnt == k-5:
    rcnt = 0
    for word in words:
      check = True
      for w in word:
        if not learn[ord(w) - ord('a')]:
          check = False
          break
      if check:
        rcnt += 1
    answer = max(answer, rcnt)
    return 
  for i in range(idx, 26):
    if not learn[i]:
      learn[i] = 1
      dfs(i, cnt+1)
      learn[i] = 0

dfs(0, 0)
print(answer)