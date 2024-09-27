import sys

n, m = map(int, sys.stdin.readline().split(" "))
dic = {}
for _ in range(n):
    dic[input().strip()] = 1
    
answer = n

for _ in range(m):
    temp = list(sys.stdin.readline().rstrip().split(","))
    for word in temp:
        if word in dic:
            if dic[word] == 1:
                answer -= 1
            dic[word] -= 1
    print(answer)            
