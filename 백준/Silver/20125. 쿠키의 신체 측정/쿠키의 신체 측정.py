n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

def getHeart():
    centerX, centerY = 0, 0
    for i in range(n):
        for k in range(n):
            if board[i][k] == '*':
                centerX = i+1
                centerY = k
                return centerX, centerY
                

# 심장
centerX, centerY = getHeart()
print(centerX+1, centerY+1) # 4 1 


leftArm = 0
for k in range(centerY):
    if board[centerX][k] == '*':
        leftArm += 1
        
rightArm = 0
for k in range(centerY+1, n):
    if board[centerX][k] == '*':
        rightArm += 1

back = 0
for i in range(centerX+1, n):
    if board[i][centerY] == '*':
        back+= 1
    else:
        break

leftLeg = 0
for i in range(centerX+back+1,n):
    if board[i][centerY-1] == '*':
        leftLeg += 1
    else:
        break
    
rightLeg = 0
for i in range(centerX+back+1,n):
    if board[i][centerY+1] == '*':
        rightLeg += 1
    else:
        break
print(leftArm, rightArm, back, leftLeg, rightLeg)