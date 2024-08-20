import sys 
input = sys.stdin.readline

n = int(input())
nums = [[0] * n for _ in range(4)]
dict = {}
ans = 0

for i in range(n):
  row = list(map(int, input().split()))
  for j in range(4):
    nums[j][i] = row[j]

for i in range(n):
  for j in range(n):
    num = nums[0][i]+nums[1][j]
    if num in dict:
      dict[num] += 1
    else:
      dict[num] = 1

for i in range(n):
  for j in range(n):
    num = nums[2][i] + nums[3][j]
    if -num in dict.keys():
      ans += dict[-num]

print(ans)