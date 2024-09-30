sentence = list(input())

ans = []
keep = []
flag = 0
for i in sentence:
    if i == '<':
        ans.extend(keep[::-1])
        keep = []
        keep.append(i)
        flag = 1
    elif i == '>':
        keep.append(i)
        ans.extend(keep)
        keep = []
        flag = 0
    elif flag == 0 and i == ' ':
        keep = keep[::-1]
        keep.append(i)
        ans.extend(keep)
        keep = []
    else:
        keep.append(i)
    
ans.extend(keep[::-1])

print(''.join(ans))