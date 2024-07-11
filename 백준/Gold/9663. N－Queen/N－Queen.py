import sys
input = sys.stdin.readline

def adjacent(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x -i:
            return False
    return True

def dfs(x):
    global result 
    if x == n:
        result += 1
    else:
        for i in range(n):
            row[x] = i
            if adjacent(x):
                dfs(x+1)

n = int(input().strip())
row = [0] * n
result = 0
# print(row)
dfs(0)
print(result)