def solution(land):
    for n in range(1, len(land)):
        land[n][0] += max(land[n-1][1],land[n-1][2],land[n-1][3])
        land[n][1] += max(land[n-1][0],land[n-1][2],land[n-1][3])
        land[n][2] += max(land[n-1][0],land[n-1][1],land[n-1][3])
        land[n][3] += max(land[n-1][0],land[n-1][1],land[n-1][2])
    return max(land[-1])