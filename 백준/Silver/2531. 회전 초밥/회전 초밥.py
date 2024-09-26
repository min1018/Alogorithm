from collections import defaultdict

total, case, k, coupon = map(int, input().split(" "))
list = [int(input()) for _ in range(total)]

list = list + list[:k]
ans = 0
check = defaultdict(int)
check[coupon] = 1

for i in range(k):
    check[list[i]] += 1
    
left, right = 0, k   
for i in range(total):
    ans = max(ans, len(check))
    check[list[left]] -= 1
    check[list[right]] += 1
    if check[list[left]] == 0:
        del check[list[left]]
    right += 1
    left += 1
    
print(ans)
