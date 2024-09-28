n, which = map(int, input().split(" "))

case = []
for _ in range(n):
    temp = list(map(int, input().split(" ")))
    if temp[0] == which:
        sg, ss, sb = temp[1], temp[2], temp[3]
    case.append([temp[1], temp[2], temp[3]])
    
case.sort(key = lambda x:(-x[0], -x[1], -x[2]))

print(case.index([sg, ss, sb]) + 1)