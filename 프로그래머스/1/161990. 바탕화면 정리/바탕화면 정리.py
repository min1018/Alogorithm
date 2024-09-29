import sys

def solution(wallpaper):
    answer = []
    minX, minY = sys.maxsize, sys.maxsize
    maxX, maxY = -1, -1
    for i in range(len(wallpaper)):
        for k in range(len(wallpaper[0])):
            if wallpaper[i][k] == '#':
                minX = min(i, minX)
                minY = min(k, minY)
                maxX = max(i+1, maxX)
                maxY = max(k+1, maxY)
    answer = [minX, minY, maxX, maxY]
    return answer