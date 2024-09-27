import sys

n, m = map(int, sys.stdin.readline().split(" "))
nums = []
for _ in range(n):
    nums.append(sys.stdin.readline().rstrip())
    
nums = set(nums)

for _ in range(m):
    temp = set(list(sys.stdin.readline().rstrip().split(",")))
    nums -= temp
    
    print(len(nums))            
