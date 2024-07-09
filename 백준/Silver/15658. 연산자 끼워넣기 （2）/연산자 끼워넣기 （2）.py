n = int(input())
nums = list(map(int, input().split(" ")))
plus, minus, mult, div = map(int, input().split(" "))

maxnum = -1e9
minnum = 1e9

def dfs(cnt, total, plus, minus, mult, div):
  global maxnum, minnum
  if cnt == n-1:
    maxnum = max(maxnum, total)
    minnum = min(minnum, total)
    return 
  if plus:
    dfs(cnt+1, total + nums[cnt+1], plus-1, minus, mult, div)
  if minus:
    dfs(cnt+1, total-nums[cnt+1], plus, minus-1, mult, div)
  if mult: 
    dfs(cnt+1, total*nums[cnt+1], plus, minus, mult-1, div)
  if div: 
    dfs(cnt+1, int(total/nums[cnt+1]), plus, minus, mult, div-1)

#연산기호가 몇개 남았는지 어떻게 기록하고 다니지?
dfs(0, nums[0], plus, minus, mult, div)

print(maxnum)
print(minnum)