n = int(input())
nums = list(map(int, input().split(" ")))

poss = [0] * 21 
poss[nums[0]] = 1

for i in range(1, n-1):
  tmp = [0] * 21
  curr = nums[i]
  for k in range(0, 21):
    if poss[k] != 0: # k == 이전까지의 계산한 값 
      if 0 <= curr + k <= 20:
        tmp[curr+k] += poss[k]
      if 0 <= k-curr <= 20:
        tmp[k-curr] += poss[k]
  poss = tmp
  # print(curr, poss)


print(poss[nums[-1]])