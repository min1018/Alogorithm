from itertools import combinations

n = int(input())
nums = list(map(int, input().split(" ")))
poss = []
# 모든 경우의 수를 리스트에 추가하고 정렬해서 찾아낸다 
for i in range(1, n+1):
  temp = list(map(sum, combinations(nums, i)))
  poss += temp
poss.sort()
poss = list(set(poss))
standard = [i for i in range(1, len(poss)+3)] # 중간에 하나 빈경우, 마지막 하나 추가 
answer = sorted(list(set(standard) - set(poss)))
print(answer[0])

