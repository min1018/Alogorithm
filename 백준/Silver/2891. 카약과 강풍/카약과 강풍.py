n, b, o = map(int, input().split(" "))
broke = set(map(int, input().split(" ")))
onemore = set(map(int, input().split(" ")))

# 손상됨, 하나더 -> 대여 불가, 그걸로 출전
intersection = broke & onemore
broke = list(broke - intersection)
onemore = list(onemore - intersection)

ans = 0
broke.sort()
for broken in broke:
  if broken - 1 in onemore:
    onemore.remove(broken-1)
  elif broken + 1 in onemore:
    onemore.remove(broken+1)
  else:
    ans += 1
print(ans)