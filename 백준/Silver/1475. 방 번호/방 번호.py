import math

nums = list(map(int, list(input())))

dic = {}
for i in nums:
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1

keep = list(dic.values())
ans = max(keep)

if (6 in dic and dic[6] == ans) or (9 in dic and dic[9]) == ans:
    tmp = dic.get(6,0) + dic.get(9,0)
    dic[6] = math.ceil(tmp/2)
    dic[9] = math.ceil(tmp/2)
    ans = max(list(dic.values()))

print(ans)
# dic.values -> 뽑아내서 
# max 씌움 
# 만약 걔가 6이나 9라면 6개수 + 9개수 나누기 2로 변경해서 다시 max 구하기
