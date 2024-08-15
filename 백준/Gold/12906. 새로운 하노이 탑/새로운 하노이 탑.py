from collections import deque 

visited = set()
q = deque()

a = input().split()
t1 = a[-1] if len(a) > 1 else ""
a = input().split()
t2 = a[-1] if len(a) > 1 else ""
a = input().split()
t3 = a[-1] if len(a) > 1 else ""

q.append((t1, t2, t3, 0))

while q:
  a, b, c, cnt = q.popleft()
  str = a+'/'+b+'/'+c

  if a == 'A'*len(a) and b =='B'*len(b) and c =='C'*len(c):
    print(cnt)
    break

  if str not in visited:
    visited.add(str)

    if len(a)>0:
      q.append((a[:-1], b+a[-1], c, cnt + 1))
      q.append((a[:-1], b, c+a[-1], cnt + 1))

    if len(b)>0:
      q.append((a, b[:-1], c+b[-1], cnt + 1))
      q.append((a+b[-1], b[:-1], c, cnt + 1))

    if len(c)>0:
      q.append((a, b+c[-1], c[:-1], cnt + 1))
      q.append((a+c[-1], b, c[:-1], cnt + 1))