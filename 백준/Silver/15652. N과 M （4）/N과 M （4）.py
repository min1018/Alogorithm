from itertools import combinations_with_replacement

n, m = map(int, input().split(" "))
tmp = list(i for i in range(1, 1+n))
ans = list(combinations_with_replacement(tmp, m))

for a in ans:
    print(*a)