n = int(input())

case = []
for _ in range(n):
    case.append(list(map(int, input().split(" "))))
case.sort(key = lambda x : x[0])

maxIndex, maxHeight = 0, 0
for i in range(n):
    index, height = case[i]
    if maxHeight < height:
        maxIndex, maxHeight = i, height

ans = 0
index, height = case[0]       
for i in range(maxIndex+1):
    currindex, currheight = case[i]
    if currheight >= height:
        ans += height * (currindex - index)
        index, height = currindex, currheight
    else: 
        continue

index, height = case[-1]     
for k in range(n-1, maxIndex -1, -1):
    currindex, currheight = case[k]
    if currheight >= height: 
        ans += height * (index - currindex)
        index, height = currindex, currheight
    else: 
        continue
print(ans+maxHeight)