n = int(input())
balls = input()

cnt = []

temp = balls.rstrip('R')
cnt.append(temp.count("R"))

temp = balls.rstrip('B')
cnt.append(temp.count("B"))

temp = balls.lstrip('R')
cnt.append(temp.count("R"))

temp = balls.lstrip('B')
cnt.append(temp.count("B"))

print(min(cnt))