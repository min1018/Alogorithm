n = int(input())

work = [list(map(int, input().split(" "))) for i in range(n)]
#걸리는 시간, 수입

best = [0 for _ in range(n+1)]

for i in range(n):
  for k in range(i+work[i][0], n+1):
    if best[k] < best[i] + work[i][1]:
      best[k] = best[i] + work[i][1]

print(best[-1])