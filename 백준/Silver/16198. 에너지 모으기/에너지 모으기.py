# 모든 경우를 다 찾아야함 -> 효율적으로 dfs 
# depth == n-2 

# 리스트 사이의 숫자가 빠지고 이런거 어떻게 표현하지?
# 1. visited 로 방문하지 않은거 구하기 
# 2. 리스트에 직접 제거하기 

def dfs(total):
  global ans
  if len(nums) == 2:
    if ans < total:
      ans = total
      return 
  for i in range(1, len(nums)-1):
    temp = nums[i]
    del nums[i]
    dfs(total + nums[i-1] * nums[i])
    nums.insert(i, temp)
  
    


ans = -1
n = int(input())
nums = list(map(int, input().split(" ")))

dfs(0)
print(ans)