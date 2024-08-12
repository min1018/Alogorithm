n = int(input())
nums = list(map(int, input().split(" ")))
poss = [0] * n

if n == 1:
  print(0)
  exit()
if nums[0] != 0:
  for k in range(1, nums[0]+1):
    poss[k] = 1
    if k == n-1:
      print(1)
      exit()

  

for i in range(1, n):
  if poss[i] != 0 : #현재 위치에 도달할 수 있는 경우 
    for k in range(1, nums[i]+1): #그 위치에서 이동할 수 있는 칸만큼 
      if i+k < n:
        if poss[i+k] != 0:
          if poss[i]+1 < poss[i+k]:
            poss[i+k] = poss[i] + 1 # 점프 횟수 +1 기록 
        else :
          poss[i+k] = poss[i] + 1
      if i + k == n-1:
        print(poss[i]+1)
        exit()

if poss[n-1] == 0:
  print(-1)
